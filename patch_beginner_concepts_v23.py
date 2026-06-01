#!/usr/bin/env python3
"""
patch_beginner_concepts_v23.py — Wave 23: SOLID & design patterns, privilege
escalation, Linux storage (LVM/RAID), audit process, CLI text processing.

New sentinels:
  BEGINNER23-SCRIPT v1   — SOLID principles, common design patterns
  BEGINNER23-PENTEST v1  — Privilege escalation & enumeration (authorized labs)
  BEGINNER23-LINUX v1    — Storage management: mounting, LVM, RAID, fstab
  BEGINNER23-GRC v1      — The audit process, evidence, control testing
  BEGINNER23-SHORTCUT v1 — CLI text-processing mastery (grep/find/cut/sort combos)
"""
from pathlib import Path

SCRIPT_INJECT_ANCHOR   = "<!-- /domain-body script -->"
PENTEST_INJECT_ANCHOR  = "<!-- /domain-body pentest -->"
LINUX_INJECT_ANCHOR    = "<!-- /domain-body linux -->"
GRC_INJECT_ANCHOR      = "<!-- /domain-body grc -->"
SHORTCUT_INJECT_ANCHOR = "<!-- /domain-body shortcuts -->"

# ─────────────────────────────── SCRIPT wave 23 ──────────────────────────────
SCRIPT_SENTINEL = "<!-- BEGINNER23-SCRIPT v1 -->"
SCRIPT_CONTENT = """
<!-- BEGINNER23-SCRIPT v1 -->
<!-- ── TOPIC: SOLID PRINCIPLES ───────────────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">🧱</span>
    <span class="topic-name">SOLID Principles — Writing Code That Survives Change</span>
    <span class="topic-badge">SCRIPT • Design</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">WHY DESIGN PRINCIPLES</div>
      <div class="concept-title">Code Is Read and Changed Far More Than Written</div>
      <div class="concept-desc">A program is rarely "done" — requirements change, bugs are fixed, features added. SOLID is five principles (coined by Robert C. Martin) for structuring code so it's easier to understand, extend, and change without breaking everything. You don't need to memorize them as dogma, but understanding the ideas dramatically improves your code as you move past beginner scripts.</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">THE FIVE PRINCIPLES</div>
      <div class="concept-title">S - O - L - I - D</div>
      <table class="ai-table">
        <thead><tr><th>Letter</th><th>Principle</th><th>Plain English</th></tr></thead>
        <tbody>
          <tr><td><strong>S</strong></td><td>Single Responsibility</td><td>A class/function should do ONE thing. One reason to change.</td></tr>
          <tr><td><strong>O</strong></td><td>Open/Closed</td><td>Open to extension, closed to modification — add behavior without editing existing code.</td></tr>
          <tr><td><strong>L</strong></td><td>Liskov Substitution</td><td>A subclass should work anywhere its parent is expected, without surprises.</td></tr>
          <tr><td><strong>I</strong></td><td>Interface Segregation</td><td>Many small, focused interfaces beat one giant one. Don't force clients to depend on methods they don't use.</td></tr>
          <tr><td><strong>D</strong></td><td>Dependency Inversion</td><td>Depend on abstractions, not concrete implementations. Inject dependencies.</td></tr>
        </tbody>
      </table>
    </div>
    <div class="concept-card">
      <div class="concept-label">SRP IN ACTION</div>
      <div class="concept-title">Single Responsibility — Before &amp; After</div>
      <div class="code-block"><span class="com"># BAD — one class does everything (hard to test/change)</span>
<span class="kw">class</span> <span class="fn">Report</span>:
    <span class="kw">def</span> <span class="fn">fetch_data</span>(self): ...      <span class="com"># talks to DB</span>
    <span class="kw">def</span> <span class="fn">format_html</span>(self): ...     <span class="com"># formatting</span>
    <span class="kw">def</span> <span class="fn">send_email</span>(self): ...      <span class="com"># email/network</span>
<span class="com"># Three reasons to change → fragile</span>

<span class="com"># GOOD — each class has one job</span>
<span class="kw">class</span> <span class="fn">ReportRepository</span>:     <span class="kw">def</span> <span class="fn">fetch</span>(self): ...
<span class="kw">class</span> <span class="fn">ReportFormatter</span>:      <span class="kw">def</span> <span class="fn">to_html</span>(self, data): ...
<span class="kw">class</span> <span class="fn">EmailSender</span>:          <span class="kw">def</span> <span class="fn">send</span>(self, html): ...
<span class="com"># Each is independently testable and replaceable</span></div>
    </div>
    <div class="concept-card">
      <div class="concept-label">DEPENDENCY INVERSION</div>
      <div class="concept-title">Inject Dependencies — Don't Hardcode Them</div>
      <div class="code-block"><span class="com"># BAD — hardcoded dependency, impossible to test without a real DB</span>
<span class="kw">class</span> <span class="fn">UserService</span>:
    <span class="kw">def</span> <span class="fn">__init__</span>(self):
        self.db = PostgresDatabase()   <span class="com"># locked to Postgres</span>

<span class="com"># GOOD — depend on an abstraction, pass it in</span>
<span class="kw">class</span> <span class="fn">UserService</span>:
    <span class="kw">def</span> <span class="fn">__init__</span>(self, db):     <span class="com"># inject any DB-like object</span>
        self.db = db
<span class="com"># In tests, pass a fake DB. In prod, pass the real one.</span>
service = UserService(PostgresDatabase())
test    = UserService(FakeInMemoryDatabase())</div>
    </div>
  </div>
</div>

<!-- ── TOPIC: DESIGN PATTERNS ────────────────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">📐</span>
    <span class="topic-name">Design Patterns — Named Solutions to Common Problems</span>
    <span class="topic-badge">SCRIPT • Design</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">WHAT THEY ARE</div>
      <div class="concept-title">Reusable Vocabulary for Structuring Code</div>
      <div class="concept-desc">Design patterns are battle-tested, named solutions to recurring design problems. Knowing them gives you a shared vocabulary ("let's use a factory here") and saves you from reinventing structures. Don't force them in — but recognizing when one fits is a sign of growth. Here are the ones beginners meet most often.</div>
      <table class="ai-table">
        <thead><tr><th>Pattern</th><th>Solves</th><th>Example</th></tr></thead>
        <tbody>
          <tr><td>Factory</td><td>Creating objects without specifying exact class</td><td><code>get_parser("json")</code> returns the right parser</td></tr>
          <tr><td>Singleton</td><td>Exactly one instance shared everywhere</td><td>A single config or connection pool</td></tr>
          <tr><td>Strategy</td><td>Swap algorithms at runtime</td><td>Pluggable sorting/auth/compression methods</td></tr>
          <tr><td>Observer</td><td>Notify many objects when state changes</td><td>Event systems, pub/sub, callbacks</td></tr>
          <tr><td>Decorator</td><td>Add behavior without changing the object</td><td>Python's <code>@decorators</code>, middleware</td></tr>
          <tr><td>Adapter</td><td>Make incompatible interfaces work together</td><td>Wrapping a third-party API in your interface</td></tr>
        </tbody>
      </table>
    </div>
    <div class="concept-card">
      <div class="concept-label">STRATEGY EXAMPLE</div>
      <div class="concept-title">Swappable Behavior in Python</div>
      <div class="code-block"><span class="com"># Strategy: pass behavior as a function/object</span>
<span class="kw">def</span> <span class="fn">process</span>(data, transform):    <span class="com"># transform is the "strategy"</span>
    <span class="kw">return</span> [transform(x) <span class="kw">for</span> x <span class="kw">in</span> data]

process([<span class="num">1</span>, <span class="num">2</span>, <span class="num">3</span>], <span class="kw">lambda</span> x: x*<span class="num">2</span>)     <span class="com"># [2, 4, 6]</span>
process([<span class="num">1</span>, <span class="num">2</span>, <span class="num">3</span>], <span class="fn">str</span>)              <span class="com"># ['1', '2', '3']</span>

<span class="com"># Factory: centralize object creation</span>
<span class="kw">def</span> <span class="fn">get_notifier</span>(kind):
    <span class="kw">return</span> {
        <span class="str">"email"</span>: EmailNotifier,
        <span class="str">"slack"</span>: SlackNotifier,
        <span class="str">"sms"</span>:   SMSNotifier,
    }[kind]()

notifier = get_notifier(<span class="str">"slack"</span>)   <span class="com"># caller doesn't know the class</span>
notifier.send(<span class="str">"Deploy complete"</span>)</div>
      <div class="concept-desc"><strong>A warning:</strong> patterns are tools, not goals. Forcing patterns into simple code ("over-engineering") is as bad as having none. Reach for them when complexity actually demands it.</div>
    </div>
  </div>
</div>
"""

