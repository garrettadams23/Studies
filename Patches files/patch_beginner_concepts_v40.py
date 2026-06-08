#!/usr/bin/env python3
"""Wave 40: beginner-friendly content additions across 5 domains."""
import re
from html.parser import HTMLParser

S_OPS = "<!-- BEGINNER40-OPS v1 -->"
A_OPS = "<!-- /domain-body ops -->"
C_OPS = S_OPS + """
<div class="topic">
  <div class="topic-header">
    <span class="topic-badge">Beginner</span>
    <h3>Writing Runbooks That People Actually Follow</h3>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <span class="concept-label">Concept</span>
      <h4 class="concept-title">A runbook is a conversation with your future self at 3 AM</h4>
      <p class="concept-desc">A runbook is a step-by-step procedure for handling a specific operational situation —
      restarting a stuck service, failing over a database, rotating an expired certificate. The test of a good runbook
      isn't whether the author understands it; it's whether a half-asleep on-call engineer who has never touched this
      system can follow it correctly under pressure, at 3 AM, without calling anyone for help.</p>
    </div>
    <div class="concept-card">
      <span class="concept-label">Concept</span>
      <h4 class="concept-title">The anatomy of a runbook that survives contact with reality</h4>
      <table class="ai-table">
        <tr><th>Section</th><th>Purpose</th><th>What goes wrong without it</th></tr>
        <tr><td>Trigger / symptoms</td><td>How do you know this runbook applies right now?</td><td>Engineer wastes 20 minutes confirming they're even looking at the right problem</td></tr>
        <tr><td>Blast radius / impact</td><td>Who and what is affected if this goes wrong further?</td><td>Nobody escalates because nobody realized how big the problem actually was</td></tr>
        <tr><td>Preconditions</td><td>What access, tools, or state do you need before starting?</td><td>Engineer gets halfway through and discovers they don't have the right permissions</td></tr>
        <tr><td>Numbered steps with exact commands</td><td>Remove all guesswork — copy, paste, run</td><td>"Restart the service" becomes a 45-minute detour into "which service, on which host, with which flag?"</td></tr>
        <tr><td>Verification step</td><td>How do you confirm the fix actually worked?</td><td>Engineer declares victory, closes the ticket, and the issue recurs an hour later</td></tr>
        <tr><td>Rollback / escalation path</td><td>What do you do if this *doesn't* work?</td><td>Engineer freezes, unsure whether to keep pushing or wake someone up</td></tr>
      </table>
    </div>
    <div class="concept-card">
      <span class="concept-label">Hands-on</span>
      <h4 class="concept-title">A short runbook excerpt, written the right way</h4>
      <pre class="code-block"><span class="com"># RUNBOOK: API gateway returning 503s</span>

<span class="com"># TRIGGER: PagerDuty alert "gateway-503-rate-high" fires when error
# rate > 5% for 5 minutes straight.</span>

<span class="com"># IMPACT: All customer-facing API traffic degraded. Treat as SEV-2.</span>

<span class="com"># STEP 1 — confirm the alert is real, not a monitoring blip</span>
curl -s -o /dev/null -w &quot;%{http_code}\\n&quot; https://api.internal.example.com/healthz
<span class="com"># Expect: 200. If you see 503 here too, this is real — continue.</span>

<span class="com"># STEP 2 — check whether it's one node or all of them</span>
kubectl get pods -n gateway -o wide
<span class="com"># Look for pods stuck in CrashLoopBackOff or 0/1 Ready</span>

<span class="com"># STEP 3 — restart only the unhealthy pods (NOT the whole deployment)</span>
kubectl delete pod &lt;pod-name&gt; -n gateway
<span class="com"># Kubernetes will reschedule it automatically — this is non-destructive</span>

<span class="com"># VERIFY — error rate back under 1% for 5 consecutive minutes</span>
watch -n 10 'curl -s https://api.internal.example.com/metrics | grep error_rate'

<span class="com"># IF STILL FAILING after step 3 — STOP. Escalate to #platform-oncall.
# Do not attempt a full deployment restart without a second engineer present.</span></pre>
    </div>
    <div class="concept-card">
      <span class="concept-label">Mindset</span>
      <h4 class="concept-title">You can't make someone make the right choice...</h4>
      <p class="concept-desc"><strong>...yet you can pick up the pieces afterwards.</strong> No matter how clear your
      runbook is, someone under pressure will eventually skip the verification step, run the command on the wrong host,
      or improvise instead of escalating. That's not a reason to stop writing good runbooks — it's the reason to also
      write the recovery procedure for "someone did the wrong thing." The best operational teams plan for both the happy
      path and the moment a tired human deviates from it.</p>
    </div>
  </div>
</div>
""" + "\n" + A_OPS

