#!/usr/bin/env python3
"""
patch_beginner_concepts_v10.py — Wave 10: Cloud fundamentals, Docker/containers,
advanced security topics, scripting patterns, and more.

New sentinels:
  BEGINNER10-SCRIPT v1  — Cloud concepts in Python (boto3 taste), env vars, config
  BEGINNER10-NET v1     — Cloud networking, VPC, CDN, SD-WAN
  BEGINNER10-LINUX v1   — Docker/containers intro, basic commands
  BEGINNER10-SEC v1     — Identity & access management, zero trust, supply chain
  BEGINNER10-LIFE v1    — Soft skills for tech: clear communication, documentation
"""
from pathlib import Path

SCRIPT_INJECT_ANCHOR = "<!-- /domain-body script -->"
NET_INJECT_ANCHOR    = "<!-- /domain-body net -->"
LINUX_INJECT_ANCHOR  = "<!-- /domain-body linux -->"
SEC_INJECT_ANCHOR    = "<!-- /domain-body sec -->"
LIFE_INJECT_ANCHOR   = "<!-- /domain-body lifestyle -->"

# ─────────────────────────────── SCRIPTING wave 10 ───────────────────────────
SCRIPT_SENTINEL = "<!-- BEGINNER10-SCRIPT v1 -->"
SCRIPT_CONTENT = """
<!-- BEGINNER10-SCRIPT v1 -->
<!-- ── TOPIC: ENVIRONMENT VARIABLES & CONFIG ─────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">🔧</span>
    <span class="topic-name">Environment Variables &amp; Configuration — Keep Secrets Out of Code</span>
    <span class="topic-badge">SCRIPT • Essential</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">WHY NOT HARDCODE</div>
      <div class="concept-title">Credentials in Code Get Leaked</div>
      <div class="concept-desc">If you put your API key, database password, or secret token directly in your code and push it to GitHub, it's compromised — even if you delete it later. Git history is forever. GitHub bots scan every public push for secrets within seconds. Keep secrets in environment variables, not source code.</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">ENVIRONMENT VARIABLES</div>
      <div class="concept-title">OS-Level Key-Value Pairs</div>
      <div class="code-block"><span class="com"># Set in shell (temporary)</span>
export DB_PASSWORD=<span class="str">"supersecret"</span>
export API_KEY=<span class="str">"abc123xyz"</span>

<span class="com"># Read in Python</span>
<span class="kw">import</span> os

db_pass = os.environ[<span class="str">"DB_PASSWORD"</span>]           <span class="com"># raises KeyError if missing</span>
api_key = os.environ.get(<span class="str">"API_KEY"</span>)             <span class="com"># returns None if missing</span>
port    = os.environ.get(<span class="str">"PORT"</span>, <span class="str">"8080"</span>)       <span class="com"># use default if not set</span>

<span class="com"># Validate required vars at startup (fail fast)</span>
required = [<span class="str">"DB_HOST"</span>, <span class="str">"DB_PASSWORD"</span>, <span class="str">"SECRET_KEY"</span>]
missing = [k <span class="kw">for</span> k <span class="kw">in</span> required <span class="kw">if</span> k <span class="kw">not in</span> os.environ]
<span class="kw">if</span> missing:
    <span class="kw">raise</span> RuntimeError(<span class="str">f"Missing env vars: {missing}"</span>)</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">.ENV FILES</div>
      <div class="concept-title">python-dotenv — Local Development</div>
      <div class="code-block"><span class="com"># .env file (NEVER commit this!)</span>
DB_HOST=localhost
DB_PASSWORD=dev_password_123
API_KEY=test_key_abc
DEBUG=true

<span class="com"># .gitignore should have:</span>
.env
.env.*
*.env</div>
      <div class="code-block"><span class="com"># In Python: pip install python-dotenv</span>
<span class="kw">from</span> dotenv <span class="kw">import</span> load_dotenv
load_dotenv()   <span class="com"># loads .env into os.environ</span>

<span class="kw">import</span> os
db_host = os.environ[<span class="str">"DB_HOST"</span>]   <span class="com"># now available</span></div>
    </div>
    <div class="concept-card">
      <div class="concept-label">CONFIG FILES</div>
      <div class="concept-title">TOML, YAML, JSON for Non-Secret Config</div>
      <div class="code-block"><span class="com"># config.toml (Python 3.11+ has built-in tomllib)</span>
[database]
host = "localhost"
port = 5432
name = "myapp"

[server]
port = 8080
debug = false</div>
      <div class="code-block"><span class="kw">import</span> tomllib

<span class="kw">with</span> <span class="fn">open</span>(<span class="str">"config.toml"</span>, <span class="str">"rb"</span>) <span class="kw">as</span> f:
    config = tomllib.load(f)

db_host = config[<span class="str">"database"</span>][<span class="str">"host"</span>]
server_port = config[<span class="str">"server"</span>][<span class="str">"port"</span>]</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">12-FACTOR APP</div>
      <div class="concept-title">Best Practice: Config in the Environment</div>
      <div class="concept-desc">The 12-Factor App methodology (widely adopted for cloud-native apps) says: store ALL config in environment variables. This way the SAME code runs in dev, staging, and production — only the env vars change. No "if environment == 'production':" branches. No secrets in git. Works with any deployment platform (Docker, Kubernetes, Heroku, Lambda).</div>
    </div>
  </div>
</div>

<!-- ── TOPIC: LOGGING — DO IT RIGHT ──────────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">📋</span>
    <span class="topic-name">Logging — Stop Using print(), Use logging</span>
    <span class="topic-badge">SCRIPT • Professional</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">WHY PROPER LOGGING</div>
      <div class="concept-title">print() Disappears; Logs Persist</div>
      <div class="concept-desc"><code>print()</code> dumps to stdout with no timestamp, no severity, and no way to control verbosity. The <code>logging</code> module gives you: severity levels, timestamps, where the log came from, file/console output, filtering, and structured formats for log aggregation tools.</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">BASIC SETUP</div>
      <div class="concept-title">Configure Once at Entry Point</div>
      <div class="code-block"><span class="kw">import</span> logging

<span class="com"># Configure at application startup (once)</span>
logging.basicConfig(
    level=logging.INFO,
    format=<span class="str">'%(asctime)s [%(levelname)s] %(name)s: %(message)s'</span>,
    datefmt=<span class="str">'%Y-%m-%d %H:%M:%S'</span>,
    handlers=[
        logging.StreamHandler(),           <span class="com"># console output</span>
        logging.FileHandler(<span class="str">'app.log'</span>),    <span class="com"># also write to file</span>
    ]
)

<span class="com"># Get a logger per module (best practice)</span>
logger = logging.getLogger(__name__)

<span class="com"># Five severity levels</span>
logger.debug(<span class="str">"Detailed debugging info"</span>)   <span class="com"># only in dev</span>
logger.info(<span class="str">"User Alice logged in"</span>)
logger.warning(<span class="str">"Config not found, using defaults"</span>)
logger.error(<span class="str">"Failed to connect to database"</span>)
logger.critical(<span class="str">"System cannot start — exiting"</span>)</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">STRUCTURED LOGGING</div>
      <div class="concept-title">JSON Logs for Modern Observability</div>
      <div class="concept-desc">Plain text logs are for humans to read. JSON logs are for machines to search. Modern stacks (ELK, Splunk, Datadog) ingest JSON and let you query <code>user_id:42 AND action:login</code> instead of grepping strings.</div>
      <div class="code-block"><span class="com"># pip install structlog</span>
<span class="kw">import</span> structlog

logger = structlog.get_logger()

logger.info(<span class="str">"user_login"</span>,
            user_id=<span class="num">42</span>,
            ip=<span class="str">"192.168.1.5"</span>,
            success=<span class="kw">True</span>)
<span class="com"># Output: {"event": "user_login", "user_id": 42, "ip": "...", "success": true, "timestamp": "..."}</span></div>
    </div>
    <div class="concept-card">
      <div class="concept-label">LOG LEVELS IN PRODUCTION</div>
      <div class="concept-title">Filter by Severity</div>
      <div class="concept-desc"><strong>Production</strong>: set to WARNING or INFO. DEBUG is too verbose — logs become noise, disk fills up, secrets can leak (DEBUG often logs full request bodies).<br>
      <strong>Dev/staging</strong>: DEBUG is fine and useful.<br>
      Control via env var: <code>LOG_LEVEL=DEBUG python3 app.py</code> with <code>level=os.environ.get("LOG_LEVEL", "INFO")</code></div>
    </div>
  </div>
</div>

<!-- ── TOPIC: VIRTUAL ENVIRONMENTS & REPRODUCIBILITY ─────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">📦</span>
    <span class="topic-name">Reproducible Python Environments — Make It Work Everywhere</span>
    <span class="topic-badge">SCRIPT • Professional</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">THE PROBLEM</div>
      <div class="concept-title">"Works on My Machine"</div>
      <div class="concept-desc">Your script depends on specific library versions. Your teammate installs different versions and it breaks. You deploy to a server with yet another version and it crashes. Reproducibility means anyone — or any server — can run your code and get identical results.</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">REQUIREMENTS FILES</div>
      <div class="concept-title">Pin Exact Versions for Production</div>
      <div class="code-block"><span class="com"># requirements.txt — exact versions (production)</span>
requests==2.31.0
flask==3.0.0
sqlalchemy==2.0.23
python-dotenv==1.0.0

<span class="com"># requirements-dev.txt — dev-only tools</span>
pytest==7.4.3
pytest-cov==4.1.0
black==23.11.0
mypy==1.7.1

<span class="com"># Generate from current environment</span>
pip freeze &gt; requirements.txt

<span class="com"># Recreate environment exactly</span>
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">PYPROJECT.TOML</div>
      <div class="concept-title">Modern Python Project Standard</div>
      <div class="concept-desc">The modern Python packaging standard uses <code>pyproject.toml</code> (PEP 517/518). Tools like <code>uv</code>, <code>poetry</code>, and <code>hatch</code> use it. It combines: package metadata, dependencies, build config, tool config (black, mypy settings) — all in one file. Gradually replacing <code>setup.py</code> + <code>requirements.txt</code>.</div>
    </div>
  </div>
</div>
"""

