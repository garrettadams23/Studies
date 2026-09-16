#!/usr/bin/env python3
"""
check_acronyms.py — an acronym whose letters do not come from its expansion.

The session operating manual lists ten failures and the guard for each. Failure
#10 is the only one whose guard column says **nothing catches this**: two wrong
acronym expansions shipped in earlier sessions and were found by reading. This
is the check that was missing.

The signal is deliberately the narrow, decidable one. Two earlier heuristics in
this repository failed by being *plausible* — 635 hits for "a line that looks
like it ends mid-statement", 343 for "a two-space continuation" — and both
failed the same way: they described something that is usually true of a defect
instead of something that is impossible without one.

So the rule here is not "the initials should match the words", which is false of
a fifth of a real dictionary (`Antivirus` legitimately yields AV, `Demilitarized
Zone` yields DMZ). It is:

    **the acronym's letters must appear, in order, somewhere in its expansion**

An acronym is by construction a compression of the phrase it stands for. If its
letters are not even a subsequence of that phrase's letters, the pairing cannot
be a compression of it, and one of the two is wrong. That is a property of the
words, not a guess about house style, and on this dictionary it fires on 2.4% of
meanings rather than 21%.

Two readings are allowed, and a meaning passes if either does:

  * **literal** — letters only, case and punctuation discarded.
    `SFTP` ⊂ `SSH File Transfer Protocol`. `AV` ⊂ `Antivirus`.
  * **numeronym** — the number-words below first become digits, so `B2B` ⊂
    `Business to Business` and `4WD` ⊂ `Four Wheel Drive`. Nothing else is
    substituted: the reading has to stay decidable.

## What a failure means, and why it is not always a bug

A real dictionary contains genuine acronyms that are not compressions at all —
`a11y`, `XSS`, `UTC`, `RX`. Those are not errors to be fixed, they are facts
about how the name was formed, and a reader who wonders why accessibility is
spelled with an 11 in it deserves an answer.

So a violating meaning must carry an **`l` field** saying how the letters *are*
formed. It is not gate-only metadata: `gen_acronym_domain.py` renders it in the
dictionary beside the expansion, which is the reason to require it. A field that
only silences a check teaches people to write something they do not mean — see
`check_volatility.py`'s docstring on exactly that failure — and one that a
reader sees does not.

The check runs in both directions. An `l` on a meaning that *passes* is also an
error: it means the expansion was corrected at some point and the explanation of
the old one was left behind, which is how a file like this rots.

Usage:
  python3 tools/check_acronyms.py
  python3 tools/check_acronyms.py --list        # every explained meaning
  python3 tools/check_acronyms.py --self-test   # the rule, on fixtures
"""

import json
import re
import sys
from pathlib import Path

EXP_STOP = {"of", "and", "the", "for", "a", "an", "to", "in", "on", "over",
            "with", "as", "by", "at", "or"}


def initials(exp):
    """The letters an expansion's significant words contribute."""
    words = [w for w in re.split(r"[\s/&-]+", exp) if w and w.lower() not in EXP_STOP]
    return "".join(w[0] for w in words).upper()

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "data" / "acronyms.json"

# The only substitutions the numeronym reading makes. Cardinals up to ten, plus
# the two homophones that are actually written as digits in names — "to" in B2B
# and "for" in things like 4WD. Ordinals are deliberately absent: "Fourth
# Extended Filesystem" is EXT4 because 4 is a version suffix, not because
# "fourth" was spelled as a digit, and letting the reading cover it would hide
# the distinction the `l` field exists to record.
NUMERONYMS = {
    "zero": "0", "one": "1", "two": "2", "three": "3", "four": "4",
    "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9",
    "ten": "10", "to": "2", "too": "2", "for": "4", "fore": "4",
}
NUM_RE = re.compile(r"\b(" + "|".join(NUMERONYMS) + r")\b")


