#!/usr/bin/env python3
"""Build docs/assets/data/airspace_zones.json for the Airspace Explorer.

Covers every airport that can be staffed on the VATPHIL network (from
VoiceChannels.txt), not just briefing airports:
  * CTR  -> real polygon from the sector file (2609.ese SECTOR/SECTORLINE)
  * ATZ  -> 5 NM circle for every tower (Class B, SFC-2000)
  * AAZ  -> 5 NM circle for every Radio/FSS (Class G, SFC-2000)
Aerodrome coordinates come from the sector file's [AIRPORT] block; names from
the briefing list where available, otherwise derived from the VATSIM callsign.
Frequencies from VoiceChannels.txt.
"""
import re, json, os, datetime

ROOT = os.path.join(os.path.dirname(__file__), "..")
SF   = os.path.join(ROOT, "..", "..", "VATPHIL-Sector-Files")
ESE  = os.path.join(SF, "2609.ese")
SCT  = os.path.join(SF, "2609.sct")
VC   = os.path.join(SF, "RPHI", "Settings", "VoiceChannels.txt")

def dms(s):
    sign = 1 if s[0] in "NE" else -1
    r = s[1:].split(".")
    deg, mn = float(r[0]), float(r[1])
    sec = float(r[2] + "." + r[3]) if len(r) > 3 else float(r[2])
    return sign * (deg + mn / 60 + sec / 3600)

# --- names from the briefing aerodrome list (index.md) ---
idx = open(os.path.join(ROOT, "docs/briefings/index.md"), encoding="utf-8").read()
names = {}
for m in re.finditer(r'icao:\s*"(RP[A-Z]{2})".*?name:\s*"([^"]+)"', idx):
    names[m.group(1)] = m.group(2)

# --- frequencies from VoiceChannels: icao -> {suffix: (name, freq)} ---
vc = {}
for line in open(VC, encoding="utf-8", errors="ignore"):
    m = re.match(r'AG:(RP[A-Z]{2})_([A-Z0-9_]+?)\s+([^:]+):([\d.]+)', line.strip())
    if m:
        vc.setdefault(m.group(1), {})[m.group(2)] = (m.group(3).strip(), m.group(4))

def strip_cs(nm):
    return re.sub(r'\s+(Control Tower|Tower|Radio|Approach|Ground|Delivery|ATIS)$', '', nm).strip()

# fill names for staffable airports without a briefing page (from the callsign)
for ic, f in vc.items():
    if ic not in names:
        for k in ("TWR", "R_TWR", "APP"):
            if k in f:
                names[ic] = strip_cs(f[k][0]); break
        names.setdefault(ic, ic)

def unit(icao, kinds):
    f = vc.get(icao, {})
    for k in kinds:
        if k in f:
            return f[k]
    return (None, None)

# --- coordinates from the sector file [AIRPORT] block ---
sct = open(SCT, encoding="utf-8", errors="replace").read()
coords, inair = {}, False
for ln in sct.splitlines():
    if ln.startswith("[AIRPORT]"): inair = True; continue
    if inair and ln.startswith("["): break
    if inair:
        m = re.match(r'^(RP[A-Z]{2})\s+\S+\s+([NS][\d.]+)\s+([EW][\d.]+)', ln)
        if m:
            try: coords[m.group(1)] = (dms(m.group(2)), dms(m.group(3)))
            except Exception: pass

# staffable airports not listed in the sector file's [AIRPORT] block (coords from AIP/OurAirports)
FALLBACK = {"RPLV": (15.4347, 121.0910), "RPUQ": (17.55472, 120.35611),
            "RPVU": (12.31083, 122.08444), "RPMJ": (6.05361, 121.01111)}
for ic, c in FALLBACK.items():
    coords.setdefault(ic, c)
# fill any remaining gaps from the briefing aerodrome list
for m in re.finditer(r'icao:\s*"(RP[A-Z]{2})".*?lat:\s*([-\d.]+),\s*lon:\s*([-\d.]+)', idx):
    coords.setdefault(m.group(1), (float(m.group(2)), float(m.group(3))))

