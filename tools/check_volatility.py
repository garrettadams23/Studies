#!/usr/bin/env python3
"""
check_volatility.py — the claims that age, and whether they say when they were checked.

Two conventions live here, and both exist because a reference site's real
failure mode is not being wrong on the day it is written. It is being right on
the day it is written and silently wrong two years later.

**Volatile spans** mark the specific claim that will age:

    <span class="volatile" data-checked="2026-08">Security &amp; Compliance Center</span>

Applied to the claim, not the topic — what goes stale is a console name or a
limit, not the paragraph around it.

**Fact anchors** record where a version-specific number came from, so the next
reader can re-verify it in a minute instead of re-researching it in an hour:

    <!-- fact: six levels of management groups | source: Azure subscription
         limits | checked: 2026-08 -->

An HTML comment, so it costs the reader nothing and the next maintainer
everything.

What this checks, and what it only reports:

  * **Errors** — a malformed or future `data-checked`, or a fact anchor missing
    a field. These are unambiguous and fail the build.
  * **A queue** — spans and anchors sorted oldest first, so a freshness pass
    has somewhere to start.
  * **Candidates** — topics that name a vendor console and carry no dated span.
    Reported, never failed: plenty of them mention a console in passing without
    making a claim about it, and a gate would only teach people to add a span
    they do not mean. Each row carries the sentence it matched, because a list
    whose entries can only be dismissed by grepping for them is a list nobody
    dismisses — see `context()`.

Usage:
  python3 tools/check_volatility.py
  python3 tools/check_volatility.py --candidates   # just the work queue
  python3 tools/check_volatility.py --self-test    # the console regex, on fixtures
"""

import collections
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).parent.parent
DATA = ROOT / "data"
sys.path.insert(0, str(ROOT / "tools"))

from lint_content import domain_of, topic_label  # noqa: E402

TOPIC_RE = re.compile(r'<div class="topic"')
VOLATILE_RE = re.compile(r'<span class="volatile"([^>]*)>')
CHECKED_RE = re.compile(r'data-checked="([^"]*)"')
FACT_RE = re.compile(r"<!--\s*fact:(.*?)-->", re.S)
MONTH_RE = re.compile(r"^\d{4}-(0[1-9]|1[0-2])$")

# Named vendor surfaces. Deliberately specific: "console" on its own matches a
# terminal 133 times on this site, and a candidate list that noisy is not a
# work queue, it is wallpaper.
# Tuned against its own output. The first version reported 14 topics, of which
# **3 carried a real claim** — 21% precision, on a list a person is expected to
# read every session. Four causes, all measured:
#
#   * `exchange admin` and `teams admin` matched inside "Exchange
#     Administrator" and "Teams administration". Fixed with a trailing \b.
#   * `management console` named the Microsoft Management Console — an
#     on-premises snap-in host whose name has not moved since the 1990s — and
#     the generic phrase "most of the management consoles". Removed: this check
#     is about vendor consoles that get renamed, and MMC is the opposite of that.
#   * `cloud console` is a generic noun phrase, never a product name. Two hits,
#     both meaning "whichever cloud you use". Removed.
#   * `\badmin\.[a-z]` matched `old-admin.example.com` in a subdomain
#     enumeration example. Now requires a real boundary before it and skips
#     the reserved example domains.
#
# The point is not the four rules. It is that an advisory list a person reads
# every session is worth only as much as its precision, and precision here was
# measurable in one pass over the output.
CONSOLE_RE = re.compile(
    r"admin cent(?:er|re)\b|entra admin\b|azure portal\b|aws console\b|"
    r"gcp console\b|purview portal\b|defender portal\b|"
    r"intune (?:portal|admin)\b|exchange admin\b|teams admin\b|"
    r"sharepoint admin\b|security cent(?:er|re)\b|"
    r"(?<![\w-])portal\.(?!example\b)[a-z]|(?<![\w-])admin\.(?!example\b)[a-z]|"
    # The console *hosts*, enumerated rather than pattern-matched. This set is
    # small, and it is the highest-value thing on the list: endpoint.microsoft
    # .com became intune.microsoft.com, and every card naming the old one was
    # wrong the day it moved. A broad `\w+\.microsoft\.com` would swallow every
    # learn.microsoft.com documentation link instead.
    r"\b(?:entra|intune|purview|compliance|security)\.microsoft\.com\b",
    re.I)


def context(block, match, width=62):
    """The words either side of a console hit, as a reader would see them.

    The row above names the topic and the phrase that matched; it never names
    what the sentence was doing, so dismissing a false positive costs a grep.
    Measured on this site's own output: all three candidates reported today are
    false positives, and the newest is a shape the fixtures below do not cover —
    *every Exchange admin meets* is a job title, not a console. The regex cannot
    separate those two senses without evidence it does not have, so the report
    shows the sentence and lets a person do it in a second instead.
    """
    window = block[max(0, match.start() - 400):match.end() + 400]
    plain = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", window)).strip()
    at = plain.lower().find(match.group(0).lower())
    if at == -1:                       # the hit was inside an attribute
        return plain[:width * 2]
    start, end = max(0, at - width), min(len(plain), at + len(match.group(0)) + width)
    return (("…" if start else "") + plain[start:end]
            + ("…" if end < len(plain) else ""))


