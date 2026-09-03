#!/usr/bin/env python3
"""
check_gates.py — the Makefile and the CI workflow must run the same gates.

There were two hand-maintained lists of what has to pass, and neither was a
superset of the other. `search` ran on the server and not locally. `resilience`,
`mobile` and `backup` ran locally and not on the server. Four generated
artefacts were checked only on the server.

That is not a tidiness problem, it is how three real defects shipped. CI failed
on **every push for nine commits** — the acronym domain was missing four
acronyms and a whole subject group — and the failure was invisible to anyone
running `make check`, which passed. The social card told everyone who shared a
link that the site had 1,519 topics when it had 1,534, and the job step that
said so had been red long enough to stop meaning anything.

So: `make all` and the workflow must agree, and this fails the build when they
do not. It is the gate on the gates.

## What counts as a gate

Anything that can fail on purpose: a script named `check_*`, `lint_*`,
`page_budget.py` or `*_test.mjs`, or any command carrying `--check`,
`--verify`, `--self-test` or `--strict`. Generators (`build.py`,
`gen_acronym_domain.py` with no flag) and the censuses are exempt — they report
or they write, they do not gate, and where they run is a matter of convenience.

Usage:
    python3 tools/check_gates.py
    python3 tools/check_gates.py --list     # print both sets and exit 0
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MAKEFILE = ROOT / "Makefile"
WORKFLOW = ROOT / ".github" / "workflows" / "build-check.yml"

# A command that reports or generates rather than gating. Where these run is a
# choice; where a gate runs is not.
NOT_A_GATE = {
    "python3 build.py",
    "python3 tools/gen_acronym_domain.py",
    "python3 tools/annotate_acronyms.py",
    "python3 tools/depth_report.py",
    "python3 tools/near_duplicates.py",
    "python3 tools/orphan_report.py",
    "python3 tools/gen_og_image.mjs",
    "node tools/gen_og_image.mjs",
    "node tools/query_probe.mjs",
}

GATE_NAME_RE = re.compile(r"tools/(?:check_|lint_)|tools/page_budget\.py|_test\.mjs$")
GATE_FLAG_RE = re.compile(r"--(?:check|verify|self-test|strict|check-card|pairs)\b")
CMD_RE = re.compile(r"^(python3?|node)\s+(\S+)(.*)$")


def normalise(line):
    """One shell line -> a canonical command string, or None if it is not one."""
    line = line.strip()
    if not line or line.startswith("#") or "::error::" in line:
        return None
    line = line.replace("$(PY)", "python3").replace("$(NODE)", "node")
    line = re.sub(r"^@", "", line)
    # A workflow step is either `run: <cmd>` or a `run: |` block of bare lines.
    line = re.sub(r"^-?\s*run:\s*", "", line)
    m = CMD_RE.match(line)
    if not m:
        return None
    runner, script, rest = m.group(1), m.group(2), m.group(3).strip()
    runner = "python3" if runner.startswith("python") else runner
    return f"{runner} {script} {rest}".strip()


def is_gate(cmd):
    if cmd in NOT_A_GATE:
        return False
    return bool(GATE_NAME_RE.search(cmd.split()[1]) or GATE_FLAG_RE.search(cmd))


def make_targets():
    """target -> (prerequisites, recipe lines)."""
    out, current = {}, None
    for raw in MAKEFILE.read_text(encoding="utf-8").splitlines():
        if raw.startswith("\t"):
            if current:
                out[current][1].append(raw)
            continue
        m = re.match(r"^([a-z][\w-]*)\s*:([^=]*)$", raw)
        if m and not raw.startswith(".PHONY"):
            current = m.group(1)
            out.setdefault(current, (m.group(2).split(), []))
        elif raw.strip():
            current = None
    return out


def reachable(target, targets, seen=None):
    """Every recipe line of a target and everything it depends on."""
    seen = seen if seen is not None else set()
    if target in seen or target not in targets:
        return []
    seen.add(target)
    prereqs, recipe = targets[target]
    lines = []
    for p in prereqs:
        lines += reachable(p, targets, seen)
    return lines + recipe


def workflow_commands():
    # The workflow is a flat list of steps; scanning every line is enough and
    # needs no YAML parser (this repo is stdlib-only on purpose).
    return [normalise(l) for l in WORKFLOW.read_text(encoding="utf-8").splitlines()]


def main():
    targets = make_targets()
    if "all" not in targets:
        print("::error::Makefile has no 'all' target to compare against.")
        return 1

    local = {c for c in (normalise(l) for l in reachable("all", targets))
             if c and is_gate(c)}
    ci = {c for c in workflow_commands() if c and is_gate(c)}

    if "--list" in sys.argv:
        print(f"make all ({len(local)}):")
        for c in sorted(local):
            print(f"  {c}")
        print(f"\nbuild-check.yml ({len(ci)}):")
        for c in sorted(ci):
            print(f"  {c}")
        return 0

    only_local, only_ci = sorted(local - ci), sorted(ci - local)
    if not only_local and not only_ci:
        print(f"Gates agree — {len(local)} in both 'make all' and build-check.yml.")
        return 0

    print("::error::'make all' and .github/workflows/build-check.yml disagree "
          "about which gates run. A gate on one side only is a gate that fails "
          "where nobody is looking.")
    for c in only_local:
        print(f"  make all only : {c}")
    for c in only_ci:
        print(f"  workflow only : {c}")
    print("\nAdd the missing side, or — if it genuinely does not gate — name it "
          "in NOT_A_GATE with a reason.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
