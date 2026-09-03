#!/usr/bin/env python3
"""
lint_content.py — Enforces CONTRIBUTING.md mechanically.

Errors fail the build. Warnings are counted and printed as a single trend line,
so historical debt gets tracked rather than either blocking work or being
quietly forgotten.

A warning is only worth tracking if someone is accountable for the number. Two
have graduated to errors once their count reached zero, which turns them into
ratchets — they can no longer regress:

  * topics with no `.topic-name` (was 90)
  * hard-coded colours (was 148, of which 8 were never colours at all)

`inline style attribute` is the third, and it graduated differently, because it
can never reach zero: 806 of them colour the first cell of a `.ref-table`, where
a utility class provably cannot win on specificity. So it is a **ceiling**
rather than a zero — the count may fall and may not rise. It was 2,707 when the
ceiling was introduced and 1,565 immediately after, because 1,142 of them were
one shape (`.concept-desc` with a top margin) that already had a class name.

`ai-table` is no longer a warning at all. It was labelled "prefer ref-table",
which asserted a preference nobody had agreed and the stylesheet contradicts:
the two are different designs (12px versus ~14px text, and an amber versus a
white first column), so converting 360 tables across 18 domains would be a
visible redesign, not a cleanup. It is reported as a census line instead.

Usage:
    python3 tools/lint_content.py             # errors fail, warnings reported
    python3 tools/lint_content.py --strict     # warnings fail too
"""

import collections
import re
import sys
from datetime import datetime, timezone
from html import unescape
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"

VOID = {"br", "hr", "img", "input", "meta", "link", "source", "col"}

# Counts that may fall and may not rise. Lower a number here in the same commit
# that earns it; raising one needs a reason written beside it.
#
# "table with no verdict" went 513 -> 748 when the rule was corrected, and that
# is not a relaxation: the old rule looked 260 characters past the table and
# accepted whatever prose it found, including the *next card's*. 288 cards that
# genuinely end on a table were passing because the card after them opened with
# a paragraph. The reason is written out in tables_without_verdict() below, with
# the decomposition — 460 flagged by both rules, 39 the old rule got wrong, 288
# it never saw.
#
# 748 -> 712 in that same commit: every card in `career` that ended on a table
# now ends on a judgement instead. 36 written by hand, none of them filler.
CEILINGS = {"inline style attribute": 1565, "table with no verdict": 712}


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


# ── Where a domain's source lives ───────────────────────────────────────────
# A domain is normally one file, `data/<id>.html`. A domain that has outgrown
# one file is split into ordered parts — `data/<id>.01-name.html`,
# `data/<id>.02-name.html` — which build.py concatenates in filename order.
#
# The parts build into the *same* domain, which is the whole point: the topic
# order is unchanged, so every slug, permalink and stored progress key survives
# a split untouched. Splitting into a new *domain* would not.


def domain_files(domain_id, data_dir=None):
    """The source files for one domain, in build order."""
    data_dir = data_dir or DATA
    single = data_dir / f"{domain_id}.html"
    parts = sorted(data_dir.glob(f"{domain_id}.*.html"))
    if single.exists():
        if parts:
            raise SystemExit(
                f"error: {domain_id} has both {single.name} and "
                f"{len(parts)} part file(s). Pick one — a domain is either one "
                f"file or a set of parts, never both.")
        return [single]
    return parts


def domain_of(path):
    """The domain a source file belongs to: `script.03-python.html` -> `script`."""
    return path.name.split(".", 1)[0]


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


# A colour literal only matters where it is actually used as a colour. The old
# check was a bare `#[0-9a-fA-F]{3,6}` sweep, which also counted "deploy #4521",
# "invoice #4471" and every CSS sample that teaches hex notation — 8 of the 148
# it reported were not colours at all. A counter nobody can drive to zero is
# decoration, so this matches the claim instead: a literal in a style attribute
# or in an SVG paint attribute.
STYLE_ATTR_RE = re.compile(r'\bstyle="([^"]*)"', re.S)
PAINT_ATTR_RE = re.compile(
    r'\b(?:fill|stroke|stop-color|flood-color|lighting-color|bgcolor|color)\s*=\s*'
    r'"(#[0-9a-fA-F]{3,8})"'
)
HEX_RE = re.compile(r"#[0-9a-fA-F]{3,8}\b")


