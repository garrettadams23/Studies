#!/usr/bin/env python3
"""
patch_beginner_concepts_v8.py — Wave 8: Networking depth + pentest starter +
scripting advanced + military comms + shortcuts/productivity deep-dive.

New sentinels:
  BEGINNER8-NET v1      — Switching/VLANs, routing protocols, NAT types
  BEGINNER8-PENTEST v1  — Getting started in ethical hacking, lab setup, legal
  BEGINNER8-SCRIPT v1   — Type hints, dataclasses, testing with pytest
  BEGINNER8-MIL v1      — Military communication standards, SALUTE, SITREP
  BEGINNER8-SHORTCUT v1 — Terminal/command-line productivity, tmux basics
"""
from pathlib import Path

NET_INJECT_ANCHOR      = "<!-- /domain-body net -->"
PENTEST_INJECT_ANCHOR  = "<!-- /domain-body pentest -->"
SCRIPT_INJECT_ANCHOR   = "<!-- /domain-body script -->"
MIL_INJECT_ANCHOR      = "<!-- /domain-body military -->"
SHORTCUT_INJECT_ANCHOR = "<!-- /domain-body shortcut -->"

# ─────────────────────────────── NET wave 8 ──────────────────────────────────
NET_SENTINEL = "<!-- BEGINNER8-NET v1 -->"
NET_CONTENT = """
<!-- BEGINNER8-NET v1 -->
<!-- ── TOPIC: SWITCHING & VLANs ──────────────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">🔀</span>
    <span class="topic-name">Switching &amp; VLANs — Dividing Your Network Logically</span>
    <span class="topic-badge">NET • Foundation</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">SWITCH vs HUB vs ROUTER</div>
      <div class="concept-title">Three Different Devices, Three Layers</div>
      <div class="concept-desc"><strong>Hub</strong> — Layer 1; dumb repeater. Sends every frame to every port. Creates collisions. Legacy/obsolete.<br>
      <strong>Switch</strong> — Layer 2; intelligent. Learns which MAC addresses are on which ports using a MAC address table. Sends frames only to the correct port. Creates collision domains per port.<br>
      <strong>Router</strong> — Layer 3; connects different networks. Uses IP addresses and routing tables to forward packets between subnets and out to the internet.</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">HOW A SWITCH WORKS</div>
      <div class="concept-title">MAC Address Table Learning</div>
      <div class="concept-desc">1. Frame arrives with source MAC AA:BB on port 1 → switch records AA:BB → Port 1 in table.<br>
      2. Destination MAC CC:DD — not in table yet → switch <strong>floods</strong> to all ports except source.<br>
      3. Device CC:DD responds → its MAC gets recorded.<br>
      4. Next frame to CC:DD → switch delivers it only to the correct port.<br>
      This is why switches are efficient — after learning, minimal unnecessary traffic.</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">VLANS</div>
      <div class="concept-title">Virtual LANs — Logical Network Segmentation</div>
      <div class="concept-desc">A VLAN divides one physical switch into multiple logical networks. Devices in different VLANs cannot communicate directly even if they're plugged into the same switch — they need a router (Layer 3) to cross VLAN boundaries. Benefits:<br>
      • <strong>Security</strong>: production servers on VLAN 10, guest WiFi on VLAN 99 — guests can't see servers<br>
      • <strong>Performance</strong>: reduce broadcast domain size<br>
      • <strong>Organization</strong>: group devices by function, not location</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">TRUNK vs ACCESS PORTS</div>
      <div class="concept-title">Single VLAN vs Multiple VLANs</div>
      <div class="concept-desc"><strong>Access port</strong> — carries traffic for exactly ONE VLAN. Used for end devices (PCs, printers). Device doesn't know it's on a VLAN.<br>
      <strong>Trunk port</strong> — carries traffic for MULTIPLE VLANs simultaneously. Used between switches, or switch-to-router. Uses 802.1Q tags to label which VLAN each frame belongs to.</div>
    </div>
    <table class="ai-table">
      <thead><tr><th>Feature</th><th>Access Port</th><th>Trunk Port</th></tr></thead>
      <tbody>
        <tr><td>VLANs carried</td><td>One</td><td>Multiple</td></tr>
        <tr><td>802.1Q tag</td><td>No (stripped)</td><td>Yes (tagged)</td></tr>
        <tr><td>Connected to</td><td>End devices</td><td>Switches, routers, uplinks</td></tr>
        <tr><td>Native VLAN</td><td>N/A</td><td>Untagged VLAN (usually VLAN 1)</td></tr>
      </tbody>
    </table>
  </div>
</div>

<!-- ── TOPIC: ROUTING PROTOCOLS 101 ──────────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">🗺️</span>
    <span class="topic-name">Routing Protocols — How Routers Find the Best Path</span>
    <span class="topic-badge">NET • Intermediate</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">STATIC vs DYNAMIC ROUTING</div>
      <div class="concept-title">Manual Routes vs Self-Learning</div>
      <div class="concept-desc"><strong>Static routes</strong> — an admin manually configures each route. Simple, predictable, no overhead. Works for small networks. Fails when the network changes (adding a link, a failure) because you have to manually update every router.<br>
      <strong>Dynamic routing protocols</strong> — routers talk to each other and automatically discover routes. Self-healing when links fail. Required for large networks.</div>
    </div>
    <table class="ai-table">
      <thead><tr><th>Protocol</th><th>Type</th><th>Algorithm</th><th>Use Case</th></tr></thead>
      <tbody>
        <tr><td>RIP</td><td>Distance Vector</td><td>Hop count (max 15)</td><td>Legacy / tiny networks</td></tr>
        <tr><td>OSPF</td><td>Link State</td><td>Dijkstra (cost)</td><td>Enterprise interior routing</td></tr>
        <tr><td>EIGRP</td><td>Hybrid (Cisco)</td><td>Bandwidth + delay</td><td>Cisco enterprise networks</td></tr>
        <tr><td>BGP</td><td>Path Vector</td><td>Policy-based</td><td>Internet backbone; ISP routing</td></tr>
      </tbody>
    </table>
    <div class="concept-card">
      <div class="concept-label">BGP</div>
      <div class="concept-title">The Protocol That Runs the Internet</div>
      <div class="concept-desc">BGP (Border Gateway Protocol) is used between ISPs and large organizations to exchange routing information across the internet. Every major network has an ASN (Autonomous System Number). BGP is policy-driven — companies can influence which paths their traffic takes. A BGP misconfiguration can accidentally route the internet's traffic through your network (BGP hijacking).</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">DEFAULT ROUTE</div>
      <div class="concept-title">The Fallback Route (0.0.0.0/0)</div>
      <div class="concept-desc">The default route (<code>0.0.0.0/0</code> or <code>::/0</code>) matches ANY destination. It's the "if nothing else matches, send it here" rule — usually pointing to the upstream router or internet gateway. Every end device has a default gateway for this reason.</div>
    </div>
  </div>
</div>
"""

