#!/usr/bin/env python3
"""Wave 37 – Linux HA/clustering, web server TLS hardening, audit prep, network automation, pentest reporting."""
from pathlib import Path
from html.parser import HTMLParser

S_LINUX  = "<!-- BEGINNER37-LINUX v1 -->"
S_OPS    = "<!-- BEGINNER37-OPS v1 -->"
S_GRC    = "<!-- BEGINNER37-GRC v1 -->"
S_SCRIPT = "<!-- BEGINNER37-SCRIPT v1 -->"
S_PENTEST= "<!-- BEGINNER37-PENTEST v1 -->"

A_LINUX  = "<!-- /domain-body linux -->"
A_OPS    = "<!-- /domain-body ops -->"
A_GRC    = "<!-- /domain-body grc -->"
A_SCRIPT = "<!-- /domain-body script -->"
A_PENTEST= "<!-- /domain-body pentest -->"

# ══════════════════════════════════════════════════════════════════════════
# LINUX – High availability and clustering
# ══════════════════════════════════════════════════════════════════════════
C_LINUX = """
<!-- BEGINNER37-LINUX v1 -->
<!-- ── TOPIC: High Availability & Clustering ─────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-badge">Beginner</span>
    High Availability – Keeping Services Up When Servers Fail
  </div>
  <div class="topic-body">

    <div class="concept-card">
      <div class="concept-label">Core Concept</div>
      <div class="concept-title">What "High Availability" Actually Means</div>
      <div class="concept-desc">
        <strong>High Availability (HA)</strong> means a service keeps
        running even when individual components fail. The goal isn't
        "never fails" (impossible) — it's "fails without anyone
        noticing."<br><br>
        <strong>Availability is usually expressed in "nines":</strong>
      </div>
      <div class="code-block">
<span class="com">Availability   Downtime per year    Downtime per month   Common label</span>
99%            3.65 days            7.3 hours            "Two nines"
99.9%          8.77 hours           43.8 minutes         "Three nines"
99.99%         52.6 minutes         4.4 minutes          "Four nines"
99.999%        5.26 minutes         26 seconds           "Five nines"

<span class="com"># The jump from 99.9% to 99.99% looks small on paper</span>
<span class="com"># but represents 10x more engineering effort and cost.</span>
<span class="com"># Most businesses don't NEED five nines — that's a question</span>
<span class="com"># for the business, not a default engineering goal.</span>
      </div>
    </div>

    <div class="concept-card">
      <div class="concept-label">Building Blocks</div>
      <div class="concept-title">The Three Pillars of HA Architecture</div>
      <div class="concept-desc">
        &bull; <strong>Redundancy</strong> — more than one of everything
          that can fail (servers, disks, network paths, power supplies,
          even data centres). "One is none, two is one."<br><br>
        &bull; <strong>Load balancing</strong> — distributes traffic
          across multiple servers; if one fails, traffic routes around
          it automatically.<br><br>
        &bull; <strong>Failover</strong> — automatic detection of failure
          and automatic switch to a standby. The faster and more silent
          the failover, the higher the availability.<br><br>
        <em>"Not my circus, not my monkey"</em> — true HA requires
        cooperation across teams: network (redundant paths), ops
        (clustering software), and the application itself (must handle
        being restarted/relocated gracefully). No single team can build
        HA alone.
      </div>
    </div>

    <div class="concept-card">
      <div class="concept-label">keepalived</div>
      <div class="concept-title">Floating IPs with keepalived (VRRP)</div>
      <div class="concept-desc">
        <code>keepalived</code> implements <strong>VRRP (Virtual Router
        Redundancy Protocol)</strong> — two or more servers share a
        "virtual" IP address. If the active server dies, a standby
        instantly takes over the IP — clients never notice.
      </div>
      <div class="code-block">
<span class="com"># Install on both servers</span>
sudo apt install keepalived

<span class="com"># /etc/keepalived/keepalived.conf — PRIMARY server</span>
vrrp_instance VI_1 {
    state MASTER
    interface eth0
    virtual_router_id 51
    priority 150            <span class="com"># higher number = preferred primary</span>
    advert_int 1
    authentication {
        auth_type PASS
        auth_pass mysecret
    }
    virtual_ipaddress {
        192.168.1.100/24    <span class="com"># the floating/shared IP</span>
    }
}

<span class="com"># /etc/keepalived/keepalived.conf — BACKUP server</span>
<span class="com"># Same config, but: state BACKUP   and   priority 100</span>

<span class="com"># Start and watch the failover live</span>
sudo systemctl enable --now keepalived
sudo journalctl -u keepalived -f

<span class="com"># Test it: stop keepalived on the primary, watch the IP migrate</span>
sudo systemctl stop keepalived
ip addr show eth0   <span class="com"># run this on the backup — it now owns .100</span>
      </div>
    </div>

    <div class="concept-card">
      <div class="concept-label">Pacemaker/Corosync</div>
      <div class="concept-title">Cluster Resource Management</div>
      <div class="concept-desc">
        For more complex services (databases, file servers), you need a
        full <strong>cluster resource manager</strong>:
        <code>Corosync</code> handles cluster membership/messaging;
        <code>Pacemaker</code> decides what runs where and handles
        failover logic.<br><br>
        <em>"Assume" makes an ass out of you and me</em> — never assume
        a cluster is healthy just because the service responds. Check
        cluster status directly; a "split-brain" scenario (both nodes
        think they're primary) can silently corrupt data.
      </div>
      <div class="code-block">
<span class="com"># View overall cluster status</span>
sudo pcs status

<span class="com"># Output shows: which node is active, resource locations, any failures</span>
<span class="com">Cluster name: web_cluster</span>
<span class="com">Stack: corosync</span>
<span class="com">Current DC: node1 (version ...)  - partition with quorum</span>
<span class="com">2 nodes configured</span>
<span class="com">2 resource instances configured</span>
<span class="com">Online: [ node1 node2 ]</span>
<span class="com">Full list of resources:</span>
<span class="com">  Floating_IP    (ocf::heartbeat:IPaddr2):  Started node1</span>
<span class="com">  WebServer      (systemd:nginx):           Started node1</span>

<span class="com"># Manually move a resource to test failover</span>
sudo pcs resource move WebServer node2

<span class="com"># Check for "quorum" — without it, clusters refuse to act</span>
<span class="com"># (this is the safety mechanism that PREVENTS split-brain)</span>
sudo corosync-quorumtool
      </div>
    </div>

  </div>
</div>
"""

