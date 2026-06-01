#!/usr/bin/env python3
"""Wave 32 – DNS deep-dive, malware analysis, GRC NIST/ISO, advanced bash, IoT security."""
from pathlib import Path
from html.parser import HTMLParser

S_NET    = "<!-- BEGINNER32-NET v1 -->"
S_SEC    = "<!-- BEGINNER32-SEC v1 -->"
S_GRC    = "<!-- BEGINNER32-GRC v1 -->"
S_LINUX  = "<!-- BEGINNER32-LINUX v1 -->"
S_SCRIPT = "<!-- BEGINNER32-SCRIPT v1 -->"

A_NET    = "<!-- /domain-body net -->"
A_SEC    = "<!-- /domain-body sec -->"
A_GRC    = "<!-- /domain-body grc -->"
A_LINUX  = "<!-- /domain-body linux -->"
A_SCRIPT = "<!-- /domain-body script -->"

# ══════════════════════════════════════════════════════════════════════════
# NET – DNS deep-dive
# ══════════════════════════════════════════════════════════════════════════
C_NET = """
<!-- BEGINNER32-NET v1 -->
<!-- ── TOPIC: DNS Deep-Dive ───────────────────────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-badge">Beginner</span>
    DNS Deep-Dive – How Domain Names Actually Work
  </div>
  <div class="topic-body">

    <div class="concept-card">
      <div class="concept-label">Core Concept</div>
      <div class="concept-title">The DNS Resolution Walk</div>
      <div class="concept-desc">
        When you type <code>www.example.com</code> in a browser, this is what
        happens before the first byte of the page arrives:<br><br>
        1. Browser checks its <strong>local cache</strong> — did we look this up
           recently?<br>
        2. OS checks <strong>/etc/hosts</strong> (or Windows Hosts file) — manual
           overrides.<br>
        3. OS asks the <strong>Recursive Resolver</strong> (usually your router
           or ISP, or 8.8.8.8/1.1.1.1).<br>
        4. Resolver asks a <strong>Root Name Server</strong> (.): "Who handles
           <code>.com</code>?"<br>
        5. Root refers to the <strong>.com TLD server</strong>: "Ask
           <code>ns1.example.com</code>."<br>
        6. Resolver asks <code>ns1.example.com</code>: "What's the IP for
           <code>www</code>?"<br>
        7. <strong>Authoritative answer</strong> returned: <code>93.184.216.34</code>.<br>
        8. Resolver caches the result for the TTL; returns it to your browser.<br><br>
        Total time: usually 10–100 ms. Cached lookups: &lt;1 ms.
      </div>
    </div>

    <div class="concept-card">
      <div class="concept-label">Record Types</div>
      <div class="concept-title">DNS Record Types You Must Know</div>
      <div class="concept-desc">
        DNS stores different information in different record types:
      </div>
      <div class="code-block">
<span class="com">Record  Purpose                        Example</span>
A       IPv4 address                   www  A  93.184.216.34
AAAA    IPv6 address                   www  AAAA  2606:2800::1
CNAME   Alias to another name          blog  CNAME  myapp.netlify.app.
MX      Mail server (+ priority)       @    MX 10  mail.example.com.
TXT     Arbitrary text (SPF, DKIM)     @    TXT  "v=spf1 include:..."
NS      Authoritative name servers     @    NS   ns1.example.com.
PTR     Reverse lookup (IP → name)     34.216.184.93.in-addr.arpa  PTR  www.example.com.
SOA     Zone metadata (serial, TTL)    Start of Authority record
SRV     Service location               _sip._tcp  SRV  10 5 5060 sip.example.com.

<span class="com"># Query DNS with dig</span>
dig www.example.com A               <span class="com"># IPv4</span>
dig www.example.com AAAA            <span class="com"># IPv6</span>
dig example.com MX                  <span class="com"># mail servers</span>
dig example.com TXT                 <span class="com"># SPF / DKIM / verification tokens</span>
dig -x <span class="num">93.184.216.34</span>               <span class="com"># reverse lookup (PTR)</span>
dig @<span class="num">8.8.8.8</span> www.example.com       <span class="com"># use Google's resolver</span>
dig +trace www.example.com          <span class="com"># walk the full resolution chain</span>
      </div>
    </div>

    <div class="concept-card">
      <div class="concept-label">Security</div>
      <div class="concept-title">DNS Security – DNSSEC, DoH, DNS Attacks</div>
      <div class="concept-desc">
        DNS was designed in the 1980s with no security. Several attacks exploit this:<br><br>
        <strong>DNS Cache Poisoning</strong> — attacker injects a false record
        into a resolver's cache so users get sent to the wrong IP.<br>
        <em>Fix:</em> DNSSEC — cryptographic signatures on DNS records.<br><br>
        <strong>DNS Hijacking</strong> — malware or rogue ISP changes the
        resolver you use.<br>
        <em>Fix:</em> DNS-over-HTTPS (DoH) or DNS-over-TLS (DoT) —
        encrypts queries so no one can tamper in transit.<br><br>
        <strong>DNS Tunnelling</strong> — attacker encodes data inside DNS
        queries to exfiltrate data or establish C2 (bypasses firewalls).<br>
        <em>Fix:</em> Monitor for unusually long query names, high query
        volume per host, rare TLDs.<br><br>
        <em>"Assume" makes an ass out of you and me</em> — never assume DNS
        responses are authentic unless DNSSEC is validated end-to-end.
      </div>
      <div class="code-block">
<span class="com"># Check if a domain has DNSSEC enabled</span>
dig example.com DNSKEY +short
dig example.com DS +short

<span class="com"># Test DNS-over-HTTPS (Cloudflare DoH)</span>
curl -sH <span class="str">"accept: application/dns-json"</span> \
  <span class="str">"https://cloudflare-dns.com/dns-query?name=example.com&amp;type=A"</span> | \
  python3 -m json.tool

<span class="com"># Detect suspicious long DNS names (potential tunnelling)</span>
<span class="com"># In tcpdump: capture DNS on port 53</span>
sudo tcpdump -i eth0 -w dns.pcap port <span class="num">53</span>
<span class="com"># Then grep for names longer than 50 chars</span>
tshark -r dns.pcap -T fields -e dns.qry.name | \
  awk <span class="str">'length &gt; 50'</span> | sort | uniq -c | sort -rn
      </div>
    </div>

    <div class="concept-card">
      <div class="concept-label">Operations</div>
      <div class="concept-title">Managing DNS Zones</div>
      <div class="concept-desc">
        Whether you use Route 53, Cloudflare, or BIND on-prem, the
        concepts are the same. Best practices:<br><br>
        &bull; Set <strong>low TTLs</strong> (e.g. 300 s) before planned
          changes; restore high TTLs (3600+) after.<br>
        &bull; Always have <strong>at least two NS servers</strong> in
          different locations for redundancy.<br>
        &bull; Use <strong>split-horizon DNS</strong> — internal names
          resolve to private IPs; external names resolve to public IPs.<br>
        &bull; Add <strong>SPF, DKIM, DMARC</strong> TXT records for every
          domain that sends email to prevent spoofing.<br>
        &bull; <em>You can't make someone make the right choice, yet you
          can pick up the pieces afterwards</em> — when a TTL-expired
          stale record sends users to a dead IP, reduce TTL proactively
          next time.
      </div>
    </div>

  </div>
</div>
"""

