#!/usr/bin/env python3
"""
patch_beginner_concepts_v17.py — Wave 17: Subnetting math, ML fundamentals,
ITIL/service management, Python data & dates, Git deeper.

New sentinels:
  BEGINNER17-NET v1     — Subnetting deep dive (CIDR, binary, calculating subnets)
  BEGINNER17-AI v1      — Machine learning fundamentals, training vs inference
  BEGINNER17-OPS v1     — ITIL, service management, change/problem management
  BEGINNER17-SCRIPT v1  — Dates/times, working with data (pandas intro)
  BEGINNER17-SHORTCUT v1 — Git power user, rebasing, stashing, bisect
"""
from pathlib import Path

NET_INJECT_ANCHOR      = "<!-- /domain-body net -->"
AI_INJECT_ANCHOR       = "<!-- /domain-body ai -->"
OPS_INJECT_ANCHOR      = "<!-- /domain-body ops -->"
SCRIPT_INJECT_ANCHOR   = "<!-- /domain-body script -->"
SHORTCUT_INJECT_ANCHOR = "<!-- /domain-body shortcuts -->"

# ─────────────────────────────── NET wave 17 ─────────────────────────────────
NET_SENTINEL = "<!-- BEGINNER17-NET v1 -->"
NET_CONTENT = """
<!-- BEGINNER17-NET v1 -->
<!-- ── TOPIC: SUBNETTING ─────────────────────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">🧮</span>
    <span class="topic-name">Subnetting — The Math That Scares Beginners (It Shouldn't)</span>
    <span class="topic-badge">NET • Foundation</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">WHAT IS SUBNETTING</div>
      <div class="concept-title">Dividing a Network Into Smaller Networks</div>
      <div class="concept-desc">An IP address has two parts: a <strong>network portion</strong> (which network you're on) and a <strong>host portion</strong> (which specific device). Subnetting is the art of deciding where to draw that line — splitting a big address block into smaller, organized chunks. Why? Security (isolate departments), efficiency (reduce broadcast traffic), and organization. It intimidates beginners, but it's just binary math you can learn in an afternoon.</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">CIDR NOTATION</div>
      <div class="concept-title">The /24 Explained</div>
      <div class="concept-desc">An IPv4 address is 32 bits. CIDR (Classless Inter-Domain Routing) notation like <code>192.168.1.0/24</code> means "the first 24 bits are the network portion." The remaining bits (32 − 24 = 8) are for hosts. More network bits = smaller subnet = fewer hosts.</div>
      <div class="code-block"><span class="com"># 192.168.1.0/24 in binary</span>
192.168.1.0
11000000.10101000.00000001.00000000
└──────── 24 network bits ────────┘└8 host┘

<span class="com"># The /24 tells you the subnet mask</span>
/24 = 255.255.255.0
<span class="com"># (24 ones, then 8 zeros)</span>
11111111.11111111.11111111.00000000</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">THE KEY FORMULAS</div>
      <div class="concept-title">Hosts and Subnets — Memorize These</div>
      <div class="code-block"><span class="com"># Number of usable hosts per subnet</span>
usable hosts = 2^(host bits) − 2
<span class="com"># (subtract 2: network address + broadcast address)</span>

<span class="com"># Example: /24 has 8 host bits</span>
2^8 − 2 = 256 − 2 = 254 usable hosts

<span class="com"># Example: /26 has 6 host bits</span>
2^6 − 2 = 64 − 2 = 62 usable hosts

<span class="com"># Number of subnets when you "borrow" bits</span>
subnets = 2^(borrowed bits)</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">CIDR CHEAT SHEET</div>
      <div class="concept-title">Common Prefixes at a Glance</div>
      <table class="ai-table">
        <thead><tr><th>CIDR</th><th>Subnet Mask</th><th>Host Bits</th><th>Usable Hosts</th><th>Block Size</th></tr></thead>
        <tbody>
          <tr><td>/30</td><td>255.255.255.252</td><td>2</td><td>2</td><td>4 (point-to-point links)</td></tr>
          <tr><td>/29</td><td>255.255.255.248</td><td>3</td><td>6</td><td>8</td></tr>
          <tr><td>/28</td><td>255.255.255.240</td><td>4</td><td>14</td><td>16</td></tr>
          <tr><td>/27</td><td>255.255.255.224</td><td>5</td><td>30</td><td>32</td></tr>
          <tr><td>/26</td><td>255.255.255.192</td><td>6</td><td>62</td><td>64</td></tr>
          <tr><td>/25</td><td>255.255.255.128</td><td>7</td><td>126</td><td>128</td></tr>
          <tr><td>/24</td><td>255.255.255.0</td><td>8</td><td>254</td><td>256</td></tr>
          <tr><td>/23</td><td>255.255.254.0</td><td>9</td><td>510</td><td>512</td></tr>
          <tr><td>/16</td><td>255.255.0.0</td><td>16</td><td>65,534</td><td>65,536</td></tr>
        </tbody>
      </table>
    </div>
    <div class="concept-card">
      <div class="concept-label">WORKED EXAMPLE</div>
      <div class="concept-title">Finding Network, Broadcast, and Range</div>
      <div class="concept-desc">Given an IP and CIDR, here's how to find the key addresses. This is the most common subnetting question on exams and the job.</div>
      <div class="code-block"><span class="com"># Given: 192.168.1.100/26  — what subnet is it in?</span>

<span class="com"># Step 1: /26 → block size. Host bits = 32-26 = 6. Block = 2^6 = 64</span>
<span class="com"># Step 2: subnets start at multiples of the block size (64):</span>
<span class="com">#   192.168.1.0, .64, .128, .192</span>
<span class="com"># Step 3: .100 falls between .64 and .128 → subnet is .64</span>

Network address:   192.168.1.64    <span class="com"># first address (not usable)</span>
First usable host: 192.168.1.65
Last usable host:  192.168.1.126
Broadcast address: 192.168.1.127   <span class="com"># last address (not usable)</span>
Next subnet:       192.168.1.128

<span class="com"># Shortcut: "block size" trick — count by 64s. Done.</span></div>
    </div>
    <div class="concept-card">
      <div class="concept-label">LET THE COMPUTER DO IT</div>
      <div class="concept-title">Tools That Calculate Subnets For You</div>
      <div class="code-block"><span class="com"># Linux: ipcalc shows everything</span>
ipcalc 192.168.1.100/26
<span class="com"># Address, Netmask, Network, Broadcast, HostMin, HostMax, Hosts/Net</span>

<span class="com"># sipcalc (more detailed)</span>
sipcalc 10.0.0.0/22

<span class="com"># Python — the ipaddress module is built in</span>
python3 -c "import ipaddress; n=ipaddress.ip_network('192.168.1.0/26'); \\
print(n.network_address, n.broadcast_address, n.num_addresses)"

<span class="com"># Python interactive — useful for automation</span>
<span class="kw">import</span> ipaddress
net = ipaddress.ip_network(<span class="str">'192.168.1.0/26'</span>)
<span class="fn">print</span>(net.netmask)            <span class="com"># 255.255.255.192</span>
<span class="fn">print</span>(<span class="fn">list</span>(net.hosts())[<span class="num">0</span>])    <span class="com"># first usable host</span>
<span class="fn">print</span>(net.num_addresses)      <span class="com"># 64</span></div>
    </div>
  </div>
</div>
"""

