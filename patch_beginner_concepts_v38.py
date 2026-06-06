#!/usr/bin/env python3
"""Wave 38 – API security (OAuth2/JWT), container internals, change management, web scraping, certs roadmap."""
from pathlib import Path
from html.parser import HTMLParser

S_SEC      = "<!-- BEGINNER38-SEC v1 -->"
S_LINUX    = "<!-- BEGINNER38-LINUX v1 -->"
S_GRC      = "<!-- BEGINNER38-GRC v1 -->"
S_SCRIPT   = "<!-- BEGINNER38-SCRIPT v1 -->"
S_LIFESTYLE= "<!-- BEGINNER38-LIFESTYLE v1 -->"

A_SEC      = "<!-- /domain-body sec -->"
A_LINUX    = "<!-- /domain-body linux -->"
A_GRC      = "<!-- /domain-body grc -->"
A_SCRIPT   = "<!-- /domain-body script -->"
A_LIFESTYLE= "<!-- /domain-body lifestyle -->"

# ══════════════════════════════════════════════════════════════════════════
# SEC – API security: OAuth2 & JWT
# ══════════════════════════════════════════════════════════════════════════
C_SEC = """
<!-- BEGINNER38-SEC v1 -->
<!-- ── TOPIC: API Security – OAuth2 & JWT ────────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-badge">Beginner</span>
    API Security – OAuth2, JWT &amp; Token-Based Authentication
  </div>
  <div class="topic-body">

    <div class="concept-card">
      <div class="concept-label">Core Concept</div>
      <div class="concept-title">Why Modern APIs Don't Use Passwords Directly</div>
      <div class="concept-desc">
        Imagine giving your house key (password) to every app that needs
        to check your mailbox. If one app is compromised, your whole
        house is at risk. <strong>Token-based authentication</strong>
        solves this: you get a limited, revocable, expiring "guest pass"
        instead of handing out your master key.<br><br>
        <strong>The vocabulary you'll see everywhere:</strong><br>
        &bull; <em>Authentication</em> — "Who are you?" (proving identity).<br>
        &bull; <em>Authorization</em> — "What are you allowed to do?"
          (granting permissions).<br>
        &bull; <em>Token</em> — a piece of data that proves you've already
          authenticated, so you don't have to send your password every
          single request.<br><br>
        <em>"Assume" makes an ass out of you and me</em> — never assume
        "the user is logged in" means "the user is allowed to do this
        specific action." Authentication and authorization are different
        checks — confusing them is the root of A01 (Broken Access Control).
      </div>
    </div>

    <div class="concept-card">
      <div class="concept-label">OAuth2</div>
      <div class="concept-title">OAuth2 – The "Sign in With Google" Flow</div>
      <div class="concept-desc">
        <strong>OAuth2</strong> is the protocol behind every "Sign in
        with Google/GitHub/Microsoft" button. It lets an app access your
        data on another service <em>without ever seeing your password</em>
        for that service.<br><br>
        <strong>Key roles in OAuth2:</strong><br>
        &bull; <em>Resource Owner</em> — you, the user.<br>
        &bull; <em>Client</em> — the app requesting access (e.g. a
          scheduling tool that wants to read your Google Calendar).<br>
        &bull; <em>Authorization Server</em> — issues tokens (e.g. Google's
          login servers).<br>
        &bull; <em>Resource Server</em> — holds your data and checks
          tokens (e.g. the Google Calendar API).
      </div>
      <div class="code-block">
<span class="com">─── The Authorization Code Flow (most common, most secure) ────</span>

1. You click "Sign in with Google" on ScheduleApp
2. ScheduleApp redirects you to Google's login page
   GET https://accounts.google.com/o/oauth2/auth
       ?client_id=schedule_app_123
       &amp;redirect_uri=https://scheduleapp.com/callback
       &amp;scope=calendar.readonly
       &amp;response_type=code

3. You log in to GOOGLE directly (ScheduleApp never sees your password)
4. Google asks: "ScheduleApp wants to read your calendar. Allow?"
5. You click Allow → Google redirects back with a temporary CODE
   https://scheduleapp.com/callback?code=4/0AX4XfWh...

6. ScheduleApp's SERVER (not your browser) exchanges the code for tokens
   POST https://oauth2.googleapis.com/token
       { client_id, client_secret, code, grant_type: "authorization_code" }

7. Google returns:
   {
     "access_token":  "ya29.a0AfH6...",   ← used for API calls, short-lived
     "refresh_token": "1//0gLGn...",      ← used to get new access tokens
     "expires_in": 3600
   }

8. ScheduleApp now calls the Calendar API with the access token —
   never touching your Google password at any point in this process
      </div>
    </div>

    <div class="concept-card">
      <div class="concept-label">JWT</div>
      <div class="concept-title">JWT – JSON Web Tokens Decoded</div>
      <div class="concept-desc">
        A <strong>JWT (JSON Web Token)</strong> is a self-contained,
        signed token — three Base64-encoded parts separated by dots:
        <code>header.payload.signature</code>. The server can verify it's
        legitimate without a database lookup, because the signature
        proves it hasn't been tampered with.
      </div>
      <div class="code-block">
<span class="com"># A JWT looks like this (one long string with two dots):</span>
eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJhbGljZSIsInJvbGUiOiJhZG1pbiJ9.SflKxwRJSMeKKF2QT4f...

<span class="com"># Decoded HEADER (algorithm + token type):</span>
{ <span class="str">"alg"</span>: <span class="str">"HS256"</span>, <span class="str">"typ"</span>: <span class="str">"JWT"</span> }

<span class="com"># Decoded PAYLOAD (claims — the actual data):</span>
{
  <span class="str">"sub"</span>:  <span class="str">"alice"</span>,        <span class="com"># subject = who this token is about</span>
  <span class="str">"role"</span>: <span class="str">"admin"</span>,
  <span class="str">"iat"</span>:  <span class="num">1717689600</span>,    <span class="com"># issued-at timestamp</span>
  <span class="str">"exp"</span>:  <span class="num">1717693200</span>     <span class="com"># expiration timestamp — ALWAYS set this!</span>
}

<span class="com"># SIGNATURE — proves the token wasn't modified</span>
<span class="com"># HMACSHA256(base64(header) + "." + base64(payload), SECRET_KEY)</span>

<span class="com"># Generate and verify with Python (PyJWT)</span>
<span class="kw">import</span> jwt, datetime

token = jwt.encode(
    {<span class="str">"sub"</span>: <span class="str">"alice"</span>, <span class="str">"role"</span>: <span class="str">"admin"</span>,
     <span class="str">"exp"</span>: datetime.datetime.utcnow() + datetime.timedelta(hours=<span class="num">1</span>)},
    <span class="str">"your-secret-key"</span>, algorithm=<span class="str">"HS256"</span>
)

<span class="kw">try</span>:
    payload = jwt.decode(token, <span class="str">"your-secret-key"</span>, algorithms=[<span class="str">"HS256"</span>])
    <span class="fn">print</span>(<span class="str">"Valid token for:"</span>, payload[<span class="str">"sub"</span>])
<span class="kw">except</span> jwt.ExpiredSignatureError:
    <span class="fn">print</span>(<span class="str">"Token expired — request a new one"</span>)
<span class="kw">except</span> jwt.InvalidTokenError:
    <span class="fn">print</span>(<span class="str">"Invalid token — reject the request"</span>)
      </div>
    </div>

    <div class="concept-card">
      <div class="concept-label">Common Mistakes</div>
      <div class="concept-title">JWT &amp; Token Pitfalls That Cause Breaches</div>
      <div class="concept-desc">
        <em>"Not my circus, not my monkey"</em> — but if you're reviewing
        someone else's API design, these are the red flags worth raising
        immediately:<br><br>
        &bull; <strong>"alg: none" attack</strong> — some JWT libraries
          will accept tokens with no signature if you ask nicely.
          Always explicitly specify allowed algorithms when verifying.<br>
        &bull; <strong>Storing JWTs in localStorage</strong> — accessible
          to any JavaScript on the page (XSS risk). HttpOnly cookies
          are safer for session tokens.<br>
        &bull; <strong>No expiration</strong> — a stolen token that never
          expires is a permanent backdoor. Always set <code>exp</code>,
          and keep access tokens short-lived (minutes to hours).<br>
        &bull; <strong>Sensitive data in the payload</strong> — JWT
          payloads are Base64-encoded, NOT encrypted. Anyone can decode
          and read them. Never put passwords or secrets in a JWT.<br>
        &bull; <strong>No revocation strategy</strong> — once issued, a
          JWT is valid until it expires. Plan for "I need to log this
          user out everywhere right now" (e.g. short expiry + refresh
          token blocklist).
      </div>
    </div>

  </div>
</div>
"""

