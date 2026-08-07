#!/usr/bin/env python3
"""
lint_content.py — Enforces CONTRIBUTING.md mechanically.

Errors fail the build. Warnings are counted and printed as a single trend line,
so historical debt (90 topics with no `.topic-name`, 148 hard-coded colours)
gets tracked rather than either blocking work or being quietly forgotten.

Usage:
    python3 tools/lint_content.py             # errors fail, warnings reported
    python3 tools/lint_content.py --strict     # warnings fail too
"""

import collections
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"

VOID = {"br", "hr", "img", "input", "meta", "link", "source", "col"}


class Nesting(HTMLParser):
    """Reports tags that are never closed, and closing tags with no opener."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack, self.unclosed, self.stray = [], [], []

    def handle_startendtag(self, tag, attrs):
        # `<br />`, `<line ... />`: self-closing, therefore inherently balanced.
        # The base class would otherwise fire starttag *and* endtag, and a void
        # element skipped on the way in becomes a stray close on the way out.
        return

    def handle_starttag(self, tag, attrs):
        if tag not in VOID:
            self.stack.append((tag, self.getpos()[0]))

    def handle_endtag(self, tag):
        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i][0] == tag:
                self.unclosed.extend(self.stack[i + 1:])
                del self.stack[i:]
                return
        self.stray.append((tag, self.getpos()[0]))


def slugify(s):
    """Byte-for-byte port of slugify() in script.js.

    JavaScript's \\w is ASCII-only; Python's is Unicode-aware by default, so
    without re.ASCII the two disagree the moment a title contains an accent —
    exactly the drift a slug guard exists to catch. Every title is ASCII today,
    which is precisely why the bug would go unnoticed.
    """
    s = s.lower()
    s = re.sub(r"[^\w\s-]", "", s, flags=re.ASCII)
    s = s.strip()
    s = re.sub(r"[\s_]+", "-", s)
    s = re.sub(r"-+", "-", s)
    return s[:60] or "topic"


ACRO_SPAN_RE = re.compile(r'\s*<span class="acro-exp">\([^<]*?\)</span\s*>')
TOPIC_START_RE = re.compile(r'<div class="topic"')

# Prettier splits tags across lines — `<span class="topic-name"\n  >` and
# `</span\n>` are both valid and both appear in data/*.html. Every pattern that
# matches markup here has to tolerate that, or it silently under-reports.
TOPIC_NAME_RE = re.compile(r'<span\b[^>]*class="topic-name"[^>]*>(.*?)</span\s*>', re.S)
TOPIC_HEADER_RE = re.compile(r'<div\b[^>]*class="topic-header"[^>]*>(.*?)</div\s*>', re.S)


def topic_blocks(text):
    """(line_number, html) for each .topic, up to the next one."""
    lines = text.splitlines(keepends=True)
    starts = [i for i, l in enumerate(lines) if TOPIC_START_RE.search(l)]
    for n, i in enumerate(starts):
        end = starts[n + 1] if n + 1 < len(starts) else len(lines)
        yield i + 1, "".join(lines[i:end])


def topic_label(block):
    """What script.js would use as the slug source, expansions removed."""
    plain = ACRO_SPAN_RE.sub("", block)
    m = TOPIC_NAME_RE.search(plain)
    if m:
        raw = m.group(1)
    else:
        h = TOPIC_HEADER_RE.search(plain)
        raw = h.group(1) if h else ""
    from html import unescape
    return unescape(re.sub(r"<[^>]+>", "", raw)).strip(), bool(m)


def main():
    strict = "--strict" in sys.argv
    errors, warns = [], collections.Counter()
    seen_slugs = {}

    # Domain order matters: script.js walks .domain-section in document order,
    # so a collision is only real if it survives that ordering.
    import json
    order = [d["id"] for d in json.loads((DATA / "domains.json").read_text())]
    files = [DATA / f"{d}.html" for d in order if (DATA / f"{d}.html").exists()]

    for path in files:
        text = path.read_text(encoding="utf-8")
        name = path.name

        parser = Nesting()
        parser.feed(f"<div>{text}</div>")
        for tag, line in parser.unclosed + parser.stack[1:]:
            errors.append(f"{name}:{line}: unclosed <{tag}>")
        for tag, line in parser.stray:
            errors.append(f"{name}:{line}: stray </{tag}>")

        for m in TOPIC_HEADER_RE.finditer(text):
            if re.search(r"<h[1-6]\b", m.group(1)):
                line = text[: m.start()].count("\n") + 1
                errors.append(
                    f"{name}:{line}: heading tag inside .topic-header — the title is "
                    f"styled by .topic-name; a nested <h3> renders a size larger than "
                    f"every neighbouring card"
                )

        if "topic-chevron" in text:
            errors.append(f"{name}: uses banned class 'topic-chevron' (use 'topic-chev')")

        for line_no, block in topic_blocks(text):
            label, has_name = topic_label(block)
            if not has_name:
                # Was a warning for two sessions and nobody acted on it. It only
                # became interesting once it produced a visible bug: the label
                # falls back to the header's textContent, which swallows the
                # badge word and the injected ★ ✓ 🔗 buttons, so the flashcard,
                # the quiz option and the study-list row all read wrong.
                errors.append(
                    f"{name}:{line_no}: topic title is a bare text node — wrap it in "
                    f'<span class="topic-name">. Run: python tools/fix_topic_names.py'
                )
            if not label:
                errors.append(f"{name}:{line_no}: topic has no usable title")
                continue
            base = slugify(label)
            slug, i = base, 2
            while slug in seen_slugs:
                slug = f"{base}-{i}"
                i += 1
            if i > 2:
                first = seen_slugs[base]
                warns["slug collision (auto-suffixed)"] += 1
                errors.append(
                    f"{name}:{line_no}: slug '{base}' already used by {first} "
                    f"— permalinks shift; rename one of them"
                )
            seen_slugs[slug] = f"{name}:{line_no}"

        # The annotator owns this class; hand-written ones get stripped silently.
        for m in re.finditer(r'<span class="acro-exp">', text):
            pass  # presence is fine — they are generated; see --check on the annotator

        warns["hard-coded hex colour"] += len(re.findall(r"#[0-9a-fA-F]{3,6}\b", text))
        warns["inline style attribute"] += len(re.findall(r'\bstyle="', text))
        warns["ai-table (prefer ref-table)"] += text.count('class="ai-table"')

    print(f"Linted {len(files)} domain files, {len(seen_slugs)} topics.\n")
    if errors:
        print(f"ERRORS ({len(errors)}):")
        for e in errors[:40]:
            print(f"  {e}")
        if len(errors) > 40:
            print(f"  … and {len(errors) - 40} more")
        print()
    print("Warnings (tracked, not blocking):")
    for k, v in sorted(warns.items(), key=lambda kv: -kv[1]):
        print(f"  {v:>6}  {k}")
    print(f"\nTREND {' '.join(f'{k.split()[0]}={v}' for k, v in sorted(warns.items()))}")

    if errors:
        return 1
    if strict and sum(warns.values()):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
