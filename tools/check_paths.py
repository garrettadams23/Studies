#!/usr/bin/env python3
"""
check_paths.py — every step in data/paths.json points at a topic that exists.

A learning path is an ordered list of topic ids over content that already
exists, so the only way it breaks is by pointing somewhere that has gone. The
page drops an unresolvable step rather than rendering it, which means a broken
path looks like a *shorter* path — a silent failure, and exactly the shape this
project keeps finding. This is the check that makes it loud.

Also reports, because all three are worth knowing before editing a path:

  * a step listed twice in one path — almost always a copy-paste
  * how much of the site the paths reach, and which domains they draw on
  * **hand-written topics that are on no path at all**, by name

That third one was added after the plan's navigation row — *0 hand-written
orphans, 0 hand-written topics off a path* — turned out to be **half true**.
The orphan half is measured: `orphan_report.py` names deep orphans and the
register reopens on one. The path half was only ever asserted, and three
topics had quietly fallen off it: two from the session that added CBT, DBT and
qigong, one from the session that gave `web` its cascade card. Each was linked
into `related.json` — so the gated layer caught its half — and none was given a
path step, because nothing looked.

The bare coverage line could not show it. 60 generated acronym pages are off
every path by design, so the interesting three hid inside *1,490 of 1,553* and
would have gone on hiding at any size. Naming them is the same move
`depth_report.py --thin` makes for cards that are short on purpose: the count
is uninformative while the deliberate cases dominate it, so print the ones a
person has to judge.

`orphan_report.py` carried the matching claim in a comment — *the same 60 are
the whole of the gap in `suggest_related.py --check` and in `check_paths.py`* —
which was true when written and false by the time anybody counted. Fixed there
too.

Exit status is 1 if any step fails to resolve. Topics off a path are **reported,
never failed**: a topic does not owe a path, and a gate here would push people
to pad a syllabus to clear a build.

Usage:
  python3 tools/check_paths.py
  python3 tools/check_paths.py --ordering    # pairs two paths order differently
  python3 tools/check_paths.py --self-test   # the off-path split, on fixtures
"""

import collections
import json
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent
DATA = ROOT / "data"
sys.path.insert(0, str(ROOT / "tools"))

import suggest_related  # noqa: E402

REQUIRED = ("id", "name", "icon", "blurb", "for", "steps")

# Generated domains are off every path on purpose — the acronym dictionary's
# A-Z and By-Area index pages are a lookup surface, not a syllabus. Kept as a
# named set rather than a threshold so that adding a generated domain is a
# visible decision, which is the lesson from a category field in a generated
# taxonomy moving the site's topic count.
GENERATED_DOMAINS = {"acronym"}


def orderings(paths):
    """(pairs ordered by two or more paths, the ones ordered both ways).

    A path lists topics in an order, and 95 of the 1,497 topics on a path are on
    more than one. Wherever two paths share a **pair**, they are both making a
    claim about which comes first — and it is worth knowing how often those
    claims agree, because the answer decides what `paths.json` can be used for.

    It is 30%: of the 56 pairs that two or more paths both order, **17 are
    ordered in opposite directions**. Read one at a time, every one of them is
    two legitimate stories:

        `cryptography-end-to-end` puts encryption basics before password
        hashing, because the track builds from primitives. `security-for-
        everyone` puts hashing first, because it is the concrete thing a reader
        has met. Neither is wrong, and no third path can arbitrate.

    **So a path is a narrative order, not a prerequisite graph**, and the
    disagreement rate is the evidence rather than the problem. A global ordering
    derived from `paths.json` — a generated curriculum, a "what should I read
    first" feature — would be building on a relation this data does not carry,
    and would contradict itself on a third of the pairs it found. That is the
    reason this reports and does not gate: there is nothing here to fix.

    Printed rather than left to be re-derived, on this repository's own rule
    that a diagnosis reached by hand more than once should be printed.
    """
    order = collections.defaultdict(set)
    for p in paths:
        steps = p.get("steps") or []
        for i, x in enumerate(steps):
            for y in steps[i + 1:]:
                order[(x, y)].add(p.get("id", "<no id>"))
    # Normalise first. Iterating the keys and skipping `x > y` misses every pair
    # that only ever appears in the reverse lexical direction — it reported 38
    # shared pairs against a hand count of 56, which is the kind of quiet
    # undercount a report is worst at showing you.
    shared, both = [], []
    for x, y in sorted({tuple(sorted(k)) for k in order}):
        fwd, rev = order.get((x, y), set()), order.get((y, x), set())
        # Distinct *paths*, not assertions. A path that repeats a step orders
        # the same pair both ways on its own, and counting that as two paths
        # disagreeing would turn a copy-paste — which the duplicate warning
        # above already reports — into a second, wronger finding.
        if len(fwd | rev) > 1:
            shared.append((x, y))
            if fwd and rev:
                both.append((x, y, sorted(fwd), sorted(rev)))
    return shared, sorted(both)


