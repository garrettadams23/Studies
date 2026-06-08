#!/usr/bin/env python3
"""Wave 36 – Email/mail server admin, OWASP Top 10, GDPR/CCPA, Git workflows, home lab."""
from pathlib import Path
from html.parser import HTMLParser

S_LINUX    = "<!-- BEGINNER36-LINUX v1 -->"
S_SEC      = "<!-- BEGINNER36-SEC v1 -->"
S_GRC      = "<!-- BEGINNER36-GRC v1 -->"
S_SCRIPT   = "<!-- BEGINNER36-SCRIPT v1 -->"
S_LIFESTYLE= "<!-- BEGINNER36-LIFESTYLE v1 -->"

A_LINUX    = "<!-- /domain-body linux -->"
A_SEC      = "<!-- /domain-body sec -->"
A_GRC      = "<!-- /domain-body grc -->"
A_SCRIPT   = "<!-- /domain-body script -->"
A_LIFESTYLE= "<!-- /domain-body lifestyle -->"

# ══════════════════════════════════════════════════════════════════════════
# LINUX – Mail server administration basics
# ══════════════════════════════════════════════════════════════════════════
C_LINUX = """
<!-- BEGINNER36-LINUX v1 -->
<!-- ── TOPIC: Mail Server Administration ─────────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-badge">Beginner</span>
    Mail Servers – Postfix, Dovecot &amp; Email Plumbing
  </div>
  <div class="topic-body">

    <div class="concept-card">
      <div class="concept-label">Core Concept</div>
      <div class="concept-title">How Email Actually Travels</div>
      <div class="concept-desc">
        Email involves more moving parts than people realise. Three
        protocols and two server roles cover almost everything:<br><br>
        &bull; <strong>MTA (Mail Transfer Agent)</strong> — moves mail
          between servers using <strong>SMTP</strong> (Simple Mail
          Transfer Protocol, port 25/587). Examples: Postfix, Exim, Sendmail.<br>
        &bull; <strong>MDA / IMAP-POP server</strong> — stores mail and
          lets users retrieve it. Examples: Dovecot.<br>
        &bull; <strong>IMAP</strong> (port 143/993) — keeps mail on the
          server, syncs across devices (the modern standard).<br>
        &bull; <strong>POP3</strong> (port 110/995) — downloads mail to
          one device, often deletes it from the server (legacy).<br><br>
        <strong>The journey of an email:</strong><br>
        Your client → your MTA (SMTP) → recipient's MX server (SMTP) →
        recipient's mailbox store → recipient's client (IMAP/POP3).
      </div>
    </div>

    <div class="concept-card">
      <div class="concept-label">Postfix Setup</div>
      <div class="concept-title">Basic Postfix Configuration</div>
      <div class="concept-desc">
        Postfix is the most widely deployed open-source MTA. Its main
        config file is <code>/etc/postfix/main.cf</code>.
      </div>
      <div class="code-block">
<span class="com"># Install Postfix (choose "Internet Site" during setup)</span>
sudo apt install postfix mailutils

<span class="com"># Key settings in /etc/postfix/main.cf</span>
myhostname = mail.example.com
mydomain   = example.com
myorigin   = $mydomain
inet_interfaces = all
mydestination = $myhostname, localhost.$mydomain, $mydomain

<span class="com"># Restrict who can relay mail through your server (CRITICAL — </span>
<span class="com"># an open relay gets you blacklisted within hours)</span>
smtpd_relay_restrictions =
    permit_mynetworks,
    permit_sasl_authenticated,
    reject_unauth_destination

<span class="com"># Enforce TLS for incoming and outgoing mail</span>
smtpd_tls_cert_file = /etc/letsencrypt/live/mail.example.com/fullchain.pem
smtpd_tls_key_file  = /etc/letsencrypt/live/mail.example.com/privkey.pem
smtpd_tls_security_level = may
smtp_tls_security_level  = may

<span class="com"># Apply config and restart</span>
sudo postfix check
sudo systemctl restart postfix

<span class="com"># Test sending mail from the CLI</span>
echo <span class="str">"Test body"</span> | mail -s <span class="str">"Test subject"</span> alice@example.com

<span class="com"># Watch the mail log in real time</span>
sudo tail -f /var/log/mail.log
      </div>
    </div>

    <div class="concept-card">
      <div class="concept-label">Security</div>
      <div class="concept-title">Don't Become an Open Relay</div>
      <div class="concept-desc">
        <em>"Assume" makes an ass out of you and me</em> — never assume
        your default mail server config is safe to expose. The single
        most common rookie mistake is leaving a server as an
        <strong>open relay</strong> — anyone on the internet can use it
        to send mail through you.<br><br>
        Within hours, spammers find it, your server's IP lands on every
        major blacklist (Spamhaus, SORBS), and legitimate mail from your
        domain stops being delivered anywhere.<br><br>
        <strong>Checklist before going live:</strong><br>
        &bull; Test from an external network — try relaying through your
          server from outside; it must be rejected.<br>
        &bull; Require SASL authentication for any relay.<br>
        &bull; Set up SPF, DKIM, DMARC (covered in the Social Engineering
          topic) — receivers use these to validate your mail.<br>
        &bull; Check your IP against blacklists regularly:
          <code>https://mxtoolbox.com/blacklists.aspx</code>
      </div>
      <div class="code-block">
<span class="com"># Test for open relay from an external host (use mail-tester.com</span>
<span class="com"># or manually with telnet — should be REJECTED for unauth relay)</span>
telnet mail.example.com <span class="num">25</span>
EHLO test.com
MAIL FROM:&lt;attacker@evil.com&gt;
RCPT TO:&lt;victim@someoneelse.com&gt;
<span class="com"># Expected: "554 5.7.1 Relay access denied" — if you get "250 OK"</span>
<span class="com"># at this stage, YOU ARE AN OPEN RELAY. Fix immediately.</span>

<span class="com"># Check your sending IP reputation</span>
dig +short mail.example.com
<span class="com"># Then check at: mxtoolbox.com/blacklists.aspx</span>
      </div>
    </div>

    <div class="concept-card">
      <div class="concept-label">Troubleshooting</div>
      <div class="concept-title">Diagnosing Common Mail Delivery Issues</div>
      <div class="concept-desc">
        <em>You can't make someone make the right choice, yet you can pick
        up the pieces afterwards</em> — when "my email isn't sending"
        tickets come in, work through this systematically:<br><br>
        1. Check the mail queue: <code>postqueue -p</code> — stuck messages
           reveal delivery problems.<br>
        2. Read <code>/var/log/mail.log</code> for the message ID — it
           shows every hop and any errors.<br>
        3. Verify DNS — does your MX record point to the right server?
           <code>dig example.com MX</code><br>
        4. Test authentication — can the user actually log in via
           IMAP/SMTP with their credentials?<br>
        5. Check spam folder and recipient's blacklist status — sometimes
           "not delivered" really means "filtered as spam."<br>
        6. Use <code>mail-tester.com</code> — sends a test email and
           grades your entire setup (SPF/DKIM/DMARC/blacklist/content).
      </div>
    </div>

  </div>
</div>
"""