# ══════════════════════════════════════════════════════════════════════════
# OPS – Web server TLS hardening (nginx/Apache)
# ══════════════════════════════════════════════════════════════════════════
C_OPS = """
<!-- BEGINNER37-OPS v1 -->
<!-- ── TOPIC: Web Server TLS Hardening ───────────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-badge">Beginner</span>
    Web Server Hardening – nginx, Apache &amp; TLS Done Right
  </div>
  <div class="topic-body">

    <div class="concept-card">
      <div class="concept-label">Core Concept</div>
      <div class="concept-title">The Default Config Is Not the Secure Config</div>
      <div class="concept-desc">
        Out of the box, web servers prioritise compatibility over
        security — they'll happily serve old TLS versions, leak version
        information, and allow risky HTTP methods. Hardening means
        deliberately tightening these defaults.<br><br>
        <strong>The five hardening layers:</strong><br>
        1. <em>TLS configuration</em> — which protocol versions and
           ciphers are allowed.<br>
        2. <em>HTTP security headers</em> — instructions to the browser
           about how to treat your site.<br>
        3. <em>Information disclosure</em> — hide server version and
           technology stack from attackers.<br>
        4. <em>Rate limiting</em> — slow down brute-force and scraping
           attempts.<br>
        5. <em>Certificate management</em> — automated renewal so sites
           never go down from an expired cert (a surprisingly common
           self-inflicted outage).
      </div>
    </div>

    <div class="concept-card">
      <div class="concept-label">nginx Hardening</div>
      <div class="concept-title">A Hardened nginx Server Block</div>
      <div class="concept-desc">
        This configuration covers the essentials most security scanners
        and compliance checks look for.
      </div>
      <div class="code-block">
<span class="com"># /etc/nginx/sites-available/example.com</span>
server {
    listen 443 ssl http2;
    server_name example.com;

    <span class="com"># ── TLS: only modern protocols and strong ciphers ──</span>
    ssl_certificate     /etc/letsencrypt/live/example.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/example.com/privkey.pem;
    ssl_protocols       TLSv1.2 TLSv1.3;          <span class="com"># no SSLv3, TLSv1.0, TLSv1.1</span>
    ssl_ciphers         HIGH:!aNULL:!MD5:!3DES;
    ssl_prefer_server_ciphers on;
    ssl_session_cache   shared:SSL:10m;

    <span class="com"># ── Hide version info (reduces fingerprinting) ──</span>
    server_tokens off;

    <span class="com"># ── Security headers ──</span>
    add_header Strict-Transport-Security "max-age=63072000; includeSubDomains" always;
    add_header X-Frame-Options "SAMEORIGIN" always;
    add_header X-Content-Type-Options "nosniff" always;
    add_header Referrer-Policy "strict-origin-when-cross-origin" always;
    add_header Content-Security-Policy "default-src 'self'" always;

    <span class="com"># ── Rate limiting (defined in http{} block, applied here) ──</span>
    limit_req zone=login_limit burst=5 nodelay;

    location / {
        proxy_pass http://127.0.0.1:8080;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}

<span class="com"># Redirect all plain HTTP to HTTPS</span>
server {
    listen 80;
    server_name example.com;
    return 301 https://$host$request_uri;
}

<span class="com"># In the http{} block — define the rate limit zone:</span>
<span class="com"># limit_req_zone $binary_remote_addr zone=login_limit:10m rate=5r/m;</span>
      </div>
    </div>

    <div class="concept-card">
      <div class="concept-label">Headers Explained</div>
      <div class="concept-title">What Each Security Header Actually Does</div>
      <div class="concept-desc">
        <table class="ai-table">
          <tr><th>Header</th><th>What it tells the browser</th></tr>
          <tr><td>Strict-Transport-Security</td><td>"Always use HTTPS for this site, never fall back to HTTP"</td></tr>
          <tr><td>X-Frame-Options</td><td>"Don't let other sites embed me in an iframe" (stops clickjacking)</td></tr>
          <tr><td>X-Content-Type-Options</td><td>"Don't guess file types — trust what I declared" (stops MIME sniffing attacks)</td></tr>
          <tr><td>Content-Security-Policy</td><td>"Only load scripts/styles/images from these approved sources"</td></tr>
          <tr><td>Referrer-Policy</td><td>"Don't leak the full URL to other sites when users click links"</td></tr>
        </table>
        <br>
        <em>"Assume" makes an ass out of you and me</em> — never assume
        adding these headers won't break anything. <code>Content-Security-Policy</code>
        especially can silently break legitimate site features (third-party
        widgets, inline scripts). Test in <code>report-only</code> mode first:
        <code>Content-Security-Policy-Report-Only</code> logs violations
        without blocking anything.
      </div>
    </div>

    <div class="concept-card">
      <div class="concept-label">Verification</div>
      <div class="concept-title">Testing Your Hardening Actually Worked</div>
      <div class="concept-desc">
        <em>You can't make someone make the right choice, yet you can pick
        up the pieces afterwards</em> — but you can also <em>verify</em>
        the choice was made correctly in the first place. Don't trust
        your config — test it.
      </div>
      <div class="code-block">
<span class="com"># Free online TLS configuration scanner (the industry standard)</span>
<span class="com"># https://www.ssllabs.com/ssltest/  → grades A+ to F</span>

<span class="com"># Check from the command line with testssl.sh</span>
docker run --rm -ti drwetter/testssl.sh https://example.com

<span class="com"># Check which protocols/ciphers your server actually offers</span>
nmap --script ssl-enum-ciphers -p 443 example.com

<span class="com"># Verify security headers are present</span>
curl -sI https://example.com | grep -iE \
  '(strict-transport|x-frame|x-content-type|content-security)'

<span class="com"># Check certificate expiration (set up monitoring for this!)</span>
echo | openssl s_client -servername example.com -connect example.com:443 2&gt;/dev/null \
  | openssl x509 -noout -dates

<span class="com"># Automated renewal with certbot — verify the timer is active</span>
sudo systemctl status certbot.timer
sudo certbot renew --dry-run
      </div>
    </div>

  </div>
</div>
"""

