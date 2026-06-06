#!/usr/bin/env python3
"""Wave 44: beginner-friendly content additions across 5 domains."""
import re
from html.parser import HTMLParser

S_PENTEST = "<!-- BEGINNER44-PENTEST v1 -->"
A_PENTEST = "<!-- /domain-body pentest -->"
C_PENTEST = S_PENTEST + """
<div class="topic">
  <div class="topic-header">
    <span class="topic-badge">Beginner</span>
    <h3>Web App Basics – Finding Your First IDOR (Lab Practice)</h3>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <span class="concept-label">Scope first</span>
      <h4 class="concept-title">Practice on intentionally vulnerable apps, not live targets</h4>
      <p class="concept-desc">IDOR (Insecure Direct Object Reference) is one of the most common — and most beginner-friendly
      — web vulnerabilities to learn, because it requires no special tools, just careful observation and a willingness to
      change one number in a URL. Practice it on platforms built for that purpose: OWASP Juice Shop, DVWA, PortSwigger's
      free Web Security Academy labs, or HackTheBox/TryHackMe boxes. Trying this against a real company's website without
      written authorization is unauthorized access — full stop, regardless of how "easy" the bug looks.</p>
    </div>
    <div class="concept-card">
      <span class="concept-label">Concept</span>
      <h4 class="concept-title">The bug, in one sentence</h4>
      <p class="concept-desc">An IDOR happens when an application lets you access an object — an invoice, a user profile,
      an uploaded file — purely by referencing its ID, <em>without checking whether you're actually allowed to see it</em>.
      The application correctly checks "are you logged in?" but skips the second, equally important question: "are you
      logged in as someone who's allowed to see <strong>this specific</strong> thing?"</p>
    </div>
    <div class="concept-card">
      <span class="concept-label">Hands-on (lab only)</span>
      <h4 class="concept-title">Spotting the pattern</h4>
      <pre class="code-block"><span class="com"># You log in as yourself and view your own invoice. The URL looks like:</span>
https://shop.example.lab/invoices/4471

<span class="com"># Out of curiosity, you change the number by one:</span>
https://shop.example.lab/invoices/4470

<span class="com"># If the application returns SOMEONE ELSE'S invoice — full name,
# address, items purchased — instead of an "access denied" page,
# you've just found an IDOR. The fix the developer needs to make
# is conceptually simple:</span>

<span class="com"># VULNERABLE — trusts the ID in the URL completely</span>
<span class="kw">def</span> <span class="fn">get_invoice</span>(invoice_id):
    <span class="kw">return</span> db.query(<span class="str">&quot;SELECT * FROM invoices WHERE id = ?&quot;</span>, invoice_id)

<span class="com"># FIXED — also verifies the invoice actually belongs to the requester</span>
<span class="kw">def</span> <span class="fn">get_invoice</span>(invoice_id, current_user):
    invoice = db.query(<span class="str">&quot;SELECT * FROM invoices WHERE id = ?&quot;</span>, invoice_id)
    <span class="kw">if</span> invoice <span class="kw">is</span> <span class="kw">None</span> <span class="kw">or</span> invoice.owner_id != current_user.id:
        <span class="kw">raise</span> PermissionError(<span class="str">&quot;Not your invoice&quot;</span>)
    <span class="kw">return</span> invoice</pre>
      <p class="concept-desc">That's genuinely the whole bug class — "the server checked *what* but not *who*." Once you
      can spot the pattern, you'll start noticing it in URLs, API requests, and form fields everywhere: numeric IDs,
      sequential filenames, predictable tokens. The hunting skill transfers far more than any specific tool does.</p>
    </div>
    <div class="concept-card">
      <span class="concept-label">Mindset</span>
      <h4 class="concept-title">Assume makes an ass out of you and me — including about your own code</h4>
      <p class="concept-desc">If you're the one writing the application, the natural assumption is "well, why would
      anyone change the number in the URL?" That single assumption is the entire vulnerability. Defensive development
      means assuming every input — URL parameters, form fields, API payloads, cookies — will eventually be tampered with
      by someone curious, malicious, or simply running an automated scanner, and verifying authorization on every single
      request rather than trusting that users will only ask for things they're "supposed to."</p>
    </div>
  </div>
</div>
""" + "\n" + A_PENTEST