# ══════════════════════════════════════════════════════════════════════════
# SEC – OWASP Top 10 web application security
# ══════════════════════════════════════════════════════════════════════════
C_SEC = """
<!-- BEGINNER36-SEC v1 -->
<!-- ── TOPIC: OWASP Top 10 Web App Security ──────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-badge">Beginner</span>
    OWASP Top 10 – The Web Vulnerabilities Everyone Must Know
  </div>
  <div class="topic-body">

    <div class="concept-card">
      <div class="concept-label">Core Concept</div>
      <div class="concept-title">What Is OWASP and Why the Top 10 Matters</div>
      <div class="concept-desc">
        <strong>OWASP (Open Worldwide Application Security Project)</strong>
        publishes the <strong>OWASP Top 10</strong> — a regularly updated
        list of the most critical web application security risks, based
        on real-world data from organisations worldwide.<br><br>
        It's the closest thing the industry has to a "must-know" list for
        anyone who builds, tests, or defends web applications. Job
        postings reference it; certifications test on it; bug bounty
        programs are organised around it.<br><br>
        <em>"Not my circus, not my monkey"</em> — you don't need to be a
        developer to understand these. Knowing <em>what</em> each
        vulnerability is and <em>why</em> it matters makes you valuable
        in security reviews, incident response, and conversations with
        engineering teams.
      </div>
    </div>

    <div class="concept-card">
      <div class="concept-label">The List</div>
      <div class="concept-title">OWASP Top 10 (2021 Edition) Explained Simply</div>
      <div class="concept-desc">
        Each entry below: what it is, in plain language, with an
        everyday analogy.
      </div>
      <div class="code-block">
<span class="com">A01: Broken Access Control</span>
  Users can do things they shouldn't (view others' data, admin pages).
  Analogy: A hotel keycard that opens every room, not just yours.

<span class="com">A02: Cryptographic Failures</span>
  Sensitive data stored or transmitted without proper encryption.
  Analogy: Writing your PIN on the back of your bank card.

<span class="com">A03: Injection (SQL, NoSQL, Command, LDAP)</span>
  Untrusted input is executed as code/commands by the backend.
  Analogy: Writing "ignore my rent and give me $1,000,000" on a check
  — and the bank's system actually processing it as written.

<span class="com">A04: Insecure Design</span>
  The flaw is in the blueprint, not the code — security wasn't designed in.
  Analogy: A bank vault with a sturdy door but no walls.

<span class="com">A05: Security Misconfiguration</span>
  Default passwords, verbose error messages, unnecessary features enabled.
  Analogy: Leaving the factory-set "admin/admin" login on a new router.

<span class="com">A06: Vulnerable and Outdated Components</span>
  Using libraries/frameworks with known, unpatched vulnerabilities.
  Analogy: Driving a car with a known faulty brake recall you never fixed.

<span class="com">A07: Identification and Authentication Failures</span>
  Weak password rules, no MFA, predictable session tokens.
  Analogy: A door that locks, but the key is "1234" for every customer.

<span class="com">A08: Software and Data Integrity Failures</span>
  Trusting code/updates from sources without verifying their integrity.
  Analogy: Accepting a "replacement" car part from a stranger in a parking lot.

<span class="com">A09: Security Logging and Monitoring Failures</span>
  Attacks go undetected because no one is watching the logs.
  Analogy: A security camera that's recording but nobody ever reviews the tape.

<span class="com">A10: Server-Side Request Forgery (SSRF)</span>
  Attacker tricks the server into making requests on their behalf,
  often reaching internal systems the attacker couldn't reach directly.
  Analogy: Convincing the receptionist to walk into the vault and
  read you what's inside, since you're not allowed in yourself.
      </div>
    </div>

    <div class="concept-card">
      <div class="concept-label">Hands-On Example</div>
      <div class="concept-title">SQL Injection — The Classic A03 Example</div>
      <div class="concept-desc">
        This is the canonical example every security professional learns.
        <em>Only test against systems you own or have authorisation to
        test (e.g. DVWA, OWASP Juice Shop, your own lab).</em>
      </div>
      <div class="code-block">
<span class="com">─── VULNERABLE CODE (Python/Flask, never do this) ────────────</span>
username = request.form[<span class="str">'username'</span>]
password = request.form[<span class="str">'password'</span>]
query = <span class="fn">f</span><span class="str">"SELECT * FROM users WHERE username='{username}' AND password='{password}'"</span>
cursor.execute(query)   <span class="com"># string concatenation = injection waiting to happen</span>

<span class="com">─── THE ATTACK ────────────────────────────────────────────────</span>
<span class="com"># Attacker enters this as the username:</span>
admin' --
<span class="com"># Resulting query becomes:</span>
<span class="com">SELECT * FROM users WHERE username='admin' -- ' AND password='whatever'</span>
<span class="com"># The "--" comments out the password check entirely. Instant login bypass.</span>

<span class="com">─── THE FIX: parameterised queries (always do this) ──────────</span>
query = <span class="str">"SELECT * FROM users WHERE username = %s AND password = %s"</span>
cursor.execute(query, (username, password))
<span class="com"># The database driver treats username/password as DATA, never as CODE —</span>
<span class="com"># no matter what characters the attacker includes.</span>

<span class="com"># SQLAlchemy ORM (also safe — handles parameterisation for you)</span>
user = User.query.filter_by(username=username, password=password).first()
      </div>
    </div>

    <div class="concept-card">
      <div class="concept-label">Defence Mindset</div>
      <div class="concept-title">"Never Trust User Input" — The Golden Rule</div>
      <div class="concept-desc">
        <em>"Assume" makes an ass out of you and me</em> — and nowhere is
        this truer than in web development. Every single piece of data
        that comes from outside your application — form fields, URL
        parameters, HTTP headers, cookies, file uploads, even data from
        "trusted" third-party APIs — must be treated as potentially
        hostile until validated.<br><br>
        <strong>Defence in depth for web apps:</strong><br>
        &bull; Validate input on the server (client-side validation is a
          UX nicety, not a security control — it's trivially bypassed).<br>
        &bull; Use parameterised queries / ORMs — never string-concatenate
          SQL.<br>
        &bull; Encode output based on context (HTML, JS, URL, SQL each
          need different encoding).<br>
        &bull; Apply the principle of least privilege to database
          accounts — your web app's DB user shouldn't be able to
          <code>DROP TABLE</code>.<br>
        &bull; Keep dependencies updated — run <code>npm audit</code>,
          <code>pip-audit</code>, or Dependabot regularly.<br>
        &bull; Practice on intentionally vulnerable apps: OWASP Juice
          Shop, DVWA, PortSwigger Web Security Academy (all free, all legal).
      </div>
    </div>

  </div>
</div>
"""

