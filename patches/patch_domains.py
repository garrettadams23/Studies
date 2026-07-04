#!/usr/bin/env python3
"""Inject the remaining domains into the IT reference tool.

Domains: PenTest, Linux/Systems, Shortcuts (+DoD), Military Staff Codes,
Lifestyle & Philosophy. Each is injected independently and idempotently.

DRY-RUN by default; pass --write to apply (creates .bak backups).
Run from the project root, or point at a folder with --dir PATH.
"""
import sys, os, shutil

# ---- builders (the ONE place the HTML conventions live) ------------------
def card(label, title, desc, code=""):
    cb = f'<pre class="code-block">{code}</pre>' if code else ""
    return (f'<div class="concept-card"><div class="concept-label">{label}</div>'
            f'<div class="concept-title">{title}</div>'
            f'<div class="concept-desc">{desc}</div>{cb}</div>')

def tbl(headers, rows):
    th = "".join(f"<th>{h}</th>" for h in headers)
    body = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows)
    return (f'<table class="ai-table"><thead><tr>{th}</tr></thead>'
            f'<tbody>{body}</tbody></table>')

def topic(icon, name, badge, *blocks):
    return (f'<div class="topic"><div class="topic-header">'
            f'<span class="topic-icon">{icon}</span>'
            f'<span class="topic-name">{name}</span>'
            f'<span class="topic-badge">{badge}</span>'
            f'<span class="topic-chevron">&rsaquo;</span></div>'
            f'<div class="topic-body">{"".join(blocks)}</div></div>')

