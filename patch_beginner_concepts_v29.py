#!/usr/bin/env python3
"""
patch_beginner_concepts_v29.py — Wave 29: Testing strategy & TDD, threat
modeling & secure SDLC, incident command, Linux perf debugging, synthesis.

New sentinels:
  BEGINNER29-SCRIPT v1  — Testing strategy, the test pyramid, TDD
  BEGINNER29-SEC v1     — Threat modeling (STRIDE), secure SDLC, shift-left
  BEGINNER29-OPS v1     — Incident command system, managing major incidents
  BEGINNER29-LINUX v1   — Performance debugging (strace/ltrace/perf/lsof)
  BEGINNER29-LIFE v1    — Synthesis: the craftsperson's mindset, tying it together
"""
from pathlib import Path

SCRIPT_INJECT_ANCHOR = "<!-- /domain-body script -->"
SEC_INJECT_ANCHOR    = "<!-- /domain-body sec -->"
OPS_INJECT_ANCHOR    = "<!-- /domain-body ops -->"
LINUX_INJECT_ANCHOR  = "<!-- /domain-body linux -->"
LIFE_INJECT_ANCHOR   = "<!-- /domain-body lifestyle -->"

# ─────────────────────────────── SCRIPT wave 29 ──────────────────────────────
SCRIPT_SENTINEL = "<!-- BEGINNER29-SCRIPT v1 -->"
SCRIPT_CONTENT = """
<!-- BEGINNER29-SCRIPT v1 -->
<!-- ── TOPIC: TESTING STRATEGY ───────────────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">🧪</span>
    <span class="topic-name">Testing Strategy — Why and How to Test</span>
    <span class="topic-badge">SCRIPT • Professional</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">WHY TEST</div>
      <div class="concept-title">Tests Are Your Safety Net for Change</div>
      <div class="concept-desc">Tests aren't about proving code works once — they're about being able to <em>change</em> code confidently later. Without tests, every change risks silently breaking something elsewhere, so people become afraid to touch the code (it "ossifies"). With a good test suite, you refactor fearlessly: if you break something, a test tells you instantly. Tests are also living documentation of how the code is meant to behave.</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">THE TEST PYRAMID</div>
      <div class="concept-title">Many Fast Tests, Few Slow Ones</div>
      <table class="ai-table">
        <thead><tr><th>Level</th><th>Tests</th><th>Speed</th><th>How Many</th></tr></thead>
        <tbody>
          <tr><td>Unit (base)</td><td>One function/class in isolation</td><td>Milliseconds</td><td>Many (the bulk)</td></tr>
          <tr><td>Integration (middle)</td><td>Components working together (DB, API)</td><td>Slower</td><td>Some</td></tr>
          <tr><td>End-to-end (top)</td><td>Whole system, like a real user</td><td>Slow, flaky</td><td>Few</td></tr>
        </tbody>
      </table>
      <div class="concept-desc">The shape is a pyramid for a reason: lots of fast, reliable unit tests at the base; fewer slow, brittle E2E tests at the top. The "ice cream cone" anti-pattern (mostly slow E2E tests) makes a suite slow and flaky — painful to run, so people stop running it.</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">TDD</div>
      <div class="concept-title">Test-Driven Development — Red, Green, Refactor</div>
      <div class="concept-desc">TDD flips the usual order: write the test <em>first</em>, watch it fail, then write just enough code to pass. It forces you to clarify what the code should do before writing it, and guarantees test coverage. Not everyone does strict TDD, but the cycle is a valuable tool to know.</div>
      <div class="code-block"><span class="com"># 1. RED — write a failing test first</span>
<span class="kw">def</span> <span class="fn">test_celsius_to_fahrenheit</span>():
    <span class="kw">assert</span> c_to_f(<span class="num">100</span>) == <span class="num">212</span>
    <span class="kw">assert</span> c_to_f(<span class="num">0</span>) == <span class="num">32</span>
<span class="com"># Run it → fails (c_to_f doesn't exist yet)</span>

<span class="com"># 2. GREEN — write the minimum to pass</span>
<span class="kw">def</span> <span class="fn">c_to_f</span>(c):
    <span class="kw">return</span> c * <span class="num">9</span>/<span class="num">5</span> + <span class="num">32</span>
<span class="com"># Run it → passes ✓</span>

<span class="com"># 3. REFACTOR — clean up, tests keep you safe</span>
<span class="com"># (add type hints, edge cases, docstring — re-run tests)</span></div>
    </div>
    <div class="concept-card">
      <div class="concept-label">WHAT MAKES A GOOD TEST</div>
      <div class="concept-title">Qualities to Aim For</div>
      <table class="ai-table">
        <thead><tr><th>Quality</th><th>Meaning</th></tr></thead>
        <tbody>
          <tr><td>Fast</td><td>Runs in milliseconds — so you run them constantly</td></tr>
          <tr><td>Isolated</td><td>Doesn't depend on other tests or run order</td></tr>
          <tr><td>Repeatable</td><td>Same result every time (no flakiness, no real network/time)</td></tr>
          <tr><td>Clear failure</td><td>When it fails, you immediately know what broke</td></tr>
          <tr><td>Tests behavior, not implementation</td><td>Survives refactoring; tests what, not how</td></tr>
          <tr><td>Covers edge cases</td><td>Empty, zero, negative, huge, None, unicode</td></tr>
        </tbody>
      </table>
    </div>
  </div>
</div>
"""

