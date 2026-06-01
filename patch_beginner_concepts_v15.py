#!/usr/bin/env python3
"""
patch_beginner_concepts_v15.py — Wave 15: Debugging, endpoint security,
Infrastructure as Code, VPN/proxies, and IT survival mindsets.

New sentinels:
  BEGINNER15-SCRIPT v1  — Debugging (pdb), logging vs print, profiling
  BEGINNER15-SEC v1     — Endpoint security, EDR/XDR, antivirus, DLP
  BEGINNER15-OPS v1     — Infrastructure as Code, Ansible, config management
  BEGINNER15-NET v1     — VPNs, proxies, tunneling, zero trust network access
  BEGINNER15-LIFE v1    — IT survival mindsets (boundaries, assumptions, ownership)
"""
from pathlib import Path

SCRIPT_INJECT_ANCHOR = "<!-- /domain-body script -->"
SEC_INJECT_ANCHOR    = "<!-- /domain-body sec -->"
OPS_INJECT_ANCHOR    = "<!-- /domain-body ops -->"
NET_INJECT_ANCHOR    = "<!-- /domain-body net -->"
LIFE_INJECT_ANCHOR   = "<!-- /domain-body lifestyle -->"

# ─────────────────────────────── SCRIPTING wave 15 ───────────────────────────
SCRIPT_SENTINEL = "<!-- BEGINNER15-SCRIPT v1 -->"
SCRIPT_CONTENT = """
<!-- BEGINNER15-SCRIPT v1 -->
<!-- ── TOPIC: DEBUGGING ──────────────────────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">🐛</span>
    <span class="topic-name">Debugging — Finding Out Why Your Code Lies to You</span>
    <span class="topic-badge">SCRIPT • Essential</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">THE DEBUGGING MINDSET</div>
      <div class="concept-title">The Bug Is Always in Your Assumptions</div>
      <div class="concept-desc">Debugging is the process of figuring out the gap between what you THINK the code does and what it ACTUALLY does. The number one rule: <strong>don't guess — observe</strong>. Beginners change random things hoping it works. Professionals form a hypothesis, test it, and narrow down the cause. The scientific method applied to code.</div>
      <table class="ai-table">
        <thead><tr><th>Step</th><th>What to Do</th></tr></thead>
        <tbody>
          <tr><td>1. Reproduce</td><td>Make the bug happen reliably. A bug you can't reproduce is one you can't fix.</td></tr>
          <tr><td>2. Isolate</td><td>Narrow down WHERE it happens. Binary search the code — comment out halves.</td></tr>
          <tr><td>3. Hypothesize</td><td>Form a specific theory: "I think x is None here"</td></tr>
          <tr><td>4. Test</td><td>Add a print/breakpoint to confirm or reject the theory</td></tr>
          <tr><td>5. Fix &amp; verify</td><td>Fix it, confirm the bug is gone, confirm you didn't break anything else</td></tr>
        </tbody>
      </table>
    </div>
    <div class="concept-card">
      <div class="concept-label">PRINT DEBUGGING</div>
      <div class="concept-title">The Humble print() — Still Useful</div>
      <div class="concept-desc">Don't be ashamed of print debugging — even senior engineers use it. The trick is to print the right things: variable values, types, and "I got here" markers.</div>
      <div class="code-block"><span class="com"># Print value AND type (the type often reveals the bug)</span>
<span class="fn">print</span>(<span class="str">f"DEBUG x = {x!r} (type: {type(x).__name__})"</span>)

<span class="com"># f-string = debugging (Python 3.8+) — prints name AND value</span>
<span class="fn">print</span>(<span class="str">f"{x=}"</span>)            <span class="com"># x=42</span>
<span class="fn">print</span>(<span class="str">f"{user.name=}"</span>)    <span class="com"># user.name='Alice'</span>

<span class="com"># Mark execution flow</span>
<span class="fn">print</span>(<span class="str">">>> entered process_data()"</span>)
<span class="fn">print</span>(<span class="str">f">>> loop iteration {i}, item={item}"</span>)

<span class="com"># Pretty-print complex structures</span>
<span class="kw">from</span> pprint <span class="kw">import</span> pprint
pprint(complicated_nested_dict)</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">THE DEBUGGER (pdb)</div>
      <div class="concept-title">Pause and Inspect Live Execution</div>
      <div class="concept-desc">A debugger lets you pause execution and inspect everything at that exact moment — variables, the call stack, step through line by line. Far more powerful than print for complex bugs.</div>
      <div class="code-block"><span class="com"># Drop a breakpoint anywhere (Python 3.7+)</span>
<span class="kw">def</span> <span class="fn">process</span>(data):
    result = transform(data)
    <span class="fn">breakpoint</span>()        <span class="com"># execution pauses here, opens pdb</span>
    <span class="kw">return</span> result

<span class="com"># pdb commands once paused:</span>
n     <span class="com"># next line (step over)</span>
s     <span class="com"># step into function call</span>
c     <span class="com"># continue until next breakpoint</span>
l     <span class="com"># list code around current line</span>
p x   <span class="com"># print variable x</span>
pp x  <span class="com"># pretty-print x</span>
w     <span class="com"># where am I (show call stack)</span>
q     <span class="com"># quit debugging</span>

<span class="com"># Run a whole script under the debugger</span>
python -m pdb myscript.py</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">READING TRACEBACKS</div>
      <div class="concept-title">The Error Message Is a Map, Not an Insult</div>
      <div class="concept-desc">Python tracebacks read bottom-up for the error type, and the call chain top-to-bottom. The most useful line is usually the LAST line of YOUR code before it enters a library.</div>
      <div class="code-block">Traceback (most recent call last):
  File <span class="str">"app.py"</span>, line 42, <span class="kw">in</span> &lt;module&gt;
    main()                          <span class="com"># ← call chain starts here</span>
  File <span class="str">"app.py"</span>, line 30, <span class="kw">in</span> main
    user = get_user(uid)            <span class="com"># ← then here</span>
  File <span class="str">"app.py"</span>, line 18, <span class="kw">in</span> get_user
    <span class="kw">return</span> users[uid][<span class="str">"name"</span>]    <span class="com"># ← THE ACTUAL PROBLEM LINE</span>
KeyError: 'name'                    <span class="com"># ← WHAT went wrong</span>

<span class="com"># Reading strategy:</span>
<span class="com"># 1. Last line  = the error type and message</span>
<span class="com"># 2. Line above = exactly where it broke</span>
<span class="com"># 3. Work upward to understand HOW you got there</span></div>
    </div>
  </div>
</div>

<!-- ── TOPIC: VIRTUAL ENVIRONMENTS & DEPENDENCY ISOLATION ── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">🧪</span>
    <span class="topic-name">Virtual Environments — Isolating Project Dependencies</span>
    <span class="topic-badge">SCRIPT • Essential</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">THE PROBLEM THEY SOLVE</div>
      <div class="concept-title">Dependency Hell</div>
      <div class="concept-desc">Project A needs Django 3.2. Project B needs Django 4.2. If you install packages globally, they conflict — you can only have one version. Virtual environments give each project its own isolated set of packages, so they never interfere. <strong>Rule: never <code>pip install</code> into your system Python.</strong> Always use a virtual environment.</div>
      <div class="code-block"><span class="com"># Create a virtual environment (built into Python 3)</span>
python -m venv .venv

<span class="com"># Activate it</span>
source .venv/bin/activate     <span class="com"># Linux/Mac</span>
.venv\\Scripts\\activate         <span class="com"># Windows</span>

<span class="com"># Your prompt now shows (.venv) — pip installs go HERE, isolated</span>
pip install requests flask
pip list                      <span class="com"># only this project's packages</span>

<span class="com"># Freeze exact versions for reproducibility</span>
pip freeze &gt; requirements.txt

<span class="com"># Recreate the environment elsewhere</span>
pip install -r requirements.txt

<span class="com"># Leave the environment</span>
deactivate</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">MODERN TOOLING</div>
      <div class="concept-title">The New Generation of Python Tools</div>
      <table class="ai-table">
        <thead><tr><th>Tool</th><th>What It Does</th><th>Why People Like It</th></tr></thead>
        <tbody>
          <tr><td><code>venv</code> + <code>pip</code></td><td>Built-in, standard</td><td>Always available, no install needed</td></tr>
          <tr><td><code>uv</code></td><td>Ultra-fast package installer + venv manager (Rust)</td><td>10-100x faster than pip; modern favorite</td></tr>
          <tr><td><code>poetry</code></td><td>Dependency management + packaging</td><td>Lock files, clean pyproject.toml workflow</td></tr>
          <tr><td><code>pipenv</code></td><td>Combines pip + venv</td><td>Pipfile.lock for reproducibility</td></tr>
          <tr><td><code>conda</code></td><td>Cross-language package manager</td><td>Popular in data science (handles non-Python deps)</td></tr>
          <tr><td><code>pipx</code></td><td>Install CLI tools in isolated envs</td><td>Global CLI tools without polluting system</td></tr>
        </tbody>
      </table>
    </div>
  </div>
</div>
"""

