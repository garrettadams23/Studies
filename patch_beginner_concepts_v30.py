#!/usr/bin/env python3
"""Wave 30 – Active Directory, DB ops, NFS/Samba, Windows admin, PowerShell basics."""
from pathlib import Path
from html.parser import HTMLParser

# ── sentinels ──────────────────────────────────────────────────────────────
S_NET      = "<!-- BEGINNER30-NET v1 -->"
S_OPS      = "<!-- BEGINNER30-OPS v1 -->"
S_LINUX    = "<!-- BEGINNER30-LINUX v1 -->"
S_LIFESTYLE= "<!-- BEGINNER30-LIFESTYLE v1 -->"
S_SCRIPT   = "<!-- BEGINNER30-SCRIPT v1 -->"

# ── anchors ────────────────────────────────────────────────────────────────
A_NET      = "<!-- /domain-body net -->"
A_OPS      = "<!-- /domain-body ops -->"
A_LINUX    = "<!-- /domain-body linux -->"
A_LIFESTYLE= "<!-- /domain-body lifestyle -->"
A_SCRIPT   = "<!-- /domain-body script -->"

# ══════════════════════════════════════════════════════════════════════════
# NET – Active Directory & LDAP basics
# ══════════════════════════════════════════════════════════════════════════
C_NET = """
<!-- BEGINNER30-NET v1 -->
<!-- ── TOPIC: Active Directory & LDAP ────────────────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-badge">Beginner</span>
    Active Directory &amp; LDAP – Enterprise Identity 101
  </div>
  <div class="topic-body">

    <div class="concept-card">
      <div class="concept-label">Core Concept</div>
      <div class="concept-title">What Is Active Directory?</div>
      <div class="concept-desc">
        Active Directory (AD) is Microsoft's directory service — the central
        phonebook of every Windows enterprise. It stores <strong>users,
        computers, groups, and policies</strong> in a tree of
        <em>Organizational Units (OUs)</em>. When you log in at work, your
        laptop asks a <em>Domain Controller (DC)</em> to verify your password.
        <br><br>
        <strong>Key vocabulary:</strong><br>
        &bull; <em>Domain</em> – a boundary of administration (e.g. <code>corp.example.com</code>).<br>
        &bull; <em>Forest</em> – one or more domains that trust each other.<br>
        &bull; <em>OU</em> – a folder inside AD used to organise objects.<br>
        &bull; <em>GPO</em> – Group Policy Object; rules pushed to computers/users.<br>
        &bull; <em>DC</em> – Domain Controller; the server that runs AD.
        <br><br>
        <em>"Not my circus, not my monkey"</em> — if you are not the AD admin,
        do not make changes in AD. Escalate to the team that owns it.
      </div>
    </div>

    <div class="concept-card">
      <div class="concept-label">Protocol</div>
      <div class="concept-title">LDAP – How Applications Talk to AD</div>
      <div class="concept-desc">
        <strong>LDAP (Lightweight Directory Access Protocol)</strong> is the
        language software uses to query AD. Every object has a
        <em>Distinguished Name (DN)</em> — a path like a file system path:<br>
        <code>CN=Alice Smith,OU=Finance,DC=corp,DC=example,DC=com</code><br><br>
        Common LDAP operations:<br>
        &bull; <strong>Bind</strong> – authenticate (log in) to the directory.<br>
        &bull; <strong>Search</strong> – find objects matching a filter.<br>
        &bull; <strong>Add / Modify / Delete</strong> – manage objects (admin only).<br><br>
        Port 389 = plain LDAP &nbsp;|&nbsp; Port 636 = LDAPS (TLS encrypted — always prefer this).
      </div>
      <div class="code-block">
<span class="com"># Query AD with Python ldap3 (read-only example)</span>
<span class="kw">from</span> ldap3 <span class="kw">import</span> Server, Connection, ALL, SUBTREE

server = Server(<span class="str">'ldaps://dc01.corp.example.com'</span>, get_info=ALL)
conn   = Connection(server,
                    user=<span class="str">'corp\\svc_readonly'</span>,
                    password=<span class="str">'S3cur3P@ss!'</span>,
                    auto_bind=<span class="kw">True</span>)

<span class="com"># Find all users in the Finance OU</span>
conn.search(
    search_base=<span class="str">'OU=Finance,DC=corp,DC=example,DC=com'</span>,
    search_filter=<span class="str">'(&amp;(objectClass=user)(!(userAccountControl:1.2.840.113556.1.4.803:=2)))'</span>,
    search_scope=SUBTREE,
    attributes=[<span class="str">'cn'</span>, <span class="str">'mail'</span>, <span class="str">'department'</span>]
)

<span class="kw">for</span> entry <span class="kw">in</span> conn.entries:
    <span class="fn">print</span>(entry.cn, entry.mail)

conn.unbind()
<span class="com"># The filter above: objectClass=user AND NOT disabled (bit 2 of UAC)</span>
      </div>
    </div>

    <div class="concept-card">
      <div class="concept-label">Authentication</div>
      <div class="concept-title">Kerberos in Plain English</div>
      <div class="concept-desc">
        Kerberos is the default authentication protocol for AD domains. Think of
        it as a <em>theme-park wristband</em> system:<br><br>
        1. You show your password <strong>once</strong> to the
           <em>Key Distribution Center (KDC)</em> on the DC.<br>
        2. The KDC gives you a <strong>Ticket-Granting Ticket (TGT)</strong> —
           your all-day wristband.<br>
        3. When you access a resource (file share, web app), you show the TGT
           to get a <strong>Service Ticket</strong> — a ride ticket for that
           specific attraction.<br>
        4. The resource trusts the service ticket without ever seeing your
           password again.<br><br>
        <strong>Why this matters for beginners:</strong> you never type your
        password again during the work day — Single Sign-On (SSO).
        Kerberos tickets expire (default 10 hours), so you may be prompted
        again next day.
      </div>
    </div>

    <div class="concept-card">
      <div class="concept-label">Best Practice</div>
      <div class="concept-title">Principle of Least Privilege in AD</div>
      <div class="concept-desc">
        <em>"Assume" makes an ass out of you and me</em> — never assume a user
        needs more permissions than their job requires. In AD:<br><br>
        &bull; Give users <strong>standard accounts</strong> for daily work.<br>
        &bull; Admins use a <strong>separate admin account</strong>
          (e.g. <code>a-alice</code>) only when elevated tasks are needed.<br>
        &bull; Service accounts get <strong>only the groups they need</strong>.<br>
        &bull; Review group memberships quarterly — "account creep" is real.<br><br>
        The <em>Domain Admins</em> group is the most powerful group in the
        domain. Its membership list should be tiny and audited constantly.
      </div>
    </div>

  </div>
</div>
"""