def letters(text):
    """Everything that can carry an acronym letter, lowercased."""
    return re.sub(r"[^a-z0-9]", "", text.lower())


def numeronym(text):
    """The same, with number-words spelled as digits first."""
    return letters(NUM_RE.sub(lambda m: NUMERONYMS[m.group(1)], text.lower()))


def is_subsequence(needle, haystack):
    it = iter(haystack)
    return all(c in it for c in needle)


def derives(acronym, expansion):
    """Can the acronym's letters be drawn, in order, from the expansion?"""
    key = letters(acronym)
    if not key:
        return True
    return is_subsequence(key, letters(expansion)) or is_subsequence(
        key, numeronym(expansion)
    )


# ── the fields that steer the annotator ─────────────────────────────────────
#
# `annotate` picks which meaning gets stamped into prose. `byDomain` overrides
# it per file, and a null there drops the acronym from that domain. A typo in
# either is the quietest possible defect: `annotate` falls through to `m[0]["e"]`
# and a misspelled domain key is simply never consulted, so the wrong expansion
# ships **site-wide** and the build stays green. That is failure #10's exact
# shape, arriving through the configuration rather than through the prose.
#
# All of these pass on the dictionary today. They are here so they keep passing,
# which is the same reason `check_css_vars.py` guards a count already at zero.
def same_meaning(a, b):
    """Are these two expansions the same claim written twice?

    Two shapes, both decidable, and the dictionary had one of each:

      * **Punctuation only.** ATT&CK carried *Adversarial Tactics, Techniques,
        and Common Knowledge* and *Adversarial Tactics, Techniques and Common
        Knowledge* as two meanings. An Oxford comma is not a second meaning, and
        the dictionary page listed both.
      * **One of them expands an acronym the other leaves short.** DPAPI carried
        *Data Protection Application Programming Interface* and *Data Protection
        API*. The differing tail's initials spell the short token, which is the
        definition of it being the same phrase.

    Anything subtler is a judgement and belongs to a reader, which is why this
    stops at two rules rather than reaching for a similarity score.
    """
    wa, wb = a.replace(",", " ").lower().split(), b.replace(",", " ").lower().split()
    if wa == wb:
        return True
    if len(wa) > len(wb):
        wa, wb = wb, wa
    # wa is the shorter. Walk the common head, then ask whether the rest of the
    # longer one is the expansion of the next word in the shorter one.
    i = 0
    while i < len(wa) and i < len(wb) and wa[i] == wb[i]:
        i += 1
    rest_short, rest_long = wa[i:], wb[i:]
    if len(rest_short) != 1 or len(rest_long) < 2:
        return False
    return initials(" ".join(rest_long)).lower() == rest_short[0].replace(".", "")


def structure(entries, domain_ids):
    """Problems in the fields that decide what the annotator writes."""
    problems = []
    seen = set()
    for e in entries:
        acro, meanings = e["a"], [m["e"] for m in e["m"]]
        for i, one in enumerate(meanings):
            for other in meanings[i + 1:]:
                if same_meaning(one, other):
                    problems.append(f"{acro}: {one!r} and {other!r} are the same "
                                    f"expansion written twice, and the dictionary "
                                    f"page lists both as meanings")
        if acro in seen:
            problems.append(f"{acro}: two entries with exactly this spelling. "
                            f"SOC/SoC and IOC/IoC differ by case on purpose; an "
                            f"exact duplicate is one entry too many")
        seen.add(acro)
        chosen = e.get("annotate")
        if chosen and chosen not in meanings:
            problems.append(f"{acro}: annotate is {chosen!r}, which is not one of this "
                            f"entry's meanings ({', '.join(meanings)}). The annotator "
                            f"falls through to {meanings[0]!r} and says nothing")
        if chosen and e.get("noAnnotate"):
            problems.append(f"{acro}: has both annotate={chosen!r} and noAnnotate. "
                            f"noAnnotate wins, so the annotate value is a comment "
                            f"wearing a setting's clothes")
        for dom, val in (e.get("byDomain") or {}).items():
            if dom not in domain_ids:
                problems.append(f"{acro}: byDomain names {dom!r}, which is not a domain "
                                f"on this site, so it is never consulted")
            if val is not None and val not in meanings:
                problems.append(f"{acro}: byDomain[{dom!r}] is {val!r}, which is not one "
                                f"of this entry's meanings ({', '.join(meanings)})")
    return problems


