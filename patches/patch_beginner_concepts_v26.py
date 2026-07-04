#!/usr/bin/env python3
"""
patch_beginner_concepts_v26.py — Wave 26: Data validation (Pydantic), malware
analysis basics, robust bash scripting, privacy regulations, intermediate Vim.

New sentinels:
  BEGINNER26-SCRIPT v1   — Data validation with Pydantic, JSON schema, parsing untrusted input
  BEGINNER26-THREAT v1   — Malware analysis basics (static/dynamic/sandboxing)
  BEGINNER26-LINUX v1    — Robust bash scripting (set -euo pipefail, arrays, traps)
  BEGINNER26-GRC v1      — Privacy regulations (GDPR/CCPA), data subject rights
  BEGINNER26-SHORTCUT v1 — Intermediate Vim: the editing language (motions + operators)
"""
from pathlib import Path

SCRIPT_INJECT_ANCHOR   = "<!-- /domain-body script -->"
THREAT_INJECT_ANCHOR   = "<!-- /domain-body threat -->"
LINUX_INJECT_ANCHOR    = "<!-- /domain-body linux -->"
GRC_INJECT_ANCHOR      = "<!-- /domain-body grc -->"
SHORTCUT_INJECT_ANCHOR = "<!-- /domain-body shortcuts -->"

# ─────────────────────────────── SCRIPT wave 26 ──────────────────────────────
SCRIPT_SENTINEL = "<!-- BEGINNER26-SCRIPT v1 -->"
SCRIPT_CONTENT = """
<!-- BEGINNER26-SCRIPT v1 -->
<!-- ── TOPIC: DATA VALIDATION ────────────────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">✅</span>
    <span class="topic-name">Data Validation — Never Trust Input</span>
    <span class="topic-badge">SCRIPT • Essential</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">THE GOLDEN RULE</div>
      <div class="concept-title">All Input Is Guilty Until Proven Innocent</div>
      <div class="concept-desc">Data from users, APIs, files, and networks is untrusted — it may be malformed, malicious, or just wrong. Validating it at the boundary (before it enters your logic) prevents both bugs and security holes (injection, crashes, corrupted data). The principle: <strong>parse, don't just check</strong> — convert raw input into trusted, typed objects at the edge, so the rest of your code can assume the data is clean.</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">PYDANTIC</div>
      <div class="concept-title">Validation via Type Hints</div>
      <div class="concept-desc">Pydantic is the most popular Python validation library (and the engine behind FastAPI). You declare the shape of your data with types; Pydantic validates, coerces, and gives clear errors — turning messy input into trusted objects.</div>
      <div class="code-block"><span class="com"># pip install pydantic</span>
<span class="kw">from</span> pydantic <span class="kw">import</span> BaseModel, EmailStr, Field, field_validator

<span class="kw">class</span> <span class="fn">User</span>(BaseModel):
    name: str = Field(min_length=<span class="num">1</span>, max_length=<span class="num">100</span>)
    age: <span class="fn">int</span> = Field(ge=<span class="num">0</span>, le=<span class="num">150</span>)      <span class="com"># 0 ≤ age ≤ 150</span>
    email: EmailStr                          <span class="com"># validated email format</span>
    role: str = <span class="str">"user"</span>                      <span class="com"># default</span>

    <span class="fn">@field_validator</span>(<span class="str">"name"</span>)
    <span class="fn">@classmethod</span>
    <span class="kw">def</span> <span class="fn">no_digits</span>(cls, v):
        <span class="kw">if</span> <span class="fn">any</span>(c.isdigit() <span class="kw">for</span> c <span class="kw">in</span> v):
            <span class="kw">raise</span> ValueError(<span class="str">"name cannot contain digits"</span>)
        <span class="kw">return</span> v

<span class="com"># Valid input → trusted object (note: "30" coerced to int 30)</span>
u = User(name=<span class="str">"Alice"</span>, age=<span class="str">"30"</span>, email=<span class="str">"a@example.com"</span>)
<span class="fn">print</span>(u.age)            <span class="com"># 30 (an int)</span>

<span class="com"># Invalid input → clear, structured error</span>
<span class="kw">try</span>:
    User(name=<span class="str">"Bob3"</span>, age=<span class="num">-5</span>, email=<span class="str">"not-an-email"</span>)
<span class="kw">except</span> Exception <span class="kw">as</span> e:
    <span class="fn">print</span>(e)             <span class="com"># lists every validation failure</span></div>
    </div>
    <div class="concept-card">
      <div class="concept-label">VALIDATION PRINCIPLES</div>
      <div class="concept-title">Rules That Apply Everywhere</div>
      <table class="ai-table">
        <thead><tr><th>Principle</th><th>Meaning</th></tr></thead>
        <tbody>
          <tr><td>Allowlist &gt; denylist</td><td>Define what's ALLOWED, not what's banned (you'll always miss a bad case)</td></tr>
          <tr><td>Validate at the boundary</td><td>Clean data once at entry; trust it internally</td></tr>
          <tr><td>Fail closed</td><td>If validation fails, reject — don't "best effort" process garbage</td></tr>
          <tr><td>Validate type, range, format, AND length</td><td>"It's an int" isn't enough — is it in a sane range?</td></tr>
          <tr><td>Sanitize for the destination</td><td>Escape for SQL/HTML/shell where the data is USED</td></tr>
          <tr><td>Don't trust client-side validation</td><td>JS checks are UX, not security — always re-validate server-side</td></tr>
        </tbody>
      </table>
    </div>
  </div>
</div>
"""

