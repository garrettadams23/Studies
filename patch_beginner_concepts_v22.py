#!/usr/bin/env python3
"""
patch_beginner_concepts_v22.py — Wave 22: Encoding & character sets, DNS
security, IDS/IPS & deception, GitOps/observability, on-call & stress.

New sentinels:
  BEGINNER22-SCRIPT v1  — Encoding (base64/hex/URL), character sets, UTF-8, bytes vs str
  BEGINNER22-NET v1     — DNS deep dive, record types, DNS security (DNSSEC, DoH/DoT)
  BEGINNER22-SEC v1     — IDS/IPS, network detection, honeypots, deception tech
  BEGINNER22-OPS v1     — GitOps, observability stack, the three pillars in practice
  BEGINNER22-LIFE v1    — On-call survival, stress management, work-life in IT
"""
from pathlib import Path

SCRIPT_INJECT_ANCHOR = "<!-- /domain-body script -->"
NET_INJECT_ANCHOR    = "<!-- /domain-body net -->"
SEC_INJECT_ANCHOR    = "<!-- /domain-body sec -->"
OPS_INJECT_ANCHOR    = "<!-- /domain-body ops -->"
LIFE_INJECT_ANCHOR   = "<!-- /domain-body lifestyle -->"

# ─────────────────────────────── SCRIPT wave 22 ──────────────────────────────
SCRIPT_SENTINEL = "<!-- BEGINNER22-SCRIPT v1 -->"
SCRIPT_CONTENT = """
<!-- BEGINNER22-SCRIPT v1 -->
<!-- ── TOPIC: ENCODING & CHARACTER SETS ──────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">🔤</span>
    <span class="topic-name">Encoding — Bytes, Text, and Why "It Works on My Machine"</span>
    <span class="topic-badge">SCRIPT • Foundation</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">BYTES VS TEXT</div>
      <div class="concept-title">The Distinction That Trips Up Everyone</div>
      <div class="concept-desc">Computers store everything as bytes (numbers 0-255). Text is bytes <em>interpreted</em> through an encoding. <code>str</code> is human-readable text; <code>bytes</code> is raw binary. You <strong>encode</strong> text → bytes (to send/store) and <strong>decode</strong> bytes → text (to read). Confusing the two causes the classic <code>UnicodeDecodeError</code> and garbled "mojibake" text.</div>
      <div class="code-block"><span class="com"># Text (str) ↔ raw bytes</span>
text = <span class="str">"café"</span>
data = text.encode(<span class="str">"utf-8"</span>)        <span class="com"># str → bytes: b'caf\\xc3\\xa9'</span>
back = data.decode(<span class="str">"utf-8"</span>)        <span class="com"># bytes → str: 'café'</span>

<span class="com"># The golden rule: decode at input, encode at output.</span>
<span class="com"># Work with str internally; only deal in bytes at the edges</span>
<span class="com"># (files, network, subprocess).</span>

<span class="com"># Always specify encoding explicitly — don't rely on defaults</span>
<span class="kw">with</span> <span class="fn">open</span>(<span class="str">"f.txt"</span>, encoding=<span class="str">"utf-8"</span>) <span class="kw">as</span> f: ...</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">UTF-8 & UNICODE</div>
      <div class="concept-title">One Encoding to Rule Them All</div>
      <div class="concept-desc"><strong>Unicode</strong> assigns every character a number ("code point") — covering every language, emoji, and symbol. <strong>UTF-8</strong> is the dominant way to encode those code points as bytes: it's variable-width (1 byte for ASCII, up to 4 for others) and backward-compatible with ASCII. Rule of thumb: <strong>use UTF-8 everywhere</strong>. Legacy encodings (Latin-1, Windows-1252) cause the most "weird character" bugs.</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">ENCODING SCHEMES</div>
      <div class="concept-title">Base64, Hex, URL — Different Jobs</div>
      <div class="concept-desc">These are <em>not</em> encryption — they're reversible representations, no secrecy. They exist to safely move binary data through text-only channels.</div>
      <table class="ai-table">
        <thead><tr><th>Scheme</th><th>Purpose</th><th>Example</th></tr></thead>
        <tbody>
          <tr><td>Base64</td><td>Binary → ASCII text (email attachments, JWTs, data URIs)</td><td><code>SGVsbG8=</code> = "Hello"</td></tr>
          <tr><td>Hex</td><td>Binary → readable hex (hashes, debugging, MAC addresses)</td><td><code>48656c6c6f</code> = "Hello"</td></tr>
          <tr><td>URL encoding</td><td>Make text safe in URLs (% escaping)</td><td><code>%20</code> = space, <code>%40</code> = @</td></tr>
        </tbody>
      </table>
      <div class="code-block"><span class="kw">import</span> base64, urllib.parse

<span class="com"># Base64</span>
base64.b64encode(<span class="str">b"Hello"</span>)              <span class="com"># b'SGVsbG8='</span>
base64.b64decode(<span class="str">b"SGVsbG8="</span>)           <span class="com"># b'Hello'</span>

<span class="com"># Hex</span>
<span class="str">b"Hello"</span>.hex()                       <span class="com"># '48656c6c6f'</span>
<span class="fn">bytes</span>.fromhex(<span class="str">"48656c6c6f"</span>)            <span class="com"># b'Hello'</span>

<span class="com"># URL encoding</span>
urllib.parse.quote(<span class="str">"a b@c"</span>)            <span class="com"># 'a%20b%40c'</span>
urllib.parse.unquote(<span class="str">"a%20b%40c"</span>)       <span class="com"># 'a b@c'</span>

<span class="com"># Command-line equivalents (handy in pentest/CTF)</span>
<span class="com"># echo -n "Hello" | base64</span>
<span class="com"># echo "SGVsbG8=" | base64 -d</span>
<span class="com"># echo -n "Hello" | xxd -p</span></div>
    </div>
    <div class="concept-card">
      <div class="concept-label">HASHING (NOT ENCODING)</div>
      <div class="concept-title">One-Way by Design</div>
      <div class="concept-desc">Don't confuse hashing with encoding/encryption. <strong>Encoding</strong> is reversible (anyone can decode). <strong>Encryption</strong> is reversible with a key. <strong>Hashing</strong> is one-way — you cannot get the input back from the hash. Hashing is for integrity checks and password storage, never for "hiding" data you need to recover.</div>
      <div class="code-block"><span class="kw">import</span> hashlib

<span class="com"># Integrity check — verify a file wasn't altered</span>
data = Path(<span class="str">"file.iso"</span>).read_bytes()
<span class="fn">print</span>(hashlib.sha256(data).hexdigest())

<span class="com"># Command line equivalent</span>
<span class="com"># sha256sum file.iso</span></div>
    </div>
  </div>
</div>
"""