S_SHORTCUT = "<!-- BEGINNER40-SHORTCUT v1 -->"
A_SHORTCUT = "<!-- /domain-body shortcuts -->"
C_SHORTCUT = S_SHORTCUT + """
<div class="topic">
  <div class="topic-header">
    <span class="topic-badge">Beginner</span>
    <h3>Browser Power Moves – Tabs, History, and DevTools Shortcuts</h3>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <span class="concept-label">Concept</span>
      <h4 class="concept-title">Most people use 10% of their browser</h4>
      <p class="concept-desc">If you spend your day in a browser — and almost everyone in IT does — a handful of muscle-memory
      shortcuts can save you dozens of clicks an hour. These work across Chrome, Edge, and Firefox unless noted otherwise
      (swap <code>Ctrl</code> for <code>Cmd</code> on macOS).</p>
    </div>
    <div class="concept-card">
      <span class="concept-label">Reference</span>
      <h4 class="concept-title">Tab and window management</h4>
      <table class="ai-table">
        <tr><th>Shortcut</th><th>What it does</th></tr>
        <tr><td><code>Ctrl+T</code></td><td>Open a new tab</td></tr>
        <tr><td><code>Ctrl+Shift+T</code></td><td>Reopen the last closed tab (works multiple times — it's a stack!)</td></tr>
        <tr><td><code>Ctrl+Tab</code> / <code>Ctrl+Shift+Tab</code></td><td>Jump to the next / previous tab</td></tr>
        <tr><td><code>Ctrl+1</code> through <code>Ctrl+8</code></td><td>Jump directly to tab 1–8 by position</td></tr>
        <tr><td><code>Ctrl+9</code></td><td>Jump to the <em>last</em> tab, no matter how many are open</td></tr>
        <tr><td><code>Ctrl+L</code> or <code>Alt+D</code></td><td>Jump straight to the address bar (faster than clicking)</td></tr>
        <tr><td><code>Ctrl+Shift+N</code></td><td>Open a new incognito/private window — handy for testing as a "logged out" user</td></tr>
      </table>
    </div>
    <div class="concept-card">
      <span class="concept-label">Reference</span>
      <h4 class="concept-title">Navigation, search, and page tools</h4>
      <table class="ai-table">
        <tr><th>Shortcut</th><th>What it does</th></tr>
        <tr><td><code>Ctrl+F</code></td><td>Find text on the current page — your fastest way to locate something in a long doc or log dump</td></tr>
        <tr><td><code>Ctrl+H</code></td><td>Open browsing history — useful for re-finding "that ticket from yesterday"</td></tr>
        <tr><td><code>Alt+Left</code> / <code>Alt+Right</code></td><td>Back / forward (faster than reaching for the mouse)</td></tr>
        <tr><td><code>Ctrl+R</code> / <code>F5</code></td><td>Reload the page</td></tr>
        <tr><td><code>Ctrl+Shift+R</code></td><td>Hard reload — bypasses the cache (your go-to when "the page looks wrong" after a deploy)</td></tr>
        <tr><td><code>Ctrl+D</code></td><td>Bookmark the current page</td></tr>
      </table>
    </div>
    <div class="concept-card">
      <span class="concept-label">Hands-on</span>
      <h4 class="concept-title">DevTools shortcuts every helpdesk and dev should know</h4>
      <table class="ai-table">
        <tr><th>Shortcut</th><th>What it does</th></tr>
        <tr><td><code>F12</code> or <code>Ctrl+Shift+I</code></td><td>Open Developer Tools — your window into what the page is actually doing</td></tr>
        <tr><td><code>Ctrl+Shift+J</code></td><td>Jump straight to the Console tab (where JavaScript errors show up)</td></tr>
        <tr><td><code>Ctrl+Shift+C</code></td><td>"Inspect element" mode — click anything on the page to see its underlying HTML/CSS</td></tr>
        <tr><td>Network tab + <code>Ctrl+R</code></td><td>Watch every request the page makes as it loads — essential for "why is this slow / broken?"</td></tr>
      </table>
      <p class="concept-desc">When a user reports "the website is broken," opening the Console tab before doing anything
      else often shows you the actual JavaScript error in seconds — turning a vague complaint into an actionable bug
      report you can hand to a developer.</p>
    </div>
    <div class="concept-card">
      <span class="concept-label">Mindset</span>
      <h4 class="concept-title">Assume makes an ass out of you and me</h4>
      <p class="concept-desc">"It works fine for me" is rarely the end of the story — it might be a cached version of the
      page, a browser extension interfering, or a cookie holding onto stale session data. Before assuming the user is
      "doing something wrong," try <code>Ctrl+Shift+N</code> for a clean incognito window: if the problem disappears there,
      you've just proven it's local to their browser profile, not the website — and saved everyone a lot of back-and-forth.</p>
    </div>
  </div>
</div>
""" + "\n" + A_SHORTCUT