# =========================================================================
# PENTEST  (PenTest+)
# =========================================================================
PENTEST = [
  topic("🎯", "Methodology &amp; Phases", "PenTest+ • PT0-002",
    card("ENGAGEMENT", "Scoping &amp; Authorization",
         "Define targets, exclusions, timing, and a signed authorization (get-out-of-jail letter) before touching anything. Capture constraints, points of contact, and a deconfliction process for accidental impact."),
    card("GOVERNANCE", "Rules of Engagement (RoE)",
         "The contract for behavior: allowed techniques, working hours, data-handling rules, and escalation paths. No RoE = no test."),
    card("TYPES", "Test &amp; Team Styles",
         "Black-box (no knowledge), gray-box (partial), white-box (full). External vs. internal vantage. Red (attack), blue (defend), purple (collaborate)."),
    tbl(["Phase", "Goal", "Tools"],
        [["Planning / Scoping", "RoE, authorization, scope", "Docs, contracts"],
         ["Recon (OSINT)", "Gather public info", "whois, theHarvester, Shodan"],
         ["Scanning / Enum", "Map hosts &amp; services", "Nmap, enum4linux"],
         ["Vuln Analysis", "Find weaknesses", "Nessus, Nikto"],
         ["Exploitation", "Gain access", "Metasploit, sqlmap, Hydra"],
         ["Post-Exploitation", "Escalate, pivot, exfil", "Mimikatz, LinPEAS"],
         ["Reporting", "Findings &amp; remediation", "Writeup, retest"]])
  ),
  topic("🔎", "Reconnaissance (OSINT)", "PenTest+ • Recon",
    card("PASSIVE", "No-Touch Intel",
         "Collect data without contacting the target: WHOIS, DNS records, breach dumps, social media, job posts, and Google dorking. Zero footprint on the target."),
    card("ACTIVE", "Direct Probing",
         "Interact with target infrastructure — DNS zone transfers, banner grabs, light service queries. Faster but detectable.",
         "<span class='com'># Passive-to-active recon</span>\n"
         "<span class='fn'>whois</span> example.com\n"
         "<span class='fn'>dig</span> example.com ANY +short\n"
         "<span class='fn'>theHarvester</span> -d example.com -b all"),
    tbl(["Tool", "Use"],
        [["whois / dig / nslookup", "Domain &amp; DNS records"],
         ["theHarvester", "Emails, hosts, subdomains"],
         ["Shodan / Censys", "Internet-exposed devices"],
         ["Recon-ng / Maltego", "Automated OSINT &amp; link analysis"],
         ["Google dorking", "Indexed sensitive files"]])
  ),
  topic("📡", "Scanning &amp; Enumeration", "PenTest+ • Discovery",
    card("HOST/PORT", "Nmap Essentials",
         "The workhorse: discover hosts, open ports, service versions, and OS, then run NSE scripts for deeper enumeration.",
         "<span class='com'># SYN scan + version + default scripts + OS, all ports</span>\n"
         "<span class='fn'>nmap</span> -sS -sV -sC -O -p- -T4 10.0.0.5\n"
         "<span class='com'># Targeted UDP + NSE vuln scripts</span>\n"
         "<span class='fn'>nmap</span> -sU -p 53,161 --script vuln 10.0.0.5"),
    card("ENUM", "Service Enumeration",
         "Pull users, shares, and config from exposed services: SMB (enum4linux, smbclient), SNMP (snmpwalk), LDAP, and NFS showmount."),
    tbl(["Nmap Flag", "Meaning"],
        [["-sS / -sT / -sU", "SYN / TCP-connect / UDP scan"],
         ["-sV / -O", "Service version / OS detection"],
         ["-sC / --script", "Default / chosen NSE scripts"],
         ["-p- / -p 80,443", "All ports / specific ports"],
         ["-T0…-T5", "Timing: stealthy → aggressive"],
         ["-Pn", "Skip host discovery (assume up)"]])
  ),
  topic("💥", "Exploitation", "PenTest+ • Attacks",
    card("FRAMEWORK", "Metasploit &amp; searchsploit",
         "Find a matching exploit, configure it, and fire. Meterpreter gives a powerful post-exploitation session.",
         "<span class='com'># Find, then use an exploit</span>\n"
         "<span class='fn'>searchsploit</span> apache 2.4\n"
         "<span class='fn'>msfconsole</span> -q\n"
         "<span class='kw'>use</span> exploit/multi/handler\n"
         "<span class='kw'>set</span> PAYLOAD windows/meterpreter/reverse_tcp\n"
         "<span class='kw'>set</span> LHOST 10.0.0.9 ; <span class='kw'>run</span>"),
    card("PASSWORDS", "Credential Attacks",
         "Online brute/spray with Hydra; offline cracking with John or Hashcat against captured hashes. Beware lockout policies when spraying."),
    card("WEB", "Web Exploitation",
         "sqlmap automates SQL injection; Burp Suite / ZAP intercept and tamper requests for XSS, IDOR, auth flaws, and SSRF."),
    tbl(["Tool", "Purpose"],
        [["Metasploit", "Exploit framework + payloads"],
         ["searchsploit / Exploit-DB", "Public exploit lookup"],
         ["Hydra / Medusa", "Online password attacks"],
         ["John / Hashcat", "Offline hash cracking"],
         ["sqlmap", "Automated SQL injection"],
         ["Burp Suite / ZAP", "Web proxy &amp; testing"]])
  ),
  topic("🔝", "Post-Exploitation &amp; PrivEsc", "PenTest+ • Foothold",
    card("PRIVESC", "Escalate Privileges",
         "Linux: check sudo rights, SUID binaries, cron, and kernel exploits. Windows: weak service perms, unquoted paths, token impersonation, AlwaysInstallElevated.",
         "<span class='com'># Linux privesc quick checks</span>\n"
         "<span class='fn'>sudo</span> -l\n"
         "<span class='fn'>find</span> / -perm -4000 -type f 2>/dev/null\n"
         "<span class='fn'>uname</span> -a   <span class='com'># kernel version for exploits</span>"),
    card("LATERAL", "Move &amp; Persist",
         "Spread with pass-the-hash, PsExec, WinRM, or RDP; plant persistence (services, scheduled tasks, SSH keys). Map AD attack paths with BloodHound."),
    card("PIVOT", "Pivoting &amp; Exfil",
         "Tunnel into segmented networks with SSH port-forwards or proxychains; stage and exfiltrate data; clean logs only if the RoE allows."),
    tbl(["Technique", "Tool / Method"],
        [["Enumeration", "LinPEAS / WinPEAS"],
         ["Credential dump", "Mimikatz, secretsdump"],
         ["AD attack paths", "BloodHound / SharpHound"],
         ["Pass-the-Hash", "impacket, CrackMapExec"],
         ["Tunneling / pivot", "proxychains, SSH -L/-D, Chisel"]])
  ),
  topic("🌐", "Web, Wireless &amp; Reporting", "PenTest+ • Specialized",
    card("WIRELESS", "Wi-Fi Attacks",
         "Capture handshakes and crack with aircrack-ng, abuse WPS, or stand up an evil twin / deauth to harvest credentials."),
    card("REPORTING", "The Real Deliverable",
         "An executive summary plus detailed findings: each with risk rating, evidence, impact, and concrete remediation. Offer a retest to confirm fixes."),
    tbl(["OWASP Top 10 (2021)", "Risk"],
        [["A01", "Broken Access Control"],
         ["A02", "Cryptographic Failures"],
         ["A03", "Injection (SQLi, XSS)"],
         ["A04", "Insecure Design"],
         ["A05", "Security Misconfiguration"],
         ["A06", "Vulnerable Components"],
         ["A07", "Auth Failures"],
         ["A08", "Software / Data Integrity"],
         ["A09", "Logging &amp; Monitoring Failures"],
         ["A10", "Server-Side Request Forgery"]])
  ),
]