# ─────────────────────────────── PENTEST wave 23 ─────────────────────────────
PENTEST_SENTINEL = "<!-- BEGINNER23-PENTEST v1 -->"
PENTEST_CONTENT = """
<!-- BEGINNER23-PENTEST v1 -->
<!-- ── TOPIC: PRIVILEGE ESCALATION ───────────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">⬆️</span>
    <span class="topic-name">Privilege Escalation — From Foothold to Full Control</span>
    <span class="topic-badge">PENTEST • Authorized Only</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">⚠️ AUTHORIZED USE ONLY</div>
      <div class="concept-title">Your Lab, CTFs, or Written Engagements</div>
      <div class="concept-desc">Privilege escalation techniques are core to penetration testing and equally core to <em>defending</em> — knowing how attackers escalate tells you what to harden. Practice only on systems you own or are explicitly authorized to test (HTB, TryHackMe, your home lab).</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">THE CONCEPT</div>
      <div class="concept-title">Two Directions of Escalation</div>
      <div class="concept-desc">After getting initial access (a foothold), attackers rarely land with the privileges they want. Privilege escalation is the step of gaining higher access.</div>
      <table class="ai-table">
        <thead><tr><th>Type</th><th>Meaning</th><th>Example</th></tr></thead>
        <tbody>
          <tr><td>Vertical (privesc)</td><td>Gain HIGHER privileges</td><td>Standard user → root/admin</td></tr>
          <tr><td>Horizontal</td><td>Access ANOTHER user's resources at the same level</td><td>User A reads User B's files</td></tr>
        </tbody>
      </table>
    </div>
    <div class="concept-card">
      <div class="concept-label">ENUMERATION FIRST</div>
      <div class="concept-title">"Enumeration Is 90% of Privesc"</div>
      <div class="concept-desc">You can't escalate what you haven't found. Systematic enumeration of the system reveals the misconfiguration or vulnerability that lets you escalate. Automated scripts (run only in authorized labs) speed this up enormously.</div>
      <table class="ai-table">
        <thead><tr><th>Check</th><th>Linux</th><th>Windows</th></tr></thead>
        <tbody>
          <tr><td>Who am I / privileges</td><td><code>id</code>, <code>sudo -l</code></td><td><code>whoami /priv</code></td></tr>
          <tr><td>SUID / special perms</td><td><code>find / -perm -4000 2&gt;/dev/null</code></td><td>Unquoted service paths, weak ACLs</td></tr>
          <tr><td>Scheduled tasks</td><td><code>cat /etc/crontab</code></td><td><code>schtasks /query</code></td></tr>
          <tr><td>Kernel / OS version</td><td><code>uname -a</code></td><td><code>systeminfo</code></td></tr>
          <tr><td>Stored credentials</td><td>config files, history, <code>.env</code></td><td>Registry, SAM, unattended files</td></tr>
          <tr><td>Automated helper</td><td>LinPEAS, linenum.sh</td><td>WinPEAS, PowerUp</td></tr>
        </tbody>
      </table>
    </div>
    <div class="concept-card">
      <div class="concept-label">COMMON VECTORS</div>
      <div class="concept-title">How Escalation Actually Happens</div>
      <table class="ai-table">
        <thead><tr><th>Vector</th><th>Why It Works</th><th>Defense</th></tr></thead>
        <tbody>
          <tr><td>Misconfigured sudo</td><td>A user can run a program as root that can spawn a shell</td><td>Restrict sudoers; review <code>sudo -l</code></td></tr>
          <tr><td>SUID binaries</td><td>A SUID program can be abused to run as its owner (root)</td><td>Remove unneeded SUID bits</td></tr>
          <tr><td>Writable scripts run by root</td><td>A cron job runs your modified script as root</td><td>Fix file permissions</td></tr>
          <tr><td>Kernel exploits</td><td>Unpatched kernel vulnerability</td><td>Patch promptly</td></tr>
          <tr><td>Stored/reused credentials</td><td>Passwords in files, reuse across accounts</td><td>Secrets management, unique creds</td></tr>
          <tr><td>PATH hijacking</td><td>Privileged script calls a binary by relative name</td><td>Use absolute paths in scripts</td></tr>
        </tbody>
      </table>
      <div class="concept-desc"><strong>GTFOBins</strong> (and LOLBAS for Windows) are reference sites listing how common binaries can be abused for escalation — invaluable for both attackers and defenders auditing their systems.</div>
    </div>
  </div>
</div>
"""

