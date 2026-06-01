#!/usr/bin/env python3
"""Inject beginner-friendly "explain it like I'm new to IT" concepts into every
domain, plus a large Programming-from-Zero expansion in the Scripting domain and
a Mental Models / folk-wisdom topic in Lifestyle.

Each domain gets its own sentinel so the patch is idempotent and safe to re-run.
DRY-RUN by default; pass --write to apply (creates a .bak backup of index.html).
Run from the project root, or point at a folder with --dir PATH.
"""
import sys, os, shutil

# ---- builders (same conventions as the other patch scripts) --------------
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
# NET — Networking for absolute beginners
# =========================================================================
NET = [
  topic("🧒", "Networking for Absolute Beginners", "Net+ • Start Here",
    card("BIG IDEA", "What Is a Network?",
         "A network is just two or more computers that can talk to each other. "
         "Your home Wi-Fi is a small network; the Internet is the giant network "
         "that connects all the small ones together. If computers are houses, the "
         "network is the system of roads between them."),
    card("ANALOGY", "IP Address = Mailing Address",
         "Every device on a network has an IP address (e.g., 192.168.1.10) so data "
         "knows where to go — exactly like a street address tells the mail carrier "
         "which house. No address, no delivery."),
    card("ANALOGY", "Packets = Envelopes",
         "Big files are chopped into small chunks called packets. Each packet is an "
         "envelope with a from-address, a to-address, and a piece of the message. "
         "They travel separately and get reassembled at the other end."),
    card("ANALOGY", "Ports = Apartment Numbers",
         "One device (one IP) runs many programs at once. A port number says which "
         "program the data is for — like an apartment number after the street address. "
         "Web pages use port 80/443, email and other services use their own."),
    card("ROLES", "Client vs. Server",
         "The client asks (your phone opening a website); the server answers (the "
         "computer that stores that website). Most of what you do online is a polite "
         "back-and-forth of requests and responses."),
    card("HARDWARE", "Router vs. Switch",
         "A switch connects devices inside one network (like hallways in a building). "
         "A router connects different networks together and finds the path between "
         "them (like roads between cities). Your home box is usually both in one."),
    card("ANALOGY", "DNS = The Phonebook",
         "Humans remember names (google.com); computers need numbers (an IP). DNS is "
         "the phonebook that looks up the name and returns the number, automatically, "
         "every time you click a link."),
    tbl(["Beginner Term", "Plain-English Meaning"],
        [["Bandwidth", "How wide the pipe is — how much data fits per second"],
         ["Latency", "How long one trip takes — the delay / 'lag'"],
         ["LAN", "Local network — your home or office"],
         ["WAN", "Wide network — connects distant sites; the Internet is the biggest"],
         ["Wi-Fi", "A network with no cables — radio instead of wires"],
         ["Firewall", "A guard that decides which traffic is allowed in or out"]])
  ),
]

# =========================================================================
# SEC — Security basics in plain English
# =========================================================================
SEC = [
  topic("🧒", "Security Basics in Plain English", "Sec+ • Start Here",
    card("BIG IDEA", "The CIA Triad (No Spies Involved)",
         "Security protects three things. Confidentiality = only the right people can "
         "see it (a sealed letter). Integrity = nobody changed it secretly (a tamper "
         "seal). Availability = it's there when you need it (the door is unlocked for "
         "you). Almost every security idea protects one of these three."),
    card("ANALOGY", "Authentication vs. Authorization",
         "Authentication proves who you are (showing your ID at the door). "
         "Authorization decides what you're allowed to do once inside (your key only "
         "opens certain rooms). You authenticate first, then you're authorized."),
    card("ANALOGY", "Encryption = a Locked Box",
         "Encryption scrambles data so only someone with the key can read it. Picture "
         "putting a note in a locked box: anyone can carry the box, but only the "
         "key-holder can open it. That's why 'https' sites are safer."),
    card("HABIT", "Passwords → Passphrases + MFA",
         "Long beats complicated: 'correct-horse-battery-staple' is stronger and "
         "easier than 'P@ss1'. Multi-factor authentication (MFA) adds a second proof "
         "(a code on your phone) so a stolen password alone isn't enough."),
    card("MINDSET", "Least Privilege",
         "Give people (and programs) only the access they truly need — nothing extra. "
         "The new intern doesn't get the master key. Less access means less damage if "
         "an account is ever stolen."),
    card("STREET-SMART", "Spotting Phishing",
         "Phishing is a fake message that tricks you into clicking or typing a "
         "password. Red flags: urgency ('act now!'), odd sender addresses, surprise "
         "links, and requests for credentials. When unsure, don't click — verify "
         "through a channel you trust."),
    tbl(["You Hear…", "It Really Means…"],
        [["Vulnerability", "A weakness (an unlocked window)"],
         ["Threat", "Something that could exploit it (a burglar)"],
         ["Risk", "The chance it actually hurts you (likelihood × impact)"],
         ["Zero Trust", "Verify everyone every time — assume nothing is safe by default"],
         ["Hardening", "Closing doors you don't use to shrink the target"]])
  ),
]

