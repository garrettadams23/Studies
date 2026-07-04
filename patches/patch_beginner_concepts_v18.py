#!/usr/bin/env python3
"""
patch_beginner_concepts_v18.py — Wave 18: Code quality tooling, ransomware/
threat actors, SSH hardening, performance/capacity, military leadership.

New sentinels:
  BEGINNER18-SCRIPT v1  — Code quality (black/ruff/mypy/pre-commit), mocking in tests
  BEGINNER18-THREAT v1  — Ransomware deep dive, threat actor taxonomy, APTs
  BEGINNER18-LINUX v1   — SSH deep dive and hardening, key management
  BEGINNER18-OPS v1     — Performance tuning, capacity planning, log management
  BEGINNER18-MIL v1     — After-action reviews, troop leading procedures, leadership
"""
from pathlib import Path

SCRIPT_INJECT_ANCHOR = "<!-- /domain-body script -->"
THREAT_INJECT_ANCHOR = "<!-- /domain-body threat -->"
LINUX_INJECT_ANCHOR  = "<!-- /domain-body linux -->"
OPS_INJECT_ANCHOR    = "<!-- /domain-body ops -->"
MIL_INJECT_ANCHOR    = "<!-- /domain-body military -->"

# ─────────────────────────────── SCRIPT wave 18 ──────────────────────────────
SCRIPT_SENTINEL = "<!-- BEGINNER18-SCRIPT v1 -->"
SCRIPT_CONTENT = """
<!-- BEGINNER18-SCRIPT v1 -->
<!-- ── TOPIC: CODE QUALITY TOOLING ───────────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">✨</span>
    <span class="topic-name">Code Quality Tooling — Let Robots Enforce the Boring Rules</span>
    <span class="topic-badge">SCRIPT • Professional</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">WHY IT MATTERS</div>
      <div class="concept-title">Consistency Beats Cleverness</div>
      <div class="concept-desc">Professional codebases use automated tools to enforce style, catch bugs, and keep code consistent — so humans don't waste time arguing about formatting in code review. These tools run automatically (locally and in CI), catching issues before they reach production. Setting them up marks the transition from "I write scripts" to "I write professional software."</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">THE TOOLBOX</div>
      <div class="concept-title">The Modern Python Quality Stack</div>
      <table class="ai-table">
        <thead><tr><th>Tool</th><th>Category</th><th>What It Does</th></tr></thead>
        <tbody>
          <tr><td><code>black</code></td><td>Formatter</td><td>Auto-formats code to one consistent style — no debate</td></tr>
          <tr><td><code>ruff</code></td><td>Linter + formatter</td><td>Ultra-fast (Rust); replaces flake8, isort, and more</td></tr>
          <tr><td><code>mypy</code></td><td>Type checker</td><td>Catches type errors using your type hints — before runtime</td></tr>
          <tr><td><code>pytest</code></td><td>Test runner</td><td>Runs your automated tests</td></tr>
          <tr><td><code>bandit</code></td><td>Security linter</td><td>Flags common security issues (hardcoded secrets, eval)</td></tr>
          <tr><td><code>pre-commit</code></td><td>Git hook manager</td><td>Runs all the above automatically before each commit</td></tr>
        </tbody>
      </table>
    </div>
    <div class="concept-card">
      <div class="concept-label">USING THEM</div>
      <div class="concept-title">Run Them From the Command Line</div>
      <div class="code-block"><span class="com"># Format code automatically</span>
black .                       <span class="com"># reformat everything</span>
ruff format .                 <span class="com"># ruff's formatter (black-compatible)</span>

<span class="com"># Lint — find problems</span>
ruff check .                  <span class="com"># report issues</span>
ruff check --fix .            <span class="com"># auto-fix what it can</span>

<span class="com"># Type check</span>
mypy myproject/

<span class="com"># Security scan</span>
bandit -r myproject/

<span class="com"># Run tests with coverage</span>
pytest --cov=myproject</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">PRE-COMMIT HOOKS</div>
      <div class="concept-title">Automate Quality on Every Commit</div>
      <div class="concept-desc">pre-commit runs your quality tools automatically every time you <code>git commit</code>. If something fails, the commit is blocked until you fix it. This catches problems at the earliest possible moment.</div>
      <div class="code-block"><span class="com"># .pre-commit-config.yaml</span>
repos:
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.4.0
    hooks:
      - id: ruff
        args: [--fix]
      - id: ruff-format
  - repo: https://github.com/pre-commit/mirrors-mypy
    rev: v1.10.0
    hooks:
      - id: mypy

<span class="com"># Install once, then it runs on every commit</span>
pip install pre-commit
pre-commit install
pre-commit run --all-files    <span class="com"># run manually on whole repo</span></div>
    </div>
  </div>
</div>

<!-- ── TOPIC: MOCKING IN TESTS ───────────────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">🎭</span>
    <span class="topic-name">Mocking — Testing Code That Talks to the Outside World</span>
    <span class="topic-badge">SCRIPT • Testing</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">THE PROBLEM</div>
      <div class="concept-title">How Do You Test Code That Calls an API?</div>
      <div class="concept-desc">Your function calls a real API, queries a database, or reads the system clock. You can't have your tests hitting a real server (slow, flaky, costs money, may not exist in CI). The solution is <strong>mocking</strong>: replacing the real dependency with a fake that you control, so you can test YOUR logic in isolation.</div>
      <div class="code-block"><span class="kw">from</span> unittest.mock <span class="kw">import</span> patch, MagicMock
<span class="kw">import</span> requests

<span class="com"># The function under test — calls a real API</span>
<span class="kw">def</span> <span class="fn">get_user_count</span>():
    resp = requests.get(<span class="str">"https://api.example.com/users"</span>)
    <span class="kw">return</span> resp.json()[<span class="str">"count"</span>]

<span class="com"># The test — mock out requests.get so no real call happens</span>
<span class="fn">@patch</span>(<span class="str">"requests.get"</span>)
<span class="kw">def</span> <span class="fn">test_get_user_count</span>(mock_get):
    <span class="com"># Configure the fake response</span>
    mock_get.return_value.json.return_value = {<span class="str">"count"</span>: <span class="num">42</span>}

    <span class="com"># Call the function — it uses the mock, not the real API</span>
    result = get_user_count()

    <span class="com"># Assert YOUR logic worked</span>
    <span class="kw">assert</span> result == <span class="num">42</span>
    mock_get.assert_called_once_with(<span class="str">"https://api.example.com/users"</span>)</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">MOCKING CONCEPTS</div>
      <div class="concept-title">The Vocabulary of Test Doubles</div>
      <table class="ai-table">
        <thead><tr><th>Term</th><th>What It Is</th></tr></thead>
        <tbody>
          <tr><td>Mock</td><td>A fake object you configure and inspect (was it called? with what?)</td></tr>
          <tr><td>Stub</td><td>A fake that returns canned answers, no behavior verification</td></tr>
          <tr><td>Patch</td><td>Temporarily replace a real object with a mock during a test</td></tr>
          <tr><td>Fixture</td><td>Reusable test setup (e.g., a fresh DB, sample data)</td></tr>
          <tr><td>Spy</td><td>Wraps a real object but records how it was called</td></tr>
          <tr><td>Fake</td><td>A working but simplified implementation (e.g., in-memory DB)</td></tr>
        </tbody>
      </table>
      <div class="concept-desc"><strong>Rule of thumb:</strong> mock at the boundaries (network, disk, time, randomness) — not your own internal logic. Over-mocking makes tests that pass even when the real code is broken.</div>
    </div>
  </div>
</div>
"""