# ─────────────────────────────── NET wave 22 ─────────────────────────────────
NET_SENTINEL = "<!-- BEGINNER22-NET v1 -->"
NET_CONTENT = """
<!-- BEGINNER22-NET v1 -->
<!-- ── TOPIC: DNS DEEP DIVE & SECURITY ───────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">🌍</span>
    <span class="topic-name">DNS Deep Dive — Records, Resolution &amp; Security</span>
    <span class="topic-badge">NET • Essential</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">RECORD TYPES</div>
      <div class="concept-title">The DNS Records You'll Actually Touch</div>
      <table class="ai-table">
        <thead><tr><th>Record</th><th>Maps</th><th>Example / Use</th></tr></thead>
        <tbody>
          <tr><td>A</td><td>Name → IPv4</td><td><code>example.com → 93.184.216.34</code></td></tr>
          <tr><td>AAAA</td><td>Name → IPv6</td><td><code>example.com → 2606:2800:...</code></td></tr>
          <tr><td>CNAME</td><td>Name → another name (alias)</td><td><code>www → example.com</code></td></tr>
          <tr><td>MX</td><td>Mail servers for a domain</td><td>Routes email; has priority values</td></tr>
          <tr><td>TXT</td><td>Arbitrary text</td><td>SPF, DKIM, domain verification</td></tr>
          <tr><td>NS</td><td>Authoritative nameservers</td><td>Who's in charge of this zone</td></tr>
          <tr><td>SOA</td><td>Zone metadata</td><td>Serial, refresh, TTL defaults</td></tr>
          <tr><td>PTR</td><td>IP → name (reverse DNS)</td><td>Mail server reputation, logging</td></tr>
          <tr><td>SRV</td><td>Service location (host+port)</td><td>SIP, LDAP, Microsoft AD</td></tr>
          <tr><td>CAA</td><td>Which CAs may issue certs</td><td>Prevents rogue certificate issuance</td></tr>
        </tbody>
      </table>
    </div>
    <div class="concept-card">
      <div class="concept-label">DIG — THE DNS SWISS ARMY KNIFE</div>
      <div class="concept-title">Query DNS Like a Pro</div>
      <div class="code-block">dig example.com                  <span class="com"># A record (default)</span>
dig example.com +short           <span class="com"># just the answer</span>
dig AAAA example.com             <span class="com"># IPv6</span>
dig MX example.com               <span class="com"># mail servers</span>
dig TXT example.com              <span class="com"># SPF/DKIM/verification</span>
dig NS example.com               <span class="com"># nameservers</span>
dig +trace example.com           <span class="com"># follow the full resolution path</span>
dig @8.8.8.8 example.com         <span class="com"># query a specific resolver</span>
dig -x 93.184.216.34             <span class="com"># reverse lookup (PTR)</span>
dig example.com ANY              <span class="com"># all records (often restricted)</span>

<span class="com"># Troubleshooting: is it a DNS problem or not?</span>
<span class="com"># If dig resolves but the app fails → not DNS</span>
<span class="com"># If dig fails → check resolver (/etc/resolv.conf)</span></div>
    </div>
    <div class="concept-card">
      <div class="concept-label">DNS SECURITY</div>
      <div class="concept-title">DNS Was Not Built Securely</div>
      <div class="concept-desc">Classic DNS is unauthenticated and unencrypted — attackers can forge responses (cache poisoning, spoofing) or snoop on your lookups. Several technologies address this:</div>
      <table class="ai-table">
        <thead><tr><th>Tech</th><th>Protects</th><th>How</th></tr></thead>
        <tbody>
          <tr><td>DNSSEC</td><td>Integrity / authenticity</td><td>Cryptographically signs records — detects forgery (doesn't encrypt)</td></tr>
          <tr><td>DoH (DNS over HTTPS)</td><td>Privacy</td><td>Encrypts queries inside HTTPS (port 443)</td></tr>
          <tr><td>DoT (DNS over TLS)</td><td>Privacy</td><td>Encrypts DNS in TLS (port 853)</td></tr>
          <tr><td>DNS filtering</td><td>Blocking</td><td>Resolver blocks malicious/known-bad domains (e.g., Pi-hole, Quad9)</td></tr>
        </tbody>
      </table>
    </div>
    <div class="concept-card">
      <div class="concept-label">DNS-BASED ATTACKS</div>
      <div class="concept-title">Why Defenders Watch DNS Closely</div>
      <table class="ai-table">
        <thead><tr><th>Attack</th><th>What It Does</th></tr></thead>
        <tbody>
          <tr><td>Cache poisoning</td><td>Inject false records so victims go to attacker's site</td></tr>
          <tr><td>DNS tunneling</td><td>Smuggle data/C2 traffic inside DNS queries (evades firewalls)</td></tr>
          <tr><td>Domain hijacking</td><td>Take over a domain's registration or nameservers</td></tr>
          <tr><td>Fast flux</td><td>Rapidly rotate IPs to keep malicious infra alive</td></tr>
          <tr><td>Typosquatting</td><td>Register lookalike domains (gooogle.com) for phishing</td></tr>
        </tbody>
      </table>
      <div class="concept-desc">DNS logs are gold for threat hunting — unusual domains, high-entropy subdomains (tunneling), and newly-registered domains are strong indicators of compromise.</div>
    </div>
  </div>
</div>
"""

