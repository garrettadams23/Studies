#!/usr/bin/env python3
"""
ti84_trainer.py — Drills the TI-84 Plus CE key sequences the Math domain documents.

This is not an emulator. Emulating the calculator would be a large project with
no learning payoff, and the real device is already a poor practice environment
because it never tells you whether you used it well. This drills the thing that
actually needs practice: knowing which keys produce which result, and knowing
where the machine will answer confidently and be wrong.

The one rule the design turns on: **every number this program states is computed
here, in Python, at run time.** Nothing is a hand-typed constant, so the drill
cannot be wrong about arithmetic even if a drill is edited carelessly. Each drill
that has a numeric answer carries a `compute` expression; `--verify` evaluates
every one and is wired into CI.

    python tools/ti84_trainer.py              a full run, all areas
    python tools/ti84_trainer.py --area calc  just the CALC menu
    python tools/ti84_trainer.py --list       show the bank without drilling
    python tools/ti84_trainer.py --verify     CI gate: every compute evaluates,
                                              every drill is well-formed

Drill bank: data/ti84_drills.json. Spec: plan.md, CALCULUS TRACK section 3.
"""

import argparse
import json
import math
import pathlib
import random
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
BANK = ROOT / "data" / "ti84_drills.json"

AREAS = {
    "mode": "Mode setup",
    "numeric": "Numeric functions (nDeriv, fnInt, Σ, logBASE)",
    "calc": "The CALC menu and graphing",
    "errors": "Errors, traps, and where the calculator lies",
}


# ── the numeric routines, mirroring what the calculator does ────────────────
# nDeriv on the TI-84 uses a symmetric difference quotient, which is exactly why
# it returns a confident answer at a corner. Reproducing that here rather than
# using an exact derivative keeps the drill honest about the machine's behaviour.

def nderiv(f, x, h=1e-5):
    """Symmetric difference quotient — the same estimate the TI-84 makes."""
    return (f(x + h) - f(x - h)) / (2 * h)


def fnint(f, a, b, n=2000):
    """Composite Simpson's rule. n must be even, so it is forced even."""
    n = n if n % 2 == 0 else n + 1
    h = (b - a) / n
    total = f(a) + f(b)
    for i in range(1, n):
        total += (4 if i % 2 else 2) * f(a + i * h)
    return total * h / 3


SAFE = {"math": math, "nderiv": nderiv, "fnint": fnint, "abs": abs,
        "sum": sum, "range": range, "float": float, "int": int}


def evaluate(expr):
    """Run a drill's `compute` in a namespace with no builtins."""
    return eval(expr, {"__builtins__": {}}, SAFE)  # noqa: S307 — fixed, in-repo input


def fmt(value):
    if isinstance(value, float):
        if abs(value) < 1e-10:
            return f"0 (computed as {value:.3g} — floating point, read it as zero)"
        rounded = round(value, 10)
        return f"{rounded:g}"
    return str(value)


# ── answer matching ────────────────────────────────────────────────────────
# Deliberately forgiving. The point is whether the person knows the sequence,
# not whether they typed the parentheses the way the bank happens to store them.

def normalise(text):
    text = text.lower().strip()
    text = text.replace("²", "2").replace("^", "").replace("π", "pi")
    text = re.sub(r"[^\w]+", " ", text)
    return " ".join(text.split())


def matches(given, accepted):
    g = normalise(given)
    if not g:
        return False
    for a in accepted:
        n = normalise(a)
        if g == n or n in g or g in n:
            return True
    return False


def load():
    data = json.loads(BANK.read_text(encoding="utf-8"))
    return data["drills"]


def verify():
    """CI gate. Checks structure and that every computed answer evaluates."""
    problems, computed = [], 0
    try:
        drills = load()
    except Exception as exc:                                   # noqa: BLE001
        print(f"error: cannot read {BANK.name}: {exc}", file=sys.stderr)
        return 1

    seen = set()
    for d in drills:
        did = d.get("id", "<no id>")
        for field in ("id", "area", "prompt", "accept", "answer"):
            if not d.get(field):
                problems.append(f"{did}: missing '{field}'")
        if did in seen:
            problems.append(f"{did}: duplicate id")
        seen.add(did)
        if d.get("area") not in AREAS:
            problems.append(f"{did}: unknown area {d.get('area')!r}")
        if not isinstance(d.get("accept"), list) or not d["accept"]:
            problems.append(f"{did}: 'accept' must be a non-empty list")
        if "compute" in d:
            try:
                evaluate(d["compute"])
                computed += 1
            except Exception as exc:                           # noqa: BLE001
                problems.append(f"{did}: compute failed — {exc}")

    missing = sorted(set(AREAS) - {d.get("area") for d in drills})
    if missing:
        problems.append("no drills for area(s): " + ", ".join(missing))

    for p in problems:
        print(f"error: {p}", file=sys.stderr)
    if problems:
        return 1
    print(f"{len(drills)} drills across {len(AREAS)} areas; "
          f"{computed} answers computed at run time. OK.")
    return 0


