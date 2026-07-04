#!/usr/bin/env python3
"""Wave 43: beginner-friendly content additions across 5 domains."""
import re
from html.parser import HTMLParser

S_NET = "<!-- BEGINNER43-NET v1 -->"
A_NET = "<!-- /domain-body net -->"
C_NET = S_NET + """
<div class="topic">
  <div class="topic-header">
    <span class="topic-badge">Beginner</span>
    <h3>Subnetting Without the Headache – CIDR Notation Made Practical</h3>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <span class="concept-label">Concept</span>
      <h4 class="concept-title">A subnet is just "how big is this neighborhood?"</h4>
      <p class="concept-desc">An IP address tells you a device's location; a subnet mask tells you how many of its
      neighbors share the same local "neighborhood" — the group of addresses that can talk to each other directly,
      without going through a router. CIDR notation (<code>/24</code>, <code>/26</code>, etc.) is just a compact way of
      writing that mask: the number after the slash tells you how many bits are reserved for identifying the network
      itself, leaving the rest for individual hosts.</p>
    </div>
    <div class="concept-card">
      <span class="concept-label">Concept</span>
      <h4 class="concept-title">The CIDR cheat sheet beginners actually reach for</h4>
      <table class="ai-table">
        <tr><th>CIDR</th><th>Subnet mask</th><th>Usable hosts</th><th>Common use</th></tr>
        <tr><td>/24</td><td>255.255.255.0</td><td>254</td><td>Typical small office or home network</td></tr>
        <tr><td>/25</td><td>255.255.255.128</td><td>126</td><td>Splitting a /24 in half — two departments, one building</td></tr>
        <tr><td>/26</td><td>255.255.255.192</td><td>62</td><td>A single floor or smaller team</td></tr>
        <tr><td>/27</td><td>255.255.255.224</td><td>30</td><td>A small lab, a rack of servers, a point-to-point link group</td></tr>
        <tr><td>/30</td><td>255.255.255.252</td><td>2</td><td>A direct link between two routers — exactly enough for both ends</td></tr>
      </table>
      <p class="concept-desc">Notice the pattern: every step from /24 toward /32 cuts the available addresses roughly in
      half. "Usable hosts" is two less than the raw count — one address is reserved to identify the network itself, and
      one is reserved as the broadcast address that reaches every device in that subnet at once.</p>
    </div>
    <div class="concept-card">
      <span class="concept-label">Hands-on</span>
      <h4 class="concept-title">Let the tools do the arithmetic — verify, don't memorize</h4>
      <pre class="code-block"><span class="com"># pip install — actually it's built into Python's standard library!</span>
<span class="kw">import</span> ipaddress

network = ipaddress.ip_network(<span class="str">&quot;192.168.10.0/26&quot;</span>)
<span class="fn">print</span>(<span class="str">f&quot;Network address:   {network.network_address}&quot;</span>)
<span class="fn">print</span>(<span class="str">f&quot;Broadcast address: {network.broadcast_address}&quot;</span>)
<span class="fn">print</span>(<span class="str">f&quot;Usable hosts:      {network.num_addresses - 2}&quot;</span>)
<span class="fn">print</span>(<span class="str">f&quot;First usable host: {list(network.hosts())[0]}&quot;</span>)
<span class="fn">print</span>(<span class="str">f&quot;Last usable host:  {list(network.hosts())[-1]}&quot;</span>)

<span class="com"># Quick check: is this address inside that subnet?</span>
ip = ipaddress.ip_address(<span class="str">&quot;192.168.10.40&quot;</span>)
<span class="fn">print</span>(<span class="str">f&quot;{ip} in {network}? {ip in network}&quot;</span>)

<span class="com"># Splitting a network into smaller subnets — handy for planning
# departmental allocations from a single block you've been given</span>
<span class="kw">for</span> sub <span class="kw">in</span> network.subnets(new_prefix=28):
    <span class="fn">print</span>(<span class="str">f&quot;  Sub-block: {sub}&quot;</span>)</pre>
      <p class="concept-desc">This is the honest secret of subnetting: nobody who works with networks daily does the binary
      math by hand every time. They've internalized the cheat-sheet patterns for common cases, and they reach for a
      calculator (or <span class="kw">ipaddress</span>, or <span class="kw">ipcalc</span> on the command line) to double-check
      anything unusual. Knowing how it works conceptually — and knowing how to verify it — beats memorizing tables you'll
      forget under pressure.</p>
    </div>
    <div class="concept-card">
      <span class="concept-label">Mindset</span>
      <h4 class="concept-title">Assume makes an ass out of you and me</h4>
      <p class="concept-desc">"That device should be able to reach the server, they're both on the 192.168.x.x range" is a
      classic trap — two addresses can look similar and still be in completely different subnets, unable to communicate
      without a router between them. Before troubleshooting further up the stack, verify the actual subnet boundaries
      with a tool like the one above rather than eyeballing the addresses and assuming they're neighbors.</p>
    </div>
  </div>
</div>
""" + "\n" + A_NET

