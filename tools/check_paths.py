#!/usr/bin/env python3
"""
check_paths.py — every step in data/paths.json points at a topic that exists.

A learning path is an ordered list of topic ids over content that already
exists, so the only way it breaks is by pointing somewhere that has gone. The
page drops an unresolvable step rather than rendering it, which means a broken
path looks like a *shorter* path — a silent failure, and exactly the shape this
project keeps finding. This is the check that makes it loud.

Also reports, because both are worth knowing before editing a path:

  * a step listed twice in one path — almost always a copy-paste
  * how much of the site the paths reach, and which domains they draw on

Exit status is 1 if any step fails to resolve.

Usage:
  python3 tools/check_paths.py
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


def main():
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
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
