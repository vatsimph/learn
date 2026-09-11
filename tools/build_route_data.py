#!/usr/bin/env python3
"""
Build the data file for the Random Flight Generator
(docs/briefings/flight-generator.md).

Reads the VATPHIL routes list and a EuroScope sector file (.sct), then for each
route precomputes:

  * "line" — the full drawn polyline [[lat,lon], ...], following real airways
             (their intermediate points) between the named fixes.
  * "pts"  — every named point along the route to label:
             [["IDENT", lat, lon, kind], ...]  kind = "ap" (airport endpoint),
             "fix" (written in the route) or "awy" (airway bend waypoint).
  * "awy"  — one label per airway leg: [["NAME", aLat, aLon, bLat, bLon], ...]
             where a..b is the mid segment of that leg (for a rotated label).

Output: docs/assets/data/routes.json  (original fields + line + pts + awy).

Re-run whenever Routes.json or the sector file changes:

    python3 tools/build_route_data.py \
        --routes /path/to/Routes.json --sct /path/to/2608.sct
"""
import argparse, json, math, os, re, sys
from collections import deque

MANUAL = {
    "RPVV": ("N012.07.17.653", "E120.05.49.923"),  # Busuanga (Coron)
    "VHHH": ("N022.18.32.000", "E113.54.52.000"),  # Hong Kong Intl
    "VHHX": ("N022.19.43.000", "E114.11.34.000"),  # Hong Kong (Kai Tak)
    "VMMC": ("N022.08.59.000", "E113.35.31.000"),  # Macau Intl
    "ZGSZ": ("N022.38.21.000", "E113.48.39.000"),  # Shenzhen Bao'an
}

POINT_SECTIONS = ("VOR", "NDB", "FIXES", "AIRPORT")
AIRWAY_SECTIONS = ("HIGH AIRWAY", "LOW AIRWAY")
NODE_ROUND = 5
MATCH_TOL = 0.03


def dms(tok):
    h = tok[0]
    d, m, si, sf = tok[1:].split(".")
    v = int(d) + int(m) / 60 + float(f"{si}.{sf}") / 3600
    return round(-v if h in "SW" else v, 6)


def key(lat, lon):
    return (round(lat, NODE_ROUND), round(lon, NODE_ROUND))


def nmdist(a, b):
    R = 3440.065
    dlat = math.radians(b[0] - a[0])
    dlon = math.radians(b[1] - a[1])
    s = (math.sin(dlat / 2) ** 2
         + math.cos(math.radians(a[0])) * math.cos(math.radians(b[0])) * math.sin(dlon / 2) ** 2)
    return 2 * R * math.asin(min(1, math.sqrt(s)))


def parse_sct(path):
    coords, airways, section = {}, {}, None
    for line in open(path, encoding="latin-1"):
        s = line.rstrip("\n")
        head = re.match(r"^\[(.+?)\]", s)
        if head:
            section = head.group(1)
            continue
        if not s.strip() or s.lstrip().startswith(";"):
            continue
        p = s.split()
        if section in POINT_SECTIONS:
            if section == "FIXES":
                if len(p) >= 3 and p[1][0] in "NS" and p[2][0] in "EW":
                    name, la, lo = p[0], p[1], p[2]
                else:
                    continue
            else:
                if len(p) >= 4 and p[2][0] in "NS" and p[3][0] in "EW":
                    name, la, lo = p[0], p[2], p[3]
                else:
                    continue
            try:
                coords.setdefault(name, [dms(la), dms(lo)])
            except Exception:
                pass
        elif section in AIRWAY_SECTIONS:
            if len(p) >= 5 and p[1][0] in "NS":
                try:
                    a = key(dms(p[1]), dms(p[2]))
                    b = key(dms(p[3]), dms(p[4]))
                except Exception:
                    continue
                g = airways.setdefault(p[0], {})
                g.setdefault(a, set()).add(b)
                g.setdefault(b, set()).add(a)
    for name, (la, lo) in MANUAL.items():
        coords.setdefault(name, [dms(la), dms(lo)])
    return coords, airways


def nearest_node(graph, ll):
    best, bestd = None, MATCH_TOL ** 2
    for n in graph:
        d = (n[0] - ll[0]) ** 2 + (n[1] - ll[1]) ** 2
        if d <= bestd:
            best, bestd = n, d
    return best


