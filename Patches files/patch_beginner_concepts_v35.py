#!/usr/bin/env python3
"""Wave 35 – CI/CD pipelines, social engineering defense, BCP/DR, regex mastery, leadership."""
from pathlib import Path
from html.parser import HTMLParser

S_OPS      = "<!-- BEGINNER35-OPS v1 -->"
S_SEC      = "<!-- BEGINNER35-SEC v1 -->"
S_GRC      = "<!-- BEGINNER35-GRC v1 -->"
S_SCRIPT   = "<!-- BEGINNER35-SCRIPT v1 -->"
S_MILITARY = "<!-- BEGINNER35-MILITARY v1 -->"

A_OPS      = "<!-- /domain-body ops -->"
A_SEC      = "<!-- /domain-body sec -->"
A_GRC      = "<!-- /domain-body grc -->"
A_SCRIPT   = "<!-- /domain-body script -->"
A_MILITARY = "<!-- /domain-body military -->"

# ══════════════════════════════════════════════════════════════════════════
# OPS – CI/CD pipeline fundamentals
# ══════════════════════════════════════════════════════════════════════════
C_OPS = """
<!-- BEGINNER35-OPS v1 -->
<!-- ── TOPIC: CI/CD Pipeline Fundamentals ────────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-badge">Beginner</span>
    CI/CD Pipelines – From Commit to Production Automatically
  </div>
  <div class="topic-body">

    <div class="concept-card">
      <div class="concept-label">Core Concept</div>
      <div class="concept-title">What CI/CD Actually Means</div>
      <div class="concept-desc">
        <strong>Continuous Integration (CI)</strong> — every code change is
        automatically built and tested the moment it's pushed. Catches bugs
        within minutes instead of weeks.<br><br>
        <strong>Continuous Delivery (CD)</strong> — every change that passes
        CI is automatically packaged and ready to deploy (a human clicks
        "go").<br><br>
        <strong>Continuous Deployment</strong> — every change that passes CI
        is automatically deployed to production with no human in the loop.<br><br>
        <strong>The pipeline stages (typical order):</strong><br>
        1. Checkout code → 2. Install dependencies → 3. Lint/static analysis
        → 4. Unit tests → 5. Build artifact (binary, container image) →
        6. Integration tests → 7. Security scan → 8. Deploy to staging →
        9. Smoke tests → 10. Deploy to production.<br><br>
        <em>"Not my circus, not my monkey"</em> — if your pipeline is red,
        do not merge more changes on top of it. Fix the pipeline first;
        a broken main branch blocks everyone.
      </div>
    </div>

    <div class="concept-card">
      <div class="concept-label">GitHub Actions</div>
      <div class="concept-title">A Real CI/CD Pipeline in YAML</div>
      <div class="concept-desc">
        GitHub Actions is one of the most common CI/CD tools — config
        lives in <code>.github/workflows/*.yml</code> right alongside your
        code.
      </div>
      <div class="code-block">
<span class="com"># .github/workflows/ci.yml</span>
name: CI Pipeline

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: <span class="str">"3.12"</span>

      - name: Install dependencies
        run: pip install -r requirements.txt -r requirements-dev.txt

      - name: Lint
        run: ruff check .

      - name: Run tests with coverage
        run: pytest --cov=src --cov-report=xml --cov-fail-under=<span class="num">80</span>

      - name: Security scan
        run: |
          pip install bandit
          bandit -r src/ -ll

  build-and-push:
    needs: test               <span class="com"># only runs if 'test' job passes</span>
    runs-on: ubuntu-latest
    if: github.ref == <span class="str">'refs/heads/main'</span>
    steps:
      - uses: actions/checkout@v4
      - name: Build container image
        run: docker build -t myapp:${{ github.sha }} .
      - name: Scan image
        run: trivy image --exit-code 1 --severity CRITICAL myapp:${{ github.sha }}
      - name: Push to registry
        run: |
          echo ${{ secrets.REGISTRY_TOKEN }} | docker login -u user --password-stdin
          docker push myapp:${{ github.sha }}
      </div>
    </div>

    <div class="concept-card">
      <div class="concept-label">Deployment Strategies</div>
      <div class="concept-title">How to Ship Without Breaking Things</div>
      <div class="concept-desc">
        How you roll out a new version matters as much as the code itself:<br><br>
        &bull; <strong>Rolling update</strong> — replace instances one at a
          time; if health checks fail, stop and roll back. Default in
          Kubernetes.<br>
        &bull; <strong>Blue-green deployment</strong> — run two identical
          environments ("blue" = current, "green" = new); switch traffic
          instantly; instant rollback by switching back.<br>
        &bull; <strong>Canary release</strong> — send 5% of traffic to the
          new version, watch metrics, gradually increase to 100% (or roll
          back if errors spike).<br>
        &bull; <strong>Feature flags</strong> — deploy code "dark" (disabled),
          then turn it on for specific users without a new deployment.<br><br>
        <em>"Assume" makes an ass out of you and me</em> — never assume a
        deploy "should be fine" because it worked in staging. Staging never
        perfectly mirrors production load, data, and integrations.
      </div>
    </div>

    <div class="concept-card">
      <div class="concept-label">Failure Recovery</div>
      <div class="concept-title">When the Pipeline Ships a Bad Release</div>
      <div class="concept-desc">
        <em>You can't make someone make the right choice, yet you can pick
        up the pieces afterwards</em> — a teammate's bad commit will reach
        production eventually. Your safety net matters more than
        prevention alone.<br><br>
        <strong>Build these into every pipeline:</strong><br>
        &bull; <strong>Automated rollback</strong> — if health checks fail
          post-deploy, automatically revert to the last known-good version.<br>
        &bull; <strong>Deployment markers</strong> — send an event to your
          monitoring system on every deploy, so spikes can be correlated
          instantly: "errors started 90 seconds after deploy #4521."<br>
        &bull; <strong>Fast rollback path</strong> — rolling back should
          take seconds, not the same time as a forward deploy.<br>
        &bull; <strong>Post-incident review</strong> — every bad release
          gets a blameless writeup: what broke, why CI didn't catch it,
          what test or gate would have.
      </div>
    </div>

  </div>
</div>
"""