# =========================================================================
# THREAT — Threats explained simply
# =========================================================================
THREAT = [
  topic("🧒", "Threats Explained Simply", "Sec+ • Start Here",
    card("BIG IDEA", "Malware = Digital Germs",
         "Malware is any software built to harm or steal. Like germs, some spreads on "
         "its own, some needs you to 'touch' it (open a file), and good hygiene "
         "(updates, caution, antivirus) prevents most infections."),
    card("FIELD GUIDE", "Virus vs. Worm vs. Trojan",
         "A virus attaches to a file and spreads when you run it. A worm copies itself "
         "across the network with no help. A trojan pretends to be something good (a "
         "free game) but smuggles in something bad — named after the wooden horse."),
    card("ANALOGY", "Vulnerability → Exploit → Threat",
         "The unlocked window is the vulnerability. Climbing through it is the exploit. "
         "The burglar who does it is the threat actor. Fixing the lock (patching) "
         "removes the opportunity."),
    card("HUMAN HACKING", "Social Engineering",
         "The easiest way past a strong lock is to trick someone into opening it. "
         "Social engineering hacks people, not machines — impersonation, fake "
         "urgency, flattery, or pretending to be IT support. Skepticism is a control."),
    card("MODERN THREAT", "Ransomware",
         "Ransomware locks your files with encryption and demands payment for the key. "
         "The best defense isn't paying — it's good, tested backups kept offline, so "
         "you can restore and walk away."),
    tbl(["Trick", "How to Not Fall for It"],
        [["Phishing email", "Check the sender; hover links; never rush"],
         ["Tailgating", "Don't hold secure doors for strangers"],
         ["Pretexting", "Verify identity before sharing info"],
         ["Baiting (free USB)", "Never plug in found devices"],
         ["Pop-up 'virus' alert", "Close it; real AV doesn't cold-call you"]])
  ),
]

# =========================================================================
# GRC — Risk & rules in plain English
# =========================================================================
GRC = [
  topic("🧒", "Risk &amp; Rules in Plain English", "GRC • Start Here",
    card("BIG IDEA", "What Is Risk?",
         "Risk = how likely something bad is × how badly it would hurt. Crossing a "
         "quiet street is low risk; crossing a highway blindfolded is high. Security "
         "work is mostly about lowering one or both of those numbers."),
    card("THE FOUR CHOICES", "How to Handle Risk",
         "You can Accept it (live with a small chance), Avoid it (don't do the risky "
         "thing), Transfer it (buy insurance so someone else pays), or Mitigate it "
         "(add controls to shrink it). Everyday life uses all four."),
    card("ANALOGY", "Policy vs. Standard vs. Procedure",
         "A policy is the rule ('we drive safely'). A standard is the specific "
         "requirement ('wear seatbelts'). A procedure is the step-by-step ('click, "
         "pull, buckle'). Together they turn good intentions into repeatable action."),
    card("WHY IT EXISTS", "Compliance Isn't Just Paperwork",
         "Compliance means following laws and standards (like HIPAA for health data). "
         "It feels like red tape, but the rules usually exist because someone got hurt "
         "before they existed. 'Compliant' is the floor, not the ceiling, of security."),
    tbl(["Term", "Plain-English Meaning"],
        [["Governance", "Who decides the rules and makes sure they're followed"],
         ["Asset", "Anything worth protecting (data, devices, people)"],
         ["Control", "A safeguard that lowers risk (a lock, a backup, a policy)"],
         ["Audit", "An outside check that you actually do what you say"],
         ["Defense-in-depth", "Many layers, so one failure isn't game over"]])
  ),
]

# =========================================================================
# OPS — Security operations for beginners
# =========================================================================
OPS = [
  topic("🧒", "Security Operations for Beginners", "CySA+ • Start Here",
    card("BIG IDEA", "What a SOC Does",
         "A Security Operations Center (SOC) is the team that watches the screens — "
         "like a building's security guards reviewing cameras 24/7. They notice odd "
         "activity, investigate, and respond before small problems become big ones."),
    card("ANALOGY", "Logs = a Diary",
         "Every device keeps logs: a timestamped diary of what happened (who logged "
         "in, what failed, what changed). When something goes wrong, the logs are the "
         "story you read back to find out how and when."),
    card("ANALOGY", "Alerts &amp; False Alarms",
         "Monitoring tools raise alerts the way a smoke detector beeps. Some are real "
         "fires; many are burnt toast (false positives). A big part of the job is "
         "tuning the detector so it cries wolf less."),
    card("PROCESS", "Incident Response, Simply",
         "When something bad happens: Prepare → Identify → Contain (stop the bleeding) "
         "→ Eradicate (remove the cause) → Recover (get back to normal) → Lessons "
         "Learned (so it doesn't happen twice). Calm, ordered steps beat panic."),
    card("MINDSET", "Assume Breach &amp; Back Up",
         "Mature teams assume an attacker will get in eventually, so they limit damage "
         "and keep tested backups. A backup you've never restored is just a hope — "
         "practice the recovery before you need it."),
    tbl(["Tool / Term", "What It's For"],
        [["SIEM", "Collects all the logs in one searchable place"],
         ["EDR", "Watches each computer for bad behavior"],
         ["Playbook", "A pre-written recipe for handling an incident"],
         ["Triage", "Sorting alerts by how urgent they are"],
         ["Forensics", "Carefully gathering evidence after the fact"]])
  ),
]

