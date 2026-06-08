#!/usr/bin/env python3
"""Wave 41: beginner-friendly content additions across 5 domains."""
import re
from html.parser import HTMLParser

S_PENTEST = "<!-- BEGINNER41-PENTEST v1 -->"
A_PENTEST = "<!-- /domain-body pentest -->"
C_PENTEST = S_PENTEST + """
<div class="topic">
  <div class="topic-header">
    <span class="topic-badge">Beginner</span>
    <h3>Reading an Nmap Scan Like a Pro</h3>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <span class="concept-label">Scope first</span>
      <h4 class="concept-title">Only scan what you're authorized to scan</h4>
      <p class="concept-desc">Network scanning against systems you don't own or have written authorization to test can be
      illegal — even a "harmless" port scan can trigger intrusion alerts, violate acceptable-use policies, or break
      laws depending on jurisdiction. Everything below assumes a home lab, a CTF range, or a signed engagement scope
      document. The goal is to understand what a scan is actually telling you — both as an attacker's recon step and as
      something your own monitoring tools should be able to detect.</p>
    </div>
    <div class="concept-card">
      <span class="concept-label">Concept</span>
      <h4 class="concept-title">What a port scan is actually asking</h4>
      <p class="concept-desc">A port scan sends carefully-crafted packets to a range of ports and studies the responses to
      infer what's running. It's less "breaking in" and more "knocking on every door on the street and noting which ones
      answer, which ones politely say 'go away,' and which ones never respond at all." Each of those three outcomes means
      something different — and confusing them is the most common beginner mistake.</p>
      <table class="ai-table">
        <tr><th>Nmap state</th><th>What it means</th><th>Why it matters</th></tr>
        <tr><td>open</td><td>Something is actively listening and accepted the connection attempt</td><td>A real, running service — the most actionable finding</td></tr>
        <tr><td>closed</td><td>The host responded, but explicitly said "nothing is listening here"</td><td>Confirms the host is alive and reachable; just not on this port</td></tr>
        <tr><td>filtered</td><td>No response came back at all — a firewall is likely silently dropping the probe</td><td>Tells you about a defense being present, even though you learned nothing about the service behind it</td></tr>
      </table>
    </div>
    <div class="concept-card">
      <span class="concept-label">Hands-on (lab only)</span>
      <h4 class="concept-title">Reading real scan output</h4>
      <pre class="code-block"><span class="com"># A common starting scan against a lab target</span>
nmap -sV -sC -p- 192.168.56.10

<span class="com"># Sample output, annotated:
#
# PORT     STATE  SERVICE      VERSION
# 22/tcp   open   ssh          OpenSSH 8.9p1 Ubuntu       &lt;- version banner: a clue for vuln research
# 80/tcp   open   http         Apache httpd 2.4.52        &lt;- web server; worth browsing manually
# 139/tcp  open   netbios-ssn  Samba smbd 4.15.13-Ubuntu  &lt;- file sharing; check for anonymous access
# 445/tcp  open   microsoft-ds Samba smbd 4.15.13-Ubuntu
# 3306/tcp closed mysql                                   &lt;- reachable host, but DB isn't exposed here
#
# |_http-title: Apache2 Ubuntu Default Page: It works    &lt;- script output: default page = likely fresh install</span>

<span class="com"># -sV  : detect service/version banners
# -sC  : run nmap's default safe script set (banner grabs, basic enum)
# -p-  : scan all 65,535 ports, not just the common 1,000
# (this is noisy and slow — fine in a lab, a giveaway in a real engagement)</span></pre>
      <p class="concept-desc">Notice how much you can infer before exploiting anything: an outdated Apache banner suggests
      checking for known CVEs; an exposed Samba share suggests testing for anonymous (null session) access; a default
      "It works" page suggests the box was stood up quickly and may not have been hardened yet. Recon is where most of
      the real thinking happens — exploitation is often the easy part once you understand what you're looking at.</p>
    </div>
    <div class="concept-card">
      <span class="concept-label">Mindset</span>
      <h4 class="concept-title">Assume makes an ass out of you and me</h4>
      <p class="concept-desc">A "filtered" port doesn't mean "nothing is there" — it might mean a firewall is hiding a
      critical service from casual scanning. And an "open" port running a service with a familiar name doesn't guarantee
      it's actually that service — administrators sometimes run things on nonstandard ports specifically to throw off
      scans like this. Treat every scan result as a hypothesis to verify, not a fact to act on.</p>
    </div>
  </div>
</div>
""" + "\n" + A_PENTEST

