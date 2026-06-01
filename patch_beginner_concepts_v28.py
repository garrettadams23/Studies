#!/usr/bin/env python3
"""
patch_beginner_concepts_v28.py — Wave 28: Serialization safety & rich CLIs,
threat intel lifecycle & insider threats, namespaces/cgroups, network
monitoring, military leadership.

New sentinels:
  BEGINNER28-SCRIPT v1  — Serialization safety (pickle/YAML/JSON), rich CLI output
  BEGINNER28-THREAT v1  — Threat intelligence lifecycle, insider threats, UEBA
  BEGINNER28-LINUX v1   — Namespaces & cgroups (how containers really work)
  BEGINNER28-NET v1     — Network monitoring (SNMP, NetFlow, packet capture)
  BEGINNER28-MIL v1     — Leadership styles, mission command, unit cohesion
"""
from pathlib import Path

SCRIPT_INJECT_ANCHOR = "<!-- /domain-body script -->"
THREAT_INJECT_ANCHOR = "<!-- /domain-body threat -->"
LINUX_INJECT_ANCHOR  = "<!-- /domain-body linux -->"
NET_INJECT_ANCHOR    = "<!-- /domain-body net -->"
MIL_INJECT_ANCHOR    = "<!-- /domain-body military -->"

# ─────────────────────────────── SCRIPT wave 28 ──────────────────────────────
SCRIPT_SENTINEL = "<!-- BEGINNER28-SCRIPT v1 -->"
SCRIPT_CONTENT = """
<!-- BEGINNER28-SCRIPT v1 -->
<!-- ── TOPIC: SERIALIZATION SAFELY ───────────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">📦</span>
    <span class="topic-name">Serialization — Saving Objects (Without Opening a Hole)</span>
    <span class="topic-badge">SCRIPT • Security</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">WHAT IT IS</div>
      <div class="concept-title">Turning Objects Into Bytes and Back</div>
      <div class="concept-desc">Serialization converts in-memory objects into a storable/transmittable format (text or bytes); deserialization reverses it. You do this constantly — saving config, sending API payloads, caching. But <em>how</em> you serialize has big security implications. Some formats can execute code when loaded — a classic, devastating vulnerability.</div>
      <table class="ai-table">
        <thead><tr><th>Format</th><th>Use For</th><th>Safe to load untrusted?</th></tr></thead>
        <tbody>
          <tr><td>JSON</td><td>APIs, config, data exchange</td><td>✓ Yes (data only)</td></tr>
          <tr><td>YAML</td><td>Config files</td><td>⚠️ Only with <code>safe_load</code></td></tr>
          <tr><td>Pickle</td><td>Python-only object caching</td><td>✗ NEVER — can execute code</td></tr>
          <tr><td>TOML</td><td>Config (pyproject.toml)</td><td>✓ Yes</td></tr>
          <tr><td>Protobuf/MessagePack</td><td>Fast binary, cross-language</td><td>✓ Yes (schema-based)</td></tr>
        </tbody>
      </table>
    </div>
    <div class="concept-card">
      <div class="concept-label">THE PICKLE TRAP</div>
      <div class="concept-title">Deserializing Untrusted Data = Remote Code Execution</div>
      <div class="concept-desc">Python's <code>pickle</code> can reconstruct arbitrary objects — including ones that run code on load. <strong>Never unpickle data from an untrusted source</strong> (uploaded files, network input, caches an attacker can touch). The same danger exists in other languages (Java deserialization, .NET, PHP). It's a top cause of critical CVEs.</div>
      <div class="code-block"><span class="com"># DANGER — a malicious pickle can run ANY code on load</span>
<span class="kw">import</span> pickle
data = pickle.loads(untrusted_bytes)   <span class="com"># ✗ may execute attacker code!</span>

<span class="com"># SAFE alternatives for untrusted data</span>
<span class="kw">import</span> json, yaml
obj = json.loads(untrusted_string)        <span class="com"># ✓ data only</span>
cfg = yaml.safe_load(untrusted_yaml)      <span class="com"># ✓ safe_load, NOT load</span>

<span class="com"># yaml.load() (without SafeLoader) is the dangerous one — avoid</span></div>
    </div>
    <div class="concept-card">
      <div class="concept-label">FRIENDLY CLI OUTPUT</div>
      <div class="concept-title">Make Your Tools Pleasant to Use</div>
      <div class="concept-desc">Good output makes tools far more usable. The <code>rich</code> library adds color, tables, progress bars, and pretty tracebacks with almost no effort; <code>click</code>/<code>typer</code> build polished command-line interfaces.</div>
      <div class="code-block"><span class="com"># pip install rich</span>
<span class="kw">from</span> rich.console <span class="kw">import</span> Console
<span class="kw">from</span> rich.table <span class="kw">import</span> Table

console = Console()
console.print(<span class="str">"[bold green]✓ Success[/]"</span>)
console.print(<span class="str">"[bold red]✗ Error[/]"</span>, <span class="str">"disk full"</span>)

<span class="com"># A formatted table in a few lines</span>
table = Table(title=<span class="str">"Servers"</span>)
table.add_column(<span class="str">"Host"</span>); table.add_column(<span class="str">"Status"</span>)
table.add_row(<span class="str">"web1"</span>, <span class="str">"[green]up[/]"</span>)
table.add_row(<span class="str">"db1"</span>, <span class="str">"[red]down[/]"</span>)
console.print(table)

<span class="com"># Progress bar for long operations</span>
<span class="kw">from</span> rich.progress <span class="kw">import</span> track
<span class="kw">for</span> item <span class="kw">in</span> track(items, description=<span class="str">"Processing..."</span>):
    process(item)</div>
    </div>
  </div>
</div>
"""

