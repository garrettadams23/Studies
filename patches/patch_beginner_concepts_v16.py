#!/usr/bin/env python3
"""
patch_beginner_concepts_v16.py — Wave 16: IT automation scripting,
third-party risk, digital forensics, Linux permissions, home labs.

New sentinels:
  BEGINNER16-SCRIPT v1  — Practical IT automation scripting (subprocess, scheduling, files)
  BEGINNER16-GRC v1     — Third-party/vendor risk, security awareness programs
  BEGINNER16-THREAT v1  — Digital forensics basics, evidence handling, memory/disk
  BEGINNER16-LINUX v1   — Permissions deep dive, special bits, ACLs, SELinux/AppArmor
  BEGINNER16-LIFE v1    — Building a home lab, certification roadmap, study strategy
"""
from pathlib import Path

SCRIPT_INJECT_ANCHOR = "<!-- /domain-body script -->"
GRC_INJECT_ANCHOR    = "<!-- /domain-body grc -->"
THREAT_INJECT_ANCHOR = "<!-- /domain-body threat -->"
LINUX_INJECT_ANCHOR  = "<!-- /domain-body linux -->"
LIFE_INJECT_ANCHOR   = "<!-- /domain-body lifestyle -->"

# ─────────────────────────────── SCRIPTING wave 16 ───────────────────────────
SCRIPT_SENTINEL = "<!-- BEGINNER16-SCRIPT v1 -->"
SCRIPT_CONTENT = """
<!-- BEGINNER16-SCRIPT v1 -->
<!-- ── TOPIC: IT AUTOMATION SCRIPTING ────────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">⚙️</span>
    <span class="topic-name">IT Automation — Scripting the Boring Stuff Away</span>
    <span class="topic-badge">SCRIPT • Practical</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">WHY AUTOMATE</div>
      <div class="concept-title">If You Do It Twice, Script It</div>
      <div class="concept-desc">The single highest-leverage skill in IT is automation. Every repetitive task you script is time given back forever — and scripts don't make typos at 2am. The rule of thumb: if you'll do something more than twice, or if doing it manually is error-prone, automate it. Python is the go-to language because it's readable, batteries-included, and runs everywhere.</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">RUNNING SYSTEM COMMANDS</div>
      <div class="concept-title">subprocess — Python Talking to the Shell</div>
      <div class="concept-desc">The <code>subprocess</code> module runs external commands from Python. Use it to wrap CLI tools, automate system tasks, and glue together programs. Always prefer the list form (not a string) to avoid shell injection.</div>
      <div class="code-block"><span class="kw">import</span> subprocess

<span class="com"># Run a command, capture output (the modern way)</span>
result = subprocess.run(
    [<span class="str">"ls"</span>, <span class="str">"-la"</span>, <span class="str">"/var/log"</span>],
    capture_output=<span class="kw">True</span>,
    text=<span class="kw">True</span>,          <span class="com"># decode bytes → str</span>
    timeout=<span class="num">30</span>,          <span class="com"># don't hang forever</span>
)
<span class="fn">print</span>(result.stdout)        <span class="com"># the command's output</span>
<span class="fn">print</span>(result.returncode)    <span class="com"># 0 = success</span>

<span class="com"># Raise an exception if the command fails</span>
subprocess.run([<span class="str">"systemctl"</span>, <span class="str">"restart"</span>, <span class="str">"nginx"</span>], check=<span class="kw">True</span>)

<span class="com"># Check a command's exit code without crashing</span>
result = subprocess.run([<span class="str">"ping"</span>, <span class="str">"-c"</span>, <span class="str">"1"</span>, <span class="str">"8.8.8.8"</span>],
                        capture_output=<span class="kw">True</span>)
<span class="kw">if</span> result.returncode == <span class="num">0</span>:
    <span class="fn">print</span>(<span class="str">"Host is up"</span>)

<span class="com"># DANGER: shell=True allows injection if input is untrusted</span>
<span class="com"># subprocess.run(f"rm {user_input}", shell=True)  # NEVER do this</span></div>
    </div>
    <div class="concept-card">
      <div class="concept-label">FILE SYSTEM AUTOMATION</div>
      <div class="concept-title">Bulk File Operations</div>
      <div class="code-block"><span class="kw">from</span> pathlib <span class="kw">import</span> Path
<span class="kw">import</span> shutil, datetime

<span class="com"># Find and clean up old log files (&gt; 30 days)</span>
log_dir = Path(<span class="str">"/var/log/myapp"</span>)
cutoff = datetime.datetime.now() - datetime.timedelta(days=<span class="num">30</span>)

<span class="kw">for</span> log <span class="kw">in</span> log_dir.glob(<span class="str">"*.log"</span>):
    mtime = datetime.datetime.fromtimestamp(log.stat().st_mtime)
    <span class="kw">if</span> mtime &lt; cutoff:
        <span class="fn">print</span>(<span class="str">f"Deleting old log: {log.name}"</span>)
        log.unlink()           <span class="com"># delete the file</span>

<span class="com"># Bulk rename — add date prefix to all PDFs</span>
today = datetime.date.today().isoformat()
<span class="kw">for</span> pdf <span class="kw">in</span> Path(<span class="str">"reports"</span>).glob(<span class="str">"*.pdf"</span>):
    pdf.rename(pdf.parent / <span class="str">f"{today}_{pdf.name}"</span>)

<span class="com"># Copy / move / archive</span>
shutil.copy(<span class="str">"config.yml"</span>, <span class="str">"config.yml.bak"</span>)
shutil.move(<span class="str">"old/"</span>, <span class="str">"archive/old/"</span>)
shutil.make_archive(<span class="str">"backup"</span>, <span class="str">"gztar"</span>, <span class="str">"/data"</span>)  <span class="com"># → backup.tar.gz</span>

<span class="com"># Disk usage check</span>
total, used, free = shutil.disk_usage(<span class="str">"/"</span>)
<span class="fn">print</span>(<span class="str">f"Free: {free // (2**30)} GB"</span>)</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">A REAL AUTOMATION SCRIPT</div>
      <div class="concept-title">Putting It Together — A Disk Space Alert</div>
      <div class="code-block"><span class="com">#!/usr/bin/env python3</span>
<span class="str">&quot;&quot;&quot;Alert if any mounted disk exceeds 85% usage.&quot;&quot;&quot;</span>
<span class="kw">import</span> shutil, smtplib, sys
<span class="kw">from</span> pathlib <span class="kw">import</span> Path

THRESHOLD = <span class="num">85</span>   <span class="com"># percent</span>
MOUNTS = [<span class="str">"/"</span>, <span class="str">"/var"</span>, <span class="str">"/home"</span>]

<span class="kw">def</span> <span class="fn">check_disk</span>(path):
    <span class="kw">if</span> <span class="kw">not</span> Path(path).exists():
        <span class="kw">return</span> <span class="kw">None</span>
    total, used, free = shutil.disk_usage(path)
    percent = (used / total) * <span class="num">100</span>
    <span class="kw">return</span> percent

<span class="kw">def</span> <span class="fn">main</span>():
    alerts = []
    <span class="kw">for</span> mount <span class="kw">in</span> MOUNTS:
        pct = check_disk(mount)
        <span class="kw">if</span> pct <span class="kw">and</span> pct &gt; THRESHOLD:
            alerts.append(<span class="str">f"{mount}: {pct:.1f}% full"</span>)

    <span class="kw">if</span> alerts:
        <span class="fn">print</span>(<span class="str">"DISK ALERT:"</span>)
        <span class="kw">for</span> a <span class="kw">in</span> alerts:
            <span class="fn">print</span>(<span class="str">f"  {a}"</span>)
        sys.exit(<span class="num">1</span>)   <span class="com"># non-zero = alerting systems notice</span>
    <span class="kw">else</span>:
        <span class="fn">print</span>(<span class="str">"All disks healthy"</span>)

<span class="kw">if</span> __name__ == <span class="str">"__main__"</span>:
    main()

<span class="com"># Schedule it with cron: */15 * * * * /usr/bin/python3 /opt/disk_check.py</span></div>
    </div>
  </div>
</div>

<!-- ── TOPIC: BUILDING A REST API ────────────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">🌐</span>
    <span class="topic-name">Building a REST API — From Zero to Running Endpoint</span>
    <span class="topic-badge">SCRIPT • Practical</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">FASTAPI</div>
      <div class="concept-title">The Modern Way to Build APIs in Python</div>
      <div class="concept-desc">FastAPI is the most popular modern Python web framework for building APIs. It's fast, gives you automatic interactive docs (Swagger UI), and validates request data automatically using type hints. Perfect for building internal tools, automation endpoints, and microservices.</div>
      <div class="code-block"><span class="com"># pip install fastapi uvicorn</span>
<span class="kw">from</span> fastapi <span class="kw">import</span> FastAPI, HTTPException
<span class="kw">from</span> pydantic <span class="kw">import</span> BaseModel

app = FastAPI()

<span class="com"># Pydantic model — auto-validates incoming JSON</span>
<span class="kw">class</span> <span class="fn">Server</span>(BaseModel):
    hostname: str
    ip: str
    is_active: bool = <span class="kw">True</span>

<span class="com"># In-memory "database" for the example</span>
servers = {}

<span class="fn">@app.get</span>(<span class="str">"/"</span>)
<span class="kw">def</span> <span class="fn">root</span>():
    <span class="kw">return</span> {<span class="str">"status"</span>: <span class="str">"ok"</span>}

<span class="fn">@app.get</span>(<span class="str">"/servers"</span>)
<span class="kw">def</span> <span class="fn">list_servers</span>():
    <span class="kw">return</span> <span class="fn">list</span>(servers.values())

<span class="fn">@app.get</span>(<span class="str">"/servers/{hostname}"</span>)
<span class="kw">def</span> <span class="fn">get_server</span>(hostname: str):
    <span class="kw">if</span> hostname <span class="kw">not</span> <span class="kw">in</span> servers:
        <span class="kw">raise</span> HTTPException(status_code=<span class="num">404</span>, detail=<span class="str">"Not found"</span>)
    <span class="kw">return</span> servers[hostname]

<span class="fn">@app.post</span>(<span class="str">"/servers"</span>)
<span class="kw">def</span> <span class="fn">create_server</span>(server: Server):
    servers[server.hostname] = server
    <span class="kw">return</span> {<span class="str">"created"</span>: server.hostname}

<span class="com"># Run it:  uvicorn main:app --reload</span>
<span class="com"># Auto docs at: http://localhost:8000/docs</span></div>
    </div>
  </div>
</div>
"""