# ══════════════════════════════════════════════════════════════════════════
# GRC – GDPR / CCPA privacy law fundamentals
# ══════════════════════════════════════════════════════════════════════════
C_GRC = """
<!-- BEGINNER36-GRC v1 -->
<!-- ── TOPIC: GDPR & CCPA Privacy Law Basics ─────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-badge">Beginner</span>
    Privacy Law – GDPR &amp; CCPA for IT Professionals
  </div>
  <div class="topic-body">

    <div class="concept-card">
      <div class="concept-label">Core Concept</div>
      <div class="concept-title">Why IT People Need to Understand Privacy Law</div>
      <div class="concept-desc">
        Privacy regulations turn technical decisions into legal
        obligations. The engineer who designs a database schema, the
        admin who configures backup retention, and the analyst who
        exports a report all make choices that can create — or violate —
        legal compliance.<br><br>
        <strong>Two regulations every IT pro should recognise:</strong><br>
        &bull; <strong>GDPR (General Data Protection Regulation)</strong>
          — EU law; applies to any organisation processing the personal
          data of EU residents, regardless of where the company is based.
          Massive fines: up to €20 million or 4% of global annual revenue.<br>
        &bull; <strong>CCPA / CPRA (California Consumer Privacy Act)</strong>
          — California law with similar goals; influences how US companies
          handle privacy nationwide because it's easier to apply one
          standard everywhere.<br><br>
        <em>"Not my circus, not my monkey"</em> — legal interpretation
        belongs to your privacy/legal team. But you're often the one who
        has to <em>technically implement</em> their requirements — so
        speaking their language matters.
      </div>
    </div>

    <div class="concept-card">
      <div class="concept-label">Key Concepts</div>
      <div class="concept-title">GDPR Vocabulary You'll Actually Encounter</div>
      <div class="concept-desc">
        These terms appear in privacy policies, vendor contracts, and
        compliance tickets constantly:
      </div>
      <div class="code-block">
<span class="com">Term                    Meaning</span>
PII / Personal Data     Any info that can identify a person — name, email,
                        IP address, device ID, location data, even an
                        opinion ABOUT a person counts under GDPR

Data Subject            The person the data is about (your customer/user)

Data Controller         The organisation that decides WHY and HOW
                        data is processed (usually: your company)

Data Processor          An organisation that processes data ON BEHALF
                        of the controller (e.g. your cloud provider,
                        your email marketing tool)

Lawful Basis            One of six legal reasons you're allowed to
                        process personal data (consent, contract,
                        legal obligation, vital interests, public task,
                        legitimate interests)

DPA                     Data Processing Agreement — required contract
                        between controller and processor

DPO                     Data Protection Officer — required role for
                        organisations doing large-scale data processing

DPIA                    Data Protection Impact Assessment — required
                        before launching high-risk data processing

Right to be Forgotten   A person can request deletion of their data
                        ("right to erasure" — Article 17)

Data Portability        A person can request their data in a
                        machine-readable format to move to another service
      </div>
    </div>

    <div class="concept-card">
      <div class="concept-label">Practical Impact</div>
      <div class="concept-title">How Privacy Law Shapes Technical Decisions</div>
      <div class="concept-desc">
        These regulations aren't abstract — they directly drive
        engineering and operations requirements:<br><br>
        &bull; <strong>Data minimisation</strong> — collect only what
          you need. "We might use it someday" is not a lawful basis.<br>
        &bull; <strong>Retention limits</strong> — you must be able to
          say <em>why</em> data is kept for X days/years, and delete it
          after. "We never delete anything" is a compliance risk, not
          a feature.<br>
        &bull; <strong>Right to erasure</strong> — when a user asks to be
          forgotten, can your systems actually find and delete every
          copy of their data — including backups, logs, and analytics
          exports? Most companies discover gaps here the hard way.<br>
        &bull; <strong>Breach notification</strong> — GDPR requires
          notifying regulators within <strong>72 hours</strong> of
          becoming aware of a breach involving personal data. Your
          incident response plan needs a privacy notification step
          built in, not bolted on afterward.<br>
        &bull; <strong>Privacy by Design</strong> — GDPR Article 25
          requires building privacy protections into systems from the
          start, not retrofitting them after a complaint.
      </div>
    </div>

    <div class="concept-card">
      <div class="concept-label">Real Scenario</div>
      <div class="concept-title">Handling a "Right to Erasure" Request</div>
      <div class="concept-desc">
        <em>You can't make someone make the right choice, yet you can pick
        up the pieces afterwards</em> — your legal team will get these
        requests; you'll be the one who has to fulfil them technically.<br><br>
        <strong>A realistic erasure-request workflow:</strong><br>
        1. Verify the requester's identity (don't delete the wrong
           person's data because someone claimed to be them).<br>
        2. Map every system that holds this person's data — production
           DB, data warehouse, email lists, support tickets, backups,
           analytics, third-party processors.<br>
        3. Determine if any <em>legal exception</em> applies (e.g. you
           must keep financial records for tax purposes — document
           this and inform the requester what's retained and why).<br>
        4. Execute deletion (or anonymisation, where deletion isn't
           feasible — e.g. financial records that must be retained but
           can have personal identifiers stripped).<br>
        5. Confirm and document — the audit trail proves you complied,
           and protects you if questioned later.<br><br>
        <em>"Assume" makes an ass out of you and me</em> — never assume
        "delete the user record" actually erased the person's data. Check
        every cache, replica, log line, and backup copy.
      </div>
    </div>

  </div>
</div>
"""

