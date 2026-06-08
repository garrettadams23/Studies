#!/usr/bin/env python3
"""
patch_beginner_concepts_v27.py — Wave 27: Webhooks/bot automation, HTTP deep
dive, zero trust architecture, SRE principles, growing into senior roles.

New sentinels:
  BEGINNER27-SCRIPT v1  — Webhooks, ChatOps bots, event-driven automation
  BEGINNER27-NET v1     — HTTP protocol deep dive (methods, status codes, HTTP/2-3)
  BEGINNER27-SEC v1     — Zero Trust architecture, microsegmentation, BeyondCorp
  BEGINNER27-OPS v1     — SRE principles, SLO/error budgets, toil, chaos engineering
  BEGINNER27-LIFE v1    — Growing into senior/lead roles, scope, influence
"""
from pathlib import Path

SCRIPT_INJECT_ANCHOR = "<!-- /domain-body script -->"
NET_INJECT_ANCHOR    = "<!-- /domain-body net -->"
SEC_INJECT_ANCHOR    = "<!-- /domain-body sec -->"
OPS_INJECT_ANCHOR    = "<!-- /domain-body ops -->"
LIFE_INJECT_ANCHOR   = "<!-- /domain-body lifestyle -->"

# ─────────────────────────────── SCRIPT wave 27 ──────────────────────────────
SCRIPT_SENTINEL = "<!-- BEGINNER27-SCRIPT v1 -->"
SCRIPT_CONTENT = """
<!-- BEGINNER27-SCRIPT v1 -->
<!-- ── TOPIC: WEBHOOKS & CHATOPS ─────────────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">🪝</span>
    <span class="topic-name">Webhooks &amp; ChatOps — Event-Driven Automation</span>
    <span class="topic-badge">SCRIPT • Practical</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">WEBHOOKS</div>
      <div class="concept-title">"Don't Call Us, We'll Call You"</div>
      <div class="concept-desc">Polling means repeatedly asking "anything new yet?" — wasteful and slow. A webhook flips it: you give a service a URL, and it sends an HTTP POST to that URL when an event happens (a push, a payment, an alert). It's the backbone of modern integrations — GitHub→CI, Stripe→your app, monitoring→Slack. Your side just needs an endpoint that listens.</div>
      <div class="code-block"><span class="com"># A minimal webhook RECEIVER (Flask)</span>
<span class="kw">from</span> flask <span class="kw">import</span> Flask, request, abort
<span class="kw">import</span> hmac, hashlib, os

app = Flask(__name__)
SECRET = os.environ[<span class="str">"WEBHOOK_SECRET"</span>].encode()

<span class="fn">@app.post</span>(<span class="str">"/webhook"</span>)
<span class="kw">def</span> <span class="fn">webhook</span>():
    <span class="com"># 1. VERIFY the signature — never trust an unverified webhook!</span>
    sig = request.headers.get(<span class="str">"X-Signature"</span>, <span class="str">""</span>)
    expected = hmac.new(SECRET, request.data, hashlib.sha256).hexdigest()
    <span class="kw">if</span> <span class="kw">not</span> hmac.compare_digest(sig, expected):
        abort(<span class="num">401</span>)

    <span class="com"># 2. Process the event</span>
    event = request.json
    <span class="kw">if</span> event[<span class="str">"action"</span>] == <span class="str">"opened"</span>:
        handle_new_issue(event)

    <span class="com"># 3. Respond FAST (2xx) — do slow work in the background</span>
    <span class="kw">return</span> <span class="str">""</span>, <span class="num">204</span></div>
    </div>
    <div class="concept-card">
      <div class="concept-label">WEBHOOK BEST PRACTICES</div>
      <div class="concept-title">Receiving Webhooks Safely</div>
      <table class="ai-table">
        <thead><tr><th>Practice</th><th>Why</th></tr></thead>
        <tbody>
          <tr><td>Verify the signature</td><td>Anyone can POST to your URL — confirm it's really the sender (HMAC)</td></tr>
          <tr><td>Respond quickly (2xx)</td><td>Senders time out; do heavy work async (queue it)</td></tr>
          <tr><td>Be idempotent</td><td>Senders retry — handle duplicate deliveries safely</td></tr>
          <tr><td>Use HTTPS</td><td>Payloads often contain sensitive data</td></tr>
          <tr><td>Validate the payload</td><td>It's untrusted input — validate before acting</td></tr>
        </tbody>
      </table>
    </div>
    <div class="concept-card">
      <div class="concept-label">SENDING NOTIFICATIONS</div>
      <div class="concept-title">ChatOps — Pipe Events to Slack/Discord</div>
      <div class="code-block"><span class="kw">import</span> requests, os

<span class="com"># Slack incoming webhook — post an alert from any script</span>
<span class="kw">def</span> <span class="fn">notify_slack</span>(text, level=<span class="str">"info"</span>):
    emoji = {<span class="str">"info"</span>: <span class="str">"ℹ️"</span>, <span class="str">"warn"</span>: <span class="str">"⚠️"</span>, <span class="str">"error"</span>: <span class="str">"🚨"</span>}[level]
    requests.post(
        os.environ[<span class="str">"SLACK_WEBHOOK_URL"</span>],
        json={<span class="str">"text"</span>: <span class="str">f"{emoji} {text}"</span>},
        timeout=<span class="num">5</span>,
    )

<span class="com"># Wire it into your monitoring scripts</span>
<span class="kw">if</span> disk_usage &gt; <span class="num">90</span>:
    notify_slack(<span class="str">f"Disk at {disk_usage}% on web1"</span>, level=<span class="str">"error"</span>)

<span class="com"># This is "ChatOps" — operations surfaced and run from chat.</span>
<span class="com"># Alerts, deploy notifications, even running commands via bots.</span></div>
    </div>
  </div>
</div>
"""