S_GRC = "<!-- BEGINNER41-GRC v1 -->"
A_GRC = "<!-- /domain-body grc -->"
C_GRC = S_GRC + """
<div class="topic">
  <div class="topic-header">
    <span class="topic-badge">Beginner</span>
    <h3>Data Classification – Why "Just Be Careful With Data" Isn't a Policy</h3>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <span class="concept-label">Concept</span>
      <h4 class="concept-title">You can't protect what you haven't labeled</h4>
      <p class="concept-desc">Data classification is the practice of sorting information into categories based on how
      sensitive it is and what would happen if it were exposed — then attaching specific handling rules to each category.
      Without it, every piece of data effectively gets the same treatment, which means either everything is locked down so
      tightly that nobody can get work done, or — far more commonly — sensitive data ends up handled exactly like the
      public marketing brochure sitting next to it.</p>
    </div>
    <div class="concept-card">
      <span class="concept-label">Concept</span>
      <h4 class="concept-title">A typical four-tier classification scheme</h4>
      <table class="ai-table">
        <tr><th>Tier</th><th>Example data</th><th>Typical handling rule</th></tr>
        <tr><td>Public</td><td>Marketing materials, published job postings, press releases</td><td>No restrictions — designed to be shared widely</td></tr>
        <tr><td>Internal</td><td>Org charts, internal wikis, meeting notes, project plans</td><td>Employees only; not for external sharing, but low-risk if briefly exposed</td></tr>
        <tr><td>Confidential</td><td>Customer contracts, financial forecasts, source code, salary bands</td><td>Need-to-know basis; encryption in transit and at rest; access logged</td></tr>
        <tr><td>Restricted</td><td>Health records, payment card data, social security numbers, trade secrets</td><td>Strictly limited access; mandatory encryption; often subject to legal/regulatory requirements (HIPAA, PCI-DSS, GDPR)</td></tr>
      </table>
      <p class="concept-desc">The exact tier names vary by organization (some use "Secret" / "Top Secret" in government
      contexts, others use simple "Tier 1/2/3"), but the underlying logic is always the same: more sensitive data earns
      more restrictive handling, and that handling needs to be written down so people don't have to guess.</p>
    </div>
    <div class="concept-card">
      <span class="concept-label">Hands-on</span>
      <h4 class="concept-title">What classification looks like in daily work</h4>
      <pre class="code-block"><span class="com"># A classification label embedded right in a document header —
# this single line answers "how careful do I need to be with this file?"
# before anyone even opens it.</span>

CLASSIFICATION: CONFIDENTIAL — Internal Distribution Only
Document: Q3 Customer Churn Analysis
Owner: Data &amp; Analytics Team
Handling: Do not forward externally. Store only in the
          approved &quot;Confidential&quot; SharePoint library.
          Do not paste contents into AI assistants or
          external collaboration tools.
Retention: Delete after 3 years per data retention schedule DR-014.

<span class="com"># Some organizations enforce this with technology, not just policy —
# email systems that auto-detect classification labels and block
# external sends, DLP (Data Loss Prevention) tools that scan outgoing
# attachments for SSN/credit-card patterns, etc.</span></pre>
    </div>
    <div class="concept-card">
      <span class="concept-label">Mindset</span>
      <h4 class="concept-title">Not my circus, not my monkey — except data doesn't respect org charts</h4>
      <p class="concept-desc">"That's the legal team's data, not mine" is exactly the kind of thinking that lets sensitive
      information drift into unprotected places — a shared drive, a personal laptop, a chat export. If you handle data you
      didn't create and aren't sure how it should be classified, the responsible move is to ask the owning team rather
      than guess. The few minutes it takes to confirm "is this Confidential or just Internal?" is far cheaper than
      explaining, after the fact, why it ended up somewhere it shouldn't have.</p>
    </div>
  </div>
</div>
""" + "\n" + A_GRC