def topics(text):
    starts = [m.start() for m in TOPIC_RE.finditer(text)]
    for n, start in enumerate(starts):
        end = starts[n + 1] if n + 1 < len(starts) else len(text)
        yield text[start:end]


def main():
    today = datetime.now(timezone.utc).strftime("%Y-%m")
    errors = []
    spans, facts, candidates = [], [], []

    for path in sorted(DATA.glob("*.html")):
        if path.name == "acronym.html":
            continue
        domain = domain_of(path)
        text = path.read_text(encoding="utf-8")

        for block in topics(text):
            label, _ = topic_label(block)
            block_spans = VOLATILE_RE.findall(block)
            for attrs in block_spans:
                m = CHECKED_RE.search(attrs)
                if not m:
                    errors.append(f"{path.name}: a volatile span has no data-checked "
                                  f"(in '{label[:50]}')")
                    continue
                when = m.group(1)
                if not MONTH_RE.match(when):
                    errors.append(f"{path.name}: data-checked=\"{when}\" is not YYYY-MM "
                                  f"(in '{label[:50]}')")
                elif when > today:
                    errors.append(f"{path.name}: data-checked=\"{when}\" is in the future "
                                  f"(in '{label[:50]}')")
                else:
                    spans.append((when, domain, label))

            for body in FACT_RE.findall(block):
                fields = dict()
                for part in body.split("|"):
                    if ":" in part:
                        k, v = part.split(":", 1)
                        fields[k.strip().lower()] = " ".join(v.split())
                missing = [k for k in ("source", "checked") if not fields.get(k)]
                claim = " ".join(body.split("|")[0].split())
                if missing:
                    errors.append(f"{path.name}: fact anchor '{claim[:40]}' is missing "
                                  f"{', '.join(missing)}")
                elif not MONTH_RE.match(fields["checked"]):
                    errors.append(f"{path.name}: fact anchor '{claim[:40]}' has "
                                  f"checked=\"{fields['checked']}\", not YYYY-MM")
                else:
                    facts.append((fields["checked"], domain, claim))

            if not block_spans:
                hit = CONSOLE_RE.search(block)
                if hit:
                    candidates.append((domain, label, hit.group(0),
                                       context(block, hit)))

    if "--candidates" not in sys.argv:
        for e in errors:
            print(f"ERROR {e}")
        by_month = collections.Counter(w for w, _, _ in spans + facts)
        print(f"\n{len(spans)} volatile span(s), {len(facts)} fact anchor(s).")
        for month in sorted(by_month):
            print(f"  {month}  {by_month[month]}")
        oldest = sorted(spans + facts)[:5]
        if oldest and oldest[0][0] < today:
            print("\n  oldest, worth re-checking first:")
            for when, domain, label in oldest:
                print(f"    {when}  {domain:12} {label[:56]}")

    print(f"\n{len(candidates)} topic(s) name a vendor console with no dated span:")
    for domain, label, hit, ctx in candidates[:20]:
        print(f"  {domain:12} {label[:52]:54} — {hit}")
        print(f"    {ctx}")
    if len(candidates) > 20:
        print(f"  …and {len(candidates) - 20} more")

    return 1 if errors else 0


# Fixtures, not examples: each line is a shape that was actually in the content
# when CONSOLE_RE was tuned. A regex narrowed on evidence is one edit away from
# being widened back by someone who does not have the evidence, so the evidence
# lives here.
CONSOLE_FIXTURES = [
    # (text, should_match, why)
    ("Entra admin center ▸ Conditional Access", True, "a named console path"),
    ("sign in at intune.microsoft.com", True, "a console host"),
    ("Guest access in Teams | Teams admin", True, "names where a setting lives"),
    ("the Microsoft 365 admin centre", True, "a console by name"),
    ("Exchange Administrator — mailboxes, mail flow", False,
     "a role name, not a console"),
    ("most Teams administration is really SharePoint", False,
     "'teams admin' inside 'administration'"),
    ("gpmc.msc — Group Policy Management Console", False,
     "an on-premises snap-in, renamed never"),
    ("Server Core removes most of the management consoles", False,
     "generic prose"),
    ("Click through cloud console vs define in code", False,
     "'cloud console' is a noun phrase, not a product"),
    ("finding the forgotten old-admin.example.com", False,
     "an example hostname in a subdomain-enumeration card"),
    ("Two on-prem mechanics every Exchange admin meets", True,
     "a job title, not a console — indistinguishable from 'in the Exchange "
     "admin' without evidence, so the report shows the sentence instead"),
]


def self_test():
    failures = 0
    for text, want, why in CONSOLE_FIXTURES:
        got = bool(CONSOLE_RE.search(text))
        if got != want:
            failures += 1
            print(f"FAIL  expected {'a match' if want else 'no match'} "
                  f"({why}): {text!r}")
    print(f"self-test: {len(CONSOLE_FIXTURES)} fixtures, {failures} failure(s).")
    return 1 if failures else 0


if __name__ == "__main__":
    if "--self-test" in sys.argv:
        sys.exit(self_test())
    sys.exit(main())