# ─────────────────────────────── NET wave 27 ─────────────────────────────────
NET_SENTINEL = "<!-- BEGINNER27-NET v1 -->"
NET_CONTENT = """
<!-- BEGINNER27-NET v1 -->
<!-- ── TOPIC: HTTP PROTOCOL DEEP DIVE ────────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">🌐</span>
    <span class="topic-name">HTTP — The Protocol That Runs the Web</span>
    <span class="topic-badge">NET • Essential</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">ANATOMY OF A REQUEST</div>
      <div class="concept-title">What Actually Goes Over the Wire</div>
      <div class="code-block"><span class="com"># An HTTP request is plain text (in HTTP/1.1)</span>
GET /api/users?page=2 HTTP/1.1      <span class="com"># method, path, version</span>
Host: example.com                    <span class="com"># required header</span>
User-Agent: curl/8.0
Accept: application/json
Authorization: Bearer eyJ...
                                     <span class="com"># blank line = end of headers</span>
                                     <span class="com"># (body goes here for POST/PUT)</span>

<span class="com"># The response</span>
HTTP/1.1 200 OK                      <span class="com"># version, status code, reason</span>
Content-Type: application/json
Content-Length: 142

{"users": [...]}                     <span class="com"># body</span></div>
    </div>
    <div class="concept-card">
      <div class="concept-label">METHODS (VERBS)</div>
      <div class="concept-title">What You Want to Do</div>
      <table class="ai-table">
        <thead><tr><th>Method</th><th>Purpose</th><th>Safe?</th><th>Idempotent?</th></tr></thead>
        <tbody>
          <tr><td>GET</td><td>Retrieve data</td><td>Yes (no change)</td><td>Yes</td></tr>
          <tr><td>POST</td><td>Create / submit</td><td>No</td><td>No (repeats create dups)</td></tr>
          <tr><td>PUT</td><td>Replace entirely</td><td>No</td><td>Yes</td></tr>
          <tr><td>PATCH</td><td>Partial update</td><td>No</td><td>Usually no</td></tr>
          <tr><td>DELETE</td><td>Remove</td><td>No</td><td>Yes</td></tr>
          <tr><td>HEAD</td><td>Like GET, headers only</td><td>Yes</td><td>Yes</td></tr>
          <tr><td>OPTIONS</td><td>Ask what's allowed (CORS preflight)</td><td>Yes</td><td>Yes</td></tr>
        </tbody>
      </table>
      <div class="concept-desc"><strong>Idempotent</strong> = doing it twice has the same effect as once. Matters for retries: safely retry a PUT/DELETE, but a retried POST might create duplicates.</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">STATUS CODES</div>
      <div class="concept-title">The Server's Answer, by Category</div>
      <table class="ai-table">
        <thead><tr><th>Range</th><th>Meaning</th><th>Common Examples</th></tr></thead>
        <tbody>
          <tr><td>1xx</td><td>Informational</td><td>100 Continue, 101 Switching Protocols</td></tr>
          <tr><td>2xx</td><td>Success</td><td>200 OK, 201 Created, 204 No Content</td></tr>
          <tr><td>3xx</td><td>Redirection</td><td>301 Moved, 304 Not Modified, 307 Temp Redirect</td></tr>
          <tr><td>4xx</td><td>Client error (YOUR fault)</td><td>400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found, 429 Too Many Requests</td></tr>
          <tr><td>5xx</td><td>Server error (THEIR fault)</td><td>500 Internal Error, 502 Bad Gateway, 503 Unavailable, 504 Timeout</td></tr>
        </tbody>
      </table>
      <div class="concept-desc">Quick memory aid: <strong>4xx = you messed up</strong> (bad request, not allowed); <strong>5xx = the server messed up</strong>. 401 = "who are you?" (not authenticated); 403 = "I know who you are, but no" (not authorized).</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">HTTP VERSIONS</div>
      <div class="concept-title">1.1 → 2 → 3</div>
      <table class="ai-table">
        <thead><tr><th>Version</th><th>Key Change</th><th>Benefit</th></tr></thead>
        <tbody>
          <tr><td>HTTP/1.1</td><td>Text-based, one request at a time per connection</td><td>Simple; suffers head-of-line blocking</td></tr>
          <tr><td>HTTP/2</td><td>Binary, multiplexed streams over one connection</td><td>Many parallel requests, header compression — faster</td></tr>
          <tr><td>HTTP/3</td><td>Runs over QUIC (UDP) instead of TCP</td><td>No TCP head-of-line blocking; faster on lossy/mobile networks</td></tr>
        </tbody>
      </table>
      <div class="concept-desc"><strong>Statelessness:</strong> HTTP itself is stateless — each request is independent. "Sessions" are layered on top via cookies/tokens, because the protocol doesn't remember you between requests.</div>
    </div>
  </div>
</div>
"""

