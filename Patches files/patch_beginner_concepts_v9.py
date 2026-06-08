#!/usr/bin/env python3
"""
patch_beginner_concepts_v9.py — Wave 9: Databases, Git workflow, Cloud basics,
advanced scripting patterns, and more life/career skills.

New sentinels:
  BEGINNER9-SCRIPT v1   — Databases with Python (SQLite, SQL basics)
  BEGINNER9-NET v1      — OSI/TCP-IP model practical, firewalls, load balancers
  BEGINNER9-LINUX v1    — Systemd, networking commands, disk management
  BEGINNER9-SEC v1      — Encryption deep-dive, certificates, TLS/HTTPS
  BEGINNER9-LIFE v1     — Git for everyone, career paths in IT
"""
from pathlib import Path

SCRIPT_INJECT_ANCHOR = "<!-- /domain-body script -->"
NET_INJECT_ANCHOR    = "<!-- /domain-body net -->"
LINUX_INJECT_ANCHOR  = "<!-- /domain-body linux -->"
SEC_INJECT_ANCHOR    = "<!-- /domain-body sec -->"
LIFE_INJECT_ANCHOR   = "<!-- /domain-body lifestyle -->"

# ─────────────────────────────── SCRIPTING wave 9 ────────────────────────────
SCRIPT_SENTINEL = "<!-- BEGINNER9-SCRIPT v1 -->"
SCRIPT_CONTENT = """
<!-- BEGINNER9-SCRIPT v1 -->
<!-- ── TOPIC: SQL & DATABASES FOR BEGINNERS ──────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">🗄️</span>
    <span class="topic-name">SQL &amp; Databases — Where Data Actually Lives</span>
    <span class="topic-badge">SCRIPT • Foundation</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">WHAT IS A DATABASE</div>
      <div class="concept-title">Structured, Persistent, Queryable Storage</div>
      <div class="concept-desc">A database stores data so it can be retrieved, filtered, sorted, and updated efficiently. A file full of JSON works for small things; a real database handles millions of rows, concurrent users, transactions, and relationships between tables without losing data.</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">RELATIONAL DATABASES</div>
      <div class="concept-title">Tables, Rows, and Relationships</div>
      <div class="concept-desc">A <strong>relational database</strong> stores data in tables (like spreadsheets). Each table has rows (records) and columns (fields). Tables relate to each other through <strong>foreign keys</strong>. SQL (Structured Query Language) is the language for interacting with them. Popular: PostgreSQL, MySQL, SQLite, Microsoft SQL Server, Oracle.</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">BASIC SQL</div>
      <div class="concept-title">CRUD in SQL — Create, Read, Update, Delete</div>
      <div class="code-block"><span class="com">-- Create a table</span>
<span class="kw">CREATE TABLE</span> users (
    id      INTEGER <span class="kw">PRIMARY KEY</span> AUTOINCREMENT,
    name    TEXT <span class="kw">NOT NULL</span>,
    email   TEXT <span class="kw">UNIQUE NOT NULL</span>,
    age     INTEGER,
    created DATETIME <span class="kw">DEFAULT</span> CURRENT_TIMESTAMP
);

<span class="com">-- Insert rows</span>
<span class="kw">INSERT INTO</span> users (name, email, age)
<span class="kw">VALUES</span> (<span class="str">'Alice'</span>, <span class="str">'alice@example.com'</span>, <span class="num">30</span>);

<span class="com">-- Read / query</span>
<span class="kw">SELECT</span> * <span class="kw">FROM</span> users;
<span class="kw">SELECT</span> name, email <span class="kw">FROM</span> users <span class="kw">WHERE</span> age &gt; <span class="num">25</span>;
<span class="kw">SELECT</span> * <span class="kw">FROM</span> users <span class="kw">ORDER BY</span> name <span class="kw">ASC LIMIT</span> <span class="num">10</span>;

<span class="com">-- Update</span>
<span class="kw">UPDATE</span> users <span class="kw">SET</span> age = <span class="num">31</span> <span class="kw">WHERE</span> email = <span class="str">'alice@example.com'</span>;

<span class="com">-- Delete</span>
<span class="kw">DELETE FROM</span> users <span class="kw">WHERE</span> id = <span class="num">5</span>;</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">JOINS</div>
      <div class="concept-title">Combine Data From Multiple Tables</div>
      <div class="code-block"><span class="com">-- Users and their orders (one user, many orders)</span>
<span class="kw">CREATE TABLE</span> orders (
    id      INTEGER <span class="kw">PRIMARY KEY</span>,
    user_id INTEGER <span class="kw">REFERENCES</span> users(id),
    amount  REAL,
    status  TEXT
);

<span class="com">-- INNER JOIN: only rows that match in BOTH tables</span>
<span class="kw">SELECT</span> users.name, orders.amount, orders.status
<span class="kw">FROM</span> orders
<span class="kw">INNER JOIN</span> users <span class="kw">ON</span> orders.user_id = users.id;

<span class="com">-- LEFT JOIN: all users, even those with no orders</span>
<span class="kw">SELECT</span> users.name, orders.amount
<span class="kw">FROM</span> users
<span class="kw">LEFT JOIN</span> orders <span class="kw">ON</span> users.id = orders.user_id;

<span class="com">-- Aggregate: total spent per user</span>
<span class="kw">SELECT</span> users.name, <span class="fn">SUM</span>(orders.amount) <span class="kw">AS</span> total
<span class="kw">FROM</span> users
<span class="kw">LEFT JOIN</span> orders <span class="kw">ON</span> users.id = orders.user_id
<span class="kw">GROUP BY</span> users.id
<span class="kw">ORDER BY</span> total <span class="kw">DESC</span>;</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">PYTHON + SQLITE</div>
      <div class="concept-title">Embedded Database, No Server Required</div>
      <div class="code-block"><span class="kw">import</span> sqlite3

<span class="com"># Connect (creates file if not exists)</span>
conn = sqlite3.connect(<span class="str">"mydb.sqlite"</span>)
conn.row_factory = sqlite3.Row   <span class="com"># access columns by name</span>
cursor = conn.cursor()

<span class="com"># Create table</span>
cursor.execute(<span class="str">&quot;&quot;&quot;
    CREATE TABLE IF NOT EXISTS notes (
        id    INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        body  TEXT
    )
&quot;&quot;&quot;</span>)

<span class="com"># Parameterized insert (ALWAYS use ? placeholders, never f-strings in SQL!)</span>
cursor.execute(<span class="str">"INSERT INTO notes (title, body) VALUES (?, ?)"</span>,
               (<span class="str">"First note"</span>, <span class="str">"Content here"</span>))
conn.commit()

<span class="com"># Query</span>
rows = cursor.execute(<span class="str">"SELECT * FROM notes ORDER BY id DESC"</span>).fetchall()
<span class="kw">for</span> row <span class="kw">in</span> rows:
    <span class="fn">print</span>(row[<span class="str">"title"</span>], row[<span class="str">"body"</span>])

conn.close()</div>
      <div class="concept-desc">The <code>?</code> placeholder is critical. <strong>Never</strong> build SQL with string formatting — that's how SQL injection happens: <code>f"WHERE name = '{user_input}'"</code> lets attackers inject arbitrary SQL.</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">SQL vs NoSQL</div>
      <div class="concept-title">Relational vs Document/Key-Value/Graph</div>
      <div class="concept-desc"><strong>SQL databases</strong> (PostgreSQL, MySQL, SQLite) — structured schema, ACID transactions, complex queries, relationships. Best for: financial data, user records, anything needing data integrity.<br>
      <strong>NoSQL databases</strong> — flexible schemas, horizontal scaling, specialized access patterns:<br>
      • <strong>Document</strong> (MongoDB) — JSON-like docs; good for varying schemas<br>
      • <strong>Key-Value</strong> (Redis) — extremely fast lookups; caching, sessions<br>
      • <strong>Column-family</strong> (Cassandra) — time-series, logs, analytics<br>
      • <strong>Graph</strong> (Neo4j) — relationships between entities (social network, fraud detection)</div>
    </div>
  </div>
</div>

<!-- ── TOPIC: GIT WORKFLOW — VERSION CONTROL ──────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">🌿</span>
    <span class="topic-name">Git — Version Control Every Developer Needs</span>
    <span class="topic-badge">SCRIPT • Essential</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">WHAT IS GIT</div>
      <div class="concept-title">Distributed Version Control</div>
      <div class="concept-desc">Git tracks every change made to your code. It lets you: travel back in time to any previous state, work on different features simultaneously (branches), collaborate without overwriting each other's work, and understand who changed what and why. Every professional software project uses git. No exceptions.</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">CORE CONCEPTS</div>
      <div class="concept-title">Repository · Commit · Branch · Remote</div>
      <div class="concept-desc"><strong>Repository (repo)</strong> — the folder of your project + all its history.<br>
      <strong>Commit</strong> — a snapshot of your code at a point in time, with a message describing the change.<br>
      <strong>Branch</strong> — an independent line of development. Main/master is the production branch. Feature branches let you experiment without breaking main.<br>
      <strong>Remote</strong> — a copy of the repo on another server (GitHub, GitLab). Push to share; pull to get others' changes.</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">DAILY WORKFLOW</div>
      <div class="concept-title">The Commands You Use Every Day</div>
      <div class="code-block"><span class="com"># Start: clone an existing repo</span>
git clone https://github.com/user/repo.git

<span class="com"># Check current state</span>
git status
git diff              <span class="com"># see unstaged changes</span>
git diff --staged     <span class="com"># see staged changes</span>

<span class="com"># Stage specific files (not everything)</span>
git add src/main.py
git add -p            <span class="com"># interactive: stage hunks one at a time</span>

<span class="com"># Commit with a meaningful message</span>
git commit -m <span class="str">"fix: prevent crash on empty input in login form"</span>

<span class="com"># Push to remote branch</span>
git push origin feature/my-feature

<span class="com"># Pull latest changes</span>
git pull origin main

<span class="com"># View history</span>
git log --oneline --graph -20</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">BRANCHING</div>
      <div class="concept-title">Feature → Review → Merge</div>
      <div class="code-block"><span class="com"># Create and switch to new branch</span>
git checkout -b feature/add-search
<span class="com"># (modern equivalent)</span>
git switch -c feature/add-search

<span class="com"># See all branches</span>
git branch -a

<span class="com"># Switch between branches</span>
git switch main
git switch feature/add-search

<span class="com"># Merge feature into main</span>
git switch main
git merge feature/add-search

<span class="com"># Delete merged branch</span>
git branch -d feature/add-search</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">UNDO</div>
      <div class="concept-title">Getting Out of Trouble</div>
      <div class="code-block"><span class="com"># Unstage a file (keep changes in working directory)</span>
git restore --staged myfile.py

<span class="com"># Discard local changes to a file (destructive!)</span>
git restore myfile.py

<span class="com"># Undo last commit (keep changes staged)</span>
git reset --soft HEAD~1

<span class="com"># Create a new commit that reverses a specific commit</span>
git revert abc1234    <span class="com"># safe for shared branches</span>

<span class="com"># See which commit introduced a bug (binary search)</span>
git bisect start
git bisect bad         <span class="com"># current commit is bad</span>
git bisect good v1.2   <span class="com"># this tag was good</span></div>
    </div>
    <div class="concept-card">
      <div class="concept-label">COMMIT MESSAGES</div>
      <div class="concept-title">The Conventional Commits Format</div>
      <div class="concept-desc">Good commit messages make history readable and enable automated changelogs. Format: <code>type(scope): description</code><br>
      <code>feat: add password strength meter</code><br>
      <code>fix: prevent null pointer on empty response</code><br>
      <code>docs: update API endpoint documentation</code><br>
      <code>refactor: extract validation logic into helper</code><br>
      <code>test: add unit tests for login flow</code><br>
      <code>chore: upgrade dependencies to latest</code></div>
    </div>
  </div>
</div>
"""

