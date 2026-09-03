#!/usr/bin/env python3
"""
depth_report.py — how deep the cards are, and whether a deepening pass is real.

plan.md Phase 8 rests entirely on one measurement that previously existed only
inside that document. A number stated in a plan and not produced by a committed
script is a claim with a shelf life, so this is the script.

Two numbers, and the second one is the point:

  * **thin count** — topics with a single `.concept-card` and under 1,800 plain
    characters. **288 of 1,432 (20%)** when this was written — plan.md Phase 8
    quotes 330, which is the same population before the two reference domains
    below are excluded. Concentrated entirely in domains authored before the
    current card form settled: `data` 93% thin, `web` 85%, `redteam` 77%, while
    `cs`, `infra`, `hw`, `m365` and `math` are 0%.

  * **mean characters per concept card** — the counter-metric. Phase 8's first
    failure mode is padding: words added, nothing said. Padding lowers the thin
    count *and* raises this number, so reporting only the first would reward the
    exact failure the plan warns about.

Reference domains are excluded from the thin count, not from the totals:
`shortcut` is scannable by design and `acronym` is generated, so a short card in
either is correct rather than debt. See plan.md Phase 8 §4.

Usage:
  python3 tools/depth_report.py                 # the census
  python3 tools/depth_report.py --domain data   # one domain, topic by topic
  python3 tools/depth_report.py --thin          # just the thin topics, worst first
"""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
sys.path.insert(0, str(ROOT / "tools"))
from lint_content import domain_files  # noqa: E402

THIN_CHARS = 1800
REFERENCE_DOMAINS = {"shortcut", "acronym"}

TOPIC_RE = re.compile(r'<div class="topic"')
TAG_RE = re.compile(r"<[^>]+>")
NAME_RE = re.compile(r'class="topic-name"[^>]*>(.*?)</span>\s*(?:<span class="topic-badge|</div>)', re.S)
BADGE_RE = re.compile(r'class="topic-badge">(.*?)</span>', re.S)

# The closing judgement after a table. It is prose, so it counts in a card's
# characters, and the verdict programme therefore moved the padding metric from
# 1,281 to 1,368 — a 7% rise, in a number this file prints with the words "it
# must not rise" beside it.
#
# Measured, rather than argued about. Excluding verdicts, the same corpus reads
# **1,106 before the programme and 1,108 after**: body prose per card did not
# move at all, while 360,667 characters of closing judgement were added. So the
# rise was entirely the thing the programme set out to add.
#
# The metric could not say that, because it mixed two populations — the prose a
# card is padded with, and the one sentence it is supposed to end on. Both
# numbers are printed now. The one to watch is the second.
VERDICT_RE = re.compile(
    r'<(?:div|p)\b[^>]*class="[^"]*\bconcept-desc verdict\b[^"]*"[^>]*>'
    r'.*?</(?:div|p)\s*>', re.S)

# Badge prefixes that mark a card as *deliberately* short. Wave D10 went looking
# for the shortest cards on the site and found these: the beginner layer, and
# per-certification objective summaries. Neither wants deepening — one would
# stop being a beginner card and the other would stop being a skim.
DELIBERATE = ("beginner", "linux+", "pentest+", "military", "mil ", "sec+", "net+",
              "a+", "security+", "reference", "all tracks")


def _deliberate(badge):
    b = badge.lower()
    return any(b.startswith(d) or f" {d}" in b for d in DELIBERATE)


def topics(domain, badges=False):
    """(title, plain_chars, concept_cards) for every topic in one domain."""
    text = "".join(p.read_text(encoding="utf-8") for p in domain_files(domain))
    starts = [m.start() for m in TOPIC_RE.finditer(text)]
    for n, start in enumerate(starts):
        end = starts[n + 1] if n + 1 < len(starts) else len(text)
        block = text[start:end]
        name = NAME_RE.search(block)
        title = re.sub(r"\s+", " ", TAG_RE.sub("", name.group(1))).strip() if name else "?"
        row = (title, len(TAG_RE.sub("", block)),
               len(re.findall(r'class="concept-card"', block)),
               len(TAG_RE.sub("", VERDICT_RE.sub("", block))))
        if not badges:
            yield row
            continue
        bg = BADGE_RE.search(block)
        yield row + (re.sub(r"\s+", " ", TAG_RE.sub("", bg.group(1))).strip() if bg else "-",)