# =========================================================================
# LINUX / SYSTEMS  (Linux+, A+)
# =========================================================================
LINUX = [
  topic("📁", "Filesystem &amp; Navigation", "Linux+ • FHS",
    card("LAYOUT", "Filesystem Hierarchy (FHS)",
         "Everything hangs off / (root). Config in /etc, logs &amp; variable data in /var, users in /home, binaries in /bin and /usr."),
    card("FIND", "Locating Files",
         "find walks the tree live with rich filters; locate is instant but uses a database (updatedb).",
         "<span class='com'># Logs modified in the last 7 days</span>\n"
         "<span class='fn'>find</span> /var/log -name '*.log' -mtime -7\n"
         "<span class='fn'>locate</span> sshd_config"),
    tbl(["Path", "Holds"],
        [["/etc", "System &amp; service config"],
         ["/var", "Logs, mail, spool, web data"],
         ["/home", "User home directories"],
         ["/usr", "User programs &amp; libraries"],
         ["/bin /sbin", "Essential / admin binaries"],
         ["/proc /sys", "Kernel &amp; process info (virtual)"],
         ["/opt", "Add-on / third-party software"]])
  ),
  topic("📝", "File Ops &amp; Text Processing", "Linux+ • CLI",
    card("FILES", "Manage &amp; View",
         "cp / mv / rm / mkdir / touch / ln manage files; cat / less / head / tail view them. tail -f follows a live log."),
    card("TEXT", "grep, sed, awk &amp; Pipes",
         "Chain small tools with pipes (|) and redirection (&gt; &gt;&gt; 2&gt;&amp;1) to slice text. grep filters, sed edits, awk handles columns.",
         "<span class='com'># Top source IPs hitting 404s</span>\n"
         "<span class='fn'>cat</span> access.log | <span class='fn'>grep</span> ' 404 ' | "
         "<span class='fn'>awk</span> '{print $1}' | <span class='fn'>sort</span> | "
         "<span class='fn'>uniq</span> -c | <span class='fn'>sort</span> -rn | <span class='fn'>head</span>")
  ),
  topic("🔐", "Permissions &amp; Ownership", "Linux+ • Security",
    card("MODEL", "rwx for User / Group / Other",
         "Three triads of read(4)/write(2)/execute(1). chmod sets them numerically or symbolically; chown / chgrp set ownership; umask sets defaults.",
         "<span class='com'># rwxr-xr-x  then add exec for owner, remove write for group</span>\n"
         "<span class='fn'>chmod</span> 755 deploy.sh\n"
         "<span class='fn'>chmod</span> u+x,g-w report.txt\n"
         "<span class='fn'>chown</span> alice:devs report.txt"),
    card("SPECIAL", "SUID / SGID / Sticky",
         "SUID (4000) runs as the file owner — a classic privesc target. SGID (2000) inherits group. Sticky (1000) on /tmp lets only owners delete their files."),
    tbl(["Octal", "Symbolic", "Meaning"],
        [["7", "rwx", "Read, write, execute"],
         ["6", "rw-", "Read, write"],
         ["5", "r-x", "Read, execute"],
         ["4", "r--", "Read only"],
         ["755", "rwxr-xr-x", "Common for scripts/dirs"],
         ["644", "rw-r--r--", "Common for files"]])
  ),
  topic("👤", "Users, Groups &amp; Privilege", "Linux+ • IAM",
    card("ACCOUNTS", "Where Identity Lives",
         "/etc/passwd lists accounts, /etc/shadow stores password hashes (root-only), /etc/group defines groups. Manage with useradd / usermod / passwd."),
    card("ELEVATE", "sudo vs. su",
         "su switches to another user (needs their password); sudo runs a single command with elevated rights per /etc/sudoers (use visudo to edit safely)."),
    tbl(["File", "Purpose"],
        [["/etc/passwd", "User accounts (no passwords)"],
         ["/etc/shadow", "Hashed passwords (root-only)"],
         ["/etc/group", "Group memberships"],
         ["/etc/sudoers", "Who may run what as whom"]])
  ),
  topic("⚙️", "Processes &amp; Services", "Linux+ • A+",
    card("PROCESSES", "Inspect &amp; Signal",
         "ps / top / htop show running processes. kill sends signals: SIGTERM(15) asks nicely, SIGKILL(9) forces. nohup / &amp; / bg / fg manage jobs.",
         "<span class='com'># Find and stop a process</span>\n"
         "<span class='fn'>ps</span> aux | <span class='fn'>grep</span> nginx\n"
         "<span class='fn'>kill</span> -15 1337    <span class='com'># graceful</span>\n"
         "<span class='fn'>kill</span> -9 1337     <span class='com'># force</span>"),
    card("SERVICES", "systemd",
         "systemctl controls services and boot behavior; journalctl reads the systemd log.",
         "<span class='fn'>systemctl</span> status sshd\n"
         "<span class='fn'>systemctl</span> enable --now nginx\n"
         "<span class='fn'>journalctl</span> -u sshd -n 50 --no-pager"),
    tbl(["Signal", "Number", "Effect"],
        [["SIGHUP", "1", "Reload config"],
         ["SIGINT", "2", "Interrupt (Ctrl+C)"],
         ["SIGKILL", "9", "Force kill (uncatchable)"],
         ["SIGTERM", "15", "Graceful terminate (default)"],
         ["SIGSTOP", "19", "Pause process"]])
  ),
  topic("📦", "Package Management", "Linux+ • Distros",
    card("WHY", "Packages &amp; Repos",
         "Package managers resolve dependencies and pull signed software from repositories. The tool depends on the distro family."),
    tbl(["Family", "Manager", "Install / Update"],
        [["Debian / Ubuntu", "apt, dpkg", "apt install / apt update &amp;&amp; apt upgrade"],
         ["RHEL / Fedora", "dnf, yum, rpm", "dnf install / dnf upgrade"],
         ["Arch", "pacman", "pacman -S / pacman -Syu"],
         ["Universal", "snap, flatpak", "snap install / flatpak install"]])
  ),
  topic("🌐", "Networking (CLI)", "Linux+ • Net",
    card("INSPECT", "Interfaces &amp; Sockets",
         "ip replaces ifconfig for addresses and routes; ss (or netstat) lists listening ports and connections.",
         "<span class='fn'>ip</span> a            <span class='com'># addresses</span>\n"
         "<span class='fn'>ss</span> -tulpn       <span class='com'># listening TCP/UDP + PID</span>\n"
         "<span class='fn'>ip</span> route"),
    card("CONNECT", "Transfer &amp; Remote",
         "curl / wget fetch URLs; ssh / scp / rsync handle remote shells and sync. Firewall via ufw, firewalld, or raw iptables/nftables.",
         "<span class='fn'>ssh</span> -i key.pem user@10.0.0.5\n"
         "<span class='fn'>rsync</span> -avz ./site/ user@host:/var/www/\n"
         "<span class='fn'>curl</span> -sI https://example.com")
  ),
  topic("🛡️", "Shell, Cron &amp; Hardening", "Linux+ • SecOps",
    card("SHELL", "Bash Environment",
         "Variables and PATH live in the shell; persistent settings go in ~/.bashrc or /etc/profile. export makes a variable available to child processes."),
    card("SCHEDULE", "cron &amp; systemd timers",
         "crontab -e schedules recurring jobs; at runs one-off jobs; systemd timers are the modern alternative with logging.",
         "<span class='com'># min hr dom mon dow   command</span>\n"
         "0 2 * * *   /usr/bin/backup.sh    <span class='com'># 02:00 every day</span>\n"
         "*/15 * * * * /usr/bin/healthcheck  <span class='com'># every 15 min</span>"),
    card("HARDEN", "Baseline Hardening",
         "Use SSH keys (disable password &amp; root login), keep patched, run fail2ban, and enforce MAC with SELinux or AppArmor. Watch /var/log for anomalies."),
    tbl(["Cron Field", "Range"],
        [["Minute", "0–59"],
         ["Hour", "0–23"],
         ["Day of month", "1–31"],
         ["Month", "1–12"],
         ["Day of week", "0–6 (Sun=0)"]])
  ),
]