S_AI = "<!-- BEGINNER44-AI v1 -->"
A_AI = "<!-- /domain-body ai -->"
C_AI = S_AI + """
<div class="topic">
  <div class="topic-header">
    <span class="topic-badge">Beginner</span>
    <h3>Fine-Tuning vs. Prompting vs. RAG – Picking the Right Tool</h3>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <span class="concept-label">Concept</span>
      <h4 class="concept-title">Three different ways to make an AI behave the way you need</h4>
      <p class="concept-desc">A common beginner question is "how do I make the model know about <em>my</em> stuff?" — and
      there are three quite different answers, each suited to a different kind of problem. Picking the wrong one is one
      of the most expensive mistakes teams make when adopting AI: spending months fine-tuning a model when a well-written
      prompt would have solved the problem in an afternoon, or vice versa.</p>
    </div>
    <div class="concept-card">
      <span class="concept-label">Concept</span>
      <h4 class="concept-title">Side-by-side comparison</h4>
      <table class="ai-table">
        <tr><th>Approach</th><th>What it actually does</th><th>Best for</th><th>Cost / effort</th></tr>
        <tr><td>Prompting</td><td>Carefully writing your instructions and examples directly into each request</td><td>Quick experiments, well-defined tasks, "explain this in the style of a 5-year-old"</td><td>Lowest — just your time writing and iterating</td></tr>
        <tr><td>RAG (retrieval-augmented generation)</td><td>Looking up relevant documents at request time and including them in the prompt</td><td>Answering questions about specific, changing, or proprietary documents (your company's wiki, recent tickets)</td><td>Moderate — needs a document pipeline and a vector database, but no model training</td></tr>
        <tr><td>Fine-tuning</td><td>Further training an existing model on your own examples so its underlying behavior changes</td><td>Teaching a consistent style, format, or specialized skill across thousands of interactions</td><td>Highest — needs quality training data, compute, and ongoing maintenance as the base model updates</td></tr>
      </table>
    </div>
    <div class="concept-card">
      <span class="concept-label">Concept</span>
      <h4 class="concept-title">A simple decision guide</h4>
      <pre class="code-block"><span class="com"># Ask yourself, in order:</span>

<span class="com"># 1. "Can I solve this by just writing better instructions?"</span>
<span class="kw">if</span> problem_is_about_HOW_the_model_responds:
    <span class="fn">use</span>(<span class="str">&quot;prompting — try this FIRST, always&quot;</span>)

<span class="com"># 2. "Does the model need to know about specific facts or
#     documents that change over time or are private to me?"</span>
<span class="kw">elif</span> problem_is_about_WHAT_the_model_knows <span class="kw">and</span> data_changes_often:
    <span class="fn">use</span>(<span class="str">&quot;RAG — retrieval keeps the model current without retraining&quot;</span>)

<span class="com"># 3. "Do I need the model to consistently behave a certain way
#     across thousands of cases, in a way prompting can't reliably achieve?"</span>
<span class="kw">elif</span> need_consistent_specialized_behavior_at_scale:
    <span class="fn">use</span>(<span class="str">&quot;fine-tuning — but only after prompting and RAG fall short&quot;</span>)

<span class="com"># Most real problems are solved at step 1 or step 2.
# Step 3 is rarer than people assume when they first hear about it.</span></pre>
    </div>
    <div class="concept-card">
      <span class="concept-label">Mindset</span>
      <h4 class="concept-title">Assume makes an ass out of you and me</h4>
      <p class="concept-desc">"We need to fine-tune a model" is a conclusion people often jump to because it <em>sounds</em>
      like the sophisticated, serious answer — when a focused system prompt and a couple of good examples would have
      gotten 90% of the way there for a fraction of the cost and complexity. Before committing to the most expensive
      option, it's worth actually testing whether the cheaper ones fail — rather than assuming they will.</p>
    </div>
  </div>
</div>
""" + "\n" + A_AI

