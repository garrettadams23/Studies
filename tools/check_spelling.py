#!/usr/bin/env python3
"""
check_spelling.py — the site says it is written in American English. Is it?

`CONTRIBUTING.md` states the convention without qualification: *"The site is
written in **American English**."* It names `data/renames.json` as the mechanism
and `check_renames.py` as the gate, and that pairing is where the claim quietly
stopped being true. The registry is a list of **vendor renames** — an old name,
a new name, and the month the vendor changed it — and a spelling is none of
those things. The `centre` row carries `"since": "2026-09"`, which is the month
somebody decided, not a month anything was renamed.

So the convention was enforced for the two words that prompted it and for no
others. Measured across the site's prose the day this file was written:

    behaviour  246      organise  252      licence  115      programme  138
    colour      65      optimise   73      defence   62      artefact    88
    favour      33      authorise  78      judgement 58      catalogue   54

**Roughly two thousand occurrences**, in a site whose own acronym dictionary is
unanimously American — and the sharpest evidence is inside a single entry of it.
`CAL` expands to **Client Access License** and the note one line below reads
*"Per-user or per-device **licence** to connect to a Windows Server"*. The same
object, two fields apart, spells the same word both ways. That is the `centre`
finding again — *the prose had been disagreeing with the reference it ships* —
except this time both halves are in the same file.

## Rules, and one dictionary that says it is one

The distinction is the whole design, and it is the one `script.js` already makes
about plurals: *a real stemmer needs a tokenised index, and the irregulars are a
dictionary, not a rule.*

  * **`-ise` → `-ize`**, with `-isation`, `-ised`, `-ising`, `-iser`. A rule. It
    over-matches the words where `ise` is not a suffix — *compromise*,
    *enterprise*, *otherwise* — so those are excluded by name in `ISE_KEEP`,
    which is a closed list of about thirty words that English is not going to
    extend.
  * **`-yse` → `-yze`**. The same rule, one vowel over, and `analyses` is
    excluded because it is *also* the plural of **analysis**, identical in both
    dialects, and nothing in the string says which one it is. Excluding it is a
    miss; converting it would be a wrong guess, and this file takes the miss for
    the same reason `plurals()` does.
  * **`-our` → `-or`**. A rule with a three-character stem floor, which is what
    keeps `four`, `hour`, `tour`, `pour`, `sour`, `your`, `our` and `flour` out
    without naming any of them. `detour` and `glamour` are named, the first
    because it is not a dialect pair and the second because American English
    keeps it.
  * **The irregulars** — `licence`, `defence`, `programme`, `judgement`,
    `artefact`, `catalogue`, `grey`, `practise`, the doubled-`l` inflections and
    the rest. **A dictionary, and it says so.** There is a rule underneath the
    doubled `l` (it turns on which syllable is stressed) and this file is not
    going to implement stress: `cancelled` is two `l`s and `installed` is two
    `l`s and no regex separates them.

## What it reads

Prose only, the same definition `check_renames.py` uses — no `<pre>`, no
`<code>`, no tag interiors, no generated `.acro-exp` spans — plus the string
fields of the data files that render as prose. It deliberately does **not** read
`related.json`, or `paths.json`'s `steps`: those are slugs derived from titles,
and a slug changes when its title does, through `fix_topic_names.py
--aliases-only`, never by find-and-replace.

Exit status is 1 on any finding, so CI can gate on it.

Usage:
  python3 tools/check_spelling.py              # every finding, by file
  python3 tools/check_spelling.py --census     # by word, commonest first
  python3 tools/check_spelling.py --fix        # apply, prose only
  python3 tools/check_spelling.py --self-test  # the rules, on fixtures
  python3 tools/check_spelling.py --list       # the rules and their exceptions
"""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
sys.path.insert(0, str(ROOT / "tools"))
from lint_content import TAG_RE  # noqa: E402

PRE_RE = re.compile(r"<(pre|code)\b.*?</\1>", re.S | re.I)
ACRO_EXP_RE = re.compile(r'<span class="acro-exp">\([^<]*?\)</span\s*>')

# ── the rules ───────────────────────────────────────────────────────────────
# A three-character stem floor on each, which is load-bearing rather than
# cautious: it is what excludes `our`, `four`, `hour`, `tour`, `pour`, `sour`,
# `your`, `flour`, `raise`, `noise` and `wise` without naming one of them.
ISE_RE = re.compile(r"(?<![A-Za-z])([A-Za-z]{3,}?)is(e|es|ed|ing|er|ers|ation|ations)(?![A-Za-z])", re.I)
YSE_RE = re.compile(r"(?<![A-Za-z])([A-Za-z]{3,}?)ys(e|ed|ing|er|ers)(?![A-Za-z])", re.I)
OUR_RE = re.compile(r"(?<![A-Za-z])([A-Za-z]{3,}?)our"
                    r"(s|ed|ing|al|ally|ite|ites|able|ably|less|ful|fully|ist|ists)?"
                    r"(?![A-Za-z])", re.I)

