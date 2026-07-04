#!/usr/bin/env python3
"""
patch_beginner_concepts_v24.py — Wave 24: Cloud automation (boto3), NAT/port
forwarding, the ip command, OSINT for defenders, professional ethics.

New sentinels:
  BEGINNER24-SCRIPT v1  — Cloud automation with boto3 (AWS SDK), task scheduling
  BEGINNER24-NET v1     — NAT deep dive, PAT, port forwarding, NAT traversal
  BEGINNER24-LINUX v1   — The ip command (replacing ifconfig), network config
  BEGINNER24-THREAT v1  — OSINT for defenders, attack-surface monitoring
  BEGINNER24-LIFE v1    — Professional ethics in IT, codes of conduct, doing right
"""
from pathlib import Path

SCRIPT_INJECT_ANCHOR = "<!-- /domain-body script -->"
NET_INJECT_ANCHOR    = "<!-- /domain-body net -->"
LINUX_INJECT_ANCHOR  = "<!-- /domain-body linux -->"
THREAT_INJECT_ANCHOR = "<!-- /domain-body threat -->"
LIFE_INJECT_ANCHOR   = "<!-- /domain-body lifestyle -->"

# ─────────────────────────────── SCRIPT wave 24 ──────────────────────────────
SCRIPT_SENTINEL = "<!-- BEGINNER24-SCRIPT v1 -->"
SCRIPT_CONTENT = """
<!-- BEGINNER24-SCRIPT v1 -->
<!-- ── TOPIC: CLOUD AUTOMATION WITH PYTHON ───────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">☁️</span>
    <span class="topic-name">Cloud Automation — Controlling Infrastructure with Code</span>
    <span class="topic-badge">SCRIPT • Cloud</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">CLOUD SDKs</div>
      <div class="concept-title">Every Cloud Action Is an API Call</div>
      <div class="concept-desc">Everything you can click in a cloud console (AWS/Azure/GCP) is really an API call underneath. Cloud SDKs let you make those calls from code — so you can automate provisioning, build self-service tools, generate reports, and respond to events programmatically. <code>boto3</code> is the AWS SDK for Python and the most common starting point.</div>
      <div class="code-block"><span class="com"># pip install boto3</span>
<span class="kw">import</span> boto3

<span class="com"># Credentials come from env vars, ~/.aws/credentials, or IAM role</span>
<span class="com"># NEVER hardcode AWS keys in code</span>

<span class="com"># List all S3 buckets</span>
s3 = boto3.client(<span class="str">"s3"</span>)
<span class="kw">for</span> bucket <span class="kw">in</span> s3.list_buckets()[<span class="str">"Buckets"</span>]:
    <span class="fn">print</span>(bucket[<span class="str">"Name"</span>])

<span class="com"># Upload / download a file</span>
s3.upload_file(<span class="str">"report.pdf"</span>, <span class="str">"my-bucket"</span>, <span class="str">"reports/report.pdf"</span>)
s3.download_file(<span class="str">"my-bucket"</span>, <span class="str">"reports/report.pdf"</span>, <span class="str">"local.pdf"</span>)

<span class="com"># List running EC2 instances</span>
ec2 = boto3.resource(<span class="str">"ec2"</span>)
<span class="kw">for</span> inst <span class="kw">in</span> ec2.instances.<span class="fn">filter</span>(
    Filters=[{<span class="str">"Name"</span>: <span class="str">"instance-state-name"</span>, <span class="str">"Values"</span>: [<span class="str">"running"</span>]}]
):
    <span class="fn">print</span>(inst.id, inst.instance_type, inst.public_ip_address)</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">SECURITY-RELEVANT AUTOMATION</div>
      <div class="concept-title">A Practical Example — Find Public S3 Buckets</div>
      <div class="concept-desc">Misconfigured public S3 buckets are a classic breach cause. Automation lets you audit at scale — exactly the kind of high-value script a cloud security engineer writes.</div>
      <div class="code-block"><span class="kw">import</span> boto3
<span class="kw">from</span> botocore.exceptions <span class="kw">import</span> ClientError

s3 = boto3.client(<span class="str">"s3"</span>)

<span class="kw">for</span> b <span class="kw">in</span> s3.list_buckets()[<span class="str">"Buckets"</span>]:
    name = b[<span class="str">"Name"</span>]
    <span class="kw">try</span>:
        acl = s3.get_bucket_acl(Bucket=name)
        <span class="kw">for</span> grant <span class="kw">in</span> acl[<span class="str">"Grants"</span>]:
            grantee = grant.get(<span class="str">"Grantee"</span>, {})
            <span class="kw">if</span> grantee.get(<span class="str">"URI"</span>, <span class="str">""</span>).endswith(<span class="str">"AllUsers"</span>):
                <span class="fn">print</span>(<span class="str">f"⚠️  PUBLIC bucket: {name}"</span>)
    <span class="kw">except</span> ClientError <span class="kw">as</span> e:
        <span class="fn">print</span>(<span class="str">f"Could not check {name}: {e}"</span>)</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">SCHEDULING WORK</div>
      <div class="concept-title">From cron to Task Queues</div>
      <div class="concept-desc">Automation needs to run on a schedule or in response to events. Options scale with complexity.</div>
      <table class="ai-table">
        <thead><tr><th>Approach</th><th>Best For</th></tr></thead>
        <tbody>
          <tr><td>cron / systemd timers</td><td>Simple recurring jobs on one machine</td></tr>
          <tr><td>APScheduler (Python lib)</td><td>Scheduling inside a running Python app</td></tr>
          <tr><td>Celery + Redis/RabbitMQ</td><td>Distributed background tasks, retries, scale</td></tr>
          <tr><td>Cloud functions (Lambda)</td><td>Event-driven, serverless, pay-per-run</td></tr>
          <tr><td>Airflow / Dagster</td><td>Complex data pipelines with dependencies (DAGs)</td></tr>
        </tbody>
      </table>
    </div>
  </div>
</div>
"""

