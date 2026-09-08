#!/usr/bin/env python3
"""
check_plan_numbers.py — plan.md's headline table, checked against the tools it credits.

The table at the top of plan.md opens with a claim about itself:

    **The measured state, as of the last session record.** Every number below is
    produced by a tool in `tools/`, not by anybody's recollection.

It was produced by a tool once. After that it was maintained by hand, and by the
time anything checked it **nine of its thirteen derivable rows were wrong** —
including the one that matters most for planning:

    Page budget | 4% raw headroom — room for ~66 more topics

The budget had been raised in a session two dozen records earlier and the row
never moved. The real figure was **35% and room for ~840**, so the site's
headline constraint understated its own headroom by a factor of twelve. A reader
deciding whether there was room to write would have concluded there was not.

This is the same defect the repository has now shipped three times, and every
time in something that reports rather than gates: the social card claiming 1,519
topics over a site with 1,534; four generated artefacts checked only on the
server; and now the plan's own census. The fix is always the same shape — the
number gets re-derived and compared, and the comparison runs where somebody
looks.

## What it checks

Every row whose value a script can derive today, without a browser and without a
stopwatch. For each, the numbers the owning tool reports must appear in the row,
matched on digit boundaries so that `6` does not satisfy a row that says `60`.

Rows are matched by their **Measure** cell, not by position, so inserting a row
does not silently shift the checks onto the wrong ones.

## What it deliberately does not check

Four rows need a browser or a timing run on one particular machine, and one of
them says so in its own text — *this container only*. Re-deriving those here
would either make the gate need Chromium or, worse, make it quietly assert a
timing figure from whatever hardware CI happened to allocate. They are listed as
unchecked on every run, so their status is visible rather than assumed.

## Why a failed parse is a failure and not a pass

Every derivation asserts it found what it was looking for. A regex that stops
matching because a tool reworded its output would otherwise turn this gate into
one that reports "0 drifted" forever — and a validator that reports zero because
it stopped looking is indistinguishable from one that found nothing wrong. That
distinction is the whole reason `check_markup.py` carries a self-test.

Usage:
  python3 tools/check_plan_numbers.py
  python3 tools/check_plan_numbers.py --list        # every derived number
  python3 tools/check_plan_numbers.py --self-test   # row matching, on fixtures
"""

import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PLAN = ROOT / "plan.md"
HEADER = "| Measure | Value | Tool |"

# Rows that need Chromium or a stopwatch. Named so a run says what it did not do.
UNCHECKED = {
    "Reader questions answered": "query_probe.mjs drives a real browser",
    "Throttled load": "a timing run, and the row itself says 'this container only'",
    "Search &amp; heap at 3x the content": "a synthetic timing run",
    "Gate results": "the per-suite counts come from a full `make all`",
}


def run(*cmd):
    """A tool's stdout, or a hard failure. Never a silent empty string."""
    proc = subprocess.run(
        [sys.executable, str(ROOT / "tools" / cmd[0]), *cmd[1:]],
        capture_output=True, text=True, cwd=ROOT,
    )
    if not proc.stdout.strip():
        raise SystemExit(f"{cmd[0]} produced no output — cannot derive from it")
    return proc.stdout


def grab(pattern, text, source, count=1):
    """Ints from the first match, asserting the shape is still what we parse."""
    m = re.search(pattern, text)
    if not m:
        raise SystemExit(
            f"{source}: output no longer matches {pattern!r}.\n"
            "  This gate cannot check what it cannot parse — fix the pattern "
            "rather than deleting the row."
        )
    vals = [int(g.replace(",", "")) for g in m.groups()]
    if len(vals) != count:
        raise SystemExit(f"{source}: expected {count} numbers, parsed {len(vals)}")
    return vals


def derive():
    """-> {measure cell: [numbers that must appear in the row]}"""
    out = {}

    depth = run("depth_report.py")
    topics, thin, thin_pct = grab(
        r"([\d,]+) topics · ([\d,]+) single-concept and under [\d,]+ plain chars \((\d+)%\)",
        depth, "depth_report.py", 3)
    mean, mean_nv = grab(
        r"mean chars per concept card: ([\d,]+)\s+\(([\d,]+) excluding verdicts\)",
        depth, "depth_report.py", 2)
    median, p10 = grab(
        r"median topic: ([\d,]+) plain chars · 10th percentile: ([\d,]+)",
        depth, "depth_report.py", 2)
    domains = len(json.loads((ROOT / "data" / "domains.json").read_text(encoding="utf-8")))

    out["Topics"] = [topics, domains]
    out["Thin (one card, under 1,800 chars)"] = [thin, thin_pct]
    out["Mean chars per concept card"] = [mean, mean_nv]
    out["Depth tail"] = [p10, median]

    orph = run("orphan_report.py")
    n_orph, = grab(r"([\d,]+) of [\d,]+ topics have no related link", orph, "orphan_report.py")
    deep, = grab(r"([\d,]+) of those are deep", orph, "orphan_report.py")
    out["Orphans"] = [n_orph, deep]

    dup = run("near_duplicates.py")
    pairs, titles, over, contain = grab(
        r"([\d,]+) pair\(s\) across ([\d,]+) titles: ([\d,]+) at or above 0\.50, and ([\d,]+) marked",
        dup, "near_duplicates.py", 4)
    deliberate, read, unread = grab(
        r"([\d,]+) differ on something §3 calls deliberate; ([\d,]+) were read and kept.*?"
        r"\*\*([\d,]+) have not been read\*\*",
        dup, "near_duplicates.py", 3)
    out["Near-duplicate pairs"] = [pairs, over, contain, deliberate, read, unread]

    paths = run("check_paths.py")
    n_paths, steps, reach, total = grab(
        r"([\d,]+) paths, ([\d,]+) steps, ([\d,]+) distinct topics of ([\d,]+) on the site",
        paths, "check_paths.py", 4)
    out["Learning paths"] = [n_paths, steps, reach, total]

    rel = run("suggest_related.py", "--check")
    linked, links, oneway = grab(
        r"([\d,]+) topics carry ([\d,]+) links \(([\d,]+) one-way\)",
        rel, "suggest_related.py --check", 3)
    out["Related links"] = [linked, links, oneway]

    budget = run("page_budget.py")
    raw_pct, = grab(r"raw_mb\s+[\d.]+\s+[\d.]+\s+(\d+)% left", budget, "page_budget.py")
    room, = grab(r"Room for ~([\d,]+) more", budget, "page_budget.py")
    out["Page budget"] = [raw_pct, room]

    gates = run("check_gates.py")
    n_gates, = grab(r"([\d,]+) in both", gates, "check_gates.py")
    out["Gates"] = [n_gates]

    lint = run("lint_content.py")
    verdictless, = grab(r"TREND .*?table=([\d,]+)", lint, "lint_content.py")
    out["Cards ending on a table with no verdict"] = [verdictless]

    return out


