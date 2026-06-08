#!/usr/bin/env python3
"""Wave 48: beginner-friendly content additions across 5 domains."""
import re
from html.parser import HTMLParser

S_OPS = "<!-- BEGINNER48-OPS v1 -->"
A_OPS = "<!-- /domain-body ops -->"
C_OPS = S_OPS + """
<div class="topic">
  <div class="topic-header">
    <span class="topic-badge">Beginner</span>
    <h3>SLOs, SLAs, and Error Budgets – How Teams Decide "Good Enough" on Purpose</h3>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <span class="concept-label">Concept</span>
      <h4 class="concept-title">"100% uptime" is a trap, not a goal</h4>
      <p class="concept-desc">New engineers often assume the goal of operations is "never go down." In practice,
      chasing 100% reliability is usually wasteful — the cost and risk of every additional "nine" of uptime grows
      enormously, while the benefit to users flattens out. Mature teams instead define, on purpose, exactly how
      reliable a service needs to be — and then treat any reliability beyond that target as a resource to be
      spent deliberately, not hoarded out of fear.</p>
    </div>
    <div class="concept-card">
      <span class="concept-label">Concept</span>
      <h4 class="concept-title">The vocabulary: SLI, SLO, and SLA</h4>
      <table class="ai-table">
        <tr><th>Term</th><th>What it means</th></tr>
        <tr><td>SLI — Service Level Indicator</td><td>The actual measurement: "what percentage of requests
        succeeded in under 200ms over the last 28 days?"</td></tr>
        <tr><td>SLO — Service Level Objective</td><td>The internal target the team holds itself to: "99.9% of
        requests succeed in under 200ms." This is a goal, set deliberately by the team that owns the service.</td></tr>
        <tr><td>SLA — Service Level Agreement</td><td>An external promise, often contractual, usually with
        consequences (refunds, penalties) if it's missed. SLAs are typically looser than internal SLOs, on
        purpose — you want room to notice and fix a problem before it becomes a broken promise to a customer.</td></tr>
      </table>
      <p class="concept-desc">Notice the relationship: SLOs should be stricter than SLAs. That gap is your early
      warning system — it gives the team time to react before an internal target slip turns into an external,
      contractual failure.</p>
    </div>
    <div class="concept-card">
      <span class="concept-label">Concept</span>
      <h4 class="concept-title">Error budgets: turning "how much can we afford to break" into a number</h4>
      <p class="concept-desc">If your SLO is "99.9% of requests succeed," then by definition you're allowed
      0.1% of requests to fail — that 0.1% is your <em>error budget</em>. This single reframe changes how teams
      operate in a genuinely useful way:</p>
      <pre class="code-block"><span class="com"># A simplified way teams reason about error budgets month to month:</span>

SLO target          = 99.9% successful requests
Total requests      = 10,000,000 this month
Allowed failures    = 10,000,000 * (1 - 0.999) = 10,000   <span class="com"># the "budget"</span>
Actual failures     = 6,200                                <span class="com"># the "spend"</span>
Remaining budget    = 10,000 - 6,200 = 3,800

<span class="com"># With budget remaining, the team can reasonably:</span>
<span class="com">#   - ship a riskier feature this sprint</span>
<span class="com">#   - run a planned failover drill during business hours</span>
<span class="com">#   - take on a migration that carries some risk of brief blips</span>

<span class="com"># With the budget nearly exhausted, the team instead:</span>
<span class="com">#   - freezes risky changes</span>
<span class="com">#   - prioritizes reliability work over new features</span>
<span class="com">#   - investigates what's been eating the budget, and why</span></pre>
      <p class="concept-desc">The elegance here: error budgets turn an emotionally loaded question — "should we
      be more careful?" — into a measurable, depoliticized one. Nobody has to argue about <em>vibes</em>; the
      number tells the team whether it's currently in "ship mode" or "stabilize mode," and everyone can see the
      same data driving that call.</p>
    </div>
    <div class="concept-card">
      <span class="concept-label">Concept</span>
      <h4 class="concept-title">Why this connects back to "not my circus, not my monkey"</h4>
      <p class="concept-desc">Without shared SLOs, reliability conversations often degrade into finger-pointing —
      "the database team's queries are slow" versus "the application team is sending too much traffic." A clearly
      defined, jointly-owned SLO reframes the question from <em>whose fault is this</em> to <em>are we, together,
      meeting the target we agreed to</em>. It converts a blame exercise into a shared one — which is exactly the
      opposite of "not my circus": everyone touching the service shares the same circus, and the same monkey,
      whether they like it or not. SLOs simply make that shared ownership visible and measurable instead of
      something people argue about after the fact.</p>
    </div>
  </div>
</div>
""" + "\n" + A_OPS

