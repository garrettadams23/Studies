#!/usr/bin/env python3
"""A performance budget for index.html, so "the page is getting big" stops being
a feeling and starts being a number CI can fail on.

The risk register carried "3.2 MB and grows with every wave" for months without
anyone timing a load. Measured, on this build:

    over the wire   836 KB gzipped (24% of raw) — what a visitor actually waits for
    elements        78,819
    first paint     160 ms desktop · 336 ms on a phone at 4x CPU throttle
    chip filter     28 ms desktop · 50 ms phone
    load event      308 ms desktop · 1,284 ms phone

So the page is not slow today, and a lazy-loading rewrite would be optimising
against a number nobody had looked at. What it *is* is unbounded — every wave
adds to it and nothing pushes back. This script is the thing that pushes back.

The budgets sit roughly 25% above today's values: a normal content wave passes,
a doubling does not. When one is hit, that is the moment to have the
lazy-loading conversation — with a measurement in hand.

    python tools/page_budget.py            report and enforce
    python tools/page_budget.py --report   report only, never fail
"""

import gzip
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PAGE = ROOT / "index.html"

BUDGET = {
    "gzip_kb": 1100,      # what the visitor downloads; Netlify serves compressed
    "raw_mb": 4.2,        # what the browser parses
    "elements": 93_000,   # static markup; the live DOM runs ~4,400 higher
}

# Counts opening tags only: not closing tags, not comments, not doctype.
#
# This measures the *static* markup: 74,464 against the 75,063 a browser reports
# with script.js stubbed out, a 0.8% undercount from tags inside inline SVG
# attributes and the like. The live page carries about 4,400 more (78,819),
# injected at runtime — chiefly the four-element tool cluster script.js adds to
# each of 915 topics. The budget is on the static number because that is what a
# content wave changes and what CI can measure without a browser.
TAG_RE = re.compile(r"<(?!/|!)([a-zA-Z][a-zA-Z0-9-]*)")
VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link",
        "meta", "param", "source", "track", "wbr"}


def measure():
    raw = PAGE.read_bytes()
    text = raw.decode("utf-8")
    # A <script type="application/json"> block is data, not markup — anything
    # angle-bracketed inside it would otherwise be counted as elements.
    body = re.sub(r"<script[^>]*type=\"application/json\"[^>]*>.*?</script>", "",
                  text, flags=re.S)
    return {
        "gzip_kb": len(gzip.compress(raw, 9)) / 1024,
        "raw_mb": len(raw) / 1024 / 1024,
        "elements": len(TAG_RE.findall(body)),
    }


def main():
    if not PAGE.exists():
        print("error: index.html not found — run python build.py first", file=sys.stderr)
        return 1

    m = measure()
    report_only = "--report" in sys.argv
    over = []
    print(f"{'metric':<12} {'now':>10} {'budget':>10}   headroom")
    for key, budget in BUDGET.items():
        now = m[key]
        pct = now / budget * 100
        fmt = "{:>10,.0f}" if key == "elements" else "{:>10,.1f}"
        print(f"{key:<12} {fmt.format(now)} {fmt.format(budget)}   {100 - pct:>5.0f}% left"
              + ("  ** OVER **" if now > budget else ""))
        if now > budget:
            over.append(f"{key}: {now:,.1f} exceeds the budget of {budget:,.1f}")

    if over and not report_only:
        print(file=sys.stderr)
        for line in over:
            print(f"error: {line}", file=sys.stderr)
        print("\nThe page grew past its budget. Either the growth is worth it and the\n"
              "budget in tools/page_budget.py should move — deliberately, in its own\n"
              "commit — or this is the moment to make the page smaller.", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
