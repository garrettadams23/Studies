#!/usr/bin/env python3
"""Second wave of beginner content — deepens the coding track for someone brand
new to IT and adds more life/mental-model concepts. Idempotent (own sentinels).

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
# SCRIPT — deeper coding fundamentals
# =========================================================================
SCRIPT2 = [
  topic("🧮", "Operators &amp; Expressions", "Beginner • Core",
    card("DO MATH", "Arithmetic Operators",
         "Operators are the verbs of code. The math ones work like a calculator, with "
         "one extra: <strong>%</strong> (modulo) gives the remainder — handy for "
         "“is this number even?” (n % 2 == 0).",
         "<span class='com'>// JavaScript</span>\n"
         "<span class='num'>7</span> + <span class='num'>2</span>   <span class='com'>// 9   add</span>\n"
         "<span class='num'>7</span> - <span class='num'>2</span>   <span class='com'>// 5   subtract</span>\n"
         "<span class='num'>7</span> * <span class='num'>2</span>   <span class='com'>// 14  multiply</span>\n"
         "<span class='num'>7</span> / <span class='num'>2</span>   <span class='com'>// 3.5 divide</span>\n"
         "<span class='num'>7</span> % <span class='num'>2</span>   <span class='com'>// 1   remainder</span>"),
    card("COMPARE", "Comparison &amp; Logic",
         "Comparisons ask a true/false question; logical operators combine them. "
         "Watch the classic trap: <strong>=</strong> assigns a value, but "
         "<strong>==</strong> (or ===) compares two. One equals sign in an if "
         "statement is a top-three beginner bug."),
    tbl(["Operator", "Means", "Example → result"],
        [["==  /  ===", "Equal to", "5 == 5 → true"],
         ["!=", "Not equal", "5 != 4 → true"],
         ["&gt;  &lt;", "Greater / less than", "5 &gt; 4 → true"],
         ["&gt;=  &lt;=", "Greater/less or equal", "5 &gt;= 5 → true"],
         ["&amp;&amp;", "AND (both true)", "true &amp;&amp; false → false"],
         ["||", "OR (either true)", "true || false → true"],
         ["!", "NOT (flips it)", "!true → false"]]),
    card("ORDER", "Precedence — Use Parentheses",
         "Just like math, * happens before +. When in doubt, add parentheses to make "
         "the order obvious — they cost nothing and save confusion: "
         "(price * qty) + tax reads clearly.")
  ),
  topic("🔤", "Working with Text — Strings", "Beginner • Core",
    card("BASICS", "Strings Are Just Text",
         "A string is any run of characters in quotes: a name, an address, a whole "
         "paragraph. You can measure it, change its case, search it, and stitch pieces "
         "together (concatenation).",
         "<span class='com'>// JavaScript</span>\n"
         "<span class='kw'>let</span> s = <span class='str'>\"Hello\"</span>;\n"
         "s.length              <span class='com'>// 5</span>\n"
         "s.toUpperCase()       <span class='com'>// \"HELLO\"</span>\n"
         "s + <span class='str'>\" world\"</span>        <span class='com'>// \"Hello world\"</span>"),
    card("MODERN", "Templates Beat Gluing",
         "Instead of mashing strings and variables with +, most languages let you drop "
         "variables right inside a string. It’s easier to read and harder to break.",
         "<span class='com'>// JavaScript template literal (back-ticks)</span>\n"
         "<span class='kw'>let</span> name = <span class='str'>\"Sam\"</span>;\n"
         "<span class='str'>`Hi ${name}, you have ${3 + 2} alerts`</span>\n"
         "<span class='com'># Bash</span>\n"
         "<span class='fn'>echo</span> <span class='str'>\"Hi $name\"</span>"),
    card("GOTCHA", "Quotes &amp; Escaping",
         "If your text contains a quote, you either switch quote styles or “escape” it "
         "with a backslash (\\\"). A stray quote is the reason a script suddenly "
         "refuses to run — count your quotes when text breaks.")
  ),
  topic("📥", "Input &amp; Output — Talking to the User", "Beginner • Core",
    card("OUTPUT", "Printing Results",
         "The first thing every coder does is print something — the classic “Hello, "
         "world!”. Printing is also how you peek at what your code is doing while you "
         "build it.",
         "<span class='com'># Bash</span>\n"
         "<span class='fn'>echo</span> <span class='str'>\"Hello, world!\"</span>\n"
         "<span class='com'>// JavaScript</span>\n"
         "<span class='fn'>console</span>.log(<span class='str'>\"Hello, world!\"</span>);"),
    card("INPUT", "Arguments &amp; Reading In",
         "Scripts often take input two ways: arguments typed after the command, or by "
         "asking the user mid-run. Arguments make scripts reusable on different files "
         "or values.",
         "<span class='com'># Bash: first argument after the script name</span>\n"
         "<span class='fn'>echo</span> <span class='str'>\"Backing up $1\"</span>\n"
         "<span class='com'># run as:  ./backup.sh  /home/sam</span>"),
    card("THREE STREAMS", "stdin, stdout, stderr",
         "Programs have an in-tray (stdin), a normal out-tray (stdout), and a separate "
         "error out-tray (stderr). Keeping errors separate lets you log problems "
         "without polluting real results — and lets you pipe output into the next tool."),
    card("SIGNAL", "Exit Codes",
         "When a program finishes it returns a number: 0 means success, anything else "
         "means a problem. Scripts use this to decide what to do next — “if the backup "
         "succeeded, then delete the temp file.”")
  ),
  topic("🔭", "Scope — Where Variables Live", "Beginner • Core",
    card("IDEA", "Local vs. Global",
         "Scope is where a variable can be seen. A variable made inside a function is "
         "usually local — it exists only in that room and vanishes when the function "
         "ends. A global is visible everywhere, like a notice on the front door."),
    card("WHY CARE", "Globals Cause Spooky Bugs",
         "If everything is global, any line anywhere can change it, and tracking down "
         "“who set this to 0?” becomes misery. Keep variables as local as possible; "
         "pass what a function needs in, and return what it produces out.",
         "<span class='com'>// JavaScript</span>\n"
         "<span class='kw'>function</span> <span class='fn'>tip</span>(bill) {\n"
         "  <span class='kw'>let</span> rate = <span class='num'>0.2</span>;  <span class='com'>// local: lives only here</span>\n"
         "  <span class='kw'>return</span> bill * rate;\n"
         "}")
  ),
  topic("🧰", "Which Language Should I Learn First?", "Beginner • Guidance",
    card("RELAX", "The Concepts Transfer",
         "Don’t agonize over the “best” first language — variables, loops, functions, "
         "and data structures exist in all of them. Learn one well and the next one is "
         "mostly new vocabulary, not new ideas."),
    card("HONEST PICK", "A Simple Recommendation",
         "For most beginners: start with <strong>Python</strong> — it reads almost "
         "like English and is used everywhere from security scripting to AI. Add "
         "<strong>JavaScript</strong> when you want things to happen in a web browser."),
    tbl(["Goal", "Good First Language", "Why"],
        [["General / automation / AI", "Python", "Readable, huge library ecosystem"],
         ["Websites &amp; browser apps", "JavaScript", "The only language browsers run"],
         ["Glue tasks on Linux/servers", "Bash", "Built into every Unix shell"],
         ["Asking questions of data", "SQL", "The language of databases"],
         ["Windows administration", "PowerShell", "Deep control of Windows + objects"]])
  ),
  topic("🌐", "How the Web Works (for Coders)", "Beginner • Web",
    card("THE TRIO", "HTML, CSS, JavaScript",
         "Every web page is three layers working together: HTML is the structure "
         "(the skeleton), CSS is the style (the skin and clothes), and JavaScript is "
         "the behavior (the muscles that react when you click).",
         "<span class='com'>&lt;!-- a tiny page --&gt;</span>\n"
         "&lt;<span class='kw'>h1</span>&gt;Hello&lt;/<span class='kw'>h1</span>&gt;          <span class='com'>&lt;!-- HTML: structure --&gt;</span>\n"
         "&lt;<span class='kw'>style</span>&gt; h1 { color: teal } &lt;/<span class='kw'>style</span>&gt;  <span class='com'>&lt;!-- CSS --&gt;</span>\n"
         "&lt;<span class='kw'>script</span>&gt; <span class='fn'>alert</span>(<span class='str'>'hi'</span>) &lt;/<span class='kw'>script</span>&gt;   <span class='com'>&lt;!-- JS --&gt;</span>"),
    card("THE TRIP", "What Happens When You Click a Link",
         "Your browser (the client) asks a server for a page. DNS turns the name into "
         "an address, the request travels over the Internet, the server replies with "
         "HTML/CSS/JS, and the browser paints it on screen — usually in under a second."),
    card("TWO SIDES", "Frontend vs. Backend",
         "Frontend is what runs in the browser — what you see and click. Backend is "
         "what runs on the server — databases, logins, business logic. “Full-stack” "
         "just means someone comfortable on both sides."),
    tbl(["Layer", "Job", "Beginner Analogy"],
        [["HTML", "Content &amp; structure", "The walls and rooms"],
         ["CSS", "Look &amp; layout", "Paint and furniture"],
         ["JavaScript", "Interactivity", "Light switches that do things"],
         ["Backend / API", "Data &amp; rules", "The staff in the back office"]])
  ),
  topic("🔐", "Secure Coding Basics (Beginner)", "Beginner • SecX",
    card("RULE #1", "Never Trust Input",
         "Anything a user (or another system) sends could be a mistake or an attack. "
         "Always check it: right type, sane length, expected format. “Validate, don’t "
         "assume” is the whole game — and ties straight back to ASS-U-ME."),
    card("CLASSIC ATTACK", "SQL Injection, Simply",
         "If you build a database query by gluing in raw user text, a clever user can "
         "write text that changes your query. The fix: use parameters / prepared "
         "statements so input is treated as data, never as commands.",
         "<span class='com'># BAD — user text becomes part of the command</span>\n"
         "query = <span class='str'>\"SELECT * FROM users WHERE name='\"</span> + name + <span class='str'>\"'\"</span>\n\n"
         "<span class='com'># GOOD — the ? is a safe placeholder for data</span>\n"
         "query = <span class='str'>\"SELECT * FROM users WHERE name = ?\"</span>"),
    card("SECRETS", "Don’t Hardcode Passwords",
         "Never paste passwords, API keys, or tokens directly into code that gets "
         "shared or pushed to GitHub. Use environment variables or a secrets manager. "
         "Leaked keys in public repos are scooped up by bots within minutes."),
    card("HABITS", "The Cheap Wins",
         "Keep dependencies updated (old libraries have known holes), give code the "
         "least access it needs, log errors but never log passwords, and let proven "
         "libraries handle crypto — never invent your own encryption."),
    tbl(["Beginner Mistake", "Safer Habit"],
        [["Trusting user input", "Validate &amp; sanitize everything"],
         ["Building queries by gluing strings", "Parameterized / prepared statements"],
         ["Passwords in the source code", "Environment variables / secrets vault"],
         ["Showing raw errors to users", "Friendly message + log the detail"],
         ["Rolling your own crypto", "Use vetted, standard libraries"]])
  ),
]

# =========================================================================
# NET — second beginner topic
# =========================================================================
NET2 = [
  topic("🔢", "IP Addresses &amp; Subnets (Gently)", "Net+ • Start Here",
    card("READ IT", "What an IPv4 Address Looks Like",
         "IPv4 is four numbers 0–255 separated by dots, like 192.168.1.50. Each device "
         "on a network needs one. We’re slowly running out of them, which is why "
         "IPv6 (much longer, with letters) was invented."),
    card("TWO WORLDS", "Public vs. Private",
         "Private addresses (like 192.168.x.x and 10.x.x.x) are reused inside homes and "
         "offices — like apartment numbers that only mean something in your building. "
         "Public addresses are unique on the whole Internet, like a full street address."),
    card("NEIGHBORHOODS", "What a Subnet Is",
         "A subnet groups nearby addresses into one neighborhood so traffic stays "
         "local and organized. The subnet mask (e.g., 255.255.255.0) is just the line "
         "that says “these addresses are neighbors; everything else is out of town.”"),
    tbl(["Term", "Plain-English Meaning"],
        [["DHCP", "Hands out IP addresses automatically so you don’t have to"],
         ["Default gateway", "The exit door to other networks / the Internet"],
         ["Subnet mask", "Marks which part of the address is the neighborhood"],
         ["IPv6", "The newer, much larger address system"],
         ["NAT", "Lets many private devices share one public address"]])
  ),
]

# =========================================================================
# SEC — everyday hygiene
# =========================================================================
SEC2 = [
  topic("🧱", "Everyday Security Hygiene", "Sec+ • Start Here",
    card("DO THESE", "The Habits That Stop Most Attacks",
         "You don’t need to be an expert to be safe. A handful of boring habits blocks "
         "the vast majority of real-world attacks — the digital equivalent of washing "
         "your hands and locking your door."),
    card("BACKUPS", "The 3-2-1 Rule",
         "Keep 3 copies of anything important, on 2 different kinds of storage, with 1 "
         "copy kept offsite/offline. Then a lost laptop, a crashed drive, or "
         "ransomware becomes an annoyance instead of a disaster — if you’ve tested "
         "that the restore actually works."),
    card("PASSWORDS", "Use a Manager + MFA",
         "Humans can’t remember 100 strong, unique passwords — so don’t. A password "
         "manager remembers them for you; you remember one good master passphrase. "
         "Turn on multi-factor authentication everywhere it’s offered."),
    tbl(["Habit", "Why It Helps"],
        [["Install updates promptly", "Patches close known holes attackers use"],
         ["Password manager", "Unique strong passwords without memorizing"],
         ["Enable MFA", "A stolen password alone won’t get in"],
         ["Think before you click", "Stops most phishing cold"],
         ["Lock your screen", "30 seconds away ≠ open to anyone walking by"],
         ["Back up (3-2-1)", "Turns disasters into inconveniences"]])
  ),
]

# =========================================================================
# LINUX — permissions & packages
# =========================================================================
LINUX2 = [
  topic("🧭", "Permissions &amp; Packages for Newcomers", "Linux+ • Start Here",
    card("WHO CAN DO WHAT", "Read, Write, Execute",
         "Every file says what three groups may do with it: the owner, the group, and "
         "everyone else. The three powers are read (look), write (change), and execute "
         "(run it as a program). ‘rwx’ is just those three letters."),
    card("ADMIN MODE", "sudo = “do this as admin”",
         "Normal users can’t break the whole system by accident — a safety feature. "
         "Putting sudo in front of a command says “I really mean it, run this with "
         "admin power.” Use it deliberately; with great power comes great rm -rf.",
         "<span class='fn'>sudo</span> apt update      <span class='com'># run as administrator</span>\n"
         "<span class='fn'>chmod</span> +x script.sh   <span class='com'># make a file runnable</span>"),
    card("APP STORE FOR THE TERMINAL", "Package Managers",
         "You don’t download installers in Linux — a package manager fetches, installs, "
         "and updates software from trusted repositories, handling all the pieces it "
         "depends on. apt (Debian/Ubuntu), dnf (Fedora), and pacman (Arch) are the "
         "common ones."),
    tbl(["You Want To…", "Command (Ubuntu/Debian)"],
        [["Refresh the catalog", "sudo apt update"],
         ["Install a program", "sudo apt install name"],
         ["Update everything", "sudo apt upgrade"],
         ["Remove a program", "sudo apt remove name"],
         ["Search for one", "apt search keyword"]])
  ),
]

# =========================================================================
# LIFESTYLE — habits, communication, resilience, more proverbs
# =========================================================================
LIFE2 = [
  topic("⏳", "Habits &amp; Time", "Lifestyle • Getting Things Done",
    card("COMPOUNDING", "1% Better",
         "Tiny improvements compound. Getting 1% better each day isn’t flashy, but over "
         "a year it stacks into a transformation. Big results are usually small habits "
         "repeated longer than other people are willing to."),
    card("START SMALL", "The Two-Minute Rule",
         "To beat procrastination, shrink the task until starting takes under two "
         "minutes: “write one sentence,” “open the file,” “put on the shoes.” Starting "
         "is the hard part; momentum does the rest."),
    card("PRIORITIES", "Eat the Frog",
         "Do your most important (often most dreaded) task first, while your energy and "
         "willpower are fresh. Everything after it feels downhill, and you’re not "
         "dragging the dread around all day."),
    tbl(["Idea", "In One Line"],
        [["Pareto (80/20)", "A few efforts produce most of the results"],
         ["Parkinson’s Law", "Work expands to fill the time you give it"],
         ["Time-boxing", "Give a task a fixed slot, then stop"],
         ["Don’t-break-the-chain", "Mark each day you do the habit; keep the streak"]])
  ),
  topic("🗣️", "Communication &amp; Relationships", "Lifestyle • People",
    card("LISTEN", "Seek First to Understand",
         "Most arguments are two people waiting to talk. Try to truly understand the "
         "other side first — repeat it back until they say “yes, exactly.” You can’t "
         "be persuasive to someone who doesn’t feel heard."),
    card("OWN IT", "Use “I” Statements",
         "“I felt ignored when the change shipped without a heads-up” lands far better "
         "than “you always ignore me.” Describe your experience instead of accusing, "
         "and the other person can hear you instead of defending."),
    card("CHARITY", "Assume Good Intent",
         "Walk in assuming people are doing their best with what they know (see "
         "Hanlon’s Razor). It’s usually true, it lowers your blood pressure, and it "
         "leaves room to be pleasantly surprised."),
    card("MANNERS", "Praise in Public, Correct in Private",
         "Recognition feels best with an audience; criticism stings worst with one. "
         "Flip the venues and people trust you with hard feedback because you never "
         "made it humiliating.")
  ),
  topic("💪", "Resilience &amp; Perspective", "Lifestyle • Inner Game",
    card("REFRAME", "It’s Not What Happens, It’s How You Read It",
         "Two people hit the same traffic jam: one fumes, one catches up on a podcast. "
         "The event is identical; the story you tell about it is the part you control "
         "— and the story decides how it feels."),
    card("GRATITUDE", "Name Three Good Things",
         "A nightly habit of naming three things that went right rewires attention "
         "toward what’s working. It’s nearly free and quietly powerful against a brain "
         "wired to dwell on threats."),
    card("PERSPECTIVE", "This Too Shall Pass",
         "Good times and hard times are both weather, not climate. Remembering that "
         "keeps you humble in the highs and hopeful in the lows. A smooth sea never "
         "made a skilled sailor."),
    card("GROWTH", "Add the Word “Yet”",
         "“I can’t do this” becomes “I can’t do this <em>yet</em>.” Skills are built, "
         "not bestowed — the expert was once a beginner who didn’t quit. Struggle is "
         "the feeling of learning happening."),
    tbl(["Proverb", "The Lesson"],
        [["Measure twice, cut once", "A little planning prevents big waste"],
         ["Give a man a fish…", "Teaching beats doing-for, long term"],
         ["Best time to plant a tree was 20 yrs ago…", "The second best time is now — start"],
         ["Don’t let perfect be the enemy of good", "Shipping beats stalling"]])
  ),
]

DOMAINS = [
  dict(name="Networking", sentinel="<!-- BEGINNER2-NET v1 -->",   topics=NET2,
       anchors=["<!-- /domain-body net -->"]),
  dict(name="Security",   sentinel="<!-- BEGINNER2-SEC v1 -->",   topics=SEC2,
       anchors=["<!-- /domain-body sec -->"]),
  dict(name="Linux",      sentinel="<!-- BEGINNER2-LINUX v1 -->", topics=LINUX2,
       anchors=["<!-- /domain-body linux -->"]),
  dict(name="Script",     sentinel="<!-- BEGINNER2-SCRIPT v1 -->",topics=SCRIPT2,
       anchors=["<!-- /domain-body script -->"]),
  dict(name="Lifestyle",  sentinel="<!-- BEGINNER2-LIFE v1 -->",  topics=LIFE2,
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
    print("BEGINNER-CONCEPTS-V2 patch —", "WRITE" if write else "DRY-RUN (add --write to apply)")
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
        print("\nLooks right? Apply with:  python3 patch_beginner_concepts_v2.py --write")

if __name__ == "__main__":
    main()