# ══════════════════════════════════════════════════════════════════════════
# OPS – PostgreSQL database administration basics
# ══════════════════════════════════════════════════════════════════════════
C_OPS = """
<!-- BEGINNER30-OPS v1 -->
<!-- ── TOPIC: PostgreSQL Admin Basics ────────────────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-badge">Beginner</span>
    PostgreSQL Administration – Database Ops 101
  </div>
  <div class="topic-body">

    <div class="concept-card">
      <div class="concept-label">Core Concept</div>
      <div class="concept-title">What Is a Database Server?</div>
      <div class="concept-desc">
        A <strong>database server</strong> stores data in structured tables and
        answers queries from applications. PostgreSQL (Postgres) is the most
        popular open-source relational database. As an ops person you are
        responsible for keeping it <em>running, backed up, and fast</em>.
        <br><br>
        <strong>Quick orientation:</strong><br>
        &bull; <em>Cluster</em> – one running Postgres instance (port 5432).<br>
        &bull; <em>Database</em> – a namespace inside the cluster.<br>
        &bull; <em>Schema</em> – a namespace inside a database (default: <code>public</code>).<br>
        &bull; <em>Table</em> – rows &amp; columns, like a spreadsheet.<br>
        &bull; <em>Role</em> – a user or group (Postgres uses one object for both).
      </div>
    </div>

    <div class="concept-card">
      <div class="concept-label">Daily Commands</div>
      <div class="concept-title">psql – The Postgres CLI</div>
      <div class="concept-desc">
        <code>psql</code> is the interactive terminal for Postgres.
        Master these and you can do 80 % of admin tasks.
      </div>
      <div class="code-block">
<span class="com"># Connect as the postgres superuser</span>
sudo -u postgres psql

<span class="com">-- Inside psql (lines starting with -- are SQL comments)</span>
<span class="com">-- List all databases</span>
\l

<span class="com">-- Connect to a specific database</span>
\c myapp_db

<span class="com">-- List tables in current schema</span>
\dt

<span class="com">-- Show table structure</span>
\d users

<span class="com">-- Run a query</span>
<span class="kw">SELECT</span> id, email <span class="kw">FROM</span> users <span class="kw">LIMIT</span> <span class="num">5</span>;

<span class="com">-- Show currently running queries</span>
<span class="kw">SELECT</span> pid, now() - query_start <span class="kw">AS</span> duration, query
<span class="kw">FROM</span>  pg_stat_activity
<span class="kw">WHERE</span> state = <span class="str">'active'</span>
<span class="kw">ORDER BY</span> duration <span class="kw">DESC</span>;

<span class="com">-- Kill a stuck query (use pid from above)</span>
<span class="kw">SELECT</span> pg_terminate_backend(<span class="num">12345</span>);

<span class="com">-- Quit psql</span>
\q
      </div>
    </div>

    <div class="concept-card">
      <div class="concept-label">Backup &amp; Restore</div>
      <div class="concept-title">pg_dump and pg_restore</div>
      <div class="concept-desc">
        <em>You can't make someone make the right choice, yet you can pick up
        the pieces afterwards</em> — a developer may drop a table by accident.
        Your job is to have a backup ready so you can restore it.
      </div>
      <div class="code-block">
<span class="com"># Backup a single database to a compressed file</span>
pg_dump -U postgres -Fc myapp_db &gt; myapp_db_$(date +%F).dump

<span class="com"># Backup all databases (SQL text format)</span>
pg_dumpall -U postgres &gt; all_databases_$(date +%F).sql

<span class="com"># Restore from a compressed dump</span>
pg_restore -U postgres -d myapp_db --clean myapp_db_2026-06-01.dump

<span class="com"># Restore from SQL text dump</span>
psql -U postgres &lt; all_databases_2026-06-01.sql

<span class="com"># Automate nightly backup via cron (runs at 2 AM daily)</span>
<span class="com"># Add to crontab with: crontab -e</span>
0 2 * * * pg_dump -U postgres -Fc myapp_db &gt; /backups/myapp_$(date +\%F).dump
      </div>
    </div>

    <div class="concept-card">
      <div class="concept-label">Performance</div>
      <div class="concept-title">VACUUM, ANALYZE, and Indexes</div>
      <div class="concept-desc">
        Postgres uses <em>Multi-Version Concurrency Control (MVCC)</em> —
        deleted rows are not immediately removed, they become "dead tuples."
        <code>VACUUM</code> reclaims that space. <code>ANALYZE</code> updates
        statistics so the query planner makes good choices.
        <br><br>
        <strong>Autovacuum</strong> handles this automatically in normal
        operation — never disable it.
        <br><br>
        <strong>Indexes</strong> speed up queries on large tables (like a book's
        index). Add one when a column appears frequently in <code>WHERE</code>
        clauses, but don't over-index — every index slows down
        <code>INSERT</code>/<code>UPDATE</code>.
      </div>
      <div class="code-block">
<span class="com">-- Manual vacuum + analyze (safe to run any time)</span>
<span class="kw">VACUUM ANALYZE</span> users;

<span class="com">-- Check table bloat (dead tuple ratio)</span>
<span class="kw">SELECT</span> relname, n_dead_tup, n_live_tup,
       round(n_dead_tup::numeric / nullif(n_live_tup,<span class="num">0</span>) * <span class="num">100</span>, <span class="num">2</span>) <span class="kw">AS</span> dead_pct
<span class="kw">FROM</span>  pg_stat_user_tables
<span class="kw">ORDER BY</span> dead_pct <span class="kw">DESC NULLS LAST</span>;

<span class="com">-- Add an index on the email column</span>
<span class="kw">CREATE INDEX CONCURRENTLY</span> idx_users_email <span class="kw">ON</span> users(email);
<span class="com">-- CONCURRENTLY = no table lock, safe on production</span>

<span class="com">-- Explain a query (show execution plan)</span>
<span class="kw">EXPLAIN ANALYZE SELECT</span> * <span class="kw">FROM</span> users <span class="kw">WHERE</span> email = <span class="str">'alice@example.com'</span>;
      </div>
    </div>

  </div>
</div>
"""