# ─────────────────────────────── NET wave 9 ──────────────────────────────────
NET_SENTINEL = "<!-- BEGINNER9-NET v1 -->"
NET_CONTENT = """
<!-- BEGINNER9-NET v1 -->
<!-- ── TOPIC: FIREWALLS — NETWORK'S BOUNCER ──────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">🧱</span>
    <span class="topic-name">Firewalls — The Network's Bouncer</span>
    <span class="topic-badge">NET • Foundation</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">WHAT A FIREWALL DOES</div>
      <div class="concept-title">Permit or Deny Based on Rules</div>
      <div class="concept-desc">A firewall inspects network traffic and decides whether to allow or block it based on rules. Think of it as a bouncer with a list: traffic that matches an allow rule gets in; everything else is dropped or rejected. The implicit deny rule: if nothing matches, deny.</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">FIREWALL TYPES</div>
      <div class="concept-title">Packet Filter → Stateful → NGFW</div>
      <div class="concept-desc"><strong>Packet filter (L3/L4)</strong> — examines individual packets: source/dest IP, port, protocol. No context (doesn't know if it's a new connection or response). Fast but dumb.<br>
      <strong>Stateful inspection</strong> — tracks connection state. Knows if a packet is part of an established session. Much smarter — allows response traffic automatically.<br>
      <strong>NGFW (Next-Gen Firewall)</strong> — adds application awareness (block YouTube regardless of port), IPS, deep packet inspection, user identity, SSL inspection. Most enterprise firewalls today.</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">IPTABLES BASICS</div>
      <div class="concept-title">Linux Built-In Firewall</div>
      <div class="code-block"><span class="com"># View current rules</span>
sudo iptables -L -v -n

<span class="com"># Allow established connections (critical — add first)</span>
sudo iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT

<span class="com"># Allow SSH (before blocking everything else!)</span>
sudo iptables -A INPUT -p tcp --dport 22 -j ACCEPT

<span class="com"># Allow web traffic</span>
sudo iptables -A INPUT -p tcp --dport 80 -j ACCEPT
sudo iptables -A INPUT -p tcp --dport 443 -j ACCEPT

<span class="com"># Drop everything else</span>
sudo iptables -A INPUT -j DROP

<span class="com"># Modern replacement: nftables / ufw</span>
sudo ufw enable
sudo ufw allow 22/tcp
sudo ufw allow 443/tcp
sudo ufw status verbose</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">DMZ</div>
      <div class="concept-title">De-Militarized Zone — Public-Facing Servers</div>
      <div class="concept-desc">A DMZ is a network segment between the internet and your internal network. Public-facing servers (web servers, mail servers) go in the DMZ. If they're compromised, the attacker is in the DMZ — not directly on your internal network. Two firewalls: one between internet and DMZ, another between DMZ and internal. Defense in depth.</div>
    </div>
  </div>
</div>

<!-- ── TOPIC: LOAD BALANCERS & HIGH AVAILABILITY ─────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">⚖️</span>
    <span class="topic-name">Load Balancers &amp; High Availability — Never Go Down</span>
    <span class="topic-badge">NET • Intermediate</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">THE PROBLEM</div>
      <div class="concept-title">One Server = Single Point of Failure</div>
      <div class="concept-desc">If your entire service runs on one server and it crashes, everyone is down. High availability (HA) architectures spread load across multiple servers so that if one fails, others continue serving traffic seamlessly. <strong>HA goal</strong>: no single component failure takes down the service.</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">LOAD BALANCER</div>
      <div class="concept-title">Distributes Traffic Across Backend Servers</div>
      <div class="concept-desc">A load balancer sits in front of your servers and routes each incoming request to one of the backends. Algorithms:<br>
      <strong>Round-robin</strong> — server 1, server 2, server 3, server 1… Even distribution.<br>
      <strong>Least connections</strong> — sends to whichever server has the fewest active connections.<br>
      <strong>IP hash</strong> — same client IP always goes to the same server (sticky sessions).<br>
      <strong>Weighted</strong> — big server gets more traffic than small server.</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">HEALTH CHECKS</div>
      <div class="concept-title">Automatically Remove Failing Servers</div>
      <div class="concept-desc">A load balancer periodically pings each backend (HTTP GET /health, TCP connect, etc.). If a backend fails N consecutive checks, it's removed from the pool. No human intervention needed — traffic automatically shifts to healthy servers. When it recovers, it re-enters the pool.</div>
    </div>
    <table class="ai-table">
      <thead><tr><th>Concept</th><th>Meaning</th><th>Common SLA</th></tr></thead>
      <tbody>
        <tr><td>High Availability (HA)</td><td>System stays up despite component failures</td><td>99.9% = 8.7 hrs/yr downtime</td></tr>
        <tr><td>99.99% ("four nines")</td><td>Enterprise HA target</td><td>52 min/yr downtime</td></tr>
        <tr><td>99.999% ("five nines")</td><td>Telco/critical systems</td><td>5.25 min/yr downtime</td></tr>
        <tr><td>RTO</td><td>Recovery Time Objective — max acceptable downtime</td><td>Defined in DR plan</td></tr>
        <tr><td>RPO</td><td>Recovery Point Objective — max acceptable data loss</td><td>Defined in DR plan</td></tr>
      </tbody>
    </table>
  </div>
</div>
"""

