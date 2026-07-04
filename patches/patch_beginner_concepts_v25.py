#!/usr/bin/env python3
"""
patch_beginner_concepts_v25.py — Wave 25: Big O & algorithms, cryptography
fundamentals & PKI, container security, 802.1X/NAC, breaking into IT.

New sentinels:
  BEGINNER25-SCRIPT v1  — Big O notation, data structures, common algorithms, recursion
  BEGINNER25-SEC v1     — Cryptography fundamentals, key exchange, PKI deep dive
  BEGINNER25-OPS v1     — Container security, image scanning, runtime hardening
  BEGINNER25-NET v1     — 802.1X, NAC, enterprise wireless security
  BEGINNER25-LIFE v1    — Breaking into IT, career transitions, the first 90 days
"""
from pathlib import Path

SCRIPT_INJECT_ANCHOR = "<!-- /domain-body script -->"
SEC_INJECT_ANCHOR    = "<!-- /domain-body sec -->"
OPS_INJECT_ANCHOR    = "<!-- /domain-body ops -->"
NET_INJECT_ANCHOR    = "<!-- /domain-body net -->"
LIFE_INJECT_ANCHOR   = "<!-- /domain-body lifestyle -->"

# ─────────────────────────────── SCRIPT wave 25 ──────────────────────────────
SCRIPT_SENTINEL = "<!-- BEGINNER25-SCRIPT v1 -->"
SCRIPT_CONTENT = """
<!-- BEGINNER25-SCRIPT v1 -->
<!-- ── TOPIC: BIG O & ALGORITHMS ─────────────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">📈</span>
    <span class="topic-name">Big O &amp; Algorithms — Will Your Code Survive Real Data?</span>
    <span class="topic-badge">SCRIPT • CS Foundation</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">WHAT BIG O MEASURES</div>
      <div class="concept-title">How Cost Grows as Input Grows</div>
      <div class="concept-desc">Big O notation describes how an algorithm's time (or memory) scales as the input size (n) grows. It ignores constants and small terms to focus on the <em>growth rate</em>. Why care? Code that works fine on 100 items can hang forever on 10 million. Understanding Big O helps you spot the difference between "fast enough" and "will melt in production."</div>
      <table class="ai-table">
        <thead><tr><th>Big O</th><th>Name</th><th>n=10</th><th>n=1,000,000</th><th>Example</th></tr></thead>
        <tbody>
          <tr><td>O(1)</td><td>Constant</td><td>1</td><td>1</td><td>Dict/hash lookup, array index</td></tr>
          <tr><td>O(log n)</td><td>Logarithmic</td><td>~3</td><td>~20</td><td>Binary search</td></tr>
          <tr><td>O(n)</td><td>Linear</td><td>10</td><td>1,000,000</td><td>Loop through a list once</td></tr>
          <tr><td>O(n log n)</td><td>Linearithmic</td><td>~33</td><td>~20M</td><td>Good sorting (merge/quick)</td></tr>
          <tr><td>O(n²)</td><td>Quadratic</td><td>100</td><td>10¹²</td><td>Nested loops (the danger zone)</td></tr>
          <tr><td>O(2ⁿ)</td><td>Exponential</td><td>1,024</td><td>astronomical</td><td>Brute-force, naive recursion</td></tr>
        </tbody>
      </table>
    </div>
    <div class="concept-card">
      <div class="concept-label">THE CLASSIC MISTAKE</div>
      <div class="concept-title">Hidden O(n²) — and the Fix</div>
      <div class="code-block"><span class="com"># SLOW — O(n²): checking membership in a list inside a loop</span>
<span class="kw">def</span> <span class="fn">find_dupes_slow</span>(items):
    dupes = []
    <span class="kw">for</span> x <span class="kw">in</span> items:
        <span class="kw">if</span> items.count(x) &gt; <span class="num">1</span>:    <span class="com"># .count scans the WHOLE list each time</span>
            dupes.append(x)
    <span class="kw">return</span> dupes
<span class="com"># 1M items → ~1 trillion operations → hangs forever</span>

<span class="com"># FAST — O(n): use a set/dict for O(1) lookups</span>
<span class="kw">def</span> <span class="fn">find_dupes_fast</span>(items):
    seen, dupes = <span class="fn">set</span>(), <span class="fn">set</span>()
    <span class="kw">for</span> x <span class="kw">in</span> items:
        <span class="kw">if</span> x <span class="kw">in</span> seen:       <span class="com"># set lookup is O(1)</span>
            dupes.add(x)
        seen.add(x)
    <span class="kw">return</span> dupes
<span class="com"># 1M items → ~1M operations → instant</span></div>
      <div class="concept-desc"><strong>The #1 practical lesson:</strong> when you need fast lookups, use a <code>set</code> or <code>dict</code> (hash-based, O(1)) instead of repeatedly scanning a <code>list</code> (O(n)). This single insight fixes a huge fraction of slow code.</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">DATA STRUCTURE COSTS</div>
      <div class="concept-title">Pick the Right Tool</div>
      <table class="ai-table">
        <thead><tr><th>Structure</th><th>Lookup</th><th>Insert</th><th>Best For</th></tr></thead>
        <tbody>
          <tr><td>list (array)</td><td>O(n) search / O(1) index</td><td>O(1) append</td><td>Ordered sequence, iteration</td></tr>
          <tr><td>dict (hash map)</td><td>O(1)</td><td>O(1)</td><td>Key → value lookups</td></tr>
          <tr><td>set (hash)</td><td>O(1)</td><td>O(1)</td><td>Membership tests, dedup</td></tr>
          <tr><td>deque</td><td>O(n)</td><td>O(1) both ends</td><td>Queues, sliding windows</td></tr>
          <tr><td>heap (priority queue)</td><td>O(1) min</td><td>O(log n)</td><td>"Top N", schedulers</td></tr>
        </tbody>
      </table>
    </div>
    <div class="concept-card">
      <div class="concept-label">RECURSION</div>
      <div class="concept-title">A Function That Calls Itself</div>
      <div class="concept-desc">Recursion solves a problem by breaking it into smaller versions of itself. Every recursion needs a <strong>base case</strong> (when to stop) — forget it and you get infinite recursion (stack overflow). Great for tree/nested structures; for simple counting, a loop is usually clearer and faster.</div>
      <div class="code-block"><span class="com"># Walk a nested folder structure (natural fit for recursion)</span>
<span class="kw">def</span> <span class="fn">total_size</span>(path):
    <span class="kw">if</span> path.is_file():              <span class="com"># BASE CASE</span>
        <span class="kw">return</span> path.stat().st_size
    <span class="kw">return</span> <span class="fn">sum</span>(total_size(child)    <span class="com"># RECURSE into each child</span>
               <span class="kw">for</span> child <span class="kw">in</span> path.iterdir())

<span class="com"># Binary search — O(log n), a recursive classic</span>
<span class="kw">def</span> <span class="fn">bsearch</span>(arr, target, lo=<span class="num">0</span>, hi=<span class="kw">None</span>):
    <span class="kw">if</span> hi <span class="kw">is</span> <span class="kw">None</span>: hi = <span class="fn">len</span>(arr) - <span class="num">1</span>
    <span class="kw">if</span> lo &gt; hi: <span class="kw">return</span> -<span class="num">1</span>          <span class="com"># BASE CASE: not found</span>
    mid = (lo + hi) // <span class="num">2</span>
    <span class="kw">if</span> arr[mid] == target: <span class="kw">return</span> mid
    <span class="kw">if</span> arr[mid] &lt; target:
        <span class="kw">return</span> bsearch(arr, target, mid+<span class="num">1</span>, hi)
    <span class="kw">return</span> bsearch(arr, target, lo, mid-<span class="num">1</span>)</div>
    </div>
  </div>
</div>
"""