# ─────────────────────────────── NET wave 10 ─────────────────────────────────
NET_SENTINEL = "<!-- BEGINNER10-NET v1 -->"
NET_CONTENT = """
<!-- BEGINNER10-NET v1 -->
<!-- ── TOPIC: CLOUD NETWORKING — VPC & CDN ───────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">☁️</span>
    <span class="topic-name">Cloud Networking — VPC, Subnets &amp; CDNs</span>
    <span class="topic-badge">NET • Cloud</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">CLOUD MODELS</div>
      <div class="concept-title">IaaS · PaaS · SaaS</div>
      <div class="concept-desc"><strong>IaaS (Infrastructure as a Service)</strong> — rent VMs, storage, networking. You manage OS and above. Examples: AWS EC2, Azure VMs, Google Compute Engine. Most control, most responsibility.<br>
      <strong>PaaS (Platform as a Service)</strong> — deploy your app code; provider manages OS, runtime, scaling. Examples: Heroku, AWS Elastic Beanstalk, Google App Engine.<br>
      <strong>SaaS (Software as a Service)</strong> — use the finished product. Salesforce, Office 365, Gmail. No infrastructure concern at all.</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">VPC</div>
      <div class="concept-title">Virtual Private Cloud — Your Private Network in the Cloud</div>
      <div class="concept-desc">A VPC is a logically isolated section of the cloud where you launch resources in a network you define. You control IP ranges, subnets, routing tables, and gateways — just like a physical data center, but virtualized.</div>
      <table class="ai-table">
        <thead><tr><th>Component</th><th>Purpose</th></tr></thead>
        <tbody>
          <tr><td>VPC CIDR</td><td>IP range for the entire VPC (e.g., 10.0.0.0/16)</td></tr>
          <tr><td>Subnet</td><td>Sub-range within VPC; public (internet) or private</td></tr>
          <tr><td>Internet Gateway</td><td>Allows public subnets to reach the internet</td></tr>
          <tr><td>NAT Gateway</td><td>Lets private subnets initiate outbound internet; no inbound</td></tr>
          <tr><td>Route Table</td><td>Defines where traffic goes (0.0.0.0/0 → IGW for public)</td></tr>
          <tr><td>Security Group</td><td>Stateful firewall at instance level</td></tr>
          <tr><td>NACL</td><td>Stateless firewall at subnet level</td></tr>
        </tbody>
      </table>
    </div>
    <div class="concept-card">
      <div class="concept-label">CDN</div>
      <div class="concept-title">Content Delivery Network — Cache at the Edge</div>
      <div class="concept-desc">A CDN stores copies of your static content (images, JS, CSS, videos) at servers (PoPs — Points of Presence) close to users worldwide. When a user in Tokyo requests your image, it comes from a Tokyo edge node, not your origin server in Virginia. Result: dramatically lower latency and reduced origin server load. Examples: Cloudflare, AWS CloudFront, Fastly, Akamai.</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">SHARED RESPONSIBILITY MODEL</div>
      <div class="concept-title">Who Is Responsible for What in Cloud?</div>
      <div class="concept-desc">AWS/Azure/GCP secure <strong>the cloud</strong> (physical hardware, hypervisor, network). You secure <strong>in the cloud</strong> (your VMs, data, IAM config, encryption, application code). Misconfigurations (public S3 buckets, overly permissive security groups, no encryption) are YOUR responsibility, not the cloud provider's. This is the source of most cloud breaches.</div>
    </div>
  </div>
</div>
"""

