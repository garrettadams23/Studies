#!/usr/bin/env python3
"""Wave 34 – Docker security, packet analysis, vendor risk mgmt, LVM, IT soft skills."""
from pathlib import Path
from html.parser import HTMLParser

S_SEC      = "<!-- BEGINNER34-SEC v1 -->"
S_NET      = "<!-- BEGINNER34-NET v1 -->"
S_GRC      = "<!-- BEGINNER34-GRC v1 -->"
S_LINUX    = "<!-- BEGINNER34-LINUX v1 -->"
S_LIFESTYLE= "<!-- BEGINNER34-LIFESTYLE v1 -->"

A_SEC      = "<!-- /domain-body sec -->"
A_NET      = "<!-- /domain-body net -->"
A_GRC      = "<!-- /domain-body grc -->"
A_LINUX    = "<!-- /domain-body linux -->"
A_LIFESTYLE= "<!-- /domain-body lifestyle -->"

# ══════════════════════════════════════════════════════════════════════════
# SEC – Docker / container security hardening
# ══════════════════════════════════════════════════════════════════════════
C_SEC = """
<!-- BEGINNER34-SEC v1 -->
<!-- ── TOPIC: Container Security Hardening ───────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-badge">Beginner</span>
    Container Security – Hardening Docker &amp; Images
  </div>
  <div class="topic-body">

    <div class="concept-card">
      <div class="concept-label">Core Concept</div>
      <div class="concept-title">The Container Threat Model</div>
      <div class="concept-desc">
        Containers share the host's kernel — they are <em>not</em> as
        isolated as virtual machines. A misconfigured container can:<br><br>
        &bull; Access the host filesystem (if volumes are mis-mounted).<br>
        &bull; Escape to the host (kernel exploits, privileged mode).<br>
        &bull; Run as root inside the container — and root in a container
          can sometimes mean root on the host.<br>
        &bull; Pull a malicious base image from a public registry.<br><br>
        <strong>Defence-in-depth layers for containers:</strong><br>
        1. Secure the image (what you build).<br>
        2. Secure the registry (where images are stored).<br>
        3. Secure the runtime (how containers run).<br>
        4. Secure the orchestrator (Kubernetes RBAC, network policies).<br><br>
        <em>"Assume" makes an ass out of you and me</em> — never assume a
        public Docker Hub image is safe just because it has many downloads.
        Scan it first.
      </div>
    </div>

    <div class="concept-card">
      <div class="concept-label">Image Hardening</div>
      <div class="concept-title">Writing a Secure Dockerfile</div>
      <div class="concept-desc">
        Most container vulnerabilities are introduced at build time.
        Compare an insecure Dockerfile to a hardened one:
      </div>
      <div class="code-block">
<span class="com">─── INSECURE (common beginner mistakes) ──────────────────────</span>
FROM ubuntu:latest          <span class="com"># 'latest' = unpredictable, large attack surface</span>
RUN apt-get update &amp;&amp; apt-get install -y python3 curl vim
COPY . /app
WORKDIR /app
CMD ["python3", "app.py"]   <span class="com"># runs as root by default!</span>

<span class="com">─── HARDENED ─────────────────────────────────────────────────</span>
FROM python:3.<span class="num">12</span>-slim@sha256:abc123...   <span class="com"># pinned digest, minimal base</span>

<span class="com"># Create a non-root user</span>
RUN groupadd -r appuser &amp;&amp; useradd -r -g appuser appuser

<span class="com"># Install only what's needed; clean up apt cache</span>
RUN apt-get update &amp;&amp; \
    apt-get install -y --no-install-recommends curl &amp;&amp; \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY --chown=appuser:appuser requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY --chown=appuser:appuser . .

USER appuser                <span class="com"># drop root privileges</span>
EXPOSE <span class="num">8080</span>
HEALTHCHECK --interval=<span class="num">30</span>s CMD curl -f http://localhost:<span class="num">8080</span>/health || exit <span class="num">1</span>
CMD ["python3", "app.py"]
      </div>
    </div>

    <div class="concept-card">
      <div class="concept-label">Scanning</div>
      <div class="concept-title">Scanning Images for Vulnerabilities</div>
      <div class="concept-desc">
        Before deploying any image, scan it. Integrate scanning into your
        CI/CD pipeline so vulnerable images never reach production.
      </div>
      <div class="code-block">
<span class="com"># Trivy — fast, free, open-source vulnerability scanner</span>
trivy image myapp:<span class="num">1.2</span>.<span class="num">3</span>

<span class="com"># Fail the build if HIGH or CRITICAL vulnerabilities are found</span>
trivy image --severity HIGH,CRITICAL --exit-code <span class="num">1</span> myapp:<span class="num">1.2</span>.<span class="num">3</span>

<span class="com"># Scan a Dockerfile for misconfigurations (not just the built image)</span>
trivy config ./Dockerfile

<span class="com"># Scan for secrets accidentally baked into the image</span>
trivy image --scanners secret myapp:<span class="num">1.2</span>.<span class="num">3</span>

<span class="com"># Docker Scout (built into modern Docker Desktop)</span>
docker scout cves myapp:<span class="num">1.2</span>.<span class="num">3</span>

<span class="com"># GitHub Actions: scan on every push</span>
<span class="com"># - uses: aquasecurity/trivy-action@master</span>
<span class="com">#   with:</span>
<span class="com">#     image-ref: 'myapp:${{ github.sha }}'</span>
<span class="com">#     severity: 'CRITICAL,HIGH'</span>
<span class="com">#     exit-code: '1'</span>
      </div>
    </div>

    <div class="concept-card">
      <div class="concept-label">Runtime Hardening</div>
      <div class="concept-title">Running Containers Safely</div>
      <div class="concept-desc">
        Docker run flags matter as much as the image itself:
      </div>
      <div class="code-block">
<span class="com"># NEVER do this in production:</span>
docker run --privileged -v /:/host myimage   <span class="com"># full host access!</span>

<span class="com"># Hardened run command:</span>
docker run \
  --read-only \                          <span class="com"># filesystem is read-only</span>
  --tmpfs /tmp \                         <span class="com"># writable tmp, in-memory only</span>
  --cap-drop=ALL \                       <span class="com"># drop all Linux capabilities</span>
  --cap-add=NET_BIND_SERVICE \           <span class="com"># add back only what's needed</span>
  --security-opt=no-new-privileges \     <span class="com"># block privilege escalation</span>
  --memory=512m --cpus=1 \               <span class="com"># resource limits (DoS protection)</span>
  --user $(id -u):$(id -g) \             <span class="com"># run as host's non-root user</span>
  myimage:<span class="num">1.2</span>.<span class="num">3</span>

<span class="com"># Audit running containers for risky configurations</span>
docker inspect myapp_container | python3 -c \
  <span class="str">"import sys,json; c=json.load(sys.stdin)[0]; \
print('Privileged:', c['HostConfig']['Privileged']); \
print('User:', c['Config']['User'] or 'root (DANGER)')"</span>
      </div>
    </div>

  </div>
</div>
"""