# ─────────────────────────────── PENTEST wave 8 ──────────────────────────────
PENTEST_SENTINEL = "<!-- BEGINNER8-PENTEST v1 -->"
PENTEST_CONTENT = """
<!-- BEGINNER8-PENTEST v1 -->
<!-- ── TOPIC: GETTING STARTED IN ETHICAL HACKING ─────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">🔓</span>
    <span class="topic-name">Getting Started in Ethical Hacking — The Right Way</span>
    <span class="topic-badge">PENTEST • Start Here</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">LEGAL FOUNDATION</div>
      <div class="concept-title">Authorization Is Everything</div>
      <div class="concept-desc">Hacking without permission is a federal crime in the US (CFAA) and illegal worldwide. <strong>Authorization must be explicit, in writing, before you touch anything.</strong> "It was just a test" is not a defense. Ethical hacking means having a signed contract, defined scope, and legal protection before you start.</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">THE LEARNER'S PATH</div>
      <div class="concept-title">Legal Practice Environments</div>
      <div class="concept-desc"><strong>Your own lab</strong>: VMs on your laptop (VirtualBox + Kali Linux + vulnerable VMs like Metasploitable, DVWA). 100% legal, full control.<br>
      <strong>Hack The Box (HTB)</strong>: paid platform with realistic machines to compromise. Legal by design.<br>
      <strong>TryHackMe</strong>: beginner-friendly guided rooms with hand-holding. Best starting point.<br>
      <strong>PicoCTF, CTFtime</strong>: Capture The Flag competitions. Legal challenges with prizes.<br>
      <strong>OWASP WebGoat</strong>: intentionally vulnerable web app for learning web attacks.</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">FOUNDATION KNOWLEDGE</div>
      <div class="concept-title">What to Learn Before "Hacking"</div>
      <div class="concept-desc">The best hackers are really strong defenders first. Build this foundation:<br>
      1. Networking fundamentals (TCP/IP, DNS, HTTP, firewalls)<br>
      2. Linux command line (file system, permissions, processes, scripting)<br>
      3. Programming basics (Python especially — automate, parse, build tools)<br>
      4. Web technology (HTML, HTTP methods, cookies, sessions, same-origin policy)<br>
      5. OS security concepts (users, privilege, authentication)<br>
      6. Cryptography basics (hashing, symmetric, asymmetric)<br>
      Then take CompTIA Security+ → CEH/OSCP path.</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">CERTIFICATIONS</div>
      <div class="concept-title">Industry-Recognized Pentest Certs</div>
      <table class="ai-table">
        <thead><tr><th>Cert</th><th>Level</th><th>Style</th><th>Focus</th></tr></thead>
        <tbody>
          <tr><td>CompTIA Security+</td><td>Beginner</td><td>Multiple choice</td><td>Broad security concepts</td></tr>
          <tr><td>CompTIA PenTest+</td><td>Intermediate</td><td>MC + performance</td><td>Pentest methodology</td></tr>
          <tr><td>CEH (EC-Council)</td><td>Intermediate</td><td>Multiple choice</td><td>Tools and techniques (theory-heavy)</td></tr>
          <tr><td>OSCP (OffSec)</td><td>Advanced</td><td>24-hr practical exam</td><td>Hands-on exploitation; gold standard</td></tr>
          <tr><td>GPEN (GIAC)</td><td>Advanced</td><td>MC + practical</td><td>Network pentesting</td></tr>
        </tbody>
      </table>
    </div>
    <div class="concept-card">
      <div class="concept-label">KALI LINUX</div>
      <div class="concept-title">The Pentest Distro</div>
      <div class="concept-desc">Kali Linux (by Offensive Security) is a Debian-based distro pre-loaded with hundreds of security tools: Nmap, Metasploit, Burp Suite, Wireshark, Aircrack-ng, John the Ripper, Hashcat, and more. <strong>Don't use Kali as your daily driver</strong> — it runs as root by default and is designed for testing, not everyday use. Run it in a VM or bootable USB for lab work.</div>
    </div>
  </div>
</div>

<!-- ── TOPIC: BASIC RECON & ENUMERATION ──────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">🔍</span>
    <span class="topic-name">Basic Recon &amp; Enumeration — Know Your Target</span>
    <span class="topic-badge">PENTEST • Foundation</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">PASSIVE vs ACTIVE RECON</div>
      <div class="concept-title">Invisible vs Detectable</div>
      <div class="concept-desc"><strong>Passive recon</strong> — gather information WITHOUT touching the target. No packets sent to their systems. Examples: WHOIS, DNS lookups, Google dorking, LinkedIn, Shodan, certificate transparency logs. Hard to detect.<br>
      <strong>Active recon</strong> — directly query the target's systems. Port scans, banner grabbing, web crawling. Generates logs on their end. Only legal with authorization.</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">NMAP BASICS</div>
      <div class="concept-title">The Port Scanner Every Tester Uses</div>
      <div class="code-block"><span class="com"># Quick scan — top 1000 ports</span>
nmap 192.168.1.1

<span class="com"># SYN scan (stealthier, requires root)</span>
sudo nmap -sS 192.168.1.1

<span class="com"># Service/version detection</span>
nmap -sV 192.168.1.1

<span class="com"># OS fingerprinting</span>
sudo nmap -O 192.168.1.1

<span class="com"># Full scan: all ports + service + OS + scripts</span>
sudo nmap -A -p- 192.168.1.1

<span class="com"># Scan a range</span>
nmap 192.168.1.0/24

<span class="com"># Output to file</span>
nmap -oA scan_results 192.168.1.1</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">OSINT TOOLS</div>
      <div class="concept-title">Open-Source Intelligence</div>
      <div class="concept-desc"><strong>Shodan</strong> — search engine for internet-connected devices. Find exposed cameras, industrial control systems, unpatched servers.<br>
      <strong>theHarvester</strong> — collect emails, subdomains, hosts from public sources.<br>
      <strong>Maltego</strong> — visual relationship mapping (person → email → domain → IP → org).<br>
      <strong>Google Dorks</strong> — advanced Google search operators to find sensitive files: <code>site:example.com filetype:pdf "confidential"</code><br>
      <strong>crt.sh</strong> — certificate transparency logs; find all subdomains of a domain.</div>
    </div>
  </div>
</div>
"""

