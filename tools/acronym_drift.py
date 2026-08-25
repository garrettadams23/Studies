#!/usr/bin/env python3
"""
acronym_drift.py — capitalised tokens in the content that the dictionary has
never heard of, as a work queue for data/acronyms.json.

The dictionary is the backbone of three features: the inline expansions the
annotator injects, the acronym-aware search, and the acronym quiz. All three
only work for acronyms that are *in* it, and every content wave writes new ones.
Nothing was watching that gap. This counts it.

The report is a queue, not a gate. Plenty of what it lists should never be
added — a product name, a shouted word in a heading, a register name in a code
block — and a CI step that fails on new capitalised tokens would block every
content wave for a `TODO` in a snippet. It is meant to be read before a
dictionary wave, not to stop a build.

Nothing here gates CI, and that is a decision rather than an omission. The two
things this tool can measure — a capitalised token the dictionary lacks, and an
entry no card uses — are both legitimate in quantity. The first is full of
product names; the second is 173 entries as of writing, and the dictionary is
also a standalone reference domain and the quiz's question bank, so an entry
existing for its own sake is the point rather than a defect. A gate on either
would fail every content wave for reasons no one should act on.

What it excludes, and why each exclusion is here rather than in a stop list:

  * anything already in data/acronyms.json, in any casing
  * anything inside <pre>, <code> or an attribute — code and markup are full of
    capitals that are not acronyms, and counting them buries the real ones
  * the expansion the annotator writes, `ABC (Expanded Form)`, which would
    otherwise report every acronym the dictionary *does* know as a bare token
  * single letters, pure numbers, and Roman-numeral-looking tokens
  * the categorical labels — `.topic-badge`, `.concept-label` — which are
    shouted by design ("TERMS", "LIFESTYLE", "CORE") and are not prose
  * a plural of an entry the dictionary already has: APIs, VMs, URLs
  * an ordinary English word being shouted in a heading — WHAT, WHY, FROM, KEY.
    There is no wordlist to consult, so the content supplies one: a token whose
    lowercase form appears often in the site's own lowercase prose is a word,
    not an acronym. It costs nothing, needs no data file, and adapts as the
    writing does.

Usage:
  python3 tools/acronym_drift.py                # the queue, most frequent first
  python3 tools/acronym_drift.py --top 40
  python3 tools/acronym_drift.py --domain sec
  python3 tools/acronym_drift.py --unused       # entries no card outside the acronym domain uses
"""

import collections
import json
import re
import sys
from html import unescape
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from lint_content import domain_files  # noqa: E402

ROOT = Path(__file__).parent.parent
DATA = ROOT / "data"

PRE_RE = re.compile(r"<(pre|code)\b.*?</\1>", re.S | re.I)
LABEL_RE = re.compile(
    r'<span class="topic-badge">.*?</span\s*>|<div class="concept-label">.*?</div\s*>', re.S)
TAG_RE = re.compile(r"<[^>]+>")
ACRO_EXP_RE = re.compile(r'<span class="acro-exp">\([^<]*?\)</span\s*>')
# Two or more capitals, allowing digits and a trailing lowercase 's' or 'e'
# (IPs, VLANs, 10GbE) — the shapes the dictionary itself already uses.
#
# The first two branches exist because an ampersand is not a word character, so
# a single `\b…\b` token split `ATT&CK` — which the dictionary knows — into
# `ATT` and `CK`, and reported both as unknown 39 times each, at positions 7
# and 8 of the drift list. Only an ampersand with no spaces around it joins a
# token: "Backup &amp; Recovery" stays two words, because the spaces stop the
# first branch and its first word has one capital.
TOKEN_RE = re.compile(
    r"\b[A-Z][A-Za-z0-9]*[A-Z0-9][A-Za-z0-9]*&[A-Z][A-Za-z0-9]*\b"   # ATT&CK
    r"|\b[A-Z]&[A-Z]\b"                                              # M&A, R&D
    r"|\b[A-Z][A-Za-z0-9]*[A-Z0-9][A-Za-z0-9]*\b")

# Words that are all-capitals in prose without being acronyms. Short on purpose:
# anything longer is a sign the exclusions above are not doing their job.
NOT_ACRONYMS = {
    "AND", "BUT", "FOR", "NOT", "THE", "YOU", "ALL", "ANY", "NEW", "OLD",
    "YES", "NO", "OK", "TODO", "NOTE", "WARNING", "IMPORTANT",
    "I", "II", "III", "IV", "VI", "VII", "VIII", "IX", "XI", "XII",
}