# ─────────────────────────────── SEC wave 22 ─────────────────────────────────
SEC_SENTINEL = "<!-- BEGINNER22-SEC v1 -->"
SEC_CONTENT = """
<!-- BEGINNER22-SEC v1 -->
<!-- ── TOPIC: IDS/IPS & NETWORK DETECTION ────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">🚨</span>
    <span class="topic-name">IDS/IPS &amp; Detection — Catching Attacks on the Wire</span>
    <span class="topic-badge">SEC • Essential</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">IDS VS IPS</div>
      <div class="concept-title">Detect vs Prevent</div>
      <div class="concept-desc">An <strong>IDS</strong> (Intrusion Detection System) watches traffic and <em>alerts</em> on suspicious activity — it's a smoke detector. An <strong>IPS</strong> (Intrusion Prevention System) sits inline and can <em>block</em> the traffic — a sprinkler system. The tradeoff: an IPS can stop attacks in real time, but a false positive can block legitimate traffic.</div>
      <table class="ai-table">
        <thead><tr><th>Aspect</th><th>IDS</th><th>IPS</th></tr></thead>
        <tbody>
          <tr><td>Placement</td><td>Out-of-band (sees a copy of traffic)</td><td>Inline (traffic flows through it)</td></tr>
          <tr><td>Action</td><td>Alerts only</td><td>Alerts AND blocks/drops</td></tr>
          <tr><td>Risk of false positive</td><td>Annoying alert</td><td>Blocks real traffic (outage)</td></tr>
          <tr><td>Tools</td><td>Snort, Suricata, Zeek</td><td>Snort/Suricata (inline mode)</td></tr>
        </tbody>
      </table>
    </div>
    <div class="concept-card">
      <div class="concept-label">DETECTION METHODS</div>
      <div class="concept-title">Signature vs Anomaly vs Behavior</div>
      <table class="ai-table">
        <thead><tr><th>Method</th><th>How It Works</th><th>Strength / Weakness</th></tr></thead>
        <tbody>
          <tr><td>Signature-based</td><td>Match known attack patterns/rules</td><td>+ Accurate for known threats; − misses novel attacks</td></tr>
          <tr><td>Anomaly-based</td><td>Flag deviations from a learned baseline</td><td>+ Catches unknowns; − more false positives</td></tr>
          <tr><td>Behavior-based</td><td>Detect malicious sequences of actions</td><td>+ Catches TTPs; − needs tuning</td></tr>
        </tbody>
      </table>
      <div class="code-block"><span class="com"># A simple Suricata/Snort rule (signature)</span>
alert tcp any any -&gt; any 80 (msg:"Possible SQLi";
  content:"UNION SELECT"; nocase; sid:1000001;)
<span class="com"># Triggers an alert when "UNION SELECT" appears in HTTP traffic</span></div>
    </div>
    <div class="concept-card">
      <div class="concept-label">FALSE POSITIVES & TUNING</div>
      <div class="concept-title">The Analyst's Daily Reality</div>
      <div class="concept-desc">The hardest part of detection isn't getting alerts — it's getting <em>useful</em> alerts. Too many false positives cause "alert fatigue," where analysts start ignoring everything (and miss the real one). Tuning — adjusting rules to your environment, suppressing known-good noise — is a continuous, high-value job. The goal: high signal, low noise.</div>
      <table class="ai-table">
        <thead><tr><th>Term</th><th>Meaning</th></tr></thead>
        <tbody>
          <tr><td>True Positive</td><td>Alert fired, was a real attack ✓</td></tr>
          <tr><td>False Positive</td><td>Alert fired, was benign (noise)</td></tr>
          <tr><td>True Negative</td><td>No alert, nothing happened ✓</td></tr>
          <tr><td>False Negative</td><td>No alert, but there WAS an attack (the scary one)</td></tr>
        </tbody>
      </table>
    </div>
    <div class="concept-card">
      <div class="concept-label">DECEPTION TECHNOLOGY</div>
      <div class="concept-title">Honeypots — Let Them Attack a Trap</div>
      <div class="concept-desc">A <strong>honeypot</strong> is a decoy system designed to be attacked. Since no legitimate user should ever touch it, <em>any</em> interaction is suspicious — making honeypots an extremely low-false-positive detection method. They also reveal attacker tools and techniques. Related: <strong>honeytokens</strong> (fake credentials/files that alert when used) and <strong>honeynets</strong> (whole decoy networks).</div>
      <table class="ai-table">
        <thead><tr><th>Type</th><th>Description</th></tr></thead>
        <tbody>
          <tr><td>Low-interaction</td><td>Emulates a few services; safe, limited intel</td></tr>
          <tr><td>High-interaction</td><td>Real systems; rich intel but risky to run</td></tr>
          <tr><td>Honeytoken</td><td>Fake API key/document/AD account that triggers an alert when touched</td></tr>
          <tr><td>Canary</td><td>A tripwire (e.g., a file or DNS token) signaling a breach</td></tr>
        </tbody>
      </table>
    </div>
  </div>
</div>
"""