# ─────────────────────────────── THREAT wave 26 ──────────────────────────────
THREAT_SENTINEL = "<!-- BEGINNER26-THREAT v1 -->"
THREAT_CONTENT = """
<!-- BEGINNER26-THREAT v1 -->
<!-- ── TOPIC: MALWARE ANALYSIS BASICS ────────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">🔬</span>
    <span class="topic-name">Malware Analysis — Understanding What the Bad Code Does</span>
    <span class="topic-badge">THREAT • Investigation</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">⚠️ SAFETY FIRST</div>
      <div class="concept-title">Analyze Only in an Isolated Lab</div>
      <div class="concept-desc">Live malware can spread, exfiltrate, or destroy. Analyze it only in an isolated environment: an air-gapped or snapshot-able VM, no shared folders, no network (or a controlled fake network). Never run a sample on your real machine or corporate network. Take a VM snapshot before, revert after.</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">STATIC VS DYNAMIC</div>
      <div class="concept-title">Two Complementary Approaches</div>
      <table class="ai-table">
        <thead><tr><th>Approach</th><th>What It Is</th><th>Risk</th><th>Reveals</th></tr></thead>
        <tbody>
          <tr><td>Static analysis</td><td>Examine the file WITHOUT running it</td><td>Low (not executed)</td><td>Strings, imports, structure, indicators</td></tr>
          <tr><td>Dynamic analysis</td><td>RUN it in a sandbox and observe behavior</td><td>Higher (it executes)</td><td>Actual network calls, file/registry changes, persistence</td></tr>
        </tbody>
      </table>
      <div class="concept-desc">Real analysts use both: static to form hypotheses safely, dynamic to confirm what it actually does. Advanced malware detects sandboxes and hides — so neither alone is complete.</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">STATIC ANALYSIS TOOLKIT</div>
      <div class="concept-title">First Look at a Sample</div>
      <div class="code-block"><span class="com"># Hash it (identify + look up reputation — never UPLOAD if sensitive)</span>
sha256sum sample.exe
<span class="com"># Check the hash on VirusTotal (hash lookup, not file upload)</span>

<span class="com"># Extract readable strings — URLs, IPs, commands often hide here</span>
strings -n 8 sample.exe | grep -iE "http|\\.exe|cmd|powershell"

<span class="com"># File type and metadata</span>
file sample.exe

<span class="com"># PE analysis (Windows executables) — imports reveal capabilities</span>
<span class="com"># e.g., imports of WinHTTP = network; CryptEncrypt = ransomware?</span>
<span class="com"># Tools: PEStudio, pefile (Python), CFF Explorer</span>

<span class="com"># Detect packing/obfuscation (high entropy = likely packed)</span>
<span class="com"># Tools: DIE (Detect It Easy)</span></div>
    </div>
    <div class="concept-card">
      <div class="concept-label">DYNAMIC ANALYSIS</div>
      <div class="concept-title">Watch It Misbehave Safely</div>
      <table class="ai-table">
        <thead><tr><th>What to Watch</th><th>Tool / Method</th></tr></thead>
        <tbody>
          <tr><td>Processes spawned</td><td>Process Monitor / Process Explorer (Windows)</td></tr>
          <tr><td>File &amp; registry changes</td><td>Procmon, Regshot (before/after diff)</td></tr>
          <tr><td>Network connections (C2)</td><td>Wireshark, fakedns, INetSim (fake internet)</td></tr>
          <tr><td>Persistence mechanisms</td><td>Autoruns — what it set to survive reboot</td></tr>
          <tr><td>Automated sandbox</td><td>Cuckoo, Any.Run, Joe Sandbox — full report</td></tr>
        </tbody>
      </table>
      <div class="concept-desc">The goal is to extract <strong>IOCs</strong> (Indicators of Compromise) — hashes, C2 domains/IPs, file paths, registry keys — that you can then hunt for across your environment to find other infected hosts.</div>
    </div>
  </div>
</div>
"""

