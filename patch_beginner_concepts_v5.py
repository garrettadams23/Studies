#!/usr/bin/env python3
"""Fifth wave — rounds out the coding track (conditionals, truthiness, variable
conventions, dates/times, a gentle async intro, and an annotated capstone) plus
a general troubleshooting-methodology topic. Idempotent (own sentinels).

DRY-RUN by default; pass --write to apply (creates a .bak backup of index.html).
Run from the project root, or point at a folder with --dir PATH.
"""
import sys, os, shutil

def card(label, title, desc, code=""):
    cb = f'<pre class="code-block">{code}</pre>' if code else ""
    return (f'<div class="concept-card"><div class="concept-label">{label}</div>'
            f'<div class="concept-title">{title}</div>'
            f'<div class="concept-desc">{desc}</div>{cb}</div>')

def tbl(headers, rows):
    th = "".join(f"<th>{h}</th>" for h in headers)
    body = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows)
    return (f'<table class="ai-table"><thead><tr>{th}</tr></thead>'
            f'<tbody>{body}</tbody></table>')

def topic(icon, name, badge, *blocks):
    return (f'<div class="topic"><div class="topic-header">'
            f'<span class="topic-icon">{icon}</span>'
            f'<span class="topic-name">{name}</span>'
            f'<span class="topic-badge">{badge}</span>'
            f'<span class="topic-chevron">&rsaquo;</span></div>'
            f'<div class="topic-body">{"".join(blocks)}</div></div>')

