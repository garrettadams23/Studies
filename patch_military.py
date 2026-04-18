#!/usr/bin/env python3
"""
patch_military.py — Injects the Military Staff Codes domain.

Targets: index.html  (filter chip + full domain section)
         style.css   (accent colour + chip class)

Usage:  python3 patch_military.py
Idempotent: skips already-patched files.
"""
import sys

SENTINEL = 'data-domain="military"'

# ── CHIP ─────────────────────────────────────────────────────────────────────
# Placed after the LIFESTYLE chip (or after SHORTCUTS chip if lifestyle not yet added)

CHIP_ANCHOR = '        <!-- theme + expand moved to header -->'

CHIP_HTML = '''        <!-- theme + expand moved to header -->
        <div class="chip c-military" onclick="filter(\'military\', this)">
          🎖️ MILITARY CODES
        </div>'''

# ── DOMAIN SECTION ────────────────────────────────────────────────────────────
DOMAIN_ANCHOR = '    </div>\n    <!-- /container -->'

DOMAIN_HTML = '''
      <!-- ══════════════════════════════════════════════════════════════════
           DOMAIN: MILITARY STAFF CODES
           Topics: Prefix Letters · Functional Numbers · Sub-designators
                   Branch Comparison · Common Examples
      ══════════════════════════════════════════════════════════════════════ -->
      <div class="domain-section domain-military" data-domain="military">
        <div class="domain-header" onclick="toggleDomain(this)">
          <span class="domain-icon">🎖️</span>
          <span class="domain-title">Military Staff Codes</span>
          <div class="cert-tags">
            <span class="ctag ctag-military">MIL</span>
          </div>
          <span class="domain-sub">J · G · S · N · A · C · M — Functional Numbers 1–9 · Sub-designators · Branch Comparison</span>
          <span class="chevron">▾</span>
        </div>
        <div class="domain-body">

          <!-- ── TOPIC: HOW THE SYSTEM WORKS ──────────────────────────── -->
          <div class="topic">
            <div class="topic-header" onclick="toggleTopic(this)">
              <span class="topic-icon">📐</span>
              <span class="topic-name">How Staff Codes Work — Letter + Number + Sub</span>
              <span class="topic-badge">SYSTEM OVERVIEW</span>
              <span class="topic-chev">▶</span>
            </div>
            <div class="topic-body">
              <div class="concept-card">
                <div class="concept-label">Structure</div>
                <div class="concept-title">Decoding Any Staff Designator</div>
                <div class="concept-desc">
                  Military staff designators follow a consistent three-part formula.
                  <strong style="color:var(--amber)">Letter</strong> = which organization/level this staff belongs to.
                  <strong style="color:var(--cyan)">First number</strong> = the functional area (what they do).
                  <strong style="color:var(--green)">Second number (optional)</strong> = the branch or sub-section within that function.
                </div>
                <div class="dw">
                  <div class="dt">▸ ANATOMY OF A STAFF CODE</div>
                  <div style="display:flex;align-items:stretch;gap:0;margin-bottom:18px;flex-wrap:wrap;gap:6px">
                    <div style="flex:1;min-width:120px;background:rgba(255,176,32,.08);border:2px solid rgba(255,176,32,.4);border-radius:6px;padding:16px;text-align:center">
                      <div style="font-family:var(--mono);font-size:36px;font-weight:700;color:var(--amber)">J</div>
                      <div style="font-size:12px;font-weight:700;color:var(--amber);margin-top:4px">PREFIX LETTER</div>
                      <div style="font-size:11px;color:var(--muted);margin-top:4px">Org level &amp; branch<br>J=Joint, G=Army Div,<br>S=Battalion, N=Navy…</div>
                    </div>
                    <div style="display:flex;align-items:center;font-size:24px;color:var(--muted);padding:0 4px">+</div>
                    <div style="flex:1;min-width:120px;background:rgba(0,212,255,.08);border:2px solid rgba(0,212,255,.4);border-radius:6px;padding:16px;text-align:center">
                      <div style="font-family:var(--mono);font-size:36px;font-weight:700;color:var(--cyan)">6</div>
                      <div style="font-size:12px;font-weight:700;color:var(--cyan);margin-top:4px">FUNCTIONAL NUMBER</div>
                      <div style="font-size:11px;color:var(--muted);margin-top:4px">What they do<br>1=Personnel, 2=Intel,<br>3=Ops, 4=Logistics…</div>
                    </div>
                    <div style="display:flex;align-items:center;font-size:24px;color:var(--muted);padding:0 4px">+</div>
                    <div style="flex:1;min-width:120px;background:rgba(0,255,153,.08);border:2px solid rgba(0,255,153,.4);border-radius:6px;padding:16px;text-align:center">
                      <div style="font-family:var(--mono);font-size:36px;font-weight:700;color:var(--green)">3</div>
                      <div style="font-size:12px;font-weight:700;color:var(--green);margin-top:4px">SUB-DESIGNATOR</div>
                      <div style="font-size:11px;color:var(--muted);margin-top:4px">Branch within function<br>3=Operations branch<br>(optional, used in larger HQs)</div>
                    </div>
                  </div>
                  <div class="info-bar" style="background:rgba(255,176,32,.05);border:1px solid rgba(255,176,32,.2);margin-bottom:14px">
                    <strong style="color:var(--amber)">J63</strong> decoded:
                    <strong style="color:var(--amber)">J</strong> = Joint command ·
                    <strong style="color:var(--cyan)">6</strong> = Communications &amp; IT directorate ·
                    <strong style="color:var(--green)">3</strong> = Operations branch within that directorate.<br>
                    <span style="font-size:11px;color:var(--muted)">= The section that runs day-to-day network and communications operations for a joint command.</span>
                  </div>
                  <div class="info-bar" style="background:rgba(0,212,255,.05);border:1px solid rgba(0,212,255,.2)">
                    <strong style="color:var(--cyan)">S4</strong> decoded:
                    <strong style="color:var(--amber)">S</strong> = Staff (battalion/brigade level) ·
                    <strong style="color:var(--cyan)">4</strong> = Logistics &amp; Supply.<br>
                    <span style="font-size:11px;color:var(--muted)">= The logistics officer at a battalion — responsible for supply, maintenance, and equipment for that unit.</span>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <!-- ── TOPIC: PREFIX LETTERS ─────────────────────────────────── -->
          <div class="topic">
            <div class="topic-header" onclick="toggleTopic(this)">
              <span class="topic-icon">🔤</span>
              <span class="topic-name">Prefix Letters — J · G · S · N · A · C · M · F</span>
              <span class="topic-badge">ALL PREFIXES</span>
              <span class="topic-chev">▶</span>
            </div>
            <div class="topic-body">
              <div class="concept-card">
                <div class="concept-label">Reference — All Major Prefixes</div>
                <div class="concept-title">Organization Level &amp; Service Branch Designators</div>
                <div class="concept-desc">
                  The prefix letter indicates <strong style="color:var(--amber)">which command level and which military service</strong>
                  the staff section belongs to. The same number (e.g., 3 = Operations) means the same function regardless of letter prefix.
                </div>
                <div class="dw">
                  <table class="ref-table">
                    <tr>
                      <th>Prefix</th>
                      <th>Stands For</th>
                      <th>Used By / Level</th>
                      <th>Example Commands</th>
                      <th>Numbers Used</th>
                    </tr>
                    <tr>
                      <td style="color:var(--cyan);font-size:20px;font-family:var(--mono);font-weight:700">J</td>
                      <td><strong>Joint</strong></td>
                      <td>Unified &amp; combatant commands with two or more service branches</td>
                      <td>CENTCOM, INDOPACOM, SOCOM, DIA, CJCS, USFK, NATO HQ</td>
                      <td>J1–J9</td>
                    </tr>
                    <tr>
                      <td style="color:var(--green);font-size:20px;font-family:var(--mono);font-weight:700">G</td>
                      <td><strong>General Staff</strong></td>
                      <td>Army divisions, corps, and above (General Officer-led commands)</td>
                      <td>82nd Airborne HQ, 1st Cav HQ, Army corps HQs</td>
                      <td>G1–G9</td>
                    </tr>
                    <tr>
                      <td style="color:var(--amber);font-size:20px;font-family:var(--mono);font-weight:700">S</td>
                      <td><strong>Staff</strong></td>
                      <td>Army &amp; Marine Corps at battalion and brigade level (below division)</td>
                      <td>1-8 Infantry Bn, 2d Marines Regt, Brigade Combat Teams</td>
                      <td>S1–S6 (S7–S9 uncommon)</td>
                    </tr>
                    <tr>
                      <td style="color:var(--red);font-size:20px;font-family:var(--mono);font-weight:700">N</td>
                      <td><strong>Navy</strong></td>
                      <td>Navy headquarters, fleet commands, and naval installations</td>
                      <td>CNO staff, NAVAIR, NAVSEA, Fleet Forces Command</td>
                      <td>N1–N9</td>
                    </tr>
                    <tr>
                      <td style="color:var(--purple);font-size:20px;font-family:var(--mono);font-weight:700">A</td>
                      <td><strong>Air Force</strong></td>
                      <td>HAF (Headquarters Air Force) and major command (MAJCOM) staff</td>
                      <td>HAF, ACC, AMC, AFSOC, PACAF, USAFE</td>
                      <td>A1–A10</td>
                    </tr>
                    <tr>
                      <td style="color:var(--purple);font-size:20px;font-family:var(--mono);font-weight:700">AF</td>
                      <td><strong>Air Force (alt form)</strong></td>
                      <td>Used in some Air Force numbered air force HQs and wing-level staff for formal documents</td>
                      <td>1st Air Force, 12th Air Force</td>
                      <td>Same as A-series</td>
                    </tr>
                    <tr>
                      <td style="color:#38bdf8;font-size:20px;font-family:var(--mono);font-weight:700">M</td>
                      <td><strong>Marine Corps</strong></td>
                      <td>Marine Expeditionary Force (MEF) and Marine division level</td>
                      <td>I MEF, II MEF, III MEF, MARFORPAC</td>
                      <td>M1–M9 (MEF uses G at div, S at bn)</td>
                    </tr>
                    <tr>
                      <td style="color:#fb923c;font-size:20px;font-family:var(--mono);font-weight:700">C</td>
                      <td><strong>Combined</strong></td>
                      <td>Multinational/coalition commands where two or more nations operate together</td>
                      <td>Combined Forces Command Korea, NATO Allied Command Ops</td>
                      <td>C1–C9</td>
                    </tr>
                    <tr>
                      <td style="color:#f472b6;font-size:20px;font-family:var(--mono);font-weight:700">F</td>
                      <td><strong>Fleet / Force</strong></td>
                      <td>Navy fleet-level commands; also used for some Air Force force-level designations</td>
                      <td>3rd Fleet, 7th Fleet, U.S. Fleet Forces Command</td>
                      <td>F1–F9</td>
                    </tr>
                    <tr>
                      <td style="color:var(--muted);font-size:20px;font-family:var(--mono);font-weight:700">CG</td>
                      <td><strong>Coast Guard</strong></td>
                      <td>U.S. Coast Guard headquarters and district commands</td>
                      <td>COMDT staff, Coast Guard districts</td>
                      <td>CG-1 through CG-9</td>
                    </tr>
                  </table>
                  <div class="info-bar ib-muted" style="margin-top:12px;font-size:11.5px">
                    ⓘ <strong style="color:var(--text)">Combined vs Joint:</strong>
                    <strong style="color:var(--amber)">Joint (J)</strong> = multiple US military services working together.
                    <strong style="color:var(--cyan)">Combined (C)</strong> = multiple nations working together.
                    A command can be both — e.g., Combined Joint Task Force = multinational + multi-service.
                  </div>
                </div>
              </div>
            </div>
          </div>

          <!-- ── TOPIC: FUNCTIONAL NUMBERS 1–9 ────────────────────────── -->
          <div class="topic">
            <div class="topic-header" onclick="toggleTopic(this)">
              <span class="topic-icon">🔢</span>
              <span class="topic-name">Functional Numbers 1 through 9 — What Each Number Means</span>
              <span class="topic-badge">ALL NUMBERS</span>
              <span class="topic-chev">▶</span>
            </div>
            <div class="topic-body">
              <div class="concept-card">
                <div class="concept-label">Reference — Universal Functional Areas</div>
                <div class="concept-title">Numbers are consistent across ALL prefix letters</div>
                <div class="concept-desc">
                  Regardless of whether the prefix is J, G, S, N, or A — the number always means the same functional area.
                  A <strong style="color:var(--cyan)">J3</strong> and an <strong style="color:var(--amber)">S3</strong> both handle Operations — just at different command levels.
                </div>
                <div class="dw">
                  <div class="kc-row row-cyan" style="margin-bottom:6px">
                    <div class="kc-num text-cyan" style="font-size:22px;font-family:var(--mono);width:36px">1</div>
                    <div class="kc-phase" style="min-width:220px">Manpower &amp; Personnel</div>
                    <div class="kc-desc">Human resources, strength reporting, assignments, promotions, awards, disciplinary actions, casualty reporting, morale and welfare. The "HR department" of a military headquarters. <span style="color:var(--cyan)">J1 · G1 · S1 · N1 · A1</span></div>
                  </div>
                  <div class="kc-row row-red" style="margin-bottom:6px">
                    <div class="kc-num text-red" style="font-size:22px;font-family:var(--mono);width:36px">2</div>
                    <div class="kc-phase" style="min-width:220px">Intelligence</div>
                    <div class="kc-desc">All-source intelligence: HUMINT, SIGINT, GEOINT, OSINT, MASINT. Threat assessments, enemy order of battle, ISR (Intelligence, Surveillance, Reconnaissance), targeting. <span style="color:var(--cyan)">J2 · G2 · S2 · N2 · A2</span></div>
                  </div>
                  <div class="kc-row row-amber" style="margin-bottom:6px">
                    <div class="kc-num text-amber" style="font-size:22px;font-family:var(--mono);width:36px">3</div>
                    <div class="kc-phase" style="min-width:220px">Operations</div>
                    <div class="kc-desc">Current and ongoing operations — the main effort of any HQ. Battle rhythm, OPORD execution, fires coordination, battle tracking, exercises, and training management. The largest and busiest staff section. <span style="color:var(--cyan)">J3 · G3 · S3 · N3 · A3</span></div>
                  </div>
                  <div class="kc-row row-green" style="margin-bottom:6px">
                    <div class="kc-num text-green" style="font-size:22px;font-family:var(--mono);width:36px">4</div>
                    <div class="kc-phase" style="min-width:220px">Logistics &amp; Supply</div>
                    <div class="kc-desc">Sustainment: supply (Class I–IX), maintenance, transportation, field services, mortuary affairs, contracting. Ensures the force has what it needs to fight and survive. <span style="color:var(--cyan)">J4 · G4 · S4 · N4 · A4</span></div>
                  </div>
                  <div class="kc-row row-purple" style="margin-bottom:6px">
                    <div class="kc-num text-purple" style="font-size:22px;font-family:var(--mono);width:36px">5</div>
                    <div class="kc-phase" style="min-width:220px">Plans &amp; Strategy</div>
                    <div class="kc-desc">Future operations planning — from 96 hours out through long-range strategy. Operational plans (OPLANs), concept development, war gaming, campaign design, interagency coordination. Distinct from J3 (current ops). <span style="color:var(--cyan)">J5 · G5 · S5 · N5 · A5</span></div>
                  </div>
                  <div class="kc-row row-blue" style="margin-bottom:6px">
                    <div class="kc-num text-blue" style="font-size:22px;font-family:var(--mono);width:36px">6</div>
                    <div class="kc-phase" style="min-width:220px">Communications, Signal &amp; IT</div>
                    <div class="kc-desc">All networks, radios, satellite comms, data links, IT infrastructure, cybersecurity, COMSEC (communications security), and information management. The military's IT department. <span style="color:var(--cyan)">J6 · G6 · S6 · N6 · A6</span></div>
                  </div>
                  <div class="kc-row" style="border-color:rgba(251,146,60,.5);background:rgba(251,146,60,.05);margin-bottom:6px">
                    <div class="kc-num" style="color:#fb923c;font-size:22px;font-family:var(--mono);width:36px">7</div>
                    <div class="kc-phase" style="min-width:220px;color:#fb923c">Training &amp; Force Development</div>
                    <div class="kc-desc">Exercise planning, readiness reporting, individual and collective training programs, force generation, leader development. Air Force A7 = installations &amp; mission support. Usage varies by branch. <span style="color:var(--cyan)">J7 · G7 · A7</span></div>
                  </div>
                  <div class="kc-row" style="border-color:rgba(244,114,182,.5);background:rgba(244,114,182,.05);margin-bottom:6px">
                    <div class="kc-num" style="color:#f472b6;font-size:22px;font-family:var(--mono);width:36px">8</div>
                    <div class="kc-phase" style="min-width:220px;color:#f472b6">Financial Management &amp; Resources</div>
                    <div class="kc-desc">Budgeting, resource allocation, comptroller functions, program objective memoranda (POM), contracts oversight, cost analysis, financial reporting to higher commands. <span style="color:var(--cyan)">J8 · G8 · N8 · A8</span></div>
                  </div>
                  <div class="kc-row" style="border-color:rgba(132,204,22,.5);background:rgba(132,204,22,.05)">
                    <div class="kc-num" style="color:#84cc16;font-size:22px;font-family:var(--mono);width:36px">9</div>
                    <div class="kc-phase" style="min-width:220px;color:#84cc16">Civil Affairs &amp; Interagency</div>
                    <div class="kc-desc">Civil-military operations, host-nation relations, NGO/IGO coordination, reconstruction, PSYOP (Psychological Operations) coordination, USAID partnerships, governance support in conflict zones. <span style="color:var(--cyan)">J9 · G9 · S9 · A9</span></div>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <!-- ── TOPIC: SUB-DESIGNATORS ────────────────────────────────── -->
          <div class="topic">
            <div class="topic-header" onclick="toggleTopic(this)">
              <span class="topic-icon">🔭</span>
              <span class="topic-name">Sub-Designators — The Third Digit (e.g., J63)</span>
              <span class="topic-badge">BRANCH LEVEL</span>
              <span class="topic-chev">▶</span>
            </div>
            <div class="topic-body">
              <div class="concept-card">
                <div class="concept-label">Reference — Sub-Sections Within Directorates</div>
                <div class="concept-title">Third Digit = Branch Within the Functional Directorate</div>
                <div class="concept-desc">
                  Large headquarters (combatant commands, service HQs) further divide each directorate into branches.
                  The third digit follows the same 1–9 logic: <strong style="color:var(--amber)">1=Manpower, 2=Intel, 3=Ops, 4=Logistics</strong> within that function.
                  Smaller units (battalions, brigades) rarely use sub-designators.
                </div>
                <div class="dw">
                  <div class="dt">▸ UNIVERSAL SUB-DESIGNATOR LOGIC</div>
                  <table class="ref-table" style="margin-bottom:18px">
                    <tr><th>Sub #</th><th>Function Within the Directorate</th><th>Example in J6</th></tr>
                    <tr><td style="color:var(--cyan)">X1</td><td>Manpower &amp; Personnel within that function — staffing, billets, HR for the directorate</td><td>J61 — J6 manpower &amp; workforce management</td></tr>
                    <tr><td style="color:var(--cyan)">X2</td><td>Requirements, Architecture &amp; Assessment — needs analysis, doctrine, policy</td><td>J62 — Network architecture &amp; requirements</td></tr>
                    <tr><td style="color:var(--cyan)">X3</td><td>Operations — day-to-day execution, current operational support</td><td>J63 — Network operations &amp; comms ops center</td></tr>
                    <tr><td style="color:var(--cyan)">X4</td><td>Logistics, Resources &amp; Programs — budget, contracts, sustainment of the function</td><td>J64 — IT programs, resource management</td></tr>
                    <tr><td style="color:var(--cyan)">X5</td><td>Plans &amp; Strategy — future development, long-range planning within the function</td><td>J65 — Comms policy &amp; interoperability plans</td></tr>
                    <tr><td style="color:var(--cyan)">X6</td><td>Communications within the function — less common at sub-level</td><td>J66 — COMSEC &amp; crypto management</td></tr>
                    <tr><td style="color:var(--cyan)">X7</td><td>Training &amp; Exercises within the function</td><td>J67 — Comms training &amp; exercise support</td></tr>
                    <tr><td style="color:var(--cyan)">X8</td><td>Financial management specific to the function</td><td>J68 — IT budget &amp; acquisition oversight</td></tr>
                    <tr><td style="color:var(--cyan)">X9</td><td>Interagency / special programs within the function</td><td>J69 — Coalition network integration</td></tr>
                  </table>
                  <div class="dt">▸ COMMON SUB-DESIGNATOR EXAMPLES ACROSS PREFIXES</div>
                  <table class="ref-table">
                    <tr><th>Code</th><th>Full Meaning</th><th>What They Do</th></tr>
                    <tr><td style="color:var(--amber)">J21</td><td>Joint Intelligence — Manpower/Personnel</td><td>Manages intelligence staffing, billets, and clearance processing at joint commands</td></tr>
                    <tr><td style="color:var(--amber)">J22</td><td>Joint Intelligence — Production</td><td>Produces all-source intelligence assessments, threat reports, and finished intelligence</td></tr>
                    <tr><td style="color:var(--amber)">J23</td><td>Joint Intelligence — Operations</td><td>Runs the Joint Intelligence Support Element (JISE), 24/7 intelligence battle tracking</td></tr>
                    <tr><td style="color:var(--amber)">J33</td><td>Joint Operations — Current Ops</td><td>The battle watch; monitors ongoing missions and executes the commander's current orders</td></tr>
                    <tr><td style="color:var(--amber)">J35</td><td>Joint Operations — Future Ops</td><td>Plans operations 24–96 hours out; bridges J3 (current) and J5 (future)</td></tr>
                    <tr><td style="color:var(--amber)">J39</td><td>Joint Operations — Info Operations</td><td>IO, PSYOP, MISO, deception operations coordination</td></tr>
                    <tr><td style="color:var(--amber)">J51</td><td>Joint Plans — Strategy</td><td>Grand strategy, theater campaign plan development</td></tr>
                    <tr><td style="color:var(--amber)">J52</td><td>Joint Plans — Assessments</td><td>Campaign assessments, measures of effectiveness (MOE)</td></tr>
                    <tr><td style="color:var(--amber)">J53</td><td>Joint Plans — Operational Plans</td><td>Writes OPLANs, CONPLANs, functional plans</td></tr>
                    <tr><td style="color:var(--amber)">J61</td><td>Joint Comms — Workforce</td><td>Communications directorate manpower, billet management</td></tr>
                    <tr><td style="color:var(--amber)">J62</td><td>Joint Comms — Architecture</td><td>Network design, requirements, standards, policy</td></tr>
                    <tr><td style="color:var(--amber)">J63</td><td>Joint Comms — <strong>Operations</strong></td><td>Runs the Network Operations Center (NOC); manages live comms/data networks; most visible J6 element</td></tr>
                    <tr><td style="color:var(--amber)">J64</td><td>Joint Comms — Programs &amp; Resources</td><td>IT acquisition, budget, contracts for comm systems</td></tr>
                    <tr><td style="color:var(--amber)">J65</td><td>Joint Comms — Policy &amp; Interoperability</td><td>Coalition network standards, info-sharing policies</td></tr>
                  </table>
                </div>
              </div>
            </div>
          </div>

          <!-- ── TOPIC: BRANCH-BY-BRANCH COMPARISON ───────────────────── -->
          <div class="topic">
            <div class="topic-header" onclick="toggleTopic(this)">
              <span class="topic-icon">⚖️</span>
              <span class="topic-name">Branch Comparison — Same Number, Different Context</span>
              <span class="topic-badge">SIDE-BY-SIDE</span>
              <span class="topic-chev">▶</span>
            </div>
            <div class="topic-body">
              <div class="concept-card">
                <div class="concept-label">Cross-Branch Reference</div>
                <div class="concept-title">How Each Branch Uses the Same Numbers Differently</div>
                <div class="concept-desc">
                  The number means the same function, but the <strong style="color:var(--amber)">scope, size, and tools</strong> differ dramatically between
                  a battalion S-section and a combatant command J-directorate.
                </div>
                <div class="dw">
                  <div class="dt">▸ FUNCTION 1 — PERSONNEL</div>
                  <table class="ref-table" style="margin-bottom:14px">
                    <tr><th>Code</th><th>Level</th><th>Focus &amp; Scope</th></tr>
                    <tr><td style="color:var(--cyan)">S1</td><td>Battalion (400–1000 personnel)</td><td>Leave requests, promotions, awards, strength reports, casualty notification for the battalion. Usually 2–4 people.</td></tr>
                    <tr><td style="color:var(--cyan)">G1</td><td>Division (10,000–20,000 personnel)</td><td>Same functions but manages policy across multiple brigades. Interfaces with Army HRC (Human Resources Command).</td></tr>
                    <tr><td style="color:var(--cyan)">J1</td><td>Combatant Command (multi-service, global)</td><td>Manages manpower for all services assigned to the command; joint manning documents; handles inter-service personnel policy conflicts.</td></tr>
                    <tr><td style="color:var(--cyan)">N1</td><td>Navy HQ</td><td>Total force management for all Navy personnel: recruiting, retention, career development, diversity programs.</td></tr>
                    <tr><td style="color:var(--cyan)">A1</td><td>Headquarters Air Force</td><td>Manpower &amp; personnel for the entire Air Force: force structure decisions, officer/enlisted development, Air Force Personnel Center (AFPC) oversight.</td></tr>
                  </table>
                  <div class="dt">▸ FUNCTION 3 — OPERATIONS (THE MAIN EFFORT)</div>
                  <table class="ref-table" style="margin-bottom:14px">
                    <tr><th>Code</th><th>Level</th><th>Focus &amp; Scope</th></tr>
                    <tr><td style="color:var(--amber)">S3</td><td>Battalion</td><td>Plans and supervises all battalion training and combat operations. Runs the battalion Tactical Operations Center (TOC). Usually a Major.</td></tr>
                    <tr><td style="color:var(--amber)">G3</td><td>Division</td><td>Synchronizes maneuver, fires, aviation, and combat support across the division. Manages the Division Main CP battle rhythm.</td></tr>
                    <tr><td style="color:var(--amber)">J3</td><td>Combatant Command</td><td>Executes the commander's operational concept across all services globally. Runs the 24/7 Joint Operations Center (JOC). Often a 2-star billet.</td></tr>
                    <tr><td style="color:var(--amber)">N3</td><td>Navy Fleet</td><td>Fleet operational employment; ship deployment scheduling; current fleet operations and readiness.</td></tr>
                    <tr><td style="color:var(--amber)">A3</td><td>Air Force</td><td>Largest Air Force staff directorate. Oversees air operations, flying hour programs, readiness, and airpower employment globally.</td></tr>
                  </table>
                  <div class="dt">▸ FUNCTION 6 — COMMUNICATIONS &amp; IT</div>
                  <table class="ref-table">
                    <tr><th>Code</th><th>Level</th><th>Focus &amp; Scope</th></tr>
                    <tr><td style="color:var(--green)">S6</td><td>Battalion</td><td>Maintains radios (SINCGARS, SOCOM radios), tactical comms, NIPR/SIPR terminal at battalion level. Often a Warrant Officer or Captain.</td></tr>
                    <tr><td style="color:var(--green)">G6</td><td>Division</td><td>Division network (Tactical LAN), frequency management, satellite terminals, Signal Battalion oversight.</td></tr>
                    <tr><td style="color:var(--green)">J6</td><td>Combatant Command</td><td>Enterprise-level network operations. Manages the Joint Information Environment (JIE); classified and unclassified networks; cyber integration with USCYBERCOM.</td></tr>
                    <tr><td style="color:var(--green)">N6</td><td>Navy</td><td>Navy enterprise networks (NMCI/ONE-Net), shipboard comms systems, spectrum management, Navy COMSEC program.</td></tr>
                    <tr><td style="color:var(--green)">A6</td><td>Air Force</td><td>AFNET, Air Force IT infrastructure, C2 systems, spectrum, cyberspace capabilities integration into air operations.</td></tr>
                  </table>
                </div>
              </div>
            </div>
          </div>

          <!-- ── TOPIC: QUICK REFERENCE TABLE ─────────────────────────── -->
          <div class="topic">
            <div class="topic-header" onclick="toggleTopic(this)">
              <span class="topic-icon">📋</span>
              <span class="topic-name">Quick Reference — Full Cross-Matrix</span>
              <span class="topic-badge">CHEAT SHEET</span>
              <span class="topic-chev">▶</span>
            </div>
            <div class="topic-body">
              <div class="concept-card">
                <div class="concept-label">At-a-Glance Matrix</div>
                <div class="concept-title">All Prefixes × All Numbers</div>
                <div class="dw">
                  <table class="ref-table">
                    <tr>
                      <th>Number</th>
                      <th>Function</th>
                      <th style="color:var(--cyan)">J (Joint)</th>
                      <th style="color:var(--green)">G (Army Div+)</th>
                      <th style="color:var(--amber)">S (Bn/Bde)</th>
                      <th style="color:var(--red)">N (Navy)</th>
                      <th style="color:var(--purple)">A (Air Force)</th>
                      <th style="color:#38bdf8">C (Combined)</th>
                    </tr>
                    <tr>
                      <td style="font-family:var(--mono);font-weight:700;font-size:15px;color:var(--text)">1</td>
                      <td><strong>Personnel &amp; Manpower</strong></td>
                      <td>J1</td><td>G1</td><td>S1</td><td>N1</td><td>A1</td><td>C1</td>
                    </tr>
                    <tr>
                      <td style="font-family:var(--mono);font-weight:700;font-size:15px;color:var(--text)">2</td>
                      <td><strong>Intelligence</strong></td>
                      <td>J2</td><td>G2</td><td>S2</td><td>N2</td><td>A2</td><td>C2</td>
                    </tr>
                    <tr>
                      <td style="font-family:var(--mono);font-weight:700;font-size:15px;color:var(--text)">3</td>
                      <td><strong>Operations</strong></td>
                      <td>J3</td><td>G3</td><td>S3</td><td>N3</td><td>A3</td><td>C3</td>
                    </tr>
                    <tr>
                      <td style="font-family:var(--mono);font-weight:700;font-size:15px;color:var(--text)">4</td>
                      <td><strong>Logistics</strong></td>
                      <td>J4</td><td>G4</td><td>S4</td><td>N4</td><td>A4</td><td>C4</td>
                    </tr>
                    <tr>
                      <td style="font-family:var(--mono);font-weight:700;font-size:15px;color:var(--text)">5</td>
                      <td><strong>Plans &amp; Strategy</strong></td>
                      <td>J5</td><td>G5</td><td>S5</td><td>N5</td><td>A5</td><td>C5</td>
                    </tr>
                    <tr>
                      <td style="font-family:var(--mono);font-weight:700;font-size:15px;color:var(--text)">6</td>
                      <td><strong>Communications &amp; IT</strong></td>
                      <td>J6</td><td>G6</td><td>S6</td><td>N6</td><td>A6</td><td>C6</td>
                    </tr>
                    <tr>
                      <td style="font-family:var(--mono);font-weight:700;font-size:15px;color:var(--text)">7</td>
                      <td><strong>Training / Force Dev</strong></td>
                      <td>J7</td><td>G7</td><td style="color:var(--muted)">(rare)</td><td>N7</td><td>A7*</td><td>C7</td>
                    </tr>
                    <tr>
                      <td style="font-family:var(--mono);font-weight:700;font-size:15px;color:var(--text)">8</td>
                      <td><strong>Financial Mgmt</strong></td>
                      <td>J8</td><td>G8</td><td style="color:var(--muted)">(rare)</td><td>N8</td><td>A8</td><td>C8</td>
                    </tr>
                    <tr>
                      <td style="font-family:var(--mono);font-weight:700;font-size:15px;color:var(--text)">9</td>
                      <td><strong>Civil Affairs / Interagency</strong></td>
                      <td>J9</td><td>G9</td><td>S9</td><td>N9</td><td>A9</td><td>C9</td>
                    </tr>
                    <tr>
                      <td style="font-family:var(--mono);font-weight:700;font-size:15px;color:var(--muted)">10</td>
                      <td style="color:var(--muted)">Installations (AF only)</td>
                      <td style="color:var(--muted)">—</td><td style="color:var(--muted)">—</td><td style="color:var(--muted)">—</td><td style="color:var(--muted)">—</td><td style="color:var(--purple)">A10</td><td style="color:var(--muted)">—</td>
                    </tr>
                  </table>
                  <div class="info-bar ib-muted" style="margin-top:10px;font-size:11.5px">
                    * <strong style="color:var(--purple)">A7</strong> (Air Force) = Installations &amp; Mission Support — differs from the Army/Joint usage of 7 as Training.
                    <strong style="color:var(--purple)">A10</strong> = Air Force Installations unique to HAF structure.
                    S7–S9 are rarely staffed at battalion level; those functions roll up to brigade or higher.
                  </div>
                  <div class="dt" style="margin-top:16px">▸ SUPPLY CLASS CODES (companion reference for S4/G4/J4)</div>
                  <table class="ref-table">
                    <tr><th>Class</th><th>Supply Category</th><th>Examples</th></tr>
                    <tr><td style="color:var(--cyan)">Class I</td><td>Subsistence (food &amp; water)</td><td>MREs, bulk food, bottled water, rations</td></tr>
                    <tr><td style="color:var(--cyan)">Class II</td><td>Clothing &amp; individual equipment</td><td>Uniforms, boots, helmets, body armor</td></tr>
                    <tr><td style="color:var(--cyan)">Class III</td><td>Petroleum, oils, lubricants (POL)</td><td>JP-8 jet fuel (IIIB), diesel, motor oil</td></tr>
                    <tr><td style="color:var(--cyan)">Class IV</td><td>Construction materials</td><td>Lumber, HESCO barriers, concertina wire</td></tr>
                    <tr><td style="color:var(--cyan)">Class V</td><td>Ammunition</td><td>All rounds, missiles, explosives, pyrotechnics</td></tr>
                    <tr><td style="color:var(--cyan)">Class VI</td><td>Personal demand items</td><td>PX/BX goods: toiletries, snacks, sundries</td></tr>
                    <tr><td style="color:var(--cyan)">Class VII</td><td>Major end items</td><td>Vehicles, aircraft, weapon systems, radios</td></tr>
                    <tr><td style="color:var(--cyan)">Class VIII</td><td>Medical supplies</td><td>Medications, blood, surgical equipment</td></tr>
                    <tr><td style="color:var(--cyan)">Class IX</td><td>Repair parts &amp; components</td><td>Vehicle parts, electronic components</td></tr>
                    <tr><td style="color:var(--cyan)">Class X</td><td>Agricultural &amp; economic development</td><td>Seeds, tools, farming equipment (COIN ops)</td></tr>
                  </table>
                </div>
              </div>
            </div>
          </div>

        </div><!-- /domain-body military -->
      </div><!-- /domain-section military -->

    </div>
    <!-- /container -->'''

