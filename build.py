#!/usr/bin/env python3
"""
build.py — Assembles index.html from source files.

Source files:
  index-shell.html      Page skeleton (header, filter bar, container placeholder)
  data/domains.json     Domain metadata array
  data/{id}.html        Inner content of each domain's .domain-body

Output:
  index.html            Self-contained page (works with file://, no server needed)

Usage:
  python3 build.py
"""

import json
import html as html_lib
import re
import sys
from pathlib import Path

ROOT = Path(__file__).parent
DATA = ROOT / "data"

# Set to False (or pass --no-minify) to keep the built HTML pretty-printed.
MINIFY = "--no-minify" not in sys.argv

_PRE_RE = re.compile(r"<pre\b.*?</pre>", re.DOTALL | re.IGNORECASE)


def minify_html(source):
    """Strip leading indentation and blank lines from the built HTML.

    Whitespace between a newline and a tag collapses to nothing meaningful in
    HTML rendering, so removing it is safe and shaves ~19% off the output.
    <pre> blocks are protected verbatim because their whitespace is literal.
    """
    pres = []

    def _stash(m):
        pres.append(m.group(0))
        return f"\x00PRE{len(pres) - 1}\x00"

    protected = _PRE_RE.sub(_stash, source)
    lines = (ln.rstrip() for ln in protected.split("\n"))
    minified = "\n".join(ln.lstrip() for ln in lines if ln.strip())

    for i, block in enumerate(pres):
        minified = minified.replace(f"\x00PRE{i}\x00", block)
    return minified


def build_cert_tags(cert_tags):
    parts = []
    for tag in cert_tags:
        parts.append(f'<span class="ctag {tag["cls"]}">{tag["text"]}</span>')
    return "\n            ".join(parts)


def build_domain_section(domain, body_content):
    cert_tags_html = build_cert_tags(domain["certTags"])
    sub = domain["sub"]
    return f"""\
      <div class="domain-section {domain['colorClass']}" data-domain="{domain['id']}">
        <div class="domain-header">
          <span class="domain-icon">{domain['icon']}</span>
          <span class="domain-title">{domain['title']}</span>
          <div class="cert-tags">
            {cert_tags_html}
          </div>
          <span class="domain-sub">{sub}</span>
          <span class="chevron">▾</span>
        </div>
        <div class="domain-body">
{body_content}
        </div>
      </div>"""


def build_acronym_payload():
    """The dictionary, compacted for the quiz and the acronym-aware search.

    Only what those two need — acronym, its expansions, and its subject area.
    Notes and per-domain overrides are dropped, which halves the payload
    against shipping acronyms.json verbatim.
    """
    path = DATA / "acronyms.json"
    if not path.exists():
        return "[]"
    entries = json.loads(path.read_text(encoding="utf-8"))["entries"]
    compact = [[e["a"], [m["e"] for m in e["m"]], e["m"][0]["c"]] for e in entries]
    payload = json.dumps(compact, separators=(",", ":"), ensure_ascii=False)
    # A JSON block ends at the first "</script>" the parser sees, wherever it is.
    print(f"  + acronym payload ({len(payload):,} chars, {len(entries)} entries)")
    return payload.replace("</", "<\\/")


def build_slug_aliases():
    """Old topic slug -> current one, so a shared permalink never rots.

    Written by tools/fix_topic_names.py whenever a rename moves a slug. The page
    uses it to redirect a stale hash and to migrate the progress stored under
    the old id.
    """
    path = DATA / "slug-aliases.json"
    if not path.exists():
        return "{}"
    aliases = json.loads(path.read_text(encoding="utf-8"))
    payload = json.dumps(aliases, separators=(",", ":"), ensure_ascii=False)
    print(f"  + slug aliases ({len(payload):,} chars, {len(aliases)} entries)")
    return payload.replace("</", "<\\/")


def main():
    shell_path = ROOT / "index-shell.html"
    domains_path = DATA / "domains.json"

    if not shell_path.exists():
        print("ERROR: index-shell.html not found.", file=sys.stderr)
        sys.exit(1)
    if not domains_path.exists():
        print("ERROR: data/domains.json not found.", file=sys.stderr)
        sys.exit(1)

    shell = shell_path.read_text(encoding="utf-8")
    domains = json.loads(domains_path.read_text(encoding="utf-8"))

    sections = []
    for domain in domains:
        body_path = DATA / f"{domain['id']}.html"
        if not body_path.exists():
            print(f"WARNING: {body_path} not found — skipping {domain['id']}.")
            continue
        body = body_path.read_text(encoding="utf-8")
        sections.append(build_domain_section(domain, body))
        print(f"  + {domain['id']} ({len(body):,} chars)")

    domains_html = "\n\n".join(sections)
    output = shell.replace("<!-- DOMAINS_CONTENT -->", domains_html)
    output = output.replace("<!-- ACRONYM_DATA -->", build_acronym_payload())
    output = output.replace("<!-- SLUG_ALIASES -->", build_slug_aliases())

    if MINIFY:
        raw_len = len(output)
        output = minify_html(output)
        saved = raw_len - len(output)
        print(f"\n  minified: {raw_len:,} -> {len(output):,} chars (-{saved / raw_len * 100:.0f}%)")

    out_path = ROOT / "index.html"
    out_path.write_text(output, encoding="utf-8")
    print(f"Built {out_path} ({len(output):,} chars, {len(output.encode()):,} bytes)")


if __name__ == "__main__":
    main()