# Words where `ise` is not the suffix: one word, not one word spelled twice.
# Closed, and English is not going to extend it. `malvertise` is a coinage from
# *advertising* and is spelled that way in both dialects; `denoise` is *de* +
# *noise*; `mauvaise` is French and appears in `philosophy`.
ISE_KEEP = {
    "advertise", "advise", "appraise", "braise", "chaise", "clockwise", "compromise",
    "comprise", "concise", "cruise", "denoise", "disguise", "enterprise", "excise",
    "exercise", "expertise", "franchise", "imprecise", "improvise", "likewise",
    "malvertise", "mauvaise", "merchandise", "otherwise", "pairwise", "paradise",
    "praise", "precise", "premise", "promise", "raise", "reprise", "revise",
    "stepwise", "supervise", "surprise", "televise", "treatise", "unexercise",
    "unwise", "unsupervise",
}
# `analyses` is the plural of *analysis* as often as it is a verb, and the two
# are identical in both dialects. A miss, taken on purpose.
YSE_KEEP = {"analyses"}
# `detour` is not a dialect pair. American English keeps `glamour`.
OUR_KEEP = {"detour", "devour", "contour", "velour", "glamour", "troubadour"}

# ── the dictionary that says it is one ──────────────────────────────────────
# Each entry is British -> American. Inflections are written out rather than
# derived, because the doubled `l` is a stress rule and `cancelled` sits beside
# `installed` with nothing in the string to tell them apart.
IRREGULAR = {
    "licence": "license", "licences": "licenses", "licenced": "licensed",
    "defence": "defense", "defences": "defenses",
    "offence": "offense", "offences": "offenses",
    "pretence": "pretense",
    "practise": "practice", "practises": "practices", "practised": "practiced",
    "practising": "practicing",
    "judgement": "judgment", "judgements": "judgments",
    "artefact": "artifact", "artefacts": "artifacts",
    "catalogue": "catalog", "catalogues": "catalogs", "catalogued": "cataloged",
    "cataloguing": "cataloging",
    "programme": "program", "programmes": "programs",
    "grey": "gray", "greys": "grays", "greyed": "grayed", "greying": "graying",
    "ageing": "aging",
    "metre": "meter", "metres": "meters",
    "litre": "liter", "litres": "liters",
    "fibre": "fiber", "fibres": "fibers",
    "centre": "center", "centres": "centers", "centred": "centered",
    "centring": "centering", "datacentre": "datacenter", "datacentres": "datacenters",
    "theatre": "theater", "theatres": "theaters",
    "sceptic": "skeptic", "sceptics": "skeptics", "sceptical": "skeptical",
    "manoeuvre": "maneuver", "manoeuvres": "maneuvers",
    "mould": "mold", "moulds": "molds",
    "storey": "story", "storeys": "stories",
    "tyre": "tire", "tyres": "tires",
    "enquiry": "inquiry", "enquiries": "inquiries",
    "cancelled": "canceled", "cancelling": "canceling",
    "labelled": "labeled", "labelling": "labeling",
    "modelled": "modeled", "modelling": "modeling",
    "travelled": "traveled", "travelling": "traveling",
    "levelled": "leveled", "levelling": "leveling",
    "signalled": "signaled", "signalling": "signaling",
    "totalled": "totaled", "totalling": "totaling",
    "fuelled": "fueled", "fuelling": "fueling",
    "marvellous": "marvelous", "skilful": "skillful",
    "fulfil": "fulfill", "fulfils": "fulfills",
    "fulfilment": "fulfillment", "fulfilments": "fulfillments",
    "enrolment": "enrollment", "enrolments": "enrollments",
    "instalment": "installment", "instalments": "installments",
    "distil": "distill", "instil": "instill", "appal": "appall",
}
IRREGULAR_RE = re.compile(r"(?<![A-Za-z])(" + "|".join(sorted(IRREGULAR, key=len, reverse=True))
                          + r")(?![A-Za-z])", re.I)

# JSON files whose string values render as prose, and the keys to read in each.
# `related.json` and `paths.json`'s `steps` are slugs, not prose: a slug moves
# when its title does, through fix_topic_names.py, never by replacement.
JSON_PROSE = {
    "acronyms.json": None,               # every string but the keys
    "domain-intros.json": None,
    "paths.json": {"name", "blurb", "for"},
}


