#!/usr/bin/env python3
"""Wave 33 – Wireless security, threat hunting, SOC 2, Python async, OPSEC."""
from pathlib import Path
from html.parser import HTMLParser

S_NET      = "<!-- BEGINNER33-NET v1 -->"
S_THREAT   = "<!-- BEGINNER33-THREAT v1 -->"
S_GRC      = "<!-- BEGINNER33-GRC v1 -->"
S_SCRIPT   = "<!-- BEGINNER33-SCRIPT v1 -->"
S_MILITARY = "<!-- BEGINNER33-MILITARY v1 -->"

A_NET      = "<!-- /domain-body net -->"
A_THREAT   = "<!-- /domain-body threat -->"
A_GRC      = "<!-- /domain-body grc -->"
A_SCRIPT   = "<!-- /domain-body script -->"
A_MILITARY = "<!-- /domain-body military -->"

# ══════════════════════════════════════════════════════════════════════════
# NET – Wireless / 802.11 security
# ══════════════════════════════════════════════════════════════════════════
C_NET = """
<!-- BEGINNER33-NET v1 -->
<!-- ── TOPIC: Wireless Security – 802.11 ─────────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-badge">Beginner</span>
    Wireless Security – 802.11 Standards &amp; Wi-Fi Hardening
  </div>
  <div class="topic-body">

    <div class="concept-card">
      <div class="concept-label">Core Concept</div>
      <div class="concept-title">Wi-Fi Security Evolution: WEP → WPA3</div>
      <div class="concept-desc">
        Wi-Fi security has gone through several generations. Knowing the
        history helps you understand why old protocols are dangerous:<br><br>
        <table class="ai-table">
          <tr><th>Protocol</th><th>Year</th><th>Encryption</th><th>Status</th></tr>
          <tr><td>WEP</td><td>1997</td><td>RC4 (broken)</td><td>Never use</td></tr>
          <tr><td>WPA (TKIP)</td><td>2003</td><td>RC4 improved</td><td>Avoid</td></tr>
          <tr><td>WPA2-Personal</td><td>2004</td><td>AES-CCMP</td><td>OK with strong passphrase</td></tr>
          <tr><td>WPA2-Enterprise</td><td>2004</td><td>AES + 802.1X/RADIUS</td><td>Recommended for orgs</td></tr>
          <tr><td>WPA3-Personal</td><td>2018</td><td>AES + SAE</td><td>Best for home/small biz</td></tr>
          <tr><td>WPA3-Enterprise</td><td>2018</td><td>AES-256 + SAE</td><td>Best for enterprise</td></tr>
        </table>
        <br>
        <strong>WPA2-Personal weakness:</strong> offline dictionary attacks
        against the 4-way handshake. A weak passphrase = cracked in hours.
        <br><strong>WPA3 fix:</strong> SAE (Simultaneous Authentication of
        Equals) prevents offline cracking — each authentication is unique.
      </div>
    </div>

    <div class="concept-card">
      <div class="concept-label">Enterprise Wi-Fi</div>
      <div class="concept-title">WPA2-Enterprise with RADIUS</div>
      <div class="concept-desc">
        In corporate environments, each user authenticates with their own
        AD credentials rather than a shared passphrase. This uses
        <strong>802.1X</strong> and a <strong>RADIUS server</strong>
        (FreeRADIUS or Windows NPS).<br><br>
        Benefits:<br>
        &bull; No shared secret to leak — each user has unique creds.<br>
        &bull; Revoke a single user's access without changing the Wi-Fi
          password for everyone.<br>
        &bull; Full audit trail of who connected when.<br>
        &bull; Mutual authentication via certificates prevents evil-twin
          attacks.
      </div>
      <div class="code-block">
<span class="com"># FreeRADIUS quick test (after setup)</span>
radtest alice Password1 localhost 0 testing123
<span class="com"># Output: Access-Accept → credentials valid</span>
<span class="com"># Output: Access-Reject  → bad credentials</span>

<span class="com">── Key 802.1X flow ──────────────────────────────────────────</span>
Client (Supplicant)  →  AP (Authenticator)  →  RADIUS Server
       EAP-Request/Identity
&lt;──────────────────────────────────────────────────────────
       EAP-Response/Identity (alice@corp.com)
──────────────────────────────────────────────────────────&gt;
       RADIUS Access-Request (forwarded)
                             ──────────────────────────────&gt;
       RADIUS Access-Accept / Reject
                             &lt;──────────────────────────────
       EAP-Success / Failure
&lt;──────────────────────────────────────────────────────────
       [4-way handshake to derive per-session keys]
      </div>
    </div>

    <div class="concept-card">
      <div class="concept-label">Attacks</div>
      <div class="concept-title">Common Wi-Fi Attacks &amp; Defences</div>
      <div class="concept-desc">
        <em>"Assume" makes an ass out of you and me</em> — never assume
        the Wi-Fi network you're on is the real one. Rogue APs can be
        set up in minutes.
      </div>
      <div class="code-block">
<span class="com">Attack          Description                          Defence</span>
Evil Twin       Fake AP with same SSID captures creds  WPA3/EAP-TLS cert auth
Deauth flood    Force clients to reconnect (DOS)        802.11w Management Frame Protection
PMKID attack    Capture beacon, crack offline           Long random WPA2 passphrase
KRACK           Key reinstallation in WPA2 handshake    Patch all clients and APs
WPS PIN bruteforce 8-digit PIN cracked in hours         Disable WPS entirely

<span class="com"># Check if a Linux NIC supports monitor mode</span>
iw list | grep -A5 <span class="str">"Supported interface modes"</span>
<span class="com"># Must show "monitor" mode for wireless analysis tools</span>

<span class="com"># Detect rogue APs on your network (passive scan)</span>
sudo iwlist wlan0 scanning | grep -E <span class="str">"(ESSID|Address|Encryption)"</span>
<span class="com"># Compare BSSID (MAC) list against your authorised AP inventory</span>

<span class="com"># Check if WPS is enabled (vulnerable)</span>
sudo wash -i wlan0 -C   <span class="com"># part of reaver suite; scan for WPS-enabled APs</span>
      </div>
    </div>

    <div class="concept-card">
      <div class="concept-label">Hardening</div>
      <div class="concept-title">Wi-Fi Network Design Best Practices</div>
      <div class="concept-desc">
        &bull; Use <strong>WPA3</strong> where supported; WPA2-Enterprise
          for corporate devices.<br>
        &bull; <strong>Separate SSIDs for different trust levels</strong>:
          Corp, Guest, IoT — each on its own VLAN.<br>
        &bull; Guest SSID: internet-only; no access to internal resources.<br>
        &bull; <strong>Disable SSID broadcast</strong> only adds minor
          friction — determined attackers still find hidden SSIDs. Don't
          rely on it for security.<br>
        &bull; Enable <strong>802.11w</strong> (Management Frame Protection)
          to block deauthentication attacks.<br>
        &bull; Use a <strong>long, random passphrase</strong> (&gt;20 chars)
          for WPA2-Personal — mix upper/lower/digit/symbol.<br>
        &bull; Audit connected clients quarterly; disable MAC addresses
          that no longer belong to active employees/devices.<br>
        &bull; <em>You can't make someone make the right choice, yet you
          can pick up the pieces afterwards</em> — when an employee
          connects a personal rogue AP, your WIDS (Wireless IDS) catches
          it; have a process to contain it quickly.
      </div>
    </div>

  </div>
</div>
"""