S_LINUX = "<!-- BEGINNER41-LINUX v1 -->"
A_LINUX = "<!-- /domain-body linux -->"
C_LINUX = S_LINUX + """
<div class="topic">
  <div class="topic-header">
    <span class="topic-badge">Beginner</span>
    <h3>systemd Essentials – Services, Units, and Why Things Start at Boot</h3>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <span class="concept-label">Concept</span>
      <h4 class="concept-title">systemd is the "stage manager" of a modern Linux system</h4>
      <p class="concept-desc">When a Linux machine boots, dozens of things need to happen in roughly the right order —
      mount filesystems, bring up networking, start the SSH daemon, launch your web server. systemd is the init system
      (process ID 1) responsible for orchestrating all of that, and for keeping track of every running service afterward.
      Almost every major distribution (Ubuntu, Debian, RHEL/CentOS/Fedora, Arch) uses it today, which makes it one of the
      highest-leverage things a beginner can learn — the same handful of commands work nearly everywhere.</p>
    </div>
    <div class="concept-card">
      <span class="concept-label">Concept</span>
      <h4 class="concept-title">Units: the building blocks systemd manages</h4>
      <table class="ai-table">
        <tr><th>Unit type</th><th>Manages</th><th>Example</th></tr>
        <tr><td>.service</td><td>A long-running background process (a daemon)</td><td><code>nginx.service</code>, <code>sshd.service</code></td></tr>
        <tr><td>.timer</td><td>A scheduled job — systemd's modern alternative to cron</td><td><code>logrotate.timer</code></td></tr>
        <tr><td>.socket</td><td>A network or IPC socket that can start a service on demand when something connects</td><td><code>docker.socket</code></td></tr>
        <tr><td>.mount</td><td>A filesystem mount point</td><td><code>home.mount</code></td></tr>
        <tr><td>.target</td><td>A grouping of other units — a "milestone" the system reaches during boot</td><td><code>multi-user.target</code>, <code>graphical.target</code></td></tr>
      </table>
    </div>
    <div class="concept-card">
      <span class="concept-label">Hands-on</span>
      <h4 class="concept-title">The commands you'll reach for constantly</h4>
      <pre class="code-block"><span class="com"># Check whether a service is running right now</span>
systemctl status nginx

<span class="com"># Start / stop / restart a service immediately (this run only)</span>
sudo systemctl start nginx
sudo systemctl stop nginx
sudo systemctl restart nginx
<span class="com"># 'reload' re-reads config without dropping active connections — gentler than restart</span>
sudo systemctl reload nginx

<span class="com"># Make a service start automatically at every future boot
# (note: this does NOT start it right now — the two are independent!)</span>
sudo systemctl enable nginx

<span class="com"># Do both at once — enable AND start immediately</span>
sudo systemctl enable --now nginx

<span class="com"># See WHY something failed — the most useful troubleshooting command here</span>
journalctl -u nginx -n 50 --no-pager

<span class="com"># Follow a service's logs live, the way you'd 'tail -f' a log file</span>
journalctl -u nginx -f</pre>
    </div>
    <div class="concept-card">
      <span class="concept-label">Common pitfall</span>
      <h4 class="concept-title">"I started it, why didn't it survive the reboot?" (and the reverse)</h4>
      <p class="concept-desc"><span class="kw">enable</span> and <span class="kw">start</span> are two completely independent
      switches that beginners frequently conflate:</p>
      <table class="ai-table">
        <tr><th>Command</th><th>Running right now?</th><th>Will it start on next boot?</th></tr>
        <tr><td><code>systemctl start foo</code></td><td>Yes</td><td>No — forgotten on reboot unless also enabled</td></tr>
        <tr><td><code>systemctl enable foo</code></td><td>No — stays stopped until started</td><td>Yes — but won't help you *today*</td></tr>
        <tr><td><code>systemctl enable --now foo</code></td><td>Yes</td><td>Yes</td></tr>
      </table>
      <p class="concept-desc">"I enabled it but it's still not running" and "it was working until the server rebooted" are
      two of the most common systemd tickets — and both trace back to this exact distinction. <strong>Assume makes an ass
      out of you and me</strong>: always run <span class="kw">systemctl status</span> to confirm both the current state
      <em>and</em> whether it's enabled, rather than assuming one implies the other.</p>
    </div>
  </div>
</div>
""" + "\n" + A_LINUX

