#!/usr/bin/env python3
"""
patch_beginner_concepts_v11.py — Wave 11: Advanced topics + deeper practical coverage.

New sentinels:
  BEGINNER11-SCRIPT v1  — Async programming, concurrency, web scraping basics
  BEGINNER11-NET v1     — Network troubleshooting methodology, packet analysis
  BEGINNER11-THREAT v1  — Vulnerability management, CVEs, patching strategy
  BEGINNER11-OPS v1     — Backup strategies, disaster recovery, business continuity
  BEGINNER11-LIFE v1    — Dealing with failure, growth mindset, mentorship
"""
from pathlib import Path

SCRIPT_INJECT_ANCHOR = "<!-- /domain-body script -->"
NET_INJECT_ANCHOR    = "<!-- /domain-body net -->"
THREAT_INJECT_ANCHOR = "<!-- /domain-body threat -->"
OPS_INJECT_ANCHOR    = "<!-- /domain-body ops -->"
LIFE_INJECT_ANCHOR   = "<!-- /domain-body lifestyle -->"

# ─────────────────────────────── SCRIPTING wave 11 ───────────────────────────
SCRIPT_SENTINEL = "<!-- BEGINNER11-SCRIPT v1 -->"
SCRIPT_CONTENT = """
<!-- BEGINNER11-SCRIPT v1 -->
<!-- ── TOPIC: ASYNC PROGRAMMING ─────────────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">⏳</span>
    <span class="topic-name">Async Programming — Do More Without Waiting</span>
    <span class="topic-badge">SCRIPT • Intermediate</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">THE PROBLEM</div>
      <div class="concept-title">I/O-Bound vs CPU-Bound Work</div>
      <div class="concept-desc"><strong>CPU-bound</strong>: computation is the bottleneck (image processing, cryptography, simulations). More CPU cores help. Use <code>multiprocessing</code>.<br>
      <strong>I/O-bound</strong>: waiting for external things (network responses, disk reads, database queries). CPU is mostly idle waiting. One thread can handle hundreds of concurrent I/O operations by switching between them while each waits. Use <code>asyncio</code>.</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">ASYNC / AWAIT</div>
      <div class="concept-title">Coroutines in Python</div>
      <div class="concept-desc">An <code>async def</code> function is a coroutine — it can pause itself at <code>await</code> points while other coroutines run. The event loop switches between them, never blocking the thread.</div>
      <div class="code-block"><span class="kw">import</span> asyncio
<span class="kw">import</span> aiohttp   <span class="com"># pip install aiohttp</span>

<span class="kw">async def</span> <span class="fn">fetch_url</span>(session, url):
    <span class="kw">async with</span> session.get(url) <span class="kw">as</span> response:
        text = <span class="kw">await</span> response.text()
        <span class="fn">print</span>(<span class="str">f"{url}: {len(text)} chars"</span>)
        <span class="kw">return</span> text

<span class="kw">async def</span> <span class="fn">main</span>():
    urls = [
        <span class="str">"https://httpbin.org/delay/1"</span>,
        <span class="str">"https://httpbin.org/delay/1"</span>,
        <span class="str">"https://httpbin.org/delay/1"</span>,
    ]
    <span class="kw">async with</span> aiohttp.ClientSession() <span class="kw">as</span> session:
        <span class="com"># Fetch all three CONCURRENTLY — takes ~1s total, not 3s</span>
        tasks = [<span class="fn">fetch_url</span>(session, url) <span class="kw">for</span> url <span class="kw">in</span> urls]
        results = <span class="kw">await</span> asyncio.gather(*tasks)

asyncio.run(<span class="fn">main</span>())</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">asyncio ESSENTIALS</div>
      <div class="concept-title">The Key Building Blocks</div>
      <div class="code-block"><span class="com"># asyncio.gather — run coroutines concurrently</span>
results = <span class="kw">await</span> asyncio.gather(coro1(), coro2(), coro3())

<span class="com"># asyncio.create_task — fire and forget</span>
task = asyncio.create_task(<span class="fn">some_coro</span>())
<span class="com"># do other work, then...</span>
result = <span class="kw">await</span> task

<span class="com"># asyncio.wait_for — timeout</span>
<span class="kw">try</span>:
    result = <span class="kw">await</span> asyncio.wait_for(<span class="fn">slow_coro</span>(), timeout=<span class="num">5.0</span>)
<span class="kw">except</span> asyncio.TimeoutError:
    <span class="fn">print</span>(<span class="str">"Timed out!"</span>)

<span class="com"># asyncio.sleep — non-blocking wait</span>
<span class="kw">await</span> asyncio.sleep(<span class="num">1</span>)    <span class="com"># other tasks run during this second</span>
<span class="com"># vs time.sleep(1)        # BLOCKS the whole thread!</span></div>
    </div>
    <div class="concept-card">
      <div class="concept-label">THREADING FOR I/O</div>
      <div class="concept-title">When You Can't Use Async</div>
      <div class="concept-desc">Not all libraries support async. For blocking I/O calls with regular (synchronous) libraries, use threads:</div>
      <div class="code-block"><span class="kw">from</span> concurrent.futures <span class="kw">import</span> ThreadPoolExecutor
<span class="kw">import</span> requests

<span class="kw">def</span> <span class="fn">fetch</span>(url):
    <span class="kw">return</span> requests.get(url).text

urls = [<span class="str">"https://example.com"</span>] * <span class="num">10</span>

<span class="com"># Run up to 5 requests concurrently</span>
<span class="kw">with</span> ThreadPoolExecutor(max_workers=<span class="num">5</span>) <span class="kw">as</span> pool:
    results = <span class="fn">list</span>(pool.map(<span class="fn">fetch</span>, urls))</div>
    </div>
  </div>
</div>

<!-- ── TOPIC: WEB SCRAPING BASICS ────────────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">🕷️</span>
    <span class="topic-name">Web Scraping — Extracting Data From Websites</span>
    <span class="topic-badge">SCRIPT • Practical</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">LEGAL & ETHICAL NOTE</div>
      <div class="concept-title">Check robots.txt and Terms of Service</div>
      <div class="concept-desc">Before scraping, check the site's <code>robots.txt</code> (example.com/robots.txt) — it specifies which paths bots may access. Read the Terms of Service — many prohibit automated access. Don't overload servers (add delays). Prefer official APIs when available. Scraping for research or personal use is generally gray area; commercial use of scraped data is often illegal.</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">REQUESTS + BEAUTIFULSOUP</div>
      <div class="concept-title">The Classic Scraping Stack</div>
      <div class="code-block"><span class="com"># pip install requests beautifulsoup4</span>
<span class="kw">import</span> requests
<span class="kw">from</span> bs4 <span class="kw">import</span> BeautifulSoup

url = <span class="str">"https://books.toscrape.com/"</span>  <span class="com"># practice site</span>
response = requests.get(url)
soup = BeautifulSoup(response.text, <span class="str">"html.parser"</span>)

<span class="com"># Find by tag</span>
titles = soup.find_all(<span class="str">"h3"</span>)

<span class="com"># Find by CSS selector</span>
prices = soup.select(<span class="str">".price_color"</span>)

<span class="com"># Find by attribute</span>
links = soup.find_all(<span class="str">"a"</span>, href=<span class="kw">True</span>)

<span class="kw">for</span> title, price <span class="kw">in</span> <span class="fn">zip</span>(titles[:5], prices[:5]):
    <span class="fn">print</span>(<span class="str">f"{title.text.strip()} — {price.text}"</span>)</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">BE A POLITE SCRAPER</div>
      <div class="concept-title">Rate Limit and Identify Yourself</div>
      <div class="code-block"><span class="kw">import</span> time
<span class="kw">import</span> requests

headers = {
    <span class="str">"User-Agent"</span>: <span class="str">"MyResearchBot/1.0 (contact: me@example.com)"</span>
}

<span class="kw">for</span> page <span class="kw">in</span> <span class="fn">range</span>(<span class="num">1</span>, <span class="num">11</span>):
    url = <span class="str">f"https://example.com/page/{page}"</span>
    resp = requests.get(url, headers=headers)
    <span class="com"># Process resp...</span>
    time.sleep(<span class="num">1</span>)   <span class="com"># 1 second between requests</span></div>
    </div>
  </div>
</div>
"""

