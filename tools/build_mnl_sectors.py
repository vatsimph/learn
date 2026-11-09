#!/usr/bin/env python3
"""
Build the Manila ACC sector polygons for the briefings map
(docs/briefings/index.md, `var sectors = [...]`) from the boundary lines in
tools/mnl_sector_lines.geojson (FIR border + sector boundary lines).

The lines are noded and polygonized into atomic cells; each published sector
is the union of its atomic cells.  Prints the JS lines to paste / writes them
into index.md between the `var sectors = [` ... `];` markers.

Run: venv/bin/python tools/build_mnl_sectors.py
"""
import json, os, re
from shapely.geometry import shape, Point, LineString, mapping
from shapely.ops import unary_union, polygonize, snap, split

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LINES = os.path.join(HERE, "tools", "mnl_sector_lines.geojson")
EXPLORER = os.path.join(HERE, "docs", "assets", "data", "mnl_sectors.json")  # Airspace Explorer
INDEX = os.path.join(HERE, "docs", "briefings", "index.md")

# representative (lon, lat) inside each atomic cell
SEEDS = {
    "NW": (118.0, 20.0), "NE": (127.0, 18.0),
    "CN": (120.0, 16.5), "CE": (123.5, 15.5),
    "CW": (118.5, 14.0), "CS": (122.5, 13.2),
    "W": (115.0, 14.0), "SW": (117.0, 10.3),
    "S": (121.0, 8.0), "SE": (127.0, 10.0),
    "CIRCLE": (121.02, 14.5),
}
# published sectors -> atomic cells (circle halves are added to CN / CS)
SECTORS = [
    ("MNL_C",   ["CN", "CE", "CW", "CS"]),
    ("MNL_CNC", ["CN", "CE"]),
    ("MNL_CNS", ["CW", "CS"]),
    ("MNL_BBN", ["NW", "NE", "CN", "CE", "W"]),
    ("MNL_BBS", ["CW", "CS", "SW", "S", "SE"]),
    ("MNL_BB2", ["CS", "S", "SE"]),
    ("MNL_NW", ["NW"]), ("MNL_NE", ["NE"]),
    ("MNL_CN", ["CN"]), ("MNL_CE", ["CE"]),
    ("MNL_CW", ["CW"]), ("MNL_CS", ["CS"]),
    ("MNL_W", ["W"]), ("MNL_SW", ["SW"]),
    ("MNL_S", ["S"]), ("MNL_SE", ["SE"]),
]


# id -> (name, primary frequency); keep in sync with SECTOR_INFO in index.md
INFO = {
    "MNL_C": ("Manila Inner Combined", "132.075"),
    "MNL_CNC": ("Manila Central North Combined", "129.000"),
    "MNL_CNS": ("Manila Central South Combined", "131.500"),
    "MNL_BBN": ("Manila North Combined", "126.575"),
    "MNL_BBS": ("Manila South Combined", "133.500"),
    "MNL_BB2": ("Manila Split South 2", "124.900"),
    "MNL_NW": ("Manila North West", "128.700"), "MNL_NE": ("Manila North East", "132.500"),
    "MNL_CN": ("Manila Central North", "120.500"), "MNL_CE": ("Manila Central East", "128.750"),
    "MNL_CW": ("Manila Central West", "132.700"), "MNL_CS": ("Manila Central South", "125.700"),
    "MNL_W": ("Manila West", "133.750"), "MNL_SW": ("Manila South West", "118.900"),
    "MNL_S": ("Manila South", "124.900"), "MNL_SE": ("Manila South East", "125.700"),
}


def main():
    feats = json.load(open(LINES))["features"]
    fir = [f for f in feats if f["properties"]["name"] == "FIR Border"][0]
    fir_line = shape(fir["geometry"])
    lines = []
    for f in feats:
        g = shape(f["geometry"])
        if f["properties"]["name"] != "FIR Border":
            g = snap(g, fir_line, 0.01)          # lines end on the FIR border
        lines.append(g)
    lines = [snap(g, unary_union(lines), 0.005) for g in lines]
    cells = list(polygonize(unary_union(lines)))
    print("cells:", len(cells))

    found = {}
    for name, (x, y) in SEEDS.items():
        hit = [c for c in cells if c.contains(Point(x, y))]
        assert len(hit) == 1, (name, len(hit))
        found[name] = hit[0]
    assert len({id(c) for c in found.values()}) == len(SEEDS), "seeds share a cell"
    assert len(cells) == len(SEEDS), "unexpected extra cells: %d" % (len(cells) - len(SEEDS))

    # Manila circle: north half -> CN, south half -> CS (split on the BB line)
    circ = found["CIRCLE"]
    minx, miny, maxx, maxy = circ.bounds
    cut = LineString([(120.69444444, 14.61027778), (121.36277778, 14.46777778)])
    ext = LineString([(minx - 1, 14.61027778 + (14.61027778 - 14.46777778) / (121.36277778 - 120.69444444) * (minx - 1 - 120.69444444)),
                      (maxx + 1, 14.61027778 + (14.61027778 - 14.46777778) / (121.36277778 - 120.69444444) * (maxx + 1 - 120.69444444))])
    parts = list(split(circ, ext).geoms)
    assert len(parts) == 2
    north = max(parts, key=lambda p: p.centroid.y)
    south = min(parts, key=lambda p: p.centroid.y)
    found["CN"] = unary_union([found["CN"], north])
    found["CS"] = unary_union([found["CS"], south])

    out = []
    explorer = []
    for sid, members in SECTORS:
        u = unary_union([found[m] for m in members]).buffer(0)
        g = mapping(u)
        if g["type"] == "Polygon":
            g = {"type": "MultiPolygon", "coordinates": [g["coordinates"]]}
        # round coords
        def rnd(o):
            return [rnd(i) for i in o] if isinstance(o, (list, tuple)) and o and isinstance(o[0], (list, tuple)) else [round(o[0], 6), round(o[1], 6)]
        g["coordinates"] = rnd(g["coordinates"])
        out.append({"type": "Feature", "properties": {"id": sid}, "geometry": g})
        nm, fq = INFO[sid]
        explorer.append({"type": "Feature", "properties": {"id": sid, "name": nm, "freq": fq}, "geometry": g})
        print(sid, u.geom_type, round(u.area, 2), "holes:", sum(len(p.interiors) for p in (u.geoms if u.geom_type == "MultiPolygon" else [u])))

    with open(EXPLORER, "w") as fh:
        json.dump({"type": "FeatureCollection", "features": explorer}, fh, separators=(",", ":"))
    print("wrote", EXPLORER)

    js = "  var sectors = [\n" + ",\n".join("    " + json.dumps(f, separators=(",", ":")) for f in out) + "\n  ];"
    src = open(INDEX, encoding="utf-8").read()
    new, n = re.subn(r"  var sectors = \[\n.*?\n  \];", lambda m: js, src, count=1, flags=re.S)
    assert n == 1
    open(INDEX, "w", encoding="utf-8").write(new)
    print("updated", INDEX)


if __name__ == "__main__":
    main()