# ══════════════════════════════════════════════════════════════════════════
# SEC – Social engineering & phishing defense
# ══════════════════════════════════════════════════════════════════════════
C_SEC = """
<!-- BEGINNER35-SEC v1 -->
<!-- ── TOPIC: Social Engineering & Phishing Defense ──────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-badge">Beginner</span>
    Social Engineering – Defending the Human Layer
  </div>
  <div class="topic-body">

    <div class="concept-card">
      <div class="concept-label">Core Concept</div>
      <div class="concept-title">Why Humans Are the Top Attack Vector</div>
      <div class="concept-desc">
        Firewalls and encryption don't stop an attacker who simply
        <em>asks nicely</em>. <strong>Social engineering</strong> exploits
        human psychology — trust, urgency, fear, helpfulness, curiosity —
        to bypass technical controls entirely. Roughly 80%+ of breaches
        start with some form of human manipulation.<br><br>
        <strong>The psychological levers attackers pull:</strong><br>
        &bull; <em>Authority</em> — "This is the CEO; I need this done now."<br>
        &bull; <em>Urgency</em> — "Your account will be locked in 1 hour."<br>
        &bull; <em>Fear</em> — "Suspicious activity detected on your account."<br>
        &bull; <em>Curiosity</em> — "See who viewed your profile" links.<br>
        &bull; <em>Helpfulness</em> — "I'm locked out, can you let me in?"<br><br>
        <em>"Assume" makes an ass out of you and me</em> — never assume a
        message is legitimate because it looks official, knows your name,
        or comes from someone you recognise. Verify through a second channel.
      </div>
    </div>

    <div class="concept-card">
      <div class="concept-label">Phishing Types</div>
      <div class="concept-title">Phishing, Spear Phishing, Vishing, Smishing</div>
      <div class="concept-desc">
        Modern phishing comes in many flavours — knowing the names helps
        you train others and write better detection rules.
      </div>
      <div class="code-block">
<span class="com">Type            Channel       Description</span>
Phishing        Email         Mass email to many targets, generic content
Spear phishing  Email         Targeted, personalised — uses real names/projects
Whaling         Email         Spear phishing aimed at executives (CEO/CFO)
Vishing         Phone/voice   Caller impersonates IT support, bank, vendor
Smishing        SMS/text      "Your package couldn't be delivered, click here"
Quishing        QR code       Malicious QR codes on posters, parking meters, emails
Pretexting      Any           Attacker invents a scenario to extract info
                              ("I'm from Acme Audit, I need your employee list")
Watering hole   Web           Attacker compromises a site the target visits often
Business Email  Email         Impersonates a vendor/exec to redirect payments
Compromise (BEC)              ("Update our bank details for the next invoice")

<span class="com"># Quick red-flag checklist for suspicious emails:</span>
<span class="com"># [ ] Sender domain slightly misspelled (paypa1.com, micros0ft.com)</span>
<span class="com"># [ ] Generic greeting ("Dear Customer") on a "personal" message</span>
<span class="com"># [ ] Urgency or threat language ("act now or lose access")</span>
<span class="com"># [ ] Hover over links — does the URL match the displayed text?</span>
<span class="com"># [ ] Unexpected attachment (.exe, .zip, .html, macro-enabled .docm)</span>
<span class="com"># [ ] Request to bypass normal process ("don't tell finance, just wire it")</span>
      </div>
    </div>

    <div class="concept-card">
      <div class="concept-label">Technical Controls</div>
      <div class="concept-title">Email Authentication: SPF, DKIM, DMARC</div>
      <div class="concept-desc">
        These three DNS-based protocols work together to stop attackers
        from spoofing your domain in phishing emails:<br><br>
        &bull; <strong>SPF (Sender Policy Framework)</strong> — a DNS TXT
          record listing which mail servers are allowed to send for your
          domain.<br>
        &bull; <strong>DKIM (DomainKeys Identified Mail)</strong> —
          cryptographically signs outgoing emails so receivers can verify
          they weren't altered in transit.<br>
        &bull; <strong>DMARC (Domain-based Message Authentication)</strong>
          — tells receiving servers what to do when SPF/DKIM checks fail
          (quarantine, reject) and where to send reports.
      </div>
      <div class="code-block">
<span class="com"># SPF record — only these servers may send as @example.com</span>
example.com.  TXT  "v=spf1 include:_spf.google.com include:sendgrid.net -all"
<span class="com"># -all = hard fail anything not listed (strict)</span>
<span class="com"># ~all = soft fail (mark as suspicious but still deliver)</span>

<span class="com"># DKIM record — public key for verifying signatures</span>
google._domainkey.example.com.  TXT  "v=DKIM1; k=rsa; p=MIGfMA0GCSq..."

<span class="com"># DMARC record — policy + reporting address</span>
_dmarc.example.com.  TXT  "v=DMARC1; p=quarantine; rua=mailto:dmarc-reports@example.com; pct=100"
<span class="com"># p=none       → monitor only (start here)</span>
<span class="com"># p=quarantine → send failures to spam folder</span>
<span class="com"># p=reject     → block failures outright (end goal)</span>

<span class="com"># Check your domain's current posture</span>
dig example.com TXT | grep spf
dig _dmarc.example.com TXT
      </div>
    </div>

    <div class="concept-card">
      <div class="concept-label">Human Layer</div>
      <div class="concept-title">Building a Phishing-Resilient Culture</div>
      <div class="concept-desc">
        <em>You can't make someone make the right choice, yet you can pick
        up the pieces afterwards</em> — and you can also stack the deck so
        the right choice is the easy choice:<br><br>
        &bull; Run <strong>regular phishing simulations</strong> — not to
          punish people who click, but to identify training needs.<br>
        &bull; Make reporting <strong>one click away</strong> — a
          "Report Phishing" button in the mail client beats a confusing
          forward-to-security process.<br>
        &bull; <strong>Never punish someone for reporting</strong> a real
          click — punishment teaches people to hide mistakes, which is
          the worst outcome for security.<br>
        &bull; Establish a <strong>verbal verification process</strong> for
          financial requests: "any wire transfer change requires a phone
          call to a known number — no exceptions, regardless of who's asking."<br>
        &bull; Celebrate good catches publicly — "Maria caught a spear
          phishing attempt this week" builds a security-positive culture.
      </div>
    </div>

  </div>
</div>
"""