# ── keeping the card and the drill bank in step ─────────────────────────────
# The card used to describe the trainer in prose, naming two of the four areas.
# Prose cannot be checked, so it drifted the moment an area was added. The block
# between these markers is generated from the bank instead, and --check-card is
# wired into CI so the two cannot disagree again.
CARD = ROOT / "data" / "math.html"
BEGIN = "<!-- BEGIN GENERATED: ti84-drill-index -->"
END = "<!-- END GENERATED: ti84-drill-index -->"


def card_block(indent="      "):
    """The drill index, as it should appear inside the TI-84 card."""
    drills = load()
    rows = [
        f"{indent}  <tr><td><code>--area {area}</code></td><td>{label}</td>"
        f"<td>{sum(1 for d in drills if d['area'] == area)}</td></tr>"
        for area, label in AREAS.items()
    ]
    return "\n".join([
        f"{indent}{BEGIN}",
        f"{indent}<!-- Generated by tools/ti84_trainer.py --sync-card. Do not edit by hand. -->",
        f'{indent}<table class="ref-table">',
        f"{indent}  <tr><th>Flag</th><th>Covers</th><th>Drills</th></tr>",
        *rows,
        f"{indent}</table>",
        f"{indent}{END}",
    ])


def sync_card(check=False):
    text = CARD.read_text(encoding="utf-8")
    if BEGIN not in text or END not in text:
        print(f"error: {CARD.name} has no ti84-drill-index markers", file=sys.stderr)
        return 1

    start = text.index(BEGIN)
    indent = text[: start].rsplit("\n", 1)[-1]
    end = text.index(END) + len(END)
    updated = text[: start - len(indent)] + card_block(indent) + text[end:]

    if check:
        if updated != text:
            print(
                "::error::the TI-84 drill index in data/math.html is out of step "
                "with data/ti84_drills.json. Run "
                "'python tools/ti84_trainer.py --sync-card' and commit the result.",
                file=sys.stderr,
            )
            return 1
        print("TI-84 drill index is in step with the bank.")
        return 0

    CARD.write_text(updated, encoding="utf-8")
    print(f"Synced the drill index into {CARD.name}.")
    return 0


def show_list():
    drills = load()
    for area, label in AREAS.items():
        rows = [d for d in drills if d["area"] == area]
        print(f"\n{label}  ({len(rows)})")
        for d in rows:
            print(f"  {d['id']:<18} {d['answer']}")
    print()
    return 0


def run(area=None, limit=None, shuffle=True):
    drills = [d for d in load() if area is None or d["area"] == area]
    if not drills:
        print(f"No drills for area {area!r}. Try --list.", file=sys.stderr)
        return 1
    if shuffle:
        random.shuffle(drills)
    if limit:
        drills = drills[:limit]

    print("\nTI-84 Plus CE trainer — type your answer, or press Enter to skip.")
    print("Ctrl-C to stop.\n")
    right = 0
    try:
        for i, d in enumerate(drills, 1):
            print(f"[{i}/{len(drills)}]  {d['prompt']}")
            try:
                given = input("  > ")
            except EOFError:
                print("\n(no input — stopping)")
                break
            ok = matches(given, d["accept"])
            right += ok
            print(f"  {'correct' if ok else 'not quite'} — {d['answer']}")
            if "compute" in d:
                print(f"  answer: {fmt(evaluate(d['compute']))}")
            if d.get("note"):
                print(f"  note:   {d['note']}")
            print()
    except KeyboardInterrupt:
        print("\n\nStopped.")

    done = min(i, len(drills)) if drills else 0
    print(f"{right}/{done} correct.")
    if right < done:
        print("The ones you missed are the ones worth writing in the notepad.")
    return 0


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[1])
    ap.add_argument("--area", choices=sorted(AREAS), help="drill one area only")
    ap.add_argument("--limit", type=int, help="stop after N drills")
    ap.add_argument("--ordered", action="store_true", help="do not shuffle")
    ap.add_argument("--list", action="store_true", help="print the bank and exit")
    ap.add_argument("--verify", action="store_true", help="CI gate; no interaction")
    ap.add_argument("--sync-card", action="store_true",
                    help="write the drill index into the TI-84 card")
    ap.add_argument("--check-card", action="store_true",
                    help="CI gate: fail if the card's drill index is stale")
    args = ap.parse_args()

    if args.verify:
        return verify()
    if args.check_card:
        return sync_card(check=True)
    if args.sync_card:
        return sync_card()
    if args.list:
        return show_list()
    return run(args.area, args.limit, not args.ordered)


if __name__ == "__main__":
    try:
        sys.exit(main())
    except BrokenPipeError:
        # Piping to `head` or `less` closes the pipe early; that is not an error.
        # Redirect stdout to devnull so the interpreter's own flush stays quiet.
        import os
        os.dup2(os.open(os.devnull, os.O_WRONLY), sys.stdout.fileno())
        sys.exit(0)