# ─────────────────────────────── SCRIPTING wave 8 ────────────────────────────
SCRIPT_SENTINEL = "<!-- BEGINNER8-SCRIPT v1 -->"
SCRIPT_CONTENT = """
<!-- BEGINNER8-SCRIPT v1 -->
<!-- ── TOPIC: TYPE HINTS & DATACLASSES ───────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">🏷️</span>
    <span class="topic-name">Type Hints &amp; Dataclasses — Self-Documenting Code</span>
    <span class="topic-badge">SCRIPT • Intermediate</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">TYPE HINTS</div>
      <div class="concept-title">Optional but Powerful Annotations</div>
      <div class="concept-desc">Python is dynamically typed but supports optional type annotations. Type hints don't change runtime behavior — they're documentation AND they enable static analysis tools (mypy, pyright) to catch type errors before running.</div>
      <div class="code-block"><span class="kw">from</span> typing <span class="kw">import</span> Optional, List, Dict, Tuple, Union

<span class="com"># Basic function with type hints</span>
<span class="kw">def</span> <span class="fn">greet</span>(name: str, count: int = <span class="num">1</span>) -> str:
    <span class="kw">return</span> <span class="str">f"Hello, {name}! "</span> * count

<span class="com"># Optional — can be None</span>
<span class="kw">def</span> <span class="fn">find_user</span>(user_id: int) -> Optional[str]:
    <span class="kw">return</span> database.get(user_id)   <span class="com"># may be None</span>

<span class="com"># Collections</span>
<span class="kw">def</span> <span class="fn">process</span>(items: List[str]) -> Dict[str, int]:
    <span class="kw">return</span> {item: <span class="fn">len</span>(item) <span class="kw">for</span> item <span class="kw">in</span> items}

<span class="com"># Python 3.10+ — simpler union syntax</span>
<span class="kw">def</span> <span class="fn">maybe</span>(val: str | <span class="kw">None</span>) -> int | str:
    <span class="kw">return</span> <span class="fn">len</span>(val) <span class="kw">if</span> val <span class="kw">else</span> <span class="str">"empty"</span></div>
    </div>
    <div class="concept-card">
      <div class="concept-label">DATACLASSES</div>
      <div class="concept-title">Structured Data Without Boilerplate</div>
      <div class="concept-desc">Dataclasses auto-generate <code>__init__</code>, <code>__repr__</code>, <code>__eq__</code> based on your field definitions. Less code, more clarity.</div>
      <div class="code-block"><span class="kw">from</span> dataclasses <span class="kw">import</span> dataclass, field
<span class="kw">from</span> datetime <span class="kw">import</span> datetime

@dataclass
<span class="kw">class</span> <span class="fn">User</span>:
    name: str
    email: str
    age: int
    active: bool = <span class="kw">True</span>
    tags: list = field(default_factory=<span class="fn">list</span>)  <span class="com"># mutable default</span>
    created: datetime = field(default_factory=datetime.now)

<span class="com"># __init__ is auto-generated</span>
alice = <span class="fn">User</span>(<span class="str">"Alice"</span>, <span class="str">"alice@example.com"</span>, <span class="num">30</span>)

<span class="com"># __repr__ is auto-generated</span>
<span class="fn">print</span>(alice)  <span class="com"># User(name='Alice', email='alice@example.com', ...)</span>

<span class="com"># __eq__ is auto-generated</span>
bob1 = <span class="fn">User</span>(<span class="str">"Bob"</span>, <span class="str">"bob@example.com"</span>, <span class="num">25</span>)
bob2 = <span class="fn">User</span>(<span class="str">"Bob"</span>, <span class="str">"bob@example.com"</span>, <span class="num">25</span>)
<span class="fn">print</span>(bob1 == bob2)   <span class="com"># True</span>

<span class="com"># Frozen (immutable) dataclass</span>
@dataclass(frozen=<span class="kw">True</span>)
<span class="kw">class</span> <span class="fn">Point</span>:
    x: float
    y: float</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">NAMED TUPLES</div>
      <div class="concept-title">Lightweight Immutable Records</div>
      <div class="code-block"><span class="kw">from</span> typing <span class="kw">import</span> NamedTuple

<span class="kw">class</span> <span class="fn">Color</span>(NamedTuple):
    red: int
    green: int
    blue: int
    alpha: int = <span class="num">255</span>

red = <span class="fn">Color</span>(<span class="num">255</span>, <span class="num">0</span>, <span class="num">0</span>)
<span class="fn">print</span>(red.red)      <span class="com"># 255  — named access</span>
<span class="fn">print</span>(red[<span class="num">0</span>])       <span class="com"># 255  — index access</span>
r, g, b, a = red    <span class="com"># unpacking works</span></div>
    </div>
  </div>
</div>

<!-- ── TOPIC: TESTING WITH PYTEST ────────────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">🧪</span>
    <span class="topic-name">Testing With pytest — Prove Your Code Works</span>
    <span class="topic-badge">SCRIPT • Professional</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">WHY TEST</div>
      <div class="concept-title">Tests Are Proof + Future-Proofing</div>
      <div class="concept-desc">Tests prove your code does what you think it does. More importantly, they let you change code confidently — if the tests still pass, you haven't broken anything. No tests → every change is a gamble. Professional code has tests. Security code ESPECIALLY needs tests (what happens on malformed input?).</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">YOUR FIRST TEST</div>
      <div class="concept-title">Create test_math.py</div>
      <div class="code-block"><span class="com"># File: test_math.py</span>
<span class="com"># Convention: test files start with test_, test functions start with test_</span>

<span class="kw">def</span> <span class="fn">add</span>(a, b):
    <span class="kw">return</span> a + b

<span class="kw">def</span> <span class="fn">divide</span>(a, b):
    <span class="kw">if</span> b == <span class="num">0</span>:
        <span class="kw">raise</span> ValueError(<span class="str">"Cannot divide by zero"</span>)
    <span class="kw">return</span> a / b

<span class="com"># Tests</span>
<span class="kw">def</span> <span class="fn">test_add</span>():
    <span class="kw">assert</span> <span class="fn">add</span>(<span class="num">2</span>, <span class="num">3</span>) == <span class="num">5</span>
    <span class="kw">assert</span> <span class="fn">add</span>(-<span class="num">1</span>, <span class="num">1</span>) == <span class="num">0</span>
    <span class="kw">assert</span> <span class="fn">add</span>(<span class="num">0</span>, <span class="num">0</span>) == <span class="num">0</span>

<span class="kw">def</span> <span class="fn">test_divide</span>():
    <span class="kw">assert</span> <span class="fn">divide</span>(<span class="num">10</span>, <span class="num">2</span>) == <span class="num">5.0</span>

<span class="kw">def</span> <span class="fn">test_divide_by_zero</span>():
    <span class="kw">import</span> pytest
    <span class="kw">with</span> pytest.raises(ValueError):
        <span class="fn">divide</span>(<span class="num">5</span>, <span class="num">0</span>)</div>
      <div class="concept-desc">Run: <code>pip install pytest</code> then <code>pytest test_math.py -v</code></div>
    </div>
    <div class="concept-card">
      <div class="concept-label">FIXTURES</div>
      <div class="concept-title">Shared Setup Code</div>
      <div class="code-block"><span class="kw">import</span> pytest

@pytest.fixture
<span class="kw">def</span> <span class="fn">sample_user</span>():
    <span class="com"># Runs before each test that requests it</span>
    <span class="kw">return</span> {<span class="str">"name"</span>: <span class="str">"Alice"</span>, <span class="str">"email"</span>: <span class="str">"alice@test.com"</span>, <span class="str">"age"</span>: <span class="num">30</span>}

<span class="kw">def</span> <span class="fn">test_user_name</span>(sample_user):    <span class="com"># pytest auto-injects the fixture</span>
    <span class="kw">assert</span> sample_user[<span class="str">"name"</span>] == <span class="str">"Alice"</span>

<span class="kw">def</span> <span class="fn">test_user_email</span>(sample_user):
    <span class="kw">assert</span> <span class="str">"@"</span> <span class="kw">in</span> sample_user[<span class="str">"email"</span>]</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">PARAMETRIZE</div>
      <div class="concept-title">Run One Test With Many Inputs</div>
      <div class="code-block">@pytest.mark.parametrize(<span class="str">"a, b, expected"</span>, [
    (<span class="num">1</span>, <span class="num">2</span>, <span class="num">3</span>),
    (<span class="num">0</span>, <span class="num">0</span>, <span class="num">0</span>),
    (-<span class="num">1</span>, <span class="num">1</span>, <span class="num">0</span>),
    (<span class="num">100</span>, -<span class="num">50</span>, <span class="num">50</span>),
])
<span class="kw">def</span> <span class="fn">test_add_many</span>(a, b, expected):
    <span class="kw">assert</span> <span class="fn">add</span>(a, b) == expected</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">COVERAGE</div>
      <div class="concept-title">How Much of Your Code Is Tested?</div>
      <div class="code-block"><span class="com"># Install pytest-cov</span>
pip install pytest-cov

<span class="com"># Run tests with coverage report</span>
pytest --cov=mymodule --cov-report=html

<span class="com"># View htmlcov/index.html to see untested lines</span></div>
      <div class="concept-desc">Aim for 80%+ coverage on core logic. 100% is rarely worth the diminishing returns. Coverage measures LINES tested, not BEHAVIOR tested — write meaningful tests, not box-checking tests.</div>
    </div>
  </div>
</div>
"""