# ══════════════════════════════════════════════════════════════════════════
# THREAT – Threat hunting methodology
# ══════════════════════════════════════════════════════════════════════════
C_THREAT = """
<!-- BEGINNER33-THREAT v1 -->
<!-- ── TOPIC: Threat Hunting Methodology ─────────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-badge">Beginner</span>
    Threat Hunting – Finding What Detection Missed
  </div>
  <div class="topic-body">

    <div class="concept-card">
      <div class="concept-label">Core Concept</div>
      <div class="concept-title">What Is Threat Hunting?</div>
      <div class="concept-desc">
        <strong>Threat hunting</strong> is the proactive, hypothesis-driven
        search for threats that automated detection has missed.
        A SIEM fires alerts when rules match — but sophisticated attackers
        live below the alert threshold (low-and-slow attacks, living-off-the-land).<br><br>
        <strong>Reactive (SIEM)</strong>: Wait for an alert → investigate.<br>
        <strong>Proactive (Hunting)</strong>: Form a hypothesis → search
        for evidence → prove or disprove it.<br><br>
        <em>"Not my circus, not my monkey"</em> — threat hunting is a
        specialised skill, but junior analysts can learn the mindset: always
        ask "what would an attacker do that looks normal?"
      </div>
    </div>

    <div class="concept-card">
      <div class="concept-label">Process</div>
      <div class="concept-title">The Hunt Loop</div>
      <div class="concept-desc">
        Every hunt follows the same loop:
      </div>
      <div class="code-block">
<span class="com">1. FORM HYPOTHESIS</span>
   "Attackers using PowerShell for lateral movement would show
    powershell.exe spawned by a non-interactive parent process
    (e.g. wsmprovhost, mmc, svchost) running encoded commands."

<span class="com">2. COLLECT RELEVANT DATA</span>
   Pull process creation events (Event ID 4688 or Sysmon Event 1)
   Filter: ParentImage ends with wsmprovhost.exe OR mmc.exe
           AND CommandLine contains -EncodedCommand OR -Enc

<span class="com">3. ANALYSE</span>
   Cluster results by user, host, time
   Look for outliers — rare parents, unusual times, unexpected users

<span class="com">4. INVESTIGATE ANOMALIES</span>
   Pivot: what did the process do next? (child processes, network, files)
   Corroborate: does EDR show the same activity?

<span class="com">5. OUTCOME</span>
   TRUE POSITIVE  → Incident response
   FALSE POSITIVE → Document; tune detection rules
   INCONCLUSIVE   → Expand data sources; reformulate hypothesis

<span class="com">6. CREATE DETECTION RULE</span>
   Turn confirmed attacker behaviour into an automated SIEM rule
   so the hunt never needs to be repeated manually
      </div>
    </div>

    <div class="concept-card">
      <div class="concept-label">MITRE ATT&amp;CK</div>
      <div class="concept-title">Using ATT&amp;CK as a Hunting Framework</div>
      <div class="concept-desc">
        <strong>MITRE ATT&amp;CK</strong> is a knowledge base of adversary
        tactics and techniques based on real-world attacks. It gives
        hunters a <em>menu of hypotheses</em>:<br><br>
        &bull; Tactics = <em>why</em> (Initial Access, Execution,
          Persistence, Lateral Movement, Exfiltration…)<br>
        &bull; Techniques = <em>how</em> (T1059 – Command and Scripting
          Interpreter, T1078 – Valid Accounts…)<br>
        &bull; Sub-techniques = specific implementations<br><br>
        Workflow:<br>
        1. Pick a tactic (e.g. Persistence).<br>
        2. List techniques relevant to your environment.<br>
        3. Form a hypothesis for each technique.<br>
        4. Hunt.<br>
        5. Document coverage on your ATT&amp;CK matrix.
      </div>
      <div class="code-block">
<span class="com"># Splunk hunt: T1053.005 – Scheduled Task/Job (Windows)</span>
index=windows (EventCode=<span class="num">4698</span> OR EventCode=<span class="num">4702</span>)
| eval suspicious=if(like(TaskContent,<span class="str">"%powershell%"</span>)
                  OR like(TaskContent,<span class="str">"%cmd.exe%"</span>)
                  OR like(TaskContent,<span class="str">"%wscript%"</span>),<span class="str">"YES"</span>,<span class="str">"NO"</span>)
| where suspicious=<span class="str">"YES"</span>
| stats count by ComputerName, SubjectUserName, TaskName

<span class="com"># Linux hunt: T1136.001 – Create Local Account</span>
grep <span class="str">"new user"</span> /var/log/auth.log | \
  awk <span class="str">'{print $1,$2,$3,$NF}'</span> | sort

<span class="com"># Hunt for DNS tunnelling: unusually long hostnames</span>
<span class="com"># Splunk SPL:</span>
index=dns
| eval qlen=len(query)
| where qlen &gt; <span class="num">50</span>
| stats count, values(query) by src_ip
| sort -count
      </div>
    </div>

    <div class="concept-card">
      <div class="concept-label">Tools</div>
      <div class="concept-title">Essential Threat Hunting Tools</div>
      <div class="concept-desc">
        &bull; <strong>Sysmon</strong> (Windows) — enriches Windows event
          logs with process GUID, parent-child relationships, network
          connections, and file hashes. Free from Microsoft Sysinternals.<br>
        &bull; <strong>Velociraptor</strong> — open-source agent for rapid
          endpoint forensics and hunting at scale.<br>
        &bull; <strong>osquery</strong> — SQL interface to OS internals;
          ask "SELECT name, pid FROM processes WHERE name LIKE '%powershell%'."<br>
        &bull; <strong>SIGMA</strong> — generic detection rule format that
          converts to Splunk, Elastic, QRadar queries.
        Hunters write SIGMA rules to share TTP detection across SIEM
        platforms.
      </div>
      <div class="code-block">
<span class="com"># osquery – live process inspection (runs on Windows/Linux/macOS)</span>
osqueryi
<span class="kw">SELECT</span> name, pid, parent, cmdline
<span class="kw">FROM</span>  processes
<span class="kw">WHERE</span> name <span class="kw">LIKE</span> <span class="str">'%powershell%'</span>
<span class="kw">   OR</span> cmdline <span class="kw">LIKE</span> <span class="str">'%-EncodedCommand%'</span>;

<span class="com"># Find all network connections to suspicious ports</span>
<span class="kw">SELECT</span> p.name, p.pid, n.local_port, n.remote_address, n.remote_port, n.state
<span class="kw">FROM</span>  process_open_sockets n
<span class="kw">JOIN</span>  processes p <span class="kw">ON</span> p.pid = n.pid
<span class="kw">WHERE</span> n.remote_port <span class="kw">NOT IN</span> (<span class="num">80</span>, <span class="num">443</span>, <span class="num">53</span>, <span class="num">123</span>)
  <span class="kw">AND</span> n.state = <span class="str">'ESTABLISHED'</span>;
      </div>
    </div>

  </div>
</div>
"""

