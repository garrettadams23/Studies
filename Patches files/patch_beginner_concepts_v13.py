#!/usr/bin/env python3
"""
patch_beginner_concepts_v13.py — Wave 13: Exception handling, IPv6,
package management, business continuity, interview prep.

New sentinels:
  BEGINNER13-SCRIPT v1  — Exception handling, custom exceptions, context cleanup
  BEGINNER13-NET v1     — IPv6 fundamentals, dual-stack, migration
  BEGINNER13-LINUX v1   — Package management (apt/dnf/snap), compiling from source
  BEGINNER13-GRC v1     — Business continuity, data classification, privacy regs
  BEGINNER13-LIFE v1    — Interview prep, STAR method, salary negotiation
"""
from pathlib import Path

SCRIPT_INJECT_ANCHOR = "<!-- /domain-body script -->"
NET_INJECT_ANCHOR    = "<!-- /domain-body net -->"
LINUX_INJECT_ANCHOR  = "<!-- /domain-body linux -->"
GRC_INJECT_ANCHOR    = "<!-- /domain-body grc -->"
LIFE_INJECT_ANCHOR   = "<!-- /domain-body lifestyle -->"

# ─────────────────────────────── SCRIPTING wave 13 ───────────────────────────
SCRIPT_SENTINEL = "<!-- BEGINNER13-SCRIPT v1 -->"
SCRIPT_CONTENT = """
<!-- BEGINNER13-SCRIPT v1 -->
<!-- ── TOPIC: EXCEPTION HANDLING ─────────────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">🛡️</span>
    <span class="topic-name">Exception Handling — Writing Code That Doesn't Crash</span>
    <span class="topic-badge">SCRIPT • Essential</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">WHY EXCEPTIONS MATTER</div>
      <div class="concept-title">The Real World Is Messy</div>
      <div class="concept-desc">Programs fail. Files don't exist. Networks time out. Users enter garbage. Exceptions are Python's way of signaling that something went wrong at runtime. Good code anticipates failures and handles them gracefully — instead of crashing with a wall of red text.</div>
      <div class="code-block"><span class="com"># Without exception handling — crashes if file missing</span>
<span class="kw">with</span> <span class="fn">open</span>(<span class="str">"config.txt"</span>) <span class="kw">as</span> f:
    data = f.read()   <span class="com"># FileNotFoundError kills the program</span>

<span class="com"># With exception handling — graceful fallback</span>
<span class="kw">try</span>:
    <span class="kw">with</span> <span class="fn">open</span>(<span class="str">"config.txt"</span>) <span class="kw">as</span> f:
        data = f.read()
<span class="kw">except</span> FileNotFoundError:
    <span class="fn">print</span>(<span class="str">"Config not found, using defaults"</span>)
    data = <span class="str">""</span></div>
    </div>
    <div class="concept-card">
      <div class="concept-label">TRY/EXCEPT ANATOMY</div>
      <div class="concept-title">The Full try Block Structure</div>
      <div class="code-block"><span class="kw">try</span>:
    result = risky_operation()         <span class="com"># code that might fail</span>
<span class="kw">except</span> ValueError <span class="kw">as</span> e:
    <span class="fn">print</span>(<span class="str">f"Bad value: </span>{e}<span class="str">"</span>)              <span class="com"># handle specific exception</span>
<span class="kw">except</span> (TypeError, KeyError) <span class="kw">as</span> e:
    <span class="fn">print</span>(<span class="str">f"Type or key problem: </span>{e}<span class="str">"</span>)   <span class="com"># handle multiple types</span>
<span class="kw">except</span> Exception <span class="kw">as</span> e:
    <span class="fn">print</span>(<span class="str">f"Unexpected error: </span>{e}<span class="str">"</span>)       <span class="com"># catch-all (use sparingly)</span>
    <span class="kw">raise</span>                               <span class="com"># re-raise to preserve traceback</span>
<span class="kw">else</span>:
    <span class="fn">print</span>(<span class="str">"Success!"</span>)                    <span class="com"># runs only if NO exception</span>
<span class="kw">finally</span>:
    cleanup()                           <span class="com"># ALWAYS runs — perfect for cleanup</span></div>
    </div>
    <div class="concept-card">
      <div class="concept-label">EXCEPTION HIERARCHY</div>
      <div class="concept-title">Python's Exception Family Tree</div>
      <table class="ai-table">
        <thead><tr><th>Exception</th><th>When It Occurs</th><th>Common Cause</th></tr></thead>
        <tbody>
          <tr><td><code>ValueError</code></td><td>Wrong type of value</td><td><code>int("abc")</code>, bad format</td></tr>
          <tr><td><code>TypeError</code></td><td>Wrong type entirely</td><td><code>"a" + 1</code>, wrong arg count</td></tr>
          <tr><td><code>KeyError</code></td><td>Dict key missing</td><td><code>d["missing"]</code></td></tr>
          <tr><td><code>IndexError</code></td><td>List index out of range</td><td><code>lst[99]</code> on small list</td></tr>
          <tr><td><code>AttributeError</code></td><td>Object has no attribute</td><td><code>None.strip()</code></td></tr>
          <tr><td><code>FileNotFoundError</code></td><td>File/dir doesn't exist</td><td><code>open("ghost.txt")</code></td></tr>
          <tr><td><code>PermissionError</code></td><td>OS blocks access</td><td>Reading root-owned file</td></tr>
          <tr><td><code>TimeoutError</code></td><td>Operation took too long</td><td>Network requests, DB queries</td></tr>
          <tr><td><code>ConnectionError</code></td><td>Network problem</td><td>Server down, no internet</td></tr>
          <tr><td><code>ZeroDivisionError</code></td><td>Divide by zero</td><td><code>x / 0</code></td></tr>
          <tr><td><code>ImportError</code></td><td>Module not found</td><td>Package not installed</td></tr>
          <tr><td><code>StopIteration</code></td><td>Iterator exhausted</td><td><code>next()</code> on empty iterator</td></tr>
        </tbody>
      </table>
    </div>
    <div class="concept-card">
      <div class="concept-label">CUSTOM EXCEPTIONS</div>
      <div class="concept-title">Create Your Own Exception Types</div>
      <div class="concept-desc">Custom exceptions make your code's error vocabulary explicit. When a caller sees <code>InsufficientFundsError</code>, they know exactly what went wrong — no guessing from a generic <code>ValueError</code>.</div>
      <div class="code-block"><span class="com"># Define custom exceptions by inheriting from Exception</span>
<span class="kw">class</span> <span class="fn">AppError</span>(Exception):
    <span class="str">&quot;&quot;&quot;Base class for all app-specific errors.&quot;&quot;&quot;</span>

<span class="kw">class</span> <span class="fn">InsufficientFundsError</span>(AppError):
    <span class="kw">def</span> <span class="fn">__init__</span>(self, needed, available):
        self.needed = needed
        self.available = available
        <span class="fn">super().__init__</span>(
            <span class="str">f"Need ${needed:.2f} but only ${available:.2f} available"</span>
        )

<span class="kw">class</span> <span class="fn">UserNotFoundError</span>(AppError):
    <span class="kw">pass</span>   <span class="com"># simple — message comes from caller</span>

<span class="com"># Usage</span>
<span class="kw">def</span> <span class="fn">withdraw</span>(account, amount):
    <span class="kw">if</span> account.balance &lt; amount:
        <span class="kw">raise</span> <span class="fn">InsufficientFundsError</span>(amount, account.balance)
    account.balance -= amount

<span class="kw">try</span>:
    <span class="fn">withdraw</span>(my_account, <span class="num">500</span>)
<span class="kw">except</span> InsufficientFundsError <span class="kw">as</span> e:
    <span class="fn">print</span>(e)              <span class="com"># "Need $500.00 but only $23.50 available"</span>
    <span class="fn">print</span>(e.needed)       <span class="com"># 500</span></div>
    </div>
    <div class="concept-card">
      <div class="concept-label">BEST PRACTICES</div>
      <div class="concept-title">Exception Handling Rules of Thumb</div>
      <table class="ai-table">
        <thead><tr><th>Rule</th><th>Good</th><th>Bad</th></tr></thead>
        <tbody>
          <tr><td>Be specific</td><td><code>except FileNotFoundError</code></td><td><code>except Exception</code> (hides bugs)</td></tr>
          <tr><td>Don't swallow silently</td><td>Log or re-raise</td><td><code>except: pass</code> (nightmare to debug)</td></tr>
          <tr><td>Use finally for cleanup</td><td><code>finally: conn.close()</code></td><td>Cleanup only in try block (may not run)</td></tr>
          <tr><td>Fail fast</td><td>Validate inputs early</td><td>Catch errors deep in call stack</td></tr>
          <tr><td>Error messages</td><td>Include context and values</td><td>Just "error occurred"</td></tr>
          <tr><td>EAFP vs LBYL</td><td>Python prefers EAFP (try it)</td><td>Checking every condition first</td></tr>
        </tbody>
      </table>
      <div class="code-block"><span class="com"># LBYL (Look Before You Leap) — C/Java style</span>
<span class="kw">if</span> <span class="str">"key"</span> <span class="kw">in</span> my_dict:
    value = my_dict[<span class="str">"key"</span>]

<span class="com"># EAFP (Easier to Ask Forgiveness than Permission) — Pythonic</span>
<span class="kw">try</span>:
    value = my_dict[<span class="str">"key"</span>]
<span class="kw">except</span> KeyError:
    value = default

<span class="com"># Even better — use .get()</span>
value = my_dict.get(<span class="str">"key"</span>, default)</div>
    </div>
  </div>
</div>

<!-- ── TOPIC: WORKING WITH FILES ─────────────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">📂</span>
    <span class="topic-name">Working with Files — Reading, Writing, and Paths</span>
    <span class="topic-badge">SCRIPT • Essential</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">PATHLIB</div>
      <div class="concept-title">The Modern Way to Handle File Paths</div>
      <div class="concept-desc"><code>pathlib.Path</code> is the Python 3 way to work with files and directories. It's object-oriented, cross-platform (handles Windows/Linux path separators), and far cleaner than string concatenation or the old <code>os.path</code> module.</div>
      <div class="code-block"><span class="kw">from</span> pathlib <span class="kw">import</span> Path

p = Path(<span class="str">"/home/alice/documents/report.txt"</span>)

<span class="com"># Path components</span>
p.name        <span class="com"># "report.txt"</span>
p.stem        <span class="com"># "report"</span>
p.suffix      <span class="com"># ".txt"</span>
p.parent      <span class="com"># Path("/home/alice/documents")</span>

<span class="com"># Navigation with / operator</span>
home = Path.home()               <span class="com"># /home/alice</span>
config = home / <span class="str">".config"</span> / <span class="str">"app.json"</span>

<span class="com"># Check existence</span>
p.exists()          <span class="com"># True/False</span>
p.is_file()         <span class="com"># True if regular file</span>
p.is_dir()          <span class="com"># True if directory</span>

<span class="com"># Read/write shortcuts</span>
text = p.read_text(encoding=<span class="str">"utf-8"</span>)
p.write_text(<span class="str">"hello"</span>, encoding=<span class="str">"utf-8"</span>)
data = p.read_bytes()

<span class="com"># List directory contents</span>
<span class="kw">for</span> f <span class="kw">in</span> Path(<span class="str">"."</span>).iterdir():
    <span class="fn">print</span>(f)

<span class="com"># Find all Python files recursively</span>
<span class="kw">for</span> f <span class="kw">in</span> Path(<span class="str">"."</span>).rglob(<span class="str">"*.py"</span>):
    <span class="fn">print</span>(f)

<span class="com"># Create directories</span>
Path(<span class="str">"output/reports"</span>).mkdir(parents=<span class="kw">True</span>, exist_ok=<span class="kw">True</span>)</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">FILE MODES</div>
      <div class="concept-title">open() Mode Reference</div>
      <table class="ai-table">
        <thead><tr><th>Mode</th><th>Meaning</th><th>Creates?</th><th>Truncates?</th></tr></thead>
        <tbody>
          <tr><td><code>'r'</code></td><td>Read (default)</td><td>No — error if missing</td><td>No</td></tr>
          <tr><td><code>'w'</code></td><td>Write</td><td>Yes</td><td>Yes — overwrites!</td></tr>
          <tr><td><code>'a'</code></td><td>Append</td><td>Yes</td><td>No — adds to end</td></tr>
          <tr><td><code>'x'</code></td><td>Exclusive create</td><td>Yes — error if exists</td><td>N/A</td></tr>
          <tr><td><code>'r+'</code></td><td>Read + write</td><td>No</td><td>No</td></tr>
          <tr><td><code>'b'</code></td><td>Binary mode (combine: 'rb', 'wb')</td><td>—</td><td>—</td></tr>
          <tr><td><code>'t'</code></td><td>Text mode (default)</td><td>—</td><td>—</td></tr>
        </tbody>
      </table>
    </div>
    <div class="concept-card">
      <div class="concept-label">CSV AND JSON FILES</div>
      <div class="concept-title">Working with Structured Data Files</div>
      <div class="code-block"><span class="kw">import</span> csv, json

<span class="com"># ── CSV ──────────────────────────────────────────────────</span>
<span class="com"># Read CSV into list of dicts</span>
<span class="kw">with</span> <span class="fn">open</span>(<span class="str">"users.csv"</span>, newline=<span class="str">""</span>) <span class="kw">as</span> f:
    reader = csv.DictReader(f)
    users = <span class="fn">list</span>(reader)    <span class="com"># [{"name": "Alice", "age": "30"}, ...]</span>

<span class="com"># Write CSV from list of dicts</span>
<span class="kw">with</span> <span class="fn">open</span>(<span class="str">"output.csv"</span>, <span class="str">"w"</span>, newline=<span class="str">""</span>) <span class="kw">as</span> f:
    writer = csv.DictWriter(f, fieldnames=[<span class="str">"name"</span>, <span class="str">"age"</span>])
    writer.writeheader()
    writer.writerows(users)

<span class="com"># ── JSON ──────────────────────────────────────────────────</span>
<span class="com"># Read JSON file</span>
<span class="kw">with</span> <span class="fn">open</span>(<span class="str">"config.json"</span>) <span class="kw">as</span> f:
    config = json.load(f)        <span class="com"># parse file → Python dict</span>

<span class="com"># Write JSON file (pretty-printed)</span>
<span class="kw">with</span> <span class="fn">open</span>(<span class="str">"output.json"</span>, <span class="str">"w"</span>) <span class="kw">as</span> f:
    json.dump(config, f, indent=<span class="num">2</span>)

<span class="com"># JSON string ↔ Python object</span>
data = json.loads(<span class="str">'{"key": "value"}'</span>)  <span class="com"># string → dict</span>
text = json.dumps(data, indent=<span class="num">2</span>)       <span class="com"># dict → string</span></div>
    </div>
  </div>
</div>
"""