# ─────────────────────────────── SEC wave 27 ─────────────────────────────────
SEC_SENTINEL = "<!-- BEGINNER27-SEC v1 -->"
SEC_CONTENT = """
<!-- BEGINNER27-SEC v1 -->
<!-- ── TOPIC: ZERO TRUST ARCHITECTURE ────────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">🚫</span>
    <span class="topic-name">Zero Trust — Never Trust, Always Verify</span>
    <span class="topic-badge">SEC • Architecture</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">THE PARADIGM SHIFT</div>
      <div class="concept-title">The Castle-and-Moat Model Is Dead</div>
      <div class="concept-desc">Old security assumed a trusted "inside" (the corporate network) protected by a perimeter firewall — once you were in, you were trusted. But with cloud, remote work, and mobile, there is no clean inside/outside. And attackers who breach the perimeter get free rein. <strong>Zero Trust</strong> assumes the network is already hostile: trust nothing by default, verify every request explicitly, regardless of where it comes from.</div>
      <table class="ai-table">
        <thead><tr><th>Castle-and-Moat (Old)</th><th>Zero Trust (New)</th></tr></thead>
        <tbody>
          <tr><td>Trust based on network location</td><td>Trust based on identity + context, verified every time</td></tr>
          <tr><td>Inside = trusted</td><td>Inside = just as untrusted as outside</td></tr>
          <tr><td>One breach = lateral free movement</td><td>Each resource separately protected</td></tr>
          <tr><td>VPN grants broad network access</td><td>Per-app access, continuously re-verified</td></tr>
        </tbody>
      </table>
    </div>
    <div class="concept-card">
      <div class="concept-label">CORE PRINCIPLES</div>
      <div class="concept-title">The Three Tenets</div>
      <table class="ai-table">
        <thead><tr><th>Principle</th><th>Meaning</th></tr></thead>
        <tbody>
          <tr><td>Verify explicitly</td><td>Always authenticate &amp; authorize based on all available signals (identity, device, location, behavior)</td></tr>
          <tr><td>Least privilege access</td><td>Give minimal access, just-in-time and just-enough</td></tr>
          <tr><td>Assume breach</td><td>Act as if attackers are already inside — segment, monitor, limit blast radius</td></tr>
        </tbody>
      </table>
    </div>
    <div class="concept-card">
      <div class="concept-label">BUILDING BLOCKS</div>
      <div class="concept-title">What Implements Zero Trust</div>
      <table class="ai-table">
        <thead><tr><th>Component</th><th>Role</th></tr></thead>
        <tbody>
          <tr><td>Strong identity (IAM + MFA)</td><td>The new perimeter is identity — verify who</td></tr>
          <tr><td>Device posture</td><td>Is the device managed, patched, healthy?</td></tr>
          <tr><td>Microsegmentation</td><td>Divide the network into tiny zones — contain lateral movement</td></tr>
          <tr><td>Policy engine (PEP/PDP)</td><td>Decides allow/deny per request based on context</td></tr>
          <tr><td>Continuous monitoring</td><td>Re-evaluate trust constantly, not just at login</td></tr>
          <tr><td>Encryption everywhere</td><td>Protect data in transit even "inside"</td></tr>
        </tbody>
      </table>
    </div>
    <div class="concept-card">
      <div class="concept-label">IN PRACTICE</div>
      <div class="concept-title">A Real Implementation</div>
      <div class="concept-desc">Google's <strong>BeyondCorp</strong> is the famous reference implementation — employees access apps without a traditional VPN; every request is authenticated and authorized based on user identity and device trust, whether they're in the office or a coffee shop. Modern tools (Cloudflare Access, Tailscale, Zscaler, Azure AD Conditional Access) bring Zero Trust to organizations of any size. <strong>Note:</strong> Zero Trust is a strategy and journey, not a single product you buy — beware vendors selling "the Zero Trust box."</div>
    </div>
  </div>
</div>
"""