# ─────────────────────────────── MILITARY wave 8 ─────────────────────────────
MIL_SENTINEL = "<!-- BEGINNER8-MIL v1 -->"
MIL_CONTENT = """
<!-- BEGINNER8-MIL v1 -->
<!-- ── TOPIC: MILITARY COMMUNICATION STANDARDS ──────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">📻</span>
    <span class="topic-name">Military Communication Standards — Clear, Concise, Correct</span>
    <span class="topic-badge">MIL • Foundation</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">WHY MILITARY COMMS</div>
      <div class="concept-title">When Miscommunication Costs Lives</div>
      <div class="concept-desc">Military communication standards were designed for high-stress, noisy, partial-information environments where a misunderstood message can have catastrophic consequences. These principles apply directly to IT operations, incident response, and emergency management — anywhere clarity under pressure matters.</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">SALUTE REPORT</div>
      <div class="concept-title">Size · Activity · Location · Unit · Time · Equipment</div>
      <div class="concept-desc">A SALUTE report is a standardized format for reporting enemy contact or suspicious activity. Gives responders exactly what they need, in the right order, nothing extra.</div>
      <table class="ai-table">
        <thead><tr><th>Letter</th><th>Field</th><th>Example</th></tr></thead>
        <tbody>
          <tr><td>S</td><td>Size</td><td>3 individuals</td></tr>
          <tr><td>A</td><td>Activity</td><td>Moving northbound along the road</td></tr>
          <tr><td>L</td><td>Location</td><td>Grid 123456, 500m east of checkpoint</td></tr>
          <tr><td>U</td><td>Unit/Uniform</td><td>Civilian clothing, no visible insignia</td></tr>
          <tr><td>T</td><td>Time</td><td>0830 local</td></tr>
          <tr><td>E</td><td>Equipment</td><td>Armed, backpacks, one vehicle</td></tr>
        </tbody>
      </table>
      <div class="concept-desc"><strong>IT application</strong>: Use SALUTE-style structured reporting for security incidents — "3 systems affected, lateral movement detected, VLAN 10, identified at 14:32 UTC, using PSExec and Mimikatz."</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">SITREP</div>
      <div class="concept-title">Situation Report — Periodic Status Update</div>
      <div class="concept-desc">A SITREP (Situation Report) is a standardized periodic update on current status. Key elements:<br>
      <strong>Current situation</strong> — what is happening right now<br>
      <strong>What has been accomplished</strong> — progress since last report<br>
      <strong>Next actions</strong> — what you're about to do<br>
      <strong>Issues/requests</strong> — what you need from higher command<br>
      Format matters: be concise, use the same structure every time, report at agreed intervals (even "no change" is information).</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">RADIO PROCEDURE</div>
      <div class="concept-title">Pro-Words (Procedural Words)</div>
      <table class="ai-table">
        <thead><tr><th>Pro-Word</th><th>Meaning</th></tr></thead>
        <tbody>
          <tr><td>OVER</td><td>My transmission is complete; I expect a reply</td></tr>
          <tr><td>OUT</td><td>Conversation is finished; no reply expected</td></tr>
          <tr><td>ROGER</td><td>I received and understood your last message</td></tr>
          <tr><td>WILCO</td><td>I understand and WILL comply (includes Roger)</td></tr>
          <tr><td>SAY AGAIN</td><td>Repeat your last transmission (not "repeat" — that has an artillery meaning)</td></tr>
          <tr><td>BREAK</td><td>Short pause in a long transmission</td></tr>
          <tr><td>STANDBY</td><td>Wait, I'll get back to you</td></tr>
          <tr><td>NEGATIVE</td><td>No / incorrect</td></tr>
          <tr><td>AFFIRM</td><td>Yes / correct</td></tr>
        </tbody>
      </table>
    </div>
    <div class="concept-card">
      <div class="concept-label">BREVITY IN ALL COMMS</div>
      <div class="concept-title">Say It Once, Say It Right</div>
      <div class="concept-desc">Military communication demands brevity because radio time is shared, batteries die, and enemies can intercept. The principle: say everything necessary, nothing more. In IT: this same discipline makes incident bridge calls, escalation emails, and Slack channels dramatically more effective. State the problem, the impact, what you've tried, what you need — then stop talking.</div>
    </div>
  </div>
</div>
"""

