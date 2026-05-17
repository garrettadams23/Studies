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
import sys
from pathlib import Path

ROOT = Path(__file__).parent
DATA = ROOT / "data"


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

    out_path = ROOT / "index.html"
    out_path.write_text(output, encoding="utf-8")
    print(f"\nBuilt {out_path} ({len(output):,} chars, {len(output.encode()):,} bytes)")


if __name__ == "__main__":
    main()