# ─────────────────────────────── SEC wave 29 ─────────────────────────────────
SEC_SENTINEL = "<!-- BEGINNER29-SEC v1 -->"
SEC_CONTENT = """
<!-- BEGINNER29-SEC v1 -->
<!-- ── TOPIC: THREAT MODELING & SECURE SDLC ──────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">🗺️</span>
    <span class="topic-name">Threat Modeling — Finding Flaws Before You Build Them</span>
    <span class="topic-badge">SEC • Design</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">SHIFT LEFT</div>
      <div class="concept-title">The Earlier You Catch It, the Cheaper It Is</div>
      <div class="concept-desc">A bug found in design costs almost nothing to fix; the same flaw found in production after a breach costs a fortune (and your reputation). "Shift left" means moving security earlier in the development lifecycle — into design and coding — rather than bolting it on at the end. Threat modeling is the design-phase practice of systematically asking "how could this be attacked?" before a line of code is written.</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">THE FOUR QUESTIONS</div>
      <div class="concept-title">A Simple Threat Modeling Framework</div>
      <table class="ai-table">
        <thead><tr><th>Question</th><th>Activity</th></tr></thead>
        <tbody>
          <tr><td>1. What are we building?</td><td>Diagram the system, data flows, trust boundaries</td></tr>
          <tr><td>2. What can go wrong?</td><td>Brainstorm threats (use STRIDE below)</td></tr>
          <tr><td>3. What are we going to do about it?</td><td>Decide mitigations for each real threat</td></tr>
          <tr><td>4. Did we do a good job?</td><td>Review and validate the model</td></tr>
        </tbody>
      </table>
    </div>
    <div class="concept-card">
      <div class="concept-label">STRIDE</div>
      <div class="concept-title">A Checklist of Threat Categories</div>
      <div class="concept-desc">STRIDE (from Microsoft) is a mnemonic for six categories of threats — run each part of your system through it to find weaknesses. Each threat maps to a security property it violates.</div>
      <table class="ai-table">
        <thead><tr><th>Letter</th><th>Threat</th><th>Violates</th><th>Mitigation</th></tr></thead>
        <tbody>
          <tr><td><strong>S</strong></td><td>Spoofing (pretending to be someone)</td><td>Authentication</td><td>Strong auth, MFA</td></tr>
          <tr><td><strong>T</strong></td><td>Tampering (altering data)</td><td>Integrity</td><td>Hashing, signatures, validation</td></tr>
          <tr><td><strong>R</strong></td><td>Repudiation (denying an action)</td><td>Non-repudiation</td><td>Logging, audit trails, signatures</td></tr>
          <tr><td><strong>I</strong></td><td>Information disclosure (leaks)</td><td>Confidentiality</td><td>Encryption, access control</td></tr>
          <tr><td><strong>D</strong></td><td>Denial of service</td><td>Availability</td><td>Rate limiting, scaling, redundancy</td></tr>
          <tr><td><strong>E</strong></td><td>Elevation of privilege</td><td>Authorization</td><td>Least privilege, input validation</td></tr>
        </tbody>
      </table>
    </div>
    <div class="concept-card">
      <div class="concept-label">SECURE SDLC</div>
      <div class="concept-title">Security at Every Stage</div>
      <table class="ai-table">
        <thead><tr><th>Stage</th><th>Security Activity</th></tr></thead>
        <tbody>
          <tr><td>Requirements</td><td>Define security requirements &amp; abuse cases</td></tr>
          <tr><td>Design</td><td>Threat modeling, secure architecture review</td></tr>
          <tr><td>Code</td><td>Secure coding standards, SAST, peer review</td></tr>
          <tr><td>Build/Test</td><td>DAST, dependency scanning (SCA), secrets scanning</td></tr>
          <tr><td>Deploy</td><td>Hardened configs, IaC scanning, least privilege</td></tr>
          <tr><td>Operate</td><td>Monitoring, patching, pen testing, bug bounty</td></tr>
        </tbody>
      </table>
      <div class="concept-desc">Embedding these (often called DevSecOps) makes security continuous and shared — "everyone's responsibility" — rather than a gate at the end that slows everyone down.</div>
    </div>
  </div>
</div>
"""