# ─────────────────────────────── GRC wave 16 ─────────────────────────────────
GRC_SENTINEL = "<!-- BEGINNER16-GRC v1 -->"
GRC_CONTENT = """
<!-- BEGINNER16-GRC v1 -->
<!-- ── TOPIC: THIRD-PARTY RISK MANAGEMENT ────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">🤝</span>
    <span class="topic-name">Third-Party Risk — Your Security Is Only as Strong as Your Vendors</span>
    <span class="topic-badge">GRC • Essential</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">WHY IT MATTERS</div>
      <div class="concept-title">You Outsource the Work, Not the Risk</div>
      <div class="concept-desc">Modern organizations rely on dozens or hundreds of third parties: cloud providers, SaaS apps, payment processors, contractors, managed service providers. Each one is a potential entry point. Some of the biggest breaches in history came through third parties — Target (2013) was breached via an HVAC vendor's credentials. You can outsource a function, but you cannot outsource accountability for the risk.</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">THE VENDOR RISK LIFECYCLE</div>
      <div class="concept-title">Managing Risk Across the Relationship</div>
      <table class="ai-table">
        <thead><tr><th>Phase</th><th>Activity</th></tr></thead>
        <tbody>
          <tr><td>1. Due diligence</td><td>Before signing: assess the vendor's security posture (questionnaires, certifications)</td></tr>
          <tr><td>2. Contracting</td><td>Bake security requirements into the contract: SLAs, breach notification, right to audit, data handling</td></tr>
          <tr><td>3. Onboarding</td><td>Grant least-privilege access; integrate securely</td></tr>
          <tr><td>4. Ongoing monitoring</td><td>Periodic reassessment; watch for the vendor's own breaches</td></tr>
          <tr><td>5. Offboarding</td><td>Revoke all access, retrieve/destroy data, confirm in writing</td></tr>
        </tbody>
      </table>
    </div>
    <div class="concept-card">
      <div class="concept-label">ASSESSMENT TOOLS</div>
      <div class="concept-title">How You Actually Evaluate a Vendor</div>
      <table class="ai-table">
        <thead><tr><th>Tool</th><th>What It Is</th><th>Strength</th></tr></thead>
        <tbody>
          <tr><td>SOC 2 Type II report</td><td>Independent audit of a vendor's controls over a time period</td><td>Gold standard — verified by a third party</td></tr>
          <tr><td>ISO 27001 certificate</td><td>Proof of a certified information security management system</td><td>Internationally recognized</td></tr>
          <tr><td>Security questionnaire (SIG, CAIQ)</td><td>Standardized list of security questions</td><td>Broad coverage, but self-reported</td></tr>
          <tr><td>Penetration test report</td><td>Evidence the vendor tests their own security</td><td>Shows real-world testing</td></tr>
          <tr><td>Security ratings (BitSight, SecurityScorecard)</td><td>External scan-based scoring</td><td>Continuous, outside-in view</td></tr>
        </tbody>
      </table>
    </div>
    <div class="concept-card">
      <div class="concept-label">FOURTH-PARTY RISK</div>
      <div class="concept-title">Your Vendors Have Vendors Too</div>
      <div class="concept-desc">It goes deeper. Your SaaS vendor relies on AWS, which relies on... a chain of dependencies. A "fourth party" is your vendor's vendor. The 2020 SolarWinds attack and the 2023 MOVEit breach showed how a single compromised supplier can cascade through thousands of downstream organizations. This is why understanding your full supply chain — and concentration risk (everyone depending on the same provider) — matters.</div>
    </div>
  </div>
</div>

<!-- ── TOPIC: SECURITY AWARENESS PROGRAMS ────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">📣</span>
    <span class="topic-name">Security Awareness — Turning People Into a Defense Layer</span>
    <span class="topic-badge">GRC • Human Factor</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">THE HUMAN FIREWALL</div>
      <div class="concept-title">People Are the Most Targeted Attack Surface</div>
      <div class="concept-desc">The vast majority of breaches involve a human element — clicking a phishing link, weak passwords, misconfiguration, falling for social engineering. You can buy the best technical controls in the world, but a single tricked employee can bypass all of them. Security awareness training turns employees from the weakest link into an active layer of defense — the "human firewall."</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">WHAT GOOD TRAINING LOOKS LIKE</div>
      <div class="concept-title">Beyond the Annual Boring Video</div>
      <table class="ai-table">
        <thead><tr><th>Element</th><th>Why It Works</th></tr></thead>
        <tbody>
          <tr><td>Phishing simulations</td><td>Safe practice — send fake phish, coach those who click (don't punish)</td></tr>
          <tr><td>Bite-sized + frequent</td><td>Short, regular nudges beat one long annual session</td></tr>
          <tr><td>Role-specific</td><td>Finance gets BEC training; devs get secure coding</td></tr>
          <tr><td>Real examples</td><td>Show actual attacks the org has seen — relevance drives retention</td></tr>
          <tr><td>Easy reporting</td><td>One-click "report phish" button — make doing the right thing frictionless</td></tr>
          <tr><td>Positive culture</td><td>Reward reporting; never shame mistakes — fear makes people hide incidents</td></tr>
        </tbody>
      </table>
    </div>
  </div>
</div>
"""

