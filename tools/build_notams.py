#!/usr/bin/env python3
"""Fetch current Philippine NOTAMs from the CAAP AIS API and bake them into a
static JSON the NOTAMs page reads. The CAAP API sits behind Imperva and sends
no CORS header, so the browser cannot fetch it directly — this runs at build
time instead.

Airport coordinates come from the OurAirports open dataset (also build time),
and are embedded in the output so the page needs nothing external at runtime.

Output: docs/assets/data/notams.json
  { generated, total, airports:{ICAO:[lat,lon,name]}, notams:[ {...} ] }

Re-run to refresh:  venv/bin/python tools/build_notams.py
"""
import csv, io, json, os, re, subprocess, sys
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone

SERIES = {"B": "bravo", "C": "charlie"}
MODAL = "https://ais.caap.gov.ph/notam-admin/notam/{ser}/{id}/modal"

API = ("https://ais.caap.gov.ph/notam-admin/api/notams-lazy"
       "?page=1&per_page=5000&series=all&validity_type=all")
AIRPORTS_CSV = "https://davidmegginson.github.io/ourairports-data/airports.csv"
OUT = os.path.join(os.path.dirname(__file__), "..", "docs", "assets", "data", "notams.json")


def curl(url, origin=None):
    cmd = ["curl", "-sS", "--max-time", "60", url]
    if origin:
        cmd += ["-H", "Origin: " + origin]
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        raise RuntimeError("curl failed for %s: %s" % (url, r.stderr[:200]))
    return r.stdout


def iso(dtstr):
    """'2026-10-02 04:00:00' (UTC) -> '2026-10-02T04:00:00Z'. None -> None."""
    if not dtstr or dtstr in ("NULL", "0000-00-00 00:00:00"):
        return None
    return dtstr.strip().replace(" ", "T") + "Z"


# lat = DD MM [SS[.ss]] N/S , lon = DDD MM [SS[.ss]] E/W , small gap between them.
_COORD = re.compile(
    r"(\d{2})(\d{2})(\d{2}(?:\.\d+)?)?\s*([NS])[\s\-–]{0,3}(\d{3})(\d{2})(\d{2}(?:\.\d+)?)?\s*([EW])")
_AREA_KW = ("BOUNDED BY", "WITHIN:", "WI:", "AREA BOUND", "AREA:",
            "TAKE PLACE WI", "FALL AREA", "ACT WI", "OPS WI", "CONDUCTED WI")


def _deg(d, m, s, hemi):
    v = int(d) + int(m) / 60.0 + (float(s) if s else 0.0) / 3600.0
    return round(-v if hemi in "SW" else v, 5)


def parse_geo(text):
    """Pull a drawable shape out of the NOTAM free text, or return None.
    Types: poly (area), circ (centre + radius NM), line (2 pts), pts (markers)."""
    pts = []
    for m in _COORD.finditer(text):
        lat = _deg(m.group(1), m.group(2), m.group(3), m.group(4))
        lon = _deg(m.group(5), m.group(6), m.group(7), m.group(8))
        if 3 < lat < 23 and 114 < lon < 134:          # sanity: in/near RPHI
            pts.append([lat, lon])
    if not pts:
        return None
    U = text.upper()
    uniq = []
    for p in pts:
        if not uniq or uniq[-1] != p:
            uniq.append(p)
    closed = len(uniq) >= 4 and uniq[0] == uniq[-1]
    ring = uniq[:-1] if closed else uniq
    area_kw = any(k in U for k in _AREA_KW)

    if (area_kw or closed) and len(ring) >= 3:
        return {"t": "poly", "c": ring}
    rad = None
    if any(k in U for k in ("RADIUS", "CENTERED", "CENTRED", "CIRCLE", "NM OF", "WI ")):
        rm = re.search(r"(\d+(?:\.\d+)?)\s*NM", U)
        if rm:
            rad = float(rm.group(1))
    if rad and rad <= 400 and uniq:
        return {"t": "circ", "c": [uniq[0]], "r": rad}
    if len(uniq) == 2:
        return {"t": "line", "c": uniq}
    return {"t": "pts", "c": uniq}


