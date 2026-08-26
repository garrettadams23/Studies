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


def topics(domain):
    """(title, plain_chars, concept_cards) for every topic in one domain."""
    text = "".join(p.read_text(encoding="utf-8") for p in domain_files(domain))
    starts = [m.start() for m in TOPIC_RE.finditer(text)]
    for n, start in enumerate(starts):
        end = starts[n + 1] if n + 1 < len(starts) else len(text)
        block = text[start:end]
        name = NAME_RE.search(block)
        title = re.sub(r"\s+", " ", TAG_RE.sub("", name.group(1))).strip() if name else "?"
        yield title, len(TAG_RE.sub("", block)), len(re.findall(r'class="concept-card"', block))


def main():
    args = sys.argv[1:]
    only = None
    if "--domain" in args:
        only = args[args.index("--domain") + 1]

    rows, thin_rows, lengths = [], [], []
    total = thin = chars = cards = 0
    for dom in json.loads((DATA / "domains.json").read_text(encoding="utf-8")):
        did = dom["id"]
        if only and did != only:
            continue
        n = t = 0
        for title, length, cc in topics(did):
            total += 1
            n += 1
            chars += length
            cards += cc
            if did not in REFERENCE_DOMAINS:
                lengths.append(length)
            if cc <= 1 and length < THIN_CHARS and did not in REFERENCE_DOMAINS:
                thin += 1
                t += 1
                thin_rows.append((length, did, title))
        if n:
            rows.append((round(100 * t / n), t, n, did))

    if "--thin" in args:
        thin_rows.sort()
        for length, did, title in thin_rows:
            print(f"{length:>6}  {did:<12} {title[:62]}")
        print(f"\n{len(thin_rows)} thin topic(s).")
        return 0

    if only:
        for title, length, cc in sorted(topics(only), key=lambda r: r[1]):
            mark = "thin" if cc <= 1 and length < THIN_CHARS else "    "
            print(f"{mark} {length:>6} chars  {cc} card(s)  {title[:56]}")
        return 0

    rows.sort(reverse=True)
    print(f"{total:,} topics · {thin} single-concept and under {THIN_CHARS:,} plain "
          f"chars ({round(100 * thin / total)}%)")
    print(f"mean chars per concept card: {round(chars / max(cards, 1)):,}   "
          f"← the padding counter-metric: it must not rise")
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