# ─────────────────────────────── THREAT wave 16 ──────────────────────────────
THREAT_SENTINEL = "<!-- BEGINNER16-THREAT v1 -->"
THREAT_CONTENT = """
<!-- BEGINNER16-THREAT v1 -->
<!-- ── TOPIC: DIGITAL FORENSICS BASICS ───────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">🔬</span>
    <span class="topic-name">Digital Forensics — Reconstructing What Happened</span>
    <span class="topic-badge">THREAT • Investigation</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">WHAT IS DFIR</div>
      <div class="concept-title">Digital Forensics &amp; Incident Response</div>
      <div class="concept-desc">When something bad happens — a breach, insider theft, malware — digital forensics is the discipline of collecting, preserving, and analyzing evidence to answer: what happened, when, how, and who. Forensics must be done carefully because the findings may end up in court, or drive critical business decisions. The cardinal rule: <strong>preserve the original, work on copies.</strong></div>
    </div>
    <div class="concept-card">
      <div class="concept-label">ORDER OF VOLATILITY</div>
      <div class="concept-title">Collect the Most Fragile Evidence First</div>
      <div class="concept-desc">Some evidence disappears fast (RAM vanishes on shutdown); some persists (disk). When collecting evidence, work from most volatile to least — RFC 3227's order of volatility — or you'll lose the fragile stuff forever.</div>
      <table class="ai-table">
        <thead><tr><th>Order</th><th>Source</th><th>Lifetime</th></tr></thead>
        <tbody>
          <tr><td>1 (most volatile)</td><td>CPU registers, cache</td><td>Nanoseconds</td></tr>
          <tr><td>2</td><td>RAM (running processes, network connections, encryption keys)</td><td>Until power off</td></tr>
          <tr><td>3</td><td>Network state, routing tables, ARP cache</td><td>Seconds to minutes</td></tr>
          <tr><td>4</td><td>Running processes, temp files</td><td>Until reboot</td></tr>
          <tr><td>5</td><td>Disk (files, logs, deleted-but-recoverable data)</td><td>Persistent</td></tr>
          <tr><td>6 (least volatile)</td><td>Backups, archived logs, printouts</td><td>Long-term</td></tr>
        </tbody>
      </table>
    </div>
    <div class="concept-card">
      <div class="concept-label">CHAIN OF CUSTODY</div>
      <div class="concept-title">Proving the Evidence Wasn't Tampered With</div>
      <div class="concept-desc">Chain of custody is the documented, unbroken trail showing who handled evidence, when, why, and how — from collection to courtroom. If you can't prove the evidence wasn't altered, it's worthless. Two technical pillars support this:</div>
      <table class="ai-table">
        <thead><tr><th>Technique</th><th>Purpose</th></tr></thead>
        <tbody>
          <tr><td>Hashing (SHA-256)</td><td>Hash the evidence at collection. Any change = different hash = tampering detected.</td></tr>
          <tr><td>Write blockers</td><td>Hardware/software that allows reading a drive but prevents any writes to it</td></tr>
          <tr><td>Forensic imaging</td><td>Bit-for-bit copy (<code>dd</code>, FTK Imager). Analyze the image, never the original.</td></tr>
          <tr><td>Documentation</td><td>Log every transfer: who, what, when, where, why — signed</td></tr>
        </tbody>
      </table>
      <div class="code-block"><span class="com"># Create a forensic disk image and hash it (Linux)</span>
sudo dd if=/dev/sdb of=evidence.img bs=4M status=progress

<span class="com"># Hash BEFORE and AFTER to prove integrity</span>
sha256sum /dev/sdb        <span class="com"># hash of original</span>
sha256sum evidence.img    <span class="com"># must match — proves a faithful copy</span>

<span class="com"># Better: use a tool that images AND hashes in one step</span>
<span class="com"># dc3dd, ewfacquire (E01 format), or FTK Imager</span></div>
    </div>
    <div class="concept-card">
      <div class="concept-label">ARTIFACTS TO EXAMINE</div>
      <div class="concept-title">Where the Evidence Lives</div>
      <table class="ai-table">
        <thead><tr><th>Artifact</th><th>What It Reveals</th></tr></thead>
        <tbody>
          <tr><td>Memory dump</td><td>Running malware, decryption keys, network connections, injected code</td></tr>
          <tr><td>Windows Event Logs</td><td>Logons, process creation, service installs, account changes</td></tr>
          <tr><td>Registry</td><td>Persistence mechanisms, USB history, recently run programs</td></tr>
          <tr><td>Browser history/cache</td><td>Downloaded files, visited sites, exfil destinations</td></tr>
          <tr><td>Prefetch / Shimcache / Amcache</td><td>Evidence of program execution (even if deleted)</td></tr>
          <tr><td>File system timestamps (MACB)</td><td>Modified, Accessed, Created, Birth — timeline reconstruction</td></tr>
          <tr><td>Network captures (PCAP)</td><td>C2 traffic, data exfiltration, lateral movement</td></tr>
        </tbody>
      </table>
    </div>
  </div>
</div>
"""