# =========================================================================
# SHORTCUTS  (+ DoD quick reference)
# =========================================================================
SHORTCUTS = [
  topic("🪟", "Windows", "Shortcuts • OS",
    tbl(["Keys", "Action"],
        [["Win + L", "Lock screen"],
         ["Win + D", "Show / hide desktop"],
         ["Win + E", "Open File Explorer"],
         ["Win + R", "Run dialog"],
         ["Win + Shift + S", "Snip a screenshot"],
         ["Win + . ", "Emoji picker"],
         ["Ctrl + Shift + Esc", "Task Manager"],
         ["Alt + Tab", "Switch windows"],
         ["Win + Tab", "Task view"]])
  ),
  topic("🍎", "macOS", "Shortcuts • OS",
    tbl(["Keys", "Action"],
        [["Cmd + Space", "Spotlight search"],
         ["Cmd + Tab", "Switch apps"],
         ["Cmd + W / Q", "Close window / quit app"],
         ["Cmd + Shift + 4", "Screenshot selection"],
         ["Cmd + `", "Cycle app windows"],
         ["Cmd + Opt + Esc", "Force quit"],
         ["Ctrl + Cmd + Q", "Lock screen"],
         ["Cmd + Shift + .", "Show hidden files"]])
  ),
  topic("⌨️", "Terminal / Bash", "Shortcuts • CLI",
    tbl(["Keys", "Action"],
        [["Ctrl + C", "Kill current command"],
         ["Ctrl + Z", "Suspend to background"],
         ["Ctrl + R", "Reverse history search"],
         ["Ctrl + A / E", "Jump to line start / end"],
         ["Ctrl + U / K", "Cut to start / end of line"],
         ["Ctrl + W", "Delete previous word"],
         ["Ctrl + L", "Clear screen"],
         ["!!", "Repeat last command"],
         ["Ctrl + D", "Logout / EOF"]])
  ),
  topic("✏️", "Vim", "Shortcuts • Editor",
    card("MODES", "Modal Editing",
         "Vim starts in Normal mode. Press i or a to Insert, Esc to return. Commands begin with : in Normal mode."),
    tbl(["Keys", "Action"],
        [["i / a / o", "Insert before / after / new line"],
         [":w  :q  :wq", "Write, quit, write+quit"],
         [":q!", "Quit without saving"],
         ["dd / yy / p", "Delete / yank / paste line"],
         ["/text  then n", "Search, next match"],
         ["gg / G", "Top / bottom of file"],
         [":%s/old/new/g", "Replace all"]])
  ),
  topic("💻", "VS Code", "Shortcuts • Editor",
    tbl(["Keys", "Action"],
        [["Ctrl/Cmd + P", "Quick open file"],
         ["Ctrl/Cmd + Shift + P", "Command palette"],
         ["Ctrl + ` ", "Toggle terminal"],
         ["Ctrl/Cmd + /", "Toggle comment"],
         ["Ctrl/Cmd + B", "Toggle sidebar"],
         ["Ctrl/Cmd + Shift + F", "Search across files"],
         ["F2", "Rename symbol"],
         ["Alt + ↑ / ↓", "Move line up / down"]])
  ),
  topic("🖥️", "tmux &amp; Browser", "Shortcuts • Tools",
    card("TMUX", "Prefix = Ctrl + B",
         "Press the prefix, then a key: c new window, n/p next/prev, % split vertical, \" split horizontal, d detach, arrows to move between panes."),
    tbl(["Browser Keys", "Action"],
        [["Ctrl/Cmd + T / W", "New / close tab"],
         ["Ctrl/Cmd + Shift + T", "Reopen closed tab"],
         ["Ctrl/Cmd + L", "Focus address bar"],
         ["Ctrl/Cmd + F", "Find on page"],
         ["Ctrl + Tab", "Next tab"],
         ["Ctrl/Cmd + Shift + N", "Private window"]])
  ),
  topic("🎖️", "DoD Quick Reference", "Shortcuts • DoD",
    card("CONTEXT", "Networks &amp; Access",
         "DoD work spans classification domains and PKI-based identity. The CAC is the smart-card credential for authentication and digital signing."),
    tbl(["Term", "Meaning"],
        [["CAC", "Common Access Card (smart-card credential)"],
         ["PKI", "Public Key Infrastructure (certs/keys)"],
         ["NIPRNet", "Unclassified DoD network"],
         ["SIPRNet", "Secret-level classified network"],
         ["JWICS", "Top Secret / SCI network"],
         ["RMF", "Risk Management Framework (NIST 800-37)"],
         ["ATO / IATT", "Authorization / Interim Auth to Test"],
         ["eMASS", "Enterprise Mission Assurance Support Service"],
         ["STIG", "Security Technical Implementation Guide"],
         ["SCAP", "Security Content Automation Protocol"],
         ["POA&amp;M", "Plan of Action &amp; Milestones"],
         ["IAVA", "Information Assurance Vulnerability Alert"],
         ["DISA", "Defense Information Systems Agency"],
         ["FISMA", "Federal Information Security Modernization Act"]])
  ),
]

