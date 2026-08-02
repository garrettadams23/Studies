#!/usr/bin/env python3
"""
gen_acronym_domain.py — Builds data/acronym.html from data/acronyms.json.

data/acronyms.json is the single source of truth for every acronym expansion on
the site. This script renders it as the "Acronym Dictionary" domain: one topic
per letter plus one topic per subject category, using the standard `.topic` /
`.concept-card` / `.ref-table` markup from CONTRIBUTING.md.

Usage:
    python3 tools/gen_acronym_domain.py && python3 build.py
"""

import html
import json
import re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "data" / "acronyms.json"
OUT = ROOT / "data" / "acronym.html"

# Icons keep the per-letter topics visually distinct from the category topics.
LETTER_ICON = "🔤"
CATEGORY_ICONS = {
    "AI": "🤖",
    "Business": "💼",
    "Certifications": "🎓",
    "Cloud": "☁️",
    "Compliance": "⚖️",
    "Cryptography": "🔑",
    "Data": "📊",
    "DevOps": "🔁",
    "Endpoint": "🖥️",
    "Engineering": "🏛️",
    "Government": "🎖️",
    "Hardware": "🔧",
    "Linux": "🐧",
    "Microsoft": "🪟",
    "Misc": "🧩",
    "Networking": "🌐",
    "Operations": "🔬",
    "Organizations": "🏢",
    "Risk": "⚠️",
    "Security": "🔐",
    "Standards": "📐",
    "Storage": "💾",
    "Systems": "⚙️",
    "Virtualization": "📦",
    "Web": "🕸️",
    "Windows": "🪟",
}


def esc(s):
    return html.escape(s, quote=False)


def load_entries():
    data = json.loads(SRC.read_text(encoding="utf-8"))
    return data["entries"]


def bucket_letter(acronym):
    """Group key for the A–Z topics; anything not starting a–z lands in 0–9."""
    first = acronym[0].upper()
    return first if "A" <= first <= "Z" else "0–9"


def meanings_cell(meanings):
    """Render one or more meanings for a single acronym as a table cell body."""
    parts = []
    for m in meanings:
        chunk = f'<strong class="c-cyan">{esc(m["e"])}</strong>'
        if m.get("n"):
            chunk += f'<br /><span class="c-muted">{esc(m["n"])}</span>'
        parts.append(chunk)
    return '<br /><span class="c-muted">— or —</span><br />'.join(parts)


def render_table(entries, show_category=True):
    head = (
        "<tr><th>Acronym</th><th>Stands For</th>"
        + ("<th>Area</th>" if show_category else "")
        + "</tr>"
    )
    rows = []
    for e in entries:
        cats = " · ".join(dict.fromkeys(m["c"] for m in e["m"]))
        cat_cell = f"<td>{esc(cats)}</td>" if show_category else ""
        rows.append(
            "<tr>"
            f'<td><strong class="c-amber">{esc(e["a"])}</strong></td>'
            f'<td>{meanings_cell(e["m"])}</td>'
            f"{cat_cell}"
            "</tr>"
        )
    return (
        '<table class="ref-table">\n'
        f"  <thead>{head}</thead>\n"
        "  <tbody>\n    " + "\n    ".join(rows) + "\n  </tbody>\n"
        "</table>"
    )


def topic(icon, name, badge, label, title, desc, body):
    return f"""\
          <!-- ── TOPIC: {name.upper()} ─────────────────────────────── -->
          <div class="topic">
            <div class="topic-header">
              <span class="topic-icon">{icon}</span>
              <span class="topic-name">{esc(name)}</span>
              <span class="topic-badge">{esc(badge)}</span>
              <span class="topic-chev">▶</span>
            </div>
            <div class="topic-body">
              <div class="concept-card">
                <div class="concept-label">{esc(label)}</div>
                <div class="concept-title">{esc(title)}</div>
                <div class="concept-desc">{desc}</div>
                <div class="dw">
{body}
                </div>
              </div>
            </div>
          </div>"""


def main():
    entries = load_entries()

    by_letter = defaultdict(list)
    by_category = defaultdict(list)
    for e in entries:
        by_letter[bucket_letter(e["a"])].append(e)
        for cat in dict.fromkeys(m["c"] for m in e["m"]):
            by_category[cat].append(e)

    total_meanings = sum(len(e["m"]) for e in entries)
    letters = sorted(by_letter, key=lambda k: (k != "0–9", k))

    sections = []

    # ── Overview topic ────────────────────────────────────────────────────
    index_links = " · ".join(
        f'<strong class="c-cyan">{esc(l)}</strong> <span class="c-muted">'
        f"({len(by_letter[l])})</span>"
        for l in letters
    )
    cat_rows = "\n    ".join(
        f"<tr><td>{CATEGORY_ICONS.get(c, '•')} <strong class=\"c-amber\">{esc(c)}</strong></td>"
        f"<td>{len(by_category[c])}</td></tr>"
        for c in sorted(by_category)
    )
    overview_body = (
        '                  <table class="ref-table">\n'
        "                    <thead><tr><th>Area</th><th>Acronyms</th></tr></thead>\n"
        f"                    <tbody>\n    {cat_rows}\n                    </tbody>\n"
        "                  </table>"
    )
    sections.append(
        topic(
            "📖",
            "How to Use This Dictionary",
            "START HERE",
            "Overview",
            f"{len(entries)} acronyms · {total_meanings} meanings",
            "Every acronym used anywhere on this site is expanded inline the first "
            "time it appears in a topic — the grey text in brackets beside it. This "
            "domain is the full lookup table: browse "
            "<strong>A&nbsp;–&nbsp;Z</strong> below, jump to a subject area, or use "
            "the search box at the top of the page (it matches both the acronym and "
            "what it stands for). Where an acronym means more than one thing, every "
            f"meaning is listed. Letter index: {index_links}.",
            overview_body,
        )
    )

    # ── A–Z topics ────────────────────────────────────────────────────────
    for letter in letters:
        group = by_letter[letter]
        sections.append(
            topic(
                LETTER_ICON,
                f"Acronyms — {letter}",
                f"{len(group)} TERMS",
                "A–Z Index",
                f"{letter} — {len(group)} acronyms",
                f"Every acronym in the dictionary beginning with "
                f"<strong>{esc(letter)}</strong>, with each meaning it carries in IT.",
                "                  " + render_table(group),
            )
        )

    # ── Category topics ───────────────────────────────────────────────────
    for cat in sorted(by_category):
        group = sorted(by_category[cat], key=lambda e: e["a"].upper())
        sections.append(
            topic(
                CATEGORY_ICONS.get(cat, "🧩"),
                f"By Area — {cat}",
                f"{len(group)} TERMS",
                "Subject Index",
                f"{cat} acronyms",
                f"The {len(group)} dictionary entries that belong to "
                f"<strong>{esc(cat)}</strong>.",
                "                  " + render_table(group, show_category=False),
            )
        )

    header = (
        "<!-- ══════════════════════════════════════════════════════════════\n"
        "     GENERATED FILE — do not hand-edit.\n"
        "     Source: data/acronyms.json\n"
        "     Regenerate: python3 tools/gen_acronym_domain.py && python3 build.py\n"
        "     ══════════════════════════════════════════════════════════════ -->\n"
    )
    OUT.write_text(header + "\n\n".join(sections) + "\n", encoding="utf-8")
    print(
        f"Wrote {OUT.relative_to(ROOT)}: {len(entries)} acronyms, "
        f"{total_meanings} meanings, {len(sections)} topics"
    )


if __name__ == "__main__":
    main()
