#!/usr/bin/env python3
"""
patch.py  —  IT & Cybersecurity Reference Tool Patcher
=======================================================
Usage: python3 patch.py   (run from project root)

Domain anchors needed in index.html:
    <!-- /domain-body networking -->
    <!-- /domain-body security-core -->
    <!-- /domain-body script -->
"""
import sys
from pathlib import Path
B = Path(__file__).parent

DOMAINS = {
    "<!-- /domain-body networking -->": [
        B / "frag_networking.html",
    ],
    "<!-- /domain-body security-core -->": [
        B / "frag_security_core.html",
    ],
    "<!-- /domain-body script -->": [
        B / "frag_ps_bash.html",
        B / "frag_html_css_js.html",
        B / "frag_json_sql.html",
        B / "url_encoding_fragment.html",
    ],
}

APPENDS = [
    (B/"style.css",  B/"style_additions.css",  "url-codec-wrap"),
    (B/"script.js",  B/"script_additions.js",  "urlToolEncode"),
]

def r(p):     return p.read_text(encoding="utf-8")
def w(p, t):  p.write_text(t, encoding="utf-8"); print(f"  OK {p.name}")
def need(p):
    if not p.exists(): print(f"  MISS {p.name}"); sys.exit(1)

def patch_html():
    need(B/"index.html")
    html = r(B/"index.html")
    changed = False
    for anchor, frags in DOMAINS.items():
        for f in frags: need(f)
        marker = frags[0].stem.replace("frag_","").replace("_","-")
        tag    = f"patch-{marker}"
        if tag in html:
            print(f"  SKIP {marker} (already patched)"); continue
        if anchor not in html:
            print(f"  WARN anchor not found: {anchor}"); continue
        block = f"\n<!-- {tag} -->\n" + "\n".join(r(f) for f in frags) + f"\n<!-- /{tag} -->\n"
        html  = html.replace(anchor, block + "        " + anchor, 1)
        print(f"  INJ  {marker} ({len(frags)} file(s))")
        changed = True
    if changed: w(B/"index.html", html)

def patch_appends():
    for target, frag, guard in APPENDS:
        need(target); need(frag)
        src = r(target)
        if guard in src: print(f"  SKIP {target.name}"); continue
        w(target, src + "\n" + r(frag))

def main():
    print("\n-- IT & Cybersecurity Reference Patcher --")
    print("[1/2] HTML domains"); patch_html()
    print("[2/2] CSS + JS");     patch_appends()
    print("\nDone.\n")

if __name__ == "__main__":
    main()
