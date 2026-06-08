#!/usr/bin/env python3
"""
patch_beginner_concepts_v7.py — Wave 7: GRC foundations + Threat basics +
Ops tools + AI practical use + Scripting advanced patterns.

New sentinels:
  BEGINNER7-GRC v1     — Risk management basics, compliance frameworks, audits
  BEGINNER7-THREAT v1  — Attack lifecycle, indicators, MITRE ATT&CK intro
  BEGINNER7-OPS v1     — SIEM basics, log analysis, incident response phases
  BEGINNER7-AI v1      — Prompt engineering, AI tools for IT, using AI responsibly
  BEGINNER7-SCRIPT v1  — List comprehensions, generators, decorators, context managers
"""
from pathlib import Path

GRC_INJECT_ANCHOR    = "<!-- /domain-body grc -->"
THREAT_INJECT_ANCHOR = "<!-- /domain-body threat -->"
OPS_INJECT_ANCHOR    = "<!-- /domain-body ops -->"
AI_INJECT_ANCHOR     = "<!-- /domain-body ai -->"
SCRIPT_INJECT_ANCHOR = "<!-- /domain-body script -->"

# ─────────────────────────────── GRC wave 7 ──────────────────────────────────
GRC_SENTINEL = "<!-- BEGINNER7-GRC v1 -->"
GRC_CONTENT = """
<!-- BEGINNER7-GRC v1 -->
<!-- ── TOPIC: RISK MANAGEMENT 101 ───────────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">⚖️</span>
    <span class="topic-name">Risk Management 101 — Threat, Vulnerability, Impact</span>
    <span class="topic-badge">GRC • Start Here</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">THREE CORE TERMS</div>
      <div class="concept-title">Threat · Vulnerability · Risk</div>
      <div class="concept-desc"><strong>Threat</strong> — something that COULD cause harm (fire, hacker, disgruntled employee). Threats are mostly out of your control.<br>
      <strong>Vulnerability</strong> — a weakness that a threat can exploit (unpatched software, unlocked door, weak password). These are in your control.<br>
      <strong>Risk</strong> — the likelihood × impact of a threat exploiting a vulnerability. Risk = Threat × Vulnerability × Impact.</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">RISK RESPONSES</div>
      <div class="concept-title">Accept · Avoid · Transfer · Mitigate</div>
      <div class="concept-desc"><strong>Avoid</strong> — stop doing the risky thing entirely (don't store data you don't need).<br>
      <strong>Mitigate</strong> — reduce likelihood or impact (patch the vulnerability, add MFA).<br>
      <strong>Transfer</strong> — shift the financial impact to someone else (buy cyber insurance, outsource to an MSSP).<br>
      <strong>Accept</strong> — acknowledge the risk but do nothing (when cost of mitigation &gt; expected loss). Always document accepted risks.</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">QUALITATIVE vs QUANTITATIVE</div>
      <div class="concept-title">High/Medium/Low vs Actual Dollars</div>
      <div class="concept-desc"><strong>Qualitative</strong> — ranks risks as High/Medium/Low using judgment. Fast, good for prioritization, but subjective.<br>
      <strong>Quantitative</strong> — assigns dollar values. Uses:<br>
      <strong>AV</strong> (Asset Value) — what the asset is worth<br>
      <strong>EF</strong> (Exposure Factor) — % of asset lost if threat occurs<br>
      <strong>SLE</strong> = AV × EF — Single Loss Expectancy<br>
      <strong>ARO</strong> (Annual Rate of Occurrence) — how often per year<br>
      <strong>ALE</strong> = SLE × ARO — Annual Loss Expectancy</div>
    </div>
    <table class="ai-table">
      <thead><tr><th>Acronym</th><th>Meaning</th><th>Example ($1M server, fire burns 30%, happens 0.1/yr)</th></tr></thead>
      <tbody>
        <tr><td>AV</td><td>Asset Value</td><td>$1,000,000</td></tr>
        <tr><td>EF</td><td>Exposure Factor</td><td>30% = 0.30</td></tr>
        <tr><td>SLE</td><td>Single Loss Expectancy (AV × EF)</td><td>$300,000</td></tr>
        <tr><td>ARO</td><td>Annual Rate of Occurrence</td><td>0.1 (once per 10 years)</td></tr>
        <tr><td>ALE</td><td>Annual Loss Expectancy (SLE × ARO)</td><td>$30,000</td></tr>
      </tbody>
    </table>
    <div class="concept-card">
      <div class="concept-label">RESIDUAL RISK</div>
      <div class="concept-title">What's Left After Controls</div>
      <div class="concept-desc">No control eliminates 100% of risk. After applying safeguards, you have <strong>residual risk</strong> — what you accept as the remaining exposure. Risk appetite is how much residual risk an organization is willing to tolerate. Risk tolerance is the acceptable variance around that.</div>
    </div>
  </div>
</div>

<!-- ── TOPIC: COMPLIANCE FRAMEWORKS ──────────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">📋</span>
    <span class="topic-name">Compliance Frameworks — Playing by the Rules</span>
    <span class="topic-badge">GRC • Foundation</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">WHY FRAMEWORKS EXIST</div>
      <div class="concept-title">Baselines, Audits, and Legal Requirements</div>
      <div class="concept-desc">Companies face legal, contractual, or industry requirements to prove they handle data and systems securely. Frameworks provide a <strong>common language</strong> and a <strong>checklist</strong> so everyone knows what "secure enough" means. Being compliant ≠ being secure, but it's a starting floor.</div>
    </div>
    <table class="ai-table">
      <thead><tr><th>Framework</th><th>Who It's For</th><th>Focus</th></tr></thead>
      <tbody>
        <tr><td>NIST CSF</td><td>Any org, especially US federal</td><td>Identify, Protect, Detect, Respond, Recover</td></tr>
        <tr><td>ISO 27001</td><td>Any org worldwide</td><td>Information Security Management System (ISMS)</td></tr>
        <tr><td>PCI-DSS</td><td>Anyone taking credit cards</td><td>Cardholder data security; 12 requirements</td></tr>
        <tr><td>HIPAA</td><td>US healthcare providers</td><td>Protected Health Information (PHI) privacy</td></tr>
        <tr><td>SOC 2</td><td>SaaS / cloud service providers</td><td>Trust Service Criteria: Security, Availability, etc.</td></tr>
        <tr><td>GDPR</td><td>Any org with EU user data</td><td>Data privacy, user rights, breach notification</td></tr>
        <tr><td>CMMC</td><td>US defense contractors</td><td>Cybersecurity Maturity Model; tiered levels</td></tr>
        <tr><td>CIS Controls</td><td>Any org</td><td>18 prioritized security actions</td></tr>
      </tbody>
    </table>
    <div class="concept-card">
      <div class="concept-label">AUDIT TYPES</div>
      <div class="concept-title">Internal, External, Third-Party</div>
      <div class="concept-desc"><strong>Internal audit</strong> — done by your own staff or internal audit team. Finds issues before outsiders do. Not independent, but faster and cheaper.<br>
      <strong>External audit</strong> — done by a third-party firm. Required for SOC 2, ISO 27001 certification, PCI-DSS. Independent opinion carries more weight.<br>
      <strong>Penetration test</strong> — adversarial: ethical hackers try to break in. Reveals what a real attacker would find. Required by PCI-DSS annually.</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">POLICY HIERARCHY</div>
      <div class="concept-title">Policy → Standard → Procedure → Guideline</div>
      <div class="concept-desc"><strong>Policy</strong> — high-level statement of intent. "All data must be encrypted at rest." Non-negotiable.<br>
      <strong>Standard</strong> — specific requirements to meet the policy. "Use AES-256."<br>
      <strong>Procedure</strong> — step-by-step how to implement. "Run this script, configure this setting."<br>
      <strong>Guideline</strong> — recommended but not mandatory best practices. "Consider using a VPN on public Wi-Fi."</div>
    </div>
  </div>
</div>
"""

