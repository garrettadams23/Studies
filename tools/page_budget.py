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

## Why the byte ceiling moved from 1,100 KB to 2,200 KB, and then to 2,350

The gzip budget was set when it was assumed to be what hurt. For this site it
is not, and the reason is structural rather than a matter of taste:

    the download is paid once   — sw.js precaches the page, so a returning
                                  reader fetches nothing, and this is a
                                  reference people re-open rather than a
                                  landing page they see once
    the parse is paid always    — the browser still tokenises the whole file on
                                  every load, cache or no cache

So the number that was being enforced is the one that amortises away, and the
number that was not being enforced is the one paid on every visit.

The owner's call, explicitly: a slow first visit does not matter for this site.
That is the one cost of ignoring bytes — nobody else pays it, since Netlify's
free bandwidth allowance is ~23,000 visits a month even at four times this
size. So **raw_mb is now the binding budget and gzip_kb is a tripwire behind
it**: gzip_kb is set to whatever 8.0 MB of real content compresses to, so that
raw_mb always fails first and gzip_kb only fires if something goes wrong that
bytes see and raw size does not. It was 2,200 KB, from a 3.85x ratio; the ratio
has since drifted, and the section below is what that cost.

## Re-measured at 1,535 topics, and what the old table got wrong

This file used to carry a four-row table ending "linear, about 125 ms of load
per additional MB", and told the next person to re-measure without leaving them
anything to re-measure with. `tools/measure_load.mjs` is now that thing
(`make measure`). Three runs, this container, Chromium at 4x CPU throttle:

    mult   raw MB   domInteractive   load event   search   JS heap   indexed
     0x      0.4          416-531      461-561      2 ms     10 MB     1,535
     1x      7.7        1884-2005    2726-3027     33 ms     28 MB     1,535
     2x     14.9        3207-3467    4199-4400     34 ms     28 MB     1,535
     3x     22.2        3362-3691    4337-4735     35-41ms   28 MB     1,535

Unthrottled on the same container the 1x page loads in **629 ms**, so the 4x
throttle is doing what it is there for — standing in for a slow phone — and
none of these figures describes the machine anyone actually develops on.

**Three things in that table contradict the one it replaces.**

*The absolute figures do not transfer.* The old table says 1,164 ms at 8.1 MB;
the same procedure here says ~2,900 ms at 7.7 MB. Neither machine is wrong and
neither is a reader's phone. So a threshold written in milliseconds cannot be
checked anywhere but where it was set — see the revisit trigger below.

*Load is not linear in raw size, because most of it is not raw size.* Running
each variant twice, once with script.js stubbed out, splits the cost:

    mult   tokenise only   with script.js   script.js's share
     0x          533 ms           554 ms              21 ms
     1x        1,917 ms         3,126 ms           1,209 ms
     2x        3,308 ms         4,183 ms             875 ms
     3x        3,469 ms         4,390 ms             921 ms

**script.js's share is flat**: ~1 s whether the page carries one copy of the
library or three. That is the deferral working exactly as designed — it was
built so the load path never parses the content, and this is the measurement
that says so. What grows is the browser's own tokenising, ~190 ms per MB across
the first two steps (the 3x point came in below that line in the one run made,
which is not enough to call a ceiling).

So the load decomposes, on this machine, as **~0.5 s of shell + ~1.0 s of
script.js + ~190 ms per MB of content**. At today's 7.7 MB the fixed 1.5 s is
larger than the 1.4 s the content costs. **Trimming content cannot get below
that floor**, which is worth knowing before anyone proposes shrinking the
library to make the page fast.

*The search and heap columns were never measurable this way.* The duplication
multiplies the markup; it does not touch the id map build.py inlines as JSON,
which is what topicIndex() and therefore search read. Measured: `blocks` goes
30 -> 90 while `indexed` stays at 1,535. Search and heap are flat **by
construction**, so the old table's rising search and heap columns cannot be
reproduced by this model and nothing here bounds either. Sizing them needs a
different model — real extra topics, or a synthetic index.

### The revisit trigger, corrected

Session 19 set one: revisit lazy-loading when the throttled load passes ~3 s.
On this container today's page is already there, and on the machine that set the
line it would not be. **The trigger is unevaluable as written** — it is an
absolute number standing in for something relative, which is the same defect as
the gzip tripwire below and the absolute ceiling in `search_test.mjs`, now the
third instance.

What replaces it is a *shape* test, computable from a single `make measure` run
on whatever machine is to hand and therefore portable: **revisit when the
1x -> 2x load delta stops being smaller than the 0x -> 1x delta.** Today they
are 2.5 s and 1.3 s — decelerating hard, because the growing term is tokenising
and the fixed term is not. If doubling the content ever costs what the first
copy cost, something structural has changed (the likeliest being that the
deferral stopped deferring), and that is worth acting on wherever it is seen.

### The missing measurement, made — and it argues for the budget

The paragraph that used to sit here said raw_mb stayed at 8.0 because raising a
ceiling needs a positive argument, and the measurement that would supply one —
search and heap against a *real* index of N topics — was one the duplication
model could not make. `measure_load.mjs --synthetic` makes it: every domain is
cloned into `<id>__k` with its topic ids suffixed, across the shell, the
deferred blocks and the topic-index payload, so topicIndex() really returns N
times the topics.

    indexed   raw MB   load event   search (warm)   JS heap
      1,534      7.6      3,022 ms          36 ms     28 MB   <- today
      3,068     15.0      5,277 ms          53 ms     65 MB
      4,602     22.4      6,956 ms          86 ms     93 MB

