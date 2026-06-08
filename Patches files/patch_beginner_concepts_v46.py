#!/usr/bin/env python3
"""Wave 46: beginner-friendly content additions across 5 domains."""
import re
from html.parser import HTMLParser

S_THREAT = "<!-- BEGINNER46-THREAT v1 -->"
A_THREAT = "<!-- /domain-body threat -->"
C_THREAT = S_THREAT + """
<div class="topic">
  <div class="topic-header">
    <span class="topic-badge">Beginner</span>
    <h3>Ransomware – How It Spreads, and Why Backups Aren't the Whole Story</h3>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <span class="concept-label">Concept</span>
      <h4 class="concept-title">Ransomware in one sentence</h4>
      <p class="concept-desc">Ransomware is malicious software that encrypts a victim's files (or locks them out of their
      systems entirely) and demands payment — usually in cryptocurrency — for the key to restore access. Modern
      ransomware operations have evolved well past "encrypt and demand money": many now also steal data first and
      threaten to publish it, a tactic called <em>double extortion</em> that defeats the old assumption "we have backups,
      so we're fine."</p>
    </div>
    <div class="concept-card">
      <span class="concept-label">Concept</span>
      <h4 class="concept-title">A typical attack chain — and where it can be stopped</h4>
      <table class="ai-table">
        <tr><th>Stage</th><th>What happens</th><th>A defense that fits here</th></tr>
        <tr><td>1. Initial access</td><td>Phishing email, exposed RDP, or a vulnerable internet-facing service</td><td>Email filtering, MFA, patching, closing unnecessary exposed ports</td></tr>
        <tr><td>2. Spread / escalate</td><td>The attacker moves laterally through the network, gathering higher privileges</td><td>Network segmentation, least-privilege access, monitoring for unusual internal traffic</td></tr>
        <tr><td>3. Data theft (often skipped by less sophisticated groups)</td><td>Sensitive files are quietly exfiltrated before anything is encrypted</td><td>Data loss prevention, monitoring for unusual outbound transfer volumes</td></tr>
        <tr><td>4. Detonation</td><td>Files across the network are encrypted, often during off-hours to maximize damage before detection</td><td>Endpoint detection that flags mass file-modification behavior in real time</td></tr>
        <tr><td>5. Extortion</td><td>A ransom note appears; the attacker may also threaten to leak stolen data</td><td>Incident response plan, legal counsel, law enforcement contact — decided BEFORE this moment, not during it</td></tr>
      </table>
      <p class="concept-desc">Notice how much happens <em>before</em> stage 4 — the part most people picture when they
      hear "ransomware attack." By the time files start encrypting, the attacker has often already been inside the
      network for days or weeks. That's both bad news (damage may already be done) and good news (there were many earlier
      chances to catch it).</p>
    </div>
    <div class="concept-card">
      <span class="concept-label">Hands-on</span>
      <h4 class="concept-title">Verifying your backups are actually a safety net (not just a checkbox)</h4>
      <pre class="code-block"><span class="com"># A backup that ransomware can also encrypt or delete isn't a backup —
# it's just another file the attacker controls. Ask these questions:</span>

<span class="com"># 1. Are backups stored OFFLINE or in a way ransomware can't reach?
#    (immutable cloud storage, air-gapped tape, write-once media —
#    NOT just another network drive with the same credentials)</span>

<span class="com"># 2. Have you actually TESTED a full restore recently — not just
#    confirmed the backup job "completed successfully"?</span>
<span class="com">#    A backup nobody has ever restored from is a THEORY, not a plan.</span>

<span class="com"># 3. How far back do your retention policies go? If an attacker
#    was quietly inside for six weeks before detonating, and your
#    backups only go back two, you may be restoring already-compromised data</span>

<span class="com"># 4. Who has the credentials to delete or modify backups —
#    and is that access separated from everyday admin accounts?</span></pre>
      <p class="concept-desc">The 3-2-1 rule is a useful baseline to test your setup against: at least <strong>3</strong>
      copies of your data, on <strong>2</strong> different types of media, with <strong>1</strong> copy stored offsite
      (and ideally offline). Many organizations that "had backups" still paid ransoms — because their backups were
      reachable from the same compromised network as everything else.</p>
    </div>
    <div class="concept-card">
      <span class="concept-label">Mindset</span>
      <h4 class="concept-title">Assume makes an ass out of you and me — "we have backups" is not a plan</h4>
      <p class="concept-desc">"We're covered, we have backups" is one of the most common — and most dangerous — assumptions
      in incident preparedness, precisely because it sounds like due diligence without requiring anyone to verify it
      actually works. A real plan answers harder questions: how long would a full restore actually take (hours? days?
      weeks?), what would you tell customers during that gap, and who makes the call about whether to involve law
      enforcement? Untested assumptions don't reveal themselves until the worst possible moment to discover them.</p>
    </div>
  </div>
</div>
""" + "\n" + A_THREAT