# ─────────────────────────────── THREAT wave 7 ───────────────────────────────
THREAT_SENTINEL = "<!-- BEGINNER7-THREAT v1 -->"
THREAT_CONTENT = """
<!-- BEGINNER7-THREAT v1 -->
<!-- ── TOPIC: HOW ATTACKS ACTUALLY WORK ──────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">🎯</span>
    <span class="topic-name">How Attacks Actually Work — The Attacker's Mindset</span>
    <span class="topic-badge">THREAT • Start Here</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">THE CYBER KILL CHAIN</div>
      <div class="concept-title">Lockheed Martin's 7-Phase Attack Model</div>
      <div class="concept-desc">Attacks almost never happen in a single step. They follow a pattern — and defenders can stop the attack at any phase.</div>
      <table class="ai-table">
        <thead><tr><th>#</th><th>Phase</th><th>What the Attacker Does</th><th>Defender's Job</th></tr></thead>
        <tbody>
          <tr><td>1</td><td>Reconnaissance</td><td>Research target: LinkedIn, DNS, Shodan scans</td><td>Minimize public attack surface</td></tr>
          <tr><td>2</td><td>Weaponization</td><td>Build exploit + payload (malware, phishing doc)</td><td>Threat intelligence</td></tr>
          <tr><td>3</td><td>Delivery</td><td>Send the payload (email, USB, watering hole)</td><td>Email filtering, web proxy</td></tr>
          <tr><td>4</td><td>Exploitation</td><td>Trigger the vulnerability, execute code</td><td>Patching, endpoint protection</td></tr>
          <tr><td>5</td><td>Installation</td><td>Install backdoor / malware for persistence</td><td>Application whitelisting, EDR</td></tr>
          <tr><td>6</td><td>C2 (Command &amp; Control)</td><td>Phone home; receive instructions from attacker</td><td>Network monitoring, DNS filtering</td></tr>
          <tr><td>7</td><td>Actions on Objectives</td><td>Steal data, encrypt for ransom, pivot laterally</td><td>DLP, data segmentation, SIEM alerts</td></tr>
        </tbody>
      </table>
    </div>
    <div class="concept-card">
      <div class="concept-label">MITRE ATT&CK</div>
      <div class="concept-title">A Library of Real Attacker Techniques</div>
      <div class="concept-desc">MITRE ATT&amp;CK is a free, publicly maintained matrix of <strong>Tactics</strong> (why), <strong>Techniques</strong> (how), and <strong>Sub-techniques</strong> (specific implementation) that real adversaries actually use. It's based on observed incidents, not theory.<br>
      <strong>Tactics</strong>: Initial Access → Execution → Persistence → Privilege Escalation → Defense Evasion → Credential Access → Discovery → Lateral Movement → Collection → Exfiltration → Impact<br>
      Use it to: map what an attacker could do, identify detection gaps, communicate about threats in a standard language.</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">INDICATORS</div>
      <div class="concept-title">IOC vs IOA vs TTP</div>
      <div class="concept-desc"><strong>IOC (Indicator of Compromise)</strong> — forensic evidence that an attack occurred: malicious IP, hash of known malware, C2 domain. Reactive — tells you it already happened.<br>
      <strong>IOA (Indicator of Attack)</strong> — behavior suggesting an attack is in progress: port scan, privilege escalation, unusual process. Proactive — catch it as it happens.<br>
      <strong>TTP (Tactics, Techniques, Procedures)</strong> — the attacker's playbook. Hardest to change. Even if they change their malware hash, TTPs stay constant. Best for long-term defense.</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">COMMON MALWARE TYPES</div>
      <div class="concept-title">Virus · Worm · Trojan · Ransomware · Rootkit · Spyware</div>
      <div class="concept-desc"><strong>Virus</strong> — attaches to legitimate files; needs user action to spread.<br>
      <strong>Worm</strong> — self-replicating; spreads over networks without human action (WannaCry, Slammer).<br>
      <strong>Trojan</strong> — looks legitimate; hides malicious payload (fake crack, infected installer).<br>
      <strong>Ransomware</strong> — encrypts your files; demands payment for the key.<br>
      <strong>Rootkit</strong> — hides malware from the OS itself; persistence at the kernel level.<br>
      <strong>Spyware/Keylogger</strong> — silently records keystrokes, screenshots, credentials.<br>
      <strong>Botnet agent</strong> — your machine becomes a "zombie" that attackers remotely control.</div>
    </div>
  </div>
</div>

<!-- ── TOPIC: SOCIAL ENGINEERING DEEP DIVE ───────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">🎭</span>
    <span class="topic-name">Social Engineering — People Are the Attack Surface</span>
    <span class="topic-badge">THREAT • Practical</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">SIX INFLUENCE PRINCIPLES</div>
      <div class="concept-title">Cialdini's Weapons Attackers Exploit</div>
      <div class="concept-desc"><strong>Reciprocity</strong> — do something for someone, they feel obligated to return the favor.<br>
      <strong>Commitment &amp; Consistency</strong> — once someone agrees to a small ask, they're likely to agree to bigger asks.<br>
      <strong>Social Proof</strong> — "Everyone on your team already approved this."<br>
      <strong>Authority</strong> — "This is the CTO" / "Microsoft support calling."<br>
      <strong>Liking</strong> — you comply more with people you like or who seem like you.<br>
      <strong>Scarcity/Urgency</strong> — "This needs to happen in the next 30 minutes or the system goes down."</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">PRETEXTING</div>
      <div class="concept-title">Creating a False Identity or Scenario</div>
      <div class="concept-desc">The attacker creates a believable story — "I'm from IT, we're doing an audit," or "I'm a new vendor, I need temporary access." They do research first (LinkedIn, OSINT) to make it convincing. The pretext gives the victim a reason to comply that doesn't trigger suspicion.</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">DEFENSE</div>
      <div class="concept-title">Out-of-Band Verification Is the Key</div>
      <div class="concept-desc">When someone asks for access, credentials, or data:<br>
      1. <strong>Slow down</strong> — urgency is a manipulation tool. Real emergencies have procedures.<br>
      2. <strong>Verify independently</strong> — don't call the number they gave you; look it up yourself.<br>
      3. <strong>Follow the process</strong> — the process exists exactly for these moments.<br>
      4. <strong>It's okay to say no</strong> — "Let me verify this request through proper channels first." A real insider won't mind.</div>
    </div>
  </div>
</div>
"""

