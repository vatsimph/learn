#!/usr/bin/env python3
"""
Build the Manila ACC outer-boundary polygon used by the Flight Generator map
(docs/briefings/flight-generator.md).

It reads the sector GeoJSON embedded in the main briefings map
(docs/briefings/index.md), dissolves all the overlapping ACC split sectors into
a single outline and writes:

    docs/assets/data/mnl_boundary.json   (a GeoJSON FeatureCollection)

Requires shapely:  venv/bin/python -m pip install shapely
Run:               venv/bin/python tools/build_mnl_boundary.py
"""
import json, os
from shapely.geometry import shape, mapping
from shapely.ops import unary_union

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INDEX = os.path.join(HERE, "docs", "briefings", "index.md")
OUT = os.path.join(HERE, "docs", "assets", "data", "mnl_boundary.json")


def extract_js_array(src, varname):
    i = src.index("var " + varname + " = ")
    start = src.index("[", i)
    depth = 0
    for j in range(start, len(src)):
        if src[j] == "[":
            depth += 1
        elif src[j] == "]":
            depth -= 1
            if depth == 0:
                return json.loads(src[start:j + 1])
    raise ValueError("unterminated array for " + varname)


def main():
    sectors = extract_js_array(open(INDEX).read(), "sectors")
    union = unary_union([shape(f["geometry"]) for f in sectors])
    union = union.buffer(0).simplify(0.01, preserve_topology=True)
    fc = {
        "type": "FeatureCollection",
        "features": [{
            "type": "Feature",
            "properties": {"id": "MNL_ACC", "name": "Manila ACC"},
            "geometry": mapping(union),
        }],
    }
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    json.dump(fc, open(OUT, "w"), separators=(",", ":"))
    print(f"sectors dissolved: {len(sectors)} -> {union.geom_type}")
    print(f"wrote {OUT} ({os.path.getsize(OUT)} bytes)")


if __name__ == "__main__":
    main()
