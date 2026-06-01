#!/usr/bin/env python3
"""
patch_beginner_concepts_v19.py — Wave 19: Concurrency models, secrets
management, RAG/embeddings, network design, technical writing.

New sentinels:
  BEGINNER19-SCRIPT v1  — Concurrency: threading vs multiprocessing vs async, GIL, sockets
  BEGINNER19-SEC v1     — Secrets management, key management, Vault/KMS
  BEGINNER19-AI v1      — Embeddings, vector databases, RAG (retrieval-augmented generation)
  BEGINNER19-NET v1     — Network topologies, design principles, redundancy
  BEGINNER19-LIFE v1    — Technical writing, documentation, building a public presence
"""
from pathlib import Path

SCRIPT_INJECT_ANCHOR = "<!-- /domain-body script -->"
SEC_INJECT_ANCHOR    = "<!-- /domain-body sec -->"
AI_INJECT_ANCHOR     = "<!-- /domain-body ai -->"
NET_INJECT_ANCHOR    = "<!-- /domain-body net -->"
LIFE_INJECT_ANCHOR   = "<!-- /domain-body lifestyle -->"

# ─────────────────────────────── SCRIPT wave 19 ──────────────────────────────
SCRIPT_SENTINEL = "<!-- BEGINNER19-SCRIPT v1 -->"
SCRIPT_CONTENT = """
<!-- BEGINNER19-SCRIPT v1 -->
<!-- ── TOPIC: CONCURRENCY MODELS ─────────────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">🔀</span>
    <span class="topic-name">Concurrency — Doing More Than One Thing at Once</span>
    <span class="topic-badge">SCRIPT • Advanced</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">CONCURRENCY VS PARALLELISM</div>
      <div class="concept-title">Two Words People Confuse</div>
      <div class="concept-desc"><strong>Concurrency</strong> is dealing with many things at once (structure) — like a chef juggling several dishes, switching between them. <strong>Parallelism</strong> is doing many things at literally the same instant (execution) — like several chefs each cooking one dish. Concurrency is about structure; parallelism is about simultaneous execution. You can have concurrency on a single core (task switching); you need multiple cores for true parallelism.</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">THE GIL</div>
      <div class="concept-title">Why Python Threads Don't Speed Up CPU Work</div>
      <div class="concept-desc">CPython has a Global Interpreter Lock (GIL) — only one thread executes Python bytecode at a time. This means threads <em>don't</em> give you parallel CPU work in Python. But they're still great for I/O-bound work (waiting on network/disk), because the GIL is released during I/O waits. The key question for choosing a tool: <strong>is your task I/O-bound or CPU-bound?</strong></div>
      <table class="ai-table">
        <thead><tr><th>Tool</th><th>Best For</th><th>True Parallelism?</th><th>Why</th></tr></thead>
        <tbody>
          <tr><td><code>threading</code></td><td>I/O-bound (network, disk, APIs)</td><td>No (GIL)</td><td>Threads wait on I/O concurrently; cheap</td></tr>
          <tr><td><code>asyncio</code></td><td>I/O-bound, many concurrent tasks</td><td>No</td><td>Single thread, cooperative; scales to thousands</td></tr>
          <tr><td><code>multiprocessing</code></td><td>CPU-bound (math, image processing)</td><td>Yes</td><td>Separate processes, each its own GIL/core</td></tr>
        </tbody>
      </table>
    </div>
    <div class="concept-card">
      <div class="concept-label">THREADING — I/O BOUND</div>
      <div class="concept-title">Run Many Network Calls Concurrently</div>
      <div class="code-block"><span class="kw">from</span> concurrent.futures <span class="kw">import</span> ThreadPoolExecutor
<span class="kw">import</span> requests

urls = [<span class="str">"https://api.example.com/a"</span>,
        <span class="str">"https://api.example.com/b"</span>,
        <span class="str">"https://api.example.com/c"</span>]

<span class="kw">def</span> <span class="fn">fetch</span>(url):
    <span class="kw">return</span> requests.get(url).status_code

<span class="com"># 3 requests run concurrently instead of one-by-one</span>
<span class="kw">with</span> ThreadPoolExecutor(max_workers=<span class="num">5</span>) <span class="kw">as</span> pool:
    results = <span class="fn">list</span>(pool.map(fetch, urls))
<span class="fn">print</span>(results)   <span class="com"># much faster than sequential for I/O</span></div>
    </div>
    <div class="concept-card">
      <div class="concept-label">MULTIPROCESSING — CPU BOUND</div>
      <div class="concept-title">Use All Your Cores for Heavy Computation</div>
      <div class="code-block"><span class="kw">from</span> concurrent.futures <span class="kw">import</span> ProcessPoolExecutor

<span class="kw">def</span> <span class="fn">heavy_compute</span>(n):
    <span class="kw">return</span> <span class="fn">sum</span>(i*i <span class="kw">for</span> i <span class="kw">in</span> <span class="fn">range</span>(n))   <span class="com"># CPU-intensive</span>

numbers = [<span class="num">10_000_000</span>] * <span class="num">8</span>

<span class="com"># Each process runs on a separate core — true parallelism</span>
<span class="kw">with</span> ProcessPoolExecutor() <span class="kw">as</span> pool:
    results = <span class="fn">list</span>(pool.map(heavy_compute, numbers))

<span class="com"># For CPU work this is ~Ncores faster. Threads would NOT help here.</span></div>
    </div>
    <div class="concept-card">
      <div class="concept-label">RACE CONDITIONS</div>
      <div class="concept-title">The Classic Concurrency Bug</div>
      <div class="concept-desc">When multiple threads modify shared data without coordination, you get race conditions — results depend on unpredictable timing. The fix is a <strong>lock</strong> (mutex) that ensures only one thread touches the shared data at a time. Race conditions are notoriously hard to debug because they're intermittent.</div>
      <div class="code-block"><span class="kw">import</span> threading

counter = <span class="num">0</span>
lock = threading.Lock()

<span class="kw">def</span> <span class="fn">increment</span>():
    <span class="kw">global</span> counter
    <span class="kw">with</span> lock:                <span class="com"># only one thread at a time here</span>
        counter += <span class="num">1</span>            <span class="com"># this is NOT atomic without the lock</span>

<span class="com"># Without the lock, the final count would be unpredictably wrong</span>
<span class="com"># because += is read-modify-write (three steps that can interleave)</span></div>
    </div>
  </div>
</div>

<!-- ── TOPIC: SOCKET PROGRAMMING ─────────────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">🔌</span>
    <span class="topic-name">Sockets — Networking from First Principles</span>
    <span class="topic-badge">SCRIPT • Networking</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">WHAT IS A SOCKET</div>
      <div class="concept-title">The Endpoint of a Network Connection</div>
      <div class="concept-desc">A socket is the programming interface for network communication — an endpoint defined by an IP address and a port. Every network app (browsers, servers, SSH) uses sockets under the hood. Understanding raw sockets demystifies how all higher-level networking works, and it's invaluable for network tools, scanners, and security testing.</div>
      <div class="code-block"><span class="kw">import</span> socket

<span class="com"># ── A simple TCP client ──────────────────────────────────</span>
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  <span class="com"># IPv4, TCP</span>
s.connect((<span class="str">"example.com"</span>, <span class="num">80</span>))
s.sendall(<span class="str">b"GET / HTTP/1.0\\r\\nHost: example.com\\r\\n\\r\\n"</span>)
response = s.recv(<span class="num">4096</span>)
<span class="fn">print</span>(response.decode())
s.close()

<span class="com"># ── A port scanner (the basis of nmap) ───────────────────</span>
<span class="kw">def</span> <span class="fn">scan_port</span>(host, port, timeout=<span class="num">1</span>):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(timeout)
    result = s.connect_ex((host, port))   <span class="com"># 0 = open</span>
    s.close()
    <span class="kw">return</span> result == <span class="num">0</span>

<span class="kw">for</span> port <span class="kw">in</span> [<span class="num">22</span>, <span class="num">80</span>, <span class="num">443</span>, <span class="num">3306</span>]:
    state = <span class="str">"open"</span> <span class="kw">if</span> scan_port(<span class="str">"127.0.0.1"</span>, port) <span class="kw">else</span> <span class="str">"closed"</span>
    <span class="fn">print</span>(<span class="str">f"Port {port}: {state}"</span>)</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">A MINIMAL SERVER</div>
      <div class="concept-title">Listening for Connections</div>
      <div class="code-block"><span class="kw">import</span> socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, <span class="num">1</span>)
server.bind((<span class="str">"0.0.0.0"</span>, <span class="num">9999</span>))   <span class="com"># listen on all interfaces, port 9999</span>
server.listen(<span class="num">5</span>)                  <span class="com"># queue up to 5 pending connections</span>
<span class="fn">print</span>(<span class="str">"Listening on :9999"</span>)

<span class="kw">while</span> <span class="kw">True</span>:
    conn, addr = server.accept()     <span class="com"># blocks until a client connects</span>
    <span class="fn">print</span>(<span class="str">f"Connection from {addr}"</span>)
    data = conn.recv(<span class="num">1024</span>)
    conn.sendall(<span class="str">b"Hello from server\\n"</span>)
    conn.close()</div>
    </div>
  </div>
</div>
"""

