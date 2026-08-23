#!/usr/bin/env python3
"""
check_renames.py — old vendor names still being used as though current.

Vendors rename things constantly, and a reference site is where those names go
to rot. "Azure AD" is not wrong in the way a broken link is wrong — it is worse,
because it reads as current and quietly dates the whole card. Nobody notices,
because the person writing knows what it means.

The registry is data/renames.json. Each entry pairs an old name with its current
one, the month the rename happened, and an `allow` list of phrases where the old
string is still literally correct: a product whose own name never changed
("Azure AD Connect" outlived "Azure AD"), a label in a console, a protocol
identifier ("twitter:card" is the meta tag's actual name).

Two mentions are always fine and are not reported:

  * an explicitly historical one — "formerly Azure AD", "renamed from SCCM",
    "used to be called". A card explaining a rename has to say the old name.
  * one that sits within a short distance of the new name, which is the same
    thing written less formally: "Entra ID (Azure AD)".

Everything else is a use of the old name as though it were the current one.

Scope is deliberately narrow. It reads prose only — no code blocks, no
attributes, no generated acronym domain — because a name inside a command or a
URL is usually still correct and always noisy.

Exit status is 1 on any unexplained use, so CI can gate on it.

Usage:
  python3 tools/check_renames.py
  python3 tools/check_renames.py --domain endpoint
  python3 tools/check_renames.py --list        # the registry, oldest rename first
"""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent
DATA = ROOT / "data"

PRE_RE = re.compile(r"<(pre|code)\b.*?</\1>", re.S | re.I)
TAG_RE = re.compile(r"<[^>]+>")
ACRO_EXP_RE = re.compile(r'<span class="acro-exp">\([^<]*?\)</span\s*>')

# Words that mark a mention as deliberately historical.
HISTORICAL = re.compile(
    r"formerly|renamed|used to be|previously|was called|once called|"
    r"old name|until \d{4}|before the rename|historic",
    re.I)

# How far either side of the old name to look for the new one, or for a word
# marking the mention as historical. Wide enough for a parenthetical, narrow
# enough that an unrelated sentence does not excuse it.
WINDOW = 90


def prose(text):
    text = PRE_RE.sub(" ", text)
    text = ACRO_EXP_RE.sub(" ", text)
    return TAG_RE.sub(" ", text)


def explained(text, start, end, new):
    window = text[max(0, start - WINDOW): end + WINDOW]
    return bool(HISTORICAL.search(window)) or new.lower() in window.lower()


def scan(only_domain=None):
    registry = json.loads((DATA / "renames.json").read_text(encoding="utf-8"))["renames"]
    findings = []
    for path in sorted(DATA.glob("*.html")):
        domain = path.stem
        # The acronym domain is generated from the dictionary, and the dictionary
        # legitimately records old expansions.
        if domain == "acronym" or (only_domain and domain != only_domain):
            continue
        text = prose(path.read_text(encoding="utf-8"))
        for entry in registry:
            old, new = entry["old"], entry["new"]
            for m in re.finditer(r"\b" + re.escape(old) + r"\b", text):
                s, e = m.start(), m.end()
                # An allowed phrase means the old string is part of a name that
                # is still correct — check the text actually there, not the
                # registry's idea of it.
                context = text[s: s + max(len(a) for a in entry["allow"]) + 4] if entry["allow"] else ""
                if any(context.startswith(a) or a in text[max(0, s - 12): e + 12]
                       for a in entry["allow"]):
                    continue
                if explained(text, s, e, new):
                    continue
                line = text[: s].count("\n") + 1
                snippet = re.sub(r"\s+", " ", text[max(0, s - 40): e + 40]).strip()
                findings.append((domain, line, old, new, snippet))
    return findings


def main():
    args = sys.argv[1:]
    if "--list" in args:
        registry = json.loads((DATA / "renames.json").read_text(encoding="utf-8"))["renames"]
        for e in sorted(registry, key=lambda x: x["since"]):
            print(f"{e['since']}  {e['old']:<38} -> {e['new']}")
        print(f"\n{len(registry)} renames on record.")
        return 0

    only = args[args.index("--domain") + 1] if "--domain" in args else None
    findings = scan(only)
    for domain, line, old, new, snippet in findings:
        print(f"{domain}.html:~{line}: '{old}' should be '{new}'")
        print(f"    …{snippet}…")
    print(f"\n{len(findings)} unexplained use(s) of a renamed product.")
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())
