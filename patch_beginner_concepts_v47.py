#!/usr/bin/env python3
"""Wave 47: beginner-friendly content additions across 5 domains."""
import re
from html.parser import HTMLParser

S_GRC = "<!-- BEGINNER47-GRC v1 -->"
A_GRC = "<!-- /domain-body grc -->"
C_GRC = S_GRC + """
<div class="topic">
  <div class="topic-header">
    <span class="topic-badge">Beginner</span>
    <h3>Vendor Risk Assessments – Why "We Use a Cloud Provider" Isn't a Security Plan</h3>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <span class="concept-label">Concept</span>
      <h4 class="concept-title">Your security perimeter includes everyone you trust with your data</h4>
      <p class="concept-desc">The moment your organization sends data to a third party — a payroll processor, a CRM,
      a cloud storage vendor, an email marketing tool — that vendor's security posture becomes <em>your</em> risk.
      A vendor risk assessment is the structured process of asking, before you sign the contract: "If this company
      gets breached, what happens to us?" It's not paranoia; it's recognizing that <span class="kw">trust is
      transitive</span> in ways that are easy to forget when a sales demo looks slick.</p>
      <p class="concept-desc">This mindset matters far beyond the procurement team. <em>"Not my circus, not my
      monkey"</em> feels tempting when a vendor's outage or breach isn't technically your fault — but if their
      failure takes down your service or exposes your customers' data, it becomes very much your circus, very
      quickly. Vendor risk assessments exist precisely so that "their problem" doesn't silently become "our
      incident" with zero warning.</p>
    </div>
    <div class="concept-card">
      <span class="concept-label">Concept</span>
      <h4 class="concept-title">What a basic assessment actually looks at</h4>
      <p class="concept-desc">You don't need a fifty-page questionnaire to start thinking like a risk assessor.
      A few foundational questions cover most of the ground:</p>
      <table class="ai-table">
        <tr><th>Question</th><th>Why it matters</th></tr>
        <tr><td>What data will they actually touch?</td><td>A vendor that only sees anonymized analytics is a very
        different risk than one holding customer SSNs or health records.</td></tr>
        <tr><td>Do they have independent security certifications?</td><td>Reports like SOC 2 or ISO 27001 mean
        someone outside the company has actually checked their controls — not just taken their word for it.</td></tr>
        <tr><td>What's their incident history and notification process?</td><td>Every vendor has had something go
        wrong eventually. What matters is whether they tell you quickly and clearly when it does.</td></tr>
        <tr><td>Can you get your data back out if you leave?</td><td>"Vendor lock-in" isn't just inconvenient — if
        exporting your own data is difficult or impossible, that's a risk worth pricing in up front.</td></tr>
        <tr><td>Who do *they* trust?</td><td>Many vendors rely on their own subcontractors and cloud providers —
        the chain of trust can run several layers deep.</td></tr>
      </table>
    </div>
    <div class="concept-card">
      <span class="concept-label">Concept</span>
      <h4 class="concept-title">Assumptions are where vendor relationships quietly go wrong</h4>
      <p class="concept-desc"><em>"Assume makes an ass out of you and me"</em> shows up constantly in vendor
      management. Common assumptions worth never making without verification:</p>
      <pre class="code-block"><span class="com"># Assumptions that have caused real incidents at real companies:</span>

<span class="com"># "They're a big, well-known company, so they must be secure."</span>
<span class="com">#   -- Size correlates with budget, not automatically with diligence.</span>

<span class="com"># "Our contract says they'll encrypt our data, so it's encrypted."</span>
<span class="com">#   -- A clause in a contract is a promise, not a technical control.
<span class="com">#      Ask HOW, not just whether.</span></span>

<span class="com"># "They passed their assessment last year, so they're still fine."</span>
<span class="com">#   -- Security postures change. Staff turn over. Infrastructure migrates.
<span class="com">#      Reassessment on a schedule isn't bureaucracy -- it's hygiene.</span></span>

<span class="com"># "IT/Legal/Procurement already checked this, so I don't need to."</span>
<span class="com">#   -- Diffusion of responsibility is how gaps get through. If something
<span class="com">#      seems off, say so -- even if "someone else" supposedly verified it.</span></span></pre>
      <p class="concept-desc">None of this means treating every vendor like a hostile actor. It means replacing
      comfortable guesses with quick, specific questions — because the cost of asking is minutes, and the cost of
      assuming wrong can be measured in headlines.</p>
    </div>
  </div>
</div>
""" + "\n" + A_GRC

