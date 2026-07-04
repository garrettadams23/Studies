#!/usr/bin/env python3
"""
patch_beginner_concepts_v14.py — Wave 14: Pentest methodology,
threat hunting, PowerShell basics, AI ethics, military decision-making.

New sentinels:
  BEGINNER14-PENTEST v1  — Web app pentest methodology, OWASP testing, Burp Suite
  BEGINNER14-THREAT v1   — Threat hunting, hypothesis-driven approach, tools
  BEGINNER14-SHORTCUT v1 — PowerShell basics for Windows/cross-platform
  BEGINNER14-AI v1       — AI ethics, bias, responsible AI, limitations
  BEGINNER14-MIL v1      — OODA loop, commander's intent, decision-making under pressure
"""
from pathlib import Path

PENTEST_INJECT_ANCHOR  = "<!-- /domain-body pentest -->"
THREAT_INJECT_ANCHOR   = "<!-- /domain-body threat -->"
SHORTCUT_INJECT_ANCHOR = "<!-- /domain-body shortcuts -->"
AI_INJECT_ANCHOR       = "<!-- /domain-body ai -->"
MIL_INJECT_ANCHOR      = "<!-- /domain-body military -->"

# ─────────────────────────────── PENTEST wave 14 ─────────────────────────────
PENTEST_SENTINEL = "<!-- BEGINNER14-PENTEST v1 -->"
PENTEST_CONTENT = """
<!-- BEGINNER14-PENTEST v1 -->
<!-- ── TOPIC: WEB APPLICATION PENTESTING ─────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">🕸️</span>
    <span class="topic-name">Web Application Pentesting — Hacking the Web Safely</span>
    <span class="topic-badge">PENTEST • Methodology</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">WEB APP ATTACK SURFACE</div>
      <div class="concept-title">Where Web Vulnerabilities Live</div>
      <div class="concept-desc">Web applications are the most attacked surface in modern environments. Unlike network pentesting (ports and protocols), web app testing focuses on application logic, input handling, and authentication. The good news: most web vulnerabilities are predictable and well-documented (OWASP). The bad news: developers keep repeating the same mistakes.</div>
      <table class="ai-table">
        <thead><tr><th>Layer</th><th>What to Test</th><th>Common Findings</th></tr></thead>
        <tbody>
          <tr><td>Authentication</td><td>Login, password reset, MFA bypass</td><td>Weak passwords, enumeration, broken token reset</td></tr>
          <tr><td>Authorization</td><td>Horizontal/vertical privilege escalation</td><td>IDOR — access other users' data by changing IDs</td></tr>
          <tr><td>Input Handling</td><td>Forms, query params, headers, file uploads</td><td>SQLi, XSS, XXE, command injection</td></tr>
          <tr><td>Session Management</td><td>Cookies, tokens, session fixation</td><td>Predictable tokens, missing Secure/HttpOnly flags</td></tr>
          <tr><td>Business Logic</td><td>Purchase flows, transfers, state machines</td><td>Negative quantities, price manipulation, race conditions</td></tr>
          <tr><td>API Endpoints</td><td>REST/GraphQL endpoints</td><td>Missing auth, verbose errors, mass assignment</td></tr>
        </tbody>
      </table>
    </div>
    <div class="concept-card">
      <div class="concept-label">BURP SUITE BASICS</div>
      <div class="concept-title">The Swiss Army Knife for Web Testing</div>
      <div class="concept-desc">Burp Suite is the industry-standard web proxy for intercepting, modifying, and replaying HTTP/HTTPS traffic. The Community edition is free and powerful enough for most learning. Professional adds the scanner.</div>
      <table class="ai-table">
        <thead><tr><th>Tool</th><th>Purpose</th><th>Beginner Use</th></tr></thead>
        <tbody>
          <tr><td>Proxy → Intercept</td><td>Pause and inspect every request</td><td>See what the browser actually sends</td></tr>
          <tr><td>Proxy → HTTP History</td><td>Log of all requests made</td><td>Find interesting endpoints and parameters</td></tr>
          <tr><td>Repeater</td><td>Resend and modify individual requests</td><td>Test input handling by changing values manually</td></tr>
          <tr><td>Intruder</td><td>Automated fuzzing with payload lists</td><td>Password spraying, parameter enumeration</td></tr>
          <tr><td>Decoder</td><td>Encode/decode base64, URL, HTML, hex</td><td>Decode tokens and encoded parameters</td></tr>
          <tr><td>Scanner (Pro)</td><td>Automated vulnerability scanning</td><td>Passive and active scanning</td></tr>
        </tbody>
      </table>
    </div>
    <div class="concept-card">
      <div class="concept-label">IDOR DEEP DIVE</div>
      <div class="concept-title">Insecure Direct Object Reference — The #1 Finding</div>
      <div class="concept-desc">IDOR (now categorized under Broken Access Control, OWASP A01) occurs when an application uses user-controllable references to access objects without verifying the user is authorized. It's the most common web vulnerability by volume.</div>
      <div class="code-block"><span class="com"># Vulnerable pattern — user ID directly in URL</span>
GET /api/users/1234/profile      <span class="com"># your profile</span>
GET /api/users/1235/profile      <span class="com"># someone else's — do you get it?</span>

<span class="com"># Vulnerable pattern — order ID in parameter</span>
GET /orders?id=8821              <span class="com"># your order</span>
GET /orders?id=8820              <span class="com"># try decrementing — another user's order?</span>

<span class="com"># Where to look</span>
- Numeric IDs in URLs, query params, request bodies
- GUIDs (sometimes predictable if v1 — time-based)
- Encoded values — decode them first (base64, hex)
- Hidden form fields with IDs

<span class="com"># How to test</span>
1. Create two test accounts (Alice and Bob)
2. As Alice, perform action that creates a resource → note the ID
3. Log in as Bob, try to access the same resource ID
4. If Bob can access Alice's resource = IDOR</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">COMMAND INJECTION</div>
      <div class="concept-title">When the App Runs Your Input as Shell Commands</div>
      <div class="concept-desc">Command injection occurs when user input is passed to a system shell without sanitization. If you can get your input executed as OS commands, you typically own the server. Critical severity — always.</div>
      <div class="code-block"><span class="com"># Common in features that: ping IPs, resolve DNS, process files,</span>
<span class="com"># run nmap, send email via sendmail, resize images via ImageMagick</span>

<span class="com"># Basic test payloads — try in any input field</span>
; id                  <span class="com"># semicolon chains commands</span>
&amp;&amp; id                 <span class="com"># run if first cmd succeeds</span>
|| id                 <span class="com"># run if first cmd fails</span>
`id`                  <span class="com"># backtick subshell</span>
$(id)                 <span class="com"># $() subshell (URL: %24%28id%29)</span>
| id                  <span class="com"># pipe output</span>

<span class="com"># If you see "uid=33(www-data)" in the response — confirmed!</span>

<span class="com"># Blind injection — no output visible, infer via timing</span>
; sleep 5             <span class="com"># if response delays 5s — blind injection exists</span></div>
    </div>
  </div>
</div>

<!-- ── TOPIC: RECON METHODOLOGY ──────────────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">🔭</span>
    <span class="topic-name">Recon Methodology — Intelligence Before Attack</span>
    <span class="topic-badge">PENTEST • Methodology</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">PASSIVE RECON TOOLS</div>
      <div class="concept-title">Gather Intel Without Touching the Target</div>
      <div class="concept-desc">Passive recon uses publicly available information — no packets sent to the target. This is legal and leaves no trace. Do it before any active testing to understand the target's footprint.</div>
      <table class="ai-table">
        <thead><tr><th>Tool/Resource</th><th>What It Finds</th><th>Example Use</th></tr></thead>
        <tbody>
          <tr><td>WHOIS</td><td>Domain ownership, registrar, dates</td><td><code>whois target.com</code></td></tr>
          <tr><td>Shodan.io</td><td>Internet-facing devices and services</td><td>Search <code>hostname:target.com</code></td></tr>
          <tr><td>Censys.io</td><td>TLS certificates, open ports</td><td>Discover subdomains via cert transparency</td></tr>
          <tr><td>crt.sh</td><td>Certificate transparency logs</td><td>Find all subdomains issued TLS certs</td></tr>
          <tr><td>Google Dorks</td><td>Indexed sensitive files</td><td><code>site:target.com filetype:pdf</code></td></tr>
          <tr><td>theHarvester</td><td>Emails, subdomains, IPs from public sources</td><td><code>theHarvester -d target.com -b google</code></td></tr>
          <tr><td>LinkedIn/social</td><td>Employee names, tech stack, org structure</td><td>Job postings reveal what software they use</td></tr>
          <tr><td>Wayback Machine</td><td>Old versions of the site</td><td>Find removed pages with sensitive info</td></tr>
        </tbody>
      </table>
    </div>
  </div>
</div>
"""