# ══════════════════════════════════════════════════════════════════════════
# LINUX – Container internals: cgroups & namespaces
# ══════════════════════════════════════════════════════════════════════════
C_LINUX = """
<!-- BEGINNER38-LINUX v1 -->
<!-- ── TOPIC: Container Internals – cgroups & Namespaces ─────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-badge">Intermediate</span>
    Container Internals – What Docker Is Actually Built From
  </div>
  <div class="topic-body">

    <div class="concept-card">
      <div class="concept-label">Core Concept</div>
      <div class="concept-title">Containers Are Not Magic — They're Linux Features</div>
      <div class="concept-desc">
        Here's the secret that demystifies Docker: <strong>"containers"
        aren't a real thing in the Linux kernel.</strong> Docker (and
        Podman, containerd, etc.) is really just a friendly interface
        around two much older Linux kernel features:<br><br>
        &bull; <strong>Namespaces</strong> — make a process think it's
          alone on the system (its own PIDs, network, filesystem,
          hostname).<br>
        &bull; <strong>cgroups (control groups)</strong> — limit and
          measure how much CPU, memory, and I/O a process (or group of
          processes) can use.<br><br>
        Put these two together — a process that can't see anything
        outside its bubble (namespaces) and can't consume more than its
        allotted resources (cgroups) — and you have a "container."<br><br>
        Understanding this helps you debug containers like Linux
        processes (because that's exactly what they are) and explains
        why container escapes are possible — they exploit gaps in this
        kernel-level isolation.
      </div>
    </div>

    <div class="concept-card">
      <div class="concept-label">Namespaces</div>
      <div class="concept-title">The Six Linux Namespace Types</div>
      <div class="concept-desc">
        Each namespace type isolates a different slice of what a process
        can see:
      </div>
      <div class="code-block">
<span class="com">Namespace   What it isolates                     What this means for a container</span>
PID         Process IDs                          Container's PID 1 looks like the
                                                  only process on the system
NET         Network interfaces, routes, ports    Container has its own IP, can't
                                                  see the host's network traffic
MNT         Filesystem mount points              Container sees its own root
                                                  filesystem, not the host's
UTS         Hostname and domain name             Container can have its own
                                                  hostname (e.g. "web-7d9f8c")
IPC         Inter-process communication          Container can't access host's
            (shared memory, semaphores)           shared memory segments
USER        User and group IDs                   "root" inside the container can
                                                  map to an unprivileged host user

<span class="com"># See the namespaces of a running process</span>
ls -la /proc/$(pgrep -f myapp | head -1)/ns/

<span class="com"># Output looks like:</span>
<span class="com"># lrwxrwxrwx ... net  -&gt; 'net:[4026532245]'</span>
<span class="com"># lrwxrwxrwx ... pid  -&gt; 'pid:[4026532248]'</span>
<span class="com"># lrwxrwxrwx ... uts  -&gt; 'uts:[4026532246]'</span>

<span class="com"># Compare to the host's own namespaces (PID 1)</span>
ls -la /proc/1/ns/
<span class="com"># Different numbers = different namespace = isolated</span>

<span class="com"># Run your own minimal "container" with unshare (no Docker needed!)</span>
sudo unshare --pid --net --mount --uts --fork bash
hostname my-fake-container       <span class="com"># changes hostname ONLY inside this shell</span>
ps aux                           <span class="com"># shows almost nothing — your own PID namespace</span>
      </div>
    </div>

    <div class="concept-card">
      <div class="concept-label">cgroups</div>
      <div class="concept-title">cgroups – Resource Limits in Action</div>
      <div class="concept-desc">
        cgroups are how Docker enforces <code>--memory=512m</code> and
        <code>--cpus=1</code>. They live in a virtual filesystem you can
        explore directly.
      </div>
      <div class="code-block">
<span class="com"># Find a container's cgroup (modern systems use cgroup v2)</span>
docker inspect --format '{{.Id}}' myapp_container

<span class="com"># Explore its resource limits directly in the filesystem</span>
cd /sys/fs/cgroup/system.slice/docker-&lt;container-id&gt;.scope/

cat memory.max          <span class="com"># memory limit in bytes (or "max" = unlimited)</span>
cat memory.current      <span class="com"># current memory usage RIGHT NOW</span>
cat cpu.max             <span class="com"># CPU quota and period</span>
cat io.stat             <span class="com"># disk I/O statistics</span>

<span class="com"># Watch a container's resource consumption live</span>
docker stats myapp_container

<span class="com"># Create your own cgroup limit manually (educational — Docker</span>
<span class="com"># does this automatically, but seeing it raw removes the mystery)</span>
sudo mkdir /sys/fs/cgroup/my_limited_group
echo "100000 100000" | sudo tee /sys/fs/cgroup/my_limited_group/cpu.max
echo $$ | sudo tee /sys/fs/cgroup/my_limited_group/cgroup.procs
<span class="com"># Now THIS SHELL is limited to 100% of one CPU core</span>
      </div>
    </div>

    <div class="concept-card">
      <div class="concept-label">Why It Matters</div>
      <div class="concept-title">Using This Knowledge to Debug Real Problems</div>
      <div class="concept-desc">
        <em>You can't make someone make the right choice, yet you can pick
        up the pieces afterwards</em> — when a container mysteriously
        gets killed or throttled, knowing the internals turns "it's
        broken, restart it" into "I found exactly why, here's the fix":<br><br>
        &bull; <strong>"My container keeps getting OOM-killed"</strong> →
          Check <code>memory.current</code> vs <code>memory.max</code> —
          the cgroup is enforcing a limit you set too low.<br>
        &bull; <strong>"My container is randomly slow"</strong> →
          Check <code>cpu.max</code> — CPU throttling from cgroup limits
          looks exactly like random slowness from the inside.<br>
        &bull; <strong>"Processes inside my container can see host
          processes"</strong> → The container may be running with
          <code>--pid=host</code> — a misconfiguration that breaks PID
          namespace isolation (and is a security risk).<br>
        &bull; <strong>"I need to debug a container that has no shell"</strong>
          → Use <code>nsenter</code> to attach to its namespaces directly
          from the host: <code>nsenter -t &lt;PID&gt; -n -p -m sh</code>
      </div>
    </div>

  </div>
</div>
"""