# =========================================================================
# PENTEST — Ethical hacking 101
# =========================================================================
PENTEST = [
  topic("🧒", "Ethical Hacking 101", "PenTest+ • Start Here",
    card("BIG IDEA", "What Is a Penetration Test?",
         "A pentest is hiring someone to break into your systems on purpose — with "
         "permission — to find the holes before a real attacker does. Think of a hotel "
         "paying a locksmith to test every lock and report which ones are weak."),
    card("THE LINE", "Permission Is Everything",
         "The only difference between a penetration tester and a criminal is written "
         "authorization and scope. Same tools, same techniques — but one has a signed "
         "'get-out-of-jail' agreement saying exactly what they're allowed to touch."),
    card("STYLES", "Black / Gray / White Box",
         "Black-box = the tester knows nothing (like a real outsider). White-box = "
         "they get full details and source (a thorough inside review). Gray-box is in "
         "between. More knowledge = deeper testing in less time."),
    card("MINDSET", "Think Like an Attacker",
         "Hacking is mostly curiosity plus stubbornness: 'What happens if I do the "
         "unexpected?' Testers chain small, boring weaknesses into one big problem — "
         "which is exactly why defenders should fix the 'small' stuff."),
    tbl(["Phase", "In Plain English"],
        [["Recon", "Quietly learn everything public about the target"],
         ["Scanning", "Knock on doors to see what's open"],
         ["Exploitation", "Use a weakness to get in"],
         ["Post-exploit", "See how far you can reach once inside"],
         ["Reporting", "Write up findings + how to fix them — the real product"]])
  ),
]

# =========================================================================
# LINUX — Linux for newcomers
# =========================================================================
LINUX = [
  topic("🧒", "Linux for Newcomers", "Linux+ • Start Here",
    card("BIG IDEA", "What Is an Operating System?",
         "The OS is the manager between you and the hardware — it hands out memory, "
         "runs programs, and talks to the disk and network. Windows, macOS, and Linux "
         "are all operating systems; Linux runs most of the servers on the Internet."),
    card("ANALOGY", "The Terminal Isn't Scary",
         "The terminal (or shell) is just a text way to give commands instead of "
         "clicking. Typing 'copy this file there' can be faster and more exact than "
         "dragging icons. The blinking prompt is simply asking 'what next?'"),
    card("MENTAL MODEL", "Everything Is a File",
         "In Linux, your documents, your devices, even some settings are all treated "
         "as files in one big tree that starts at / (the root). Learn to move around "
         "that tree and you've learned half of Linux."),
    card("GOTCHA", "Case &amp; Spaces Matter",
         "'Report.txt' and 'report.txt' are different files, and a space can confuse a "
         "command. Beginners trip on this constantly — when something 'isn't found,' "
         "check capitalization and spelling first."),
    tbl(["Command", "Says…", "Like…"],
        [["pwd", "Where am I?", "Checking your current room"],
         ["ls", "What's here?", "Looking around the room"],
         ["cd folder", "Go inside", "Walking through a door"],
         ["cp / mv", "Copy / move", "Duplicating or relocating"],
         ["cat file", "Show contents", "Reading the page out loud"],
         ["man cmd", "Show the manual", "Reading the instructions"]])
  ),
]