# ─────────────────────────────── SEC wave 19 ─────────────────────────────────
SEC_SENTINEL = "<!-- BEGINNER19-SEC v1 -->"
SEC_CONTENT = """
<!-- BEGINNER19-SEC v1 -->
<!-- ── TOPIC: SECRETS MANAGEMENT ─────────────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">🗝️</span>
    <span class="topic-name">Secrets Management — Stop Hardcoding Passwords</span>
    <span class="topic-badge">SEC • Essential</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">THE PROBLEM</div>
      <div class="concept-title">Secrets End Up Everywhere They Shouldn't</div>
      <div class="concept-desc">Passwords, API keys, database credentials, TLS private keys, tokens — collectively "secrets." The cardinal sin is hardcoding them in source code, where they get committed to Git, copied around, and leaked. GitHub is constantly scanned by attackers for accidentally committed AWS keys (they're exploited within minutes). Secrets management is the discipline of storing, accessing, rotating, and auditing secrets safely.</div>
      <table class="ai-table">
        <thead><tr><th>Anti-Pattern</th><th>Do This Instead</th></tr></thead>
        <tbody>
          <tr><td>Hardcoded in source: <code>api_key = "sk-abc123"</code></td><td>Environment variable or secrets manager</td></tr>
          <tr><td>Committed config file with passwords</td><td><code>.gitignore</code> it; use a template + secrets store</td></tr>
          <tr><td>Secrets in Slack/email/wiki</td><td>A proper vault with access controls</td></tr>
          <tr><td>Same password reused everywhere</td><td>Unique secrets, rotated regularly</td></tr>
          <tr><td>Shared admin credentials</td><td>Individual accounts + just-in-time access</td></tr>
        </tbody>
      </table>
    </div>
    <div class="concept-card">
      <div class="concept-label">SECRETS MANAGERS</div>
      <div class="concept-title">Purpose-Built Tools for Secrets</div>
      <table class="ai-table">
        <thead><tr><th>Tool</th><th>Notes</th></tr></thead>
        <tbody>
          <tr><td>HashiCorp Vault</td><td>The gold standard; dynamic secrets, leasing, broad integrations</td></tr>
          <tr><td>AWS Secrets Manager / Parameter Store</td><td>Native to AWS; auto-rotation</td></tr>
          <tr><td>Azure Key Vault / GCP Secret Manager</td><td>Cloud-native equivalents</td></tr>
          <tr><td>1Password / Bitwarden (Secrets)</td><td>Team-friendly, good for smaller orgs</td></tr>
          <tr><td>Sealed Secrets / SOPS</td><td>Encrypt secrets so they CAN live in Git safely</td></tr>
        </tbody>
      </table>
    </div>
    <div class="concept-card">
      <div class="concept-label">KEY MANAGEMENT</div>
      <div class="concept-title">The Lifecycle of Cryptographic Keys</div>
      <div class="concept-desc">Encryption is only as strong as your key management. A perfectly encrypted database is worthless if the key sits in plaintext next to it. Keys have a lifecycle that must be managed.</div>
      <table class="ai-table">
        <thead><tr><th>Phase</th><th>What It Involves</th></tr></thead>
        <tbody>
          <tr><td>Generation</td><td>Create keys with strong randomness, sufficient length</td></tr>
          <tr><td>Storage</td><td>Protect keys: HSM (Hardware Security Module) or KMS, never plaintext</td></tr>
          <tr><td>Distribution</td><td>Get keys to where they're needed securely</td></tr>
          <tr><td>Rotation</td><td>Replace keys periodically — limits damage if one leaks</td></tr>
          <tr><td>Revocation</td><td>Invalidate compromised keys immediately</td></tr>
          <tr><td>Destruction</td><td>Securely delete retired keys</td></tr>
        </tbody>
      </table>
      <div class="concept-desc">A <strong>KMS</strong> (Key Management Service) handles this lifecycle. <strong>Envelope encryption</strong> is the common pattern: a data key encrypts your data, and a master key (in the KMS/HSM) encrypts the data key — so the master key never leaves the secure boundary.</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">SECRET SCANNING</div>
      <div class="concept-title">Catch Leaks Before They Ship</div>
      <div class="code-block"><span class="com"># Scan a repo for committed secrets</span>
gitleaks detect --source .          <span class="com"># popular open-source scanner</span>
trufflehog git file://.             <span class="com"># also scans git history</span>

<span class="com"># If you DID commit a secret:</span>
<span class="com"># 1. ROTATE it immediately (assume it's compromised)</span>
<span class="com"># 2. Remove from history (git filter-repo / BFG)</span>
<span class="com"># 3. Add pre-commit hook to prevent recurrence</span>

<span class="com"># Prevent future leaks with a pre-commit hook</span>
<span class="com"># (gitleaks has a pre-commit integration)</span></div>
    </div>
  </div>
</div>
"""