# ─────────────────────────────── NET wave 11 ─────────────────────────────────
NET_SENTINEL = "<!-- BEGINNER11-NET v1 -->"
NET_CONTENT = """
<!-- BEGINNER11-NET v1 -->
<!-- ── TOPIC: NETWORK TROUBLESHOOTING ───────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">🔍</span>
    <span class="topic-name">Network Troubleshooting — A Systematic Approach</span>
    <span class="topic-badge">NET • Practical</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">OSI TROUBLESHOOTING</div>
      <div class="concept-title">Bottom-Up or Top-Down</div>
      <div class="concept-desc">Two strategies for network problems:<br>
      <strong>Bottom-up (most common for no-connectivity)</strong>: Physical (cable/light?) → Data Link (ARP, MAC?) → Network (ping, IP?) → Transport (port open?) → Application (service running?).<br>
      <strong>Top-down</strong>: Start at the application ("the web page is slow") and work down to find where the degradation is.</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">THE DIAGNOSTIC TOOLKIT</div>
      <div class="concept-title">Commands Every Network Person Uses</div>
      <div class="code-block"><span class="com"># Layer 1-2: Physical / Link</span>
ip link show                    <span class="com"># interface status, MAC</span>
ethtool eth0                    <span class="com"># speed, duplex, link detected</span>

<span class="com"># Layer 3: IP connectivity</span>
ip addr show                    <span class="com"># IP addresses</span>
ip route show                   <span class="com"># routing table</span>
ping 8.8.8.8                    <span class="com"># basic reachability</span>
ping -c 4 google.com            <span class="com"># DNS + ICMP check</span>

<span class="com"># Path tracing</span>
traceroute 8.8.8.8              <span class="com"># hops to destination</span>
mtr google.com                  <span class="com"># live traceroute with packet loss</span>

<span class="com"># Layer 4: Transport / Ports</span>
ss -tlnp                        <span class="com"># listening TCP ports</span>
ss -ulnp                        <span class="com"># listening UDP ports</span>
nc -zv 192.168.1.1 22           <span class="com"># test TCP port connectivity</span>
telnet 192.168.1.1 80           <span class="com"># old-school port test</span>

<span class="com"># DNS</span>
dig google.com                  <span class="com"># DNS lookup</span>
nslookup google.com             <span class="com"># Windows/Linux</span>
resolvectl query google.com     <span class="com"># systemd-resolved</span></div>
    </div>
    <div class="concept-card">
      <div class="concept-label">PACKET CAPTURE</div>
      <div class="concept-title">See What's Actually on the Wire</div>
      <div class="code-block"><span class="com"># Capture on interface eth0</span>
sudo tcpdump -i eth0

<span class="com"># Capture HTTP traffic</span>
sudo tcpdump -i eth0 port 80 -w capture.pcap

<span class="com"># Capture DNS queries</span>
sudo tcpdump -i any port 53 -n

<span class="com"># Show packet contents in ASCII</span>
sudo tcpdump -i eth0 -A

<span class="com"># Read saved capture</span>
tcpdump -r capture.pcap</div>
      <div class="concept-desc">Open <code>.pcap</code> files in Wireshark for graphical analysis. Wireshark's "Follow TCP Stream" shows entire conversations. Filter: <code>http.request</code>, <code>tcp.flags.syn==1</code>, <code>dns</code>, <code>ip.addr==192.168.1.5</code></div>
    </div>
    <div class="concept-card">
      <div class="concept-label">COMMON SYMPTOMS</div>
      <div class="concept-title">Problem → Most Likely Cause</div>
      <table class="ai-table">
        <thead><tr><th>Symptom</th><th>Check First</th></tr></thead>
        <tbody>
          <tr><td>No connectivity at all</td><td>IP address assigned? (169.254.x.x = DHCP failed)</td></tr>
          <tr><td>Can ping IP, not hostname</td><td>DNS — wrong resolver, DHCP giving bad DNS</td></tr>
          <tr><td>Can ping gateway, not internet</td><td>ISP issue, default route, firewall blocking outbound</td></tr>
          <tr><td>Intermittent packet loss</td><td>Bad cable, duplex mismatch, overloaded link</td></tr>
          <tr><td>High latency only to one site</td><td>Routing issue, CDN problem, that site's servers</td></tr>
          <tr><td>App works internally, not externally</td><td>Firewall port not open, NAT not configured</td></tr>
        </tbody>
      </table>
    </div>
  </div>
</div>
"""