# ─────────────────────────────── OPS wave 29 ─────────────────────────────────
OPS_SENTINEL = "<!-- BEGINNER29-OPS v1 -->"
OPS_CONTENT = """
<!-- BEGINNER29-OPS v1 -->
<!-- ── TOPIC: INCIDENT COMMAND ───────────────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">🧯</span>
    <span class="topic-name">Incident Command — Running a Major Incident Without Chaos</span>
    <span class="topic-badge">OPS • Critical</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">WHY STRUCTURE</div>
      <div class="concept-title">Big Incidents Fail on Coordination, Not Tech</div>
      <div class="concept-desc">In a major incident, the technical problem is often not the hardest part — coordination is. Without structure you get chaos: everyone debugging the same thing, no one talking to stakeholders, conflicting changes, decision paralysis. Tech companies borrowed the <strong>Incident Command System (ICS)</strong> from emergency services (firefighters) to bring order. The key idea: assign clear roles so the responders can focus while someone else coordinates and communicates.</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">THE ROLES</div>
      <div class="concept-title">Who Does What in a Major Incident</div>
      <table class="ai-table">
        <thead><tr><th>Role</th><th>Responsibility</th></tr></thead>
        <tbody>
          <tr><td>Incident Commander (IC)</td><td>Coordinates the response, makes decisions, owns the incident. Does NOT fix — directs. The single point of accountability.</td></tr>
          <tr><td>Operations / Responders</td><td>The hands-on engineers actually investigating and fixing</td></tr>
          <tr><td>Communications Lead</td><td>Updates stakeholders, status page, customers — frees the IC to lead</td></tr>
          <tr><td>Scribe</td><td>Maintains the timeline of what happened and when (gold for the post-mortem)</td></tr>
          <tr><td>Subject Matter Experts</td><td>Pulled in as needed for specific systems</td></tr>
        </tbody>
      </table>
      <div class="concept-desc">In a small incident one person may wear several hats — but even then, <em>declaring</em> who is IC prevents the "everyone assumes someone else has it" failure.</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">RUNNING IT</div>
      <div class="concept-title">The Flow of a Well-Managed Incident</div>
      <table class="ai-table">
        <thead><tr><th>Phase</th><th>Action</th></tr></thead>
        <tbody>
          <tr><td>Declare</td><td>Call it an incident, assign an IC, open a dedicated channel/bridge</td></tr>
          <tr><td>Assess</td><td>Establish severity &amp; impact; who/what is affected</td></tr>
          <tr><td>Mitigate</td><td>Restore service first (workarounds OK); root cause can wait</td></tr>
          <tr><td>Communicate</td><td>Regular updates — internal + external; silence breeds panic</td></tr>
          <tr><td>Resolve</td><td>Confirm service restored &amp; stable</td></tr>
          <tr><td>Review</td><td>Blameless post-mortem; turn lessons into action items</td></tr>
        </tbody>
      </table>
    </div>
    <div class="concept-card">
      <div class="concept-label">GOLDEN RULES</div>
      <div class="concept-title">Hard-Won Incident Wisdom</div>
      <div class="concept-desc"><strong>Restore first, diagnose later</strong> — users want service back, not your root-cause theory. <strong>One person changes things at a time</strong> — coordinate through the IC to avoid conflicting fixes that make it worse. <strong>Communicate more than feels necessary</strong> — stakeholders fill silence with worst-case assumptions. <strong>It's OK to escalate / wake people up</strong> — a prolonged outage costs far more than someone's sleep. And recall the mindset thread: stay calm, work the process, own what's yours, and don't let panic (or blame) drive decisions. The calm, structured responder is worth ten frantic geniuses.</div>
    </div>
  </div>
</div>
"""