# ══════════════════════════════════════════════════════════════════════════
# LINUX – NFS & Samba file sharing
# ══════════════════════════════════════════════════════════════════════════
C_LINUX = """
<!-- BEGINNER30-LINUX v1 -->
<!-- ── TOPIC: NFS & Samba Network Storage ────────────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-badge">Beginner</span>
    NFS &amp; Samba – Sharing Files Across the Network
  </div>
  <div class="topic-body">

    <div class="concept-card">
      <div class="concept-label">Core Concept</div>
      <div class="concept-title">NFS vs Samba – When to Use Which</div>
      <div class="concept-desc">
        Two protocols dominate network file sharing on Linux:<br><br>
        <strong>NFS (Network File System)</strong><br>
        &bull; Linux-to-Linux sharing (Unix permissions, UIDs).<br>
        &bull; Fast and simple; no user login required (host-based trust).<br>
        &bull; Best for: server-to-server shares, Kubernetes persistent volumes,
          developer workstations on the same trusted LAN.<br><br>
        <strong>Samba (SMB/CIFS)</strong><br>
        &bull; Linux server sharing files to Windows clients (and macOS).<br>
        &bull; Supports AD authentication — Windows users log in with their
          domain credentials.<br>
        &bull; Best for: office file servers, home directories for Windows users.<br><br>
        <em>"Not my circus, not my monkey"</em> — if Windows clients are
        complaining about a share, check with the Windows team before touching
        Samba config; their GPOs may be overriding settings.
      </div>
    </div>

    <div class="concept-card">
      <div class="concept-label">NFS Server</div>
      <div class="concept-title">Setting Up an NFS Export</div>
      <div class="concept-desc">
        The NFS server exposes directories via <code>/etc/exports</code>.
        Each line names the directory and which clients may mount it.
      </div>
      <div class="code-block">
<span class="com"># Install NFS server (Debian/Ubuntu)</span>
sudo apt install nfs-kernel-server

<span class="com"># Create a shared directory</span>
sudo mkdir -p /srv/share
sudo chown nobody:nogroup /srv/share
sudo chmod <span class="num">755</span> /srv/share

<span class="com"># Edit /etc/exports</span>
<span class="com"># Format: /path  client(options)</span>
<span class="com"># rw = read-write | sync = safe writes | no_subtree_check = faster</span>
/srv/share  <span class="num">192.168.1</span>.0/<span class="num">24</span>(rw,sync,no_subtree_check)

<span class="com"># Apply changes and restart</span>
sudo exportfs -ra
sudo systemctl restart nfs-kernel-server

<span class="com">─────────── NFS CLIENT SIDE ───────────</span>
<span class="com"># Install NFS client tools</span>
sudo apt install nfs-common

<span class="com"># Mount the share temporarily</span>
sudo mount <span class="num">192.168.1</span>.<span class="num">10</span>:/srv/share /mnt/nfs

<span class="com"># Make it persistent (add to /etc/fstab)</span>
<span class="num">192.168.1</span>.<span class="num">10</span>:/srv/share  /mnt/nfs  nfs  defaults,_netdev  <span class="num">0 0</span>
      </div>
    </div>

    <div class="concept-card">
      <div class="concept-label">Samba Server</div>
      <div class="concept-title">Setting Up a Samba Share</div>
      <div class="concept-desc">
        Samba's configuration lives in <code>/etc/samba/smb.conf</code>.
        The <code>[global]</code> section sets domain-wide options;
        each <code>[share-name]</code> section defines one share.
      </div>
      <div class="code-block">
<span class="com"># Install Samba</span>
sudo apt install samba

<span class="com"># /etc/samba/smb.conf snippet</span>
[global]
   workgroup = CORP
   server string = File Server
   security = user           <span class="com">; or 'ads' for AD integration</span>
   map to guest = Bad User   <span class="com">; unauthenticated = read-only guest</span>

[documents]
   path = /srv/samba/documents
   browseable = yes
   read only = no
   valid users = @finance     <span class="com">; only 'finance' Linux group</span>
   create mask = <span class="num">0664</span>
   directory mask = <span class="num">0775</span>

<span class="com"># Create a Samba user (must already be a Linux user)</span>
sudo smbpasswd -a alice

<span class="com"># Check config for errors</span>
testparm

<span class="com"># Restart Samba</span>
sudo systemctl restart smbd nmbd

<span class="com"># Mount from Linux client (CIFS)</span>
sudo mount -t cifs //fileserver/documents /mnt/docs \
  -o username=alice,password=secret,uid=$(id -u)
      </div>
    </div>

    <div class="concept-card">
      <div class="concept-label">Troubleshooting</div>
      <div class="concept-title">Common NFS &amp; Samba Gotchas</div>
      <div class="concept-desc">
        <em>"Assume" makes an ass out of you and me</em> — don't assume the
        firewall allows NFS/SMB traffic. Always verify:<br><br>
        <strong>NFS troubleshooting:</strong><br>
        &bull; <code>sudo showmount -e 192.168.1.10</code> — list exports from a server.<br>
        &bull; NFS needs ports 111 (rpcbind) and 2049 (nfsd) open in the firewall.<br>
        &bull; UID mismatch = files owned by wrong user; use <code>idmapd</code>
          or explicit UID mapping.<br><br>
        <strong>Samba troubleshooting:</strong><br>
        &bull; <code>smbclient -L //server -U alice</code> — list shares.<br>
        &bull; <code>sudo smbstatus</code> — show connected clients and locked files.<br>
        &bull; Check <code>/var/log/samba/log.smbd</code> for auth failures.<br>
        &bull; SMB needs TCP 445 (and 139 for older clients).
      </div>
    </div>

  </div>
</div>
"""