# ─────────────────────────────── SEC wave 15 ─────────────────────────────────
SEC_SENTINEL = "<!-- BEGINNER15-SEC v1 -->"
SEC_CONTENT = """
<!-- BEGINNER15-SEC v1 -->
<!-- ── TOPIC: ENDPOINT SECURITY ──────────────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">💻</span>
    <span class="topic-name">Endpoint Security — Protecting the Devices People Actually Use</span>
    <span class="topic-badge">SEC • Essential</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">WHY ENDPOINTS MATTER</div>
      <div class="concept-title">The Endpoint Is the New Perimeter</div>
      <div class="concept-desc">The old security model was a hard perimeter (firewall) around a soft inside. But with remote work, cloud, and mobile, there is no perimeter — laptops connect from coffee shops, phones access company email. The endpoint (any device: laptop, phone, server, IoT) is now where attacks land. Most breaches start with a compromised endpoint: a clicked phishing link, a malicious download, a stolen laptop.</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">AV → EDR → XDR</div>
      <div class="concept-title">The Evolution of Endpoint Protection</div>
      <table class="ai-table">
        <thead><tr><th>Generation</th><th>Full Name</th><th>How It Works</th><th>Limitation</th></tr></thead>
        <tbody>
          <tr><td>AV</td><td>Antivirus</td><td>Signature-based — matches known malware fingerprints</td><td>Can't catch new/unknown (zero-day) malware</td></tr>
          <tr><td>NGAV</td><td>Next-Gen Antivirus</td><td>Adds behavioral analysis, ML, heuristics</td><td>Still focused on prevention, limited investigation</td></tr>
          <tr><td>EDR</td><td>Endpoint Detection &amp; Response</td><td>Records endpoint activity, detects suspicious behavior, enables investigation + response</td><td>Endpoint-only visibility</td></tr>
          <tr><td>XDR</td><td>Extended Detection &amp; Response</td><td>Correlates across endpoint, network, email, cloud, identity</td><td>Complexity, cost, vendor lock-in</td></tr>
          <tr><td>MDR</td><td>Managed Detection &amp; Response</td><td>EDR/XDR + a human SOC team running it for you</td><td>Outsourced — less direct control</td></tr>
        </tbody>
      </table>
    </div>
    <div class="concept-card">
      <div class="concept-label">EDR CAPABILITIES</div>
      <div class="concept-title">What EDR Actually Does</div>
      <table class="ai-table">
        <thead><tr><th>Capability</th><th>What It Means</th></tr></thead>
        <tbody>
          <tr><td>Continuous recording</td><td>Logs process launches, file changes, network connections, registry edits — like a flight recorder</td></tr>
          <tr><td>Behavioral detection</td><td>Flags suspicious sequences (Word spawns PowerShell spawns cmd = likely malicious)</td></tr>
          <tr><td>Threat hunting</td><td>Lets analysts query historical data: "show every host that ran certutil last week"</td></tr>
          <tr><td>Isolation</td><td>Remotely quarantine a compromised host from the network (but keep EDR connection)</td></tr>
          <tr><td>Remediation</td><td>Kill processes, delete files, roll back changes remotely</td></tr>
          <tr><td>Root cause analysis</td><td>Reconstruct the full attack chain from initial access to impact</td></tr>
        </tbody>
      </table>
    </div>
    <div class="concept-card">
      <div class="concept-label">ENDPOINT HARDENING</div>
      <div class="concept-title">Reduce the Attack Surface Before Anything Lands</div>
      <table class="ai-table">
        <thead><tr><th>Control</th><th>Why It Helps</th></tr></thead>
        <tbody>
          <tr><td>Disk encryption (BitLocker/FileVault/LUKS)</td><td>Stolen laptop = no data exposure</td></tr>
          <tr><td>Application allowlisting</td><td>Only approved apps run — blocks unknown malware</td></tr>
          <tr><td>Least privilege (no local admin)</td><td>Malware can't install system-wide if user isn't admin</td></tr>
          <tr><td>Patch management</td><td>Closes known vulnerabilities attackers exploit</td></tr>
          <tr><td>Host firewall</td><td>Blocks unexpected inbound/outbound connections</td></tr>
          <tr><td>Disable macros / restrict Office</td><td>Macros are a top malware delivery vector</td></tr>
          <tr><td>USB control</td><td>Blocks malicious USB drops and data exfiltration</td></tr>
        </tbody>
      </table>
    </div>
    <div class="concept-card">
      <div class="concept-label">DLP</div>
      <div class="concept-title">Data Loss Prevention — Stopping Data From Walking Out</div>
      <div class="concept-desc">DLP tools detect and prevent sensitive data (PII, credit cards, source code, classified docs) from leaving the organization — whether by accident (employee emails a spreadsheet to wrong address) or malice (insider exfiltrating data). DLP works by inspecting content against patterns and policies at three points:</div>
      <table class="ai-table">
        <thead><tr><th>DLP Type</th><th>Where It Watches</th><th>Example Block</th></tr></thead>
        <tbody>
          <tr><td>Data in motion</td><td>Network traffic, email, web uploads</td><td>Blocks email containing SSNs to external address</td></tr>
          <tr><td>Data at rest</td><td>Files on disks, databases, cloud storage</td><td>Finds unencrypted credit card numbers in a file share</td></tr>
          <tr><td>Data in use</td><td>Endpoint actions (copy, print, USB)</td><td>Blocks copying customer DB to a USB drive</td></tr>
        </tbody>
      </table>
    </div>
  </div>
</div>
"""