# ─────────────────────────────── THREAT wave 11 ──────────────────────────────
THREAT_SENTINEL = "<!-- BEGINNER11-THREAT v1 -->"
THREAT_CONTENT = """
<!-- BEGINNER11-THREAT v1 -->
<!-- ── TOPIC: VULNERABILITY MANAGEMENT ───────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">🩹</span>
    <span class="topic-name">Vulnerability Management — Finding and Fixing Weaknesses</span>
    <span class="topic-badge">THREAT • Foundation</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">VULNERABILITY LIFECYCLE</div>
      <div class="concept-title">Identify → Assess → Prioritize → Remediate → Verify</div>
      <div class="concept-desc">Vulnerability management is a continuous cycle, not a one-time scan. Networks change daily — new systems appear, software updates fail, configurations drift. The cycle never ends.</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">CVE & CVSS</div>
      <div class="concept-title">Common Vulnerabilities and Their Severity</div>
      <div class="concept-desc"><strong>CVE (Common Vulnerabilities and Exposures)</strong> — a unique identifier for each publicly known vulnerability. Format: <code>CVE-2021-44228</code> (Log4Shell). The year and a serial number. Lookup: <code>cve.mitre.org</code> or <code>nvd.nist.gov</code>.<br>
      <strong>CVSS (Common Vulnerability Scoring System)</strong> — a 0-10 score for severity:<br>
      <strong>9.0-10.0 = Critical</strong>: patch immediately<br>
      <strong>7.0-8.9 = High</strong>: patch this week<br>
      <strong>4.0-6.9 = Medium</strong>: patch this month<br>
      <strong>0.1-3.9 = Low</strong>: scheduled patching<br>
      <strong>0.0 = None</strong>: not a security issue</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">SCANNING TOOLS</div>
      <div class="concept-title">Identify What's Exposed</div>
      <div class="concept-desc"><strong>Nessus</strong> (Tenable) — industry standard enterprise vuln scanner. Identifies unpatched software, misconfigurations, weak credentials.<br>
      <strong>OpenVAS</strong> — open-source alternative.<br>
      <strong>Qualys</strong> — cloud-based; no agent required for network scans.<br>
      <strong>Trivy</strong> — open-source container image scanner; finds vulnerable packages in Docker images.<br>
      <strong>OWASP ZAP</strong> — web application scanner; finds XSS, SQLi, CSRF, etc.</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">PATCH STRATEGY</div>
      <div class="concept-title">Risk-Based Prioritization</div>
      <div class="concept-desc">You'll never patch everything immediately — there are always too many vulnerabilities. Prioritize based on:<br>
      1. <strong>CVSS score</strong> — base severity<br>
      2. <strong>Exploitability</strong> — is it being actively exploited? Check CISA's Known Exploited Vulnerabilities (KEV) catalog.<br>
      3. <strong>Asset criticality</strong> — a critical vuln on an internet-facing production server beats the same vuln on an air-gapped test system.<br>
      4. <strong>Compensating controls</strong> — if a WAF blocks the exploit vector, urgency is lower until you can patch.</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">ZERO DAY</div>
      <div class="concept-title">The Patch Doesn't Exist Yet</div>
      <div class="concept-desc">A <strong>zero-day vulnerability</strong> is one that has no patch yet — vendors have had "zero days" to fix it. Zero-days in the wild (actively being exploited) are the most dangerous. Defenses: defense-in-depth (don't rely on patches alone), network segmentation to limit blast radius, EDR to detect exploitation behavior, and monitoring for indicators.</div>
    </div>
  </div>
</div>
"""