def airway_between(graph, a_ll, b_ll):
    start, end = nearest_node(graph, a_ll), nearest_node(graph, b_ll)
    if not start or not end or start == end:
        return None
    prev = {start: None}
    q = deque([start])
    while q:
        cur = q.popleft()
        if cur == end:
            break
        for nb in graph[cur]:
            if nb not in prev:
                prev[nb] = cur
                q.append(nb)
    if end not in prev:
        return None
    path, cur = [], end
    while cur is not None:
        path.append(cur)
        cur = prev[cur]
    path.reverse()
    return [[n[0], n[1]] for n in path[1:-1]]


def mid_segment(poly):
    """Return the [a, b] segment straddling the half-length of a polyline."""
    if len(poly) < 2:
        return None
    lens = [nmdist(poly[i], poly[i + 1]) for i in range(len(poly) - 1)]
    half, acc = sum(lens) / 2, 0.0
    for i, l in enumerate(lens):
        if acc + l >= half:
            return poly[i], poly[i + 1]
        acc += l
    return poly[-2], poly[-1]


def expand(route, coords, airways, name_of):
    named = [route["dept"]]
    conn = []
    cur = None
    for tok in route["route"].split():
        if tok in airways:
            cur = tok
        elif tok == "DCT":
            cur = None
        elif tok in coords:
            named.append(tok)
            conn.append(cur)
            cur = None
        else:
            cur = None
    named.append(route["dest"])
    conn.append(cur)
    named = [n for n in named if n in coords]

    nodes = [{"name": named[0], "ll": coords[named[0]], "kind": "ap"}]
    legs = []
    for k in range(len(named) - 1):
        a, b = named[k], named[k + 1]
        awy = conn[k] if k < len(conn) else None
        i0 = len(nodes) - 1
        mids = airway_between(airways[awy], coords[a], coords[b]) if awy in airways else None
        if mids:
            for m in mids:
                nodes.append({"name": name_of.get(key(m[0], m[1])), "ll": m, "kind": "awy"})
        last = (k == len(named) - 2)
        nodes.append({"name": b, "ll": coords[b], "kind": "ap" if last else "fix"})
        legs.append((awy if awy in airways else None, i0, len(nodes) - 1))

    line = [n["ll"] for n in nodes]
    pts = [[n["name"], n["ll"][0], n["ll"][1], n["kind"]] for n in nodes if n["name"]]
    awy = []
    for name, i0, i1 in legs:
        if not name:
            continue
        seg = mid_segment([nodes[i]["ll"] for i in range(i0, i1 + 1)])
        if seg:
            awy.append([name, seg[0][0], seg[0][1], seg[1][0], seg[1][1]])
    return line, pts, awy


def main():
    here = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    ap = argparse.ArgumentParser()
    ap.add_argument("--routes", required=True)
    ap.add_argument("--sct", required=True)
    ap.add_argument("--out", default=os.path.join(here, "docs", "assets", "data"))
    args = ap.parse_args()

    coords, airways = parse_sct(args.sct)
    name_of = {}
    for n, (la, lo) in coords.items():
        name_of.setdefault(key(la, lo), n)

    routes = json.load(open(args.routes))
    data = routes["data"]
    missing = []
    for r in data:
        if r["dept"] not in coords or r["dest"] not in coords:
            missing.append(f'{r["dept"]}-{r["dest"]}')
            r["line"], r["pts"], r["awy"] = [], [], []
            continue
        r["line"], r["pts"], r["awy"] = expand(r, coords, airways, name_of)

    os.makedirs(args.out, exist_ok=True)
    dst = os.path.join(args.out, "routes.json")
    json.dump(routes, open(dst, "w"), separators=(",", ":"))
    print(f"routes: {len(data)}   sct fixes: {len(coords)}   airways: {len(airways)}")
    print(f"avg polyline points/route: {sum(len(r['line']) for r in data)/max(1,len(data)):.1f}")
    print(f"routes missing an endpoint airport: {missing or 'none'}")
    print(f"wrote {dst} ({os.path.getsize(dst)} bytes)")
    if missing:
        print("  -> add them to MANUAL in this script.", file=sys.stderr)


if __name__ == "__main__":
    main()