# ─────────────────────────────── OPS wave 7 ──────────────────────────────────
OPS_SENTINEL = "<!-- BEGINNER7-OPS v1 -->"
OPS_CONTENT = """
<!-- BEGINNER7-OPS v1 -->
<!-- ── TOPIC: SIEM & LOG ANALYSIS ─────────────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">📊</span>
    <span class="topic-name">SIEM &amp; Log Analysis — Finding Signals in the Noise</span>
    <span class="topic-badge">OPS • Foundation</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">WHAT IS A SIEM</div>
      <div class="concept-title">Security Information and Event Management</div>
      <div class="concept-desc">A SIEM collects log data from across your environment — firewalls, servers, endpoints, cloud, applications — into one place. It correlates events across sources to spot attacks that would be invisible in any single log. Common SIEMs: Splunk, Microsoft Sentinel, IBM QRadar, Elastic/SIEM, LogRhythm.</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">LOG SOURCES</div>
      <div class="concept-title">What Feeds the SIEM</div>
      <table class="ai-table">
        <thead><tr><th>Source</th><th>What It Tells You</th></tr></thead>
        <tbody>
          <tr><td>Windows Event Logs</td><td>Logins (4624/4625), privilege use, process creation (4688)</td></tr>
          <tr><td>Syslog (Linux)</td><td>Auth events, sudo usage, service starts/stops</td></tr>
          <tr><td>Firewall/IDS</td><td>Blocked connections, port scans, policy violations</td></tr>
          <tr><td>DNS logs</td><td>Domains queried — DGA domains, C2 beaconing</td></tr>
          <tr><td>Web proxy/WAF</td><td>HTTP requests, blocked URLs, content filtering</td></tr>
          <tr><td>EDR (Endpoint)</td><td>Process execution, file changes, lateral movement</td></tr>
          <tr><td>Cloud logs (CloudTrail)</td><td>API calls, resource changes, IAM activity</td></tr>
          <tr><td>Email gateway</td><td>Spam, phishing, attachment analysis</td></tr>
        </tbody>
      </table>
    </div>
    <div class="concept-card">
      <div class="concept-label">READING LOGS</div>
      <div class="concept-title">Common Linux Log Analysis Commands</div>
      <div class="code-block"><span class="com"># View authentication log in real time</span>
tail -f /var/log/auth.log

<span class="com"># Find failed SSH login attempts</span>
grep <span class="str">"Failed password"</span> /var/log/auth.log | tail -50

<span class="com"># Count failed logins per IP (top offenders)</span>
grep <span class="str">"Failed password"</span> /var/log/auth.log \
  | awk <span class="str">'{print $11}'</span> \
  | sort | uniq -c | sort -rn | head -20

<span class="com"># Find successful logins after multiple failures (credential stuffing sign)</span>
grep <span class="str">"Accepted password"</span> /var/log/auth.log

<span class="com"># Search system logs for errors</span>
journalctl -p err -n 100

<span class="com"># Check who's logged in right now</span>
who
w
last | head -20</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">FALSE POSITIVES</div>
      <div class="concept-title">Alert Fatigue Is a Real Threat</div>
      <div class="concept-desc">When a SIEM generates 10,000 alerts per day, analysts tune out. Alert fatigue causes real attacks to be dismissed as noise. Good SOC work involves constantly tuning detection rules — raising thresholds for noisy rules, adding context (business hours, user role, geography), and building baselines for normal behavior.</div>
    </div>
  </div>
</div>

<!-- ── TOPIC: INCIDENT RESPONSE PHASES ───────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">🚨</span>
    <span class="topic-name">Incident Response — What to Do When It Goes Wrong</span>
    <span class="topic-badge">OPS • Critical</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">NIST IR PHASES</div>
      <div class="concept-title">Preparation → Detection → Containment → Eradication → Recovery → Lessons Learned</div>
      <div class="concept-desc">The NIST SP 800-61 Incident Response lifecycle is the industry standard. Each phase has specific goals and outputs.</div>
      <table class="ai-table">
        <thead><tr><th>Phase</th><th>Goal</th><th>Key Actions</th></tr></thead>
        <tbody>
          <tr><td>Preparation</td><td>Be ready before incidents happen</td><td>IR plan, playbooks, tools, training, tabletops</td></tr>
          <tr><td>Detection &amp; Analysis</td><td>Know something happened</td><td>SIEM alerts, IOC analysis, triage, severity scoring</td></tr>
          <tr><td>Containment</td><td>Stop the bleeding</td><td>Isolate systems, block IPs/hashes, preserve evidence</td></tr>
          <tr><td>Eradication</td><td>Remove the threat</td><td>Delete malware, patch vulnerability, reset credentials</td></tr>
          <tr><td>Recovery</td><td>Get back to normal</td><td>Restore from clean backup, monitor for re-infection</td></tr>
          <tr><td>Post-Incident</td><td>Learn and improve</td><td>Root cause analysis, update playbooks, retrain staff</td></tr>
        </tbody>
      </table>
    </div>
    <div class="concept-card">
      <div class="concept-label">CONTAINMENT STRATEGIES</div>
      <div class="concept-title">Short-Term vs Long-Term</div>
      <div class="concept-desc"><strong>Short-term</strong>: immediate isolation — unplug network cable, disable account, null-route IP. Buy time without losing evidence.<br>
      <strong>Long-term</strong>: rebuild system from a known-good image, re-image endpoints, force password resets, revoke compromised certificates.<br>
      Key decision: <em>preserve evidence vs stop the bleeding</em>. If active data exfiltration is happening, containment wins. If already contained, preserve first.</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">CHAIN OF CUSTODY</div>
      <div class="concept-title">Evidence Must Be Unimpeachable</div>
      <div class="concept-desc">If the incident leads to legal action or law enforcement, digital evidence must be collected and handled correctly. Document: who collected it, when, what state it was in, and how it was stored. Use write blockers for disk imaging. Hash every piece of evidence (MD5 + SHA-256) and verify hashes later. Mishandled evidence gets thrown out.</div>
    </div>
  </div>
</div>
"""