# ─────────────────────────────── OPS wave 27 ─────────────────────────────────
OPS_SENTINEL = "<!-- BEGINNER27-OPS v1 -->"
OPS_CONTENT = """
<!-- BEGINNER27-OPS v1 -->
<!-- ── TOPIC: SRE PRINCIPLES ─────────────────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">🎚️</span>
    <span class="topic-name">SRE — Engineering Reliability with Data, Not Heroics</span>
    <span class="topic-badge">OPS • Modern</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">WHAT IS SRE</div>
      <div class="concept-title">"What Happens When a Software Engineer Runs Operations"</div>
      <div class="concept-desc">Site Reliability Engineering (SRE), pioneered at Google, applies software-engineering thinking to operations. Instead of manually firefighting, SREs use code, automation, and data to make systems reliable at scale. The core insight: reliability is a feature you can measure and budget for — not an absolute. 100% reliability is the wrong target (it's impossibly expensive and users can't even tell).</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">ERROR BUDGETS</div>
      <div class="concept-title">Reliability You Can Spend</div>
      <div class="concept-desc">If your SLO is 99.9% availability, then 0.1% unreliability is your <strong>error budget</strong> — about 43 minutes/month you're "allowed" to be down. This brilliantly resolves the eternal dev-vs-ops conflict: as long as you're within budget, ship features fast. Blow the budget? Freeze features and focus on reliability. It turns reliability into a shared, data-driven decision instead of an argument.</div>
      <table class="ai-table">
        <thead><tr><th>SLO</th><th>Downtime/month</th><th>Downtime/year</th></tr></thead>
        <tbody>
          <tr><td>99% (two nines)</td><td>~7.3 hours</td><td>~3.65 days</td></tr>
          <tr><td>99.9% (three nines)</td><td>~43 minutes</td><td>~8.8 hours</td></tr>
          <tr><td>99.99% (four nines)</td><td>~4.3 minutes</td><td>~52 minutes</td></tr>
          <tr><td>99.999% (five nines)</td><td>~26 seconds</td><td>~5.3 minutes</td></tr>
        </tbody>
      </table>
    </div>
    <div class="concept-card">
      <div class="concept-label">TOIL</div>
      <div class="concept-title">The Enemy of Engineering</div>
      <div class="concept-desc"><strong>Toil</strong> is manual, repetitive, automatable work that scales linearly with growth and produces no lasting value — resetting passwords by hand, manually restarting services, copy-pasting between dashboards. SRE culture caps toil (often at ~50% of time) and invests the rest in automation and engineering that <em>eliminates</em> toil. If you're doing something tedious for the third time, that's a signal to automate it.</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">CHAOS ENGINEERING</div>
      <div class="concept-title">Break It on Purpose, on Your Terms</div>
      <div class="concept-desc">Chaos engineering deliberately injects failures (kill a server, add latency, drop a dependency) into systems — ideally in production, carefully — to discover weaknesses <em>before</em> they cause real outages. Netflix's "Chaos Monkey" randomly kills instances to force engineers to build resilient systems. The philosophy: you don't truly know your system is resilient until you've tested it failing. Start small, in a controlled blast radius, with a hypothesis and a way to abort.</div>
    </div>
  </div>
</div>
"""