# ══════════════════════════════════════════════════════════════════════════
# GRC – SOC 2 trust service criteria
# ══════════════════════════════════════════════════════════════════════════
C_GRC = """
<!-- BEGINNER33-GRC v1 -->
<!-- ── TOPIC: SOC 2 Trust Service Criteria ────────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-badge">Beginner</span>
    SOC 2 – Trust Service Criteria for Cloud Service Providers
  </div>
  <div class="topic-body">

    <div class="concept-card">
      <div class="concept-label">Core Concept</div>
      <div class="concept-title">What Is SOC 2?</div>
      <div class="concept-desc">
        <strong>SOC 2 (System and Organisation Controls 2)</strong> is an
        auditing standard for service providers that store or process
        customer data. If a customer asks "Is your cloud platform secure?",
        a SOC 2 Type II report is the answer.<br><br>
        <strong>Type I</strong> — snapshot: controls are <em>designed</em>
        correctly at a point in time.<br>
        <strong>Type II</strong> — over time (6–12 months): controls
        <em>operated</em> effectively throughout the period. Much more
        valuable.<br><br>
        <strong>Five Trust Service Criteria (TSC):</strong><br>
        &bull; <strong>Security</strong> (CC) — mandatory; the core criteria.<br>
        &bull; Availability (A) — system is available as promised.<br>
        &bull; Processing Integrity (PI) — processing is complete, accurate.<br>
        &bull; Confidentiality (C) — sensitive data is protected.<br>
        &bull; Privacy (P) — personal information lifecycle is managed.<br><br>
        Most SaaS companies start with Security + Availability + Confidentiality.
      </div>
    </div>

    <div class="concept-card">
      <div class="concept-label">Common Criteria</div>
      <div class="concept-title">The CC (Common Criteria) Control Families</div>
      <div class="concept-desc">
        The Security TSC is organised into <em>Common Criteria</em> (CC)
        categories. Here is what auditors look for in each:
      </div>
      <div class="code-block">
<span class="com">CC Category  Name                  Example controls auditors check</span>
CC1          Control Environment   Code of conduct, security policies documented
CC2          Communication         Security roles communicated; vendor reviews
CC3          Risk Assessment       Annual risk assessment; risk register
CC4          Monitoring Activities Vulnerability scans; penetration test results
CC5          Control Activities    Change management process; access reviews
CC6          Logical Access        MFA enforced; least privilege; offboarding
CC7          System Operations     SIEM alerts; incident response tested
CC8          Change Management     SDLC policy; code review; CI/CD controls
CC9          Risk Mitigation       Business continuity; DRP tested; cyber insurance

<span class="com"># What "evidence" looks like for CC6 (Logical Access):</span>
<span class="com"># - Screenshot: MFA enabled for all admin accounts</span>
<span class="com"># - Export: access review spreadsheet signed by manager</span>
<span class="com"># - Ticket: off-boarding of departed employee within 24 hours</span>
<span class="com"># - Policy: Access Control Policy document with effective date</span>
      </div>
    </div>

    <div class="concept-card">
      <div class="concept-label">Preparation</div>
      <div class="concept-title">Getting Ready for a SOC 2 Audit</div>
      <div class="concept-desc">
        <em>"Assume" makes an ass out of you and me</em> — assume the
        auditor will ask for evidence of <em>every</em> control. If you
        can't produce it, the control doesn't exist in their eyes.<br><br>
        <strong>12-month preparation checklist:</strong><br>
        &bull; Write &amp; approve all required policies (Security, Access
          Control, Incident Response, Change Management, Business Continuity).<br>
        &bull; Implement MFA everywhere — no exceptions for admin accounts.<br>
        &bull; Run quarterly access reviews and save the results.<br>
        &bull; Conduct an annual penetration test; remediate High/Critical
          findings before the audit window.<br>
        &bull; Set up a vulnerability scanning cadence (weekly automated
          scans, monthly review).<br>
        &bull; Use a ticketing system for changes — ad-hoc changes leave
          no evidence trail.<br>
        &bull; Document your incident response plan and run a tabletop
          exercise annually.<br>
        &bull; Use a GRC tool (Vanta, Drata, Secureframe) to collect and
          store evidence automatically.
      </div>
    </div>

    <div class="concept-card">
      <div class="concept-label">Mindset</div>
      <div class="concept-title">Compliance vs Security</div>
      <div class="concept-desc">
        <em>Compliance is not security</em> — passing a SOC 2 audit proves
        you had the right controls during the audit window; it does not
        guarantee you won't be breached.<br><br>
        Think of compliance as the <em>floor</em>, not the ceiling. A
        company can tick every SOC 2 box and still have a poor security
        culture, unpatched systems, or a weak incident response capability.<br><br>
        <em>You can't make someone make the right choice, yet you can pick
        up the pieces afterwards</em> — compliance frameworks give you the
        documented process to recover professionally when something goes
        wrong. The audit trail you built during SOC 2 prep becomes your
        lifeline when a regulator or customer asks what happened.
      </div>
    </div>

  </div>
</div>
"""

