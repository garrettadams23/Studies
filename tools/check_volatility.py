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
    they do not mean.

Usage:
  python3 tools/check_volatility.py
  python3 tools/check_volatility.py --candidates   # just the work queue
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
CONSOLE_RE = re.compile(
    r"admin cent(?:er|re)|entra admin|azure portal|aws console|gcp console|"
    r"cloud console|purview portal|defender portal|intune (?:portal|admin)|"
    r"exchange admin|teams admin|sharepoint admin|security cent(?:er|re)|"
    r"management console|\bportal\.[a-z]|\badmin\.[a-z]",
    re.I)


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

            if not block_spans and CONSOLE_RE.search(block):
                hit = CONSOLE_RE.search(block).group(0)
                candidates.append((domain, label, hit))

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
    for domain, label, hit in candidates[:20]:
        print(f"  {domain:12} {label[:52]:54} — {hit}")
    if len(candidates) > 20:
        print(f"  …and {len(candidates) - 20} more")

    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
