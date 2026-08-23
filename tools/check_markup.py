#!/usr/bin/env python3
"""
check_markup.py — a real parser over every content fragment, and over the page.

`lint_content.py` enforces the *conventions* — which classes a card uses, that a
topic has a name, that a cross-reference resolves. It reads the files as text,
which is the right tool for those rules and the wrong one for this question:
whether the markup is well-formed at all. A `</div` missing its `>`, a `<span>`
never closed, a `</td>` in a row that has no cell open — none of those break any
convention, and all of them change what the browser builds.

They matter more here than in an ordinary page. A domain's content is parsed
once as *text* by build.py, shipped inside an inert script block, and only
becomes elements when `innerHTML` runs on it. A stray tag is therefore invisible
until a reader opens that one domain, and what the browser does to repair it —
usually by hoisting the rest of the card out of its parent — is silent.

What this checks, per file:

  * every element that needs closing is closed, in the right order
  * no closing tag arrives without a matching open one
  * void elements are not given a closing tag

What it deliberately does *not* check is which classes appear where — that is
`lint_content.py`'s job, and the two should not drift into checking each other's
rules.

Fragments, not documents: `data/*.html` files are the inner HTML of a
`.domain-body`, so there is no <html> or <body> and a bare stack is the right
model. index.html *is* a document and is parsed the same way, which catches a
shell that lost a tag.

Exit status is 1 on any error, so CI can gate on it.

`--self-test` runs the checker over deliberately broken fragments and fails if
any of them passes. A validator that reports "0 errors" is indistinguishable
from one that has quietly stopped looking, and this repo has shipped a check
that passed for a reason unrelated to the feature three times now.

Usage:
  python3 tools/check_markup.py
  python3 tools/check_markup.py data/net.html
  python3 tools/check_markup.py --self-test
"""

import sys
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).parent.parent
DATA = ROOT / "data"

# HTML's void elements: they never have a closing tag, and a parser that expects
# one would report every <br> in the content as unclosed.
VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link",
        "meta", "param", "source", "track", "wbr"}

# Elements the HTML parser itself closes implicitly, so an unclosed one is
# legal markup rather than a mistake. Kept deliberately short — everything the
# content actually uses is closed explicitly, and treating more tags as
# optional is how a real error gets waved through.
OPTIONAL_CLOSE = {"li", "p", "tr", "td", "th", "thead", "tbody", "tfoot",
                  "option", "dd", "dt"}


class Checker(HTMLParser):
    def __init__(self, name):
        super().__init__(convert_charrefs=True)
        self.name = name
        self.stack = []
        self.errors = []

    def _at(self):
        line, col = self.getpos()
        return f"{self.name}:{line}:{col}"

    def handle_starttag(self, tag, attrs):
        if tag in VOID:
            return
        self.stack.append((tag, self.getpos()[0]))

    def handle_startendtag(self, tag, attrs):
        pass  # <foo /> — self-closing, nothing to track

    def handle_endtag(self, tag):
        if tag in VOID:
            self.errors.append(f"{self._at()}: </{tag}> — void element, never closed")
            return
        if not any(t == tag for t, _ in self.stack):
            self.errors.append(f"{self._at()}: </{tag}> with nothing open to close")
            return
        # Pop to the matching open tag, reporting anything skipped that was not
        # allowed to close implicitly. This is what catches a <div> closed by
        # the </div> meant for its parent — the classic cause of a card ending
        # up outside the topic it belongs to.
        while self.stack:
            top, line = self.stack.pop()
            if top == tag:
                break
            if top not in OPTIONAL_CLOSE:
                self.errors.append(
                    f"{self.name}:{line}: <{top}> is never closed "
                    f"(still open at </{tag}> on line {self.getpos()[0]})")

    def finish(self):
        for tag, line in self.stack:
            if tag not in OPTIONAL_CLOSE:
                self.errors.append(f"{self.name}:{line}: <{tag}> is never closed")
        return self.errors


def check_file(path):
    p = Checker(path.name)
    p.feed(path.read_text(encoding="utf-8"))
    p.close()
    return p.finish()


# Each fragment is broken in one specific way, paired with what the checker has
# to say about it. Kept next to the rules they exercise so a change to one is
# obviously a change to the other.
BROKEN = [
    ('<div class="topic"><span class="topic-name">X</div>', "never closed"),
    ('<div class="a"><div class="b">hi</div>', "never closed"),
    ("<div>hi</div></div>", "nothing open to close"),
    ("<div><br></br></div>", "void element"),
    ('<div><span class="x">a<span class="y">b</span></div>', "never closed"),
]


def self_test():
    failures = 0
    for n, (fragment, wanted) in enumerate(BROKEN, 1):
        p = Checker(f"fixture-{n}")
        p.feed(fragment)
        p.close()
        errors = p.finish()
        got = " ".join(errors)
        if not errors:
            print(f"SELF-TEST {n} FAILED: no error reported for {fragment!r}")
            failures += 1
        elif wanted not in got:
            print(f"SELF-TEST {n} FAILED: wanted {wanted!r}, got {got!r}")
            failures += 1
    ok = Checker("fixture-ok")
    ok.feed('<div class="topic"><span class="topic-name">X</span><br></div>')
    ok.close()
    if ok.finish():
        print(f"SELF-TEST FAILED: well-formed markup reported errors: {ok.finish()}")
        failures += 1
    print(f"self-test: {len(BROKEN) + 1} fixtures, {failures} failure(s).")
    return 1 if failures else 0


def main():
    if "--self-test" in sys.argv:
        return self_test()
    args = [a for a in sys.argv[1:] if not a.startswith("-")]
    if args:
        files = [Path(a) for a in args]
    else:
        files = sorted(DATA.glob("*.html"))
        index = ROOT / "index.html"
        if index.exists():
            files.append(index)

    total_errors, checked = 0, 0
    for path in files:
        errors = check_file(path)
        checked += 1
        for e in errors:
            print(f"ERROR {e}")
        total_errors += len(errors)

    print(f"\n{checked} file(s) parsed, {total_errors} markup error(s).")
    return 1 if total_errors else 0


if __name__ == "__main__":
    sys.exit(main())
