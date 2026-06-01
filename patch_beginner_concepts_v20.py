#!/usr/bin/env python3
"""
patch_beginner_concepts_v20.py — Wave 20: Password attacks, web security
headers, Linux boot/logs, tmux deep dive, complete CLI tools.

New sentinels:
  BEGINNER20-PENTEST v1  — Password attacks, hash cracking, wordlists, auth attacks
  BEGINNER20-SEC v1      — Web security headers, browser security model, cookies, CORS
  BEGINNER20-LINUX v1    — Boot process, log files, journald, system troubleshooting
  BEGINNER20-SHORTCUT v1 — tmux deep dive, terminal multiplexing, workflows
  BEGINNER20-SCRIPT v1   — Building a complete CLI tool (argparse + config + logging)
"""
from pathlib import Path

PENTEST_INJECT_ANCHOR  = "<!-- /domain-body pentest -->"
SEC_INJECT_ANCHOR      = "<!-- /domain-body sec -->"
LINUX_INJECT_ANCHOR    = "<!-- /domain-body linux -->"
SHORTCUT_INJECT_ANCHOR = "<!-- /domain-body shortcuts -->"
SCRIPT_INJECT_ANCHOR   = "<!-- /domain-body script -->"

# ─────────────────────────────── PENTEST wave 20 ─────────────────────────────
PENTEST_SENTINEL = "<!-- BEGINNER20-PENTEST v1 -->"
PENTEST_CONTENT = """
<!-- BEGINNER20-PENTEST v1 -->
<!-- ── TOPIC: PASSWORD ATTACKS ───────────────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">🔓</span>
    <span class="topic-name">Password Attacks — How Credentials Get Cracked</span>
    <span class="topic-badge">PENTEST • Authorized Only</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">⚠️ ETHICS FIRST</div>
      <div class="concept-title">Only on Systems You're Authorized to Test</div>
      <div class="concept-desc">Everything here is for authorized penetration testing, CTFs, your own lab, and understanding defense. Cracking passwords you don't own is a crime. The reason defenders learn these techniques is to understand why strong hashing, MFA, and rate-limiting matter — and to test their own org's resilience with written authorization.</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">ATTACK TYPES</div>
      <div class="concept-title">Online vs Offline Attacks</div>
      <table class="ai-table">
        <thead><tr><th>Attack</th><th>How It Works</th><th>Defense</th></tr></thead>
        <tbody>
          <tr><td>Brute force</td><td>Try every possible combination</td><td>Length + complexity (makes it infeasible)</td></tr>
          <tr><td>Dictionary</td><td>Try a wordlist of likely passwords</td><td>Don't use common passwords</td></tr>
          <tr><td>Credential stuffing</td><td>Reuse leaked user:pass from other breaches</td><td>Unique passwords per site; MFA</td></tr>
          <tr><td>Password spraying</td><td>Try ONE common password against MANY accounts (avoids lockout)</td><td>MFA, anomaly detection</td></tr>
          <tr><td>Rainbow tables</td><td>Precomputed hash→password lookups</td><td>Salting (makes tables useless)</td></tr>
        </tbody>
      </table>
      <div class="concept-desc"><strong>Online</strong> attacks hit a live login (slow, rate-limited, detectable). <strong>Offline</strong> attacks crack a stolen hash database locally (fast, unlimited guesses — why a breached hash dump is so dangerous).</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">HASH CRACKING</div>
      <div class="concept-title">hashcat and John the Ripper</div>
      <div class="concept-desc">When attackers steal a database, they get password <em>hashes</em>, not plaintext. Cracking tools guess passwords, hash each guess, and compare. GPUs make this billions of guesses per second — which is why weak hashing (fast MD5/SHA1, no salt) is catastrophic and slow hashing (bcrypt, Argon2) is essential.</div>
      <div class="code-block"><span class="com"># Identify a hash type first</span>
hashid '$2y$10$...'        <span class="com"># identifies bcrypt</span>

<span class="com"># hashcat — dictionary attack (mode -a 0)</span>
hashcat -m 0 -a 0 hashes.txt rockyou.txt    <span class="com"># -m 0 = MD5</span>
hashcat -m 1000 -a 0 ntlm.txt rockyou.txt   <span class="com"># -m 1000 = NTLM</span>

<span class="com"># hashcat — with rules (mutate words: P@ssw0rd!, etc.)</span>
hashcat -m 0 -a 0 hashes.txt rockyou.txt -r best64.rule

<span class="com"># hashcat — brute force a mask (mode -a 3)</span>
hashcat -m 0 -a 3 hashes.txt ?u?l?l?l?d?d?d?d   <span class="com"># Ulll dddd</span>

<span class="com"># John the Ripper</span>
john --wordlist=rockyou.txt hashes.txt
john --show hashes.txt     <span class="com"># show cracked results</span></div>
    </div>
    <div class="concept-card">
      <div class="concept-label">WORDLISTS & RULES</div>
      <div class="concept-title">The Attacker's Ammunition</div>
      <table class="ai-table">
        <thead><tr><th>Resource</th><th>What It Is</th></tr></thead>
        <tbody>
          <tr><td>rockyou.txt</td><td>14M real passwords from a 2009 breach — the classic starter wordlist</td></tr>
          <tr><td>SecLists</td><td>Huge collection of wordlists for passwords, usernames, fuzzing, payloads</td></tr>
          <tr><td>Mutation rules</td><td>Transform words: capitalize, append years/symbols (best64, dive)</td></tr>
          <tr><td>Custom (CeWL)</td><td>Scrape a target's website to build a tailored wordlist</td></tr>
          <tr><td>crunch</td><td>Generate wordlists by pattern (for masks/known formats)</td></tr>
        </tbody>
      </table>
      <div class="concept-desc"><strong>The defensive lesson:</strong> this is exactly why length beats complexity. A 16-character passphrase resists all of this; "P@ssw0rd1" falls in milliseconds because it's in every wordlist and matches every rule.</div>
    </div>
  </div>
</div>
"""