# ─────────────────────────────── AI wave 7 ───────────────────────────────────
AI_SENTINEL = "<!-- BEGINNER7-AI v1 -->"
AI_CONTENT = """
<!-- BEGINNER7-AI v1 -->
<!-- ── TOPIC: PROMPT ENGINEERING ─────────────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">💬</span>
    <span class="topic-name">Prompt Engineering — Getting Better Answers from AI</span>
    <span class="topic-badge">AI • Practical</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">WHAT IS PROMPT ENGINEERING</div>
      <div class="concept-title">Communicating Clearly With AI</div>
      <div class="concept-desc">Prompt engineering is the skill of crafting inputs to AI systems to get the most useful outputs. It's part science (what techniques work) and part communication (being clear about what you actually want). The better you describe your problem, context, and desired output, the better the result.</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">ANATOMY OF A GOOD PROMPT</div>
      <div class="concept-title">Role + Context + Task + Format + Constraints</div>
      <div class="concept-desc"><strong>Role</strong>: "Act as a senior Linux sysadmin…"<br>
      <strong>Context</strong>: "…working in a small startup with Ubuntu 22.04 servers…"<br>
      <strong>Task</strong>: "…write a bash script that checks disk usage on all mounts…"<br>
      <strong>Format</strong>: "…output a commented script followed by a usage example…"<br>
      <strong>Constraints</strong>: "…avoid dependencies beyond standard tools, no sudo required."</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">TECHNIQUES</div>
      <div class="concept-title">Zero-Shot, Few-Shot, Chain-of-Thought</div>
      <div class="concept-desc"><strong>Zero-shot</strong> — just ask the question directly. Good for simple tasks.<br>
      <strong>Few-shot</strong> — provide 2-3 examples of the input-output pattern you want, then give your actual input. Dramatically improves consistency.<br>
      <strong>Chain-of-thought</strong> — ask the model to "think step by step" or show its reasoning. Dramatically improves accuracy on math, logic, and multi-step problems.<br>
      <strong>Self-critique</strong> — ask it to review its own output and identify flaws, then improve.</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">CONTEXT WINDOW</div>
      <div class="concept-title">The Model's Working Memory</div>
      <div class="concept-desc">Every AI conversation has a <strong>context window</strong> — the maximum amount of text the model can consider at once (prompt + conversation + output). Older models: ~4K tokens. Modern: 128K-1M+ tokens. When context fills up, the model loses earlier parts of the conversation. For long tasks, periodically summarize earlier context.</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">AI LIMITATIONS</div>
      <div class="concept-title">Hallucinations, Stale Knowledge, Confidence Without Accuracy</div>
      <div class="concept-desc"><strong>Hallucinations</strong> — AI confidently states false information. Always verify facts, especially URLs, statistics, legal claims, and medical information.<br>
      <strong>Training cutoff</strong> — the model doesn't know about events after its training data ends. For current events, use a model with web search or check yourself.<br>
      <strong>Sycophancy</strong> — models tend to agree with users to avoid conflict. Push back with "Are you sure?" or "What are the counterarguments?"<br>
      <strong>No reasoning</strong> — LLMs predict tokens, they don't "think." They can be spectacularly wrong on logic puzzles while sounding confident.</div>
    </div>
  </div>
</div>

<!-- ── TOPIC: AI TOOLS FOR IT PROFESSIONALS ───────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">🛠️</span>
    <span class="topic-name">AI Tools for IT Work — Practical Everyday Use</span>
    <span class="topic-badge">AI • Practical</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">CODING ASSISTANT</div>
      <div class="concept-title">Writing, Explaining, and Debugging Code</div>
      <div class="concept-desc">AI coding assistants (GitHub Copilot, Claude, ChatGPT) accelerate development significantly for:<br>
      • Generating boilerplate (database models, API endpoints, config files)<br>
      • Explaining unfamiliar code line by line<br>
      • Debugging — paste your error + code, ask "what's wrong?"<br>
      • Converting between languages (Python → Bash → PowerShell)<br>
      • Writing unit tests<br>
      • Regex pattern generation<br>
      <strong>Key habit</strong>: read and understand every line before using it. AI-generated code can have security vulnerabilities.</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">SECURITY USE CASES</div>
      <div class="concept-title">AI in the SOC</div>
      <div class="concept-desc">• <strong>Log analysis</strong>: paste a suspicious log entry, ask "what does this indicate?"<br>
      • <strong>Malware triage</strong>: describe behavior, ask for analysis (never upload actual malware to public AI)<br>
      • <strong>Report writing</strong>: incident reports, executive summaries, risk assessments<br>
      • <strong>Query generation</strong>: "write a Splunk query to find PowerShell encoded command execution"<br>
      • <strong>CTF assistance</strong>: explain encoding/encryption, suggest approaches to challenges<br>
      • <strong>Phishing analysis</strong>: paste email headers, ask for red flags</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">RESPONSIBLE USE</div>
      <div class="concept-title">What Not to Send to AI</div>
      <div class="concept-desc">• Never paste customer PII, health records, or financial data into public AI tools<br>
      • Never paste your organization's confidential/proprietary code<br>
      • Never share network diagrams, internal IP ranges, or security architecture with public models<br>
      • Check your company's AI policy before using any AI tool for work tasks<br>
      Enterprise versions of tools (Azure OpenAI, Claude for Enterprise) don't train on your data — use those for work.</div>
    </div>
  </div>
</div>
"""

