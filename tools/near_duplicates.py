#!/usr/bin/env python3
"""
near_duplicates.py — topics that may already exist, before you write another one.

plan.md Phase 9. The audit method that governs new content — probe titles, verify
the zeros — has only ever been applied to the card being written *now*. Nothing
has looked backwards, so a session that covered a subject an earlier session had
already covered added a second card and the site kept both.

36 pairs shared 50% or more of their meaningful tokens when this was written.
Two `script` cards on regular expressions, two on Git, three Kubernetes cards
across two domains, three wireless cards in one. Several pairs differ only in
whether the title uses an em dash or an en dash, which dates them to different
sessions that could not see each other.

**This cannot be a gate.** Legitimate duplication exists and plan.md Phase 9 §3
enumerates it: a beginner card beside a deep one, a reference table beside a
concept card, and the same subject from an attacker's and a defender's side are
all deliberate. So it is a census, and the mode that matters is `--title`:

    python3 tools/near_duplicates.py --title "Spanning Tree — Why a Loop …"

run *before* writing, because by review time the cost is already sunk.

Every pair also carries what it **differs on**, in §3's terms — see
`differences()` for why that was missing and what it changes. Of 39 pairs, 29
differ on something §3 calls deliberate and 10 differ on nothing; those 10 are
§3's last row, "the real population", and `--unexplained` lists them alone.

Usage:
  python3 tools/near_duplicates.py                 # every pair at or above the floor
  python3 tools/near_duplicates.py --unexplained   # only the pairs §3 does not explain
  python3 tools/near_duplicates.py --title "…"     # does this card already exist?
  python3 tools/near_duplicates.py --floor 0.4     # widen it
"""

import itertools
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
sys.path.insert(0, str(ROOT / "tools"))
from lint_content import domain_files  # noqa: E402

FLOOR = 0.5
# Generated from the dictionary, so every entry duplicates a title by construction.
SKIP_DOMAINS = {"acronym"}

# Words that carry no subject. Deliberately short: a long stop list starts
# discarding real content words and the overlap scores drift upward.
STOP = set("""the a an of and or to in for on at by with from as is are was be been
that this these those it its your you what why how when where which who not no but
vs versus into over under about after before than then them they we our us do does
did done can could should would will actually really just only more most less least
one two three first every each all any some other another same different new old
good bad best worst practice practical guide intro introduction overview basics
fundamentals reference explained deep dive part""".split())

TAG_RE = re.compile(r"<[^>]+>")
ACRO_RE = re.compile(r'<span class="acro-exp">.*?</span\s*>', re.S)
NAME_RE = re.compile(r'class="topic-name"[^>]*>(.*?)</span>\s*(?:<span class="topic-badge|</div>)', re.S)
TOPIC_RE = re.compile(r'<div class="topic"')
BADGE_RE = re.compile(r'<span class="topic-badge">(.*?)</span>', re.S)


def _fold(word):
    """Crude singular. 'loops' and 'loop' are the same subject; 'class' is not
    a plural of 'clas', which is why the `ss` ending is left alone."""
    if len(word) > 3 and word.endswith("s") and not word.endswith("ss"):
        return word[:-1]
    return word


_ACRO_MAP = None


def _acronyms():
    """acronym -> its expansions' words, from the dictionary.

    An abbreviation and its expansion share no characters, so a token census
    cannot see that they are the same subject. `ADRs & Design Docs` and
    `Architecture Decision Records — …` scored **0.00** against each other, and
    the `--title` pre-flight said "clear to write" for a card the site already
    had. Expanding both sides before tokenising is the fix.
    """
    global _ACRO_MAP
    if _ACRO_MAP is None:
        _ACRO_MAP = {}
        try:
            entries = json.loads((DATA / "acronyms.json").read_text(encoding="utf-8"))["entries"]
        except (OSError, ValueError, KeyError):
            return _ACRO_MAP
        for e in entries:
            words = set()
            for m in e.get("m", []):
                words |= {w.lower() for w in re.findall(r"[A-Za-z0-9']+", m.get("e", ""))}
            key = re.sub(r"[^a-z0-9]", "", e["a"].lower())
            if key:
                _ACRO_MAP[key] = words
    return _ACRO_MAP