# ─────────────────────────────── LINUX wave 23 ───────────────────────────────
LINUX_SENTINEL = "<!-- BEGINNER23-LINUX v1 -->"
LINUX_CONTENT = """
<!-- BEGINNER23-LINUX v1 -->
<!-- ── TOPIC: STORAGE MANAGEMENT ─────────────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">💾</span>
    <span class="topic-name">Storage Management — Disks, Partitions, LVM &amp; RAID</span>
    <span class="topic-badge">LINUX • Essential</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">THE STACK</div>
      <div class="concept-title">From Physical Disk to Mounted Directory</div>
      <div class="concept-desc">Linux storage is layered: a physical disk is divided into partitions, each formatted with a filesystem, then mounted onto a directory in the unified tree. Understanding the layers is key to managing storage and troubleshooting "disk full" emergencies.</div>
      <div class="code-block"><span class="com"># See block devices and their layout</span>
lsblk                          <span class="com"># tree of disks/partitions/mounts</span>
lsblk -f                       <span class="com"># include filesystem + UUID</span>
fdisk -l                       <span class="com"># detailed partition tables</span>

<span class="com"># Disk usage</span>
df -h                          <span class="com"># free space per filesystem</span>
df -i                          <span class="com"># inode usage (can fill before space!)</span>
du -sh /var/*                  <span class="com"># what's eating space in /var</span>
du -h --max-depth=1 / | sort -h   <span class="com"># biggest dirs</span></div>
    </div>
    <div class="concept-card">
      <div class="concept-label">PARTITION → FORMAT → MOUNT</div>
      <div class="concept-title">Adding a New Disk</div>
      <div class="code-block"><span class="com"># 1. Partition the new disk (e.g., /dev/sdb)</span>
sudo fdisk /dev/sdb            <span class="com"># interactive: n, w (or use parted)</span>

<span class="com"># 2. Create a filesystem</span>
sudo mkfs.ext4 /dev/sdb1       <span class="com"># or xfs, btrfs</span>

<span class="com"># 3. Mount it</span>
sudo mkdir /mnt/data
sudo mount /dev/sdb1 /mnt/data

<span class="com"># 4. Make it permanent — add to /etc/fstab (use UUID!)</span>
blkid /dev/sdb1                <span class="com"># get the UUID</span>
<span class="com"># /etc/fstab line:</span>
<span class="com"># UUID=xxxx-xxxx  /mnt/data  ext4  defaults  0  2</span>
sudo mount -a                  <span class="com"># test fstab WITHOUT rebooting</span></div>
      <div class="concept-desc"><strong>Always use UUIDs in fstab</strong>, not <code>/dev/sdb1</code> — device names can change between boots, and a bad fstab can prevent the system from booting. Test with <code>mount -a</code> before rebooting.</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">LVM</div>
      <div class="concept-title">Logical Volume Manager — Flexible Storage</div>
      <div class="concept-desc">LVM adds a layer of abstraction so you can resize volumes, span disks, and snapshot — without repartitioning. The hierarchy: Physical Volumes (PV) → grouped into a Volume Group (VG) → carved into Logical Volumes (LV) that you format and mount. The killer feature: grow a volume on the fly when you add a disk.</div>
      <div class="code-block"><span class="com"># PV → VG → LV</span>
sudo pvcreate /dev/sdb /dev/sdc       <span class="com"># mark disks as PVs</span>
sudo vgcreate data_vg /dev/sdb /dev/sdc   <span class="com"># pool them into a VG</span>
sudo lvcreate -L 50G -n data_lv data_vg   <span class="com"># carve a 50G LV</span>
sudo mkfs.ext4 /dev/data_vg/data_lv
sudo mount /dev/data_vg/data_lv /mnt/data

<span class="com"># The magic: extend it later (no downtime)</span>
sudo lvextend -L +20G /dev/data_vg/data_lv
sudo resize2fs /dev/data_vg/data_lv   <span class="com"># grow the filesystem too</span></div>
    </div>
    <div class="concept-card">
      <div class="concept-label">RAID LEVELS</div>
      <div class="concept-title">Redundancy and Performance Tradeoffs</div>
      <div class="concept-desc">RAID combines multiple disks for redundancy, performance, or both. <strong>RAID is not a backup</strong> — it protects against disk failure, not against deletion, corruption, or ransomware.</div>
      <table class="ai-table">
        <thead><tr><th>Level</th><th>Min Disks</th><th>Redundancy</th><th>Notes</th></tr></thead>
        <tbody>
          <tr><td>RAID 0 (stripe)</td><td>2</td><td>None</td><td>Fast, but ANY disk loss = all data lost</td></tr>
          <tr><td>RAID 1 (mirror)</td><td>2</td><td>1 disk</td><td>Full copy; simple, safe, 50% capacity</td></tr>
          <tr><td>RAID 5 (parity)</td><td>3</td><td>1 disk</td><td>Good balance; slow rebuilds on big disks</td></tr>
          <tr><td>RAID 6 (dual parity)</td><td>4</td><td>2 disks</td><td>Survives 2 failures; safer for large arrays</td></tr>
          <tr><td>RAID 10 (1+0)</td><td>4</td><td>Per mirror</td><td>Fast AND redundant; popular for databases</td></tr>
        </tbody>
      </table>
    </div>
  </div>
</div>
"""