S_LIFESTYLE = "<!-- BEGINNER41-LIFESTYLE v1 -->"
A_LIFESTYLE = "<!-- /domain-body lifestyle -->"
C_LIFESTYLE = S_LIFESTYLE + """
<div class="topic">
  <div class="topic-header">
    <span class="topic-badge">Beginner</span>
    <h3>Building a Home Lab Without Breaking the Bank</h3>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <span class="concept-label">Why this matters</span>
      <h4 class="concept-title">You learn IT by breaking things you're allowed to break</h4>
      <p class="concept-desc">Reading about Linux, networking, or virtualization only gets you so far — at some point you
      need a place to actually try things, watch them fail, and figure out why. A home lab is exactly that: an
      environment that's entirely yours, where "I broke it" is a learning opportunity instead of an incident report.
      The good news is that a genuinely useful lab doesn't require expensive server hardware — many people start with
      nothing more than the laptop they already own.</p>
    </div>
    <div class="concept-card">
      <span class="concept-label">Concept</span>
      <h4 class="concept-title">Three tiers of home lab, roughly by budget</h4>
      <table class="ai-table">
        <tr><th>Tier</th><th>What it looks like</th><th>What you can practice</th></tr>
        <tr><td>$0 — Virtual only</td><td>VirtualBox or VMware Workstation Player on your existing laptop, running Linux/Windows VMs</td><td>OS administration, networking basics, scripting, vulnerable-VM practice (CTF-style boxes)</td></tr>
        <tr><td>~$100–300 — Single-board / mini PC</td><td>A Raspberry Pi, a used mini PC (e.g. an old Dell Optiplex), or a NAS device</td><td>Always-on services (Pi-hole, file sharing, monitoring dashboards), real hardware troubleshooting</td></tr>
        <tr><td>$300+ — Small cluster / used enterprise gear</td><td>Several mini PCs or a used rack-mount server running a hypervisor (Proxmox, ESXi)</td><td>Virtualization at scale, container orchestration (Kubernetes), simulating multi-server environments</td></tr>
      </table>
      <p class="concept-desc">Most people get more learning value from spending six months deeply exploring a $0 virtual
      lab than from buying $1,000 of gear and never finding time to use it. Start at the bottom of this table — you can
      always grow upward once you've outgrown what virtualization alone can teach you.</p>
    </div>
    <div class="concept-card">
      <span class="concept-label">Hands-on</span>
      <h4 class="concept-title">Your first lab session, start to finish</h4>
      <pre class="code-block"><span class="com"># 1. Install a free hypervisor (VirtualBox shown; VMware Player works too)
#    Download from the official site — never a third-party mirror.</span>

<span class="com"># 2. Download a beginner-friendly Linux ISO</span>
<span class="com">#    Ubuntu Server, Debian, or a purpose-built vulnerable distro
#    like those found on VulnHub or in TryHackMe/HackTheBox labs</span>

<span class="com"># 3. Create a VM with isolated "host-only" or "internal" networking
#    so it can't reach (or be reached from) your real home network —
#    this matters MOST when you're deliberately running vulnerable software</span>

<span class="com"># 4. Once it's running, practice the fundamentals:</span>
ssh labuser@192.168.56.20
sudo apt update &amp;&amp; sudo apt upgrade -y
sudo systemctl status ssh
ip a
df -h

<span class="com"># 5. Take a snapshot BEFORE you experiment — this is the home lab's
#    superpower. Break something? Restore the snapshot and you're
#    back to a clean state in seconds, no consequences.</span></pre>
    </div>
    <div class="concept-card">
      <span class="concept-label">Mindset</span>
      <h4 class="concept-title">Assume makes an ass out of you and me — isolate before you experiment</h4>
      <p class="concept-desc">Before you spin up a deliberately vulnerable VM to practice exploitation, double — then
      triple — check that its network adapter is set to host-only or internal mode, not bridged. A bridged vulnerable
      machine is directly reachable from (and can potentially reach out to) your entire home network and, depending on
      your router, the wider internet. "I assumed it was isolated" is one of the most common — and most avoidable —
      home lab mistakes.</p>
    </div>
  </div>
</div>
""" + "\n" + A_LIFESTYLE