# ─────────────────────────────── AI wave 17 ──────────────────────────────────
AI_SENTINEL = "<!-- BEGINNER17-AI v1 -->"
AI_CONTENT = """
<!-- BEGINNER17-AI v1 -->
<!-- ── TOPIC: MACHINE LEARNING FUNDAMENTALS ──────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">🧠</span>
    <span class="topic-name">Machine Learning Fundamentals — How Machines "Learn"</span>
    <span class="topic-badge">AI • Foundation</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">THE CORE IDEA</div>
      <div class="concept-title">Programming by Example, Not by Rules</div>
      <div class="concept-desc">Traditional programming: a human writes explicit rules (if spam words, mark as spam). Machine learning flips this: you feed the computer thousands of examples (emails labeled spam/not-spam) and it <em>learns the rules itself</em> by finding patterns. The output is a "model" — a mathematical function that makes predictions on new, unseen data. ML shines where rules are too complex to write by hand (image recognition, fraud detection, language).</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">THE THREE TYPES</div>
      <div class="concept-title">Supervised, Unsupervised, Reinforcement</div>
      <table class="ai-table">
        <thead><tr><th>Type</th><th>Training Data</th><th>Goal</th><th>Examples</th></tr></thead>
        <tbody>
          <tr><td><strong>Supervised</strong></td><td>Labeled (input → known answer)</td><td>Predict the label for new inputs</td><td>Spam detection, fraud detection, image classification, price prediction</td></tr>
          <tr><td><strong>Unsupervised</strong></td><td>Unlabeled (no answers given)</td><td>Find hidden structure/groups</td><td>Customer segmentation, anomaly detection, recommendation</td></tr>
          <tr><td><strong>Reinforcement</strong></td><td>Reward/penalty signals</td><td>Learn optimal actions by trial and error</td><td>Game AI (AlphaGo), robotics, self-driving</td></tr>
        </tbody>
      </table>
    </div>
    <div class="concept-card">
      <div class="concept-label">SUPERVISED: TWO FLAVORS</div>
      <div class="concept-title">Classification vs Regression</div>
      <table class="ai-table">
        <thead><tr><th>Task</th><th>Predicts</th><th>Output</th><th>Example</th></tr></thead>
        <tbody>
          <tr><td>Classification</td><td>A category</td><td>Discrete label</td><td>"Is this login malicious? yes/no"</td></tr>
          <tr><td>Regression</td><td>A number</td><td>Continuous value</td><td>"How many attacks next hour?"</td></tr>
        </tbody>
      </table>
    </div>
    <div class="concept-card">
      <div class="concept-label">TRAINING VS INFERENCE</div>
      <div class="concept-title">The Two Phases of an ML Model's Life</div>
      <table class="ai-table">
        <thead><tr><th>Phase</th><th>What Happens</th><th>Cost</th><th>When</th></tr></thead>
        <tbody>
          <tr><td><strong>Training</strong></td><td>Model learns patterns from data; adjusts internal parameters (weights)</td><td>Expensive (GPUs, hours/days/weeks)</td><td>Done once (or periodically retrained)</td></tr>
          <tr><td><strong>Inference</strong></td><td>Trained model makes predictions on new data</td><td>Cheap, fast (milliseconds)</td><td>Every time you use it (in production)</td></tr>
        </tbody>
      </table>
    </div>
    <div class="concept-card">
      <div class="concept-label">KEY PITFALLS</div>
      <div class="concept-title">Overfitting, Underfitting, and Data Splits</div>
      <div class="concept-desc">The biggest ML mistake is a model that memorizes the training data but fails on new data — like a student who memorizes the practice test answers but can't solve new problems. This is <strong>overfitting</strong>. To detect it, you split your data.</div>
      <table class="ai-table">
        <thead><tr><th>Term</th><th>Meaning</th></tr></thead>
        <tbody>
          <tr><td>Training set (~70%)</td><td>Data the model learns from</td></tr>
          <tr><td>Validation set (~15%)</td><td>Used to tune the model during development</td></tr>
          <tr><td>Test set (~15%)</td><td>Held back — final unbiased check on unseen data</td></tr>
          <tr><td>Overfitting</td><td>Great on training data, bad on test data (memorized, didn't generalize)</td></tr>
          <tr><td>Underfitting</td><td>Bad on both — model too simple to capture the pattern</td></tr>
        </tbody>
      </table>
    </div>
    <div class="concept-card">
      <div class="concept-label">WHERE LLMs FIT</div>
      <div class="concept-title">From ML to Deep Learning to LLMs</div>
      <div class="concept-desc"><strong>Machine Learning</strong> is the broad field. <strong>Deep Learning</strong> is a subset using neural networks with many layers — great for images, audio, language. <strong>Large Language Models</strong> (GPT, Claude) are huge deep-learning models trained on vast text to predict the next token. They're a type of deep learning, which is a type of ML, which is a type of AI. Each is a circle inside the larger one: AI ⊃ ML ⊃ Deep Learning ⊃ LLMs.</div>
    </div>
  </div>
</div>
"""