def scan(entries):
    """-> (unexplained, stale) — violations with no `l`, and `l` with no violation."""
    unexplained, stale = [], []
    for entry in entries:
        acronym = entry["a"]
        for meaning in entry["m"]:
            expansion = meaning["e"]
            ok = derives(acronym, expansion)
            has_l = bool(meaning.get("l", "").strip())
            if not ok and not has_l:
                unexplained.append((acronym, expansion))
            elif ok and has_l:
                stale.append((acronym, expansion, meaning["l"]))
    return unexplained, stale


# Fixtures. Each pair is (acronym, expansion, should_derive). The false ones are
# the shapes this check exists to catch; the true ones are the shapes an
# initials-matching check would have failed, and which is why it is not one.
FIXTURES = [
    ("SFTP", "SSH File Transfer Protocol", True),      # letters span three words
    ("AV", "Antivirus", True),                          # both letters, one word
    ("DMZ", "Demilitarized Zone", True),                # D and M inside one word
    ("AAA", "Authentication, Authorization, and Accounting", True),
    ("B2B", "Business to Business", True),              # numeronym reading
    ("HTTP", "HyperText Transfer Protocol", True),
    ("OTP", "One-Time Password", True),                 # 'one' must stay readable as letters
    ("QPS", "Queries Per Second", True),                # 'second' is not a numeronym
    ("CCM", "Configuration Manager Client", False),     # right words, wrong order
    ("NBT", "NetBIOS Name Service", False),             # the T has no source
    ("SSL", "Transport Layer Security", False),         # a different protocol entirely
    ("a11y", "Accessibility", False),                   # real, and needs explaining
]


STRUCTURE_FIXTURES = [
    ("a clean entry",
     [{"a": "X", "m": [{"e": "One"}, {"e": "Two"}], "annotate": "Two"}], 0),
    ("annotate naming a meaning the entry does not have",
     [{"a": "X", "m": [{"e": "One"}], "annotate": "Onee"}], 1),
    ("annotate and noAnnotate together",
     [{"a": "X", "m": [{"e": "One"}], "annotate": "One", "noAnnotate": True}], 1),
    ("byDomain naming a domain that does not exist",
     [{"a": "X", "m": [{"e": "One"}], "byDomain": {"nosuch": "One"}}], 1),
    ("byDomain naming a meaning the entry does not have",
     [{"a": "X", "m": [{"e": "One"}], "byDomain": {"net": "Other"}}], 1),
    ("a null byDomain is a deliberate do-not-annotate, not an error",
     [{"a": "X", "m": [{"e": "One"}], "byDomain": {"net": None}}], 0),
    ("two entries spelled exactly the same",
     [{"a": "X", "m": [{"e": "One"}]}, {"a": "X", "m": [{"e": "Two"}]}], 1),
    ("two entries differing only by case are the SOC/SoC convention",
     [{"a": "SOC", "m": [{"e": "One"}]}, {"a": "SoC", "m": [{"e": "Two"}]}], 0),
    ("one meaning twice, differing by an Oxford comma",
     [{"a": "X", "m": [{"e": "Tactics, Techniques, and Knowledge"},
                       {"e": "Tactics, Techniques and Knowledge"}]}], 1),
    ("one meaning twice, one of them leaving an acronym short",
     [{"a": "X", "m": [{"e": "Data Protection Application Programming Interface"},
                       {"e": "Data Protection API"}]}], 1),
    ("two genuinely different meanings are not a duplicate",
     [{"a": "X", "m": [{"e": "Auto Scaling Group"},
                       {"e": "Application Security Group"}]}], 0),
    ("a shared head does not make two meanings the same",
     [{"a": "X", "m": [{"e": "Data Protection Officer"},
                       {"e": "Data Protection Impact Assessment"}]}], 0),
]


