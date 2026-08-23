#!/usr/bin/env python3
"""
annotate_acronyms.py — Adds inline expansions beside acronyms in data/*.html.

Reads data/acronyms.json (the single source of truth) and, for every domain
file, appends a small parenthetical beside the *first* use of each acronym
within each topic:

    ACL <span class="acro-exp">(Access Control List)</span>

Rules that keep the result readable and safe:
  * First occurrence per topic only — repeat uses stay clean.
  * Never inside <pre>, <code>, <kbd>, <script>, <style> or SVG, so command
    output and code samples are untouched.
  * Never inside badges, chips, chevrons or icons, where there is no room.
  * Skipped when the expansion already appears within ~250 characters, so
    tables that already spell the term out are not annotated twice.
  * Case-sensitive whole-token matching, with an optional plural "s".
  * Idempotent: existing .acro-exp spans are stripped before re-annotating, so
    the script can be re-run after every content change.

Usage:
    python3 tools/annotate_acronyms.py [--check] && python3 build.py

    --check  Report what would change and exit non-zero if anything would,
             without writing files.
"""

import html
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
SRC = DATA / "acronyms.json"

# The dictionary domain is generated from the same JSON — annotating it would
# expand acronyms inside their own definitions.
EXCLUDE_FILES = {"acronym.html"}

# Elements whose text is literal (code, keystrokes, drawings) or has no room.
SKIP_TAGS = {
    "pre", "code", "kbd", "script", "style", "svg", "textarea", "title",
    "line", "circle", "text", "path", "rect", "option", "button",
}

# Elements whose class marks them as a chip, badge, icon or syntax token.
SKIP_CLASSES = {
    "topic-badge", "topic-chev", "topic-icon", "domain-icon", "domain-sub",
    "chevron", "ctag", "code-block", "code-label", "acro-exp",
    # A cross-reference quotes another card's title verbatim. Annotating inside
    # one rewrites the quoted title, so it stops matching the card it names and
    # the linter's xref check fails on markup that was correct when written.
    "xref",
    # syntax-highlighting tokens (normally inside <pre>, but not always)
    "kw", "str", "com", "fn", "var", "num", "tag", "type", "attr", "val",
    "prop", "sel", "oper",
}

EXP_SPAN_RE = re.compile(r'\s*<span class="acro-exp">\([^<]*?\)</span>')
TOKEN_RE = re.compile(r"<!--.*?-->|<[^>]+>", re.DOTALL)
TAG_RE = re.compile(r"</?\s*([a-zA-Z0-9]+)")
CLASS_RE = re.compile(r'class="([^"]*)"')
VOID_TAGS = {"br", "hr", "img", "input", "meta", "link", "source", "col", "path",
             "circle", "line", "rect", "use"}


def load_acronyms(domain):
    """Return {html-escaped acronym: expansion} for one domain file.

    An acronym with several meanings uses its `annotate` expansion; `byDomain`
    overrides that per file, and a null override drops the acronym from this
    domain entirely (used where a term is genuinely ambiguous in context).
    A `byDomain` entry wins over `noAnnotate`, so a term that is unsafe almost
    everywhere — POST, TIP — can still be expanded in the one domain that
    always means it literally.
    """
    entries = json.loads(SRC.read_text(encoding="utf-8"))["entries"]
    table = {}
    for e in entries:
        by_domain = e.get("byDomain") or {}
        if domain in by_domain:
            expansion = by_domain[domain]
            if not expansion:
                continue
        elif e.get("noAnnotate"):
            continue
        else:
            expansion = e.get("annotate") or e["m"][0]["e"]
        table[html.escape(e["a"], quote=False)] = html.escape(expansion, quote=False)
    return table


def build_pattern(terms):
    """Longest-first alternation so ATT&CK wins over AT, IPsec over IP, etc."""
    ordered = sorted(terms, key=len, reverse=True)
    alt = "|".join(re.escape(t) for t in ordered)
    # The trailing lookahead also rejects hyphen/slash compounds — SHA-256,
    # OS-native, DNS/NTP — where a bracket in the middle would read badly. Those
    # occurrences are simply passed over; a later plain mention still gets one.
    return re.compile(
        r"(?<![A-Za-z0-9_&/-])(" + alt + r")s?(?![A-Za-z0-9_])(?![-/][A-Za-z0-9])"
    )


def strip_tags(fragment):
    return html.unescape(TOKEN_RE.sub(" ", fragment))


