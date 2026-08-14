#!/usr/bin/env python3
"""
gen_cheatsheet.py — Builds CALCULUS-CHEAT-SHEET.md from the Math domain.

The file used to claim "Generated from the Math domain" while actually being a
hand-transcription of one card out of sixteen. This makes the claim true: every
section below comes from data/math.html, so the printable sheet cannot drift
from the site.

Only the reference material is emitted — tables, prose callouts and code
blocks. SVG diagrams are noted with a pointer to the site rather than being
mangled into text, because a labelled triangle does not survive markdown.

Usage:
    python3 tools/gen_cheatsheet.py            # write the file
    python3 tools/gen_cheatsheet.py --check    # fail if it is stale (CI)
"""

import html as html_lib
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "data" / "math.html"
OUTPUT = ROOT / "CALCULUS-CHEAT-SHEET.md"

# Prettier splits tags across lines, so every pattern here tolerates a newline
# before the closing angle bracket — the same rule lint_content.py follows.
TOPIC_START_RE = re.compile(r'<div class="topic"')
TOPIC_NAME_RE = re.compile(r'<span\b[^>]*class="topic-name"[^>]*>(.*?)</span\s*>', re.S)
TOPIC_BADGE_RE = re.compile(r'<span\b[^>]*class="topic-badge"[^>]*>(.*?)</span\s*>', re.S)
CARD_START_RE = re.compile(r'<div class="concept-card">')
LABEL_RE = re.compile(r'<span\b[^>]*class="concept-label"[^>]*>(.*?)</span\s*>', re.S)
TITLE_RE = re.compile(r'<h4\b[^>]*class="concept-title"[^>]*>(.*?)</h4\s*>', re.S)
DESC_RE = re.compile(r'<p\b[^>]*class="concept-desc"[^>]*>(.*?)</p\s*>', re.S)
TABLE_RE = re.compile(r'<table\b[^>]*class="ref-table"[^>]*>(.*?)</table\s*>', re.S)
ROW_RE = re.compile(r"<tr\b[^>]*>(.*?)</tr\s*>", re.S)
CELL_RE = re.compile(r"<(th|td)\b[^>]*>(.*?)</\1\s*>", re.S)
PRE_RE = re.compile(r'<pre\b[^>]*class="code-block"[^>]*>(.*?)</pre\s*>', re.S)
SVG_RE = re.compile(r"<svg\b.*?</svg\s*>", re.S)

# The annotator owns these; they are generated decoration and would otherwise
# make the output churn every time it runs.
ACRO_SPAN_RE = re.compile(r'\s*<span class="acro-exp">\([^<]*?\)</span\s*>')


def inline(fragment):
    """HTML fragment -> plain text, preserving how the site reads mathematics.

    <sub>/<sup> carry real meaning in a formula, so they are transliterated
    rather than dropped: `x<sup>n+1</sup>` must not become `xn+1`.
    """
    s = ACRO_SPAN_RE.sub("", fragment)
    s = re.sub(r"<br\s*/?>", "; ", s)
    s = re.sub(r"<sub\b[^>]*>(.*?)</sub\s*>", r"_\1", s, flags=re.S)
    s = re.sub(r"<sup\b[^>]*>(.*?)</sup\s*>", r"^(\1)", s, flags=re.S)
    s = re.sub(r"<[^>]+>", "", s)
    s = html_lib.unescape(s)
    s = s.replace("\xa0", " ")
    return re.sub(r"\s+", " ", s).strip()


def cell(fragment):
    """Inline text safe to drop between table pipes.

    Calculus is full of absolute-value bars, and `ln|x| + C` in a two-column
    row silently renders as four columns. The old hand-written sheet had
    exactly that bug in two tables.
    """
    return inline(fragment).replace("|", r"\|")


def blocks(text, start_re):
    """(html,) for each region beginning at start_re, up to the next one."""
    lines = text.splitlines(keepends=True)
    starts = [i for i, l in enumerate(lines) if start_re.search(l)]
    for n, i in enumerate(starts):
        end = starts[n + 1] if n + 1 < len(starts) else len(lines)
        yield "".join(lines[i:end])