# ─────────────────────────────── OPS wave 15 ─────────────────────────────────
OPS_SENTINEL = "<!-- BEGINNER15-OPS v1 -->"
OPS_CONTENT = """
<!-- BEGINNER15-OPS v1 -->
<!-- ── TOPIC: INFRASTRUCTURE AS CODE ─────────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">🏗️</span>
    <span class="topic-name">Infrastructure as Code — Servers You Define in Text Files</span>
    <span class="topic-badge">OPS • Modern</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">THE BIG IDEA</div>
      <div class="concept-title">Stop Clicking, Start Declaring</div>
      <div class="concept-desc">The old way: log into a server, click through setup wizards, run commands manually, hope you remember what you did. The problem? It's not repeatable, not documented, and "works on my server" becomes a nightmare. Infrastructure as Code (IaC) means defining your servers, networks, and configs in version-controlled text files. Run the file → get identical infrastructure every time. This is the foundation of modern operations.</div>
      <table class="ai-table">
        <thead><tr><th>Manual (Old Way)</th><th>IaC (Modern Way)</th></tr></thead>
        <tbody>
          <tr><td>Click through cloud console</td><td>Define in code, run once</td></tr>
          <tr><td>"How did we set this up?" — nobody knows</td><td>The code IS the documentation</td></tr>
          <tr><td>Snowflake servers (each unique)</td><td>Identical, reproducible environments</td></tr>
          <tr><td>Disaster recovery = panic</td><td>Disaster recovery = re-run the code</td></tr>
          <tr><td>No change history</td><td>Git history of every infra change</td></tr>
        </tbody>
      </table>
    </div>
    <div class="concept-card">
      <div class="concept-label">DECLARATIVE VS IMPERATIVE</div>
      <div class="concept-title">Describe the Destination, Not the Route</div>
      <div class="concept-desc"><strong>Imperative</strong>: list every step ("install nginx, then edit config, then start service"). <strong>Declarative</strong>: describe the desired end state ("nginx should be installed and running"), and the tool figures out how to get there. Declarative is idempotent — running it 100 times produces the same result as running it once. Most modern IaC is declarative.</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">THE TOOL LANDSCAPE</div>
      <div class="concept-title">Common IaC and Config Management Tools</div>
      <table class="ai-table">
        <thead><tr><th>Tool</th><th>Category</th><th>Language</th><th>Best For</th></tr></thead>
        <tbody>
          <tr><td>Terraform / OpenTofu</td><td>Provisioning</td><td>HCL (declarative)</td><td>Creating cloud resources (VMs, networks, DBs)</td></tr>
          <tr><td>Ansible</td><td>Config management</td><td>YAML (declarative)</td><td>Configuring servers, app deployment (agentless)</td></tr>
          <tr><td>Puppet</td><td>Config management</td><td>Puppet DSL</td><td>Large fleets, enforced desired state (agent)</td></tr>
          <tr><td>Chef</td><td>Config management</td><td>Ruby</td><td>Complex config (agent-based)</td></tr>
          <tr><td>CloudFormation</td><td>Provisioning</td><td>YAML/JSON</td><td>AWS-native infrastructure</td></tr>
          <tr><td>Pulumi</td><td>Provisioning</td><td>Python/TS/Go</td><td>Teams who prefer real programming languages</td></tr>
        </tbody>
      </table>
    </div>
    <div class="concept-card">
      <div class="concept-label">ANSIBLE BASICS</div>
      <div class="concept-title">The Most Beginner-Friendly IaC Tool</div>
      <div class="concept-desc">Ansible is popular for beginners because it's agentless (just needs SSH), uses readable YAML, and requires nothing installed on target machines. A "playbook" describes the desired state of a set of hosts.</div>
      <div class="code-block"><span class="com"># inventory.ini — define your hosts</span>
[webservers]
web1.example.com
web2.example.com

[dbservers]
db1.example.com

<span class="com"># ─────────────────────────────────────────────────────</span>
<span class="com"># playbook.yml — describe desired state</span>
- name: Configure web servers
  hosts: webservers
  become: yes              <span class="com"># use sudo</span>
  tasks:
    - name: Install nginx
      apt:
        name: nginx
        state: present     <span class="com"># declarative — "should exist"</span>

    - name: Start and enable nginx
      service:
        name: nginx
        state: started
        enabled: yes

    - name: Deploy config file
      copy:
        src: ./nginx.conf
        dest: /etc/nginx/nginx.conf
      notify: Restart nginx   <span class="com"># trigger handler if changed</span>

  handlers:
    - name: Restart nginx
      service:
        name: nginx
        state: restarted

<span class="com"># Run it</span>
ansible-playbook -i inventory.ini playbook.yml</div>
    </div>
  </div>
</div>
"""