# ─────────────────────────────── LINUX wave 29 ───────────────────────────────
LINUX_SENTINEL = "<!-- BEGINNER29-LINUX v1 -->"
LINUX_CONTENT = """
<!-- BEGINNER29-LINUX v1 -->
<!-- ── TOPIC: PERFORMANCE DEBUGGING ──────────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">🔬</span>
    <span class="topic-name">Performance Debugging — When You Need to Go Deeper</span>
    <span class="topic-badge">LINUX • Advanced</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">BEYOND top</div>
      <div class="concept-title">Tools for "Why Is This Process Doing That?"</div>
      <div class="concept-desc">When the basic tools (top, free, df) tell you <em>which</em> process is misbehaving but not <em>why</em>, Linux has powerful introspection tools. These let you see exactly what a running process is doing — which system calls it makes, which files it touches, where it's stuck.</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">STRACE & LTRACE</div>
      <div class="concept-title">Watch a Process Talk to the Kernel</div>
      <div class="concept-desc"><code>strace</code> traces system calls (a process's requests to the kernel — open files, read, write, network). It's invaluable for "why is this hanging?" or "what file is it failing to find?" <code>ltrace</code> does the same for library calls.</div>
      <div class="code-block"><span class="com"># Trace system calls of a command</span>
strace ls /tmp

<span class="com"># Attach to a RUNNING process (find why it's stuck)</span>
sudo strace -p 12345

<span class="com"># Only file-related calls — "what file can't it find?"</span>
strace -e trace=open,openat,stat myprogram

<span class="com"># Count syscalls + time spent (find the bottleneck)</span>
strace -c myprogram

<span class="com"># Classic use: a program fails silently → strace reveals</span>
<span class="com"># ENOENT (missing file) or EACCES (permission denied)</span></div>
    </div>
    <div class="concept-card">
      <div class="concept-label">LSOF & FUSER</div>
      <div class="concept-title">Who Has That File/Port Open?</div>
      <div class="code-block"><span class="com"># What files does a process have open?</span>
lsof -p 12345

<span class="com"># Which process is using a port? (the classic "port in use")</span>
sudo lsof -i :8080
sudo ss -tlnp | grep 8080

<span class="com"># Why can't I unmount this disk? What's using it?</span>
lsof +D /mnt/data
fuser -m /mnt/data

<span class="com"># Find deleted-but-still-open files eating disk space</span>
lsof | grep deleted        <span class="com"># common cause of "df full but du not"</span></div>
    </div>
    <div class="concept-card">
      <div class="concept-label">DEEPER TOOLS</div>
      <div class="concept-title">When You Need the Heavy Artillery</div>
      <table class="ai-table">
        <thead><tr><th>Tool</th><th>Use</th></tr></thead>
        <tbody>
          <tr><td><code>vmstat 1</code></td><td>System-wide CPU/memory/IO/swap, refreshed each second</td></tr>
          <tr><td><code>iostat -x 1</code></td><td>Per-disk I/O — find the saturated disk (%util)</td></tr>
          <tr><td><code>perf top</code></td><td>Real-time CPU profiling — which functions burn CPU</td></tr>
          <tr><td><code>pidstat 1</code></td><td>Per-process resource use over time</td></tr>
          <tr><td>eBPF tools (bcc/bpftrace)</td><td>Deep, low-overhead kernel observability (modern frontier)</td></tr>
          <tr><td>Flame graphs</td><td>Visualize where CPU time goes across the call stack</td></tr>
        </tbody>
      </table>
      <div class="concept-desc"><strong>Methodology beats tools:</strong> recall the USE method — for each resource check Utilization, Saturation, Errors. Start broad (which resource?), then reach for these tools to drill into the specific process. Don't randomly run tools hoping for an answer.</div>
    </div>
  </div>
</div>
"""