def tokens(title, expand=False):
    """The meaningful words in a title, lower-cased, expansions already gone.

    `expand=True` additionally pulls each acronym's dictionary meanings in, so
    an abbreviation and its written-out form overlap. **That is right for
    `--title` and wrong for the census**, and the measurement says so: turning
    it on everywhere took the pairwise count from 40 to 80, because any two
    titles sharing an acronym now also share every word of its expansions.

    So the census compares titles as written — a symmetric question where the
    extra tokens are almost all noise — and `--title` compares a candidate
    against them expanded, where a single missed match costs a duplicate card.
    Asymmetric tools for asymmetric questions.
    """
    title = re.sub(r"\(.*?\)", " ", title)
    raw = re.findall(r"[a-z0-9']+", title.lower())
    out = {_fold(w) for w in raw if w not in STOP and len(w) > 2}
    if expand:
        acro = _acronyms()
        for w in raw:
            for key in (w, _fold(w)):     # `ADRs` folds to `adr`; try both
                for e in acro.get(key, ()):
                    if e not in STOP and len(e) > 2:
                        out.add(_fold(e))
    return out


# plan.md Phase 9 §3 enumerates the duplication that is deliberate. Nothing has
# ever *shown* that enumeration next to the pairs, so the pairs §3 has already
# settled sit permanently at the top of this census and every session that runs
# it re-derives which ones are which.
#
# Worse, the stop list eats the words that record the decision. `fundamentals`
# and `reference` are both in STOP — correctly, for a subject measure — so
# *Kubernetes – Container Orchestration Fundamentals* and *Kubernetes —
# Container Orchestration Reference* tokenise identically and score **1.00**,
# the top of the list, on the strength of the two words that say they are a
# deliberate pair. The score is not wrong; it is answering "same subject?", and
# the answer is yes. What was missing is the second question.
#
# So each pair now carries what it *differs* on, stated as fact rather than as a
# verdict — the reader still opens both, which is §3's actual test. The pairs
# that differ on nothing are the population §3's last row calls "the real one",
# and `--unexplained` shows only those.

# Same rule as build.py's stamp_level(), and for the same reason: the badge is
# the only difficulty signal the markup carries. Kept in step by hand — if one
# moves, move the other.
_BEGINNER_RE = re.compile(r"\bbeginner\b", re.I)
_ADVANCED_RE = re.compile(r"\b(advanced|expert|deep)\b", re.I)
_REFERENCE_RE = re.compile(r"\breference\b", re.I)

# §3 row 3, encoded as §3 states it: two *domain pairings*, not a two-way split
# of the security domains. `pentest`↔`redteam` is methodology beside adversary
# tradecraft; `threat`↔`blueteam` is what the attacker does beside how you catch
# it. §3 says these pairings are "usually" the perspective case — usually, so it
# reports the pairing and leaves the judgement to whoever opens both.
PERSPECTIVE_PAIRS = {frozenset({"pentest", "redteam"}),
                     frozenset({"threat", "blueteam"})}

# A fourth class, which §3's table did not have and measurement supplied: the
# site keeps 37 **certification-objective** cards, badged with the exam rather
# than the subject. `depth_report.py` already knows about them — its DELIBERATE
# list exempts them from deepening, because a Linux+ objective summary that grew
# would stop being a skim. The same fact makes one of them beside a practitioner
# card deliberate rather than duplicated, and it explained two pairs that had
# nothing else to say for them. This is the CompTIA subset of that list; the rest
# of it (beginner, reference) is already covered by the two signals above.
CERT_BADGES = ("linux+", "pentest+", "sec+", "net+", "a+", "security+")


def level_of(badge):
    """beginner | advanced | core, from a topic's badge text."""
    if _BEGINNER_RE.search(badge):
        return "beginner"
    if _ADVANCED_RE.search(badge):
        return "advanced"
    return "core"


def _is_cert(badge):
    """True for a certification-objective badge. Matched the way depth_report's
    `_deliberate()` matches, so `Linux+ • IAM` and `DEVOPS · LINUX+` both count."""
    b = badge.lower()
    return any(b.startswith(c) or f" {c}" in b for c in CERT_BADGES)