# ─────────────────────────────── SEC wave 25 ─────────────────────────────────
SEC_SENTINEL = "<!-- BEGINNER25-SEC v1 -->"
SEC_CONTENT = """
<!-- BEGINNER25-SEC v1 -->
<!-- ── TOPIC: CRYPTOGRAPHY FUNDAMENTALS ──────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">🔐</span>
    <span class="topic-name">Cryptography Fundamentals — The Building Blocks of Security</span>
    <span class="topic-badge">SEC • Foundation</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">THE THREE GOALS</div>
      <div class="concept-title">What Crypto Actually Provides</div>
      <table class="ai-table">
        <thead><tr><th>Goal</th><th>Means</th><th>Provided By</th></tr></thead>
        <tbody>
          <tr><td>Confidentiality</td><td>Only authorized parties can read it</td><td>Encryption</td></tr>
          <tr><td>Integrity</td><td>Detect if data was altered</td><td>Hashing / MAC</td></tr>
          <tr><td>Authenticity / Non-repudiation</td><td>Prove who sent it; they can't deny it</td><td>Digital signatures</td></tr>
        </tbody>
      </table>
      <div class="concept-desc">Together with availability, confidentiality and integrity form the <strong>CIA triad</strong> — the foundation of all of information security.</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">SYMMETRIC VS ASYMMETRIC</div>
      <div class="concept-title">One Key or Two?</div>
      <table class="ai-table">
        <thead><tr><th>Aspect</th><th>Symmetric</th><th>Asymmetric (public-key)</th></tr></thead>
        <tbody>
          <tr><td>Keys</td><td>One shared secret key</td><td>Key pair: public + private</td></tr>
          <tr><td>Speed</td><td>Fast (bulk data)</td><td>Slow (small data only)</td></tr>
          <tr><td>Problem it has</td><td>How to share the key securely?</td><td>Slow; needs trust in public keys</td></tr>
          <tr><td>Algorithms</td><td>AES, ChaCha20</td><td>RSA, ECC, Diffie-Hellman</td></tr>
          <tr><td>Used for</td><td>Encrypting actual data</td><td>Key exchange, signatures</td></tr>
        </tbody>
      </table>
      <div class="concept-desc"><strong>The clever combination:</strong> real systems (like HTTPS) use asymmetric crypto to securely <em>exchange a symmetric key</em>, then use fast symmetric crypto for the actual data. Best of both worlds.</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">KEY EXCHANGE</div>
      <div class="concept-title">Diffie-Hellman — Sharing a Secret in Public</div>
      <div class="concept-desc">How do two parties agree on a secret key over a network an eavesdropper is watching? Diffie-Hellman key exchange lets them derive a shared secret without ever transmitting it — using math (modular exponentiation / elliptic curves) that's easy to compute forward but practically impossible to reverse. The eavesdropper sees the public exchanges but cannot compute the shared secret. This is the magic that makes HTTPS possible.</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">PKI</div>
      <div class="concept-title">Public Key Infrastructure — Who Do You Trust?</div>
      <div class="concept-desc">Public-key crypto has a chicken-and-egg problem: how do you know a public key really belongs to who it claims? PKI solves this with <strong>certificates</strong> — a public key plus identity, vouched for (signed) by a trusted <strong>Certificate Authority (CA)</strong>. Your browser/OS trusts a set of root CAs, forming a "chain of trust."</div>
      <table class="ai-table">
        <thead><tr><th>Component</th><th>Role</th></tr></thead>
        <tbody>
          <tr><td>Certificate (X.509)</td><td>Binds a public key to an identity (domain, org)</td></tr>
          <tr><td>Certificate Authority (CA)</td><td>Trusted issuer that signs certificates</td></tr>
          <tr><td>Root CA</td><td>Top of the trust chain; pre-installed in OS/browser</td></tr>
          <tr><td>Intermediate CA</td><td>Signed by root; issues end certs (protects the root)</td></tr>
          <tr><td>CSR</td><td>Certificate Signing Request — you ask a CA to sign your key</td></tr>
          <tr><td>CRL / OCSP</td><td>Ways to check if a cert was revoked</td></tr>
        </tbody>
      </table>
    </div>
    <div class="concept-card">
      <div class="concept-label">DON'T ROLL YOUR OWN</div>
      <div class="concept-title">The Cardinal Rule of Crypto</div>
      <div class="concept-desc">Never invent your own cryptographic algorithm or implementation. Decades of expert scrutiny go into vetted libraries; homemade crypto is almost always broken in subtle ways. Use established, audited libraries (libsodium, the OS's TLS stack, Python's <code>cryptography</code>), use them in their default/recommended modes, and keep them updated. Your job is to use crypto correctly, not to build it.</div>
    </div>
  </div>
</div>
"""

