#!/usr/bin/env python3
"""
check_precache.py — the service worker's offline promise, checked against the site.

`sw.js` precaches the whole site so it installs as an offline PWA, and the
README sells that: *"Offline-first — self-hosted fonts and zero third-party
requests."* Seven browser gates run against this repository and **not one of them
loads the service worker**, so the claim was the only untested thing on the front
page.

Two ways it breaks, and the first is worse than it looks:

  * **A precached path that does not exist.** `cache.addAll()` is atomic: one
    404 rejects the whole promise, the install fails, and *nothing* is cached.
    A single mistyped filename does not cost you one font — it costs you the
    entire offline mode, silently, on a site that still works perfectly online.
  * **An asset the page needs that is not precached.** It resolves from the
    network, so it works in every test anyone runs and fails only for the reader
    who is actually offline.

Both are decidable from the files, which is why this needs no browser.

## What counts as a referenced asset

`href` and `src` in the built page, and `url()` in any precached stylesheet.
Deliberately not every `url(` in the page: content prose contains
`sha256(code_verifier)` in an OAuth explanation and a dozen other parenthesised
things, so a reference must also **look like a file** — a path with an
extension — before it is believed. External URLs, `data:` payloads and in-page
fragments are not assets to cache.

Usage:
  python3 tools/check_precache.py
  python3 tools/check_precache.py --list        # what is cached, and what needs it
  python3 tools/check_precache.py --self-test   # the parsers, on fixtures
"""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SW = ROOT / "sw.js"
PAGE = ROOT / "index.html"

_PRECACHE_RE = re.compile(r"const PRECACHE = \[(.*?)\];", re.S)
_QUOTED_RE = re.compile(r'"([^"]+)"')
_ATTR_RE = re.compile(r'(?:href|src)="([^"]+)"')
_CSS_URL_RE = re.compile(r"url\(\s*['\"]?([^'\")\s]+)['\"]?\s*\)")
# A reference is believed only if it names a file. Without this, prose wins:
# index.html contains `sha256(code_verifier)` inside a card about PKCE.
_LOOKS_LIKE_FILE = re.compile(r"\.[A-Za-z0-9]{2,5}$")
_SKIP_PREFIX = ("http://", "https://", "//", "data:", "#", "mailto:", "javascript:")


def precached(text):
    """The paths listed in sw.js's PRECACHE array."""
    block = _PRECACHE_RE.search(text)
    if not block:
        raise SystemExit(
            "sw.js: no `const PRECACHE = [...]` array — this check cannot verify "
            "an offline promise it cannot find. Fix the pattern, not this line.")
    return _QUOTED_RE.findall(block.group(1))


def references(text, base="/", css=False):
    """Local asset paths referenced by one file, rooted at the site root."""
    found = _CSS_URL_RE.findall(text) if css else _ATTR_RE.findall(text)
    out = []
    for ref in found:
        if ref.startswith(_SKIP_PREFIX) or not _LOOKS_LIKE_FILE.search(ref):
            continue
        if ref.startswith("/"):
            out.append(ref)
        else:
            out.append(base.rstrip("/") + "/" + ref.lstrip("./"))
    return sorted(set(out))


def manifest_icons(text, base):
    """Icon paths a web app manifest names, rooted at the site root.

    The manifest is precached; its icons were not, and nothing noticed because
    the first version of this check followed stylesheets and stopped. A PWA
    installed with no network gets no icon — the one asset whose absence the
    reader sees on their home screen.
    """
    try:
        data = json.loads(text)
    except ValueError:
        return []
    out = []
    for icon in data.get("icons") or []:
        src = icon.get("src") or ""
        if not src or src.startswith(_SKIP_PREFIX):
            continue
        out.append(src if src.startswith("/")
                   else base.rstrip("/") + "/" + src.lstrip("./"))
    return sorted(set(out))