# ══════════════════════════════════════════════════════════════════════════
# LIFESTYLE – Windows Administration for IT beginners
# ══════════════════════════════════════════════════════════════════════════
C_LIFESTYLE = """
<!-- BEGINNER30-LIFESTYLE v1 -->
<!-- ── TOPIC: Windows Admin Fundamentals ─────────────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-badge">Beginner</span>
    Windows Administration Fundamentals
  </div>
  <div class="topic-body">

    <div class="concept-card">
      <div class="concept-label">Core Concept</div>
      <div class="concept-title">The Windows Admin Toolkit</div>
      <div class="concept-desc">
        Enterprise Windows administration revolves around a handful of tools.
        Learn these early — they show up in every IT job that involves Windows:<br><br>
        <strong>GUI Tools (MMC Snap-ins):</strong><br>
        &bull; <code>dsa.msc</code> — Active Directory Users &amp; Computers (ADUC).<br>
        &bull; <code>gpmc.msc</code> — Group Policy Management Console.<br>
        &bull; <code>compmgmt.msc</code> — Computer Management (local users, disks, services).<br>
        &bull; <code>eventvwr.msc</code> — Event Viewer (logs for everything).<br>
        &bull; <code>services.msc</code> — Start/stop/configure Windows services.<br><br>
        <strong>Command-line:</strong><br>
        &bull; <code>cmd.exe</code> — the classic command prompt (legacy but everywhere).<br>
        &bull; <code>powershell.exe</code> / <code>pwsh.exe</code> — the modern admin shell.<br>
        &bull; <code>wmic</code> / <code>winrm</code> — remote management from CLI.
      </div>
    </div>

    <div class="concept-card">
      <div class="concept-label">User Management</div>
      <div class="concept-title">Managing Users in Active Directory</div>
      <div class="concept-desc">
        Common day-one helpdesk tasks in Active Directory Users &amp; Computers (ADUC):
      </div>
      <div class="code-block">
<span class="com">-- Open ADUC: Win+R → dsa.msc</span>
<span class="com">-- Or via PowerShell (if RSAT tools installed):</span>

<span class="com"># Create a new AD user</span>
New-ADUser `
  -Name <span class="str">"Bob Jones"</span> `
  -SamAccountName <span class="str">"bjones"</span> `
  -UserPrincipalName <span class="str">"bjones@corp.example.com"</span> `
  -AccountPassword (ConvertTo-SecureString <span class="str">"TempP@ss1"</span> -AsPlainText -Force) `
  -ChangePasswordAtLogon $true `
  -Enabled $true `
  -Path <span class="str">"OU=Finance,DC=corp,DC=example,DC=com"</span>

<span class="com"># Unlock a locked-out account</span>
Unlock-ADAccount -Identity bjones

<span class="com"># Reset a password</span>
Set-ADAccountPassword bjones `
  -NewPassword (ConvertTo-SecureString <span class="str">"NewP@ss99"</span> -AsPlainText -Force) `
  -Reset

<span class="com"># Disable an account (departing employee)</span>
Disable-ADAccount -Identity bjones

<span class="com"># Find all disabled accounts in an OU</span>
Search-ADAccount -SearchBase <span class="str">"OU=Finance,DC=corp,DC=example,DC=com"</span> `
                 -AccountDisabled | Select Name, SamAccountName
      </div>
    </div>

    <div class="concept-card">
      <div class="concept-label">Group Policy</div>
      <div class="concept-title">Group Policy Objects (GPOs) Explained</div>
      <div class="concept-desc">
        A <strong>GPO</strong> is a collection of settings pushed from the domain
        controller to computers and users automatically. Examples of what GPOs
        control:<br><br>
        &bull; Password complexity requirements.<br>
        &bull; Screen lock after N minutes of inactivity.<br>
        &bull; Mapped drives (e.g. <code>H:</code> = home folder on file server).<br>
        &bull; Software deployment (install apps on logon).<br>
        &bull; Firewall rules, browser settings, USB restrictions.<br><br>
        GPOs apply in order: <strong>Local → Site → Domain → OU</strong> (LSDOU).
        Later policies win unless "Enforced" is set. Use
        <code>gpresult /r</code> on a PC to see which GPOs actually applied.
        <br><br>
        <em>You can't make someone make the right choice, yet you can pick up
        the pieces afterwards</em> — GPOs don't stop a determined user
        completely, but they raise the barrier and give you an audit trail
        when something goes wrong.
      </div>
    </div>

    <div class="concept-card">
      <div class="concept-label">Remote Access</div>
      <div class="concept-title">Remote Desktop &amp; PowerShell Remoting</div>
      <div class="concept-desc">
        Two primary ways to manage remote Windows machines:
      </div>
      <div class="code-block">
<span class="com"># ── Remote Desktop (RDP) ──</span>
<span class="com"># From Linux: install freerdp2</span>
xfreerdp /v:workstation01.corp.example.com /u:alice /d:CORP

<span class="com"># From Windows: mstsc.exe</span>
mstsc /v:workstation01.corp.example.com

<span class="com"># ── PowerShell Remoting (WinRM) ──</span>
<span class="com"># Enable on the target machine (run as admin once):</span>
Enable-PSRemoting -Force

<span class="com"># Connect to a remote session</span>
Enter-PSSession -ComputerName workstation01 -Credential CORP\alice

<span class="com"># Run a command on multiple machines at once</span>
Invoke-Command -ComputerName srv01, srv02, srv03 `
  -ScriptBlock { Get-Service -Name Spooler | Select Name, Status }

<span class="com"># Copy a file to a remote machine</span>
$s = New-PSSession -ComputerName srv01 -Credential CORP\alice
Copy-Item -Path C:\patch.msi -Destination C:\Temp\ -ToSession $s
Remove-PSSession $s
      </div>
    </div>

  </div>
</div>
"""