# ─────────────────────────────── THREAT wave 28 ──────────────────────────────
THREAT_SENTINEL = "<!-- BEGINNER28-THREAT v1 -->"
THREAT_CONTENT = """
<!-- BEGINNER28-THREAT v1 -->
<!-- ── TOPIC: THREAT INTELLIGENCE ────────────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">🧭</span>
    <span class="topic-name">Threat Intelligence — Turning Data Into Decisions</span>
    <span class="topic-badge">THREAT • Strategic</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">WHAT IT IS</div>
      <div class="concept-title">Knowing Your Enemy</div>
      <div class="concept-desc">Threat intelligence (CTI) is evidence-based knowledge about threats — who's attacking, how, and why — used to make better security decisions. It's the difference between reacting blindly and defending with foresight. Good intel is <em>actionable</em>: it tells you what to do, not just interesting facts. There are three levels, serving different audiences.</div>
      <table class="ai-table">
        <thead><tr><th>Level</th><th>Audience</th><th>Example</th></tr></thead>
        <tbody>
          <tr><td>Strategic</td><td>Executives</td><td>"Ransomware groups are targeting our industry" — informs budget/risk</td></tr>
          <tr><td>Operational</td><td>SOC managers, hunters</td><td>"This group uses spear-phishing then RDP" — TTPs, campaigns</td></tr>
          <tr><td>Tactical</td><td>Analysts, tools</td><td>Specific IOCs: bad IPs, hashes, domains to block</td></tr>
        </tbody>
      </table>
    </div>
    <div class="concept-card">
      <div class="concept-label">THE INTEL LIFECYCLE</div>
      <div class="concept-title">From Requirement to Action</div>
      <table class="ai-table">
        <thead><tr><th>Phase</th><th>What Happens</th></tr></thead>
        <tbody>
          <tr><td>1. Direction</td><td>Define what you need to know (intelligence requirements)</td></tr>
          <tr><td>2. Collection</td><td>Gather data (feeds, OSINT, internal logs, dark web)</td></tr>
          <tr><td>3. Processing</td><td>Normalize, deduplicate, translate, structure</td></tr>
          <tr><td>4. Analysis</td><td>Turn data into meaning — context, assessment</td></tr>
          <tr><td>5. Dissemination</td><td>Get it to the right people in a usable form</td></tr>
          <tr><td>6. Feedback</td><td>Was it useful? Refine requirements — loop</td></tr>
        </tbody>
      </table>
      <div class="concept-desc">Standards like <strong>STIX</strong> (structured threat data) and <strong>TAXII</strong> (the transport for sharing it) let organizations exchange intel automatically — for example via an ISAC (Information Sharing and Analysis Center) for your industry.</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">INSIDER THREATS</div>
      <div class="concept-title">The Danger From Within</div>
      <div class="concept-desc">Not all threats come from outside. Insiders — employees, contractors — already have access and trust, making them especially dangerous and hard to detect. They aren't always malicious.</div>
      <table class="ai-table">
        <thead><tr><th>Type</th><th>Motivation</th><th>Example</th></tr></thead>
        <tbody>
          <tr><td>Malicious insider</td><td>Revenge, money, espionage</td><td>Disgruntled admin steals/sabotages data</td></tr>
          <tr><td>Negligent insider</td><td>Carelessness</td><td>Clicks phishing, misconfigures a bucket</td></tr>
          <tr><td>Compromised insider</td><td>Account taken over</td><td>Attacker uses a real employee's credentials</td></tr>
        </tbody>
      </table>
    </div>
    <div class="concept-card">
      <div class="concept-label">UEBA</div>
      <div class="concept-title">User &amp; Entity Behavior Analytics</div>
      <div class="concept-desc">UEBA builds a baseline of normal behavior for each user/device, then flags anomalies — the technical core of insider-threat and compromised-account detection. Examples: a user suddenly downloading gigabytes at 3am, accessing systems they never touch, or logging in from two countries an hour apart ("impossible travel"). Because it's behavior-based, UEBA catches threats that signature rules miss — including insiders using legitimate access in illegitimate ways.</div>
    </div>
  </div>
</div>
"""

