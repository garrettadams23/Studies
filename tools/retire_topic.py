#!/usr/bin/env python3
"""
retire_topic.py — merge one topic into another without losing anybody's progress.

plan.md Phase 9's rule is **merge, never delete**, and §4 says why: a topic id is
a permalink somebody may have bookmarked, and five `localStorage` prefixes key on
it — `reviewed:` `bookmark:` `known:` `srs:` `note:`. Deleting a block silently
strands all of it. Recording an alias moves the lot.

This does the whole move in one command:

  1. refuses if the retired id is referenced by `related.json`, `paths.json` or a
     `<span class="xref">` anywhere, and names what to fix first;
  2. deletes the retired topic's block from its source file;
  3. records `old -> new` in `data/slug-aliases.json`, which `build.py` inlines
     and `script.js` uses to redirect a stale link *and* migrate the progress.

Step 1 is here because the first wave of merges got away with skipping it. Four
topics were retired and none happened to be referenced — luck, not design, and
`make check` would only have caught it afterwards, with the block already gone.

It does not merge *content*. Absorbing what the retired card had that the
survivor lacked is a judgement, and every merge in wave one needed one — the
survivor was missing Wi-Fi 7, or a legal distinction, or a verdict. Do that by
hand first, then run this.

Usage:
  python3 tools/retire_topic.py <domain> --retire "<title fragment>" --into "<title fragment>"
  python3 tools/retire_topic.py <domain> --retire "…" --into "…" --dry
"""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
sys.path.insert(0, str(ROOT / "tools"))
from lint_content import domain_files, slugify, topic_label  # noqa: E402

TOPIC = re.compile(r'<div class="topic"')


def locate(domain, needle):
    """(path, start, end, block) for the one topic whose block contains `needle`."""
    hits = []
    for path in domain_files(domain):
        text = path.read_text(encoding="utf-8")
        starts = [m.start() for m in TOPIC.finditer(text)]
        for n, start in enumerate(starts):
            end = starts[n + 1] if n + 1 < len(starts) else len(text)
            if needle in text[start:end]:
                hits.append((path, start, end, text[start:end]))
    if not hits:
        raise SystemExit(f"error: no topic in '{domain}' contains {needle!r}")
    if len(hits) > 1:
        raise SystemExit(f"error: {len(hits)} topics in '{domain}' contain {needle!r} "
                         f"— narrow the fragment")
    return hits[0]


def references(old_id, old_title):
    """Everything that would break if this topic simply vanished."""
    problems = []

    related = json.loads((DATA / "related.json").read_text(encoding="utf-8"))
    if old_id in related:
        problems.append(f"related.json has {old_id} as a source with "
                        f"{len(related[old_id])} link(s)")
    for src, targets in related.items():
        if old_id in targets:
            problems.append(f"related.json: {src} -> {old_id}")

    paths = json.loads((DATA / "paths.json").read_text(encoding="utf-8"))
    for step in re.findall(r'"([a-z0-9-]+)"', json.dumps(paths)):
        if step == old_id:
            problems.append(f"paths.json includes {old_id} as a step")
            break

    plain = re.sub(r"\s+", " ", old_title)
    for path in sorted(DATA.glob("*.html")):
        for m in re.finditer(r'<span class="xref">(.*?)</span\s*>', path.read_text(encoding="utf-8"), re.S):
            got = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", m.group(1))).strip()
            if got == plain:
                problems.append(f"{path.name} cross-references it by title")
    return problems


def main():
    args = sys.argv[1:]
    if "--retire" not in args or "--into" not in args or not args:
        print(__doc__.strip().rsplit("Usage:", 1)[-1].strip())
        return 2
    domain = args[0]
    retired_needle = args[args.index("--retire") + 1]
    survivor_needle = args[args.index("--into") + 1]
    dry = "--dry" in args

    rpath, rstart, rend, rblock = locate(domain, retired_needle)
    _, _, _, sblock = locate(domain, survivor_needle)
    rtitle, _ = topic_label(rblock)
    stitle, _ = topic_label(sblock)
    old, new = slugify(rtitle), slugify(stitle)

    if old == new:
        raise SystemExit("error: both fragments matched the same topic")

    print(f"  retire  {old}\n            {rtitle[:66]}")
    print(f"    into  {new}\n            {stitle[:66]}")

    problems = references(old, rtitle)
    if problems:
        print(f"\nREFUSED — {len(problems)} reference(s) would break:")
        for p in problems[:12]:
            print(f"  {p}")
        print("\nRepoint these at the survivor first, then run this again.")
        return 1

    if dry:
        print("\n--dry: nothing written. No references would break.")
        return 0

    text = rpath.read_text(encoding="utf-8")
    end = rend
    while end < len(text) and text[end] == "\n":
        end += 1
    rpath.write_text(text[:rstart] + text[end:], encoding="utf-8")

    alias_file = DATA / "slug-aliases.json"
    aliases = json.loads(alias_file.read_text(encoding="utf-8"))
    # If anything already pointed at the id being retired, follow it forward so
    # no alias is left aiming at a topic that no longer exists.
    for k, v in list(aliases.items()):
        if v == old:
            aliases[k] = new
    aliases[old] = new
    alias_file.write_text(
        json.dumps(dict(sorted(aliases.items())), indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8")

    print(f"\n  {rpath.name}: block removed")
    print(f"  slug-aliases.json: {len(aliases)} entries")
    print("  now run: make acronyms && make build && make check")
    return 0


if __name__ == "__main__":
    sys.exit(main())