# =========================================================================
# AI — AI & ML for beginners
# =========================================================================
AI = [
  topic("🧒", "AI &amp; ML for Beginners", "AI+ • Start Here",
    card("BIG IDEA", "AI vs. Machine Learning",
         "AI is the broad goal: machines doing things that seem smart. Machine "
         "learning is the most common way we get there — instead of writing every "
         "rule, we show the computer thousands of examples and let it find the "
         "pattern, the way a child learns 'dog' from seeing many dogs."),
    card("ANALOGY", "Training vs. Inference",
         "Training is studying for the test (slow, done once, needs lots of examples). "
         "Inference is taking the test (fast, done every time you use it). A finished, "
         "trained model is like a graduate answering questions from what it learned."),
    card("PLAIN", "What Is a 'Model'?",
         "A model is the pattern the computer learned, frozen into math. You give it "
         "an input (a photo) and it gives a best-guess output (‘cat’). It is "
         "confident-sounding but not conscious — it predicts, it doesn't 'know.'"),
    card("RULE OF THUMB", "Garbage In, Garbage Out",
         "A model is only as good as its examples. Biased or messy training data → "
         "biased or messy answers. This is why cleaning and choosing data is most of "
         "the real work in ML."),
    card("HEADS-UP", "Hallucination",
         "When an AI doesn't know, it may invent a fluent, confident, wrong answer — "
         "called a hallucination. Treat AI output like advice from a fast, well-read "
         "intern: useful, but check anything that matters."),
    tbl(["Buzzword", "Beginner Translation"],
        [["Prompt", "The instructions/question you give the AI"],
         ["Token", "A small chunk of text the model reads/writes"],
         ["LLM", "Large Language Model — predicts the next word very well"],
         ["Neural network", "Layers of simple math loosely inspired by brain cells"],
         ["Bias", "Unfair skew baked in from the data"]])
  ),
]

# =========================================================================
# SHORTCUT — universal shortcuts everyone should know
# =========================================================================
SHORTCUT = [
  topic("🧒", "Universal Shortcuts Everyone Should Know", "General • Start Here",
    card("WHY", "Shortcuts Save Hours",
         "Keyboard shortcuts keep your hands on the keys instead of reaching for the "
         "mouse. A second saved a hundred times a day adds up fast. Learn five and "
         "they become muscle memory within a week."),
    card("TIP", "Ctrl on Windows/Linux = ⌘ on Mac",
         "Most shortcuts are identical across apps — only the modifier key changes. "
         "If you know the Windows combo, the Mac one is usually the same with Command "
         "instead of Ctrl."),
    tbl(["Keys (Win/Linux)", "What It Does"],
        [["Ctrl + C / V / X", "Copy / Paste / Cut"],
         ["Ctrl + Z / Y", "Undo / Redo — your safety net"],
         ["Ctrl + A", "Select all"],
         ["Ctrl + S", "Save (do it often!)"],
         ["Ctrl + F", "Find on the page"],
         ["Alt + Tab", "Switch between open apps"],
         ["Ctrl + Shift + T", "Reopen the tab you just closed"],
         ["Win + L", "Lock your screen when you walk away"]])
  ),
]

# =========================================================================
# MILITARY — reading the codes (beginner)
# =========================================================================
MILITARY = [
  topic("🧒", "Reading Military Codes (Beginner)", "MIL • Start Here",
    card("BIG IDEA", "Why the Letters and Numbers?",
         "Militaries need to communicate fast and without confusion. So they "
         "standardize: a letter says which level/branch a staff section is, a number "
         "says its job, and a phonetic alphabet keeps spoken letters from being "
         "misheard over a noisy radio."),
    card("DECODE IT", "Letter + Number",
         "Read the letter, then the number. The letter is the echelon/service (S, G, "
         "J…), the number is the function (1 = people, 2 = intel, 3 = operations…). "
         "So J2 is Joint Intelligence and S4 is unit-level Logistics."),
    card("SPELL IT OUT", "NATO Phonetic Alphabet",
         "To avoid 'B' vs 'D' mix-ups, each letter gets a word: Alpha, Bravo, Charlie, "
         "Delta… 'CAT' becomes 'Charlie-Alpha-Tango.' Pilots, police, and IT support "
         "all borrow this trick for spelling things aloud."),
    card("CLOCK", "24-Hour (Military) Time",
         "No AM/PM confusion: the day runs 0000 to 2359. 1:00 PM is 1300 ('thirteen "
         "hundred'). Subtract 12 from afternoon hours to get back to a 12-hour clock."),
    tbl(["Number", "Staff Function"],
        [["1", "Personnel (people / admin)"],
         ["2", "Intelligence (information)"],
         ["3", "Operations (the mission)"],
         ["4", "Logistics (supply)"],
         ["6", "Communications / Cyber"]])
  ),
]