# =========================================================================
# MILITARY STAFF CODES  (Continental Staff System)
# =========================================================================
MILITARY = [
  topic("🎖️", "Staff System Overview", "Military • Doctrine",
    card("SYSTEM", "The Continental Staff System",
         "Modern militaries number staff sections 1–9 by function. A letter prefix shows the echelon and service, so S2, G2, and J2 are all Intelligence at different levels."),
    card("READING", "Decode Any Code",
         "Read the letter then the number: letter = level/service, number = function. Example — J6 is Joint Communications/Cyber; S4 is unit-level Logistics."),
    tbl(["Prefix", "Echelon / Service"],
        [["S", "Battalion &amp; Brigade staff"],
         ["G", "Division and higher (general staff)"],
         ["N", "Navy staff"],
         ["A", "Air Force staff"],
         ["J", "Joint (multi-service) staff"],
         ["C", "Combined / multinational staff"]])
  ),
  topic("🔢", "Staff Functions 1–9", "Military • Sections",
    card("FUNCTIONS", "What Each Number Owns",
         "The numbered sections are consistent across echelons; only the prefix changes with level and service."),
    tbl(["Number", "Function", "Examples"],
        [["1", "Personnel / Administration", "S1, G1, J1"],
         ["2", "Intelligence", "S2, G2, J2"],
         ["3", "Operations", "S3, G3, J3"],
         ["4", "Logistics", "S4, G4, J4"],
         ["5", "Plans / Strategy", "S5, G5, J5"],
         ["6", "Signal / Communications / Cyber", "S6, G6, J6"],
         ["7", "Training / Force Development", "S7, G7, J7"],
         ["8", "Resource Management / Finance", "G8, J8"],
         ["9", "Civil-Military Operations", "S9, G9, J9"]])
  ),
  topic("⚓", "Common Codes Decoded", "Military • Reference",
    tbl(["Code", "Meaning"],
        [["J2", "Joint Intelligence"],
         ["J3", "Joint Operations"],
         ["J6", "Joint Comms / Cyber / C4 systems"],
         ["G3", "Division Operations"],
         ["S1", "Battalion Personnel / Admin"],
         ["S4", "Battalion Logistics"],
         ["N2", "Naval Intelligence"],
         ["A3", "Air Force Operations"],
         ["XO", "Executive Officer (deputy commander)"],
         ["NCO / SNCO", "Non-Commissioned / Senior NCO"]])
  ),
]

