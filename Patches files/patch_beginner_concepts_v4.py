#!/usr/bin/env python3
"""Fourth wave — hands-on coding essentials for brand-new beginners, plus a few
more practical-life concepts. Idempotent (own sentinels).

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
# SCRIPT — wave 4 (hands-on essentials)
# =========================================================================
SCRIPT4 = [
  topic("🔢", "Numbers, Math &amp; Rounding Gotchas", "Beginner • Core",
    card("TWO KINDS", "Integers vs. Decimals",
         "Whole numbers (integers) and decimals (floats) behave differently. In some "
         "languages 7 / 2 with two integers throws away the decimal and gives 3, not "
         "3.5 — a surprise that bites beginners. When precision matters, make sure "
         "you’re using floats."),
    card("FAMOUS BUG", "Why 0.1 + 0.2 ≠ 0.3",
         "Computers store decimals in binary, which can’t represent some fractions "
         "exactly — just like 1/3 is messy in decimal. So tiny rounding errors appear. "
         "It’s not a bug in your code; it’s how floating point works everywhere.",
         "<span class='com'>// JavaScript</span>\n"
         "<span class='num'>0.1</span> + <span class='num'>0.2</span>   <span class='com'>// 0.30000000000000004</span>\n"
         "<span class='com'>// round when displaying money, etc.</span>\n"
         "(<span class='num'>0.1</span> + <span class='num'>0.2</span>).toFixed(<span class='num'>2</span>)  <span class='com'>// \"0.30\"</span>"),
    card("CONVERT", "Turning Text into Numbers",
         "Input often arrives as text (“42”), and \"42\" + 1 may glue into \"421\" "
         "instead of adding. Convert first. Reach for the modulo trick (n % 2) to test "
         "even/odd, and rounding functions to tidy decimals.",
         "<span class='com'>// JavaScript</span>\n"
         "<span class='fn'>Number</span>(<span class='str'>\"42\"</span>) + <span class='num'>1</span>   <span class='com'>// 43</span>\n"
         "<span class='fn'>Math</span>.round(<span class='num'>3.7</span>)     <span class='com'>// 4</span>")
  ),
  topic("📋", "Looping Over Data — Iteration Patterns", "Beginner • Core",
    card("FOR-EACH", "Do Something to Every Item",
         "The most common loop visits each item in a list in turn. You rarely need the "
         "index — you just want ‘for each thing, do this.’ Cleaner and harder to get "
         "wrong than counting positions by hand.",
         "<span class='com'>// JavaScript</span>\n"
         "<span class='kw'>const</span> names = [<span class='str'>\"Sam\"</span>, <span class='str'>\"Ada\"</span>];\n"
         "<span class='kw'>for</span> (<span class='kw'>const</span> n <span class='kw'>of</span> names) {\n"
         "  <span class='fn'>console</span>.log(<span class='str'>`Hi ${n}`</span>);\n"
         "}"),
    card("ACCUMULATOR", "Build Up a Result",
         "A huge share of real code is: start with an empty total/list, loop, and add "
         "to it. Summing numbers, counting matches, filtering a list — all the same "
         "shape. Recognize the pattern and most tasks look familiar.",
         "<span class='com'># Bash: total the numbers in a file</span>\n"
         "total=<span class='num'>0</span>\n"
         "<span class='kw'>while</span> <span class='kw'>read</span> n; <span class='kw'>do</span>\n"
         "  total=$((total + n))\n"
         "<span class='kw'>done</span> &lt; numbers.txt\n"
         "<span class='fn'>echo</span> $total"),
    card("STEERING", "break &amp; continue",
         "Inside a loop, break exits early (‘found it — stop looking’) and continue "
         "skips to the next item (‘not interested in this one’). They keep loops from "
         "doing needless work."),
    card("NESTING", "Loops Inside Loops",
         "A loop inside a loop handles grids and combinations — every row, and within "
         "each row every column. Powerful, but remember it multiplies the work: 1,000 "
         "× 1,000 is a million steps. Use with care on big data.")
  ),
  topic("🧰", "Standard Library &amp; Packages", "Beginner • Tooling",
    card("DON'T REINVENT", "Someone Already Wrote It",
         "Need today’s date, a random number, JSON parsing, or HTTP requests? It "
         "almost certainly already exists. The standard library ships with the "
         "language; packages add the rest. Borrowing well-tested code beats writing "
         "buggy new code."),
    card("BRING IT IN", "import / require",
         "You pull in extra code with one line at the top of your file, then use it. "
         "Each language has its own word, but the idea is identical.",
         "<span class='com'># Python</span>\n"
         "<span class='kw'>import</span> random\n"
         "random.<span class='fn'>randint</span>(<span class='num'>1</span>, <span class='num'>6</span>)   <span class='com'># roll a die</span>\n"
         "<span class='com'>// JavaScript (Node)</span>\n"
         "<span class='kw'>const</span> fs = <span class='fn'>require</span>(<span class='str'>\"fs\"</span>);"),
    card("PACKAGE MANAGERS", "pip, npm &amp; Friends",
         "When you need something beyond the standard library, a package manager "
         "installs it from a public registry. pip for Python, npm for JavaScript. One "
         "command and the toolbox grows — just install only what you trust."),
    tbl(["Language", "Manager", "Install Example"],
        [["Python", "pip", "pip install requests"],
         ["JavaScript", "npm", "npm install axios"],
         ["Ruby", "gem", "gem install rails"],
         ["Rust", "cargo", "cargo add serde"]])
  ),
  topic("🧯", "Handling Errors Gracefully", "Beginner • Quality",
    card("CHOICE", "Crash or Catch?",
         "When something can fail — a missing file, bad input, a dropped network — you "
         "either let it crash (loud, sometimes fine) or catch it and respond calmly. "
         "User-facing programs should catch and show a friendly message, not a wall of "
         "red."),
    card("THE SHAPE", "try / catch (try / except)",
         "Wrap the risky bit in ‘try’; if it fails, the ‘catch’ block runs instead of "
         "crashing. A ‘finally’ block always runs, perfect for cleanup like closing a "
         "file.",
         "<span class='com'># Python</span>\n"
         "<span class='kw'>try</span>:\n"
         "    data = <span class='fn'>open</span>(<span class='str'>\"config.txt\"</span>).read()\n"
         "<span class='kw'>except</span> FileNotFoundError:\n"
         "    <span class='fn'>print</span>(<span class='str'>\"No config — using defaults\"</span>)"),
    card("BETTER", "Validate Before You Leap",
         "Many errors are avoidable: check that a number is in range or a field isn’t "
         "empty before using it. Use exceptions for the genuinely unexpected, not as a "
         "substitute for basic checks.")
  ),
  topic("🗃️", "Reading &amp; Writing Files", "Beginner • Core",
    card("WHY", "Programs Remember by Saving",
         "Variables vanish when a program ends; files persist. Reading and writing "
         "files is how scripts load settings, process data, and save results you can "
         "use tomorrow."),
    card("PATTERN", "Open, Use, Close",
         "Always pair opening a file with closing it. Modern languages give you a "
         "‘with’/auto-close form so you can’t forget — it tidies up even if an error "
         "happens midway.",
         "<span class='com'># Python: read a file line by line</span>\n"
         "<span class='kw'>with</span> <span class='fn'>open</span>(<span class='str'>\"log.txt\"</span>) <span class='kw'>as</span> f:\n"
         "    <span class='kw'>for</span> line <span class='kw'>in</span> f:\n"
         "        <span class='fn'>print</span>(line.strip())"),
    card("DATA FILES", "CSV: a Spreadsheet in Text",
         "CSV (comma-separated values) is the simplest way to store rows and columns "
         "as plain text — name,age on each line. Every spreadsheet and database can "
         "read it, which is why beginners meet it early."),
    card("CAREFUL", "Writing Overwrites",
         "Opening a file to write (‘w’) usually erases what was there; append mode "
         "(‘a’) adds to the end. Mixing these up is a classic way to wipe data — know "
         "which mode you’re in.")
  ),
  topic("♻️", "Refactoring &amp; Clean Code", "Beginner • Craft",
    card("WHAT", "Same Behavior, Better Shape",
         "Refactoring means improving how code reads without changing what it does. "
         "Working code can still be messy; tidying it later (once tests pass) is normal "
         "and healthy, not a sign you did it wrong."),
    card("QUICK WINS", "Names, Constants, Small Functions",
         "Three cheap upgrades: rename x to taxRate; replace mystery numbers with named "
         "constants (MAX_RETRIES = 3); and split a giant function into a few small "
         "ones that each do one thing. Future-you will be grateful."),
    card("DRY AGAIN", "Three Strikes, Refactor",
         "Copy-pasted the same logic a third time? That’s the signal to pull it into "
         "one function. Duplication isn’t just ugly — it’s a bug waiting to be fixed in "
         "only some of the copies."),
    tbl(["Smell (warning sign)", "Tidy-Up"],
        [["Mystery number like 86400", "Name it: SECONDS_PER_DAY"],
         ["Function that’s 200 lines", "Split into small, named steps"],
         ["Copy-pasted block ×3", "Extract one shared function"],
         ["Names like a, x, tmp", "Rename to what they mean"]])
  ),
  topic("🔍", "Regex in Plain English (Gentle Intro)", "Beginner • Text",
    card("WHAT", "Patterns for Finding Text",
         "A regular expression (regex) is a tiny language for describing text patterns "
         "— ‘a ZIP code,’ ‘any email,’ ‘three digits then a dash.’ It looks like cat "
         "walked on the keyboard, but you only need a few pieces to start."),
    card("STARTER PIECES", "The Handful That Covers a Lot",
         "Learn these and you can read most simple patterns: \\d is a digit, \\w a "
         "letter/number, . is any character, + means one-or-more, * means zero-or-more, "
         "and ^ $ anchor the start and end.",
         "<span class='com'># find 3 digits, a dash, then 4 digits (a phone tail)</span>\n"
         "<span class='str'>\\d{3}-\\d{4}</span>\n"
         "<span class='com'># a very rough email shape</span>\n"
         "<span class='str'>\\w+@\\w+\\.\\w+</span>"),
    card("ADVICE", "Test, Don’t Guess",
         "Even pros build regex on a live tester (paste sample text, watch matches "
         "light up) rather than in their head. Start loose, tighten until only the "
         "right things match. See this domain’s full Regex topic for the complete map.")
  ),
]

# =========================================================================
# LIFESTYLE — wave 3 (practical life)
# =========================================================================
LIFE3 = [
  topic("🧭", "Decision-Making", "Lifestyle • Judgment",
    card("DOORS", "One-Way vs. Two-Way Doors",
         "Some decisions are reversible (a two-way door — try it, walk back if wrong) "
         "and some aren’t (a one-way door). Spend real deliberation on the one-way "
         "doors; move fast and experiment on the rest. Most choices are two-way."),
    card("TRADE-OFFS", "Opportunity Cost",
         "Saying yes to one thing is saying no to everything else you could do with "
         "that time or money. The real cost of a choice isn’t just its price — it’s the "
         "best thing you gave up to make it."),
    card("ENOUGH", "Good Enough Beats Endless Search",
         "Chasing the absolute best (maximizing) often costs more than it returns. "
         "Decide what ‘good enough’ looks like up front, pick the first option that "
         "clears the bar, and move on. Done decisions free your mind."),
    card("PAUSE", "Sleep On the Big Ones",
         "Strong emotion is a bad time to decide. For anything major, give it a night; "
         "tomorrow’s calmer brain sees options today’s couldn’t. Urgency is often "
         "manufactured — real deadlines survive a good night’s sleep.")
  ),
  topic("🌱", "Money &amp; Adulting Basics", "Lifestyle • Practical",
    card("BUDGET", "The 50/30/20 Rule",
         "A simple starting budget: roughly 50% of take-home pay to needs (rent, food, "
         "bills), 30% to wants, and 20% to saving and paying down debt. Adjust to your "
         "life — the point is that every dollar gets a job."),
    card("SAFETY NET", "Emergency Fund First",
         "Before investing or splurging, build a cushion of a few months’ expenses in "
         "easy-to-reach savings. It turns a flat tire or lost job from a crisis into an "
         "inconvenience — and lets you sleep at night."),
    card("TIME MAGIC", "Compound Interest",
         "Money (and debt) grows on itself over time. Save early and modest amounts "
         "snowball; carry high-interest debt and it snowballs against you. Time is the "
         "ingredient — starting now beats starting big."),
    card("WATCH OUT", "Avoid Lifestyle Creep",
         "When income rises, spending quietly rises to match, and you feel no richer. "
         "Bank part of every raise before you get used to it. Distinguish needs from "
         "wants honestly — most ‘needs’ are wants in a nicer outfit."),
    tbl(["Term", "Plain Meaning"],
        [["Net (take-home) pay", "What lands in your account after tax"],
         ["Emergency fund", "3–6 months of expenses, kept accessible"],
         ["Interest", "The cost of borrowing / reward for saving"],
         ["Credit score", "A track record of repaying on time"],
         ["Budget", "A plan that gives every dollar a job"]])
  ),
]

DOMAINS = [
  dict(name="Script",    sentinel="<!-- BEGINNER4-SCRIPT v1 -->", topics=SCRIPT4,
       anchors=["<!-- /domain-body script -->"]),
  dict(name="Lifestyle", sentinel="<!-- BEGINNER4-LIFE v1 -->",   topics=LIFE3,
       anchors=["<!-- /domain-body lifestyle -->"]),
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
    print("BEGINNER-CONCEPTS-V4 patch —", "WRITE" if write else "DRY-RUN (add --write to apply)")
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
        print("\nLooks right? Apply with:  python3 patch_beginner_concepts_v4.py --write")

if __name__ == "__main__":
    main()