def main():
    args = sys.argv[1:]
    only = None
    if "--domain" in args:
        only = args[args.index("--domain") + 1]

    rows, thin_rows, lengths = [], [], []
    total = thin = chars = cards = body_chars = 0
    for dom in json.loads((DATA / "domains.json").read_text(encoding="utf-8")):
        did = dom["id"]
        if only and did != only:
            continue
        n = t = 0
        for title, length, cc, body in topics(did):
            total += 1
            n += 1
            chars += length
            body_chars += body
            cards += cc
            if did not in REFERENCE_DOMAINS:
                lengths.append(length)
            if cc <= 1 and length < THIN_CHARS and did not in REFERENCE_DOMAINS:
                thin += 1
                t += 1
                thin_rows.append((length, did, title))
        if n:
            rows.append((round(100 * t / n), t, n, did))

    if "--bottom" in args:
        # The bottom of the site by length, regardless of concept-card count.
        # `--thin` answers "which cards are one card and short"; this answers
        # "which cards are shortest", and wave D10 exists because those are not
        # the same list — nine waves moved the 10th percentile by three
        # characters while the thin count fell by 77.
        n = int(args[args.index("--bottom") + 1]) if len(args) > args.index("--bottom") + 1 \
            and args[args.index("--bottom") + 1].isdigit() else 20
        every = []
        for dom in json.loads((DATA / "domains.json").read_text(encoding="utf-8")):
            did = dom["id"]
            if did in REFERENCE_DOMAINS or (only and did != only):
                continue
            for title, length, cc, _body, badge in topics(did, badges=True):
                every.append((length, cc, did, title, badge))
        every.sort()
        for length, cc, did, title, badge in every[:n]:
            mark = "·" if _deliberate(badge) else " "
            print(f"{length:>6} {mark} {cc} card(s)  {did:<10} {title[:42]:<44} [{badge[:22]}]")
        cut = every[len(every) // 10][0]
        decile = every[:max(len(every) // 10, 1)]
        marked = sum(1 for r in decile if _deliberate(r[4]))
        print(f"\n{n} shortest of {len(every):,} non-reference topics. "
              f"10th percentile is {cut:,} chars.")
        print(f"{marked} of the {len(decile)} in the bottom decile carry a badge that means "
              f"deliberately short (·)\n  — the beginner layer and the per-certification "
              f"objective skims. Deepening those is not the win it looks like.")
        return 0

    if "--thin" in args:
        thin_rows.sort()
        for length, did, title in thin_rows:
            print(f"{length:>6}  {did:<12} {title[:62]}")
        print(f"\n{len(thin_rows)} thin topic(s).")
        return 0

    if only:
        for title, length, cc, _body in sorted(topics(only), key=lambda r: r[1]):
            mark = "thin" if cc <= 1 and length < THIN_CHARS else "    "
            print(f"{mark} {length:>6} chars  {cc} card(s)  {title[:56]}")
        return 0

    rows.sort(reverse=True)
    print(f"{total:,} topics · {thin} single-concept and under {THIN_CHARS:,} plain "
          f"chars ({round(100 * thin / total)}%)")
    print(f"mean chars per concept card: {round(chars / max(cards, 1)):,}"
          f"  ({round(body_chars / max(cards, 1)):,} excluding verdicts)   "
          f"← the padding counter-metric: the second number must not rise")
    # The mean is not enough on its own, and Phase 8's closing record said so
    # before this line existed: seven waves each picked eight cards and nothing
    # forced them to be the eight hardest. A programme that only ever deepened
    # the easiest cards would leave the mean flat and the **median** flat too —
    # while a programme reaching the real tail moves the median up, because the
    # cards it lifts are the ones sitting below it.
    if lengths:
        lengths.sort()
        mid = len(lengths) // 2
        median = lengths[mid] if len(lengths) % 2 else (lengths[mid - 1] + lengths[mid]) // 2
        p10 = lengths[len(lengths) // 10]
        print(f"median topic: {median:,} plain chars · 10th percentile: {p10:,}   "
              f"← the tail: this is what a deepening wave has to move\n")
    else:
        print()
    print(f"{'domain':<13}{'thin':>6}{'topics':>8}{'thin %':>8}")
    for pct, t, n, did in rows:
        note = "  (reference — excluded)" if did in REFERENCE_DOMAINS else ""
        print(f"{did:<13}{t:>6}{n:>8}{pct:>7}%{note}")
    return 0


if __name__ == "__main__":
    # These are census tools people pipe into `head`. Without this, closing
    # the pipe raises BrokenPipeError out of print() and looks like a crash.
    try:
        import signal
        signal.signal(signal.SIGPIPE, signal.SIG_DFL)
    except (ImportError, AttributeError, ValueError):
        pass
    sys.exit(main())