S_SEC = "<!-- BEGINNER46-SEC v1 -->"
A_SEC = "<!-- /domain-body sec -->"
C_SEC = S_SEC + """
<div class="topic">
  <div class="topic-header">
    <span class="topic-badge">Beginner</span>
    <h3>Security Headers – The HTTP Response Fields That Quietly Protect You</h3>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <span class="concept-label">Concept</span>
      <h4 class="concept-title">A web server can tell your browser how to defend you</h4>
      <p class="concept-desc">When your browser loads a webpage, the server sends back more than just the page content —
      it also sends HTTP response headers, a set of instructions about how the browser should treat that content. A
      handful of these headers exist purely for security: they tell the browser "don't allow this page to be embedded
      elsewhere," "only ever load this site over HTTPS," or "don't run scripts from sources I haven't explicitly
      approved." Most users never see them — but their presence (or absence) says a lot about how seriously a site takes
      security.</p>
    </div>
    <div class="concept-card">
      <span class="concept-label">Concept</span>
      <h4 class="concept-title">The headers worth knowing</h4>
      <table class="ai-table">
        <tr><th>Header</th><th>What it does</th><th>What it protects against</th></tr>
        <tr><td><code>Strict-Transport-Security</code></td><td>Tells the browser "always use HTTPS for this site, never plain HTTP, even if a link points to http://"</td><td>Downgrade attacks that try to trick a browser into an unencrypted connection</td></tr>
        <tr><td><code>Content-Security-Policy</code></td><td>Whitelists exactly where scripts, styles, and other resources are allowed to load from</td><td>Cross-site scripting (XSS) — even if an attacker injects a script tag, the browser refuses to run it if its source isn't on the approved list</td></tr>
        <tr><td><code>X-Frame-Options</code></td><td>Controls whether the page can be displayed inside a frame on another site</td><td>Clickjacking — tricking users into clicking something different from what they think they're clicking</td></tr>
        <tr><td><code>X-Content-Type-Options</code></td><td>Tells the browser "don't try to guess the file type — trust what I told you it is"</td><td>MIME-sniffing attacks that disguise malicious files as harmless ones</td></tr>
        <tr><td><code>Referrer-Policy</code></td><td>Controls how much of the originating URL gets shared when a user clicks a link to another site</td><td>Accidentally leaking sensitive information (like search queries or internal URLs) to third-party sites</td></tr>
      </table>
    </div>
    <div class="concept-card">
      <span class="concept-label">Hands-on</span>
      <h4 class="concept-title">Checking what headers a site actually sends</h4>
      <pre class="code-block"><span class="com"># See the raw response headers for any site</span>
curl -sI https://example.com

<span class="com"># Filter for just the security-relevant ones</span>
curl -sI https://example.com | grep -iE &quot;strict-transport|content-security|x-frame|x-content-type|referrer-policy&quot;

<span class="com"># A snippet of what a well-configured response might include:
#
#   strict-transport-security: max-age=63072000; includeSubDomains
#   content-security-policy: default-src 'self'; script-src 'self' cdn.example.com
#   x-frame-options: DENY
#   x-content-type-options: nosniff
#   referrer-policy: strict-origin-when-cross-origin</span>

<span class="com"># Or use a free online scanner that grades a site's headers and
# explains exactly what's missing — useful both for learning AND
# for getting a quick read on a vendor's security posture</span></pre>
      <p class="concept-desc">Running this against a few of your own frequently-used sites is a genuinely eye-opening
      exercise — you'll often find that well-known, security-conscious organizations send a rich set of these headers,
      while smaller or older sites send almost none.</p>
    </div>
    <div class="concept-card">
      <span class="concept-label">Mindset</span>
      <h4 class="concept-title">Not my circus, not my monkey — except your users' browsers are always your circus</h4>
      <p class="concept-desc">It's tempting for a small team to think "security headers are for big companies with
      dedicated security staff" — but a single missing <code>Content-Security-Policy</code> header can be the difference
      between an XSS bug being a minor annoyance and it being a full account-takeover vector. These headers cost nothing
      to add, take minutes to configure on most modern web frameworks, and quietly protect every single visitor without
      requiring them to do anything at all. Few security investments offer that kind of return for that little effort.</p>
    </div>
  </div>
</div>
""" + "\n" + A_SEC

