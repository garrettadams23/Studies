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
  python3 tools/check_renames.py --self-test   # the matching rules, on fixtures
  python3 tools/check_renames.py --list        # the registry, oldest rename first
"""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent
DATA = ROOT / "data"
sys.path.insert(0, str(ROOT / "tools"))
from lint_content import TAG_RE  # noqa: E402

PRE_RE = re.compile(r"<(pre|code)\b.*?</\1>", re.S | re.I)
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


# Endings a renamed *word* takes. Only words opt in, via `"inflect": true` in
# the registry — a product name does not pluralise into a different product, and
# `(?:s|d|ed|ing)?` hung on "Azure AD" would be noise looking for somewhere to
# happen.
INFLECTIONS = r"(?:s|d|ed|ing)?"


def pattern_for(entry):
    """The regex for one registry entry.

    Matched case-insensitively, always. The first version was not, and it is the
    reason this function exists: the registry has said "whitelist -> allowlist"
    since 2020, `make check` was green the whole time, and the site contained
    **Whitelist who can SSH in**, **Whitelist which executables are allowed to
    run** and **Whitelists exactly where scripts may load from**. A rename is a
    rename whatever the capitalisation, and a sentence-initial capital is the
    single likeliest place for one to hide, because that is where prose puts the
    word it is about.

    The trailing `\b` did the rest of the hiding: `\bwhitelist\b` does not match
    *whitelisting*, and the word most often appears as a gerund. Five of the six
    misses were one or the other; four of them were both.
    """
    return r"\b" + re.escape(entry["old"]) + (INFLECTIONS if entry.get("inflect") else "") + r"\b"


def explained(text, start, end, new):
    window = text[max(0, start - WINDOW): end + WINDOW]
    return bool(HISTORICAL.search(window)) or new.lower() in window.lower()


def findings_in(text, registry, domain="-"):
    """Every unexplained use of a renamed name in one already-prose string.

    Split out of scan() so the self-test can hand it text instead of a file. The
    logic below is the whole check; scan() is the file walk around it.
    """
    findings = []
    if True:
        for entry in registry:
            old, new = entry["old"], entry["new"]
            for m in re.finditer(pattern_for(entry), text, re.I):
                s, e = m.start(), m.end()
                # An allowed phrase means the old string is part of a name that
                # is still correct — check the text actually there, not the
                # registry's idea of it.
                context = text[s: s + max(len(a) for a in entry["allow"]) + 4] if entry["allow"] else ""
                lowered = context.lower()
                near = text[max(0, s - 12): e + 12].lower()
                if any(lowered.startswith(a.lower()) or a.lower() in near
                       for a in entry["allow"]):
                    continue
                if explained(text, s, e, new):
                    continue
                line = text[: s].count("\n") + 1
                snippet = re.sub(r"\s+", " ", text[max(0, s - 40): e + 40]).strip()
                findings.append((domain, line, old, new, snippet))
    return findings


def scan(only_domain=None):
    registry = json.loads((DATA / "renames.json").read_text(encoding="utf-8"))["renames"]
    findings = []
    for path in sorted(DATA.glob("*.html")):
        domain = path.stem
        # The acronym domain is generated from the dictionary, and the dictionary
        # legitimately records old expansions.
        if domain == "acronym" or (only_domain and domain != only_domain):
            continue
        findings += findings_in(prose(path.read_text(encoding="utf-8")), registry, domain)
    return findings


def self_test():
    """The matching rules, on text with a known answer.

    Written after the check was found to have been quietly half-working for as
    long as it had existed: case-sensitive, and with a trailing word boundary
    that a gerund cannot satisfy. Six real uses were sitting in the content with
    the build green, and the registry had listed the rename since 2020.
    """
    reg = [
        {"old": "whitelist", "new": "allowlist", "since": "2020-06", "allow": [], "inflect": True},
        {"old": "Azure AD", "new": "Entra ID", "since": "2023-07", "allow": ["Azure AD Connect"]},
    ]
    cases = [
        ("lowercase, as the registry writes it", "use a whitelist for this", 1),
        ("sentence-initial capital — the miss that started this", "Whitelist who can SSH in", 1),
        ("a gerund, which the trailing \\b used to refuse", "Application whitelisting, EDR", 1),
        ("a plural", "Whitelists exactly where scripts load from", 1),
        ("a past participle", "a whitelisted domain added to fix one", 1),
        ("explicitly historical", "allowlists, formerly whitelists", 0),
        ("the new name sitting beside it", "an allowlist (previously a whitelist)", 0),
        ("an allowed phrase keeps its old string", "Azure AD Connect syncs the directory", 0),
        ("the same product without the allowed suffix", "sign in with Azure AD", 1),
        ("a product name in the wrong case is still that product", "sign in with azure ad", 1),
        ("a non-inflecting entry does not inflect", "two Azure ADs walk into a bar", 0),
        ("substring of a longer word is not a match", "the whitelistings", 0),
    ]
    bad = 0
    for name, text, expect in cases:
        got = len(findings_in(text, reg))
        if got != expect:
            bad += 1
            print(f"FAIL : {name} — expected {expect}, got {got}")
    print(f"check_renames self-test: {len(cases)} fixtures, {bad} failure(s).")
    return bad


def main():
    args = sys.argv[1:]
    if "--self-test" in args:
        return 1 if self_test() else 0
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