# ══════════════════════════════════════════════════════════════════════════
# SEC – Malware analysis basics
# ══════════════════════════════════════════════════════════════════════════
C_SEC = """
<!-- BEGINNER32-SEC v1 -->
<!-- ── TOPIC: Malware Analysis Basics ────────────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-badge">Beginner</span>
    Malware Analysis – Static &amp; Dynamic Analysis Fundamentals
  </div>
  <div class="topic-body">

    <div class="concept-card">
      <div class="concept-label">Core Concept</div>
      <div class="concept-title">What Is Malware Analysis?</div>
      <div class="concept-desc">
        <strong>Malware analysis</strong> is the process of understanding what
        a malicious file does. There are two approaches:<br><br>
        <strong>Static analysis</strong> — examine the file without running it.
        Look at strings, headers, imports, code structure.<br>
        <em>Safe but limited</em> — obfuscated malware hides its behaviour.<br><br>
        <strong>Dynamic analysis</strong> — run the file in an isolated
        sandbox and observe its behaviour (network calls, file writes,
        registry changes, process spawning).<br>
        <em>Reveals behaviour but requires a safe environment.</em><br><br>
        <strong>The golden rule:</strong> never run malware on a production or
        host machine. Always use a dedicated, isolated VM (snapshots
        enabled, no network or host-only network).<br><br>
        <em>"Not my circus, not my monkey"</em> — reverse engineering packed
        malware is a specialist skill. For most incidents, initial triage
        with static analysis + a sandbox is enough to classify the threat.
      </div>
    </div>

    <div class="concept-card">
      <div class="concept-label">Static Analysis</div>
      <div class="concept-title">Triage a Suspicious File Without Running It</div>
      <div class="concept-desc">
        These tools work on Linux and give you a lot of information
        before you ever execute anything.
      </div>
      <div class="code-block">
<span class="com"># 1. Get a hash (share with VirusTotal)</span>
sha256sum suspicious.exe
md5sum suspicious.exe

<span class="com"># 2. Identify the file type (never trust the extension)</span>
file suspicious.exe
<span class="com"># Output: PE32 executable (GUI) Intel 80386, for MS Windows</span>

<span class="com"># 3. Extract human-readable strings</span>
strings suspicious.exe | grep -E <span class="str">'(http|cmd|powershell|reg |HKEY)'</span>
strings -el suspicious.exe   <span class="com"># Unicode strings (wide char)</span>

<span class="com"># 4. Check PE headers (Windows executables)</span>
<span class="com"># Install: pip install pefile</span>
python3 - &lt;&lt;<span class="str">'EOF'</span>
import pefile
pe = pefile.PE(<span class="str">"suspicious.exe"</span>)
print(<span class="str">"Imports:"</span>)
for entry in pe.DIRECTORY_ENTRY_IMPORT:
    print(<span class="str">" "</span>, entry.dll.decode())
    for imp in entry.imports:
        print(<span class="str">"   "</span>, imp.name.decode() if imp.name else hex(imp.ordinal))
<span class="str">EOF</span>

<span class="com"># 5. Check entropy (high entropy = packed/encrypted = suspicious)</span>
<span class="com"># Install: pip install pefile</span>
python3 -c <span class="str">"import pefile; pe=pefile.PE('suspicious.exe'); [print(s.Name,s.get_entropy()) for s in pe.sections]"</span>
<span class="com"># Entropy &gt; 7.0 in a .text section usually means packer/encryption</span>

<span class="com"># 6. Submit to VirusTotal (no execution, just hash lookup)</span>
curl -s --request GET \
  --url <span class="str">"https://www.virustotal.com/api/v3/files/$(sha256sum suspicious.exe | cut -d' ' -f1)"</span> \
  --header <span class="str">"x-apikey: YOUR_VT_KEY"</span> | python3 -m json.tool | grep -A2 last_analysis_stats
      </div>
    </div>

    <div class="concept-card">
      <div class="concept-label">Dynamic Analysis</div>
      <div class="concept-title">Sandbox Analysis &amp; Behavioural Indicators</div>
      <div class="concept-desc">
        Free online sandboxes: <strong>Any.Run</strong>, <strong>Hybrid
        Analysis</strong>, <strong>Joe Sandbox</strong>. Upload the file;
        get a full behavioural report in minutes without running anything
        locally.<br><br>
        When reading a sandbox report, look for <strong>Indicators of
        Compromise (IoCs)</strong>:<br><br>
        &bull; <em>Network</em>: C2 server IPs/domains, beaconing intervals,
          unusual ports.<br>
        &bull; <em>Files</em>: dropped executables, modified startup folders,
          scheduled tasks created.<br>
        &bull; <em>Registry</em>: <code>HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run</code>
          — persistence mechanism.<br>
        &bull; <em>Processes</em>: PowerShell spawned by Word/Excel
          (macro malware), cmd.exe spawned by browser.<br>
        &bull; <em>MITRE ATT&amp;CK</em>: sandbox reports map behaviours to
          ATT&amp;CK tactics and techniques.
      </div>
    </div>

    <div class="concept-card">
      <div class="concept-label">Response</div>
      <div class="concept-title">After Malware Is Confirmed — What To Do</div>
      <div class="concept-desc">
        <em>You can't make someone make the right choice, yet you can pick
        up the pieces afterwards.</em> When a user opens a phishing
        attachment:<br><br>
        1. <strong>Isolate</strong> the machine (pull the network cable or
           disable NIC via remote management).<br>
        2. <strong>Preserve</strong> a memory image if possible
          (<code>winpmem</code> on Windows).<br>
        3. <strong>Collect IoCs</strong> (hashes, IPs, domains, registry
          keys) from the malware analysis.<br>
        4. <strong>Hunt</strong> across the fleet — was the same file
          opened on other machines? (EDR/SIEM query by hash).<br>
        5. <strong>Block</strong> IoCs at firewall, DNS, and email gateway.<br>
        6. <strong>Eradicate &amp; restore</strong> — reimage from known
          good backup; patch the vulnerability that was exploited.<br>
        7. <strong>Document &amp; improve</strong> — update playbooks,
          add detection rules, conduct phishing awareness training.
      </div>
    </div>

  </div>
</div>
"""