def parse_alt(text):
    """Best-effort vertical extent, only where the text states it clearly.
    Returns {"txt": "...", "ft": <top in feet or None>} or None.
    NOTE: the CAAP API exposes no lower/upper limits, and airspace NOTAMs here
    state none, so in practice this is obstacle heights (HGT ... FT) plus the
    rare explicit FL / FT AMSL mention. 'LOWER' in the data means aircraft
    category (e.g. B737-800 AND LOWER), not altitude, so it is ignored."""
    U = text.upper()
    m = re.search(r"HGT[^.\n]{0,30}?(\d{1,5})\s*FT", U)
    if m:
        ft = int(m.group(1))
        return {"txt": str(ft) + " ft (obst)", "ft": ft}
    m = re.search(r"\b(\d{3,5})\s*FT\s*(AMSL|AGL|MSL)\b", U)
    if m:
        ft = int(m.group(1))
        return {"txt": m.group(1) + " ft " + m.group(2), "ft": ft}
    m = re.search(r"\bFL\s?(\d{2,3})\b", U)
    if m:
        return {"txt": "FL" + m.group(1), "ft": int(m.group(1)) * 100}
    return None


def fetch_modal(series, nid):
    """The list API drops the Q-line limits, the D) schedule and F)/G) items.
    The per-NOTAM modal returns the full ICAO NOTAM, so we scrape it for those.
    Returns a dict {low,high,sched,fitem,gitem} or {} on failure."""
    ser = SERIES.get(series, str(series).lower())
    url = MODAL.format(ser=ser, id=nid)
    for _ in range(2):
        r = subprocess.run(["curl", "-s", "--max-time", "25", url,
                            "-H", "X-Requested-With: XMLHttpRequest"],
                           capture_output=True, text=True)
        if r.returncode == 0 and len(r.stdout) > 500:
            return parse_modal(r.stdout)
    return {}


def parse_modal(html):
    t = re.sub(r"<script.*?</script>", " ", html, flags=re.S)
    t = re.sub(r"<style.*?</style>", " ", t, flags=re.S)
    t = re.sub(r"<[^>]+>", " ", t).replace("&nbsp;", " ").replace("&amp;", "&")
    lines, started = [], False
    for l in t.splitlines():
        l = re.sub(r"[ \t]+", " ", l).strip()
        if re.match(r"Q\)", l):
            started = True
        if started and l:
            lines.append(l)
    raw = "\n".join(lines)
    out = {}
    m = re.search(r"Q\)\s*([^\n]+)", raw)
    if m:
        parts = m.group(1).split("/")
        if len(parts) >= 8:
            try:
                out["low"] = int(parts[5])
                out["high"] = int(parts[6])
            except ValueError:
                pass
    for it, key in (("D", "sched"), ("F", "fitem"), ("G", "gitem")):
        m = re.search(r"(?:^|\n)" + it + r"\)\s*([^\n]*(?:\n(?![A-GQ]\))[^\n]*)*)", raw)
        if m and m.group(1).strip():
            out[key] = re.sub(r"\s+", " ", m.group(1).strip())
    return out


def alt_display(rec):
    """Human vertical extent, preferring the official F)/G) items."""
    f, g = rec.get("fitem"), rec.get("gitem")
    lo, hi = rec.get("low"), rec.get("high")
    if f and g:
        return f + " – " + g
    if g:
        return "up to " + g
    if lo is not None and hi is not None and not (lo == 0 and hi >= 999):
        fl = lambda x: "GND" if x == 0 else ("UNL" if x >= 999 else "FL" + str(x).zfill(3))
        return fl(lo) + " – " + fl(hi)
    return None