# ══════════════════════════════════════════════════════════════════════════
# NET – Packet analysis with Wireshark/tcpdump
# ══════════════════════════════════════════════════════════════════════════
C_NET = """
<!-- BEGINNER34-NET v1 -->
<!-- ── TOPIC: Network Packet Analysis ────────────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-badge">Beginner</span>
    Packet Analysis – Reading the Network's Mind with Wireshark
  </div>
  <div class="topic-body">

    <div class="concept-card">
      <div class="concept-label">Core Concept</div>
      <div class="concept-title">Why Capture Packets?</div>
      <div class="concept-desc">
        Every problem on a network eventually shows up in the packets —
        slow apps, failed connections, intrusions, misconfigurations. A
        <strong>packet capture (pcap)</strong> is ground truth: it shows
        exactly what was sent and received, byte for byte.<br><br>
        <strong>Tools:</strong><br>
        &bull; <code>tcpdump</code> — command-line capture; runs anywhere,
          even on headless servers.<br>
        &bull; <strong>Wireshark</strong> — GUI analysis; the gold standard
          for deep inspection.<br>
        &bull; <code>tshark</code> — Wireshark's CLI sibling; great for
          scripting and automation.<br><br>
        <em>"Not my circus, not my monkey"</em> — capturing traffic on a
        network you don't own or have authorization for is illegal in most
        jurisdictions (wiretapping laws). Always get written authorization.
      </div>
    </div>

    <div class="concept-card">
      <div class="concept-label">Capture</div>
      <div class="concept-title">Capturing Traffic with tcpdump</div>
      <div class="concept-desc">
        <code>tcpdump</code> uses Berkeley Packet Filter (BPF) syntax to
        select exactly the traffic you care about — capturing everything
        creates huge files and noise.
      </div>
      <div class="code-block">
<span class="com"># Capture all traffic on eth0, write to a file (analyse later in Wireshark)</span>
sudo tcpdump -i eth0 -w capture.pcap

<span class="com"># Capture only HTTP traffic (port 80) with full packet content</span>
sudo tcpdump -i eth0 -s <span class="num">0</span> -w http.pcap port <span class="num">80</span>

<span class="com"># Capture traffic to/from a specific host</span>
sudo tcpdump -i eth0 host <span class="num">192.168.1</span>.<span class="num">50</span>

<span class="com"># Capture traffic between two hosts on a specific port</span>
sudo tcpdump -i eth0 'host 192.168.1.50 and host 192.168.1.10 and port 443'

<span class="com"># Show packets live, with readable ASCII (good for HTTP debugging)</span>
sudo tcpdump -i eth0 -A port <span class="num">80</span>

<span class="com"># Capture only SYN packets (new connection attempts — good for scan detection)</span>
sudo tcpdump -i eth0 'tcp[tcpflags] == tcp-syn'

<span class="com"># Rotate captures every 100MB, keep last 10 files (long-running capture)</span>
sudo tcpdump -i eth0 -w /data/cap.pcap -C <span class="num">100</span> -W <span class="num">10</span>
      </div>
    </div>

    <div class="concept-card">
      <div class="concept-label">Analysis</div>
      <div class="concept-title">Reading a Capture in Wireshark</div>
      <div class="concept-desc">
        Wireshark's <strong>display filter</strong> bar (top of the window)
        is the most powerful tool — it narrows thousands of packets down
        to the handful you care about.
      </div>
      <div class="code-block">
<span class="com">─── Useful Wireshark display filters ─────────────────────────</span>
ip.addr == <span class="num">192.168.1</span>.<span class="num">50</span>             <span class="com"># traffic to/from this host</span>
tcp.port == <span class="num">443</span>                     <span class="com"># HTTPS traffic</span>
http.request.method == <span class="str">"POST"</span>       <span class="com"># only POST requests</span>
http contains <span class="str">"password"</span>             <span class="com"># find plaintext passwords (HTTP only!)</span>
tcp.flags.syn == <span class="num">1</span> &amp;&amp; tcp.flags.ack == <span class="num">0</span>  <span class="com"># new connections (SYN scan)</span>
tcp.analysis.retransmission       <span class="com"># packets that had to be resent (perf issue)</span>
dns.qry.name contains <span class="str">"evil"</span>          <span class="com"># suspicious DNS lookups</span>
tls.handshake.extensions_server_name == <span class="str">"example.com"</span>  <span class="com"># TLS SNI filter</span>

<span class="com">─── Right-click any packet → Follow → TCP Stream ─────────────</span>
<span class="com"># Reconstructs the entire conversation as readable text —</span>
<span class="com"># the single most useful feature for understanding "what happened"</span>

<span class="com">─── Statistics menu ───────────────────────────────────────────</span>
<span class="com"># Conversations: who talked to whom, how much data</span>
<span class="com"># Protocol Hierarchy: breakdown of traffic by protocol</span>
<span class="com"># IO Graph: visualise traffic volume over time (spot spikes)</span>
      </div>
    </div>

    <div class="concept-card">
      <div class="concept-label">tshark</div>
      <div class="concept-title">Scripting Analysis with tshark</div>
      <div class="concept-desc">
        For repeatable analysis or processing huge captures, script it
        with <code>tshark</code> instead of clicking through the GUI.
      </div>
      <div class="code-block">
<span class="com"># Extract all unique source/destination IP pairs</span>
tshark -r capture.pcap -T fields -e ip.src -e ip.dst | sort -u

<span class="com"># Count HTTP requests by destination host</span>
tshark -r capture.pcap -Y "http.request" -T fields -e http.host | \
    sort | uniq -c | sort -rn

<span class="com"># Extract all DNS queries (great for spotting C2 domains)</span>
tshark -r capture.pcap -Y "dns.flags.response == 0" \
    -T fields -e frame.time -e ip.src -e dns.qry.name

<span class="com"># Find the top talkers by byte volume</span>
tshark -r capture.pcap -q -z conv,ip | head -<span class="num">20</span>

<span class="com"># Extract files transferred over HTTP (incident response)</span>
tshark -r capture.pcap --export-objects http,/tmp/extracted_files/
      </div>
    </div>

  </div>
</div>
"""