# ─────────────────────────────── NET wave 15 ─────────────────────────────────
NET_SENTINEL = "<!-- BEGINNER15-NET v1 -->"
NET_CONTENT = """
<!-- BEGINNER15-NET v1 -->
<!-- ── TOPIC: VPNs AND TUNNELING ─────────────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">🔐</span>
    <span class="topic-name">VPNs &amp; Tunneling — Secure Connections Over Untrusted Networks</span>
    <span class="topic-badge">NET • Essential</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">WHAT A VPN ACTUALLY DOES</div>
      <div class="concept-title">An Encrypted Tunnel Through a Hostile Network</div>
      <div class="concept-desc">A VPN (Virtual Private Network) creates an encrypted tunnel between your device and a VPN server. Everything inside the tunnel is encrypted, so even on untrusted networks (coffee shop Wi-Fi), nobody can read your traffic. There are two distinct use cases that people confuse:</div>
      <table class="ai-table">
        <thead><tr><th>Type</th><th>Purpose</th><th>Example</th></tr></thead>
        <tbody>
          <tr><td><strong>Remote Access VPN</strong></td><td>Connect a remote user to a private corporate network</td><td>Working from home, accessing internal apps</td></tr>
          <tr><td><strong>Site-to-Site VPN</strong></td><td>Connect two networks (offices) over the internet</td><td>Branch office ↔ HQ network</td></tr>
          <tr><td><strong>Commercial VPN</strong></td><td>Privacy/geo-unblocking for consumers</td><td>NordVPN, hiding traffic from ISP</td></tr>
        </tbody>
      </table>
    </div>
    <div class="concept-card">
      <div class="concept-label">VPN PROTOCOLS</div>
      <div class="concept-title">How the Tunnel Is Built</div>
      <table class="ai-table">
        <thead><tr><th>Protocol</th><th>Notes</th></tr></thead>
        <tbody>
          <tr><td>WireGuard</td><td>Modern, fast, simple, ~4000 lines of code. Increasingly the default.</td></tr>
          <tr><td>OpenVPN</td><td>Mature, flexible, widely supported. SSL/TLS-based.</td></tr>
          <tr><td>IPsec/IKEv2</td><td>Built into most OSes, great for mobile (reconnects fast). Common for site-to-site.</td></tr>
          <tr><td>L2TP/IPsec</td><td>Older; L2TP provides tunnel, IPsec provides encryption.</td></tr>
          <tr><td>PPTP</td><td>Obsolete — broken encryption. Never use.</td></tr>
        </tbody>
      </table>
    </div>
    <div class="concept-card">
      <div class="concept-label">PROXIES VS VPNs</div>
      <div class="concept-title">Related But Different</div>
      <table class="ai-table">
        <thead><tr><th>Feature</th><th>Proxy</th><th>VPN</th></tr></thead>
        <tbody>
          <tr><td>Scope</td><td>Per-application (e.g., just the browser)</td><td>Entire device (all traffic)</td></tr>
          <tr><td>Encryption</td><td>Often none (just relays)</td><td>Always encrypted</td></tr>
          <tr><td>Layer</td><td>Application layer (L7)</td><td>Network layer (L3)</td></tr>
          <tr><td>Common use</td><td>Web filtering, caching, hiding origin IP</td><td>Secure remote access, privacy</td></tr>
        </tbody>
      </table>
      <div class="concept-desc">A <strong>forward proxy</strong> sits between users and the internet (corporate web filtering). A <strong>reverse proxy</strong> sits in front of servers (load balancing, TLS termination, hiding backend — e.g., nginx, Cloudflare).</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">SSH TUNNELING</div>
      <div class="concept-title">The Poor Man's VPN</div>
      <div class="concept-desc">SSH can forward ports through its encrypted connection — a quick way to securely reach services without a full VPN. Essential for accessing internal services through a jump host.</div>
      <div class="code-block"><span class="com"># Local port forward — reach a remote DB through SSH</span>
<span class="com"># "Make my localhost:5432 → db.internal:5432 via jumphost"</span>
ssh -L 5432:db.internal:5432 user@jumphost
<span class="com"># Now connect to localhost:5432 → actually hits db.internal</span>

<span class="com"># Remote port forward — expose YOUR local service to remote</span>
ssh -R 8080:localhost:3000 user@remote
<span class="com"># remote's :8080 → your local :3000</span>

<span class="com"># Dynamic forward — SOCKS proxy (route browser through SSH)</span>
ssh -D 1080 user@jumphost
<span class="com"># Set browser SOCKS proxy to localhost:1080</span>

<span class="com"># Jump through a bastion to reach an internal host</span>
ssh -J bastion.example.com user@internal-host</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">ZERO TRUST NETWORK ACCESS</div>
      <div class="concept-title">The VPN Replacement</div>
      <div class="concept-desc">Traditional VPNs give you access to the whole network once connected (overly trusting). Zero Trust Network Access (ZTNA) flips this: <em>"never trust, always verify."</em> Every request is authenticated and authorized individually, granting access only to specific applications — not the whole network. Tools like Cloudflare Access, Tailscale, and Zscaler implement this. Increasingly replacing legacy VPNs.</div>
    </div>
  </div>
</div>
"""

