#!/usr/bin/env python3
"""Wave 45: beginner-friendly content additions across 5 domains."""
import re
from html.parser import HTMLParser

S_OPS = "<!-- BEGINNER45-OPS v1 -->"
A_OPS = "<!-- /domain-body ops -->"
C_OPS = S_OPS + """
<div class="topic">
  <div class="topic-header">
    <span class="topic-badge">Beginner</span>
    <h3>Writing a Postmortem People Actually Learn From</h3>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <span class="concept-label">Concept</span>
      <h4 class="concept-title">A postmortem is a story about a system, not a trial of a person</h4>
      <p class="concept-desc">A postmortem (or "post-incident review") is a written analysis of what happened during an
      outage or incident, why it happened, and what will change as a result. The single most important design decision in
      any postmortem process is whether it's <em>blameless</em> — focused on "what conditions made this mistake possible
      and likely?" rather than "who do we blame for this?" Get that one decision right, and people will tell you the truth
      about what happened. Get it wrong, and every future postmortem will quietly omit the details that actually mattered.</p>
    </div>
    <div class="concept-card">
      <span class="concept-label">Concept</span>
      <h4 class="concept-title">The shape of a postmortem that actually gets read</h4>
      <table class="ai-table">
        <tr><th>Section</th><th>What it answers</th><th>Common mistake to avoid</th></tr>
        <tr><td>Summary</td><td>What happened, in 3-4 sentences a busy executive could read in 20 seconds</td><td>Burying the headline under technical preamble nobody reads first</td></tr>
        <tr><td>Impact</td><td>Who was affected, for how long, and how badly — with real numbers</td><td>Vague language like "some users experienced issues" instead of "approximately 4,200 users over 38 minutes"</td></tr>
        <tr><td>Timeline</td><td>What happened, in order, with timestamps — including detection and response</td><td>Starting the timeline at "the fix" instead of at the first sign something was wrong</td></tr>
        <tr><td>Root cause(s)</td><td>Why it happened — usually more than one contributing factor, not a single villain</td><td>Stopping at "a bad config was deployed" instead of asking "why was it possible to deploy that config unreviewed?"</td></tr>
        <tr><td>Action items</td><td>Specific, owned, dated changes that reduce the chance of recurrence</td><td>Vague commitments like "we'll be more careful" — that's not an action item, it's a hope</td></tr>
      </table>
    </div>
    <div class="concept-card">
      <span class="concept-label">Hands-on</span>
      <h4 class="concept-title">The "five whys" — finding the real root cause</h4>
      <pre class="code-block"><span class="com"># A simple technique for digging past the surface-level explanation.
# Keep asking "why" until you reach something you can actually fix.</span>

Problem: The payment service was down for 40 minutes.

Why #1: Why was it down?
   -&gt; The service crashed when it ran out of memory.

Why #2: Why did it run out of memory?
   -&gt; A new code path loaded an entire customer table into memory at once.

Why #3: Why did that code path do that?
   -&gt; The developer tested only against a small sample database in staging.

Why #4: Why didn't testing catch this before production?
   -&gt; Staging databases aren't seeded with production-scale data volumes.

Why #5: Why isn't that part of the standard testing process?
   -&gt; There's no documented requirement for load-realistic staging data.

<span class="com"># Notice where this ended up: not "the developer made a mistake"
# (Why #1-3), but "our process doesn't ensure realistic testing
# conditions" (Why #5) — a SYSTEM problem with a fixable solution,
# not a PERSON problem with only blame to offer.</span></pre>
    </div>
    <div class="concept-card">
      <span class="concept-label">Mindset</span>
      <h4 class="concept-title">Not my circus, not my monkey — except blameless culture is everyone's circus</h4>
      <p class="concept-desc">It's easy to think "writing good postmortems is the SRE team's job" — but a blameless
      culture is built or destroyed by everyone in the room, in the moment someone says "well, obviously <em>they</em>
      should have known better." One unkind comment in a review meeting can undo months of careful culture-building, and
      it teaches everyone present — not just the person being criticized — that honesty here has a cost. Protecting that
      culture, even in a meeting that isn't "yours," is part of keeping the whole system honest enough to actually improve.</p>
    </div>
  </div>
</div>
""" + "\n" + A_OPS