# ─────────────────────────────── NET wave 24 ─────────────────────────────────
NET_SENTINEL = "<!-- BEGINNER24-NET v1 -->"
NET_CONTENT = """
<!-- BEGINNER24-NET v1 -->
<!-- ── TOPIC: NAT & PORT FORWARDING ──────────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">🔀</span>
    <span class="topic-name">NAT &amp; Port Forwarding — How Private Networks Reach the Internet</span>
    <span class="topic-badge">NET • Essential</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">WHY NAT EXISTS</div>
      <div class="concept-title">Many Private Devices, One Public IP</div>
      <div class="concept-desc">There aren't enough IPv4 addresses for every device. NAT (Network Address Translation) lets a whole network of devices with private IPs (192.168.x.x) share a single public IP. Your home router does this: it translates internal addresses to its one public address on the way out, and remembers which internal device each connection belongs to so replies come back correctly.</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">TYPES OF NAT</div>
      <div class="concept-title">Static, Dynamic, and PAT</div>
      <table class="ai-table">
        <thead><tr><th>Type</th><th>How It Works</th><th>Use</th></tr></thead>
        <tbody>
          <tr><td>Static NAT</td><td>One private IP ↔ one public IP (fixed)</td><td>Exposing a specific internal server</td></tr>
          <tr><td>Dynamic NAT</td><td>Private IPs map to a pool of public IPs</td><td>Less common; needs many public IPs</td></tr>
          <tr><td>PAT / NAT overload</td><td>Many private IPs → one public IP, distinguished by port</td><td>The home router model — by far the most common</td></tr>
        </tbody>
      </table>
      <div class="concept-desc"><strong>PAT</strong> (Port Address Translation) is what "NAT" almost always means in practice. The router tracks connections by (internal IP:port ↔ public IP:port) so dozens of devices share one address.</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">PORT FORWARDING</div>
      <div class="concept-title">Letting the Outside Reach In</div>
      <div class="concept-desc">By default, NAT blocks unsolicited inbound connections (a nice side-effect: a basic firewall). But sometimes you WANT external access to an internal service — a game server, a web server, SSH to your home lab. Port forwarding tells the router: "traffic arriving on public port X → send to internal host:port Y."</div>
      <div class="code-block"><span class="com"># Example port-forward rules on a router</span>
Public :443  → 192.168.1.10:443    <span class="com"># web server</span>
Public :2222 → 192.168.1.20:22     <span class="com"># SSH to lab box</span>

<span class="com"># ⚠️ Security: every forwarded port is exposed to the internet.</span>
<span class="com"># Forward only what you must; prefer a VPN for remote access.</span>

<span class="com"># Linux iptables DNAT (what routers do under the hood)</span>
iptables -t nat -A PREROUTING -p tcp --dport 443 \\
  -j DNAT --to-destination 192.168.1.10:443</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">NAT CHALLENGES</div>
      <div class="concept-title">Why Some Apps Struggle Behind NAT</div>
      <table class="ai-table">
        <thead><tr><th>Issue</th><th>Solution</th></tr></thead>
        <tbody>
          <tr><td>Two peers both behind NAT (VoIP, P2P, gaming)</td><td>STUN/TURN/ICE — NAT traversal protocols</td></tr>
          <tr><td>App needs a stable inbound port</td><td>Port forwarding or UPnP (convenient but risky)</td></tr>
          <tr><td>Tracking which device did what (logging)</td><td>CGNAT complicates attribution at ISP scale</td></tr>
          <tr><td>Reaching home services remotely</td><td>VPN, reverse tunnel, or ZTNA (Tailscale/Cloudflare)</td></tr>
        </tbody>
      </table>
      <div class="concept-desc">Note: <strong>IPv6 largely removes the need for NAT</strong> — there are enough addresses for every device to have a public one (with firewalls, not NAT, providing the security boundary).</div>
    </div>
  </div>
</div>
"""