def known():
    """Every acronym the dictionary carries, upper-cased for comparison."""
    entries = json.loads((DATA / "acronyms.json").read_text(encoding="utf-8"))["entries"]
    return {e["a"].upper() for e in entries}, entries


def prose(text):
    """A file's readable text: no code blocks, no markup, no injected expansions."""
    text = PRE_RE.sub(" ", text)
    text = LABEL_RE.sub(" ", text)
    text = ACRO_EXP_RE.sub(" ", text)
    return unescape(TAG_RE.sub(" ", text))


WORD_RE = re.compile(r"\b[a-z]{2,}\b")
# How often a lowercase form has to appear before an upper-case sighting of it
# is read as shouting rather than as an acronym. Twenty is enough to clear
# "what", "from" and "key" while leaving genuinely rare words alone.
WORD_FLOOR = 20


def common_words(texts):
    counts = collections.Counter()
    for t in texts:
        counts.update(WORD_RE.findall(t))
    return {w for w, c in counts.items() if c >= WORD_FLOOR}


def scan(only_domain=None):
    seen = collections.Counter()
    where = collections.defaultdict(set)
    used = set()
    vocab, _ = known()
    domains = [d["id"] for d in json.loads((DATA / "domains.json").read_text(encoding="utf-8"))]
    texts = {}
    for domain in domains:
        paths = domain_files(domain)
        if paths:
            texts[domain] = prose("".join(p.read_text(encoding="utf-8") for p in paths))
    # The word list comes from the whole site even when the report is narrowed
    # to one domain: what counts as an ordinary word does not change per domain.
    words = common_words(texts.values())

    for domain, text in texts.items():
        if only_domain and domain != only_domain:
            continue
        for token in TOKEN_RE.findall(text):
            up = token.upper()
            if up in vocab:
                used.add(up)
                continue
            # A plural of something the dictionary knows is not drift.
            if up.endswith("S") and up[:-1] in vocab:
                used.add(up[:-1])
                continue
            if up in NOT_ACRONYMS or len(token) < 2 or token.isdigit():
                continue
            if token.isupper() and token.lower() in words:
                continue
            seen[token] += 1
            where[token].add(domain)
    return seen, where, used


def check_unused():
    """Dictionary entries no card outside the generated acronym domain uses.

    Searched as literal strings rather than through the tokenizer, because a
    third of the dictionary does not tokenize: "TCP/IP", "SOC 2", "TACACS+" and
    "TL;DR" all carry characters a word-boundary regex will not match, and a
    check that reported them as unused would be reporting on its own regex.

    data/acronym.html is excluded: it is generated *from* the dictionary, so
    every entry appears there by construction and it cannot be evidence of use.
    """
    vocab, entries = known()
    corpus = []
    for path in sorted(DATA.glob("*.html")):
        if path.name == "acronym.html":
            continue
        corpus.append(prose(path.read_text(encoding="utf-8")).upper())
    blob = " ".join(corpus)
    unused = sorted(a for a in vocab if a not in blob)
    for a in unused:
        print(f"unused: {a}")
    print(f"\n{len(vocab)} entries, {len(unused)} used by no card outside "
          f"the generated acronym domain.")
    # Always zero: see the module docstring. An entry that exists only in the
    # dictionary is serving the reference domain and the quiz, not rotting.
    return 0


def main():
    args = sys.argv[1:]
    only_domain = args[args.index("--domain") + 1] if "--domain" in args else None
    top = int(args[args.index("--top") + 1]) if "--top" in args else 60

    seen, where, used = scan(only_domain)

    if "--unused" in args:
        return check_unused()

    rows = seen.most_common(top)
    if not rows:
        print("No unknown capitalised tokens found.")
        return 0
    width = max(len(t) for t, _ in rows)
    print(f"{'token':<{width}}  count  domains")
    for token, count in rows:
        doms = ", ".join(sorted(where[token])[:4])
        extra = "" if len(where[token]) <= 4 else f" +{len(where[token]) - 4}"
        print(f"{token:<{width}}  {count:5}  {doms}{extra}")
    total = len(seen)
    print(f"\n{total} unknown token(s); {sum(seen.values())} occurrence(s). "
          f"{len(used)} dictionary entries are in use.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