S_LINUX = "<!-- BEGINNER45-LINUX v1 -->"
A_LINUX = "<!-- /domain-body linux -->"
C_LINUX = S_LINUX + """
<div class="topic">
  <div class="topic-header">
    <span class="topic-badge">Beginner</span>
    <h3>Process Management – Finding and Taming Runaway Processes</h3>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <span class="concept-label">Concept</span>
      <h4 class="concept-title">Every running thing is a process — and every process tells a story</h4>
      <p class="concept-desc">A process is a running instance of a program — and at any moment, a Linux system might have
      hundreds of them, most quietly doing their job. The skill of process management is being able to quickly answer
      "what's running, what's it doing, is it behaving normally, and how do I deal with it if it isn't?" — questions that
      come up constantly in troubleshooting, whether the symptom is "the server feels slow" or "this thing won't quit."</p>
    </div>
    <div class="concept-card">
      <span class="concept-label">Hands-on</span>
      <h4 class="concept-title">Seeing what's running, and how it's behaving</h4>
      <pre class="code-block"><span class="com"># The classic snapshot view — every process, full detail</span>
ps aux

<span class="com"># Live, auto-refreshing view sorted by resource usage —
# your first stop when something "feels slow"</span>
top
<span class="com"># or, with friendlier output and mouse support:</span>
htop

<span class="com"># Find processes by name — handy when you know what you're
# looking for but not its process ID (PID)</span>
pgrep -fl nginx

<span class="com"># See the full ancestry — what launched what, and in what order
# (extremely useful for understanding "where did this come from?")</span>
ps -ef --forest

<span class="com"># Check what files and network connections a specific process has open —
# great for "why won't this file unmount?" or "what is this PID
# actually talking to?"</span>
lsof -p 4821</pre>
    </div>
    <div class="concept-card">
      <span class="concept-label">Concept</span>
      <h4 class="concept-title">Stopping a process: three signals, three very different outcomes</h4>
      <table class="ai-table">
        <tr><th>Signal</th><th>Command</th><th>What it actually means</th></tr>
        <tr><td>SIGTERM (15)</td><td><code>kill 4821</code></td><td>"Please shut yourself down gracefully" — gives the process a chance to save state, close connections, and clean up</td></tr>
        <tr><td>SIGKILL (9)</td><td><code>kill -9 4821</code></td><td>"Stop immediately, no negotiation" — the kernel terminates it on the spot; the process gets no chance to clean up anything</td></tr>
        <tr><td>SIGHUP (1)</td><td><code>kill -1 4821</code></td><td>"Reload your configuration" — many daemons treat this as "re-read your config file without fully restarting"</td></tr>
      </table>
      <p class="concept-desc">The escalation order matters: try <span class="kw">SIGTERM</span> first, wait a few seconds,
      and reach for <span class="kw">SIGKILL</span> only if the process genuinely won't respond. Reaching straight for
      <code>kill -9</code> out of habit is how database processes end up with corrupted files and temp directories end up
      full of orphaned lock files — the very cleanup steps SIGTERM would have given the process a chance to perform.</p>
    </div>
    <div class="concept-card">
      <span class="concept-label">Mindset</span>
      <h4 class="concept-title">Assume makes an ass out of you and me — verify the PID before you kill it</h4>
      <p class="concept-desc">Process IDs get reused constantly as old processes exit and new ones start — the PID you
      noted five minutes ago in a different terminal might belong to a completely different program by the time you act
      on it. Before running <code>kill</code> on a number you wrote down earlier, re-run <code>ps</code> or
      <code>pgrep</code> to confirm that PID still belongs to what you think it does. The few seconds that takes is far
      cheaper than explaining why you killed the wrong service.</p>
    </div>
  </div>
</div>
""" + "\n" + A_LINUX