# =========================================================================
# SCRIPT — wave 5 (round out the track)
# =========================================================================
SCRIPT5 = [
  topic("🌳", "Conditionals Deep-Dive", "Beginner • Core",
    card("CHAINS", "else-if Ladders &amp; switch",
         "When there are more than two paths, chain else-if — or use switch/case when "
         "you’re checking one value against many options. switch can be cleaner, but "
         "remember to break each case so it doesn’t fall through.",
         "<span class='com'>// JavaScript</span>\n"
         "<span class='kw'>switch</span> (day) {\n"
         "  <span class='kw'>case</span> <span class='str'>\"Sat\"</span>:\n"
         "  <span class='kw'>case</span> <span class='str'>\"Sun\"</span>: <span class='fn'>console</span>.log(<span class='str'>\"weekend\"</span>); <span class='kw'>break</span>;\n"
         "  <span class='kw'>default</span>:  <span class='fn'>console</span>.log(<span class='str'>\"weekday\"</span>);\n"
         "}"),
    card("ONE-LINER", "The Ternary",
         "For a quick either/or, the ternary picks one of two values in a single line: "
         "condition ? thisIfTrue : thisIfFalse. Great for tiny choices; don’t nest "
         "them or they turn to soup.",
         "<span class='com'>// JavaScript</span>\n"
         "<span class='kw'>let</span> label = age &gt;= <span class='num'>18</span> ? <span class='str'>\"adult\"</span> : <span class='str'>\"minor\"</span>;"),
    card("FLATTEN", "Guard Clauses Beat Deep Nesting",
         "Instead of wrapping everything in nested ifs, check the bad cases first and "
         "bail out early. The happy path then reads straight down the page with less "
         "indentation — easier to follow.",
         "<span class='com'>// JavaScript</span>\n"
         "<span class='kw'>function</span> <span class='fn'>pay</span>(user) {\n"
         "  <span class='kw'>if</span> (!user) <span class='kw'>return</span>;      <span class='com'>// bail early</span>\n"
         "  <span class='com'>// main logic, no deep nesting</span>\n"
         "}")
  ),
  topic("⚖️", "Truthiness &amp; Common Pitfalls", "Beginner • Gotchas",
    card("YES/NO-ISH", "What Counts as True or False",
         "In an if, values that aren’t strictly true/false still get judged ‘truthy’ or "
         "‘falsy.’ Knowing the falsy list prevents head-scratchers like ‘why didn’t my "
         "if run when the number was 0?’"),
    card("EQUALITY", "== vs. === (and null vs. undefined)",
         "Some languages have loose equality (==) that converts types before comparing "
         "— so 0 == \"\" can be true. Prefer strict (===) to avoid surprises. ‘null’ "
         "is an intentional empty; ‘undefined’ means never set — subtly different."),
    card("CLASSIC BUGS", "Off-by-One &amp; Mutating While Looping",
         "Two beginner classics: counting from 1 when arrays start at 0 (off-by-one), "
         "and adding/removing items from a list while you’re looping over it (which "
         "skips or repeats items). When a loop acts haunted, suspect these first."),
    tbl(["Falsy in JavaScript", "Everything Else Is Truthy"],
        [["false", "true"],
         ["0", "any non-zero number"],
         ["\"\" (empty string)", "any non-empty string"],
         ["null / undefined", "any object or array (even empty [])"],
         ["NaN", "\"0\" and \"false\" (they’re non-empty text!)"]])
  ),
  topic("📦", "Variables: const, let &amp; Naming", "Beginner • Craft",
    card("DEFAULT", "Reach for const First",
         "Declare values that won’t change as constants (const); use let only when you "
         "truly reassign. ‘const by default’ means fewer things can change behind your "
         "back, which means fewer bugs. Avoid the old, leaky ‘var.’"),
    card("READABILITY", "Naming Conventions",
         "Teams pick a style and stick to it so code looks consistent. The big three: "
         "camelCase (totalPrice), snake_case (total_price), and UPPER_SNAKE for "
         "constants (MAX_USERS). Match whatever the file around you already uses."),
    tbl(["Style", "Looks Like", "Common In"],
        [["camelCase", "userName", "JavaScript, Java"],
         ["snake_case", "user_name", "Python, Ruby, SQL"],
         ["PascalCase", "UserAccount", "Class/type names"],
         ["UPPER_SNAKE", "MAX_RETRIES", "Constants everywhere"],
         ["kebab-case", "user-name", "CSS, file names, URLs"]])
  ),
  topic("🗓️", "Dates, Times &amp; Time Zones", "Beginner • Real-World",
    card("UNDER THE HOOD", "Time Is a Big Number",
         "Computers often store a moment as the number of seconds (or milliseconds) "
         "since Jan 1, 1970 — the ‘Unix epoch.’ It looks meaningless (1700000000) but "
         "it’s easy to compare and do math on, then format for humans at the end."),
    card("THE HEADACHE", "Always Store UTC",
         "Time zones and daylight saving cause endless bugs. The pro habit: store and "
         "calculate in UTC (one global clock), and convert to the user’s local time "
         "only when displaying. Never assume everyone is in your zone."),
    card("FORMAT", "ISO 8601 — the Sane Format",
         "Write dates as YYYY-MM-DD (2026-06-01) and timestamps as "
         "2026-06-01T13:45:00Z. It sorts correctly as text, removes the "
         "is-it-month-or-day confusion, and every language understands it.")
  ),
  topic("🧵", "A First Look at Async", "Beginner • Web",
    card("ANALOGY", "Don’t Stand at the Counter",
         "Some tasks take time — fetching data, reading a big file. ‘Synchronous’ code "
         "waits in line, frozen, until it’s done. ‘Asynchronous’ code is like ordering "
         "food, taking a buzzer, and sitting down — you get on with other things and "
         "react when it’s ready."),
    card("WHY IT MATTERS", "Keeps Apps Responsive",
         "If a web page waited synchronously for every download, it would freeze on "
         "every click. Async lets the page stay alive while data loads in the "
         "background — essential for anything that talks to the network."),
    card("MODERN SHAPE", "async / await",
         "Today’s clean way: mark a function ‘async,’ then ‘await’ the slow step as if "
         "it were normal top-to-bottom code. It reads simply but doesn’t block the rest "
         "of the program.",
         "<span class='com'>// JavaScript</span>\n"
         "<span class='kw'>async function</span> <span class='fn'>load</span>() {\n"
         "  <span class='kw'>const</span> res  = <span class='kw'>await</span> <span class='fn'>fetch</span>(<span class='str'>\"/data.json\"</span>);\n"
         "  <span class='kw'>const</span> data = <span class='kw'>await</span> res.json();\n"
         "  <span class='fn'>console</span>.log(data);\n"
         "}")
  ),
  topic("🏁", "Capstone — Read a Whole Tiny Program", "Beginner • Putting It Together",
    card("THE GOAL", "Everything You’ve Learned, in 7 Lines",
         "Here’s a complete little program that counts the long words in a sentence. "
         "It uses a variable, a list, a loop, a condition, an accumulator, and output "
         "— the core toolkit. Read it top to bottom; you now know every piece.",
         "<span class='com'># Python — count words longer than 4 letters</span>\n"
         "text  = <span class='str'>\"the quick brown fox jumps\"</span>  <span class='com'># a string</span>\n"
         "words = text.<span class='fn'>split</span>()      <span class='com'># -&gt; list of words</span>\n"
         "count = <span class='num'>0</span>                  <span class='com'># accumulator starts empty</span>\n"
         "<span class='kw'>for</span> w <span class='kw'>in</span> words:           <span class='com'># visit each word</span>\n"
         "    <span class='kw'>if</span> <span class='fn'>len</span>(w) &gt; <span class='num'>4</span>:        <span class='com'># the decision</span>\n"
         "        count = count + <span class='num'>1</span>   <span class='com'># update the total</span>\n"
         "<span class='fn'>print</span>(<span class='str'>f\"{count} long words\"</span>)  <span class='com'># show the result → 2</span>"),
    card("NOW YOU", "Change It &amp; See",
         "The fastest way to cement this: change one thing and predict the result "
         "before you run it. Make the limit 3 instead of 4. Count short words instead. "
         "Print each long word. Tiny experiments turn reading into understanding."),
    card("WHERE NEXT", "Keep the Momentum",
         "You’ve got variables, types, conditionals, loops, functions, data "
         "structures, errors, files, and the workflow. Next: pick one small real "
         "project, build it badly, then improve it. That loop — build, struggle, "
         "learn, repeat — is the whole career in miniature.")
  ),
]