def differences(a, b):
    """What a pair differs on, in §3's terms. Empty means §3 offers nothing.

    Deliberately factual. "level beginner/core" is something the markup says;
    "this pair is fine" is a judgement only reading both cards can make.
    """
    out = []
    if a["level"] != b["level"]:
        out.append(f'level {a["level"]}/{b["level"]}')
    if a["reference"] != b["reference"]:
        out.append("reference/concept")
    if frozenset({a["domain"], b["domain"]}) in PERSPECTIVE_PAIRS:
        out.append("attacker/defender view")
    if a["cert"] != b["cert"]:
        out.append("cert objective/practitioner")
    return out


def titles():
    """A record per hand-written topic: domain, title, and the §3 signals."""
    for dom in json.loads((DATA / "domains.json").read_text(encoding="utf-8")):
        did = dom["id"]
        if did in SKIP_DOMAINS:
            continue
        text = "".join(p.read_text(encoding="utf-8") for p in domain_files(did))
        starts = [m.start() for m in TOPIC_RE.finditer(text)]
        for n, start in enumerate(starts):
            end = starts[n + 1] if n + 1 < len(starts) else len(text)
            block = ACRO_RE.sub("", text[start:end])
            m = NAME_RE.search(block)
            if not m:
                continue
            title = re.sub(r"\s+", " ", TAG_RE.sub("", m.group(1))).strip()
            bm = BADGE_RE.search(block)
            badge = TAG_RE.sub("", bm.group(1)).strip() if bm else ""
            yield {
                "domain": did,
                "title": title,
                "level": level_of(badge),
                # §3 row 2. A card that calls itself a reference is looked up,
                # not read, and sits beside a concept card on purpose.
                "reference": bool(_REFERENCE_RE.search(title + " " + badge)),
                "cert": _is_cert(badge),
            }


def overlap(a, b):
    """Jaccard — symmetric, for comparing two existing titles."""
    return len(a & b) / len(a | b) if a and b else 0.0


def covered(want, have):
    """Containment — what share of a *candidate* title already exists.

    Jaccard is the wrong measure for `--title`, and getting this wrong was the
    first version of this tool: a short candidate against a long existing title
    scores low on Jaccard however completely the subject is covered. "Spanning
    Tree Protocol — Loops and Convergence" scored 0.25 against the site's own
    spanning-tree card and reported "clear to write".
    """
    return len(want & have) / len(want) if want else 0.0


def main():
    args = sys.argv[1:]
    floor = float(args[args.index("--floor") + 1]) if "--floor" in args else FLOOR
    only_unexplained = "--unexplained" in args
    rows = [(r, tokens(r["title"])) for r in titles()]

    if "--title" in args:
        # Both sides expanded — see tokens().
        want = tokens(args[args.index("--title") + 1], expand=True)
        hits = sorted(((covered(want, tokens(r["title"], expand=True)), r["domain"], r["title"])
                       for r, _ in rows), reverse=True)
        near = [h for h in hits if h[0] >= floor]
        for score, d, t in (near or hits[:5]):
            print(f"  {score:.2f}  [{d}] {t[:66]}")
        if near:
            print(f"\n{len(near)} existing topic(s) at or above {floor:.2f}. "
                  f"Read them before writing — plan.md Phase 9 §3 lists the "
                  f"duplication that is deliberate.")
            return 1
        print(f"\nNothing at or above {floor:.2f}; closest shown. Clear to write.")
        return 0

    pairs = []
    for (a, ka), (b, kb) in itertools.combinations(rows, 2):
        score = overlap(ka, kb)
        if score >= floor:
            pairs.append((score, a, b, differences(a, b)))
    pairs.sort(key=lambda p: (-p[0], p[1]["title"]))

    shown = 0
    for score, a, b, diff in pairs:
        if only_unexplained and diff:
            continue
        shown += 1
        print(f'  {score:.2f}  [{a["domain"]}] {a["title"][:60]}\n'
              f'        [{b["domain"]}] {b["title"][:60]}\n'
              f'        → {"; ".join(diff) if diff else "§3 offers nothing — read both"}')

    unexplained = sum(1 for _, _, _, d in pairs if not d)
    print(f"\n{len(pairs)} pair(s) at or above {floor:.2f}, across {len(rows):,} titles.")
    print(f"{len(pairs) - unexplained} differ on something §3 calls deliberate; "
          f"**{unexplained} differ on nothing** — `--unexplained` lists those alone.")
    print("A census, not a gate — see this file's docstring.")
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