# ══════════════════════════════════════════════════════════════════════════
# GRC – Audit preparation and evidence collection
# ══════════════════════════════════════════════════════════════════════════
C_GRC = """
<!-- BEGINNER37-GRC v1 -->
<!-- ── TOPIC: Audit Preparation & Evidence Collection ────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-badge">Beginner</span>
    Audit Prep – Surviving (and Thriving In) a Compliance Audit
  </div>
  <div class="topic-body">

    <div class="concept-card">
      <div class="concept-label">Core Concept</div>
      <div class="concept-title">What Auditors Actually Want From You</div>
      <div class="concept-desc">
        An audit isn't an attack — it's a structured conversation where
        someone independent verifies that your controls work as
        documented. Auditors aren't trying to trick you; they're trying
        to form an opinion based on <strong>evidence</strong>.<br><br>
        The golden rule of audits: <strong>"Pics or it didn't happen."</strong>
        A control that exists only in someone's head, or only as a
        promise in a policy document, does not exist from an auditor's
        perspective. If you can't show it, prove it, or export it — it's
        not auditable.<br><br>
        <em>"Assume" makes an ass out of you and me</em> — never assume
        the auditor will "just trust" your explanation. Bring the
        screenshot, the export, the ticket, the signed document.
      </div>
    </div>

    <div class="concept-card">
      <div class="concept-label">Evidence Types</div>
      <div class="concept-title">What "Good Evidence" Looks Like</div>
      <div class="concept-desc">
        Every control needs proof in one of these forms — collect them
        continuously, not the week before the audit:
      </div>
      <div class="code-block">
<span class="com">Control claim                  Acceptable evidence</span>
─────────────────────────────────────────────────────────────────
"We enforce MFA"               Screenshot of IdP config showing MFA
                               required + report of users with MFA enabled

"We patch within 30 days"      Vulnerability scan reports (before/after)
                               + patch management tickets with timestamps

"We review access quarterly"   Signed access review spreadsheet with
                               manager approval + date + names removed/changed

"We train staff on security"   Training completion report from your
                               LMS, with names, dates, and pass rates

"We test our DR plan"          Tabletop exercise notes, attendee list,
                               action items and their resolution

"We log security events"       SIEM dashboard screenshot + sample alert
                               + documented response to that alert

"We encrypt data at rest"      Configuration export showing encryption
                               enabled (e.g. AWS RDS "Encrypted: true")

<span class="com"># PRO TIP: Build an "evidence locker" — a shared drive organized</span>
<span class="com"># by control ID, updated monthly. Audit week becomes "export the</span>
<span class="com"># folder" instead of a fire drill.</span>
      </div>
    </div>

    <div class="concept-card">
      <div class="concept-label">The Audit Itself</div>
      <div class="concept-title">How to Behave During an Audit Interview</div>
      <div class="concept-desc">
        You will likely be interviewed as part of an audit. A few rules
        keep these conversations smooth:<br><br>
        1. <strong>Answer the question asked — nothing more.</strong>
           Volunteering extra information often opens new lines of
           inquiry you weren't prepared for.<br>
        2. <strong>"I don't know, but I'll find out and follow up"</strong>
           is a perfectly good answer. Guessing and being wrong is far
           worse than admitting you need to check.<br>
        3. <strong>Describe what actually happens</strong>, not what the
           policy says should happen. If reality and policy differ,
           that's useful information for everyone — including you.<br>
        4. <strong>Don't argue with the auditor's framework</strong> —
           if you disagree with a finding, raise it through your
           compliance lead, calmly, with evidence.<br><br>
        <em>"Not my circus, not my monkey"</em> — if a question is about
        a control your team doesn't own, say so and point to the right
        owner. Guessing on someone else's behalf creates confusion for
        everyone, including the auditor.
      </div>
    </div>

    <div class="concept-card">
      <div class="concept-label">After the Audit</div>
      <div class="concept-title">Handling Findings &amp; Continuous Improvement</div>
      <div class="concept-desc">
        <em>You can't make someone make the right choice, yet you can pick
        up the pieces afterwards</em> — audits regularly surface gaps no
        one knew existed. That's not failure; that's the system working.<br><br>
        <strong>When findings come back:</strong><br>
        1. Don't panic or get defensive — findings are data, not insults.<br>
        2. Categorise by severity and assign owners with deadlines.<br>
        3. Write a <em>remediation plan</em> — what will change, by when,
           and how you'll prove it's fixed.<br>
        4. Track remediation like any other project — with a ticket,
           a deadline, and a verification step.<br>
        5. Feed lessons back into your evidence-collection process so
           the same gap doesn't surprise you next year.<br><br>
        Organisations that treat audits as an annual annoyance stay stuck
        in the same findings loop. Organisations that treat them as a
        free, expert-guided risk assessment use them to get measurably
        better every single year.
      </div>
    </div>

  </div>
</div>
"""