S_LINUX = "<!-- BEGINNER43-LINUX v1 -->"
A_LINUX = "<!-- /domain-body linux -->"
C_LINUX = S_LINUX + """
<div class="topic">
  <div class="topic-header">
    <span class="topic-badge">Beginner</span>
    <h3>File Permissions Demystified – rwx, Octal Notation, and chmod</h3>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <span class="concept-label">Concept</span>
      <h4 class="concept-title">Reading the permission string, left to right</h4>
      <p class="concept-desc">Run <code>ls -l</code> and you'll see a string like <code>-rwxr-xr--</code> at the start of
      each line. It looks cryptic until you break it into four pieces:</p>
      <table class="ai-table">
        <tr><th>Position</th><th>Means</th><th>In <code>-rwxr-xr--</code></th></tr>
        <tr><td>1st character</td><td>File type: <code>-</code> regular file, <code>d</code> directory, <code>l</code> symlink</td><td><code>-</code> (a regular file)</td></tr>
        <tr><td>Characters 2-4</td><td>Owner's permissions: read, write, execute</td><td><code>rwx</code> — owner can do all three</td></tr>
        <tr><td>Characters 5-7</td><td>Group's permissions</td><td><code>r-x</code> — group can read and execute, not write</td></tr>
        <tr><td>Characters 8-10</td><td>Everyone else's permissions</td><td><code>r--</code> — others can only read</td></tr>
      </table>
      <p class="concept-desc">For a directory, the meaning of each letter shifts slightly: <span class="kw">r</span> lets
      you list its contents, <span class="kw">w</span> lets you create/delete files inside it, and <span class="kw">x</span>
      lets you actually <em>enter</em> it (via <code>cd</code>) or access files inside by full path. A directory with
      <code>r--</code> but no <code>x</code> is a common source of confusing "permission denied" errors — you can see
      what's there but can't actually get in.</p>
    </div>
    <div class="concept-card">
      <span class="concept-label">Concept</span>
      <h4 class="concept-title">Octal notation: the same thing, in a faster shorthand</h4>
      <p class="concept-desc">Each <span class="kw">rwx</span> triplet can be represented as a single digit by adding up
      values: read = 4, write = 2, execute = 1. So <code>rwx</code> = 4+2+1 = <strong>7</strong>, <code>r-x</code> = 4+0+1 =
      <strong>5</strong>, and <code>r--</code> = 4+0+0 = <strong>4</strong>. That makes <code>-rwxr-xr--</code> equivalent
      to the much more typeable <code>754</code> — which is exactly the form you'll see in <span class="kw">chmod</span>
      commands and deployment scripts everywhere.</p>
      <table class="ai-table">
        <tr><th>Octal digit</th><th>Permissions granted</th><th>Common use</th></tr>
        <tr><td>7</td><td>rwx — read, write, execute</td><td>Scripts and programs you own and run</td></tr>
        <tr><td>6</td><td>rw- — read and write, no execute</td><td>Regular documents and config files</td></tr>
        <tr><td>5</td><td>r-x — read and execute, no write</td><td>Shared programs others should run but not modify</td></tr>
        <tr><td>4</td><td>r-- — read only</td><td>Reference files nobody but the owner should change</td></tr>
      </table>
    </div>
    <div class="concept-card">
      <span class="concept-label">Hands-on</span>
      <h4 class="concept-title">Setting permissions deliberately</h4>
      <pre class="code-block"><span class="com"># View permissions in detail</span>
ls -l deploy.sh

<span class="com"># Make a script executable for the owner only — common for personal scripts</span>
chmod 700 deploy.sh
<span class="com"># Result: rwx------  (owner: full control, everyone else: nothing)</span>

<span class="com"># Make a shared script runnable by the whole team, editable only by the owner</span>
chmod 755 deploy.sh
<span class="com"># Result: rwxr-xr-x  (owner: full, group/others: read+execute)</span>

<span class="com"># Symbolic form — same end result, sometimes clearer to read in scripts</span>
chmod u=rwx,g=rx,o=rx deploy.sh

<span class="com"># Add execute permission without disturbing existing read/write bits</span>
chmod +x deploy.sh

<span class="com"># Recursively fix an entire directory tree (use carefully!)</span>
chmod -R u=rwX,g=rX,o= /opt/myapp</pre>
    </div>
    <div class="concept-card">
      <span class="concept-label">Mindset</span>
      <h4 class="concept-title">"chmod 777 it" is the duct tape of permissions — and just as ugly under the surface</h4>
      <p class="concept-desc"><span class="kw">chmod 777</span> grants read, write, and execute to literally everyone — the
      owner, the group, and every other user on the system. It "fixes" almost any permission error instantly, which is
      exactly why it spreads through forums and Stack Overflow answers as a quick solution. <strong>Assume makes an ass
      out of you and me</strong>: assuming "wide open" is harmless because "it's just my home lab" is how a small
      convenience habit becomes a real vulnerability the day that file matters. Take the extra thirty seconds to figure
      out the <em>narrowest</em> permission that actually solves the problem — your future self (and anyone auditing the
      system later) will thank you.</p>
    </div>
  </div>
</div>
""" + "\n" + A_LINUX