# ─────────────────────────────── LINUX wave 28 ───────────────────────────────
LINUX_SENTINEL = "<!-- BEGINNER28-LINUX v1 -->"
LINUX_CONTENT = """
<!-- BEGINNER28-LINUX v1 -->
<!-- ── TOPIC: HOW CONTAINERS REALLY WORK ─────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">🧬</span>
    <span class="topic-name">Under the Hood — Namespaces &amp; cgroups</span>
    <span class="topic-badge">LINUX • Advanced</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">THE SECRET</div>
      <div class="concept-title">Containers Are Just Linux Processes</div>
      <div class="concept-desc">A container isn't a lightweight VM — it's a normal Linux process that's been <em>isolated</em> using two kernel features: <strong>namespaces</strong> (what a process can SEE) and <strong>cgroups</strong> (what a process can USE). Docker just orchestrates these kernel primitives nicely. Understanding this demystifies containers — and explains both their efficiency and their security model (shared kernel = the isolation boundary).</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">NAMESPACES</div>
      <div class="concept-title">Isolating What a Process Sees</div>
      <div class="concept-desc">Namespaces give a process its own private view of a system resource — so a container thinks it has its own hostname, network, process tree, etc., while really sharing one kernel.</div>
      <table class="ai-table">
        <thead><tr><th>Namespace</th><th>Isolates</th></tr></thead>
        <tbody>
          <tr><td>PID</td><td>Process IDs — container sees its own PID 1, not the host's processes</td></tr>
          <tr><td>NET</td><td>Network interfaces, IPs, routing, ports</td></tr>
          <tr><td>MNT</td><td>Mount points / filesystem view</td></tr>
          <tr><td>UTS</td><td>Hostname and domain name</td></tr>
          <tr><td>IPC</td><td>Inter-process communication (shared memory)</td></tr>
          <tr><td>USER</td><td>User/group IDs — can be root inside, unprivileged outside</td></tr>
        </tbody>
      </table>
      <div class="code-block"><span class="com"># See namespaces a process belongs to</span>
ls -l /proc/$$/ns        <span class="com"># $$ = current shell's PID</span>

<span class="com"># Run a process in a new namespace (the raw primitive)</span>
sudo unshare --pid --fork --mount-proc bash
<span class="com"># Inside: ps aux shows almost nothing — isolated PID namespace</span></div>
    </div>
    <div class="concept-card">
      <div class="concept-label">CGROUPS</div>
      <div class="concept-title">Limiting What a Process Can Use</div>
      <div class="concept-desc">Control groups (cgroups) limit and account for resource usage — CPU, memory, disk I/O, network. This is how <code>docker run --memory 512m</code> works, and how the kernel prevents one container from starving the others. Hit a memory cgroup limit and the OOM killer terminates the process.</div>
      <div class="code-block"><span class="com"># Docker resource limits are cgroups under the hood</span>
docker run --memory 512m --cpus 1.5 myapp

<span class="com"># systemd uses cgroups too — limit a service</span>
systemctl set-property nginx.service MemoryMax=1G CPUQuota=50%

<span class="com"># Inspect cgroup hierarchy</span>
systemd-cgls                 <span class="com"># tree of cgroups</span>
systemd-cgtop                <span class="com"># top-like view of cgroup resource use</span></div>
    </div>
    <div class="concept-card">
      <div class="concept-label">THE SECURITY ANGLE</div>
      <div class="concept-title">Why "Shared Kernel" Matters</div>
      <div class="concept-desc">Because all containers share the host kernel, a kernel vulnerability or a misconfiguration can allow a <strong>container escape</strong> — breaking isolation to reach the host. This is why container hardening matters (no root, drop capabilities, read-only, seccomp profiles that restrict syscalls) and why high-security workloads sometimes use stronger isolation: <strong>gVisor</strong> (sandboxed kernel), <strong>Kata Containers</strong> (lightweight VMs per container), or just plain VMs. Defense in depth applies even to containers.</div>
    </div>
  </div>
</div>
"""