# ─────────────────────────────── LINUX wave 16 ───────────────────────────────
LINUX_SENTINEL = "<!-- BEGINNER16-LINUX v1 -->"
LINUX_CONTENT = """
<!-- BEGINNER16-LINUX v1 -->
<!-- ── TOPIC: FILE PERMISSIONS DEEP DIVE ─────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">🔑</span>
    <span class="topic-name">Linux Permissions — Who Can Do What, In Depth</span>
    <span class="topic-badge">LINUX • Essential</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">THE PERMISSION MODEL</div>
      <div class="concept-title">Reading rwxr-xr-- at a Glance</div>
      <div class="concept-desc">Every Linux file has an owner, a group, and a set of permissions for three categories: user (owner), group, and others. Permissions are read (r), write (w), and execute (x). When you run <code>ls -l</code>, the first 10 characters tell the whole story.</div>
      <div class="code-block"><span class="com"># ls -l output explained</span>
-rwxr-xr--  1  alice  devs  2048  Jan 15  script.sh
^└┬┘└┬┘└┬┘     └─┬─┘  └┬─┘
│ │  │  │        │     └── group name
│ │  │  │        └──────── owner name
│ │  │  └── others: r-- (read only)
│ │  └───── group:  r-x (read + execute)
│ └──────── owner:  rwx (read + write + execute)
└────────── type: - file, d dir, l symlink

<span class="com"># Numeric (octal) — each digit is a sum:  r=4  w=2  x=1</span>
rwx = 4+2+1 = 7
r-x = 4+0+1 = 5
r-- = 4+0+0 = 4
<span class="com"># So rwxr-xr-- = 754</span></div>
    </div>
    <div class="concept-card">
      <div class="concept-label">CHMOD &amp; CHOWN</div>
      <div class="concept-title">Changing Permissions and Ownership</div>
      <div class="code-block"><span class="com"># Numeric (octal) mode — set absolute permissions</span>
chmod 755 script.sh        <span class="com"># rwxr-xr-x (common for scripts)</span>
chmod 644 file.txt         <span class="com"># rw-r--r-- (common for files)</span>
chmod 600 ~/.ssh/id_rsa    <span class="com"># rw------- (private keys MUST be this)</span>
chmod 700 ~/.ssh           <span class="com"># rwx------ (private dir)</span>

<span class="com"># Symbolic mode — modify relative to current</span>
chmod u+x script.sh        <span class="com"># add execute for owner</span>
chmod g-w file.txt         <span class="com"># remove write for group</span>
chmod o= secret.txt        <span class="com"># remove ALL for others</span>
chmod a+r public.txt       <span class="com"># add read for all (a = all)</span>
chmod -R 755 /var/www      <span class="com"># recursive</span>

<span class="com"># Change ownership (usually needs sudo)</span>
chown alice file.txt           <span class="com"># change owner</span>
chown alice:devs file.txt      <span class="com"># change owner AND group</span>
chown -R www-data:www-data /var/www   <span class="com"># recursive</span>
chgrp devs file.txt            <span class="com"># change group only</span></div>
    </div>
    <div class="concept-card">
      <div class="concept-label">SPECIAL PERMISSION BITS</div>
      <div class="concept-title">SUID, SGID, and the Sticky Bit</div>
      <div class="concept-desc">Beyond rwx, there are three special bits that change execution and inheritance behavior. These matter for both administration and security (SUID binaries are a classic privilege-escalation target).</div>
      <table class="ai-table">
        <thead><tr><th>Bit</th><th>Octal</th><th>Effect</th><th>Example</th></tr></thead>
        <tbody>
          <tr><td>SUID</td><td>4000</td><td>Run file as the FILE's owner, not the runner</td><td><code>passwd</code> runs as root so users can change their own password</td></tr>
          <tr><td>SGID</td><td>2000</td><td>On file: run as group. On dir: new files inherit the dir's group</td><td>Shared project directories</td></tr>
          <tr><td>Sticky</td><td>1000</td><td>On dir: only the file owner can delete their files</td><td><code>/tmp</code> — anyone can write, but can't delete others' files</td></tr>
        </tbody>
      </table>
      <div class="code-block"><span class="com"># Set special bits</span>
chmod u+s binary       <span class="com"># SUID</span>
chmod g+s shared_dir   <span class="com"># SGID</span>
chmod +t /shared       <span class="com"># sticky bit</span>

<span class="com"># SECURITY: hunt for SUID binaries (privilege escalation recon)</span>
find / -perm -4000 -type f 2&gt;/dev/null</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">UMASK & ACLs</div>
      <div class="concept-title">Default Permissions and Fine-Grained Control</div>
      <div class="code-block"><span class="com"># umask — sets DEFAULT permissions for new files</span>
umask                  <span class="com"># show current (often 022)</span>
<span class="com"># New files: 666 - umask. New dirs: 777 - umask</span>
<span class="com"># umask 022 → files 644, dirs 755</span>

<span class="com"># ACLs — go beyond owner/group/other for specific users</span>
getfacl file.txt                        <span class="com"># view ACLs</span>
setfacl -m u:bob:rw file.txt            <span class="com"># give bob read+write</span>
setfacl -m g:contractors:r file.txt     <span class="com"># give a group read</span>
setfacl -x u:bob file.txt               <span class="com"># remove bob's ACL</span>
<span class="com"># A "+" after permissions in ls -l means ACLs are present</span></div>
    </div>
    <div class="concept-card">
      <div class="concept-label">MANDATORY ACCESS CONTROL</div>
      <div class="concept-title">SELinux and AppArmor</div>
      <div class="concept-desc">Standard permissions are Discretionary Access Control (DAC) — owners decide. SELinux (Red Hat) and AppArmor (Ubuntu/SUSE) add Mandatory Access Control (MAC): a system-wide policy enforces what processes can do, regardless of file ownership. Even root is constrained. This contains compromised services — a hacked web server can only touch what its policy allows.</div>
      <div class="code-block"><span class="com"># SELinux (Red Hat family)</span>
getenforce                  <span class="com"># Enforcing / Permissive / Disabled</span>
sestatus                    <span class="com"># detailed status</span>
ls -Z file.txt              <span class="com"># show SELinux context</span>
setenforce 0                <span class="com"># temporarily permissive (testing)</span>
<span class="com"># Tip: don't disable SELinux to "fix" an issue — fix the policy</span>

<span class="com"># AppArmor (Ubuntu/Debian/SUSE)</span>
sudo aa-status              <span class="com"># list profiles and their mode</span>
sudo aa-complain /path/to/program   <span class="com"># log violations, don't block</span>
sudo aa-enforce /path/to/program    <span class="com"># enforce the profile</span></div>
    </div>
  </div>
</div>
"""