S_MILITARY = "<!-- BEGINNER48-MILITARY v1 -->"
A_MILITARY = "<!-- /domain-body military -->"
C_MILITARY = S_MILITARY + """
<div class="topic">
  <div class="topic-header">
    <span class="topic-badge">Beginner</span>
    <h3>Security Clearances as a Civilian IT Asset – What They're Worth, and What They Aren't</h3>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <span class="concept-label">Concept</span>
      <h4 class="concept-title">An active or recent clearance can be a genuine fast-pass into certain roles</h4>
      <p class="concept-desc">If you held a security clearance during your service — Secret, Top Secret, TS/SCI,
      or others — that clearance can be a real differentiator in the civilian IT job market, particularly for
      government contractors and agencies that support defense, intelligence, and federal infrastructure work.
      The reinvestigation and onboarding process for a brand-new clearance can take many months and cost an
      employer real money; walking in with one already adjudicated can make you measurably more attractive than
      an equally-skilled candidate who would need to start that process from zero.</p>
    </div>
    <div class="concept-card">
      <span class="concept-label">Concept</span>
      <h4 class="concept-title">What actually carries over, and what doesn't (this is where assumptions bite)</h4>
      <p class="concept-desc"><em>"Assume makes an ass out of you and me"</em> applies directly here — a
      surprising number of separating service members assume their clearance status works differently than it
      actually does. A few realities worth knowing up front:</p>
      <table class="ai-table">
        <tr><th>Assumption</th><th>Reality</th></tr>
        <tr><td>"My clearance stays active forever."</td><td>Clearances generally go into a dormant or expired
        status if not used within a certain window (often around 24 months) — though reinstatement is frequently
        faster than starting fresh.</td></tr>
        <tr><td>"Any company can sponsor me to keep it active."</td><td>Generally only employers with an active
        government contract requiring cleared personnel can sponsor or maintain a clearance — this significantly
        narrows which employers can actually use it.</td></tr>
        <tr><td>"A clearance proves I'm good at IT."</td><td>It proves you passed a background investigation —
        nothing more. Employers will still expect to see real technical skill behind it. The clearance opens
        doors; it doesn't walk through them for you.</td></tr>
        <tr><td>"I should mention my clearance level loudly and often."</td><td>Listing the level (e.g., "Active
        Secret Clearance") on a resume is normal and expected. Discussing the *details* of cleared work — even
        seemingly mundane ones — can cross lines you don't want to cross. When in doubt, describe scope and
        impact in unclassified terms.</td></tr>
      </table>
    </div>
    <div class="concept-card">
      <span class="concept-label">Concept</span>
      <h4 class="concept-title">Where to actually look for cleared opportunities</h4>
      <p class="concept-desc">Cleared roles aren't typically found through general-purpose job boards — there's
      a parallel ecosystem built specifically around them:</p>
      <pre class="code-block"><span class="com"># Channels worth exploring if you hold (or recently held) a clearance:</span>

<span class="com"># 1. Cleared-specific job boards and career fairs</span>
<span class="com">#    -- These exist specifically because general boards don't filter
#       for clearance status, and cleared roles often can't be posted publicly</span>

<span class="com"># 2. Defense contractors and systems integrators</span>
<span class="com">#    -- Companies that hold government contracts requiring cleared staff
#       often have entire recruiting pipelines built around veterans</span>

<span class="com"># 3. Your base's Transition Assistance Program (TAP) office</span>
<span class="com">#    -- Often has direct relationships with cleared employers and
#       can help you understand exactly where your clearance currently stands</span>

<span class="com"># 4. Veteran-focused recruiting events and military-to-civilian programs</span>
<span class="com">#    -- Many specifically target candidates with clearances, because
#       employers attending know exactly what that population brings</span></pre>
    </div>
    <div class="concept-card">
      <span class="concept-label">Concept</span>
      <h4 class="concept-title">If the clearance route doesn't pan out, that's not a dead end</h4>
      <p class="concept-desc">Some veterans assume that if they don't land a cleared role quickly, the clearance
      was "wasted," or that the broader transition is going poorly. <em>"You can't make someone make the right
      choice, yet you can pick up the pieces afterwards"</em> is worth holding onto here — you can't force a
      hiring manager to value your clearance the way you do, or force a contract to materialize on your timeline.
      What you can do is keep building skills that stand entirely on their own, clearance or not. A strong
      technical foundation travels with you regardless of which doors happen to open first — and often, the
      cleared opportunity arrives later, once you're already established and simply easier to say yes to.</p>
    </div>
  </div>
</div>
""" + "\n" + A_MILITARY

