#!/usr/bin/env python3
"""
patch_beginner_concepts_v6.py — Wave 6: deeper coding + practical domain content.

New sentinels:
  BEGINNER6-SCRIPT v1   — APIs & HTTP, JSON data handling, modules/packages, OOP basics
  BEGINNER6-NET v1      — How DNS works, DHCP, NAT deep dive, wireless basics
  BEGINNER6-SEC v1      — Passwords & hashing, MFA, phishing anatomy, encryption types
  BEGINNER6-LINUX v1    — Shell scripting basics, cron jobs, processes & signals
  BEGINNER6-LIFE v1     — Learning mindset, imposter syndrome, burnout prevention
"""
import re
import sys
from pathlib import Path

SCRIPT_INJECT_ANCHOR = "<!-- /domain-body script -->"
NET_INJECT_ANCHOR    = "<!-- /domain-body net -->"
SEC_INJECT_ANCHOR    = "<!-- /domain-body sec -->"
LINUX_INJECT_ANCHOR  = "<!-- /domain-body linux -->"
LIFE_INJECT_ANCHOR   = "<!-- /domain-body lifestyle -->"

# ─────────────────────────────── SCRIPTING wave 6 ────────────────────────────
SCRIPT_SENTINEL = "<!-- BEGINNER6-SCRIPT v1 -->"
SCRIPT_CONTENT = """
<!-- BEGINNER6-SCRIPT v1 -->
<!-- ── TOPIC: APIs & HTTP FOR BEGINNERS ─────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">🌐</span>
    <span class="topic-name">APIs &amp; HTTP — How Programs Talk to Each Other</span>
    <span class="topic-badge">SCRIPT • Start Here</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">WHAT IS AN API</div>
      <div class="concept-title">Application Programming Interface</div>
      <div class="concept-desc">An API is a <strong>menu at a restaurant</strong>. You don't walk into the kitchen — you order from a menu (the API), the kitchen (server) makes it, and the waiter (HTTP) brings it back. You get what you need without knowing how it's made.</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">HTTP VERBS</div>
      <div class="concept-title">GET · POST · PUT · DELETE</div>
      <div class="concept-desc">The four core actions match CRUD:<br>
      <strong>GET</strong> — read/fetch data (no side effects)<br>
      <strong>POST</strong> — create/send new data<br>
      <strong>PUT</strong> — replace existing data entirely<br>
      <strong>DELETE</strong> — remove data<br>
      Think: GET a pizza menu, POST your order, PUT a replacement order, DELETE it.</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">STATUS CODES</div>
      <div class="concept-title">What the Server Says Back</div>
      <div class="concept-desc">Every response has a 3-digit status code.<br>
      <strong>2xx</strong> = Success (200 OK, 201 Created)<br>
      <strong>3xx</strong> = Redirect (301 Moved, 304 Not Modified)<br>
      <strong>4xx</strong> = Your fault (400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found)<br>
      <strong>5xx</strong> = Server's fault (500 Internal Server Error, 503 Service Unavailable)</div>
    </div>
    <table class="ai-table">
      <thead><tr><th>Code</th><th>Name</th><th>Plain English</th></tr></thead>
      <tbody>
        <tr><td>200</td><td>OK</td><td>Everything worked</td></tr>
        <tr><td>201</td><td>Created</td><td>New thing was made</td></tr>
        <tr><td>400</td><td>Bad Request</td><td>You sent garbage data</td></tr>
        <tr><td>401</td><td>Unauthorized</td><td>Who are you? Log in first</td></tr>
        <tr><td>403</td><td>Forbidden</td><td>I know who you are — you still can't</td></tr>
        <tr><td>404</td><td>Not Found</td><td>That URL doesn't exist</td></tr>
        <tr><td>429</td><td>Too Many Requests</td><td>Slow down, you're spamming</td></tr>
        <tr><td>500</td><td>Internal Server Error</td><td>The server broke (not your fault)</td></tr>
      </tbody>
    </table>
    <div class="concept-card">
      <div class="concept-label">MAKING A REQUEST</div>
      <div class="concept-title">Python fetch example</div>
      <div class="concept-desc">Using the <code>requests</code> library (install with <code>pip install requests</code>):</div>
      <div class="code-block"><span class="kw">import</span> requests

<span class="com"># Fetch a list of users from a free test API</span>
response = requests.get(<span class="str">"https://jsonplaceholder.typicode.com/users"</span>)

<span class="com"># Always check the status before trusting the data</span>
<span class="kw">if</span> response.status_code == <span class="num">200</span>:
    users = response.json()        <span class="com"># parse JSON into a Python list</span>
    <span class="kw">for</span> user <span class="kw">in</span> users[:3]:
        <span class="fn">print</span>(user[<span class="str">"name"</span>], <span class="str">"-"</span>, user[<span class="str">"email"</span>])
<span class="kw">else</span>:
    <span class="fn">print</span>(<span class="str">f"Error: {response.status_code}"</span>)</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">HEADERS & AUTH</div>
      <div class="concept-title">Talking With a Credential</div>
      <div class="concept-desc">Most real APIs require an API key or token. Send it in the header, NOT the URL (URLs can appear in logs):</div>
      <div class="code-block"><span class="com"># Bearer token auth (most common for modern APIs)</span>
headers = {
    <span class="str">"Authorization"</span>: <span class="str">"Bearer YOUR_API_KEY_HERE"</span>,
    <span class="str">"Content-Type"</span>: <span class="str">"application/json"</span>,
}
response = requests.get(<span class="str">"https://api.example.com/data"</span>, headers=headers)</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">REST vs SOAP vs GRAPHQL</div>
      <div class="concept-title">Three API Styles</div>
      <div class="concept-desc"><strong>REST</strong> — most common today; uses HTTP verbs + URLs; returns JSON. Easy to learn, widely supported.<br>
      <strong>SOAP</strong> — older enterprise style; uses XML; very structured and verbose. You'll encounter it in legacy systems.<br>
      <strong>GraphQL</strong> — you ask for exactly what you need in one request; returns only what you specified. Reduces over-fetching.</div>
    </div>
  </div>
</div>

<!-- ── TOPIC: JSON DATA HANDLING ────────────────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">📦</span>
    <span class="topic-name">JSON — The Universal Data Language</span>
    <span class="topic-badge">SCRIPT • Practical</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">WHAT IS JSON</div>
      <div class="concept-title">JavaScript Object Notation</div>
      <div class="concept-desc">JSON is text that represents structured data. It's <strong>language-neutral</strong> — Python, JavaScript, Java, Go all read it. You'll use JSON constantly: API responses, config files, log data, database records.</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">VALID JSON TYPES</div>
      <div class="concept-title">Six Data Types in JSON</div>
      <div class="code-block"><span class="com">// JSON supports exactly these value types:</span>
{
  <span class="str">"string"</span>:   <span class="str">"hello world"</span>,
  <span class="str">"number"</span>:   <span class="num">42</span>,
  <span class="str">"float"</span>:    <span class="num">3.14</span>,
  <span class="str">"boolean"</span>:  <span class="kw">true</span>,
  <span class="str">"nothing"</span>:  <span class="kw">null</span>,
  <span class="str">"array"</span>:    [<span class="num">1</span>, <span class="num">2</span>, <span class="num">3</span>],
  <span class="str">"object"</span>:   { <span class="str">"key"</span>: <span class="str">"value"</span> }
}</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">PARSE & SERIALIZE</div>
      <div class="concept-title">JSON in Python — Two Directions</div>
      <div class="code-block"><span class="kw">import</span> json

<span class="com"># JSON string → Python object (parse/deserialize)</span>
text = <span class="str">'{"name": "Alice", "age": 30}'</span>
person = json.loads(text)
<span class="fn">print</span>(person[<span class="str">"name"</span>])   <span class="com"># Alice</span>

<span class="com"># Python object → JSON string (serialize/dump)</span>
data = {<span class="str">"city"</span>: <span class="str">"Austin"</span>, <span class="str">"pop"</span>: <span class="num">961000</span>}
text = json.dumps(data, indent=<span class="num">2</span>)
<span class="fn">print</span>(text)

<span class="com"># Write JSON to a file</span>
<span class="kw">with</span> <span class="fn">open</span>(<span class="str">"output.json"</span>, <span class="str">"w"</span>) <span class="kw">as</span> f:
    json.dump(data, f, indent=<span class="num">2</span>)

<span class="com"># Read JSON from a file</span>
<span class="kw">with</span> <span class="fn">open</span>(<span class="str">"output.json"</span>) <span class="kw">as</span> f:
    loaded = json.load(f)</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">NESTED JSON</div>
      <div class="concept-title">Digging Into Deep Structures</div>
      <div class="concept-desc">Real API data is often nested. Navigate with chained bracket notation, but always guard against missing keys using <code>.get()</code>:</div>
      <div class="code-block"><span class="com"># Typical API response structure</span>
data = {
    <span class="str">"user"</span>: {
        <span class="str">"profile"</span>: {
            <span class="str">"name"</span>: <span class="str">"Bob"</span>,
            <span class="str">"tags"</span>: [<span class="str">"admin"</span>, <span class="str">"dev"</span>]
        }
    }
}

<span class="com"># Safe deep access</span>
name = data.get(<span class="str">"user"</span>, {}).get(<span class="str">"profile"</span>, {}).get(<span class="str">"name"</span>, <span class="str">"unknown"</span>)
first_tag = data[<span class="str">"user"</span>][<span class="str">"profile"</span>][<span class="str">"tags"</span>][<span class="num">0</span>]  <span class="com"># "admin"</span></div>
    </div>
    <div class="concept-card">
      <div class="concept-label">COMMON GOTCHAS</div>
      <div class="concept-title">JSON Pitfalls for Beginners</div>
      <div class="concept-desc"><strong>Trailing commas</strong> — JSON does NOT allow them. <code>{"a":1,}</code> is invalid.<br>
      <strong>Single quotes</strong> — JSON requires double quotes. <code>{'a':'b'}</code> is invalid.<br>
      <strong>Comments</strong> — standard JSON has no comments. Use JSONC or strip them before parsing.<br>
      <strong>Large numbers</strong> — JSON numbers lose precision beyond 2^53. Use strings for large IDs.</div>
    </div>
  </div>
</div>

<!-- ── TOPIC: MODULES & PACKAGES ─────────────────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">📚</span>
    <span class="topic-name">Modules, Packages &amp; pip — Using Other People's Code</span>
    <span class="topic-badge">SCRIPT • Foundation</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">MODULE vs PACKAGE</div>
      <div class="concept-title">Files vs Folders of Code</div>
      <div class="concept-desc">A <strong>module</strong> is a single <code>.py</code> file containing functions, classes, or variables you can import. A <strong>package</strong> is a folder of modules with an <code>__init__.py</code> file. A <strong>library</strong> is a collection of packages. The standard library comes with Python; third-party ones need <code>pip</code>.</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">IMPORTING</div>
      <div class="concept-title">Five Import Patterns</div>
      <div class="code-block"><span class="kw">import</span> math                     <span class="com"># import whole module</span>
<span class="fn">print</span>(math.sqrt(<span class="num">16</span>))

<span class="kw">from</span> math <span class="kw">import</span> sqrt            <span class="com"># import one thing</span>
<span class="fn">print</span>(sqrt(<span class="num">16</span>))

<span class="kw">from</span> math <span class="kw">import</span> sqrt, pi        <span class="com"># import several things</span>

<span class="kw">import</span> numpy <span class="kw">as</span> np              <span class="com"># alias (numpy convention)</span>

<span class="kw">from</span> os.path <span class="kw">import</span> join, exists <span class="com"># from submodule</span></div>
    </div>
    <div class="concept-card">
      <div class="concept-label">PIP</div>
      <div class="concept-title">Python's Package Installer</div>
      <div class="code-block"><span class="com"># Install a package from PyPI</span>
pip install requests

<span class="com"># Install a specific version</span>
pip install requests==2.31.0

<span class="com"># Install from a requirements file</span>
pip install -r requirements.txt

<span class="com"># See what's installed</span>
pip list

<span class="com"># Freeze current environment to requirements.txt</span>
pip freeze &gt; requirements.txt

<span class="com"># Uninstall</span>
pip uninstall requests</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">VIRTUAL ENVIRONMENTS</div>
      <div class="concept-title">Keep Projects Isolated</div>
      <div class="concept-desc">Never install packages globally. Use a virtual environment so Project A and Project B can have different versions of the same library without conflict.</div>
      <div class="code-block"><span class="com"># Create venv (Python 3.3+)</span>
python3 -m venv .venv

<span class="com"># Activate it</span>
source .venv/bin/activate       <span class="com"># macOS/Linux</span>
.venv\Scripts\activate          <span class="com"># Windows</span>

<span class="com"># Now pip installs go into .venv only</span>
pip install requests

<span class="com"># Deactivate when done</span>
deactivate</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">USEFUL STDLIB</div>
      <div class="concept-title">Built-In Batteries Worth Knowing</div>
      <div class="concept-desc">Python's standard library has everything you need for common tasks — no pip required:</div>
      <table class="ai-table">
        <thead><tr><th>Module</th><th>What It Does</th></tr></thead>
        <tbody>
          <tr><td>os, pathlib</td><td>File and directory operations</td></tr>
          <tr><td>sys</td><td>Command-line args, exit codes</td></tr>
          <tr><td>json</td><td>Parse and create JSON</td></tr>
          <tr><td>datetime</td><td>Dates, times, timedeltas</td></tr>
          <tr><td>re</td><td>Regular expressions</td></tr>
          <tr><td>random</td><td>Random numbers, shuffling, sampling</td></tr>
          <tr><td>collections</td><td>Counter, defaultdict, deque, namedtuple</td></tr>
          <tr><td>itertools</td><td>Combinatoric iterators (product, chain, etc.)</td></tr>
          <tr><td>math</td><td>Floor, ceil, sqrt, log, trig</td></tr>
          <tr><td>hashlib</td><td>MD5, SHA-256 hashing</td></tr>
          <tr><td>subprocess</td><td>Run shell commands from Python</td></tr>
          <tr><td>logging</td><td>Proper logging (not just print)</td></tr>
        </tbody>
      </table>
    </div>
  </div>
</div>

<!-- ── TOPIC: OOP BASICS ──────────────────────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">🏗️</span>
    <span class="topic-name">Object-Oriented Programming — Classes &amp; Objects</span>
    <span class="topic-badge">SCRIPT • Intermediate</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">THE BIG IDEA</div>
      <div class="concept-title">Bundle Data + Behavior Together</div>
      <div class="concept-desc">OOP groups related <strong>data (attributes)</strong> and <strong>actions (methods)</strong> into one unit called a <strong>class</strong>. A <strong>class</strong> is a blueprint; an <strong>object</strong> (or instance) is the real thing built from that blueprint. One blueprint → many objects.</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">CLASS ANATOMY</div>
      <div class="concept-title">Your First Class</div>
      <div class="code-block"><span class="kw">class</span> <span class="fn">Dog</span>:
    <span class="com"># __init__ runs when you create a new Dog</span>
    <span class="kw">def</span> <span class="fn">__init__</span>(<span class="kw">self</span>, name, breed):
        <span class="kw">self</span>.name  = name   <span class="com"># instance attribute</span>
        <span class="kw">self</span>.breed = breed
        <span class="kw">self</span>.tricks = []    <span class="com"># every dog starts with no tricks</span>

    <span class="kw">def</span> <span class="fn">learn</span>(<span class="kw">self</span>, trick):
        <span class="kw">self</span>.tricks.append(trick)

    <span class="kw">def</span> <span class="fn">show_off</span>(<span class="kw">self</span>):
        <span class="kw">if</span> <span class="kw">self</span>.tricks:
            <span class="fn">print</span>(<span class="str">f"{self.name} knows: {', '.join(self.tricks)}"</span>)
        <span class="kw">else</span>:
            <span class="fn">print</span>(<span class="str">f"{self.name} knows nothing yet."</span>)

<span class="com"># Create two Dog objects from one blueprint</span>
rex = <span class="fn">Dog</span>(<span class="str">"Rex"</span>, <span class="str">"Lab"</span>)
buddy = <span class="fn">Dog</span>(<span class="str">"Buddy"</span>, <span class="str">"Poodle"</span>)

rex.learn(<span class="str">"sit"</span>)
rex.learn(<span class="str">"shake"</span>)
rex.show_off()     <span class="com"># Rex knows: sit, shake</span>
buddy.show_off()   <span class="com"># Buddy knows nothing yet.</span></div>
    </div>
    <div class="concept-card">
      <div class="concept-label">FOUR PILLARS</div>
      <div class="concept-title">Encapsulation · Inheritance · Polymorphism · Abstraction</div>
      <div class="concept-desc"><strong>Encapsulation</strong> — hide internal details; expose only what's needed (private <code>_name</code> convention in Python).<br>
      <strong>Inheritance</strong> — child class gets parent's methods; add or override as needed.<br>
      <strong>Polymorphism</strong> — same method name, different behavior per class (<code>speak()</code> on Dog vs Cat).<br>
      <strong>Abstraction</strong> — focus on WHAT, not HOW (you call <code>.sort()</code> without knowing the algorithm).</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">INHERITANCE EXAMPLE</div>
      <div class="concept-title">Extend Without Duplicating</div>
      <div class="code-block"><span class="kw">class</span> <span class="fn">Animal</span>:
    <span class="kw">def</span> <span class="fn">__init__</span>(<span class="kw">self</span>, name):
        <span class="kw">self</span>.name = name

    <span class="kw">def</span> <span class="fn">speak</span>(<span class="kw">self</span>):
        <span class="kw">raise</span> NotImplementedError

<span class="kw">class</span> <span class="fn">Dog</span>(Animal):           <span class="com"># Dog inherits from Animal</span>
    <span class="kw">def</span> <span class="fn">speak</span>(<span class="kw">self</span>):
        <span class="kw">return</span> <span class="str">f"{self.name} says Woof!"</span>

<span class="kw">class</span> <span class="fn">Cat</span>(Animal):
    <span class="kw">def</span> <span class="fn">speak</span>(<span class="kw">self</span>):
        <span class="kw">return</span> <span class="str">f"{self.name} says Meow."</span>

animals = [<span class="fn">Dog</span>(<span class="str">"Rex"</span>), <span class="fn">Cat</span>(<span class="str">"Whiskers"</span>), <span class="fn">Dog</span>(<span class="str">"Buddy"</span>)]
<span class="kw">for</span> a <span class="kw">in</span> animals:
    <span class="fn">print</span>(a.speak())   <span class="com"># polymorphism — same call, different result</span></div>
    </div>
    <div class="concept-card">
      <div class="concept-label">WHEN TO USE OOP</div>
      <div class="concept-title">Not Everything Needs a Class</div>
      <div class="concept-desc">OOP shines when you have <strong>multiple instances of the same kind of thing</strong> (users, transactions, network packets). Overkill for a 30-line script that reads a file and prints output. Rule of thumb: if you're writing the same data structure twice, make it a class.</div>
    </div>
  </div>
</div>

<!-- ── TOPIC: DATA STRUCTURES — WHICH TO PICK ──────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">🗂️</span>
    <span class="topic-name">Choosing the Right Data Structure</span>
    <span class="topic-badge">SCRIPT • Intermediate</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">THE LINEUP</div>
      <div class="concept-title">List · Tuple · Dict · Set · Queue · Stack</div>
      <div class="concept-desc">Each structure is optimized for different operations. Picking the wrong one makes your code slow and confusing. Picking the right one makes it fast and readable.</div>
    </div>
    <table class="ai-table">
      <thead><tr><th>Structure</th><th>Ordered?</th><th>Mutable?</th><th>Duplicates?</th><th>Best For</th></tr></thead>
      <tbody>
        <tr><td>list []</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Ordered collections you'll iterate</td></tr>
        <tr><td>tuple ()</td><td>Yes</td><td>No</td><td>Yes</td><td>Immutable records (coordinates, RGB)</td></tr>
        <tr><td>dict {}</td><td>Yes (3.7+)</td><td>Yes</td><td>Keys: No</td><td>Key→value lookup; configs, counters</td></tr>
        <tr><td>set {}</td><td>No</td><td>Yes</td><td>No</td><td>Membership tests; de-duplication</td></tr>
        <tr><td>deque</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Fast append/pop from both ends</td></tr>
        <tr><td>heapq</td><td>Partial</td><td>Yes</td><td>Yes</td><td>Always get the smallest/largest item</td></tr>
      </tbody>
    </table>
    <div class="concept-card">
      <div class="concept-label">DICT TRICKS</div>
      <div class="concept-title">Patterns You'll Use Weekly</div>
      <div class="code-block"><span class="kw">from</span> collections <span class="kw">import</span> defaultdict, Counter

<span class="com"># Count word frequencies (classic interview problem)</span>
words = [<span class="str">"apple"</span>, <span class="str">"banana"</span>, <span class="str">"apple"</span>, <span class="str">"cherry"</span>, <span class="str">"banana"</span>, <span class="str">"apple"</span>]
counts = Counter(words)
<span class="fn">print</span>(counts.most_common(<span class="num">2</span>))  <span class="com"># [('apple', 3), ('banana', 2)]</span>

<span class="com"># Group items without KeyError</span>
groups = defaultdict(<span class="fn">list</span>)
<span class="kw">for</span> word <span class="kw">in</span> words:
    groups[word[<span class="num">0</span>]].append(word)  <span class="com"># group by first letter</span>

<span class="com"># Dict comprehension — build in one line</span>
squared = {x: x**<span class="num">2</span> <span class="kw">for</span> x <span class="kw">in</span> <span class="fn">range</span>(<span class="num">5</span>)}  <span class="com"># {0:0, 1:1, 2:4, 3:9, 4:16}</span>

<span class="com"># Merge two dicts (Python 3.9+)</span>
a = {<span class="str">"x"</span>: <span class="num">1</span>}
b = {<span class="str">"y"</span>: <span class="num">2</span>}
merged = a | b   <span class="com"># {"x": 1, "y": 2}</span></div>
    </div>
    <div class="concept-card">
      <div class="concept-label">SET USE CASES</div>
      <div class="concept-title">Membership Test is O(1)</div>
      <div class="code-block"><span class="com"># De-duplicate a list instantly</span>
names = [<span class="str">"Alice"</span>, <span class="str">"Bob"</span>, <span class="str">"Alice"</span>, <span class="str">"Carol"</span>]
unique = <span class="fn">list</span>(<span class="fn">set</span>(names))

<span class="com"># Fast membership test (1M items, still instant)</span>
allowed = {<span class="str">"admin"</span>, <span class="str">"editor"</span>, <span class="str">"viewer"</span>}
<span class="kw">if</span> user_role <span class="kw">in</span> allowed:    <span class="com"># O(1) — use set, not list</span>
    grant_access()

<span class="com"># Set operations</span>
a = {<span class="num">1</span>, <span class="num">2</span>, <span class="num">3</span>}
b = {<span class="num">2</span>, <span class="num">3</span>, <span class="num">4</span>}
a &amp; b   <span class="com"># {2, 3}   intersection</span>
a | b   <span class="com"># {1,2,3,4} union</span>
a - b   <span class="com"># {1}      difference</span>
a ^ b   <span class="com"># {1, 4}  symmetric difference</span></div>
    </div>
  </div>
</div>
"""