# ─────────────────────────────── SEC wave 20 ─────────────────────────────────
SEC_SENTINEL = "<!-- BEGINNER20-SEC v1 -->"
SEC_CONTENT = """
<!-- BEGINNER20-SEC v1 -->
<!-- ── TOPIC: WEB SECURITY HEADERS ───────────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">🛡️</span>
    <span class="topic-name">Web Security Headers — Free Defense in a Few Lines</span>
    <span class="topic-badge">SEC • Practical</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">THE IDEA</div>
      <div class="concept-title">HTTP Headers That Harden the Browser</div>
      <div class="concept-desc">Web servers can send special HTTP response headers that instruct the browser to enforce security protections. They're cheap to add and prevent entire classes of attacks (XSS, clickjacking, protocol downgrade). Auditing these is often one of the first things a security review checks.</div>
      <table class="ai-table">
        <thead><tr><th>Header</th><th>Protects Against</th><th>Example</th></tr></thead>
        <tbody>
          <tr><td>Content-Security-Policy</td><td>XSS, data injection</td><td><code>default-src 'self'</code></td></tr>
          <tr><td>Strict-Transport-Security (HSTS)</td><td>Protocol downgrade, SSL stripping</td><td><code>max-age=31536000; includeSubDomains</code></td></tr>
          <tr><td>X-Frame-Options</td><td>Clickjacking</td><td><code>DENY</code> (don't allow framing)</td></tr>
          <tr><td>X-Content-Type-Options</td><td>MIME sniffing attacks</td><td><code>nosniff</code></td></tr>
          <tr><td>Referrer-Policy</td><td>Leaking URLs to other sites</td><td><code>strict-origin-when-cross-origin</code></td></tr>
          <tr><td>Permissions-Policy</td><td>Abuse of browser features (camera, mic)</td><td><code>geolocation=(), camera=()</code></td></tr>
        </tbody>
      </table>
    </div>
    <div class="concept-card">
      <div class="concept-label">COOKIE SECURITY</div>
      <div class="concept-title">The Flags That Protect Sessions</div>
      <div class="concept-desc">Session cookies are prime theft targets — steal one and you can impersonate the user. Three flags dramatically reduce the risk.</div>
      <table class="ai-table">
        <thead><tr><th>Flag</th><th>Effect</th></tr></thead>
        <tbody>
          <tr><td><code>Secure</code></td><td>Cookie only sent over HTTPS (never plaintext HTTP)</td></tr>
          <tr><td><code>HttpOnly</code></td><td>JavaScript can't read it — defeats cookie theft via XSS</td></tr>
          <tr><td><code>SameSite=Strict/Lax</code></td><td>Not sent on cross-site requests — defeats CSRF</td></tr>
        </tbody>
      </table>
      <div class="code-block"><span class="com"># A well-secured session cookie</span>
Set-Cookie: session=abc123; Secure; HttpOnly; SameSite=Strict; Path=/</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">SAME-ORIGIN & CORS</div>
      <div class="concept-title">The Browser's Core Security Boundary</div>
      <div class="concept-desc">The <strong>Same-Origin Policy</strong> is the foundation of web security: a page from <code>siteA.com</code> can't read data from <code>siteB.com</code>. "Origin" = scheme + host + port. This stops a malicious site from reading your bank session. <strong>CORS</strong> (Cross-Origin Resource Sharing) is the controlled way to relax this — a server explicitly opts in to allow specific other origins to call it. CORS errors confuse beginners, but they're the browser <em>protecting</em> the user, not a bug.</div>
      <div class="code-block"><span class="com"># Server allows a specific origin to call its API</span>
Access-Control-Allow-Origin: https://app.example.com
Access-Control-Allow-Methods: GET, POST
Access-Control-Allow-Credentials: true

<span class="com"># Common beginner mistake (insecure!) — allow everything:</span>
Access-Control-Allow-Origin: *    <span class="com"># OK for public APIs, dangerous with credentials</span></div>
    </div>
    <div class="concept-card">
      <div class="concept-label">TESTING HEADERS</div>
      <div class="concept-title">Quickly Audit a Site's Headers</div>
      <div class="code-block"><span class="com"># See response headers with curl</span>
curl -I https://example.com         <span class="com"># HEAD request, headers only</span>
curl -sD - https://example.com -o /dev/null   <span class="com"># dump headers</span>

<span class="com"># Online graders: securityheaders.com, Mozilla Observatory</span>
<span class="com"># Browser DevTools → Network tab → click request → Headers</span></div>
    </div>
  </div>
</div>
"""