S_SEC = "<!-- BEGINNER48-SEC v1 -->"
A_SEC = "<!-- /domain-body sec -->"
C_SEC = S_SEC + """
<div class="topic">
  <div class="topic-header">
    <span class="topic-badge">Beginner</span>
    <h3>Multi-Factor Authentication – Not All "Extra Steps" Provide Equal Protection</h3>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <span class="concept-label">Concept</span>
      <h4 class="concept-title">The core idea: combine things from different categories</h4>
      <p class="concept-desc">Multi-factor authentication (MFA) strengthens login security by requiring proof
      from more than one of these categories: <strong>something you know</strong> (a password, a PIN),
      <strong>something you have</strong> (a phone, a hardware key), and <strong>something you are</strong> (a
      fingerprint, facial recognition). The strength comes specifically from the combination spanning categories —
      a password plus a security question is technically "two things," but both live in "something you know,"
      so a single type of compromise (social engineering, a data breach) can defeat both at once.</p>
    </div>
    <div class="concept-card">
      <span class="concept-label">Concept</span>
      <h4 class="concept-title">Not all MFA methods resist the same attacks — a quick comparison</h4>
      <table class="ai-table">
        <tr><th>Method</th><th>Strength / weakness</th></tr>
        <tr><td>SMS text codes</td><td>Far better than nothing, but vulnerable to <em>SIM-swapping</em> — an
        attacker convincing your carrier to move your number to their device — and to interception on
        compromised networks.</td></tr>
        <tr><td>Authenticator apps (TOTP)</td><td>Generates time-based codes locally on your device, with no
        network transmission to intercept. A meaningful step up from SMS, though still phishable if a user is
        tricked into typing the code into a fake site.</td></tr>
        <tr><td>Push notifications</td><td>Convenient — just tap "approve" — but vulnerable to <em>MFA fatigue
        attacks</em>, where an attacker spams approval requests hoping a tired or distracted user taps "yes" just
        to make the notifications stop.</td></tr>
        <tr><td>Hardware security keys (e.g., FIDO2/WebAuthn)</td><td>Currently the strongest widely-available
        option — cryptographically tied to the legitimate site, making them resistant to phishing even when a
        user is actively being deceived.</td></tr>
      </table>
    </div>
    <div class="concept-card">
      <span class="concept-label">Concept</span>
      <h4 class="concept-title">A walkthrough of an MFA fatigue attack — and why it works on careful people</h4>
      <pre class="code-block"><span class="com"># A composite scenario based on real reported incidents:</span>

01:47 AM -- Push notification: "Approve sign-in to CorpVPN?"  [Deny]
01:48 AM -- Push notification: "Approve sign-in to CorpVPN?"  [Deny]
01:49 AM -- Push notification: "Approve sign-in to CorpVPN?"  [Deny]
<span class="com"># ... continues for twenty more minutes ...</span>
02:14 AM -- Push notification: "Approve sign-in to CorpVPN?"  [Approve]
            <span class="com"># exhausted, half-asleep, just wanting it to stop</span>

<span class="com"># The attacker didn't need to break the cryptography at all --
# they only needed to make "make it stop" feel more urgent than
# "is this actually me logging in?"</span></pre>
      <p class="concept-desc">This is exactly why <em>"assume makes an ass out of you and me"</em> matters at 2
      AM as much as at 2 PM: assuming a wave of approval prompts must mean "my phone is glitching" rather than
      "someone is actively trying to get in" is the precise gap this attack is built to exploit. The correct
      response to unexpected MFA prompts isn't to make them stop — it's to deny, and immediately tell your
      security team, even if it feels like an overreaction at 2 AM. It rarely is.</p>
    </div>
    <div class="concept-card">
      <span class="concept-label">Concept</span>
      <h4 class="concept-title">The takeaway: MFA is a meaningful upgrade, not a magic shield</h4>
      <p class="concept-desc">Enabling MFA — any form of it — dramatically reduces your exposure to the most
      common account-takeover techniques, and is one of the single highest-value security habits a person can
      adopt. But "I have MFA enabled" doesn't mean "I am now unphishable," any more than wearing a seatbelt means
      a collision can't hurt you. Understanding *which* method you're using, and what it does and doesn't defend
      against, is what turns a checkbox into actual protection.</p>
    </div>
  </div>
</div>
""" + "\n" + A_SEC