# ─────────────────────────────── NET wave 13 ─────────────────────────────────
NET_SENTINEL = "<!-- BEGINNER13-NET v1 -->"
NET_CONTENT = """
<!-- BEGINNER13-NET v1 -->
<!-- ── TOPIC: IPv6 FUNDAMENTALS ─────────────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">🌐</span>
    <span class="topic-name">IPv6 — The Internet's Upgrade</span>
    <span class="topic-badge">NET • Essential</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">WHY IPv6</div>
      <div class="concept-title">IPv4 Ran Out of Addresses</div>
      <div class="concept-desc">IPv4 has 4.3 billion addresses. That sounds like a lot — until you realize there are 8 billion people, each with multiple devices, plus billions of IoT gadgets. IPv4 officially ran out in 2011. IPv6 solves this with 340 undecillion addresses (3.4 × 10³⁸) — roughly one address per atom on Earth's surface. You'll encounter IPv6 constantly in modern networks.</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">ADDRESS FORMAT</div>
      <div class="concept-title">Reading and Writing IPv6 Addresses</div>
      <div class="concept-desc">IPv6 addresses are 128 bits written as 8 groups of 4 hex digits separated by colons. Two simplification rules reduce the ugliness.</div>
      <div class="code-block"><span class="com"># Full form — 8 groups of 4 hex digits</span>
2001:0db8:0000:0000:0000:ff00:0042:8329

<span class="com"># Rule 1: Drop leading zeros in each group</span>
2001:db8:0:0:0:ff00:42:8329

<span class="com"># Rule 2: Replace ONE run of consecutive all-zero groups with ::</span>
2001:db8::ff00:42:8329   <span class="com"># :: replaces :0:0:0:</span>

<span class="com"># Loopback (equivalent to 127.0.0.1)</span>
::1

<span class="com"># Unspecified address (equivalent to 0.0.0.0)</span>
::

<span class="com"># IPv6 in URLs — brackets required to avoid port confusion</span>
http://[2001:db8::1]:8080/path</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">ADDRESS TYPES</div>
      <div class="concept-title">IPv6 Address Categories</div>
      <table class="ai-table">
        <thead><tr><th>Type</th><th>Prefix</th><th>Scope</th><th>IPv4 Equivalent</th></tr></thead>
        <tbody>
          <tr><td>Global Unicast</td><td><code>2000::/3</code></td><td>Public internet-routable</td><td>Public IP</td></tr>
          <tr><td>Link-Local</td><td><code>fe80::/10</code></td><td>This link only (not routed)</td><td>169.254.x.x (APIPA)</td></tr>
          <tr><td>Unique Local</td><td><code>fc00::/7</code></td><td>Private org network</td><td>RFC 1918 (10.x, 172.16.x, 192.168.x)</td></tr>
          <tr><td>Loopback</td><td><code>::1/128</code></td><td>This device only</td><td>127.0.0.1</td></tr>
          <tr><td>Multicast</td><td><code>ff00::/8</code></td><td>Group of devices</td><td>224.0.0.0/4</td></tr>
          <tr><td>Anycast</td><td>From unicast range</td><td>Nearest of a group</td><td>No direct equivalent</td></tr>
        </tbody>
      </table>
    </div>
    <div class="concept-card">
      <div class="concept-label">KEY DIFFERENCES</div>
      <div class="concept-title">IPv6 vs IPv4 — What Changed</div>
      <table class="ai-table">
        <thead><tr><th>Feature</th><th>IPv4</th><th>IPv6</th></tr></thead>
        <tbody>
          <tr><td>Address size</td><td>32 bits (~4.3B addresses)</td><td>128 bits (340 undecillion)</td></tr>
          <tr><td>NAT required?</td><td>Yes (address exhaustion)</td><td>No (enough for all devices)</td></tr>
          <tr><td>Header size</td><td>Variable (20-60 bytes)</td><td>Fixed (40 bytes) — faster routing</td></tr>
          <tr><td>Broadcast</td><td>Yes (network noise)</td><td>No — replaced by multicast</td></tr>
          <tr><td>Auto-configuration</td><td>Needs DHCP</td><td>SLAAC (stateless, no server needed)</td></tr>
          <tr><td>IPsec</td><td>Optional</td><td>Built into spec</td></tr>
          <tr><td>Fragmentation</td><td>Routers can fragment</td><td>End hosts only (routers don't)</td></tr>
        </tbody>
      </table>
    </div>
    <div class="concept-card">
      <div class="concept-label">DUAL-STACK & TRANSITION</div>
      <div class="concept-title">Running IPv4 and IPv6 Together</div>
      <div class="concept-desc">Most networks today run <strong>dual-stack</strong> — both IPv4 and IPv6 simultaneously. When a client connects, it prefers IPv6 (via "Happy Eyeballs" algorithm). This lets networks migrate gradually without a hard cutover.</div>
      <div class="code-block"><span class="com"># Check your IPv6 addresses (Linux)</span>
ip -6 addr show

<span class="com"># Ping using IPv6</span>
ping6 ::1                          <span class="com"># loopback</span>
ping6 -I eth0 fe80::1%eth0         <span class="com"># link-local requires interface</span>

<span class="com"># Traceroute IPv6</span>
traceroute6 2001:4860:4860::8888   <span class="com"># Google's IPv6 DNS</span>

<span class="com"># Check if site has IPv6 (AAAA record)</span>
dig AAAA google.com
nslookup -type=AAAA google.com

<span class="com"># Curl over IPv6</span>
curl -6 https://ipv6.google.com</div>
    </div>
  </div>
</div>

<!-- ── TOPIC: NETWORK PROTOCOLS DEEP DIVE ─────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">🔌</span>
    <span class="topic-name">Common Protocols — What's Actually Happening on the Wire</span>
    <span class="topic-badge">NET • Reference</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">APPLICATION LAYER PROTOCOLS</div>
      <div class="concept-title">Protocols You'll Use Every Day</div>
      <table class="ai-table">
        <thead><tr><th>Protocol</th><th>Port</th><th>Purpose</th><th>Secure Version</th></tr></thead>
        <tbody>
          <tr><td>HTTP</td><td>80/tcp</td><td>Web traffic</td><td>HTTPS (443)</td></tr>
          <tr><td>HTTPS</td><td>443/tcp</td><td>Encrypted web</td><td>Already secure</td></tr>
          <tr><td>DNS</td><td>53/udp+tcp</td><td>Name resolution</td><td>DoH (443), DoT (853)</td></tr>
          <tr><td>SSH</td><td>22/tcp</td><td>Encrypted remote shell</td><td>Already secure</td></tr>
          <tr><td>FTP</td><td>21/tcp</td><td>File transfer (insecure)</td><td>SFTP (22), FTPS (990)</td></tr>
          <tr><td>SMTP</td><td>25/tcp</td><td>Send email (server-to-server)</td><td>SMTPS (465/587)</td></tr>
          <tr><td>IMAP</td><td>143/tcp</td><td>Read email (syncs)</td><td>IMAPS (993)</td></tr>
          <tr><td>POP3</td><td>110/tcp</td><td>Read email (downloads)</td><td>POP3S (995)</td></tr>
          <tr><td>SNMP</td><td>161/udp</td><td>Network device management</td><td>SNMPv3</td></tr>
          <tr><td>NTP</td><td>123/udp</td><td>Time synchronization</td><td>NTPsec</td></tr>
          <tr><td>RDP</td><td>3389/tcp</td><td>Windows remote desktop</td><td>TLS-wrapped RDP</td></tr>
          <tr><td>LDAP</td><td>389/tcp</td><td>Directory services (AD)</td><td>LDAPS (636)</td></tr>
        </tbody>
      </table>
    </div>
    <div class="concept-card">
      <div class="concept-label">TCP VS UDP</div>
      <div class="concept-title">Choosing the Right Transport Protocol</div>
      <table class="ai-table">
        <thead><tr><th>Feature</th><th>TCP</th><th>UDP</th></tr></thead>
        <tbody>
          <tr><td>Connection</td><td>Connection-oriented (3-way handshake)</td><td>Connectionless — fire and forget</td></tr>
          <tr><td>Reliability</td><td>Guaranteed delivery, retransmits lost packets</td><td>No guarantee — packets can be lost</td></tr>
          <tr><td>Ordering</td><td>Delivers in order</td><td>Out-of-order possible</td></tr>
          <tr><td>Speed</td><td>Slower (overhead)</td><td>Faster (minimal overhead)</td></tr>
          <tr><td>Use case</td><td>HTTP, SSH, email, file transfer</td><td>DNS, video streaming, VoIP, gaming</td></tr>
          <tr><td>Header size</td><td>20+ bytes</td><td>8 bytes</td></tr>
        </tbody>
      </table>
    </div>
  </div>
</div>
"""

