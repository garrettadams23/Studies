#!/usr/bin/env python3
"""check_css_vars.py — every custom property this stylesheet reads is defined.

`var(--name)` with no fallback, where `--name` is never declared, is invalid at
computed-value time. It does not fail loudly, it does not warn, and it does not
fall back to the property's initial value either — the declaration is discarded
and the element **inherits** whatever its parent had. So the symptom is not a
missing colour; it is a plausible-looking wrong one, which is the hardest kind
to notice.

## The bug that produced this file

    .domain-matches { color: var(--bg1); background: var(--accent); }

`--bg1` is not a variable on this site. The three that exist are `--bg`,
`--bg2` and `--bg3`. So the per-domain search-result badge inherited the domain
header's light text and drew it on a bright accent, failing contrast on ten of
the thirty domains — and it had done so for as long as the badge had existed,
because **the badge only appears while a search is running** and nothing scanned
that state. `a11y_test.mjs` found it the day it learned to type into the search
box; this file is so that the next one is found by `make check` instead.

A second, quieter instance came out with it: `var(--text-muted)` inside a
`[data-domain="mental-disorders"]` block, for a domain that does not exist and
under a `body.light` theme selector this site has never used. Dead twice over.
`style_equiv.mjs` confirmed deleting all 23 lines changed no computed style on
any of 153,187 elements.

## Why a static check is the right shape here

This is the sharp kind of signal, not the plausible kind. A name is either
declared somewhere in the file or it is not; there is no threshold, no scoring,
and no judgement call for a reader to overrule. Contrast needs a browser and
`a11y_test.mjs` has it — but that only sees the states it visits, and this sees
every rule in the file whether or not anything renders it today.

**And the same rule inside `style="…"`, which was the half this file missed.**
The reasoning for scoping it to `style.css` was right about the corpus and wrong
about the scope: `data/*.html` does mention `var(--gap)` and `var(--spacing-md)`
inside code samples that *teach* custom properties, and flagging one would be
the instrument being wrong about what it is reading — but a `var()` inside a
**style attribute** is not a teaching example. It is a live declaration with
exactly the bug above available to it, and there are **1,061 of them** in the
content against **four** `var()` mentions anywhere else in `data/`. Scoping to
the attribute keeps every teaching example out by construction rather than by
exemption, which is why this needs no allow-list.

`script.js` reads five of them by name too, writing `var(--cyan)` and friends
into markup it generates, with the same failure available and nothing looking.
Ten occurrences — small, and there is no version of this check that covers a
thousand live reads in the content and declines to cover ten in the script.

The original scope was set by the defect that produced the file, and the defect
happened to be in the stylesheet. That is a bad reason for a boundary, and it is
the second time this session that a guard's reach turned out to be the shape of
the bug that motivated it rather than the shape of the class. The rule the file
should have had from the start: **every place the site names a custom property,
the name is declared or it is not.**

A `var(--name, fallback)` is exempt: naming a fallback is how you deliberately
read a property that may not be set, which is what `var(--accent, var(--cyan))`
does thirty times over for the per-domain accents.

Covers `style.css`, every `style="…"` attribute in `data/*.html`, and the
`var()` reads in `script.js`.

## And class names, which is the same bug one layer over

A class that no rule defines fails the same way an undeclared variable does:
silently, and plausibly. `class="c-yellow"` sat on nine table cells in six
files, meant as the caution tone between green and red, and every one rendered
as body text — the house tone is `c-amber`, and `.c-yellow` was never written.
The operating manual in plan.md lists that exact class as failure 6, with the
guard *grep `style.css` for the utility class before using one*. A habit, and
it was got past nine times. Beside it, 61 code spans carried `class="m"`, a
catch-all for literals that colored nothing, and one decorator carried `nd`.

So every class on a real element in `data/*.html` and `index-shell.html` must
be one a selector in `style.css` names, or sit on `ALLOW_UNRULED` with the
reason it needs no rule. **Real element** is the point of using a parser here
rather than a pattern: the first census was a regex, it counted fifteen
unruled names, and one of them — `link` — was text inside a code sample that
teaches HTML. A parser finds fourteen, every one on a real element and none in
the teaching, which is the same scoping argument the attribute check above makes for
`var()`, arrived at by the opposite route.

The allow list is for names that are not style hooks at all: a label naming
which layer of a stack a row is, or an SVG `<g>` whose children carry the
classes that draw them. A class that *names* a style it does not apply is not
on it — `style-orange` was removed instead, because its element was colored by
an inline `var(--orange)` and the class only claimed the credit.

Not covered: class strings `script.js` writes into generated markup. Parsing
template literals reliably is a different tool, and nothing there has drifted
yet that anyone has seen. Named here so its absence is visible.

Usage:
  python3 tools/check_css_vars.py
  python3 tools/check_css_vars.py --self-test
"""