# ══════════════════════════════════════════════════════════════════════════
# SCRIPT – Network automation with Python (Netmiko)
# ══════════════════════════════════════════════════════════════════════════
C_SCRIPT = """
<!-- BEGINNER37-SCRIPT v1 -->
<!-- ── TOPIC: Network Automation with Python ─────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-badge">Intermediate</span>
    Network Automation – Configuring Switches &amp; Routers with Python
  </div>
  <div class="topic-body">

    <div class="concept-card">
      <div class="concept-label">Core Concept</div>
      <div class="concept-title">Why Automate Network Devices?</div>
      <div class="concept-desc">
        Traditionally, network engineers configure switches and routers
        by hand, one device at a time, over SSH or console — a slow,
        error-prone, and undocumented process. <strong>Network
        automation</strong> applies the same scripting discipline you'd
        use for servers to network gear.<br><br>
        <strong>Why it matters:</strong><br>
        &bull; Configure 200 switches identically in minutes instead of
          weeks.<br>
        &bull; Eliminate "fat-finger" typos that cause outages.<br>
        &bull; Generate configs from templates — guaranteed consistency.<br>
        &bull; Audit configurations across the fleet — find the one
          switch with a forgotten setting.<br><br>
        <em>"Not my circus, not my monkey"</em> — network automation
        touches production infrastructure directly. Always test scripts
        against lab devices first, and always have a way to reach the
        device out-of-band if your script locks you out.
      </div>
    </div>

    <div class="concept-card">
      <div class="concept-label">Netmiko</div>
      <div class="concept-title">Connecting to Devices with Netmiko</div>
      <div class="concept-desc">
        <strong>Netmiko</strong> is a Python library that wraps SSH
        connections to network devices, handling the quirks of dozens
        of vendor CLIs (Cisco, Juniper, Arista, HP, and more) behind a
        consistent interface.
      </div>
      <div class="code-block">
<span class="com"># pip install netmiko</span>
<span class="kw">from</span> netmiko <span class="kw">import</span> ConnectHandler

device = {
    <span class="str">"device_type"</span>: <span class="str">"cisco_ios"</span>,
    <span class="str">"host"</span>:        <span class="str">"192.168.1.1"</span>,
    <span class="str">"username"</span>:    <span class="str">"admin"</span>,
    <span class="str">"password"</span>:    <span class="str">"S3cur3P@ss"</span>,
    <span class="str">"secret"</span>:      <span class="str">"enable_secret_pw"</span>,   <span class="com"># for privileged mode</span>
}

<span class="kw">with</span> ConnectHandler(**device) <span class="kw">as</span> conn:
    conn.enable()                                <span class="com"># enter privileged exec mode</span>

    <span class="com"># Run a read-only command and capture the output</span>
    output = conn.send_command(<span class="str">"show ip interface brief"</span>)
    <span class="fn">print</span>(output)

    <span class="com"># Send a set of configuration commands</span>
    config_commands = [
        <span class="str">"interface GigabitEthernet0/1"</span>,
        <span class="str">"description Uplink-to-Core-Switch"</span>,
        <span class="str">"switchport mode trunk"</span>,
        <span class="str">"switchport trunk allowed vlan 10,20,30"</span>,
    ]
    output = conn.send_config_set(config_commands)
    <span class="fn">print</span>(output)

    <span class="com"># Save the running config to startup config (don't lose changes on reload)</span>
    conn.save_config()
      </div>
    </div>

    <div class="concept-card">
      <div class="concept-label">Scaling Up</div>
      <div class="concept-title">Running Commands Across Many Devices</div>
      <div class="concept-desc">
        The real power of automation appears when you apply one script
        to a fleet of devices — and capture results in a structured way
        for later analysis.
      </div>
      <div class="code-block">
<span class="kw">from</span> netmiko <span class="kw">import</span> ConnectHandler
<span class="kw">from</span> concurrent.futures <span class="kw">import</span> ThreadPoolExecutor
<span class="kw">import</span> csv

DEVICES = [
    {<span class="str">"device_type"</span>: <span class="str">"cisco_ios"</span>, <span class="str">"host"</span>: <span class="str">"192.168.1.1"</span>,  <span class="str">"username"</span>: <span class="str">"admin"</span>, <span class="str">"password"</span>: <span class="str">"pw"</span>},
    {<span class="str">"device_type"</span>: <span class="str">"cisco_ios"</span>, <span class="str">"host"</span>: <span class="str">"192.168.1.2"</span>,  <span class="str">"username"</span>: <span class="str">"admin"</span>, <span class="str">"password"</span>: <span class="str">"pw"</span>},
    {<span class="str">"device_type"</span>: <span class="str">"arista_eos"</span>, <span class="str">"host"</span>: <span class="str">"192.168.1.10"</span>, <span class="str">"username"</span>: <span class="str">"admin"</span>, <span class="str">"password"</span>: <span class="str">"pw"</span>},
]

<span class="kw">def</span> <span class="fn">audit_device</span>(device: dict) -&gt; dict:
    <span class="kw">try</span>:
        <span class="kw">with</span> ConnectHandler(**device) <span class="kw">as</span> conn:
            version = conn.send_command(<span class="str">"show version"</span>)
            ntp     = conn.send_command(<span class="str">"show ntp status"</span>)
            <span class="kw">return</span> {
                <span class="str">"host"</span>: device[<span class="str">"host"</span>],
                <span class="str">"status"</span>: <span class="str">"OK"</span>,
                <span class="str">"ntp_synced"</span>: <span class="str">"synchronized"</span> <span class="kw">in</span> ntp.lower(),
            }
    <span class="kw">except</span> Exception <span class="kw">as</span> e:
        <span class="kw">return</span> {<span class="str">"host"</span>: device[<span class="str">"host"</span>], <span class="str">"status"</span>: <span class="fn">f</span><span class="str">"FAILED: {e}"</span>}

<span class="com"># Run audits in parallel — 50 devices in the time of 1</span>
<span class="kw">with</span> ThreadPoolExecutor(max_workers=<span class="num">10</span>) <span class="kw">as</span> pool:
    results = <span class="fn">list</span>(pool.map(audit_device, DEVICES))

<span class="com"># Write results to CSV for the team's review</span>
<span class="kw">with</span> <span class="fn">open</span>(<span class="str">"network_audit.csv"</span>, <span class="str">"w"</span>, newline=<span class="str">""</span>) <span class="kw">as</span> f:
    writer = csv.DictWriter(f, fieldnames=[<span class="str">"host"</span>, <span class="str">"status"</span>, <span class="str">"ntp_synced"</span>])
    writer.writeheader()
    writer.writerows(results)
      </div>
    </div>

    <div class="concept-card">
      <div class="concept-label">Safety Practices</div>
      <div class="concept-title">Automating Without Causing an Outage</div>
      <div class="concept-desc">
        <em>"Assume" makes an ass out of you and me</em> — and an
        automation script that "should be safe" can take down an entire
        network in seconds. Build in these safeguards:<br><br>
        &bull; <strong>Dry-run mode</strong> — print what the script
          <em>would</em> do before letting it actually run.<br>
        &bull; <strong>Backup before changing</strong> — always pull
          <code>show running-config</code> and save it before pushing
          new config.<br>
        &bull; <strong>Change in small batches</strong> — 5 devices,
          verify, then 50, not all 500 at once.<br>
        &bull; <strong>Read-only first</strong> — run audits and reports
          for weeks before attempting configuration changes.<br>
        &bull; <strong>Out-of-band access</strong> — confirm you (or
          someone) has console/serial access in case a script locks
          everyone out over the network.<br><br>
        <em>You can't make someone make the right choice, yet you can pick
        up the pieces afterwards</em> — when a script does cause an
        outage, the saved "before" configs are what let you restore
        service in minutes instead of hours.
      </div>
    </div>

  </div>
</div>
"""