S_GRC = "<!-- BEGINNER45-GRC v1 -->"
A_GRC = "<!-- /domain-body grc -->"
C_GRC = S_GRC + """
<div class="topic">
  <div class="topic-header">
    <span class="topic-badge">Beginner</span>
    <h3>The Three Lines of Defense – Who's Actually Watching the Risk?</h3>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <span class="concept-label">Concept</span>
      <h4 class="concept-title">A model for "who's responsible for managing risk, exactly?"</h4>
      <p class="concept-desc">In any organization larger than a handful of people, risk management can't be just one
      team's job — but it also can't be "everyone's job" in a way that means nobody owns it. The Three Lines model is a
      widely-used way of dividing that responsibility clearly, so that risk gets caught at multiple independent layers
      rather than relying on any single point of failure (including, notably, relying entirely on people grading their
      own homework).</p>
    </div>
    <div class="concept-card">
      <span class="concept-label">Concept</span>
      <h4 class="concept-title">The three lines, and what each one actually does</h4>
      <table class="ai-table">
        <tr><th>Line</th><th>Who's in it</th><th>Their job</th><th>Analogy</th></tr>
        <tr><td>First line</td><td>Operational teams — IT, engineering, customer service, anyone doing the day-to-day work</td><td>Own and manage risk directly, in real time, as part of doing their jobs</td><td>The pilots flying the plane — responsible for safe operation, moment to moment</td></tr>
        <tr><td>Second line</td><td>Risk management, compliance, security teams</td><td>Set policy, provide expertise, monitor whether the first line is actually managing risk well</td><td>The airline's safety and compliance department — defines standards and checks adherence</td></tr>
        <tr><td>Third line</td><td>Internal audit</td><td>Independently verify that BOTH the first and second lines are functioning as intended — answers to leadership and the board, not to the teams it reviews</td><td>An independent aviation regulator — checks the airline itself, including its own safety department</td></tr>
      </table>
      <p class="concept-desc">The key design principle is independence: the third line doesn't report to the people it's
      checking on. That's not a vote of distrust in any individual — it's an acknowledgment that even well-intentioned
      people are bad at objectively grading their own work, especially when their own performance review depends on the answer.</p>
    </div>
    <div class="concept-card">
      <span class="concept-label">Hands-on</span>
      <h4 class="concept-title">Spotting the three lines in a real scenario</h4>
      <pre class="code-block"><span class="com"># Scenario: a company is rolling out a new customer database</span>

FIRST LINE  - The engineering team building the system follows
              secure coding practices, runs their own tests, and
              flags risks they notice during development.
              (&quot;We're the ones building it — we manage the
              day-to-day risk as we go.&quot;)

SECOND LINE - The security team reviews the design before launch,
              sets the encryption standards the engineers must
              follow, and runs periodic vulnerability scans
              after launch.
              (&quot;We set the rules and check whether engineering
              is actually following them.&quot;)

THIRD LINE  - Internal audit, reporting directly to the board,
              independently reviews BOTH the engineering team's
              practices AND whether the security team's oversight
              process is actually effective — not just whether
              a checklist was completed.
              (&quot;We check whether the checkers are checking
              the right things, thoroughly, without bias.&quot;)</pre>
    </div>
    <div class="concept-card">
      <span class="concept-label">Mindset</span>
      <h4 class="concept-title">Not my circus, not my monkey — knowing your line is the whole point</h4>
      <p class="concept-desc">Confusion about which "line" you're in is a common source of organizational friction —
      a first-line team that thinks "compliance will catch anything we miss" is quietly creating the exact gap the model
      was designed to prevent. Understanding which line you sit in — and which lines exist above and beside you — isn't
      bureaucratic trivia. It's the difference between confidently owning your part of the system and assuming, wrongly,
      that someone else already has it covered.</p>
    </div>
  </div>
</div>
""" + "\n" + A_GRC