S_LINUX = "<!-- BEGINNER47-LINUX v1 -->"
A_LINUX = "<!-- /domain-body linux -->"
C_LINUX = S_LINUX + """
<div class="topic">
  <div class="topic-header">
    <span class="topic-badge">Beginner</span>
    <h3>"The Disk Is Full" – Diagnosing Storage Problems Like a Calm Professional</h3>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <span class="concept-label">Concept</span>
      <h4 class="concept-title">The classic 2 AM page: "No space left on device"</h4>
      <p class="concept-desc">Few alerts feel as urgent as a server running out of disk space — services start
      failing to write logs, databases stop accepting writes, and everything gets weird in ways that don't
      immediately look storage-related. The good news: diagnosing <em>where</em> the space went is usually a
      five-minute job once you know the right three commands and the order to run them in.</p>
    </div>
    <div class="concept-card">
      <span class="concept-label">Concept</span>
      <h4 class="concept-title">Step 1 — confirm it, and find which filesystem is the problem</h4>
      <p class="concept-desc"><code>df</code> ("disk free") shows you space at the filesystem level — this is
      where you confirm the emergency is real and identify exactly which mount point is the culprit:</p>
      <pre class="code-block"><span class="com"># -h = human-readable sizes (GB/MB instead of raw byte counts)</span>
df -h

<span class="com"># Typical output -- the "Use%" column is what you're scanning for:</span>
<span class="com"># Filesystem      Size  Used Avail Use% Mounted on</span>
<span class="com"># /dev/sda1        50G   48G  0.5G  99% /</span>
<span class="com"># /dev/sdb1       200G   80G  110G  43% /var/log</span>
<span class="com">#</span>
<span class="com"># Here, the root filesystem ("/") is the emergency -- 99% full.</span>
<span class="com"># /var/log on its own disk is fine. Now we know WHERE to dig.</span></pre>
    </div>
    <div class="concept-card">
      <span class="concept-label">Concept</span>
      <h4 class="concept-title">Step 2 — find which directory is actually eating the space</h4>
      <p class="concept-desc">Once you know <em>which</em> filesystem is full, <code>du</code> ("disk usage") helps
      you walk down the directory tree to find the actual offender — usually a runaway log file, an old backup
      nobody cleaned up, or a temp directory that grew out of control:</p>
      <pre class="code-block"><span class="com"># Summarize top-level directory sizes, sorted largest first:</span>
du -h --max-depth=1 / 2&gt;/dev/null | sort -rh | head -10

<span class="com"># Drill into the biggest offender, one level deeper:</span>
du -h --max-depth=1 /var 2&gt;/dev/null | sort -rh | head -10

<span class="com"># Often the trail leads somewhere very specific, e.g.:</span>
<span class="com">#   23G   /var/log/myapp/debug.log</span>
<span class="com">#   -- a log rotation policy was never configured for this app</span></pre>
    </div>
    <div class="concept-card">
      <span class="concept-label">Concept</span>
      <h4 class="concept-title">Step 3 — understand the "phantom space" trap before you panic further</h4>
      <p class="concept-desc">Here's a scenario that confuses almost every beginner at least once: you delete a
      huge file, run <code>df</code> again, and the space <em>still isn't free</em>. This isn't a bug — it's how
      Unix-like systems handle deletion. If a running process still has the file open, the space isn't released
      until that process closes it (or restarts). <code>lsof</code> ("list open files") reveals exactly this:</p>
      <pre class="code-block"><span class="com"># Find processes holding open file handles to deleted files
# (the "(deleted)" marker is the giveaway):</span>
lsof +L1 2&gt;/dev/null | grep deleted

<span class="com"># Output might show something like:</span>
<span class="com"># myapp     2841  root   12w   REG   8,1  19327352  (deleted) /var/log/myapp/debug.log</span>
<span class="com">#</span>
<span class="com"># The fix isn't deleting it again -- it's already gone from the
# directory listing. Restart (or signal) the process holding it open,
# and the space returns immediately.</span></pre>
      <p class="concept-desc">This is also a perfect moment to remember <em>"assume makes an ass out of you and
      me"</em> — assuming a deleted file's space was reclaimed (when it wasn't) has led more than one engineer to
      delete <em>more</em> files in a panic, sometimes ones that were actually needed. Confirm with <code>lsof</code>
      before escalating to more drastic measures.</p>
    </div>
  </div>
</div>
""" + "\n" + A_LINUX