# ─────────────────────────────── GRC wave 23 ─────────────────────────────────
GRC_SENTINEL = "<!-- BEGINNER23-GRC v1 -->"
GRC_CONTENT = """
<!-- BEGINNER23-GRC v1 -->
<!-- ── TOPIC: THE AUDIT PROCESS ──────────────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">🔍</span>
    <span class="topic-name">The Audit Process — Proving Controls Actually Work</span>
    <span class="topic-badge">GRC • Process</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">WHY AUDITS EXIST</div>
      <div class="concept-title">Trust, but Verify — With Evidence</div>
      <div class="concept-desc">Saying "we're secure" means nothing without proof. An audit is an independent examination that verifies controls exist and actually work — providing assurance to customers, regulators, and leadership. For IT staff, audits can feel like an interruption, but understanding the process makes them far smoother: auditors need <em>evidence</em>, and the better you prepare it, the faster it goes.</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">AUDIT TYPES</div>
      <div class="concept-title">Who's Doing the Auditing?</div>
      <table class="ai-table">
        <thead><tr><th>Type</th><th>Who</th><th>Purpose</th></tr></thead>
        <tbody>
          <tr><td>1st party (internal)</td><td>Your own audit team</td><td>Self-check before external audits; continuous improvement</td></tr>
          <tr><td>2nd party</td><td>A customer/partner audits you</td><td>Vendor assurance ("can we trust this supplier?")</td></tr>
          <tr><td>3rd party (external)</td><td>Independent firm (e.g., for SOC 2, ISO)</td><td>Certification, regulatory, customer-facing assurance</td></tr>
        </tbody>
      </table>
    </div>
    <div class="concept-card">
      <div class="concept-label">THE PHASES</div>
      <div class="concept-title">How an Audit Flows</div>
      <table class="ai-table">
        <thead><tr><th>Phase</th><th>What Happens</th></tr></thead>
        <tbody>
          <tr><td>1. Planning &amp; scoping</td><td>Define what's in scope, which controls, time period</td></tr>
          <tr><td>2. Fieldwork</td><td>Auditor requests evidence, interviews staff, tests controls</td></tr>
          <tr><td>3. Testing</td><td>Sample-based or full testing of whether controls operate effectively</td></tr>
          <tr><td>4. Findings</td><td>Document gaps/exceptions (deficiencies)</td></tr>
          <tr><td>5. Reporting</td><td>Formal report; management responds with remediation plans</td></tr>
          <tr><td>6. Remediation &amp; follow-up</td><td>Fix the findings; re-test in next cycle</td></tr>
        </tbody>
      </table>
    </div>
    <div class="concept-card">
      <div class="concept-label">EVIDENCE & TESTING</div>
      <div class="concept-title">What Auditors Actually Ask For</div>
      <div class="concept-desc">Auditors test controls in increasingly rigorous ways. Knowing what they want helps you prepare evidence in advance (screenshots, logs, tickets, configs, policies — all with dates).</div>
      <table class="ai-table">
        <thead><tr><th>Method</th><th>Example</th></tr></thead>
        <tbody>
          <tr><td>Inquiry</td><td>"Describe your access review process" (weakest evidence alone)</td></tr>
          <tr><td>Observation</td><td>Auditor watches you perform the control</td></tr>
          <tr><td>Inspection</td><td>Review documents/configs (policy, firewall rules, logs)</td></tr>
          <tr><td>Re-performance</td><td>Auditor independently re-does the control to confirm (strongest)</td></tr>
        </tbody>
      </table>
      <div class="concept-desc"><strong>Pro tip:</strong> "if it isn't documented, it didn't happen." Auditors live on evidence with timestamps. Keep tickets, approvals, and logs — automated evidence collection saves enormous pain at audit time.</div>
    </div>
  </div>
</div>
"""