# ─────────────────────────────── LINUX wave 9 ────────────────────────────────
LINUX_SENTINEL = "<!-- BEGINNER9-LINUX v1 -->"
LINUX_CONTENT = """
<!-- BEGINNER9-LINUX v1 -->
<!-- ── TOPIC: SYSTEMD & SERVICE MANAGEMENT ───────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">⚙️</span>
    <span class="topic-name">systemd — Managing Linux Services</span>
    <span class="topic-badge">LINUX • Ops</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">WHAT IS SYSTEMD</div>
      <div class="concept-title">PID 1 — The Init System</div>
      <div class="concept-desc">systemd is the first process started by the kernel (PID 1) and the parent of all other processes. It manages:<br>
      • Starting/stopping services (daemons)<br>
      • Parallel boot for faster startup<br>
      • Service dependencies and ordering<br>
      • Logging (journald)<br>
      • Socket activation, timers (replacement for cron), mounts</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">systemctl COMMANDS</div>
      <div class="concept-title">Start, Stop, Enable, Status</div>
      <div class="code-block"><span class="com"># Service status</span>
systemctl status nginx
systemctl status ssh

<span class="com"># Start / stop / restart</span>
sudo systemctl start nginx
sudo systemctl stop nginx
sudo systemctl restart nginx

<span class="com"># Reload config without full restart</span>
sudo systemctl reload nginx

<span class="com"># Enable at boot / disable</span>
sudo systemctl enable nginx
sudo systemctl disable nginx

<span class="com"># Enable AND start immediately</span>
sudo systemctl enable --now nginx

<span class="com"># List all running services</span>
systemctl list-units --type=service --state=running

<span class="com"># List failed services</span>
systemctl --failed</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">JOURNALCTL</div>
      <div class="concept-title">Reading Service Logs</div>
      <div class="code-block"><span class="com"># All logs (most recent at bottom)</span>
journalctl

<span class="com"># Logs for a specific service</span>
journalctl -u nginx
journalctl -u nginx --since "1 hour ago"

<span class="com"># Follow in real time (like tail -f)</span>
journalctl -u nginx -f

<span class="com"># Only errors and above</span>
journalctl -p err

<span class="com"># Since last boot</span>
journalctl -b

<span class="com"># From a time range</span>
journalctl --since "2024-01-15 09:00" --until "2024-01-15 10:00"</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">WRITE A UNIT FILE</div>
      <div class="concept-title">Run Your Script as a Service</div>
      <div class="code-block"><span class="com"># Create /etc/systemd/system/myapp.service</span>
[Unit]
Description=My Python Application
After=network.target

[Service]
Type=simple
User=www-data
WorkingDirectory=/opt/myapp
ExecStart=/usr/bin/python3 /opt/myapp/server.py
Restart=always
RestartSec=5
StandardOutput=journal
StandardError=journal

[Install]
WantedBy=multi-user.target</div>
      <div class="code-block"><span class="com"># Reload systemd, start, enable</span>
sudo systemctl daemon-reload
sudo systemctl enable --now myapp</div>
    </div>
  </div>
</div>

<!-- ── TOPIC: DISK MANAGEMENT & STORAGE ──────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">💾</span>
    <span class="topic-name">Disk Management — Partitions, Filesystems &amp; LVM</span>
    <span class="topic-badge">LINUX • Foundation</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">CHECK DISK USAGE</div>
      <div class="concept-title">df and du — Your First Diagnostic</div>
      <div class="code-block"><span class="com"># Disk space by filesystem</span>
df -h

<span class="com"># Where is space being used in a directory?</span>
du -sh /var/log/*          <span class="com"># sizes in human readable</span>
du -sh /* 2>/dev/null      <span class="com"># top-level dirs</span>

<span class="com"># Find the 10 largest files</span>
find / -type f -printf '%s %p\n' 2>/dev/null \
  | sort -rn | head -10

<span class="com"># What files are open (and may not show freed space)</span>
lsof +L1 | grep deleted</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">PARTITIONS</div>
      <div class="concept-title">Dividing Physical Disks</div>
      <div class="concept-desc">A partition divides a physical disk into logical sections. Common layout:<br>
      <code>/boot</code> — kernel and boot files (~500MB)<br>
      <code>/</code> — root filesystem (everything else)<br>
      <code>/home</code> — user data (separate so OS reinstall preserves data)<br>
      <code>swap</code> — overflow memory (RAM extension on disk; slow)<br>
      Tools: <code>fdisk</code> (MBR), <code>gdisk</code> (GPT), <code>parted</code> (both)</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">FILESYSTEMS</div>
      <div class="concept-title">How Data Is Organized on Disk</div>
      <table class="ai-table">
        <thead><tr><th>Filesystem</th><th>OS</th><th>Strengths</th></tr></thead>
        <tbody>
          <tr><td>ext4</td><td>Linux</td><td>Default Linux; journaled; stable; 16TB max file</td></tr>
          <tr><td>xfs</td><td>Linux</td><td>High-performance; great for large files; RHEL default</td></tr>
          <tr><td>btrfs</td><td>Linux</td><td>Copy-on-write; snapshots; checksums; still maturing</td></tr>
          <tr><td>NTFS</td><td>Windows</td><td>Windows default; full permissions; mountable on Linux</td></tr>
          <tr><td>FAT32/exFAT</td><td>Universal</td><td>USB drives; read/write anywhere; no permissions</td></tr>
          <tr><td>APFS</td><td>macOS</td><td>Apple default; encrypted; snapshot support</td></tr>
          <tr><td>ZFS</td><td>BSD/Linux</td><td>Enterprise; built-in RAID; checksums; snapshots</td></tr>
        </tbody>
      </table>
    </div>
  </div>
</div>
"""

