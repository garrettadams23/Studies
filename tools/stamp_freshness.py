#!/usr/bin/env python3
"""
stamp_freshness.py — Records when each topic was last genuinely edited.

Writes `data-reviewed="YYYY-MM"` onto every `.topic` in `data/*.html`, taken
from git history rather than from anyone remembering to update it.

The problem this has to solve
-----------------------------
`git blame` reports the last commit that touched a line, and mechanical passes
touch nearly every line. The acronym annotation alone rewrote 2,388 lines
across 19 files in one commit, and this script's own stamping pass rewrites
every `.topic` opening tag. A naive blame would therefore report the whole site
as freshly reviewed — worse than having no metadata at all.

So before blaming, each commit in a file's history is classified: if the file's
content *with mechanical markup normalised away* is identical to its parent's,
that commit changed nothing real and is passed to `git blame --ignore-rev`.
Mechanical markup means the annotator's `.acro-exp` spans and this script's own
`data-reviewed` attributes, which makes the pass self-healing — the stamping
commit classifies itself as mechanical on the next run, with no SHA list to
maintain by hand.

Usage:
    python3 tools/stamp_freshness.py --only m365   # stamp one domain — the usual case
    python3 tools/stamp_freshness.py --current-only   # whole tree, safely: see below
    python3 tools/stamp_freshness.py            # stamp everything; see the warning below
    python3 tools/stamp_freshness.py --verify   # CI gate: are the stamps valid?
    python3 tools/stamp_freshness.py --check    # report drift, write nothing
    python3 tools/stamp_freshness.py --report   # oldest volatile topics

**Prefer --only.** A whole-tree write re-derives every stamp on the site from
`git blame`, and blame heuristics differ between git releases — one content wave
that added 18 cards also moved ~250 untouched topics into later months with no
edit behind the move. Stamping the file you actually changed avoids inventing
freshness for the rest of the site.

**Or `--current-only`, when several sessions have gone unstamped.** It re-derives
everything and then writes only the moves that land in *this* month, holding every
earlier-month re-derivation at whatever the file already said. Measured on the pass
that produced it: 453 moves, 158 into the current month — real content work nobody
had re-stamped — and 295 shuffling between two earlier months where the content had
not changed and only the derivation had. The second kind is what `--only` exists to
avoid, and this is how to avoid it without knowing in advance which files to name.

--verify and --check are not the same question. --verify asks whether every
topic carries a plausible stamp, using no git at all, so its answer does not
depend on the git version running it. --check re-derives every stamp from
`git blame` and reports any that would move — useful locally, unsuitable as a
build gate, because blame heuristics differ between git releases.
"""

import re
import subprocess
import sys
from datetime import datetime, timezone
from html import unescape
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"

# Generated from data/acronyms.json — its dates would be meaningless.
EXCLUDE = {"acronym.html"}

TOPIC_OPEN_RE = re.compile(r'<div class="topic"((?:\s+[^>]*?)?)>')
REVIEWED_ATTR_RE = re.compile(r'\s+data-reviewed="\d{4}-\d{2}"')
ACRO_SPAN_RE = re.compile(r'\s*<span class="acro-exp">\([^<]*?\)</span\s*>')
# Only the wrapper, never the title inside it — a retitled card is a real edit
# and must keep showing up as one. Safe to match non-greedily because ACRO_SPAN_RE
# has already removed the only spans that nest inside a topic name.
TOPIC_NAME_TAG_RE = re.compile(r'<span\b[^>]*class="topic-name"[^>]*>(.*?)</span\s*>', re.S)
# Unwrapping a stray <h3> around a title is markup, not a rewrite. Safe to strip
# the tags anywhere: a heading whose text changed still differs after the strip.
HEADER_H_TAG_RE = re.compile(r"</?h[1-6]\b[^>]*>")

