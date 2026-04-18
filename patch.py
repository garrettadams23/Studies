#!/usr/bin/env python3
"""
patch.py — Injects the Lifestyle & Philosophy domain into the Tech Reference site.
Targets: index.html  (chip + domain section)
         style.css   (accent + utility classes)
         script.js   (no changes needed — existing logic handles new domain)

Usage:  python3 patch.py
Idempotent: re-running skips already-patched files (checks for sentinel string).
"""

import sys

SENTINEL = 'data-domain="lifestyle"'   # abort if already injected

# ─── CHIP ────────────────────────────────────────────────────────────────────
# Inserted after the SHORTCUTS chip and before the Theme toggle button.

CHIP_ANCHOR = '        <!-- Theme toggle — uses localStorage for persistence -->'

CHIP_HTML = '''        <div class="chip c-lifestyle" onclick="filter(\'lifestyle\', this)">
          🧘 LIFESTYLE &amp; PHILOSOPHY
        </div>
        <!-- Theme toggle — uses localStorage for persistence -->'''

# ─── DOMAIN SECTION ──────────────────────────────────────────────────────────
# Inserted right before the closing </div> <!-- /container -->

DOMAIN_ANCHOR = '    </div>\n    <!-- /container -->'

DOMAIN_HTML = '''
      <!-- ══════════════════════════════════════════════════════════════════
           DOMAIN: LIFESTYLE & PHILOSOPHY
           Topics: Stoicism · Machiavellianism · Psychology · Philosophy
                   Buddhism · Taoism · Existentialism · Minimalism
      ══════════════════════════════════════════════════════════════════════ -->
      <div class="domain-section domain-lifestyle" data-domain="lifestyle">
        <div class="domain-header" onclick="toggleDomain(this)">
          <span class="domain-icon">🧘</span>
          <span class="domain-title">Lifestyle &amp; Philosophy</span>
          <div class="cert-tags">
            <span class="ctag ctag-lifestyle">LIFE</span>
          </div>
          <span class="domain-sub">Stoicism · Machiavellianism · Psychology · Buddhism · Taoism · Existentialism · Minimalism</span>
          <span class="chevron">▾</span>
        </div>
        <div class="domain-body">

          <!-- ── TOPIC: STOICISM ─────────────────────────────────────── -->
          <div class="topic">
            <div class="topic-header" onclick="toggleTopic(this)">
              <span class="topic-icon">🏛️</span>
              <span class="topic-name">Stoicism — The Art of Rational Endurance</span>
              <span class="topic-badge">PHILOSOPHY</span>
              <span class="topic-chev">▶</span>
            </div>
            <div class="topic-body">
              <div class="concept-card">
                <div class="concept-label">Ancient Greek · Roman</div>
                <div class="concept-title">Core Doctrines &amp; Daily Practice</div>
                <div class="concept-desc">
                  Founded ~300 BC by Zeno of Citium. Stoics held that <strong style="color:var(--amber)">virtue alone is sufficient for happiness</strong>
                  and that emotions rooted in false judgements must be overcome through reason.
                </div>
                <div class="dw">
                  <div class="dt">▸ THE FOUR CARDINAL VIRTUES</div>
                  <div class="card-grid" style="grid-template-columns:repeat(auto-fit,minmax(170px,1fr));margin-bottom:14px">
                    <div class="g-card row-cyan" style="border-color:rgba(0,212,255,.3)">
                      <div class="g-name text-cyan">Wisdom (Sophia)</div>
                      <div class="g-desc">Knowing what is good, bad, and indifferent. The foundation of all other virtues.</div>
                    </div>
                    <div class="g-card row-green" style="border-color:rgba(0,255,153,.3)">
                      <div class="g-name text-green">Justice (Dikaiosyne)</div>
                      <div class="g-desc">Acting rightly toward others. Social duty; fairness in all dealings.</div>
                    </div>
                    <div class="g-card row-amber" style="border-color:rgba(255,176,32,.3)">
                      <div class="g-name text-amber">Courage (Andreia)</div>
                      <div class="g-desc">Facing hardship, pain, and death without flinching. Moral as well as physical.</div>
                    </div>
                    <div class="g-card row-purple" style="border-color:rgba(168,85,247,.3)">
                      <div class="g-name text-purple">Temperance (Sophrosyne)</div>
                      <div class="g-desc">Self-discipline and moderation. Mastery over appetites and impulses.</div>
                    </div>
                  </div>
                  <div class="dt">▸ CORE PRINCIPLES</div>
                  <table class="ref-table" style="margin-bottom:14px">
                    <tr><th>Principle</th><th>Meaning</th><th>Practice</th></tr>
                    <tr>
                      <td style="color:var(--cyan)">Dichotomy of Control</td>
                      <td>Some things are "up to us" (prohairesis) — judgements, impulses, desires. Everything else is external and indifferent.</td>
                      <td>Ask "Is this in my control?" before reacting to any event.</td>
                    </tr>
                    <tr>
                      <td style="color:var(--cyan)">Memento Mori</td>
                      <td>"Remember you will die." Mortality awareness as a tool for gratitude and urgency.</td>
                      <td>Morning reflection: treat each day as a gift, not a given.</td>
                    </tr>
                    <tr>
                      <td style="color:var(--cyan)">Amor Fati</td>
                      <td>"Love of fate." Accept and embrace everything that happens — not mere tolerance, but affirmation.</td>
                      <td>Reframe obstacles as opportunities; say "it was meant to be" and mean it.</td>
                    </tr>
                    <tr>
                      <td style="color:var(--cyan)">Negative Visualization (Premeditatio Malorum)</td>
                      <td>Deliberately imagine loss — of health, relationships, possessions — to appreciate what you have.</td>
                      <td>Evening: briefly imagine losing what you value most, then feel gratitude for its presence.</td>
                    </tr>
                    <tr>
                      <td style="color:var(--cyan)">Sympatheia</td>
                      <td>All things are interconnected in one rational whole (the Logos). We are citizens of the universe.</td>
                      <td>When frustrated by others: "They act from ignorance, not malice. I would do the same without better judgement."</td>
                    </tr>
                  </table>
                  <div class="dt">▸ KEY FIGURES &amp; TEXTS</div>
                  <table class="ref-table" style="margin-bottom:14px">
                    <tr><th>Figure</th><th>Era</th><th>Key Work</th><th>Contribution</th></tr>
                    <tr><td style="color:var(--amber)">Marcus Aurelius</td><td>121–180 AD</td><td>Meditations</td><td>Roman Emperor. Private journal of self-discipline; applied Stoicism in governance.</td></tr>
                    <tr><td style="color:var(--amber)">Epictetus</td><td>50–135 AD</td><td>Enchiridion, Discourses</td><td>Former slave. Focused on inner freedom regardless of external circumstance.</td></tr>
                    <tr><td style="color:var(--amber)">Seneca</td><td>4 BC–65 AD</td><td>Letters to Lucilius, On the Shortness of Life</td><td>Statesman and playwright. Practical moral essays on time, wealth, and death.</td></tr>
                    <tr><td style="color:var(--amber)">Zeno of Citium</td><td>334–262 BC</td><td>—</td><td>Founder of the Stoic school in Athens' painted porch (Stoa Poikile).</td></tr>
                  </table>
                  <div class="dt">▸ DAILY STOIC PRACTICE</div>
                  <div class="kc-row row-cyan"><div class="kc-num text-cyan">AM</div><div class="kc-phase">Morning Journal</div><div class="kc-desc">What obstacles might I face today? How will I respond virtuously? Rehearse the day — adversities and all.</div></div>
                  <div class="kc-row row-amber"><div class="kc-num text-amber">MID</div><div class="kc-phase">Pause &amp; Label</div><div class="kc-desc">When emotion arises, name it: "I notice anger." The gap between stimulus and response is where virtue lives.</div></div>
                  <div class="kc-row row-green"><div class="kc-num text-green">PM</div><div class="kc-phase">Evening Review</div><div class="kc-desc">What did I do well? What could I have done better? No self-flagellation — just honest assessment. (Seneca's method)</div></div>
                </div>
              </div>
            </div>
          </div>

          <!-- ── TOPIC: MACHIAVELLIANISM ──────────────────────────── -->
          <div class="topic">
            <div class="topic-header" onclick="toggleTopic(this)">
              <span class="topic-icon">♟️</span>
              <span class="topic-name">Machiavellianism — Power, Realism &amp; Strategy</span>
              <span class="topic-badge">POLITICAL PHILOSOPHY</span>
              <span class="topic-chev">▶</span>
            </div>
            <div class="topic-body">
              <div class="concept-card">
                <div class="concept-label">Niccolò Machiavelli · 1469–1527</div>
                <div class="concept-title">The Prince &amp; the Discourses — Realpolitik Framework</div>
                <div class="concept-desc">
                  Machiavelli separated political science from ethics. His work describes <strong style="color:var(--red)">how power actually operates</strong>,
                  not how it ideally should. Often misread as endorsing cruelty; actually a clinical observer of political reality.
                </div>
                <div class="dw">
                  <div class="dt">▸ CORE CONCEPTS</div>
                  <table class="ref-table" style="margin-bottom:14px">
                    <tr><th>Concept</th><th>Meaning</th></tr>
                    <tr><td style="color:var(--red)">Virtù</td><td>Not "virtue" but <em>prowess</em> — strength, skill, cunning, willpower. The ruler's capacity to shape events through force of character and action.</td></tr>
                    <tr><td style="color:var(--red)">Fortuna</td><td>Fortune/chance — the unpredictable half of all outcomes. Virtù can master ~50% of fate; the rest is Fortuna. She favors the bold.</td></tr>
                    <tr><td style="color:var(--red)">The Lion &amp; the Fox</td><td>A ruler must be both: the <strong>lion</strong> to frighten wolves (force), the <strong>fox</strong> to recognize traps (cunning). Neither alone is sufficient.</td></tr>
                    <tr><td style="color:var(--red)">Economy of Violence</td><td>Cruelties must be committed all at once; benefits distributed gradually. Sudden harshness is quickly forgotten; lingering harm festers.</td></tr>
                    <tr><td style="color:var(--red)">Appearance vs. Reality</td><td>It is unnecessary to actually possess virtues — it is sufficient to appear to have them. People judge by what they see, not what is.</td></tr>
                    <tr><td style="color:var(--red)">Love vs. Fear</td><td>It is safer to be feared than loved <em>if</em> you cannot be both. But avoid being hated — hatred is fatal; fear can be managed.</td></tr>
                  </table>
                  <div class="dt">▸ THE 48 LAWS — ROBERT GREENE'S SYNTHESIS</div>
                  <div class="card-grid" style="grid-template-columns:repeat(auto-fit,minmax(200px,1fr));margin-bottom:14px">
                    <div class="g-card" style="border-color:rgba(255,77,109,.3)">
                      <div class="g-name text-red">Never Outshine the Master</div>
                      <div class="g-desc">Always make those above you feel superior. Conceal your talent when needed.</div>
                    </div>
                    <div class="g-card" style="border-color:rgba(255,77,109,.3)">
                      <div class="g-name text-red">Conceal Your Intentions</div>
                      <div class="g-desc">Keep people off-balance. Reveal purpose only when it cannot be stopped.</div>
                    </div>
                    <div class="g-card" style="border-color:rgba(255,77,109,.3)">
                      <div class="g-name text-red">Guard Your Reputation</div>
                      <div class="g-desc">Reputation is the cornerstone of power. A single crack and you are vulnerable.</div>
                    </div>
                    <div class="g-card" style="border-color:rgba(255,77,109,.3)">
                      <div class="g-name text-red">Play on People's Need to Believe</div>
                      <div class="g-desc">People crave meaning. Offer a cause, a vision — they will follow willingly.</div>
                    </div>
                  </div>
                  <div class="dt">▸ DARK TRIAD CONTEXT (Psychology)</div>
                  <table class="ref-table">
                    <tr><th>Trait</th><th>Core</th><th>Distinction</th></tr>
                    <tr><td style="color:var(--amber)">Machiavellianism</td><td>Cynical worldview, strategic manipulation, delayed gratification</td><td>Calculating and patient; manipulates for long-term gain</td></tr>
                    <tr><td style="color:var(--amber)">Narcissism</td><td>Grandiosity, entitlement, need for admiration</td><td>Emotional; manipulates for ego supply and status</td></tr>
                    <tr><td style="color:var(--amber)">Psychopathy</td><td>Low empathy, impulsivity, callousness</td><td>Reactive; least strategic of the three</td></tr>
                  </table>
                </div>
              </div>
            </div>
          </div>

          <!-- ── TOPIC: PSYCHOLOGY ───────────────────────────────────── -->
          <div class="topic">
            <div class="topic-header" onclick="toggleTopic(this)">
              <span class="topic-icon">🧠</span>
              <span class="topic-name">Psychology — Mind, Behavior &amp; Biases</span>
              <span class="topic-badge">COGNITIVE SCIENCE</span>
              <span class="topic-chev">▶</span>
            </div>
            <div class="topic-body">
              <div class="concept-card">
                <div class="concept-label">Applied Psychology</div>
                <div class="concept-title">Cognitive Biases · Defense Mechanisms · Frameworks</div>
                <div class="concept-desc">
                  Psychology studies the mind and behavior. Understanding your cognitive architecture is the first step to overcoming it.
                  <strong style="color:var(--cyan)">"Knowing yourself is the beginning of all wisdom."</strong> — Aristotle
                </div>
                <div class="dw">
                  <div class="dt">▸ KEY COGNITIVE BIASES</div>
                  <table class="ref-table" style="margin-bottom:14px">
                    <tr><th>Bias</th><th>Description</th><th>Example</th></tr>
                    <tr><td style="color:var(--cyan)">Confirmation Bias</td><td>Seek info that confirms existing beliefs; ignore contradicting evidence</td><td>Only reading news aligned with your politics</td></tr>
                    <tr><td style="color:var(--cyan)">Dunning-Kruger Effect</td><td>Incompetent people overestimate ability; experts underestimate theirs</td><td>Beginner investor convinced they've outsmarted the market</td></tr>
                    <tr><td style="color:var(--cyan)">Sunk Cost Fallacy</td><td>Continue bad decisions because of past investment (time/money/effort)</td><td>Finishing a terrible book because you've read half of it</td></tr>
                    <tr><td style="color:var(--cyan)">Availability Heuristic</td><td>Judge probability by how easily examples come to mind</td><td>Fear flying after seeing news of a crash; ignoring car risk</td></tr>
                    <tr><td style="color:var(--cyan)">Fundamental Attribution Error</td><td>Over-attribute others' behavior to character; under-attribute to situation</td><td>"They cut me off — they're a bad person" (vs. they're late for hospital)</td></tr>
                    <tr><td style="color:var(--cyan)">Anchoring</td><td>Over-rely on first piece of information encountered</td><td>$100 item marked down to $70 feels like a deal regardless of value</td></tr>
                    <tr><td style="color:var(--cyan)">Negativity Bias</td><td>Negative events register more strongly than equally positive ones</td><td>One criticism outweighs ten compliments</td></tr>
                    <tr><td style="color:var(--cyan)">Halo Effect</td><td>One positive trait causes assumption of other positive traits</td><td>Attractive people assumed to be more competent</td></tr>
                  </table>
                  <div class="dt">▸ EGO DEFENSE MECHANISMS (Freud / Anna Freud)</div>
                  <table class="ref-table" style="margin-bottom:14px">
                    <tr><th>Mechanism</th><th>Description</th></tr>
                    <tr><td style="color:var(--purple)">Repression</td><td>Unconsciously pushing threatening thoughts out of awareness</td></tr>
                    <tr><td style="color:var(--purple)">Rationalization</td><td>Creating logical explanations to justify unacceptable behavior</td></tr>
                    <tr><td style="color:var(--purple)">Projection</td><td>Attributing your own unacceptable feelings to others</td></tr>
                    <tr><td style="color:var(--purple)">Denial</td><td>Refusing to acknowledge a painful reality</td></tr>
                    <tr><td style="color:var(--purple)">Displacement</td><td>Redirecting emotion from original source to safer target</td></tr>
                    <tr><td style="color:var(--purple)">Sublimation</td><td>Channeling unacceptable impulses into socially acceptable activity (e.g., aggression → sport)</td></tr>
                  </table>
                  <div class="dt">▸ KEY FRAMEWORKS</div>
                  <div class="card-grid" style="grid-template-columns:repeat(auto-fit,minmax(200px,1fr))">
                    <div class="g-card" style="border-color:rgba(0,212,255,.3)">
                      <div class="g-name text-cyan">Maslow's Hierarchy</div>
                      <div class="g-desc">Physiological → Safety → Love/Belonging → Esteem → Self-Actualization. Lower needs must be satisfied before higher ones motivate.</div>
                    </div>
                    <div class="g-card" style="border-color:rgba(0,255,153,.3)">
                      <div class="g-name text-green">Locus of Control</div>
                      <div class="g-desc"><strong>Internal:</strong> outcomes result from your actions. <strong>External:</strong> outcomes are luck/fate. Internal LoC correlates strongly with resilience and achievement.</div>
                    </div>
                    <div class="g-card" style="border-color:rgba(255,176,32,.3)">
                      <div class="g-name text-amber">Growth vs Fixed Mindset</div>
                      <div class="g-desc">Carol Dweck. Fixed: ability is innate and static. Growth: ability is developed through effort. Growth mindset predicts higher achievement and resilience.</div>
                    </div>
                    <div class="g-card" style="border-color:rgba(168,85,247,.3)">
                      <div class="g-name text-purple">Flow State (Csikszentmihalyi)</div>
                      <div class="g-desc">Optimal experience at the intersection of high challenge + high skill. Time distorts. Deep absorption. Intrinsic reward. Cultivated through deliberate practice.</div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <!-- ── TOPIC: PHILOSOPHY ───────────────────────────────────── -->
          <div class="topic">
            <div class="topic-header" onclick="toggleTopic(this)">
              <span class="topic-icon">📜</span>
              <span class="topic-name">Philosophy — Schools of Thought</span>
              <span class="topic-badge">WESTERN TRADITION</span>
              <span class="topic-chev">▶</span>
            </div>
            <div class="topic-body">
              <div class="concept-card">
                <div class="concept-label">Epistemology · Metaphysics · Ethics · Logic</div>
                <div class="concept-title">Major Schools &amp; Key Thinkers</div>
                <div class="dw">
                  <div class="dt">▸ MAJOR SCHOOLS</div>
                  <table class="ref-table" style="margin-bottom:14px">
                    <tr><th>School</th><th>Era</th><th>Core Claim</th><th>Key Figures</th></tr>
                    <tr><td style="color:var(--cyan)">Rationalism</td><td>17th–18th c.</td><td>Knowledge derived primarily from reason, not senses. Innate ideas exist.</td><td>Descartes, Spinoza, Leibniz</td></tr>
                    <tr><td style="color:var(--cyan)">Empiricism</td><td>17th–18th c.</td><td>All knowledge derives from sensory experience. The mind starts as a blank slate (tabula rasa).</td><td>Locke, Hume, Berkeley</td></tr>
                    <tr><td style="color:var(--cyan)">Pragmatism</td><td>19th–20th c.</td><td>Truth is what works in practice. Ideas are tools; their value is in their consequences.</td><td>Peirce, James, Dewey</td></tr>
                    <tr><td style="color:var(--cyan)">Existentialism</td><td>20th c.</td><td>Existence precedes essence. Individuals create their own meaning in an indifferent universe.</td><td>Sartre, Camus, Heidegger, de Beauvoir</td></tr>
                    <tr><td style="color:var(--cyan)">Utilitarianism</td><td>18th–19th c.</td><td>The morally right action maximizes overall happiness (utility) for the greatest number.</td><td>Bentham, Mill</td></tr>
                    <tr><td style="color:var(--cyan)">Kantian Ethics (Deontology)</td><td>18th c.</td><td>Act only according to maxims you could will to be universal laws. Duty above consequences.</td><td>Immanuel Kant</td></tr>
                    <tr><td style="color:var(--cyan)">Virtue Ethics</td><td>Ancient Greek</td><td>Focus on developing good character (virtues) rather than rules or outcomes.</td><td>Aristotle, MacIntyre</td></tr>
                    <tr><td style="color:var(--cyan)">Nihilism</td><td>19th–20th c.</td><td>Life has no intrinsic meaning, purpose, or value. Traditional morality is groundless.</td><td>Nietzsche (critic), Cioran</td></tr>
                  </table>
                  <div class="dt">▸ ESSENTIAL CONCEPTS</div>
                  <table class="ref-table">
                    <tr><th>Concept</th><th>Definition</th></tr>
                    <tr><td style="color:var(--amber)">Cogito ergo sum</td><td>"I think, therefore I am." Descartes' foundational certainty — even a deceiver cannot doubt the existence of the doubter.</td></tr>
                    <tr><td style="color:var(--amber)">Categorical Imperative</td><td>Kant: act only on maxims that could become universal laws. Treat humanity never merely as means but always as ends.</td></tr>
                    <tr><td style="color:var(--amber)">Absurdism</td><td>Camus: life is inherently meaningless yet humans persistently seek meaning — this conflict is the Absurd. Response: revolt (not suicide, not faith).</td></tr>
                    <tr><td style="color:var(--amber)">Veil of Ignorance</td><td>Rawls: design a just society without knowing your position in it. Ensures impartiality — you'd design fairness since you might be disadvantaged.</td></tr>
                    <tr><td style="color:var(--amber)">Übermensch</td><td>Nietzsche's "Overman" — one who creates their own values after the "death of God." Not a racial concept; a call to self-overcoming.</td></tr>
                    <tr><td style="color:var(--amber)">Solipsism</td><td>Only one's own mind is certain to exist. All else may be illusion. A logical extreme rarely endorsed but philosophically significant.</td></tr>
                  </table>
                </div>
              </div>
            </div>
          </div>

          <!-- ── TOPIC: BUDDHISM ─────────────────────────────────────── -->
          <div class="topic">
            <div class="topic-header" onclick="toggleTopic(this)">
              <span class="topic-icon">☸️</span>
              <span class="topic-name">Buddhism — The Path to Liberation</span>
              <span class="topic-badge">SPIRITUAL PHILOSOPHY</span>
              <span class="topic-chev">▶</span>
            </div>
            <div class="topic-body">
              <div class="concept-card">
                <div class="concept-label">Siddhartha Gautama · ~563–483 BC</div>
                <div class="concept-title">Four Noble Truths · Eightfold Path · Core Concepts</div>
                <div class="concept-desc">
                  Buddhism is both a religion and a philosophy. Its goal is the cessation of <em>dukkha</em> (suffering) through understanding the nature of mind and reality.
                  Not theistic in the Western sense — the Buddha is a teacher, not a god.
                </div>
                <div class="dw">
                  <div class="dt">▸ THE FOUR NOBLE TRUTHS (Catvāri Āryasatyāni)</div>
                  <div class="kc-row row-amber"><div class="kc-num text-amber">1</div><div class="kc-phase">Dukkha (Suffering)</div><div class="kc-desc">Life inherently contains suffering, dissatisfaction, and imperfection. Birth, aging, sickness, death, getting what we don't want, not getting what we want — all are dukkha.</div></div>
                  <div class="kc-row row-red"><div class="kc-num text-red">2</div><div class="kc-phase">Samudāya (Origin)</div><div class="kc-desc">The origin of suffering is craving (tanha) — for pleasure, for existence, for non-existence. Attachment and aversion are the roots.</div></div>
                  <div class="kc-row row-cyan"><div class="kc-num text-cyan">3</div><div class="kc-phase">Nirodha (Cessation)</div><div class="kc-desc">Suffering can cease. Nirvana is the complete extinguishing of craving — a state of peace, freedom, and liberation.</div></div>
                  <div class="kc-row row-green"><div class="kc-num text-green">4</div><div class="kc-phase">Magga (The Path)</div><div class="kc-desc">The Noble Eightfold Path is the way to end suffering. Practical and systematic — not metaphysical belief but lived practice.</div></div>
                  <div class="dt" style="margin-top:14px">▸ THE NOBLE EIGHTFOLD PATH</div>
                  <table class="ref-table" style="margin-bottom:14px">
                    <tr><th>Path</th><th>Category</th><th>Meaning</th></tr>
                    <tr><td style="color:var(--green)">Right View</td><td>Wisdom</td><td>Understanding the Four Noble Truths; seeing reality as it is, not as we wish it to be.</td></tr>
                    <tr><td style="color:var(--green)">Right Intention</td><td>Wisdom</td><td>Commitment to non-attachment, non-ill-will, and non-harmfulness.</td></tr>
                    <tr><td style="color:var(--cyan)">Right Speech</td><td>Ethics</td><td>Abstaining from lying, divisive speech, harsh speech, and idle chatter.</td></tr>
                    <tr><td style="color:var(--cyan)">Right Action</td><td>Ethics</td><td>Abstaining from killing, stealing, and sexual misconduct.</td></tr>
                    <tr><td style="color:var(--cyan)">Right Livelihood</td><td>Ethics</td><td>Earning a living that does not cause harm to others or oneself.</td></tr>
                    <tr><td style="color:var(--purple)">Right Effort</td><td>Meditation</td><td>Cultivating wholesome states and abandoning unwholesome ones continuously.</td></tr>
                    <tr><td style="color:var(--purple)">Right Mindfulness</td><td>Meditation</td><td>Present-moment awareness of body, feelings, mind-states, and phenomena.</td></tr>
                    <tr><td style="color:var(--purple)">Right Concentration</td><td>Meditation</td><td>Developing deep meditative absorption (jhanas) as foundation for insight.</td></tr>
                  </table>
                  <div class="dt">▸ CORE CONCEPTS (THE THREE MARKS OF EXISTENCE)</div>
                  <div class="card-grid" style="grid-template-columns:repeat(auto-fit,minmax(190px,1fr))">
                    <div class="g-card" style="border-color:rgba(0,212,255,.3)">
                      <div class="g-name text-cyan">Anicca — Impermanence</div>
                      <div class="g-desc">All conditioned phenomena are impermanent. Clinging to what is transient is the source of suffering. Release attachment.</div>
                    </div>
                    <div class="g-card" style="border-color:rgba(255,176,32,.3)">
                      <div class="g-name text-amber">Dukkha — Unsatisfactoriness</div>
                      <div class="g-desc">Even pleasant experiences carry an undercurrent of dissatisfaction because they end. Nothing conditioned can permanently satisfy.</div>
                    </div>
                    <div class="g-card" style="border-color:rgba(0,255,153,.3)">
                      <div class="g-name text-green">Anatta — Non-Self</div>
                      <div class="g-desc">The "self" is not a fixed, permanent entity but a changing process of aggregates (skandhas). Liberating when truly understood.</div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <!-- ── TOPIC: TAOISM ───────────────────────────────────────── -->
          <div class="topic">
            <div class="topic-header" onclick="toggleTopic(this)">
              <span class="topic-icon">☯️</span>
              <span class="topic-name">Taoism — The Way of Nature</span>
              <span class="topic-badge">CHINESE PHILOSOPHY</span>
              <span class="topic-chev">▶</span>
            </div>
            <div class="topic-body">
              <div class="concept-card">
                <div class="concept-label">Lao Tzu · ~6th–4th c. BC</div>
                <div class="concept-title">Tao Te Ching — The Classic of the Way and Its Power</div>
                <div class="concept-desc">
                  The Tao (道) — the Way — is the fundamental, unnamed principle underlying all of reality. It cannot be named or fully grasped, only lived.
                  <em>"The Tao that can be told is not the eternal Tao."</em>
                </div>
                <div class="dw">
                  <div class="dt">▸ CORE PRINCIPLES</div>
                  <table class="ref-table" style="margin-bottom:14px">
                    <tr><th>Principle</th><th>Meaning</th><th>Application</th></tr>
                    <tr><td style="color:var(--green)">Wu Wei (無為)</td><td>"Non-action" or effortless action. Acting in harmony with the natural flow rather than forcing outcomes.</td><td>Avoid unnecessary struggle. Like water: yield, go around, persist gently.</td></tr>
                    <tr><td style="color:var(--green)">Pu (樸) — Simplicity</td><td>The uncarved block. Original nature before social conditioning. Simplicity as strength.</td><td>Strip away pretense. Return to what is essential and natural.</td></tr>
                    <tr><td style="color:var(--green)">Te (德) — Virtue/Power</td><td>Inner virtue or power that arises naturally when aligned with the Tao. Not morality imposed from outside but integrity from within.</td><td>Be genuinely good, not performatively good.</td></tr>
                    <tr><td style="color:var(--green)">Yin-Yang (陰陽)</td><td>All opposites are interdependent and contain each other's seed. Darkness within light, light within darkness. Change is constant.</td><td>Stop seeing circumstances as purely good or bad. Both are transforming.</td></tr>
                    <tr><td style="color:var(--green)">Ziran (自然)</td><td>Self-so, naturalness. Things should be allowed to follow their own nature.</td><td>Stop trying to control what is inherently wild and self-organizing.</td></tr>
                  </table>
                  <div class="dt">▸ WATER AS TAOIST METAPHOR</div>
                  <div class="info-bar" style="background:rgba(0,255,153,.04);border:1px solid rgba(0,255,153,.2);color:var(--text)">
                    Water is the supreme Taoist metaphor. It is:<br>
                    · <strong style="color:var(--green)">Soft</strong> yet wears down the hardest rock (persistence)<br>
                    · <strong style="color:var(--green)">Low</strong> — it always seeks the lowest point (humility)<br>
                    · <strong style="color:var(--green)">Yielding</strong> — flows around obstacles rather than fighting them<br>
                    · <strong style="color:var(--green)">Essential</strong> — all life depends on it, yet it does not demand recognition<br>
                    <em>"Nothing in the world is as soft and yielding as water, yet nothing is better at dissolving the hard and inflexible."</em>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <!-- ── TOPIC: EXISTENTIALISM ───────────────────────────────── -->
          <div class="topic">
            <div class="topic-header" onclick="toggleTopic(this)">
              <span class="topic-icon">🌑</span>
              <span class="topic-name">Existentialism &amp; Absurdism</span>
              <span class="topic-badge">20TH C. PHILOSOPHY</span>
              <span class="topic-chev">▶</span>
            </div>
            <div class="topic-body">
              <div class="concept-card">
                <div class="concept-label">Sartre · Camus · Kierkegaard · Heidegger</div>
                <div class="concept-title">"Existence precedes essence" — Building meaning in a meaningless universe</div>
                <div class="concept-desc">
                  Existentialism holds that there is no pre-given human nature or purpose. We exist first, then create ourselves through choices.
                  This is both terrifying (<strong style="color:var(--red)">radical freedom</strong>) and liberating.
                </div>
                <div class="dw">
                  <div class="dt">▸ KEY CONCEPTS</div>
                  <table class="ref-table" style="margin-bottom:14px">
                    <tr><th>Concept</th><th>Thinker</th><th>Meaning</th></tr>
                    <tr><td style="color:var(--red)">Radical Freedom</td><td>Sartre</td><td>We are "condemned to be free" — there is no escape from choice. Even refusing to choose is a choice. Total responsibility for self.</td></tr>
                    <tr><td style="color:var(--red)">Bad Faith (Mauvaise Foi)</td><td>Sartre</td><td>Pretending you have no choice; adopting a fixed identity to escape freedom. E.g., "I can't help it, that's just who I am."</td></tr>
                    <tr><td style="color:var(--red)">The Absurd</td><td>Camus</td><td>The conflict between humans' need for meaning and the universe's silent indifference. Three responses: physical suicide (wrong), philosophical suicide (religion — bad faith), or revolt (the only authentic response).</td></tr>
                    <tr><td style="color:var(--red)">Authenticity</td><td>Heidegger</td><td>Owning your existence — facing death (Being-toward-death) rather than fleeing into das Man (the "they-self" of conformity).</td></tr>
                    <tr><td style="color:var(--red)">Leap of Faith</td><td>Kierkegaard</td><td>Rational thought cannot resolve the deepest questions. Authentic existence requires a passionate, subjective commitment despite uncertainty.</td></tr>
                    <tr><td style="color:var(--red)">Thrownness (Geworfenheit)</td><td>Heidegger</td><td>We are "thrown" into existence — we did not choose our time, place, language, culture. But we are responsible for what we do with this situation.</td></tr>
                  </table>
                  <div class="dt">▸ THE MYTH OF SISYPHUS — CAMUS</div>
                  <div class="info-bar" style="background:rgba(255,77,109,.04);border:1px solid rgba(255,77,109,.2);color:var(--text)">
                    Sisyphus is condemned to roll a boulder up a hill for eternity — it always rolls back down. Camus argues this is the human condition.<br><br>
                    The resolution: <strong style="color:var(--red)">"One must imagine Sisyphus happy."</strong><br>
                    Not because the task is meaningful in any cosmic sense, but because <em>the struggle itself fills his heart.</em>
                    Revolt against absurdity — continuing to live, create, love — is the only authentic response.
                  </div>
                </div>
              </div>
            </div>
          </div>

          <!-- ── TOPIC: MINIMALISM & INTENTIONAL LIVING ──────────────── -->
          <div class="topic">
            <div class="topic-header" onclick="toggleTopic(this)">
              <span class="topic-icon">⬜</span>
              <span class="topic-name">Minimalism &amp; Intentional Living</span>
              <span class="topic-badge">LIFESTYLE</span>
              <span class="topic-chev">▶</span>
            </div>
            <div class="topic-body">
              <div class="concept-card">
                <div class="concept-label">Modern Practice</div>
                <div class="concept-title">Intentionality · Essentialism · Deep Work</div>
                <div class="dw">
                  <div class="dt">▸ CORE PRINCIPLES</div>
                  <div class="card-grid" style="grid-template-columns:repeat(auto-fit,minmax(200px,1fr));margin-bottom:14px">
                    <div class="g-card" style="border-color:rgba(0,212,255,.3)">
                      <div class="g-name text-cyan">Essentialism (Greg McKeown)</div>
                      <div class="g-desc">The disciplined pursuit of less. Not about doing more things — about doing the <em>right</em> things. "If it's not a clear yes, it's a no."</div>
                    </div>
                    <div class="g-card" style="border-color:rgba(0,255,153,.3)">
                      <div class="g-name text-green">Deep Work (Cal Newport)</div>
                      <div class="g-desc">Cognitively demanding tasks performed in a state of distraction-free concentration. The skill of the 21st century. Rare + valuable = leverage.</div>
                    </div>
                    <div class="g-card" style="border-color:rgba(255,176,32,.3)">
                      <div class="g-name text-amber">KonMari Method</div>
                      <div class="g-desc">Keep only what "sparks joy." Tidy by category, not location. The goal: create an environment that supports who you want to become.</div>
                    </div>
                    <div class="g-card" style="border-color:rgba(168,85,247,.3)">
                      <div class="g-name text-purple">Parkinson's Law</div>
                      <div class="g-desc">Work expands to fill the time allotted. Impose artificial constraints. Deadlines create focus. Less time + clear priority = better output.</div>
                    </div>
                  </div>
                  <div class="dt">▸ HIGH-PERFORMANCE LIFESTYLE FRAMEWORKS</div>
                  <table class="ref-table">
                    <tr><th>Framework</th><th>Key Idea</th><th>Source</th></tr>
                    <tr><td style="color:var(--cyan)">80/20 Principle (Pareto)</td><td>80% of results come from 20% of efforts. Identify and double down on the vital few. Ruthlessly eliminate the trivial many.</td><td>Vilfredo Pareto / Tim Ferriss</td></tr>
                    <tr><td style="color:var(--cyan)">Atomic Habits</td><td>Systems over goals. 1% better every day = 37x better in a year. Identity-based habits: "I am a writer" vs "I want to write."</td><td>James Clear</td></tr>
                    <tr><td style="color:var(--cyan)">Ikigai</td><td>Japanese: reason for being. The intersection of what you love, what you're good at, what the world needs, and what you can be paid for.</td><td>Japanese philosophy</td></tr>
                    <tr><td style="color:var(--cyan)">Memento Vivere</td><td>"Remember to live." The counterpoint to Memento Mori — not just contemplating death, but using that awareness to fully inhabit life.</td><td>Stoic tradition</td></tr>
                    <tr><td style="color:var(--cyan)">Wabi-Sabi</td><td>Japanese aesthetic: find beauty in imperfection, transience, and incompleteness. A cracked bowl repaired with gold (Kintsugi) is more beautiful for its history.</td><td>Japanese philosophy</td></tr>
                  </table>
                </div>
              </div>
            </div>
          </div>

        </div><!-- /domain-body lifestyle -->
      </div><!-- /domain-section lifestyle -->

    </div>
    <!-- /container -->'''