# =========================================================================
# LIFESTYLE & PHILOSOPHY
# =========================================================================
LIFE = [
  topic("🏛️", "Stoicism", "Philosophy • Virtue Ethics",
    card("CORE", "The Dichotomy of Control",
         "Focus only on what is up to you — your judgments and actions — and accept the rest. Live by the four virtues: wisdom, justice, courage, temperance."),
    card("FIGURES", "The Big Three",
         "Marcus Aurelius (Meditations), Epictetus (Enchiridion), and Seneca (Letters). Roots in Zeno of Citium, c. 300 BCE."),
    card("PRACTICE", "Daily Exercises",
         "Negative visualization (premeditatio malorum), memento mori (remember mortality), and amor fati (love your fate) build resilience and gratitude.")
  ),
  topic("♟️", "Machiavellianism", "Philosophy • Political Realism",
    card("SOURCE", "The Prince (1532)",
         "Niccolò Machiavelli analyzed power as it is, not as it should be. A ruler must master virtù (skill/decisiveness) to manage fortuna (chance)."),
    card("IDEAS", "Realpolitik",
         "Outcomes can justify hard means; it is safer to be feared than loved if you cannot be both. Pragmatic statecraft over idealism."),
    card("NOTE", "Two Meanings",
         "Distinguish the political philosophy from the psychology term 'Machiavellianism' — a dark-triad trait describing manipulative, self-serving behavior.")
  ),
  topic("🧠", "Psychology", "Lifestyle • Mind",
    card("SCHOOLS", "Major Approaches",
         "Psychodynamic (unconscious drives), behavioral (conditioning), cognitive (thinking patterns), and humanistic (growth &amp; self-actualization)."),
    card("APPLIED", "Useful Frameworks",
         "CBT links thoughts→feelings→behavior. Classical vs. operant conditioning explains learned responses. Maslow's hierarchy ranks human needs. The DSM-5 is the diagnostic standard (for clinicians, not self-diagnosis)."),
    tbl(["Cognitive Bias", "What It Is"],
        [["Confirmation bias", "Favoring info that fits beliefs"],
         ["Anchoring", "Over-weighting the first number seen"],
         ["Dunning-Kruger", "Low skill, high confidence"],
         ["Sunk cost", "Continuing because of past investment"],
         ["Availability", "Judging by what comes to mind easily"]])
  ),
  topic("☸️", "Buddhism", "Philosophy • Eastern",
    card("CORE", "Four Noble Truths",
         "Life contains suffering (dukkha); craving causes it; it can cease; and the Eightfold Path is the way out. Reality is marked by impermanence and non-self (anatta)."),
    card("SCHOOLS", "Traditions",
         "Theravada (elder teaching), Mahayana (great vehicle), Zen (direct insight), and Vajrayana (Tibetan). Meditation (samatha &amp; vipassana) is central."),
    tbl(["Eightfold Path", "Group"],
        [["Right View / Intention", "Wisdom"],
         ["Right Speech / Action / Livelihood", "Ethics"],
         ["Right Effort / Mindfulness / Concentration", "Mental discipline"]])
  ),
  topic("☯️", "Taoism", "Philosophy • Eastern",
    card("CORE", "The Tao &amp; Wu Wei",
         "The Tao is the natural way underlying everything. Wu wei — effortless action — means moving with nature's flow rather than forcing it."),
    card("FIGURES", "Texts &amp; Symbols",
         "Lao Tzu's Tao Te Ching and Zhuangzi's writings are foundational. Yin-yang expresses complementary opposites in dynamic balance.")
  ),
  topic("🌌", "Existentialism", "Philosophy • Modern",
    card("CORE", "Existence Precedes Essence",
         "We are not born with a fixed purpose; we create meaning through free choices and bear full responsibility for them."),
    card("THEMES", "Freedom, Absurd, Authenticity",
         "Camus framed the absurd (seeking meaning in a silent universe); the answer is to live authentically rather than in 'bad faith'."),
    card("FIGURES", "Key Thinkers",
         "Kierkegaard, Nietzsche, Sartre, Camus, and Simone de Beauvoir — spanning religious and atheist existentialism.")
  ),
  topic("◻️", "Minimalism", "Lifestyle • Intentionality",
    card("CORE", "Less, But Better",
         "Own and do fewer things, chosen deliberately, so attention and resources go to what matters most. Subtraction as a path to clarity."),
    card("PRACTICE", "Applying It",
         "Declutter to essentials, resist mindless consumption, and extend the idea to time and screens (digital minimalism: tools serve values, not the reverse).")
  ),
  topic("🌙", "Wicca", "Spirituality • Modern Pagan",
    card("CORE", "Rede &amp; Threefold Law",
         "A modern nature-based religion popularized by Gerald Gardner. The Wiccan Rede — 'an it harm none, do what ye will' — and the Threefold Law (energy returns thrice) guide ethics."),
    card("PRACTICE", "Deity &amp; Ritual",
         "Many honor a Goddess and God and mark eight seasonal sabbats. Ritual tools include the athame, chalice, wand, and pentacle."),
    tbl(["Wheel of the Year", "~Date"],
        [["Samhain", "Oct 31"],
         ["Yule", "Winter solstice"],
         ["Imbolc", "Feb 1–2"],
         ["Ostara", "Spring equinox"],
         ["Beltane", "May 1"],
         ["Litha", "Summer solstice"],
         ["Lughnasadh", "Aug 1"],
         ["Mabon", "Autumn equinox"]])
  ),
  topic("🌿", "Paganism", "Spirituality • Umbrella",
    card("CORE", "A Broad Family",
         "An umbrella for nature-centered and often polytheistic or animistic spiritualities outside the Abrahamic mainstream. Reverence for nature and cycles is common."),
    card("PATHS", "Reconstructionism",
         "Many revive historical traditions: Heathenry / Ásatrú (Norse), Hellenism (Greek), Kemeticism (Egyptian), and Celtic paths.")
  ),
  topic("🌳", "Druidism", "Spirituality • Nature Path",
    card("CORE", "Modern Druidry",
         "A contemporary nature spirituality inspired by Celtic culture, honoring the land, ancestors, and the changing seasons. Awen names creative/divine inspiration."),
    card("PRACTICE", "Community &amp; Cycle",
         "Practitioners gather in groves and observe seasonal festivals. Modern orders include OBOD and ADF; emphasis is on creativity, ecology, and reflection.")
  ),
]