S_LIFESTYLE = "<!-- BEGINNER45-LIFESTYLE v1 -->"
A_LIFESTYLE = "<!-- /domain-body lifestyle -->"
C_LIFESTYLE = S_LIFESTYLE + """
<div class="topic">
  <div class="topic-header">
    <span class="topic-badge">Beginner</span>
    <h3>Imposter Syndrome in IT – You're Not the Only One Faking It (a Little)</h3>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <span class="concept-label">Why this matters</span>
      <h4 class="concept-title">The feeling that everyone else "gets it" and you're just guessing</h4>
      <p class="concept-desc">Imposter syndrome is the persistent feeling that you don't actually deserve your role or
      success — that you've somehow fooled everyone, and it's only a matter of time before they "find out." It's
      remarkably common in IT specifically, because the field changes constantly: there will <em>always</em> be a tool,
      a framework, or an acronym you've never heard of, no matter how senior you become. That's not a sign you don't
      belong. It's the actual, permanent shape of working in technology — and recognizing that is half the battle.</p>
    </div>
    <div class="concept-card">
      <span class="concept-label">Concept</span>
      <h4 class="concept-title">Reframing three thoughts that fuel it</h4>
      <table class="ai-table">
        <tr><th>The thought</th><th>A more accurate reframe</th></tr>
        <tr><td>"Everyone else seems to know what they're doing"</td><td>You're seeing their confident output, not their search history, their Stack Overflow tabs, or their private doubts. Confidence is often a performance, not a measure of actual certainty.</td></tr>
        <tr><td>"I had to look that up — a 'real' expert wouldn't need to"</td><td>Looking things up efficiently <em>is</em> the actual skill. The most senior engineers you'll meet Google things constantly — they've just gotten faster at finding good answers and verifying them.</td></tr>
        <tr><td>"I only got this opportunity by luck / good timing"</td><td>Being prepared when an opportunity appeared <em>is</em> the skill. Luck without preparation produces nothing; preparation without any luck rarely gets noticed. Both matter — and you supplied the half that was actually yours to supply.</td></tr>
      </table>
    </div>
    <div class="concept-card">
      <span class="concept-label">Hands-on</span>
      <h4 class="concept-title">A concrete habit that actually helps: the "evidence log"</h4>
      <pre class="code-block"><span class="com"># A simple personal practice: keep a running note — a text file,
# a notes app, anything — where you record concrete moments that
# contradict the "I don't actually know what I'm doing" narrative.
# Re-read it specifically on the days that narrative gets loud.</span>

2026-04-02 - Diagnosed the VPN issue that had stumped two other
             people for three days. Turned out to be a routing
             rule from an old config nobody remembered existed.

2026-04-19 - A junior teammate asked ME to explain subnetting.
             I actually understood it well enough to teach it —
             six months ago I was the one asking that question.

2026-05-30 - Wrote a script that automated a task that used to
             eat up two hours of someone's Friday every week.
             They actually said thank you, unprompted.

<span class="com"># None of these are "I am a genius." They're all just small,
# factual, undeniable evidence that you are, in fact, learning,
# contributing, and growing — which is the entire actual job.</span></pre>
    </div>
    <div class="concept-card">
      <span class="concept-label">Mindset</span>
      <h4 class="concept-title">You can't make someone make the right choice...</h4>
      <p class="concept-desc"><strong>...yet you can pick up the pieces afterwards — including your own.</strong> You
      can't will away every doubt, and you can't make your brain stop occasionally whispering "you don't belong here."
      What you <em>can</em> do is decide, in advance, how you'll respond to that whisper when it shows up: by checking it
      against actual evidence, by talking to someone who's been there, and by remembering that the discomfort of learning
      something new is not the same thing as evidence that you can't. Almost everyone you admire in this field felt
      exactly what you're feeling right now, at some point — they just kept showing up anyway. That's the whole secret,
      and it's available to you too.</p>
    </div>
  </div>
</div>
""" + "\n" + A_LIFESTYLE