# ══════════════════════════════════════════════════════════════════════════
# GRC – NIST CSF and ISO 27001 for beginners
# ══════════════════════════════════════════════════════════════════════════
C_GRC = """
<!-- BEGINNER32-GRC v1 -->
<!-- ── TOPIC: NIST CSF & ISO 27001 Intro ─────────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-badge">Beginner</span>
    NIST CSF &amp; ISO 27001 – GRC Frameworks Explained
  </div>
  <div class="topic-body">

    <div class="concept-card">
      <div class="concept-label">Core Concept</div>
      <div class="concept-title">Why Frameworks Exist</div>
      <div class="concept-desc">
        Security teams face endless possible controls and threats. A
        <strong>framework</strong> is a structured, vendor-neutral map that
        helps organisations decide <em>what to do</em> and prove to
        auditors they are doing it.<br><br>
        <strong>Two you will encounter everywhere:</strong><br><br>
        &bull; <em>NIST Cybersecurity Framework (CSF)</em> — a US government
          framework widely adopted globally. Voluntary; practical. Free.<br>
        &bull; <em>ISO/IEC 27001</em> — an international standard. Auditable;
          leads to a formal certification. Costs money to audit.<br><br>
        <em>"Not my circus, not my monkey"</em> — as a junior analyst you
        don't own compliance, but you will be asked to evidence controls.
        Knowing the framework language makes you valuable from day one.
      </div>
    </div>

    <div class="concept-card">
      <div class="concept-label">NIST CSF</div>
      <div class="concept-title">The Six CSF Functions</div>
      <div class="concept-desc">
        NIST CSF 2.0 organises security activities into six <em>Functions</em>.
        Think of them as the security life-cycle:
      </div>
      <div class="code-block">
<span class="com">Function    Colour  What it means</span>
GOVERN      Blue    Org-level policies, roles, risk strategy
IDENTIFY    Yellow  Know your assets, data, risks
PROTECT     Green   Controls to prevent incidents
DETECT      Orange  Monitoring to catch incidents
RESPOND     Red     Contain &amp; handle an incident
RECOVER     Purple  Restore operations; lessons learned

<span class="com">Each function has Categories → Sub-categories (controls)</span>
<span class="com">Example controls per function:</span>

IDENTIFY:
  - Asset inventory (hardware, software, data)
  - Risk assessment process
  - Vendor/third-party risk program

PROTECT:
  - Identity management (MFA, PAM)
  - Data encryption at rest and in transit
  - Security awareness training
  - Patch management

DETECT:
  - SIEM / log monitoring
  - Intrusion detection system (IDS)
  - Anomaly detection

RESPOND:
  - Incident response plan (IRP)
  - Communication procedures
  - Evidence preservation

RECOVER:
  - Backup &amp; restore procedures
  - Disaster recovery plan (DRP)
  - Post-incident review
      </div>
    </div>

    <div class="concept-card">
      <div class="concept-label">ISO 27001</div>
      <div class="concept-title">ISO 27001 Structure in Plain English</div>
      <div class="concept-desc">
        ISO 27001 requires organisations to build an <strong>Information
        Security Management System (ISMS)</strong> — a set of documented
        policies, processes, and controls that are continuously improved.<br><br>
        <strong>Annex A</strong> lists 93 controls across 4 themes:<br>
        &bull; Organisational controls (policies, roles, supplier relations).<br>
        &bull; People controls (screening, training, disciplinary process).<br>
        &bull; Physical controls (access to buildings, equipment disposal).<br>
        &bull; Technological controls (access control, encryption, monitoring).<br><br>
        The audit process:<br>
        1. <strong>Stage 1</strong> — auditor reviews your documentation.<br>
        2. <strong>Stage 2</strong> — auditor observes processes &amp; interviews staff.<br>
        3. <strong>Surveillance</strong> — annual follow-up audits.<br>
        4. <strong>Recertification</strong> — full audit every 3 years.<br><br>
        <em>"Assume" makes an ass out of you and me</em> — never assume a
        control is implemented just because a policy document says so.
        Auditors look for <em>evidence</em> (logs, screenshots, tickets).
      </div>
    </div>

    <div class="concept-card">
      <div class="concept-label">Risk Register</div>
      <div class="concept-title">How to Build a Simple Risk Register</div>
      <div class="concept-desc">
        Both frameworks require a <strong>risk register</strong> — a living
        document that tracks risks, their likelihood, impact, and treatment.
      </div>
      <div class="code-block">
<span class="com">Risk Register (simplified)</span>

ID    Risk                    Likelihood  Impact  Score  Treatment
R-01  Unpatched VMs exploited High(3)     High(3)   9    Patch within 30 days SLA
R-02  Phishing → cred theft   High(3)     Med(2)    6    MFA rollout + awareness training
R-03  Ransomware via RDP      Med(2)      High(3)   6    Disable RDP, use VPN+Bastion
R-04  Vendor data breach      Low(1)      High(3)   3    Annual vendor security review
R-05  Physical server theft   Low(1)      Med(2)    2    Cage locks, CCTV, accepted residual

<span class="com">Score = Likelihood × Impact (1–3 scale)</span>
<span class="com">Treatment options: Mitigate / Transfer (insurance) / Accept / Avoid</span>

<span class="com"># Python: quick risk score calculator</span>
risks = [
    (<span class="str">"Unpatched VMs"</span>, <span class="num">3</span>, <span class="num">3</span>),
    (<span class="str">"Phishing"</span>,      <span class="num">3</span>, <span class="num">2</span>),
    (<span class="str">"RDP ransomware"</span>, <span class="num">2</span>, <span class="num">3</span>),
]
<span class="kw">for</span> name, likelihood, impact <span class="kw">in</span> sorted(risks, key=<span class="kw">lambda</span> x: -x[<span class="num">1</span>]*x[<span class="num">2</span>]):
    <span class="fn">print</span>(<span class="fn">f</span><span class="str">"{name:25s}  score={likelihood*impact}"</span>)
      </div>
    </div>

  </div>
</div>
"""

