#!/usr/bin/env python3
"""
reconcile_build.py

Syncs the current patched index.html back into:
  - index-shell.html  (shell with search bar + notepad injections)
  - data/{id}.html    (each domain's content)

After running this, `python3 build.py` should reproduce index.html exactly.

Recovering a domain used to mean walking nested <div>s from `.domain-body` to
its matching close tag and hoping the depth count survived. It does not any
more: build.py parks each body verbatim in a `<script type="text/html">` block
whose only terminator is `</script`, so the content comes back out by slicing
between two markers. The one thing that has to be undone is the `id="…"` build.py
stamps on each topic — those are generated, and writing them back into data/*
would make the next build stamp them twice.
"""

import json
from pathlib import Path
import re

ROOT = Path(__file__).parent
DATA = ROOT / "data"


def domain_ids():
    """Every domain in data/domains.json, in page order."""
    return [d["id"] for d in json.loads((DATA / "domains.json").read_text(encoding="utf-8"))]


TOPIC_ID_RE = re.compile(r'(<div class="topic")( id="[^"]*")')


def extract_domain_body(content: str, domain_id: str) -> str:
    """Pull one domain's source back out of its deferred content block."""
    open_re = re.compile(
        r'<script type="text/html" class="domain-src" data-domain="'
        + re.escape(domain_id) + r'"\s*>')
    m = open_re.search(content)
    if not m:
        raise ValueError(f"Deferred content block not found: {domain_id}")
    end = content.find("</script>", m.end())
    if end < 0:
        raise ValueError(f"Unterminated content block: {domain_id}")
    body = content[m.end():end]
    if body.startswith("\n"):
        body = body[1:]
    # build.py stamps the topic ids on the way out; data/* never carries them.
    return TOPIC_ID_RE.sub(r"\1", body).rstrip()


def build_new_shell(content: str) -> str:
    """Build the new index-shell.html by extracting shell structure from index.html."""

    # Part 1: everything from <!doctype to just before the search bar comment
    sb_marker = '<!-- SEARCH BAR'
    sb_start = content.find(sb_marker)
    if sb_start < 0:
        raise ValueError("Search bar comment not found in index.html")
    shell_prefix = content[:sb_start]

    # Part 2: search bar HTML (from <!-- SEARCH BAR --> up to and including <!-- /search-bar --><!-- /container -->)
    container_div = '<div class="container" id="domain-container">'
    container_start = content.find(container_div, sb_start)
    if container_start < 0:
        raise ValueError("Container div not found after search bar")
    # Search bar is from sb_start to just before container_div
    # Include the <!-- /container --> marker
    search_bar_html = content[sb_start:container_start]

    # Part 3: container + placeholder + closing
    # After all domain sections, find the container closing
    # The last domain closes with:  \n        </div>\n      </div>\n    </div>
    # Then script.js
    script_js = '<script src="script.js"></script>'
    script_pos = content.rfind(script_js)
    # Container closes just before script.js
    # Find the </div> before script.js (closing the container)
    closing_div_end = content.rfind('</div>', 0, script_pos) + len('</div>')
    # The container closing is that last </div> + \n\n
    container_close_section = content[container_start + len(container_div):closing_div_end]
    # We don't need the domains content, just need placeholder
    # Actually we just need: open container, placeholder, close container
    container_section = (
        container_div + "\n"
        "<!-- DOMAINS_CONTENT -->\n"
        "    </div>"
    )

    # Part 4: script.js + notepad HTML
    notepad_start = content.find('<!-- NOTEPAD: slide tab -->', script_pos)
    body_end = content.rfind('</body>')
    post_domains = "\n\n    " + script_js + "\n    " + content[notepad_start:body_end]

    # Part 5: closing tags (no leading \n — content[notepad_start:body_end] already ends with \n)
    closing = "</body>\n</html>\n"

    return shell_prefix + search_bar_html + container_section + post_domains + closing


def main():
    index_html = (ROOT / "index.html").read_text(encoding="utf-8")

    # 1. Extract and write each domain's body content
    for domain_id in domain_ids():
        body = extract_domain_body(index_html, domain_id)
        out_path = DATA / f"{domain_id}.html"
        out_path.write_text(body, encoding="utf-8")
        print(f"  wrote {out_path.name} ({len(body):,} chars)")

    # 2. Build and write new index-shell.html
    new_shell = build_new_shell(index_html)
    shell_path = ROOT / "index-shell.html"
    shell_path.write_text(new_shell, encoding="utf-8")
    print(f"\n  wrote index-shell.html ({len(new_shell):,} chars)")

    # 3. Verify: run build.py logic manually and compare
    import sys
    sys.path.insert(0, str(ROOT))
    import build as build_mod

    shell = new_shell
    domains = json.loads((DATA / "domains.json").read_text(encoding="utf-8"))
    sections = []
    used = set()
    for domain in domains:
        body_path = DATA / f"{domain['id']}.html"
        if not body_path.exists():
            print(f"  WARNING: {body_path} missing")
            continue
        body, _ = build_mod.assign_topic_ids(
            body_path.read_text(encoding="utf-8"), used)
        sections.append(build_mod.build_domain_section(domain, body))

    domains_html = "\n\n".join(sections)
    rebuilt = shell.replace("<!-- DOMAINS_CONTENT -->", domains_html)

    # Compare
    if rebuilt == index_html:
        print("\n  VERIFIED: build.py output matches current index.html exactly.")
    else:
        # Find first difference
        diff_pos = next((i for i, (a, b) in enumerate(zip(rebuilt, index_html)) if a != b), -1)
        if diff_pos < 0:
            print(f"\n  NEAR-MATCH: lengths differ (rebuilt={len(rebuilt)}, original={len(index_html)})")
        else:
            print(f"\n  MISMATCH at char {diff_pos}:")
            print(f"    rebuilt:  {repr(rebuilt[max(0,diff_pos-80):diff_pos+80])}")
            print(f"    original: {repr(index_html[max(0,diff_pos-80):diff_pos+80])}")
        print("  Writing rebuilt.html for diff inspection.")
        (ROOT / "rebuilt.html").write_text(rebuilt, encoding="utf-8")

    print(f"\nDone. Current index.html: {len(index_html):,} chars")


if __name__ == "__main__":
    main()