S_AI = "<!-- BEGINNER46-AI v1 -->"
A_AI = "<!-- /domain-body ai -->"
C_AI = S_AI + """
<div class="topic">
  <div class="topic-header">
    <span class="topic-badge">Beginner</span>
    <h3>Bias in AI Models – Where It Comes From and Why "Just Remove It" Isn't Simple</h3>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <span class="concept-label">Concept</span>
      <h4 class="concept-title">A model learns patterns from its training data — including the unfair ones</h4>
      <p class="concept-desc">Bias in AI isn't usually the result of a developer deliberately programming prejudice into a
      system. It emerges because models learn statistical patterns from huge amounts of real-world data — and the real
      world contains historical inequities, stereotypes, and uneven representation. A model trained on decades of hiring
      data from an industry that historically favored one group will tend to reproduce that pattern, even though no line
      of code ever explicitly said to. The bias was already baked into the data long before the model ever saw it.</p>
    </div>
    <div class="concept-card">
      <span class="concept-label">Concept</span>
      <h4 class="concept-title">A few of the ways bias commonly enters a system</h4>
      <table class="ai-table">
        <tr><th>Source</th><th>How it happens</th><th>Real-world example</th></tr>
        <tr><td>Historical data bias</td><td>Past decisions reflected in the training data carry forward old inequities</td><td>A resume-screening tool trained on a company's past hires learns to favor whatever group was historically hired most</td></tr>
        <tr><td>Representation gaps</td><td>Some groups, languages, or scenarios are underrepresented in the training data</td><td>Facial recognition systems performing measurably worse on faces less common in their training images</td></tr>
        <tr><td>Labeling bias</td><td>The humans who labeled training examples brought their own assumptions to the task</td><td>Content moderation systems flagging dialects or phrasings associated with certain communities as "more toxic" than equivalent statements in other phrasing</td></tr>
        <tr><td>Feedback loops</td><td>A biased system's outputs become tomorrow's training data, reinforcing the original pattern</td><td>A recommendation system that shows certain content more often, generating more engagement data that "confirms" it should keep doing so</td></tr>
      </table>
    </div>
    <div class="concept-card">
      <span class="concept-label">Hands-on</span>
      <h4 class="concept-title">A simple way to probe for bias yourself</h4>
      <pre class="code-block"><span class="com"># A basic technique: hold the scenario constant, vary ONE detail,
# and compare the outputs. Differences that correlate with that
# one detail — rather than with anything actually relevant to
# the task — are worth investigating further.</span>

prompts = [
    <span class="str">&quot;Write a short reference letter for Maria, a software engineer
    with 5 years of experience leading backend infrastructure projects.&quot;</span>,

    <span class="str">&quot;Write a short reference letter for James, a software engineer
    with 5 years of experience leading backend infrastructure projects.&quot;</span>,
]

<span class="com"># Identical qualifications, only the name differs. Then ask:
# - Do the letters differ in tone, confidence, or word choice?
# - Are the same achievements framed differently?
# - Would a hiring manager react to these two letters the same way?
#
# This exact technique — "audit by controlled comparison" — is a
# real, recognized method used in fairness research. You don't need
# special tools to start noticing patterns; you need a controlled
# comparison and a willingness to look closely at what comes back.</span></pre>
    </div>
    <div class="concept-card">
      <span class="concept-label">Mindset</span>
      <h4 class="concept-title">Assume makes an ass out of you and me — "the algorithm said so" isn't an answer</h4>
      <p class="concept-desc">It's tempting to treat an AI system's output as more "objective" than a human's judgment,
      precisely because it comes from math rather than a person with visible opinions. That assumption is exactly
      backwards in this context — the math was trained on human decisions, with all their patterns intact, just rendered
      less visible. Treating a model's output as automatically neutral is how bias quietly gets <em>more</em> power, not
      less — hidden behind a interface that looks impartial. Asking "where did this pattern in the data come from, and
      whose interests did it historically serve?" is not cynicism. It's the same due diligence you'd apply to any other
      decision-making system that affects real people.</p>
    </div>
  </div>
</div>
""" + "\n" + A_AI