# ─────────────────────────────── LINUX wave 26 ───────────────────────────────
LINUX_SENTINEL = "<!-- BEGINNER26-LINUX v1 -->"
LINUX_CONTENT = """
<!-- BEGINNER26-LINUX v1 -->
<!-- ── TOPIC: ROBUST BASH SCRIPTING ──────────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">🐚</span>
    <span class="topic-name">Robust Bash — Scripts That Don't Silently Destroy Things</span>
    <span class="topic-badge">LINUX • Advanced</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">THE UNSAFE DEFAULT</div>
      <div class="concept-title">Bash Keeps Going After Errors</div>
      <div class="concept-desc">By default, a bash script continues after a command fails — which can be catastrophic (imagine <code>cd /backup; rm -rf *</code> where the <code>cd</code> silently failed). The first thing every serious bash script should do is enable strict mode. This one line prevents a huge class of disasters.</div>
      <div class="code-block"><span class="com">#!/usr/bin/env bash</span>
<span class="kw">set</span> -euo pipefail
<span class="com"># -e  : exit immediately if any command fails</span>
<span class="com"># -u  : error on use of undefined variables (catches typos!)</span>
<span class="com"># -o pipefail : a pipeline fails if ANY part fails (not just the last)</span>

IFS=$'\\n\\t'   <span class="com"># safer word-splitting (avoid spaces breaking loops)</span></div>
    </div>
    <div class="concept-card">
      <div class="concept-label">QUOTING & VARIABLES</div>
      <div class="concept-title">The #1 Source of Bash Bugs</div>
      <div class="code-block"><span class="com"># ALWAYS quote variable expansions — unquoted breaks on spaces</span>
file=<span class="str">"my report.txt"</span>
rm $file              <span class="com"># ✗ tries to rm "my" AND "report.txt"!</span>
rm <span class="str">"$file"</span>            <span class="com"># ✓ correct</span>

<span class="com"># Default values and required checks</span>
name=<span class="str">"${1:-world}"</span>      <span class="com"># use $1, or "world" if unset</span>
: <span class="str">"${API_KEY:?API_KEY must be set}"</span>   <span class="com"># abort if unset</span>

<span class="com"># Command substitution — prefer $() over backticks</span>
count=$(grep -c ERROR app.log)
today=$(date +%F)

<span class="com"># Arithmetic</span>
<span class="kw">if</span> (( count &gt; 10 )); <span class="kw">then</span> <span class="kw">echo</span> <span class="str">"too many"</span>; <span class="kw">fi</span></div>
    </div>
    <div class="concept-card">
      <div class="concept-label">ARRAYS & LOOPS</div>
      <div class="concept-title">Handling Lists Safely</div>
      <div class="code-block"><span class="com"># Arrays</span>
servers=(<span class="str">"web1"</span> <span class="str">"web2"</span> <span class="str">"db1"</span>)
<span class="kw">echo</span> <span class="str">"${servers[0]}"</span>       <span class="com"># web1</span>
<span class="kw">echo</span> <span class="str">"${#servers[@]}"</span>      <span class="com"># length: 3</span>

<span class="com"># Loop over array — quote "${arr[@]}" !</span>
<span class="kw">for</span> s <span class="kw">in</span> <span class="str">"${servers[@]}"</span>; <span class="kw">do</span>
    <span class="kw">echo</span> <span class="str">"Checking $s"</span>
<span class="kw">done</span>

<span class="com"># Loop over files SAFELY (handles spaces/newlines)</span>
<span class="kw">while</span> IFS= <span class="kw">read</span> -r -d <span class="str">''</span> f; <span class="kw">do</span>
    <span class="kw">echo</span> <span class="str">"Found: $f"</span>
<span class="kw">done</span> &lt; &lt;(find . -name <span class="str">"*.log"</span> -print0)</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">CLEANUP & FUNCTIONS</div>
      <div class="concept-title">Traps and Reusable Code</div>
      <div class="code-block"><span class="com"># trap — run cleanup on exit (even on error/Ctrl-C)</span>
tmpdir=$(mktemp -d)
cleanup() { rm -rf <span class="str">"$tmpdir"</span>; }
<span class="kw">trap</span> cleanup EXIT       <span class="com"># guaranteed cleanup, no leftover temp files</span>

<span class="com"># Functions with local variables</span>
log() {
    <span class="kw">local</span> level=<span class="str">"$1"</span>; <span class="kw">shift</span>
    <span class="kw">echo</span> <span class="str">"[$(date +%T)] $level: $*"</span> &gt;&amp;2
}
log INFO <span class="str">"Starting backup"</span>
log ERROR <span class="str">"Disk full"</span></div>
      <div class="concept-desc"><strong>Lint your scripts with <code>shellcheck</code></strong> — it catches quoting bugs, unsafe patterns, and common mistakes automatically. Run it on every script; it will make you a dramatically better bash author.</div>
    </div>
  </div>
</div>
"""

