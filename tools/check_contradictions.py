#!/usr/bin/env python3
"""
check_contradictions.py — the same thing said two different ways, in two places.

At 1,369 topics across 30 domains, the failure this site is most exposed to is
not a wrong fact — it is two cards that are each defensible and disagree with
each other. A reader who meets both loses confidence in all of it, and no
existing check looks for this: the linter checks structure, the markup checker
checks well-formedness, and both are perfectly happy with two cards saying
different things.

Two kinds are checkable mechanically, and this checks those two rather than
pretending to check "contradictions" in general:

  1. **Acronym expansions written in prose that disagree with the dictionary.**
     A card writing "RTO (Recovery Time Object)" beside a dictionary that says
     "Recovery Time Objective" is a plain contradiction, and it is invisible to
     the annotator, which only ever *adds* expansions and never reads the
     hand-written ones.

  2. **Port numbers attached to a service.** "SSH on 22" appears all over a site
     like this, and a single card saying 23 is both wrong and hard to spot.

Everything else — a limit, a retention period, a version number — needs to know
what the number is *about*, which no amount of regex supplies. Those belong to
a reader, and the tool says so rather than guessing.

Both checks report; only mismatches against the dictionary can fail the build,
because the dictionary is the one place with an authoritative answer.

Usage:
  python3 tools/check_contradictions.py
  python3 tools/check_contradictions.py --ports        # the port table only
  python3 tools/check_contradictions.py --strict       # non-zero on any finding
"""

import collections
import json
import re
import sys
from html import unescape
from pathlib import Path

ROOT = Path(__file__).parent.parent
DATA = ROOT / "data"

PRE_RE = re.compile(r"<(pre|code)\b.*?</\1>", re.S | re.I)
TAG_RE = re.compile(r"<[^>]+>")
ACRO_EXP_RE = re.compile(r'<span class="acro-exp">\([^<]*?\)</span\s*>')

# "UEM (Unified Endpoint Management)" written by hand in prose. The annotator's
# own spans are stripped first, so what is left was typed by an author.
INLINE_EXP_RE = re.compile(r"\b([A-Z][A-Za-z0-9]{1,9})\s*\(([A-Z][^()]{4,60}?)\)")

# "SSH on port 22", "port 22 (SSH)", "22/tcp", "TCP 22".
PORT_PATTERNS = [
    re.compile(r"\b([A-Z][A-Za-z0-9/-]{1,14})\b[^.\n]{0,24}?\bport\s+(\d{1,5})\b"),
    re.compile(r"\bport\s+(\d{1,5})\b[^.\n]{0,12}?\(([A-Za-z][A-Za-z0-9/-]{1,14})\)"),
    re.compile(r"\b([A-Z][A-Za-z0-9/-]{1,14})\b[^.\n]{0,10}?\b(\d{1,5})/(?:tcp|udp)\b", re.I),
]

# Words dropped when taking initials: an expansion's initials are built from its
# significant words, which is how acronyms are formed in the first place.
EXP_STOP = {"of", "and", "the", "for", "a", "an", "to", "in", "on", "over",
            "with", "as", "by", "at", "or"}


def initials(exp):
    words = [w for w in re.split(r"[\s/&-]+", exp) if w and w.lower() not in EXP_STOP]
    return "".join(w[0] for w in words).upper()


def looks_like_expansion(acro, exp):
    """Does this parenthetical even claim to expand the acronym?

    Most parentheticals after a capitalised token are examples or asides —
    "SIEM (Wazuh, Security Onion)", "AI (NIST AI RMF)", "C2 (Beacon)" — and
    reporting them as disagreeing with the dictionary is pure noise. An actual
    expansion's initials spell the acronym, give or take a letter for the
    shorthands people write: "Next-Gen Firewall" for NGFW, "Process ID" for PID.

    Without this test the check produced 40 findings, of which roughly five were
    real. With it, what is left is worth reading.
    """
    letters = re.sub(r"[^A-Z]", "", acro.upper())
    got = initials(exp)
    if not letters or not got:
        return False
    if got == letters:
        return True
    # A single initial is not evidence of anything: "AI (AlphaGo)" and
    # "AP (Authenticator)" would both pass a prefix test and neither is an
    # expansion. Require at least two, for any acronym of at least two letters.
    if len(got) < 2 and len(letters) >= 2:
        return False
    # One letter of slack, in either direction, and only at the end.
    return (letters.startswith(got) or got.startswith(letters)) and abs(len(got) - len(letters)) <= 1


