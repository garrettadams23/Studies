#!/usr/bin/env python3
"""Third wave of beginner content — more core coding foundations for someone
brand new to IT, plus a second beginner topic for the remaining domains.
Idempotent (own sentinels).

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
# SCRIPT — more foundations
# =========================================================================
SCRIPT3 = [
  topic("🧠", "How Computers Think — Bits &amp; Binary", "Beginner • Foundations",
    card("THE ATOM", "Bits &amp; Bytes",
         "Deep down, a computer only knows two states: on/off, 1/0. One of those is a "
         "bit. Eight bits make a byte, which is enough to store one character like the "
         "letter ‘A’. Everything — text, photos, music — is ultimately just bytes."),
    card("WHY HEX", "Binary, Decimal &amp; Hex",
         "Binary (base-2) is how the machine counts; it gets long fast, so coders "
         "often write numbers in hex (base-16, 0–9 then A–F) as a compact shorthand. "
         "That’s why colors look like #FF8800 — three hex bytes for red, green, blue."),
    card("TEXT IS NUMBERS", "ASCII &amp; Unicode",
         "Computers store letters as numbers using a lookup table. ASCII covered "
         "English; Unicode extended it to every language and emoji on Earth. So 😀 and "
         "‘A’ are both just agreed-upon numbers under the hood."),
    tbl(["Unit", "Size", "Rough Real-World Amount"],
        [["Bit", "1 or 0", "A single yes/no"],
         ["Byte", "8 bits", "One character"],
         ["Kilobyte (KB)", "~1,000 bytes", "A short email"],
         ["Megabyte (MB)", "~1,000 KB", "A minute of music"],
         ["Gigabyte (GB)", "~1,000 MB", "A long movie"],
         ["Terabyte (TB)", "~1,000 GB", "A big hard drive"]])
  ),
  topic("📁", "Files, Paths &amp; the Command Line", "Beginner • Foundations",
    card("ADDRESS", "Absolute vs. Relative Paths",
         "A path is a file’s address. Absolute starts from the root and is the full "
         "address (/home/sam/notes.txt) — true from anywhere. Relative starts from "
         "where you currently are (notes.txt or ../notes.txt) — like “two doors down "
         "from here.”"),
    card("SHORTHAND", "The Symbols You’ll See",
         "A few path symbols show up constantly: . is here, .. is up one folder, ~ is "
         "your home folder, and / separates folders (\\ on Windows). Learn these four "
         "and the command line stops feeling like a maze."),
    card("SUPERPOWER", "Pipes &amp; Redirects",
         "The Unix philosophy: small tools that do one thing, joined together. A pipe "
         "(|) feeds one command’s output into the next; a redirect (&gt;) sends output "
         "into a file. This is how huge tasks get built from tiny pieces.",
         "<span class='com'># count how many lines contain \"error\"</span>\n"
         "<span class='fn'>cat</span> app.log | <span class='fn'>grep</span> error | <span class='fn'>wc</span> -l\n"
         "<span class='com'># save the matches to a file</span>\n"
         "<span class='fn'>grep</span> error app.log &gt; errors.txt"),
    card("TIP", "Tab Completion &amp; History",
         "Two habits that make the terminal feel fast: press Tab to auto-finish file "
         "names (fewer typos), and press the Up arrow to recall commands you already "
         "ran. Lazy is efficient here.")
  ),
  topic("🧩", "Thinking in Algorithms", "Beginner • Problem-Solving",
    card("PLAIN", "An Algorithm Is Just a Plan",
         "An algorithm is a clear, finite list of steps to get a result — a recipe, "
         "directions to a friend’s house, the steps to make tea. Coding is mostly "
         "writing the plan precisely enough that a literal machine can follow it."),
    card("WORKED EXAMPLE", "Find the Biggest Number",
         "Watch how a vague goal becomes steps: assume the first item is the biggest, "
         "look at each remaining item, and whenever you see a bigger one, remember it "
         "instead. At the end, you’re holding the biggest. That’s an algorithm.",
         "<span class='com'># pseudocode</span>\n"
         "biggest = first item\n"
         "<span class='kw'>for</span> each item in list:\n"
         "    <span class='kw'>if</span> item &gt; biggest:\n"
         "        biggest = item\n"
         "<span class='kw'>return</span> biggest"),
    card("WHY IT MATTERS", "Some Plans Are Faster",
         "Finding a name in a shuffled pile means checking every card; in a sorted "
         "phone book you can flip to the middle and halve the search each time. Same "
         "goal, wildly different speed — that idea (Big-O) is why algorithm choice "
         "matters as data grows.")
  ),
  topic("🏛️", "Programming Paradigms (Gently)", "Beginner • Concepts",
    card("DON'T PANIC", "Different Styles, Same Goal",
         "A paradigm is just a style of organizing code. You’ll hear scary words — "
         "they describe how people keep big programs tidy. As a beginner you’ll mostly "
         "write procedural code (step by step) and that’s perfectly fine."),
    card("OBJECTS", "What ‘Object-Oriented’ Means",
         "OOP bundles data with the actions on it into ‘objects’ — nouns that can do "
         "verbs. A Car object holds its speed and color (data) and can drive() or "
         "brake() (actions). It mirrors how we already think about things in the world."),
    tbl(["Paradigm", "The Idea", "One Line"],
        [["Procedural", "Steps in order", "Do this, then this, then this"],
         ["Object-oriented", "Bundled nouns", "Objects hold data + actions"],
         ["Functional", "Pure functions", "Inputs in, outputs out, no surprises"],
         ["Event-driven", "React to events", "When clicked, do this"]])
  ),
  topic("🧪", "Testing Your Code", "Beginner • Quality",
    card("WHY", "Tests Catch Tomorrow’s Bug",
         "A test is code that checks your code still works. It feels like extra effort "
         "until the day a ‘small fix’ silently breaks something across the project — "
         "and a test catches it in one second instead of a customer catching it later."),
    card("THE SHAPE", "Arrange, Act, Assert",
         "Most tests follow three beats: set up the inputs (arrange), run the thing "
         "(act), and check the result is what you expected (assert). If the assertion "
         "fails, you found a bug — on purpose, in private.",
         "<span class='com'>// a tiny test of add(a,b)</span>\n"
         "<span class='kw'>let</span> result = <span class='fn'>add</span>(<span class='num'>2</span>, <span class='num'>3</span>);   <span class='com'>// act</span>\n"
         "<span class='fn'>assert</span>(result === <span class='num'>5</span>);   <span class='com'>// expect 5</span>"),
    card("EDGE CASES", "Happy Path vs. Sad Path",
         "The happy path is normal input (add 2 and 3). The sad path is the weird "
         "stuff: empty values, zero, negatives, huge numbers, the wrong type. Bugs "
         "love the edges — test there, not just the easy middle.")
  ),
  topic("💻", "Setting Up to Code", "Beginner • Getting Started",
    card("TOOLS", "What You Actually Need",
         "Three free things get you coding: a good editor (VS Code is the popular "
         "pick), a terminal (already on your computer), and the language installed "
         "(e.g., Python). That’s it — no expensive software required."),
    card("FIRST RUN", "Editor → Save → Run",
         "The loop: type code in the editor, save the file with the right extension "
         "(.py, .js, .sh), then run it from the terminal. Seeing your first output "
         "appear is the moment it clicks.",
         "<span class='com'># save as hello.py, then in the terminal:</span>\n"
         "<span class='fn'>python3</span> hello.py\n"
         "<span class='com'># save as hello.js, then:</span>\n"
         "<span class='fn'>node</span> hello.js"),
    tbl(["Language", "File Ends In", "Run It With"],
        [["Python", ".py", "python3 file.py"],
         ["JavaScript", ".js", "node file.js"],
         ["Bash", ".sh", "bash file.sh"],
         ["HTML", ".html", "open it in a browser"]])
  ),
  topic("📚", "Learning to Learn Code", "Beginner • Mindset",
    card("REAL SKILL", "Searching Is a Skill, Not Cheating",
         "Professionals look things up all day. The talent is asking well: include the "
         "language, what you tried, and the exact error text. ‘python read file line by "
         "line’ beats ‘why broken.’"),
    card("UNDERSTAND IT", "Copy to Learn, Not to Paste",
         "Borrowing example code is fine — but read it line by line until you could "
         "rewrite it yourself. Pasting code you don’t understand just moves the bug "
         "somewhere you can’t find it."),
    card("SHRINK IT", "Smallest Reproducible Example",
         "Stuck on a bug in 200 lines? Strip it down to the 5 lines that still break. "
         "Half the time you’ll spot the problem yourself; the other half you’ll get a "
         "great answer because the question is clear."),
    card("GROW IT", "Build Tiny Real Projects",
         "Tutorials teach syntax; projects teach problem-solving. Automate something "
         "you actually do — rename photos, total a budget, scrape a page. Finishing "
         "small real things beats half-watching long courses.")
  ),
]

# =========================================================================
# THREAT — kill chain simply
# =========================================================================
THREAT2 = [
  topic("🔗", "Anatomy of an Attack (Step by Step)", "Sec+ • Start Here",
    card("BIG IDEA", "Attacks Happen in Stages",
         "Real attacks aren’t one magic click — they’re a chain of steps, each "
         "depending on the last. The good news: break any link and you stop the whole "
         "attack. Defenders aim to catch it as early as possible."),
    card("WALKTHROUGH", "The Cyber Kill Chain, Plainly",
         "First the attacker studies you (recon), then sends the bait (delivery), "
         "tricks a weakness (exploitation), drops their tool (installation), phones "
         "home for orders (command &amp; control), and finally acts — steals, encrypts, "
         "or spies (actions on objectives)."),
    tbl(["Stage", "What the Attacker Does", "A Defense"],
        [["Recon", "Research the target", "Limit public info"],
         ["Delivery", "Send phishing / malware", "Email filtering, training"],
         ["Exploitation", "Trigger the weakness", "Patch &amp; harden"],
         ["Installation", "Plant their foothold", "Endpoint protection (EDR)"],
         ["Command &amp; Control", "Remote-control it", "Monitor outbound traffic"],
         ["Actions", "Steal / encrypt / spy", "Least privilege, backups"]])
  ),
]

# =========================================================================
# GRC — frameworks without jargon
# =========================================================================
GRC2 = [
  topic("📋", "Frameworks Without the Jargon", "GRC • Start Here",
    card("WHAT", "A Framework Is a Good-Practice Checklist",
         "You don’t have to invent security from scratch — experts already wrote down "
         "what works. A framework is that shared checklist, so organizations aim at a "
         "known-good target instead of guessing."),
    card("THE BIG ONE", "NIST CSF in Five Words",
         "The popular NIST Cybersecurity Framework boils down to five plain verbs: "
         "Identify what you have, Protect it, Detect trouble, Respond when it happens, "
         "and Recover afterward. (A newer sixth, Govern, wraps leadership around it.)"),
    card("WHY", "Common Language, Fewer Gaps",
         "Frameworks let a whole team — and auditors, and vendors — speak the same "
         "language and spot what’s missing. ‘We’re weak on Detect’ is a clear, "
         "actionable sentence everyone understands."),
    tbl(["NIST CSF Function", "The Question It Answers"],
        [["Identify", "What do we have and what’s at risk?"],
         ["Protect", "How do we safeguard it?"],
         ["Detect", "How will we notice an attack?"],
         ["Respond", "What do we do when it happens?"],
         ["Recover", "How do we get back to normal?"]])
  ),
]

# =========================================================================
# OPS — a day in the SOC
# =========================================================================
OPS2 = [
  topic("🚨", "A Day in the SOC", "CySA+ • Start Here",
    card("THE FLOW", "From Alert to Resolution",
         "An analyst’s day is a queue of alerts. For each: triage (is it real and how "
         "urgent?), investigate (what actually happened?), respond or escalate, then "
         "document so the next person isn’t starting from zero."),
    card("TEAMS", "Tier 1, 2, 3",
         "Tier 1 triages the flood and handles the routine; Tier 2 digs into the "
         "tricky ones; Tier 3 are the specialists and threat hunters. It’s a normal "
         "career ladder — most people start at Tier 1 and learn fast."),
    card("MEASURE", "Why Speed Matters",
         "Two clocks rule the SOC: how fast you notice (detect) and how fast you "
         "contain (respond). The longer an attacker has, the more they take — so "
         "shaving minutes off those times is the whole point."),
    tbl(["Term", "Plain Meaning"],
        [["Triage", "Sort by urgency, like an ER"],
         ["Escalate", "Hand a hard one up a tier"],
         ["False positive", "An alert that turned out to be nothing"],
         ["Handoff", "Briefing the next shift so nothing drops"],
         ["MTTR", "Mean time to respond — average cleanup speed"]])
  ),
]

# =========================================================================
# PENTEST — scoping & RoE
# =========================================================================
PENTEST2 = [
  topic("🧾", "Scoping &amp; Rules of Engagement", "PenTest+ • Start Here",
    card("WHY PAPERWORK", "The Boring Part Keeps You Out of Jail",
         "Before any hacking, both sides sign what’s allowed. This isn’t bureaucracy "
         "for its own sake — it’s the difference between a paid professional and a "
         "felony. Scope and authorization are the seatbelt of the job."),
    card("SCOPE", "What’s In, What’s Off-Limits",
         "Scope lists exactly which systems, addresses, and techniques are fair game — "
         "and which are absolutely not (production payroll, third-party clouds, "
         "physical break-ins). When in doubt, it’s out of scope."),
    card("SAFETY", "Deconfliction &amp; the ‘Get-Out-of-Jail’ Letter",
         "Testers carry written authorization in case security catches them (good — "
         "that means detection works!). A deconfliction contact lets everyone quickly "
         "tell ‘is this the tester, or a real attacker?’ during the engagement."),
    tbl(["RoE Item", "Why It’s There"],
        [["Authorization", "Written proof you’re allowed"],
         ["Scope / exclusions", "Exactly what you may and may not touch"],
         ["Time windows", "When testing is permitted"],
         ["Data handling", "How findings &amp; sensitive data are protected"],
         ["Emergency contact", "Who to call if something goes wrong"]])
  ),
]

# =========================================================================
# AI — using AI well
# =========================================================================
AI2 = [
  topic("🤝", "Using AI Well — Prompting &amp; Responsibility", "AI+ • Start Here",
    card("BE CLEAR", "Specific Prompts Get Better Answers",
         "Vague in, vague out. Tell the AI the role, the goal, the format, and any "
         "constraints. ‘Explain DNS to a 10-year-old in 3 sentences’ beats ‘explain "
         "DNS’ every time."),
    card("SHOW, DON'T JUST TELL", "Give Context &amp; Examples",
         "Paste the relevant details and one example of what ‘good’ looks like. The "
         "model can’t read your mind or your files — context is the single biggest "
         "lever on answer quality. Then iterate: refine and ask again."),
    card("TRUST CAREFULLY", "Verify, Don’t Outsource Judgment",
         "AI is a fast, confident intern that sometimes makes things up (hallucinates). "
         "Use it to draft, brainstorm, and explain — then check anything that matters. "
         "You stay responsible for the final answer."),
    card("BE SAFE", "Don’t Paste Secrets",
         "Never feed passwords, customer data, or company secrets into tools you don’t "
         "control — assume it could be stored or seen. Watch for bias too: AI learned "
         "from human data and can repeat human prejudices."),
    tbl(["Weak Prompt", "Stronger Prompt"],
        [["“fix my code”", "“This Python errors with X; here are 10 lines — what’s wrong?”"],
         ["“write about dogs”", "“Write 100 friendly words on crate-training a puppy”"],
         ["“is this safe?”", "“List risks in this login function and how to fix each”"]])
  ),
]

# =========================================================================
# SHORTCUT — text & window editing
# =========================================================================
SHORTCUT2 = [
  topic("📝", "Text-Editing &amp; Window Shortcuts", "General • Start Here",
    card("EDIT FASTER", "Move &amp; Select by Word/Line",
         "Hold Ctrl (⌥ on Mac) to jump word-by-word instead of letter-by-letter; add "
         "Shift to select as you go. Home/End jump to the start/end of a line. These "
         "turn clumsy editing into precision."),
    card("WINDOWS", "Snap &amp; Switch",
         "Win + ← / → snaps a window to half the screen — perfect for notes beside a "
         "browser. Win + Tab (or ⌃↑ on Mac) shows everything open. Virtual desktops "
         "let you keep work and life in separate spaces."),
    tbl(["Keys (Win/Linux)", "What It Does"],
        [["Ctrl + ← / →", "Jump one word left/right"],
         ["Shift + ← / →", "Select while moving"],
         ["Ctrl + Shift + ← / →", "Select a word at a time"],
         ["Home / End", "Start / end of the line"],
         ["Ctrl + Backspace", "Delete the previous word"],
         ["Win + ← / →", "Snap window to half-screen"],
         ["Win + D", "Show the desktop"]])
  ),
]

# =========================================================================
# MILITARY — ranks & echelons
# =========================================================================
MILITARY2 = [
  topic("🎖️", "Ranks &amp; Echelons (Very Basic)", "MIL • Start Here",
    card("THREE GROUPS", "Enlisted, NCO, Officer",
         "Most militaries have three broad tiers. Enlisted are the trained doers; "
         "NCOs (non-commissioned officers, like sergeants) are experienced leaders "
         "risen from the ranks; officers are commissioned leaders who plan and command. "
         "NCOs are often called ‘the backbone.’"),
    card("SIZE LADDER", "From Squad to Division",
         "Units nest like Russian dolls, each led by a more senior person: a handful "
         "of troops form a squad, squads form a platoon, platoons a company, and so on "
         "up. Bigger unit = higher-ranking commander."),
    tbl(["Unit (Army, roughly)", "Size", "Led By (roughly)"],
        [["Squad", "~8–12", "Sergeant"],
         ["Platoon", "~30–40", "Lieutenant"],
         ["Company", "~100–150", "Captain"],
         ["Battalion", "~500–800", "Lt. Colonel"],
         ["Brigade", "~3,000+", "Colonel"],
         ["Division", "~10,000+", "Major General"]])
  ),
]

DOMAINS = [
  dict(name="Script",    sentinel="<!-- BEGINNER3-SCRIPT v1 -->", topics=SCRIPT3,
       anchors=["<!-- /domain-body script -->"]),
  dict(name="Threat",    sentinel="<!-- BEGINNER3-THREAT v1 -->", topics=THREAT2,
       anchors=["<!-- /domain-body threat -->"]),
  dict(name="GRC",       sentinel="<!-- BEGINNER3-GRC v1 -->",    topics=GRC2,
       anchors=["<!-- /domain-body grc -->"]),
  dict(name="Ops",       sentinel="<!-- BEGINNER3-OPS v1 -->",    topics=OPS2,
       anchors=["<!-- /domain-body ops -->"]),
  dict(name="PenTest",   sentinel="<!-- BEGINNER3-PENTEST v1 -->",topics=PENTEST2,
       anchors=["<!-- /domain-body pentest -->"]),
  dict(name="AI",        sentinel="<!-- BEGINNER3-AI v1 -->",     topics=AI2,
       anchors=["<!-- /domain-body ai -->"]),
  dict(name="Shortcut",  sentinel="<!-- BEGINNER3-SHORTCUT v1 -->",topics=SHORTCUT2,
       anchors=["<!-- /domain-body shortcuts -->", "<!-- /domain-body shortcut -->"]),
  dict(name="Military",  sentinel="<!-- BEGINNER3-MIL v1 -->",    topics=MILITARY2,
       anchors=["<!-- /domain-body military -->"]),
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
    print("BEGINNER-CONCEPTS-V3 patch —", "WRITE" if write else "DRY-RUN (add --write to apply)")
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
        print("\nLooks right? Apply with:  python3 patch_beginner_concepts_v3.py --write")

if __name__ == "__main__":
    main()