def self_test():
    failures = []
    for acronym, expansion, expected in FIXTURES:
        got = derives(acronym, expansion)
        if got != expected:
            failures.append(f"  {acronym!r} / {expansion!r}: expected {expected}, got {got}")

    # The two-directional part of the rule, on synthetic entries.
    entries = [
        {"a": "XYZ", "m": [{"e": "Something Else Entirely"}]},
        {"a": "XYZ", "m": [{"e": "Something Else Entirely", "l": "a name, not an initialism"}]},
        {"a": "TLS", "m": [{"e": "Transport Layer Security", "l": "left over"}]},
        {"a": "TLS", "m": [{"e": "Transport Layer Security"}]},
    ]
    unexplained, stale = scan(entries)
    if len(unexplained) != 1:
        failures.append(f"  expected 1 unexplained violation, got {len(unexplained)}")
    if len(stale) != 1:
        failures.append(f"  expected 1 stale explanation, got {len(stale)}")
    if any(m.get("l") == "" for e in entries for m in e["m"]):
        failures.append("  fixture entries were mutated")

    if failures:
        print("check_acronyms self-test FAILED:")
        print("\n".join(failures))
        return 1
    for name, entries, want in STRUCTURE_FIXTURES:
        got = len(structure(entries, {"net", "sec"}))
        if got != want:
            print(f"check_acronyms self-test FAILED: {name} — expected {want}, got {got}")
            return 1
    print(f"check_acronyms self-test passed ({len(FIXTURES)} fixtures + both "
          f"directions + {len(STRUCTURE_FIXTURES)} structure fixtures).")
    return 0


def main():
    args = sys.argv[1:]
    if "--self-test" in args:
        return self_test()

    entries = json.loads(SRC.read_text(encoding="utf-8"))["entries"]
    total = sum(len(e["m"]) for e in entries)

    if "--list" in args:
        rows = [
            (e["a"], m["e"], m["l"])
            for e in entries for m in e["m"] if m.get("l")
        ]
        for acronym, expansion, why in sorted(rows):
            print(f"{acronym:<10} {expansion}\n{'':<10} {why}")
        print(f"\n{len(rows)} of {total} meanings explain their letters.")
        return 0

    domain_ids = {d["id"] for d in json.loads(
        (SRC.parent / "domains.json").read_text(encoding="utf-8"))}
    problems = structure(entries, domain_ids)
    for line in problems:
        print(f"ERROR {line}")

    unexplained, stale = scan(entries)
    for acronym, expansion in unexplained:
        print(f"{acronym}: '{expansion}' — the letters are not drawn from the expansion,")
        print(f"{'':<{len(acronym) + 2}}and no 'l' field says how they are formed.")
    for acronym, expansion, why in stale:
        print(f"{acronym}: '{expansion}' derives cleanly, so the 'l' field is stale:")
        print(f"{'':<{len(acronym) + 2}}{why!r}")

    explained = sum(1 for e in entries for m in e["m"] if m.get("l"))
    steered = sum(1 for e in entries if e.get("annotate") or e.get("byDomain")
                  or e.get("noAnnotate"))
    print(
        f"\n{total} meanings · {explained} explain their letters · "
        f"{len(unexplained)} unexplained · {len(stale)} stale · "
        f"{steered} entries steer the annotator, {len(problems)} of them malformed."
    )
    return 1 if (unexplained or stale or problems) else 0


if __name__ == "__main__":
    sys.exit(main())