# ─────────────────────────────── SHORTCUT wave 8 ─────────────────────────────
SHORTCUT_SENTINEL = "<!-- BEGINNER8-SHORTCUT v1 -->"
SHORTCUT_CONTENT = """
<!-- BEGINNER8-SHORTCUT v1 -->
<!-- ── TOPIC: TERMINAL PRODUCTIVITY ──────────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">💻</span>
    <span class="topic-name">Terminal Productivity — Work Faster at the Command Line</span>
    <span class="topic-badge">SHORTCUT • Practical</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">BASH READLINE SHORTCUTS</div>
      <div class="concept-title">Move Without the Arrow Keys</div>
      <table class="ai-table">
        <thead><tr><th>Shortcut</th><th>Action</th></tr></thead>
        <tbody>
          <tr><td>Ctrl+A</td><td>Move cursor to beginning of line</td></tr>
          <tr><td>Ctrl+E</td><td>Move cursor to end of line</td></tr>
          <tr><td>Ctrl+F / Ctrl+B</td><td>Move forward/back one character</td></tr>
          <tr><td>Alt+F / Alt+B</td><td>Move forward/back one WORD</td></tr>
          <tr><td>Ctrl+W</td><td>Delete word before cursor</td></tr>
          <tr><td>Alt+D</td><td>Delete word after cursor</td></tr>
          <tr><td>Ctrl+K</td><td>Delete from cursor to end of line</td></tr>
          <tr><td>Ctrl+U</td><td>Delete from cursor to beginning of line</td></tr>
          <tr><td>Ctrl+Y</td><td>Paste (yank) deleted text back</td></tr>
          <tr><td>Ctrl+R</td><td>Reverse search command history (type to filter)</td></tr>
          <tr><td>Ctrl+G</td><td>Cancel current history search</td></tr>
          <tr><td>!!</td><td>Repeat last command</td></tr>
          <tr><td>!$</td><td>Last argument of previous command</td></tr>
          <tr><td>Alt+.</td><td>Insert last argument of previous command</td></tr>
        </tbody>
      </table>
    </div>
    <div class="concept-card">
      <div class="concept-label">HISTORY TRICKS</div>
      <div class="concept-title">Never Retype Long Commands</div>
      <div class="code-block"><span class="com"># See your command history</span>
history | tail -20

<span class="com"># Run command #42 from history</span>
!42

<span class="com"># Run last command starting with "nmap"</span>
!nmap

<span class="com"># Substitute in last command (fix typos fast)</span>
<span class="com"># If you typed: cat /etc/paaswd</span>
^paaswd^passwd    <span class="com"># re-runs with correction</span>

<span class="com"># Search history with fzf (install separately)</span>
Ctrl+R   <span class="com"># built-in incremental search</span></div>
    </div>
    <div class="concept-card">
      <div class="concept-label">TMUX BASICS</div>
      <div class="concept-title">Multiple Terminals in One Window</div>
      <div class="concept-desc">tmux is a terminal multiplexer — splits your terminal into multiple panes, creates persistent sessions that survive network disconnects, and lets you detach/reattach from long-running tasks.</div>
      <div class="code-block"><span class="com"># Start new session</span>
tmux new -s mysession

<span class="com"># Detach (leaves session running)</span>
Ctrl+B then D

<span class="com"># Reattach later</span>
tmux attach -t mysession

<span class="com"># Key bindings (all start with Ctrl+B, the prefix)</span>
<span class="com"># Split horizontally</span>
Ctrl+B then %

<span class="com"># Split vertically</span>
Ctrl+B then "

<span class="com"># Move between panes</span>
Ctrl+B then arrow key

<span class="com"># New window (tab)</span>
Ctrl+B then C

<span class="com"># Switch windows</span>
Ctrl+B then N / P

<span class="com"># Kill current pane</span>
Ctrl+B then X</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">ALIASES</div>
      <div class="concept-title">Shortcut Your Most-Used Commands</div>
      <div class="code-block"><span class="com"># Add to ~/.bashrc or ~/.zshrc</span>

<span class="com"># Shorter ls with detail</span>
alias ll=<span class="str">'ls -lah --color=auto'</span>

<span class="com"># Never accidentally remove files</span>
alias rm=<span class="str">'rm -i'</span>

<span class="com"># Quick git shortcuts</span>
alias gs=<span class="str">'git status'</span>
alias gd=<span class="str">'git diff'</span>
alias gl=<span class="str">'git log --oneline --graph -20'</span>

<span class="com"># SSH with key timeout</span>
alias ssha=<span class="str">'eval $(ssh-agent) &amp;&amp; ssh-add'</span>

<span class="com"># Python shortcut</span>
alias py=<span class="str">'python3'</span>

<span class="com"># Apply changes</span>
source ~/.bashrc</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">PIPES & REDIRECTION</div>
      <div class="concept-title">Compose Powerful One-Liners</div>
      <div class="code-block"><span class="com"># | pipes output of one command into next</span>
ps aux | grep python | grep -v grep

<span class="com"># &gt; overwrites file, &gt;&gt; appends</span>
<span class="fn">echo</span> <span class="str">"hello"</span> &gt; output.txt
<span class="fn">echo</span> <span class="str">"world"</span> &gt;&gt; output.txt

<span class="com"># 2&gt; redirects stderr, 2&gt;&amp;1 merges with stdout</span>
command &gt; out.log 2&gt;&amp;1

<span class="com"># /dev/null discards output</span>
command &gt; /dev/null 2&gt;&amp;1

<span class="com"># tee: write to file AND stdout simultaneously</span>
<span class="fn">ls</span> -la | tee listing.txt

<span class="com"># xargs: turn output into arguments</span>
find . -name <span class="str">"*.tmp"</span> | xargs rm -f</div>
    </div>
  </div>
</div>
"""