# ══════════════════════════════════════════════════════════════════════════
# LINUX – Advanced bash scripting patterns
# ══════════════════════════════════════════════════════════════════════════
C_LINUX = """
<!-- BEGINNER32-LINUX v1 -->
<!-- ── TOPIC: Advanced Bash Scripting Patterns ────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-badge">Intermediate</span>
    Advanced Bash Scripting – Patterns for Reliable Scripts
  </div>
  <div class="topic-body">

    <div class="concept-card">
      <div class="concept-label">Robustness</div>
      <div class="concept-title">The Safe-Script Header</div>
      <div class="concept-desc">
        Every production bash script should start with these four settings.
        They turn silent failures into loud, debuggable errors.
      </div>
      <div class="code-block">
#!/usr/bin/env bash
set -euo pipefail

<span class="com"># set -e  : exit immediately on any command error</span>
<span class="com"># set -u  : treat unset variables as errors (catches typos)</span>
<span class="com"># set -o pipefail : pipeline fails if any command in it fails</span>
<span class="com">#           (without this: cmd1 | cmd2  — cmd1 failure is hidden)</span>

<span class="com"># Add a trap to print the line number that failed</span>
trap <span class="str">'echo "ERROR: line $LINENO exit code $?"'</span> ERR

<span class="com"># Constant: mark read-only variables</span>
readonly LOG_DIR=<span class="str">"/var/log/myapp"</span>
readonly MAX_RETRIES=<span class="num">3</span>

<span class="com"># ─── Example: fail loudly ────────────────────────────────────</span>
# Without set -u:  echo $UNSET_VAR  → empty string (silent bug)
# With    set -u:  echo $UNSET_VAR  → "unbound variable" error → exit
      </div>
    </div>

    <div class="concept-card">
      <div class="concept-label">Functions</div>
      <div class="concept-title">Reusable Functions &amp; Logging</div>
      <div class="concept-desc">
        Good scripts have a <code>log</code> function, a <code>die</code>
        function, and small single-purpose helper functions.
      </div>
      <div class="code-block">
#!/usr/bin/env bash
set -euo pipefail

<span class="com"># Logging with timestamps and levels</span>
log()  { echo <span class="str">"[$(date +%T)] INFO  $*"</span>  ; }
warn() { echo <span class="str">"[$(date +%T)] WARN  $*"</span> &gt;&amp;<span class="num">2</span>; }
die()  { echo <span class="str">"[$(date +%T)] ERROR $*"</span> &gt;&amp;<span class="num">2</span>; exit <span class="num">1</span>; }

<span class="com"># Check dependencies at script start</span>
require() {
    for cmd in <span class="str">"$@"</span>; do
        command -v <span class="str">"$cmd"</span> &gt;/dev/null <span class="num">2</span>&gt;&amp;<span class="num">1</span> || die <span class="str">"Required: $cmd"</span>
    done
}
require curl jq aws

<span class="com"># Retry a command up to N times with backoff</span>
retry() {
    local max=<span class="str">"$1"</span>; shift
    local delay=<span class="num">2</span>
    local attempt=<span class="num">1</span>
    <span class="kw">while</span> ! <span class="str">"$@"</span>; do
        (( attempt++ ))
        [[ attempt -gt max ]] &amp;&amp; die <span class="str">"Command failed after $max attempts: $*"</span>
        warn <span class="str">"Attempt $attempt/$max failed. Retrying in ${delay}s..."</span>
        sleep <span class="str">"$delay"</span>
        (( delay *= <span class="num">2</span> ))
    done
}

retry <span class="num">3</span> curl -sf https://api.example.com/health
log <span class="str">"Health check passed"</span>
      </div>
    </div>

    <div class="concept-card">
      <div class="concept-label">Input Handling</div>
      <div class="concept-title">Argument Parsing &amp; Validation</div>
      <div class="concept-desc">
        Scripts that accept arguments need clear usage messages and
        input validation. Use <code>getopts</code> for short flags or
        manual <code>case</code> for long options.
      </div>
      <div class="code-block">
#!/usr/bin/env bash
set -euo pipefail
die() { echo "ERROR: $*" &gt;&amp;<span class="num">2</span>; exit <span class="num">1</span>; }

usage() {
    cat &lt;&lt;<span class="str">EOF
Usage: $0 -e ENV -r REGION [-d]
  -e  Environment (dev|staging|prod)
  -r  AWS region  (e.g. us-east-1)
  -d  Dry-run mode (no changes)
EOF</span>
    exit <span class="num">1</span>
}

ENV=<span class="str">""</span>; REGION=<span class="str">""</span>; DRYRUN=false

while getopts <span class="str">":e:r:dh"</span> opt; do
    case <span class="str">"$opt"</span> in
        e) ENV=<span class="str">"$OPTARG"</span>   ;;
        r) REGION=<span class="str">"$OPTARG"</span> ;;
        d) DRYRUN=true    ;;
        h|*) usage        ;;
    esac
done

[[ -z <span class="str">"$ENV"</span>    ]] &amp;&amp; die <span class="str">"Environment (-e) is required"</span>
[[ -z <span class="str">"$REGION"</span> ]] &amp;&amp; die <span class="str">"Region (-r) is required"</span>
[[ <span class="str">"$ENV"</span> =~ ^(dev|staging|prod)$ ]] || die <span class="str">"Invalid env: $ENV"</span>

echo <span class="str">"Deploying to $ENV / $REGION (dryrun=$DRYRUN)"</span>
<span class="kw">if</span> [[ <span class="str">"$DRYRUN"</span> == false ]]; then
    echo <span class="str">"... would deploy here ..."</span>
fi
      </div>
    </div>

    <div class="concept-card">
      <div class="concept-label">Process Control</div>
      <div class="concept-title">Background Jobs, Signals &amp; Cleanup</div>
      <div class="concept-desc">
        Production scripts often run long background jobs and need to
        clean up temp files even if they are interrupted.
      </div>
      <div class="code-block">
#!/usr/bin/env bash
set -euo pipefail

TMPDIR_WORK=$(mktemp -d)

<span class="com"># Cleanup on exit, interrupt, or error</span>
cleanup() { rm -rf <span class="str">"$TMPDIR_WORK"</span>; echo <span class="str">"Cleaned up $TMPDIR_WORK"</span>; }
trap cleanup EXIT INT TERM

<span class="com"># Run two jobs in parallel, wait for both</span>
process_chunk() {
    local chunk=<span class="str">"$1"</span>
    echo <span class="str">"Processing $chunk ..."</span>
    sleep <span class="num">2</span>   <span class="com"># simulate work</span>
    echo <span class="str">"Done $chunk"</span>
}

for chunk in A B C; do
    process_chunk <span class="str">"$chunk"</span> &amp;   <span class="com"># &amp; runs in background</span>
done
wait    <span class="com"># wait for all background jobs to finish</span>
echo <span class="str">"All chunks processed"</span>

<span class="com"># Check exit code of a background job</span>
my_job &amp;
job_pid=$!
wait <span class="str">"$job_pid"
job_exit=$?
[[ $job_exit -eq 0 ]]</span> || die <span class="str">"my_job failed (exit $job_exit)"</span>
      </div>
    </div>

  </div>
</div>
"""