S_LIFESTYLE = "<!-- BEGINNER47-LIFESTYLE v1 -->"
A_LIFESTYLE = "<!-- /domain-body lifestyle -->"
C_LIFESTYLE = S_LIFESTYLE + """
<div class="topic">
  <div class="topic-header">
    <span class="topic-badge">Beginner</span>
    <h3>Negotiating Your First IT Offer Without Feeling Like You're Being Greedy</h3>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <span class="concept-label">Concept</span>
      <h4 class="concept-title">The discomfort is normal — and it's not a sign you're doing something wrong</h4>
      <p class="concept-desc">For a lot of people moving into IT — especially career-changers and those coming
      from environments where you didn't negotiate your compensation — the idea of pushing back on a job offer
      feels presumptuous, even rude. It isn't. Negotiation is a completely normal, expected part of professional
      hiring. Companies build room into their offers anticipating it. Not asking doesn't make you "easy to work
      with" — it usually just means leaving money and terms on the table that were available the whole time.</p>
    </div>
    <div class="concept-card">
      <span class="concept-label">Concept</span>
      <h4 class="concept-title">What's actually negotiable (it's often more than just salary)</h4>
      <table class="ai-table">
        <tr><th>Item</th><th>Notes</th></tr>
        <tr><td>Base salary</td><td>The most obvious lever, and often the most flexible at larger companies with
        defined pay bands.</td></tr>
        <tr><td>Sign-on bonus</td><td>Sometimes easier for a company to grant than raising base salary, since it's
        a one-time cost rather than an ongoing commitment.</td></tr>
        <tr><td>Start date</td><td>Worth negotiating if you need time to relocate, finish a certification, or just
        decompress between jobs.</td></tr>
        <tr><td>Remote / hybrid flexibility</td><td>Increasingly common to discuss explicitly rather than assume —
        get it in writing if it matters to you.</td></tr>
        <tr><td>Title</td><td>Can matter more than people expect for future job searches — "Associate" vs.
        "Engineer" can change how recruiters filter you years later.</td></tr>
        <tr><td>PTO / professional development budget</td><td>Training budgets and certification reimbursement are
        often easier for companies to grant than cash, and can be worth thousands over a year.</td></tr>
      </table>
    </div>
    <div class="concept-card">
      <span class="concept-label">Concept</span>
      <h4 class="concept-title">A simple, low-stress script for the conversation</h4>
      <p class="concept-desc">You don't need to be a slick negotiator. A calm, direct, appreciative tone works
      better than an aggressive one — and it's far more sustainable for your own nerves:</p>
      <pre class="code-block"><span class="com"># A reasonable, low-drama way to open the conversation:</span>

"Thank you so much for the offer -- I'm genuinely excited about this role
and the team. Before I confirm, I wanted to ask whether there's any
flexibility on the base salary. Based on my research into similar roles
in this market, I was hoping for something closer to $X."

<span class="com"># If they can't move on salary, pivoting is completely normal:</span>

"I understand if there's not room to move on the base right now -- would
there be flexibility on a sign-on bonus, or on the start date? I'd also
love to understand what the path to [next title] typically looks like
on this team."

<span class="com"># And if you decide to accept as-is, that's a perfectly valid outcome too --</span>
<span class="com"># the goal isn't "always get more," it's "never wonder whether you should have asked."</span></pre>
    </div>
    <div class="concept-card">
      <span class="concept-label">Concept</span>
      <h4 class="concept-title">What to do when the answer is "no" — because it sometimes will be</h4>
      <p class="concept-desc">This is where <em>"you can't make someone make the right choice, yet you can pick up
      the pieces afterwards"</em> becomes genuinely useful. You can present your case clearly, professionally, and
      with good research behind it — but you cannot force a hiring manager or a budget committee to say yes. Some
      companies genuinely have no room to move; others simply won't, regardless of how reasonable the ask is.
      Either way, the decision about how to respond stays entirely yours: accept as-is, counter once more, or walk
      away. None of those are failures — they're just different valid endings to a conversation you were right to
      have started.</p>
    </div>
  </div>
</div>
""" + "\n" + A_LIFESTYLE

