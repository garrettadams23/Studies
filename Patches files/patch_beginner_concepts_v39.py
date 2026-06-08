#!/usr/bin/env python3
"""Wave 39: beginner-friendly content additions across 5 domains."""
import re
from html.parser import HTMLParser

S_NET = "<!-- BEGINNER39-NET v1 -->"
A_NET = "<!-- /domain-body net -->"
C_NET = S_NET + """
<div class="topic">
  <div class="topic-header">
    <span class="topic-badge">Beginner</span>
    <h3>DNS Deep Dive – How Name Resolution Really Works</h3>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <span class="concept-label">Mindset</span>
      <h4 class="concept-title">Assume makes an ass out of you and me</h4>
      <p class="concept-desc">When a website "won't load," don't assume it's the web server. DNS failures look identical
      to outages from the user's perspective. Walking the resolution chain step by step — instead of guessing — is what
      separates a five-minute fix from an hour of chasing the wrong problem.</p>
    </div>
    <div class="concept-card">
      <span class="concept-label">Concept</span>
      <h4 class="concept-title">The resolution chain, in order</h4>
      <p class="concept-desc">When you type <code>example.com</code> into a browser, your computer doesn't magically know
      where to send the request. It walks a chain of lookups:</p>
      <table class="ai-table">
        <tr><th>Step</th><th>What happens</th><th>Where it's checked</th></tr>
        <tr><td>1. Browser cache</td><td>"Have I looked this up in the last few minutes?"</td><td>Browser memory</td></tr>
        <tr><td>2. OS cache</td><td>"Does the operating system already know this?"</td><td><code>systemd-resolved</code> / <code>dnsmasq</code> / Windows DNS Client</td></tr>
        <tr><td>3. Hosts file</td><td>"Is there a manual override?"</td><td><code>/etc/hosts</code> or <code>C:\\Windows\\System32\\drivers\\etc\\hosts</code></td></tr>
        <tr><td>4. Recursive resolver</td><td>"Ask my configured DNS server (ISP, 1.1.1.1, 8.8.8.8) to find it"</td><td><code>/etc/resolv.conf</code></td></tr>
        <tr><td>5. Root → TLD → authoritative</td><td>The resolver walks the DNS hierarchy until it finds the authoritative answer</td><td>Global DNS infrastructure</td></tr>
      </table>
      <p class="concept-desc">Most "the website is down" tickets are solved at step 2 or 3 — a stale cache entry or a
      leftover hosts file edit from testing months ago.</p>
    </div>
    <div class="concept-card">
      <span class="concept-label">Hands-on</span>
      <h4 class="concept-title">Tracing resolution yourself</h4>
      <pre class="code-block"><span class="com"># See which resolver your system is configured to use</span>
cat /etc/resolv.conf

<span class="com"># Look up a name and show the full trip — timing included</span>
dig example.com

<span class="com"># Trace the entire chain from the root servers down (educational, slower)</span>
dig +trace example.com

<span class="com"># Ask a *specific* DNS server directly, bypassing your default resolver</span>
dig @1.1.1.1 example.com

<span class="com"># Check what record types exist — A (IPv4), AAAA (IPv6), MX (mail), TXT, CNAME</span>
dig example.com MX
dig example.com TXT

<span class="com"># Reverse lookup: what name does this IP resolve back to?</span>
dig -x 93.184.216.34</pre>
      <p class="concept-desc">The <span class="kw">+trace</span> flag is especially good for learning — it shows the
      actual hierarchy: your resolver asks a root server "who handles .com?", then asks that TLD server "who handles
      example.com?", then finally asks the authoritative server for the actual IP.</p>
    </div>
    <div class="concept-card">
      <span class="concept-label">Common pitfall</span>
      <h4 class="concept-title">"It works on my machine" — DNS cache edition</h4>
      <p class="concept-desc">A classic scenario: a developer changes a DNS record, tells you "it's updated," and your
      browser still shows the old site. Both of you are right — the record changed at the authoritative server, but your
      resolver cached the old answer for its full TTL (time-to-live). Common fixes, in order of how invasive they are:</p>
      <pre class="code-block"><span class="com"># Flush just your local OS resolver cache (Linux with systemd-resolved)</span>
sudo resolvectl flush-caches

<span class="com"># macOS</span>
sudo dscacheutil -flushcache; sudo killall -HUP mDNSResponder

<span class="com"># Windows (run as administrator)</span>
ipconfig /flushdns

<span class="com"># Or simply query a different resolver to sanity-check the *real* current value</span>
dig @8.8.8.8 example.com +short</pre>
      <p class="concept-desc">If a record was just changed, remember that TTL still applies globally — other people's
      resolvers around the world will keep serving the cached answer until their TTL expires too. This is why planned DNS
      cutovers lower the TTL days in advance.</p>
    </div>
  </div>
</div>
""" + "\n" + A_NET