# ══════════════════════════════════════════════════════════════════════════
# PENTEST – Reporting and client communication
# ══════════════════════════════════════════════════════════════════════════
C_PENTEST = """
<!-- BEGINNER37-PENTEST v1 -->
<!-- ── TOPIC: Pentest Reporting & Communication ──────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-badge">Beginner</span>
    Pentest Reporting – The Skill That Makes or Breaks Your Career
  </div>
  <div class="topic-body">

    <div class="concept-card">
      <div class="concept-label">Core Concept</div>
      <div class="concept-title">The Report IS the Deliverable</div>
      <div class="concept-desc">
        Here's something that surprises new pentesters: the client isn't
        paying for the hacking — they're paying for the
        <strong>report</strong>. The exploitation is invisible to them;
        the report is the only artifact that proves value, drives
        budget decisions, and gets vulnerabilities fixed.<br><br>
        A brilliant exploit chain documented poorly helps no one. A
        moderate finding explained clearly, with a fix the client can
        actually implement, changes the organisation's security posture.<br><br>
        <em>"Not my circus, not my monkey"</em> — your job is to find and
        clearly document risk, not to fix it yourself or shame the team
        that introduced it. Stay in your lane; the client's team owns
        remediation.
      </div>
    </div>

    <div class="concept-card">
      <div class="concept-label">Structure</div>
      <div class="concept-title">Anatomy of a Professional Pentest Report</div>
      <div class="concept-desc">
        Most reports follow this structure — because it serves two very
        different audiences in one document:
      </div>
      <div class="code-block">
<span class="com">1. EXECUTIVE SUMMARY  (for leadership — 1-2 pages, no jargon)</span>
   - Why the test was done, scope, and timeframe
   - Overall risk posture in plain language
   - Top 3-5 findings and their business impact
   - High-level recommendations and themes

<span class="com">2. SCOPE & METHODOLOGY  (for the record)</span>
   - What was tested (IPs, applications, date range)
   - What was explicitly OUT of scope
   - Testing methodology / framework used (e.g. PTES, OWASP)
   - Rules of engagement (testing windows, contacts, escalation path)

<span class="com">3. FINDINGS  (for the technical team — the bulk of the report)</span>
   For EACH finding:
   - Title & unique ID (e.g. "F-001: SQL Injection in Login Form")
   - Severity (Critical / High / Medium / Low / Informational)
   - CVSS score (standardized severity scoring — see below)
   - Description: what the vulnerability is, in plain terms
   - Evidence: screenshots, request/response pairs, proof-of-concept
   - Impact: what an attacker could actually DO with this
   - Remediation: SPECIFIC steps to fix it (not "improve security")
   - References: CWE ID, OWASP category, vendor advisories

<span class="com">4. APPENDICES</span>
   - Raw scan output, tool versions, full request/response logs
      </div>
    </div>

    <div class="concept-card">
      <div class="concept-label">Severity Scoring</div>
      <div class="concept-title">CVSS – Communicating Severity Consistently</div>
      <div class="concept-desc">
        <strong>CVSS (Common Vulnerability Scoring System)</strong> turns
        "this seems pretty bad" into a reproducible number from 0-10,
        based on factors like attack complexity, privileges required,
        and impact on confidentiality/integrity/availability.<br><br>
        <table class="ai-table">
          <tr><th>Score</th><th>Severity</th><th>Typical client reaction</th></tr>
          <tr><td>9.0 - 10.0</td><td>Critical</td><td>Drop everything, fix today</td></tr>
          <tr><td>7.0 - 8.9</td><td>High</td><td>Fix within days/this sprint</td></tr>
          <tr><td>4.0 - 6.9</td><td>Medium</td><td>Fix within the quarter</td></tr>
          <tr><td>0.1 - 3.9</td><td>Low</td><td>Fix when convenient</td></tr>
          <tr><td>0.0</td><td>Informational</td><td>Awareness only, no action required</td></tr>
        </table>
        <br>
        <em>"Assume" makes an ass out of you and me</em> — never assume
        your gut feeling about severity matches the client's risk
        tolerance. CVSS gives both sides a shared, defensible scale —
        use the official calculator at <code>first.org/cvss/calculator</code>.
      </div>
    </div>

    <div class="concept-card">
      <div class="concept-label">Communication</div>
      <div class="concept-title">Writing Findings People Actually Act On</div>
      <div class="concept-desc">
        <em>You can't make someone make the right choice, yet you can pick
        up the pieces afterwards</em> — but you absolutely CAN make the
        right choice the easiest one to make, by writing findings that
        remove every excuse not to fix them.<br><br>
        <strong>Compare these two remediation write-ups:</strong><br><br>
        <strong>Weak:</strong> "Improve input validation and sanitize
        user input to prevent injection attacks."<br>
        <em>(What does the developer actually DO with this on Monday morning?)</em><br><br>
        <strong>Strong:</strong> "Replace the string-concatenated SQL
        query in <code>login.py</code> line 47 with a parameterized
        query using the existing SQLAlchemy ORM (see
        <code>user_search.py</code> line 112 for an example already in
        the codebase). Estimated effort: 1-2 hours including tests."<br><br>
        The second version respects the reader's time, references their
        own code, gives a model to copy, and estimates effort for
        planning — it gets fixed <em>this week</em> instead of sitting
        in a backlog for a year.
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
    (A_LINUX,   S_LINUX,   C_LINUX),
    (A_OPS,     S_OPS,     C_OPS),
    (A_GRC,     S_GRC,     C_GRC),
    (A_SCRIPT,  S_SCRIPT,  C_SCRIPT),
    (A_PENTEST, S_PENTEST, C_PENTEST),
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