def hex_colours(text):
    """(line_number, literal) for each hex used as a colour."""
    for m in STYLE_ATTR_RE.finditer(text):
        for h in HEX_RE.finditer(m.group(1)):
            yield text[: m.start()].count("\n") + 1, h.group(0)
    for m in PAINT_ATTR_RE.finditer(text):
        yield text[: m.start()].count("\n") + 1, m.group(1)


# `.ref-table td:first-child` sets colour at specificity (0,2,1); a `c-*` utility
# class is (0,1,0) and loses. 1614 first cells carried one that had never once
# rendered — boilerplate applied to a column the design already styles. They were
# removed, so this guards the count at zero rather than letting it creep back.
# Both table styles colour their own first column at (0,2,1) — `.ref-table
# td:first-child` and `.ai-table td:first-child` — so a utility class loses to
# either. `.ai-table` has never carried a dead class; the guard covers it so it
# never starts.
REF_TABLE_RE = re.compile(
    r'<table\b[^>]*class="(?:ref-table|ai-table)"[^>]*>.*?</table\s*>', re.S)
ROW_RE = re.compile(r"<tr\b[^>]*>.*?</tr\s*>", re.S)
FIRST_CELL_RE = re.compile(r"<(td|th)\b([^>]*)>")
COLOUR_CLASS_RE = re.compile(r"\bc-(?:cyan|green|amber|red|purple|muted)\b")


def dead_first_cell_classes(text):
    """(line_number, class) for colour classes that cannot render."""
    for table in REF_TABLE_RE.finditer(text):
        for row in ROW_RE.finditer(table.group(0)):
            cell = FIRST_CELL_RE.search(row.group(0))
            if not cell or cell.group(1) != "td":
                continue
            hit = COLOUR_CLASS_RE.search(cell.group(2) or "")
            if hit:
                at = table.start() + row.start() + cell.start()
                yield text[:at].count("\n") + 1, hit.group(0)


# A volatile claim is marked where the claim is, not where the topic is. The
# keyword heuristic this replaces flagged 184 of 888 topics — including "Google
# Chrome — Keyboard Shortcuts" and "Access Control Models" — because prose
# mentioned "console" or "tier". A convention only sticks if it can be checked,
# so the shape is enforced here before anything is asked to rely on it.
VOLATILE_RE = re.compile(r'<(\w+)\b([^>]*\bclass="[^"]*\bvolatile\b[^"]*"[^>]*)>')
CHECKED_RE = re.compile(r'\bdata-checked="([^"]*)"')
STRAY_CHECKED_RE = re.compile(r'<(\w+)\b([^>]*\bdata-checked="[^"]*"[^>]*)>')


# `.concept-desc.verdict` exists precisely for the sentence that follows a table.
# 1,142 cards wrote it as an inline margin first; this keeps them converted.
VERDICT_MARGIN_RE = re.compile(
    r'<\w+ class="concept-desc"[^>]*\bstyle="[^"]*\bmargin-top\s*:')


def verdict_margins(text):
    """Line numbers where a .concept-desc sets its top margin inline."""
    for m in VERDICT_MARGIN_RE.finditer(text):
        yield text[: m.start()].count("\n") + 1


# Phase 10 T3. `style.css` has asserted "every table gets a verdict" since the
# `.verdict` class was introduced, and nothing has ever checked it. Measured at
# introduction: 2,098 tables site-wide, 565 followed by nothing at all.
#
# A warning with a ceiling rather than an error, for the same reason the inline
# style count is: the number is too large to clear in one pass, and a few are
# legitimate — a reference table in `shortcut` needs no verdict, which is why
# that domain and the generated `acronym` domain are excluded outright.
VERDICT_EXEMPT = {"shortcut", "acronym"}
_CARD_RE = re.compile(r'<div class="concept-card">')