S_SEC = "<!-- BEGINNER44-SEC v1 -->"
A_SEC = "<!-- /domain-body sec -->"
C_SEC = S_SEC + """
<div class="topic">
  <div class="topic-header">
    <span class="topic-badge">Beginner</span>
    <h3>Zero Trust – "Never Trust, Always Verify" Explained Simply</h3>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <span class="concept-label">Concept</span>
      <h4 class="concept-title">The old model: a castle with a moat</h4>
      <p class="concept-desc">Traditional network security worked like a medieval castle — build strong walls (firewalls)
      around the perimeter, and trust everything inside them. Once you were "inside the network," you were generally
      treated as trustworthy by default. This worked reasonably well when "inside the network" meant "physically in the
      building, on a company-owned computer." It works far less well in a world of remote work, cloud services, personal
      devices, and contractors — where the very idea of a single, defensible "inside" has mostly dissolved.</p>
    </div>
    <div class="concept-card">
      <span class="concept-label">Concept</span>
      <h4 class="concept-title">Zero Trust flips the assumption</h4>
      <p class="concept-desc">Zero Trust starts from a different premise: <strong>don't automatically trust anything,
      whether it's inside or outside the network</strong> — verify every request, every time, based on who's asking, what
      they're asking for, and the context they're asking from. The name sounds extreme, but the underlying idea is closer
      to "trust, but continuously re-verify" than "trust no one ever." A useful mental model: instead of one big castle
      wall, imagine every single room has its own locked door and its own ID check — including rooms you're already inside.</p>
      <table class="ai-table">
        <tr><th>Castle-and-moat thinking</th><th>Zero Trust thinking</th></tr>
        <tr><td>"You're on the VPN, so you must be legitimate"</td><td>"You're on the VPN — now let's also verify your device is patched, your identity via MFA, and that this specific request makes sense for your role"</td></tr>
        <tr><td>One login grants broad access to "the network"</td><td>Each request to each resource is evaluated on its own merits, continuously</td></tr>
        <tr><td>Internal traffic is implicitly trusted</td><td>Internal traffic is monitored and verified just like external traffic</td></tr>
      </table>
    </div>
    <div class="concept-card">
      <span class="concept-label">Concept</span>
      <h4 class="concept-title">The building blocks you'll hear about</h4>
      <table class="ai-table">
        <tr><th>Component</th><th>What it contributes</th></tr>
        <tr><td>Strong identity verification (MFA)</td><td>Confirms "you are who you say you are" before granting anything</td></tr>
        <tr><td>Least-privilege access</td><td>You only get access to exactly what your role requires — nothing "just in case"</td></tr>
        <tr><td>Micro-segmentation</td><td>The network is divided into small zones, so a breach in one area can't freely spread to others</td></tr>
        <tr><td>Continuous monitoring</td><td>Behavior is watched constantly — a login from a new country at 3 AM is a signal worth checking, even from a "trusted" account</td></tr>
        <tr><td>Device health checks</td><td>Access can depend on whether the requesting device is patched, encrypted, and free of known malware</td></tr>
      </table>
    </div>
    <div class="concept-card">
      <span class="concept-label">Mindset</span>
      <h4 class="concept-title">Assume makes an ass out of you and me — the philosophy in one phrase</h4>
      <p class="concept-desc">If you remember nothing else about Zero Trust, remember this: it is, in essence, "assume
      makes an ass out of you and me," turned into an architecture. Every assumption that something is safe because of
      *where* it's coming from — "it's an internal IP," "it's a company laptop," "they logged in successfully an hour
      ago" — is exactly the kind of assumption attackers count on defenders making. Zero Trust simply builds systems that
      verify instead of assume, by design, every single time.</p>
    </div>
  </div>
</div>
""" + "\n" + A_SEC