# ─────────────────────────────── LINUX wave 10 ───────────────────────────────
LINUX_SENTINEL = "<!-- BEGINNER10-LINUX v1 -->"
LINUX_CONTENT = """
<!-- BEGINNER10-LINUX v1 -->
<!-- ── TOPIC: DOCKER & CONTAINERS ────────────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">🐳</span>
    <span class="topic-name">Docker &amp; Containers — Package Once, Run Anywhere</span>
    <span class="topic-badge">LINUX • Modern Ops</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">WHAT IS A CONTAINER</div>
      <div class="concept-title">Isolated Process, Not a Full VM</div>
      <div class="concept-desc">A container packages your app + its dependencies + runtime into one portable unit. It shares the host OS kernel (unlike a VM which has its own). Result: starts in milliseconds, uses far less memory than a VM, runs identically everywhere. "Works on my machine" is solved — because you ship the machine.</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">CONTAINER vs VM</div>
      <div class="concept-title">Isolation Trade-offs</div>
      <table class="ai-table">
        <thead><tr><th></th><th>Container</th><th>VM</th></tr></thead>
        <tbody>
          <tr><td>Startup</td><td>Milliseconds</td><td>Minutes</td></tr>
          <tr><td>Memory overhead</td><td>MBs</td><td>GBs</td></tr>
          <tr><td>Isolation</td><td>Process-level (shares kernel)</td><td>Full OS isolation</td></tr>
          <tr><td>Security</td><td>Lower (kernel shared)</td><td>Higher (separate kernel)</td></tr>
          <tr><td>Portability</td><td>Very high</td><td>High (but larger images)</td></tr>
        </tbody>
      </table>
    </div>
    <div class="concept-card">
      <div class="concept-label">BASIC DOCKER COMMANDS</div>
      <div class="concept-title">Pull, Run, List, Stop, Remove</div>
      <div class="code-block"><span class="com"># Pull an image from Docker Hub</span>
docker pull ubuntu:22.04
docker pull nginx:latest

<span class="com"># Run a container</span>
docker run nginx               <span class="com"># foreground</span>
docker run -d nginx            <span class="com"># detached (background)</span>
docker run -it ubuntu bash     <span class="com"># interactive terminal</span>

<span class="com"># Port mapping (host:container)</span>
docker run -d -p 8080:80 nginx   <span class="com"># localhost:8080 → container:80</span>

<span class="com"># List running containers</span>
docker ps
docker ps -a   <span class="com"># including stopped</span>

<span class="com"># Logs</span>
docker logs container_id
docker logs -f container_id    <span class="com"># follow</span>

<span class="com"># Stop, start, remove</span>
docker stop container_id
docker start container_id
docker rm container_id

<span class="com"># Get a shell in a running container</span>
docker exec -it container_id bash</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">DOCKERFILE</div>
      <div class="concept-title">Recipe to Build Your Image</div>
      <div class="code-block"><span class="com"># Dockerfile — simple Python app</span>
FROM python:3.12-slim           <span class="com"># base image</span>

WORKDIR /app                    <span class="com"># working directory inside container</span>

COPY requirements.txt .         <span class="com"># copy deps first (cache layers)</span>
RUN pip install -r requirements.txt

COPY . .                        <span class="com"># then copy app code</span>

ENV PORT=8080                   <span class="com"># environment variable</span>
EXPOSE 8080                     <span class="com"># document port (doesn't publish)</span>

CMD [<span class="str">"python3"</span>, <span class="str">"app.py"</span>]       <span class="com"># default command</span></div>
      <div class="code-block"><span class="com"># Build the image</span>
docker build -t myapp:latest .

<span class="com"># Run it</span>
docker run -d -p 8080:8080 myapp:latest</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">DOCKER COMPOSE</div>
      <div class="concept-title">Multi-Container Applications</div>
      <div class="code-block"><span class="com"># docker-compose.yml</span>
version: <span class="str">"3.9"</span>
services:
  web:
    build: .
    ports:
      - <span class="str">"8080:8080"</span>
    environment:
      - DB_HOST=db
    depends_on:
      - db

  db:
    image: postgres:16
    environment:
      POSTGRES_PASSWORD: devpassword
      POSTGRES_DB: myapp
    volumes:
      - pgdata:/var/lib/postgresql/data

volumes:
  pgdata:</div>
      <div class="code-block"><span class="com"># Start all services</span>
docker compose up -d

<span class="com"># Stop all services</span>
docker compose down

<span class="com"># View logs for all services</span>
docker compose logs -f</div>
    </div>
  </div>
</div>
"""