S_SHORTCUT = "<!-- BEGINNER48-SHORTCUT v1 -->"
A_SHORTCUT = "<!-- /domain-body shortcuts -->"
C_SHORTCUT = S_SHORTCUT + """
<div class="topic">
  <div class="topic-header">
    <span class="topic-badge">Beginner</span>
    <h3>Vim Survival Mode – Just Enough to Edit a File and Escape With Your Sanity</h3>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <span class="concept-label">Concept</span>
      <h4 class="concept-title">Why you'll meet vim whether you plan to or not</h4>
      <p class="concept-desc">Sooner or later, an SSH session into a minimal server will drop you into
      <code>vim</code> (or its lighter cousin <code>vi</code>) — usually because it's the default editor for
      <code>crontab -e</code>, <code>git commit</code>, or a config file edit, and there's no GUI text editor
      available. The famous joke about "how do I exit vim" exists because vim has <em>modes</em> — and if you
      don't know that, the editor genuinely looks like it's ignoring your keyboard. Once the modal concept clicks,
      vim stops being mysterious and starts being a fast, always-available tool.</p>
    </div>
    <div class="concept-card">
      <span class="concept-label">Concept</span>
      <h4 class="concept-title">The one idea that unlocks everything: modes</h4>
      <p class="concept-desc">Vim has (for our purposes) two modes that matter on day one:</p>
      <table class="ai-table">
        <tr><th>Mode</th><th>What it's for</th><th>How to get there</th></tr>
        <tr><td>Normal mode</td><td>Navigating, deleting, copying, saving, quitting — your keystrokes are
        <em>commands</em>, not text.</td><td>Press <code>Esc</code> (this is the default mode on opening a file)</td></tr>
        <tr><td>Insert mode</td><td>Actually typing text into the file, like a normal editor.</td>
        <td>Press <code>i</code> from normal mode</td></tr>
      </table>
      <p class="concept-desc">The single most common beginner mistake is typing while still in normal mode —
      which causes seemingly-random things to happen (text gets deleted, the cursor jumps around) because every
      letter is being interpreted as a command. The fix for "everything is going wrong" is almost always:
      press <code>Esc</code> to get back to a known state, breathe, then proceed deliberately.</p>
    </div>
    <div class="concept-card">
      <span class="concept-label">Concept</span>
      <h4 class="concept-title">The complete "survive and escape" reference</h4>
      <pre class="code-block"><span class="com"># Opening and the absolute essentials:</span>
vim filename.txt        <span class="com"># open (or create) a file</span>

<span class="com"># Getting INTO insert mode (i.e., "let me type now"):</span>
i                       <span class="com"># insert before the cursor</span>
a                       <span class="com"># insert after the cursor</span>
o                       <span class="com"># open a new line below and start typing</span>

<span class="com"># Getting OUT of insert mode (the step everyone forgets):</span>
Esc                     <span class="com"># back to normal mode -- do this before any command</span>

<span class="com"># Saving and quitting (all typed in NORMAL mode, after Esc):</span>
:w                      <span class="com"># write (save) the file</span>
:q                      <span class="com"># quit (fails if there are unsaved changes)</span>
:wq                     <span class="com"># write AND quit -- the one most people want</span>
:q!                     <span class="com"># quit WITHOUT saving -- "undo my mess and let me out"</span>

<span class="com"># A few moves that make you dangerous in normal mode:</span>
dd                      <span class="com"># delete the current line</span>
u                       <span class="com"># undo the last change</span>
/searchterm             <span class="com"># search forward for "searchterm", Enter to jump to it</span></pre>
    </div>
    <div class="concept-card">
      <span class="concept-label">Concept</span>
      <h4 class="concept-title">Permission to not love it — and a perfectly fine alternative</h4>
      <p class="concept-desc">Plenty of capable engineers never grow to love vim, and that's completely fine —
      <em>"not my circus, not my monkey"</em> can apply to entire categories of tools, not just incidents. If a
      box has <code>nano</code> available, it's a far gentler editor that shows its commands on-screen at all
      times (<code>Ctrl+O</code> to save, <code>Ctrl+X</code> to exit). The only non-negotiable skill is knowing
      how to escape vim when it's the *only* option available — which, on a surprising number of minimal servers,
      it eventually will be.</p>
    </div>
  </div>
</div>
""" + "\n" + A_SHORTCUT