# ─── CSS ADDITIONS ────────────────────────────────────────────────────────────
CSS_ADDITIONS = """
/* ── LIFESTYLE & PHILOSOPHY DOMAIN ── */
.domain-lifestyle { --accent: #a78bfa; }
.chip.c-lifestyle { color: #a78bfa; border-color: rgba(167,139,250,.3); }
.chip.c-lifestyle.active,
.chip.c-lifestyle:hover { background: rgba(167,139,250,.12); }
.ctag-lifestyle { color: #a78bfa; border-color: rgba(167,139,250,.3); }
[data-theme="light"] .chip.c-lifestyle { color: #7c3aed; border-color: rgba(124,58,237,.3); }
[data-theme="light"] .chip.c-lifestyle.active { background: rgba(124,58,237,.1) !important; color: #6d28d9 !important; border-color: #6d28d9 !important; }
"""


# ─── PATCH FUNCTIONS ──────────────────────────────────────────────────────────

def patch_file(path, anchor, replacement, label):
    with open(path, "r", encoding="utf-8") as f:
        src = f.read()
    if SENTINEL in src and "index.html" in path:
        print(f"  SKIP  {path} — already patched")
        return
    if anchor not in src:
        print(f"  ERROR {path} — anchor not found: {anchor[:60]!r}")
        sys.exit(1)
    patched = src.replace(anchor, replacement, 1)
    with open(path, "w", encoding="utf-8") as f:
        f.write(patched)
    print(f"  OK    {path} — {label}")


def patch_css(path):
    with open(path, "r", encoding="utf-8") as f:
        src = f.read()
    if "domain-lifestyle" in src:
        print(f"  SKIP  {path} — already patched")
        return
    with open(path, "a", encoding="utf-8") as f:
        f.write(CSS_ADDITIONS)
    print(f"  OK    {path} — appended lifestyle styles")


# ─── MAIN ─────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("Patching Tech Reference files...")

    patch_file(
        "index.html",
        CHIP_ANCHOR,
        CHIP_HTML,
        "injected lifestyle chip"
    )

    patch_file(
        "index.html",
        DOMAIN_ANCHOR,
        DOMAIN_HTML,
        "injected lifestyle domain section"
    )

    patch_css("style.css")

    print("Done. Open index.html in your browser to verify.")