# ─────────────────────────────── THREAT wave 18 ──────────────────────────────
THREAT_SENTINEL = "<!-- BEGINNER18-THREAT v1 -->"
THREAT_CONTENT = """
<!-- BEGINNER18-THREAT v1 -->
<!-- ── TOPIC: RANSOMWARE DEEP DIVE ───────────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">🔒</span>
    <span class="topic-name">Ransomware — The Defining Threat of the Era</span>
    <span class="topic-badge">THREAT • Critical</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">HOW IT WORKS</div>
      <div class="concept-title">The Ransomware Attack Lifecycle</div>
      <div class="concept-desc">Ransomware encrypts your files and demands payment for the decryption key. But modern ransomware is rarely a single event — it's the final stage of a longer intrusion. Understanding the full lifecycle reveals many points where defenders can intervene before the encryption ever happens.</div>
      <table class="ai-table">
        <thead><tr><th>Stage</th><th>What Happens</th><th>Defense Opportunity</th></tr></thead>
        <tbody>
          <tr><td>1. Initial access</td><td>Phishing, exposed RDP, exploited VPN/vuln</td><td>MFA, patching, email filtering, awareness</td></tr>
          <tr><td>2. Establish foothold</td><td>Install backdoor, C2 channel</td><td>EDR detection, egress filtering</td></tr>
          <tr><td>3. Privilege escalation</td><td>Get domain admin</td><td>Least privilege, tiered admin, patching</td></tr>
          <tr><td>4. Lateral movement</td><td>Spread across the network</td><td>Network segmentation, monitoring</td></tr>
          <tr><td>5. Exfiltration</td><td>Steal data for double extortion</td><td>DLP, egress monitoring</td></tr>
          <tr><td>6. Encryption</td><td>Deploy ransomware everywhere at once</td><td>Immutable backups, EDR behavioral blocking</td></tr>
          <tr><td>7. Extortion</td><td>Demand payment; threaten to leak data</td><td>IR plan, backups, legal/comms ready</td></tr>
        </tbody>
      </table>
    </div>
    <div class="concept-card">
      <div class="concept-label">MODERN TACTICS</div>
      <div class="concept-title">Why It Got So Much Worse</div>
      <table class="ai-table">
        <thead><tr><th>Tactic</th><th>What It Means</th></tr></thead>
        <tbody>
          <tr><td>Double extortion</td><td>Steal data BEFORE encrypting — "pay or we leak it publicly." Backups alone no longer save you.</td></tr>
          <tr><td>Triple extortion</td><td>Also threaten customers, DDoS, or regulators</td></tr>
          <tr><td>RaaS (Ransomware-as-a-Service)</td><td>Developers rent ransomware to "affiliates" for a cut — lowers the skill barrier dramatically</td></tr>
          <tr><td>Big game hunting</td><td>Targeting large orgs for massive payouts rather than spray-and-pray</td></tr>
          <tr><td>Living off the land</td><td>Using built-in tools (PsExec, PowerShell) to evade detection</td></tr>
        </tbody>
      </table>
    </div>
    <div class="concept-card">
      <div class="concept-label">DEFENSE & RESPONSE</div>
      <div class="concept-title">Should You Pay? (Generally, No)</div>
      <div class="concept-desc">Authorities (FBI, CISA) discourage paying: it funds crime, marks you as a target, and offers no guarantee of recovery (decryptors are often buggy or incomplete). The best defense is preparation: <strong>immutable, offline backups</strong> (can't be encrypted), tested recovery, network segmentation, MFA everywhere, and a rehearsed incident response plan. The organizations that recover fastest are the ones that prepared before the attack.</div>
    </div>
  </div>
</div>

<!-- ── TOPIC: THREAT ACTOR TAXONOMY ──────────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">🎭</span>
    <span class="topic-name">Threat Actors — Know Your Adversary</span>
    <span class="topic-badge">THREAT • Foundation</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">WHO ATTACKS AND WHY</div>
      <div class="concept-title">The Threat Actor Spectrum</div>
      <div class="concept-desc">Different attackers have different motivations, resources, and skill — which shapes how they attack and how you defend. Understanding who might target you (your "threat model") helps prioritize defenses.</div>
      <table class="ai-table">
        <thead><tr><th>Actor</th><th>Motivation</th><th>Sophistication</th><th>Example</th></tr></thead>
        <tbody>
          <tr><td>Script kiddie</td><td>Bragging rights, curiosity</td><td>Low — uses others' tools</td><td>Running downloaded exploits</td></tr>
          <tr><td>Hacktivist</td><td>Ideology, political message</td><td>Low-medium</td><td>Anonymous, website defacement, DDoS</td></tr>
          <tr><td>Cybercriminal</td><td>Money</td><td>Medium-high</td><td>Ransomware gangs, banking trojans, fraud</td></tr>
          <tr><td>Insider threat</td><td>Revenge, money, negligence</td><td>Varies (has legit access)</td><td>Disgruntled employee stealing data</td></tr>
          <tr><td>Nation-state (APT)</td><td>Espionage, sabotage, strategic</td><td>Very high, well-funded, patient</td><td>Stuxnet, SolarWinds</td></tr>
          <tr><td>Terrorist / cyberterror</td><td>Fear, disruption</td><td>Varies</td><td>Attacks on critical infrastructure</td></tr>
        </tbody>
      </table>
    </div>
    <div class="concept-card">
      <div class="concept-label">APTs</div>
      <div class="concept-title">Advanced Persistent Threats</div>
      <div class="concept-desc">An APT is a sophisticated, well-resourced (usually nation-state) attacker that gains access and stays hidden for a <em>long time</em> — months or years — pursuing strategic goals like espionage. The name breaks down: <strong>Advanced</strong> (custom tools, zero-days), <strong>Persistent</strong> (long-term, patient, re-establishes access), <strong>Threat</strong> (organized, funded, goal-driven). They're given names/numbers by researchers: APT28 (Fancy Bear), APT29 (Cozy Bear), Lazarus Group. Defending against APTs requires assuming breach, deep monitoring, and threat hunting — you won't stop them at the door.</div>
    </div>
  </div>
</div>
"""