S_SCRIPT = "<!-- BEGINNER44-SCRIPT v1 -->"
A_SCRIPT = "<!-- /domain-body script -->"
C_SCRIPT = S_SCRIPT + """
<div class="topic">
  <div class="topic-header">
    <span class="topic-badge">Beginner</span>
    <h3>Regular Expressions – A Survival Guide for IT Tasks</h3>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <span class="concept-label">Concept</span>
      <h4 class="concept-title">Regex is "find by pattern" instead of "find by exact text"</h4>
      <p class="concept-desc">A regular expression is a mini-language for describing patterns in text — instead of
      searching for the literal string "192.168.1.1", you can search for "anything that looks like an IPv4 address."
      That shift — from matching exact text to matching <em>shapes</em> of text — is what makes regex so powerful for log
      analysis, data validation, and bulk text processing. It has a reputation for looking like line noise, but a
      relatively small set of building blocks covers the vast majority of real IT use cases.</p>
    </div>
    <div class="concept-card">
      <span class="concept-label">Reference</span>
      <h4 class="concept-title">The building blocks that cover 80% of cases</h4>
      <table class="ai-table">
        <tr><th>Pattern</th><th>Matches</th><th>Example</th></tr>
        <tr><td><code>\\d</code></td><td>Any single digit (0-9)</td><td><code>\\d\\d\\d</code> matches "404", "500", "200"</td></tr>
        <tr><td><code>\\w</code></td><td>Any "word" character — letters, digits, underscore</td><td><code>\\w+</code> matches "username_42"</td></tr>
        <tr><td><code>\\s</code></td><td>Any whitespace — space, tab, newline</td><td>Useful for splitting on flexible spacing in logs</td></tr>
        <tr><td><code>+</code></td><td>"One or more" of the thing before it</td><td><code>\\d+</code> matches "5", "404", "1000000"</td></tr>
        <tr><td><code>*</code></td><td>"Zero or more" of the thing before it</td><td><code>colou*r</code> matches both "color" and "colour"</td></tr>
        <tr><td><code>.</code></td><td>Any single character (use carefully — very broad!)</td><td><code>error.log</code> would also match "errorXlog"</td></tr>
        <tr><td><code>()</code></td><td>A "capture group" — pulls out a specific piece of the match</td><td>Grabbing just the IP address out of a full log line</td></tr>
        <tr><td><code>^</code> / <code>$</code></td><td>Start / end of the line</td><td><code>^ERROR</code> matches lines that *begin* with ERROR</td></tr>
      </table>
    </div>
    <div class="concept-card">
      <span class="concept-label">Hands-on</span>
      <h4 class="concept-title">A real log-parsing example, built up piece by piece</h4>
      <pre class="code-block"><span class="kw">import</span> re

log_line = <span class="str">'2026-06-06 03:14:07 ERROR [auth-service] Failed login from 203.0.113.42 for user jdoe'</span>

<span class="com"># Build the pattern in labeled pieces — far more readable than one giant blob</span>
pattern = (
    <span class="str">r&quot;(?P&lt;date&gt;\\d{4}-\\d{2}-\\d{2}) &quot;</span>          <span class="com"># 2026-06-06</span>
    <span class="str">r&quot;(?P&lt;time&gt;\\d{2}:\\d{2}:\\d{2}) &quot;</span>          <span class="com"># 03:14:07</span>
    <span class="str">r&quot;(?P&lt;level&gt;\\w+) &quot;</span>                       <span class="com"># ERROR</span>
    <span class="str">r&quot;\\[(?P&lt;service&gt;[\\w-]+)\\] &quot;</span>            <span class="com"># [auth-service]</span>
    <span class="str">r&quot;.*from (?P&lt;ip&gt;\\d+\\.\\d+\\.\\d+\\.\\d+) &quot;</span>  <span class="com"># 203.0.113.42</span>
    <span class="str">r&quot;for user (?P&lt;user&gt;\\w+)&quot;</span>                <span class="com"># jdoe</span>
)

match = re.search(pattern, log_line)
<span class="kw">if</span> match:
    <span class="fn">print</span>(<span class="str">f&quot;{match['level']} from {match['ip']} targeting account '{match['user']}'&quot;</span>)
    <span class="fn">print</span>(<span class="str">f&quot;Service: {match['service']}  at {match['date']} {match['time']}&quot;</span>)
<span class="com"># Output:
# ERROR from 203.0.113.42 targeting account 'jdoe'
# Service: auth-service  at 2026-06-06 03:14:07</span></pre>
      <p class="concept-desc">Named groups (<code>(?P&lt;name&gt;...)</code>) are the difference between a regex you can
      read again in six months and one you'll have to rebuild from scratch. They turn "what does group 4 mean again?"
      into "oh, that's obviously the IP address."</p>
    </div>
    <div class="concept-card">
      <span class="concept-label">Mindset</span>
      <h4 class="concept-title">Assume makes an ass out of you and me — test against real, messy data</h4>
      <p class="concept-desc">A pattern that works perfectly on the three sample lines you wrote it against can fall apart
      the moment it meets real-world data — an extra space, a different timestamp format, a username with a hyphen you
      didn't anticipate. Before trusting a regex in a script that runs unattended, run it against a large, genuinely messy
      sample of real data and actually look at what it *fails* to match — that's usually far more informative than looking
      at what it successfully matches.</p>
    </div>
  </div>
</div>
""" + "\n" + A_SCRIPT

