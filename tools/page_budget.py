#!/usr/bin/env python3
"""A performance budget for index.html, so "the page is getting big" stops being
a feeling and starts being a number CI can fail on.

The risk register carried "3.2 MB and grows with every wave" for months without
anyone timing a load. Re-measured in session 19, at 1,007 topics:

    over the wire   967 KB gzipped — what a visitor actually waits for
    elements        82,680 static markup · 87,489 live DOM
    load event      819 ms desktop · 1,615 ms on a phone at 4x CPU throttle
    chip filter      60 ms on that same throttled phone (median of 3)
    search           in the same range

**Measure interaction inside the page, not from the test driver.** A first pass
timed the chip filter by wrapping `page.click()` and got 677 ms, which looks
like a serious regression and is almost entirely Playwright's round trip. Timing
the same work with `performance.now()` in the page gives 60 ms. One of those
numbers would have justified a rewrite.

Since then the page ships one domain's content at a time (build.py's deferred
blocks), which changed what "elements" means and split this budget in two:

    dom_elements       what the browser builds at load — the shell and 29
                       domain headers, and at most one domain's content after
                       that. 92,330 -> 484 measured at 1,080 topics.
    content_elements   what sits in the deferred blocks: the whole library,
                       parsed as text and built only on demand. This is the
                       number a content wave moves, and the one that used to be
                       "elements".

Both still matter. The first is what a visitor pays on arrival; the second is
what they download either way, and it is why the byte budgets did not move.

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
    "gzip_kb": 1100,          # what the visitor downloads; Netlify serves compressed
    "raw_mb": 4.4,            # what the browser parses
    "dom_elements": 1_500,    # what it builds at load: shell + domain headers
    "content_elements": 100_000,  # the deferred library, built one domain at a time
}

# Counts opening tags only: not closing tags, not comments, not doctype.
#
# This measures the *static* markup: within about 1% of what a browser reports
# with script.js stubbed out, the gap being tags inside inline SVG attributes
# and the like. The live page carries more, injected at runtime — chiefly the
# four-element tool cluster script.js adds to each topic of the open domain.
TAG_RE = re.compile(r"<(?!/|!)([a-zA-Z][a-zA-Z0-9-]*)")
VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link",
        "meta", "param", "source", "track", "wbr"}

# The two <script> shapes that hold data rather than markup. A JSON payload was
# always excluded; a deferred domain block is excluded from the *DOM* count and
# counted on its own, because the browser builds none of it at load.
JSON_BLOCK_RE = re.compile(r"<script[^>]*type=\"application/json\"[^>]*>.*?</script\s*>", re.S)
DEFERRED_BLOCK_RE = re.compile(r"<script[^>]*class=\"domain-src\"[^>]*>(.*?)</script\s*>", re.S)


def measure():
    raw = PAGE.read_bytes()
    text = raw.decode("utf-8")
    deferred = DEFERRED_BLOCK_RE.findall(text)
    shell = JSON_BLOCK_RE.sub("", DEFERRED_BLOCK_RE.sub("", text))
    return {
        "gzip_kb": len(gzip.compress(raw, 9)) / 1024,
        "raw_mb": len(raw) / 1024 / 1024,
        "dom_elements": len(TAG_RE.findall(shell)),
        "content_elements": sum(len(TAG_RE.findall(d)) for d in deferred),
    }


def main():
    if not PAGE.exists():
        print("error: index.html not found — run python build.py first", file=sys.stderr)
        return 1

    m = measure()
    report_only = "--report" in sys.argv
    over = []
    print(f"{'metric':<17} {'now':>10} {'budget':>10}   headroom")
    for key, budget in BUDGET.items():
        now = m[key]
        pct = now / budget * 100
        fmt = "{:>10,.1f}" if key in ("gzip_kb", "raw_mb") else "{:>10,.0f}"
        print(f"{key:<17} {fmt.format(now)} {fmt.format(budget)}   {100 - pct:>5.0f}% left"
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