# ─────────────────────────────── LINUX wave 24 ───────────────────────────────
LINUX_SENTINEL = "<!-- BEGINNER24-LINUX v1 -->"
LINUX_CONTENT = """
<!-- BEGINNER24-LINUX v1 -->
<!-- ── TOPIC: THE IP COMMAND ─────────────────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">🧩</span>
    <span class="topic-name">The ip Command — Modern Linux Networking</span>
    <span class="topic-badge">LINUX • Essential</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">OUT WITH ifconfig</div>
      <div class="concept-title">ip Replaced the Old net-tools</div>
      <div class="concept-desc">The classic commands (<code>ifconfig</code>, <code>route</code>, <code>netstat</code>, <code>arp</code>) are deprecated and often not even installed on modern Linux. The <code>ip</code> command (from iproute2) replaces them all with a consistent syntax: <code>ip OBJECT COMMAND</code>. Learn it — it's what you'll find everywhere now.</div>
      <table class="ai-table">
        <thead><tr><th>Old Command</th><th>New ip Equivalent</th></tr></thead>
        <tbody>
          <tr><td><code>ifconfig</code></td><td><code>ip addr</code></td></tr>
          <tr><td><code>ifconfig eth0 up/down</code></td><td><code>ip link set eth0 up/down</code></td></tr>
          <tr><td><code>route -n</code></td><td><code>ip route</code></td></tr>
          <tr><td><code>arp -a</code></td><td><code>ip neigh</code></td></tr>
          <tr><td><code>netstat -tulpn</code></td><td><code>ss -tulpn</code></td></tr>
        </tbody>
      </table>
    </div>
    <div class="concept-card">
      <div class="concept-label">ADDRESSES & LINKS</div>
      <div class="concept-title">Viewing and Configuring Interfaces</div>
      <div class="code-block"><span class="com"># Show IP addresses</span>
ip addr                        <span class="com"># all interfaces (or: ip a)</span>
ip addr show eth0              <span class="com"># one interface</span>
ip -br addr                    <span class="com"># brief, clean output</span>
ip -4 addr                     <span class="com"># IPv4 only</span>

<span class="com"># Show link (layer 2) state</span>
ip link                        <span class="com"># interfaces up/down, MAC</span>

<span class="com"># Bring an interface up/down</span>
sudo ip link set eth0 up
sudo ip link set eth0 down

<span class="com"># Assign an IP (temporary — lost on reboot)</span>
sudo ip addr add 192.168.1.50/24 dev eth0
sudo ip addr del 192.168.1.50/24 dev eth0</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">ROUTING & NEIGHBORS</div>
      <div class="concept-title">Inspecting the Routing Table</div>
      <div class="code-block"><span class="com"># Show the routing table</span>
ip route                       <span class="com"># (or: ip r)</span>
ip route get 8.8.8.8           <span class="com"># which route/iface for this dest?</span>

<span class="com"># Default gateway line looks like:</span>
<span class="com"># default via 192.168.1.1 dev eth0</span>

<span class="com"># Add/delete routes (temporary)</span>
sudo ip route add 10.0.0.0/24 via 192.168.1.1
sudo ip route del 10.0.0.0/24

<span class="com"># ARP table (IP ↔ MAC mappings on the local link)</span>
ip neigh

<span class="com"># Socket statistics (replaces netstat)</span>
ss -tulpn                      <span class="com"># listening TCP/UDP + process</span>
ss -tn state established       <span class="com"># active connections</span></div>
    </div>
    <div class="concept-card">
      <div class="concept-label">PERSISTENT CONFIG</div>
      <div class="concept-title">Making Changes Survive Reboot</div>
      <div class="concept-desc"><code>ip</code> changes are temporary. To make networking persistent, edit the distro's config system — which varies. Know which your system uses.</div>
      <table class="ai-table">
        <thead><tr><th>System</th><th>Used By</th><th>Config</th></tr></thead>
        <tbody>
          <tr><td>Netplan</td><td>Modern Ubuntu</td><td>YAML in <code>/etc/netplan/</code> → <code>netplan apply</code></td></tr>
          <tr><td>NetworkManager</td><td>Desktop, RHEL/Fedora</td><td><code>nmcli</code> / <code>nmtui</code></td></tr>
          <tr><td>systemd-networkd</td><td>Servers, containers</td><td><code>/etc/systemd/network/*.network</code></td></tr>
          <tr><td>ifupdown</td><td>Older Debian</td><td><code>/etc/network/interfaces</code></td></tr>
        </tbody>
      </table>
    </div>
  </div>
</div>
"""