S_MILITARY = "<!-- BEGINNER44-MILITARY v1 -->"
A_MILITARY = "<!-- /domain-body military -->"
C_MILITARY = S_MILITARY + """
<div class="topic">
  <div class="topic-header">
    <span class="topic-badge">Beginner</span>
    <h3>Networking Events Without the Awkwardness – A Veteran's Field Guide</h3>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <span class="concept-label">Why this matters</span>
      <h4 class="concept-title">"Networking" sounds fake until it gets you a job</h4>
      <p class="concept-desc">Plenty of capable people — veterans especially, coming from a culture that often values
      humility and "letting your work speak for itself" — find the idea of "networking" deeply uncomfortable, even
      slightly dishonest-feeling. Reframe it: networking is just having genuine conversations with people who do
      interesting work, and staying in touch. The job-finding part is a side effect of doing that consistently — not
      the awkward main event it's often made out to be.</p>
    </div>
    <div class="concept-card">
      <span class="concept-label">Concept</span>
      <h4 class="concept-title">Where IT networking actually happens (most of it isn't fancy galas)</h4>
      <table class="ai-table">
        <tr><th>Venue</th><th>What it actually looks like</th><th>Why it works</th></tr>
        <tr><td>Local user groups / meetups</td><td>A monthly gathering of people who use the same tools (Linux, AWS, cybersecurity) — usually free, usually casual</td><td>Low-pressure, recurring — you become a familiar face over a few months without ever "selling" yourself</td></tr>
        <tr><td>Veteran-focused tech programs</td><td>Organizations specifically built to connect transitioning service members with IT employers and mentors</td><td>Everyone there already understands your background — no translation needed, no awkward "so, tell me about your service" small talk</td></tr>
        <tr><td>Online communities</td><td>Subreddits, Discord servers, LinkedIn groups focused on specific certifications or technologies</td><td>Lower social pressure than in-person events — you can build relationships entirely on the strength of your questions and contributions</td></tr>
        <tr><td>Certification study groups</td><td>People preparing for the same exam, often meeting weekly to quiz each other</td><td>Built-in shared goal — conversation starts itself, friendships form naturally around mutual struggle and progress</td></tr>
      </table>
    </div>
    <div class="concept-card">
      <span class="concept-label">Hands-on</span>
      <h4 class="concept-title">A simple script for your first conversation (genuinely, not cynically)</h4>
      <pre class="code-block"><span class="com"># The goal of a first conversation is NOT "get a job out of this person."
# It's "have one genuine, useful exchange." That's it. Everything
# else follows from doing that consistently, many times, over months.</span>

<span class="com"># An opener that works because it's true and specific:</span>
&quot;Hey, I'm transitioning out of [your role] and getting into IT —
 working through my Security+ right now. What got you started
 in this field?&quot;

<span class="com"># A good follow-up that shows you're actually listening:</span>
&quot;That's interesting — how is that different day-to-day from
 what I'd expect coming from [your background]?&quot;

<span class="com"># The single most useful thing you can do afterward — not
# during the conversation, but within 48 hours of it:</span>
&quot;Hey [name], really enjoyed talking about [specific thing they
 said] — wanted to say thanks for the perspective. I'll let you
 know how the Security+ exam goes!&quot;

<span class="com"># That last message is the entire "secret" — most people never
# follow up at all, which means simply doing it puts you ahead
# of nearly everyone else they met that night.</span></pre>
    </div>
    <div class="concept-card">
      <span class="concept-label">Mindset</span>
      <h4 class="concept-title">Not my circus, not my monkey — but this circus is worth joining</h4>
      <p class="concept-desc">It's tempting to think "I'll network once I actually have something impressive to show" —
      but that backwards thinking keeps a lot of talented people invisible right when visibility would help them most.
      The people who'll eventually want to help you get hired are the same people you'd be meeting now, while you're
      still learning. Showing up consistently while you're a beginner — asking good questions, being genuinely curious,
      following up — builds the exact relationships that turn into opportunities later. You don't need to be impressive
      yet. You need to be present, and real.</p>
    </div>
  </div>
</div>
""" + "\n" + A_MILITARY


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
    (A_PENTEST, S_PENTEST, C_PENTEST),
    (A_AI, S_AI, C_AI),
    (A_SEC, S_SEC, C_SEC),
    (A_SCRIPT, S_SCRIPT, C_SCRIPT),
    (A_MILITARY, S_MILITARY, C_MILITARY),
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