# ─────────────────────────────── OPS wave 11 ─────────────────────────────────
OPS_SENTINEL = "<!-- BEGINNER11-OPS v1 -->"
OPS_CONTENT = """
<!-- BEGINNER11-OPS v1 -->
<!-- ── TOPIC: BACKUP & DISASTER RECOVERY ─────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">💾</span>
    <span class="topic-name">Backup &amp; Disaster Recovery — Surviving the Worst Case</span>
    <span class="topic-badge">OPS • Critical</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">THE 3-2-1 RULE</div>
      <div class="concept-title">Three Copies, Two Media, One Off-Site</div>
      <div class="concept-desc"><strong>3</strong> copies of your data (original + 2 backups)<br>
      <strong>2</strong> different storage types (SSD + external drive, local + cloud)<br>
      <strong>1</strong> copy off-site (cloud, different building, different region)<br>
      Why: ransomware encrypts local + network shares. Fire/flood destroys same-room copies. Off-site survives both. Modern extension: 3-2-1-1-0 (add 1 offline/air-gapped copy and 0 errors verified by testing).</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">BACKUP TYPES</div>
      <div class="concept-title">Full vs Incremental vs Differential</div>
      <table class="ai-table">
        <thead><tr><th>Type</th><th>What It Backs Up</th><th>Backup Speed</th><th>Restore Speed</th></tr></thead>
        <tbody>
          <tr><td>Full</td><td>Everything</td><td>Slow</td><td>Fast (one file)</td></tr>
          <tr><td>Incremental</td><td>Changes since last backup of any type</td><td>Fast</td><td>Slow (full + all incrementals)</td></tr>
          <tr><td>Differential</td><td>Changes since last FULL backup</td><td>Medium</td><td>Medium (full + last differential)</td></tr>
        </tbody>
      </table>
    </div>
    <div class="concept-card">
      <div class="concept-label">RTO & RPO</div>
      <div class="concept-title">Recovery Time and Data Loss Objectives</div>
      <div class="concept-desc"><strong>RTO (Recovery Time Objective)</strong> — how long can the business tolerate being down? An e-commerce site might have an RTO of 1 hour. A hospital might have an RTO of minutes.<br>
      <strong>RPO (Recovery Point Objective)</strong> — how much data can we afford to lose? If RPO is 4 hours, backups must run at least every 4 hours.<br>
      These drive backup strategy: low RTO/RPO requires continuous replication and hot standby; high RTO/RPO can use daily backups to tape.</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">TEST YOUR BACKUPS</div>
      <div class="concept-title">An Untested Backup Is Not a Backup</div>
      <div class="concept-desc">Backups regularly fail silently (disk full, permission error, partial write). The only way to know a backup is good is to restore from it in a test environment. Restore tests should be:<br>
      • Scheduled (quarterly at minimum)<br>
      • Documented (how long did restore take? any errors?)<br>
      • Realistic (restore to isolated environment, not production)<br>
      Many organizations discover their backups are corrupted during an actual disaster — the worst time to find out.</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">RANSOMWARE RESPONSE</div>
      <div class="concept-title">When Encryption Happens to You</div>
      <div class="concept-desc">If ransomware strikes:<br>
      1. <strong>Isolate</strong> affected systems immediately — disconnect from network<br>
      2. <strong>Don't pay</strong> if you have clean backups — payment doesn't guarantee decryption<br>
      3. <strong>Preserve evidence</strong> — image affected systems before wiping<br>
      4. <strong>Restore from known-good backup</strong> made before infection<br>
      5. <strong>Find the initial access</strong> before coming back online — if you restore without finding the entry point, you'll be re-infected</div>
    </div>
  </div>
</div>

<!-- ── TOPIC: MONITORING & OBSERVABILITY ─────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">📡</span>
    <span class="topic-name">Monitoring &amp; Observability — Know Before Users Complain</span>
    <span class="topic-badge">OPS • Foundation</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">THREE PILLARS</div>
      <div class="concept-title">Metrics · Logs · Traces</div>
      <div class="concept-desc"><strong>Metrics</strong> — numerical measurements over time: CPU %, request rate, error rate, latency percentiles (p50, p95, p99). Great for dashboards and alerting thresholds.<br>
      <strong>Logs</strong> — event records: what happened, when, and on which system. Needed to understand the WHY behind a metric spike.<br>
      <strong>Traces</strong> — record the journey of a single request through multiple services. Essential for distributed systems to find which service is causing latency.</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">KEY METRICS</div>
      <div class="concept-title">The Four Golden Signals (Google SRE)</div>
      <div class="concept-desc"><strong>Latency</strong> — how long does a request take? Track P95/P99 not just average (average hides slow outliers).<br>
      <strong>Traffic</strong> — how many requests per second? Understand normal baseline so anomalies are visible.<br>
      <strong>Errors</strong> — what percentage of requests fail? Even 0.1% on 1M req/s is 1000 errors/sec.<br>
      <strong>Saturation</strong> — how full is your system? CPU, memory, disk, connections — approaching limits causes cascading failures.</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">ALERTING PHILOSOPHY</div>
      <div class="concept-title">Alert on Symptoms, Not Causes</div>
      <div class="concept-desc">Alert when USERS are affected, not when internal metrics are interesting. "Error rate &gt; 1% for 5 minutes" is a user-facing symptom. "CPU &gt; 80%" is a cause that may or may not matter. Too many non-actionable alerts → alert fatigue → real alerts ignored. Every alert should have a runbook: what to check, what to do, who to escalate to.</div>
    </div>
  </div>
</div>
"""