# Prettier splits tags across lines — `<span class="topic-name"\n  >` and
# `</span\n>` are both valid and both appear in data/*.html. Every pattern that
# matches markup here has to tolerate that, or it silently under-reports.
TOPIC_NAME_RE = re.compile(r'<span\b[^>]*class="topic-name"[^>]*>(.*?)</span\s*>', re.S)

# A marked claim: <span class="volatile" data-checked="YYYY-MM">…</span>.
# This is what --report reads. The claim carries its own verification date,
# which is deliberately not the card's `data-reviewed`: rewording a card is not
# the same act as re-checking that a console path still exists.
VOLATILE_CLAIM_RE = re.compile(
    r'<(\w+)\b[^>]*\bclass="[^"]*\bvolatile\b[^"]*"[^>]*'
    r'\bdata-checked="(\d{4}-\d{2})"[^>]*>(.*?)</\1\s*>',
    re.S,
)

# Terms that *might* indicate something that moves. Kept only to help an author
# find claims worth marking — never as the report itself.
#
# It was the report, and it was not good enough: 184 of 888 topics, 20% of the
# site, including "Google Chrome — Keyboard Shortcuts" and "Access Control
# Models". `console` alone was the sole trigger for 25 of them. Matching the
# *shape* of a claim instead (breadcrumbs, prices, versions) halves the noise
# and still cannot tell "Settings > Devices > Enrol" from the comparison
# "Python → Bash → PowerShell", because the difference is meaning, not form.
# Hence the explicit mark; this is now a candidate finder, under --candidates.
VOLATILE_HINTS = re.compile(
    r"\b(Intune|MECM|SCCM|Entra|Azure|AWS|GCP|Jamf|Workspace ONE|Autopilot|"
    r"portal|console|admin center|pricing|price|licen[cs]e|SKU|tier|"
    r"as of \d{4}|version \d)\b",
    re.IGNORECASE,
)


def git(*args, **kw):
    return subprocess.run(
        ["git", *args], cwd=ROOT, capture_output=True, text=True, **kw
    )


def normalise(text):
    """Strip markup that mechanical passes own, so real edits can be spotted.

    The `.topic-name` wrapper counts as mechanical: tools/fix_topic_names.py
    adds it around a title that was already there, and nobody re-read those
    cards. Detecting it here is what stops the wrapping commit from claiming
    ninety topics were reviewed the month it ran — the same trap the acronym
    annotator set, solved the same way.
    """
    text = ACRO_SPAN_RE.sub("", text)
    text = TOPIC_NAME_TAG_RE.sub(r"\1", text)
    text = HEADER_H_TAG_RE.sub("", text)
    return REVIEWED_ATTR_RE.sub("", text)


def is_mechanical(sha, rel_path):
    after = git("show", f"{sha}:{rel_path}")
    parent = git("show", f"{sha}^:{rel_path}")
    if after.returncode != 0 or parent.returncode != 0:
        return False                        # added or deleted, not a markup pass
    return normalise(after.stdout) == normalise(parent.stdout)


_GLOBAL_PASSES = None


def global_markup_passes():
    """Commits that changed nothing real in *any* domain file they touched.

    The annotator, the freshness stamp and the `.topic-name` wrap all sweep
    every file at once. Such a commit is safe to ignore when blaming any file,
    which matters once content moves between files: after a domain split, a
    card's history lives in the file it came from, and a per-path scan of the
    new file cannot see the sweeps that touched the old one. Blame follows the
    content with -C; the ignore list has to follow it too.
    """
    global _GLOBAL_PASSES
    if _GLOBAL_PASSES is not None:
        return _GLOBAL_PASSES
    out = []
    for sha in git("log", "--format=%H", "--", "data").stdout.split():
        touched = [f for f in git("show", "--name-only", "--format=", sha).stdout.split()
                   if f.startswith("data/") and f.endswith(".html")
                   and f.rsplit("/", 1)[-1] not in EXCLUDE]
        if touched and all(is_mechanical(sha, f) for f in touched):
            out.append(sha)
    _GLOBAL_PASSES = out
    return out