S_THREAT = "<!-- BEGINNER43-THREAT v1 -->"
A_THREAT = "<!-- /domain-body threat -->"
C_THREAT = S_THREAT + """
<div class="topic">
  <div class="topic-header">
    <span class="topic-badge">Beginner</span>
    <h3>Open-Source Intelligence (OSINT) – What's Already Public About You</h3>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <span class="concept-label">Concept</span>
      <h4 class="concept-title">OSINT is intelligence gathered from things that are already public</h4>
      <p class="concept-desc">Open-Source Intelligence means collecting and analyzing information from publicly available
      sources — social media, company websites, public records, code repositories, even old cached pages — to build a
      picture of a person or organization. It requires no hacking and breaks no laws on its own; the "open" in the name
      is the whole point. Understanding OSINT matters for two very different reasons: attackers use it during the
      reconnaissance phase of an intrusion (recall the Cyber Kill Chain's first stage), and defenders use the exact same
      techniques to find out what an attacker could learn about their own organization before someone else does.</p>
    </div>
    <div class="concept-card">
      <span class="concept-label">Concept</span>
      <h4 class="concept-title">What attackers commonly piece together — and from where</h4>
      <table class="ai-table">
        <tr><th>Information</th><th>Common public sources</th><th>How it gets used</th></tr>
        <tr><td>Employee names &amp; roles</td><td>LinkedIn, company "About Us" pages, conference speaker lists</td><td>Crafting believable spear-phishing emails ("Hi, this is Dana from IT...")</td></tr>
        <tr><td>Technology stack</td><td>Job postings ("must know AWS, Kubernetes, Salesforce"), public code repos</td><td>Targeting known vulnerabilities in the specific tools an org uses</td></tr>
        <tr><td>Email address format</td><td>Press releases, public filings, "contact us" pages</td><td>Guessing other employees' addresses (firstname.lastname@company.com)</td></tr>
        <tr><td>Physical &amp; schedule details</td><td>Social media check-ins, out-of-office replies, event listings</td><td>Timing attacks for when key personnel are away or distracted</td></tr>
      </table>
    </div>
    <div class="concept-card">
      <span class="concept-label">Hands-on (lab/personal use only)</span>
      <h4 class="concept-title">Running your own OSINT check on yourself or your org</h4>
      <pre class="code-block"><span class="com"># See what Google has indexed about a domain — often more than expected</span>
site:example.com filetype:pdf
site:example.com &quot;confidential&quot;

<span class="com"># Check what WHOIS records reveal about a domain's registration</span>
whois example.com | grep -iE &quot;registrant|admin|tech&quot;

<span class="com"># Look up historical versions of a public page — sometimes old,
# supposedly-removed information is still archived</span>
<span class="com"># https://web.archive.org/web/*/example.com</span>

<span class="com"># Search for exposed credentials tied to a domain (read-only check —
# this is the same database breach-notification services use)</span>
<span class="com"># https://haveibeenpwned.com/DomainSearch (requires domain verification)</span>

<span class="com"># Review what a public GitHub org has accidentally exposed —
# old commits sometimes contain credentials that were later "removed"
# but remain in the git history forever</span>
git log -p --all | grep -iE &quot;password|secret|api[_-]?key&quot;</pre>
      <p class="concept-desc">That last command is worth sitting with — deleting a sensitive line from the latest commit
      does <em>not</em> remove it from history. Anyone who clones the repository can still find it with a simple search.
      This is one of the most common, entirely preventable ways organizations leak credentials.</p>
    </div>
    <div class="concept-card">
      <span class="concept-label">Mindset</span>
      <h4 class="concept-title">Not my circus, not my monkey — except your digital footprint is always yours</h4>
      <p class="concept-desc">It's easy to assume "I'm not important enough to be a target" — but OSINT-driven attacks
      rarely target individuals for who they are; they target whoever happens to be reachable and useful as a stepping
      stone toward something bigger (a company network, a family member, a connected account). Periodically searching
      your own name, checking what your old social media posts reveal, and reviewing what your employer has published
      about you isn't paranoia — it's the same "know what's exposed before someone else finds it" thinking that
      professional security teams apply to entire organizations, just scaled down to one person.</p>
    </div>
  </div>
</div>
""" + "\n" + A_THREAT