S_THREAT = "<!-- BEGINNER41-THREAT v1 -->"
A_THREAT = "<!-- /domain-body threat -->"
C_THREAT = S_THREAT + """
<div class="topic">
  <div class="topic-header">
    <span class="topic-badge">Beginner</span>
    <h3>The Cyber Kill Chain – Thinking Like the Attacker, Stage by Stage</h3>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <span class="concept-label">Concept</span>
      <h4 class="concept-title">An attack isn't one event — it's a sequence</h4>
      <p class="concept-desc">The Cyber Kill Chain (developed by Lockheed Martin) is a model that breaks an intrusion down
      into a sequence of stages an attacker has to move through, in order, to succeed. Its real value for a defender isn't
      memorizing the stage names — it's the realization that <em>every stage is a chance to stop the attack</em>. You don't
      need to catch every intrusion at the front door; catching it at any single stage breaks the whole chain.</p>
    </div>
    <div class="concept-card">
      <span class="concept-label">Concept</span>
      <h4 class="concept-title">The seven stages, and where defenders can intervene</h4>
      <table class="ai-table">
        <tr><th>Stage</th><th>What the attacker is doing</th><th>A defense that fits here</th></tr>
        <tr><td>1. Reconnaissance</td><td>Researching the target — employee names on LinkedIn, exposed services, leaked credentials</td><td>Limiting public information exposure; monitoring for scanning activity</td></tr>
        <tr><td>2. Weaponization</td><td>Building or obtaining a malicious payload (often off-the-shelf)</td><td>Threat intelligence feeds that flag known tooling and infrastructure</td></tr>
        <tr><td>3. Delivery</td><td>Getting the payload to the target — phishing email, infected USB, compromised website</td><td>Email filtering, web proxies, user awareness training</td></tr>
        <tr><td>4. Exploitation</td><td>Triggering the payload — a user opens the attachment, a vulnerable service is hit</td><td>Patch management, application allow-listing, endpoint protection</td></tr>
        <tr><td>5. Installation</td><td>Establishing persistence — a backdoor, scheduled task, or new service</td><td>EDR tools that flag unusual process trees and new persistence mechanisms</td></tr>
        <tr><td>6. Command &amp; Control (C2)</td><td>Calling home to an attacker-controlled server for further instructions</td><td>Network monitoring for unusual outbound connections; DNS filtering</td></tr>
        <tr><td>7. Actions on Objectives</td><td>The actual goal — data theft, ransomware deployment, sabotage</td><td>Data loss prevention, network segmentation, offline backups</td></tr>
      </table>
    </div>
    <div class="concept-card">
      <span class="concept-label">Hands-on</span>
      <h4 class="concept-title">Mapping a real incident to the chain</h4>
      <pre class="code-block"><span class="com"># A simplified, anonymized incident timeline mapped to kill-chain stages —
# this is the kind of analysis that goes into a post-incident report</span>

Day 1   - Attacker scrapes employee names from the company website
          [STAGE 1: Reconnaissance]

Day 3   - Crafted phishing email sent to 40 employees, spoofing IT support
          [STAGE 3: Delivery — using a generic, purchased phishing kit, STAGE 2]

Day 3   - One employee clicks the link and enters their credentials
          on a cloned login page
          [STAGE 4: Exploitation]

Day 4   - Attacker logs in with stolen credentials, installs a
          scheduled task that re-establishes a connection on reboot
          [STAGE 5: Installation]

Day 4-9 - Compromised account quietly contacts an external server
          every few hours; goes unnoticed amid normal traffic
          [STAGE 6: Command &amp; Control]

Day 10  - Attacker begins exporting files from a shared drive
          — DLP tooling flags the unusual transfer volume and
          the SOC cuts off network access within 12 minutes
          [STAGE 7: Actions on Objectives — INTERRUPTED HERE]</pre>
      <p class="concept-desc">Notice that the chain was broken at stage 7 — late, but not too late. A faster catch at
      stage 6 (alerting on the unusual outbound C2 traffic over six days) would have prevented the data exfiltration
      entirely. Every stage that gets caught earlier shrinks the blast radius of everything that follows.</p>
    </div>
    <div class="concept-card">
      <span class="concept-label">Mindset</span>
      <h4 class="concept-title">You can't make someone make the right choice...</h4>
      <p class="concept-desc"><strong>...yet you can pick up the pieces afterwards.</strong> No amount of training
      guarantees that nobody will ever click a phishing link — humans are the part of the chain you can influence but
      never fully control. That's exactly why mature security programs don't rely on stage 3/4 prevention alone. They
      build detection and response capability for stages 5 through 7 too — because when, not if, someone clicks, the
      chain still has several more links where you can catch it.</p>
    </div>
  </div>
</div>
""" + "\n" + A_THREAT