def scan():
    """-> (missing_on_disk, referenced_but_uncached, cached, needed)"""
    cache = precached(SW.read_text(encoding="utf-8"))
    missing = [p for p in cache if p != "/" and not (ROOT / p.lstrip("/")).exists()]

    needed = references(PAGE.read_text(encoding="utf-8"))
    # Stylesheets pull their own assets, and their urls are relative to the
    # stylesheet rather than to the page — a font in /Img/fonts.css is /Img/…
    for sheet in [p for p in cache if p.endswith(".css")]:
        path = ROOT / sheet.lstrip("/")
        if path.exists():
            base = "/" + str(path.relative_to(ROOT).parent).replace("\\", "/")
            needed += references(path.read_text(encoding="utf-8"), base=base, css=True)

    # …and so do web app manifests, whose icons are what an install shows.
    for man in [p for p in cache if p.endswith(".webmanifest")]:
        path = ROOT / man.lstrip("/")
        if path.exists():
            base = "/" + str(path.relative_to(ROOT).parent).replace("\\", "/")
            needed += manifest_icons(path.read_text(encoding="utf-8"), base)

    needed = sorted(set(needed))
    uncached = [p for p in needed
                if p not in cache and (ROOT / p.lstrip("/")).exists()]
    return missing, uncached, cache, needed


FIXTURES = [
    ('<img src="/Img/a.png"><link href="style.css">', "/", False,
     ["/Img/a.png", "/style.css"], "page attributes, absolute and relative"),
    ('<a href="https://example.com/x.png">', "/", False, [],
     "an off-site asset is not ours to cache"),
    ('<a href="#top"><img src="data:image/png;base64,AAAA">', "/", False, [],
     "fragments and data: payloads are not files"),
    ('<p>the verifier is sha256(code_verifier) and url(not_a_file)</p>', "/", True, [],
     "prose that looks like a url() but names no file"),
    ("@font-face{src:url('fonts/x.woff2')}", "/Img", True, ["/Img/fonts/x.woff2"],
     "a stylesheet's url is relative to the stylesheet"),
]

MANIFEST_FIXTURES = [
    ('{"icons":[{"src":"a-192.png"},{"src":"a-512.png"}]}', "/Img/favicon",
     ["/Img/favicon/a-192.png", "/Img/favicon/a-512.png"],
     "icons are relative to the manifest, like a stylesheet's urls"),
    ('{"icons":[{"src":"https://cdn.example/x.png"}]}', "/Img/favicon", [],
     "an off-site icon is not ours to cache"),
    ('{"name":"no icons here"}', "/Img/favicon", [], "a manifest with no icons"),
    ("not json at all", "/Img/favicon", [], "a manifest that does not parse"),
]


def self_test():
    failures = []
    for text, base, css, want, why in FIXTURES:
        got = references(text, base=base, css=css)
        if got != want:
            failures.append(f"  {why}: got {got}, expected {want}")
    for text, base, want, why in MANIFEST_FIXTURES:
        got = manifest_icons(text, base)
        if got != want:
            failures.append(f"  {why}: got {got}, expected {want}")
    try:
        precached("no array here")
    except SystemExit:
        pass
    else:
        failures.append("  a missing PRECACHE array did not raise")
    if failures:
        print("check_precache self-test FAILED:")
        print("\n".join(failures))
        return 1
    print(f"check_precache self-test passed "
          f"({len(FIXTURES) + len(MANIFEST_FIXTURES)} fixtures + the array guard).")
    return 0


def main():
    args = sys.argv[1:]
    if "--self-test" in args:
        return self_test()

    missing, uncached, cache, needed = scan()

    if "--list" in args:
        for p in cache:
            print(f"  cached    {p}")
        for p in needed:
            print(f"  {'needed    ' if p in cache else 'UNCACHED  '}{p}")
        return 0

    for p in missing:
        print(f"sw.js: precaches '{p}', which does not exist. cache.addAll() is "
              f"atomic — one 404 and nothing is cached at all, so offline mode "
              f"fails entirely and silently.")
    for p in uncached:
        print(f"sw.js: the page needs '{p}' and it is not precached — it resolves "
              f"from the network, so it works everywhere except offline.")

    print(f"\n{len(cache)} precached · {len(needed)} referenced · "
          f"{len(missing)} missing on disk · {len(uncached)} needed but uncached.")
    return 1 if (missing or uncached) else 0


if __name__ == "__main__":
    sys.exit(main())