# ─────────────────────────────── OPS wave 25 ─────────────────────────────────
OPS_SENTINEL = "<!-- BEGINNER25-OPS v1 -->"
OPS_CONTENT = """
<!-- BEGINNER25-OPS v1 -->
<!-- ── TOPIC: CONTAINER SECURITY ─────────────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">🐳</span>
    <span class="topic-name">Container Security — Hardening Docker &amp; Images</span>
    <span class="topic-badge">OPS • Security</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">CONTAINERS AREN'T VMs</div>
      <div class="concept-title">Shared Kernel = Shared Risk</div>
      <div class="concept-desc">Containers share the host's kernel (unlike VMs, which each have their own). That makes them lightweight and fast — but it also means a container escape can potentially compromise the host and every other container. Container security is about reducing what a compromised container can reach and do.</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">IMAGE SECURITY</div>
      <div class="concept-title">Start From a Clean, Minimal Base</div>
      <table class="ai-table">
        <thead><tr><th>Practice</th><th>Why</th></tr></thead>
        <tbody>
          <tr><td>Use minimal base images</td><td>Alpine/distroless = smaller attack surface, fewer CVEs</td></tr>
          <tr><td>Pin image versions (digests)</td><td><code>python:3.12</code> not <code>python:latest</code> — reproducible, no surprise updates</td></tr>
          <tr><td>Scan images for vulnerabilities</td><td>Trivy, Grype, Clair find known CVEs in layers</td></tr>
          <tr><td>Don't bake in secrets</td><td>Secrets in image layers persist even if "deleted" later</td></tr>
          <tr><td>Use trusted sources</td><td>Official images; verify signatures (cosign/Sigstore)</td></tr>
          <tr><td>Multi-stage builds</td><td>Don't ship build tools/source in the final image</td></tr>
        </tbody>
      </table>
      <div class="code-block"><span class="com"># Scan an image for known vulnerabilities</span>
trivy image python:3.12
grype nginx:latest

<span class="com"># Multi-stage build — final image has only what it needs</span>
<span class="com"># FROM golang:1.22 AS build</span>
<span class="com"># ... compile ...</span>
<span class="com"># FROM gcr.io/distroless/static   # tiny, no shell, no package mgr</span>
<span class="com"># COPY --from=build /app /app</span></div>
    </div>
    <div class="concept-card">
      <div class="concept-label">RUNTIME HARDENING</div>
      <div class="concept-title">Limit What a Container Can Do</div>
      <table class="ai-table">
        <thead><tr><th>Control</th><th>How</th></tr></thead>
        <tbody>
          <tr><td>Don't run as root</td><td><code>USER appuser</code> in Dockerfile; <code>--user 1000</code></td></tr>
          <tr><td>Read-only filesystem</td><td><code>--read-only</code> — malware can't write</td></tr>
          <tr><td>Drop capabilities</td><td><code>--cap-drop ALL</code> then add only what's needed</td></tr>
          <tr><td>No new privileges</td><td><code>--security-opt no-new-privileges</code></td></tr>
          <tr><td>Limit resources</td><td><code>--memory --cpus</code> — contain DoS / runaway</td></tr>
          <tr><td>Don't mount the Docker socket</td><td><code>/var/run/docker.sock</code> inside = root on host</td></tr>
          <tr><td>Network segmentation</td><td>Custom networks; don't expose ports you don't need</td></tr>
        </tbody>
      </table>
    </div>
    <div class="concept-card">
      <div class="concept-label">THE 4 Cs</div>
      <div class="concept-title">Cloud Native Security Layers</div>
      <div class="concept-desc">Container security is layered — each layer depends on the one outside it. Weakness in an outer layer undermines all the inner ones.</div>
      <table class="ai-table">
        <thead><tr><th>Layer</th><th>Secure By</th></tr></thead>
        <tbody>
          <tr><td><strong>C</strong>loud / infrastructure</td><td>Hardened hosts, IAM, network policy</td></tr>
          <tr><td><strong>C</strong>luster</td><td>RBAC, network policies, admission control</td></tr>
          <tr><td><strong>C</strong>ontainer</td><td>Minimal images, scanning, no root</td></tr>
          <tr><td><strong>C</strong>ode</td><td>Secure coding, dependency hygiene, secrets management</td></tr>
        </tbody>
      </table>
    </div>
  </div>
</div>
"""