def tables_without_verdict(text):
    """Line numbers where a *card* ends on a table and says nothing after it.

    This used to be "a table with no `.concept-desc` in the next 260
    characters", which is a different and worse question. A card that lays out
    three reference tables under three `.dt` headings was counted three times,
    and the fix it implied — prose wedged between two tables that belong
    together — makes the card worse, not better.

    It was also wrong in the other and larger direction. 260 characters reaches
    past the end of a short card, so a card that ended on a table and was
    followed by a card opening with a paragraph counted as satisfied. Decomposed
    against the corrected rule:

        460   flagged by both — real, and were being counted
         39   old rule only — mid-card tables, the wrong edit to ask for
        288   new rule only — the window bled into the next card

    So the backlog was never 499. It is 748, and it was under-reported by more
    than a third for as long as the rule has existed.

    A card whose last element is a table has genuinely left the reader with data
    and no judgement, which is what `.concept-desc.verdict` is for.
    """
    starts = [m.start() for m in _CARD_RE.finditer(text)]
    bounds = list(zip(starts, starts[1:] + [len(text)]))
    for m in re.finditer(r"</table\s*>", text):
        card_end = next((e for s, e in bounds if s <= m.start() < e), None)
        if card_end is None:
            continue  # a table outside any concept card — not this rule's business
        if "concept-desc" not in text[m.end():card_end]:
            yield text[: m.start()].count("\n") + 1


def volatile_problems(text, today):
    """(line_number, message) for malformed volatile-claim markup."""
    for m in VOLATILE_RE.finditer(text):
        line = text[: m.start()].count("\n") + 1
        got = CHECKED_RE.search(m.group(2))
        if not got:
            yield line, ('class="volatile" without data-checked — the mark is '
                         'only useful if it says when the claim was verified')
            continue
        stamp = got.group(1)
        if not re.fullmatch(r"\d{4}-(0[1-9]|1[0-2])", stamp):
            yield line, f'data-checked="{stamp}" is not a YYYY-MM month'
        elif stamp > today:
            yield line, f'data-checked="{stamp}" is in the future (now {today})'

    for m in STRAY_CHECKED_RE.finditer(text):
        if "volatile" in m.group(2):
            continue
        line = text[: m.start()].count("\n") + 1
        yield line, ('data-checked without class="volatile" — nothing reads it, '
                     'so the claim will not appear in the freshness report')


# A card that says "see X in the Security domain" is making a claim about the
# site, and prose cannot be checked — four such references were already dangling
# when this was written, two of them naming cards that had been retitled and one
# naming a card that never existed. Cross-references use an explicit span so the
# target can be verified:
#
#     <span class="xref">Exact Topic Title</span>
XREF_RE = re.compile(r'<span class="xref">(.*?)</span\s*>', re.S)


def xref_targets(text):
    """(line_number, title) for each cross-reference in a file."""
    for m in XREF_RE.finditer(text):
        # The acronym annotator injects expansions inside any element, this span
        # included, so strip them exactly as topic_label() does — otherwise a
        # reference breaks the first time the annotator runs over it.
        title = unescape(re.sub(r"<[^>]+>", "", ACRO_SPAN_RE.sub("", m.group(1))))
        yield text[: m.start()].count("\n") + 1, re.sub(r"\s+", " ", title).strip()