# ══════════════════════════════════════════════════════════════════════════
# SCRIPT – PowerShell scripting fundamentals
# ══════════════════════════════════════════════════════════════════════════
C_SCRIPT = """
<!-- BEGINNER30-SCRIPT v1 -->
<!-- ── TOPIC: PowerShell Scripting Fundamentals ──────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-badge">Beginner</span>
    PowerShell Scripting – Automate Windows &amp; Cross-Platform
  </div>
  <div class="topic-body">

    <div class="concept-card">
      <div class="concept-label">Core Concept</div>
      <div class="concept-title">PowerShell vs Bash – Key Differences</div>
      <div class="concept-desc">
        PowerShell looks like a shell but behaves like a programming language.
        The most important difference: <strong>PowerShell passes objects,
        Bash passes text.</strong><br><br>
        <table class="ai-table">
          <tr><th>Feature</th><th>Bash</th><th>PowerShell</th></tr>
          <tr><td>Output type</td><td>Plain text</td><td>.NET objects</td></tr>
          <tr><td>Pipe</td><td><code>grep, awk, cut</code></td><td>property access</td></tr>
          <tr><td>Error handling</td><td><code>$? / set -e</code></td><td><code>try/catch</code></td></tr>
          <tr><td>OS</td><td>Linux/macOS</td><td>Windows, Linux, macOS</td></tr>
          <tr><td>Extension</td><td><code>.sh</code></td><td><code>.ps1</code></td></tr>
        </table>
        <br>
        PowerShell is now open-source and cross-platform (pwsh). For Windows
        administration it is the <em>standard</em> — learn it even if you
        primarily work on Linux.
      </div>
    </div>

    <div class="concept-card">
      <div class="concept-label">Syntax</div>
      <div class="concept-title">PowerShell Fundamentals</div>
      <div class="concept-desc">Variables, loops, conditionals, functions — the building blocks.</div>
      <div class="code-block">
<span class="com"># Variables start with $</span>
$name   = <span class="str">"Alice"</span>
$age    = <span class="num">30</span>
$active = $true

<span class="com"># String interpolation (double quotes expand variables)</span>
Write-Host <span class="str">"Hello, $name! You are $age years old."</span>

<span class="com"># Arrays</span>
$servers = <span class="str">"srv01"</span>, <span class="str">"srv02"</span>, <span class="str">"srv03"</span>
$servers[<span class="num">0</span>]          <span class="com"># srv01</span>
$servers.Count     <span class="com"># 3</span>

<span class="com"># Hash table (dictionary)</span>
$config = @{
    Host = <span class="str">"db01"</span>
    Port = <span class="num">5432</span>
    DB   = <span class="str">"myapp"</span>
}
$config[<span class="str">"Host"</span>]   <span class="com"># db01</span>
$config.Port     <span class="com"># 5432 — dot notation works too</span>

<span class="com"># For-each loop</span>
foreach ($server in $servers) {
    Write-Host <span class="str">"Pinging $server ..."</span>
    Test-Connection $server -Count <span class="num">1</span> -Quiet
}

<span class="com"># If / elseif / else</span>
if ($age -ge <span class="num">18</span>) {
    Write-Host <span class="str">"Adult"</span>
} elseif ($age -ge <span class="num">13</span>) {
    Write-Host <span class="str">"Teen"</span>
} else {
    Write-Host <span class="str">"Child"</span>
}

<span class="com"># Function</span>
function Get-DiskUsage {
    param([string]$Path = <span class="str">"C:\\"</span>)
    Get-PSDrive -Name ($Path[<span class="num">0</span>]) | Select Used, Free
}
Get-DiskUsage -Path <span class="str">"D:\\"</span>
      </div>
    </div>

    <div class="concept-card">
      <div class="concept-label">Object Pipeline</div>
      <div class="concept-title">Working with Objects in the Pipeline</div>
      <div class="concept-desc">
        Because PowerShell passes objects, you can filter and select
        <em>properties</em> without parsing text. This is PowerShell's
        superpower.
      </div>
      <div class="code-block">
<span class="com"># Get all running services, filter, sort, format</span>
Get-Service |
    Where-Object { $_.Status -eq <span class="str">"Running"</span> } |
    Sort-Object   DisplayName |
    Select-Object Name, DisplayName, StartType |
    Format-Table -AutoSize

<span class="com"># $_ is the current object in the pipeline</span>
<span class="com"># Where-Object = filter (like grep but for objects)</span>
<span class="com"># Select-Object = pick columns (like cut but named)</span>

<span class="com"># Find processes using more than 500 MB RAM</span>
Get-Process |
    Where-Object { $_.WorkingSet64 -gt <span class="num">500</span>MB } |
    Select-Object Name, Id,
      @{N=<span class="str">"RAM_MB"</span>; E={[math]::Round($_.WorkingSet64/<span class="num">1</span>MB)}} |
    Sort-Object RAM_MB -Descending

<span class="com"># Export to CSV for a report</span>
Get-EventLog -LogName Security -Newest <span class="num">100</span> |
    Where-Object { $_.EventID -eq <span class="num">4625</span> } |  <span class="com"># failed logons</span>
    Select-Object TimeGenerated, Message |
    Export-Csv -Path failed_logons.csv -NoTypeInformation
      </div>
    </div>

    <div class="concept-card">
      <div class="concept-label">Error Handling</div>
      <div class="concept-title">try / catch / finally in PowerShell</div>
      <div class="concept-desc">
        PowerShell uses <code>try/catch/finally</code> like most modern
        languages. Use <code>-ErrorAction Stop</code> to make cmdlets throw
        catchable exceptions (by default many just warn and continue).
      </div>
      <div class="code-block">
<span class="com"># Always use -ErrorAction Stop so errors are catchable</span>
try {
    $result = Invoke-WebRequest -Uri <span class="str">"https://api.internal/health"</span> `
                                -ErrorAction Stop
    Write-Host <span class="str">"API is UP: $($result.StatusCode)"</span>
}
catch [System.Net.WebException] {
    Write-Warning <span class="str">"Network error: $($_.Exception.Message)"</span>
}
catch {
    Write-Error   <span class="str">"Unexpected error: $($_.Exception.Message)"</span>
}
finally {
    Write-Host <span class="str">"Health check complete."</span>  <span class="com"># always runs</span>
}

<span class="com"># Log errors to a file</span>
$ErrorActionPreference = <span class="str">"Stop"</span>
try {
    Get-Content <span class="str">"C:\\missing_file.txt"</span>
} catch {
    $_ | Out-File -Append <span class="str">"C:\\Logs\\errors.log"</span>
}
      </div>
    </div>

  </div>
</div>
"""