# ---- domain registry (anchors → fragments) -------------------------------
DOMAINS = [
  dict(name="PenTest",  sentinel="<!-- PENTEST-DOMAIN v1 -->",  topics=PENTEST,
       anchors=["<!-- /domain-body pentest -->", "<!-- /domain-body pen -->",
                "<!-- /pentest -->", "<!-- /domain pentest -->"]),
  dict(name="Linux",    sentinel="<!-- LINUX-DOMAIN v1 -->",    topics=LINUX,
       anchors=["<!-- /domain-body linux -->", "<!-- /domain-body systems -->",
                "<!-- /domain-body linux-systems -->", "<!-- /linux -->"]),
  dict(name="Shortcuts", sentinel="<!-- SHORTCUTS-DOMAIN v1 -->", topics=SHORTCUTS,
       anchors=["<!-- /domain-body shortcuts -->", "<!-- /domain-body keys -->",
                "<!-- /shortcuts -->", "<!-- /domain shortcuts -->"]),
  dict(name="Military", sentinel="<!-- MILSTAFF-DOMAIN v1 -->", topics=MILITARY,
       anchors=["<!-- /domain-body military -->", "<!-- /domain-body milstaff -->",
                "<!-- /domain-body staff -->", "<!-- /military -->"]),
  dict(name="Lifestyle", sentinel="<!-- LIFESTYLE-DOMAIN v1 -->", topics=LIFE,
       anchors=["<!-- /domain-body lifestyle -->", "<!-- /domain-body philosophy -->",
                "<!-- /domain-body life -->", "<!-- /lifestyle -->", "<!-- /philosophy -->"]),
]