# ─────────────────────────────── OPS wave 22 ─────────────────────────────────
OPS_SENTINEL = "<!-- BEGINNER22-OPS v1 -->"
OPS_CONTENT = """
<!-- BEGINNER22-OPS v1 -->
<!-- ── TOPIC: OBSERVABILITY IN PRACTICE ──────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">🔭</span>
    <span class="topic-name">Observability — Knowing What Your Systems Are Doing</span>
    <span class="topic-badge">OPS • Modern</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">MONITORING VS OBSERVABILITY</div>
      <div class="concept-title">Known Unknowns vs Unknown Unknowns</div>
      <div class="concept-desc"><strong>Monitoring</strong> answers questions you already know to ask ("is CPU high?"). <strong>Observability</strong> lets you ask <em>new</em> questions about your system's behavior without shipping new code — crucial for debugging novel failures in complex distributed systems. Monitoring tells you something is wrong; observability helps you figure out <em>why</em>.</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">THE THREE PILLARS</div>
      <div class="concept-title">Metrics, Logs, Traces</div>
      <table class="ai-table">
        <thead><tr><th>Pillar</th><th>What It Is</th><th>Answers</th><th>Tools</th></tr></thead>
        <tbody>
          <tr><td>Metrics</td><td>Numeric time-series (CPU, req/s, error rate)</td><td>"What is happening?" (trends, alerts)</td><td>Prometheus, Grafana</td></tr>
          <tr><td>Logs</td><td>Timestamped event records</td><td>"What happened exactly?" (details)</td><td>Loki, ELK, Splunk</td></tr>
          <tr><td>Traces</td><td>Request's full journey across services</td><td>"Where is the slowness?" (latency per hop)</td><td>Jaeger, Tempo, OpenTelemetry</td></tr>
        </tbody>
      </table>
    </div>
    <div class="concept-card">
      <div class="concept-label">THE FOUR GOLDEN SIGNALS</div>
      <div class="concept-title">What to Watch for Any Service (Google SRE)</div>
      <table class="ai-table">
        <thead><tr><th>Signal</th><th>Meaning</th></tr></thead>
        <tbody>
          <tr><td>Latency</td><td>How long requests take (watch the slow tail: p95, p99)</td></tr>
          <tr><td>Traffic</td><td>How much demand (requests/sec)</td></tr>
          <tr><td>Errors</td><td>Rate of failed requests</td></tr>
          <tr><td>Saturation</td><td>How "full" the system is (the constrained resource)</td></tr>
        </tbody>
      </table>
      <div class="concept-desc"><strong>Alert on symptoms, not causes.</strong> Page someone for "users are getting errors" (a symptom they care about), not "CPU is 80%" (which may be totally fine). This keeps alerts meaningful and reduces fatigue.</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">GITOPS</div>
      <div class="concept-title">Git as the Single Source of Truth</div>
      <div class="concept-desc">GitOps applies software-development practices to operations: the desired state of your infrastructure and apps lives in a Git repo, and an automated agent continuously makes reality match the repo. Want to change production? Open a pull request. This gives you review, audit history, easy rollback (just revert the commit), and no manual <code>kubectl</code> drift.</div>
      <table class="ai-table">
        <thead><tr><th>Principle</th><th>Benefit</th></tr></thead>
        <tbody>
          <tr><td>Declarative state in Git</td><td>The repo IS the documentation of what's deployed</td></tr>
          <tr><td>Changes via pull request</td><td>Review + approval + audit trail for every change</td></tr>
          <tr><td>Automated reconciliation</td><td>Agent (Argo CD, Flux) keeps cluster matching Git</td></tr>
          <tr><td>Rollback = git revert</td><td>Undo a bad deploy by reverting the commit</td></tr>
        </tbody>
      </table>
    </div>
  </div>
</div>
"""