# ─────────────────────────────── NETWORKING wave 6 ───────────────────────────
NET_SENTINEL = "<!-- BEGINNER6-NET v1 -->"
NET_CONTENT = """
<!-- BEGINNER6-NET v1 -->
<!-- ── TOPIC: HOW DNS WORKS ──────────────────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">📖</span>
    <span class="topic-name">DNS — The Internet's Phone Book</span>
    <span class="topic-badge">NET • Start Here</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">THE PROBLEM DNS SOLVES</div>
      <div class="concept-title">Humans Hate Numbers</div>
      <div class="concept-desc">Computers talk to each other using IP addresses like <code>142.250.80.46</code>. Humans want to type <code>google.com</code>. DNS (Domain Name System) translates names into numbers — like a phone book that covers the whole internet.</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">THE DNS LOOKUP JOURNEY</div>
      <div class="concept-title">8 Steps From Name to IP</div>
      <div class="concept-desc">1. You type <code>google.com</code> in your browser.<br>
      2. Browser checks its own cache. If found → done.<br>
      3. OS checks its cache. If found → done.<br>
      4. OS asks your <strong>recursive resolver</strong> (your ISP or 8.8.8.8).<br>
      5. Resolver asks a <strong>root nameserver</strong> (13 clusters worldwide) — "who handles .com?"<br>
      6. Root points to the <strong>.com TLD nameserver</strong> (Verisign).<br>
      7. TLD server points to <strong>Google's authoritative nameserver</strong>.<br>
      8. Authoritative server returns the IP. Resolver caches it and gives it to you.</div>
    </div>
    <table class="ai-table">
      <thead><tr><th>DNS Record Type</th><th>Purpose</th><th>Example</th></tr></thead>
      <tbody>
        <tr><td>A</td><td>Domain → IPv4 address</td><td>google.com → 142.250.80.46</td></tr>
        <tr><td>AAAA</td><td>Domain → IPv6 address</td><td>google.com → 2607:f8b0:…</td></tr>
        <tr><td>CNAME</td><td>Alias → another domain</td><td>www.example.com → example.com</td></tr>
        <tr><td>MX</td><td>Mail server for domain</td><td>example.com → mail.example.com</td></tr>
        <tr><td>TXT</td><td>Arbitrary text (SPF, DKIM, verification)</td><td>v=spf1 include:… ~all</td></tr>
        <tr><td>NS</td><td>Nameservers for domain</td><td>ns1.google.com</td></tr>
        <tr><td>PTR</td><td>Reverse lookup: IP → domain</td><td>46.80.250.142.in-addr.arpa → google.com</td></tr>
        <tr><td>SOA</td><td>Start of Authority; zone metadata</td><td>Serial, refresh, retry, expire</td></tr>
      </tbody>
    </table>
    <div class="concept-card">
      <div class="concept-label">USEFUL DNS TOOLS</div>
      <div class="concept-title">Dig, nslookup, host</div>
      <div class="code-block"><span class="com"># Query A record for a domain</span>
dig google.com A

<span class="com"># Query MX records (mail servers)</span>
dig google.com MX

<span class="com"># Reverse lookup</span>
dig -x 142.250.80.46

<span class="com"># Use a specific resolver (8.8.8.8 = Google DNS)</span>
dig @8.8.8.8 google.com

<span class="com"># Windows equivalent</span>
nslookup google.com
nslookup -type=MX google.com</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">TTL</div>
      <div class="concept-title">Time to Live — DNS Caching Timer</div>
      <div class="concept-desc">Every DNS record has a TTL (Time To Live) in seconds. After TTL expires, resolvers re-query for fresh results. Low TTL = fast changes but more queries. High TTL = slow propagation but less load. When migrating a website, lower the TTL 24 hours before the switch.</div>
    </div>
  </div>
</div>

<!-- ── TOPIC: DHCP & IP ASSIGNMENT ───────────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">🔢</span>
    <span class="topic-name">DHCP — How Devices Get Their IP Address</span>
    <span class="topic-badge">NET • Foundation</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">DORA PROCESS</div>
      <div class="concept-title">Discover → Offer → Request → Acknowledge</div>
      <div class="concept-desc"><strong>Discover</strong> — new device broadcasts "I need an IP!" to 255.255.255.255.<br>
      <strong>Offer</strong> — DHCP server says "How about 192.168.1.25? Here's a lease offer."<br>
      <strong>Request</strong> — client says "Yes, I'll take 192.168.1.25" (broadcast, so other servers know).<br>
      <strong>Acknowledge</strong> — server confirms: "192.168.1.25 is yours for 24 hours. Here's gateway and DNS too."</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">WHAT DHCP HANDS OUT</div>
      <div class="concept-title">More Than Just an IP</div>
      <div class="concept-desc">A DHCP lease typically includes:<br>
      • <strong>IP address</strong> — unique on the local network<br>
      • <strong>Subnet mask</strong> — defines network boundary (e.g., 255.255.255.0)<br>
      • <strong>Default gateway</strong> — the router's IP (traffic leaving the network goes here)<br>
      • <strong>DNS server(s)</strong> — where to resolve names<br>
      • <strong>Lease duration</strong> — how long before re-requesting</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">STATIC vs DYNAMIC</div>
      <div class="concept-title">Manual vs Automatic Assignment</div>
      <div class="concept-desc"><strong>Dynamic</strong> — DHCP assigns from a pool; good for laptops and phones. IP may change on reconnect.<br>
      <strong>Static</strong> — manually set; never changes. Required for servers, printers, network gear (you don't want DNS records breaking because the server got a new IP).<br>
      <strong>DHCP Reservation</strong> — best of both worlds: DHCP assigns based on MAC address, so the device always gets the same IP automatically.</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">TROUBLESHOOTING</div>
      <div class="concept-title">When DHCP Fails — APIPA</div>
      <div class="concept-desc">If a device can't reach a DHCP server, Windows auto-assigns an <strong>APIPA</strong> address: <code>169.254.x.x</code>. This is a red flag — the device only has link-local connectivity and cannot reach the internet. Check: cable unplugged? DHCP server down? VLAN misconfigured?</div>
    </div>
  </div>
</div>

<!-- ── TOPIC: WIRELESS NETWORKING BASICS ─────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">📡</span>
    <span class="topic-name">Wi-Fi Basics — 802.11, Bands, and Security</span>
    <span class="topic-badge">NET • Practical</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">802.11 STANDARDS</div>
      <div class="concept-title">The Evolution of Wi-Fi</div>
      <div class="concept-desc">The 802.11 family are the IEEE wireless LAN standards. Each letter suffix means a different generation:</div>
      <table class="ai-table">
        <thead><tr><th>Standard</th><th>Wi-Fi Name</th><th>Max Speed</th><th>Band</th><th>Year</th></tr></thead>
        <tbody>
          <tr><td>802.11b</td><td>—</td><td>11 Mbps</td><td>2.4 GHz</td><td>1999</td></tr>
          <tr><td>802.11g</td><td>—</td><td>54 Mbps</td><td>2.4 GHz</td><td>2003</td></tr>
          <tr><td>802.11n</td><td>Wi-Fi 4</td><td>600 Mbps</td><td>2.4/5 GHz</td><td>2009</td></tr>
          <tr><td>802.11ac</td><td>Wi-Fi 5</td><td>3.5 Gbps</td><td>5 GHz</td><td>2013</td></tr>
          <tr><td>802.11ax</td><td>Wi-Fi 6/6E</td><td>9.6 Gbps</td><td>2.4/5/6 GHz</td><td>2019</td></tr>
          <tr><td>802.11be</td><td>Wi-Fi 7</td><td>46 Gbps</td><td>2.4/5/6 GHz</td><td>2024</td></tr>
        </tbody>
      </table>
    </div>
    <div class="concept-card">
      <div class="concept-label">2.4 GHz vs 5 GHz</div>
      <div class="concept-title">Range vs Speed Trade-off</div>
      <div class="concept-desc"><strong>2.4 GHz</strong> — longer range, penetrates walls better, more congestion (microwaves, Bluetooth, neighbors all compete), slower. Good for: IoT devices, devices far from router.<br>
      <strong>5 GHz</strong> — shorter range, struggles through walls, less congested, faster. Good for: laptops and phones close to router, streaming, gaming.<br>
      <strong>6 GHz (Wi-Fi 6E)</strong> — even faster, very short range, nearly empty spectrum. Best for: dense environments (offices, stadiums).</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">WIRELESS SECURITY</div>
      <div class="concept-title">WEP → WPA → WPA2 → WPA3</div>
      <div class="concept-desc"><strong>WEP</strong> — broken in minutes; do not use.<br>
      <strong>WPA</strong> — better but still has vulnerabilities; phase out.<br>
      <strong>WPA2-Personal (PSK)</strong> — current standard for home; uses AES-CCMP; strong if you use a long passphrase.<br>
      <strong>WPA2-Enterprise</strong> — uses RADIUS authentication; each user has their own credentials. Used in corporate environments.<br>
      <strong>WPA3</strong> — latest; uses SAE (Simultaneous Authentication of Equals) instead of PSK handshake; resistant to offline dictionary attacks.</div>
    </div>
  </div>
</div>
"""