# ─────────────────────────────── OPS wave 17 ─────────────────────────────────
OPS_SENTINEL = "<!-- BEGINNER17-OPS v1 -->"
OPS_CONTENT = """
<!-- BEGINNER17-OPS v1 -->
<!-- ── TOPIC: ITIL & SERVICE MANAGEMENT ──────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">🎫</span>
    <span class="topic-name">ITIL &amp; Service Management — How IT Runs as a Business</span>
    <span class="topic-badge">OPS • Process</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">WHAT IS ITIL</div>
      <div class="concept-title">A Framework for Delivering IT Services</div>
      <div class="concept-desc">ITIL (Information Technology Infrastructure Library) is the most widely adopted framework for IT Service Management (ITSM). It's a set of best practices for delivering IT as a service to a business — covering how you handle outages, changes, requests, and continuous improvement. You'll encounter ITIL terminology constantly in enterprise IT, especially on help desks and ops teams. Even if your company doesn't "do ITIL," they probably use its vocabulary.</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">INCIDENT VS PROBLEM VS CHANGE VS REQUEST</div>
      <div class="concept-title">The Four Terms People Mix Up</div>
      <table class="ai-table">
        <thead><tr><th>Type</th><th>Definition</th><th>Goal</th><th>Example</th></tr></thead>
        <tbody>
          <tr><td><strong>Incident</strong></td><td>Unplanned interruption or degradation of a service</td><td>Restore service ASAP (even with a workaround)</td><td>"Email is down"</td></tr>
          <tr><td><strong>Problem</strong></td><td>The underlying root cause of one or more incidents</td><td>Find &amp; fix root cause permanently</td><td>"Why does email keep going down? Bad disk."</td></tr>
          <tr><td><strong>Change</strong></td><td>Adding/modifying/removing anything that could affect services</td><td>Implement safely with minimal risk</td><td>"Upgrade the mail server"</td></tr>
          <tr><td><strong>Service Request</strong></td><td>A user asking for something standard/pre-approved</td><td>Fulfill efficiently</td><td>"I need access to the shared drive"</td></tr>
        </tbody>
      </table>
      <div class="concept-desc"><strong>Key distinction:</strong> an incident is "it's broken, fix it now." A problem is "why does it keep breaking?" You restore the incident fast (workaround), then investigate the problem to prevent recurrence.</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">INCIDENT PRIORITY</div>
      <div class="concept-title">Priority = Impact × Urgency</div>
      <div class="concept-desc">Not every incident is equal. Priority determines what gets worked first. It's calculated from <strong>impact</strong> (how many people / how critical) and <strong>urgency</strong> (how fast it needs fixing).</div>
      <table class="ai-table">
        <thead><tr><th>Priority</th><th>Typical Meaning</th><th>Example</th></tr></thead>
        <tbody>
          <tr><td>P1 — Critical</td><td>Major outage, business stopped</td><td>Entire company can't access core system</td></tr>
          <tr><td>P2 — High</td><td>Significant impact, no workaround</td><td>A department is down</td></tr>
          <tr><td>P3 — Medium</td><td>Limited impact or workaround exists</td><td>One team's printer is broken</td></tr>
          <tr><td>P4 — Low</td><td>Minor, single user, cosmetic</td><td>"My mouse settings reset"</td></tr>
        </tbody>
      </table>
    </div>
    <div class="concept-card">
      <div class="concept-label">CHANGE MANAGEMENT</div>
      <div class="concept-title">Why You Can't Just Push to Production</div>
      <div class="concept-desc">Most outages are self-inflicted — caused by changes. Change management adds guardrails so changes are reviewed, approved, scheduled, and reversible. The CAB (Change Advisory Board) reviews risky changes.</div>
      <table class="ai-table">
        <thead><tr><th>Change Type</th><th>Risk</th><th>Approval</th><th>Example</th></tr></thead>
        <tbody>
          <tr><td>Standard</td><td>Low, pre-approved</td><td>None needed (routine)</td><td>Routine password reset, known patch</td></tr>
          <tr><td>Normal</td><td>Variable</td><td>CAB review + approval</td><td>Major version upgrade</td></tr>
          <tr><td>Emergency</td><td>High (but necessary)</td><td>Expedited (ECAB)</td><td>Patch an actively exploited zero-day</td></tr>
        </tbody>
      </table>
      <div class="concept-desc">Every change should have a <strong>rollback plan</strong> ("if it breaks, how do we undo it?") and a <strong>maintenance window</strong> (a scheduled low-traffic time). "It's just a small change" is the most dangerous phrase in ops.</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">SLAs, SLOs, SLIs</div>
      <div class="concept-title">Measuring Service Quality</div>
      <table class="ai-table">
        <thead><tr><th>Term</th><th>Full Name</th><th>What It Is</th></tr></thead>
        <tbody>
          <tr><td>SLI</td><td>Service Level Indicator</td><td>The actual measurement (e.g., 99.95% uptime measured)</td></tr>
          <tr><td>SLO</td><td>Service Level Objective</td><td>Your internal target (e.g., "we aim for 99.9%")</td></tr>
          <tr><td>SLA</td><td>Service Level Agreement</td><td>The contractual promise with consequences (e.g., "99.9% or refund")</td></tr>
        </tbody>
      </table>
      <div class="concept-desc">"The number of nines" matters: 99.9% ("three nines") = 8.7 hours downtime/year. 99.99% = 52 minutes/year. 99.999% ("five nines") = 5 minutes/year. Each extra nine costs exponentially more.</div>
    </div>
  </div>
</div>
"""