def patch(filepath: str, sentinel: str, inject_content: str, inject_anchor: str):
    path = Path(filepath)
    content = path.read_text(encoding="utf-8")

    if sentinel in content:
        print(f"  [skip] {sentinel} already present in {path.name}")
        return False

    if inject_anchor not in content:
        print(f"  [ERROR] Anchor not found: {inject_anchor!r} in {path.name}")
        return False

    new_content = content.replace(inject_anchor, inject_content + "\n" + inject_anchor)
    path.write_text(new_content, encoding="utf-8")
    added = len(new_content) - len(content)
    print(f"  [ok] Injected {added:+,} chars before {inject_anchor!r} in {path.name}")
    return True


def main():
    target = "index.html"

    results = [
        patch(target, NET_SENTINEL,      NET_CONTENT,      NET_INJECT_ANCHOR),
        patch(target, PENTEST_SENTINEL,  PENTEST_CONTENT,  PENTEST_INJECT_ANCHOR),
        patch(target, SCRIPT_SENTINEL,   SCRIPT_CONTENT,   SCRIPT_INJECT_ANCHOR),
        patch(target, MIL_SENTINEL,      MIL_CONTENT,      MIL_INJECT_ANCHOR),
        patch(target, SHORTCUT_SENTINEL, SHORTCUT_CONTENT, SHORTCUT_INJECT_ANCHOR),
    ]

    if any(results):
        from html.parser import HTMLParser

        class BalanceChecker(HTMLParser):
            VOID = {"area","base","br","col","embed","hr","img","input","link","meta","param","source","track","wbr"}
            def __init__(self):
                super().__init__()
                self.stack = []
                self.strays = []
            def handle_starttag(self, tag, attrs):
                if tag not in self.VOID:
                    self.stack.append(tag)
            def handle_endtag(self, tag):
                if tag in self.VOID:
                    return
                if self.stack and self.stack[-1] == tag:
                    self.stack.pop()
                else:
                    self.strays.append(tag)

        checker = BalanceChecker()
        checker.feed(Path(target).read_text(encoding="utf-8"))
        print(f"\n  Unclosed at EOF: {checker.stack[-5:] if checker.stack else 'NONE'}")
        print(f"  Stray end tags: {len(checker.strays)}")

        new_len = Path(target).stat().st_size
        print(f"\n  {target}: {new_len:,} bytes")


if __name__ == "__main__":
    main()