# ─────────────────────────────── SEC wave 10 ─────────────────────────────────
SEC_SENTINEL = "<!-- BEGINNER10-SEC v1 -->"
SEC_CONTENT = """
<!-- BEGINNER10-SEC v1 -->
<!-- ── TOPIC: IDENTITY & ACCESS MANAGEMENT ───────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">🪪</span>
    <span class="topic-name">Identity &amp; Access Management — Who Can Do What</span>
    <span class="topic-badge">SEC • Foundation</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">THE CORE PROBLEM</div>
      <div class="concept-title">Authentication vs Authorization</div>
      <div class="concept-desc"><strong>Authentication (AuthN)</strong> — proving who you are. "I am Alice." Verified by password, biometric, token, or certificate.<br>
      <strong>Authorization (AuthZ)</strong> — what you're allowed to do. "Alice can read reports but not delete records." Enforced by permissions, roles, policies.<br>
      These are separate concerns. Getting them confused causes security holes (assuming that anyone logged in can do anything).</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">PRINCIPLE OF LEAST PRIVILEGE</div>
      <div class="concept-title">Give Only What's Needed</div>
      <div class="concept-desc">Every user, service, and process should have the minimum permissions needed to do its job — and nothing more. An analytics service that reads data shouldn't have write permissions. A developer account shouldn't have production database access by default. When something is compromised, least privilege contains the blast radius.</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">RBAC vs ABAC</div>
      <div class="concept-title">Role-Based vs Attribute-Based Access Control</div>
      <div class="concept-desc"><strong>RBAC (Role-Based)</strong> — assign roles to users; permissions attached to roles. Simple to manage at scale. "Alice is an Admin; Admins can do X, Y, Z." Standard in most systems.<br>
      <strong>ABAC (Attribute-Based)</strong> — permissions based on attributes of user, resource, environment. "Allow if user.department = finance AND resource.sensitivity = confidential AND time = business_hours." More flexible, harder to audit.</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">SSO & FEDERATION</div>
      <div class="concept-title">One Login, Many Systems</div>
      <div class="concept-desc"><strong>SSO (Single Sign-On)</strong> — log in once, access many applications. Used with SAML 2.0 or OIDC (OAuth 2.0 extension). Benefits: one password to manage, one place to revoke access when someone leaves.<br>
      <strong>OIDC/OAuth 2.0</strong> — modern standard for federated identity. "Login with Google" is OIDC. Google proves your identity to the app without giving the app your password.<br>
      <strong>SAML 2.0</strong> — XML-based, enterprise standard. Used for enterprise SSO (Okta, Azure AD, Ping).</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">ZERO TRUST</div>
      <div class="concept-title">Never Trust, Always Verify</div>
      <div class="concept-desc">Traditional security assumed: inside the network = trusted; outside = untrusted. Zero trust assumes breach and verifies every request regardless of source — even from inside the corporate network.<br>
      Principles:<br>
      • Verify explicitly — authenticate and authorize every request, every time<br>
      • Least privilege — minimal access, time-limited<br>
      • Assume breach — design as if attackers are already inside</div>
    </div>
  </div>
</div>

<!-- ── TOPIC: SUPPLY CHAIN SECURITY ──────────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">⛓️</span>
    <span class="topic-name">Supply Chain Security — Trust What You Build With</span>
    <span class="topic-badge">SEC • Advanced Awareness</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">WHAT IS SUPPLY CHAIN SECURITY</div>
      <div class="concept-title">Attackers Go for the Builder, Not the Building</div>
      <div class="concept-desc">Modern apps depend on thousands of open-source packages. Attackers compromise <strong>upstream</strong> — a popular library, build tool, or CI/CD pipeline — and then automatically infect everything downstream that uses it. The SolarWinds breach (2020) infected 18,000 organizations via a compromised software update. The XZ Utils backdoor (2024) nearly compromised SSH servers worldwide.</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">SBOM</div>
      <div class="concept-title">Software Bill of Materials</div>
      <div class="concept-desc">An SBOM is an inventory of every component in your software — all dependencies, their versions, and their licenses. Like an ingredients list for your app. When a critical vulnerability (Log4Shell, Heartbleed) drops, you can instantly check if you're affected by scanning your SBOM. Now required for software sold to US federal agencies.</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">DEPENDENCY HYGIENE</div>
      <div class="concept-title">Practical Steps to Reduce Risk</div>
      <div class="concept-desc">• <strong>Pin versions</strong>: use <code>requests==2.31.0</code> not <code>requests&gt;=2</code>. Unpinned deps silently update and break.<br>
      • <strong>Verify hashes</strong>: <code>pip install --require-hashes</code> validates that downloaded packages match expected hashes.<br>
      • <strong>Use Dependabot or Renovate</strong>: automated PRs when dependencies have security updates.<br>
      • <strong>Audit regularly</strong>: <code>pip audit</code>, <code>npm audit</code>, <code>cargo audit</code> scan for known vulnerabilities.<br>
      • <strong>Don't install unknown packages</strong>: "typosquatting" packages (requestts, colors2) exist to compromise you.</div>
    </div>
  </div>
</div>
"""