**Search is not the constraint.** ~16 ms per additional 1,000 topics, and 86 ms
at three times the current site — still inside the band where a filter feels
immediate. The fear that full-text search would not survive growth, which §4b of
plan.md spent a section on, is measurably unfounded at this scale.

**Heap grows steadily** — about 20 MB per 1,000 topics, 93 MB at 3x. Worth
knowing, not alarming.

**Load is what grows.** 3.0 s to 7.0 s across the same range, and it is the
number a reader actually waits for. So the surprise is that **raw_mb, a size
budget, is aimed at the binding constraint after all** — not by design, but it
is. That is the positive argument this section asked for, and it argues for
keeping the budget rather than moving it.

If it is moved, the numbers to move it against are above: 16 MB buys ~2x the
content for ~5.3 s of throttled load, ~53 ms of search and 65 MB of heap. That
is a judgement about readers on slow devices, and it can now be made with the
curve in front of whoever makes it.

### It was moved, to 12.0 MB — the judgement, and why not 16

The owner made the call the paragraph above says is theirs: **raise it.** The
site was at 7.7 of 8.0 MB, about 63 more cards, and the measurement says the
things people feared — search and heap — are not what binds.

**12.0 and not 16.0**, for one reason that is not about readers. A budget has to
be reachable to be a budget. 16 MB is roughly 1,700 more topics: at the rate
this site actually grows, the ceiling would not fail for years, by which time
the measurement behind it, the machine it was taken on and quite possibly the
page's architecture are all different — and a ceiling that cannot fire is
decoration. 12.0 MB is ~900 topics of headroom, which is a lot of room and still
a number a wave could one day walk into.

What it costs, read off the curve above at ~305 ms per MB between the 7.6 and
15.0 MB points:

    raw            7.7 MB  ->  12.0 MB ceiling
    throttled load  3.0 s  ->  ~4.4 s at the ceiling  (~5.3 s at 16 MB)
    search           36 ms ->  ~45 ms                 (~53 ms at 16 MB)
    heap             28 MB ->  ~48 MB                 (~65 MB at 16 MB)
    headroom      63 cards ->  ~900 cards

**16.0 MB stays the next stop and it is already priced**, so raising it again is
a decision rather than a re-derivation. The line that has to move with it is the
one below.

*And the ratio drifted again*, exactly as the tripwire section predicted it
would: 3.85x when first set, 3.672x at 1,535 topics, **3.628x today**. gzip_kb
is therefore re-derived rather than scaled — 12.0 MB at 3.628x is 3,387 KB, and
the budget is 3,550 KB so that raw_mb still fails about 5% first.

### The tripwire had got in front of the wall

3.85x held when it was measured. At 1,535 topics the page compresses at
**3.672x**. Why it drifted is not measured here and does not need to be — the
point is that it *can* drift, so a ceiling derived from it once and then carried
forward stops being what it says it is. That small drift put the arrangement the
wrong way round:

    gzip_kb 2,200 KB  ->  trips at 7.89 MB raw
    raw_mb  8.00 MB   ->  trips at 8.00 MB raw

So the tripwire would have fired first, and its failure message would have sent
the next person to shrink *bytes* — the one cost this file spends four
paragraphs explaining does not matter for this site. Measured headroom at the
time: raw 8%, gzip 7%. It was about a hundred cards from firing.

gzip_kb is now 2,350 KB: 8.0 MB at the measured 3.672x is 2,231 KB, plus room
for the ratio to drift further as content changes shape. raw_mb still fails
first, by about 5%, which is what "a tripwire behind it" has to mean. **Derive
this from a measurement whenever raw_mb moves; do not carry the old ratio.**

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
    "raw_mb": 12.0,               # the real ceiling — the owner's call, priced above, not derived from load time
    "gzip_kb": 3_550,             # 12.0 MB at the measured 3.628x, plus drift room — re-derive when raw_mb moves
    "dom_elements": 1_500,        # built at load: shell + one header per domain. ~70 domains of room
    "content_elements": 262_500,  # the deferred library at the raw_mb ceiling, at 80 elements/topic
}

# Topics, so the report can turn "7% left" into "room for ~139 more cards".
# dom_elements is deliberately excluded: it grows per *domain*, not per topic,
# so a runway in topics would be meaningless for it.
PER_TOPIC = ("raw_mb", "gzip_kb", "content_elements")
TOPIC_RE = re.compile(r'<div class="topic"')

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
    }, len(TOPIC_RE.findall(text))


def main():
    if not PAGE.exists():
        print("error: index.html not found — run python build.py first", file=sys.stderr)
        return 1

    m, topics = measure()
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

    # A percentage does not tell anybody whether the next wave fits. Topics do.
    runway = min(((BUDGET[k] - m[k]) / (m[k] / topics), k) for k in PER_TOPIC)
    print(f"\n{topics:,} topics today. Room for ~{runway[0]:,.0f} more at the current "
          f"average before {runway[1]} binds.")

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