# ══════════════════════════════════════════════════════════════════════════
# GRC – Change management process
# ══════════════════════════════════════════════════════════════════════════
C_GRC = """
<!-- BEGINNER38-GRC v1 -->
<!-- ── TOPIC: Change Management Process ──────────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-badge">Beginner</span>
    Change Management – The Process That Prevents Self-Inflicted Outages
  </div>
  <div class="topic-body">

    <div class="concept-card">
      <div class="concept-label">Core Concept</div>
      <div class="concept-title">Why Changes Need a Process At All</div>
      <div class="concept-desc">
        Here's an uncomfortable truth backed by years of incident data:
        <strong>most outages are caused by changes someone made on
        purpose</strong> — not by mysterious external forces. A
        <strong>Change Management</strong> process exists to catch the
        problems with a change <em>before</em> it goes live, not after.<br><br>
        It is NOT bureaucracy for its own sake (though badly run change
        processes can feel that way). Done well, it answers four
        questions before anything happens:<br>
        1. What exactly is changing?<br>
        2. Why are we changing it?<br>
        3. What could go wrong, and how do we know if it does?<br>
        4. How do we undo it if it goes wrong?<br><br>
        <em>"Assume" makes an ass out of you and me</em> — "this is a
        small change, it'll be fine" is the most expensive sentence in IT.
        Small changes cause some of the largest outages on record.
      </div>
    </div>

    <div class="concept-card">
      <div class="concept-label">Change Types</div>
      <div class="concept-title">Standard, Normal, and Emergency Changes</div>
      <div class="concept-desc">
        Mature change processes don't treat every change the same way —
        that would make trivial changes painfully slow AND make urgent
        fixes dangerously slow. Three tiers balance speed and safety:
      </div>
      <div class="code-block">
<span class="com">STANDARD CHANGE</span>
  Definition: Pre-approved, low-risk, repeatable, well-understood
  Examples:   Routine OS patching on a schedule, adding a DNS record
              for a new subdomain, rotating a credential per the runbook
  Process:    Pre-approved template → just execute and log it

<span class="com">NORMAL CHANGE</span>
  Definition: Has some risk; needs review before approval
  Examples:   Database schema migration, firewall rule change,
              new application deployment, infrastructure resize
  Process:    Submit a Change Request (CR) → Change Advisory Board (CAB)
              reviews → approved/rejected/needs-more-info → scheduled
              → executed → reviewed afterward

<span class="com">EMERGENCY CHANGE</span>
  Definition: Urgent fix needed RIGHT NOW to resolve an active incident
  Examples:   Blocking an active attacker's IP, rolling back a deploy
              that's causing an outage, restarting a critical service
  Process:    Verbal/expedited approval from on-call lead → execute
              immediately → FULL documentation and review afterward
              (the paperwork happens AFTER the fire is out, not during)
      </div>
    </div>

    <div class="concept-card">
      <div class="concept-label">Anatomy of a CR</div>
      <div class="concept-title">What Goes In a Good Change Request</div>
      <div class="concept-desc">
        A well-written change request makes the reviewer's job easy and
        protects you if something goes wrong — it's your evidence that
        you thought it through.
      </div>
      <div class="code-block">
<span class="com">CHANGE REQUEST: CR-2026-0614</span>
─────────────────────────────────────────────────────────
Title:           Upgrade PostgreSQL from 14.x to 16.x on prod-db-01
Requested by:    Alice Chen          Date: 2026-06-06
Risk level:      Medium
Scheduled for:   Saturday 2026-06-13, 02:00-04:00 (lowest traffic window)

WHAT is changing:
  Major version upgrade of the primary application database

WHY:
  PostgreSQL 14 reaches end-of-life in 6 months; 16.x brings
  performance improvements our reporting queries need

HOW (step by step):
  1. Take a verified full backup (pg_dump) and snapshot
  2. Stop application writes (maintenance mode)
  3. Run pg_upgrade following documented runbook RB-114
  4. Run validation query suite (see attached script)
  5. Resume application traffic; monitor for 30 minutes

ROLLBACK PLAN:
  Restore from pre-change snapshot (tested rollback time: ~12 minutes)
  Rollback decision point: any validation query failure, or >5 min
  of unexpected errors post-cutover

TESTING DONE:
  Successfully performed in staging on 2026-05-30 (see CR-2026-0589)

IMPACT IF THIS GOES WRONG:
  Up to 2 hours of read-only mode for customers; no data loss expected
  given backup/snapshot strategy

APPROVERS NEEDED:
  Database team lead, on-call SRE, Engineering manager
      </div>
    </div>

    <div class="concept-card">
      <div class="concept-label">Culture</div>
      <div class="concept-title">Making Change Management Work, Not Just Exist</div>
      <div class="concept-desc">
        <em>"Not my circus, not my monkey"</em> — if your organisation's
        change process feels like pointless paperwork, that's a sign
        the process needs fixing, not that the goal is wrong. Healthy
        change management:<br><br>
        &bull; <strong>Scales with risk</strong> — a one-line config typo
          fix shouldn't require the same ceremony as a database migration.<br>
        &bull; <strong>Makes the safe path the easy path</strong> — if
          following the process is harder than skipping it, people will
          skip it (quietly, which is worse).<br>
        &bull; <strong>Reviews without blame</strong> — when a properly
          reviewed change still causes an issue, that's a process
          improvement opportunity, not a personal failure.<br><br>
        <em>You can't make someone make the right choice, yet you can pick
        up the pieces afterwards</em> — and a good change record is
        exactly what lets you pick up those pieces fast: you know
        precisely what changed, when, why, and how to undo it. That
        turns a 4-hour outage into a 10-minute rollback.
      </div>
    </div>

  </div>
</div>
"""