# ─────────────────────────────── LIFESTYLE wave 10 ───────────────────────────
LIFE_SENTINEL = "<!-- BEGINNER10-LIFE v1 -->"
LIFE_CONTENT = """
<!-- BEGINNER10-LIFE v1 -->
<!-- ── TOPIC: CLEAR TECHNICAL COMMUNICATION ──────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">✍️</span>
    <span class="topic-name">Clear Technical Communication — The Skill That Multiplies Everything</span>
    <span class="topic-badge">LIFESTYLE • Professional</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">WHY IT MATTERS</div>
      <div class="concept-title">Technical Skill ÷ Communication = Invisible</div>
      <div class="concept-desc">The most technically brilliant person in the room accomplishes nothing if they can't explain their findings, get buy-in for solutions, or write a ticket that others can act on. Communication is the multiplier for all your other skills. A mediocre engineer who communicates exceptionally will advance faster than a brilliant engineer who can't write a coherent email.</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">PYRAMID PRINCIPLE</div>
      <div class="concept-title">Lead With Conclusion, Then Support</div>
      <div class="concept-desc">People in IT often bury the conclusion: "I checked the logs, then ran a packet capture, then tested the firewall rules, then discovered... the problem is a misconfigured DNS entry." That's backwards. Lead with: <strong>"The outage is caused by a DNS misconfiguration (confirmed). Fix takes 10 minutes. Here's what I found."</strong> Then explain. Decision-makers need the conclusion first.</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">ASKING GOOD QUESTIONS</div>
      <div class="concept-title">Show Your Work Before You Ask</div>
      <div class="concept-desc">Before asking for help, document: what you're trying to do, what you've tried, what happened, and what you expected. "It doesn't work" is unusable. "I'm trying to get nginx to serve on port 443. When I run <code>nginx -t</code> it reports a valid config. When I curl localhost:443 I get 'connection refused'. <code>ss -tlnp | grep 443</code> shows nothing listening. Here's my config block." — THIS gets a fast answer.</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">DOCUMENTATION</div>
      <div class="concept-title">Write It Down or It Didn't Happen</div>
      <div class="concept-desc">Undocumented systems exist only inside the head of whoever built them. When that person is gone (new job, vacation, hospital) everything breaks. The rule: if you configure it, document it. If you solve it, write down the solution. If you build it, document how it runs, why it's built the way it is, and how to troubleshoot common problems.<br>
      Documentation doesn't have to be perfect — a messy Confluence page, a README, or even a Slack post that gets pinned is infinitely better than nothing.</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">BLAMELESS INCIDENT REVIEWS</div>
      <div class="concept-title">Learn, Don't Prosecute</div>
      <div class="concept-desc">Post-mortems (incident reviews) are most valuable when they're <strong>blameless</strong>. "Who caused this?" prevents honest reporting and creates a culture of fear where people hide mistakes. "Why did our system make it easy for this mistake to happen?" leads to systemic fixes. The best organizations (Google, Netflix) publish their post-mortems publicly — the learning is more valuable than the embarrassment.</div>
    </div>
  </div>
</div>

<!-- ── TOPIC: THE COMPOUND EFFECT IN TECH CAREERS ────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">📈</span>
    <span class="topic-name">The Compound Effect — Small Consistent Actions Build Careers</span>
    <span class="topic-badge">LIFESTYLE • Mindset</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">THE MATH</div>
      <div class="concept-title">Daily Habits at Scale</div>
      <div class="concept-desc">30 minutes of focused learning per day = 182+ hours/year = roughly one college semester of instruction, at your own pace, on exactly what you need. Over 5 years, that's 912 hours. The person who shows up daily for a year beats the person who binge-studies for a week and then burns out.</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">SYSTEMS OVER GOALS</div>
      <div class="concept-title">Build the Habit, Not Just the Target</div>
      <div class="concept-desc">"I want to get my OSCP" is a goal. "I will do one TryHackMe room every weekday" is a system. Goals define direction; systems create movement. When you finish the OSCP, the goal disappears — but the system continues and carries you forward. Focus on building the behavior, not just achieving the outcome.</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">THE PORTFOLIO</div>
      <div class="concept-title">Show Don't Tell</div>
      <div class="concept-desc">Certs prove you studied; a portfolio proves you built. GitHub with real projects — even simple ones — is worth more than a stack of paper certs. What to build:<br>
      • Security tools or scripts you actually use<br>
      • A home lab write-up with what you deployed and why<br>
      • A CTF write-up showing your problem-solving process<br>
      • A blog post explaining something you learned<br>
      Each one is evidence of skill, initiative, and communication.</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">AVOID TUTORIAL HELL</div>
      <div class="concept-title">Stop Watching, Start Building</div>
      <div class="concept-desc">Tutorial hell: you watch video after video feeling like you're learning, but when you sit down to build something, you're lost. Break out by deliberately <strong>stopping tutorials at 50%</strong> and building the rest yourself without guidance. The struggle is the learning. Tolerate not knowing — that discomfort is the feeling of your brain forming new connections.</div>
    </div>
  </div>
</div>
"""