def mechanical_revs(rel_path):
    """Commits to ignore when blaming this file.

    Its own mechanical commits, plus every whole-tree markup pass — a rev that
    never touched this path costs nothing to list.
    """
    own = [sha for sha in git("log", "--format=%H", "--", rel_path).stdout.split()
           if is_mechanical(sha, rel_path)]
    return sorted(set(own) | set(global_markup_passes()))


def blame_times(rel_path, ignore, worktree_text):
    """line number (1-based) -> author epoch, ignoring mechanical commits.

    Blames HEAD rather than the working tree whenever the two differ only by
    mechanical markup. Otherwise this script's own stamp would show up as an
    uncommitted change dated *now*, and every topic would read as reviewed
    today the moment it was stamped a second time. When there are real
    uncommitted edits, the working tree is blamed and the new lines correctly
    date to now.
    """
    head = git("show", f"HEAD:{rel_path}")
    use_head = (
        head.returncode == 0
        and normalise(head.stdout) == normalise(worktree_text)
        and head.stdout.count("\n") == worktree_text.count("\n")
    )
    # -C -C follows lines moved or copied from another file *modified in the
    # same commit*. Splitting a domain moves cards verbatim into a new file, and
    # without this every one of them would blame to the split and claim it was
    # reviewed that month. Moving a card is not reviewing it.
    #
    # Two -C, not three: a third makes blame search every file in every commit,
    # which took this script from seconds to minutes across 21 files and buys
    # nothing — a domain split modifies both files in the one commit.
    cmd = ["blame", "--line-porcelain", "-C", "-C"]
    # The conventional escape hatch, for the commits this script cannot infer:
    # -C finds most of a relocated card, but git's copy detection has a minimum
    # block size, so a few short runs still blame the move. Listing the commit
    # here is how git itself expects that to be handled.
    if (ROOT / ".git-blame-ignore-revs").exists():
        cmd += ["--ignore-revs-file", ".git-blame-ignore-revs"]
    for sha in ignore:
        cmd += ["--ignore-rev", sha]
    cmd += (["HEAD"] if use_head else []) + ["--", rel_path]
    result = git(*cmd)
    if result.returncode != 0:
        # A file git has never seen — a domain being split out, before the
        # commit that creates it. Keep whatever stamps the markup already
        # carries; the next run, once it is committed, will confirm them.
        #
        # Narrow on purpose. A blanket except here once swallowed a malformed
        # .git-blame-ignore-revs and silently reported "0 topics stamped"
        # instead of failing, which is the worst way for a freshness tool to
        # be wrong: quietly.
        if "no such path" in result.stderr or "does not exist" in result.stderr:
            return {}
        raise SystemExit(f"git blame failed for {rel_path}:\n{result.stderr}")

    times, line_no, pending = {}, 0, None
    for line in result.stdout.splitlines():
        if re.match(r"^[0-9a-f]{40} \d+ (\d+)", line):
            line_no = int(line.split()[2])
        elif line.startswith("author-time "):
            pending = int(line.split()[1])
        elif line.startswith("\t") and pending is not None:
            times[line_no] = pending
            pending = None
    return times


def body_times(times, start, end):
    """Blame times for a topic's body — the span minus its opening tag line.

    The opening line is the one this script rewrites, and excluding it is what
    stops the stamp from oscillating. The mechanism: writing a corrected stamp
    inside a commit that *also* adds real content makes that commit
    non-mechanical, so it cannot be ignored when blaming. Blame then dates the
    opening line to that commit, `max` picks it up, and the next run pushes the
    topic forward again — after which the stamping commit is mechanical, the
    ignore list catches it, and the run after that pulls it back. Three topics
    in ops.html bounced between 2026-07 and 2026-08 that way across two waves.

    A card's opening tag carries no content, so its blame date can never be
    honest evidence that anyone reviewed the card: a real edit always touches a
    body line too. Dropping it costs nothing and removes the cycle.

    The fallback matters. Some topics in data/*.html are written on a single
    line, header and body together; there the opening line *is* the content, so
    excluding it would leave nothing to date and the topic would silently keep
    whatever stamp it already had.
    """
    body = [times[n] for n in range(start + 1, end + 1) if n in times]
    return body or [times[n] for n in range(start, end + 1) if n in times]


