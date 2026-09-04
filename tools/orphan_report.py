#!/usr/bin/env python3
"""
orphan_report.py — good cards that nothing links to.

plan.md Phase 10 T4. 902 of 1,432 topics carried no related-topic link when this
was written. That is not automatically wrong: `data/related.json` is hand-built
and hand-built things are partial. The interesting subset is narrower and much
more actionable.

**159 topics with three or more concept cards and over 3,000 plain characters had
no links in or out.** Those are not thin cards nobody bothered with — they are
some of the best writing on the site, reachable only by browsing to the domain
and scrolling. The `productivity` domain was almost entirely in this state.

So the report ranks orphans by *depth*, and the work queue it produces reads
"good cards nobody can reach from anywhere else" rather than "topics missing
metadata". Cross-references (`<span class="xref">`) count as links here even
though they live in the prose rather than in `related.json`, because a reader
can follow them — a card reachable only by an xref is connected, just not
symmetrically.

Usage:
  python3 tools/orphan_report.py              # deep orphans, deepest first
  python3 tools/orphan_report.py --all        # every unlinked topic
  python3 tools/orphan_report.py --domain productivity
"""

import collections
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"

DEEP_CARDS = 3
DEEP_CHARS = 3000

TAG_RE = re.compile(r"<[^>]+>")
# Order-independent on purpose. The first version required `id` immediately
# after `class="topic"`, and a later build change that stamped `data-read` and
# `data-level` into the same tag pushed `id` rightwards — this tool then found
# no topics at all and printed "0 of 0", which reads exactly like a clean
# result. See the zero-topic guard in main().
TOPIC_RE = re.compile(r'<div class="topic"[^>]*?\sid="([^"]+)"')
DOMAIN_RE = re.compile(
    r'<script type="text/html" class="domain-src" data-domain="([^"]+)">(.*?)</script\s*>', re.S)


def built_topics():
    """(id, domain, plain_chars, concept_cards) from the built page.

    Read from `index.html` rather than from `data/*.html` because ids are stamped
    at build time — the source files do not carry them.
    """
    page = (ROOT / "index.html").read_text(encoding="utf-8")
    for dom in DOMAIN_RE.finditer(page):
        did, body = dom.group(1), dom.group(2)
        starts = [(m.start(), m.group(1)) for m in TOPIC_RE.finditer(body)]
        for n, (start, tid) in enumerate(starts):
            end = starts[n + 1][0] if n + 1 < len(starts) else len(body)
            block = body[start:end]
            yield (tid, did, len(TAG_RE.sub("", block)),
                   len(re.findall(r'class="concept-card"', block)))


def linked_ids():
    """Every id reachable by a related-topic pair or a resolved cross-reference."""
    rel = json.loads((DATA / "related.json").read_text(encoding="utf-8"))
    ids = set(rel) | {t for v in rel.values() for t in v}
    page = (ROOT / "index.html").read_text(encoding="utf-8")
    ids |= set(re.findall(r'data-xref="([^"]+)"', page))
    return ids


def main():
    args = sys.argv[1:]
    only = args[args.index("--domain") + 1] if "--domain" in args else None
    show_all = "--all" in args

    linked = linked_ids()
    rows, total, orphans = [], 0, 0
    by_domain = collections.Counter()
    parsed = list(built_topics())
    # A census that finds nothing on a 1,400-topic site is broken, not clean.
    # This tool once printed "0 of 0 topics have no related link" for two weeks
    # because a build change moved an attribute, and the line reads like good
    # news. Fail loudly instead.
    if not parsed:
        raise SystemExit(
            "error: parsed 0 topics from index.html — the topic regex no longer "
            "matches the built markup. Run 'python build.py' first; if the page "
            "is current, this tool needs updating, not the page.")
    for tid, did, chars, cards in parsed:
        if only and did != only:
            continue
        total += 1
        if tid in linked:
            continue
        orphans += 1
        by_domain[did] += 1
        deep = cards >= DEEP_CARDS and chars >= DEEP_CHARS
        if deep or show_all:
            rows.append((cards, chars, did, tid))

    rows.sort(reverse=True)
    for cards, chars, did, tid in rows:
        print(f"  {cards} cards {chars:>6} chars  [{did}] {tid[:56]}")

    scope = f" in {only}" if only else ""
    print(f"\n{orphans:,} of {total:,} topics{scope} have no related link and no "
          f"cross-reference pointing at them.")
    # Where they are, because the headline number is meaningless without it.
    # Today all 60 are the generated acronym dictionary's A-Z and By-Area index
    # pages, where a see-also strip would point at nothing — and a reader of the
    # bare count has to work that out by hand every time. The same 60 are the
    # whole of the gap in `suggest_related.py --check` and in `check_paths.py`,
    # so three reports were each re-deriving the same exclusion in the reader's
    # head. One line here says it once.
    if by_domain:
        print("  " + " · ".join(f"{d} {n}" for d, n in by_domain.most_common(8))
              + (" · …" if len(by_domain) > 8 else ""))
    if not show_all:
        print(f"{len(rows)} of those are deep ({DEEP_CARDS}+ concept cards, "
              f"{DEEP_CHARS:,}+ chars) — good cards that are dead ends.")
        print("Run with --all for the rest. A census, not a gate.")
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