# ══════════════════════════════════════════════════════════════════════════
# SCRIPT – IoT and embedded system security for beginners
# ══════════════════════════════════════════════════════════════════════════
C_SCRIPT = """
<!-- BEGINNER32-SCRIPT v1 -->
<!-- ── TOPIC: IoT Security Fundamentals ──────────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-badge">Beginner</span>
    IoT Security – Securing Connected Devices
  </div>
  <div class="topic-body">

    <div class="concept-card">
      <div class="concept-label">Core Concept</div>
      <div class="concept-title">Why IoT Is a Security Problem</div>
      <div class="concept-desc">
        <strong>IoT (Internet of Things)</strong> devices — cameras, smart
        TVs, routers, industrial sensors, medical devices — are computers
        with network access. Unlike PCs, they often:<br><br>
        &bull; Ship with <strong>default credentials</strong> that users never
          change.<br>
        &bull; Run <strong>outdated Linux kernels</strong> with no automatic
          updates.<br>
        &bull; Expose <strong>unnecessary services</strong> (Telnet, FTP,
          unencrypted HTTP) on open ports.<br>
        &bull; Have <strong>no monitoring</strong> — nobody watches their
          logs.<br>
        &bull; Are deployed and <strong>forgotten</strong> for years.<br><br>
        The Mirai botnet (2016) compromised 600,000+ IoT devices by
        simply trying default username/password combinations and used them
        to launch the largest DDoS attack in history at the time.
        <br><br>
        <em>"Assume" makes an ass out of you and me</em> — never assume a
        device is secure because it's "just a camera" or "just a
        thermostat." Assume it is a fully capable Linux box sitting on
        your network.
      </div>
    </div>

    <div class="concept-card">
      <div class="concept-label">Discovery</div>
      <div class="concept-title">Finding IoT Devices on Your Network</div>
      <div class="concept-desc">
        You cannot protect what you cannot see. These tools enumerate
        every device on the network:
      </div>
      <div class="code-block">
<span class="com"># Discover all hosts on the LAN (ping sweep)</span>
nmap -sn <span class="num">192.168.1</span>.0/<span class="num">24</span>

<span class="com"># Identify OS and open ports of every host</span>
sudo nmap -O -sV <span class="num">192.168.1</span>.0/<span class="num">24</span> -oN lan_scan.txt

<span class="com"># Find devices running Telnet (port 23) — a huge red flag</span>
nmap -p <span class="num">23</span> --open <span class="num">192.168.1</span>.0/<span class="num">24</span>

<span class="com"># Find devices with default web UIs (port 80/8080)</span>
nmap -p <span class="num">80,8080,8443</span> --open <span class="num">192.168.1</span>.0/<span class="num">24</span>

<span class="com"># Banner grab — what software version is running?</span>
nc -zv <span class="num">192.168.1</span>.<span class="num">50</span> <span class="num">80</span>
curl -I http://<span class="num">192.168.1</span>.<span class="num">50</span>  <span class="com"># look at Server: header</span>

<span class="com"># Search Shodan for devices exposed to the internet</span>
<span class="com"># (Shodan indexes internet-facing devices — use only for research)</span>
<span class="com"># Web: shodan.io/search?query=camera+default+password</span>
      </div>
    </div>

    <div class="concept-card">
      <div class="concept-label">Hardening</div>
      <div class="concept-title">IoT Security Checklist</div>
      <div class="concept-desc">
        Apply these controls to every IoT device you manage:
      </div>
      <div class="code-block">
<span class="com">MUST-DO IoT HARDENING CHECKLIST</span>
<span class="com">───────────────────────────────────────────────────────────</span>

[ ] Change default credentials immediately after provisioning
[ ] Disable Telnet (port 23); use SSH if CLI access is needed
[ ] Disable UPnP — it auto-opens firewall holes without your knowledge
[ ] Segment IoT devices on a separate VLAN
    (IoT VLAN can reach internet but NOT corporate LAN)
[ ] Update firmware to the latest version
[ ] Set up automatic update notifications or a review schedule
[ ] Disable unused services (FTP, SNMP v1/v2 community string "public")
[ ] Change SNMP community strings to strong random values
[ ] Use HTTPS for web management; verify certificate
[ ] Enable logging and send logs to your SIEM if possible
[ ] Block inbound internet access to IoT devices at firewall
[ ] Physically label devices with their VLAN and last audit date

<span class="com"># Create an IoT VLAN rule (iptables — IoT VLAN is 192.168.10.0/24)</span>
<span class="com"># Allow IoT → internet but block IoT → corporate (192.168.1.0/24)</span>
sudo iptables -I FORWARD -s <span class="num">192.168.10</span>.0/<span class="num">24</span> \
  -d <span class="num">192.168.1</span>.0/<span class="num">24</span> -j DROP
sudo iptables -I FORWARD -s <span class="num">192.168.10</span>.0/<span class="num">24</span> \
  -d <span class="num">0</span>.0.0.0/<span class="num">0</span> -j ACCEPT
      </div>
    </div>

    <div class="concept-card">
      <div class="concept-label">Firmware Analysis</div>
      <div class="concept-title">Basic Firmware Triage with Binwalk</div>
      <div class="concept-desc">
        Firmware is the operating system of an embedded device. Security
        researchers extract and analyse firmware images to find hardcoded
        credentials, old vulnerable software, and backdoors.
        <em>Only analyse firmware you have permission to test.</em>
      </div>
      <div class="code-block">
<span class="com"># Install binwalk (firmware analysis tool)</span>
sudo apt install binwalk

<span class="com"># Scan a firmware image for embedded file systems</span>
binwalk firmware.bin

<span class="com"># Extract all file systems and compressed archives</span>
binwalk -e firmware.bin
<span class="com"># Creates _firmware.bin.extracted/</span>

<span class="com"># Search for hardcoded passwords in extracted filesystem</span>
grep -r <span class="str">"password"</span>  _firmware.bin.extracted/ --include=<span class="str">"*.conf"</span>
grep -r <span class="str">"passwd"</span>    _firmware.bin.extracted/etc/
cat _firmware.bin.extracted/etc/shadow  <span class="com"># hashed passwords</span>

<span class="com"># Look for SSL private keys</span>
find _firmware.bin.extracted/ -name <span class="str">"*.pem"</span> -o -name <span class="str">"*.key"</span>

<span class="com"># Find SUID binaries in the extracted filesystem</span>
find _firmware.bin.extracted/ -perm -<span class="num">4000</span> <span class="num">2</span>&gt;/dev/null
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
    (A_NET,    S_NET,    C_NET),
    (A_SEC,    S_SEC,    C_SEC),
    (A_GRC,    S_GRC,    C_GRC),
    (A_LINUX,  S_LINUX,  C_LINUX),
    (A_SCRIPT, S_SCRIPT, C_SCRIPT),
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
