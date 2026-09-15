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

A third mode narrows the same two checks to the place they are most likely to
find something. Site-wide, two cards that disagree are usually two cards about
different things that happen to share a word. Inside a **near-duplicate pair**
— two topics whose titles overlap by half or more, or whose subjects sit one
inside the other, per `near_duplicates.py` — both cards are about the same
subject by construction, so a disagreement
between them is a bug in one of them rather than a coincidence. plan-archive.md Phase
10 T9.

Usage:
  python3 tools/check_contradictions.py
  python3 tools/check_contradictions.py --ports        # the port table only
  python3 tools/check_contradictions.py --pairs        # near-duplicate pairs only
  python3 tools/check_contradictions.py --self-test    # the pair check, on known answers
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
# The gap between the service and the port must contain **no other capitalised
# word**. Without that, "In this estate SSH on port 22" keys the claim on "In":
# the scan starts at the leftmost capital and the first match wins. On real
# prose the bug is quieter but not absent — it is why this table used to key
# claims on CAPTURE, DEFAULT, PRIVACY and SECURE. Found by injecting a known
# contradiction into a real pair after the --pairs self-test already passed,
# which is the whole argument for doing the end-to-end check as well.
PORT_PATTERNS = [
    re.compile(r"\b([A-Z][A-Za-z0-9/-]{1,14})\b[^.\nA-Z]{0,24}\bport\s+(\d{1,5})\b"),
    re.compile(r"\bport\s+(\d{1,5})\b[^.\n]{0,12}?\(([A-Za-z][A-Za-z0-9/-]{1,14})\)"),
    re.compile(r"\b([A-Z][A-Za-z0-9/-]{1,14})\b[^.\nA-Z]{0,10}\b(\d{1,5})/(?i:tcp|udp)\b"),
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

# Capitalised words that appear next to a port number and are not the service:
# "Ticket-Based Authentication (port 88)", "Web pages use port 80/443". A short
# list on purpose — a long one starts discarding real service names.
NOT_SERVICE = {"AUTHENTICATION", "PROTOCOL", "WEB", "SERVICE", "SERVER", "TRAFFIC",
               "DEFAULT", "SOURCE", "DESTINATION", "STANDARD", "SECURE", "ENCRYPTED",
               "SHOW", "USE", "USES", "PORT", "PORTS", "NUMBER", "RANGE"}


DIV_OPEN_RE = re.compile(r"<div\b", re.I)
DIV_CLOSE_RE = re.compile(r"</div\s*>", re.I)
CODE_DIV_RE = re.compile(r'<div class="code-block"', re.I)


def strip_code_divs(text):
    """Remove `<div class="code-block">…</div>`, matching nesting.

    The house style writes code two ways — `pre.code-block` and
    `div.code-block` — and only the first is a `<pre>`. PRE_RE never saw the
    second, so **every shell sample written as a div has been read as prose**
    by this checker since it was written. That is why the port table keyed
    claims on DEFAULT, SHOW and SOURCE: they are the first word of a `# Default
    port 22` style comment.
    """
    out, pos = [], 0
    for m in CODE_DIV_RE.finditer(text):
        if m.start() < pos:
            continue
        out.append(text[pos:m.start()])
        depth, i = 0, m.start()
        while i < len(text):
            o = DIV_OPEN_RE.search(text, i)
            c = DIV_CLOSE_RE.search(text, i)
            if not c:
                i = len(text)
                break
            if o and o.start() < c.start():
                depth += 1
                i = o.end()
                continue
            depth -= 1
            i = c.end()
            if depth == 0:
                break
        pos = i
    out.append(text[pos:])
    return " ".join(out)


def prose(text):
    text = strip_code_divs(text)
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


# ── the table half ──────────────────────────────────────────────────────────
#
# The site's canonical port list is a **table**, and this check could not read
# one. The patterns above find where a port is *mentioned* in a sentence; they
# do not find where a reference *states* one. `net`'s *Common Ports — Protocol
# Reference* has a header row reading `Port(s) | Protocol | Transport | Security
# Notes` and rows under it, and a wrong number there is at once the likeliest
# port error on this site and the least likely to be caught by eye. The prose
# scan saw none of it — fifteen services, fourteen keyed from a single domain,
# against forty-five service/port pairs sitting in three labelled tables.
#
# Read by **header**, never by shape. A table qualifies when its header row has
# one cell naming a port and another naming a protocol or service; anything
# else is left alone. That is the same sharp test the rest of this toolchain
# prefers: the header says what the column is, or the table is not one of these.
TABLE_RE = re.compile(r"<table\b[^>]*>(.*?)</table>", re.S | re.I)
ROW_RE = re.compile(r"<tr\b[^>]*>(.*?)</tr>", re.S | re.I)
CELL_RE = re.compile(r"<t([hd])\b[^>]*>(.*?)</t\1>", re.S | re.I)
PORT_HEADER_RE = re.compile(r"\bports?\b|\bport\(s\)", re.I)
SERVICE_HEADER_RE = re.compile(r"\bprotocols?\b|\bservices?\b|\bapplications?\b", re.I)
PARENS_RE = re.compile(r"\([^()]*\)")


def cell_text(html):
    return re.sub(r"\s+", " ", TAG_RE.sub(" ", ACRO_EXP_RE.sub("", html))).strip()


def split_row(port_cell, service_cell):
    """(service, port) pairs from one row, or nothing when the row is ambiguous.

    A reference table combines related rows, and combining is where a naive
    reader invents a contradiction. Three real shapes, and only the third needs
    a rule:

        20 / 21   FTP (data/control)    one service, two ports  -> both are FTP
        22        SSH / SFTP / SCP      one port, three services -> all three
        514       Syslog                the ordinary case
        993 / 995 IMAPS / POP3S         two and two -> pair them, positionally

    The first prototype of this read the third row as *IMAPS on 993 and 995* and
    reported IMAPS as disagreeing with itself. The row was correct and the reader
    was wrong, which is the failure this file exists to avoid committing itself.

    Parentheticals are stripped before splitting, so the slash inside
    "FTP (data/control)" is not mistaken for a service separator.
    """
    ports = [n for n in re.findall(r"\b(\d{1,5})\b", port_cell)
             if 1 <= int(n) <= 65535]
    names = [s.strip() for s in re.split(r"\s*/\s*", PARENS_RE.sub(" ", service_cell))
             if re.match(r"^[A-Za-z][A-Za-z0-9+.-]{1,14}$", s.strip())]
    if not ports or not names:
        return []
    if len(names) == 1:
        return [(names[0], p) for p in ports]
    if len(ports) == 1:
        # The symmetric case, and the one the first version dropped: several
        # services on one port is how a reference writes a family. `22 | SSH /
        # SFTP / SCP` is three true claims, and skipping it lost the site's only
        # tabular statement of the most quoted port on it. Found by injecting a
        # wrong number into the real table and watching nothing happen.
        return [(n, ports[0]) for n in names]
    if len(names) == len(ports):
        return list(zip(names, ports))
    # Several services and a different number of ports: which goes with which is
    # not recoverable from the row, and guessing is how a check starts inventing
    # findings. Skipped on purpose.
    return []


def table_ports(src):
    """(service, port) from every header-labelled port table in one file."""
    out = []
    for table in TABLE_RE.finditer(src):
        rows = [[(kind, cell_text(html)) for kind, html in CELL_RE.findall(r)]
                for r in ROW_RE.findall(table.group(1))]
        header = next((r for r in rows if any(k == "h" for k, _ in r)), None)
        if not header:
            continue
        labels = [v for _, v in header]
        port_i = next((i for i, v in enumerate(labels) if PORT_HEADER_RE.search(v)), None)
        svc_i = next((i for i, v in enumerate(labels) if SERVICE_HEADER_RE.search(v)), None)
        if port_i is None or svc_i is None or port_i == svc_i:
            continue
        for row in rows:
            if any(k == "h" for k, _ in row) or len(row) <= max(port_i, svc_i):
                continue
            out += split_row(row[port_i][1], row[svc_i][1])
    return out


def check_ports():
    """service -> the ports the site attaches to it, so disagreement is visible."""
    seen = collections.defaultdict(lambda: collections.defaultdict(set))
    for path in sorted(DATA.glob("*.html")):
        if path.stem == "acronym":
            continue
        src = path.read_text(encoding="utf-8")
        for service, port in table_ports(src):
            if service.upper() in TRANSPORTS or service.upper() in NOT_SERVICE:
                continue
            seen[service.upper()][port].add(path.stem)
        text = prose(src)
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
                if service.upper() in TRANSPORTS or service.upper() in NOT_SERVICE:
                    continue
                seen[service.upper()][port].add(path.stem)
    return seen


def topic_bodies():
    """(domain, title, prose) for every hand-written topic on the site.

    near_duplicates.py already splits domains into topics and pulls the title;
    this reuses its regexes rather than growing a second, subtly different
    splitter — the two would drift and the pair check would silently start
    comparing the wrong text.
    """
    import near_duplicates as nd
    domains = json.loads((DATA / "domains.json").read_text(encoding="utf-8"))
    for dom in domains:
        did = dom["id"]
        if did in nd.SKIP_DOMAINS:
            continue
        text = "".join(p.read_text(encoding="utf-8") for p in nd.domain_files(did))
        starts = [m.start() for m in nd.TOPIC_RE.finditer(text)]
        for n, start in enumerate(starts):
            end = starts[n + 1] if n + 1 < len(starts) else len(text)
            block = text[start:end]
            m = nd.NAME_RE.search(nd.ACRO_RE.sub("", block))
            if not m:
                continue
            title = re.sub(r"\s+", " ", TAG_RE.sub("", m.group(1))).strip()
            yield did, title, prose(block)


def claims(text, vocab):
    """The two mechanically checkable claim kinds, keyed for comparison."""
    expansions = collections.defaultdict(set)
    for m in INLINE_EXP_RE.finditer(text):
        acro, exp = m.group(1), re.sub(r"\s+", " ", m.group(2)).strip()
        if acro in NOT_ACRONYM or not looks_like_expansion(acro, exp):
            continue
        expansions[acro.upper()].add(" ".join(norm(exp)))

    ports = collections.defaultdict(set)
    for n, pattern in enumerate(PORT_PATTERNS):
        for m in pattern.finditer(text):
            service, port = (m.group(2), m.group(1)) if n == 1 else (m.group(1), m.group(2))
            if not port.isdigit() or not 1 <= int(port) <= 65535:
                continue
            if service.upper() in TRANSPORTS or service.upper() in NOT_SERVICE:
                continue
            ports[service.upper()].add(port)
    return expansions, ports


def disagreements(c1, c2):
    """(kind, key, values_a, values_b) where two claim sets contradict.

    Two cards that each attach several values to a key are not contradicting as
    long as they overlap somewhere: SMTP on 25 in one card and on 25, 465, 587
    in another is one card being fuller, not two cards disagreeing.
    """
    out = []
    for kind, a, b in (("expansion", c1[0], c2[0]), ("port", c1[1], c2[1])):
        for key in sorted(set(a) & set(b)):
            if a[key] & b[key]:
                continue
            out.append((kind, key, sorted(a[key]), sorted(b[key])))
    return out


def check_pairs(vocab, floor):
    """Disagreements *between* the two halves of a near-duplicate pair.

    "Near-duplicate" means whatever `near_duplicates.py` means by it, and that
    widened: a title wholly inside another title is the same subject and scores
    below any Jaccard floor. Fixing the census and leaving this on the old
    definition would have left the sibling tool blind to exactly the pairs the
    census had just learned to see. 38 pairs -> 95, and still 0 disagreements.
    """
    import itertools
    import near_duplicates as nd

    rows = [(d, t, nd.tokens(t), claims(body, vocab),
             nd.tokens(nd.head(t), expand=True), nd.tokens(nd.head(t)))
            for d, t, body in topic_bodies()]
    findings, compared = [], 0
    for (d1, t1, k1, c1, h1, p1), (d2, t2, k2, c2, h2, p2) in itertools.combinations(rows, 2):
        if nd.overlap(k1, k2) < floor and not (
                nd.overlap(k1, k2) >= floor / 2 and nd.contained(h1, h2, p1, p2)):
            continue
        compared += 1
        for kind, key, a, b in disagreements(c1, c2):
            findings.append((kind, key, d1, t1, a, d2, t2, b))
    return findings, compared, len(rows)


# (name, text A, text B, how many disagreements this pair should produce)
PAIR_FIXTURES = [
    ("a port that disagrees is found",
     "<p>Kerberos on port 88 is what a domain controller answers.</p>",
     "<p>Kerberos on port 89, which is the typo this check exists for.</p>", 1),
    ("the same port twice is not a finding",
     "<p>Kerberos on port 88 is what a domain controller answers.</p>",
     "<p>Traffic reaches Kerberos on port 88 during authentication.</p>", 0),
    ("one card being fuller is not a disagreement",
     "<p>SMTP on port 25 between servers.</p>",
     "<p>SMTP on port 25, SMTP on port 587 for submission.</p>", 0),
    ("an expansion that disagrees is found",
     "<p>The RTO (Recovery Time Objective) is agreed with the business.</p>",
     "<p>Its RTO (Recovery Time Object) is four hours.</p>", 1),
    ("a parenthetical that is not an expansion is ignored",
     "<p>The SIEM (Wazuh, Security Onion) receives the logs.</p>",
     "<p>A SIEM (Splunk, Elastic) is where this lands.</p>", 0),
    ("code blocks do not produce claims",
     "<pre><code>ssh -p 2222 host   # SSH on port 2222</code></pre>",
     "<p>SSH on port 22 unless someone moved it.</p>", 0),
    ("two unrelated keys do not compare",
     "<p>LDAP on port 389 for directory reads.</p>",
     "<p>RDP on port 3389 for remote desktop.</p>", 0),
    ("a div.code-block is not prose",
     '<div class="code-block"><span class="com"># Default port 22</span>'
     '<span class="fn">ssh</span> -p 3344 host</div>',
     "<p>SSH on port 22 unless someone moved it.</p>", 0),
    ("the service is the word nearest the port, not the first capital",
     "<p>In this estate SSH on port 22 is the only path.</p>",
     "<p>Here SSH on port 2200 is the only path.</p>", 1),
]


# One row of a port table, and what it is allowed to claim. The third and the
# last are the reason this function exists at all: a combined row read naively
# reports a protocol as disagreeing with itself, and a row whose two cells
# cannot be lined up has to be skipped rather than guessed at.
ROW_FIXTURES = [
    ("the ordinary case", "514", "Syslog", [("Syslog", "514")]),
    ("one service, two ports", "20 / 21", "FTP (data/control)",
     [("FTP", "20"), ("FTP", "21")]),
    ("two services, two ports, paired in order", "993 / 995", "IMAPS / POP3S",
     [("IMAPS", "993"), ("POP3S", "995")]),
    ("a slash inside a parenthetical is not a separator", "443", "HTTPS (HTTP/TLS)",
     [("HTTPS", "443")]),
    ("a range in the port cell", "137 / 139", "NetBIOS",
     [("NetBIOS", "137"), ("NetBIOS", "139")]),
    ("several services on one port is a family, not an ambiguity", "22",
     "SSH / SFTP / SCP", [("SSH", "22"), ("SFTP", "22"), ("SCP", "22")]),
    ("counts that do not line up are skipped, not guessed", "80 / 443 / 8080",
     "HTTP / HTTPS", []),
    ("a port out of range is not a port", "99999", "Nothing", []),
    ("no service name to key on", "22", "—", []),
]


def self_test():
    """The pair comparison and the table row reader, on known answers.

    This mode reported zero findings across every real pair on its first run,
    which is the right answer and is indistinguishable from a check that cannot
    find anything. These fixtures are what tells the two apart.
    """
    vocab = dictionary()
    failures = 0
    for name, port_cell, service_cell, want in ROW_FIXTURES:
        got = split_row(port_cell, service_cell)
        status = "ok  " if got == want else "FAIL"
        if got != want:
            failures += 1
            print(f"  {status} {name}: expected {want}, got {got}")
        else:
            print(f"  {status} {name}")
    for name, a, b, want in PAIR_FIXTURES:
        got = disagreements(claims(prose(a), vocab), claims(prose(b), vocab))
        status = "ok  " if len(got) == want else "FAIL"
        if len(got) != want:
            failures += 1
            print(f"  {status} {name}: expected {want}, got {len(got)} — {got}")
        else:
            print(f"  {status} {name}")
    print(f"\nself-test: {len(PAIR_FIXTURES) + len(ROW_FIXTURES)} fixtures, "
          f"{failures} failure(s).")
    return 1 if failures else 0


def main():
    args = sys.argv[1:]
    strict = "--strict" in args
    failures = 0

    if "--self-test" in args:
        return self_test()

    if "--pairs" in args:
        floor = float(args[args.index("--floor") + 1]) if "--floor" in args else 0.5
        found, compared, total = check_pairs(dictionary(), floor)
        for kind, key, d1, t1, a, d2, t2, b in found:
            print(f"  {kind} '{key}' disagrees:")
            print(f"    [{d1}] {t1[:58]} says {', '.join(repr(x) for x in a)}")
            print(f"    [{d2}] {t2[:58]} says {', '.join(repr(x) for x in b)}")
        print(f"\n{len(found)} disagreement(s) across {compared} near-duplicate "
              f"pair(s), from {total:,} topics.")
        if not found:
            print("  Nothing — which is the expected result and the reason to keep "
                  "running it.\n  See this file's docstring for what this mode can "
                  "and cannot see.")
        return 1 if (found and strict) else 0

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