# ══════════════════════════════════════════════════════════════════════════
# SCRIPT – Python async/await for beginners
# ══════════════════════════════════════════════════════════════════════════
C_SCRIPT = """
<!-- BEGINNER33-SCRIPT v1 -->
<!-- ── TOPIC: Python async/await ─────────────────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-badge">Intermediate</span>
    Python Async/Await – Concurrent I/O Without Threads
  </div>
  <div class="topic-body">

    <div class="concept-card">
      <div class="concept-label">Core Concept</div>
      <div class="concept-title">Why Async? The Waiting Problem</div>
      <div class="concept-desc">
        A normal Python function blocks while waiting for I/O (network call,
        file read, database query). If you have 1,000 API calls to make,
        sequential blocking takes 1,000 × wait time.<br><br>
        <strong>Async</strong> lets Python do something else while waiting.
        When an I/O call is in-flight, the event loop switches to another
        coroutine — so 1,000 API calls can be in-flight simultaneously.<br><br>
        <strong>Rule of thumb:</strong><br>
        &bull; Use <code>async/await</code> for I/O-bound work (HTTP calls,
          DB queries, file I/O).<br>
        &bull; Use <code>multiprocessing</code> for CPU-bound work
          (image processing, ML training) — Python's GIL still blocks
          CPU work in a single process.<br><br>
        <em>"Not my circus, not my monkey"</em> — don't force async on
        everything. A simple script with two HTTP calls doesn't need it.
        Use it when you have many concurrent I/O operations.
      </div>
    </div>

    <div class="concept-card">
      <div class="concept-label">Syntax</div>
      <div class="concept-title">async def, await, and asyncio.run</div>
      <div class="concept-desc">
        An <code>async def</code> function is a <em>coroutine</em>. Calling
        it returns a coroutine object — it doesn't run until you
        <code>await</code> it or pass it to the event loop.
      </div>
      <div class="code-block">
<span class="kw">import</span> asyncio, time

<span class="kw">async def</span> <span class="fn">fetch_data</span>(url: str) -&gt; str:
    <span class="fn">print</span>(<span class="fn">f</span><span class="str">"Starting {url}"</span>)
    <span class="kw">await</span> asyncio.sleep(<span class="num">1</span>)   <span class="com"># simulate network wait</span>
    <span class="fn">print</span>(<span class="fn">f</span><span class="str">"Done    {url}"</span>)
    <span class="kw">return</span> <span class="fn">f</span><span class="str">"data from {url}"</span>

<span class="kw">async def</span> <span class="fn">main_sequential</span>():
    t = time.perf_counter()
    r1 = <span class="kw">await</span> <span class="fn">fetch_data</span>(<span class="str">"http://api-1"</span>)
    r2 = <span class="kw">await</span> <span class="fn">fetch_data</span>(<span class="str">"http://api-2"</span>)
    <span class="fn">print</span>(<span class="fn">f</span><span class="str">"Sequential: {time.perf_counter()-t:.1f}s"</span>)  <span class="com"># ~2 s</span>

<span class="kw">async def</span> <span class="fn">main_concurrent</span>():
    t = time.perf_counter()
    r1, r2 = <span class="kw">await</span> asyncio.gather(
        <span class="fn">fetch_data</span>(<span class="str">"http://api-1"</span>),
        <span class="fn">fetch_data</span>(<span class="str">"http://api-2"</span>),
    )
    <span class="fn">print</span>(<span class="fn">f</span><span class="str">"Concurrent: {time.perf_counter()-t:.1f}s"</span>)  <span class="com"># ~1 s</span>

asyncio.run(<span class="fn">main_sequential</span>())
asyncio.run(<span class="fn">main_concurrent</span>())
      </div>
    </div>

    <div class="concept-card">
      <div class="concept-label">HTTP Requests</div>
      <div class="concept-title">Async HTTP with aiohttp</div>
      <div class="concept-desc">
        The <code>requests</code> library is synchronous — it blocks.
        Use <code>aiohttp</code> for async HTTP. This example fetches
        100 URLs concurrently instead of one at a time.
      </div>
      <div class="code-block">
<span class="com"># pip install aiohttp</span>
<span class="kw">import</span> asyncio, aiohttp

URLS = [
    <span class="str">"https://httpbin.org/delay/1"</span>,
    <span class="str">"https://httpbin.org/delay/1"</span>,
    <span class="str">"https://httpbin.org/delay/1"</span>,
]   <span class="com"># extend to 100+ in real use</span>

<span class="kw">async def</span> <span class="fn">fetch</span>(session: aiohttp.ClientSession, url: str) -&gt; dict:
    <span class="kw">async with</span> session.get(url) <span class="kw">as</span> resp:
        data = <span class="kw">await</span> resp.json()
        <span class="kw">return</span> {<span class="str">"url"</span>: url, <span class="str">"status"</span>: resp.status}

<span class="kw">async def</span> <span class="fn">main</span>():
    <span class="kw">async with</span> aiohttp.ClientSession() <span class="kw">as</span> session:
        tasks   = [<span class="fn">fetch</span>(session, u) <span class="kw">for</span> u <span class="kw">in</span> URLS]
        results = <span class="kw">await</span> asyncio.gather(*tasks, return_exceptions=<span class="kw">True</span>)
    <span class="kw">for</span> r <span class="kw">in</span> results:
        <span class="kw">if</span> isinstance(r, Exception):
            <span class="fn">print</span>(<span class="str">"Error:"</span>, r)
        <span class="kw">else</span>:
            <span class="fn">print</span>(r)

asyncio.run(<span class="fn">main</span>())
<span class="com"># 3 × 1-second requests complete in ~1 second total</span>
      </div>
    </div>

    <div class="concept-card">
      <div class="concept-label">Rate Limiting</div>
      <div class="concept-title">Semaphores – Limiting Concurrency</div>
      <div class="concept-desc">
        Launching 10,000 coroutines at once can overwhelm an API or
        exhaust file descriptors. Use a <em>Semaphore</em> to cap
        concurrent tasks.
      </div>
      <div class="code-block">
<span class="kw">import</span> asyncio, aiohttp

<span class="kw">async def</span> <span class="fn">fetch_with_limit</span>(sem, session, url):
    <span class="kw">async with</span> sem:            <span class="com"># acquire — blocks if limit reached</span>
        <span class="kw">async with</span> session.get(url) <span class="kw">as</span> r:
            <span class="kw">return</span> <span class="kw">await</span> r.text()

<span class="kw">async def</span> <span class="fn">main</span>(urls):
    sem     = asyncio.Semaphore(<span class="num">10</span>)   <span class="com"># max 10 concurrent requests</span>
    <span class="kw">async with</span> aiohttp.ClientSession() <span class="kw">as</span> session:
        tasks = [<span class="fn">fetch_with_limit</span>(sem, session, u) <span class="kw">for</span> u <span class="kw">in</span> urls]
        <span class="kw">return</span> <span class="kw">await</span> asyncio.gather(*tasks, return_exceptions=<span class="kw">True</span>)

<span class="com"># results = asyncio.run(main(my_url_list))</span>
      </div>
    </div>

  </div>
</div>
"""