# ─────────────────────────────── LIFESTYLE wave 15 ───────────────────────────
LIFE_SENTINEL = "<!-- BEGINNER15-LIFE v1 -->"
LIFE_CONTENT = """
<!-- BEGINNER15-LIFE v1 -->
<!-- ── TOPIC: IT SURVIVAL MINDSETS ───────────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">🧠</span>
    <span class="topic-name">Survival Mindsets — Hard-Won Wisdom for a Long IT Career</span>
    <span class="topic-badge">LIFESTYLE • Wisdom</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">BOUNDARIES &amp; OWNERSHIP</div>
      <div class="concept-title">"Not My Circus, Not My Monkeys"</div>
      <div class="concept-desc">A Polish proverb (<em>"Nie mój cyrk, nie moje małpy"</em>) that every IT professional eventually learns the hard way. It means: not every problem is yours to solve, and not every fire is yours to put out. Burnout in IT comes largely from people absorbing responsibility for things outside their control or role — fixing problems caused by other teams' bad decisions, taking on emergencies that aren't theirs, getting emotionally invested in dysfunction they can't change.</div>
      <table class="ai-table">
        <thead><tr><th>Situation</th><th>Healthy Application</th></tr></thead>
        <tbody>
          <tr><td>Another team's repeated bad deploys break things</td><td>Document it, escalate to the right owner — don't silently keep firefighting their mess</td></tr>
          <tr><td>A drama-filled reorg you have no influence over</td><td>Do your job well; don't lose sleep over politics you can't change</td></tr>
          <tr><td>A user demanding you fix something outside your scope</td><td>Politely route them to the right team — being helpful ≠ being everyone's dumping ground</td></tr>
          <tr><td>A genuine emergency in YOUR area</td><td>This one IS your monkey — own it fully</td></tr>
        </tbody>
      </table>
      <div class="concept-desc"><strong>The balance:</strong> This is NOT an excuse for apathy or refusing to help. It's about distinguishing between what you're responsible for (own it completely) and what you're not (support appropriately, but don't carry the emotional and operational weight of every dysfunction). Knowing the difference is what keeps a 30-year career sustainable.</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">VERIFY, DON'T ASSUME</div>
      <div class="concept-title">"Assume Makes an Ass Out of U and Me"</div>
      <div class="concept-desc">ASSUME = ASS + U + ME. In technical work, assumptions are the root of most outages, security incidents, and wasted hours. The discipline of <em>verifying instead of assuming</em> is one of the highest-value habits in all of IT. Every senior engineer has a scar from an assumption that turned out wrong.</div>
      <table class="ai-table">
        <thead><tr><th>The Assumption</th><th>What Verifying Looks Like</th></tr></thead>
        <tbody>
          <tr><td>"The backup is working"</td><td>Actually restore from it and confirm the data is intact</td></tr>
          <tr><td>"This change is safe, it's tiny"</td><td>Test it in staging; tiny changes cause huge outages</td></tr>
          <tr><td>"The firewall is blocking that port"</td><td><code>nmap</code> it from outside and confirm</td></tr>
          <tr><td>"The user did what they said they did"</td><td>Check the logs — recollection is unreliable</td></tr>
          <tr><td>"It's probably DNS"</td><td>(It IS usually DNS — but confirm with <code>dig</code> before acting)</td></tr>
          <tr><td>"They got my email / understood the plan"</td><td>Confirm explicitly — silence is not agreement</td></tr>
        </tbody>
      </table>
      <div class="concept-desc"><strong>The professional habit:</strong> When you catch yourself thinking "it should be fine" or "they probably...", that's the exact moment to stop and verify. The cost of a 60-second check is almost always less than the cost of a wrong assumption. "Trust, but verify" — and in security, often just "verify."</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">LETTING GO OF CONTROL</div>
      <div class="concept-title">"You Can't Make Someone Make the Right Choice — But You Can Pick Up the Pieces Afterward"</div>
      <div class="concept-desc">You will constantly see people about to make bad decisions: skipping the security review, deploying on Friday at 5pm, ignoring the patch, reusing the weak password, declining the backup. You can advise. You can warn — clearly, in writing, professionally. But you cannot <em>force</em> an adult or another team to make the right call. Trying to control what isn't yours to control is a fast road to frustration and burnout.</div>
      <table class="ai-table">
        <thead><tr><th>Phase</th><th>What You Can Do</th></tr></thead>
        <tbody>
          <tr><td>Before the decision</td><td>Advise clearly, present risks/data, recommend the right path, document your recommendation in writing</td></tr>
          <tr><td>At the decision point</td><td>Accept that the decision is theirs to make (it's their authority/scope)</td></tr>
          <tr><td>If they choose poorly</td><td>Don't gloat, don't say "I told you so" — be ready to help recover</td></tr>
          <tr><td>After it breaks</td><td>Pick up the pieces calmly and competently. THIS is where you build trust and reputation.</td></tr>
        </tbody>
      </table>
      <div class="concept-desc"><strong>Why this matters:</strong> Document your recommendation (the written warning protects you and clarifies accountability). Then let go of the outcome. The engineer who stays calm, doesn't say "I told you so," and competently helps clean up the mess earns far more long-term respect and influence than the one who was technically right but bitter. Being right is worthless if you can't help recover — and your reputation is built in the recovery, not the warning.</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">PUTTING IT TOGETHER</div>
      <div class="concept-title">The Sustainable IT Professional</div>
      <div class="concept-desc">These three mindsets work as a system. <strong>Verify, don't assume</strong> keeps you technically rigorous and prevents self-inflicted disasters. <strong>Not my circus, not my monkeys</strong> protects your energy by clarifying what's actually yours to carry. <strong>You can't force the right choice, but you can pick up the pieces</strong> keeps you sane when others make mistakes you saw coming. Together they describe a professional who is rigorous about their own work, clear about their boundaries, and gracious when things go wrong — exactly the kind of person who lasts decades in this field without burning out or becoming cynical.</div>
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
        (SEC_INJECT_ANCHOR,    SEC_SENTINEL,    SEC_CONTENT),
        (OPS_INJECT_ANCHOR,    OPS_SENTINEL,    OPS_CONTENT),
        (NET_INJECT_ANCHOR,    NET_SENTINEL,    NET_CONTENT),
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