def match_case(src, dst):
    """`Behaviour` -> `Behavior`, `BEHAVIOUR` -> `BEHAVIOR`, `behaviour` -> `behavior`."""
    if src.isupper() and len(src) > 1:
        return dst.upper()
    if src[:1].isupper():
        return dst[:1].upper() + dst[1:]
    return dst


def _ise(m):
    word = m.group(0)
    if word.lower() in ISE_KEEP or (m.group(1) + "ise").lower() in ISE_KEEP:
        return None
    return match_case(word, m.group(1).lower() + "iz" + m.group(2).lower())


def _yse(m):
    word = m.group(0)
    if word.lower() in YSE_KEEP:
        return None
    return match_case(word, m.group(1).lower() + "yz" + m.group(2).lower())


def _our(m):
    word = m.group(0)
    if (m.group(1) + "our").lower() in OUR_KEEP:
        return None
    return match_case(word, m.group(1).lower() + "or" + (m.group(2) or "").lower())


def _irregular(m):
    return match_case(m.group(0), IRREGULAR[m.group(0).lower()])


# The dictionary runs **first**, because it is the exception to the rules and
# not a fourth one beside them. `practise` belongs to both: the `-ise` rule sees
# `pract` + `is` + `e` and offers **practize**, and with the dictionary second
# it never gets the chance to say `practice`. It shipped that way until the
# census printed both rows for the same word, one above the other.
#
# The self-test did not catch it because it tested each mechanism on its own
# words. There is one derived fixture now instead of a hand-picked list: every
# entry of the dictionary, through the whole pipeline. That is the only shape
# of fixture that could have failed here, because the defect was in the
# ordering rather than in either half.
RULES = [("irregular", IRREGULAR_RE, _irregular),
         ("-ise", ISE_RE, _ise), ("-yse", YSE_RE, _yse), ("-our", OUR_RE, _our)]


# Phrases where the British string is literally correct, in the same spirit as
# `renames.json`'s `allow`. **Fibre Channel** is a standard's name — ANSI T11
# spells it that way and so does every American vendor selling it — and unlike
# `ThinkCentre` the word boundary does not save it, because there is a space
# where ThinkCentre has nothing. It is the one phrase on the whole site that
# needs this, which is worth knowing: the other 2,200 hits are prose.
ALLOW = ["Fibre Channel"]
ALLOW_RE = re.compile("|".join(re.escape(a) for a in ALLOW), re.I)
HOLD_RE = re.compile("\x00(\d+)\x00")


def apply_rules(text):
    """(rewritten, [(rule, found, replacement, offset)]).

    One code path, deliberately: the report and the fix were two functions and
    they disagreed on the first thing anybody asked them — a word split across
    a tag. A census that describes a different edit from the one the `--fix`
    makes is worse than either bug alone, because it is the half a person reads
    and believes.
    """
    held = []

    def hold(m):
        held.append(m.group(0))
        return f"\x00{len(held) - 1}\x00"

    text = ALLOW_RE.sub(hold, text)
    found = []
    for name, rx, fn in RULES:
        def swap(m, name=name, fn=fn):
            new = fn(m)
            if not new or new == m.group(0):
                return m.group(0)
            found.append((name, m.group(0), new, m.start()))
            return new
        text = rx.sub(swap, text)
    text = HOLD_RE.sub(lambda m: held[int(m.group(1))], text)
    return text, sorted(found, key=lambda f: f[3])


def findings(text):
    return apply_rules(text)[1]


def rewrite(text):
    return apply_rules(text)[0]


# ── reading prose out of an HTML file, and writing it back ──────────────────
# `check_renames.py` masks non-prose by substituting spaces, which is right for
# a report and useless for a fix: the offsets it yields do not map back. This
# splits instead, so the untouchable spans survive byte for byte and only the
# text between them is rewritten.
SPLIT_RE = re.compile(r"(<(?:pre|code)\b.*?</(?:pre|code)>"
                      r"|<span class=\"acro-exp\">\([^<]*?\)</span\s*>"
                      r"|<[^>]*>)", re.S | re.I)


def html_parts(text):
    """[(is_prose, chunk)] — concatenating the chunks returns the input."""
    return [(i % 2 == 0, part) for i, part in enumerate(SPLIT_RE.split(text))]