def topic_spans(lines):
    """[(start_line, end_line, index_of_opening_tag)] for every .topic."""
    starts = [i for i, l in enumerate(lines, 1) if '<div class="topic"' in l]
    spans = []
    for n, start in enumerate(starts):
        end = starts[n + 1] - 1 if n + 1 < len(starts) else len(lines)
        spans.append((start, end))
    return spans


def verify():
    """The invariants a build can actually be failed on.

    Not the exact month. `--check` re-derives every stamp from `git blame`, and
    blame is a heuristic whose answers move between git versions: this file
    passed --check under git 2.43 and failed it under 2.54 on a GitHub runner,
    because -C copy detection and --ignore-rev reassignment disagreed about
    lines an <h3> unwrap had rewritten. Nothing about the content had changed.

    A gate that flips when the runner image upgrades is noise, and it reports
    nothing about whether a card is stale. So CI checks what is objectively
    true and version-independent — every topic carries a plausible stamp — and
    --check stays a local tool for refreshing them.
    """
    now = datetime.now(timezone.utc)
    horizon = f"{now.year}-{now.month:02d}"
    problems, seen = [], 0
    for path in sorted(DATA.glob("*.html")):
        if path.name in EXCLUDE:
            continue
        lines = path.read_text(encoding="utf-8").splitlines(keepends=True)
        for start, _ in topic_spans(lines):
            seen += 1
            m = re.search(r'data-reviewed="(\d{4})-(\d{2})"', lines[start - 1])
            if not m:
                problems.append(f"{path.name}:{start}: topic has no data-reviewed stamp")
                continue
            year, month = int(m.group(1)), int(m.group(2))
            if not 1 <= month <= 12:
                problems.append(f"{path.name}:{start}: month {month:02d} is not a month")
            elif f"{year}-{month:02d}" > horizon:
                problems.append(f"{path.name}:{start}: stamped {m.group(0)}, which is in the future")
            elif year < 2024:
                problems.append(f"{path.name}:{start}: stamped {m.group(0)}, before this site existed")

    for p in problems:
        print(f"error: {p}", file=sys.stderr)
    if problems:
        print(f"\n{len(problems)} bad stamp(s). Run 'python tools/stamp_freshness.py' and commit.",
              file=sys.stderr)
        return 1
    print(f"{seen} topics carry a valid freshness stamp (newest allowed: {horizon}).")
    return 0


def domain_files(only=None):
    """The files to stamp — all of them, or the ones named by --only.

    `--only` exists because a whole-tree write is not the safe default it looks
    like. Stamping one new domain re-derives every other stamp on the site from
    `git blame`, and blame heuristics differ between git releases: a content
    wave that added 18 cards also moved ~250 untouched topics into later months,
    with no edit behind the move. That silently inflates the freshness signal
    `--report` exists to keep honest. Name the file you actually changed.
    """
    files = [p for p in sorted(DATA.glob("*.html")) if p.name not in EXCLUDE]
    if only is None:
        return files
    # A name may be a domain (`script`), which selects all of that domain's
    # parts, or a single file (`script.03-python.html`) when only one part
    # changed — which is the point of splitting a domain in the first place.
    picked, missing = [], []
    for name in only:
        if name.endswith(".html"):
            match = [p for p in files if p.name == name]
        else:
            match = [p for p in files
                     if p.name == f"{name}.html" or p.name.startswith(f"{name}.")]
        if not match:
            missing.append(name)
        picked.extend(match)
    if missing:
        raise SystemExit(f"error: no such domain or file: {', '.join(sorted(missing))}")
    # Deduplicate while keeping build order.
    seen = set()
    return [p for p in files if p in picked and not (p in seen or seen.add(p))]