# ─────────────────────────────── AI wave 19 ──────────────────────────────────
AI_SENTINEL = "<!-- BEGINNER19-AI v1 -->"
AI_CONTENT = """
<!-- BEGINNER19-AI v1 -->
<!-- ── TOPIC: EMBEDDINGS & RAG ───────────────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">🔎</span>
    <span class="topic-name">Embeddings &amp; RAG — Giving AI Access to Your Own Data</span>
    <span class="topic-badge">AI • Modern</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">EMBEDDINGS</div>
      <div class="concept-title">Turning Meaning Into Numbers</div>
      <div class="concept-desc">An embedding is a list of numbers (a vector) that represents the <em>meaning</em> of a piece of text. Texts with similar meaning have vectors that are close together in mathematical space — even if they share no words. "How do I reset my password?" and "I forgot my login credentials" would have nearby embeddings. This is the foundation of modern semantic search, recommendations, and RAG.</div>
      <div class="code-block"><span class="com"># Conceptually — each text becomes a vector of ~1536 numbers</span>
<span class="str">"cat"</span>      → [<span class="num">0.2</span>, -<span class="num">0.5</span>, <span class="num">0.8</span>, ...]
<span class="str">"kitten"</span>   → [<span class="num">0.21</span>, -<span class="num">0.48</span>, <span class="num">0.79</span>, ...]   <span class="com"># very close to "cat"</span>
<span class="str">"airplane"</span> → [-<span class="num">0.9</span>, <span class="num">0.3</span>, -<span class="num">0.1</span>, ...]   <span class="com"># far from "cat"</span>

<span class="com"># Similarity = how close two vectors are (cosine similarity)</span>
<span class="com"># Close vectors = similar meaning. This is "semantic search".</span></div>
    </div>
    <div class="concept-card">
      <div class="concept-label">VECTOR DATABASES</div>
      <div class="concept-title">Storing and Searching Embeddings at Scale</div>
      <div class="concept-desc">A vector database stores embeddings and can instantly find the "nearest" vectors to a query — semantic search over millions of documents. Unlike a regular database (exact match), it finds things by <em>meaning</em>.</div>
      <table class="ai-table">
        <thead><tr><th>Tool</th><th>Notes</th></tr></thead>
        <tbody>
          <tr><td>Pinecone</td><td>Managed, popular, easy to start</td></tr>
          <tr><td>Weaviate / Qdrant / Milvus</td><td>Open-source, self-hostable</td></tr>
          <tr><td>Chroma</td><td>Lightweight, great for prototyping locally</td></tr>
          <tr><td>pgvector</td><td>Vector search inside PostgreSQL — no new database needed</td></tr>
          <tr><td>FAISS</td><td>Facebook's library; fast in-memory similarity search</td></tr>
        </tbody>
      </table>
    </div>
    <div class="concept-card">
      <div class="concept-label">RAG</div>
      <div class="concept-title">Retrieval-Augmented Generation</div>
      <div class="concept-desc">LLMs don't know your company's internal docs, and they hallucinate. RAG solves both: before answering, you <em>retrieve</em> relevant documents from your own data and feed them to the LLM as context. The model answers using YOUR facts, with citations. This is how most "chat with your docs" and enterprise AI assistants work — without expensive retraining.</div>
      <table class="ai-table">
        <thead><tr><th>Step</th><th>What Happens</th></tr></thead>
        <tbody>
          <tr><td>1. Ingest (offline)</td><td>Split docs into chunks, embed each, store in vector DB</td></tr>
          <tr><td>2. Query</td><td>User asks a question → embed the question</td></tr>
          <tr><td>3. Retrieve</td><td>Find the most similar chunks in the vector DB</td></tr>
          <tr><td>4. Augment</td><td>Insert those chunks into the prompt as context</td></tr>
          <tr><td>5. Generate</td><td>LLM answers using the retrieved context + cites sources</td></tr>
        </tbody>
      </table>
      <div class="concept-desc"><strong>Why it matters for IT:</strong> RAG lets you build assistants over your runbooks, security policies, ticket history, or documentation — grounded in real data, drastically reducing hallucinations. It's the most common pattern in production AI applications today.</div>
    </div>
  </div>
</div>
"""