def ambiguous_acronyms(files):
    """Ambiguous acronyms that are actually *rendered* in two or more domains.

    The annotator expands one way everywhere, confidently, and a wrong expansion
    is well-formed markup — so no other check can see it. DFS was rendered as
    "Dynamic Frequency Selection" inside a data-structures table and twice more
    in Windows Server file-services cards, while the entry's own note already
    read "Also Distributed File System".

    Exposure, not theory. An earlier version flagged every entry whose note
    contained "also", which caught COPE ("a device the user may also use
    personally") and FIFO ("a Unix named pipe is also called a FIFO") — notes
    describing a synonym, not a second meaning — and entries never annotated
    anywhere. Requiring two rendered domains drops those and leaves the ones a
    future card could genuinely get wrong.
    """
    import json
    entries = json.loads((DATA / "acronyms.json").read_text(encoding="utf-8"))["entries"]
    candidates = {
        e["a"]: e["m"][0]["e"]
        for e in entries
        if len(e.get("m", [])) == 1 and not e.get("byDomain")
        and re.search(r"\balso\b", (e["m"][0].get("n") or ""), re.I)
    }
    seen = collections.defaultdict(set)
    for path in files:
        text = path.read_text(encoding="utf-8")
        for a in candidates:
            if re.search(rf'\b{re.escape(a)} <span class="acro-exp">', text):
                seen[a].add(domain_of(path))
    return sorted((a, candidates[a], len(d)) for a, d in seen.items() if len(d) > 1)


# An acronym is only the tail of a longer one often enough to ruin an audit:
# a bare \b matched `DP` inside `UDP`, `RA` inside `YARA`, `SCP` inside `OSCP`
# and `TS` inside `HSTS`, which turned a 28-row finding into a 77-row one that
# was mostly the regex looking at itself. The lookbehind is the whole fix.
def _rendered_re(acronym):
    return re.compile(r'(?<![A-Za-z0-9])' + re.escape(acronym) +
                      r'e?s? <span class="acro-exp">')


def undecided_meanings(files):
    """(acronym, domain, default, meanings) for a rendering nobody decided.

    A dictionary entry with several meanings annotates one of them everywhere
    unless `byDomain` says otherwise, and a wrong expansion is well-formed
    markup that no other check can see. Six were live when this was written:
    ECC as Elliptic Curve Cryptography in a memory card, DC as Domain
    Controller beside a voltage rail, IPS as Intrusion Prevention System in a
    display-panel table, KVM as Kernel-based Virtual Machine among rack
    appliances, SSG as Static Site Generation next to "E-6 Staff Sergeant", and
    DORA as DevOps Research and Assessment in a list of EU regulations.

    So `byDomain` is now exhaustive rather than exceptional: every domain where
    a multi-meaning acronym renders carries a decision, including the ones that
    simply confirm the default. That makes this a ratchet at zero — a new
    domain picking one up shows here, once, before it ships.
    """
    import json
    entries = json.loads((DATA / "acronyms.json").read_text(encoding="utf-8"))["entries"]
    multi = [e for e in entries if len(e.get("m", [])) > 1]
    by_domain = collections.defaultdict(str)
    for path in files:
        by_domain[domain_of(path)] += path.read_text(encoding="utf-8")
    out = []
    for domain, text in sorted(by_domain.items()):
        if domain == "acronym":
            continue
        for e in multi:
            if domain in e.get("byDomain", {}):
                continue
            if _rendered_re(e["a"]).search(text):
                out.append((e["a"], domain,
                            e.get("annotate", e["m"][0]["e"]),
                            [m["e"] for m in e["m"]]))
    return out


# Two live defects were found by reading this census by hand rather than by any
# check: `IR` rendered as *Incident Response* inside a compiler card's title and
# in a Flipper Zero tool table, and `SMB` rendered as *Server Message Block* in
# "a common home-lab / SMB choice". Both entries were single-meaning, so
# `undecided_meanings` could not see them and no note said "also".
#
# There is no rule that catches these, because the dictionary does not know the
# second meaning exists. What correlates is *breadth*: an acronym a single
# subject owns tends to stay in that subject, and one rendered across many
# unrelated domains has usually been borrowed by one of them. So this reports
# the widest-travelling single-meaning entries as a census to read, not as a
# gate to pass.
BREADTH_FLOOR = 6


def broadly_rendered(files):
    """(acronym, expansion, domains) for single-meaning acronyms used widely."""
    import json
    entries = json.loads((DATA / "acronyms.json").read_text(encoding="utf-8"))["entries"]
    single = {e["a"]: e["m"][0]["e"] for e in entries if len(e.get("m", [])) == 1}
    by_domain = collections.defaultdict(str)
    for path in files:
        by_domain[domain_of(path)] += path.read_text(encoding="utf-8")
    seen = collections.defaultdict(set)
    for domain, text in by_domain.items():
        if domain == "acronym":
            continue
        for a in single:
            if _rendered_re(a).search(text):
                seen[a].add(domain)
    return sorted(((a, single[a], sorted(d)) for a, d in seen.items()
                   if len(d) >= BREADTH_FLOOR),
                  key=lambda r: (-len(r[2]), r[0]))