# ─────────────────────────────── SCRIPTING wave 7 ────────────────────────────
SCRIPT_SENTINEL = "<!-- BEGINNER7-SCRIPT v1 -->"
SCRIPT_CONTENT = """
<!-- BEGINNER7-SCRIPT v1 -->
<!-- ── TOPIC: LIST COMPREHENSIONS & GENERATORS ──────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">⚡</span>
    <span class="topic-name">List Comprehensions &amp; Generators — Pythonic Power</span>
    <span class="topic-badge">SCRIPT • Intermediate</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">LIST COMPREHENSION</div>
      <div class="concept-title">Build a List in One Readable Line</div>
      <div class="concept-desc">A list comprehension is a concise way to create a list by applying an expression to each item in an iterable, with an optional filter. It replaces 4-6 lines of loop code with 1.</div>
      <div class="code-block"><span class="com"># Old way</span>
squares = []
<span class="kw">for</span> x <span class="kw">in</span> <span class="fn">range</span>(<span class="num">10</span>):
    squares.append(x ** <span class="num">2</span>)

<span class="com"># List comprehension — same result</span>
squares = [x ** <span class="num">2</span> <span class="kw">for</span> x <span class="kw">in</span> <span class="fn">range</span>(<span class="num">10</span>)]

<span class="com"># With filter (only even squares)</span>
even_sq = [x ** <span class="num">2</span> <span class="kw">for</span> x <span class="kw">in</span> <span class="fn">range</span>(<span class="num">10</span>) <span class="kw">if</span> x % <span class="num">2</span> == <span class="num">0</span>]

<span class="com"># With transformation</span>
names = [<span class="str">"alice"</span>, <span class="str">"bob"</span>, <span class="str">"carol"</span>]
upper = [n.upper() <span class="kw">for</span> n <span class="kw">in</span> names]  <span class="com"># ['ALICE', 'BOB', 'CAROL']</span>

<span class="com"># Flatten a 2D list</span>
matrix = [[<span class="num">1</span>,<span class="num">2</span>],[<span class="num">3</span>,<span class="num">4</span>],[<span class="num">5</span>,<span class="num">6</span>]]
flat = [x <span class="kw">for</span> row <span class="kw">in</span> matrix <span class="kw">for</span> x <span class="kw">in</span> row]  <span class="com"># [1,2,3,4,5,6]</span></div>
    </div>
    <div class="concept-card">
      <div class="concept-label">DICT & SET COMPREHENSIONS</div>
      <div class="concept-title">Same Idea, Different Brackets</div>
      <div class="code-block"><span class="com"># Dict comprehension: name → length</span>
names = [<span class="str">"Alice"</span>, <span class="str">"Bob"</span>, <span class="str">"Carol"</span>]
lengths = {n: <span class="fn">len</span>(n) <span class="kw">for</span> n <span class="kw">in</span> names}
<span class="com"># {'Alice': 5, 'Bob': 3, 'Carol': 5}</span>

<span class="com"># Set comprehension: unique first letters</span>
firsts = {n[<span class="num">0</span>].lower() <span class="kw">for</span> n <span class="kw">in</span> names}
<span class="com"># {'a', 'b', 'c'}</span>

<span class="com"># Invert a dict</span>
original = {<span class="str">"a"</span>: <span class="num">1</span>, <span class="str">"b"</span>: <span class="num">2</span>, <span class="str">"c"</span>: <span class="num">3</span>}
inverted = {v: k <span class="kw">for</span> k, v <span class="kw">in</span> original.items()}
<span class="com"># {1: 'a', 2: 'b', 3: 'c'}</span></div>
    </div>
    <div class="concept-card">
      <div class="concept-label">GENERATORS</div>
      <div class="concept-title">Lazy Evaluation — Process One at a Time</div>
      <div class="concept-desc">A list comprehension builds the entire list in memory at once. A generator expression (<code>()</code> instead of <code>[]</code>) produces values <strong>one at a time on demand</strong>. Essential for large datasets (files with millions of lines, streaming data).</div>
      <div class="code-block"><span class="com"># List: builds 1M items in memory immediately</span>
big_list = [x**<span class="num">2</span> <span class="kw">for</span> x <span class="kw">in</span> <span class="fn">range</span>(<span class="num">1_000_000</span>)]

<span class="com"># Generator: computes each item only when asked</span>
big_gen = (x**<span class="num">2</span> <span class="kw">for</span> x <span class="kw">in</span> <span class="fn">range</span>(<span class="num">1_000_000</span>))
<span class="fn">next</span>(big_gen)  <span class="com"># 0 (computes only this one)</span>
<span class="fn">next</span>(big_gen)  <span class="com"># 1</span>

<span class="com"># Generator function with yield</span>
<span class="kw">def</span> <span class="fn">read_big_file</span>(path):
    <span class="kw">with</span> <span class="fn">open</span>(path) <span class="kw">as</span> f:
        <span class="kw">for</span> line <span class="kw">in</span> f:
            <span class="kw">yield</span> line.strip()  <span class="com"># one line at a time</span>

<span class="kw">for</span> line <span class="kw">in</span> <span class="fn">read_big_file</span>(<span class="str">"huge.log"</span>):
    <span class="kw">if</span> <span class="str">"ERROR"</span> <span class="kw">in</span> line:
        <span class="fn">print</span>(line)   <span class="com"># never loads whole file</span></div>
    </div>
  </div>
</div>

<!-- ── TOPIC: CONTEXT MANAGERS & DECORATORS ───────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">🎀</span>
    <span class="topic-name">Context Managers &amp; Decorators — Elegant Python Patterns</span>
    <span class="topic-badge">SCRIPT • Intermediate</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">CONTEXT MANAGERS</div>
      <div class="concept-title">with — Guaranteed Cleanup</div>
      <div class="concept-desc">The <code>with</code> statement ensures cleanup code runs even if an error occurs. It calls <code>__enter__</code> on open and <code>__exit__</code> on close (or exception).</div>
      <div class="code-block"><span class="com"># Without context manager (bad)</span>
f = <span class="fn">open</span>(<span class="str">"data.txt"</span>)
data = f.read()
f.close()   <span class="com"># won't run if read() throws</span>

<span class="com"># With context manager (correct)</span>
<span class="kw">with</span> <span class="fn">open</span>(<span class="str">"data.txt"</span>) <span class="kw">as</span> f:
    data = f.read()
<span class="com"># file is ALWAYS closed here, even on exception</span>

<span class="com"># Multiple resources</span>
<span class="kw">with</span> <span class="fn">open</span>(<span class="str">"in.txt"</span>) <span class="kw">as</span> src, <span class="fn">open</span>(<span class="str">"out.txt"</span>, <span class="str">"w"</span>) <span class="kw">as</span> dst:
    dst.write(src.read())

<span class="com"># Database connection pattern</span>
<span class="kw">with</span> db.connect() <span class="kw">as</span> conn:
    conn.execute(<span class="str">"INSERT INTO logs ..."</span>)
<span class="com"># connection closed + transaction committed/rolled back</span></div>
    </div>
    <div class="concept-card">
      <div class="concept-label">DECORATORS</div>
      <div class="concept-title">Functions That Wrap Functions</div>
      <div class="concept-desc">A decorator is a function that takes a function as input and returns a modified version. Used for: logging, timing, authentication checks, caching, retry logic — any cross-cutting concern you don't want to copy-paste.</div>
      <div class="code-block"><span class="kw">import</span> time
<span class="kw">from</span> functools <span class="kw">import</span> wraps

<span class="com"># Simple timer decorator</span>
<span class="kw">def</span> <span class="fn">timer</span>(func):
    @wraps(func)   <span class="com"># preserves original function metadata</span>
    <span class="kw">def</span> <span class="fn">wrapper</span>(*args, **kwargs):
        start = time.perf_counter()
        result = <span class="fn">func</span>(*args, **kwargs)
        elapsed = time.perf_counter() - start
        <span class="fn">print</span>(<span class="str">f"{func.__name__} took {elapsed:.3f}s"</span>)
        <span class="kw">return</span> result
    <span class="kw">return</span> wrapper

<span class="com"># Apply with @ syntax</span>
@timer
<span class="kw">def</span> <span class="fn">slow_operation</span>():
    time.sleep(<span class="num">1</span>)
    <span class="kw">return</span> <span class="str">"done"</span>

<span class="fn">slow_operation</span>()   <span class="com"># prints: slow_operation took 1.002s</span></div>
    </div>
    <div class="concept-card">
      <div class="concept-label">FUNCTOOLS CACHE</div>
      <div class="concept-title">Memoization in One Line</div>
      <div class="code-block"><span class="kw">from</span> functools <span class="kw">import</span> cache, lru_cache

<span class="com"># Cache all results forever</span>
@cache
<span class="kw">def</span> <span class="fn">fibonacci</span>(n):
    <span class="kw">if</span> n &lt; <span class="num">2</span>:
        <span class="kw">return</span> n
    <span class="kw">return</span> <span class="fn">fibonacci</span>(n-<span class="num">1</span>) + <span class="fn">fibonacci</span>(n-<span class="num">2</span>)

<span class="fn">fibonacci</span>(<span class="num">100</span>)  <span class="com"># instant — cache prevents redundant calls</span>

<span class="com"># LRU cache: keeps only the N most recent results</span>
@lru_cache(maxsize=<span class="num">128</span>)
<span class="kw">def</span> <span class="fn">expensive_lookup</span>(key):
    <span class="kw">return</span> database.fetch(key)</div>
    </div>
  </div>
</div>

<!-- ── TOPIC: COMMAND-LINE TOOLS IN PYTHON ────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">🖥️</span>
    <span class="topic-name">Building CLI Tools in Python — argparse &amp; click</span>
    <span class="topic-badge">SCRIPT • Practical</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">WHY CLI TOOLS</div>
      <div class="concept-title">Scripts You Can Run Anywhere</div>
      <div class="concept-desc">Good CLI tools can be used in shell scripts, cron jobs, CI pipelines, and by other team members who aren't Python developers. Proper argument parsing replaces manual <code>sys.argv</code> hacks with named arguments, help text, type validation, and sub-commands.</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">ARGPARSE</div>
      <div class="concept-title">stdlib CLI Argument Parsing</div>
      <div class="code-block"><span class="kw">import</span> argparse

parser = argparse.ArgumentParser(
    description=<span class="str">"Scan a log file for errors"</span>
)
parser.add_argument(<span class="str">"logfile"</span>, help=<span class="str">"Path to log file"</span>)
parser.add_argument(<span class="str">"-n"</span>, <span class="str">"--count"</span>, type=<span class="fn">int</span>, default=<span class="num">10</span>,
                    help=<span class="str">"Number of errors to show (default: 10)"</span>)
parser.add_argument(<span class="str">"-v"</span>, <span class="str">"--verbose"</span>, action=<span class="str">"store_true"</span>,
                    help=<span class="str">"Show full line context"</span>)

args = parser.parse_args()

<span class="fn">print</span>(<span class="str">f"Scanning {args.logfile} for top {args.count} errors"</span>)
<span class="kw">if</span> args.verbose:
    <span class="fn">print</span>(<span class="str">"Verbose mode on"</span>)</div>
      <div class="concept-desc">Usage: <code>python3 scan.py app.log -n 20 -v</code><br>Help: <code>python3 scan.py --help</code> (auto-generated!)</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">MAIN GUARD</div>
      <div class="concept-title">if __name__ == "__main__"</div>
      <div class="concept-desc">This pattern lets your file work as both a runnable script AND an importable module. When run directly, <code>__name__</code> is <code>"__main__"</code>. When imported, it's the module name. The <code>main()</code> function will NOT run on import — useful for testing.</div>
      <div class="code-block"><span class="kw">def</span> <span class="fn">main</span>():
    args = parser.parse_args()
    <span class="com"># ... do the work ...</span>

<span class="kw">if</span> __name__ == <span class="str">"__main__"</span>:
    <span class="fn">main</span>()</div>
    </div>
  </div>
</div>
"""