# ─────────────────────────────── NET wave 19 ─────────────────────────────────
NET_SENTINEL = "<!-- BEGINNER19-NET v1 -->"
NET_CONTENT = """
<!-- BEGINNER19-NET v1 -->
<!-- ── TOPIC: NETWORK DESIGN & TOPOLOGIES ────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">🗺️</span>
    <span class="topic-name">Network Design — How Networks Are Structured</span>
    <span class="topic-badge">NET • Foundation</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">TOPOLOGIES</div>
      <div class="concept-title">The Shapes Networks Take</div>
      <table class="ai-table">
        <thead><tr><th>Topology</th><th>Structure</th><th>Pros / Cons</th></tr></thead>
        <tbody>
          <tr><td>Star</td><td>All devices connect to a central switch</td><td>+ Easy to manage; − central point of failure (most common LAN)</td></tr>
          <tr><td>Mesh</td><td>Devices interconnect (full or partial)</td><td>+ Highly redundant; − expensive, complex (used in WANs, Wi-Fi mesh)</td></tr>
          <tr><td>Bus</td><td>All on a single backbone cable</td><td>− Obsolete; one break kills all</td></tr>
          <tr><td>Ring</td><td>Each device connects to two neighbors</td><td>Used in some fiber/MAN setups (with redundant ring)</td></tr>
          <tr><td>Hybrid</td><td>Combination (e.g., star-of-stars)</td><td>Real-world networks are hybrids</td></tr>
        </tbody>
      </table>
    </div>
    <div class="concept-card">
      <div class="concept-label">THE THREE-TIER MODEL</div>
      <div class="concept-title">How Enterprise Networks Are Layered</div>
      <div class="concept-desc">Classic enterprise network design uses three hierarchical layers. This separation makes networks scalable, manageable, and resilient.</div>
      <table class="ai-table">
        <thead><tr><th>Layer</th><th>Role</th><th>Devices</th></tr></thead>
        <tbody>
          <tr><td><strong>Access</strong></td><td>Where end devices connect (PCs, phones, APs)</td><td>Access switches, wall ports</td></tr>
          <tr><td><strong>Distribution</strong></td><td>Aggregates access layer; policy, routing between VLANs</td><td>L3 switches, routers</td></tr>
          <tr><td><strong>Core</strong></td><td>High-speed backbone; moves traffic fast</td><td>High-capacity core switches/routers</td></tr>
        </tbody>
      </table>
      <div class="concept-desc">In modern data centers, this is often replaced by a <strong>spine-leaf</strong> architecture: every leaf (access) switch connects to every spine switch, giving predictable low latency and easy horizontal scaling — ideal for east-west (server-to-server) traffic.</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">DESIGNING FOR RESILIENCE</div>
      <div class="concept-title">No Single Point of Failure</div>
      <table class="ai-table">
        <thead><tr><th>Technique</th><th>What It Provides</th></tr></thead>
        <tbody>
          <tr><td>Redundant links + STP</td><td>Backup paths; Spanning Tree Protocol prevents loops</td></tr>
          <tr><td>Link aggregation (LACP)</td><td>Bundle multiple links for bandwidth + failover</td></tr>
          <tr><td>Redundant gateways (HSRP/VRRP)</td><td>Two routers share a virtual IP; one takes over if the other fails</td></tr>
          <tr><td>Dual power supplies / UPS</td><td>Survive power failures</td></tr>
          <tr><td>Multiple ISPs (multihoming)</td><td>Survive an internet provider outage</td></tr>
          <tr><td>Out-of-band management</td><td>Manage gear even when the production network is down</td></tr>
        </tbody>
      </table>
    </div>
    <div class="concept-card">
      <div class="concept-label">QUALITY OF SERVICE</div>
      <div class="concept-title">QoS — Not All Traffic Is Equal</div>
      <div class="concept-desc">When the network is congested, QoS decides what gets priority. A dropped video-call packet is far worse than a delayed email — voice and video are real-time and sensitive to latency/jitter, while file downloads can wait. QoS classifies and prioritizes traffic so critical, time-sensitive flows (VoIP, video conferencing) get served first. Without it, a big backup job could ruin everyone's video calls.</div>
    </div>
  </div>
</div>
"""