# ─────────────────────────────── SCRIPT wave 17 ──────────────────────────────
SCRIPT_SENTINEL = "<!-- BEGINNER17-SCRIPT v1 -->"
SCRIPT_CONTENT = """
<!-- BEGINNER17-SCRIPT v1 -->
<!-- ── TOPIC: DATES AND TIMES ────────────────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">🕐</span>
    <span class="topic-name">Dates &amp; Times — Trickier Than You Think</span>
    <span class="topic-badge">SCRIPT • Essential</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">WHY TIME IS HARD</div>
      <div class="concept-title">Time Zones, DST, and Other Nightmares</div>
      <div class="concept-desc">Date/time handling is famously error-prone: time zones, daylight saving time, leap years, leap seconds, and ambiguous formats. The golden rules: <strong>store and compute in UTC, display in local time</strong>, and <strong>always use timezone-aware datetimes</strong> (never naive ones in production). Logs, certificates, and security events all depend on getting this right.</div>
      <div class="code-block"><span class="kw">from</span> datetime <span class="kw">import</span> datetime, timezone, timedelta

<span class="com"># Get current time — ALWAYS timezone-aware</span>
now = datetime.now(timezone.utc)        <span class="com"># aware, in UTC ✓</span>
bad = datetime.now()                    <span class="com"># naive — avoid in prod ✗</span>

<span class="com"># Format and parse (strftime / strptime)</span>
now.strftime(<span class="str">"%Y-%m-%d %H:%M:%S"</span>)      <span class="com"># 2026-06-01 14:30:00</span>
datetime.strptime(<span class="str">"2026-06-01"</span>, <span class="str">"%Y-%m-%d"</span>)

<span class="com"># ISO 8601 — the standard for APIs and logs</span>
now.isoformat()                         <span class="com"># 2026-06-01T14:30:00+00:00</span>
datetime.fromisoformat(<span class="str">"2026-06-01T14:30:00+00:00"</span>)

<span class="com"># Arithmetic with timedelta</span>
yesterday = now - timedelta(days=<span class="num">1</span>)
deadline = now + timedelta(hours=<span class="num">48</span>)
elapsed = (end - start).total_seconds()

<span class="com"># Unix timestamps (seconds since 1970-01-01 UTC)</span>
ts = now.timestamp()                    <span class="com"># 1.78e9</span>
datetime.fromtimestamp(ts, timezone.utc)</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">STRFTIME CHEAT SHEET</div>
      <div class="concept-title">Format Codes You'll Actually Use</div>
      <table class="ai-table">
        <thead><tr><th>Code</th><th>Meaning</th><th>Example</th></tr></thead>
        <tbody>
          <tr><td><code>%Y</code></td><td>4-digit year</td><td>2026</td></tr>
          <tr><td><code>%m</code></td><td>Month (01-12)</td><td>06</td></tr>
          <tr><td><code>%d</code></td><td>Day (01-31)</td><td>01</td></tr>
          <tr><td><code>%H</code></td><td>Hour 24h (00-23)</td><td>14</td></tr>
          <tr><td><code>%M</code></td><td>Minute</td><td>30</td></tr>
          <tr><td><code>%S</code></td><td>Second</td><td>00</td></tr>
          <tr><td><code>%A</code> / <code>%a</code></td><td>Weekday full / abbr</td><td>Monday / Mon</td></tr>
          <tr><td><code>%B</code> / <code>%b</code></td><td>Month full / abbr</td><td>June / Jun</td></tr>
          <tr><td><code>%z</code> / <code>%Z</code></td><td>UTC offset / tz name</td><td>+0000 / UTC</td></tr>
        </tbody>
      </table>
    </div>
  </div>
</div>

<!-- ── TOPIC: DATA ANALYSIS WITH PANDAS ──────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">📊</span>
    <span class="topic-name">Data Analysis with pandas — Spreadsheets in Code</span>
    <span class="topic-badge">SCRIPT • Practical</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">WHY PANDAS</div>
      <div class="concept-title">Excel, But Programmable and Unlimited</div>
      <div class="concept-desc">pandas is the standard Python library for working with tabular data (think spreadsheets/CSVs/database tables). It handles millions of rows, automates repetitive analysis, and integrates with everything. For IT, it's invaluable for analyzing logs, parsing CSV exports, generating reports, and crunching security data. The core object is the <strong>DataFrame</strong> — a table with labeled rows and columns.</div>
      <div class="code-block"><span class="com"># pip install pandas</span>
<span class="kw">import</span> pandas <span class="kw">as</span> pd

<span class="com"># Load data</span>
df = pd.read_csv(<span class="str">"firewall_logs.csv"</span>)
df = pd.read_json(<span class="str">"data.json"</span>)
df = pd.read_excel(<span class="str">"report.xlsx"</span>)

<span class="com"># Explore (the first thing you always do)</span>
df.head()              <span class="com"># first 5 rows</span>
df.shape               <span class="com"># (rows, columns)</span>
df.columns             <span class="com"># column names</span>
df.info()              <span class="com"># types and non-null counts</span>
df.describe()          <span class="com"># summary statistics</span></div>
    </div>
    <div class="concept-card">
      <div class="concept-label">FILTERING & ANALYSIS</div>
      <div class="concept-title">Answering Questions About Your Data</div>
      <div class="code-block"><span class="com"># Select columns</span>
df[<span class="str">"src_ip"</span>]                       <span class="com"># one column</span>
df[[<span class="str">"src_ip"</span>, <span class="str">"action"</span>]]           <span class="com"># multiple</span>

<span class="com"># Filter rows (boolean indexing)</span>
blocked = df[df[<span class="str">"action"</span>] == <span class="str">"DENY"</span>]
df[(df[<span class="str">"port"</span>] == <span class="num">22</span>) &amp; (df[<span class="str">"action"</span>] == <span class="str">"DENY"</span>)]

<span class="com"># The killer feature: group and count</span>
<span class="com"># "Which IPs were blocked the most?"</span>
top_attackers = (df[df[<span class="str">"action"</span>] == <span class="str">"DENY"</span>]
                 .groupby(<span class="str">"src_ip"</span>)
                 .size()
                 .sort_values(ascending=<span class="kw">False</span>)
                 .head(<span class="num">10</span>))
<span class="fn">print</span>(top_attackers)

<span class="com"># Value counts — quick frequency table</span>
df[<span class="str">"action"</span>].value_counts()      <span class="com"># DENY: 5021, ALLOW: 88210</span>

<span class="com"># Export results</span>
top_attackers.to_csv(<span class="str">"top_attackers.csv"</span>)</div>
    </div>
  </div>
</div>
"""