# ─────────────────────────────── LIFESTYLE wave 29 ───────────────────────────
LIFE_SENTINEL = "<!-- BEGINNER29-LIFE v1 -->"
LIFE_CONTENT = """
<!-- BEGINNER29-LIFE v1 -->
<!-- ── TOPIC: THE CRAFTSPERSON'S MINDSET ─────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">🧗</span>
    <span class="topic-name">The Craftsperson's Mindset — Tying It All Together</span>
    <span class="topic-badge">LIFESTYLE • Synthesis</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">FROM BEGINNER TO PROFESSIONAL</div>
      <div class="concept-title">It's a Way of Working, Not a Finish Line</div>
      <div class="concept-desc">Everything in this guide — networking, code, security, Linux, the war stories and the wisdom — adds up to something bigger than a pile of facts. It's a way of approaching work: with curiosity, rigor, humility, and care. You will never "finish" learning IT; the field reinvents itself every few years. The professionals who thrive aren't the ones who know everything — they're the ones who've built a durable <em>way of thinking</em> that lets them learn whatever comes next. That mindset is the real skill.</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">THE TECHNICAL HABITS</div>
      <div class="concept-title">What Separates Pros From Beginners</div>
      <table class="ai-table">
        <thead><tr><th>Habit</th><th>In Practice</th></tr></thead>
        <tbody>
          <tr><td>Understand, don't memorize</td><td>Know WHY, and you can derive the how anywhere</td></tr>
          <tr><td>Read the error message</td><td>It's usually telling you the answer — actually read it</td></tr>
          <tr><td>Reproduce before fixing</td><td>You can't fix what you can't reliably trigger</td></tr>
          <tr><td>Change one thing at a time</td><td>Otherwise you never know what worked</td></tr>
          <tr><td>Automate the third repetition</td><td>Toil compounds; so does the automation that kills it</td></tr>
          <tr><td>Leave it better than you found it</td><td>Fix the doc, add the test, clean the config</td></tr>
        </tbody>
      </table>
    </div>
    <div class="concept-card">
      <div class="concept-label">THE THREE MINDSETS, REVISITED</div>
      <div class="concept-title">The Wisdom That Holds It All Together</div>
      <div class="concept-desc">Three sayings recur throughout this guide because they apply to nearly every situation a technical professional faces — across every domain, from your first help-desk ticket to running a major incident decades later:</div>
      <table class="ai-table">
        <thead><tr><th>Saying</th><th>What It Protects</th><th>Where It Shows Up</th></tr></thead>
        <tbody>
          <tr><td><strong>"Assume makes an ass of u and me"</strong></td><td>Your technical rigor</td><td>Verify the backup, test the change, check the logs, confirm the firewall rule — never assume</td></tr>
          <tr><td><strong>"Not my circus, not my monkeys"</strong></td><td>Your energy &amp; boundaries</td><td>Own what's yours fully; support (don't absorb) what isn't; escalate rather than silently carry others' dysfunction</td></tr>
          <tr><td><strong>"You can't make someone make the right choice — but you can pick up the pieces"</strong></td><td>Your sanity &amp; reputation</td><td>Advise clearly in writing, accept the decision isn't yours, then be the calm one who helps recover — no "I told you so"</td></tr>
        </tbody>
      </table>
    </div>
    <div class="concept-card">
      <div class="concept-label">THE LONG VIEW</div>
      <div class="concept-title">Build a Career You Can Sustain</div>
      <div class="concept-desc">Technical skill gets you in the door; judgment, communication, and integrity build the career. Stay curious — the learning never stops, and that's a feature, not a bug. Be generous with knowledge; teaching others cements your own understanding and your reputation compounds. Protect your health, relationships, and focus — a burned-out expert helps no one, and "not my monkeys" exists precisely so you don't carry weight that isn't yours. Verify relentlessly, communicate clearly, document your reasoning, stay calm when others panic, and keep learning. Do that, and you'll not only survive in IT — you'll become the steady professional others rely on, for decades. That's the whole game.</div>
    </div>
  </div>
</div>
"""