# --- CTR polygons from the ESE ---
raw = open(ESE, encoding="utf-8", errors="replace").read()
sep_m = re.search(r'SECTOR:RPHI(.)RP', raw)
SEP = sep_m.group(1) if sep_m else "∑"
slines, cur = {}, None
for ln in raw.splitlines():
    if ln.startswith("SECTORLINE:"):
        cur = ln.split(":", 1)[1].strip(); slines[cur] = []
    elif ln.startswith("COORD:") and cur is not None:
        p = ln.split(":")
        try: slines[cur].append([dms(p[1].strip()), dms(p[2].strip())])
        except Exception: pass
    elif ln.startswith("SECTOR:") or ln.startswith("CIRCLE_SECTORLINE:"):
        cur = None

ctr_poly = {}
def flush(block):
    if not block: return
    m = re.match(r'^(RP[A-Z]{2}) CTR$', block["name"])
    if m and block["border"] in slines and len(slines[block["border"]]) >= 3:
        ctr_poly[m.group(1)] = {"coords": slines[block["border"]], "ceil": block["ceil"]}
block = None
for ln in raw.splitlines():
    if ln.startswith("SECTOR:"):
        flush(block); block = None
        if ln.startswith("SECTOR:RPHI" + SEP):
            parts = ln[len("SECTOR:"):].split(SEP)
            name = parts[1].strip() if len(parts) > 1 else ""
            tail = parts[-1].split(":")
            ceil = int(tail[2]) if len(tail) >= 3 and tail[2].isdigit() else None
            block = {"name": name, "ceil": ceil, "border": None}
    elif block and ln.startswith("BORDER:") and block["border"] is None:
        block["border"] = ln.split(":", 1)[1].strip()
flush(block)

# --- build zones ---
ZLABEL = {"ATZ": "Aerodrome Traffic Zone", "CTR": "Control Zone", "AAZ": "Aerodrome Advisory Zone"}
zones = []

for icao, info in ctr_poly.items():
    u = unit(icao, ["APP", "TWR", "R_TWR"])
    zones.append({"icao": icao, "name": names.get(icao, icao), "type": "CTR", "typeName": ZLABEL["CTR"],
                  "geom": "polygon", "coords": [[round(a, 5), round(b, 5)] for a, b in info["coords"]],
                  "class": "D", "lower": "SFC", "upper": (str(info["ceil"]) + " FT") if info["ceil"] else "1500 FT",
                  "unit": u[0], "freq": u[1]})

for icao, f in vc.items():
    if icao not in coords:
        continue
    lat, lon = coords[icao]
    if "TWR" in f:
        u = unit(icao, ["TWR"])
        zones.append({"icao": icao, "name": names.get(icao, icao), "type": "ATZ", "typeName": ZLABEL["ATZ"],
                      "geom": "circle", "center": [round(lat, 5), round(lon, 5)], "radiusNm": 5.0,
                      "class": "B", "lower": "SFC", "upper": "2000 FT", "unit": u[0], "freq": u[1]})
    if ("R_TWR" in f) and ("TWR" not in f):
        u = unit(icao, ["R_TWR"])
        zones.append({"icao": icao, "name": names.get(icao, icao), "type": "AAZ", "typeName": ZLABEL["AAZ"],
                      "geom": "circle", "center": [round(lat, 5), round(lon, 5)], "radiusNm": 5.0,
                      "class": "G", "lower": "SFC", "upper": "2000 FT", "unit": u[0], "freq": u[1]})

zones.sort(key=lambda z: (z["icao"], {"CTR": 0, "ATZ": 1, "AAZ": 2}[z["type"]]))
out = {"_about": "Airspace Explorer zones. CTR = polygon from 2609.ese; ATZ/AAZ = 5 NM circles. Coords from 2609.sct [AIRPORT]; freq from VoiceChannels.txt. Covers every staffable VATPHIL airport.",
       "generated": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
       "zones": zones}
json.dump(out, open(os.path.join(ROOT, "docs/assets/data/airspace_zones.json"), "w"), ensure_ascii=False, indent=0)
from collections import Counter
print("wrote", len(zones), "zones:", dict(Counter(z["type"] for z in zones)),
      "| airports:", len(set(z["icao"] for z in zones)))
print("no freq:", [z["icao"] + ":" + z["type"] for z in zones if not z["freq"]])
