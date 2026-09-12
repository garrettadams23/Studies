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
    print(f"check_acronyms self-test passed ({len(FIXTURES)} fixtures + both directions).")
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

    unexplained, stale = scan(entries)
    for acronym, expansion in unexplained:
        print(f"{acronym}: '{expansion}' — the letters are not drawn from the expansion,")
        print(f"{'':<{len(acronym) + 2}}and no 'l' field says how they are formed.")
    for acronym, expansion, why in stale:
        print(f"{acronym}: '{expansion}' derives cleanly, so the 'l' field is stale:")
        print(f"{'':<{len(acronym) + 2}}{why!r}")

    explained = sum(1 for e in entries for m in e["m"] if m.get("l"))
    print(
        f"\n{total} meanings · {explained} explain their letters · "
        f"{len(unexplained)} unexplained · {len(stale)} stale."
    )
    return 1 if (unexplained or stale) else 0


if __name__ == "__main__":
    sys.exit(main())