# ─────────────────────────────── THREAT wave 14 ──────────────────────────────
THREAT_SENTINEL = "<!-- BEGINNER14-THREAT v1 -->"
THREAT_CONTENT = """
<!-- BEGINNER14-THREAT v1 -->
<!-- ── TOPIC: THREAT HUNTING ─────────────────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">🏹</span>
    <span class="topic-name">Threat Hunting — Proactively Finding What Slipped Through</span>
    <span class="topic-badge">THREAT • Advanced</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">WHAT IS THREAT HUNTING</div>
      <div class="concept-title">The Difference Between Hunting and Alerting</div>
      <div class="concept-desc">Reactive security waits for alerts — SIEM detects something, you investigate. Threat hunting flips this: you <em>assume</em> the adversary is already in your network (a reasonable assumption for mature organizations), then proactively search for evidence of compromise. It requires no alert to trigger; you drive the investigation.</div>
      <table class="ai-table">
        <thead><tr><th>Concept</th><th>Alert-Based (Reactive)</th><th>Threat Hunting (Proactive)</th></tr></thead>
        <tbody>
          <tr><td>Trigger</td><td>SIEM rule fires</td><td>Hunter's hypothesis</td></tr>
          <tr><td>Starting point</td><td>Alert tells you where to look</td><td>You decide where to look</td></tr>
          <tr><td>Outcome</td><td>Confirm or dismiss alert</td><td>Find what rules missed; improve detection</td></tr>
          <tr><td>Skill required</td><td>Triage / analysis</td><td>Deep knowledge of attacker TTPs</td></tr>
          <tr><td>Maturity level</td><td>All orgs</td><td>Mature orgs (assume breach mindset)</td></tr>
        </tbody>
      </table>
    </div>
    <div class="concept-card">
      <div class="concept-label">THE HUNT PROCESS</div>
      <div class="concept-title">Hypothesis-Driven Hunting</div>
      <div class="concept-desc">Good threat hunting starts with a hypothesis based on threat intelligence, ATT&amp;CK techniques, or recent threat reports — not just "look for bad stuff." A structured hunt has a clear scope and produces either a confirmed finding or improved detection logic.</div>
      <table class="ai-table">
        <thead><tr><th>Step</th><th>Activity</th><th>Example</th></tr></thead>
        <tbody>
          <tr><td>1. Hypothesis</td><td>Define what attacker behavior you're looking for</td><td>"Living-off-the-land — attacker using built-in Windows tools (T1218)"</td></tr>
          <tr><td>2. Data collection</td><td>Identify relevant log sources</td><td>Windows Event Logs, Sysmon, EDR telemetry</td></tr>
          <tr><td>3. Investigation</td><td>Query, filter, and analyze data</td><td>Search for <code>mshta.exe</code>, <code>regsvr32.exe</code>, <code>certutil.exe</code> with unusual parent processes</td></tr>
          <tr><td>4. Triage</td><td>Separate normal from abnormal</td><td>Baseline normal use, flag deviations</td></tr>
          <tr><td>5. Response</td><td>Escalate findings, or...</td><td>Confirm incident → IR team</td></tr>
          <tr><td>6. Improve detection</td><td>Write new SIEM rules</td><td>Create alert for technique if no existing detection</td></tr>
        </tbody>
      </table>
    </div>
    <div class="concept-card">
      <div class="concept-label">LIVING OFF THE LAND</div>
      <div class="concept-title">LOLBins — Attackers Using Your Own Tools Against You</div>
      <div class="concept-desc">Modern attackers rarely drop custom malware immediately. Instead they abuse legitimate OS tools that are already present and trusted — harder to detect than malware. These are called LOLBins (Living Off the Land Binaries). Knowing which tools are commonly abused helps focus your hunts.</div>
      <table class="ai-table">
        <thead><tr><th>Tool</th><th>Legitimate Use</th><th>Attacker Abuse</th></tr></thead>
        <tbody>
          <tr><td><code>powershell.exe</code></td><td>Scripting, administration</td><td>Download + execute malware, encoded commands</td></tr>
          <tr><td><code>certutil.exe</code></td><td>Certificate management</td><td>Download files, decode base64 payloads</td></tr>
          <tr><td><code>mshta.exe</code></td><td>Run HTA applications</td><td>Execute malicious scripts from remote URLs</td></tr>
          <tr><td><code>regsvr32.exe</code></td><td>Register DLLs</td><td>Execute malicious scripts (Squiblydoo)</td></tr>
          <tr><td><code>wscript/cscript</code></td><td>Run VBS/JS scripts</td><td>Malicious scripts, fileless malware</td></tr>
          <tr><td><code>msiexec.exe</code></td><td>Install MSI packages</td><td>Remote payload delivery</td></tr>
          <tr><td><code>curl/wget</code> (Linux)</td><td>HTTP requests</td><td>Pull down next-stage payloads</td></tr>
        </tbody>
      </table>
    </div>
    <div class="concept-card">
      <div class="concept-label">THREAT INTEL FEEDS</div>
      <div class="concept-title">Fueling Your Hunts with Intelligence</div>
      <table class="ai-table">
        <thead><tr><th>Source</th><th>Type</th><th>Free?</th><th>Best For</th></tr></thead>
        <tbody>
          <tr><td>MITRE ATT&amp;CK</td><td>TTP framework</td><td>Yes</td><td>Hunt hypotheses, detection mapping</td></tr>
          <tr><td>AlienVault OTX</td><td>IOC feeds (IPs, hashes, domains)</td><td>Yes</td><td>Blocking bad IPs, checking IOCs</td></tr>
          <tr><td>VirusTotal</td><td>File/URL/IP reputation</td><td>Yes (limited)</td><td>Checking suspicious files and URLs</td></tr>
          <tr><td>Abuse.ch (MalwareBazaar, URLhaus)</td><td>Malware samples, malicious URLs</td><td>Yes</td><td>IOC lookup, firewall block lists</td></tr>
          <tr><td>CISA KEV</td><td>Known Exploited Vulnerabilities</td><td>Yes</td><td>Patch prioritization — these are being exploited NOW</td></tr>
          <tr><td>Recorded Future / Mandiant</td><td>Premium threat intel</td><td>No</td><td>Enterprise threat landscape, APT tracking</td></tr>
        </tbody>
      </table>
    </div>
  </div>
</div>
"""