# ─────────────────────────────── LINUX wave 18 ───────────────────────────────
LINUX_SENTINEL = "<!-- BEGINNER18-LINUX v1 -->"
LINUX_CONTENT = """
<!-- BEGINNER18-LINUX v1 -->
<!-- ── TOPIC: SSH DEEP DIVE & HARDENING ──────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">🔑</span>
    <span class="topic-name">SSH — Secure Remote Access Done Right</span>
    <span class="topic-badge">LINUX • Essential</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">SSH BASICS</div>
      <div class="concept-title">The Universal Remote Access Protocol</div>
      <div class="concept-desc">SSH (Secure Shell) is how you remotely access and manage Linux/Unix servers over an encrypted connection. It's foundational — every sysadmin, DevOps engineer, and security professional lives in SSH. It replaced the old, insecure Telnet (which sent passwords in plaintext).</div>
      <div class="code-block"><span class="com"># Connect to a server</span>
ssh alice@server.example.com
ssh -p 2222 alice@server.com      <span class="com"># custom port</span>

<span class="com"># Run a single command remotely</span>
ssh alice@server "df -h"

<span class="com"># Copy files over SSH</span>
scp file.txt alice@server:/tmp/   <span class="com"># local → remote</span>
scp alice@server:/var/log/app.log .   <span class="com"># remote → local</span>
rsync -avz ./data/ alice@server:/backup/   <span class="com"># efficient sync</span></div>
    </div>
    <div class="concept-card">
      <div class="concept-label">KEY-BASED AUTH</div>
      <div class="concept-title">Stop Using Passwords — Use Keys</div>
      <div class="concept-desc">SSH key pairs are far more secure than passwords: a private key (kept secret on your machine) and a public key (placed on servers). Authentication happens via cryptography, not a guessable password. This is THE standard for professional server access.</div>
      <div class="code-block"><span class="com"># Generate a modern key pair (ed25519 preferred)</span>
ssh-keygen -t ed25519 -C "alice@laptop"
<span class="com"># Creates ~/.ssh/id_ed25519 (private) and id_ed25519.pub (public)</span>

<span class="com"># Copy your PUBLIC key to a server (enables key login)</span>
ssh-copy-id alice@server.example.com

<span class="com"># Now you can log in without a password</span>
ssh alice@server.example.com

<span class="com"># Permissions MUST be strict or SSH refuses the key</span>
chmod 700 ~/.ssh
chmod 600 ~/.ssh/id_ed25519       <span class="com"># private key</span>
chmod 644 ~/.ssh/id_ed25519.pub   <span class="com"># public key</span>

<span class="com"># Use ssh-agent so you don't retype the passphrase</span>
eval $(ssh-agent)
ssh-add ~/.ssh/id_ed25519</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">SSH CONFIG</div>
      <div class="concept-title">Save Yourself Typing with ~/.ssh/config</div>
      <div class="code-block"><span class="com"># ~/.ssh/config — define shortcuts and defaults</span>
Host web
    HostName web1.example.com
    User alice
    Port 2222
    IdentityFile ~/.ssh/id_ed25519

Host bastion
    HostName jump.example.com
    User admin

<span class="com"># Reach internal host through the bastion automatically</span>
Host internal-db
    HostName 10.0.5.20
    User dbadmin
    ProxyJump bastion

<span class="com"># Now just:  ssh web   (instead of the full command)</span></div>
    </div>
    <div class="concept-card">
      <div class="concept-label">HARDENING SSHD</div>
      <div class="concept-title">Locking Down the SSH Server</div>
      <div class="concept-desc">SSH is the #1 target of automated internet attacks — bots constantly try to brute-force it. Hardening <code>/etc/ssh/sshd_config</code> dramatically reduces risk.</div>
      <table class="ai-table">
        <thead><tr><th>Setting</th><th>Value</th><th>Why</th></tr></thead>
        <tbody>
          <tr><td><code>PermitRootLogin</code></td><td><code>no</code></td><td>Force use of named accounts + sudo (accountability + harder to brute-force)</td></tr>
          <tr><td><code>PasswordAuthentication</code></td><td><code>no</code></td><td>Keys only — defeats password brute-forcing entirely</td></tr>
          <tr><td><code>PubkeyAuthentication</code></td><td><code>yes</code></td><td>Enable key-based auth</td></tr>
          <tr><td><code>Port</code></td><td><code>2222</code> (non-standard)</td><td>Reduces noise from automated bots (not real security, just quieter)</td></tr>
          <tr><td><code>AllowUsers</code></td><td><code>alice bob</code></td><td>Whitelist who can SSH in</td></tr>
          <tr><td><code>MaxAuthTries</code></td><td><code>3</code></td><td>Limit guesses per connection</td></tr>
        </tbody>
      </table>
      <div class="code-block"><span class="com"># Apply changes safely</span>
sudo nano /etc/ssh/sshd_config
sudo sshd -t                      <span class="com"># test config syntax FIRST</span>
sudo systemctl restart sshd

<span class="com"># Add fail2ban to auto-ban brute-forcers</span>
sudo apt install fail2ban
<span class="com"># Bans IPs after repeated failed logins</span></div>
    </div>
  </div>
</div>
"""