# ══════════════════════════════════════════════════════════════════════════
# MILITARY – OPSEC (Operational Security)
# ══════════════════════════════════════════════════════════════════════════
C_MILITARY = """
<!-- BEGINNER33-MILITARY v1 -->
<!-- ── TOPIC: OPSEC – Operational Security ───────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-badge">Beginner</span>
    OPSEC – Operational Security in Cyber &amp; Real Life
  </div>
  <div class="topic-body">

    <div class="concept-card">
      <div class="concept-label">Core Concept</div>
      <div class="concept-title">What Is OPSEC?</div>
      <div class="concept-desc">
        <strong>OPSEC (Operational Security)</strong> originated in the
        military but now applies universally to anyone who needs to protect
        sensitive information or activities from adversaries.<br><br>
        The core question: <em>"What information, if known by the wrong
        person, would allow them to harm me, my organisation, or my
        mission?"</em><br><br>
        The five-step OPSEC process:<br>
        1. <strong>Identify critical information</strong> — what do I need
           to protect? (credentials, plans, personnel, locations).<br>
        2. <strong>Analyse threats</strong> — who wants this information
           and why? (criminals, competitors, nation-states, insiders).<br>
        3. <strong>Analyse vulnerabilities</strong> — where could I
           accidentally expose this? (social media, email, public logs).<br>
        4. <strong>Assess risk</strong> — likelihood × impact for each
           vulnerability.<br>
        5. <strong>Apply countermeasures</strong> — reduce the vulnerability
           (encryption, access control, need-to-know, training).<br><br>
        <em>"Not my circus, not my monkey"</em> — if sensitive information
        belongs to your organisation, don't share it even with colleagues
        who don't need it. Need-to-know is a core OPSEC principle.
      </div>
    </div>

    <div class="concept-card">
      <div class="concept-label">Digital OPSEC</div>
      <div class="concept-title">Personal Digital Security Hygiene</div>
      <div class="concept-desc">
        Every IT professional is a target. Apply OPSEC to yourself:
      </div>
      <div class="code-block">
<span class="com">PERSONAL OPSEC CHECKLIST</span>
<span class="com">───────────────────────────────────────────────────────────</span>

CREDENTIALS
[ ] Use a password manager (Bitwarden, 1Password) — unique passwords everywhere
[ ] Enable MFA on every account that supports it (TOTP app, not SMS)
[ ] Never reuse passwords — one breach = one compromised account, not many

COMMUNICATIONS
[ ] Sensitive work: use encrypted email (ProtonMail) or end-to-end encrypted chat
[ ] Assume corporate email is monitored and archived
[ ] Don't discuss sensitive projects on public Slack workspaces / Discord

SOCIAL MEDIA
[ ] Don't post photos that reveal physical security details (badge readers, screens)
[ ] Job posting recon: attackers read your LinkedIn to map tech stack
[ ] Don't announce travel dates publicly — burglars and social engineers note it

DEVICE SECURITY
[ ] Full-disk encryption on laptops (BitLocker/FileVault/LUKS)
[ ] Screen lock within 2 minutes of inactivity
[ ] VPN on untrusted Wi-Fi (coffee shops, hotels, airports)
[ ] Webcam cover when not in use

WORK HABITS
[ ] Clear desk policy — sensitive docs face down or locked away
[ ] Shred documents before disposal; don't put them in recycling
[ ] Be aware of shoulder surfing in public spaces
[ ] Verify caller identity before providing information (voice phishing = vishing)
      </div>
    </div>

    <div class="concept-card">
      <div class="concept-label">Org OPSEC</div>
      <div class="concept-title">Protecting Sensitive Information at Scale</div>
      <div class="concept-desc">
        Organisational OPSEC controls applied in enterprise security:<br><br>
        &bull; <strong>Information classification</strong>: Public / Internal
          / Confidential / Restricted — policies dictate how each is
          handled.<br>
        &bull; <strong>Data Loss Prevention (DLP)</strong>: software that
          blocks classified files from being emailed externally or uploaded
          to personal cloud storage.<br>
        &bull; <strong>Privileged Access Workstations (PAW)</strong>: a
          dedicated, hardened device used only for admin tasks —
          never for browsing or email.<br>
        &bull; <strong>Air-gapped networks</strong>: classified systems
          with no internet connection; data moves via signed, approved
          media only.<br>
        &bull; <strong>Red team deception</strong>: honeytokens — fake
          credentials or files planted in your system; if accessed, you
          know an attacker has them.
      </div>
      <div class="code-block">
<span class="com"># Create a honeytoken file (plant it; alert if accessed)</span>
<span class="com"># On Linux: use inotifywait to alert when the file is read</span>
touch /home/admin/.aws/credentials_BACKUP_2023

inotifywait -m /home/admin/.aws/credentials_BACKUP_2023 -e access |
<span class="kw">while</span> read path action file; do
    echo <span class="str">"HONEYTOKEN ACCESSED: $path$file at $(date)"</span> | \
        mail -s <span class="str">"ALERT: Honeytoken read"</span> security-team@corp.example.com
done

<span class="com"># AWS honeytoken: create an IAM key that only fires CloudTrail events</span>
<span class="com"># Canarytokens.org generates free honeytokens for:</span>
<span class="com"># AWS keys, Word docs, PDFs, URLs, DNS names</span>
      </div>
    </div>

    <div class="concept-card">
      <div class="concept-label">Mindset</div>
      <div class="concept-title">"Assume Breach" – The Modern Security Posture</div>
      <div class="concept-desc">
        <em>"Assume" makes an ass out of you and me</em> — but in security,
        the one assumption you <em>should</em> make is that you have already
        been breached.<br><br>
        The <strong>Assume Breach</strong> philosophy:<br>
        &bull; Design systems as if an attacker already has a foothold —
          use micro-segmentation, least privilege, and mutual TLS between
          services.<br>
        &bull; Invest in <em>detection and response</em> as much as
          prevention — because prevention eventually fails.<br>
        &bull; Run red-team exercises to find gaps before real attackers do.<br>
        &bull; Know your <em>mean time to detect (MTTD)</em> and
          <em>mean time to respond (MTTR)</em> — measure and improve them
          continuously.<br><br>
        <em>You can't make someone make the right choice, yet you can pick
        up the pieces afterwards</em> — an attacker who got in through a
        phishing email is not your fault; the speed and quality of your
        response is entirely within your control.
      </div>
    </div>

  </div>
</div>
"""