# Words that look like an acronym and are not one, so a parenthetical after them
# is not an expansion.
TRANSPORTS = {"TCP", "UDP", "IP", "UFW", "IPTABLES", "NFTABLES", "FIREWALLD",
              "NETSTAT", "SS", "NMAP", "NC", "NETCAT", "TCPDUMP", "SUDO", "ALLOW",
              "DENY", "SRC", "DST", "ANY", "PORT", "PORTS"}

NOT_ACRONYM = {"The", "This", "That", "A", "An", "In", "On", "For", "It", "If",
               "See", "Note", "Use", "One", "Two", "All", "And", "But", "Or"}


def prose(text):
    text = PRE_RE.sub(" ", text)
    text = ACRO_EXP_RE.sub(" ", text)
    return unescape(TAG_RE.sub(" ", text))


def dictionary():
    entries = json.loads((DATA / "acronyms.json").read_text(encoding="utf-8"))["entries"]
    return {e["a"].upper(): [m["e"] for m in e["m"]] for e in entries}


def norm(s):
    """Compare expansions on their words, not their punctuation or case."""
    return re.sub(r"[^a-z0-9 ]", " ", s.lower()).split()


def check_expansions(vocab):
    """Hand-written expansions that disagree with the dictionary."""
    findings = []
    for path in sorted(DATA.glob("*.html")):
        if path.stem == "acronym":
            continue
        text = prose(path.read_text(encoding="utf-8"))
        for m in INLINE_EXP_RE.finditer(text):
            acro, exp = m.group(1), re.sub(r"\s+", " ", m.group(2)).strip()
            if acro in NOT_ACRONYM or acro.upper() not in vocab:
                continue
            if not looks_like_expansion(acro, exp):
                continue
            known = vocab[acro.upper()]
            if any(norm(exp) == norm(k) for k in known):
                continue
            # An expansion that is a prefix or extension of a known one is a
            # style difference, not a contradiction: "Multi-Factor
            # Authentication" against "Multi Factor Authentication (MFA)".
            if any(set(norm(exp)) <= set(norm(k)) or set(norm(k)) <= set(norm(exp))
                   for k in known):
                continue
            findings.append((path.stem, acro, exp, known))
    return findings


def check_ports():
    """service -> the ports the site attaches to it, so disagreement is visible."""
    seen = collections.defaultdict(lambda: collections.defaultdict(set))
    for path in sorted(DATA.glob("*.html")):
        if path.stem == "acronym":
            continue
        text = prose(path.read_text(encoding="utf-8"))
        for n, pattern in enumerate(PORT_PATTERNS):
            for m in pattern.finditer(text):
                if n == 1:
                    port, service = m.group(1), m.group(2)
                else:
                    service, port = m.group(1), m.group(2)
                if not port.isdigit() or not 1 <= int(port) <= 65535:
                    continue
                # A transport name or a command is not a service: "TCP ... port
                # 22" and "ufw allow 22" both match the shape and say nothing.
                if service.upper() in TRANSPORTS:
                    continue
                seen[service.upper()][port].add(path.stem)
    return seen


def main():
    args = sys.argv[1:]
    strict = "--strict" in args
    failures = 0

    if "--ports" not in args:
        vocab = dictionary()
        exp = check_expansions(vocab)
        for domain, acro, written, known in exp:
            print(f"{domain}.html: '{acro} ({written})' — the dictionary says "
                  f"{', '.join(repr(k) for k in known)}")
        print(f"\n{len(exp)} hand-written expansion(s) disagree with data/acronyms.json.")
        failures += len(exp)

    ports = check_ports()
    conflicts = {s: p for s, p in ports.items() if len(p) > 1}
    if conflicts:
        print(f"\nServices this site attaches to more than one port "
              f"({len(conflicts)} of {len(ports)}):")
        for service in sorted(conflicts):
            rows = conflicts[service]
            detail = "; ".join(
                f"{port} in {', '.join(sorted(files))}"
                for port, files in sorted(rows.items(), key=lambda r: int(r[0])))
            print(f"  {service}: {detail}")
        print("\n  Many of these are legitimate — a protocol with a plaintext and a TLS "
              "port,\n  or a name that means two things. Read the list; do not automate it.")

    return 1 if (failures and strict) else 0


if __name__ == "__main__":
    sys.exit(main())