S_PENTEST = "<!-- BEGINNER47-PENTEST v1 -->"
A_PENTEST = "<!-- /domain-body pentest -->"
C_PENTEST = S_PENTEST + """
<div class="topic">
  <div class="topic-header">
    <span class="topic-badge">Beginner</span>
    <h3>Social Engineering 101 – Why Pretexting Works on Smart People Too</h3>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <span class="concept-label">Concept</span>
      <h4 class="concept-title">Social engineering targets a person, not a system</h4>
      <p class="concept-desc">Every technical control in the world — firewalls, MFA, encryption — can be routed
      around with a single well-placed phone call to the right person at the right moment. <em>Social
      engineering</em> is the practice of manipulating people into taking actions or revealing information they
      normally wouldn't, by exploiting very human instincts: the desire to be helpful, the discomfort of
      questioning authority, and the urge to resolve an "urgent" problem quickly.</p>
      <p class="concept-desc">It's worth saying plainly: falling for a well-executed pretext is not a sign of
      being unintelligent. These techniques are specifically engineered to bypass careful thinking by creating
      time pressure and emotional urgency. Authorized social engineering tests exist to find these gaps
      <em>before</em> a real attacker does — and to build organizational "muscle memory" for spotting them.</p>
    </div>
    <div class="concept-card">
      <span class="concept-label">Concept</span>
      <h4 class="concept-title">Pretexting: building a believable fictional scenario</h4>
      <p class="concept-desc">A <em>pretext</em> is the invented backstory an attacker uses to justify their
      request — "I'm from IT and your account is locked," "I'm a vendor following up on an overdue invoice," "I'm
      the new contractor and I can't find the badge office." The strongest pretexts share a few traits:</p>
      <table class="ai-table">
        <tr><th>Element</th><th>Why it works</th></tr>
        <tr><td>Plausibility</td><td>It fits naturally into the target's normal routine — nothing about it stands
        out as unusual on its own.</td></tr>
        <tr><td>Authority</td><td>It borrows credibility from a role people are conditioned not to question — IT,
        a manager, an auditor, law enforcement.</td></tr>
        <tr><td>Urgency</td><td>It compresses the decision window so the target acts before doubt has time to
        form: "I need this in the next ten minutes or the whole team is blocked."</td></tr>
        <tr><td>A small, reasonable-sounding ask</td><td>Rarely "give me your password." More often "can you just
        confirm the last four digits" or "can you read me the code that just texted you."</td></tr>
      </table>
    </div>
    <div class="concept-card">
      <span class="concept-label">Concept</span>
      <h4 class="concept-title">A walkthrough of a realistic (and entirely plausible) pretext call</h4>
      <pre class="code-block"><span class="com"># A composite example based on patterns seen across real engagements
# (names and details fictionalized):</span>

Caller: "Hi, this is Alex from the IT helpdesk -- we're seeing some
        unusual login attempts on your account and we want to lock
        it down before anything happens. Can you confirm the email
        you usually log in with?"

Target: "Sure, it's j.martinez@company.com"

Caller: "Great, thanks. I'm sending a verification code to that address
        right now to confirm it's really you -- can you read that back
        to me once it arrives? That's how we'll know we're securing the
        right account."

<span class="com"># What's actually happening: the "verification code" is a real
# password-reset code the attacker just triggered. If the target
# reads it back, the attacker now controls the account --
# and the target believed, the entire time, that they were
# the one being protected.</span></pre>
      <p class="concept-desc">Notice that nothing in this script sounds outlandish — that's exactly the point.
      The defense isn't "be more suspicious of everyone forever" (that's exhausting and corrosive to a healthy
      workplace). It's a single habit: <strong>verify identity through a separate, known channel</strong> before
      acting on an unusual request — hang up and call the helpdesk's published number, message your manager
      directly, confirm with the vendor through the contact on file rather than the one the caller provided.</p>
    </div>
    <div class="concept-card">
      <span class="concept-label">Concept</span>
      <h4 class="concept-title">When the test "works," the org learns something — not the employee</h4>
      <p class="concept-desc">A properly run social engineering assessment treats a successful pretext as a
      finding about the <em>organization's</em> processes and training — not a referendum on any one person's
      intelligence or character. <em>"Not my circus, not my monkey"</em> is exactly the wrong instinct here on
      both sides: for the tester, every finding belongs to the org's broader security posture, not just the one
      department tested; and for the employee who got got, it's genuinely everyone's circus — which is precisely
      why the fix is shared training, clear verification procedures, and a culture where saying "let me verify
      that and call you back" is treated as competence, not obstruction.</p>
    </div>
  </div>
</div>
""" + "\n" + A_PENTEST