# ─────────────────────────────── SHORTCUT wave 23 ────────────────────────────
SHORTCUT_SENTINEL = "<!-- BEGINNER23-SHORTCUT v1 -->"
SHORTCUT_CONTENT = """
<!-- BEGINNER23-SHORTCUT v1 -->
<!-- ── TOPIC: CLI TEXT PROCESSING MASTERY ────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">⚡</span>
    <span class="topic-name">Text Processing Mastery — Combining the Classic Tools</span>
    <span class="topic-badge">SHORTCUTS • Power User</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">THE UNIX PHILOSOPHY</div>
      <div class="concept-title">Small Tools That Do One Thing, Piped Together</div>
      <div class="concept-desc">The power of the command line comes from composing small, focused tools with pipes (<code>|</code>). Each tool does one thing well; the pipe feeds one's output into the next. Mastering a handful of these — and how to chain them — lets you answer questions about logs and data in seconds that would take ages in a GUI.</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">GREP — FIND LINES</div>
      <div class="concept-title">Search Text Like a Pro</div>
      <div class="code-block">grep "ERROR" app.log               <span class="com"># lines containing ERROR</span>
grep -i "error" app.log            <span class="com"># case-insensitive</span>
grep -r "TODO" ./src               <span class="com"># recursive through dir</span>
grep -v "DEBUG" app.log            <span class="com"># INVERT — lines WITHOUT DEBUG</span>
grep -c "404" access.log           <span class="com"># count matching lines</span>
grep -n "fail" app.log             <span class="com"># show line numbers</span>
grep -A3 -B3 "panic" app.log       <span class="com"># 3 lines After + Before context</span>
grep -E "warn|error|fatal" app.log <span class="com"># regex (extended) OR</span>
grep -oE "[0-9]+\\.[0-9]+\\.[0-9]+\\.[0-9]+" log   <span class="com"># extract just IPs</span></div>
    </div>
    <div class="concept-card">
      <div class="concept-label">FIND — LOCATE FILES</div>
      <div class="concept-title">Search the Filesystem by Any Attribute</div>
      <div class="code-block">find . -name "*.log"               <span class="com"># by name pattern</span>
find / -type f -size +100M         <span class="com"># files over 100MB</span>
find . -mtime -1                   <span class="com"># modified in last 24h</span>
find /var/log -mtime +30 -delete   <span class="com"># delete logs older than 30 days</span>
find . -type f -name "*.sh" -perm -u+x   <span class="com"># executable scripts</span>

<span class="com"># find + exec / xargs — act on results</span>
find . -name "*.tmp" -exec rm {} \\;     <span class="com"># delete each match</span>
find . -name "*.py" | xargs grep "import os"   <span class="com"># grep in matches</span></div>
    </div>
    <div class="concept-card">
      <div class="concept-label">THE CLASSIC PIPELINE</div>
      <div class="concept-title">cut · sort · uniq · awk — Together</div>
      <div class="code-block"><span class="com"># "Top 10 IPs hitting my web server" — a legendary one-liner</span>
cut -d' ' -f1 access.log | sort | uniq -c | sort -rn | head -10
<span class="com">#   cut field 1 (IP) → sort → count dups → sort by count desc → top 10</span>

<span class="com"># Count HTTP status codes</span>
awk '{print $9}' access.log | sort | uniq -c | sort -rn

<span class="com"># Sum a column (e.g., total bytes transferred)</span>
awk '{sum += $10} END {print sum}' access.log

<span class="com"># Unique users who logged in today</span>
grep "$(date +%Y-%m-%d)" auth.log | grep "session opened" \\
  | awk '{print $NF}' | sort -u

<span class="com"># Find the 5 largest files under /var, human-readable</span>
find /var -type f -printf '%s %p\\n' | sort -rn | head -5 \\
  | awk '{printf "%.1f MB  %s\\n", $1/1048576, $2}'</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">MODERN ALTERNATIVES</div>
      <div class="concept-title">Faster, Friendlier Replacements</div>
      <table class="ai-table">
        <thead><tr><th>Classic</th><th>Modern</th><th>Why</th></tr></thead>
        <tbody>
          <tr><td><code>grep</code></td><td><code>ripgrep</code> (rg)</td><td>Much faster, respects .gitignore, nicer output</td></tr>
          <tr><td><code>find</code></td><td><code>fd</code></td><td>Simpler syntax, fast, sane defaults</td></tr>
          <tr><td><code>cat</code></td><td><code>bat</code></td><td>Syntax highlighting, line numbers</td></tr>
          <tr><td><code>ls</code></td><td><code>eza</code> / <code>lsd</code></td><td>Colors, icons, git status</td></tr>
          <tr><td><code>top</code></td><td><code>htop</code> / <code>btop</code></td><td>Interactive, visual</td></tr>
        </tbody>
      </table>
      <div class="concept-desc">Learn the classics first — they're on every server, everywhere, forever. The modern tools are great for your own machine but won't be on that random production box at 3am.</div>
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
        (PENTEST_INJECT_ANCHOR,  PENTEST_SENTINEL,  PENTEST_CONTENT),
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