# ─────────────────────────────── GRC wave 26 ─────────────────────────────────
GRC_SENTINEL = "<!-- BEGINNER26-GRC v1 -->"
GRC_CONTENT = """
<!-- BEGINNER26-GRC v1 -->
<!-- ── TOPIC: PRIVACY REGULATIONS ────────────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">🔏</span>
    <span class="topic-name">Privacy Regulations — GDPR, CCPA &amp; Data Rights</span>
    <span class="topic-badge">GRC • Compliance</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">WHY PRIVACY LAW MATTERS TO IT</div>
      <div class="concept-title">Data Privacy Is Now Everyone's Job</div>
      <div class="concept-desc">Privacy laws give individuals rights over their personal data and impose serious obligations (and fines) on organizations that handle it. GDPR fines can reach 4% of global annual revenue. As an IT/security professional, you implement the technical controls that make compliance possible — encryption, access controls, data deletion, breach detection. You don't need to be a lawyer, but you must understand the core concepts.</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">THE BIG LAWS</div>
      <div class="concept-title">A Quick Comparison</div>
      <table class="ai-table">
        <thead><tr><th>Law</th><th>Region</th><th>Covers</th><th>Notable</th></tr></thead>
        <tbody>
          <tr><td>GDPR</td><td>EU / EEA</td><td>Personal data of EU residents</td><td>The global benchmark; extraterritorial; huge fines</td></tr>
          <tr><td>CCPA / CPRA</td><td>California</td><td>CA consumers' personal info</td><td>Right to know, delete, opt-out of sale</td></tr>
          <tr><td>HIPAA</td><td>USA</td><td>Health information (PHI)</td><td>Healthcare-specific</td></tr>
          <tr><td>PIPEDA</td><td>Canada</td><td>Personal data (commercial)</td><td>Consent-focused</td></tr>
          <tr><td>LGPD</td><td>Brazil</td><td>Personal data</td><td>GDPR-inspired</td></tr>
        </tbody>
      </table>
    </div>
    <div class="concept-card">
      <div class="concept-label">DATA SUBJECT RIGHTS</div>
      <div class="concept-title">What Individuals Can Demand (GDPR)</div>
      <table class="ai-table">
        <thead><tr><th>Right</th><th>Meaning</th><th>IT Implication</th></tr></thead>
        <tbody>
          <tr><td>Access</td><td>"Show me the data you hold on me"</td><td>Must be able to find all of a person's data</td></tr>
          <tr><td>Rectification</td><td>"Correct my wrong data"</td><td>Editable, traceable records</td></tr>
          <tr><td>Erasure ("right to be forgotten")</td><td>"Delete my data"</td><td>Must delete across systems + backups</td></tr>
          <tr><td>Portability</td><td>"Give me my data to take elsewhere"</td><td>Export in machine-readable format</td></tr>
          <tr><td>Object / restrict</td><td>"Stop processing my data"</td><td>Flag/exclude from processing</td></tr>
        </tbody>
      </table>
    </div>
    <div class="concept-card">
      <div class="concept-label">CORE PRINCIPLES</div>
      <div class="concept-title">Privacy by Design</div>
      <table class="ai-table">
        <thead><tr><th>Principle</th><th>What It Means</th></tr></thead>
        <tbody>
          <tr><td>Lawful basis</td><td>Have a legal reason to process (consent, contract, etc.)</td></tr>
          <tr><td>Data minimization</td><td>Collect only what you actually need</td></tr>
          <tr><td>Purpose limitation</td><td>Use data only for the stated purpose</td></tr>
          <tr><td>Storage limitation</td><td>Don't keep data longer than necessary</td></tr>
          <tr><td>Privacy by design &amp; default</td><td>Build privacy in from the start, not bolted on</td></tr>
          <tr><td>Breach notification</td><td>GDPR: report breaches within 72 hours</td></tr>
        </tbody>
      </table>
      <div class="concept-desc"><strong>Key distinction:</strong> a <em>data controller</em> decides why/how data is processed; a <em>data processor</em> processes it on the controller's behalf (e.g., a cloud vendor). Both have obligations — and contracts (DPAs) define them.</div>
    </div>
  </div>
</div>
"""