S_NET = "<!-- BEGINNER45-NET v1 -->"
A_NET = "<!-- /domain-body net -->"
C_NET = S_NET + """
<div class="topic">
  <div class="topic-header">
    <span class="topic-badge">Beginner</span>
    <h3>Load Balancers Explained – Spreading the Work Around</h3>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <span class="concept-label">Concept</span>
      <h4 class="concept-title">A load balancer is a traffic cop for your servers</h4>
      <p class="concept-desc">A load balancer sits in front of a group of servers and decides which one should handle each
      incoming request — spreading the work around so no single server gets overwhelmed, and so the service keeps running
      even if one server fails. From the outside, users see a single address; behind that address, the load balancer
      quietly routes them to whichever healthy server makes the most sense at that moment.</p>
    </div>
    <div class="concept-card">
      <span class="concept-label">Concept</span>
      <h4 class="concept-title">Common balancing strategies, and when each shines</h4>
      <table class="ai-table">
        <tr><th>Strategy</th><th>How it decides</th><th>Good fit when...</th></tr>
        <tr><td>Round robin</td><td>Cycles through servers in order: 1, 2, 3, 1, 2, 3...</td><td>All servers are roughly equal in capacity and requests are roughly equal in cost</td></tr>
        <tr><td>Least connections</td><td>Sends the next request to whichever server currently has the fewest active connections</td><td>Requests vary significantly in how long they take to process</td></tr>
        <tr><td>IP hash</td><td>Routes based on a hash of the client's IP — the same client tends to land on the same server</td><td>You need "session stickiness" without a shared session store</td></tr>
        <tr><td>Weighted</td><td>Some servers get proportionally more traffic than others, based on assigned weights</td><td>Your servers have meaningfully different capacities (a newer, beefier box vs. an older one)</td></tr>
      </table>
    </div>
    <div class="concept-card">
      <span class="concept-label">Concept</span>
      <h4 class="concept-title">The unsung hero: health checks</h4>
      <p class="concept-desc">A load balancer is only as good as its ability to know which servers are actually healthy.
      It periodically polls each server — often hitting a dedicated <code>/healthz</code> endpoint — and silently stops
      sending traffic to any server that fails to respond correctly. This is the mechanism that turns "one server crashed"
      from a customer-facing outage into a non-event nobody outside the on-call team ever notices.</p>
      <pre class="code-block"><span class="com"># A minimal health endpoint, the kind a load balancer polls every few seconds</span>
<span class="kw">from</span> flask <span class="kw">import</span> Flask, jsonify
app = Flask(__name__)

<span class="kw">@app.route</span>(<span class="str">&quot;/healthz&quot;</span>)
<span class="kw">def</span> <span class="fn">health_check</span>():
    checks = {
        <span class="str">&quot;database&quot;</span>: database_is_reachable(),
        <span class="str">&quot;cache&quot;</span>: cache_is_reachable(),
        <span class="str">&quot;disk_space_ok&quot;</span>: get_free_disk_percent() &gt; 10,
    }
    healthy = <span class="fn">all</span>(checks.values())
    status_code = 200 <span class="kw">if</span> healthy <span class="kw">else</span> 503
    <span class="kw">return</span> jsonify(checks), status_code

<span class="com"># A load balancer that sees repeated 503s here will quietly stop
# routing traffic to this instance — without a single human noticing,
# until someone reviews the dashboards and finds the graceful save</span></pre>
    </div>
    <div class="concept-card">
      <span class="concept-label">Mindset</span>
      <h4 class="concept-title">Assume makes an ass out of you and me</h4>
      <p class="concept-desc">A health check that only verifies "is the web server process running?" can report "healthy"
      while the actual database connection behind it is completely down — leaving users staring at error pages from a
      server the load balancer confidently considers fine. A good health check verifies the things that actually matter
      to the user's experience, not just the easiest thing to check. "The process is running" and "the service actually
      works" are two different claims — don't let your monitoring assume they're the same.</p>
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
    (A_OPS, S_OPS, C_OPS),
    (A_LINUX, S_LINUX, C_LINUX),
    (A_GRC, S_GRC, C_GRC),
    (A_LIFESTYLE, S_LIFESTYLE, C_LIFESTYLE),
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