# ─────────────────────────────── NET wave 28 ─────────────────────────────────
NET_SENTINEL = "<!-- BEGINNER28-NET v1 -->"
NET_CONTENT = """
<!-- BEGINNER28-NET v1 -->
<!-- ── TOPIC: NETWORK MONITORING ─────────────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">📡</span>
    <span class="topic-name">Network Monitoring — Seeing What Flows Through</span>
    <span class="topic-badge">NET • Operations</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">WHY MONITOR</div>
      <div class="concept-title">You Can't Manage What You Can't See</div>
      <div class="concept-desc">Network monitoring tells you device health, bandwidth use, errors, and unusual traffic — essential for both operations (is the link saturated? is a switch down?) and security (is data being exfiltrated? is there C2 traffic?). Different techniques answer different questions, from device health to per-flow detail.</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">SNMP</div>
      <div class="concept-title">Polling Device Health</div>
      <div class="concept-desc">SNMP (Simple Network Management Protocol) lets a monitoring system query devices (switches, routers, servers, printers) for metrics — interface status, CPU, temperature, traffic counters. Devices expose values in a hierarchical database (MIB) addressed by OIDs. Tools like Zabbix, LibreNMS, and PRTG poll via SNMP and graph/alert on the results.</div>
      <table class="ai-table">
        <thead><tr><th>Version</th><th>Note</th></tr></thead>
        <tbody>
          <tr><td>SNMPv1 / v2c</td><td>Uses a plaintext "community string" — insecure; avoid on untrusted networks</td></tr>
          <tr><td>SNMPv3</td><td>Adds authentication + encryption — use this</td></tr>
        </tbody>
      </table>
    </div>
    <div class="concept-card">
      <div class="concept-label">FLOW DATA</div>
      <div class="concept-title">NetFlow / IPFIX / sFlow — Who Talked to Whom</div>
      <div class="concept-desc">Flow data records metadata about conversations (source/dest IP, ports, protocol, bytes) without capturing full packet contents. It answers "who is talking to whom, how much?" — invaluable for capacity planning, billing, and security (spotting exfiltration, scanning, or C2 beaconing) at scale, far more cheaply than full packet capture.</div>
      <table class="ai-table">
        <thead><tr><th>Tech</th><th>Origin</th><th>Note</th></tr></thead>
        <tbody>
          <tr><td>NetFlow</td><td>Cisco</td><td>The original; widely supported</td></tr>
          <tr><td>IPFIX</td><td>IETF standard</td><td>Vendor-neutral "NetFlow v10"</td></tr>
          <tr><td>sFlow</td><td>Multi-vendor</td><td>Packet sampling, lower overhead</td></tr>
        </tbody>
      </table>
    </div>
    <div class="concept-card">
      <div class="concept-label">PACKET CAPTURE</div>
      <div class="concept-title">The Full Truth on the Wire</div>
      <div class="concept-desc">When you need to see <em>exactly</em> what was sent — debugging an app, analyzing an attack — capture full packets. <code>tcpdump</code> on the CLI, Wireshark for deep GUI analysis. The most detailed (and storage-heavy) option; usually targeted at a specific problem, not always-on.</div>
      <div class="code-block"><span class="com"># tcpdump basics</span>
sudo tcpdump -i eth0                       <span class="com"># live capture</span>
sudo tcpdump -i eth0 port 443              <span class="com"># filter by port</span>
sudo tcpdump -i eth0 host 10.0.0.5         <span class="com"># filter by host</span>
sudo tcpdump -i eth0 -w capture.pcap       <span class="com"># save to file</span>
sudo tcpdump -i eth0 'tcp[tcpflags] &amp; tcp-syn != 0'   <span class="com"># SYN packets</span>

<span class="com"># Then open capture.pcap in Wireshark for deep analysis</span>
<span class="com"># Wireshark display filters: http, dns, ip.addr==10.0.0.5, tcp.port==22</span></div>
    </div>
  </div>
</div>
"""