# ─────────────────────────────── SHORTCUTS/POWERSHELL wave 14 ────────────────
SHORTCUT_SENTINEL = "<!-- BEGINNER14-SHORTCUT v1 -->"
SHORTCUT_CONTENT = """
<!-- BEGINNER14-SHORTCUT v1 -->
<!-- ── TOPIC: POWERSHELL BASICS ──────────────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">💙</span>
    <span class="topic-name">PowerShell — Windows (and Cross-Platform) Scripting</span>
    <span class="topic-badge">SHORTCUTS • Scripting</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">POWERSHELL VS CMD</div>
      <div class="concept-title">Why PowerShell Replaced Command Prompt</div>
      <div class="concept-desc">CMD (Command Prompt) is ancient — 1980s DOS heritage. PowerShell is a modern scripting environment built on .NET. Everything is an object (not just text), making it far more powerful. PowerShell Core (PS 7+) runs on Linux and Mac too — making it cross-platform. Windows admins and security teams must know it.</div>
      <table class="ai-table">
        <thead><tr><th>Feature</th><th>CMD</th><th>PowerShell</th></tr></thead>
        <tbody>
          <tr><td>Output type</td><td>Plain text</td><td>.NET objects (piped, filtered, sorted)</td></tr>
          <tr><td>Scripting</td><td>Batch files (.bat) — limited</td><td>Full scripting language (.ps1) with loops, functions, classes</td></tr>
          <tr><td>Piping</td><td>Text pipes</td><td>Object pipes — access properties directly</td></tr>
          <tr><td>Windows integration</td><td>Limited</td><td>Full access to WMI, .NET, COM, Registry</td></tr>
          <tr><td>Cross-platform</td><td>Windows only</td><td>PowerShell 7+ runs on Linux/Mac</td></tr>
          <tr><td>Security logging</td><td>Minimal</td><td>Transcription, ScriptBlock logging</td></tr>
        </tbody>
      </table>
    </div>
    <div class="concept-card">
      <div class="concept-label">CORE CONCEPTS</div>
      <div class="concept-title">Cmdlets, Objects, and the Pipeline</div>
      <div class="concept-desc">PowerShell commands are called <strong>cmdlets</strong> (pronounced "command-lets"). They follow a Verb-Noun naming pattern (<code>Get-Process</code>, <code>Set-Item</code>, <code>New-Item</code>). Output is objects with properties — you can access, filter, and pipe them.</div>
      <div class="code-block"><span class="com"># Get-Help is your best friend</span>
Get-Help Get-Process
Get-Help Get-Process -Examples
Get-Help *service*          <span class="com"># find cmdlets about services</span>

<span class="com"># Basic navigation (aliases match Linux commands)</span>
ls                          <span class="com"># alias for Get-ChildItem</span>
cd C:\\Users\\Alice           <span class="com"># alias for Set-Location</span>
pwd                         <span class="com"># Print Working Directory</span>
cat file.txt                <span class="com"># alias for Get-Content</span>
cp source dest              <span class="com"># alias for Copy-Item</span>
rm file.txt                 <span class="com"># alias for Remove-Item</span>
mkdir NewFolder             <span class="com"># alias for New-Item -ItemType Directory</span>

<span class="com"># Object pipeline — output is objects, not text</span>
Get-Process                             <span class="com"># list all processes</span>
Get-Process | Where-Object {$_.CPU -gt 50}   <span class="com"># filter by CPU</span>
Get-Process | Sort-Object CPU -Descending | Select-Object -First 10
Get-Process | Select-Object Name, CPU, WorkingSet</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">COMMON TASKS</div>
      <div class="concept-title">PowerShell Cheat Sheet</div>
      <div class="code-block"><span class="com"># Services</span>
Get-Service                             <span class="com"># list all services</span>
Get-Service -Name "wuauserv"           <span class="com"># Windows Update service</span>
Start-Service -Name "wuauserv"
Stop-Service  -Name "wuauserv"
Restart-Service -Name "wuauserv"
Set-Service -Name "wuauserv" -StartupType Disabled

<span class="com"># Files and text</span>
Get-Content C:\log.txt                  <span class="com"># read file</span>
Get-Content C:\log.txt | Select-String "error"   <span class="com"># grep equivalent</span>
"Hello World" | Out-File C:\output.txt
Add-Content C:\log.txt "new line"       <span class="com"># append</span>

<span class="com"># Network</span>
Test-NetConnection google.com           <span class="com"># ping + port check</span>
Test-NetConnection google.com -Port 443 <span class="com"># test specific port</span>
Get-NetIPAddress                        <span class="com"># your IP addresses</span>
Resolve-DnsName google.com              <span class="com"># DNS lookup</span>
Get-NetTCPConnection                    <span class="com"># netstat equivalent</span>

<span class="com"># System info</span>
Get-ComputerInfo                        <span class="com"># detailed system info</span>
Get-EventLog -LogName Security -Newest 20   <span class="com"># security log</span>
Get-WmiObject -Class Win32_LogicalDisk  <span class="com"># disk info</span>

<span class="com"># Users</span>
Get-LocalUser                           <span class="com"># list local accounts</span>
New-LocalUser -Name "alice" -Password (ConvertTo-SecureString "P@ss!" -AsPlainText -Force)
Add-LocalGroupMember -Group "Administrators" -Member "alice"</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">SCRIPTING</div>
      <div class="concept-title">Writing PowerShell Scripts</div>
      <div class="code-block"><span class="com"># Variables start with $</span>
$name = "Alice"
$count = 42
$pi = 3.14159

<span class="com"># String interpolation</span>
Write-Host "Hello, $name!"              <span class="com"># Hello, Alice!</span>
Write-Host "Pi is approximately $pi"

<span class="com"># Arrays</span>
$fruits = @("apple", "banana", "cherry")
$fruits[0]                              <span class="com"># apple</span>
$fruits.Count                           <span class="com"># 3</span>
$fruits += "date"                       <span class="com"># add element</span>

<span class="com"># Hash tables (dicts)</span>
$user = @{ Name = "Alice"; Age = 30; Role = "Admin" }
$user["Name"]                           <span class="com"># Alice</span>
$user.Role                              <span class="com"># Admin</span>

<span class="com"># If / ForEach / While</span>
if ($count -gt 10) { Write-Host "Big" } elseif ($count -gt 5) { Write-Host "Medium" } else { Write-Host "Small" }

foreach ($fruit in $fruits) {
    Write-Host "I like $fruit"
}

1..10 | ForEach-Object { Write-Host "Item $_" }   <span class="com"># 1 to 10</span>

<span class="com"># Functions</span>
function Get-Greeting {
    param([string]$Name = "World")
    return "Hello, $Name!"
}
Get-Greeting -Name "Alice"</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">EXECUTION POLICY</div>
      <div class="concept-title">Why Your Script Won't Run</div>
      <div class="concept-desc">PowerShell's execution policy restricts which scripts can run. This is a security feature — not a permission system. On a new Windows machine, scripts are often blocked by default.</div>
      <div class="code-block"><span class="com"># Check current policy</span>
Get-ExecutionPolicy

<span class="com"># Policy levels (most to least restrictive)</span>
Restricted      <span class="com"># No scripts (default on Win clients)</span>
AllSigned       <span class="com"># Only code-signed scripts</span>
RemoteSigned    <span class="com"># Local scripts OK; downloaded must be signed</span>
Unrestricted    <span class="com"># All scripts run (prompt for remote)</span>
Bypass          <span class="com"># Nothing blocked (used in automation)</span>

<span class="com"># Set for current user (doesn't require admin)</span>
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

<span class="com"># Run a script bypassing policy (one-time)</span>
powershell.exe -ExecutionPolicy Bypass -File myscript.ps1</div>
    </div>
  </div>
</div>
"""