def table_rows(text):
    """-> {measure cell: value cell} for the one headline table."""
    start = text.find(HEADER)
    if start < 0:
        raise SystemExit(f"plan.md no longer contains the row {HEADER!r}")
    rows = {}
    for line in text[start:].splitlines()[2:]:
        if not line.startswith("|"):
            break
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) >= 2:
            rows[cells[0]] = cells[1]
    return rows


def present(value, cell):
    """Is this number in the cell, on digit boundaries? 6 must not satisfy 60."""
    forms = {str(value), f"{value:,}"}
    return any(re.search(r"(?<![\d,])" + re.escape(f) + r"(?![\d,])", cell) for f in forms)


def check(rows, derived):
    missing, unknown = [], []
    for measure, values in derived.items():
        if measure not in rows:
            unknown.append(measure)
            continue
        cell = rows[measure]
        gone = [v for v in values if not present(v, cell)]
        if gone:
            missing.append((measure, gone, cell))
    return missing, unknown


FIXTURES = [
    (60, "**60**, every one generated, **0 deep**", True),
    (6, "**60**, every one generated, **0 deep**", False),      # 6 must not match 60
    (0, "**60**, every one generated, **0 deep**", True),
    (1544, "**1,544** across 30 domains", True),                 # comma form
    (1544, "**1544** across 30 domains", True),                  # bare form
    (544, "**1,544** across 30 domains", False),                 # not a suffix match
    (30, "**1,544** across 30 domains", True),
    (35, "**4% raw** headroom — room for ~66 more topics", False),
]


def self_test():
    failures = [
        f"  present({v}, {cell!r}) was {present(v, cell)}, expected {want}"
        for v, cell, want in FIXTURES if present(v, cell) != want
    ]

    sample = (
        "text before\n\n" + HEADER + "\n|---|---|---|\n"
        "| Topics | **1,544** across 30 domains | `depth_report.py` |\n"
        "| Gates | **30**, and the same 30 in `make all` | `check_gates.py` |\n"
        "\nprose after\n"
    )
    rows = table_rows(sample)
    if list(rows) != ["Topics", "Gates"]:
        failures.append(f"  table_rows parsed {list(rows)}")
    missing, unknown = check(rows, {"Topics": [1544, 30], "Gates": [33]})
    if len(missing) != 1 or missing[0][0] != "Gates":
        failures.append(f"  expected Gates to drift, got {[m[0] for m in missing]}")
    if check(rows, {"Nonexistent row": [1]})[1] != ["Nonexistent row"]:
        failures.append("  a row the table does not have was not reported")

    if failures:
        print("check_plan_numbers self-test FAILED:")
        print("\n".join(failures))
        return 1
    print(f"check_plan_numbers self-test passed ({len(FIXTURES)} fixtures + table parsing).")
    return 0


def main():
    args = sys.argv[1:]
    if "--self-test" in args:
        return self_test()

    derived = derive()
    if "--list" in args:
        for measure, values in derived.items():
            print(f"{measure:<44} {', '.join(f'{v:,}' for v in values)}")
        return 0

    rows = table_rows(PLAN.read_text(encoding="utf-8"))
    missing, unknown = check(rows, derived)

    for measure, gone, cell in missing:
        print(f"{measure}: the row does not carry {', '.join(f'{v:,}' for v in gone)}")
        print(f"    row says  {cell}")
        print(f"    tools say {', '.join(f'{v:,}' for v in derived[measure])}")
    for measure in unknown:
        print(f"{measure}: derived, but no such row in plan.md's table")

    print(
        f"\n{len(derived)} derivable row(s) · {len(missing) + len(unknown)} drifted.\n"
        f"{len(UNCHECKED)} row(s) not checked here — they need a browser or a stopwatch:"
    )
    for measure, why in UNCHECKED.items():
        print(f"  {measure:<38} {why}")
    return 1 if (missing or unknown) else 0


if __name__ == "__main__":
    sys.exit(main())