S_GRC = "<!-- BEGINNER43-GRC v1 -->"
A_GRC = "<!-- /domain-body grc -->"
C_GRC = S_GRC + """
<div class="topic">
  <div class="topic-header">
    <span class="topic-badge">Beginner</span>
    <h3>Reading a SOC 2 Report Without Falling Asleep</h3>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <span class="concept-label">Concept</span>
      <h4 class="concept-title">A SOC 2 report answers one question: "can we trust how this vendor handles our data?"</h4>
      <p class="concept-desc">SOC 2 (System and Organization Controls 2) is an independent auditor's report on how well a
      service organization's controls protect customer data. When your company evaluates a new SaaS vendor, "can you send
      us your SOC 2 report?" is one of the single most useful questions you can ask — it's a third party's documented,
      evidence-based opinion, rather than the vendor's own marketing claims about how seriously they take security.</p>
    </div>
    <div class="concept-card">
      <span class="concept-label">Concept</span>
      <h4 class="concept-title">The five Trust Services Criteria — and the one that's always included</h4>
      <table class="ai-table">
        <tr><th>Criterion</th><th>What it covers</th><th>Always included?</th></tr>
        <tr><td>Security</td><td>Protection against unauthorized access, both physical and logical</td><td>Yes — the mandatory baseline for every SOC 2 report</td></tr>
        <tr><td>Availability</td><td>Whether the system is operational and accessible as agreed/committed</td><td>Optional — included if relevant to the service</td></tr>
        <tr><td>Processing integrity</td><td>Whether the system processes data completely, accurately, and on time</td><td>Optional</td></tr>
        <tr><td>Confidentiality</td><td>Whether information designated as confidential is protected as promised</td><td>Optional</td></tr>
        <tr><td>Privacy</td><td>How personal information is collected, used, retained, and disposed of</td><td>Optional</td></tr>
      </table>
      <p class="concept-desc">A vendor handling highly sensitive customer data but only reporting on "Security" isn't
      necessarily hiding something — but it's a perfectly reasonable thing to ask about directly: "why isn't
      Confidentiality or Privacy included in your scope?"</p>
    </div>
    <div class="concept-card">
      <span class="concept-label">Concept</span>
      <h4 class="concept-title">Type I vs Type II — a snapshot vs. a track record</h4>
      <p class="concept-desc">This distinction trips up almost everyone the first time they encounter it, and it matters
      enormously:</p>
      <table class="ai-table">
        <tr><th>Report type</th><th>What it actually verifies</th><th>How much weight to give it</th></tr>
        <tr><td>Type I</td><td>"As of this one specific date, these controls were designed appropriately"</td><td>A snapshot — tells you the controls exist on paper, but not whether they actually work day to day</td></tr>
        <tr><td>Type II</td><td>"Over a period of months (often 6-12), these controls were tested and operated effectively"</td><td>Significantly stronger evidence — this is the one most procurement teams actually want to see</td></tr>
      </table>
      <p class="concept-desc">A vendor proudly waving a Type I report is, in effect, saying "we wrote down a good plan."
      A Type II report says "we followed that plan for months, and an independent auditor checked our work." If a vendor
      only has Type I, a reasonable follow-up is simply: "when do you expect to have a Type II?"</p>
    </div>
    <div class="concept-card">
      <span class="concept-label">Mindset</span>
      <h4 class="concept-title">Assume makes an ass out of you and me — read the exceptions section</h4>
      <p class="concept-desc">The most informative part of a SOC 2 report is often the section listing <em>exceptions</em>
      — instances where a control didn't operate as intended during the review period. A report with zero exceptions
      listed isn't necessarily "perfect"; sometimes it means the scope was narrow enough that nothing challenging was
      tested. A report with a few well-documented exceptions and clear remediation notes can actually be a *more*
      trustworthy signal — it shows the audit was rigorous enough to find something, and the vendor was transparent
      enough to disclose it rather than bury it.</p>
    </div>
  </div>
</div>
""" + "\n" + A_GRC