# ══════════════════════════════════════════════════════════════════════════
# GRC – Vendor / third-party risk management
# ══════════════════════════════════════════════════════════════════════════
C_GRC = """
<!-- BEGINNER34-GRC v1 -->
<!-- ── TOPIC: Vendor & Third-Party Risk Management ───────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-badge">Beginner</span>
    Vendor Risk Management – Securing the Supply Chain
  </div>
  <div class="topic-body">

    <div class="concept-card">
      <div class="concept-label">Core Concept</div>
      <div class="concept-title">Why Vendor Risk Matters</div>
      <div class="concept-desc">
        Modern organisations depend on dozens — sometimes hundreds — of
        third-party vendors: cloud providers, SaaS tools, payment
        processors, contractors, MSPs. Every one of them is a potential
        path into your data.<br><br>
        <strong>Famous supply-chain incidents:</strong><br>
        &bull; <em>SolarWinds (2020)</em> — attackers compromised a
          software update mechanism, infecting 18,000+ organisations
          including US government agencies.<br>
        &bull; <em>Target (2013)</em> — attackers entered through an
          HVAC contractor's stolen credentials, then pivoted to
          point-of-sale systems.<br>
        &bull; <em>Kaseya (2021)</em> — ransomware spread through an MSP's
          remote management software to 1,500+ downstream businesses.<br><br>
        <em>"Not my circus, not my monkey"</em> doesn't apply here — your
        vendor's breach becomes <em>your</em> incident the moment your
        data is involved. Their circus is your circus too.
      </div>
    </div>

    <div class="concept-card">
      <div class="concept-label">Process</div>
      <div class="concept-title">The Vendor Risk Assessment Lifecycle</div>
      <div class="concept-desc">
        A mature vendor risk program follows a repeatable lifecycle:
      </div>
      <div class="code-block">
<span class="com">1. TIERING — classify vendors by risk level</span>
   Tier 1 (Critical): Has access to sensitive data or core systems
                      → Full security questionnaire + SOC 2 review + annual audit
   Tier 2 (Moderate): Limited data access, important to operations
                      → Security questionnaire + annual review
   Tier 3 (Low):      No data access (e.g. office supplies vendor)
                      → Basic due diligence only

<span class="com">2. DUE DILIGENCE — before signing a contract</span>
   - Request SOC 2 Type II report (or ISO 27001 certificate)
   - Send a security questionnaire (SIG, CAIQ, or custom)
   - Review their incident history (breach disclosures, news)
   - Check their sub-processors (do THEY outsource to other vendors?)

<span class="com">3. CONTRACTING — bake security into the agreement</span>
   - Data Processing Agreement (DPA) — required for personal data (GDPR)
   - Right-to-audit clause
   - Breach notification requirements (e.g. "within 72 hours")
   - Data deletion / return clause at contract end
   - Liability and indemnification terms

<span class="com">4. ONGOING MONITORING — security doesn't stop at signing</span>
   - Annual reassessment for Tier 1/2 vendors
   - Monitor for breach news (set up alerts for vendor names)
   - Track SOC 2 report renewal dates
   - Review access logs — is the vendor only touching what they should?

<span class="com">5. OFFBOARDING — when the relationship ends</span>
   - Revoke all access (accounts, API keys, VPN)
   - Confirm data deletion in writing
   - Document the offboarding for audit evidence
      </div>
    </div>

    <div class="concept-card">
      <div class="concept-label">Questionnaires</div>
      <div class="concept-title">Reading a Security Questionnaire Response</div>
      <div class="concept-desc">
        <em>"Assume" makes an ass out of you and me</em> — don't assume a
        vendor's marketing claims ("bank-level security!", "military-grade
        encryption!") mean anything. Demand specifics:<br><br>
        &bull; "Do you encrypt data at rest?" → Ask: <em>which algorithm,
          key length, and who manages the keys?</em><br>
        &bull; "Do you have an incident response plan?" → Ask:
          <em>when was it last tested, and what's the notification SLA?</em><br>
        &bull; "Are you SOC 2 compliant?" → Ask: <em>can we see the
          actual report (Type II, not Type I)?</em><br>
        &bull; "Do you use sub-processors?" → Ask: <em>list them, and
          confirm they're held to the same standards.</em><br><br>
        Standard frameworks for questionnaires: <strong>SIG</strong>
        (Standardized Information Gathering) and <strong>CAIQ</strong>
        (Consensus Assessments Initiative Questionnaire from the Cloud
        Security Alliance) — both save time by giving vendors a
        consistent format to answer once and reuse.
      </div>
    </div>

    <div class="concept-card">
      <div class="concept-label">Incident Scenario</div>
      <div class="concept-title">When a Vendor Gets Breached</div>
      <div class="concept-desc">
        <em>You can't make someone make the right choice, yet you can pick
        up the pieces afterwards</em> — your vendor's security failure is
        not your fault, but your response is your responsibility.<br><br>
        When you learn a vendor has been breached:<br>
        1. <strong>Activate your incident response plan</strong> — treat it
           like an internal incident.<br>
        2. <strong>Determine exposure</strong> — what data did they have?
           What systems did they connect to?<br>
        3. <strong>Rotate credentials</strong> — every API key, password,
           or certificate shared with that vendor.<br>
        4. <strong>Review logs</strong> — look for unusual activity from
           the vendor's IPs/accounts in the breach window.<br>
        5. <strong>Notify</strong> — your legal/compliance team may need
           to notify regulators or affected customers.<br>
        6. <strong>Reassess the relationship</strong> — does this vendor
           remain acceptable? Document the decision either way.
      </div>
    </div>

  </div>
</div>
"""