# ─────────────────────────────── SECURITY wave 6 ─────────────────────────────
SEC_SENTINEL = "<!-- BEGINNER6-SEC v1 -->"
SEC_CONTENT = """
<!-- BEGINNER6-SEC v1 -->
<!-- ── TOPIC: PASSWORDS & HASHING ────────────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">🔑</span>
    <span class="topic-name">Passwords &amp; Hashing — How Logins Are Stored Safely</span>
    <span class="topic-badge">SEC • Start Here</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">NEVER STORE PLAINTEXT</div>
      <div class="concept-title">The Golden Rule of Password Storage</div>
      <div class="concept-desc">Databases get breached. If passwords are stored as-is, every user's password is exposed instantly. Instead, store a <strong>hash</strong> — a one-way transformation that cannot be reversed. When a user logs in, hash what they typed and compare hashes.</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">WHAT IS A HASH</div>
      <div class="concept-title">One-Way Fingerprint</div>
      <div class="concept-desc">A hash function takes any input and produces a fixed-length output. Same input ALWAYS produces same output. Even one character change completely changes the hash (avalanche effect). You cannot go from hash → original (one-way).</div>
      <div class="code-block"><span class="kw">import</span> hashlib

text = <span class="str">"hunter2"</span>
h = hashlib.sha256(text.encode()).hexdigest()
<span class="com"># f52fbd32b2b3b86ff88ef6c490628285f482af15ddcb29541f94bcf526a3f6c7</span>

text2 = <span class="str">"hunter3"</span>   <span class="com"># one char different</span>
h2 = hashlib.sha256(text2.encode()).hexdigest()
<span class="com"># 7a20f6f8c04b1a590a39c74b4f6b3c4a8e6a7f1c2d3e4f5a6b7c8d9e0f1a2b3</span>
<span class="com"># Completely different — avalanche effect</span></div>
    </div>
    <div class="concept-card">
      <div class="concept-label">SALTING</div>
      <div class="concept-title">Why Two Users With Same Password Need Different Hashes</div>
      <div class="concept-desc">Without salts, two users with "password123" produce the same hash — attackers can pre-compute tables (rainbow tables) and look up hashes instantly. A <strong>salt</strong> is a random value added to the password before hashing. Every user gets a unique salt. Rainbow tables become useless.</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">RIGHT TOOLS FOR PASSWORDS</div>
      <div class="concept-title">Use bcrypt, scrypt, or Argon2</div>
      <div class="concept-desc">SHA-256 is fast — that's GOOD for verifying file integrity, BAD for passwords (attackers can try billions/sec). <strong>bcrypt</strong>, <strong>scrypt</strong>, and <strong>Argon2</strong> are deliberately slow and memory-hard. They automatically handle salting. Never hand-roll password hashing.</div>
      <div class="code-block"><span class="com"># pip install bcrypt</span>
<span class="kw">import</span> bcrypt

<span class="com"># Hash when user registers</span>
password = <span class="str">"my_secure_pass"</span>
hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

<span class="com"># Verify on login</span>
entered = <span class="str">"my_secure_pass"</span>
<span class="kw">if</span> bcrypt.checkpw(entered.encode(), hashed):
    <span class="fn">print</span>(<span class="str">"Login OK"</span>)</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">STRONG PASSWORDS</div>
      <div class="concept-title">Length Beats Complexity</div>
      <div class="concept-desc">A 20-character random passphrase is stronger than "P@$$w0rd!" — and much easier to remember. Use a <strong>password manager</strong> (Bitwarden, 1Password, KeePass). Generate unique passwords for every site. Enable MFA everywhere possible.</div>
    </div>
  </div>
</div>

<!-- ── TOPIC: MFA & AUTHENTICATION METHODS ──────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">📲</span>
    <span class="topic-name">Multi-Factor Authentication — Layers of Proof</span>
    <span class="topic-badge">SEC • Foundation</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">THREE FACTORS</div>
      <div class="concept-title">Something You Know, Have, or Are</div>
      <div class="concept-desc"><strong>Knowledge factor</strong> — something you know: password, PIN, security questions (weakest).<br>
      <strong>Possession factor</strong> — something you have: phone (SMS code, authenticator app), hardware token (YubiKey), smart card.<br>
      <strong>Inherence factor</strong> — something you are: fingerprint, face, iris, voice.<br>
      MFA requires 2 or more different factor types. Two passwords is NOT MFA.</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">MFA METHODS RANKED</div>
      <div class="concept-title">From Weakest to Strongest</div>
      <table class="ai-table">
        <thead><tr><th>Method</th><th>Phish-resistant?</th><th>Notes</th></tr></thead>
        <tbody>
          <tr><td>SMS / email OTP</td><td>No</td><td>Vulnerable to SIM swap, SS7 attacks; better than nothing</td></tr>
          <tr><td>TOTP app (Google Auth, Authy)</td><td>Partial</td><td>Time-based 6-digit codes; can be phished in real-time</td></tr>
          <tr><td>Push notification</td><td>No</td><td>MFA fatigue attacks — user approves out of habit</td></tr>
          <tr><td>Hardware token (FIDO2/WebAuthn)</td><td>Yes</td><td>Cryptographically bound to domain; gold standard</td></tr>
          <tr><td>Passkeys</td><td>Yes</td><td>FIDO2 using device biometrics; replacing passwords</td></tr>
        </tbody>
      </table>
    </div>
    <div class="concept-card">
      <div class="concept-label">HOW TOTP WORKS</div>
      <div class="concept-title">Time-Based One-Time Passwords</div>
      <div class="concept-desc">During setup, the server shares a secret key with your phone (usually via QR code). Every 30 seconds, both your phone AND the server compute HMAC-SHA1(secret + current_time_window). They should match. An attacker needs the secret AND the current window — that's why TOTP codes expire so fast.</div>
    </div>
  </div>
</div>

<!-- ── TOPIC: PHISHING ANATOMY ────────────────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">🎣</span>
    <span class="topic-name">Phishing — Anatomy of a Social Engineering Attack</span>
    <span class="topic-badge">SEC • Threat Awareness</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">WHAT IS PHISHING</div>
      <div class="concept-title">Deception, Not Hacking</div>
      <div class="concept-desc">Phishing attacks trick people into giving up credentials, installing malware, or sending money. They exploit <strong>psychology</strong>, not software vulnerabilities. No patch exists for human instinct. The name comes from "fishing" — casting bait and waiting for a bite.</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">ATTACK VARIETIES</div>
      <div class="concept-title">Phishing, Spear, Whaling, Vishing, Smishing</div>
      <div class="concept-desc"><strong>Phishing</strong> — mass emails, generic "Dear Customer" bait.<br>
      <strong>Spear phishing</strong> — targeted at a specific person using research (LinkedIn, social media). High success rate.<br>
      <strong>Whaling</strong> — targets C-suite executives. Higher payoff.<br>
      <strong>Vishing</strong> — voice phishing by phone. "This is Microsoft Support…"<br>
      <strong>Smishing</strong> — SMS phishing. "Your package is stuck, click here."<br>
      <strong>Business Email Compromise (BEC)</strong> — impersonates a CEO to trick finance into a wire transfer.</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">RED FLAGS</div>
      <div class="concept-title">How to Spot a Phishing Attempt</div>
      <div class="concept-desc">• Urgency or fear: "Your account will be suspended in 24 hours!"<br>
      • Mismatched URLs: display text says google.com, actual link is g00gle.evil.com<br>
      • Unexpected attachment — especially .exe, .docm, .zip files<br>
      • Slightly wrong sender address: support@amaz0n.com vs amazon.com<br>
      • Grammar errors (though AI-generated phishing now has perfect grammar)<br>
      • Requests for credentials, wire transfers, or gift cards via email<br>
      • Too-good-to-be-true offers</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">DEFENSE</div>
      <div class="concept-title">What Actually Stops Phishing</div>
      <div class="concept-desc"><strong>Technical</strong>: email filtering (spam/malware), DMARC/SPF/DKIM to prevent spoofing, URL rewriting, MFA (even if credentials are stolen, attacker can't log in).<br>
      <strong>Human</strong>: regular security awareness training with simulated phishing campaigns. People need to fail safely in training, not in real attacks.<br>
      <strong>Process</strong>: out-of-band verification (call the CEO on a known number before wiring $500k).</div>
    </div>
  </div>
</div>
"""