S_LIFESTYLE = "<!-- BEGINNER43-LIFESTYLE v1 -->"
A_LIFESTYLE = "<!-- /domain-body lifestyle -->"
C_LIFESTYLE = S_LIFESTYLE + """
<div class="topic">
  <div class="topic-header">
    <span class="topic-badge">Beginner</span>
    <h3>Surviving (and Thriving In) Your First On-Call Rotation</h3>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <span class="concept-label">Why this matters</span>
      <h4 class="concept-title">Everyone remembers their first page</h4>
      <p class="concept-desc">Being on-call means carrying responsibility for responding to issues outside normal working
      hours — and for most people new to it, the first 2 AM page triggers a flood of adrenaline that makes clear thinking
      surprisingly hard. That reaction is completely normal. The goal of preparing for on-call isn't to eliminate that
      feeling — it's to have enough structure in place that you can function well *despite* it.</p>
    </div>
    <div class="concept-card">
      <span class="concept-label">Concept</span>
      <h4 class="concept-title">The five-minute checklist for "I just got paged"</h4>
      <table class="ai-table">
        <tr><th>Step</th><th>What to do</th><th>Why it helps</th></tr>
        <tr><td>1. Acknowledge first</td><td>Hit "acknowledge" in your paging tool before doing anything else</td><td>Stops the alert from escalating to someone else, and signals "I've got this"</td></tr>
        <tr><td>2. Read before you act</td><td>Actually read the alert text and any linked runbook — don't start typing commands from memory</td><td>Half of "wrong fix" stories start with skipping this step while half-asleep</td></tr>
        <tr><td>3. Assess blast radius</td><td>Is this affecting one customer or all of them? One service or several?</td><td>Determines whether you handle it solo or escalate immediately</td></tr>
        <tr><td>4. Follow the runbook</td><td>If one exists for this alert, follow it — don't improvise a "better" approach at 3 AM</td><td>3 AM you is not as clever as you feel; trust daytime you's preparation</td></tr>
        <tr><td>5. When in doubt, escalate</td><td>Waking up a second person is a minor inconvenience; a worsened outage is not</td><td>No one who matters will ever fault you for escalating a real problem</td></tr>
      </table>
    </div>
    <div class="concept-card">
      <span class="concept-label">Hands-on</span>
      <h4 class="concept-title">Preparing your "on-call kit" before your rotation starts</h4>
      <pre class="code-block"><span class="com"># Things to set up and verify BEFORE your first on-call shift begins —
# not during your first incident</span>

<span class="com"># 1. Confirm your paging app actually wakes you up
#    (test it during the day — set it to override silent/DND mode)</span>

<span class="com"># 2. Bookmark the runbooks for the services you're covering
#    — know where they live before you need them under pressure</span>

<span class="com"># 3. Make sure your laptop, VPN, and credentials all actually work
#    from outside the office network — discovering an expired VPN
#    cert during a live incident is a uniquely bad way to start a shift</span>

<span class="com"># 4. Know EXACTLY who to escalate to and how — name, contact method,
#    and what counts as a good reason to wake them up</span>

<span class="com"># 5. Keep a notes file or doc open during your shift — jot down what
#    you tried and what happened. Future-you writing the postmortem
#    will be enormously grateful to past-you for these notes</span></pre>
    </div>
    <div class="concept-card">
      <span class="concept-label">Mindset</span>
      <h4 class="concept-title">You can't make someone make the right choice...</h4>
      <p class="concept-desc"><strong>...yet you can pick up the pieces afterwards.</strong> At some point during your
      on-call career, you (or a teammate) will make the wrong call under pressure — escalate when it wasn't needed,
      or not escalate when it was. That's not a personal failing; it's an inherent risk of making time-pressured
      decisions with incomplete information. What separates healthy on-call cultures from miserable ones is what happens
      next: a blameless retrospective that asks "how do we make the right choice easier to find next time?" rather than
      "whose fault was this?" The first builds better systems and braver engineers. The second just teaches people to
      hide their mistakes — which is far more dangerous in the long run.</p>
    </div>
  </div>
</div>
""" + "\n" + A_LIFESTYLE


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
    (A_NET, S_NET, C_NET),
    (A_LINUX, S_LINUX, C_LINUX),
    (A_THREAT, S_THREAT, C_THREAT),
    (A_GRC, S_GRC, C_GRC),
    (A_LIFESTYLE, S_LIFESTYLE, C_LIFESTYLE),
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