S_LIFESTYLE = "<!-- BEGINNER48-LIFESTYLE v1 -->"
A_LIFESTYLE = "<!-- /domain-body lifestyle -->"
C_LIFESTYLE = S_LIFESTYLE + """
<div class="topic">
  <div class="topic-header">
    <span class="topic-badge">Beginner</span>
    <h3>Reading a Job Posting Like the Person Who Wrote It Did</h3>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <span class="concept-label">Concept</span>
      <h4 class="concept-title">Job postings are written by committee, under time pressure, from a template</h4>
      <p class="concept-desc">A huge source of needless self-doubt for career-changers: reading a posting that
      lists fifteen requirements, concluding "I only meet eight of these," and not applying. Here's the reality
      most hiring managers will tell you privately — postings are frequently assembled by combining a template,
      a wishlist from the team, and whatever the last person in the role happened to do. They describe an
      <em>ideal</em> candidate who often doesn't exist. Treating every line as a hard gate is one of the most
      common — and most costly — assumptions job-seekers make.</p>
    </div>
    <div class="concept-card">
      <span class="concept-label">Concept</span>
      <h4 class="concept-title">Learning to separate "must-have" from "nice-to-have" language</h4>
      <table class="ai-table">
        <tr><th>Phrase pattern</th><th>How to read it</th></tr>
        <tr><td>"Required," "must have," specific years of experience in the job title itself</td><td>Usually a
        genuine gate — though even "5 years required" sometimes flexes for a candidate who's clearly strong
        otherwise.</td></tr>
        <tr><td>"Preferred," "a plus," "nice to have," "familiarity with"</td><td>Genuinely optional in most
        cases — these are the wishlist items. Don't let them stop you from applying.</td></tr>
        <tr><td>A long, undifferentiated bullet list with no "required" vs. "preferred" split</td><td>Often a sign
        the posting was assembled quickly — treat the whole list more like a "things this role touches" overview
        than a checklist you must fully satisfy.</td></tr>
        <tr><td>Specific tools named throughout ("must know Tool X")</td><td>Frequently more about *category*
        than the specific tool — if you know a similar tool well, that's usually closer than it looks. Tools are
        commonly easier to pick up than the underlying concepts they sit on top of.</td></tr>
      </table>
    </div>
    <div class="concept-card">
      <span class="concept-label">Concept</span>
      <h4 class="concept-title">A rough rule of thumb worth knowing about</h4>
      <p class="concept-desc">Hiring research has repeatedly observed a pattern: candidates from some
      backgrounds tend to apply only when they meet nearly every listed qualification, while candidates from
      other backgrounds tend to apply when they meet a much smaller fraction — and the second group is
      frequently hired at comparable or better rates. The takeaway isn't "requirements don't matter." It's that
      <em>assuming</em> a posting is a precise, literal contract — rather than a rough sketch of a role — quietly
      filters out a lot of qualified people before a human ever reads their resume. <em>"Assume makes an ass out
      of you and me"</em> cuts both ways here: don't assume you're qualified for everything, but don't assume
      you're disqualified from everything either. Let the actual conversation answer that question.</p>
    </div>
    <div class="concept-card">
      <span class="concept-label">Concept</span>
      <h4 class="concept-title">A practical filter for "should I apply to this one?"</h4>
      <pre class="code-block"><span class="com"># A reasonable gut-check before skipping a posting:</span>

1. Do I meet MOST of the items explicitly marked "required"?
   -- If yes, the "preferred" list shouldn't stop you.

2. Am I excited about what this role actually DOES day to day,
   based on the responsibilities section (not just the title)?
   -- This matters more long-term than the qualifications list does.

3. Is there at least one thing on this list I'm genuinely
   curious to learn, rather than dreading?
   -- Growth roles are supposed to stretch you a little. That's
      not a red flag -- it's often the whole point of taking it.

<span class="com"># If the answer to all three is roughly "yes" -- apply.
# Worst case, a "no" costs you twenty minutes.
# Not applying because of a guess costs you the chance entirely.</span></pre>
      <p class="concept-desc">And if it doesn't work out — <em>"you can't make someone make the right choice, yet
      you can pick up the pieces afterwards"</em> applies just as much to rejections as to anything else. You
      can't make a hiring committee choose you. You can control how many doors you knock on, and how you respond
      when one of them eventually opens.</p>
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
    (A_OPS, S_OPS, C_OPS),
    (A_MILITARY, S_MILITARY, C_MILITARY),
    (A_SEC, S_SEC, C_SEC),
    (A_SHORTCUT, S_SHORTCUT, C_SHORTCUT),
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