# ─────────────────────────────── LIFESTYLE wave 11 ───────────────────────────
LIFE_SENTINEL = "<!-- BEGINNER11-LIFE v1 -->"
LIFE_CONTENT = """
<!-- BEGINNER11-LIFE v1 -->
<!-- ── TOPIC: DEALING WITH FAILURE ───────────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">🔄</span>
    <span class="topic-name">Dealing With Failure — Falling Forward</span>
    <span class="topic-badge">LIFESTYLE • Resilience</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">FAILURE IS PART OF THE PROCESS</div>
      <div class="concept-title">Every Expert Was Once a Beginner Who Failed Often</div>
      <div class="concept-desc">The system administrator who breaks production learns more than the one who never touches anything. The security researcher who gets stumped on a CTF challenge learns more than the one who always googles the answer. Failure is data. The only way to fail with zero risk is to never attempt anything.</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">FAIL FAST, FAIL SMALL</div>
      <div class="concept-title">Test in Safe Environments</div>
      <div class="concept-desc">The best engineers design systems where failures are small, contained, and reversible. The same principle applies to learning: set up a lab where breaking things has no real consequences. VMs, test environments, personal projects, CTF platforms — fail there freely, learn quickly, and apply carefully in production.</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">THE GROWTH MINDSET</div>
      <div class="concept-title">Not "I Can't" — "I Can't Yet"</div>
      <div class="concept-desc">Carol Dweck's research distinguishes:<br>
      <strong>Fixed mindset</strong>: "I'm just not good at networking." Treats ability as fixed.<br>
      <strong>Growth mindset</strong>: "I don't understand subnetting yet. I'll practice until I do." Treats ability as developable.<br>
      The difference isn't positive thinking — it's whether you believe effort can change outcomes. In IT, it can. Everything was learned by someone; it can be learned by you.</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">AFTER A FAILURE</div>
      <div class="concept-title">The After-Action Review</div>
      <div class="concept-desc">When something goes wrong, do a brief personal AAR:<br>
      1. <strong>What happened?</strong> — factual, no blame<br>
      2. <strong>What was supposed to happen?</strong> — the intent<br>
      3. <strong>Why was there a difference?</strong> — root cause, not symptoms<br>
      4. <strong>What will I do differently?</strong> — specific, actionable change<br>
      10 minutes of honest reflection after a failure is worth more than 10 hours of additional studying. The lesson only sticks if you extract it deliberately.</div>
    </div>
  </div>
</div>

<!-- ── TOPIC: MENTORSHIP — GIVING AND RECEIVING ───────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">🧑‍🏫</span>
    <span class="topic-name">Mentorship — The Fastest Way to Grow</span>
    <span class="topic-badge">LIFESTYLE • Career</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">FINDING A MENTOR</div>
      <div class="concept-title">Ask Specifically, Not Generally</div>
      <div class="concept-desc">Don't send a cold message saying "Will you be my mentor?" — that's a big, undefined commitment that busy people usually decline. Instead:<br>
      • Ask one specific question<br>
      • Ask for 20 minutes of their time on a specific topic<br>
      • Come prepared with what you've already tried<br>
      • Make it easy for them to say yes or no<br>
      If it goes well, the relationship develops naturally. Start small.</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">BEING A GOOD MENTEE</div>
      <div class="concept-title">Respect Their Time and Follow Through</div>
      <div class="concept-desc">The best mentees:<br>
      • Do the work between sessions (don't show up empty-handed)<br>
      • Come with specific questions, not "what should I do with my career?"<br>
      • Follow through on suggestions and report back<br>
      • Say thank you, specifically ("That advice about focusing on networking certs before security opened three job interviews")<br>
      Mentors give more to people who visibly use their advice.</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">MENTOR OTHERS</div>
      <div class="concept-title">Teaching Forces You to Actually Understand</div>
      <div class="concept-desc">You don't need to be an expert to help someone with less experience. If you're 6 months ahead of someone, your struggles are fresh and your explanations more relatable than an expert's. Explaining something you've recently learned solidifies YOUR understanding dramatically. The cycle: learn it → teach it → deeply know it.</div>
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
        patch(target, SCRIPT_SENTINEL, SCRIPT_CONTENT, SCRIPT_INJECT_ANCHOR),
        patch(target, NET_SENTINEL,    NET_CONTENT,    NET_INJECT_ANCHOR),
        patch(target, THREAT_SENTINEL, THREAT_CONTENT, THREAT_INJECT_ANCHOR),
        patch(target, OPS_SENTINEL,    OPS_CONTENT,    OPS_INJECT_ANCHOR),
        patch(target, LIFE_SENTINEL,   LIFE_CONTENT,   LIFE_INJECT_ANCHOR),
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