S_NET = "<!-- BEGINNER47-NET v1 -->"
A_NET = "<!-- /domain-body net -->"
C_NET = S_NET + """
<div class="topic">
  <div class="topic-header">
    <span class="topic-badge">Beginner</span>
    <h3>The TLS Handshake – What Actually Happens Before "https://" Feels Safe</h3>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <span class="concept-label">Concept</span>
      <h4 class="concept-title">The padlock icon represents a surprisingly elegant negotiation</h4>
      <p class="concept-desc">Every time you load an HTTPS site, your browser and the server perform a rapid
      multi-step negotiation called the <em>TLS handshake</em> — establishing trust and agreeing on encryption,
      all before a single byte of your actual page content is transmitted. It happens in well under a second,
      which is part of why it's so easy to never think about. Understanding the broad strokes demystifies a huge
      portion of "how the secure web works."</p>
    </div>
    <div class="concept-card">
      <span class="concept-label">Concept</span>
      <h4 class="concept-title">The handshake in (roughly) five steps</h4>
      <table class="ai-table">
        <tr><th>Step</th><th>What happens</th></tr>
        <tr><td>1. Client Hello</td><td>Your browser says hello and lists the encryption methods ("cipher
        suites") it supports, plus a random number used later in key generation.</td></tr>
        <tr><td>2. Server Hello + Certificate</td><td>The server picks a cipher suite both sides support and sends
        back its <em>digital certificate</em> — proof of identity issued by a trusted Certificate Authority (CA).</td></tr>
        <tr><td>3. Certificate verification</td><td>Your browser checks that the certificate is valid, unexpired,
        matches the domain you're visiting, and was signed by a CA it trusts. This is the step that turns a
        green padlock into something meaningful rather than decorative.</td></tr>
        <tr><td>4. Key exchange</td><td>Both sides use cryptographic math (often Diffie-Hellman) to agree on a
        shared <em>session key</em> — without ever transmitting that key in a form an eavesdropper could use.</td></tr>
        <tr><td>5. Secure session begins</td><td>From here on, all traffic is encrypted with the session key using
        fast symmetric encryption — the certificate-based "slow" cryptography has done its job and steps aside.</td></tr>
      </table>
    </div>
    <div class="concept-card">
      <span class="concept-label">Concept</span>
      <h4 class="concept-title">Inspecting a real certificate from the command line</h4>
      <p class="concept-desc">You don't need special tools to see this in action — <code>openssl</code> can show
      you exactly what your browser is silently checking on every visit:</p>
      <pre class="code-block"><span class="com"># Connect and dump the certificate chain for a domain:</span>
openssl s_client -connect example.com:443 -servername example.com &lt;/dev/null 2&gt;/dev/null | openssl x509 -noout -text

<span class="com"># Useful fields to look for in the output:</span>
<span class="com">#   Issuer:        which Certificate Authority vouched for this site</span>
<span class="com">#   Subject:       the domain(s) the certificate is valid for</span>
<span class="com">#   Validity:      the "Not Before" / "Not After" window -- expired
#                  certificates are a surprisingly common outage cause</span>
<span class="com">#   Signature Algorithm:  the cryptographic method used to sign it</span></pre>
    </div>
    <div class="concept-card">
      <span class="concept-label">Concept</span>
      <h4 class="concept-title">Why "the padlock is green" isn't the same as "this site is trustworthy"</h4>
      <p class="concept-desc">This is a critical distinction that <em>"assume makes an ass out of you and
      me"</em> captures perfectly. TLS guarantees two specific things: that your connection to the server is
      encrypted in transit, and that the certificate matches the domain you typed. It guarantees <strong>nothing
      whatsoever</strong> about whether the organization running that domain is honest, competent, or safe to
      hand your data to. Attackers can — and routinely do — obtain valid certificates for convincingly-misspelled
      lookalike domains. The padlock confirms "this connection isn't being eavesdropped on right now." It does
      not confirm "you should trust what's on the other end of it." Those are two different questions, and
      conflating them is one of the most common (and most exploited) assumptions on the web.</p>
    </div>
  </div>
</div>
""" + "\n" + A_NET