# ─────────────────────────────── OPS wave 18 ─────────────────────────────────
OPS_SENTINEL = "<!-- BEGINNER18-OPS v1 -->"
OPS_CONTENT = """
<!-- BEGINNER18-OPS v1 -->
<!-- ── TOPIC: PERFORMANCE & CAPACITY ─────────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">📈</span>
    <span class="topic-name">Performance &amp; Capacity — Finding and Fixing Bottlenecks</span>
    <span class="topic-badge">OPS • Essential</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">THE FOUR RESOURCES</div>
      <div class="concept-title">Everything Is CPU, Memory, Disk, or Network</div>
      <div class="concept-desc">When a system is slow, the bottleneck is almost always one of four resources. The skill is identifying <em>which one</em> — guessing wastes time. Start broad (which resource is saturated?), then drill into the offending process.</div>
      <table class="ai-table">
        <thead><tr><th>Resource</th><th>Symptom</th><th>Linux Tool</th></tr></thead>
        <tbody>
          <tr><td>CPU</td><td>High load, slow computation</td><td><code>top</code>, <code>htop</code>, <code>mpstat</code>, <code>uptime</code></td></tr>
          <tr><td>Memory</td><td>Swapping, OOM kills, slowness</td><td><code>free -h</code>, <code>vmstat</code>, <code>top</code></td></tr>
          <tr><td>Disk I/O</td><td>High iowait, slow reads/writes</td><td><code>iostat</code>, <code>iotop</code>, <code>df</code>, <code>du</code></td></tr>
          <tr><td>Network</td><td>Latency, packet loss, saturation</td><td><code>iftop</code>, <code>ss</code>, <code>nload</code>, <code>mtr</code></td></tr>
        </tbody>
      </table>
    </div>
    <div class="concept-card">
      <div class="concept-label">READING THE VITALS</div>
      <div class="concept-title">Load Average and Resource Commands</div>
      <div class="code-block"><span class="com"># Load average: 1, 5, 15-minute averages</span>
uptime
<span class="com"># load average: 2.50, 1.80, 1.20</span>
<span class="com"># Rule of thumb: compare to CPU core count.</span>
<span class="com"># load 2.5 on a 4-core box = fine. On 1 core = overloaded.</span>
nproc                  <span class="com"># how many cores you have</span>

<span class="com"># Memory — is it actually low, or just cached?</span>
free -h
<span class="com"># "available" is the number that matters, not "free"</span>
<span class="com"># Linux uses spare RAM for cache — that's good, not a problem</span>

<span class="com"># Disk I/O wait — %wa in top means CPU waiting on disk</span>
iostat -x 2           <span class="com"># %util near 100 = disk saturated</span>

<span class="com"># Find the hungriest processes</span>
top -o %CPU           <span class="com"># sort by CPU</span>
top -o %MEM           <span class="com"># sort by memory</span>
ps aux --sort=-%mem | head    <span class="com"># top memory consumers</span></div>
    </div>
    <div class="concept-card">
      <div class="concept-label">THE USE METHOD</div>
      <div class="concept-title">A Systematic Troubleshooting Framework</div>
      <div class="concept-desc">Brendan Gregg's USE method: for every resource, check three things. It's a checklist that prevents you from missing the obvious.</div>
      <table class="ai-table">
        <thead><tr><th>U-S-E</th><th>Question</th></tr></thead>
        <tbody>
          <tr><td><strong>U</strong>tilization</td><td>How busy is the resource? (% time active)</td></tr>
          <tr><td><strong>S</strong>aturation</td><td>Is there a queue/backlog of work waiting?</td></tr>
          <tr><td><strong>E</strong>rrors</td><td>Are there error events? (dropped packets, disk errors)</td></tr>
        </tbody>
      </table>
    </div>
    <div class="concept-card">
      <div class="concept-label">CAPACITY PLANNING</div>
      <div class="concept-title">Don't Wait Until It's On Fire</div>
      <div class="concept-desc">Capacity planning means predicting future resource needs based on growth trends, so you scale <em>before</em> you run out. Track utilization over time, identify the trend, and add capacity with lead time. The key metrics: current utilization, growth rate, and headroom (how much buffer before you hit limits). A disk filling at 2%/week with 20% free has ~10 weeks — plan now, not at 99%.</div>
    </div>
  </div>
</div>
"""