def prose_of(text):
    """The prose chunks, newline-joined — never concatenated.

    Concatenating them was the first version and it invented words: `<b>machine
    </b>otherwise` read as **machineotherwise**, which is not in `ISE_KEEP`, so
    the rule offered *machineotherwize*. Thirty-odd findings were that shape,
    including `corefour` and `linkyour` — the two `-our` words the stem floor is
    specifically there to keep out.

    **An element boundary is a word boundary**, which this repository already
    knows: `script.js` indexed `…modal editingvim starts…` for the same reason
    and could not find the topic named Vim. It arrives here as a different
    symptom of the same missing separator.

    It mattered only to the report — `fix()` always rewrote each chunk on its
    own — and a report that disagrees with the fix beside it is the worse of the
    two bugs, because it is the one a person reads."""
    return "\n".join(c for keep, c in html_parts(text) if keep)


def walk_json(node, keys, path=()):
    """Yield (path, string) for every prose string in a parsed JSON document."""
    if isinstance(node, dict):
        for k, v in node.items():
            if isinstance(v, str):
                if keys is None or k in keys:
                    yield path + (k,), v
            else:
                yield from walk_json(v, keys, path + (k,))
    elif isinstance(node, list):
        for i, v in enumerate(node):
            if isinstance(v, str):
                if keys is None:
                    yield path + (i,), v
            else:
                yield from walk_json(v, keys, path + (i,))


def json_indent(text, default=2):
    """The file's own indent, so a one-word fix is a one-line diff.

    Hardcoding 2 reformatted `domain-intros.json` — **604 changed lines for ten
    replacements** — which is not a cosmetic problem: a diff nobody can read is
    a diff nobody reviews, and this tool's whole claim is that its 2,192 edits
    were looked at.
    """
    for line in text.split("\n")[1:]:
        if line.strip():
            return len(line) - len(line.lstrip(" ")) or default
    return default


def set_json(node, path, value):
    for step in path[:-1]:
        node = node[step]
    node[path[-1]] = value


def sources():
    """[(label, kind, path)] — every file the convention covers."""
    out = [(p.name, "html", p) for p in sorted(DATA.glob("*.html"))]
    out += [(name, "json", DATA / name) for name in sorted(JSON_PROSE)]
    return out


def scan():
    """[(label, found, replacement, rule, context)] across every source."""
    hits = []
    for label, kind, path in sources():
        text = path.read_text(encoding="utf-8")
        if kind == "html":
            blobs = [c for keep, c in html_parts(text) if keep]
        else:
            blobs = [s for _, s in walk_json(json.loads(text), JSON_PROSE[label])]
        for blob in blobs:
            for rule, found, new, at in findings(blob):
                hits.append((label, found, new, rule, blob[max(0, at - 38):at + 38]))
    return hits


def fix():
    """Apply, prose only. -> [(label, replacements)]"""
    changed = []
    for label, kind, path in sources():
        text = path.read_text(encoding="utf-8")
        if kind == "html":
            parts = html_parts(text)
            out = "".join(rewrite(c) if keep else c for keep, c in parts)
        else:
            doc = json.loads(text)
            for jpath, s in list(walk_json(doc, JSON_PROSE[label])):
                new = rewrite(s)
                if new != s:
                    set_json(doc, jpath, new)
            out = json.dumps(doc, indent=json_indent(text), ensure_ascii=False) + "\n"
            if json.loads(out) == json.loads(text):
                out = text
        if out != text:
            n = sum(1 for _ in findings(prose_of(text) if kind == "html"
                                        else "\n".join(s for _, s in walk_json(
                                            json.loads(text), JSON_PROSE[label]))))
            path.write_text(out, encoding="utf-8")
            changed.append((label, n))
    return changed