S_AI = "<!-- BEGINNER40-AI v1 -->"
A_AI = "<!-- /domain-body ai -->"
C_AI = S_AI + """
<div class="topic">
  <div class="topic-header">
    <span class="topic-badge">Beginner</span>
    <h3>Tokens, Context Windows, and Why "Just Paste the Whole Codebase" Doesn't Work</h3>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <span class="concept-label">Concept</span>
      <h4 class="concept-title">A model doesn't read words — it reads tokens</h4>
      <p class="concept-desc">Before a language model can process text, it breaks it into <em>tokens</em> — chunks that are
      often smaller than a whole word. "Networking" might become "Network" + "ing"; a rare word might be split into three
      or four pieces; a single emoji can cost several tokens. As a rough rule of thumb in English, <strong>~4 characters ≈
      1 token</strong>, or roughly 75 words ≈ 100 tokens. This matters because nearly everything about how you interact with
      a model — cost, speed, and especially how much it can "see" at once — is measured in tokens, not words or characters.</p>
    </div>
    <div class="concept-card">
      <span class="concept-label">Concept</span>
      <h4 class="concept-title">The context window: the model's "working memory"</h4>
      <p class="concept-desc">A context window is the maximum number of tokens a model can consider at one time — your
      entire conversation, system instructions, retrieved documents, and the model's own response all have to fit inside
      it. Once a conversation grows past that limit, the oldest content has to be dropped or summarized to make room for
      new content. Picture a desk of fixed size: you can pile on more papers, but eventually something falls off the back
      to make room for what you just placed in front of you.</p>
      <table class="ai-table">
        <tr><th>Context size</th><th>Roughly equivalent to</th></tr>
        <tr><td>4,000 tokens</td><td>About 6 pages of double-spaced text</td></tr>
        <tr><td>32,000 tokens</td><td>A short novella, or a medium-sized source code file plus its tests</td></tr>
        <tr><td>200,000 tokens</td><td>A few hundred pages — a small book, or a sizeable chunk of a real codebase</td></tr>
      </table>
    </div>
    <div class="concept-card">
      <span class="concept-label">Common pitfall</span>
      <h4 class="concept-title">"I'll just paste the whole codebase in" — and three things that go wrong</h4>
      <ol>
        <li><strong>It might not fit.</strong> A real production codebase is often millions of tokens — far beyond any
        context window — so the bulk of it gets silently truncated, and you may not even notice which parts.</li>
        <li><strong>Signal gets diluted.</strong> Even when it technically fits, burying the three relevant files inside
        ten thousand irrelevant lines makes it harder — not easier — for the model to find what actually matters to your
        question. More context isn't free; it's a tradeoff.</li>
        <li><strong>Cost and latency scale with tokens.</strong> Both the time to get a response and (for paid APIs) the
        price you pay typically scale with how many tokens you send and receive. A 200,000-token prompt isn't just slower
        — it can be dramatically more expensive than a focused 2,000-token one that gets the same job done.</li>
      </ol>
      <p class="concept-desc">The skilled move isn't "give the model everything" — it's "give the model exactly what it
      needs to answer this specific question," which is precisely the problem that techniques like RAG (retrieval-augmented
      generation) and good prompt scoping are designed to solve.</p>
    </div>
    <div class="concept-card">
      <span class="concept-label">Hands-on</span>
      <h4 class="concept-title">Estimating token counts yourself</h4>
      <pre class="code-block"><span class="com"># pip install tiktoken</span>
<span class="kw">import</span> tiktoken

encoder = tiktoken.get_encoding(<span class="str">&quot;cl100k_base&quot;</span>)
text = <span class="str">&quot;Not my circus, not my monkey — but I'll still help you find the owner.&quot;</span>

tokens = encoder.encode(text)
<span class="fn">print</span>(<span class="str">f&quot;Characters: {len(text)}&quot;</span>)
<span class="fn">print</span>(<span class="str">f&quot;Tokens:     {len(tokens)}&quot;</span>)
<span class="fn">print</span>(<span class="str">f&quot;First few token IDs: {tokens[:5]}&quot;</span>)
<span class="com"># Try this on a paragraph of your own writing vs. a block of code —
# notice how code and unusual words tend to use *more* tokens per
# character than plain English prose.</span></pre>
    </div>
  </div>
</div>
""" + "\n" + A_AI