def render_table(inner):
    rows = [
        [cell(c) for _, c in CELL_RE.findall(row)]
        for row in ROW_RE.findall(inner)
    ]
    rows = [r for r in rows if r]
    if not rows:
        return []
    width = max(len(r) for r in rows)
    rows = [r + [""] * (width - len(r)) for r in rows]
    head, body = rows[0], rows[1:]
    out = ["| " + " | ".join(head) + " |", "|" + "---|" * width]
    out += ["| " + " | ".join(r) + " |" for r in body]
    return out + [""]


def render_card(html):
    """One .concept-card -> markdown, in the order the elements appear."""
    label = LABEL_RE.search(html)
    title = TITLE_RE.search(html)
    label = inline(label.group(1)) if label else ""
    title = inline(title.group(1)) if title else ""

    heading = f"{title} — {label}" if title and label else (title or label)
    out = [f"### {heading}" if heading else "###", ""]

    # Walk the card in document order so a note that follows a table stays
    # after it. Position-keyed, because these element types interleave.
    parts = []
    for m in TABLE_RE.finditer(html):
        parts.append((m.start(), render_table(m.group(1))))
    for m in DESC_RE.finditer(html):
        parts.append((m.start(), [inline(m.group(1)), ""]))
    for m in PRE_RE.finditer(html):
        code = ACRO_SPAN_RE.sub("", m.group(1))
        code = html_lib.unescape(re.sub(r"<[^>]+>", "", code)).strip("\n")
        parts.append((m.start(), ["```", *code.split("\n"), "```", ""]))
    for m in SVG_RE.finditer(html):
        parts.append((m.start(), ["*(diagram — see this card on the site)*", ""]))

    for _, lines in sorted(parts, key=lambda p: p[0]):
        out += lines
    return out


def build():
    text = SOURCE.read_text(encoding="utf-8")
    topics = []

    for block in blocks(text, TOPIC_START_RE):
        name = TOPIC_NAME_RE.search(block)
        if not name:
            continue
        badge = TOPIC_BADGE_RE.search(block)
        body = block[name.end():]
        cards = [render_card(c) for c in blocks(body, CARD_START_RE)]
        topics.append((inline(name.group(1)), inline(badge.group(1)) if badge else "", cards))

    n_cards = sum(len(c) for _, _, c in topics)
    out = [
        "# Calculus Cheat Sheet",
        "",
        "> **Generated** from `data/math.html` by `tools/gen_cheatsheet.py`.",
        "> Do not edit by hand — run the generator after changing the Math domain.",
        "",
        f"Every formula here also lives on the site as a flashcard and quiz question. "
        f"{len(topics)} topics, {n_cards} sections.",
        "",
        "## Contents",
        "",
    ]

    for name, badge, _ in topics:
        anchor = re.sub(r"[^\w\s-]", "", name.lower()).strip()
        anchor = re.sub(r"[\s_]+", "-", anchor)
        suffix = f" — {badge}" if badge else ""
        out.append(f"- [{name}](#{anchor}){suffix}")
    out.append("")

    for name, _, cards in topics:
        out += ["---", "", f"## {name}", ""]
        for card in cards:
            out += card

    # Collapse the runs of blank lines the section joins leave behind.
    lines, prev_blank = [], False
    for line in out:
        blank = not line.strip()
        if not (blank and prev_blank):
            lines.append(line)
        prev_blank = blank
    return "\n".join(lines).rstrip() + "\n"


def main():
    content = build()
    if "--check" in sys.argv:
        current = OUTPUT.read_text(encoding="utf-8") if OUTPUT.exists() else ""
        if current != content:
            print(
                f"::error::{OUTPUT.name} is out of date. "
                f"Run 'python tools/gen_cheatsheet.py' and commit the result."
            )
            return 1
        print(f"{OUTPUT.name} is up to date.")
        return 0

    OUTPUT.write_text(content, encoding="utf-8")
    print(f"Wrote {OUTPUT.name} — {len(content.splitlines())} lines.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