# ─────────────────────────────── INJECT LOGIC ────────────────────────────────
def inject(html: str, anchor: str, sentinel: str, content: str) -> tuple[str, bool]:
    if sentinel in html:
        return html, False
    pos = html.find(anchor)
    if pos == -1:
        return html, False
    return html[:pos] + content + html[pos:], True

def main():
    path = Path("index.html")
    html = path.read_text(encoding="utf-8")

    injections = [
        (SCRIPT_INJECT_ANCHOR, SCRIPT_SENTINEL, SCRIPT_CONTENT),
        (SEC_INJECT_ANCHOR,    SEC_SENTINEL,    SEC_CONTENT),
        (OPS_INJECT_ANCHOR,    OPS_SENTINEL,    OPS_CONTENT),
        (LINUX_INJECT_ANCHOR,  LINUX_SENTINEL,  LINUX_CONTENT),
        (LIFE_INJECT_ANCHOR,   LIFE_SENTINEL,   LIFE_CONTENT),
    ]

    for anchor, sentinel, content in injections:
        new_html, changed = inject(html, anchor, sentinel, content)
        if changed:
            added = len(new_html) - len(html)
            html = new_html
            print(f"  [ok] Injected +{added:,} chars before '{anchor}' in index.html")
        else:
            label = anchor.replace("<!-- /domain-body ", "").replace(" -->", "")
            print(f"  [--] Skipped '{label}' (already present)")

    path.write_text(html, encoding="utf-8")

    from html.parser import HTMLParser
    class TagChecker(HTMLParser):
        VOID = {"area","base","br","col","embed","hr","img","input",
                "link","meta","param","source","track","wbr"}
        def __init__(self):
            super().__init__()
            self.stack = []
            self.errors = []
        def handle_starttag(self, tag, attrs):
            if tag not in self.VOID:
                self.stack.append(tag)
        def handle_endtag(self, tag):
            if tag in self.VOID:
                return
            if self.stack and self.stack[-1] == tag:
                self.stack.pop()
            else:
                self.errors.append(f"Stray </{tag}>")

    checker = TagChecker()
    checker.feed(html)
    print(f"\n  Unclosed at EOF: {', '.join(checker.stack) if checker.stack else 'NONE'}")
    print(f"  Stray end tags: {len(checker.errors)}")
    print(f"\n  index.html: {len(html):,} bytes")

if __name__ == "__main__":
    main()