# ══════════════════════════════════════════════════════════════════════════
# helpers
# ══════════════════════════════════════════════════════════════════════════
def inject(html, anchor, sentinel, content):
    if sentinel in html:
        return html, False
    pos = html.find(anchor)
    if pos == -1:
        return html, False
    return html[:pos] + content + html[pos:], True


class _Checker(HTMLParser):
    def __init__(self):
        super().__init__()
        self.stack = []
        self.stray = 0
        VOID = {"area","base","br","col","embed","hr","img","input",
                "link","meta","param","source","track","wbr"}
        self._void = VOID
    def handle_starttag(self, tag, attrs):
        if tag not in self._void:
            self.stack.append(tag)
    def handle_endtag(self, tag):
        if tag in self._void:
            return
        if self.stack and self.stack[-1] == tag:
            self.stack.pop()
        else:
            self.stray += 1


def validate(html):
    c = _Checker()
    c.feed(html)
    print(f"  Unclosed at EOF : {c.stack[-5:] if c.stack else 'NONE'}")
    print(f"  Stray end tags  : {c.stray}")


WAVES = [
    (A_NET,       S_NET,       C_NET),
    (A_OPS,       S_OPS,       C_OPS),
    (A_LINUX,     S_LINUX,     C_LINUX),
    (A_LIFESTYLE, S_LIFESTYLE, C_LIFESTYLE),
    (A_SCRIPT,    S_SCRIPT,    C_SCRIPT),
]


def main():
    path = Path("index.html")
    html = path.read_text(encoding="utf-8")
    changed = False
    for anchor, sentinel, content in WAVES:
        html, did = inject(html, anchor, sentinel, content)
        label = sentinel.split()[0].lstrip("<!-").strip()
        print(f"  {label}: {'INJECTED' if did else 'already present / anchor missing'}")
        changed = changed or did
    if changed:
        path.write_text(html, encoding="utf-8")
        print(f"\n  Written {len(html):,} bytes")
    else:
        print("\n  Nothing to do.")
    print("\n  HTML balance check:")
    validate(html)


if __name__ == "__main__":
    main()