# ─────────────────────────────── SEC wave 9 ──────────────────────────────────
SEC_SENTINEL = "<!-- BEGINNER9-SEC v1 -->"
SEC_CONTENT = """
<!-- BEGINNER9-SEC v1 -->
<!-- ── TOPIC: TLS/HTTPS HOW IT WORKS ─────────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">🔒</span>
    <span class="topic-name">TLS &amp; HTTPS — How Secure Connections Work</span>
    <span class="topic-badge">SEC • Foundation</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">THE PROBLEM</div>
      <div class="concept-title">HTTP Is Plaintext — Anyone Can Read It</div>
      <div class="concept-desc">When you send a form over HTTP, the data travels through multiple hops (your router, ISP, CDN, etc.) as readable text. Anyone on those hops can see your password, credit card, messages. TLS (Transport Layer Security) encrypts the connection so even if someone intercepts the traffic, all they see is gibberish.</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">TLS HANDSHAKE</div>
      <div class="concept-title">Establish Trust + Exchange Keys</div>
      <div class="concept-desc">1. Client → Server: "Hello. I support these cipher suites and TLS versions."<br>
      2. Server → Client: "Hello. Here's my certificate. We'll use cipher X."<br>
      3. Client: Verify certificate against trusted CA list.<br>
      4. Key exchange (ECDHE): Both sides derive the same symmetric session key without ever transmitting it (Diffie-Hellman magic).<br>
      5. All further communication encrypted with that session key.<br>
      The asymmetric crypto (certificates) is only used during handshake. The bulk encryption uses faster symmetric crypto.</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">CERTIFICATES</div>
      <div class="concept-title">Digital Identity Documents</div>
      <div class="concept-desc">A TLS certificate binds a domain name to a public key, signed by a Certificate Authority (CA) the browser trusts. The chain of trust:<br>
      <strong>Root CA</strong> → (built into OS/browser)<br>
      <strong>Intermediate CA</strong> → (issued by root)<br>
      <strong>End-entity cert</strong> → (your server's cert)<br>
      If you trust the root, and the root signed the intermediate, and the intermediate signed your cert, you trust your cert.</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">CERT VALIDATION LEVELS</div>
      <div class="concept-title">DV vs OV vs EV</div>
      <div class="concept-desc"><strong>Domain Validated (DV)</strong> — CA just verifies you control the domain. Free (Let's Encrypt). Shows padlock in browser. Good for most sites.<br>
      <strong>Organization Validated (OV)</strong> — CA verifies organization identity. More trust signal for businesses.<br>
      <strong>Extended Validation (EV)</strong> — rigorous identity check. Historically showed green bar with company name (most browsers dropped this UI).</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">COMMON CERT ISSUES</div>
      <div class="concept-title">Errors You'll See and What They Mean</div>
      <table class="ai-table">
        <thead><tr><th>Error</th><th>Cause</th><th>Fix</th></tr></thead>
        <tbody>
          <tr><td>Certificate expired</td><td>cert past validity date</td><td>Renew/replace cert (Let's Encrypt auto-renews)</td></tr>
          <tr><td>Name mismatch</td><td>cert for example.com used on sub.example.com</td><td>Use wildcard cert or include SANs</td></tr>
          <tr><td>Untrusted CA</td><td>self-signed or private CA</td><td>Install CA cert in trust store or buy a public cert</td></tr>
          <tr><td>Incomplete chain</td><td>missing intermediate cert</td><td>Include full chain in server config</td></tr>
        </tbody>
      </table>
    </div>
    <div class="concept-card">
      <div class="concept-label">LET'S ENCRYPT</div>
      <div class="concept-title">Free, Automated, Trusted Certificates</div>
      <div class="concept-desc">Let's Encrypt is a free, automated CA. Use the <code>certbot</code> tool to get and auto-renew certificates with zero cost. It changed the web — HTTPS adoption went from ~40% in 2015 to ~95%+ today, largely because Let's Encrypt eliminated the cost barrier.</div>
      <div class="code-block"><span class="com"># Install certbot (Debian/Ubuntu)</span>
sudo apt install certbot python3-certbot-nginx

<span class="com"># Get cert and auto-configure nginx</span>
sudo certbot --nginx -d example.com -d www.example.com

<span class="com"># Test auto-renewal</span>
sudo certbot renew --dry-run</div>
    </div>
  </div>
</div>

<!-- ── TOPIC: ENCRYPTION FUNDAMENTALS ────────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">🔐</span>
    <span class="topic-name">Encryption Fundamentals — Symmetric vs Asymmetric</span>
    <span class="topic-badge">SEC • Foundation</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">SYMMETRIC ENCRYPTION</div>
      <div class="concept-title">Same Key to Lock and Unlock</div>
      <div class="concept-desc">One key encrypts AND decrypts. Fast, efficient for large data. Problem: key distribution — how do you securely share the key with the other party? Best algorithms: AES-256 (gold standard), ChaCha20. Used for: encrypting data at rest, bulk data transfer after handshake.</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">ASYMMETRIC ENCRYPTION</div>
      <div class="concept-title">Public Key + Private Key</div>
      <div class="concept-desc">Two mathematically linked keys. Public key encrypts (share freely — give to everyone). Private key decrypts (keep secret). Solves key distribution: encrypt with their public key → only they can decrypt with their private key. Slower than symmetric. Best algorithms: RSA-2048+, ECC (smaller keys, same strength). Used for: TLS handshake, SSH auth, digital signatures.</div>
    </div>
    <table class="ai-table">
      <thead><tr><th>Property</th><th>Symmetric</th><th>Asymmetric</th></tr></thead>
      <tbody>
        <tr><td>Keys</td><td>1 shared key</td><td>Key pair (public + private)</td></tr>
        <tr><td>Speed</td><td>Very fast</td><td>Slow (100-1000× slower)</td></tr>
        <tr><td>Key distribution</td><td>Hard (secure channel needed)</td><td>Easy (public key is public)</td></tr>
        <tr><td>Best for</td><td>Bulk data encryption</td><td>Key exchange, signatures</td></tr>
        <tr><td>Example</td><td>AES-256</td><td>RSA, ECC</td></tr>
        <tr><td>Used in TLS</td><td>Session data (after handshake)</td><td>Handshake / key exchange</td></tr>
      </tbody>
    </table>
    <div class="concept-card">
      <div class="concept-label">DIGITAL SIGNATURES</div>
      <div class="concept-title">Prove It Came From You and Wasn't Changed</div>
      <div class="concept-desc"><strong>Signing</strong>: hash the document, encrypt the hash with your PRIVATE key → signature.<br>
      <strong>Verifying</strong>: decrypt signature with sender's PUBLIC key → get hash. Hash the document yourself. If hashes match → not tampered, signed by private key holder.<br>
      Used in: software distribution (code signing), email (S/MIME, PGP), TLS certificates, git commits, JWT tokens.</div>
    </div>
  </div>
</div>
"""