# ══════════════════════════════════════════════════════════════════════════
# SCRIPT – Web scraping with Python
# ══════════════════════════════════════════════════════════════════════════
C_SCRIPT = """
<!-- BEGINNER38-SCRIPT v1 -->
<!-- ── TOPIC: Web Scraping with Python ───────────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-badge">Beginner</span>
    Web Scraping – Extracting Data from Websites with Python
  </div>
  <div class="topic-body">

    <div class="concept-card">
      <div class="concept-label">Core Concept</div>
      <div class="concept-title">What Web Scraping Is — and Isn't</div>
      <div class="concept-desc">
        <strong>Web scraping</strong> is writing code that downloads web
        pages and extracts structured data from them — prices, articles,
        contact info, statistics — instead of copying and pasting by hand.<br><br>
        <strong>Before you scrape anything:</strong><br>
        &bull; Check the site's <code>robots.txt</code>
          (<code>example.com/robots.txt</code>) — it states which parts
          the site owner permits automated tools to access.<br>
        &bull; Read the Terms of Service — many sites explicitly prohibit
          scraping; violating ToS can have legal consequences.<br>
        &bull; Prefer an official API if one exists — it's faster, more
          stable, and explicitly sanctioned.<br><br>
        <em>"Not my circus, not my monkey"</em> — scraping a site against
        its wishes makes their problem (server load, legal risk) your
        problem too. When in doubt, ask permission or use the API.
      </div>
    </div>

    <div class="concept-card">
      <div class="concept-label">Static Pages</div>
      <div class="concept-title">Scraping Static HTML with requests + BeautifulSoup</div>
      <div class="concept-desc">
        Most simple pages can be scraped with two libraries:
        <code>requests</code> downloads the page; <code>BeautifulSoup</code>
        parses the HTML into something you can search.
      </div>
      <div class="code-block">
<span class="com"># pip install requests beautifulsoup4</span>
<span class="kw">import</span> requests
<span class="kw">from</span> bs4 <span class="kw">import</span> BeautifulSoup
<span class="kw">import</span> time

HEADERS = {<span class="str">"User-Agent"</span>: <span class="str">"MyResearchBot/1.0 (contact: alice@example.com)"</span>}
<span class="com"># Identify yourself! Anonymous scrapers get blocked faster, and</span>
<span class="com"># a contact email lets site owners reach you instead of just banning you.</span>

resp = requests.get(<span class="str">"https://example.com/articles"</span>, headers=HEADERS, timeout=<span class="num">10</span>)
resp.raise_for_status()              <span class="com"># raises an exception on 4xx/5xx errors</span>

soup = BeautifulSoup(resp.text, <span class="str">"html.parser"</span>)

<span class="com"># Find elements by tag, class, or CSS selector</span>
<span class="kw">for</span> article <span class="kw">in</span> soup.select(<span class="str">"article.post"</span>):
    title = article.select_one(<span class="str">"h2.title"</span>)
    link  = article.select_one(<span class="str">"a"</span>)
    <span class="kw">if</span> title <span class="kw">and</span> link:
        <span class="fn">print</span>(title.get_text(strip=<span class="kw">True</span>), <span class="str">"-&gt;"</span>, link[<span class="str">"href"</span>])

    time.sleep(<span class="num">1</span>)   <span class="com"># BE POLITE — don't hammer their server</span>

<span class="com"># Common selector patterns:</span>
<span class="com"># soup.find("h1")                    -- first &lt;h1&gt; tag</span>
<span class="com"># soup.find_all("a", class_="link")  -- all &lt;a class="link"&gt; tags</span>
<span class="com"># soup.select("div#main &gt; p")        -- CSS selector syntax</span>
      </div>
    </div>

    <div class="concept-card">
      <div class="concept-label">Dynamic Pages</div>
      <div class="concept-title">Scraping JavaScript-Rendered Pages with Playwright</div>
      <div class="concept-desc">
        Many modern sites load content with JavaScript <em>after</em> the
        initial page loads — <code>requests</code> only sees the empty
        shell. <strong>Playwright</strong> drives a real browser, so it
        sees the page exactly as a human would.
      </div>
      <div class="code-block">
<span class="com"># pip install playwright &amp;&amp; playwright install chromium</span>
<span class="kw">from</span> playwright.sync_api <span class="kw">import</span> sync_playwright

<span class="kw">with</span> sync_playwright() <span class="kw">as</span> p:
    browser = p.chromium.launch(headless=<span class="kw">True</span>)
    page    = browser.new_page()
    page.goto(<span class="str">"https://example.com/dashboard"</span>, wait_until=<span class="str">"networkidle"</span>)

    <span class="com"># Wait for a specific element to appear (handles slow-loading content)</span>
    page.wait_for_selector(<span class="str">".data-table"</span>, timeout=<span class="num">10000</span>)

    <span class="com"># Extract text from rendered elements</span>
    rows = page.query_selector_all(<span class="str">".data-table tr"</span>)
    <span class="kw">for</span> row <span class="kw">in</span> rows:
        cells = row.query_selector_all(<span class="str">"td"</span>)
        <span class="fn">print</span>([c.inner_text() <span class="kw">for</span> c <span class="kw">in</span> cells])

    <span class="com"># Take a screenshot for debugging — invaluable when scrapers break</span>
    page.screenshot(path=<span class="str">"debug.png"</span>, full_page=<span class="kw">True</span>)

    browser.close()
      </div>
    </div>

    <div class="concept-card">
      <div class="concept-label">Best Practices</div>
      <div class="concept-title">Writing Scrapers That Don't Get You Banned</div>
      <div class="concept-desc">
        <em>"Assume" makes an ass out of you and me</em> — never assume
        a scraper that worked yesterday will work today; sites change
        their layout, add anti-bot measures, and update their ToS.<br><br>
        &bull; <strong>Respect rate limits</strong> — add delays
          (<code>time.sleep()</code>) between requests; consider the
          <code>Crawl-delay</code> directive in robots.txt.<br>
        &bull; <strong>Cache responses</strong> — don't re-download pages
          you already have; save to disk during development.<br>
        &bull; <strong>Handle failures gracefully</strong> — wrap requests
          in try/except; sites go down, layouts change, connections drop.<br>
        &bull; <strong>Use sessions for login-required sites</strong> —
          <code>requests.Session()</code> persists cookies across requests.<br>
        &bull; <strong>Monitor for layout changes</strong> — add assertions
          that fail loudly ("expected 10 columns, found 3 — site layout
          probably changed") rather than silently returning garbage data.<br><br>
        <em>You can't make someone make the right choice, yet you can pick
        up the pieces afterwards</em> — when a target site changes its
        HTML and your scraper starts returning empty results, good
        logging and alerting mean you find out in minutes, not when
        someone notices the dashboard is empty three weeks later.
      </div>
    </div>

  </div>
</div>
"""