# ─────────────────────────────── AI wave 14 ──────────────────────────────────
AI_SENTINEL = "<!-- BEGINNER14-AI v1 -->"
AI_CONTENT = """
<!-- BEGINNER14-AI v1 -->
<!-- ── TOPIC: AI ETHICS AND RESPONSIBLE AI ────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">⚖️</span>
    <span class="topic-name">AI Ethics — The Human Side of Machine Intelligence</span>
    <span class="topic-badge">AI • Critical Thinking</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">WHY ETHICS MATTERS IN AI</div>
      <div class="concept-title">AI Amplifies Existing Problems at Scale</div>
      <div class="concept-desc">A human making biased decisions affects dozens of people. An AI system making biased decisions can affect millions instantly, consistently, and without fatigue. When you build, deploy, or use AI systems in IT, you're making ethical decisions — whether you realize it or not. Understanding these issues makes you a better engineer and a more responsible practitioner.</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">BIAS IN AI</div>
      <div class="concept-title">Garbage In, Garbage Out — At Scale</div>
      <div class="concept-desc">AI learns patterns from training data. If the data reflects historical biases (and it almost always does), the model learns those biases. The dangerous part: the output looks objective because it's a computer — but it's not.</div>
      <table class="ai-table">
        <thead><tr><th>Bias Type</th><th>How It Happens</th><th>Real-World Example</th></tr></thead>
        <tbody>
          <tr><td>Historical bias</td><td>Training data reflects past discrimination</td><td>Resume screening AI deprioritizes women's resumes because historical hires were mostly men</td></tr>
          <tr><td>Sampling bias</td><td>Training data doesn't represent all users</td><td>Facial recognition fails on darker skin tones — trained mostly on lighter skin</td></tr>
          <tr><td>Measurement bias</td><td>The metric being optimized is flawed</td><td>Recidivism prediction using zip code as a proxy (correlates with race)</td></tr>
          <tr><td>Feedback loop bias</td><td>Model decisions create future training data</td><td>Predictive policing sends more cops to neighborhood X → more arrests → model says X is more dangerous</td></tr>
          <tr><td>Confirmation bias</td><td>Model amplifies what it already "believes"</td><td>Recommendation algorithms push more extreme content to keep users engaged</td></tr>
        </tbody>
      </table>
    </div>
    <div class="concept-card">
      <div class="concept-label">RESPONSIBLE AI PRINCIPLES</div>
      <div class="concept-title">The Framework Most Organizations Aim For</div>
      <table class="ai-table">
        <thead><tr><th>Principle</th><th>What It Means</th><th>In Practice</th></tr></thead>
        <tbody>
          <tr><td><strong>Fairness</strong></td><td>Don't discriminate; treat similarly-situated people similarly</td><td>Audit model outputs across demographic groups</td></tr>
          <tr><td><strong>Transparency</strong></td><td>Be able to explain how decisions are made</td><td>Log what inputs influenced what outputs; prefer explainable models</td></tr>
          <tr><td><strong>Accountability</strong></td><td>Someone is responsible for the AI's decisions</td><td>Humans in the loop for high-stakes decisions (hiring, medical, criminal)</td></tr>
          <tr><td><strong>Privacy</strong></td><td>Respect data rights; use minimal data</td><td>Data minimization; consent; right to erasure</td></tr>
          <tr><td><strong>Safety</strong></td><td>Don't cause harm</td><td>Red-teaming; adversarial testing; kill switches</td></tr>
          <tr><td><strong>Reliability</strong></td><td>Behave consistently and predictably</td><td>Monitoring, testing across edge cases, drift detection</td></tr>
        </tbody>
      </table>
    </div>
    <div class="concept-card">
      <div class="concept-label">AI LIMITATIONS FOR IT PROS</div>
      <div class="concept-title">What LLMs Actually Can't Do</div>
      <div class="concept-desc">Large language models (like the ones in ChatGPT, Claude, Copilot) are incredibly useful — and have real limitations that affect how you should use them in professional contexts.</div>
      <table class="ai-table">
        <thead><tr><th>Limitation</th><th>Why It Happens</th><th>Implication</th></tr></thead>
        <tbody>
          <tr><td>Hallucinations</td><td>Generates plausible-sounding text, even when wrong</td><td>Always verify CVEs, commands, and API docs against primary sources</td></tr>
          <tr><td>Training cutoff</td><td>Knows nothing after its cutoff date</td><td>New vulnerabilities, updated APIs, recent events — check yourself</td></tr>
          <tr><td>No real-time data</td><td>Can't browse the internet (unless given a tool)</td><td>IP reputation, current threat intel — use specialized tools</td></tr>
          <tr><td>Context window</td><td>Can only "see" so much text at once</td><td>Loses context in very long conversations; may contradict itself</td></tr>
          <tr><td>No long-term memory</td><td>Each conversation starts fresh</td><td>Doesn't know what you told it last week</td></tr>
          <tr><td>Confident when wrong</td><td>Output style doesn't signal uncertainty</td><td>An authoritative-sounding wrong answer is still wrong</td></tr>
        </tbody>
      </table>
    </div>
  </div>
</div>

<!-- ── TOPIC: BUILDING WITH AI APIs ──────────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">🤖</span>
    <span class="topic-name">Building with AI APIs — From Prompt to Production</span>
    <span class="topic-badge">AI • Practical</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">LLM API CONCEPTS</div>
      <div class="concept-title">How AI APIs Work</div>
      <div class="concept-desc">Most LLM providers (OpenAI, Anthropic, Google, Mistral) expose REST APIs. You send messages, they return completions. The key parameters that control behavior:</div>
      <table class="ai-table">
        <thead><tr><th>Parameter</th><th>What It Controls</th><th>Typical Range</th></tr></thead>
        <tbody>
          <tr><td><code>model</code></td><td>Which model to use</td><td>"gpt-4o", "claude-opus-4-8", "gemini-pro"</td></tr>
          <tr><td><code>messages</code></td><td>Conversation history (system, user, assistant roles)</td><td>Array of message objects</td></tr>
          <tr><td><code>temperature</code></td><td>Randomness: 0 = deterministic, 1 = creative</td><td>0.0 – 1.0 (some allow 2.0)</td></tr>
          <tr><td><code>max_tokens</code></td><td>Maximum length of the response</td><td>Depends on model context window</td></tr>
          <tr><td><code>top_p</code></td><td>Nucleus sampling — controls diversity</td><td>0.0 – 1.0 (usually leave at 1)</td></tr>
          <tr><td><code>stream</code></td><td>Stream tokens as generated (vs. wait for full response)</td><td>true/false</td></tr>
        </tbody>
      </table>
    </div>
    <div class="concept-card">
      <div class="concept-label">PYTHON EXAMPLE</div>
      <div class="concept-title">Calling an LLM API with Python</div>
      <div class="code-block"><span class="com"># pip install anthropic</span>
<span class="kw">import</span> anthropic

client = anthropic.Anthropic()  <span class="com"># reads ANTHROPIC_API_KEY env var</span>

<span class="com"># Simple completion</span>
message = client.messages.create(
    model=<span class="str">"claude-opus-4-8"</span>,
    max_tokens=<span class="num">1024</span>,
    messages=[
        {<span class="str">"role"</span>: <span class="str">"user"</span>, <span class="str">"content"</span>: <span class="str">"Explain TCP three-way handshake in 3 bullet points"</span>}
    ]
)
<span class="fn">print</span>(message.content[<span class="num">0</span>].text)

<span class="com"># With system prompt</span>
message = client.messages.create(
    model=<span class="str">"claude-opus-4-8"</span>,
    max_tokens=<span class="num">1024</span>,
    system=<span class="str">"You are a cybersecurity expert. Respond concisely with practical advice."</span>,
    messages=[
        {<span class="str">"role"</span>: <span class="str">"user"</span>, <span class="str">"content"</span>: <span class="str">"What are the top 3 things a new analyst should monitor?"</span>}
    ]
)

<span class="com"># Streaming (output token by token)</span>
<span class="kw">with</span> client.messages.stream(
    model=<span class="str">"claude-opus-4-8"</span>,
    max_tokens=<span class="num">1024</span>,
    messages=[{<span class="str">"role"</span>: <span class="str">"user"</span>, <span class="str">"content"</span>: <span class="str">"Write a short Python function"</span>}]
) <span class="kw">as</span> stream:
    <span class="kw">for</span> text <span class="kw">in</span> stream.text_stream:
        <span class="fn">print</span>(text, end=<span class="str">""</span>, flush=<span class="kw">True</span>)</div>
    </div>
  </div>
</div>
"""