# ══════════════════════════════════════════════════════════════════════════
# GRC – Business Continuity & Disaster Recovery Planning
# ══════════════════════════════════════════════════════════════════════════
C_GRC = """
<!-- BEGINNER35-GRC v1 -->
<!-- ── TOPIC: Business Continuity & Disaster Recovery ────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-badge">Beginner</span>
    BCP &amp; DR – Planning for the Day Everything Goes Wrong
  </div>
  <div class="topic-body">

    <div class="concept-card">
      <div class="concept-label">Core Concept</div>
      <div class="concept-title">BCP vs DR – Two Halves of Resilience</div>
      <div class="concept-desc">
        These terms are often confused but answer different questions:<br><br>
        &bull; <strong>Business Continuity Plan (BCP)</strong> — "How does
          the <em>business</em> keep operating during a disruption?"
          (alternate work locations, manual processes, communication trees,
          supplier failover).<br>
        &bull; <strong>Disaster Recovery (DR) Plan</strong> — "How do we
          restore <em>IT systems and data</em> after a disaster?"
          (backup restoration, failover data centres, system rebuild order).<br><br>
        DR is a <em>subset</em> of BCP — IT recovery is one piece of
        keeping the whole business running.<br><br>
        <em>"Not my circus, not my monkey"</em> — IT often owns DR, but
        BCP requires every department (HR, finance, legal, facilities).
        Don't try to write the whole plan alone — coordinate.
      </div>
    </div>

    <div class="concept-card">
      <div class="concept-label">Key Metrics</div>
      <div class="concept-title">RTO and RPO – The Two Numbers That Matter</div>
      <div class="concept-desc">
        Every system needs two target numbers, set by the business based
        on how much pain it can tolerate:
      </div>
      <div class="code-block">
<span class="com">RTO — Recovery Time Objective</span>
  "How long can this system be DOWN before it seriously hurts the business?"
  Example: Payment processing RTO = 1 hour
           Internal wiki RTO       = 24 hours

<span class="com">RPO — Recovery Point Objective</span>
  "How much DATA can we afford to lose, measured in time?"
  Example: Customer database RPO = 15 minutes (near-continuous replication)
           Internal reports RPO  = 24 hours (nightly backup is fine)

<span class="com">─── How RPO drives your backup strategy ─────────────────────</span>
RPO target      Backup approach required
&lt; 1 minute      Synchronous replication / multi-region active-active
15 minutes      Continuous transaction log shipping
1 hour          Frequent incremental snapshots
24 hours        Nightly full backup is sufficient

<span class="com">Tighter RTO/RPO = more expensive infrastructure.</span>
<span class="com">The business — not IT — should decide what's worth the cost.</span>
      </div>
    </div>

    <div class="concept-card">
      <div class="concept-label">Plan Components</div>
      <div class="concept-title">What Goes Into a DR Plan</div>
      <div class="concept-desc">
        A real DR plan is a living document, not a binder that gathers dust.
        Core sections:<br><br>
        1. <strong>Asset &amp; dependency inventory</strong> — what systems
           exist, and what do they depend on? (You can't recover what you
           don't know about.)<br>
        2. <strong>Recovery priority order</strong> — which systems come
           back first? (Usually: identity/auth → network → core databases
           → applications → reporting/analytics.)<br>
        3. <strong>Step-by-step recovery procedures</strong> — written so a
           person who's never done it before could follow them at 3 AM
           under stress.<br>
        4. <strong>Contact tree</strong> — who to call, in what order,
           with backup contacts (people get sick, change numbers).<br>
        5. <strong>Communication templates</strong> — pre-written
           customer/employee notifications so no one has to write them
           during a crisis.<br>
        6. <strong>Alternate site/vendor details</strong> — DR data centre
           access, backup ISP contacts, hotel block for displaced staff.
      </div>
    </div>

    <div class="concept-card">
      <div class="concept-label">Testing</div>
      <div class="concept-title">A Plan You've Never Tested Is a Guess</div>
      <div class="concept-desc">
        <em>"Assume" makes an ass out of you and me</em> — never assume
        your backups work, your failover scripts run, or your contact list
        is current. Test regularly:<br><br>
        &bull; <strong>Tabletop exercise</strong> — gather stakeholders,
          walk through a scenario verbally ("a ransomware attack encrypts
          our file server at 2 AM Saturday — what do we do?").<br>
        &bull; <strong>Walkthrough test</strong> — team members physically
          perform their roles without actually executing changes.<br>
        &bull; <strong>Simulation test</strong> — recover a system in an
          isolated environment to verify the actual procedure works.<br>
        &bull; <strong>Full interruption test</strong> — actually fail over
          to the DR site (highest confidence, highest risk — schedule
          carefully).<br><br>
        <em>You can't make someone make the right choice, yet you can pick
        up the pieces afterwards</em> — when a real disaster strikes and
        the plan works because you tested it, that's not luck. That's
        preparation paying off exactly when it matters most.
      </div>
    </div>

  </div>
</div>
"""