# ══════════════════════════════════════════════════════════════════════════
# helpers
# ══════════════════════════════════════════════════════════════════════════
def inject(html, anchor, sentinel, content):
    if sentinel in html:
        return html, False
    pos = html.find(anchor)
    if pos == -1:
        return html, False
    return html[:pos] + content + html[pos:], True


class _Checker(HTMLParser):
    def __init__(self):
        super().__init__()
        self.stack = []
        self.stray = 0
        VOID = {"area","base","br","col","embed","hr","img","input",
                "link","meta","param","source","track","wbr"}
        self._void = VOID
    def handle_starttag(self, tag, attrs):
        if tag not in self._void:
            self.stack.append(tag)
    def handle_endtag(self, tag):
        if tag in self._void:
            return
        if self.stack and self.stack[-1] == tag:
            self.stack.pop()
        else:
            self.stray += 1


def validate(html):
    c = _Checker()
    c.feed(html)
    print(f"  Unclosed at EOF : {c.stack[-5:] if c.stack else 'NONE'}")
    print(f"  Stray end tags  : {c.stray}")


WAVES = [
    (A_NET,      S_NET,      C_NET),
    (A_THREAT,   S_THREAT,   C_THREAT),
    (A_GRC,      S_GRC,      C_GRC),
    (A_SCRIPT,   S_SCRIPT,   C_SCRIPT),
    (A_MILITARY, S_MILITARY, C_MILITARY),
]


def main():
    path = Path("index.html")
    html = path.read_text(encoding="utf-8")
    changed = False
    for anchor, sentinel, content in WAVES:
        html, did = inject(html, anchor, sentinel, content)
        label = sentinel.split()[0].lstrip("<!-").strip()
        print(f"  {label}: {'INJECTED' if did else 'already present / anchor missing'}")
        changed = changed or did
    if changed:
        path.write_text(html, encoding="utf-8")
        print(f"\n  Written {len(html):,} bytes")
    else:
        print("\n  Nothing to do.")
    print("\n  HTML balance check:")
    validate(html)


if __name__ == "__main__":
    main()