# ─────────────────────────────── MILITARY wave 18 ────────────────────────────
MIL_SENTINEL = "<!-- BEGINNER18-MIL v1 -->"
MIL_CONTENT = """
<!-- BEGINNER18-MIL v1 -->
<!-- ── TOPIC: AFTER-ACTION REVIEW ────────────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">📝</span>
    <span class="topic-name">After-Action Review — Learning From Every Event</span>
    <span class="topic-badge">MILITARY • Continuous Improvement</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">WHAT IS AN AAR</div>
      <div class="concept-title">The Army's Structured Debrief</div>
      <div class="concept-desc">The After-Action Review (AAR) is a U.S. Army practice for learning from any event — a mission, an exercise, a failure. It's a structured, honest discussion conducted immediately afterward while memories are fresh. The civilian tech world adopted it as the "post-mortem" or "retrospective." It's one of the highest-leverage habits a team can build: every incident becomes a lesson instead of just a scar.</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">THE FOUR QUESTIONS</div>
      <div class="concept-title">The Core of Every AAR</div>
      <table class="ai-table">
        <thead><tr><th>Question</th><th>Purpose</th></tr></thead>
        <tbody>
          <tr><td>1. What was supposed to happen?</td><td>Establish the plan/expectation</td></tr>
          <tr><td>2. What actually happened?</td><td>Establish the facts, honestly</td></tr>
          <tr><td>3. Why was there a difference?</td><td>Root cause analysis — the real learning</td></tr>
          <tr><td>4. What do we do differently next time?</td><td>Actionable improvements, assigned owners</td></tr>
        </tbody>
      </table>
    </div>
    <div class="concept-card">
      <div class="concept-label">THE BLAMELESS PRINCIPLE</div>
      <div class="concept-title">Hunt for Causes, Not Culprits</div>
      <div class="concept-desc">The single most important rule: AARs (and post-mortems) must be <strong>blameless</strong>. The moment people fear punishment, they hide information — and you lose the lessons. The premise is that everyone acted reasonably given what they knew at the time. The goal is to fix the <em>system</em> (better tooling, clearer process, more training) that allowed the mistake, not to punish the person. This maps directly to IT incident post-mortems: when engineers can speak freely about what went wrong, the organization actually improves.</div>
      <table class="ai-table">
        <thead><tr><th>Blameless (Good)</th><th>Blameful (Toxic)</th></tr></thead>
        <tbody>
          <tr><td>"The deploy process let an untested change reach prod"</td><td>"Bob broke production"</td></tr>
          <tr><td>"Our runbook was unclear about the rollback step"</td><td>"You should have known better"</td></tr>
          <tr><td>People share mistakes openly → org learns</td><td>People hide mistakes → org repeats them</td></tr>
        </tbody>
      </table>
    </div>
  </div>
</div>

<!-- ── TOPIC: TROOP LEADING PROCEDURES ───────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">🧭</span>
    <span class="topic-name">Troop Leading Procedures — A Framework for Planning Anything</span>
    <span class="topic-badge">MILITARY • Planning</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">THE 8 STEPS (BMNT)</div>
      <div class="concept-title">How Small-Unit Leaders Plan and Prepare</div>
      <div class="concept-desc">Troop Leading Procedures (TLP) are the 8-step process small-unit leaders use to plan and execute a mission. The genius is in step 3 — issue a warning order early so the team can start preparing in <em>parallel</em> while you finish planning. This concept maps perfectly to running an IT project or incident response.</div>
      <table class="ai-table">
        <thead><tr><th>Step</th><th>Military</th><th>IT/Project Equivalent</th></tr></thead>
        <tbody>
          <tr><td>1. Receive the mission</td><td>Get the order/task</td><td>Receive the ticket/project/incident</td></tr>
          <tr><td>2. Issue a warning order</td><td>Alert the team early</td><td>"Heads up team, big task coming — start prepping"</td></tr>
          <tr><td>3. Make a tentative plan</td><td>Initial course of action</td><td>Draft approach, identify resources</td></tr>
          <tr><td>4. Initiate movement</td><td>Start positioning</td><td>Provision environments, gather access</td></tr>
          <tr><td>5. Conduct reconnaissance</td><td>Recon the terrain</td><td>Investigate the system/codebase/logs</td></tr>
          <tr><td>6. Complete the plan</td><td>Finalize details</td><td>Finalize the runbook/design</td></tr>
          <tr><td>7. Issue the order</td><td>Brief the team</td><td>Kickoff: assign roles, confirm understanding</td></tr>
          <tr><td>8. Supervise &amp; refine</td><td>Execute, adjust, rehearse</td><td>Execute, monitor, adapt as you learn</td></tr>
        </tbody>
      </table>
    </div>
    <div class="concept-card">
      <div class="concept-label">PARALLEL PLANNING</div>
      <div class="concept-title">Don't Make Your Team Wait on You</div>
      <div class="concept-desc">The biggest lesson from TLP for civilian work: <strong>warning orders enable parallel work</strong>. A weak leader plans everything in silence, then dumps a finished plan on the team at the last minute. A strong leader gives early, partial information ("we'll be migrating the database this weekend — start reviewing the schema") so the team prepares simultaneously. This compresses timelines dramatically and respects your team's ability to contribute.</div>
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
        (THREAT_INJECT_ANCHOR, THREAT_SENTINEL, THREAT_CONTENT),
        (LINUX_INJECT_ANCHOR,  LINUX_SENTINEL,  LINUX_CONTENT),
        (OPS_INJECT_ANCHOR,    OPS_SENTINEL,    OPS_CONTENT),
        (MIL_INJECT_ANCHOR,    MIL_SENTINEL,    MIL_CONTENT),
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
