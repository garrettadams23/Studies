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

Usage:
  python3 tools/check_css_vars.py
  python3 tools/check_css_vars.py --self-test
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CSS = ROOT / "style.css"
DATA = ROOT / "data"
SCRIPT = ROOT / "script.js"

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
    print(f"check_css_vars self-test: {len(FIXTURES) + len(ATTR_FIXTURES)} fixtures, "
          f"{bad} failure(s).")
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
    used = len({m.group(1) for m in USE_RE.finditer(css)})
    js_reads = len(USE_RE.findall(js))
    print(f"style.css: {declared} custom properties declared, {used} read by name, "
          f"0 read without being declared.")
    print(f"data/*.html: {attr_reads} read inside a style attribute · "
          f"script.js: {js_reads} written into generated markup · "
          f"0 read without being declared.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