# ─────────────────────────────── LIFESTYLE wave 19 ───────────────────────────
LIFE_SENTINEL = "<!-- BEGINNER19-LIFE v1 -->"
LIFE_CONTENT = """
<!-- BEGINNER19-LIFE v1 -->
<!-- ── TOPIC: TECHNICAL WRITING ──────────────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">✍️</span>
    <span class="topic-name">Technical Writing — The Underrated Career Superpower</span>
    <span class="topic-badge">LIFESTYLE • Communication</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">WHY IT MATTERS</div>
      <div class="concept-title">The Engineer Who Writes Well Gets Promoted</div>
      <div class="concept-desc">In IT, your impact is multiplied by how well you communicate it. The brilliant fix nobody understands has limited value; the clearly-documented one helps the whole team forever. Writing well — runbooks, post-mortems, design docs, tickets, emails — is one of the highest-ROI skills you can build, and it's rare enough that it makes you stand out immediately. As you grow senior, writing matters MORE, not less.</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">PRINCIPLES</div>
      <div class="concept-title">How to Write So People Actually Understand</div>
      <table class="ai-table">
        <thead><tr><th>Principle</th><th>What It Means</th></tr></thead>
        <tbody>
          <tr><td>Know your audience</td><td>Write for THEM — exec summary vs. engineer deep-dive are different</td></tr>
          <tr><td>BLUF (Bottom Line Up Front)</td><td>Put the conclusion/ask first. Don't bury it (military + journalism wisdom)</td></tr>
          <tr><td>One idea per paragraph</td><td>Walls of text don't get read</td></tr>
          <tr><td>Show, don't tell</td><td>Concrete examples and commands beat abstract description</td></tr>
          <tr><td>Cut ruthlessly</td><td>Delete every word that doesn't earn its place</td></tr>
          <tr><td>Active voice</td><td>"The script deletes logs" not "Logs are deleted by the script"</td></tr>
        </tbody>
      </table>
    </div>
    <div class="concept-card">
      <div class="concept-label">DOCUMENT TYPES</div>
      <div class="concept-title">The Docs Every IT Pro Writes</div>
      <table class="ai-table">
        <thead><tr><th>Document</th><th>Purpose &amp; Tip</th></tr></thead>
        <tbody>
          <tr><td>Runbook</td><td>Step-by-step ops procedure. Write it so a tired person at 3am can follow it.</td></tr>
          <tr><td>Post-mortem</td><td>What broke and why. Blameless. Timeline + root cause + action items.</td></tr>
          <tr><td>Design doc / RFC</td><td>Propose a change before building. Forces clear thinking; gets buy-in.</td></tr>
          <tr><td>README</td><td>How to set up and use a project. The first thing anyone reads.</td></tr>
          <tr><td>Ticket / bug report</td><td>Steps to reproduce, expected vs. actual, environment. Specifics save hours.</td></tr>
        </tbody>
      </table>
    </div>
  </div>
</div>

<!-- ── TOPIC: BUILDING A PUBLIC PRESENCE ─────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">🌟</span>
    <span class="topic-name">Building in Public — Your Reputation Compounds</span>
    <span class="topic-badge">LIFESTYLE • Career</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">THE IDEA</div>
      <div class="concept-title">Let Your Work Be Findable</div>
      <div class="concept-desc">You don't need to be an influencer. But a small, genuine public footprint — a GitHub with your projects, a blog documenting what you learn, a few helpful answers online — compounds over a career. It creates serendipity: recruiters find you, peers vouch for you, and writing things down deepens your own learning. The person who shares what they learn becomes the person others associate with that knowledge.</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">LOW-EFFORT, HIGH-RETURN</div>
      <div class="concept-title">Where to Start (No Burnout Required)</div>
      <table class="ai-table">
        <thead><tr><th>Action</th><th>Why It Pays Off</th></tr></thead>
        <tbody>
          <tr><td>Keep a GitHub with real projects</td><td>Proof of skill that beats resume bullet points</td></tr>
          <tr><td>Write up things you figured out</td><td>"How I fixed X" posts help others + cement your learning</td></tr>
          <tr><td>A clean, current LinkedIn</td><td>Where recruiters and peers actually look</td></tr>
          <tr><td>Answer questions (forums, Discord, Stack Overflow)</td><td>Builds reputation; teaching reveals your own gaps</td></tr>
          <tr><td>Document your home lab</td><td>Tangible portfolio + interview talking points</td></tr>
        </tbody>
      </table>
      <div class="concept-desc"><strong>The mindset:</strong> share to help and to learn, not to chase clout. Consistency beats intensity — one short post a month for a year is a body of work. Your future self (and your future employers) will thank you.</div>
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
        (AI_INJECT_ANCHOR,     AI_SENTINEL,     AI_CONTENT),
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