def patch(filepath: str, sentinel: str, inject_content: str, inject_anchor: str):
    path = Path(filepath)
    content = path.read_text(encoding="utf-8")

    if sentinel in content:
        print(f"  [skip] {sentinel} already present in {path.name}")
        return False

    if inject_anchor not in content:
        print(f"  [ERROR] Anchor not found: {inject_anchor!r} in {path.name}")
        return False

    new_content = content.replace(inject_anchor, inject_content + "\n" + inject_anchor)
    path.write_text(new_content, encoding="utf-8")
    added = len(new_content) - len(content)
    print(f"  [ok] Injected {added:+,} chars before {inject_anchor!r} in {path.name}")
    return True


def main():
    target = "index.html"

    results = [
        patch(target, SCRIPT_SENTINEL, SCRIPT_CONTENT, SCRIPT_INJECT_ANCHOR),
        patch(target, NET_SENTINEL,    NET_CONTENT,    NET_INJECT_ANCHOR),
        patch(target, LINUX_SENTINEL,  LINUX_CONTENT,  LINUX_INJECT_ANCHOR),
        patch(target, SEC_SENTINEL,    SEC_CONTENT,    SEC_INJECT_ANCHOR),
        patch(target, LIFE_SENTINEL,   LIFE_CONTENT,   LIFE_INJECT_ANCHOR),
    ]

    if any(results):
        from html.parser import HTMLParser

        class BalanceChecker(HTMLParser):
            VOID = {"area","base","br","col","embed","hr","img","input","link","meta","param","source","track","wbr"}
            def __init__(self):
                super().__init__()
                self.stack = []
                self.strays = []
            def handle_starttag(self, tag, attrs):
                if tag not in self.VOID:
                    self.stack.append(tag)
            def handle_endtag(self, tag):
                if tag in self.VOID:
                    return
                if self.stack and self.stack[-1] == tag:
                    self.stack.pop()
                else:
                    self.strays.append(tag)

        checker = BalanceChecker()
        checker.feed(Path(target).read_text(encoding="utf-8"))
        print(f"\n  Unclosed at EOF: {checker.stack[-5:] if checker.stack else 'NONE'}")
        print(f"  Stray end tags: {len(checker.strays)}")

        new_len = Path(target).stat().st_size
        print(f"\n  {target}: {new_len:,} bytes")


if __name__ == "__main__":
    main()
