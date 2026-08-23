#!/usr/bin/env python3
"""Wrap legacy bare-text topic titles in <span class="topic-name">, and record
every slug the rewrite moves so old links and stored progress survive it.

Ninety topics were written before `.topic-name` was a convention and carry the
title as a bare text node inside `.topic-header`. script.js falls back to the
header's own textContent for those, which swallows the `.topic-badge` word and,
once the tool cluster is injected, the ★ ✓ 🔗 buttons — so their flashcards,
quiz options and study-list rows all read wrong.

The wrap is not free. No topic in data/*.html carries an `id`, so every slug is
derived at runtime from that same text: pulling the badge out of the label
changes the slug for all ninety, which breaks shared permalinks and orphans
their `reviewed:` / `bookmark:` / `known:` / `srs:` keys. This script therefore
does both halves at once — the rewrite, and the old → new map that lets the page
heal a stale link and migrate the storage behind it.

The slug rule lives in exactly one place: lint_content.slugify, itself a port of
script.js. Ordering and the `-2` de-duplication are reproduced here from
lint_content.main so that the map is computed the way the browser numbers the
page, not the way a file happens to be laid out.

    python tools/fix_topic_names.py                 rewrite + refresh the alias map
    python tools/fix_topic_names.py --aliases-only  record slug moves already in
                                                    the tree, wrap nothing — the
                                                    mode to run after retitling
                                                    a card
    python tools/fix_topic_names.py --check         CI: fail on a legacy header,
                                                    a dangling alias, or a move
                                                    with no alias recorded
    python tools/fix_topic_names.py --report        show what would change
"""

import json
import pathlib
import re
import subprocess
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from lint_content import domain_files, slugify, topic_blocks, topic_label  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
ALIASES = DATA / "slug-aliases.json"

# Prettier splits tags across lines, so every pattern here tolerates a newline
# before the closing angle bracket. Matching `<div class="topic-header">` with a
# naive regex is how earlier passes silently under-reported.
HEADER_RE = re.compile(r'(<div\b[^>]*class="topic-header"[^>]*>)(.*?)(</div\s*>)', re.S)
LEAD_RE = re.compile(r'\s*<span\b[^>]*class="(?:topic-icon|topic-badge)"[^>]*>.*?</span\s*>', re.S)
CHEV_RE = re.compile(r'\s*<span\b[^>]*class="topic-chev"[^>]*>.*?</span\s*>\s*$', re.S)


def source_files():
    """Every domain's sources, in build order.

    Domain order matters — script.js numbers topics in document order — and so
    does part order within a domain, which source_files() supplies.
    """
    order = [d["id"] for d in json.loads((DATA / "domains.json").read_text())]
    return [f for d in order for f in domain_files(d)]


def page_slugs(texts):
    """Every topic id the browser would assign, in the order it would assign it.

    `texts` maps filename -> file contents, so this can be run against the files
    on disk before and after the rewrite without touching them.
    """
    seen, out = set(), []
    for path in source_files():
        for _, block in topic_blocks(texts[path.name]):
            label, _ = topic_label(block)
            if not label:
                continue
            base = slugify(label)
            slug, i = base, 2
            while slug in seen:
                slug = f"{base}-{i}"
                i += 1
            seen.add(slug)
            out.append((path.name, slug))
    return out


def committed_texts():
    """The domain files as HEAD has them, or None outside a git checkout.

    Slugs have to be compared against what was *published*, not against the
    working tree: a rename made in the same change as the wrap would otherwise
    be invisible, and its old permalink would go unrecorded. Edit order should
    not decide whether a link survives.
    """
    texts = {}
    for path in source_files():
        try:
            texts[path.name] = subprocess.run(
                ["git", "show", f"HEAD:data/{path.name}"],
                cwd=ROOT, capture_output=True, text=True, check=True).stdout
        except (subprocess.CalledProcessError, FileNotFoundError):
            return None
    return texts


def wrap_header(inner):
    """Wrap a bare-text title, or None if this header needs no change.

    The badge stays exactly where it is. Moving it to the modern icon/name/badge
    order would be a visual change to ninety headers on top of a slug change to
    ninety topics, and one risky thing per commit is enough.
    """
    if 'class="topic-name"' in inner:
        return None

    rest = inner
    lead = ""
    while True:
        m = LEAD_RE.match(rest)
        if not m:
            break
        lead += m.group(0)
        rest = rest[m.end():]

    trail = ""
    m = CHEV_RE.search(rest)
    if m:
        trail = m.group(0)
        rest = rest[:m.start()]

    title = rest.strip()
    if not title or "<div" in title:
        return None      # not a shape this script understands — leave it alone
    ws_l = rest[: len(rest) - len(rest.lstrip())]
    ws_r = rest[len(rest.rstrip()):]
    return f'{lead}{ws_l}<span class="topic-name">{title}</span>{ws_r}{trail}'


