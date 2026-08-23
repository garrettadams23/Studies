#!/usr/bin/env python3
"""
check_determinism.py — the same sources must produce the same bytes.

A build that embeds a timestamp, iterates a set, or depends on filesystem order
produces a different `index.html` every time it runs. Nothing looks wrong; the
diff on every commit is just noise, and the moment it *is* noise nobody reads
it — which is where a real change hides.

This builds twice and compares. It is cheap, it is the only way to notice the
day someone adds `datetime.now()` to a header, and it is the check that makes
"the built page is byte-identical" — the proof the script split relied on —
mean something.

Usage:
  python3 tools/check_determinism.py
"""

import hashlib
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent
WATCHED = ["index.html", "sw.js"]


def build():
    r = subprocess.run([sys.executable, "build.py"], cwd=ROOT,
                       capture_output=True, text=True)
    if r.returncode != 0:
        print(r.stdout[-2000:])
        print(r.stderr[-2000:], file=sys.stderr)
        raise SystemExit("error: build.py failed.")
    return {name: hashlib.sha256((ROOT / name).read_bytes()).hexdigest()
            for name in WATCHED if (ROOT / name).exists()}


def main():
    first = build()
    second = build()
    drift = [n for n in first if first[n] != second.get(n)]
    for name in sorted(first):
        mark = "DIFFERS" if name in drift else "same   "
        print(f"  {mark}  {name}  {first[name][:16]}")
    if drift:
        print(f"\n{len(drift)} file(s) differ between two identical builds.")
        print("Something in build.py is not deterministic — a timestamp, a set "
              "iteration, or filesystem order.")
        return 1
    print(f"\n{len(first)} output(s) reproducible across two builds.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