def stamp(check_only=False, only=None, current_only=False):
    """Re-derive every stamp in `files` and write the ones that moved.

    `current_only` keeps only the moves that land in **this month** and restores
    every other re-derivation to what the file already said. That is the filter
    that makes a whole-tree write safe, and it exists because the alternative was
    doing it by hand: a pass across every domain produced 453 moves, of which 158
    landed on the current month — real content work several sessions had never
    re-stamped — and 295 shuffled between two earlier months, where the content
    had not changed and only the blame derivation had.

    A "last reviewed" date that over-claims is worse than one that under-claims,
    so a stale stamp is the conservative error and the one to keep when in doubt.
    """
    files = domain_files(only)
    this_month = datetime.now(timezone.utc).strftime("%Y-%m")
    changed, stamped, kept, held = [], 0, 0, 0
    for path in files:
        rel = f"data/{path.name}"
        ignore = mechanical_revs(rel)
        original = path.read_text(encoding="utf-8")
        times = blame_times(rel, ignore, original)
        lines = original.splitlines(keepends=True)

        out = list(lines)
        for start, end in topic_spans(lines):
            span_times = body_times(times, start, end)
            if not span_times:
                continue
            when = datetime.fromtimestamp(max(span_times), timezone.utc).strftime("%Y-%m")
            if current_only:
                was = REVIEWED_ATTR_RE.search(out[start - 1])
                had = was.group(0).split('"')[1] if was else None
                # Hold everything except a move into the month we are in now.
                if had and had != when and when != this_month:
                    when, held = had, held + 1
                elif had != when:
                    kept += 1
            line = REVIEWED_ATTR_RE.sub("", out[start - 1])
            out[start - 1] = TOPIC_OPEN_RE.sub(
                lambda m: f'<div class="topic" data-reviewed="{when}"{m.group(1)}>',
                line, count=1,
            )
            stamped += 1

        result = "".join(out)
        print(f"  {path.name:<16} {len(topic_spans(lines)):>4} topics, "
              f"{len(ignore):>2} mechanical commit(s) ignored")
        if result != original:
            changed.append(path.name)
            if not check_only:
                path.write_text(result, encoding="utf-8")

    print(f"\n{stamped} topics stamped across {len(files)} file(s).")
    if current_only:
        print(f"--current-only: kept {kept} move(s) into {this_month}, "
              f"held {held} earlier-month re-derivation(s).")
    if changed:
        print(("Would update: " if check_only else "Updated: ") + ", ".join(changed))
    return 1 if (check_only and changed) else 0


def months_since(stamp):
    y, m = int(stamp[:4]), int(stamp[5:7])
    now = datetime.now(timezone.utc)
    return (now.year - y) * 12 + (now.month - m)