# ══════════════════════════════════════════════════════════════════════════
# LINUX – LVM and storage management
# ══════════════════════════════════════════════════════════════════════════
C_LINUX = """
<!-- BEGINNER34-LINUX v1 -->
<!-- ── TOPIC: LVM & Storage Management ───────────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-badge">Beginner</span>
    LVM &amp; Storage – Flexible Disk Management on Linux
  </div>
  <div class="topic-body">

    <div class="concept-card">
      <div class="concept-label">Core Concept</div>
      <div class="concept-title">Why LVM? The Problem with Fixed Partitions</div>
      <div class="concept-desc">
        Traditional partitions are fixed-size — if <code>/var</code> fills
        up, resizing it usually means backing up data, repartitioning, and
        restoring. <strong>LVM (Logical Volume Manager)</strong> adds a
        flexible layer between physical disks and filesystems.<br><br>
        <strong>The LVM stack (bottom to top):</strong><br>
        1. <em>Physical Volume (PV)</em> — a disk or partition
           (e.g. <code>/dev/sdb1</code>).<br>
        2. <em>Volume Group (VG)</em> — a pool combining one or more PVs.<br>
        3. <em>Logical Volume (LV)</em> — a "virtual partition" carved
           from the VG; this is what you format and mount.<br><br>
        Benefits: resize volumes live, add disks to a VG without downtime,
        take instant snapshots, and move data between physical disks
        transparently.
      </div>
    </div>

    <div class="concept-card">
      <div class="concept-label">Building Blocks</div>
      <div class="concept-title">Creating an LVM Setup From Scratch</div>
      <div class="concept-desc">
        This walks through turning a raw disk into a mounted, growable
        filesystem.
      </div>
      <div class="code-block">
<span class="com"># 1. Create a physical volume on a new disk</span>
sudo pvcreate /dev/sdb

<span class="com"># 2. Create a volume group from one or more PVs</span>
sudo vgcreate data_vg /dev/sdb

<span class="com"># 3. Create a logical volume (50 GB) inside the VG</span>
sudo lvcreate -L 50G -n app_data data_vg

<span class="com"># 4. Format it with a filesystem</span>
sudo mkfs.ext4 /dev/data_vg/app_data

<span class="com"># 5. Mount it</span>
sudo mkdir -p /data
sudo mount /dev/data_vg/app_data /data

<span class="com"># 6. Make it persistent — add to /etc/fstab</span>
echo '/dev/data_vg/app_data  /data  ext4  defaults  0 2' | sudo tee -a /etc/fstab

<span class="com"># Inspect the stack at any layer</span>
sudo pvdisplay     <span class="com"># physical volumes</span>
sudo vgdisplay     <span class="com"># volume groups</span>
sudo lvdisplay     <span class="com"># logical volumes</span>
lsblk              <span class="com"># visual block-device tree</span>
      </div>
    </div>

    <div class="concept-card">
      <div class="concept-label">Resizing</div>
      <div class="concept-title">Growing a Volume Without Downtime</div>
      <div class="concept-desc">
        This is LVM's superpower — extending storage on a live system,
        no reboot required. <em>Always shrink with extreme care</em>
        (and a backup) — growing is safe, shrinking can destroy data.
      </div>
      <div class="code-block">
<span class="com"># Scenario: /data is filling up. Add a new disk and grow it live.</span>

<span class="com"># 1. Add the new disk to the volume group</span>
sudo pvcreate /dev/sdc
sudo vgextend data_vg /dev/sdc

<span class="com"># 2. Grow the logical volume by 20 GB</span>
sudo lvextend -L +20G /dev/data_vg/app_data

<span class="com"># 3. Resize the filesystem to use the new space (ext4 — does this LIVE)</span>
sudo resize2fs /dev/data_vg/app_data

<span class="com"># For XFS filesystems, use xfs_growfs instead (also live):</span>
sudo xfs_growfs /data

<span class="com"># Verify the new size</span>
df -h /data

<span class="com">─── SHRINKING (dangerous — backup first!) ───────────────────</span>
<span class="com"># ext4 must be unmounted to shrink; XFS cannot be shrunk at all</span>
sudo umount /data
sudo e2fsck -f /dev/data_vg/app_data
sudo resize2fs /dev/data_vg/app_data 30G
sudo lvreduce -L 30G /dev/data_vg/app_data
      </div>
    </div>

    <div class="concept-card">
      <div class="concept-label">Snapshots</div>
      <div class="concept-title">LVM Snapshots – Instant Point-in-Time Backups</div>
      <div class="concept-desc">
        A <strong>snapshot</strong> freezes the state of a volume at an
        instant, so you can back it up consistently while the original
        keeps changing — essential for backing up live databases.<br><br>
        <em>You can't make someone make the right choice, yet you can pick
        up the pieces afterwards</em> — when someone runs a bad migration
        against production, an LVM snapshot from five minutes earlier can
        save the day.
      </div>
      <div class="code-block">
<span class="com"># Create a snapshot before a risky change (10GB reserved for changes)</span>
sudo lvcreate -L 10G -s -n app_data_snap /dev/data_vg/app_data

<span class="com"># Mount the snapshot read-only to inspect/back it up</span>
sudo mkdir /mnt/snapshot
sudo mount -o ro /dev/data_vg/app_data_snap /mnt/snapshot
<span class="com"># ... run backup tools against /mnt/snapshot ...</span>
sudo umount /mnt/snapshot

<span class="com"># Roll back to the snapshot if the change went wrong</span>
sudo umount /data
sudo lvconvert --merge /dev/data_vg/app_data_snap
<span class="com"># Volume reverts to the snapshot's state on next activation</span>

<span class="com"># Remove a snapshot once you no longer need it (frees space)</span>
sudo lvremove /dev/data_vg/app_data_snap

<span class="com"># Note: snapshots are NOT a substitute for off-site backups —</span>
<span class="com"># they live on the same physical disks as the original data!</span>
      </div>
    </div>

  </div>
</div>
"""