S_AI = "<!-- BEGINNER39-AI v1 -->"
A_AI = "<!-- /domain-body ai -->"
C_AI = S_AI + """
<div class="topic">
  <div class="topic-header">
    <span class="topic-badge">Beginner</span>
    <h3>Retrieval-Augmented Generation (RAG) Explained Simply</h3>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <span class="concept-label">Concept</span>
      <h4 class="concept-title">Why RAG exists: the "stale textbook" problem</h4>
      <p class="concept-desc">A language model is trained on a snapshot of text up to some cutoff date. Ask it about your
      company's internal wiki, last week's incident report, or this morning's product release, and it simply has no idea
      — that information was never in its training data. RAG solves this by giving the model a way to <em>look things up</em>
      at the moment you ask, rather than relying purely on what it memorized during training.</p>
    </div>
    <div class="concept-card">
      <span class="concept-label">Concept</span>
      <h4 class="concept-title">The RAG pipeline, step by step</h4>
      <table class="ai-table">
        <tr><th>Step</th><th>What happens</th><th>Plain-language analogy</th></tr>
        <tr><td>1. Chunk</td><td>Break documents into small overlapping pieces (e.g. 500 words)</td><td>Tearing a textbook into index cards</td></tr>
        <tr><td>2. Embed</td><td>Convert each chunk into a vector of numbers that captures its meaning</td><td>Filing each card by topic, not alphabetically</td></tr>
        <tr><td>3. Store</td><td>Save the vectors in a vector database (Chroma, Pinecone, pgvector, FAISS)</td><td>The filing cabinet itself</td></tr>
        <tr><td>4. Retrieve</td><td>When a question comes in, embed it too and find the most similar stored chunks</td><td>Pulling the most relevant index cards</td></tr>
        <tr><td>5. Augment + Generate</td><td>Stuff those chunks into the prompt alongside the question, then ask the model to answer using them</td><td>Handing the cards to an expert and asking them to summarize</td></tr>
      </table>
    </div>
    <div class="concept-card">
      <span class="concept-label">Hands-on</span>
      <h4 class="concept-title">A minimal RAG sketch in Python</h4>
      <pre class="code-block"><span class="com"># pip install chromadb sentence-transformers</span>
<span class="kw">import</span> chromadb
<span class="kw">from</span> sentence_transformers <span class="kw">import</span> SentenceTransformer

embedder = SentenceTransformer(<span class="str">&quot;all-MiniLM-L6-v2&quot;</span>)
client = chromadb.Client()
collection = client.create_collection(<span class="str">&quot;helpdesk_docs&quot;</span>)

<span class="com"># Step 1-3: chunk, embed, and store some internal documentation</span>
docs = [
    <span class="str">&quot;To reset your VPN password, open the self-service portal and click Reset.&quot;</span>,
    <span class="str">&quot;The office Wi-Fi SSID is CorpNet-5G; guests should use CorpNet-Guest.&quot;</span>,
    <span class="str">&quot;Laptop refresh requests go through the asset management ticket queue.&quot;</span>,
]
collection.add(
    documents=docs,
    embeddings=embedder.encode(docs).tolist(),
    ids=[<span class="str">f&quot;doc-{i}&quot;</span> <span class="kw">for</span> i <span class="kw">in</span> <span class="fn">range</span>(<span class="fn">len</span>(docs))],
)

<span class="com"># Step 4: retrieve the most relevant chunk for a user's question</span>
question = <span class="str">&quot;How do I get on the wireless network as a visitor?&quot;</span>
results = collection.query(query_embeddings=embedder.encode([question]).tolist(), n_results=1)
<span class="fn">print</span>(<span class="str">&quot;Most relevant doc:&quot;</span>, results[<span class="str">&quot;documents&quot;</span>][0][0])

<span class="com"># Step 5: in a real system, you'd now hand that retrieved text + the
# question to an LLM with a prompt like:
#   &quot;Using only the context below, answer the user's question...&quot;</span></pre>
    </div>
    <div class="concept-card">
      <span class="concept-label">Common pitfall</span>
      <h4 class="concept-title">RAG doesn't eliminate hallucination — it reduces it</h4>
      <p class="concept-desc">A model can still misread or misapply the retrieved context, blend it with memorized facts,
      or confidently answer when retrieval returned nothing useful. <strong>Assume makes an ass out of you and me</strong>
      applies directly here: never assume a RAG answer is accurate just because it cites a source. Good systems show the
      retrieved chunks alongside the answer so a human can verify the model actually used them correctly — and instruct
      the model to say "I don't know" when retrieval comes back empty, rather than filling the gap with a guess.</p>
    </div>
  </div>
</div>
""" + "\n" + A_AI