def report(limit=50):
    """Oldest *claims* that have been explicitly marked volatile.

    Reports the claim, not the topic, because "this card mentions Intune" is not
    something anyone can act on, whereas "this console path was last checked in
    June" is.
    """
    rows = []
    for path in sorted(DATA.glob("*.html")):
        if path.name in EXCLUDE:
            continue
        text = path.read_text(encoding="utf-8")
        lines = text.splitlines(keepends=True)
        spans = list(topic_spans(lines))
        for m in VOLATILE_CLAIM_RE.finditer(text):
            line = text[: m.start()].count("\n") + 1
            topic = "(outside a topic)"
            for start, end in spans:
                if start <= line <= end:
                    plain = ACRO_SPAN_RE.sub("", "".join(lines[start - 1:end]))
                    got = TOPIC_NAME_RE.search(plain)
                    if got:
                        topic = unescape(re.sub(r"<[^>]+>|\s+", " ", got.group(1))).strip()
                    break
            claim = unescape(re.sub(r"<[^>]+>|\s+", " ", m.group(3))).strip()
            rows.append((months_since(m.group(2)), m.group(2), path.stem, topic, claim))

    if not rows:
        print("No claims are marked volatile yet.\n")
        print('Mark one with <span class="volatile" data-checked="YYYY-MM">…</span>')
        print("around the specific thing that goes out of date — a console path, a")
        print("price, a limit. `--candidates` suggests topics worth looking at.")
        return 0

    rows.sort(reverse=True)
    print(f"{len(rows)} marked claims. Oldest {min(limit, len(rows))}:\n")
    print(f"{'age':>4}  {'checked':<9} {'domain':<10} {'topic':<38} claim")
    for age, when, dom, topic, claim in rows[:limit]:
        print(f"{age:>3}m  {when:<9} {dom:<10} {topic[:36]:<38} {claim[:44]}")
    return 0


def candidates(limit=50):
    """Topics whose prose *might* contain a claim worth marking. A guess."""
    rows = []
    for path in sorted(DATA.glob("*.html")):
        if path.name in EXCLUDE:
            continue
        text = path.read_text(encoding="utf-8")
        lines = text.splitlines(keepends=True)
        for start, end in topic_spans(lines):
            head = "".join(lines[start - 1:end])
            m = re.search(r'data-reviewed="(\d{4})-(\d{2})"', lines[start - 1])
            if not m:
                continue
            # Strip the annotator's expansions *first*: `.topic-name` contains a
            # nested `.acro-exp` span, so a non-greedy match would otherwise stop
            # at the inner closing tag and keep the expansion text.
            plain = ACRO_SPAN_RE.sub("", head)
            name = TOPIC_NAME_RE.search(plain)
            if name:
                name = unescape(re.sub(r"<[^>]+>|\s+", " ", name.group(1))).strip()
            else:
                name = "(no .topic-name — see the content linter)"
            if not VOLATILE_HINTS.search(head):
                continue
            # Already marked up? Then it is not a candidate; it is in --report.
            if VOLATILE_CLAIM_RE.search(head):
                continue
            age = (datetime.now(timezone.utc) - datetime(int(m.group(1)), int(m.group(2)), 1,
                                                         tzinfo=timezone.utc)).days // 30
            rows.append((age, path.stem, name, f"{m.group(1)}-{m.group(2)}"))

    rows.sort(reverse=True)
    print(f"{len(rows)} topics mention something that may move, and have no marked "
          f"claim. Oldest {min(limit, len(rows))}:\n")
    print("This is a keyword guess, not a finding — it flags 1 topic in 5, and it")
    print("cannot tell a console path from prose. Read the card, wrap the specific")
    print('claim in <span class="volatile" data-checked="YYYY-MM">, and it moves to')
    print("--report where it can actually be tracked.\n")
    print(f"{'age':>4}  {'reviewed':<9} {'domain':<10} topic")
    for age, dom, name, when in rows[:limit]:
        print(f"{age:>3}m  {when:<9} {dom:<10} {name[:62]}")
    return 0


def parse_only(argv):
    """Domain names following --only, e.g. `--only m365` or `--only m365 endpoint`."""
    if "--only" not in argv:
        return None
    rest = argv[argv.index("--only") + 1:]
    names = [a for a in rest if not a.startswith("--")]
    if not names:
        raise SystemExit("error: --only needs at least one domain name, e.g. --only m365")
    return names


if __name__ == "__main__":
    if "--verify" in sys.argv:
        sys.exit(verify())
    if "--report" in sys.argv:
        sys.exit(report())
    if "--candidates" in sys.argv:
        sys.exit(candidates())
    sys.exit(stamp(check_only="--check" in sys.argv, only=parse_only(sys.argv),
                   current_only="--current-only" in sys.argv))