# ─────────────────────────────── THREAT wave 24 ──────────────────────────────
THREAT_SENTINEL = "<!-- BEGINNER24-THREAT v1 -->"
THREAT_CONTENT = """
<!-- BEGINNER24-THREAT v1 -->
<!-- ── TOPIC: OSINT FOR DEFENDERS ────────────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">🛰️</span>
    <span class="topic-name">OSINT for Defenders — See Yourself as Attackers Do</span>
    <span class="topic-badge">THREAT • Recon</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">WHAT IS OSINT</div>
      <div class="concept-title">Open-Source Intelligence</div>
      <div class="concept-desc">OSINT is intelligence gathered from publicly available sources — no hacking required. Attackers use it to map your organization before striking; <strong>defenders use the same techniques to find their own exposure before attackers do.</strong> Reducing your "attack surface" starts with knowing what's actually out there with your name on it. It's legal, passive, and one of the highest-value defensive exercises.</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">WHAT LEAKS OUT</div>
      <div class="concept-title">Your Public Footprint</div>
      <table class="ai-table">
        <thead><tr><th>Exposure</th><th>Where Attackers Find It</th></tr></thead>
        <tbody>
          <tr><td>Forgotten internet-facing servers</td><td>Shodan, Censys (search by org/IP range)</td></tr>
          <tr><td>Subdomains &amp; shadow IT</td><td>crt.sh (cert transparency), subdomain enumeration</td></tr>
          <tr><td>Employee emails &amp; names</td><td>LinkedIn, Hunter.io, theHarvester</td></tr>
          <tr><td>Leaked credentials</td><td>HaveIBeenPwned, breach databases</td></tr>
          <tr><td>Tech stack &amp; versions</td><td>Job postings, BuiltWith, HTTP headers</td></tr>
          <tr><td>Secrets in code</td><td>Public GitHub repos, gists</td></tr>
          <tr><td>Sensitive documents</td><td>Google dorks (<code>site: filetype:</code>)</td></tr>
        </tbody>
      </table>
    </div>
    <div class="concept-card">
      <div class="concept-label">GOOGLE DORKING</div>
      <div class="concept-title">Advanced Search Operators</div>
      <div class="code-block"><span class="com"># Find exposed files on your own domain</span>
site:example.com filetype:pdf
site:example.com filetype:xlsx
site:example.com ext:sql | ext:env | ext:log

<span class="com"># Find login portals / admin pages</span>
site:example.com inurl:admin | inurl:login

<span class="com"># Find directory listings (often unintended exposure)</span>
site:example.com intitle:"index of"

<span class="com"># Find exposed config / git</span>
site:example.com inurl:.git

<span class="com"># Do this against YOUR OWN org to find leaks before attackers</span></div>
    </div>
    <div class="concept-card">
      <div class="concept-label">DEFENSIVE ACTIONS</div>
      <div class="concept-title">Turning OSINT Into Defense</div>
      <table class="ai-table">
        <thead><tr><th>Finding</th><th>Action</th></tr></thead>
        <tbody>
          <tr><td>Unknown internet-facing host</td><td>Add to inventory, assess, patch or decommission</td></tr>
          <tr><td>Leaked employee credentials</td><td>Force reset, enable MFA, monitor the account</td></tr>
          <tr><td>Secrets in a public repo</td><td>Rotate the secret immediately, scrub history</td></tr>
          <tr><td>Excessive info in job posts</td><td>Generalize tech details in future postings</td></tr>
          <tr><td>Exposed sensitive document</td><td>Remove it, check access logs, review process</td></tr>
        </tbody>
      </table>
      <div class="concept-desc"><strong>Continuous, not one-time:</strong> your attack surface changes constantly as people spin up servers and post online. Many orgs use Attack Surface Management (ASM) tools to monitor this automatically.</div>
    </div>
  </div>
</div>
"""