S_THREAT = "<!-- BEGINNER39-THREAT v1 -->"
A_THREAT = "<!-- /domain-body threat -->"
C_THREAT = S_THREAT + """
<div class="topic">
  <div class="topic-header">
    <span class="topic-badge">Beginner</span>
    <h3>Indicators of Compromise (IOCs) – What to Look For</h3>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <span class="concept-label">Concept</span>
      <h4 class="concept-title">An IOC is a clue, not a verdict</h4>
      <p class="concept-desc">An Indicator of Compromise is a piece of forensic evidence that <em>suggests</em> a system
      may have been breached — a suspicious file hash, an unusual outbound connection, a registry key that shouldn't
      exist. The word "indicator" matters: a single IOC rarely proves an intrusion on its own. It's a thread to pull, and
      pulling it carefully — rather than jumping straight to "we've been hacked, shut everything down" — is what keeps
      a real incident from turning into a self-inflicted outage.</p>
    </div>
    <div class="concept-card">
      <span class="concept-label">Concept</span>
      <h4 class="concept-title">Common IOC categories, from easy to spoof to hard to spoof</h4>
      <table class="ai-table">
        <tr><th>Category</th><th>Example</th><th>Why it's useful / limited</th></tr>
        <tr><td>File hashes (MD5/SHA256)</td><td>A known-malware binary's exact fingerprint</td><td>Precise, but trivially defeated by changing one byte of the file</td></tr>
        <tr><td>IP addresses / domains</td><td>Command-and-control server addresses</td><td>Useful for blocking, but attackers rotate infrastructure constantly</td></tr>
        <tr><td>File paths / registry keys</td><td><code>C:\\Windows\\Temp\\svch0st.exe</code> (note the zero)</td><td>Reveals attacker tradecraft, but easy to rename next time</td></tr>
        <tr><td>Behavioral patterns</td><td>"Word spawning PowerShell spawning a reverse shell"</td><td>Hardest to fake — the attacker has to actually do something different to evade it</td></tr>
      </table>
      <p class="concept-desc">This is why mature security teams talk about moving "up the Pyramid of Pain" — from
      easily-changed atomic indicators (hashes, IPs) toward TTPs (tactics, techniques, and procedures) that describe
      <em>how</em> an attacker operates, which is far more expensive for them to change.</p>
    </div>
    <div class="concept-card">
      <span class="concept-label">Hands-on</span>
      <h4 class="concept-title">Checking a suspicious file or hash yourself</h4>
      <pre class="code-block"><span class="com"># Generate a hash for a file you want to check</span>
sha256sum suspicious_attachment.pdf

<span class="com"># Search running processes for anything spawned from an unusual path</span>
ps aux | grep -E &quot;/tmp/|/dev/shm/|AppData\\\\Local\\\\Temp&quot;

<span class="com"># List recently modified files in sensitive directories — a common
# sign of tampering or dropped tooling</span>
find /etc /usr/bin /usr/local/bin -mtime -2 -type f 2>/dev/null

<span class="com"># Check outbound connections for anything talking to unfamiliar hosts</span>
ss -tunap | grep ESTAB</pre>
      <p class="concept-desc">Before you act on a hash match from a public threat-intel feed, paste it into a malware
      analysis service or sandbox to see what others have already learned about it — community context turns a bare
      indicator into something you can actually act on with confidence.</p>
    </div>
    <div class="concept-card">
      <span class="concept-label">Mindset</span>
      <h4 class="concept-title">Not my circus, not my monkey — except when it is</h4>
      <p class="concept-desc">If you spot an IOC on a system outside your scope of responsibility, resist the urge to dig
      in yourself — that's how evidence gets contaminated and chains of custody get broken. Report it through the proper
      channel to the team that owns it. But on systems that <em>are</em> yours to protect, that same phrase becomes a
      trap: "probably nothing" is exactly the thought that lets small indicators grow into large incidents. Knowing which
      circus is yours is half the job.</p>
    </div>
  </div>
</div>
""" + "\n" + A_THREAT