# ─────────────────────────────── NET wave 25 ─────────────────────────────────
NET_SENTINEL = "<!-- BEGINNER25-NET v1 -->"
NET_CONTENT = """
<!-- BEGINNER25-NET v1 -->
<!-- ── TOPIC: 802.1X & NETWORK ACCESS CONTROL ────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">🚪</span>
    <span class="topic-name">802.1X &amp; NAC — Who Gets On the Network?</span>
    <span class="topic-badge">NET • Enterprise</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">THE PROBLEM</div>
      <div class="concept-title">An Open Network Port Is an Open Door</div>
      <div class="concept-desc">In a basic network, anyone who plugs into a wall jack or knows the Wi-Fi password is on the network. In an enterprise, that's a serious risk — an attacker in the lobby, a rogue device, a compromised laptop. 802.1X and NAC enforce <em>authentication before access</em>: prove who/what you are before the network lets you communicate.</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">802.1X</div>
      <div class="concept-title">Port-Based Authentication</div>
      <div class="concept-desc">802.1X authenticates a device <em>at the port level</em> before granting network access. It involves three roles working together via the EAP protocol.</div>
      <table class="ai-table">
        <thead><tr><th>Role</th><th>Who</th><th>Job</th></tr></thead>
        <tbody>
          <tr><td>Supplicant</td><td>The device wanting access (laptop)</td><td>Provides credentials/certificate</td></tr>
          <tr><td>Authenticator</td><td>The switch or wireless AP</td><td>Gatekeeper — blocks traffic until authorized</td></tr>
          <tr><td>Authentication Server</td><td>RADIUS server</td><td>Verifies credentials, says yes/no</td></tr>
        </tbody>
      </table>
      <div class="concept-desc">Until authentication succeeds, the port only passes authentication traffic — everything else is blocked. Enterprise Wi-Fi (WPA2/3-Enterprise) uses exactly this model, which is why you log in with your <em>own</em> username/password instead of a shared Wi-Fi key.</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">NAC</div>
      <div class="concept-title">Network Access Control — Beyond Just Identity</div>
      <div class="concept-desc">NAC extends the idea: it doesn't just check <em>who</em> you are, but whether your device is <em>healthy and compliant</em> before allowing full access — and what it's allowed to reach.</div>
      <table class="ai-table">
        <thead><tr><th>NAC Capability</th><th>Example</th></tr></thead>
        <tbody>
          <tr><td>Posture assessment</td><td>Is AV running? OS patched? Disk encrypted?</td></tr>
          <tr><td>Quarantine / remediation</td><td>Non-compliant device → restricted VLAN to fix itself</td></tr>
          <tr><td>Role-based access</td><td>Guest → internet only; employee → full; IoT → isolated</td></tr>
          <tr><td>Dynamic VLAN assignment</td><td>Put devices on the right segment automatically</td></tr>
          <tr><td>Guest onboarding</td><td>Captive portal, sponsored access</td></tr>
        </tbody>
      </table>
    </div>
    <div class="concept-card">
      <div class="concept-label">RADIUS</div>
      <div class="concept-title">The AAA Workhorse</div>
      <div class="concept-desc">RADIUS (Remote Authentication Dial-In User Service) is the protocol behind most network authentication. It provides <strong>AAA</strong>: <strong>Authentication</strong> (who are you?), <strong>Authorization</strong> (what may you do?), and <strong>Accounting</strong> (what did you do? — logging/billing). It centralizes credentials so every switch and AP checks against one source (often tied to Active Directory). TACACS+ is a Cisco-oriented alternative more focused on device administration.</div>
    </div>
  </div>
</div>
"""