# ══════════════════════════════════════════════════════════════════════════
# SCRIPT – Git advanced workflows
# ══════════════════════════════════════════════════════════════════════════
C_SCRIPT = """
<!-- BEGINNER36-SCRIPT v1 -->
<!-- ── TOPIC: Git Advanced Workflows ─────────────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-badge">Intermediate</span>
    Git Advanced Workflows – Beyond add, commit, push
  </div>
  <div class="topic-body">

    <div class="concept-card">
      <div class="concept-label">Core Concept</div>
      <div class="concept-title">Why "git add, commit, push" Isn't Enough</div>
      <div class="concept-desc">
        Most beginners learn the basic Git loop and stop there. But real
        teams hit situations the basics don't cover: messy commit history,
        accidental commits to the wrong branch, finding which commit
        introduced a bug, or recovering "lost" work. These tools turn Git
        from a save-button into a powerful investigation and cleanup
        toolkit.<br><br>
        <em>"Assume" makes an ass out of you and me</em> — never assume a
        destructive Git command is safe just because the help text looks
        simple. <code>reset --hard</code>, <code>push --force</code>, and
        <code>clean -f</code> can permanently destroy work. Always know
        your escape hatch before you pull the trigger.
      </div>
    </div>

    <div class="concept-card">
      <div class="concept-label">Investigation</div>
      <div class="concept-title">git bisect — Finding the Commit That Broke Things</div>
      <div class="concept-desc">
        When a bug appears and you don't know which of the last 200
        commits introduced it, <code>git bisect</code> performs an
        automated binary search through history.
      </div>
      <div class="code-block">
<span class="com"># Start a bisect session</span>
git bisect start

<span class="com"># Tell git the current commit is broken (bad)</span>
git bisect bad

<span class="com"># Tell git a known-good commit (e.g. last release tag)</span>
git bisect good v2.3.0

<span class="com"># Git checks out a commit halfway between good and bad.</span>
<span class="com"># Test it, then tell git the result:</span>
git bisect good   <span class="com"># if this commit works</span>
<span class="com"># or</span>
git bisect bad    <span class="com"># if this commit is broken</span>

<span class="com"># Repeat — git narrows the range each time (log2(N) steps total)</span>
<span class="com"># When done, git identifies the exact commit that introduced the bug:</span>
<span class="com"># "a1b2c3d is the first bad commit"</span>

<span class="com"># Clean up when finished</span>
git bisect reset

<span class="com"># Automate it entirely with a test script (no manual testing!)</span>
git bisect start HEAD v2.3.0
git bisect run pytest tests/test_regression.py
<span class="com"># git runs the test at each step and decides good/bad automatically</span>
      </div>
    </div>

    <div class="concept-card">
      <div class="concept-label">History Cleanup</div>
      <div class="concept-title">Interactive Rebase — Cleaning Up Before You Share</div>
      <div class="concept-desc">
        Before opening a pull request, a clean commit history makes
        review far easier. <code>git rebase -i</code> lets you reorder,
        combine, edit, or drop commits.
        <strong>Only rewrite history on branches you haven't shared.</strong>
      </div>
      <div class="code-block">
<span class="com"># Interactively edit the last 5 commits</span>
git rebase -i HEAD~5

<span class="com"># This opens an editor with lines like:</span>
pick a1b2c3d Add login form
pick d4e5f6a Fix typo in login form
pick 7890abc WIP debugging
pick bcdef12 Actually fix the bug
pick 3456789 Remove debug prints

<span class="com"># Change "pick" to control what happens to each commit:</span>
<span class="com">#   pick   = keep commit as-is</span>
<span class="com">#   reword = keep changes, edit the commit message</span>
<span class="com">#   squash = combine with the commit above (keep both messages)</span>
<span class="com">#   fixup  = combine with commit above (discard this message)</span>
<span class="com">#   drop   = remove the commit entirely</span>

<span class="com"># Cleaned-up result might look like:</span>
pick   a1b2c3d Add login form
fixup  d4e5f6a Fix typo in login form
drop   7890abc WIP debugging
fixup  bcdef12 Actually fix the bug
drop   3456789 Remove debug prints

<span class="com"># Result: one clean commit "Add login form" instead of five messy ones</span>
      </div>
    </div>

    <div class="concept-card">
      <div class="concept-label">Recovery</div>
      <div class="concept-title">git reflog — Your Undo Button for Almost Anything</div>
      <div class="concept-desc">
        <em>You can't make someone make the right choice, yet you can pick
        up the pieces afterwards</em> — someone on your team will run
        <code>git reset --hard</code> on the wrong branch eventually.
        <code>git reflog</code> is how you save them.<br><br>
        Git keeps a log of <em>every</em> place HEAD has pointed —
        commits, resets, rebases, checkouts — for about 90 days, even
        ones that seem to have "vanished."
      </div>
      <div class="code-block">
<span class="com"># Show every recent HEAD movement (even "lost" commits)</span>
git reflog

<span class="com"># Output looks like:</span>
<span class="com"># a1b2c3d HEAD@{0}: reset: moving to HEAD~3</span>
<span class="com"># d4e5f6a HEAD@{1}: commit: Add payment validation</span>
<span class="com"># 7890abc HEAD@{2}: commit: Fix currency rounding bug</span>
<span class="com"># ...</span>

<span class="com"># Recover "lost" commits by checking out the reflog entry</span>
git checkout HEAD@{1}

<span class="com"># Or restore your branch to before the bad reset</span>
git reset --hard HEAD@{1}

<span class="com"># Recover a deleted branch entirely</span>
git reflog | grep <span class="str">"checkout: moving from feature-x"</span>
git branch feature-x &lt;commit-hash-from-reflog&gt;

<span class="com"># Find "dangling" commits not referenced by any branch</span>
git fsck --lost-found
      </div>
    </div>

    <div class="concept-card">
      <div class="concept-label">Workflow</div>
      <div class="concept-title">Stash, Cherry-Pick &amp; Worktrees — Juggling Work</div>
      <div class="concept-desc">
        These commands solve the "I need to switch context without
        losing my work" problem in different ways.
      </div>
      <div class="code-block">
<span class="com"># STASH — temporarily shelve uncommitted changes</span>
git stash push -m <span class="str">"WIP: refactoring auth module"</span>
git checkout main           <span class="com"># switch branches with a clean working tree</span>
<span class="com"># ... fix the urgent bug ...</span>
git checkout feature-branch
git stash pop               <span class="com"># bring your work back</span>
git stash list              <span class="com"># see all stashed changes</span>

<span class="com"># CHERRY-PICK — apply a specific commit from another branch</span>
git log other-branch --oneline   <span class="com"># find the commit hash you need</span>
git cherry-pick a1b2c3d          <span class="com"># apply just that one commit here</span>
<span class="com"># Common use: backporting a critical bugfix to a release branch</span>

<span class="com"># WORKTREES — check out multiple branches simultaneously in</span>
<span class="com"># separate directories (no stashing needed)</span>
git worktree add ../hotfix-dir hotfix/critical-bug
<span class="com"># Now you have two working directories on two branches at once —</span>
<span class="com"># build/test the hotfix while your main feature work stays untouched</span>
git worktree list
git worktree remove ../hotfix-dir
      </div>
    </div>

  </div>
</div>
"""