# ══════════════════════════════════════════════════════════════════════════
# SCRIPT – Regular expressions deep dive
# ══════════════════════════════════════════════════════════════════════════
C_SCRIPT = """
<!-- BEGINNER35-SCRIPT v1 -->
<!-- ── TOPIC: Regular Expressions Deep Dive ──────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-badge">Beginner</span>
    Regular Expressions – Pattern Matching That Pays Off Forever
  </div>
  <div class="topic-body">

    <div class="concept-card">
      <div class="concept-label">Core Concept</div>
      <div class="concept-title">Why Learn Regex?</div>
      <div class="concept-desc">
        A <strong>regular expression (regex)</strong> is a tiny language for
        describing patterns in text. It shows up <em>everywhere</em>:
        log searching (<code>grep</code>), text editors (find/replace),
        input validation, SIEM queries, firewall rules, programming
        languages.<br><br>
        Learn it once, and you can search a million-line log file for
        "every IP address that tried to log in as root" in seconds —
        a task that would take hours by hand.<br><br>
        <em>"Not my circus, not my monkey"</em> — don't write a 200-character
        regex when a simple string search does the job. Regex is powerful,
        but overusing it makes code unreadable. Use the simplest tool that
        solves the problem.
      </div>
    </div>

    <div class="concept-card">
      <div class="concept-label">Building Blocks</div>
      <div class="concept-title">The Regex Cheat Sheet</div>
      <div class="concept-desc">
        Master these symbols and you can read 90% of regexes you'll
        encounter:
      </div>
      <div class="code-block">
<span class="com">Symbol   Meaning                          Example matches</span>
.        Any single character             a.c   →  abc, a9c, a c
*        Zero or more of previous         ab*   →  a, ab, abbb
+        One or more of previous          ab+   →  ab, abbb (not "a")
?        Zero or one (optional)           colou?r → color, colour
^        Start of line/string             ^Error  → line starting with "Error"
$        End of line/string               \\.com$  → ends with ".com"
[abc]    Any one of a, b, c               gr[ae]y  → gray, grey
[^abc]   Anything EXCEPT a, b, c          [^0-9]   → any non-digit
[a-z]    Range (a through z)              [a-zA-Z0-9_]  → word characters
{n,m}    Between n and m repeats          \\d{3,5}  → 3-5 digits
\\d       Any digit  [0-9]                \\d{1,3}\\.\\d{1,3}  → IP-ish
\\w       Word char [a-zA-Z0-9_]          \\w+@\\w+   → simple email shape
\\s       Whitespace (space, tab, newline) \\s+      → one or more spaces
( )      Group / capture                 (https?)://  → captures http or https
|        OR / alternation                cat|dog    → cat OR dog
\\b       Word boundary                   \\bcat\\b    → "cat" not "category"

<span class="com"># Greedy vs lazy matching — a common gotcha:</span>
<span class="com"># &lt;.+&gt;     greedy: matches "&lt;b&gt;text&lt;/b&gt;" (too much!)</span>
<span class="com"># &lt;.+?&gt;    lazy:   matches "&lt;b&gt;" then "&lt;/b&gt;" separately (correct)</span>
      </div>
    </div>

    <div class="concept-card">
      <div class="concept-label">Practical Patterns</div>
      <div class="concept-title">Real Regexes You'll Actually Use</div>
      <div class="concept-desc">
        These are battle-tested patterns for common IT/security tasks:
      </div>
      <div class="code-block">
<span class="com"># IPv4 address (good enough for log filtering, not RFC-perfect)</span>
\\b(?:\\d{1,3}\\.){3}\\d{1,3}\\b

<span class="com"># Email address (practical, not 100% RFC compliant — nothing truly is)</span>
[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}

<span class="com"># US phone number (several common formats)</span>
\\(?\\d{3}\\)?[-. ]?\\d{3}[-. ]?\\d{4}

<span class="com"># ISO 8601 date/timestamp (2026-06-06T14:30:00Z)</span>
\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}Z?

<span class="com"># Find failed SSH logins and extract the source IP (capture group)</span>
grep -oP <span class="str">'Failed password .* from \\K[\\d.]+'</span> /var/log/auth.log

<span class="com"># Validate a strong password (8+ chars, upper, lower, digit, symbol)</span>
^(?=.*[a-z])(?=.*[A-Z])(?=.*\\d)(?=.*[^a-zA-Z\\d]).{8,}$
<span class="com"># (?=...) is a "lookahead" — checks a condition without consuming characters</span>

<span class="com"># Extract all URLs from a block of text</span>
https?://[^\\s"'&lt;&gt;]+
      </div>
    </div>

    <div class="concept-card">
      <div class="concept-label">Python re module</div>
      <div class="concept-title">Using Regex in Python</div>
      <div class="concept-desc">
        Python's <code>re</code> module is the standard way to apply
        regex in scripts. <code>re.compile()</code> pre-compiles a pattern
        for reuse — important when matching against thousands of lines.
      </div>
      <div class="code-block">
<span class="kw">import</span> re

log_line = <span class="str">"2026-06-06 09:14:32 Failed password for root from 203.0.113.7 port 51422"</span>

<span class="com"># search() — find the first match anywhere in the string</span>
m = re.search(<span class="fn">r</span><span class="str">"from (\\d{1,3}(?:\\.\\d{1,3}){3})"</span>, log_line)
<span class="kw">if</span> m:
    <span class="fn">print</span>(<span class="str">"Source IP:"</span>, m.group(<span class="num">1</span>))   <span class="com"># 203.0.113.7</span>

<span class="com"># findall() — get every match in the string as a list</span>
ips = re.findall(<span class="fn">r</span><span class="str">"\\b(?:\\d{1,3}\\.){3}\\d{1,3}\\b"</span>, log_line)

<span class="com"># sub() — find and replace (great for redacting sensitive data)</span>
redacted = re.sub(<span class="fn">r</span><span class="str">"\\b\\d{3}-\\d{2}-\\d{4}\\b"</span>, <span class="str">"[SSN-REDACTED]"</span>, text)

<span class="com"># Named groups — much more readable than numbered groups</span>
pattern = re.<span class="fn">compile</span>(
    <span class="fn">r</span><span class="str">"(?P&lt;date&gt;\\d{4}-\\d{2}-\\d{2}) (?P&lt;time&gt;\\d{2}:\\d{2}:\\d{2}) "</span>
    <span class="fn">r</span><span class="str">"Failed password for (?P&lt;user&gt;\\S+) from (?P&lt;ip&gt;[\\d.]+)"</span>
)
m = pattern.search(log_line)
<span class="kw">if</span> m:
    <span class="fn">print</span>(m.group(<span class="str">"user"</span>), m.group(<span class="str">"ip"</span>))   <span class="com"># root 203.0.113.7</span>
    <span class="fn">print</span>(m.groupdict())                  <span class="com"># full dict of named captures</span>

<span class="com"># Tip: test regexes interactively at regex101.com before deploying</span>
      </div>
    </div>

  </div>
</div>
"""