# ─────────────────────────────── LIFESTYLE wave 27 ───────────────────────────
LIFE_SENTINEL = "<!-- BEGINNER27-LIFE v1 -->"
LIFE_CONTENT = """
<!-- BEGINNER27-LIFE v1 -->
<!-- ── TOPIC: GROWING INTO SENIOR ROLES ──────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">🌱</span>
    <span class="topic-name">Growing Into Senior — Beyond Technical Skill</span>
    <span class="topic-badge">LIFESTYLE • Career</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">THE SHIFT</div>
      <div class="concept-title">Senior Isn't "Knows More Commands"</div>
      <div class="concept-desc">The jump from junior to senior isn't about memorizing more technology — it's about <em>scope and judgment</em>. Juniors are given problems and solve them. Seniors find the right problems, navigate ambiguity, anticipate consequences, and make others around them better. The technical bar matters, but what truly distinguishes seniors is how they think, communicate, and multiply the team's output.</div>
      <table class="ai-table">
        <thead><tr><th>Junior</th><th>Senior</th></tr></thead>
        <tbody>
          <tr><td>Solves the task given</td><td>Questions whether it's the right task</td></tr>
          <tr><td>Needs clear instructions</td><td>Thrives in ambiguity, defines the approach</td></tr>
          <tr><td>Focuses on "does it work?"</td><td>Considers maintainability, risk, tradeoffs, the team</td></tr>
          <tr><td>Local view (my task)</td><td>Systems view (how it fits the whole)</td></tr>
          <tr><td>Asks "how do I do X?"</td><td>Asks "should we do X, and what breaks if we do?"</td></tr>
        </tbody>
      </table>
    </div>
    <div class="concept-card">
      <div class="concept-label">FORCE MULTIPLIERS</div>
      <div class="concept-title">Habits That Build Seniority</div>
      <table class="ai-table">
        <thead><tr><th>Habit</th><th>Why It Compounds</th></tr></thead>
        <tbody>
          <tr><td>Write things down</td><td>Docs/designs scale your knowledge beyond your hours</td></tr>
          <tr><td>Make others better</td><td>Mentoring, good code reviews — your impact multiplies</td></tr>
          <tr><td>Think in tradeoffs</td><td>"It depends" + explaining why = senior judgment</td></tr>
          <tr><td>Communicate up and across</td><td>Translate tech ↔ business; influence without authority</td></tr>
          <tr><td>Own outcomes, not just tasks</td><td>See it through to working in production</td></tr>
          <tr><td>Reduce, don't add, complexity</td><td>The best seniors make systems simpler</td></tr>
        </tbody>
      </table>
    </div>
    <div class="concept-card">
      <div class="concept-label">IC OR MANAGER?</div>
      <div class="concept-title">Two Valid Ladders</div>
      <div class="concept-desc">Growth doesn't require becoming a manager. Most organizations have two parallel tracks: the <strong>Individual Contributor (IC)</strong> track (Senior → Staff → Principal engineer) and the <strong>Management</strong> track (Lead → Manager → Director). Staff+ ICs have just as much seniority and impact as managers — through deep technical leadership rather than people management. Choose based on what energizes you: solving hard technical problems, or growing people and teams. Neither is "higher."</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">THE LONG GAME</div>
      <div class="concept-title">Mindsets That Sustain a Decades-Long Career</div>
      <div class="concept-desc">The wisdom threaded through this whole guide applies most at senior levels. <strong>"Verify, don't assume"</strong> — senior mistakes are bigger, so your discipline matters more. <strong>"Not my circus, not my monkeys"</strong> — seniors are pulled in every direction; protecting your focus and boundaries is survival. <strong>"You can't make someone make the right choice, but you can pick up the pieces"</strong> — you'll advise leaders who overrule you; document, let go, and be the calm one who helps recover. Add to these: stay curious (the field never stops changing), be generous with knowledge (reputation compounds), and protect your health and relationships — a burned-out expert helps no one. The marathon, not the sprint, is what builds a great career.</div>
    </div>
  </div>
</div>
"""