# ══════════════════════════════════════════════════════════════════════════
# LIFESTYLE – Building a home lab for career growth
# ══════════════════════════════════════════════════════════════════════════
C_LIFESTYLE = """
<!-- BEGINNER36-LIFESTYLE v1 -->
<!-- ── TOPIC: Building a Home Lab for Career Growth ──────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-badge">Beginner</span>
    Home Lab – Practicing IT Skills Without Breaking Production
  </div>
  <div class="topic-body">

    <div class="concept-card">
      <div class="concept-label">Core Concept</div>
      <div class="concept-title">Why a Home Lab Accelerates Your Career</div>
      <div class="concept-desc">
        You cannot learn to fix a server outage by reading about one.
        A <strong>home lab</strong> — your own small collection of
        virtual or physical systems — gives you a safe place to break
        things, fix them, and build muscle memory before it matters in
        production.<br><br>
        Hiring managers consistently say the same thing: candidates who
        can talk through a real project they built and broke and fixed
        stand out from candidates who can only recite definitions.
        Your home lab becomes your interview stories, your portfolio,
        and your testing ground for certifications — all at once.<br><br>
        <em>"Not my circus, not my monkey"</em> — your home lab is the
        one circus that <em>is</em> yours. Break it as much as you want;
        that's the entire point.
      </div>
    </div>

    <div class="concept-card">
      <div class="concept-label">Getting Started</div>
      <div class="concept-title">Three Ways to Build a Lab (Pick Your Budget)</div>
      <div class="concept-desc">
        You don't need a server rack to start — most skills can be
        learned on hardware you already own.
      </div>
      <div class="code-block">
<span class="com">TIER 1 — $0 (use what you have)</span>
  - VirtualBox or VMware Workstation Player (free) on your laptop
  - Run 2-3 VMs: a Linux server, a Windows Server eval, a "router" VM
  - Practice: Linux administration, networking basics, AD fundamentals

<span class="com">TIER 2 — $0-50 (cloud free tiers)</span>
  - AWS Free Tier / Azure free account / Google Cloud free tier
  - Practice: cloud networking, IAM, real production-like environments
  - CAUTION: set billing alerts! "Free tier" usage limits are easy to exceed

<span class="com">TIER 3 — $100-500 (dedicated hardware)</span>
  - Used enterprise mini PC (Dell OptiPlex, Lenovo ThinkCentre — ~$80-150)
  - Or a Raspberry Pi cluster (~$150 for 3-4 nodes)
  - Run Proxmox or ESXi as a hypervisor; host many VMs/containers 24/7
  - Practice: Kubernetes clusters, self-hosted services, network segmentation

<span class="com"># Recommended starter lab build (Tier 1, totally free):</span>
<span class="com"># VM1: Ubuntu Server  — practice Linux admin, web servers, Docker</span>
<span class="com"># VM2: Windows Server Evaluation — practice AD, GPO, PowerShell</span>
<span class="com"># VM3: pfSense or OPNsense — practice firewall rules, VPN, routing</span>
<span class="com"># VM4: Kali Linux — practice security tools (on YOUR OWN lab only)</span>
      </div>
    </div>

    <div class="concept-card">
      <div class="concept-label">Project Ideas</div>
      <div class="concept-title">Lab Projects That Actually Build Skills</div>
      <div class="concept-desc">
        Don't just install things — build small projects that mirror
        real work. Here are projects mapped to the domains in this guide:<br><br>
        &bull; <strong>Networking</strong>: Set up a router/firewall VM,
          create VLANs, configure DHCP/DNS, capture and analyse your own
          traffic with Wireshark.<br>
        &bull; <strong>Security/SOC</strong>: Deploy Wazuh or Security
          Onion; generate "attacks" against your own lab; practice
          finding them in the SIEM.<br>
        &bull; <strong>Linux/Ops</strong>: Stand up a web app behind
          nginx, add a database, set up automated backups, then
          practice restoring from them.<br>
        &bull; <strong>Scripting</strong>: Write a script that monitors
          your lab's services and alerts you (Slack/email/Discord
          webhook) when something goes down.<br>
        &bull; <strong>AI</strong>: Train a small model on a public
          dataset; deploy it as an API in your lab; monitor its
          performance over time.<br><br>
        <em>"Assume" makes an ass out of you and me</em> — assume your
        first attempt at any of these will fail in some way. That failure
        IS the lesson. Document what broke and how you fixed it.
      </div>
    </div>

    <div class="concept-card">
      <div class="concept-label">Turning Practice Into Career</div>
      <div class="concept-title">Documenting Your Lab Work for Job Hunting</div>
      <div class="concept-desc">
        <em>You can't make someone make the right choice, yet you can pick
        up the pieces afterwards</em> — and you can also build proof of
        your competence so the right choice (hiring you) is easy for
        someone else to make.<br><br>
        <strong>Turn lab work into career capital:</strong><br>
        &bull; Keep a <strong>build log</strong> — a simple markdown file
          or blog documenting what you built, what broke, and how you
          fixed it. This becomes your interview stories almost verbatim.<br>
        &bull; Push configs and scripts to <strong>GitHub</strong> — a
          public repo of "my home lab automation" shows real,
          verifiable work.<br>
        &bull; Write short posts about problems you solved — you'll be
          surprised how often "I had this exact issue" comments turn
          into networking connections.<br>
        &bull; Use lab achievements to anchor certification study — pass
          the exam AND have hands-on proof you can do the thing the
          cert says you can do.<br><br>
        Five years from now, "I taught myself this in a home lab and now
        I run it in production" is one of the most compelling sentences
        you can say in an interview.
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
    (A_LINUX,     S_LINUX,     C_LINUX),
    (A_SEC,       S_SEC,       C_SEC),
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