def patch(filepath: str, sentinel: str, inject_content: str, inject_anchor: str):
    path = Path(filepath)
    content = path.read_text(encoding="utf-8")

    if sentinel in content:
        print(f"  [skip] {sentinel} already present in {path.name}")
        return False

    if inject_anchor not in content:
        print(f"  [ERROR] Anchor not found: {inject_anchor!r} in {path.name}")
        return False

    new_content = content.replace(inject_anchor, inject_content + "\n" + inject_anchor)
    path.write_text(new_content, encoding="utf-8")
    added = len(new_content) - len(content)
    print(f"  [ok] Injected {added:+,} chars before {inject_anchor!r} in {path.name}")
    return True


def main():
    target = "index.html"

    results = [
        patch(target, GRC_SENTINEL,    GRC_CONTENT,    GRC_INJECT_ANCHOR),
        patch(target, THREAT_SENTINEL, THREAT_CONTENT, THREAT_INJECT_ANCHOR),
        patch(target, OPS_SENTINEL,    OPS_CONTENT,    OPS_INJECT_ANCHOR),
        patch(target, AI_SENTINEL,     AI_CONTENT,     AI_INJECT_ANCHOR),
        patch(target, SCRIPT_SENTINEL, SCRIPT_CONTENT, SCRIPT_INJECT_ANCHOR),
    ]

    if any(results):
        from html.parser import HTMLParser

        class BalanceChecker(HTMLParser):
            VOID = {"area","base","br","col","embed","hr","img","input","link","meta","param","source","track","wbr"}
            def __init__(self):
                super().__init__()
                self.stack = []
                self.strays = []
            def handle_starttag(self, tag, attrs):
                if tag not in self.VOID:
                    self.stack.append(tag)
            def handle_endtag(self, tag):
                if tag in self.VOID:
                    return
                if self.stack and self.stack[-1] == tag:
                    self.stack.pop()
                else:
                    self.strays.append(tag)

        checker = BalanceChecker()
        checker.feed(Path(target).read_text(encoding="utf-8"))
        print(f"\n  Unclosed at EOF: {checker.stack[-5:] if checker.stack else 'NONE'}")
        print(f"  Stray end tags: {len(checker.strays)}")

        new_len = Path(target).stat().st_size
        print(f"\n  {target}: {new_len:,} bytes")


if __name__ == "__main__":
    main()
