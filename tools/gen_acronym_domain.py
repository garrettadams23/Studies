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
import sys
from textwrap import indent
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


ANATOMY_SVG = """\
<svg class="acro-svg" viewBox="0 0 1120 470" role="img" aria-labelledby="acrosvg-t acrosvg-d" preserveAspectRatio="xMidYMid meet">
  <title id="acrosvg-t">How an acronym is recorded and shown</title>
  <desc id="acrosvg-d">An acronym breaks into the words its letters stand for. On a topic page the expansion is added in brackets beside its first use. In this dictionary the same acronym is stored with its expansion, subject area, an optional note, and every other meaning it carries.</desc>

  <!-- ── 1. the letters ────────────────────────────────────────────────── -->
  <g class="acs-panel">
    <rect x="24" y="28" width="410" height="200" rx="12" />
  </g>
  <text class="acs-step" x="48" y="60">1 · What the letters stand for</text>
  <g class="acs-letters">
    <rect class="acs-letter" x="48" y="82" width="40" height="34" rx="5" />
    <text class="acs-letter-t" x="68" y="106">U</text>
    <text class="acs-word" x="104" y="106">Unified</text>

    <rect class="acs-letter" x="48" y="126" width="40" height="34" rx="5" />
    <text class="acs-letter-t" x="68" y="150">E</text>
    <text class="acs-word" x="104" y="150">Endpoint</text>

    <rect class="acs-letter" x="48" y="170" width="40" height="34" rx="5" />
    <text class="acs-letter-t" x="68" y="194">M</text>
    <text class="acs-word" x="104" y="194">Management</text>
  </g>
  <text class="acs-aside" x="268" y="150">an initialism —</text>
  <text class="acs-aside" x="268" y="172">read letter by</text>
  <text class="acs-aside" x="268" y="194">letter, not a word</text>

  <!-- ── 2. how it appears in a topic ──────────────────────────────────── -->
  <g class="acs-panel">
    <rect x="466" y="28" width="630" height="200" rx="12" />
  </g>
  <text class="acs-step" x="490" y="60">2 · Where you meet it in a topic</text>

  <rect class="acs-mockbox" x="490" y="80" width="582" height="52" rx="6" />
  <text class="acs-mock" x="510" y="112">Enrol the device in</text>
  <text class="acs-term" x="692" y="112">UEM</text>
  <text class="acs-exp" x="742" y="112">(Unified Endpoint Management)</text>

  <polyline class="acs-lead" points="708,134 708,160 620,160" />
  <text class="acs-callout acs-callout-r" x="612" y="164">the acronym</text>

  <polyline class="acs-lead acs-lead-muted" points="852,134 852,190 898,190" />
  <text class="acs-callout acs-callout-dim" x="906" y="184">added on its</text>
  <text class="acs-callout acs-callout-dim" x="906" y="204">first use in a topic</text>

  <!-- ── 3. the dictionary entry ───────────────────────────────────────── -->
  <g class="acs-panel">
    <rect x="24" y="256" width="1072" height="190" rx="12" />
  </g>
  <text class="acs-step" x="48" y="288">3 · What the dictionary stores</text>

  <line class="acs-rule" x1="48" y1="302" x2="640" y2="302" />
  <text class="acs-key" x="48" y="330">Acronym</text>
  <text class="acs-val acs-val-term" x="230" y="330">UEM</text>
  <line class="acs-rule" x1="48" y1="344" x2="640" y2="344" />
  <text class="acs-key" x="48" y="372">Stands for</text>
  <text class="acs-val" x="230" y="372">Unified Endpoint Management</text>
  <line class="acs-rule" x1="48" y1="386" x2="640" y2="386" />
  <text class="acs-key" x="48" y="414">Area</text>
  <text class="acs-val acs-val-dim" x="230" y="414">Endpoint</text>

  <line class="acs-divider" x1="680" y1="296" x2="680" y2="424" />
  <text class="acs-step acs-step-alt" x="712" y="306">When one acronym means several things</text>
  <text class="acs-alt-term" x="712" y="348">MAC</text>
  <text class="acs-alt" x="776" y="348">Media Access Control</text>
  <text class="acs-alt" x="776" y="374">Mandatory Access Control</text>
  <text class="acs-alt" x="776" y="400">Message Authentication Code</text>
  <text class="acs-alt-dim" x="712" y="428">only the one that fits the topic is shown inline</text>
</svg>
"""


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
        indent(ANATOMY_SVG, "                  ") + "\n"
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
    content = header + "\n\n".join(sections) + "\n"
    summary = (f"{len(entries)} acronyms, {total_meanings} meanings, "
               f"{len(sections)} topics")

    # --check exists because the CI equivalent — run the generator, then
    # `git diff --exit-code` — leaves the tree dirty on a machine where somebody
    # is working, so nobody runs it locally. Four acronyms (DB, GIL, HA, PCI) sat
    # in the dictionary and out of the domain for nine commits, along with a
    # whole subject group, while CI said so on every push and the message was in
    # a job step that only ever ran on the server.
    if "--check" in sys.argv:
        current = OUT.read_text(encoding="utf-8") if OUT.exists() else ""
        if current != content:
            print(
                f"::error::{OUT.relative_to(ROOT)} is out of date "
                f"(the dictionary now has {summary}). "
                f"Run 'python3 tools/gen_acronym_domain.py && python3 build.py' "
                f"and commit the result."
            )
            return 1
        print(f"{OUT.relative_to(ROOT)} is up to date — {summary}.")
        return 0

    OUT.write_text(content, encoding="utf-8")
    print(f"Wrote {OUT.relative_to(ROOT)}: {summary}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