S_SHORTCUT = "<!-- BEGINNER46-SHORTCUT v1 -->"
A_SHORTCUT = "<!-- /domain-body shortcuts -->"
C_SHORTCUT = S_SHORTCUT + """
<div class="topic">
  <div class="topic-header">
    <span class="topic-badge">Beginner</span>
    <h3>Tmux Survival Kit – Never Lose a Terminal Session Again</h3>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <span class="concept-label">Concept</span>
      <h4 class="concept-title">The problem tmux solves: "the SSH connection dropped, and I lost everything"</h4>
      <p class="concept-desc">Tmux (terminal multiplexer) lets you create terminal sessions that keep running even after
      you disconnect — whether your laptop sleeps, your VPN drops, or you just want to walk away and resume later from a
      different machine. Without it, a long-running command in an SSH session dies the instant the connection does. With
      it, you simply reconnect and find everything exactly where you left it, still running.</p>
    </div>
    <div class="concept-card">
      <span class="concept-label">Concept</span>
      <h4 class="concept-title">The mental model: sessions, windows, and panes</h4>
      <table class="ai-table">
        <tr><th>Concept</th><th>Think of it as...</th><th>Why it matters</th></tr>
        <tr><td>Session</td><td>An entire workspace — everything you're doing on this server right now</td><td>You can detach from it and it keeps running; reattach later from anywhere</td></tr>
        <tr><td>Window</td><td>A tab within that session</td><td>Switch between separate tasks (editing, monitoring logs, running tests) without separate connections</td></tr>
        <tr><td>Pane</td><td>A split within a window — multiple terminals visible side by side</td><td>Watch logs in one pane while running commands in another, all on one screen</td></tr>
      </table>
    </div>
    <div class="concept-card">
      <span class="concept-label">Reference</span>
      <h4 class="concept-title">The shortcuts that get you 90% of the way there</h4>
      <p class="concept-desc">Every tmux command starts with a "prefix" key — by default <code>Ctrl+b</code> — released,
      then followed by another key. Below, "prefix" means "press Ctrl+b, let go, then press the next key."</p>
      <table class="ai-table">
        <tr><th>Shortcut</th><th>What it does</th></tr>
        <tr><td><code>tmux new -s work</code></td><td>Start a new named session called "work" (naming sessions makes them MUCH easier to find later)</td></tr>
        <tr><td><code>prefix d</code></td><td>Detach from the current session — it keeps running in the background</td></tr>
        <tr><td><code>tmux attach -t work</code></td><td>Reattach to that session from anywhere — even a different computer</td></tr>
        <tr><td><code>tmux ls</code></td><td>List all running sessions — "what do I have going on right now?"</td></tr>
        <tr><td><code>prefix c</code></td><td>Create a new window (tab) in the current session</td></tr>
        <tr><td><code>prefix n</code> / <code>prefix p</code></td><td>Move to the next / previous window</td></tr>
        <tr><td><code>prefix %</code></td><td>Split the current pane vertically (side by side)</td></tr>
        <tr><td><code>prefix &quot;</code></td><td>Split the current pane horizontally (stacked)</td></tr>
        <tr><td><code>prefix arrow-key</code></td><td>Move between panes in that direction</td></tr>
      </table>
    </div>
    <div class="concept-card">
      <span class="concept-label">Hands-on</span>
      <h4 class="concept-title">A realistic first session, start to finish</h4>
      <pre class="code-block"><span class="com"># 1. SSH into a remote server, then start a named session</span>
ssh admin@server.example.com
tmux new -s deploy

<span class="com"># 2. Kick off something long-running — a deployment, a big sync, a build</span>
./run_deployment.sh

<span class="com"># 3. Your laptop goes to sleep / VPN hiccups / you close the lid.
#    The deployment KEEPS RUNNING on the server — tmux doesn't care
#    that your connection dropped.</span>

<span class="com"># 4. Reconnect later (even from a different machine entirely)</span>
ssh admin@server.example.com
tmux attach -t deploy
<span class="com"># ...and there it is, exactly where you left it, still running</span>

<span class="com"># 5. When you're completely done with it</span>
exit   <span class="com"># closes the window/session from inside</span>
<span class="com"># or from outside: tmux kill-session -t deploy</span></pre>
    </div>
    <div class="concept-card">
      <span class="concept-label">Mindset</span>
      <h4 class="concept-title">Assume makes an ass out of you and me — name your sessions</h4>
      <p class="concept-desc">"I'll remember which session is which" is a confident assumption at 2 PM and a source of
      genuine confusion at 2 AM when <code>tmux ls</code> shows four unnamed sessions and you can't recall which one has
      the thing you actually need. The thirty seconds it costs to type <code>tmux new -s deploy-prod-db-migration</code>
      instead of <code>tmux new</code> pays for itself the very first time you have more than one session running —
      which, if you use tmux at all regularly, will be sooner than you think.</p>
    </div>
  </div>
</div>
""" + "\n" + A_SHORTCUT