# ─────────────────────────────── LIFESTYLE wave 24 ───────────────────────────
LIFE_SENTINEL = "<!-- BEGINNER24-LIFE v1 -->"
LIFE_CONTENT = """
<!-- BEGINNER24-LIFE v1 -->
<!-- ── TOPIC: PROFESSIONAL ETHICS IN IT ──────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">⚖️</span>
    <span class="topic-name">Professional Ethics — The Responsibility That Comes With Access</span>
    <span class="topic-badge">LIFESTYLE • Integrity</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">WHY ETHICS MATTERS HERE</div>
      <div class="concept-title">You Hold Keys to the Kingdom</div>
      <div class="concept-desc">IT professionals — especially in security and admin roles — have extraordinary access: to private data, to systems that affect people's lives, to the ability to surveil or disrupt. With that access comes responsibility. Your reputation for integrity is the single most valuable asset in your career; it takes years to build and seconds to destroy. Employers hire trust as much as skill.</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">CORE PRINCIPLES</div>
      <div class="concept-title">Common Threads Across IT Codes of Ethics</div>
      <div class="concept-desc">Organizations like (ISC)², ISACA, and ACM publish codes of ethics. The recurring principles:</div>
      <table class="ai-table">
        <thead><tr><th>Principle</th><th>In Practice</th></tr></thead>
        <tbody>
          <tr><td>Protect the public &amp; common good</td><td>Public safety and trust come before employer or self-interest</td></tr>
          <tr><td>Act with integrity &amp; honesty</td><td>Don't misrepresent your skills, findings, or qualifications</td></tr>
          <tr><td>Respect privacy &amp; confidentiality</td><td>Don't snoop in data you can access but have no business reason to view</td></tr>
          <tr><td>Provide diligent, competent service</td><td>Stay within your competence; keep learning; don't fake it on critical systems</td></tr>
          <tr><td>Avoid conflicts of interest</td><td>Disclose anything that could bias your judgment</td></tr>
          <tr><td>Authorized access only</td><td>"I can" never means "I may" — access requires authorization AND a reason</td></tr>
        </tbody>
      </table>
    </div>
    <div class="concept-card">
      <div class="concept-label">THE "JUST BECAUSE YOU CAN" TRAP</div>
      <div class="concept-title">Access Is Not Permission</div>
      <div class="concept-desc">The most common ethical failure in IT isn't dramatic sabotage — it's curiosity. An admin who reads a colleague's emails "out of curiosity," peeks at executive salaries in a database, or looks up an ex's records. You may have the technical access, but using it without a legitimate business reason is a serious ethical (and often legal) violation. The rule: <strong>access data only when you have both authorization and a genuine work reason.</strong> Assume every access is logged — because it usually is.</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">WHEN YOU'RE PRESSURED</div>
      <div class="concept-title">Doing the Right Thing Under Pressure</div>
      <div class="concept-desc">Sometimes a manager or client pressures you to do something wrong: ignore a vulnerability, falsify a report, cut a security corner to ship faster, delete logs, grant inappropriate access. This is where the mindsets earlier in this guide come together. <strong>"Assume makes an ass of u and me"</strong> — get the request in writing; don't assume you understood the intent or that it's authorized. <strong>"You can't make someone make the right choice, but you can pick up the pieces"</strong> — state your professional objection clearly and in writing, offer the safer alternative, and escalate if needed; if they still choose poorly, you've created a record and done your duty. And <strong>"not my circus, not my monkeys"</strong> protects you from owning the emotional weight of a bad decision that wasn't yours to make.</div>
      <table class="ai-table">
        <thead><tr><th>When Pressured To...</th><th>Professional Response</th></tr></thead>
        <tbody>
          <tr><td>Ignore a serious vulnerability</td><td>Document the risk in writing; recommend the fix; escalate per policy</td></tr>
          <tr><td>Grant access that violates least privilege</td><td>Ask for written authorization from the data owner</td></tr>
          <tr><td>Delete or alter logs/evidence</td><td>Refuse — this may be illegal (obstruction, spoliation); escalate</td></tr>
          <tr><td>Cut a security corner to hit a deadline</td><td>Surface the tradeoff to decision-makers in writing; let them own the risk decision</td></tr>
        </tbody>
      </table>
      <div class="concept-desc">Know your organization's whistleblower and escalation channels before you need them. A clear, calm, documented objection protects both your integrity and your career — and is exactly what separates a trusted professional from a liability.</div>
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
        (THREAT_INJECT_ANCHOR, THREAT_SENTINEL, THREAT_CONTENT),
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