# ─────────────────────────────── SHORTCUT wave 17 ────────────────────────────
SHORTCUT_SENTINEL = "<!-- BEGINNER17-SHORTCUT v1 -->"
SHORTCUT_CONTENT = """
<!-- BEGINNER17-SHORTCUT v1 -->
<!-- ── TOPIC: GIT POWER USER ─────────────────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">🌳</span>
    <span class="topic-name">Git Power User — Beyond add, commit, push</span>
    <span class="topic-badge">SHORTCUTS • Version Control</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">STASHING</div>
      <div class="concept-title">Set Work Aside Temporarily</div>
      <div class="concept-desc">You're mid-change and suddenly need to switch branches for an urgent fix — but your work isn't ready to commit. <code>git stash</code> shelves your changes so you have a clean working directory, then restores them later.</div>
      <div class="code-block">git stash                    <span class="com"># shelve current changes</span>
git stash -u                 <span class="com"># include untracked files</span>
git stash list               <span class="com"># see all stashes</span>
git stash pop                <span class="com"># restore most recent &amp; remove from list</span>
git stash apply              <span class="com"># restore but KEEP in stash list</span>
git stash drop               <span class="com"># delete a stash</span>
git stash save "wip: login"  <span class="com"># named stash</span></div>
    </div>
    <div class="concept-card">
      <div class="concept-label">REBASE</div>
      <div class="concept-title">Rewrite History for a Clean Timeline</div>
      <div class="concept-desc">Rebasing moves your commits to start from a different base — useful for keeping a linear, clean history instead of merge bubbles. <strong>Golden rule: never rebase commits you've already pushed to a shared branch</strong> (it rewrites history others depend on).</div>
      <div class="code-block"><span class="com"># Update your feature branch with latest main (linear)</span>
git checkout feature
git rebase main             <span class="com"># replay your commits on top of main</span>

<span class="com"># Interactive rebase — clean up your last N commits</span>
git rebase -i HEAD~3        <span class="com"># edit/squash/reorder last 3 commits</span>
<span class="com"># In the editor: pick / squash / reword / drop / edit</span>

<span class="com"># If conflicts arise during rebase</span>
<span class="com"># fix files, then:</span>
git add &lt;files&gt;
git rebase --continue
git rebase --abort          <span class="com"># bail out, restore original state</span></div>
    </div>
    <div class="concept-card">
      <div class="concept-label">UNDOING THINGS</div>
      <div class="concept-title">The Commands That Save You</div>
      <table class="ai-table">
        <thead><tr><th>Goal</th><th>Command</th></tr></thead>
        <tbody>
          <tr><td>Unstage a file (keep changes)</td><td><code>git restore --staged file</code></td></tr>
          <tr><td>Discard local changes to a file</td><td><code>git restore file</code></td></tr>
          <tr><td>Amend the last commit</td><td><code>git commit --amend</code></td></tr>
          <tr><td>Undo last commit, keep changes staged</td><td><code>git reset --soft HEAD~1</code></td></tr>
          <tr><td>Undo last commit, keep changes unstaged</td><td><code>git reset HEAD~1</code></td></tr>
          <tr><td>Nuke last commit and changes (danger)</td><td><code>git reset --hard HEAD~1</code></td></tr>
          <tr><td>Safely undo a pushed commit</td><td><code>git revert &lt;hash&gt;</code> (makes a new inverse commit)</td></tr>
          <tr><td>Recover "lost" commits</td><td><code>git reflog</code> (your safety net — shows ALL HEAD moves)</td></tr>
        </tbody>
      </table>
    </div>
    <div class="concept-card">
      <div class="concept-label">GIT BISECT</div>
      <div class="concept-title">Binary Search to Find the Bug-Introducing Commit</div>
      <div class="concept-desc">A bug appeared somewhere in the last 200 commits but you don't know where. <code>git bisect</code> does a binary search — you test the midpoint, tell git "good" or "bad", and it homes in on the exact commit that broke things in ~log₂(n) steps.</div>
      <div class="code-block">git bisect start
git bisect bad                <span class="com"># current commit is broken</span>
git bisect good v1.0          <span class="com"># this old tag worked</span>

<span class="com"># Git checks out a commit halfway between. Test it, then:</span>
git bisect good               <span class="com"># this one works</span>
<span class="com"># — or —</span>
git bisect bad                <span class="com"># this one is broken</span>

<span class="com"># Repeat. Git narrows down to the exact culprit commit.</span>
git bisect reset              <span class="com"># done — return to where you started</span>

<span class="com"># Automate it with a test script!</span>
git bisect run ./test.sh      <span class="com"># git runs the script at each step</span></div>
    </div>
    <div class="concept-card">
      <div class="concept-label">INSPECTING</div>
      <div class="concept-title">Useful Investigation Commands</div>
      <div class="code-block">git log --oneline --graph --all   <span class="com"># visual branch history</span>
git blame file.py                 <span class="com"># who changed each line and when</span>
git show &lt;hash&gt;                    <span class="com"># view a specific commit's changes</span>
git diff main..feature            <span class="com"># compare two branches</span>
git log --grep="bug"              <span class="com"># search commit messages</span>
git log -p file.py                <span class="com"># full history of one file</span>
git log --author="alice"          <span class="com"># commits by author</span></div>
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
        (NET_INJECT_ANCHOR,      NET_SENTINEL,      NET_CONTENT),
        (AI_INJECT_ANCHOR,       AI_SENTINEL,       AI_CONTENT),
        (OPS_INJECT_ANCHOR,      OPS_SENTINEL,      OPS_CONTENT),
        (SCRIPT_INJECT_ANCHOR,   SCRIPT_SENTINEL,   SCRIPT_CONTENT),
        (SHORTCUT_INJECT_ANCHOR, SHORTCUT_SENTINEL, SHORTCUT_CONTENT),
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