# ─────────────────────────────── LINUX wave 20 ───────────────────────────────
LINUX_SENTINEL = "<!-- BEGINNER20-LINUX v1 -->"
LINUX_CONTENT = """
<!-- BEGINNER20-LINUX v1 -->
<!-- ── TOPIC: BOOT PROCESS & LOGS ────────────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">🥾</span>
    <span class="topic-name">Boot Process &amp; Logs — Understanding How Linux Starts and Speaks</span>
    <span class="topic-badge">LINUX • Essential</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">THE BOOT SEQUENCE</div>
      <div class="concept-title">From Power Button to Login Prompt</div>
      <div class="concept-desc">Knowing the boot sequence helps you troubleshoot a system that won't start — you can pinpoint which stage failed. Modern Linux boots in roughly these steps:</div>
      <table class="ai-table">
        <thead><tr><th>Stage</th><th>What Happens</th><th>If It Fails</th></tr></thead>
        <tbody>
          <tr><td>1. Firmware (BIOS/UEFI)</td><td>Hardware self-test (POST), finds boot device</td><td>No display, beeps — hardware/firmware issue</td></tr>
          <tr><td>2. Bootloader (GRUB)</td><td>Loads kernel, shows boot menu</td><td>"No bootable device", GRUB rescue prompt</td></tr>
          <tr><td>3. Kernel</td><td>Initializes hardware, mounts initramfs</td><td>Kernel panic</td></tr>
          <tr><td>4. init (systemd)</td><td>PID 1; starts all services in dependency order</td><td>Hangs on a service, emergency mode</td></tr>
          <tr><td>5. Targets/services</td><td>Reaches multi-user or graphical target</td><td>Service failures (check journalctl)</td></tr>
          <tr><td>6. Login</td><td>getty/display manager presents login</td><td>Can't log in — auth/PAM/disk-full</td></tr>
        </tbody>
      </table>
    </div>
    <div class="concept-card">
      <div class="concept-label">WHERE THE LOGS LIVE</div>
      <div class="concept-title">Important Log Locations</div>
      <table class="ai-table">
        <thead><tr><th>Path</th><th>Contains</th></tr></thead>
        <tbody>
          <tr><td><code>/var/log/syslog</code> or <code>/var/log/messages</code></td><td>General system messages</td></tr>
          <tr><td><code>/var/log/auth.log</code> or <code>/var/log/secure</code></td><td>Authentication, sudo, SSH logins</td></tr>
          <tr><td><code>/var/log/kern.log</code></td><td>Kernel messages</td></tr>
          <tr><td><code>/var/log/dmesg</code></td><td>Boot-time hardware messages</td></tr>
          <tr><td><code>/var/log/nginx/</code>, <code>/var/log/apache2/</code></td><td>Web server access/error logs</td></tr>
          <tr><td><code>journalctl</code> (systemd journal)</td><td>Unified binary log for everything systemd manages</td></tr>
        </tbody>
      </table>
    </div>
    <div class="concept-card">
      <div class="concept-label">JOURNALCTL</div>
      <div class="concept-title">Querying the systemd Journal</div>
      <div class="code-block">journalctl                       <span class="com"># all logs (q to quit)</span>
journalctl -e                    <span class="com"># jump to end (newest)</span>
journalctl -f                    <span class="com"># follow live (like tail -f)</span>
journalctl -u nginx              <span class="com"># logs for one service</span>
journalctl -u nginx --since "1 hour ago"
journalctl --since "2024-01-15 09:00" --until "10:00"
journalctl -p err                <span class="com"># only errors and worse</span>
journalctl -b                    <span class="com"># since this boot</span>
journalctl -b -1                 <span class="com"># the PREVIOUS boot (for crash analysis)</span>
journalctl -k                    <span class="com"># kernel messages (= dmesg)</span>
journalctl --disk-usage          <span class="com"># how much space logs use</span>
journalctl --vacuum-time=7d      <span class="com"># delete logs older than 7 days</span></div>
    </div>
    <div class="concept-card">
      <div class="concept-label">A TROUBLESHOOTING FLOW</div>
      <div class="concept-title">"The Server Is Acting Weird" — Where to Start</div>
      <div class="code-block"><span class="com"># 1. Is it up? Can you reach it?</span>
ping host; ssh host

<span class="com"># 2. What's the overall health?</span>
uptime              <span class="com"># load average</span>
free -h             <span class="com"># memory</span>
df -h               <span class="com"># disk full? (a VERY common cause of weirdness)</span>

<span class="com"># 3. Any failed services?</span>
systemctl --failed

<span class="com"># 4. What's in the recent logs?</span>
journalctl -p err -b --no-pager | tail -50
journalctl -u suspect-service -e

<span class="com"># 5. What's eating resources?</span>
top                 <span class="com"># or htop</span>

<span class="com"># 6. Recent changes? (the usual culprit)</span>
journalctl --since "30 min ago" | grep -i -E "error|fail|warn"</div>
    </div>
  </div>
</div>
"""