# ─────────────────────────────── LIFESTYLE wave 16 ───────────────────────────
LIFE_SENTINEL = "<!-- BEGINNER16-LIFE v1 -->"
LIFE_CONTENT = """
<!-- BEGINNER16-LIFE v1 -->
<!-- ── TOPIC: BUILDING A HOME LAB ────────────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">🧰</span>
    <span class="topic-name">Building a Home Lab — Where You Actually Learn</span>
    <span class="topic-badge">LIFESTYLE • Hands-On</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">WHY A HOME LAB</div>
      <div class="concept-title">Reading About IT ≠ Doing IT</div>
      <div class="concept-desc">You cannot learn to swim from a book. The single biggest accelerator for an IT career is a home lab — a safe environment where you can break things, experiment, and build real skills with zero risk to production or your job. Employers can tell in minutes who has hands-on experience and who only memorized concepts. A home lab is also the best source of talking points in interviews ("Tell me about something you built").</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">START FREE</div>
      <div class="concept-title">You Don't Need to Spend a Dime to Begin</div>
      <table class="ai-table">
        <thead><tr><th>Approach</th><th>What You Need</th><th>Good For</th></tr></thead>
        <tbody>
          <tr><td>VirtualBox / VMware (free tiers)</td><td>Your existing laptop + free hypervisor</td><td>Running Linux VMs, building networks of VMs</td></tr>
          <tr><td>WSL2 (Windows)</td><td>Windows 10/11</td><td>Real Linux on your Windows machine instantly</td></tr>
          <tr><td>Docker Desktop</td><td>Any laptop</td><td>Spinning up services (databases, web apps) in seconds</td></tr>
          <tr><td>Cloud free tiers</td><td>AWS/Azure/GCP/Oracle free account</td><td>Real cloud experience (watch the billing!)</td></tr>
          <tr><td>TryHackMe / HackTheBox</td><td>A browser</td><td>Guided security labs, no setup needed</td></tr>
        </tbody>
      </table>
    </div>
    <div class="concept-card">
      <div class="concept-label">LAB PROJECT IDEAS</div>
      <div class="concept-title">Build These to Learn Real Skills</div>
      <table class="ai-table">
        <thead><tr><th>Project</th><th>Skills You'll Build</th></tr></thead>
        <tbody>
          <tr><td>Set up a Linux server + host a website</td><td>Linux admin, networking, web servers, DNS</td></tr>
          <tr><td>Build an Active Directory lab (Windows Server + clients)</td><td>AD, GPO, Windows admin — huge for enterprise IT</td></tr>
          <tr><td>Deploy a SIEM (Wazuh, Security Onion) + generate logs</td><td>Log analysis, detection, SOC skills</td></tr>
          <tr><td>Set up pfSense/OPNsense firewall + segment a network</td><td>Firewalls, VLANs, routing, network security</td></tr>
          <tr><td>Run a vulnerable VM (Metasploitable) + attack it</td><td>Pentesting, exploitation, defense (in YOUR lab only)</td></tr>
          <tr><td>Self-host services (Pi-hole, Nextcloud) on a Raspberry Pi</td><td>Practical sysadmin, DNS, services, troubleshooting</td></tr>
          <tr><td>Build a CI/CD pipeline for a small app</td><td>Git, automation, Docker, DevOps</td></tr>
        </tbody>
      </table>
      <div class="concept-desc"><strong>Document everything.</strong> Write up what you built on a blog or GitHub README. This becomes your portfolio — proof of skills that beats any line on a resume.</div>
    </div>
  </div>
</div>

<!-- ── TOPIC: CERTIFICATION ROADMAP ──────────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">📜</span>
    <span class="topic-name">Certifications — The Roadmap (and How to Actually Study)</span>
    <span class="topic-badge">LIFESTYLE • Career</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">THE TRUTH ABOUT CERTS</div>
      <div class="concept-title">Certs Open Doors, Skills Keep You In the Room</div>
      <div class="concept-desc">Certifications get your resume past HR filters and prove baseline knowledge — they're especially valuable early in your career when you don't have experience to point to. But a cert without hands-on skill is hollow; experienced interviewers see through it fast. The best approach: pair every cert with a home lab project that proves you can actually do it.</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">FOUNDATIONAL CERTS</div>
      <div class="concept-title">Where to Start (Vendor-Neutral)</div>
      <table class="ai-table">
        <thead><tr><th>Cert</th><th>Domain</th><th>Why</th></tr></thead>
        <tbody>
          <tr><td>CompTIA A+</td><td>IT fundamentals / help desk</td><td>Classic entry point; hardware, OS, troubleshooting</td></tr>
          <tr><td>CompTIA Network+</td><td>Networking</td><td>Solid vendor-neutral networking foundation</td></tr>
          <tr><td>CompTIA Security+</td><td>Security</td><td>The standard entry security cert; DoD-approved (8570)</td></tr>
          <tr><td>CompTIA Linux+ / LPIC-1</td><td>Linux</td><td>Proves Linux admin fundamentals</td></tr>
          <tr><td>Cisco CCNA</td><td>Networking (Cisco)</td><td>Deep, respected networking cert</td></tr>
        </tbody>
      </table>
    </div>
    <div class="concept-card">
      <div class="concept-label">SPECIALIZATION CERTS</div>
      <div class="concept-title">Once You Pick a Direction</div>
      <table class="ai-table">
        <thead><tr><th>Path</th><th>Certs to Target</th></tr></thead>
        <tbody>
          <tr><td>Cloud</td><td>AWS Solutions Architect, Azure AZ-104, Google ACE</td></tr>
          <tr><td>Security (defense)</td><td>CySA+, GCIH, Blue Team Level 1 (BTL1)</td></tr>
          <tr><td>Offensive security</td><td>eJPT → PNPT / OSCP (hands-on, highly respected)</td></tr>
          <tr><td>GRC / management</td><td>CISA, CISM, CISSP (needs experience)</td></tr>
          <tr><td>DevOps / Cloud</td><td>Terraform Associate, CKA (Kubernetes), Docker</td></tr>
        </tbody>
      </table>
    </div>
    <div class="concept-card">
      <div class="concept-label">HOW TO STUDY</div>
      <div class="concept-title">Evidence-Based Study Strategy</div>
      <table class="ai-table">
        <thead><tr><th>Technique</th><th>How to Apply It</th></tr></thead>
        <tbody>
          <tr><td>Active recall</td><td>Test yourself constantly — flashcards, practice exams. Don't just re-read.</td></tr>
          <tr><td>Spaced repetition</td><td>Review at increasing intervals (Anki). Beats cramming for retention.</td></tr>
          <tr><td>Practice exams</td><td>Take them until you consistently score 85%+ before the real one</td></tr>
          <tr><td>Hands-on lab</td><td>Build what you study — knowledge sticks when you DO it</td></tr>
          <tr><td>Teach it</td><td>Explain a concept out loud or in writing — gaps reveal themselves (Feynman)</td></tr>
          <tr><td>Set an exam date</td><td>Book it. A deadline focuses study like nothing else.</td></tr>
        </tbody>
      </table>
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
        (GRC_INJECT_ANCHOR,    GRC_SENTINEL,    GRC_CONTENT),
        (THREAT_INJECT_ANCHOR, THREAT_SENTINEL, THREAT_CONTENT),
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