def main():
    print("fetching NOTAMs …", file=sys.stderr)
    data = json.loads(curl(API, origin="https://learn.vatphil.com"))
    notams_raw = data.get("notams", [])
    print("  got", len(notams_raw), "of", data.get("pagination", {}).get("total"), file=sys.stderr)

    print("fetching airport coordinates …", file=sys.stderr)
    coords = {}
    rdr = csv.DictReader(io.StringIO(curl(AIRPORTS_CSV)))
    for r in rdr:
        ident = r["ident"]
        if ident.startswith("RP") and len(ident) == 4:
            try:
                coords[ident] = [round(float(r["latitude_deg"]), 5),
                                 round(float(r["longitude_deg"]), 5),
                                 r["name"]]
            except (ValueError, KeyError):
                pass

    # FIR-wide / non-aerodrome indicators that OurAirports has no point for.
    # RPHI is the whole Manila FIR — plot it at a central point so its
    # (large) set of FIR-wide NOTAMs still surfaces on the map.
    coords.setdefault("RPHI", [12.8, 122.8, "Manila FIR (FIR-wide)"])

    notams, used_ap, jobs = [], {}, []
    for n in notams_raw:
        if n.get("is_draft"):
            continue
        icao = (n.get("loc_indicator") or "").strip().upper()
        est = n.get("estperm")
        est = est.upper() if isinstance(est, str) and est not in ("NULL",) else None
        body = (n.get("additional_txt") or "").replace("\r", "").strip()
        geo = parse_geo(body)
        rec = {
            "id":   n.get("id"),
            "num":  n.get("full_number") or (str(n.get("series") or "") + str(n.get("number") or "")),
            "type": n.get("notam_type"),          # N new / R replace / C cancel
            "icao": icao,
            "from": iso(n.get("begin_effect")),
            "to":   iso(n.get("end_effect")),
            "est":  est,                            # EST / PERM / None
            "code": n.get("notam_code"),           # Q-code, e.g. MKXX
            "scope": n.get("scope"),
            "purpose": n.get("purpose"),
            "traffic": n.get("traffic"),
            "text": body,
        }
        if geo:
            rec["geo"] = geo
        notams.append(rec)
        jobs.append((rec, n.get("series"), n.get("id"), body))
        if icao in coords:
            used_ap[icao] = coords[icao]

    # enrich each NOTAM with its full-modal data (Q-line limits, D/F/G items)
    print("fetching %d NOTAM modals for altitude + schedule …" % len(jobs), file=sys.stderr)
    def enrich(job):
        rec, series, nid, body = job
        m = fetch_modal(series, nid)
        if "low" in m:
            rec["low"] = m["low"]
            rec["high"] = m["high"]
        if m.get("sched"):
            rec["sched"] = m["sched"]
        for k in ("fitem", "gitem"):
            if m.get(k):
                rec[k] = m[k]
        alt = alt_display(rec) or (parse_alt(body) or {}).get("txt")
        if alt:
            rec["alt"] = alt
        return 1 if m else 0
    with ThreadPoolExecutor(max_workers=10) as ex:
        ok = sum(ex.map(enrich, jobs))
    print("  enriched %d/%d" % (ok, len(jobs)), file=sys.stderr)
    # drop the transient item fields once alt/limits are computed
    for rec in notams:
        rec.pop("fitem", None)
        rec.pop("gitem", None)

    # newest effective first
    notams.sort(key=lambda x: x["from"] or "", reverse=True)

    out = {
        "generated": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "total": len(notams),
        "airports": used_ap,
        "notams": notams,
    }
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w") as f:
        json.dump(out, f, separators=(",", ":"), ensure_ascii=False)
    kb = os.path.getsize(OUT) / 1024
    print("wrote %s  (%d NOTAMs, %d aerodromes plotted, %.0f KB)" %
          (os.path.relpath(OUT), len(notams), len(used_ap), kb))


if __name__ == "__main__":
    main()