import re
import sys
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CSS = ROOT / "style.css"
DATA = ROOT / "data"
SCRIPT = ROOT / "script.js"
SHELL = ROOT / "index-shell.html"

# Class names that are not style hooks, each with the reason it needs no rule.
# Read before being listed; a name goes here only if no rule *should* read it.
ALLOW_UNRULED = {
    **{f"layer-{n}": "a label naming which OSI or TCP/IP layer this row is; "
                     "every layer is drawn alike, so no rule reads it"
       for n in range(1, 8)},
    "acs-letters": "an SVG <g> grouping the acronym-anatomy letters; its "
                   "children carry the classes that draw them",
    "rsv-names": "an SVG <g> grouping the role-scope labels; its children "
                 "carry the classes that draw them",
    "rsv-chips": "an SVG <g> grouping the role-scope chips; its children "
                 "carry the classes that draw them",
}

# A selector's class, not a decimal: `.5rem` must not define a class `5rem`.
CLASS_RE = re.compile(r"\.(-?[A-Za-z_][\w-]*)")
COMMENT_RE = re.compile(r"/\*.*?\*/", re.S)
# Everything before a `{` is a selector list or an at-rule's prelude; what sits
# between braces is declarations, which can hold `.`-tokens that are not
# classes (a `url(…)`, a quoted `content`).
PRELUDE_RE = re.compile(r"([^{}]*)\{")

# A live declaration in the content. Deliberately only the attribute: prose and
# code samples are where the teaching examples live, and they are none of this
# check's business.
STYLE_ATTR_RE = re.compile(r'\bstyle="([^"]*)"')

DECL_RE = re.compile(r"(--[A-Za-z0-9_-]+)\s*:")
# `var(` then the name, then either `)` or `,`. The comma case carries a
# fallback and is deliberately not our business.
USE_RE = re.compile(r"var\(\s*(--[A-Za-z0-9_-]+)\s*([),])")


def undefined(css):
    """(line, name) for each var() read of a property nothing declares."""
    declared = set(DECL_RE.findall(css))
    out = []
    for m in USE_RE.finditer(css):
        name, nxt = m.group(1), m.group(2)
        if nxt == "," or name in declared:
            continue
        out.append((css.count("\n", 0, m.start()) + 1, name))
    return out


def undefined_in_attributes(html, declared):
    """(line, name, attribute) for each undefined var() in a style attribute."""
    out = []
    for m in STYLE_ATTR_RE.finditer(html):
        for v in USE_RE.finditer(m.group(1)):
            name, nxt = v.group(1), v.group(2)
            if nxt == "," or name in declared:
                continue
            out.append((html.count("\n", 0, m.start()) + 1, name, m.group(1)[:60]))
    return out


def css_classes(css):
    """Every class name a selector in the stylesheet mentions."""
    css = COMMENT_RE.sub("", css)
    return {c for prelude in PRELUDE_RE.findall(css) for c in CLASS_RE.findall(prelude)}