def off_path(rows, covered):
    """(domain, id) for each hand-written topic no path reaches, domain-sorted."""
    return sorted((r["domain"], r["id"]) for r in rows
                  if r["id"] not in covered and r["domain"] not in GENERATED_DOMAINS)


def self_test():
    """The split is set arithmetic, and set arithmetic is where the off-by-one
    lives. The fixtures are the four cases that decide it: reached, stranded,
    generated-and-stranded (not a finding), and a topic reached by some other
    path than its own domain's."""
    rows = [{"id": "a", "domain": "net"}, {"id": "b", "domain": "net"},
            {"id": "c", "domain": "acronym"}, {"id": "d", "domain": "mind"}]
    cases = [
        ("everything reached", {"a", "b", "c", "d"}, []),
        ("one hand-written stranded", {"a", "c", "d"}, [("net", "b")]),
        ("a generated page stranded is not a finding", {"a", "b", "d"}, []),
        ("two stranded, sorted by domain", {"a", "c"}, [("mind", "d"), ("net", "b")]),
        ("nothing reached", set(), [("mind", "d"), ("net", "a"), ("net", "b")]),
    ]
    bad = 0
    for name, covered, expect in cases:
        got = off_path(rows, covered)
        if got != expect:
            bad += 1
            print(f"FAIL : {name} — expected {expect}, got {got}")

    # orderings(), and the fixture that matters is the third: `b` before `a` is
    # a pair whose only key is ("b", "a"), and a loop that skips `x > y` never
    # visits it. That undercounted the live report by eighteen pairs.
    ocases = [
        ("one path asserts nothing shared", [["a", "b"]], 0, 0),
        ("two paths agreeing", [["a", "b"], ["a", "b", "c"]], 1, 0),
        ("two paths disagreeing", [["a", "b"], ["b", "a"]], 1, 1),
        ("…in reverse lexical order only", [["b", "a"], ["b", "a"]], 1, 0),
        ("a pair one path orders twice is not shared", [["a", "b", "a"]], 0, 0),
        ("three paths, one dissenting", [["a", "b"], ["a", "b"], ["b", "a"]], 1, 1),
    ]
    for name, steps, want_shared, want_both in ocases:
        shared, both = orderings([{"id": f"p{i}", "steps": s} for i, s in enumerate(steps)])
        if (len(shared), len(both)) != (want_shared, want_both):
            bad += 1
            print(f"FAIL : {name} — expected {(want_shared, want_both)}, "
                  f"got {(len(shared), len(both))}")

    print(f"check_paths self-test: {len(cases) + len(ocases)} fixtures, {bad} failure(s).")
    return 1 if bad else 0


def main():
    if "--self-test" in sys.argv:
        return self_test()
    path = DATA / "paths.json"
    if not path.exists():
        print("data/paths.json not found — nothing to check.")
        return 0
    paths = json.loads(path.read_text(encoding="utf-8"))
    rows = suggest_related.topics()
    owner = {r["id"]: r["domain"] for r in rows}

    errors, warns = [], []
    seen_ids = set()
    covered, domains = set(), collections.Counter()

    for p in paths:
        pid = p.get("id", "<no id>")
        for field in REQUIRED:
            if not p.get(field):
                errors.append(f"{pid}: missing '{field}'")
        if pid in seen_ids:
            errors.append(f"{pid}: duplicate path id")
        seen_ids.add(pid)

        steps = p.get("steps") or []
        if len(set(steps)) != len(steps):
            dupes = [s for s, n in collections.Counter(steps).items() if n > 1]
            warns.append(f"{pid}: repeats {', '.join(dupes)}")
        for step in steps:
            if step not in owner:
                errors.append(f"{pid}: step '{step}' is not a topic")
            else:
                covered.add(step)
                domains[owner[step]] += 1

    for e in errors:
        print(f"ERROR {e}")
    for w in warns:
        print(f"warn  {w}")

    total_steps = sum(len(p.get("steps") or []) for p in paths)
    print(f"\n{len(paths)} paths, {total_steps} steps, {len(covered)} distinct topics "
          f"of {len(rows)} on the site.")
    print("  " + ", ".join(f"{d} {n}" for d, n in domains.most_common()))

    if "--ordering" in sys.argv:
        shared, both = orderings(paths)
        print(f"\n{len(shared)} topic pair(s) ordered by two or more paths · "
              f"{len(both)} ordered both ways "
              f"({len(both) / len(shared):.0%} — see orderings() on why that is not a defect)")
        for x, y, fwd, rev in both:
            print(f"  {x[:58]}\n  {y[:58]}")
            print(f"     first in {', '.join(fwd)}   ·   second in {', '.join(rev)}")
        return 1 if errors else 0

    stranded = off_path(rows, covered)
    print(f"\n{len(stranded)} hand-written topic(s) on no path "
          f"({len(rows) - len(covered) - len(stranded)} generated pages are off one by design).")
    for domain, tid in stranded:
        print(f"  [{domain}] {tid[:62]}")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