def topic_label(block):
    """What script.js would use as the slug source, expansions removed."""
    plain = ACRO_SPAN_RE.sub("", block)
    m = TOPIC_NAME_RE.search(plain)
    if m:
        raw = m.group(1)
    else:
        h = TOPIC_HEADER_RE.search(plain)
        raw = h.group(1) if h else ""
    return unescape(re.sub(r"<[^>]+>", "", raw)).strip(), bool(m)


def main():
    strict = "--strict" in sys.argv
    errors, warns = [], collections.Counter()
    seen_slugs = {}
    today = datetime.now(timezone.utc).strftime("%Y-%m")
    all_titles, xrefs = set(), []
    ai_tables = 0

    # Domain order matters: script.js walks .domain-section in document order,
    # so a collision is only real if it survives that ordering.
    import json
    order = [d["id"] for d in json.loads((DATA / "domains.json").read_text())]
    files = [f for d in order for f in domain_files(d)]

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

        # A code block belongs in a <pre>, never a <div>: a <div> defaults to
        # white-space:normal and collapses the newlines, so multi-line code and
        # aligned diagrams render as one run-on line. The whole site was converted
        # to <pre class="code-block"> once the count hit zero; this keeps it there.
        for m in re.finditer(r'<div\b[^>]*class="code-block"', text):
            line = text.count("\n", 0, m.start()) + 1
            errors.append(
                f"{name}:{line}: <div class=\"code-block\"> collapses whitespace — "
                f"use <pre class=\"code-block\"> so newlines and indentation survive")

        for line_no, block in topic_blocks(text):
            label, has_name = topic_label(block)
            # The expand chevron is the affordance CSS rotates on open
            # (.topic-header.open .topic-chev). A header without one still toggles
            # — the click handler is on the header — but silently, with no visual
            # cue that the card opens. 90 older difficulty-badge headers shipped
            # without it across 15 domains; once fixed to zero this graduates to an
            # error, the way this file's warnings do, so the gap cannot return.
            # (check_markup.py proves the header is well-formed; this proves it is
            # complete — the two do not check each other's rules.)
            if 'class="topic-header"' in block:
                if "topic-chev" not in block:
                    errors.append(
                        f"{name}:{line_no}: topic-header has no "
                        f'<span class="topic-chev"> — every other topic carries the '
                        f"expand chevron; add one so the card shows that it opens")
                if "topic-icon" not in block:
                    # Graduated from a warning the moment its count hit zero: the 90
                    # badge-led headers that led with no icon were each given a
                    # subject-appropriate one, so an icon is now part of the header
                    # skeleton every topic shares, the way the chevron is.
                    errors.append(
                        f"{name}:{line_no}: topic-header has no "
                        f'<span class="topic-icon"> — every topic carries one; add a '
                        f"subject-appropriate icon as the header's first span")
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
            all_titles.add(label)

        # The annotator owns this class; hand-written ones get stripped silently.
        for m in re.finditer(r'<span class="acro-exp">', text):
            pass  # presence is fine — they are generated; see --check on the annotator

        for line_no, literal in hex_colours(text):
            errors.append(
                f"{name}:{line_no}: hard-coded colour {literal} — it keeps its "
                f"dark-mode value in light mode. Use a theme variable from "
                f":root in style.css, e.g. var(--sky), or style the element "
                f"with a class"
            )

        for line_no, msg in volatile_problems(text, today):
            errors.append(f"{name}:{line_no}: {msg}")

        # Resolved after every file is read — a card may reference any domain.
        xrefs.extend((name, ln, title) for ln, title in xref_targets(text))

        for line_no, cls in dead_first_cell_classes(text):
            errors.append(
                f"{name}:{line_no}: '{cls}' on the first cell of a .ref-table row "
                f"never renders — .ref-table td:first-child outranks it. Drop the "
                f"class (the column is already styled), or use "
                f"style=\"color: var(--…)\" if it genuinely needs a different colour"
            )

        for line_no in verdict_margins(text):
            errors.append(
                f"{name}:{line_no}: a top margin on .concept-desc is the "
                f"verdict sentence after a table — use "
                f'class="concept-desc verdict" instead of an inline style'
            )

        if domain_of(path) not in VERDICT_EXEMPT:
            warns["table with no verdict"] += sum(
                1 for _ in tables_without_verdict(text))

        warns["inline style attribute"] += len(re.findall(r'\bstyle="', text))
        ai_tables += text.count('class="ai-table"')

    # Cross-references, once every title is known.
    lowered = {t.lower() for t in all_titles}
    for name, line_no, title in xrefs:
        if title.lower() not in lowered:
            near = [t for t in all_titles if title.lower()[:18] in t.lower()]
            hint = f" Did you mean '{near[0]}'?" if near else ""
            errors.append(
                f"{name}:{line_no}: cross-reference to '{title}' matches no topic "
                f"title on the site.{hint}"
            )

    # Advisory, not blocking: each needs a human to say which meaning belongs
    # where, and the count is small enough to read.
    for acro, domain, default, meanings in undecided_meanings(files):
        errors.append(
            f"acronyms.json: {acro} renders in '{domain}' with no byDomain "
            f"decision, so it annotates as '{default}'. Meanings: "
            f"{' | '.join(meanings)}. Add \"{domain}\" to that entry's "
            f"byDomain — the right expansion, or null not to annotate there."
        )

    broad = broadly_rendered(files)

    ambiguous = ambiguous_acronyms(files)
    warns["ambiguous acronym rendered in 2+ domains"] += len(ambiguous)

    print(f"Linted {len(files)} domain files, {len(seen_slugs)} topics, "
          f"{len(xrefs)} cross-references.\n")
    if ambiguous:
        print("Ambiguous acronyms rendered identically across several domains "
              "(all current uses were checked by hand and are correct):")
        for a, exp, n in ambiguous:
            print(f"  {a:<6} always '{exp}'  — in {n} domains")
        print()
    if errors:
        print(f"ERRORS ({len(errors)}):")
        for e in errors[:40]:
            print(f"  {e}")
        if len(errors) > 40:
            print(f"  … and {len(errors) - 40} more")
        print()
    print(f"{len(broad)} single-meaning acronym(s) rendered in "
          f"{BREADTH_FLOOR}+ domains — breadth is the only signal that a second "
          f"meaning has been borrowed somewhere. Widest first:")
    for a, exp, doms in broad[:8]:
        print(f"  {a:<8} {len(doms):>2} domains  '{exp}'")
    print()

    print(f"{ai_tables} .ai-table(s) in use — the second table style, not debt. "
          f"See this file's docstring.\n")
    print("Warnings (tracked, not blocking):")
    for k, v in sorted(warns.items(), key=lambda kv: -kv[1]):
        ceiling = CEILINGS.get(k)
        over = "" if ceiling is None else f"   (ceiling {ceiling:,})"
        print(f"  {v:>6}  {k}{over}")
    print(f"\nTREND {' '.join(f'{k.split()[0]}={v}' for k, v in sorted(warns.items()))}")

    # A ceiling is a ratchet for a count that cannot reach zero. Exceeding it is
    # an error; falling below it is an invitation to lower the number here, in
    # the same commit that earned it.
    for k, ceiling in CEILINGS.items():
        if warns[k] > ceiling:
            errors.append(
                f"{k}: {warns[k]:,} exceeds the ceiling of {ceiling:,}. This "
                f"count may fall and may not rise — see the docstring for why "
                f"it is a ceiling rather than a zero."
            )
            print(f"\nERROR {errors[-1]}")

    if errors:
        return 1
    if strict and sum(warns.values()):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