# ─────────────────────────────── LIFESTYLE wave 22 ───────────────────────────
LIFE_SENTINEL = "<!-- BEGINNER22-LIFE v1 -->"
LIFE_CONTENT = """
<!-- BEGINNER22-LIFE v1 -->
<!-- ── TOPIC: SURVIVING ON-CALL ──────────────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">📟</span>
    <span class="topic-name">Surviving On-Call — When the Pager Owns Your Night</span>
    <span class="topic-badge">LIFESTYLE • Sustainability</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">THE REALITY</div>
      <div class="concept-title">On-Call Is Part of Most IT/Ops Jobs</div>
      <div class="concept-desc">Being "on-call" means you're responsible for responding to incidents outside business hours. It's a normal part of ops, SRE, and many IT roles — and it can be stressful, especially early on. The good news: most of the stress comes from being unprepared, and that's fixable. A well-run on-call rotation is sustainable; a badly-run one burns people out fast.</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">BE PREPARED</div>
      <div class="concept-title">Reduce the 3am Panic</div>
      <table class="ai-table">
        <thead><tr><th>Before Your Shift</th><th>Why</th></tr></thead>
        <tbody>
          <tr><td>Test your access &amp; tools</td><td>Don't discover your VPN is broken during an incident</td></tr>
          <tr><td>Read recent incidents/changes</td><td>Know what's fragile right now</td></tr>
          <tr><td>Know the runbooks</td><td>A clear runbook turns panic into a checklist</td></tr>
          <tr><td>Know the escalation path</td><td>Who to call when you're stuck — it's OK to escalate</td></tr>
          <tr><td>Set up your environment</td><td>Charged phone, laptop ready, alerts working</td></tr>
        </tbody>
      </table>
    </div>
    <div class="concept-card">
      <div class="concept-label">DURING AN INCIDENT</div>
      <div class="concept-title">Stay Calm, Work the Process</div>
      <div class="concept-desc">When the page fires, panic is the enemy. A structured approach keeps you effective under pressure (this is the OODA loop and incident command in action).</div>
      <table class="ai-table">
        <thead><tr><th>Step</th><th>Action</th></tr></thead>
        <tbody>
          <tr><td>1. Acknowledge</td><td>Ack the page so others know it's being handled</td></tr>
          <tr><td>2. Assess</td><td>What's the actual impact? How bad, how many users?</td></tr>
          <tr><td>3. Stabilize first</td><td>Restore service (even a workaround) before root-causing</td></tr>
          <tr><td>4. Communicate</td><td>Post status updates — silence makes everyone anxious</td></tr>
          <tr><td>5. Escalate if stuck</td><td>Don't be a hero — pull in help early, not at hour 3</td></tr>
          <tr><td>6. Post-mortem later</td><td>Blameless review once it's resolved (not at 3am)</td></tr>
        </tbody>
      </table>
    </div>
    <div class="concept-card">
      <div class="concept-label">PROTECT YOURSELF</div>
      <div class="concept-title">Sustainable On-Call Habits</div>
      <div class="concept-desc">On-call should not destroy your life. If it consistently does, that's an organizational problem worth raising (politely, with data). Healthy practices: take comp time after rough nights, push to fix the root causes of repeat pages (toil reduction), ensure rotations are large enough that nobody is always on, and use the "follow-the-sun" model across time zones where possible. <strong>Recall "not my circus, not my monkeys":</strong> respond to what's genuinely yours, escalate what isn't, and don't absorb the consequences of problems you flagged but couldn't control. An alert that pages you every night for something you can't fix is a process failure to escalate — not a personal burden to silently carry.</div>
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
        (SEC_INJECT_ANCHOR,    SEC_SENTINEL,    SEC_CONTENT),
        (OPS_INJECT_ANCHOR,    OPS_SENTINEL,    OPS_CONTENT),
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