S_NET = "<!-- BEGINNER40-NET v1 -->"
A_NET = "<!-- /domain-body net -->"
C_NET = S_NET + """
<div class="topic">
  <div class="topic-header">
    <span class="topic-badge">Beginner</span>
    <h3>VPNs Explained – Tunnels, Encryption, and What They Don't Do</h3>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <span class="concept-label">Concept</span>
      <h4 class="concept-title">A VPN is a private tunnel through a public road</h4>
      <p class="concept-desc">Imagine the internet as a public highway system — anyone running the right equipment at the
      right point could, in theory, see which trucks are going where. A VPN (Virtual Private Network) builds an
      encrypted tunnel through that highway: your traffic still travels over the same public infrastructure, but it's
      wrapped in a layer that hides its contents from anyone watching the road, and makes it appear to originate from the
      tunnel's far end rather than your actual location.</p>
    </div>
    <div class="concept-card">
      <span class="concept-label">Concept</span>
      <h4 class="concept-title">Two very different reasons people use VPNs</h4>
      <table class="ai-table">
        <tr><th>Use case</th><th>What it actually does</th><th>Common protocols</th></tr>
        <tr><td>Corporate / remote-access VPN</td><td>Lets an employee's laptop join the company's internal network from anywhere, as if it were plugged in at the office</td><td>WireGuard, OpenVPN, IPsec/IKEv2, Cisco AnyConnect</td></tr>
        <tr><td>Consumer / privacy VPN</td><td>Routes your traffic through a third-party provider's server so your ISP and local network can't see *what* you're accessing — though the VPN provider now can</td><td>WireGuard, OpenVPN (commercial offerings)</td></tr>
      </table>
      <p class="concept-desc">These solve different problems for different threat models. A corporate VPN exists so IT can
      extend a trusted network boundary to remote workers; a consumer VPN exists to shift *who* has visibility into your
      traffic — from your ISP to the VPN provider — which is a meaningfully different guarantee than "no one can see what
      I do online."</p>
    </div>
    <div class="concept-card">
      <span class="concept-label">Hands-on</span>
      <h4 class="concept-title">Setting up a minimal WireGuard tunnel (lab environment)</h4>
      <pre class="code-block"><span class="com"># Install WireGuard (Debian/Ubuntu)</span>
sudo apt install wireguard

<span class="com"># Generate a public/private keypair for this peer</span>
wg genkey | tee privatekey | wg pubkey > publickey

<span class="com"># Minimal config: /etc/wireguard/wg0.conf
# (replace placeholders with real keys and addresses)</span>
<span class="com">#
# [Interface]
# PrivateKey = &lt;this peer's private key&gt;
# Address = 10.10.0.2/24
#
# [Peer]
# PublicKey = &lt;remote peer's public key&gt;
# Endpoint = vpn.example.com:51820
# AllowedIPs = 0.0.0.0/0
# PersistentKeepalive = 25</span>

<span class="com"># Bring the tunnel up and check its status</span>
sudo wg-quick up wg0
sudo wg show

<span class="com"># Confirm your traffic is actually routing through the tunnel</span>
curl https://ifconfig.me</pre>
      <p class="concept-desc">The <span class="kw">AllowedIPs = 0.0.0.0/0</span> line is the one to read carefully — it tells
      the system to route <em>all</em> traffic through the tunnel ("full tunnel"), versus a narrower range that only sends
      specific destinations through it ("split tunnel"). Getting this wrong is one of the most common VPN
      misconfigurations: too broad and you may break local network access; too narrow and traffic you meant to protect
      goes out in the clear.</p>
    </div>
    <div class="concept-card">
      <span class="concept-label">Common pitfall</span>
      <h4 class="concept-title">"I'm on a VPN, so I'm anonymous" — assume makes an ass out of you and me</h4>
      <p class="concept-desc">A VPN hides your traffic's path and contents from your local network and ISP — it does
      <em>not</em> make you anonymous to the websites you visit. You can still be tracked through cookies, browser
      fingerprinting, account logins, and the VPN provider itself can see (and in some jurisdictions, may be compelled to
      log and disclose) your activity. Treat "I'm using a VPN" as one layer of a privacy strategy, not a magic cloak —
      and always read a provider's actual logging policy rather than assuming "no logs" means what it sounds like.</p>
    </div>
  </div>
</div>
""" + "\n" + A_NET