S_SCRIPT = "<!-- BEGINNER46-SCRIPT v1 -->"
A_SCRIPT = "<!-- /domain-body script -->"
C_SCRIPT = S_SCRIPT + """
<div class="topic">
  <div class="topic-header">
    <span class="topic-badge">Beginner</span>
    <h3>Scheduling Scripts the Right Way – Cron, Timers, and Idempotency</h3>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <span class="concept-label">Concept</span>
      <h4 class="concept-title">Automation that runs on its own schedule — and why that's harder than it sounds</h4>
      <p class="concept-desc">Plenty of useful scripts are designed to run on a schedule rather than on demand — nightly
      backups, hourly report generation, weekly cleanup jobs. Getting a script to "just run at 2 AM" is the easy part.
      The harder, more important part is making sure that when something goes wrong — the script crashes halfway, runs
      twice by accident, or runs while a previous run is still going — the result is "annoying log entry" rather than
      "corrupted data" or "duplicate emails sent to every customer."</p>
    </div>
    <div class="concept-card">
      <span class="concept-label">Hands-on</span>
      <h4 class="concept-title">The classic: cron syntax, decoded</h4>
      <pre class="code-block"><span class="com"># Cron's five fields, in order:
#   minute  hour  day-of-month  month  day-of-week</span>

<span class="com"># Run every day at 2:30 AM</span>
30 2 * * *  /opt/scripts/nightly_backup.sh

<span class="com"># Run every 15 minutes</span>
*/15 * * * *  /opt/scripts/check_health.sh

<span class="com"># Run at 9 AM, Monday through Friday only</span>
0 9 * * 1-5  /opt/scripts/send_daily_digest.sh

<span class="com"># Run on the 1st of every month at midnight</span>
0 0 1 * *   /opt/scripts/monthly_report.sh

<span class="com"># View your current scheduled jobs</span>
crontab -l

<span class="com"># Edit them (opens your default editor)</span>
crontab -e</pre>
      <p class="concept-desc">Many modern Linux systems also offer <span class="kw">systemd timers</span> as an
      alternative — they integrate with <code>journalctl</code> for logging, can express dependencies on other services,
      and handle "what if the system was off when this should have run?" more gracefully. Cron remains common and
      perfectly fine for simple jobs; timers shine once your scheduling needs get more sophisticated.</p>
    </div>
    <div class="concept-card">
      <span class="concept-label">Concept</span>
      <h4 class="concept-title">Idempotency: the property that turns "uh oh" into "no big deal"</h4>
      <p class="concept-desc">A script is <em>idempotent</em> if running it multiple times produces the same end result as
      running it once. This single property is what determines whether "the job accidentally ran twice" is a non-event
      or an incident.</p>
      <pre class="code-block"><span class="com"># NOT idempotent — running this twice creates two records,
# sends two emails, charges a customer twice...</span>
<span class="kw">def</span> <span class="fn">process_daily_signups</span>():
    new_users = get_signups_since_last_run()
    <span class="kw">for</span> user <span class="kw">in</span> new_users:
        send_welcome_email(user)
        create_billing_record(user)

<span class="com"># IDEMPOTENT — checks what's already been done before doing it again</span>
<span class="kw">def</span> <span class="fn">process_daily_signups</span>():
    new_users = get_signups_since_last_run()
    <span class="kw">for</span> user <span class="kw">in</span> new_users:
        <span class="kw">if</span> <span class="kw">not</span> already_sent_welcome_email(user):
            send_welcome_email(user)
            mark_welcome_email_sent(user)
        <span class="kw">if</span> <span class="kw">not</span> has_billing_record(user):
            create_billing_record(user)</pre>
      <p class="concept-desc">Notice the pattern: instead of just "do the thing," idempotent code asks "has this already
      been done?" first. That one habit — checking before acting, every time — is what separates scheduled automation
      you can trust from scheduled automation that occasionally needs a 3 AM apology email to customers.</p>
    </div>
    <div class="concept-card">
      <span class="concept-label">Mindset</span>
      <h4 class="concept-title">Assume makes an ass out of you and me — assume it WILL run twice someday</h4>
      <p class="concept-desc">"It only runs once a day, what are the odds it overlaps with itself?" is exactly the kind of
      assumption that holds up fine for months — until a slow database connection causes one run to take 25 hours, and
      suddenly two copies are running at once, both modifying the same data. Writing scheduled scripts as though they
      <em>will</em> eventually run concurrently or get interrupted mid-task — using locks, idempotency checks, and
      transactional updates — costs a little extra effort upfront and saves an enormous amount of cleanup later.</p>
    </div>
  </div>
</div>
""" + "\n" + A_SCRIPT


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
    (A_THREAT, S_THREAT, C_THREAT),
    (A_SEC, S_SEC, C_SEC),
    (A_AI, S_AI, C_AI),
    (A_SHORTCUT, S_SHORTCUT, C_SHORTCUT),
    (A_SCRIPT, S_SCRIPT, C_SCRIPT),
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