# =========================================================================
# OPS — troubleshooting methodology
# =========================================================================
OPS3 = [
  topic("🔧", "Troubleshooting Like a Pro", "A+ • Start Here",
    card("MINDSET", "Calm, Curious, Methodical",
         "Good troubleshooting isn’t magic or luck — it’s a repeatable method. Panic "
         "and random clicking make things worse; a calm, one-step-at-a-time approach "
         "fixes problems and teaches you something each time."),
    card("THE METHOD", "CompTIA’s 7 Steps",
         "The industry-standard loop: identify the problem, form a theory of the "
         "cause, test that theory, make a plan, fix it, verify it’s really solved "
         "(and prevention), then document what happened. Skipping ‘document’ is how "
         "the same fire gets fought twice."),
    card("FIRST QUESTIONS", "Narrow It Down Fast",
         "Start by shrinking the search: What changed recently? Does it affect one "
         "person or everyone? Can you reproduce it? ‘It worked yesterday’ plus ‘what "
         "changed’ solves a surprising share of problems."),
    card("CLASSIC WISDOM", "Check the Simple Stuff First",
         "Is it plugged in? Is it on the right network? Did you restart it? Seasoned "
         "techs aren’t being condescending — the boring, simple cause really is the "
         "answer most of the time. Rule it out before chasing the exotic."),
    tbl(["Step", "In Plain English"],
        [["1. Identify", "Gather symptoms; what exactly is wrong?"],
         ["2. Theory", "Best guess at the cause (simple first)"],
         ["3. Test theory", "Prove or disprove the guess"],
         ["4. Plan", "Decide the fix and any risk"],
         ["5. Implement", "Apply the fix (one change at a time)"],
         ["6. Verify", "Confirm it’s solved + prevent recurrence"],
         ["7. Document", "Write it down for next time"]])
  ),
]

DOMAINS = [
  dict(name="Script", sentinel="<!-- BEGINNER5-SCRIPT v1 -->", topics=SCRIPT5,
       anchors=["<!-- /domain-body script -->"]),
  dict(name="Ops",    sentinel="<!-- BEGINNER5-OPS v1 -->",    topics=OPS3,
       anchors=["<!-- /domain-body ops -->"]),
]

def patch_html(text):
    report = []
    for d in DOMAINS:
        if d["sentinel"] in text:
            report.append((d["name"], "skip (already injected)")); continue
        hit = next((a for a in d["anchors"] if a in text), None)
        if not hit:
            report.append((d["name"], "ERROR: no anchor")); continue
        block = d["sentinel"] + "\n" + "\n".join(d["topics"]) + "\n"
        text = text.replace(hit, block + hit, 1)
        report.append((d["name"], f"injected before {hit}"))
    return text, report

def main():
    write = "--write" in sys.argv
    base = sys.argv[sys.argv.index("--dir") + 1] if "--dir" in sys.argv else "."
    ipath = os.path.join(base, "index.html")
    print("BEGINNER-CONCEPTS-V5 patch —", "WRITE" if write else "DRY-RUN (add --write to apply)")
    if not os.path.exists(ipath):
        print(f"  index.html MISSING ({ipath})"); return
    src = open(ipath, encoding="utf-8").read()
    out, report = patch_html(src)
    for name, status in report:
        print(f"  {name:10} {status}")
    if write and out != src:
        shutil.copy(ipath, ipath + ".bak")
        open(ipath, "w", encoding="utf-8").write(out)
    print(f"  index.html total {len(out) - len(src):+d} chars")
    if not write:
        print("\nLooks right? Apply with:  python3 patch_beginner_concepts_v5.py --write")

if __name__ == "__main__":
    main()