# ─────────────────────────────── LINUX wave 13 ───────────────────────────────
LINUX_SENTINEL = "<!-- BEGINNER13-LINUX v1 -->"
LINUX_CONTENT = """
<!-- BEGINNER13-LINUX v1 -->
<!-- ── TOPIC: PACKAGE MANAGEMENT ─────────────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">📦</span>
    <span class="topic-name">Package Management — Installing and Managing Software</span>
    <span class="topic-badge">LINUX • Essential</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">THE BIG PICTURE</div>
      <div class="concept-title">How Linux Software Installation Works</div>
      <div class="concept-desc">Unlike Windows (download .exe, double-click) or Mac (drag to Applications), Linux uses <strong>package managers</strong> — tools that download software from trusted repositories, handle dependencies automatically, and keep everything updated consistently. Different Linux distributions use different package managers.</div>
      <table class="ai-table">
        <thead><tr><th>Distro Family</th><th>Examples</th><th>Package Manager</th><th>File Format</th></tr></thead>
        <tbody>
          <tr><td>Debian</td><td>Ubuntu, Mint, Kali, Raspberry Pi OS</td><td><code>apt</code></td><td><code>.deb</code></td></tr>
          <tr><td>Red Hat</td><td>RHEL, CentOS, Fedora, Rocky, AlmaLinux</td><td><code>dnf</code> (old: <code>yum</code>)</td><td><code>.rpm</code></td></tr>
          <tr><td>Arch</td><td>Arch Linux, Manjaro, EndeavourOS</td><td><code>pacman</code></td><td><code>.pkg.tar.zst</code></td></tr>
          <tr><td>openSUSE</td><td>openSUSE Leap/Tumbleweed</td><td><code>zypper</code></td><td><code>.rpm</code></td></tr>
          <tr><td>Universal</td><td>Any distro</td><td><code>snap</code>, <code>flatpak</code>, <code>AppImage</code></td><td>Various</td></tr>
        </tbody>
      </table>
    </div>
    <div class="concept-card">
      <div class="concept-label">APT COMMANDS</div>
      <div class="concept-title">Debian/Ubuntu Package Manager</div>
      <div class="concept-desc"><code>apt</code> (Advanced Package Tool) manages software on Debian-based systems. Always run <code>apt update</code> first to refresh the list of available packages before installing.</div>
      <div class="code-block"><span class="com"># Update package index (does NOT upgrade software)</span>
sudo apt update

<span class="com"># Upgrade all installed packages</span>
sudo apt upgrade -y

<span class="com"># Install a package</span>
sudo apt install nginx
sudo apt install -y git curl wget tree   <span class="com"># -y skips confirmation</span>

<span class="com"># Remove a package (keep config files)</span>
sudo apt remove nginx

<span class="com"># Remove package AND its config files</span>
sudo apt purge nginx

<span class="com"># Remove unused dependencies</span>
sudo apt autoremove

<span class="com"># Search for a package</span>
apt search nmap
apt-cache search "web server"

<span class="com"># Show package info</span>
apt show nginx

<span class="com"># List installed packages</span>
apt list --installed
dpkg -l | grep nginx    <span class="com"># check if specific package installed</span>

<span class="com"># Full system update (one-liner)</span>
sudo apt update &amp;&amp; sudo apt upgrade -y &amp;&amp; sudo apt autoremove -y</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">DNF / YUM COMMANDS</div>
      <div class="concept-title">Red Hat Family Package Manager</div>
      <div class="code-block"><span class="com"># dnf is the modern replacement for yum (same concepts)</span>
sudo dnf update                 <span class="com"># update package index AND upgrade</span>
sudo dnf install httpd          <span class="com"># install (httpd = nginx equivalent)</span>
sudo dnf remove httpd           <span class="com"># uninstall</span>
sudo dnf search nginx
sudo dnf info nginx
sudo dnf list installed

<span class="com"># Enable EPEL (Extra Packages for Enterprise Linux)</span>
sudo dnf install epel-release   <span class="com"># unlocks many extra packages</span></div>
    </div>
    <div class="concept-card">
      <div class="concept-label">SNAP & FLATPAK</div>
      <div class="concept-title">Universal Package Formats</div>
      <div class="concept-desc">Snap and Flatpak are universal package formats that bundle all dependencies — they run the same on any Linux distro. Useful for software not in your distro's repos, or for getting the latest version of an app.</div>
      <div class="code-block"><span class="com"># SNAP (Canonical/Ubuntu's universal packages)</span>
sudo snap install code --classic   <span class="com"># VS Code</span>
snap list                          <span class="com"># list installed snaps</span>
snap find "media player"
sudo snap refresh code             <span class="com"># update specific snap</span>
sudo snap remove code

<span class="com"># FLATPAK (community alternative, works on all distros)</span>
flatpak install flathub com.spotify.Client
flatpak run com.spotify.Client
flatpak list
flatpak update

<span class="com"># APPIMAGE (no install needed — just download and run)</span>
chmod +x SomeApp.AppImage         <span class="com"># make executable</span>
./SomeApp.AppImage                <span class="com"># run directly, no installation</span></div>
    </div>
    <div class="concept-card">
      <div class="concept-label">COMPILING FROM SOURCE</div>
      <div class="concept-title">When Packages Don't Exist</div>
      <div class="concept-desc">Sometimes software isn't in any package manager. The classic way is to compile from source code. This requires build tools and is slower, but gives you the exact version you need.</div>
      <div class="code-block"><span class="com"># Install build essentials first</span>
sudo apt install build-essential   <span class="com"># Ubuntu/Debian</span>
sudo dnf groupinstall "Development Tools"  <span class="com"># Red Hat</span>

<span class="com"># Classic build pattern (configure / make / make install)</span>
wget https://example.com/app-1.0.tar.gz
tar -xzf app-1.0.tar.gz
cd app-1.0

./configure                        <span class="com"># checks dependencies, generates Makefile</span>
./configure --prefix=/usr/local    <span class="com"># custom install location</span>
make                               <span class="com"># compile (uses all CPU cores with -j4)</span>
make -j$(nproc)                    <span class="com"># parallel compile — much faster</span>
sudo make install                  <span class="com"># copy to system</span>

<span class="com"># Clean up</span>
make clean                         <span class="com"># remove compiled objects</span></div>
    </div>
  </div>
</div>

<!-- ── TOPIC: TEXT EDITORS IN THE TERMINAL ───────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">✏️</span>
    <span class="topic-name">Terminal Text Editors — Editing Files Without a GUI</span>
    <span class="topic-badge">LINUX • Essential</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">NANO</div>
      <div class="concept-title">The Beginner-Friendly Editor</div>
      <div class="concept-desc">Nano is simple and shows keyboard shortcuts at the bottom of the screen. No modes, no memorizing commands — just type. Perfect when you need to quickly edit a config file.</div>
      <div class="code-block"><span class="com"># Open a file</span>
nano /etc/hosts
nano filename.txt

<span class="com"># Essential shortcuts (^ = Ctrl, M = Alt)</span>
Ctrl+O    <span class="com"># Save (Write Out)</span>
Ctrl+X    <span class="com"># Exit (prompts to save if modified)</span>
Ctrl+W    <span class="com"># Search (Where Is)</span>
Ctrl+\\   <span class="com"># Find and replace</span>
Ctrl+K    <span class="com"># Cut line</span>
Ctrl+U    <span class="com"># Paste (Un-cut)</span>
Ctrl+G    <span class="com"># Help</span>
Alt+U     <span class="com"># Undo</span></div>
    </div>
    <div class="concept-card">
      <div class="concept-label">VIM SURVIVAL GUIDE</div>
      <div class="concept-title">Enough Vim to Get Out Alive</div>
      <div class="concept-desc">Vim is powerful but modal — different keys do different things depending on which mode you're in. Knowing the basics is essential because many servers only have vi/vim available, and some programs (like git commit without EDITOR set) drop you into vim unexpectedly.</div>
      <div class="code-block"><span class="com"># The famous "how to exit vim" — memorize these first</span>
:q        <span class="com"># quit (only if no changes)</span>
:q!       <span class="com"># FORCE quit, discard changes</span>
:wq       <span class="com"># save and quit</span>
:x        <span class="com"># save and quit (same as :wq)</span>
ZZ        <span class="com"># save and quit (in normal mode)</span>

<span class="com"># Modes</span>
i         <span class="com"># → INSERT mode (type text)</span>
Esc       <span class="com"># → NORMAL mode (navigate/commands)</span>
v         <span class="com"># → VISUAL mode (select text)</span>
:         <span class="com"># → COMMAND mode (run :wq, :set, etc.)</span>

<span class="com"># Navigation (normal mode)</span>
hjkl      <span class="com"># left/down/up/right (arrow keys also work)</span>
gg        <span class="com"># go to first line</span>
G         <span class="com"># go to last line</span>
:50       <span class="com"># go to line 50</span>

<span class="com"># Essential edits (normal mode)</span>
dd        <span class="com"># delete current line</span>
yy        <span class="com"># yank (copy) current line</span>
p         <span class="com"># paste after cursor</span>
u         <span class="com"># undo</span>
/pattern  <span class="com"># search forward</span>
n         <span class="com"># next search result</span></div>
    </div>
  </div>
</div>
"""