# ─────────────────────────────── INJECT LOGIC ────────────────────────────────
def inject(html: str, anchor: str, sentinel: str, content: str) -> tuple[str, bool]:
    if sentinel in html:
        return html, False
    pos = html.find(anchor)
    if pos == -1:
        return html, False
    return html[:pos] + content + html[pos:], True

def main():
    path = Path("index.html")
    html = path.read_text(encoding="utf-8")

    injections = [
        (SCRIPT_INJECT_ANCHOR, SCRIPT_SENTINEL, SCRIPT_CONTENT),
        (NET_INJECT_ANCHOR,    NET_SENTINEL,    NET_CONTENT),
        (SEC_INJECT_ANCHOR,    SEC_SENTINEL,    SEC_CONTENT),
        (OPS_INJECT_ANCHOR,    OPS_SENTINEL,    OPS_CONTENT),
        (LIFE_INJECT_ANCHOR,   LIFE_SENTINEL,   LIFE_CONTENT),
    ]

    for anchor, sentinel, content in injections:
        new_html, changed = inject(html, anchor, sentinel, content)
        if changed:
            added = len(new_html) - len(html)
            html = new_html
            print(f"  [ok] Injected +{added:,} chars before '{anchor}' in index.html")
        else:
            label = anchor.replace("<!-- /domain-body ", "").replace(" -->", "")
            print(f"  [--] Skipped '{label}' (already present)")

    path.write_text(html, encoding="utf-8")

    from html.parser import HTMLParser
    class TagChecker(HTMLParser):
        VOID = {"area","base","br","col","embed","hr","img","input",
                "link","meta","param","source","track","wbr"}
        def __init__(self):
            super().__init__()
            self.stack = []
            self.errors = []
        def handle_starttag(self, tag, attrs):
            if tag not in self.VOID:
                self.stack.append(tag)
        def handle_endtag(self, tag):
            if tag in self.VOID:
                return
            if self.stack and self.stack[-1] == tag:
                self.stack.pop()
            else:
                self.errors.append(f"Stray </{tag}>")

    checker = TagChecker()
    checker.feed(html)
    print(f"\n  Unclosed at EOF: {', '.join(checker.stack) if checker.stack else 'NONE'}")
    print(f"  Stray end tags: {len(checker.errors)}")
    print(f"\n  index.html: {len(html):,} bytes")

if __name__ == "__main__":
    main()