# ─────────────────────────────── LIFESTYLE wave 25 ───────────────────────────
LIFE_SENTINEL = "<!-- BEGINNER25-LIFE v1 -->"
LIFE_CONTENT = """
<!-- BEGINNER25-LIFE v1 -->
<!-- ── TOPIC: BREAKING INTO IT ───────────────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">🚀</span>
    <span class="topic-name">Breaking Into IT — From Zero to Hired</span>
    <span class="topic-badge">LIFESTYLE • Career</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">THE GOOD NEWS</div>
      <div class="concept-title">IT Is One of the Most Accessible Skilled Careers</div>
      <div class="concept-desc">You don't need a computer science degree or to be a "genius." IT rewards curiosity, persistence, and the willingness to learn by doing. People break in from every background — military, retail, trades, teaching. What employers actually want is proof you can learn, troubleshoot, and show up reliably. The path below has worked for countless career-changers.</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">A REALISTIC ROADMAP</div>
      <div class="concept-title">The Proven On-Ramp</div>
      <table class="ai-table">
        <thead><tr><th>Step</th><th>What to Do</th></tr></thead>
        <tbody>
          <tr><td>1. Pick a direction (loosely)</td><td>Help desk/support is the classic entry point — it touches everything and teaches fundamentals</td></tr>
          <tr><td>2. Learn fundamentals</td><td>Networking, OS (Win + Linux), basic security — free resources abound</td></tr>
          <tr><td>3. Get one foundational cert</td><td>A+ or Network+ or Security+ — passes HR filters, proves baseline</td></tr>
          <tr><td>4. Build a home lab</td><td>Hands-on proof &gt; theory. Document it publicly.</td></tr>
          <tr><td>5. Polish resume + LinkedIn</td><td>Highlight transferable skills + your lab/projects</td></tr>
          <tr><td>6. Apply widely, network</td><td>Most jobs come through people — referrals beat job boards</td></tr>
          <tr><td>7. Get the first role, then grow</td><td>The first job is the hardest. After that, experience compounds.</td></tr>
        </tbody>
      </table>
    </div>
    <div class="concept-card">
      <div class="concept-label">TRANSFERABLE SKILLS</div>
      <div class="concept-title">You Already Have Valuable Experience</div>
      <div class="concept-desc">Career-changers undersell themselves. Skills from other fields are genuinely valuable in IT — name them explicitly on your resume.</div>
      <table class="ai-table">
        <thead><tr><th>From...</th><th>Translates To...</th></tr></thead>
        <tbody>
          <tr><td>Military</td><td>Discipline, working under pressure, security clearance, following + giving procedures</td></tr>
          <tr><td>Customer service / retail</td><td>Help desk gold: patience, communication, de-escalation</td></tr>
          <tr><td>Trades (electrician, etc.)</td><td>Systematic troubleshooting, reading diagrams, safety mindset</td></tr>
          <tr><td>Teaching</td><td>Explaining complex things simply, documentation, patience</td></tr>
          <tr><td>Any job</td><td>Reliability, teamwork, ownership — never underrated</td></tr>
        </tbody>
      </table>
    </div>
    <div class="concept-card">
      <div class="concept-label">THE FIRST 90 DAYS</div>
      <div class="concept-title">How to Start Strong in a New Role</div>
      <table class="ai-table">
        <thead><tr><th>Do</th><th>Why</th></tr></thead>
        <tbody>
          <tr><td>Listen and learn before changing things</td><td>Understand why things are the way they are first</td></tr>
          <tr><td>Ask questions — write down answers</td><td>Nobody expects you to know everything; they expect you to learn</td></tr>
          <tr><td>Find the docs / runbooks / wiki</td><td>Ramp up faster; spot what's missing (and fix it)</td></tr>
          <tr><td>Build relationships</td><td>Knowing who to ask is half the job</td></tr>
          <tr><td>Deliver one small win early</td><td>Builds trust and confidence both ways</td></tr>
          <tr><td>Admit what you don't know</td><td>Faking it on real systems causes outages. Honesty builds trust.</td></tr>
        </tbody>
      </table>
      <div class="concept-desc"><strong>The meta-lesson:</strong> getting in is the hard part. Once you have a foothold and keep learning, IT offers a long ladder — and the compounding skills, network, and reputation you build carry you up it for decades.</div>
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