# =========================================================================
# SCRIPT — Programming from Zero (the big one)
# =========================================================================
SCRIPT = [
  topic("👋", "Programming from Zero — Start Here", "Beginner • Foundations",
    card("BIG IDEA", "What Is Code?",
         "Code is a set of precise instructions you give a computer — like a recipe. "
         "The computer follows it exactly and literally, top to bottom, with zero "
         "common sense. Most 'bugs' are just the computer doing exactly what you said "
         "instead of what you meant."),
    card("PLAIN", "Program vs. Script",
         "A program is any software built from code. A script is a smaller program, "
         "usually run line-by-line to automate a task (rename 1,000 files, back up a "
         "folder). The line is blurry — don't worry about it as a beginner."),
    card("HOW IT RUNS", "Compiled vs. Interpreted",
         "Computers only understand 1s and 0s (machine code). Compiled languages (C, "
         "Go) translate your whole file to machine code once, then run fast. "
         "Interpreted languages (Python, JavaScript, Bash) translate line-by-line as "
         "they run — easier to start with, a little slower."),
    card("DON'T PANIC", "You Don't Memorize It",
         "Nobody remembers every command. Real developers look things up constantly, "
         "read documentation, and copy-adapt examples. The skill isn't memory — it's "
         "breaking a problem into small steps and knowing what to search for."),
    tbl(["Word You'll Hear", "What It Means"],
        [["Syntax", "The grammar/spelling rules of a language"],
         ["Source code", "The human-readable text you write"],
         ["Runtime", "While the program is actually running"],
         ["Compiler / Interpreter", "Translates your code so the CPU can run it"],
         ["IDE / Editor", "The app you write code in (VS Code, etc.)"],
         ["Library", "Pre-written code you borrow instead of reinventing"]])
  ),
  topic("📦", "Variables &amp; Data Types — Storing Information", "Beginner • Core",
    card("ANALOGY", "Variables Are Labeled Boxes",
         "A variable is a named box that holds a value you want to reuse. You put "
         "something in ('age = 30') and later open the box by name. Change the "
         "contents anytime — that's why it's 'variable.'",
         "<span class='com'># Bash</span>\n"
         "name=<span class='str'>\"Sam\"</span>\n"
         "<span class='fn'>echo</span> <span class='str'>\"Hi $name\"</span>\n\n"
         "<span class='com'>// JavaScript</span>\n"
         "<span class='kw'>let</span> name = <span class='str'>\"Sam\"</span>;\n"
         "<span class='fn'>console</span>.log(<span class='str'>`Hi ${name}`</span>);"),
    card("THE BASICS", "Common Data Types",
         "Data comes in flavors and the computer treats each differently. The number "
         "5 and the text “5” look the same to you but not to the computer — "
         "one does math, the other is just characters."),
    tbl(["Type", "Holds", "Example"],
        [["String", "Text", "\"hello\", \"192.168.0.1\""],
         ["Integer", "Whole numbers", "42, -7, 0"],
         ["Float", "Decimal numbers", "3.14, 0.5"],
         ["Boolean", "True or false", "true, false"],
         ["Null / None", "Nothing / empty on purpose", "null, None"],
         ["Array / List", "An ordered collection", "[\"a\", \"b\", \"c\"]"]]),
    card("GOTCHA", "\"5\" + 5 Isn't Always 10",
         "Mixing types causes classic beginner surprises. In JavaScript \"5\" + 5 is "
         "\"55\" (it glues text), while 5 + 5 is 10 (math). When numbers act weird, "
         "check whether they're secretly text.")
  ),
  topic("🔀", "Control Flow — Decisions &amp; Repetition", "Beginner • Core",
    card("DECISIONS", "if / else",
         "An if statement lets code choose a path based on a condition — exactly like "
         "'IF it's raining, take an umbrella, ELSE wear sunglasses.' The condition is "
         "a yes/no (boolean) question.",
         "<span class='com'># Bash</span>\n"
         "<span class='kw'>if</span> [ $age -ge 18 ]; <span class='kw'>then</span>\n"
         "  <span class='fn'>echo</span> <span class='str'>\"Adult\"</span>\n"
         "<span class='kw'>else</span>\n"
         "  <span class='fn'>echo</span> <span class='str'>\"Minor\"</span>\n"
         "<span class='kw'>fi</span>"),
    card("REPETITION", "Loops",
         "A loop repeats steps so you don't copy-paste. A 'for' loop repeats a set "
         "number of times (or once per item); a 'while' loop repeats as long as "
         "something stays true. This is where computers crush humans — tireless "
         "repetition.",
         "<span class='com'>// JavaScript: do something 3 times</span>\n"
         "<span class='kw'>for</span> (<span class='kw'>let</span> i = <span class='num'>1</span>; i &lt;= <span class='num'>3</span>; i++) {\n"
         "  <span class='fn'>console</span>.log(<span class='str'>\"Attempt \"</span> + i);\n"
         "}"),
    card("BUILDING BLOCKS", "Boolean Logic",
         "Conditions combine with AND, OR, NOT. 'Let in IF member AND over-18.' "
         "Comparisons (== equal, != not-equal, &gt; greater, &lt; less) produce the "
         "true/false that decisions and loops run on."),
    card("WATCH OUT", "Infinite Loops",
         "If a while-loop's condition never becomes false, it runs forever and freezes "
         "the program. Always make sure something inside the loop moves it toward the "
         "exit. Ctrl + C stops a runaway script in the terminal.")
  ),
  topic("🧩", "Functions — Reusable Building Blocks", "Beginner • Core",
    card("ANALOGY", "A Function Is a Mini-Recipe",
         "A function is a named block of steps you can run again and again. Define it "
         "once, 'call' it whenever. Like a coffee machine: you press the button (call "
         "it), it does the steps inside, you get coffee (the result)."),
    card("INPUTS &amp; OUTPUTS", "Parameters &amp; Return",
         "Parameters are the inputs you hand in (the beans and water); the return "
         "value is what comes back out (the coffee). Good functions do one clear job "
         "and hand back a result you can use.",
         "<span class='com'>// JavaScript</span>\n"
         "<span class='kw'>function</span> <span class='fn'>add</span>(a, b) {\n"
         "  <span class='kw'>return</span> a + b;\n"
         "}\n"
         "<span class='fn'>add</span>(<span class='num'>2</span>, <span class='num'>3</span>);  <span class='com'>// returns 5</span>"),
    card("WHY BOTHER", "Don't Repeat Yourself (DRY)",
         "If you copy-paste the same five lines in ten places and later need a fix, "
         "you fix it ten times. Put it in a function and you fix it once. Less "
         "copy-paste = fewer bugs.")
  ),
  topic("🗂️", "Data Structures — Lists &amp; Key/Value", "Beginner • Core",
    card("ORDERED", "Arrays / Lists",
         "An array is a numbered shelf of items in order. You grab items by position "
         "— and most languages start counting at 0, so the first item is index 0 "
         "(a famous beginner trip-up).",
         "<span class='com'>// JavaScript</span>\n"
         "<span class='kw'>let</span> fruits = [<span class='str'>\"apple\"</span>, <span class='str'>\"pear\"</span>];\n"
         "fruits[<span class='num'>0</span>];  <span class='com'>// \"apple\"</span>"),
    card("LABELED", "Objects / Dictionaries",
         "When order doesn't matter but labels do, use key→value pairs: look things up "
         "by name instead of number — like a contact card with labeled fields. This is "
         "exactly what JSON is built from.",
         "<span class='com'>// JavaScript object</span>\n"
         "<span class='kw'>let</span> user = {\n"
         "  name: <span class='str'>\"Sam\"</span>,\n"
         "  age:  <span class='num'>30</span>\n"
         "};\n"
         "user.name;  <span class='com'>// \"Sam\"</span>"),
    card("PICK ONE", "Which Do I Use?",
         "Need a sequence you'll loop through? Use a list. Need to look things up by a "
         "name/ID? Use an object/dictionary. You'll nest them constantly — lists of "
         "objects are everywhere in real data.")
  ),
  topic("🐞", "Errors &amp; Debugging — When Things Break", "Beginner • Survival",
    card("REFRAME", "Bugs Are Normal",
         "Every programmer writes bugs every day — the term comes from a real moth "
         "found in a 1947 computer. Errors aren't failure; they're the computer "
         "telling you precisely where it got confused. Read the message; don't fear it."),
    card("SKILL", "Read the Error Message",
         "Error messages usually name the file, the line number, and the problem. "
         "Start at the top, read the actual words, and look up anything unfamiliar. "
         "90% of beginner debugging is simply slowing down to read what it says."),
    card("TECHNIQUE", "Print &amp; Rubber-Duck",
         "Two timeless tricks: (1) print values along the way to see what the code "
         "actually has, not what you assume. (2) Explain the code out loud, line by "
         "line, to a rubber duck — you'll often hear your own mistake."),
    card("METHOD", "Change One Thing at a Time",
         "Debug like a scientist: form one guess, change one thing, test, repeat. "
         "Changing five things at once means you won't know which fixed (or broke) it. "
         "Small steps, frequent saves.")
  ),
  topic("🛠️", "The Workflow &amp; Good Habits", "Beginner • Practice",
    card("THE LOOP", "Edit → Run → Test → Fix",
         "Programming is a tight loop: make a small change, run it, see what happens, "
         "fix, repeat. Tiny iterations beat writing 200 lines and praying. If it "
         "works, save; then change the next small thing."),
    card("PLAN FIRST", "Pseudocode &amp; Decomposition",
         "Before coding, write the steps in plain English (pseudocode), then translate "
         "each line. Break a scary task into boring small ones: 'read file → split "
         "lines → count words → print total.' Small problems are solvable problems."),
    card("BE KIND", "Name Things Clearly + Comment Why",
         "Code is read far more than it's written — usually by future-you. Use names "
         "like totalPrice, not x. Comments should explain WHY, not restate the obvious. "
         "Clear beats clever.",
         "<span class='com'># Good: a name that explains itself</span>\n"
         "<span class='com'># and a comment that adds the reason</span>\n"
         "retry_limit=<span class='num'>3</span>  <span class='com'># API drops ~1 in 5 calls</span>"),
    card("HABIT", "Save Early, Save Often",
         "Save your file constantly (Ctrl + S) and, once you learn Git, commit small "
         "working steps. Losing two hours of work to a crash is a rite of passage you "
         "can skip.")
  ),
  topic("🌿", "Version Control with Git — Save Points", "Beginner • Tooling",
    card("ANALOGY", "Git = Save Points for Code",
         "Git records snapshots of your project over time, like save points in a video "
         "game. Made a mess? Load an earlier save. It also lets a team work on the "
         "same project without overwriting each other."),
    card("THE WORDS", "Repo, Commit, Push, Pull",
         "A repository (repo) is your project folder under Git's watch. A commit is one "
         "saved snapshot with a note. Push uploads your commits (to GitHub); pull "
         "downloads others'. GitHub is the cloud home where repos live and are shared."),
    card("FIRST FLOW", "The Everyday Cycle",
         "The loop you'll use 95% of the time: change files, stage them, commit with a "
         "message, push. Short, frequent commits with clear messages are a gift to "
         "your future self.",
         "<span class='fn'>git</span> add .\n"
         "<span class='fn'>git</span> commit -m <span class='str'>\"Add login form\"</span>\n"
         "<span class='fn'>git</span> push"),
    card("WHY IT MATTERS", "Fearless Experimentation",
         "Because every good state is saved, you can try a wild idea on a 'branch' "
         "knowing you can always get back. Version control turns 'I'm scared to touch "
         "it' into 'let's try and see.'")
  ),
  topic("🔌", "APIs &amp; Data Formats — How Programs Talk", "Beginner • Tooling",
    card("ANALOGY", "An API Is a Waiter",
         "An API (Application Programming Interface) lets one program ask another for "
         "something. You (the app) don't go into the kitchen; you give the waiter (the "
         "API) an order from the menu, and it brings back the dish (the data)."),
    card("REQUEST → RESPONSE", "How a Call Works",
         "Your app sends a request to a web address (endpoint); the server sends back a "
         "response, usually as JSON. A status code rides along: 200 = OK, 404 = not "
         "found, 500 = server broke. You'll learn to read those fast."),
    card("THE FORMAT", "JSON in One Card",
         "JSON is how programs swap data as text — just the objects and lists you "
         "already met: keys, values, {curly braces}, [square brackets]. It's readable "
         "by humans and every language, which is why it's everywhere.",
         "<span class='com'>// A JSON response</span>\n"
         "{\n"
         "  <span class='str'>\"user\"</span>: <span class='str'>\"sam\"</span>,\n"
         "  <span class='str'>\"admin\"</span>: <span class='kw'>true</span>,\n"
         "  <span class='str'>\"roles\"</span>: [<span class='str'>\"read\"</span>, <span class='str'>\"write\"</span>]\n"
         "}")
  ),
]

