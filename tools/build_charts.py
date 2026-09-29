#!/usr/bin/env python3
"""Bake the vatphil.com chart lists into a static JSON for the briefing chart
pickers. vatphil.com/charts?icao=XXXX is a server-rendered table (category
headers + one list of viewchart.php?id=N links per category) with no CORS
header, so the browser can't read it — this runs at build time instead. The
PDFs themselves are still served live by vatphil.com.

Which airports: every ICAO a page links as vatphil.com/charts?icao=XXXX or
marks up as <div class="chart-picker" data-icao="XXXX">, plus any given on
the command line.

Charts added, renamed or removed on vatphil.com show up on the next run; the
changes are printed. If an airport can't be fetched or comes back empty (site
down, layout changed) its previous list is kept rather than wiped.

Output: docs/assets/data/charts.json
  { generated, airports:{ ICAO:[ [category, [[id, name], ...]], ... ] } }

Re-run to refresh:  venv/bin/python tools/build_charts.py
"""
import glob, json, os, re, subprocess, sys
from datetime import datetime, timezone
from html.parser import HTMLParser

ROOT = os.path.join(os.path.dirname(__file__), "..")
OUT = os.path.join(ROOT, "docs", "assets", "data", "charts.json")
PAGE = "https://vatphil.com/charts?icao={icao}"


def curl(url):
    r = subprocess.run(["curl", "-sS", "--fail", "--max-time", "30", "-A", "Mozilla/5.0", url],
                       capture_output=True, text=True)
    if r.returncode != 0:
        raise RuntimeError(r.stderr.strip()[:200])
    return r.stdout


class ChartTable(HTMLParser):
    """#charts-table: first body row holds the category <h3>s, the next row one
    <td> per category with <a href="viewchart.php?id=N">name</a> links."""
    def __init__(self):
        super().__init__()
        self.in_table = self.in_h2 = self.in_h3 = self.in_a = False
        self.icao, self.cats, self.cols = "", [], []
        self.row = self.col = -1
        self.href = None
        self.text = ""

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "table" and a.get("id") == "charts-table":
            self.in_table = True
        if not self.in_table:
            return
        if tag == "h2":
            self.in_h2 = True
        elif tag == "tr":
            self.row += 1
            self.col = -1
        elif tag == "td":
            self.col += 1
        elif tag == "h3":
            self.in_h3, self.text = True, ""
        elif tag == "a":
            m = re.search(r"viewchart\.php\?id=(\d+)", a.get("href") or "")
            self.in_a, self.href, self.text = bool(m), m and int(m.group(1)), ""

    def handle_endtag(self, tag):
        if not self.in_table:
            return
        if tag == "table":
            self.in_table = False
        elif tag == "h2":
            self.in_h2 = False
        elif tag == "h3" and self.in_h3:
            self.in_h3 = False
            self.cats.append(" ".join(self.text.split()))
        elif tag == "a" and self.in_a:
            self.in_a = False
            while len(self.cols) <= self.col:
                self.cols.append([])
            self.cols[self.col].append([self.href, " ".join(self.text.split())])

    def handle_data(self, data):
        if self.in_h2:
            self.icao += data.strip()
        if self.in_h3 or self.in_a:
            self.text += data


def parse(page):
    p = ChartTable()
    p.feed(page)
    cats = [[c, p.cols[i] if i < len(p.cols) else []] for i, c in enumerate(p.cats)]
    return p.icao.upper(), [c for c in cats if c[1]]


def wanted_icaos():
    found = set(a.upper() for a in sys.argv[1:] if re.fullmatch(r"[A-Za-z]{4}", a))
    for path in glob.glob(os.path.join(ROOT, "docs", "**", "*.md"), recursive=True):
        with open(path, encoding="utf-8", errors="replace") as f:
            t = f.read()
        found.update(re.findall(r"vatphil\.com/charts\?icao=(RP[A-Z]{2})", t))
        found.update(re.findall(r'class="chart-picker"[^>]*data-icao="(RP[A-Z]{2})"', t))
    return sorted(found)


def describe(old, new):
    """'+2 added, 1 renamed, 1 removed' between two category lists, by chart id."""
    o = {cid: name for _, items in old for cid, name in items}
    n = {cid: name for _, items in new for cid, name in items}
    parts = []
    for label, count in (("added", len(n.keys() - o.keys())),
                         ("renamed", sum(1 for k in n.keys() & o.keys() if n[k] != o[k])),
                         ("removed", len(o.keys() - n.keys()))):
        if count:
            parts.append("%d %s" % (count, label))
    return ", ".join(parts)


def main():
    try:
        with open(OUT) as f:
            prev = json.load(f).get("airports", {})
    except (OSError, ValueError):
        prev = {}

    airports, kept, skipped = {}, [], []
    for icao in wanted_icaos():
        try:
            got, cats = parse(curl(PAGE.format(icao=icao)))
            if got != icao:
                # unknown ICAOs fall back to the RPLL page — never file that under another airport
                raise RuntimeError("page came back for %r" % got)
            if not cats:
                raise RuntimeError("no charts listed (none published, or the page layout changed)")
        except RuntimeError as e:
            if icao in prev:
                airports[icao] = prev[icao]
                kept.append(icao)
            else:
                skipped.append(icao)
            print("  %s: %s — %s" % (icao, e, "kept previous list" if icao in prev else "skipped"),
                  file=sys.stderr)
            continue
        airports[icao] = cats
        change = describe(prev.get(icao, []), cats) if icao in prev else "new airport"
        total = sum(len(items) for _, items in cats)
        print("  %s: %d charts%s" % (icao, total, " (" + change + ")" if change else ""), file=sys.stderr)

    if not airports:
        sys.exit("no chart lists fetched — keeping the existing %s" % os.path.relpath(OUT))
    out = {
        "generated": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "source": "https://vatphil.com/charts",
        "airports": airports,
    }
    with open(OUT, "w") as f:
        json.dump(out, f, separators=(",", ":"), ensure_ascii=False)
    notes = ([", %d kept from last run" % len(kept)] if kept else []) + \
            ([", %d skipped" % len(skipped)] if skipped else [])
    print("wrote %s  (%d airports%s)" % (os.path.relpath(OUT), len(airports), "".join(notes)))


if __name__ == "__main__":
    main()