# ══════════════════════════════════════════════════════════════════════════
# MILITARY – Leadership principles for IT
# ══════════════════════════════════════════════════════════════════════════
C_MILITARY = """
<!-- BEGINNER35-MILITARY v1 -->
<!-- ── TOPIC: Leadership Principles for IT Teams ─────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-badge">Beginner</span>
    Leadership – Military Principles Applied to IT Teams
  </div>
  <div class="topic-body">

    <div class="concept-card">
      <div class="concept-label">Core Concept</div>
      <div class="concept-title">Why Military Leadership Models Translate</div>
      <div class="concept-desc">
        Military leadership doctrine has been refined over centuries under
        the highest-stakes conditions imaginable — and a surprising amount
        of it maps directly onto leading an IT team through an outage,
        a project crunch, or simply day-to-day operations.<br><br>
        Both environments share key features: high-pressure decisions
        with incomplete information, the need to coordinate people who
        can't all see the whole picture, and consequences that compound
        when communication breaks down.<br><br>
        You don't need a title to lead — the engineer who keeps a calm
        head during an outage and gets the team organised is leading,
        regardless of what the org chart says.
      </div>
    </div>

    <div class="concept-card">
      <div class="concept-label">Commander's Intent</div>
      <div class="concept-title">"Commander's Intent" – Goals Over Scripts</div>
      <div class="concept-desc">
        In the military, a leader gives <strong>Commander's Intent</strong>:
        a clear statement of the <em>end goal and the "why"</em> — not a
        rigid step-by-step script. This way, when the situation changes
        (and it always does), subordinates can adapt without waiting for
        new orders.<br><br>
        <strong>In IT, this looks like:</strong><br>
        Bad delegation: "Run these five exact commands in this order."<br>
        Good delegation: "We need this service back online with zero data
        loss — here's what I know about the failure. Use your judgment;
        call me if you hit something I haven't covered."<br><br>
        Good intent-based delegation does two things: it grows your team's
        capability, and it means the mission survives even if the leader
        is unreachable — exactly when it matters most (3 AM incidents).
      </div>
    </div>

    <div class="concept-card">
      <div class="concept-label">After-Action Review</div>
      <div class="concept-title">The After-Action Review (AAR) Process</div>
      <div class="concept-desc">
        The military's <strong>After-Action Review</strong> is the direct
        ancestor of the modern "blameless postmortem." Four simple
        questions, asked after every significant event:
      </div>
      <div class="code-block">
<span class="com">THE AFTER-ACTION REVIEW — FOUR QUESTIONS</span>
<span class="com">───────────────────────────────────────────────────────</span>

1. WHAT WAS SUPPOSED TO HAPPEN?
   "The deploy was supposed to complete in 10 minutes with zero downtime."

2. WHAT ACTUALLY HAPPENED?
   "The deploy took 47 minutes and caused a 12-minute outage."

3. WHY WAS THERE A DIFFERENCE?
   "The database migration locked a table longer than expected because
    the table had grown 3x since the migration was last tested."

4. WHAT WILL WE DO DIFFERENTLY NEXT TIME?
   "Test migrations against a copy of production-sized data.
    Add a pre-flight check that estimates migration duration.
    Add an automatic abort if a migration runs longer than 5 minutes."

<span class="com">RULES THAT MAKE IT WORK:</span>
<span class="com">- No rank in the room — the newest hire's observation counts as much</span>
<span class="com">  as the senior engineer's</span>
<span class="com">- Focus on the SYSTEM, not the PERSON ("the process allowed this"</span>
<span class="com">  not "Dave messed up")</span>
<span class="com">- Write it down — verbal lessons evaporate; written ones compound</span>
      </div>
    </div>

    <div class="concept-card">
      <div class="concept-label">Mission Mindset</div>
      <div class="concept-title">Putting It All Together — Leading Through Chaos</div>
      <div class="concept-desc">
        These three phrases — central to this entire guide — are
        themselves leadership principles refined into short, memorable
        forms (the way good military doctrine often is):<br><br>
        <strong>"Not my circus, not my monkey"</strong> — a leader protects
        their team's focus. Shield people from drama and scope creep that
        doesn't serve the mission; redirect it to whoever owns it.<br><br>
        <strong>"Assume makes an ass out of you and me"</strong> — a leader
        verifies before committing resources. "I think the backup ran" is
        not the same as "I confirmed the backup completed and is restorable."<br><br>
        <strong>"You can't make someone make the right choice, yet you can
        pick up the pieces afterwards"</strong> — a leader's real value
        often shows <em>after</em> something goes wrong: staying calm,
        organising the recovery, protecting the team from blame spirals,
        and turning the failure into the team's next strength.<br><br>
        Master these three, lead with clear intent, and run honest AARs —
        and you'll out-perform leaders with twice your technical
        knowledge but none of this foundation.
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
    (A_OPS,      S_OPS,      C_OPS),
    (A_SEC,      S_SEC,      C_SEC),
    (A_GRC,      S_GRC,      C_GRC),
    (A_SCRIPT,   S_SCRIPT,   C_SCRIPT),
    (A_MILITARY, S_MILITARY, C_MILITARY),
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