def already_expanded(source, start, end, expansion):
    """True when the expansion is already spelled out right next to the match."""
    window = strip_tags(source[max(0, start - 250):end + 250]).lower()
    words = [w for w in re.findall(r"[a-z0-9]+", expansion.lower()) if len(w) > 3]
    if not words:
        words = re.findall(r"[a-z0-9]+", expansion.lower())
    return bool(words) and all(w in window for w in words[:3])


def inside_parentheses(text, index):
    """True when this position sits inside an unclosed '(' in the same run.

    Annotating there would nest brackets — "RADIUS (UDP (User Datagram
    Protocol) 1812)" — so those occurrences are left for the next mention.
    """
    depth = 0
    for ch in text[:index]:
        if ch == "(":
            depth += 1
        elif ch == ")":
            depth = max(0, depth - 1)
    return depth > 0


def annotate(source, terms, pattern):
    """Walk the file, annotating the first use of each acronym in each topic."""
    out = []
    pos = 0
    # Stack of open elements: (tag, classes, is_topic). `seen` is saved and
    # restored around each .topic so counting restarts per topic.
    stack = []
    skip_depth = 0
    seen = set()
    seen_stack = []
    added = 0

    for tag_match in TOKEN_RE.finditer(source):
        text = source[pos:tag_match.start()]
        if text:
            if skip_depth == 0:
                new_text, n = annotate_text(text, terms, pattern, seen, source, pos)
                out.append(new_text)
                added += n
            else:
                out.append(text)
        out.append(tag_match.group(0))
        pos = tag_match.end()

        token = tag_match.group(0)
        if token.startswith("<!--"):
            continue
        name_match = TAG_RE.match(token)
        if not name_match:
            continue
        name = name_match.group(1).lower()
        closing = token.startswith("</")
        self_closing = token.rstrip().endswith("/>") or name in VOID_TAGS

        if closing:
            for i in range(len(stack) - 1, -1, -1):
                if stack[i][0] == name:
                    for tag, skipped, is_topic in stack[i:][::-1]:
                        if skipped:
                            skip_depth -= 1
                        if is_topic and seen_stack:
                            seen = seen_stack.pop()
                    del stack[i:]
                    break
        elif not self_closing:
            classes = set()
            class_match = CLASS_RE.search(token)
            if class_match:
                classes = set(class_match.group(1).split())
            skipped = name in SKIP_TAGS or bool(classes & SKIP_CLASSES)
            is_topic = "topic" in classes
            if skipped:
                skip_depth += 1
            if is_topic:
                seen_stack.append(seen)
                seen = set()
            stack.append((name, skipped, is_topic))

    tail = source[pos:]
    if tail:
        if skip_depth == 0:
            new_text, n = annotate_text(tail, terms, pattern, seen, source, pos)
            out.append(new_text)
            added += n
        else:
            out.append(tail)

    return "".join(out), added


def annotate_text(text, terms, pattern, seen, source, offset):
    """Annotate one run of plain text (already known to be outside any tag)."""
    added = 0
    pieces = []
    last = 0
    for m in pattern.finditer(text):
        term = m.group(1)
        if term in seen:
            continue
        expansion = terms[term]
        abs_start = offset + m.start()
        abs_end = offset + m.end()
        if already_expanded(source, abs_start, abs_end, expansion):
            seen.add(term)
            continue
        if inside_parentheses(text, m.start()):
            continue
        pieces.append(text[last:m.end()])
        pieces.append(f' <span class="acro-exp">({expansion})</span>')
        last = m.end()
        seen.add(term)
        added += 1
    pieces.append(text[last:])
    return "".join(pieces), added


def main():
    check_only = "--check" in sys.argv

    total = 0
    changed = []
    for path in sorted(DATA.glob("*.html")):
        if path.name in EXCLUDE_FILES:
            continue
        # `script.03-python.html` is still the `script` domain, so a byDomain
        # override has to resolve from the filename prefix, not the stem.
        terms = load_acronyms(path.name.split(".", 1)[0])
        pattern = build_pattern(terms)
        original = path.read_text(encoding="utf-8")
        cleaned = EXP_SPAN_RE.sub("", original)
        result, added = annotate(cleaned, terms, pattern)
        total += added
        print(f"  {path.name:<16} {added:>5} expansions added")
        if result != original:
            changed.append(path.name)
            if not check_only:
                path.write_text(result, encoding="utf-8")

    print(f"\n{total} inline expansions across {len(changed)} file(s).")
    if check_only and changed:
        print("Out of date: " + ", ".join(changed), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