class _Classes(HTMLParser):
    """(line, tag, class) for every class on a real element — never on text."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.found = []

    def handle_starttag(self, tag, attrs):
        for key, value in attrs:
            if key == "class" and value:
                line = self.getpos()[0]
                self.found.extend((line, tag, name) for name in value.split())

    handle_startendtag = handle_starttag


def unruled_classes(html, defined, allowed=ALLOW_UNRULED):
    """(line, tag, name) for each class on an element that no rule defines."""
    parser = _Classes()
    parser.feed(html)
    parser.close()
    return [(line, tag, name) for line, tag, name in parser.found
            if name not in defined and name not in allowed]


CLASS_FIXTURES = [
    (".c-amber{color:var(--amber)}", '<td class="c-amber">x</td>', 0,
     "a class the stylesheet defines"),
    (".c-amber{color:var(--amber)}", '<td class="c-yellow">x</td>', 1,
     "the defect: a class nothing defines, which renders as plain text"),
    (".code-block .num{color:var(--cyan)}", '<span class="num">0</span>', 0,
     "a class named inside a descendant selector is defined"),
    ("@media (max-width:640px){.asl-grid{gap:4px}}", '<div class="asl-grid"></div>', 0,
     "a class defined only inside an at-rule is defined"),
    ("/* .ghost { color: red } */", '<p class="ghost">x</p>', 1,
     "a class that appears only in a comment is not"),
    (".a{background:url(Img/x.png);content:'.fake'}", '<p class="fake">x</p>', 1,
     "nor one that appears only inside a declaration"),
    (".pad{padding:.5rem}", '<p class="5rem">x</p>', 1,
     "a decimal in a value is not a class"),
    ("", '<pre class="code-block">&lt;div class="nope"&gt;</pre>', 1,
     "the code block's own class counts; the escaped sample inside it does not"),
    (".code-block{}", '<pre class="code-block">&lt;div class="nope"&gt;</pre>', 0,
     "a teaching sample is text, whatever class it names"),
    (".x{}", '<p>write <code>class="link"</code> on the anchor</p>', 0,
     "an unescaped class=\"…\" inside text is still text"),
    (".layer{}", '<div class="layer layer-7">7</div>', 0,
     "an allowed label: layer-7 is on the list, with its reason"),
    (".kc-num{}", '<div class="kc-num style-orange">03</div>', 1,
     "a class that names a style it does not apply is not on the list"),
    (".topo-svg{}", '<svg class="topo-svg"><line class="ghost-line"/></svg>', 1,
     "a self-closing SVG element is still an element"),
]


ATTR_FIXTURES = [
    ('<td style="color: var(--cyan)">x</td>', 0, "a declared property in a live attribute"),
    ('<td style="color: var(--nope)">x</td>', 1, "an undefined one, which renders as inherited"),
    ('<td style="color: var(--nope, #fff)">x</td>', 0, "a fallback is deliberate"),
    ('<p>use <code>var(--spacing-md)</code> to set it</p>', 0,
     "a teaching example is not in a style attribute"),
    ('<pre class="code-block">.card { color: var(--gap); }</pre>', 0,
     "nor is a code sample, whatever it declares"),
    ('<td style="background: var(--bg2); color: var(--nope)">x</td>', 1,
     "two reads in one attribute, one of them undefined"),
]

FIXTURES = [
    (":root{--bg:#000}\n.a{color:var(--bg1)}", 1, "the defect: a name nothing declares"),
    (":root{--bg:#000}\n.a{color:var(--bg)}", 0, "a name that is declared"),
    (":root{--bg:#000}\n.a{color:var(--bg1, #fff)}", 0,
     "a fallback is a deliberate read of a maybe-unset property"),
    (":root{--bg:#000}\n.a{color:var( --bg1 )}", 1, "whitespace inside var() does not hide it"),
    (".a{--local:#000}\n.b{color:var(--local)}", 0,
     "declared anywhere in the file counts — this check is not about scope"),
    (":root{--a:1}\n.x{color:var(--accent, var(--a))}", 0,
     "the outer name has a fallback; the inner one is declared"),
    # Written expecting 0 and corrected to 1 after the check disagreed, because
    # the check was right: in `var(--b, var(--c))` the *last* name in the chain
    # is the one with nowhere left to fall back to. If neither is declared the
    # declaration can never resolve, which is the defect this file is for.
    (":root{--a:1}\n.x{color:var(--b, var(--c))}", 1,
     "the innermost fallback is asserted to exist — nothing catches it"),
]


def self_test():
    bad = 0
    for css, want, why in FIXTURES:
        got = len(undefined(css))
        if got != want:
            bad += 1
            print(f"FAIL  {why}: found {got}, expected {want}")
    for html, want, why in ATTR_FIXTURES:
        got = len(undefined_in_attributes(html, {"--cyan", "--bg2"}))
        if got != want:
            bad += 1
            print(f"FAIL  {why}: found {got}, expected {want}")
    for css, html, want, why in CLASS_FIXTURES:
        got = len(unruled_classes(html, css_classes(css)))
        if got != want:
            bad += 1
            print(f"FAIL  {why}: found {got}, expected {want}")
    total = len(FIXTURES) + len(ATTR_FIXTURES) + len(CLASS_FIXTURES)
    print(f"check_css_vars self-test: {total} fixtures, {bad} failure(s).")
    return 1 if bad else 0


def main():
    if "--self-test" in sys.argv:
        return self_test()
    css = CSS.read_text(encoding="utf-8")
    problems = undefined(css)
    declared = len(set(DECL_RE.findall(css)))
    if problems:
        for line, name in problems:
            print(f"::error::style.css:{line}: var({name}) — nothing declares "
                  f"{name}. The declaration is dropped and the element inherits "
                  f"instead, so the wrong value looks deliberate. Declare it, "
                  f"correct the name, or give it a fallback.")
        return 1
    names = set(DECL_RE.findall(css))
    attr_problems, attr_reads = [], 0
    for path in sorted(DATA.glob("*.html")):
        html = path.read_text(encoding="utf-8")
        attr_reads += sum(len(USE_RE.findall(m.group(1)))
                          for m in STYLE_ATTR_RE.finditer(html))
        for line, name, attr in undefined_in_attributes(html, names):
            attr_problems.append((path.name, line, name, attr))
    if attr_problems:
        for fname, line, name, attr in attr_problems:
            print(f"::error::data/{fname}:{line}: var({name}) in style=\"{attr}\" — "
                  f"nothing declares {name}. The declaration is dropped and the "
                  f"element inherits instead, so the wrong value looks deliberate.")
        return 1
    js = SCRIPT.read_text(encoding="utf-8")
    js_problems = [(js.count("\n", 0, m.start()) + 1, m.group(1))
                   for m in USE_RE.finditer(js)
                   if m.group(2) != "," and m.group(1) not in names]
    if js_problems:
        for line, name in js_problems:
            print(f"::error::script.js:{line}: var({name}) — nothing declares "
                  f"{name}. It is written into generated markup, where the "
                  f"declaration is dropped and the element inherits instead.")
        return 1
    defined = css_classes(css)
    class_problems, elements, names, in_use = [], 0, set(), set()
    for path in sorted(DATA.glob("*.html")) + [SHELL]:
        html = path.read_text(encoding="utf-8")
        parser = _Classes()
        parser.feed(html)
        parser.close()
        elements += len({(line, tag) for line, tag, _ in parser.found})
        names |= {name for _, _, name in parser.found}
        in_use |= {name for _, _, name in parser.found if name in ALLOW_UNRULED}
        rel = path.relative_to(ROOT)
        class_problems += [(rel, line, tag, name)
                           for line, tag, name in unruled_classes(html, defined)]
    # Every allowed name must still be in use, or the list is describing markup
    # that is gone — the staleness any list of exceptions is most exposed to.
    stale = sorted(set(ALLOW_UNRULED) - in_use)
    if class_problems or stale:
        for rel, line, tag, name in class_problems:
            print(f"::error::{rel}:{line}: <{tag} class=\"{name}\"> — no rule in "
                  f"style.css defines .{name}, so the element renders as if the "
                  f"class were not there. Use the house class, add the rule, or "
                  f"put it on ALLOW_UNRULED with the reason it needs none.")
        for name in stale:
            print(f"::error::ALLOW_UNRULED lists {name!r}, which no element uses any "
                  f"more. Delete the entry; an exception nothing needs is how the "
                  f"next one gets waved through.")
        return 1

    used = len({m.group(1) for m in USE_RE.finditer(css)})
    js_reads = len(USE_RE.findall(js))
    print(f"style.css: {declared} custom properties declared, {used} read by name, "
          f"0 read without being declared.")
    print(f"data/*.html: {attr_reads} read inside a style attribute · "
          f"script.js: {js_reads} written into generated markup · "
          f"0 read without being declared.")
    print(f"classes: {len(names)} names on real elements in data/*.html and "
          f"index-shell.html, {len(defined)} defined by a selector · 0 without a "
          f"rule · {len(ALLOW_UNRULED)} allowed, each with its reason.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