S_PENTEST = "<!-- BEGINNER39-PENTEST v1 -->"
A_PENTEST = "<!-- /domain-body pentest -->"
C_PENTEST = S_PENTEST + """
<div class="topic">
  <div class="topic-header">
    <span class="topic-badge">Beginner</span>
    <h3>Password Attacks 101 – Cracking, Spraying, and Why MFA Matters</h3>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <span class="concept-label">Scope &amp; ethics first</span>
      <h4 class="concept-title">These techniques require written authorization</h4>
      <p class="concept-desc">Everything below is standard material in authorized penetration testing engagements,
      certifications (Security+, PenTest+, OSCP), and home lab practice against systems you own. Running these against
      accounts or systems you don't have explicit written permission to test is illegal in most jurisdictions — full stop.
      The value of learning this material is understanding <em>why</em> password policies, MFA, and account lockout
      settings exist, so you can defend against these techniques as well as recognize when they're being used against you.</p>
    </div>
    <div class="concept-card">
      <span class="concept-label">Concept</span>
      <h4 class="concept-title">Three different attacks that all "guess passwords" — but very differently</h4>
      <table class="ai-table">
        <tr><th>Attack</th><th>How it works</th><th>What makes it noisy or quiet</th></tr>
        <tr><td>Brute force</td><td>Try every possible character combination against one account</td><td>Extremely noisy and slow — usually only feasible offline against a stolen hash</td></tr>
        <tr><td>Dictionary / wordlist attack</td><td>Try a curated list of common/likely passwords against one account</td><td>Faster than brute force; still triggers lockouts if done online</td></tr>
        <tr><td>Password spraying</td><td>Try one or two common passwords (e.g. <code>Summer2026!</code>) across <em>many</em> accounts</td><td>Quiet — stays under per-account lockout thresholds, which is exactly why it's an attacker favorite</td></tr>
      </table>
      <p class="concept-desc">Password spraying is the one most likely to slip past basic defenses, because lockout
      policies are almost always designed around "five bad attempts on one account" — not "one bad attempt across
      five thousand accounts."</p>
    </div>
    <div class="concept-card">
      <span class="concept-label">Hands-on (lab only)</span>
      <h4 class="concept-title">Cracking a hash you already captured, offline</h4>
      <pre class="code-block"><span class="com"># Hashcat against a captured NTLM hash, using a wordlist + rule set
# (mode 1000 = NTLM; -a 0 = dictionary attack)</span>
hashcat -m 1000 -a 0 captured_hashes.txt rockyou.txt -r best64.rule

<span class="com"># John the Ripper, similar idea — auto-detects the hash format</span>
john --wordlist=rockyou.txt captured_hashes.txt
john --show captured_hashes.txt

<span class="com"># Generating a custom wordlist tailored to a target organization
# (combining names, years, seasons — the patterns real humans use)</span>
crunch 8 12 -t Company%%%%2026 -o custom_list.txt</pre>
      <p class="concept-desc">Notice these all happen <em>offline</em>, against a hash you already obtained through some
      other authorized step (a captured NTLM hash, a leaked database dump in a CTF, etc). Offline cracking generates zero
      log entries on the target — which is exactly why protecting hashes at rest matters as much as protecting the
      passwords themselves.</p>
    </div>
    <div class="concept-card">
      <span class="concept-label">Why this matters for defense</span>
      <h4 class="concept-title">MFA turns a successful guess into a near-miss</h4>
      <p class="concept-desc">Every attack above ends the same way without multi-factor authentication: a correct guess
      equals a compromised account. With MFA enabled, a correct password guess becomes merely a "huh, someone has my
      password" signal — assuming the user doesn't reflexively approve the resulting push notification. <strong>You can't
      make someone make the right choice, yet you can pick up the pieces afterwards</strong>: you can't force every user to
      scrutinize an MFA prompt before tapping "Approve," but you <em>can</em> configure number-matching MFA, conditional
      access policies, and anomaly alerts so that a careless tap doesn't automatically become a breach.</p>
    </div>
  </div>
</div>
""" + "\n" + A_PENTEST