# =========================================================================
# LIFESTYLE — Mental models & folk wisdom (incl. the three requested sayings)
# =========================================================================
LIFE = [
  topic("🧭", "Mental Models &amp; Folk Wisdom", "Lifestyle • Practical Wisdom",
    card("BOUNDARIES", "“Not my circus, not my monkeys.”",
         "A Polish proverb (<em>nie mój cyrk, nie moje małpy</em>) meaning: "
         "this drama isn’t mine to manage. When a mess belongs to someone else — "
         "their emotions, their choices, their chaos — you can still care without "
         "taking ownership of it. Before leaping in to fix things, ask whose circus "
         "this actually is. It pairs perfectly with the Stoic dichotomy of control: "
         "spend your energy on your own monkeys."),
    card("VERIFY", "“Assume makes an ass out of u and me.”",
         "Break the word apart — <strong>ASS&middot;U&middot;ME</strong> — and it’s "
         "a built-in memory hook: unchecked assumptions end up embarrassing everyone "
         "involved. Don’t fill gaps in what you know with guesses; ask, confirm, "
         "and write it down. In IT especially, assuming ‘someone else handled it’ "
         "or ‘that config is fine’ is how outages are born. Trade “I assumed…” "
         "for “Let me verify…”"),
    card("ACCEPTANCE", "“You can’t make someone make the right choice — but you can pick up the pieces afterward.”",
         "You don’t control other people’s decisions, only your response to them. "
         "Advise, warn, and offer help — then release the outcome, because it was never "
         "yours to steer. And when their choice goes wrong, you can still show up with "
         "grace and help them rebuild. It’s the dichotomy of control plus compassion: "
         "let go of a steering wheel you were never holding, and keep your hands free "
         "to help pick up the pieces."),
    tbl(["Saying", "Core Lesson", "Use It When…"],
        [["Not my circus, not my monkeys", "Healthy boundaries", "You’re tempted to own someone else’s drama"],
         ["Assume = ass / u / me", "Verify, don’t guess", "You catch yourself filling in unknowns"],
         ["Can’t make the right choice…", "Release + compassion", "You’re trying to control another’s decision"]])
  ),
  topic("🧠", "More Models for a Clear Head", "Lifestyle • Decision-Making",
    card("CHARITY", "Hanlon’s Razor",
         "“Never attribute to malice what is adequately explained by carelessness "
         "or a bad day.” Most slights aren’t attacks — they’re someone "
         "rushed, tired, or unaware. Assuming clumsiness over evil lowers your stress "
         "and usually turns out to be correct."),
    card("SIMPLICITY", "Occam’s Razor",
         "When you have competing explanations, start with the simplest one that fits "
         "the facts. The server is probably unplugged before it’s a sophisticated "
         "hacker. Simple guesses are faster to test — rule them out first."),
    card("CONTROL", "The Serenity Principle",
         "Sort every worry into two buckets: things I can change and things I can’t. "
         "Act on the first bucket; make peace with the second. Almost all anxiety comes "
         "from pouring effort into the wrong bucket."),
    card("FOCUS", "Circle of Control",
         "Picture three rings: what you control (your actions), what you influence "
         "(others, by asking), and what you only care about (the weather, the economy). "
         "Push your attention inward toward the center — that’s where your power "
         "actually is."),
    card("PROGRESS", "Done Beats Perfect",
         "Perfectionism is procrastination in a nice outfit. A finished, slightly rough "
         "thing helps people today; a perfect thing that never ships helps no one. Ship "
         "it, then improve it.")
  ),
]