# ─────────────────────────────── SHORTCUT wave 20 ────────────────────────────
SHORTCUT_SENTINEL = "<!-- BEGINNER20-SHORTCUT v1 -->"
SHORTCUT_CONTENT = """
<!-- BEGINNER20-SHORTCUT v1 -->
<!-- ── TOPIC: TMUX DEEP DIVE ─────────────────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">🪟</span>
    <span class="topic-name">tmux — Never Lose a Session Again</span>
    <span class="topic-badge">SHORTCUTS • Productivity</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">WHY TMUX</div>
      <div class="concept-title">The Persistent, Splittable Terminal</div>
      <div class="concept-desc">tmux (terminal multiplexer) solves two huge problems: <strong>(1) Persistence</strong> — your session keeps running on the server even if your SSH connection drops or you close your laptop. Reconnect and everything's exactly where you left it. <strong>(2) Layout</strong> — split one terminal into multiple panes and windows. For anyone who works on remote servers, tmux is life-changing. A long-running job no longer dies when your Wi-Fi hiccups.</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">THE PREFIX KEY</div>
      <div class="concept-title">Everything Starts with Ctrl+b</div>
      <div class="concept-desc">tmux commands begin with a <strong>prefix</strong> — by default <code>Ctrl+b</code> — then a key. Notation: <code>C-b</code> means Ctrl+b, release, then press the next key. (Many people remap the prefix to <code>Ctrl+a</code> for ergonomics.)</div>
      <div class="code-block"><span class="com"># Session management (from the shell)</span>
tmux                       <span class="com"># start a new session</span>
tmux new -s work           <span class="com"># named session "work"</span>
tmux ls                    <span class="com"># list sessions</span>
tmux attach -t work        <span class="com"># reattach to "work"</span>
tmux kill-session -t work

<span class="com"># THE killer feature: detach and reattach</span>
<span class="com"># C-b d   → detach (session keeps running on the server)</span>
<span class="com"># Later: tmux attach   → everything's still there</span></div>
    </div>
    <div class="concept-card">
      <div class="concept-label">PANES & WINDOWS</div>
      <div class="concept-title">Splitting and Navigating</div>
      <table class="ai-table">
        <thead><tr><th>Keys (after C-b)</th><th>Action</th></tr></thead>
        <tbody>
          <tr><td><code>%</code></td><td>Split pane vertically (left/right)</td></tr>
          <tr><td><code>"</code></td><td>Split pane horizontally (top/bottom)</td></tr>
          <tr><td><code>arrow keys</code></td><td>Move between panes</td></tr>
          <tr><td><code>o</code></td><td>Cycle to next pane</td></tr>
          <tr><td><code>z</code></td><td>Zoom pane to fullscreen (toggle)</td></tr>
          <tr><td><code>x</code></td><td>Close current pane</td></tr>
          <tr><td><code>c</code></td><td>Create a new window (like a tab)</td></tr>
          <tr><td><code>n</code> / <code>p</code></td><td>Next / previous window</td></tr>
          <tr><td><code>0-9</code></td><td>Jump to window by number</td></tr>
          <tr><td><code>,</code></td><td>Rename current window</td></tr>
          <tr><td><code>[</code></td><td>Enter scroll/copy mode (q to exit)</td></tr>
        </tbody>
      </table>
    </div>
    <div class="concept-card">
      <div class="concept-label">CONFIG</div>
      <div class="concept-title">A Sensible ~/.tmux.conf Starter</div>
      <div class="code-block"><span class="com"># ~/.tmux.conf</span>
<span class="com"># Remap prefix to Ctrl+a (easier reach)</span>
unbind C-b
set -g prefix C-a

<span class="com"># Start windows/panes at 1, not 0</span>
set -g base-index 1

<span class="com"># Enable mouse (scroll, click panes, resize)</span>
set -g mouse on

<span class="com"># More scrollback history</span>
set -g history-limit 10000

<span class="com"># Easier splits that remember current path</span>
bind | split-window -h -c "#{pane_current_path}"
bind - split-window -v -c "#{pane_current_path}"

<span class="com"># Reload config without restarting: C-a r</span>
bind r source-file ~/.tmux.conf \\; display "Reloaded!"</div>
    </div>
  </div>
</div>
"""