S_SEC = "<!-- BEGINNER40-SEC v1 -->"
A_SEC = "<!-- /domain-body sec -->"
C_SEC = S_SEC + """
<div class="topic">
  <div class="topic-header">
    <span class="topic-badge">Beginner</span>
    <h3>Phishing Beyond Email – Smishing, Vishing, and QR Code Scams</h3>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <span class="concept-label">Concept</span>
      <h4 class="concept-title">Phishing isn't just an email problem anymore</h4>
      <p class="concept-desc">Years of "don't click suspicious email links" training pushed attackers toward channels
      where users are less guarded — text messages, phone calls, and even printed QR codes. The underlying trick is
      identical in every case: create urgency, impersonate someone trusted, and get the target to act before they think.
      Only the delivery method changes.</p>
    </div>
    <div class="concept-card">
      <span class="concept-label">Concept</span>
      <h4 class="concept-title">Know the family of attacks</h4>
      <table class="ai-table">
        <tr><th>Term</th><th>Channel</th><th>Typical pretext</th></tr>
        <tr><td>Phishing</td><td>Email</td><td>"Your account will be suspended — click here to verify"</td></tr>
        <tr><td>Smishing</td><td>SMS / text message</td><td>"Your package couldn't be delivered — confirm your address" with a shortened link</td></tr>
        <tr><td>Vishing</td><td>Phone call (often with spoofed caller ID)</td><td>"This is IT support — we detected a virus on your machine, I need your password to fix it"</td></tr>
        <tr><td>Quishing</td><td>QR codes (on posters, parking meters, restaurant tables)</td><td>A sticker placed over a legitimate QR code, redirecting to a cloned login page</td></tr>
        <tr><td>Spear phishing</td><td>Any of the above, but personalized</td><td>References your actual manager's name, a real project, or a recent purchase — built from information gathered about you specifically</td></tr>
      </table>
    </div>
    <div class="concept-card">
      <span class="concept-label">Hands-on</span>
      <h4 class="concept-title">Checking a suspicious link or QR code before you tap it</h4>
      <pre class="code-block"><span class="com"># Never scan a suspicious QR code with an app that auto-opens links.
# Use a scanner that shows you the destination URL FIRST.</span>

<span class="com"># On a computer, hover (don't click) to preview where a link
# actually goes — the displayed text and the real destination
# are often two very different things</span>

<span class="com"># Expand a shortened URL safely before visiting it</span>
curl -sI https://bit.ly/suspicious-looking-link | grep -i location

<span class="com"># Check a domain's age and registration — brand-new domains
# pretending to be your bank are an enormous red flag</span>
whois suspicious-domain.com | grep -iE &quot;creation date|registrar&quot;</pre>
    </div>
    <div class="concept-card">
      <span class="concept-label">Mindset</span>
      <h4 class="concept-title">Assume makes an ass out of you and me — verify out-of-band</h4>
      <p class="concept-desc">If a text message claims to be from your bank, don't tap the link in the message to "check."
      Open your banking app directly, or call the number printed on the back of your card — never a number provided in
      the suspicious message itself. This is called <em>out-of-band verification</em>: confirming a claim through a
      channel the attacker doesn't control. The thirty seconds it costs you is far cheaper than assuming the message is
      legitimate and being wrong.</p>
    </div>
    <div class="concept-card">
      <span class="concept-label">Mindset</span>
      <h4 class="concept-title">You can't make someone make the right choice...</h4>
      <p class="concept-desc"><strong>...yet you can pick up the pieces afterwards.</strong> If a coworker admits they
      tapped a smishing link or gave information over a vishing call, the worst response is blame — that just guarantees
      the next person stays quiet about it. The right response is the same one you'd want for yourself: help them change
      the affected credentials, report it so the broader team can be warned, and treat the disclosure itself as the
      responsible action it actually was.</p>
    </div>
  </div>
</div>
""" + "\n" + A_SEC


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
    (A_SHORTCUT, S_SHORTCUT, C_SHORTCUT),
    (A_AI, S_AI, C_AI),
    (A_NET, S_NET, C_NET),
    (A_SEC, S_SEC, C_SEC),
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