# ─────────────────────────────── SHORTCUT wave 26 ────────────────────────────
SHORTCUT_SENTINEL = "<!-- BEGINNER26-SHORTCUT v1 -->"
SHORTCUT_CONTENT = """
<!-- BEGINNER26-SHORTCUT v1 -->
<!-- ── TOPIC: INTERMEDIATE VIM ───────────────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">⌨️</span>
    <span class="topic-name">Intermediate Vim — Editing as a Language</span>
    <span class="topic-badge">SHORTCUTS • Power User</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">THE BIG IDEA</div>
      <div class="concept-title">Vim Is a Language: Verb + Motion</div>
      <div class="concept-desc">Vim's power isn't memorizing hundreds of commands — it's that commands <em>compose</em> like a language. You combine a <strong>verb</strong> (operator: what to do) with a <strong>motion</strong> (where). Learn a handful of each and you can express thousands of edits. <code>d</code> (delete) + <code>w</code> (word) = <code>dw</code> "delete word." Once it clicks, editing becomes thought-speed.</div>
      <div class="code-block"><span class="com"># GRAMMAR:  [count] operator motion</span>
dw      <span class="com"># delete word</span>
d3w     <span class="com"># delete 3 words</span>
c$      <span class="com"># change to end of line</span>
y}      <span class="com"># yank (copy) to next blank line</span>
&gt;i{     <span class="com"># indent inside { } block</span>
=G      <span class="com"># auto-indent to end of file</span></div>
    </div>
    <div class="concept-card">
      <div class="concept-label">OPERATORS (VERBS)</div>
      <div class="concept-title">What to Do</div>
      <table class="ai-table">
        <thead><tr><th>Operator</th><th>Action</th></tr></thead>
        <tbody>
          <tr><td><code>d</code></td><td>Delete (cut)</td></tr>
          <tr><td><code>c</code></td><td>Change (delete + enter insert mode)</td></tr>
          <tr><td><code>y</code></td><td>Yank (copy)</td></tr>
          <tr><td><code>&gt;</code> / <code>&lt;</code></td><td>Indent / dedent</td></tr>
          <tr><td><code>=</code></td><td>Auto-format/indent</td></tr>
          <tr><td><code>gu</code> / <code>gU</code></td><td>Lowercase / uppercase</td></tr>
        </tbody>
      </table>
    </div>
    <div class="concept-card">
      <div class="concept-label">MOTIONS & TEXT OBJECTS</div>
      <div class="concept-title">Where to Act</div>
      <table class="ai-table">
        <thead><tr><th>Motion</th><th>Moves / Selects</th></tr></thead>
        <tbody>
          <tr><td><code>w</code> / <code>b</code> / <code>e</code></td><td>Word forward / back / end</td></tr>
          <tr><td><code>0</code> / <code>$</code></td><td>Start / end of line</td></tr>
          <tr><td><code>gg</code> / <code>G</code></td><td>Top / bottom of file</td></tr>
          <tr><td><code>f{char}</code> / <code>t{char}</code></td><td>Jump to / before next char</td></tr>
          <tr><td><code>%</code></td><td>Matching bracket</td></tr>
          <tr><td><code>iw</code> / <code>aw</code></td><td>Text object: inner / a word</td></tr>
          <tr><td><code>i"</code> / <code>i(</code> / <code>i{</code></td><td>Inside quotes / parens / braces</td></tr>
          <tr><td><code>it</code> / <code>ip</code></td><td>Inside tag / paragraph</td></tr>
        </tbody>
      </table>
      <div class="concept-desc"><strong>Text objects are the superpower:</strong> <code>ci"</code> = "change inside quotes" (deletes text between quotes, drops you in insert mode) — works no matter where your cursor is in the string. <code>di(</code> = delete inside parens. <code>dit</code> = delete inside HTML tag. These feel magical once learned.</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">HIGH-VALUE COMMANDS</div>
      <div class="concept-title">Things That Save Real Time</div>
      <div class="code-block">.            <span class="com"># REPEAT last change (incredibly powerful)</span>
ciw          <span class="com"># change inner word, then . to repeat on others</span>
*            <span class="com"># search for word under cursor</span>
ggVG         <span class="com"># select entire file (gg, Visual, G)</span>
:%s/old/new/g    <span class="com"># replace all "old" with "new" in file</span>
:%s/old/new/gc   <span class="com"># ...with confirmation each time</span>
u  /  Ctrl-r <span class="com"># undo / redo</span>
A            <span class="com"># jump to end of line + insert</span>
o  /  O      <span class="com"># open new line below / above</span>
&gt;G           <span class="com"># indent from cursor to end of file</span>
Ctrl-v       <span class="com"># VISUAL BLOCK — edit columns (great for tables)</span></div>
      <div class="concept-desc"><strong>The <code>.</code> command</strong> repeats your last change — pair it with a motion-based edit and you can fix dozens of spots with single keystrokes. Mastering "edit once, repeat with <code>.</code>" is the hallmark of a fluent Vim user.</div>
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
        (SCRIPT_INJECT_ANCHOR,   SCRIPT_SENTINEL,   SCRIPT_CONTENT),
        (THREAT_INJECT_ANCHOR,   THREAT_SENTINEL,   THREAT_CONTENT),
        (LINUX_INJECT_ANCHOR,    LINUX_SENTINEL,    LINUX_CONTENT),
        (GRC_INJECT_ANCHOR,      GRC_SENTINEL,      GRC_CONTENT),
        (SHORTCUT_INJECT_ANCHOR, SHORTCUT_SENTINEL, SHORTCUT_CONTENT),
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