TABLE_CSS = """/* === ref-table v1 === */
.ai-table{width:100%;border-collapse:collapse;margin:14px 0;font-size:.9rem}
.ai-table th,.ai-table td{padding:8px 10px;text-align:left;vertical-align:top;border-bottom:1px solid var(--border,#2a2f3a)}
.ai-table th{color:var(--cyan,#56d4dd);font-weight:600;border-bottom:2px solid var(--cyan,#56d4dd)}
.ai-table td:first-child{color:var(--amber,#e3b341);font-weight:600;white-space:nowrap}
.ai-table tbody tr:hover td{background:rgba(127,127,127,.08)}"""

# ---- patch logic ---------------------------------------------------------
def patch_html(text):
    report = []
    for d in DOMAINS:
        if d["sentinel"] in text:
            report.append((d["name"], "skip (already injected)")); continue
        hit = next((a for a in d["anchors"] if a in text), None)
        if not hit:
            report.append((d["name"], "ERROR: no anchor (tried " + ", ".join(d["anchors"]) + ")")); continue
        block = d["sentinel"] + "\n" + "\n".join(d["topics"]) + "\n"
        text = text.replace(hit, block + hit, 1)
        report.append((d["name"], f"injected before {hit}"))
    return text, report

def patch_css(text):
    if ".ai-table{" in text:
        return text, "skip (table css already present)"
    return text.rstrip() + "\n\n" + TABLE_CSS + "\n", "appended table css"

def main():
    write = "--write" in sys.argv
    d = sys.argv[sys.argv.index("--dir") + 1] if "--dir" in sys.argv else "."
    ipath, cpath = os.path.join(d, "index.html"), os.path.join(d, "style.css")
    print("DOMAINS patch \u2014", "WRITE" if write else "DRY-RUN (add --write to apply)")

    if os.path.exists(ipath):
        src = open(ipath, encoding="utf-8").read()
        out, report = patch_html(src)
        for name, status in report:
            print(f"  {name:10} {status}")
        if write and out != src:
            shutil.copy(ipath, ipath + ".bak")
            open(ipath, "w", encoding="utf-8").write(out)
        print(f"  index.html total {len(out) - len(src):+d} chars")
    else:
        print(f"  index.html MISSING ({ipath})")

    if os.path.exists(cpath):
        src = open(cpath, encoding="utf-8").read()
        out, status = patch_css(src)
        if write and out != src:
            shutil.copy(cpath, cpath + ".bak")
            open(cpath, "w", encoding="utf-8").write(out)
        print(f"  style.css  {status} ({len(out) - len(src):+d} chars)")
    else:
        print(f"  style.css  MISSING ({cpath})")

    print("  script.js  no changes needed (new topics load with existing JS)")
    if not write:
        print("\nLooks right? Apply with:  python patch_domains.py --write")

if __name__ == "__main__":
    main()
