#!/usr/bin/env python3
"""Extract Manila ACC sub-sector polygons + owner priority lists from the
EuroScope .ese so the Live Traffic map can light up the *actual* sector a
centre controller owns (instead of the whole FIR).

Output: docs/assets/data/acc_sectors.json
  {
    "posmap":  { "<identifier>": "<login callsign>", ... },
    "sectors": [ { "name": "...", "owners": ["CE","CN1",...],
                   "ring": [[lat,lon], ...] }, ... ]
  }
"""
import json, os, re, sys

ESE = "/Users/jacob/Desktop/VATPHIL/VATPHIL-Sector-Files/2609.ese"
OUT = os.path.join(os.path.dirname(__file__), "..", "docs", "assets", "data", "acc_sectors.json")


def dms(tok):
    # N013.51.77.000  /  E124.41.32.000  (min/sec may exceed 60 -> tolerant)
    h = tok[0]
    d, m, s = tok[1:].split(".", 2)
    val = int(d) + int(m) / 60.0 + float(s) / 3600.0
    if h in "SW":
        val = -val
    return val


def coord(line):
    _, la, lo = line.split(":", 2)
    return (round(dms(la), 6), round(dms(lo), 6))


def main():
    with open(ESE, encoding="utf-8", errors="replace") as f:
        lines = [l.rstrip("\n") for l in f]

    # --- POSITIONS: identifier -> login callsign ------------------------
    posmap = {}
    inpos = False
    for l in lines:
        if l.startswith("["):
            inpos = l.strip() == "[POSITIONS]"
            continue
        if inpos and ":" in l and not l.startswith(";"):
            p = l.split(":")
            if len(p) > 3 and p[3]:
                posmap.setdefault(p[3], p[0])

    # --- AIRSPACE -------------------------------------------------------
    sectorlines = {}         # id -> [(lat,lon), ...]
    cur_sl = None
    sectors = []             # {name, owners, border}
    cur_sec = None
    inair = False
    for l in lines:
        if l.startswith("["):
            inair = l.strip() == "[AIRSPACE]"
            cur_sl = None
            continue
        if not inair:
            continue
        if l.startswith("SECTORLINE:"):
            cur_sl = l.split(":", 1)[1].strip()
            sectorlines[cur_sl] = []
            cur_sec = None
        elif l.startswith("COORD:") and cur_sl is not None:
            sectorlines[cur_sl].append(coord(l))
        elif l.startswith("SECTOR:"):
            cur_sl = None
            name = l.split(":", 1)[1].rsplit(":", 2)[0]  # RPHI∑MANILA ACC CE∑200∑460
            cur_sec = {"raw": name, "owners": [], "border": []}
            sectors.append(cur_sec)
        elif l.startswith("OWNER:") and cur_sec is not None:
            cur_sec["owners"] = [x for x in l.split(":")[1:] if x]
        elif l.startswith("BORDER:") and cur_sec is not None:
            cur_sec["border"] = [x for x in l.split(":")[1:] if x]

    # --- stitch a set of polylines into an ordered ring -----------------
    def stitch(border):
        segs = [list(sectorlines[b]) for b in border if sectorlines.get(b)]
        if not segs:
            return []
        key = lambda p: (round(p[0], 5), round(p[1], 5))
        chain = segs.pop(0)
        changed = True
        while segs and changed:
            changed = False
            hs, he = key(chain[0]), key(chain[-1])
            for i, s in enumerate(segs):
                ss, se = key(s[0]), key(s[-1])
                if he == ss:
                    chain += s[1:]
                elif he == se:
                    chain += list(reversed(s))[1:]
                elif hs == se:
                    chain = s[:-1] + chain
                elif hs == ss:
                    chain = list(reversed(s))[:-1] + chain
                else:
                    continue
                segs.pop(i)
                changed = True
                break
        return chain

    out = {"posmap": posmap, "sectors": []}
    for s in sectors:
        if "MANILA ACC" not in s["raw"]:
            continue
        ring = stitch(s["border"])
        if len(ring) < 3:
            print("WARN could not stitch", s["raw"], "segs used", len(s["border"]), file=sys.stderr)
            continue
        # close ring
        if ring[0] != ring[-1]:
            ring.append(ring[0])
        name = s["raw"].split("∑")[1] if "∑" in s["raw"] else s["raw"]
        out["sectors"].append({
            "name": name.strip(),
            "owners": s["owners"],
            "ring": [[la, lo] for la, lo in ring],
            "leftover": len([b for b in s["border"] if not sectorlines.get(b)]),
        })
        print(f"{name.strip():18s} owners={','.join(s['owners']):20s} pts={len(ring)}")

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w") as f:
        json.dump(out, f, separators=(",", ":"))
    print("wrote", OUT, "sectors", len(out["sectors"]))
    # show identifier map for MNL centres
    for ident, cs in posmap.items():
        if cs.startswith("MNL_") and cs.endswith("_CTR") or cs == "MNL_CTR":
            print("  id", ident, "->", cs)


if __name__ == "__main__":
    main()