# ─────────────────────────────── MILITARY wave 28 ────────────────────────────
MIL_SENTINEL = "<!-- BEGINNER28-MIL v1 -->"
MIL_CONTENT = """
<!-- BEGINNER28-MIL v1 -->
<!-- ── TOPIC: LEADERSHIP STYLES & MISSION COMMAND ────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">🎖️</span>
    <span class="topic-name">Leadership — Styles, Mission Command &amp; Cohesion</span>
    <span class="topic-badge">MILITARY • Leadership</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">LEADERSHIP STYLES</div>
      <div class="concept-title">Match the Style to the Situation</div>
      <div class="concept-desc">There's no single "best" leadership style — effective leaders adapt to the situation, the people, and the stakes. The military teaches this explicitly, and it maps directly to leading technical teams and incidents.</div>
      <table class="ai-table">
        <thead><tr><th>Style</th><th>When It Works</th><th>IT Example</th></tr></thead>
        <tbody>
          <tr><td>Directive (autocratic)</td><td>Crisis, no time to debate, clear danger</td><td>Active incident — "isolate that host NOW"</td></tr>
          <tr><td>Participative</td><td>Skilled team, time to deliberate</td><td>Architecture decisions, planning</td></tr>
          <tr><td>Delegative</td><td>Highly capable, trusted people</td><td>"You own this project — keep me posted"</td></tr>
          <tr><td>Transformational</td><td>Need to inspire change/growth</td><td>Driving a culture or major modernization</td></tr>
          <tr><td>Servant</td><td>Day-to-day team enablement</td><td>Removing blockers so the team can deliver</td></tr>
        </tbody>
      </table>
      <div class="concept-desc"><strong>The skill is the switch:</strong> a leader who is directive during an outage but participative in planning earns far more than one stuck in a single mode. Reading which the moment needs is the art.</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">MISSION COMMAND</div>
      <div class="concept-title">Decentralized Execution Through Trust</div>
      <div class="concept-desc">Mission Command is the modern military's core leadership philosophy: leaders provide clear <em>intent</em> and the "why," then empower subordinates to use disciplined initiative to achieve it — without waiting for detailed orders. It rests on mutual trust, shared understanding, and accepting prudent risk. In fast-moving situations (combat or a production incident), the people closest to the problem must be able to act. Micromanagement is too slow and doesn't scale.</div>
      <table class="ai-table">
        <thead><tr><th>Principle</th><th>Meaning</th></tr></thead>
        <tbody>
          <tr><td>Build cohesive teams through trust</td><td>Trust is earned over time; it's the foundation</td></tr>
          <tr><td>Create shared understanding</td><td>Everyone knows the goal and the why</td></tr>
          <tr><td>Provide clear commander's intent</td><td>The end state, so people can adapt the how</td></tr>
          <tr><td>Exercise disciplined initiative</td><td>Act toward the intent without being told</td></tr>
          <tr><td>Use mission orders</td><td>Say what + why, not every how</td></tr>
          <tr><td>Accept prudent risk</td><td>Perfect certainty never comes; act anyway</td></tr>
        </tbody>
      </table>
    </div>
    <div class="concept-card">
      <div class="concept-label">UNIT COHESION</div>
      <div class="concept-title">What Makes Teams Perform Under Stress</div>
      <div class="concept-desc">The military invests heavily in cohesion because cohesive units perform dramatically better under pressure — and the research (e.g., Google's Project Aristotle) found the same for tech teams: the #1 predictor of high-performing teams is <strong>psychological safety</strong> — members feel safe to take risks, admit mistakes, and speak up. This connects directly to blameless post-mortems: people who fear punishment hide problems, and hidden problems compound. Leaders build cohesion by sharing hardship, being competent and fair, communicating honestly, and putting the team's welfare above their own ego. Take care of your people, and they'll take care of the mission.</div>
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
        (THREAT_INJECT_ANCHOR, THREAT_SENTINEL, THREAT_CONTENT),
        (LINUX_INJECT_ANCHOR,  LINUX_SENTINEL,  LINUX_CONTENT),
        (NET_INJECT_ANCHOR,    NET_SENTINEL,    NET_CONTENT),
        (MIL_INJECT_ANCHOR,    MIL_SENTINEL,    MIL_CONTENT),
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