# =========================================================================
# registry
# =========================================================================
DOMAINS = [
  dict(name="Networking", sentinel="<!-- BEGINNER-NET v1 -->",     topics=NET,
       anchors=["<!-- /domain-body net -->"]),
  dict(name="Security",   sentinel="<!-- BEGINNER-SEC v1 -->",     topics=SEC,
       anchors=["<!-- /domain-body sec -->"]),
  dict(name="Threat",     sentinel="<!-- BEGINNER-THREAT v1 -->",  topics=THREAT,
       anchors=["<!-- /domain-body threat -->"]),
  dict(name="GRC",        sentinel="<!-- BEGINNER-GRC v1 -->",     topics=GRC,
       anchors=["<!-- /domain-body grc -->"]),
  dict(name="Ops",        sentinel="<!-- BEGINNER-OPS v1 -->",     topics=OPS,
       anchors=["<!-- /domain-body ops -->"]),
  dict(name="PenTest",    sentinel="<!-- BEGINNER-PENTEST v1 -->", topics=PENTEST,
       anchors=["<!-- /domain-body pentest -->"]),
  dict(name="Linux",      sentinel="<!-- BEGINNER-LINUX v1 -->",   topics=LINUX,
       anchors=["<!-- /domain-body linux -->"]),
  dict(name="AI",         sentinel="<!-- BEGINNER-AI v1 -->",      topics=AI,
       anchors=["<!-- /domain-body ai -->"]),
  dict(name="Script",     sentinel="<!-- BEGINNER-SCRIPT v1 -->",  topics=SCRIPT,
       anchors=["<!-- /domain-body script -->"]),
  dict(name="Shortcut",   sentinel="<!-- BEGINNER-SHORTCUT v1 -->",topics=SHORTCUT,
       anchors=["<!-- /domain-body shortcuts -->", "<!-- /domain-body shortcut -->"]),
  dict(name="Lifestyle",  sentinel="<!-- BEGINNER-LIFE v1 -->",    topics=LIFE,
       anchors=["<!-- /domain-body lifestyle -->"]),
  dict(name="Military",   sentinel="<!-- BEGINNER-MIL v1 -->",     topics=MILITARY,
       anchors=["<!-- /domain-body military -->"]),
]

def patch_html(text):
    report = []
    for d in DOMAINS:
        if d["sentinel"] in text:
            report.append((d["name"], "skip (already injected)")); continue
        hit = next((a for a in d["anchors"] if a in text), None)
        if not hit:
            report.append((d["name"], "ERROR: no anchor (tried " + ", ".join(d["anchors"]) + ")")); continue
        block = d["sentinel"] + "\n" + "\n".join(d["topics"]) + "\n"
        text = text.replace(hit, block + hit, 1)
        report.append((d["name"], f"injected before {hit}"))
    return text, report

def main():
    write = "--write" in sys.argv
    base = sys.argv[sys.argv.index("--dir") + 1] if "--dir" in sys.argv else "."
    ipath = os.path.join(base, "index.html")
    print("BEGINNER-CONCEPTS patch —", "WRITE" if write else "DRY-RUN (add --write to apply)")
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
        print("\nLooks right? Apply with:  python3 patch_beginner_concepts.py --write")

if __name__ == "__main__":
    main()
