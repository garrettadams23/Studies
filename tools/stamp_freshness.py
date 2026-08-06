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
    python3 tools/stamp_freshness.py            # stamp in place
    python3 tools/stamp_freshness.py --check     # report drift, write nothing
    python3 tools/stamp_freshness.py --report    # oldest volatile topics
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

# Prettier splits tags across lines — `<span class="topic-name"\n  >` and
# `</span\n>` are both valid and both appear in data/*.html. Every pattern that
# matches markup here has to tolerate that, or it silently under-reports.
TOPIC_NAME_RE = re.compile(r'<span\b[^>]*class="topic-name"[^>]*>(.*?)</span\s*>', re.S)

# Terms that mark a topic as tracking something that moves: vendor consoles,
# product names, prices, versions. Only these need periodic review — the OSI
# model does not. Used to *suggest* `data-volatile`, never to apply it.
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


def topic_spans(lines):
    """[(start_line, end_line, index_of_opening_tag)] for every .topic."""
    starts = [i for i, l in enumerate(lines, 1) if '<div class="topic"' in l]
    spans = []
    for n, start in enumerate(starts):
        end = starts[n + 1] - 1 if n + 1 < len(starts) else len(lines)
        spans.append((start, end))
    return spans


def stamp(check_only=False):
    changed, stamped = [], 0
    for path in sorted(DATA.glob("*.html")):
        if path.name in EXCLUDE:
            continue
        rel = f"data/{path.name}"
        ignore = mechanical_revs(rel)
        original = path.read_text(encoding="utf-8")
        times = blame_times(rel, ignore, original)
        lines = original.splitlines(keepends=True)

        out = list(lines)
        for start, end in topic_spans(lines):
            span_times = [times[n] for n in range(start, end + 1) if n in times]
            if not span_times:
                continue
            when = datetime.fromtimestamp(max(span_times), timezone.utc).strftime("%Y-%m")
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

    print(f"\n{stamped} topics stamped across {len(list(DATA.glob('*.html'))) - len(EXCLUDE)} files.")
    if changed:
        print(("Would update: " if check_only else "Updated: ") + ", ".join(changed))
    return 1 if (check_only and changed) else 0


def report(limit=50):
    """Oldest topics that look like they track something that moves."""
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
            volatile = 'data-volatile="true"' in lines[start - 1] or bool(VOLATILE_HINTS.search(head))
            if not volatile:
                continue
            age = (datetime.now(timezone.utc) - datetime(int(m.group(1)), int(m.group(2)), 1,
                                                         tzinfo=timezone.utc)).days // 30
            rows.append((age, path.stem, name, f"{m.group(1)}-{m.group(2)}"))

    rows.sort(reverse=True)
    print(f"{len(rows)} topics look volatile. Oldest {min(limit, len(rows))}:\n")
    print(f"{'age':>4}  {'reviewed':<9} {'domain':<10} topic")
    for age, dom, name, when in rows[:limit]:
        print(f"{age:>3}m  {when:<9} {dom:<10} {name[:62]}")
    return 0


if __name__ == "__main__":
    if "--report" in sys.argv:
        sys.exit(report())
    sys.exit(stamp(check_only="--check" in sys.argv))