# ─────────────────────────────── GRC wave 13 ─────────────────────────────────
GRC_SENTINEL = "<!-- BEGINNER13-GRC v1 -->"
GRC_CONTENT = """
<!-- BEGINNER13-GRC v1 -->
<!-- ── TOPIC: BUSINESS CONTINUITY ───────────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">🔄</span>
    <span class="topic-name">Business Continuity &amp; Disaster Recovery — Keeping the Lights On</span>
    <span class="topic-badge">GRC • Essential</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">BC VS DR</div>
      <div class="concept-title">Business Continuity vs Disaster Recovery</div>
      <div class="concept-desc">These terms are related but distinct. People often use them interchangeably — they are not the same thing.</div>
      <table class="ai-table">
        <thead><tr><th>Concept</th><th>Focus</th><th>Scope</th><th>Question It Answers</th></tr></thead>
        <tbody>
          <tr><td><strong>Business Continuity (BC)</strong></td><td>Keeping operations running during a disruption</td><td>Entire organization (people, process, tech)</td><td>"How do we keep doing business?"</td></tr>
          <tr><td><strong>Disaster Recovery (DR)</strong></td><td>Restoring IT systems after a disaster</td><td>IT infrastructure, data, applications</td><td>"How do we restore our systems?"</td></tr>
          <tr><td><strong>BCP</strong></td><td>Business Continuity Plan — the document</td><td>Strategic plan covering all scenarios</td><td>"What's the written playbook?"</td></tr>
          <tr><td><strong>DRP</strong></td><td>Disaster Recovery Plan — the document</td><td>IT recovery procedures, step-by-step</td><td>"What's the IT recovery script?"</td></tr>
        </tbody>
      </table>
    </div>
    <div class="concept-card">
      <div class="concept-label">KEY METRICS</div>
      <div class="concept-title">RTO and RPO — The Two Numbers That Matter</div>
      <div class="concept-desc">Every system should have defined RTO and RPO. These drive architecture decisions: lower values require more expensive solutions (hot standby, synchronous replication). Setting them is a business decision, not a technical one — it depends on what downtime costs.</div>
      <table class="ai-table">
        <thead><tr><th>Metric</th><th>Full Name</th><th>Definition</th><th>Example</th></tr></thead>
        <tbody>
          <tr><td><strong>RTO</strong></td><td>Recovery Time Objective</td><td>Maximum acceptable downtime — how long before systems MUST be back up</td><td>"We can tolerate 4 hours of outage"</td></tr>
          <tr><td><strong>RPO</strong></td><td>Recovery Point Objective</td><td>Maximum acceptable data loss — how old can the restored data be?</td><td>"We can lose at most 1 hour of transactions"</td></tr>
          <tr><td><strong>MTTR</strong></td><td>Mean Time to Recover</td><td>Average time to restore service after failure</td><td>Historical metric from past incidents</td></tr>
          <tr><td><strong>MTBF</strong></td><td>Mean Time Between Failures</td><td>Average time between system failures</td><td>Measure of reliability</td></tr>
        </tbody>
      </table>
    </div>
    <div class="concept-card">
      <div class="concept-label">RECOVERY SITES</div>
      <div class="concept-title">Where Do You Go When Your Data Center Burns Down?</div>
      <table class="ai-table">
        <thead><tr><th>Site Type</th><th>Description</th><th>RTO</th><th>Cost</th></tr></thead>
        <tbody>
          <tr><td><strong>Hot Site</strong></td><td>Fully operational duplicate — runs in parallel. Failover in minutes.</td><td>Minutes</td><td>Very high (2× infrastructure)</td></tr>
          <tr><td><strong>Warm Site</strong></td><td>Systems and infra present, data partially synced. Needs some setup.</td><td>Hours</td><td>Moderate</td></tr>
          <tr><td><strong>Cold Site</strong></td><td>Just the building and power. You bring your equipment.</td><td>Days to weeks</td><td>Low</td></tr>
          <tr><td><strong>Cloud DR</strong></td><td>Replicate to cloud, spin up on demand. Modern favorite.</td><td>Minutes to hours</td><td>Pay-per-use (low idle cost)</td></tr>
        </tbody>
      </table>
    </div>
    <div class="concept-card">
      <div class="concept-label">TESTING</div>
      <div class="concept-title">Types of DR Tests — From Easy to Hard</div>
      <table class="ai-table">
        <thead><tr><th>Test Type</th><th>What Happens</th><th>Risk</th><th>Validates</th></tr></thead>
        <tbody>
          <tr><td>Tabletop Exercise</td><td>Team talks through scenario in a meeting</td><td>Zero</td><td>Plans and roles</td></tr>
          <tr><td>Walkthrough / Review</td><td>Review procedures, check documentation</td><td>Zero</td><td>Plan completeness</td></tr>
          <tr><td>Parallel Test</td><td>Activate DR site, run both — compare results</td><td>Low</td><td>Recovery capability</td></tr>
          <tr><td>Simulation</td><td>Simulate disaster, follow procedures in test env</td><td>Low</td><td>Procedures and timing</td></tr>
          <tr><td>Full Interruption</td><td>Actually cut over to DR — live traffic goes there</td><td>High</td><td>Everything, real-world</td></tr>
        </tbody>
      </table>
    </div>
  </div>
</div>

<!-- ── TOPIC: DATA CLASSIFICATION ────────────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">🏷️</span>
    <span class="topic-name">Data Classification — Knowing What Needs Protecting</span>
    <span class="topic-badge">GRC • Foundation</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">WHY CLASSIFY</div>
      <div class="concept-title">Not All Data Needs the Same Protection</div>
      <div class="concept-desc">Treating a public press release the same as a Social Security number is wasteful — and treating a Social Security number like a press release is negligent. Data classification is the foundation of a proportionate security program: protect data based on its value and sensitivity, not uniformly.</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">GOVERNMENT CLASSIFICATION</div>
      <div class="concept-title">Military/Government Levels</div>
      <table class="ai-table">
        <thead><tr><th>Level</th><th>Description</th><th>Unauthorized Disclosure Could...</th></tr></thead>
        <tbody>
          <tr><td>Top Secret (TS)</td><td>Most sensitive — small circle of need-to-know</td><td>Cause grave damage to national security</td></tr>
          <tr><td>Secret (S)</td><td>Sensitive national security information</td><td>Cause serious damage to national security</td></tr>
          <tr><td>Confidential (C)</td><td>Basic classified</td><td>Damage national security</td></tr>
          <tr><td>Unclassified (U)</td><td>Publicly releasable</td><td>No classified risk</td></tr>
        </tbody>
      </table>
    </div>
    <div class="concept-card">
      <div class="concept-label">COMMERCIAL CLASSIFICATION</div>
      <div class="concept-title">Business Data Levels</div>
      <table class="ai-table">
        <thead><tr><th>Level</th><th>Examples</th><th>Handling Requirements</th></tr></thead>
        <tbody>
          <tr><td><strong>Public</strong></td><td>Press releases, job postings, marketing materials</td><td>No restrictions — can share freely</td></tr>
          <tr><td><strong>Internal</strong></td><td>Employee handbooks, internal policies, org charts</td><td>Don't share outside org; no special encryption</td></tr>
          <tr><td><strong>Confidential</strong></td><td>Business plans, contracts, financial forecasts</td><td>Need-to-know basis, access controls, NDA required</td></tr>
          <tr><td><strong>Restricted / Highly Confidential</strong></td><td>PII, PCI data, source code, trade secrets, passwords</td><td>Strict access controls, encryption at rest and transit, audit logs</td></tr>
        </tbody>
      </table>
    </div>
    <div class="concept-card">
      <div class="concept-label">REGULATORY DATA TYPES</div>
      <div class="concept-title">Data Categories with Legal Protection</div>
      <table class="ai-table">
        <thead><tr><th>Acronym</th><th>Full Name</th><th>Examples</th><th>Key Law/Framework</th></tr></thead>
        <tbody>
          <tr><td><strong>PII</strong></td><td>Personally Identifiable Information</td><td>Name, SSN, DOB, address, email, IP address</td><td>GDPR, CCPA, GLBA</td></tr>
          <tr><td><strong>PHI</strong></td><td>Protected Health Information</td><td>Medical records, diagnoses, prescriptions, insurance info</td><td>HIPAA</td></tr>
          <tr><td><strong>PCI</strong></td><td>Payment Card Information</td><td>Card numbers, CVV, expiration, cardholder name</td><td>PCI-DSS</td></tr>
          <tr><td><strong>IP</strong></td><td>Intellectual Property</td><td>Source code, patents, trade secrets, formulas</td><td>IP law, NDAs, trade secret law</td></tr>
        </tbody>
      </table>
    </div>
  </div>
</div>
"""