def inject(html, anchor, sentinel, content):
    if sentinel in html:
        return html, False
    idx = html.find(anchor)
    if idx == -1:
        raise SystemExit(f"Anchor not found: {anchor}")
    return html[:idx] + content + "\n" + html[idx:], True


VOID_ELEMENTS = {"area", "base", "br", "col", "embed", "hr", "img", "input",
                 "link", "meta", "param", "source", "track", "wbr"}


class _Checker(HTMLParser):
    def __init__(self):
        super().__init__()
        self.stack = []
        self.stray = 0

    def handle_starttag(self, tag, attrs):
        if tag not in VOID_ELEMENTS:
            self.stack.append(tag)

    def handle_startendtag(self, tag, attrs):
        pass

    def handle_endtag(self, tag):
        if tag in VOID_ELEMENTS:
            return
        if self.stack and self.stack[-1] == tag:
            self.stack.pop()
        elif tag in self.stack:
            while self.stack and self.stack[-1] != tag:
                self.stack.pop()
            if self.stack:
                self.stack.pop()
        else:
            self.stray += 1


def validate(html):
    c = _Checker()
    c.feed(html)
    c.close()
    print("\n  HTML balance check:")
    print("  Unclosed at EOF :", "NONE" if not c.stack else c.stack)
    print("  Stray end tags  :", c.stray)


WAVES = [
    (A_GRC, S_GRC, C_GRC),
    (A_LINUX, S_LINUX, C_LINUX),
    (A_LIFESTYLE, S_LIFESTYLE, C_LIFESTYLE),
    (A_PENTEST, S_PENTEST, C_PENTEST),
    (A_NET, S_NET, C_NET),
]


def main():
    path = "index.html"
    with open(path, "r", encoding="utf-8") as f:
        html = f.read()

    changed_any = False
    for anchor, sentinel, content in WAVES:
        html, changed = inject(html, anchor, sentinel, content)
        print(f"  {sentinel}: {'INJECTED' if changed else 'skipped (already present)'}")
        changed_any = changed_any or changed

    if changed_any:
        with open(path, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"\n  Written {len(html):,} bytes")
    else:
        print("\n  No changes made (all sentinels already present)")

    validate(html)


if __name__ == "__main__":
    main()