# ── CSS ADDITIONS ─────────────────────────────────────────────────────────────
CSS_ADDITIONS = """
/* ── MILITARY STAFF CODES DOMAIN ── */
.domain-military { --accent: #f59e0b; }
.chip.c-military { color: #f59e0b; border-color: rgba(245,158,11,.3); }
.chip.c-military.active,
.chip.c-military:hover { background: rgba(245,158,11,.12); }
.ctag-military { color: #f59e0b; border-color: rgba(245,158,11,.3); }
[data-theme="light"] .chip.c-military { color: #b45309; border-color: rgba(180,83,9,.3); }
[data-theme="light"] .chip.c-military.active { background: rgba(180,83,9,.1) !important; color: #92400e !important; border-color: #92400e !important; }
"""


# ── HELPERS ───────────────────────────────────────────────────────────────────

def patch_replace(path, anchor, replacement, label):
    with open(path, "r", encoding="utf-8") as f:
        src = f.read()
    if anchor not in src:
        print(f"  ERROR {path} — anchor not found for: {label}")
        sys.exit(1)
    patched = src.replace(anchor, replacement, 1)
    with open(path, "w", encoding="utf-8") as f:
        f.write(patched)
    print(f"  OK    {path} — {label}")


def append_to(path, content, sentinel, label):
    with open(path, "r", encoding="utf-8") as f:
        src = f.read()
    if sentinel in src:
        print(f"  SKIP  {path} — {label} already applied")
        return
    with open(path, "a", encoding="utf-8") as f:
        f.write(content)
    print(f"  OK    {path} — {label}")


def is_patched(path):
    with open(path, "r", encoding="utf-8") as f:
        return SENTINEL in f.read()


# ── MAIN ──────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("Patching: Military Staff Codes domain...")

    if is_patched("index.html"):
        print("  SKIP  index.html — already patched")
    else:
        patch_replace("index.html", CHIP_ANCHOR, CHIP_HTML, "military chip")
        patch_replace("index.html", DOMAIN_ANCHOR, DOMAIN_HTML, "military domain section")

    append_to("style.css", CSS_ADDITIONS, "domain-military", "military CSS")

    print("Done.")