S_MILITARY = "<!-- BEGINNER39-MILITARY v1 -->"
A_MILITARY = "<!-- /domain-body military -->"
C_MILITARY = S_MILITARY + """
<div class="topic">
  <div class="topic-header">
    <span class="topic-badge">Beginner</span>
    <h3>Translating Military Experience into IT Resume Language</h3>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <span class="concept-label">Why this matters</span>
      <h4 class="concept-title">The translation gap is real — and fixable</h4>
      <p class="concept-desc">A hiring manager reading "Maintained communications equipment for a forward-deployed unit
      under field conditions" may not immediately connect that to "can troubleshoot hardware, manage inventory, and keep
      systems running with no backup support nearby." The skills transfer; the <em>vocabulary</em> doesn't, automatically.
      Translating your experience into civilian IT language isn't dishonesty or exaggeration — it's making sure the
      reader understands what you actually did.</p>
    </div>
    <div class="concept-card">
      <span class="concept-label">Concept</span>
      <h4 class="concept-title">Side-by-side: military experience to IT resume language</h4>
      <table class="ai-table">
        <tr><th>What you did</th><th>How it translates</th></tr>
        <tr><td>Stood watch / monitored systems on shift rotations</td><td>"Performed continuous system monitoring and incident triage across rotating shift schedules — directly applicable to SOC/NOC environments"</td></tr>
        <tr><td>Maintained or repaired communications/radio/radar equipment</td><td>"Diagnosed and resolved hardware faults under time pressure with limited resources — comparable to field/desktop support and infrastructure troubleshooting"</td></tr>
        <tr><td>Managed property, parts inventory, or supply accountability</td><td>"Tracked and reconciled asset inventories using accountability systems — transferable to IT asset management (ITAM)"</td></tr>
        <tr><td>Trained junior personnel on procedures or equipment</td><td>"Developed and delivered technical training to incoming team members — translates to documentation and knowledge-transfer responsibilities"</td></tr>
        <tr><td>Operated under a clearance, handled sensitive information</td><td>"Held [clearance level]; managed sensitive information per strict handling protocols — directly relevant to compliance-driven environments (GRC, government contracting)"</td></tr>
        <tr><td>Followed and enforced strict procedures / checklists</td><td>"Executed and audited compliance with documented standard operating procedures — maps to change management, runbooks, and audit readiness"</td></tr>
      </table>
    </div>
    <div class="concept-card">
      <span class="concept-label">Concept</span>
      <h4 class="concept-title">Lead with impact, not just duties</h4>
      <p class="concept-desc">Civilian resumes reward quantified outcomes over lists of responsibilities. Compare:</p>
      <pre class="code-block"><span class="com"># Weak — describes a duty, says nothing about the outcome</span>
&quot;Responsible for maintaining unit IT equipment.&quot;

<span class="com"># Strong — same underlying experience, framed around impact</span>
&quot;Maintained 40+ workstations and network devices supporting a 120-person
unit with zero unplanned downtime over a 12-month deployment, reducing
average ticket resolution time by replacing ad-hoc fixes with a
documented troubleshooting checklist.&quot;</pre>
      <p class="concept-desc">If you don't have exact numbers, reasonable estimates are fine — "approximately," "more
      than," and "supported a team of roughly X" all read as honest and specific. What recruiters are scanning for is
      scale and outcome, not decimal-point precision.</p>
    </div>
    <div class="concept-card">
      <span class="concept-label">Mindset</span>
      <h4 class="concept-title">Not my circus, not my monkey — but also, it's now your circus</h4>
      <p class="concept-desc">Military culture often instills "stay in your lane, don't volunteer for extra work" as
      survival wisdom — and that instinct can undersell you in interviews. The civilian IT world rewards people who *did*
      step outside their narrow job description: the radio tech who also fixed everyone's laptop issues, the supply
      clerk who built a spreadsheet that automated half the unit's paperwork. Those moments where you picked up something
      that "wasn't your job" are often the most resume-worthy stories you have. Don't bury them out of habit.</p>
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
    (A_NET, S_NET, C_NET),
    (A_AI, S_AI, C_AI),
    (A_THREAT, S_THREAT, C_THREAT),
    (A_PENTEST, S_PENTEST, C_PENTEST),
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