# ─────────────────────────────── LINUX wave 6 ────────────────────────────────
LINUX_SENTINEL = "<!-- BEGINNER6-LINUX v1 -->"
LINUX_CONTENT = """
<!-- BEGINNER6-LINUX v1 -->
<!-- ── TOPIC: SHELL SCRIPTING BASICS ──────────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">📜</span>
    <span class="topic-name">Shell Scripting — Automate Repetitive Work</span>
    <span class="topic-badge">LINUX • Practical</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">WHAT IS A SHELL SCRIPT</div>
      <div class="concept-title">A File Full of Commands</div>
      <div class="concept-desc">A shell script is a plain text file with a list of commands that the shell runs in order. Anything you can type at the prompt, you can put in a script. Scripts automate backups, deployments, user creation, log parsing — anything tedious and repeated.</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">YOUR FIRST SCRIPT</div>
      <div class="concept-title">Hello World in Bash</div>
      <div class="code-block"><span class="com">#!/bin/bash</span>
<span class="com"># The shebang line tells the OS which interpreter to use</span>

<span class="fn">echo</span> <span class="str">"Hello, World!"</span>
<span class="fn">echo</span> <span class="str">"Today is $(date)"</span>   <span class="com"># $() runs a command and inserts output</span></div>
      <div class="concept-desc">Make it executable: <code>chmod +x hello.sh</code><br>
      Run it: <code>./hello.sh</code></div>
    </div>
    <div class="concept-card">
      <div class="concept-label">VARIABLES & INPUT</div>
      <div class="concept-title">Storing and Reading Values</div>
      <div class="code-block"><span class="com">#!/bin/bash</span>
<span class="com"># Variables (no spaces around =)</span>
name=<span class="str">"Alice"</span>
count=<span class="num">5</span>

<span class="fn">echo</span> <span class="str">"Name: $name, Count: $count"</span>

<span class="com"># Read user input</span>
<span class="fn">read</span> -p <span class="str">"Enter your name: "</span> username
<span class="fn">echo</span> <span class="str">"Hello, $username!"</span>

<span class="com"># Command-line arguments</span>
<span class="fn">echo</span> <span class="str">"Script: $0"</span>    <span class="com"># script name</span>
<span class="fn">echo</span> <span class="str">"Arg 1: $1"</span>    <span class="com"># first argument</span>
<span class="fn">echo</span> <span class="str">"All args: $@"</span> <span class="com"># all arguments</span>
<span class="fn">echo</span> <span class="str">"Count: $#"</span>    <span class="com"># number of arguments</span></div>
    </div>
    <div class="concept-card">
      <div class="concept-label">CONDITIONALS & LOOPS</div>
      <div class="concept-title">If/Else and For in Bash</div>
      <div class="code-block"><span class="com">#!/bin/bash</span>
<span class="com"># If statement</span>
<span class="kw">if</span> [ -f <span class="str">"/etc/passwd"</span> ]; <span class="kw">then</span>
    <span class="fn">echo</span> <span class="str">"File exists"</span>
<span class="kw">elif</span> [ -d <span class="str">"/etc/passwd"</span> ]; <span class="kw">then</span>
    <span class="fn">echo</span> <span class="str">"It's a directory"</span>
<span class="kw">else</span>
    <span class="fn">echo</span> <span class="str">"Not found"</span>
<span class="kw">fi</span>

<span class="com"># For loop over a list</span>
<span class="kw">for</span> fruit <span class="kw">in</span> apple banana cherry; <span class="kw">do</span>
    <span class="fn">echo</span> <span class="str">"I like $fruit"</span>
<span class="kw">done</span>

<span class="com"># For loop over files</span>
<span class="kw">for</span> file <span class="kw">in</span> /var/log/*.log; <span class="kw">do</span>
    <span class="fn">echo</span> <span class="str">"Processing: $file"</span>
<span class="kw">done</span>

<span class="com"># While loop</span>
i=<span class="num">1</span>
<span class="kw">while</span> [ $i -le <span class="num">5</span> ]; <span class="kw">do</span>
    <span class="fn">echo</span> <span class="str">"Count: $i"</span>
    ((i++))
<span class="kw">done</span></div>
    </div>
    <div class="concept-card">
      <div class="concept-label">TEST OPERATORS</div>
      <div class="concept-title">Common [ ] Conditions</div>
      <table class="ai-table">
        <thead><tr><th>Test</th><th>Meaning</th></tr></thead>
        <tbody>
          <tr><td>[ -f file ]</td><td>File exists and is a regular file</td></tr>
          <tr><td>[ -d dir ]</td><td>Directory exists</td></tr>
          <tr><td>[ -z "$var" ]</td><td>String is empty</td></tr>
          <tr><td>[ -n "$var" ]</td><td>String is not empty</td></tr>
          <tr><td>[ "$a" = "$b" ]</td><td>Strings are equal</td></tr>
          <tr><td>[ $x -eq $y ]</td><td>Numbers are equal</td></tr>
          <tr><td>[ $x -gt $y ]</td><td>x is greater than y</td></tr>
          <tr><td>[ $x -lt $y ]</td><td>x is less than y</td></tr>
          <tr><td>[ ! condition ]</td><td>NOT (negate)</td></tr>
        </tbody>
      </table>
    </div>
    <div class="concept-card">
      <div class="concept-label">FUNCTIONS</div>
      <div class="concept-title">Reusable Blocks in Bash</div>
      <div class="code-block"><span class="com">#!/bin/bash</span>
<span class="com"># Define a function</span>
greet() {
    local name=<span class="str">"$1"</span>   <span class="com"># local vars don't leak</span>
    <span class="fn">echo</span> <span class="str">"Hello, $name!"</span>
}

<span class="com"># Function that returns a value via exit code</span>
is_root() {
    [ <span class="str">"$(id -u)"</span> -eq <span class="num">0</span> ]
}

greet <span class="str">"Alice"</span>
greet <span class="str">"Bob"</span>

<span class="kw">if</span> is_root; <span class="kw">then</span>
    <span class="fn">echo</span> <span class="str">"Running as root"</span>
<span class="kw">fi</span></div>
    </div>
  </div>
</div>

<!-- ── TOPIC: CRON JOBS — SCHEDULED TASKS ──────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">⏰</span>
    <span class="topic-name">Cron Jobs — Scheduling Tasks in Linux</span>
    <span class="topic-badge">LINUX • Ops</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">WHAT IS CRON</div>
      <div class="concept-title">Linux's Built-In Task Scheduler</div>
      <div class="concept-desc">Cron is a daemon (background service) that runs commands on a schedule. It reads configuration files called <strong>crontabs</strong> that list when and what to run. Use cases: backups, log rotation, report generation, health checks, certificate renewal.</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">CRONTAB SYNTAX</div>
      <div class="concept-title">Five Fields + Command</div>
      <div class="code-block"><span class="com"># Cron format:</span>
<span class="com"># ┌─── minute (0-59)</span>
<span class="com"># │ ┌─── hour (0-23)</span>
<span class="com"># │ │ ┌─── day of month (1-31)</span>
<span class="com"># │ │ │ ┌─── month (1-12)</span>
<span class="com"># │ │ │ │ ┌─── day of week (0-7, 0=Sun)</span>
<span class="com"># │ │ │ │ │</span>
  * * * * *  command_to_run

<span class="com"># Run backup every day at 2am</span>
<span class="num">0</span> <span class="num">2</span> * * *  /usr/local/bin/backup.sh

<span class="com"># Run every 15 minutes</span>
<span class="str">*/15</span> * * * *  /usr/local/bin/check.sh

<span class="com"># Run every Monday at 9am</span>
<span class="num">0</span> <span class="num">9</span> * * <span class="num">1</span>  /usr/local/bin/weekly-report.sh

<span class="com"># Run 1st of every month at midnight</span>
<span class="num">0</span> <span class="num">0</span> <span class="num">1</span> * *  /usr/local/bin/monthly-cleanup.sh</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">MANAGING CRONTABS</div>
      <div class="concept-title">crontab Commands</div>
      <div class="code-block"><span class="com"># Edit YOUR crontab (opens in default editor)</span>
crontab -e

<span class="com"># List your cron jobs</span>
crontab -l

<span class="com"># Remove all your cron jobs (dangerous!)</span>
crontab -r

<span class="com"># Edit another user's crontab (root only)</span>
crontab -u username -e

<span class="com"># System-wide cron directory (any executable file runs)</span>
ls /etc/cron.daily/
ls /etc/cron.weekly/
ls /etc/cron.monthly/</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">COMMON GOTCHAS</div>
      <div class="concept-title">Why Cron Jobs Silently Fail</div>
      <div class="concept-desc">• Cron uses a <strong>minimal environment</strong> — PATH is different from your login shell. Use absolute paths everywhere (<code>/usr/bin/python3</code> not just <code>python3</code>).<br>
      • <strong>Redirect output</strong> or you'll never see errors: <code>command &gt;&gt; /var/log/myjob.log 2&gt;&amp;1</code><br>
      • File permissions — the script must be executable: <code>chmod +x script.sh</code><br>
      • Use <code>crontab.guru</code> (online) to build and verify expressions before deploying.</div>
    </div>
  </div>
</div>

<!-- ── TOPIC: PROCESSES & SIGNALS ────────────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">⚙️</span>
    <span class="topic-name">Processes &amp; Signals — Running Programs in Linux</span>
    <span class="topic-badge">LINUX • Foundation</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">WHAT IS A PROCESS</div>
      <div class="concept-title">A Running Program with an ID</div>
      <div class="concept-desc">When you run a program, the kernel creates a <strong>process</strong> — an isolated execution environment with its own memory, file handles, and <strong>PID (Process ID)</strong>. The first process is <code>init</code> or <code>systemd</code> (PID 1). Every process has a parent.</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">VIEWING PROCESSES</div>
      <div class="concept-title">ps, top, htop</div>
      <div class="code-block"><span class="com"># Snapshot of all running processes</span>
ps aux

<span class="com"># Process tree (parent-child relationships)</span>
pstree

<span class="com"># Find a process by name</span>
pgrep nginx
ps aux | grep nginx

<span class="com"># Live process monitor (like Task Manager)</span>
top
htop      <span class="com"># nicer version, install with: apt install htop</span>

<span class="com"># See what a process has open</span>
lsof -p PID</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">SIGNALS</div>
      <div class="concept-title">Talking to Processes</div>
      <div class="concept-desc">Signals are messages sent to processes. The kernel or another process sends them; the receiving process handles (or ignores) them.</div>
      <table class="ai-table">
        <thead><tr><th>Signal</th><th>Number</th><th>Default Action</th><th>Common Use</th></tr></thead>
        <tbody>
          <tr><td>SIGTERM</td><td>15</td><td>Terminate</td><td>Polite kill — let process clean up</td></tr>
          <tr><td>SIGKILL</td><td>9</td><td>Kill immediately</td><td>Force kill — cannot be caught or ignored</td></tr>
          <tr><td>SIGHUP</td><td>1</td><td>Hang up</td><td>Reload config (nginx, sshd use this)</td></tr>
          <tr><td>SIGINT</td><td>2</td><td>Interrupt</td><td>What Ctrl+C sends</td></tr>
          <tr><td>SIGSTOP</td><td>19</td><td>Pause</td><td>What Ctrl+Z sends</td></tr>
          <tr><td>SIGCONT</td><td>18</td><td>Continue</td><td>Resume a paused process</td></tr>
        </tbody>
      </table>
      <div class="code-block"><span class="com"># Polite stop (give process time to clean up)</span>
kill -15 PID
kill PID      <span class="com"># same — SIGTERM is default</span>

<span class="com"># Force kill (last resort)</span>
kill -9 PID

<span class="com"># Kill all processes named "python3"</span>
pkill python3

<span class="com"># Reload nginx config without downtime</span>
kill -HUP $(pgrep nginx)</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">BACKGROUND & FOREGROUND</div>
      <div class="concept-title">Job Control</div>
      <div class="code-block"><span class="com"># Run in background from the start</span>
python3 server.py &amp;

<span class="com"># Ctrl+Z pauses a foreground process</span>
<span class="com"># bg resumes it in background</span>
bg %1

<span class="com"># fg brings background job to foreground</span>
fg %1

<span class="com"># List background jobs</span>
jobs

<span class="com"># Keep running after logout (nohup)</span>
nohup python3 server.py &gt; server.log 2&gt;&amp;1 &amp;</div>
    </div>
  </div>
</div>
"""