def rewrite(text):
    """(new_text, n_headers_wrapped)"""
    count = 0

    def sub(m):
        nonlocal count
        wrapped = wrap_header(m.group(2))
        if wrapped is None:
            return m.group(0)
        count += 1
        return m.group(1) + wrapped + m.group(3)

    return HEADER_RE.sub(sub, text), count


def compose_aliases(before, after, existing):
    """old -> new, keeping every alias we have ever published.

    An alias already in the file may point at a slug this run just moved; those
    are re-pointed rather than left dangling, so one hop is always enough at
    runtime and a link from two renames ago still lands.
    """
    if [f for f, _ in before] != [f for f, _ in after]:
        raise SystemExit("topic count or order changed — refusing to guess the pairing")

    moved = {old: new for (_, old), (_, new) in zip(before, after) if old != new}
    out = dict(moved)
    for old, new in existing.items():
        out[old] = moved.get(new, new)
    # A slug that moved away and came back is not an alias, it is itself.
    return {k: v for k, v in sorted(out.items()) if k != v}


def main():
    mode = ("check" if "--check" in sys.argv else
            "report" if "--report" in sys.argv else
            "aliases" if "--aliases-only" in sys.argv else "write")

    worktree = {p.name: p.read_text(encoding="utf-8") for p in source_files()}

    after_texts, touched = {}, {}
    for path in source_files():
        # --aliases-only leaves markup alone; it exists to record a plain rename,
        # which is the common case once the legacy headers are gone.
        new, n = (worktree[path.name], 0) if mode == "aliases" else rewrite(worktree[path.name])
        after_texts[path.name] = new
        if n:
            touched[path.name] = n
    after = page_slugs(after_texts)

    # --check is about the tree as it stands; writing a map is about what the
    # last commit published, so that a rename alongside the wrap is recorded too.
    before_texts = worktree if mode == "check" else (committed_texts() or worktree)
    before = page_slugs(before_texts)

    existing = json.loads(ALIASES.read_text()) if ALIASES.exists() else {}
    aliases = compose_aliases(before, after, existing)

    if mode == "check":
        # The map is an append-only record of links we have published, not a
        # derived artifact — CI cannot re-derive it, only check it still holds.
        problems = []
        if touched:
            problems.append(
                "legacy .topic-header titles are not wrapped in .topic-name: "
                + ", ".join(f"{f} ({n})" for f, n in sorted(touched.items()))
            )
        live = {s for _, s in after}
        dangling = sorted(f"{k} -> {v}" for k, v in existing.items() if v not in live)
        if dangling:
            problems.append("alias points at a slug that no longer exists: " + ", ".join(dangling))
        unrecorded = sorted(
            f"{o} -> {n}" for (_, o), (_, n) in zip(before, after)
            if o != n and existing.get(o) != n
        )
        if unrecorded:
            problems.append("slug would move with no alias recorded: " + ", ".join(unrecorded))
        if problems:
            for p in problems:
                print(f"error: {p}", file=sys.stderr)
            print("Run 'python tools/fix_topic_names.py' and commit the result.", file=sys.stderr)
            return 1
        print(f"topic names OK — {len(existing)} slug alias(es) on record.")
        return 0

    changed = [((f, o), n) for (f, o), (_, n) in zip(before, after) if o != n]
    if mode == "report":
        for (f, old), new in changed:
            print(f"{f:16} {old}\n{'':16} -> {new}")
        print(f"\n{len(changed)} slug(s) would move, {sum(touched.values())} header(s) would be wrapped.")
        return 0

    for path in source_files():
        if after_texts[path.name] != worktree[path.name]:
            path.write_text(after_texts[path.name], encoding="utf-8")
    ALIASES.write_text(json.dumps(aliases, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    for f, n in sorted(touched.items()):
        print(f"  {f:16} {n:3} header(s) wrapped")
    print(f"\n{sum(touched.values())} header(s) wrapped, "
          f"{len(changed)} slug(s) moved, {len(aliases)} alias(es) recorded.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
