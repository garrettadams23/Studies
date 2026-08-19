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
                       that. 92,330 -> 404 measured at 1,080 topics.
    content_elements   what sits in the deferred blocks: the whole library,
                       parsed as text and built only on demand. This is the
                       number a content wave moves, and the one that used to be
                       "elements".

## Why the byte ceiling moved from 1,100 KB to 2,200 KB

The gzip budget was set when it was assumed to be what hurt. For this site it
is not, and the reason is structural rather than a matter of taste:

    the download is paid once   — sw.js precaches the page, so a returning
                                  reader fetches nothing, and this is a
                                  reference people re-open rather than a
                                  landing page they see once
    the parse is paid always    — the browser still tokenises the whole file on
                                  every load, cache or no cache

So the number that was being enforced is the one that amortises away, and the
number that was not being enforced is the one paid on every visit. Measured by
duplicating the deferred blocks (the load path never parses them, so this
models "the same page with N times the cards"), Chromium at 4x CPU throttle:

    raw size    ~topics   load event   search (warm)   JS heap
     4.1 MB      1,080       768 ms          57 ms      14 MB   <- today
     8.1 MB      2,150     1,164 ms          97 ms      26 MB
    12.2 MB      3,230     1,822 ms         147 ms      40 MB
    16.3 MB      4,300     2,298 ms         179 ms      69 MB

Linear, about 125 ms of load per additional MB. The 3-second throttled-load
line session 19 set as its revisit trigger is not reached until roughly 22 MB.

The owner's call, explicitly: a slow first visit does not matter for this site.
That is the one cost of ignoring bytes — nobody else pays it, since Netlify's
free bandwidth allowance is ~23,000 visits a month even at four times this
size. So **raw_mb is now the binding budget and gzip_kb is a tripwire behind
it**: 2,200 KB is what 8.0 MB of real content compresses to at the measured
3.85x ratio, which means raw_mb always fails first and gzip_kb only fires if
something goes wrong that bytes see and raw size does not.

raw_mb is set to 8.0 because a budget that will actually be reached is worth
more than one that will not: it is ~1,000 more cards, and ~1.2 s of throttled
load when it lands. Re-measure there rather than assuming this table still
holds.

## One cost this file does not yet bound

Only one domain renders, so the worst *interaction* is opening the largest one,
and nothing here measures that. Today, at 4x throttle:

    acronym   16,511 content elements   127 ms to open
    script    13,729                    196 ms
    median domain  2,220                 ~35 ms

A domain three times the size of `script` would be a visibly slow open and
would pass every budget below. If that becomes a real risk, the metric to add
is the largest single domain's element count, not another page-wide total.

    python tools/page_budget.py            report and enforce
    python tools/page_budget.py --report   report only, never fail
"""

import gzip
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PAGE = ROOT / "index.html"

# Set from the measurements in the docstring, not from headroom over today's
# values. raw_mb is the one meant to bind; the other three sit behind it so that
# whichever fails, it is the one a content wave actually moves.
BUDGET = {
    "raw_mb": 8.0,                # ~1.2 s throttled load, ~2,150 topics. The real ceiling.
    "gzip_kb": 2_200,             # what 8.0 MB compresses to at 3.85x — a tripwire, not a wall
    "dom_elements": 1_500,        # built at load: shell + one header per domain. ~70 domains of room
    "content_elements": 175_000,  # the deferred library at the raw_mb ceiling, at 80 elements/topic
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
              "commit, with a fresh measurement replacing the table in this file's\n"
              "docstring — or this is the moment to make the page smaller.", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