def self_test():
    """The decisions, on fixtures. The exclusions are the half worth testing."""
    F = [
        # the -ise rule, and the words it must not touch
        ("organisation", "organization"), ("prioritise", "prioritize"),
        ("Authorised", "Authorized"), ("SANITISE", "SANITIZE"),
        ("memoisation", "memoization"), ("categorised", "categorized"),
        ("compromise", None), ("enterprise", None), ("otherwise", None),
        ("surprised", None), ("exercises", None), ("advertising", None),
        ("malvertising", None), ("denoise", None), ("expertise", None),
        ("unsupervised", None), ("wise", None), ("raise", None), ("noise", None),
        # -yse, and the plural that is not a verb
        ("analyse", "analyze"), ("analyser", "analyzer"), ("analyses", None),
        ("analysis", None), ("analyst", None),
        # -our, and the short words the stem floor keeps out without naming them
        ("behaviour", "behavior"), ("Behavioural", "Behavioral"),
        ("colourful", "colorful"), ("favourite", "favorite"),
        ("neighbouring", "neighboring"), ("rigour", "rigor"),
        ("four", None), ("hour", None), ("tour", None), ("pour", None),
        ("your", None), ("flour", None), ("our", None), ("sour", None),
        ("detour", None), ("glamour", None),
        # the dictionary, and the American forms that must survive a second pass
        ("Defence", "Defense"), ("Practising", "Practicing"),
        ("licensed", None), ("license", None), ("program", None), ("practice", None),
        ("installed", None), ("controlled", None), ("enrolled", None),
        ("greyhound", None), ("ThinkCentre", None), ("center", None), ("analyze", None),
        # the allow phrase, and the same word without it
        ("Fibre Channel", None), ("fibre channel zoning", None),
        ("fibre", "fiber"), ("Wi-Fi and Fibre Are", "Wi-Fi and Fiber Are"),
    ]
    # Every dictionary entry through the whole pipeline, derived rather than
    # picked. The hand-picked version had eleven of the sixty and none of the
    # one that overlapped a rule.
    F += list(IRREGULAR.items())
    bad = 0
    for src, want in F:
        got = rewrite(src)
        expect = want if want is not None else src
        if got != expect:
            bad += 1
            print(f"FAIL : {src!r} -> {got!r}, expected {expect!r}")

    # A fix must never disturb a tag, a code block or a generated expansion.
    SAMPLE = ('<div class="topic" data-x="behaviour">behaviour '
              '<code>--colour behaviour</code> '
              '<span class="acro-exp">(Behaviour Analytics)</span> colour</div>')
    out = rewrite_html(SAMPLE)
    for must in ('data-x="behaviour"', "<code>--colour behaviour</code>",
                 '<span class="acro-exp">(Behaviour Analytics)</span>'):
        if must not in out:
            bad += 1
            print(f"FAIL : the fix disturbed {must!r}")
    if ">behavior " not in out or " color<" not in out:
        bad += 1
        print(f"FAIL : the fix missed the prose in {out!r}")

    # An element boundary is a word boundary, and the report has to agree with
    # the fix about that or it reports words neither file contains.
    SPLIT = "<b>machine</b>otherwise <i>core</i>four <a>link</a>your"
    if findings(prose_of(SPLIT)) or rewrite_html(SPLIT) != SPLIT:
        bad += 1
        print(f"FAIL : a word split by a tag was read as one word — {rewrite_html(SPLIT)!r}")

    print(f"check_spelling self-test: {len(F) + 5} fixtures, {bad} failure(s).")
    return 1 if bad else 0


def rewrite_html(text):
    return "".join(rewrite(c) if keep else c for keep, c in html_parts(text))


def main():
    args = sys.argv[1:]
    if "--self-test" in args:
        return self_test()
    if "--list" in args:
        print(f"-ise      rule, {len(ISE_KEEP)} exception(s): {', '.join(sorted(ISE_KEEP))}")
        print(f"-yse      rule, {len(YSE_KEEP)} exception(s): {', '.join(sorted(YSE_KEEP))}")
        print(f"-our      rule, {len(OUR_KEEP)} exception(s): {', '.join(sorted(OUR_KEEP))}")
        print(f"irregular dictionary, {len(IRREGULAR)} entr(ies)")
        return 0
    if "--fix" in args:
        changed = fix()
        for label, n in changed:
            print(f"  {label:<26} {n:>5} replacement(s)")
        print(f"\n{sum(n for _, n in changed):,} replacement(s) across {len(changed)} file(s).")
        return 0

    hits = scan()
    if "--census" in args:
        import collections
        by_word = collections.Counter((f.lower(), n.lower(), r) for _, f, n, r, _ in hits)
        for (found, new, rule), n in by_word.most_common():
            print(f"  {n:>5}  {found:<18} -> {new:<18} {rule}")
        print(f"\n{len(by_word)} distinct word(s), {len(hits):,} occurrence(s).")
        return 1 if hits else 0

    for label, found, new, rule, ctx in hits[:400]:
        print(f"{label}: {found} -> {new}  [{rule}]\n    …{' '.join(ctx.split())}…")
    if len(hits) > 400:
        print(f"\n… and {len(hits) - 400:,} more. Run --census for the distinct words.")
    if hits:
        print(f"\n::error::{len(hits):,} British spelling(s). "
              f"CONTRIBUTING.md: the site is written in American English.")
        return 1
    print(f"0 British spelling(s) across {len(sources())} file(s) — "
          f"3 rules and {len(IRREGULAR)} dictionary entries.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