# ─────────────────────────────── LIFESTYLE wave 13 ───────────────────────────
LIFE_SENTINEL = "<!-- BEGINNER13-LIFE v1 -->"
LIFE_CONTENT = """
<!-- BEGINNER13-LIFE v1 -->
<!-- ── TOPIC: INTERVIEW PREPARATION ─────────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">🎯</span>
    <span class="topic-name">Interview Preparation — Getting the Job</span>
    <span class="topic-badge">LIFESTYLE • Career</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">THE STAR METHOD</div>
      <div class="concept-title">Answering Behavioral Questions</div>
      <div class="concept-desc">Behavioral questions ask you to describe past situations: "Tell me about a time when..." They're designed to predict future behavior based on past behavior. The STAR method gives your answer structure so it's clear, complete, and compelling — instead of rambling.</div>
      <table class="ai-table">
        <thead><tr><th>Letter</th><th>Component</th><th>What to Include</th></tr></thead>
        <tbody>
          <tr><td><strong>S</strong></td><td>Situation</td><td>Set the context. Where, when, what was your role? Keep brief (1-2 sentences).</td></tr>
          <tr><td><strong>T</strong></td><td>Task</td><td>What was YOUR responsibility? What needed to be done or fixed?</td></tr>
          <tr><td><strong>A</strong></td><td>Action</td><td>What did YOU specifically do? Use "I", not "we." This is the meat — be specific.</td></tr>
          <tr><td><strong>R</strong></td><td>Result</td><td>What happened? Quantify if possible ("reduced tickets by 30%", "prevented $50k outage"). What did you learn?</td></tr>
        </tbody>
      </table>
    </div>
    <div class="concept-card">
      <div class="concept-label">COMMON BEHAVIORAL QUESTIONS</div>
      <div class="concept-title">Prepare These Before Any Interview</div>
      <table class="ai-table">
        <thead><tr><th>Question</th><th>What They're Really Asking</th></tr></thead>
        <tbody>
          <tr><td>"Tell me about a time you failed"</td><td>Do you take ownership? Do you learn from mistakes?</td></tr>
          <tr><td>"Describe a conflict with a coworker"</td><td>Can you work with difficult people professionally?</td></tr>
          <tr><td>"Tell me about a project you're proud of"</td><td>What are your actual capabilities and values?</td></tr>
          <tr><td>"How do you handle competing priorities?"</td><td>Are you organized? Do you communicate proactively?</td></tr>
          <tr><td>"Tell me about a time you went above and beyond"</td><td>Do you take initiative? Are you motivated?</td></tr>
          <tr><td>"Where do you see yourself in 5 years?"</td><td>Are you serious about growth? Will you stay?</td></tr>
        </tbody>
      </table>
    </div>
    <div class="concept-card">
      <div class="concept-label">TECHNICAL INTERVIEW TIPS</div>
      <div class="concept-title">How to Approach Technical Questions</div>
      <div class="concept-desc">For IT technical interviews, knowledge matters but so does how you think. Interviewers want to see your troubleshooting process, not just that you memorized commands.</div>
      <table class="ai-table">
        <thead><tr><th>Situation</th><th>What to Do</th></tr></thead>
        <tbody>
          <tr><td>You don't know the answer</td><td>Say "I haven't encountered that specific scenario, but here's how I'd approach it..." — show your thinking</td></tr>
          <tr><td>Troubleshooting scenario</td><td>Think out loud. Start at OSI layer 1, work up. Ask clarifying questions.</td></tr>
          <tr><td>"How would you secure X?"</td><td>Use a framework: people/process/technology, or defense-in-depth layers</td></tr>
          <tr><td>Whiteboard/drawing question</td><td>Start simple, label everything, ask about constraints</td></tr>
          <tr><td>Brain freeze</td><td>"Give me a moment to think through this properly" — silence is better than rambling</td></tr>
        </tbody>
      </table>
    </div>
    <div class="concept-card">
      <div class="concept-label">QUESTIONS TO ASK THEM</div>
      <div class="concept-title">Always Have Questions Ready</div>
      <div class="concept-desc">At the end of every interview: "Do you have any questions for us?" Saying "No, I'm good" is a red flag. Asking good questions shows you're serious, helps you evaluate the role, and keeps the conversation going. Ask 2-3 from this list.</div>
      <table class="ai-table">
        <thead><tr><th>Category</th><th>Good Questions</th></tr></thead>
        <tbody>
          <tr><td>The role</td><td>"What does success look like in the first 90 days?" / "What are the biggest challenges the team is facing?"</td></tr>
          <tr><td>Growth</td><td>"How do people typically grow in this role?" / "Is there a training budget?"</td></tr>
          <tr><td>Culture</td><td>"How does the team handle incidents?" / "What's the on-call rotation like?"</td></tr>
          <tr><td>Tech stack</td><td>"What tools does the team use day-to-day?" / "How do you handle tech debt?"</td></tr>
        </tbody>
      </table>
    </div>
    <div class="concept-card">
      <div class="concept-label">SALARY NEGOTIATION</div>
      <div class="concept-title">You Should Always Negotiate</div>
      <div class="concept-desc">Most hiring managers expect negotiation. The worst they can say is no. Not negotiating is leaving money on the table. Here's the framework — and the phrases that work.</div>
      <table class="ai-table">
        <thead><tr><th>Situation</th><th>What to Say</th></tr></thead>
        <tbody>
          <tr><td>They ask for your number first</td><td>"I'd prefer to hear your budget for this role first, to make sure we're aligned." If pushed: give a researched range, top end is your real target.</td></tr>
          <tr><td>They give you an offer</td><td>Never accept on the spot. "Thank you — I'm really excited about this role. Can I have a few days to review it?"</td></tr>
          <tr><td>Counter-offer</td><td>"I'm very excited about the opportunity. Based on my research and experience, I was hoping for [X]. Is there flexibility there?"</td></tr>
          <tr><td>They say no to salary</td><td>Negotiate everything else: signing bonus, extra PTO, WFH flexibility, earlier review date, training budget, title.</td></tr>
        </tbody>
      </table>
    </div>
  </div>
</div>

<!-- ── TOPIC: TIME MANAGEMENT FOR TECH WORKERS ───────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">⏱️</span>
    <span class="topic-name">Time Management — Making Your Hours Count</span>
    <span class="topic-badge">LIFESTYLE • Productivity</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">THE CORE PROBLEM</div>
      <div class="concept-title">Tech Work Is Constantly Interrupted</div>
      <div class="concept-desc">Deep work — the focused, uninterrupted concentration that produces real output — takes approximately 23 minutes to recover from each interruption. A day of constant Slack pings and meetings produces the feeling of work with very little actual output. Protecting your focus is a technical skill, not a personality preference.</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">THE POMODORO TECHNIQUE</div>
      <div class="concept-title">Work in Focused Sprints</div>
      <div class="concept-desc">Francesco Cirillo's technique: work in 25-minute focused blocks (a "pomodoro"), then take a 5-minute break. Every 4 pomodoros, take a 15-30 minute break. Simple and effective for fighting procrastination and tracking what you actually accomplished.</div>
      <div class="code-block"><span class="com"># Pomodoro pattern</span>
[25 min work] → [5 min break]     <span class="com"># 1 pomodoro</span>
[25 min work] → [5 min break]     <span class="com"># 2nd</span>
[25 min work] → [5 min break]     <span class="com"># 3rd</span>
[25 min work] → [25 min break]    <span class="com"># 4th — long break</span>

<span class="com"># Linux terminal timer (simple)</span>
sleep 1500 &amp;&amp; echo "Pomodoro done!" | wall  <span class="com"># 25 min</span>

<span class="com"># Or use the timer command if installed</span>
timer 25m "Focus session done"</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">THE EISENHOWER MATRIX</div>
      <div class="concept-title">Prioritize by Urgency and Importance</div>
      <table class="ai-table">
        <thead><tr><th></th><th>Urgent</th><th>Not Urgent</th></tr></thead>
        <tbody>
          <tr><td><strong>Important</strong></td><td><strong>Q1: DO FIRST</strong><br>Production is down. Security incident. Deadline today.</td><td><strong>Q2: SCHEDULE</strong><br>Learning new skills. Planning. Preventing future problems.</td></tr>
          <tr><td><strong>Not Important</strong></td><td><strong>Q3: DELEGATE</strong><br>Most interruptions. Many meetings. Someone else's urgent.</td><td><strong>Q4: ELIMINATE</strong><br>Social media scrolling. Busywork. Unnecessary reports.</td></tr>
        </tbody>
      </table>
      <div class="concept-desc">The trap: most people spend too much time in Q1 (reactive firefighting) and Q3 (other people's urgency). High performers protect Q2 — this is where growth and prevention happen. If you never invest in Q2, Q1 grows forever.</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">ASYNC FIRST</div>
      <div class="concept-title">Protect Deep Work Time</div>
      <table class="ai-table">
        <thead><tr><th>Tactic</th><th>How To Implement</th></tr></thead>
        <tbody>
          <tr><td>Batch notifications</td><td>Check Slack/email at 9am, noon, 4pm — not constantly</td></tr>
          <tr><td>Time blocking</td><td>Block 2-4 hour "deep work" blocks in your calendar — treat them like meetings</td></tr>
          <tr><td>Do Not Disturb</td><td>OS-level DND during focus blocks. People survive without instant responses.</td></tr>
          <tr><td>Default to async</td><td>If it doesn't need an immediate decision, use email/ticket — not a meeting</td></tr>
          <tr><td>Weekly review</td><td>Every Friday: what did I accomplish? What are next week's top 3 priorities?</td></tr>
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
        (NET_INJECT_ANCHOR,    NET_SENTINEL,    NET_CONTENT),
        (LINUX_INJECT_ANCHOR,  LINUX_SENTINEL,  LINUX_CONTENT),
        (GRC_INJECT_ANCHOR,    GRC_SENTINEL,    GRC_CONTENT),
        (LIFE_INJECT_ANCHOR,   LIFE_SENTINEL,   LIFE_CONTENT),
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

    # Validate HTML balance
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