# ─────────────────────────────── LIFESTYLE wave 9 ────────────────────────────
LIFE_SENTINEL = "<!-- BEGINNER9-LIFE v1 -->"
LIFE_CONTENT = """
<!-- BEGINNER9-LIFE v1 -->
<!-- ── TOPIC: IT CAREER PATHS ────────────────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">🛤️</span>
    <span class="topic-name">IT Career Paths — Finding Your Lane</span>
    <span class="topic-badge">LIFESTYLE • Career</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">THE LANDSCAPE</div>
      <div class="concept-title">IT Is Not One Career — It's Dozens</div>
      <div class="concept-desc">People say "I want to work in IT" the way people say "I want to work in healthcare." That could mean doctor, nurse, EMT, surgeon, or hospital administrator. IT has specializations that barely overlap. Start broad, find what excites you, then go deep.</div>
    </div>
    <table class="ai-table">
      <thead><tr><th>Track</th><th>Roles</th><th>Entry Point</th></tr></thead>
      <tbody>
        <tr><td>Networking</td><td>Network admin, engineer, architect</td><td>CompTIA Network+, CCNA</td></tr>
        <tr><td>Security</td><td>SOC analyst, security engineer, CISO</td><td>CompTIA Security+, CEH</td></tr>
        <tr><td>Pentest/Offensive</td><td>Pen tester, red team, bug bounty hunter</td><td>Security+, OSCP</td></tr>
        <tr><td>Cloud</td><td>Cloud engineer, DevOps, SRE</td><td>AWS/Azure/GCP associate certs</td></tr>
        <tr><td>Sysadmin/Linux</td><td>Sysadmin, platform engineer</td><td>CompTIA Linux+, RHCSA</td></tr>
        <tr><td>Development</td><td>Developer, backend/frontend, full-stack</td><td>Portfolio + GitHub</td></tr>
        <tr><td>Data</td><td>Data analyst, data engineer, ML engineer</td><td>SQL + Python + portfolio</td></tr>
        <tr><td>GRC/Compliance</td><td>Analyst, auditor, compliance manager</td><td>Security+, CISA</td></tr>
        <tr><td>IT Support</td><td>Help desk, tier 1-2-3 support</td><td>CompTIA A+</td></tr>
      </tbody>
    </table>
    <div class="concept-card">
      <div class="concept-label">CERT PROGRESSION</div>
      <div class="concept-title">A Reasonable Sequence</div>
      <div class="concept-desc"><strong>Start here</strong>: CompTIA A+ (foundation), then Network+, then Security+. These three prove foundational competence to any employer and open most entry-level doors.<br>
      <strong>Specialize</strong>: Pick a track. Cloud → AWS SAA. Linux → RHCSA. Security operations → CySA+. Offensive → OSCP.<br>
      <strong>Experience &gt; certs</strong>: After the foundation, a portfolio of real projects and hands-on labs beats stacking certifications. Build things. Break things. Document what you did.</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">HELP DESK AS A FOUNDATION</div>
      <div class="concept-title">Never Underestimate Tier 1</div>
      <div class="concept-desc">Help desk is often dismissed, but it's the best possible first job in IT. You'll touch every technology: networking, hardware, OS, software, email, printers, VPNs. You'll learn how organizations actually use technology. You'll develop communication skills under pressure. Most senior engineers started at a help desk. Do the job well, build your skills after hours, and move up within 12-18 months.</div>
    </div>
  </div>
</div>

<!-- ── TOPIC: NETWORKING FOR CAREER SUCCESS ───────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">🤝</span>
    <span class="topic-name">Professional Networking — Your Career Grows Through Relationships</span>
    <span class="topic-badge">LIFESTYLE • Career</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">THE HIDDEN JOB MARKET</div>
      <div class="concept-title">Most Jobs Are Never Posted</div>
      <div class="concept-desc">Studies suggest 70-85% of jobs are filled through connections before or without a public posting. The public job board is where you compete with 200 strangers. The hidden market is where someone says "I know the perfect person for this." You want to be that person.</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">HOW TO BUILD YOUR NETWORK</div>
      <div class="concept-title">Genuinely, Not Transactionally</div>
      <div class="concept-desc">Networking isn't about collecting LinkedIn contacts to spam when you need a job. It's about building relationships over time with people who share your interests.<br>
      • <strong>Tech communities</strong>: BSides security conferences, DEF CON groups, local user groups, Discord servers<br>
      • <strong>Open source</strong>: contribute even small things (docs, bug reports); maintainers notice<br>
      • <strong>Blogging/writing</strong>: write up what you learned even if it seems basic — beginners are looking for exactly that<br>
      • <strong>Mentorship</strong>: find a mentor AND mentor someone below you; both teach you things</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">LINKEDIN ACTUALLY WORKS</div>
      <div class="concept-title">But Only If You Use It Right</div>
      <div class="concept-desc">• Complete profile with skills, certifications, and projects<br>
      • Write short posts about what you're learning — not performative, but genuine. "I just got my OSCP, here's what actually helped me."<br>
      • Connect with people at companies you want to work for and have genuine conversations before asking for referrals<br>
      • Recruiters use LinkedIn constantly — if your profile reflects your skills, inbounds will come to you</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">THE GIVE-FIRST RULE</div>
      <div class="concept-title">Add Value Before You Ask</div>
      <div class="concept-desc">The single most effective networking approach: add value to people without expecting anything in return. Answer questions in forums. Share useful resources. Help someone debug their script. Give a presentation at a meetup. Write a blog post. When you've given, people want to give back — and when you do need something, you'll have built the trust to ask.</div>
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
        patch(target, LINUX_SENTINEL,  LINUX_CONTENT,  LINUX_INJECT_ANCHOR),
        patch(target, SEC_SENTINEL,    SEC_CONTENT,    SEC_INJECT_ANCHOR),
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