def inject(html, anchor, sentinel, content):
    if sentinel in html:
        return html, False
    idx = html.find(anchor)
    if idx == -1:
        raise SystemExit(f"Anchor not found: {anchor}")
    return html[:idx] + content + "\n" + html[idx:], True


VOID_ELEMENTS = {"area", "base", "br", "col", "embed", "hr", "img", "input",
                 "link", "meta", "param", "source", "track", "wbr"}


class _Checker(HTMLParser):
    def __init__(self):
        super().__init__()
        self.stack = []
        self.stray = 0

    def handle_starttag(self, tag, attrs):
        if tag not in VOID_ELEMENTS:
            self.stack.append(tag)

    def handle_startendtag(self, tag, attrs):
        pass

    def handle_endtag(self, tag):
        if tag in VOID_ELEMENTS:
            return
        if self.stack and self.stack[-1] == tag:
            self.stack.pop()
        elif tag in self.stack:
            while self.stack and self.stack[-1] != tag:
                self.stack.pop()
            if self.stack:
                self.stack.pop()
        else:
            self.stray += 1


def validate(html):
    c = _Checker()
    c.feed(html)
    c.close()
    print("\n  HTML balance check:")
    print("  Unclosed at EOF :", "NONE" if not c.stack else c.stack)
    print("  Stray end tags  :", c.stray)


WAVES = [
    (A_PENTEST, S_PENTEST, C_PENTEST),
    (A_GRC, S_GRC, C_GRC),
    (A_LINUX, S_LINUX, C_LINUX),
    (A_LIFESTYLE, S_LIFESTYLE, C_LIFESTYLE),
    (A_THREAT, S_THREAT, C_THREAT),
]


def main():
    path = "index.html"
    with open(path, "r", encoding="utf-8") as f:
        html = f.read()

    changed_any = False
    for anchor, sentinel, content in WAVES:
        html, changed = inject(html, anchor, sentinel, content)
        print(f"  {sentinel}: {'INJECTED' if changed else 'skipped (already present)'}")
        changed_any = changed_any or changed

    if changed_any:
        with open(path, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"\n  Written {len(html):,} bytes")
    else:
        print("\n  No changes made (all sentinels already present)")

    validate(html)


if __name__ == "__main__":
    main()