# ─────────────────────────────── LIFESTYLE wave 6 ────────────────────────────
LIFE_SENTINEL = "<!-- BEGINNER6-LIFE v1 -->"
LIFE_CONTENT = """
<!-- BEGINNER6-LIFE v1 -->
<!-- ── TOPIC: IMPOSTER SYNDROME ──────────────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">🪞</span>
    <span class="topic-name">Imposter Syndrome — You Belong Here</span>
    <span class="topic-badge">LIFESTYLE • Mindset</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">WHAT IT IS</div>
      <div class="concept-title">Feeling Like a Fraud Despite Evidence</div>
      <div class="concept-desc">Imposter syndrome is the persistent belief that you don't deserve your success — that you got lucky, that you're faking it, and that it's only a matter of time before people "find out." It affects ~70% of people at some point, including seasoned professionals. Knowing that doesn't make it feel less real.</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">WHY IT HITS TECH HARD</div>
      <div class="concept-title">The Field Is Enormous and Moves Fast</div>
      <div class="concept-desc">IT and cybersecurity are so wide that <strong>nobody knows everything</strong>. Senior engineers Google basics daily. People who look confident online are performing confidence. The Dunning-Kruger effect means beginners often feel most ignorant right when they're actually making the most progress — because they've learned enough to see how much they don't know.</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">REFRAME</div>
      <div class="concept-title">Evidence-Based Thinking</div>
      <div class="concept-desc">When the voice says "I don't belong here," ask: <em>What evidence would I need to believe I do belong?</em> Usually you already have it. List what you've actually learned. Compare yourself to where you were 3 months ago — not to experts who've had 10 years. You're not behind; you're at the beginning of a long journey.</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">PRACTICAL TACTICS</div>
      <div class="concept-title">Shrinking the Voice</div>
      <div class="concept-desc">• Keep a <strong>win log</strong> — write down one thing you figured out each day, no matter how small.<br>
      • <strong>Say "I don't know"</strong> openly. It builds more trust than faking expertise.<br>
      • Find community — Discord servers, Reddit (r/learnprogramming, r/sysadmin), local meetups. Everyone started somewhere.<br>
      • Teach something simple — explaining to others reveals and solidifies your real knowledge.<br>
      • Remember: being hired/accepted IS proof you were qualified. They wouldn't have chosen you otherwise.</div>
    </div>
  </div>
</div>

<!-- ── TOPIC: BURNOUT PREVENTION ──────────────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">🔋</span>
    <span class="topic-name">Burnout — Recognizing It Before It Breaks You</span>
    <span class="topic-badge">LIFESTYLE • Wellbeing</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">WHAT IS BURNOUT</div>
      <div class="concept-title">Chronic Stress Without Recovery</div>
      <div class="concept-desc">Burnout is not just being tired. It's a state of emotional, mental, and physical exhaustion caused by prolonged stress without adequate rest. In tech, it's epidemic — driven by "hustle culture," always-on expectations, and the pressure to constantly upskill. The WHO classifies it as an occupational phenomenon.</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">THREE DIMENSIONS</div>
      <div class="concept-title">Exhaustion · Cynicism · Inefficacy</div>
      <div class="concept-desc"><strong>Exhaustion</strong> — you've got nothing left; even starting feels overwhelming.<br>
      <strong>Cynicism</strong> — you stop caring; the work that used to excite you feels pointless.<br>
      <strong>Inefficacy</strong> — you feel like you can't do anything right, even things you used to nail.<br>
      Having one is a warning sign. Having all three means you need to stop and recover — not push harder.</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">EARLY WARNING SIGNS</div>
      <div class="concept-title">Catch It Before It Catches You</div>
      <div class="concept-desc">• Dreading work that used to be engaging<br>
      • Difficulty concentrating even on simple tasks<br>
      • Irritability over minor things<br>
      • Frequently sick (immune system gets hit)<br>
      • Social withdrawal<br>
      • "Keeping the lights on" mode — minimum output, no creativity<br>
      • Feeling detached from your own work</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">RECOVERY & PREVENTION</div>
      <div class="concept-title">You Can't Sprint a Marathon</div>
      <div class="concept-desc"><strong>Recovery</strong>: requires actual rest — not "scrolling-instead-of-working" rest, but real physical and cognitive recovery. Sleep, movement, social connection, and time away from screens.<br>
      <strong>Prevention</strong>: set hard stop times. Take your PTO. Protect weekends. Say no to optional overtime consistently. Learn to distinguish between urgency that's real vs. manufactured.<br>
      <strong>The sustainable pace</strong>: 40–45 focused hours/week consistently beats 70-hour crunch weeks followed by collapse.</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">WISDOM</div>
      <div class="concept-title">Sustainable &gt; Brilliant</div>
      <div class="concept-desc">The person who shows up every day at 80% capacity for years outperforms the person who sprints at 120% for six months and then quits or crashes. Longevity is a competitive advantage. Taking care of yourself <em>is</em> the job. No certification, no salary bump, no career milestone is worth your health.</div>
    </div>
  </div>
</div>

<!-- ── TOPIC: LEARNING HOW TO LEARN ──────────────────────── -->
<div class="topic">
  <div class="topic-header">
    <span class="topic-icon">🧠</span>
    <span class="topic-name">Learning How to Learn — Build the Skill Behind All Skills</span>
    <span class="topic-badge">LIFESTYLE • Foundation</span>
    <span class="topic-chevron">›</span>
  </div>
  <div class="topic-body">
    <div class="concept-card">
      <div class="concept-label">THE FORGETTING CURVE</div>
      <div class="concept-title">You Forget 90% If You Don't Review</div>
      <div class="concept-desc">Ebbinghaus (1885) showed that without review, humans forget ~40% of new material within 20 minutes, ~70% within a day, ~90% within a week. The cure isn't reading more — it's <strong>spaced repetition</strong>: review material at increasing intervals (1 day, 3 days, 1 week, 2 weeks, 1 month).</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">ACTIVE vs PASSIVE LEARNING</div>
      <div class="concept-title">Watching ≠ Knowing</div>
      <div class="concept-desc"><strong>Passive</strong>: watching a video tutorial, reading, highlighting. Feels like learning, but retention is low (~5-10%).<br>
      <strong>Active</strong>: writing code from scratch, teaching, explaining concepts aloud, doing practice questions, building projects. Retention climbs to 70-90%.<br>
      For every hour of video, spend two hours doing something with the material. The discomfort of struggle IS the learning.</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">FEYNMAN TECHNIQUE</div>
      <div class="concept-title">If You Can't Explain It Simply, You Don't Know It Yet</div>
      <div class="concept-desc">1. Pick a concept you're studying.<br>
      2. Explain it as if teaching a 12-year-old — no jargon allowed.<br>
      3. Where you stumble or grab for words → that's your gap.<br>
      4. Go back and study only that gap.<br>
      5. Repeat until the explanation is smooth.<br>
      This technique cuts through the illusion of familiarity ("I've seen this 10 times" ≠ "I understand it").</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">DELIBERATE PRACTICE</div>
      <div class="concept-title">Push the Edge, Get Feedback, Adjust</div>
      <div class="concept-desc">Random repetition doesn't produce mastery. <strong>Deliberate practice</strong> does:<br>
      • Work at the edge of your ability — if it's easy, it's review, not growth<br>
      • Get immediate, accurate feedback (run the code; take the quiz)<br>
      • Focus on weaknesses, not strengths<br>
      • Rest and consolidate — sleep is when the brain cements learning</div>
    </div>
    <div class="concept-card">
      <div class="concept-label">COMPOUNDING KNOWLEDGE</div>
      <div class="concept-title">Small Daily Gains Add Up Exponentially</div>
      <div class="concept-desc">1% better every day for a year = 37× improvement (1.01^365 ≈ 37.8). The hard part is that the gains are invisible at first. The graph looks flat for months, then curves sharply upward. Most people quit in the flat zone. Don't compare your chapter 3 to someone else's chapter 20. Stack small wins daily, stay consistent, trust the process.</div>
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
        patch(target, SCRIPT_SENTINEL, SCRIPT_CONTENT, SCRIPT_INJECT_ANCHOR),
        patch(target, NET_SENTINEL,    NET_CONTENT,    NET_INJECT_ANCHOR),
        patch(target, SEC_SENTINEL,    SEC_CONTENT,    SEC_INJECT_ANCHOR),
        patch(target, LINUX_SENTINEL,  LINUX_CONTENT,  LINUX_INJECT_ANCHOR),
        patch(target, LIFE_SENTINEL,   LIFE_CONTENT,   LIFE_INJECT_ANCHOR),
    ]

    if any(results):
        # Validate HTML balance
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