# ─────────────────────────────── MILITARY wave 14 ────────────────────────────
MIL_SENTINEL = "<!-- BEGINNER14-MIL v1 -->"
MIL_CONTENT = """
<!-- BEGINNER14-MIL v1 -->
<!-- ── TOPIC: OODA LOOP ───────────────────────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">🎯</span>
    <span class="topic-name">OODA Loop — Decision-Making Under Pressure</span>
    <span class="topic-badge">MILITARY • Decision Frameworks</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">WHAT IS THE OODA LOOP</div>
      <div class="concept-title">The Framework Behind Fast, Good Decisions</div>
      <div class="concept-desc">Developed by Air Force Colonel John Boyd after studying why American pilots won more dogfights despite flying inferior aircraft in Korea. The answer: they could cycle through decisions faster. Boyd codified this as the OODA Loop — Observe, Orient, Decide, Act. The fighter who gets inside the opponent's OODA loop wins. Directly applicable to incident response, red teaming, and any competitive situation.</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">THE FOUR PHASES</div>
      <div class="concept-title">OODA — Breaking Down Each Stage</div>
      <table class="ai-table">
        <thead><tr><th>Phase</th><th>What Happens</th><th>Cybersecurity Application</th></tr></thead>
        <tbody>
          <tr><td><strong>Observe</strong></td><td>Gather information from the environment. Sensory data, signals, telemetry — raw uninterpreted facts.</td><td>SIEM alerts, network telemetry, threat intel feeds, user reports</td></tr>
          <tr><td><strong>Orient</strong></td><td>Make sense of what you observed. Filter through mental models, prior experience, cultural tradition, analysis. This is the most important phase — your worldview shapes everything.</td><td>Apply threat knowledge (ATT&amp;CK TTPs), understand adversary motivation, contextualize the alert</td></tr>
          <tr><td><strong>Decide</strong></td><td>Choose a course of action from available options based on your orientation.</td><td>Contain vs. monitor, escalate vs. handle, which remediation path</td></tr>
          <tr><td><strong>Act</strong></td><td>Execute the decision. Then immediately begin observing again — it's a loop.</td><td>Block IP, isolate host, patch, notify stakeholders</td></tr>
        </tbody>
      </table>
    </div>
    <div class="concept-card">
      <div class="concept-label">IT APPLICATION</div>
      <div class="concept-title">Incident Response Through the OODA Lens</div>
      <div class="concept-desc">The fastest incident responders have fast OODA loops — not because they skip steps, but because their Orient phase is automatic from experience and training. This is why tabletop exercises, purple team exercises, and studying past incidents matter: they pre-load the Orient phase.</div>
      <table class="ai-table">
        <thead><tr><th>Goal</th><th>How to Achieve It</th></tr></thead>
        <tbody>
          <tr><td>Speed up Observe</td><td>Better tooling: more log sources, better SIEM, endpoint visibility (EDR)</td></tr>
          <tr><td>Speed up Orient</td><td>Training, experience, runbooks, tabletop exercises, threat intel</td></tr>
          <tr><td>Speed up Decide</td><td>Pre-approved playbooks, clear authority (who can approve isolation?), escalation paths</td></tr>
          <tr><td>Speed up Act</td><td>Automation (SOAR), prepared scripts, pre-staged remediation tools</td></tr>
          <tr><td>Disrupt attacker's loop</td><td>Deception (honeypots), rapid changes (rotate credentials), unpredictable responses</td></tr>
        </tbody>
      </table>
    </div>
  </div>
</div>

<!-- ── TOPIC: COMMANDER'S INTENT ─────────────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">📋</span>
    <span class="topic-name">Commander's Intent — Empowering Action Without Micromanaging</span>
    <span class="topic-badge">MILITARY • Leadership</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">THE CONCEPT</div>
      <div class="concept-title">Two Levels Up, Two Levels Down</div>
      <div class="concept-desc">In military doctrine, every order includes Commander's Intent — a clear statement of the end state (what does success look like?) and purpose (why are we doing this?). When the plan breaks down (and it always does — "no plan survives first contact with the enemy"), subordinates can make independent decisions that align with the intent rather than freezing to wait for orders.</div>
      <div class="concept-desc">The rule: know your commander's intent two levels up (why your boss's boss wants this), and ensure your subordinates know yours two levels down. This creates adaptive, decentralized execution.</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">IT APPLICATION</div>
      <div class="concept-title">How Commander's Intent Applies to Tech Teams</div>
      <table class="ai-table">
        <thead><tr><th>Military Concept</th><th>IT/Tech Equivalent</th></tr></thead>
        <tbody>
          <tr><td>Commander's Intent</td><td>Business goal behind a project — "why are we building this?" Engineers who know the why make better tradeoff decisions when specs change</td></tr>
          <tr><td>Plan breaks down</td><td>Requirements change mid-sprint, production incident during deploy, API partner goes down</td></tr>
          <tr><td>Decentralized execution</td><td>On-call engineers making incident decisions without waiting for management approval</td></tr>
          <tr><td>Two levels up</td><td>Developers understanding the business context; analysts understanding org risk tolerance</td></tr>
          <tr><td>Two levels down</td><td>Team leads ensuring ICs understand the outcome, not just the task</td></tr>
        </tbody>
      </table>
    </div>
    <div class="concept-card">
      <div class="concept-label">MISSION-TYPE ORDERS</div>
      <div class="concept-title">Tell Them What and Why — Not Always How</div>
      <div class="concept-desc">The German military concept of <em>Auftragstaktik</em> (mission tactics): give subordinates the objective and constraints, then trust them to figure out the method. This produces faster, more adaptive results than prescriptive orders — because the person closest to the problem has the most relevant information.</div>
      <div class="concept-desc">Applied to IT: instead of "run these exact five commands in this order," a good manager says "we need the backup restored and the service healthy before 8am Monday — you have authority to make it happen." The engineer has context the manager doesn't.</div>
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
        (PENTEST_INJECT_ANCHOR,  PENTEST_SENTINEL,  PENTEST_CONTENT),
        (THREAT_INJECT_ANCHOR,   THREAT_SENTINEL,   THREAT_CONTENT),
        (SHORTCUT_INJECT_ANCHOR, SHORTCUT_SENTINEL, SHORTCUT_CONTENT),
        (AI_INJECT_ANCHOR,       AI_SENTINEL,       AI_CONTENT),
        (MIL_INJECT_ANCHOR,      MIL_SENTINEL,      MIL_CONTENT),
    ]

    total_added = 0
    for anchor, sentinel, content in injections:
        new_html, changed = inject(html, anchor, sentinel, content)
        if changed:
            added = len(new_html) - len(html)
            total_added += added
            html = new_html
            label = anchor.replace("<!-- /domain-body ", "").replace(" -->", "")
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