# ══════════════════════════════════════════════════════════════════════════
# LIFESTYLE – Soft skills for IT professionals
# ══════════════════════════════════════════════════════════════════════════
C_LIFESTYLE = """
<!-- BEGINNER34-LIFESTYLE v1 -->
<!-- ── TOPIC: Soft Skills for IT Professionals ───────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-badge">Beginner</span>
    Soft Skills – The Difference Between a Good and Great IT Pro
  </div>
  <div class="topic-body">

    <div class="concept-card">
      <div class="concept-label">Core Concept</div>
      <div class="concept-title">Why Soft Skills Matter More Than You Think</div>
      <div class="concept-desc">
        Technical skill gets you hired. <strong>Soft skills get you
        promoted, trusted, and recommended.</strong> Most IT failures
        aren't technical — they're communication failures: unclear
        tickets, blame-shifting, talking over people's heads, or simply
        not listening.<br><br>
        The best engineers aren't always the smartest — they're the ones
        people <em>want</em> to work with. That reputation compounds over
        a career far more than any certification.
      </div>
    </div>

    <div class="concept-card">
      <div class="concept-label">Communication</div>
      <div class="concept-title">Translating Tech for Non-Technical People</div>
      <div class="concept-desc">
        A huge part of IT work is explaining technical issues to people
        who don't share your vocabulary — managers, customers, other
        departments. Three techniques:<br><br>
        1. <strong>Lead with impact, not mechanism.</strong> Instead of
           "the database connection pool exhausted its max_connections
           limit," say "the system is slow because too many people are
           using it at once — we're adding capacity now."<br>
        2. <strong>Use analogies.</strong> "Think of a firewall like a
           bouncer at a club door — it checks IDs (rules) before letting
           anyone in."<br>
        3. <strong>Answer the question they're really asking</strong>:
           usually "is this bad?", "how long until it's fixed?", and
           "do I need to do anything?"<br><br>
        <em>"Assume" makes an ass out of you and me</em> — don't assume
        the person you're explaining to already knows the basics. Asking
        "would it help if I explained how DNS works first?" is a sign of
        respect, not condescension — when offered with the right tone.
      </div>
    </div>

    <div class="concept-card">
      <div class="concept-label">Teamwork</div>
      <div class="concept-title">Working Well on a Team Under Pressure</div>
      <div class="concept-desc">
        Incidents and deadlines bring out the worst in some people —
        finger-pointing, panic, talking over each other. Stand out by
        doing the opposite:<br><br>
        &bull; <strong>State facts, not blame.</strong> "The deploy at 2 PM
          correlates with the spike" lands very differently from
          "Bob's deploy broke everything."<br>
        &bull; <strong>Ask clarifying questions before jumping to
          solutions.</strong> "What changed right before this started?"<br>
        &bull; <strong>Volunteer for the unglamorous work</strong> — writing
          the postmortem, updating the runbook, taking notes during the
          incident call. People remember who showed up.<br>
        &bull; <strong>Give credit publicly, give feedback privately.</strong><br><br>
        <em>"Not my circus, not my monkey"</em> applies to drama, not to
        people. Stay out of office politics — but always be willing to
        help a colleague who's struggling with a technical problem.
      </div>
    </div>

    <div class="concept-card">
      <div class="concept-label">Self-Management</div>
      <div class="concept-title">Owning Your Mistakes — and Your Growth</div>
      <div class="concept-desc">
        Everyone breaks production eventually. What defines your career is
        what happens next.<br><br>
        <strong>When you make a mistake:</strong><br>
        1. Say so immediately — hiding it always makes it worse.<br>
        2. Focus on fixing it before discussing how it happened.<br>
        3. After it's resolved, write down what you learned.<br>
        4. Build a safeguard so it can't happen the same way again.<br><br>
        <em>You can't make someone make the right choice, yet you can pick
        up the pieces afterwards</em> — this applies to yourself too. You
        will misjudge things. The professionals who last decades aren't
        the ones who never err — they're the ones who recover gracefully,
        learn fast, and don't repeat the same mistake twice.<br><br>
        <strong>Career compounding tip:</strong> keep a personal log of
        problems you've solved. In a year, it becomes your interview
        stories, your mentoring material, and proof of how far you've come.
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
    (A_SEC,       S_SEC,       C_SEC),
    (A_NET,       S_NET,       C_NET),
    (A_GRC,       S_GRC,       C_GRC),
    (A_LINUX,     S_LINUX,     C_LINUX),
    (A_LIFESTYLE, S_LIFESTYLE, C_LIFESTYLE),
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