# ─────────────────────────────── SCRIPT wave 20 ──────────────────────────────
SCRIPT_SENTINEL = "<!-- BEGINNER20-SCRIPT v1 -->"
SCRIPT_CONTENT = """
<!-- BEGINNER20-SCRIPT v1 -->
<!-- ── TOPIC: BUILDING A COMPLETE CLI TOOL ───────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">🛠️</span>
    <span class="topic-name">Building a Real CLI Tool — Putting It All Together</span>
    <span class="topic-badge">SCRIPT • Capstone</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">FROM SNIPPET TO TOOL</div>
      <div class="concept-title">What Separates a Script from a Tool</div>
      <div class="concept-desc">A throwaway script has hardcoded values and prints with <code>print()</code>. A real tool that others can use has: command-line arguments, configuration, proper logging, error handling, and a clear exit code. Here's a complete example that ties together everything — argparse, logging, config, and exit codes — into a tool you'd actually deploy.</div>
      <div class="code-block"><span class="com">#!/usr/bin/env python3</span>
<span class="str">&quot;&quot;&quot;logcheck — scan a log file for error patterns and report.&quot;&quot;&quot;</span>
<span class="kw">import</span> argparse, logging, sys, re
<span class="kw">from</span> pathlib <span class="kw">import</span> Path

<span class="com"># ── Logging setup ─────────────────────────────────────────</span>
log = logging.getLogger(<span class="str">"logcheck"</span>)

<span class="kw">def</span> <span class="fn">setup_logging</span>(verbose: bool):
    level = logging.DEBUG <span class="kw">if</span> verbose <span class="kw">else</span> logging.INFO
    logging.basicConfig(
        level=level,
        format=<span class="str">"%(asctime)s %(levelname)s %(message)s"</span>,
    )

<span class="com"># ── Core logic ────────────────────────────────────────────</span>
<span class="kw">def</span> <span class="fn">scan</span>(path: Path, pattern: str) -&gt; <span class="fn">int</span>:
    regex = re.compile(pattern)
    matches = <span class="num">0</span>
    <span class="kw">with</span> path.open() <span class="kw">as</span> f:
        <span class="kw">for</span> num, line <span class="kw">in</span> <span class="fn">enumerate</span>(f, <span class="num">1</span>):
            <span class="kw">if</span> regex.search(line):
                matches += <span class="num">1</span>
                log.debug(<span class="str">"match line %d: %s"</span>, num, line.strip())
    <span class="kw">return</span> matches

<span class="com"># ── Argument parsing ──────────────────────────────────────</span>
<span class="kw">def</span> <span class="fn">main</span>(argv=<span class="kw">None</span>):
    p = argparse.ArgumentParser(description=<span class="str">"Scan a log for a pattern."</span>)
    p.add_argument(<span class="str">"logfile"</span>, type=Path, help=<span class="str">"log file to scan"</span>)
    p.add_argument(<span class="str">"-p"</span>, <span class="str">"--pattern"</span>, default=<span class="str">"ERROR"</span>, help=<span class="str">"regex pattern"</span>)
    p.add_argument(<span class="str">"-t"</span>, <span class="str">"--threshold"</span>, type=<span class="fn">int</span>, default=<span class="num">0</span>,
                   help=<span class="str">"exit non-zero if matches exceed this"</span>)
    p.add_argument(<span class="str">"-v"</span>, <span class="str">"--verbose"</span>, action=<span class="str">"store_true"</span>)
    args = p.parse_args(argv)

    setup_logging(args.verbose)

    <span class="kw">if</span> <span class="kw">not</span> args.logfile.exists():
        log.error(<span class="str">"File not found: %s"</span>, args.logfile)
        <span class="kw">return</span> <span class="num">2</span>                       <span class="com"># exit code 2 = usage/file error</span>

    count = scan(args.logfile, args.pattern)
    log.info(<span class="str">"Found %d matches for %r"</span>, count, args.pattern)

    <span class="com"># Exit code drives monitoring/automation</span>
    <span class="kw">if</span> count &gt; args.threshold:
        log.warning(<span class="str">"Threshold exceeded!"</span>)
        <span class="kw">return</span> <span class="num">1</span>
    <span class="kw">return</span> <span class="num">0</span>

<span class="kw">if</span> __name__ == <span class="str">"__main__"</span>:
    sys.exit(main())</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">USING IT</div>
      <div class="concept-title">Why This Design Pays Off</div>
      <div class="code-block"><span class="com"># Self-documenting — argparse generates --help for free</span>
./logcheck.py --help

<span class="com"># Flexible without editing code</span>
./logcheck.py /var/log/app.log
./logcheck.py /var/log/app.log -p "CRITICAL|FATAL" -t 5 -v

<span class="com"># Exit codes integrate with shell + monitoring</span>
./logcheck.py app.log -t 10 || echo "ALERT: too many errors!"

<span class="com"># Composes with other tools (the Unix philosophy)</span>
for f in /var/log/*.log; do ./logcheck.py "$f"; done</div>
      <div class="concept-desc"><strong>The key lessons:</strong> accept input via arguments (not hardcoding), use <code>logging</code> (not print) so output levels are controllable, return meaningful <strong>exit codes</strong> (0 = success, non-zero = problem) so the tool plays well with shell scripts and monitoring, and guard <code>main()</code> with <code>if __name__ == "__main__"</code> so it's also importable. This is the anatomy of every good CLI tool.</div>
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
        (SEC_INJECT_ANCHOR,      SEC_SENTINEL,      SEC_CONTENT),
        (LINUX_INJECT_ANCHOR,    LINUX_SENTINEL,    LINUX_CONTENT),
        (SHORTCUT_INJECT_ANCHOR, SHORTCUT_SENTINEL, SHORTCUT_CONTENT),
        (SCRIPT_INJECT_ANCHOR,   SCRIPT_SENTINEL,   SCRIPT_CONTENT),
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