# ══════════════════════════════════════════════════════════════════════════
# LIFESTYLE – IT certification roadmap
# ══════════════════════════════════════════════════════════════════════════
C_LIFESTYLE = """
<!-- BEGINNER38-LIFESTYLE v1 -->
<!-- ── TOPIC: IT Certification Roadmap ───────────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-badge">Beginner</span>
    Certification Roadmap – Charting a Path Through the Alphabet Soup
  </div>
  <div class="topic-body">

    <div class="concept-card">
      <div class="concept-label">Core Concept</div>
      <div class="concept-title">What Certifications Actually Do For You</div>
      <div class="concept-desc">
        Certifications are not magic keys that open doors by themselves —
        but they do three concrete things:<br><br>
        1. <strong>Get your resume past automated filters</strong> — many
           companies' applicant tracking systems literally search for
           certification keywords.<br>
        2. <strong>Give you a structured syllabus</strong> — studying for
           a cert forces you to learn breadth you might otherwise skip.<br>
        3. <strong>Signal commitment</strong> — passing a hard exam shows
           you can set a goal and follow through, which matters as much
           as the content itself.<br><br>
        <em>"Assume" makes an ass out of you and me</em> — don't assume
        a certification alone gets you the job. Pair it with hands-on
        proof (home lab projects, GitHub repos, write-ups) — that
        combination is what actually gets you hired.
      </div>
    </div>

    <div class="concept-card">
      <div class="concept-label">Foundational</div>
      <div class="concept-title">Tier 1 — Entry-Level Certifications (Start Here)</div>
      <div class="concept-desc">
        These build the broad foundation this entire guide is structured
        around. Most people new to IT should start with one of these:
      </div>
      <div class="code-block">
<span class="com">Certification          Domain            Why start here</span>
CompTIA A+             IT fundamentals   Hardware, OS, troubleshooting basics —
                                         the classic "first cert" for helpdesk
CompTIA Network+       Networking        TCP/IP, subnetting, devices, protocols —
                                         pairs perfectly with this guide's net domain
CompTIA Security+      Security          Widely required for government/defense
                                         contractor jobs (DoD 8570 baseline)
Google IT Support      IT fundamentals   Free on Coursera; project-based,
Professional Cert                        beginner-friendly, includes a portfolio
AWS Cloud Practitioner Cloud             Non-technical intro to AWS — good for
                                         anyone, technical or not, entering cloud

<span class="com"># Recommended starting combo for a brand-new IT career:</span>
<span class="com"># A+ → Network+ → Security+ → (then branch toward your specialty)</span>
      </div>
    </div>

    <div class="concept-card">
      <div class="concept-label">Specialization</div>
      <div class="concept-title">Tier 2 — Picking a Specialty Track</div>
      <div class="concept-desc">
        Once the fundamentals are solid, branch toward the area that
        excites you most — this guide's domain structure maps directly
        onto these tracks:
      </div>
      <div class="code-block">
<span class="com">If you enjoyed...   →  Consider this track  →  Certifications to target</span>

net domain          →  Networking            →  Cisco CCNA, Juniper JNCIA
sec/threat domains  →  Security Analyst/SOC  →  CompTIA CySA+, Blue Team Level 1
pentest domain      →  Offensive Security     →  eJPT, PNPT, OSCP (advanced)
linux domain        →  Systems Admin          →  RHCSA, LFCS (Linux Foundation)
ops domain          →  Cloud/DevOps           →  AWS SAA, Azure Administrator,
                                                  Certified Kubernetes Admin (CKA)
ai domain           →  Data/ML Engineering    →  AWS ML Specialty, TensorFlow Cert
grc domain          →  Governance/Compliance  →  CISA, CRISC, ISO 27001 Lead Auditor
                       (usually needs experience first — these are mid-career certs)
      </div>
    </div>

    <div class="concept-card">
      <div class="concept-label">Study Strategy</div>
      <div class="concept-title">How to Actually Pass (Not Just Study)</div>
      <div class="concept-desc">
        <em>"Not my circus, not my monkey"</em> — don't get pulled into
        certification debates online ("is X cert worth it?" threads are
        endless and rarely conclusive). Pick one aligned with your goals
        and commit.<br><br>
        <strong>A study approach that actually works:</strong><br>
        1. <strong>Get the official exam objectives</strong> — they tell
           you exactly what will be tested, often down to the percentage
           weight of each topic.<br>
        2. <strong>Build something related to each major topic</strong> —
           reading about subnetting is forgettable; calculating subnets
           for your home lab sticks.<br>
        3. <strong>Use practice exams from reputable sources</strong> —
           they reveal gaps and build the stamina for a 90-180 minute
           test under pressure.<br>
        4. <strong>Schedule the exam date early</strong> — a deadline on
           the calendar turns "someday" into "by March 15th."<br><br>
        <em>You can't make someone make the right choice, yet you can pick
        up the pieces afterwards</em> — if you fail an exam, that's data,
        not a verdict on your ability. Review what you missed, study that
        specific gap, and schedule a retake. Plenty of senior engineers
        have a "failed it the first time" story in their past.
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
    (A_LINUX,     S_LINUX,     C_LINUX),
    (A_GRC,       S_GRC,       C_GRC),
    (A_SCRIPT,    S_SCRIPT,    C_SCRIPT),
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
