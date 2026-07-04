#!/usr/bin/env python3
"""
Master patch runner for the Mental Disorders DSM-5 content in Studies/.

Targets:
  Studies/data/lifestyle.html  — HTML topic blocks
  Studies/style.css            — CSS (detail panels, domain styling)
  Studies/script.js            — JS  (DISORDER_DATA + initDisorderDetails)

Stage 1 — P1 (this script): injects base DSM-5 topic blocks into lifestyle.html.
Stage 2 — sub-patches: discovers every other patch_*.py file in this directory
  (sorted alphabetically: p2 → p3 → …) and executes each one. All sub-patches
  now use absolute paths derived from their own __file__, so no cwd tricks needed.

Usage:
  python patch_mental_disorders_lifestyle.py           # run all patches
  python patch_mental_disorders_lifestyle.py --dry-run # preview only, no writes
  python patch_mental_disorders_lifestyle.py --p1-only # run only this P1 stage
"""
import re, sys, shutil, subprocess
from pathlib import Path

# ── paths ─────────────────────────────────────────────────────────────────────
HERE   = Path(__file__).resolve().parent
DATA   = HERE.parent / 'data'
TARGET = DATA / 'lifestyle.html'

# ── sentinels ─────────────────────────────────────────────────────────────────
GUARD          = '<!-- mental-disorders-dsm5 -->'       # idempotency guard
INJECT_AFTER   = '<!-- /druidism topic -->'             # insert new content here
OLD_MARKER     = '<!-- ── Neurodevelopmental ── -->'    # start of bad injection
SECTION_CLOSE  = '\n</section>'                         # closing tag to preserve

# ── helpers ───────────────────────────────────────────────────────────────────
def read(p):      return Path(p).read_text(encoding='utf-8')
def write(p, txt): Path(p).write_text(txt, encoding='utf-8')

# ── topic HTML (lifestyle.html accordion structure) ────────────────────────────
# Each DSM-5 category → one div.topic with topic-header + topic-body.
# Inside topic-body: concept-card > dw > card-grid of g-cards.

TOPICS_HTML = '''
          <!-- mental-disorders-dsm5 -->

          <!-- ── TOPIC: NEURODEVELOPMENTAL DISORDERS ─────────────────────── -->
          <div class="topic">
            <div class="topic-header">
              <span class="topic-icon">🧩</span>
              <span class="topic-name">Neurodevelopmental Disorders</span>
              <span class="topic-badge">DSM-5 · 7 DISORDERS</span>
              <span class="topic-chev">▶</span>
            </div>
            <div class="topic-body">
              <div class="concept-card">
                <div class="concept-label">Neurodevelopmental · ICD-10 F8x / F9x</div>
                <div class="concept-title">Conditions Manifesting Early in Development</div>
                <div class="concept-desc">
                  Typically present before school age. Characterized by deficits in
                  personal, social, academic, or occupational functioning. Often persist
                  into adulthood with varying degrees of impairment.
                </div>
                <div class="dw">
                  <div class="dt">▸ DISORDERS</div>
                  <div class="card-grid">
                    <div class="g-card" style="border-color:rgba(0,212,255,0.3)">
                      <div class="g-name text-cyan">IDD — Intellectual Disability</div>
                      <div class="g-desc">Deficits in intellectual functions (reasoning, problem-solving, planning) and adaptive behavior across conceptual, social, and practical domains. Onset during developmental period.</div>
                    </div>
                    <div class="g-card" style="border-color:rgba(0,212,255,0.3)">
                      <div class="g-name text-cyan">ASD — Autism Spectrum Disorder</div>
                      <div class="g-desc">Persistent deficits in social communication/interaction + restricted, repetitive behavior patterns. Symptoms in early developmental period. ICD-10: F84.0</div>
                    </div>
                    <div class="g-card" style="border-color:rgba(0,212,255,0.3)">
                      <div class="g-name text-cyan">ADHD — Attention-Deficit/Hyperactivity Disorder</div>
                      <div class="g-desc">Persistent inattention and/or hyperactivity-impulsivity. Several symptoms before age 12 in two+ settings. Subtypes: predominantly inattentive, hyperactive-impulsive, combined. ICD-10: F90.x</div>
                    </div>
                    <div class="g-card" style="border-color:rgba(0,212,255,0.3)">
                      <div class="g-name text-cyan">SLD — Specific Learning Disorder</div>
                      <div class="g-desc">Difficulties learning academic skills (reading, writing, arithmetic) below age expectations despite interventions. Subtypes: dyslexia (reading), dysgraphia (writing), dyscalculia (math).</div>
                    </div>
                    <div class="g-card" style="border-color:rgba(0,212,255,0.3)">
                      <div class="g-name text-cyan">DLD — Language &amp; Communication Disorders</div>
                      <div class="g-desc">Persistent difficulties acquiring/using language. Includes Language Disorder, Speech Sound Disorder, Childhood-Onset Fluency Disorder (stuttering), Social (Pragmatic) Communication Disorder.</div>
                    </div>
                    <div class="g-card" style="border-color:rgba(0,212,255,0.3)">
                      <div class="g-name text-cyan">TIC — Tic Disorders / Tourette's Syndrome</div>
                      <div class="g-desc">Sudden, rapid, recurrent, nonrhythmic motor movement or vocalization. Tourette's: multiple motor + ≥1 vocal tic for &gt;1 year. Persistent (chronic) or Provisional subtypes available.</div>
                    </div>
                    <div class="g-card" style="border-color:rgba(0,212,255,0.3)">
                      <div class="g-name text-cyan">DCD — Motor Disorders</div>
                      <div class="g-desc">Developmental Coordination Disorder: acquisition/execution of motor skills below age expectations. Stereotypic Movement Disorder: repetitive, seemingly driven, nonfunctional motor behavior.</div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <!-- ── TOPIC: SCHIZOPHRENIA SPECTRUM ─────────────────────────────── -->
          <div class="topic">
            <div class="topic-header">
              <span class="topic-icon">🌀</span>
              <span class="topic-name">Schizophrenia Spectrum &amp; Psychotic Disorders</span>
              <span class="topic-badge">DSM-5 · 5 DISORDERS</span>
              <span class="topic-chev">▶</span>
            </div>
            <div class="topic-body">
              <div class="concept-card">
                <div class="concept-label">Psychotic Disorders · ICD-10 F20–F29</div>
                <div class="concept-title">Disorders of Psychosis &amp; Reality Testing</div>
                <div class="concept-desc">
                  Defined by abnormalities in ≥1 of five domains:
                  <strong style="color:var(--purple)">delusions, hallucinations, disorganized thinking,
                  grossly disorganized/abnormal motor behavior</strong>, and <strong style="color:var(--purple)">negative symptoms</strong>.
                </div>
                <div class="dw">
                  <div class="dt">▸ FIVE SYMPTOM DOMAINS</div>
                  <table class="ref-table" style="margin-bottom:14px">
                    <tr><th>Domain</th><th>Description</th></tr>
                    <tr><td style="color:var(--purple)">Delusions</td><td>Fixed beliefs not amenable to change in light of evidence; may be persecutory, referential, grandiose, erotomanic, nihilistic, or somatic</td></tr>
                    <tr><td style="color:var(--purple)">Hallucinations</td><td>Perception-like experiences without external stimulus; most commonly auditory in schizophrenia</td></tr>
                    <tr><td style="color:var(--purple)">Disorganized Speech</td><td>Derailment, loose associations, tangentiality, incoherence ("word salad")</td></tr>
                    <tr><td style="color:var(--purple)">Disorganized Behavior</td><td>Unpredictable agitation, inappropriate affect, catatonia (stupor, rigidity, waxy flexibility, echolalia)</td></tr>
                    <tr><td style="color:var(--purple)">Negative Symptoms</td><td>Diminished emotional expression (flat affect), avolition, alogia, anhedonia, asociality</td></tr>
                  </table>
                  <div class="dt">▸ DISORDERS</div>
                  <div class="card-grid">
                    <div class="g-card" style="border-color:rgba(168,85,247,0.3)">
                      <div class="g-name text-purple">SCZ — Schizophrenia</div>
                      <div class="g-desc">≥2 Criterion A symptoms for ≥1 month. Continuous signs ≥6 months. Significant functional decline. ICD-10: F20.9</div>
                    </div>
                    <div class="g-card" style="border-color:rgba(168,85,247,0.3)">
                      <div class="g-name text-purple">SZA — Schizoaffective Disorder</div>
                      <div class="g-desc">Major mood episode concurrent with Criterion A schizophrenia. Delusions/hallucinations ≥2 weeks without mood symptoms. Bipolar or Depressive type.</div>
                    </div>
                    <div class="g-card" style="border-color:rgba(168,85,247,0.3)">
                      <div class="g-name text-purple">SZF — Schizophreniform Disorder</div>
                      <div class="g-desc">Meets Criterion A of schizophrenia but episode lasts 1–6 months. Provisional until recovery or progression.</div>
                    </div>
                    <div class="g-card" style="border-color:rgba(168,85,247,0.3)">
                      <div class="g-name text-purple">DD — Delusional Disorder</div>
                      <div class="g-desc">≥1 delusion for ≥1 month. Hallucinations not prominent. Functioning not markedly impaired. Types: erotomanic, grandiose, jealous, persecutory, somatic, mixed.</div>
                    </div>
                    <div class="g-card" style="border-color:rgba(168,85,247,0.3)">
                      <div class="g-name text-purple">BPD — Brief Psychotic Disorder</div>
                      <div class="g-desc">Sudden onset of ≥1 positive symptom lasting ≥1 day but &lt;1 month. Full return to premorbid functioning. May occur with/without marked stressor.</div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <!-- ── TOPIC: BIPOLAR & RELATED ───────────────────────────────────── -->
          <div class="topic">
            <div class="topic-header">
              <span class="topic-icon">⚡</span>
              <span class="topic-name">Bipolar &amp; Related Disorders</span>
              <span class="topic-badge">DSM-5 · 3 DISORDERS</span>
              <span class="topic-chev">▶</span>
            </div>
            <div class="topic-body">
              <div class="concept-card">
                <div class="concept-label">Bipolar Spectrum · ICD-10 F30–F31</div>
                <div class="concept-title">Disorders of Mood Polarity &amp; Energy</div>
                <div class="concept-desc">
                  Bridge between schizophrenia spectrum and depressive disorders in genetics, family history,
                  and phenomenology. Characterized by episodes of mania or hypomania, often alternating
                  with depressive episodes.
                </div>
                <div class="dw">
                  <div class="dt">▸ MANIA vs. HYPOMANIA</div>
                  <table class="ref-table" style="margin-bottom:14px">
                    <tr><th>Feature</th><th>Mania</th><th>Hypomania</th></tr>
                    <tr><td style="color:var(--amber)">Duration</td><td>≥7 days (or any if hospitalized)</td><td>≥4 consecutive days</td></tr>
                    <tr><td style="color:var(--amber)">Impairment</td><td>Marked; may require hospitalization</td><td>Noticeable change but not severe impairment</td></tr>
                    <tr><td style="color:var(--amber)">Psychosis</td><td>May occur</td><td>Absent by definition</td></tr>
                    <tr><td style="color:var(--amber)">Mood</td><td>Elevated, expansive, or irritable</td><td>Same but less severe</td></tr>
                  </table>
                  <div class="dt">▸ DISORDERS</div>
                  <div class="card-grid">
                    <div class="g-card" style="border-color:rgba(255,176,32,0.3)">
                      <div class="g-name text-amber">BPI — Bipolar I Disorder</div>
                      <div class="g-desc">≥1 manic episode. May be preceded/followed by hypomanic or major depressive episodes. Manic episode: elevated/irritable mood + increased goal-directed activity. ICD-10: F31.x</div>
                    </div>
                    <div class="g-card" style="border-color:rgba(255,176,32,0.3)">
                      <div class="g-name text-amber">BPII — Bipolar II Disorder</div>
                      <div class="g-desc">≥1 hypomanic episode + ≥1 major depressive episode. No full manic episode. Hypomanic episode ≥4 days; not severe enough to cause marked impairment. ICD-10: F31.81</div>
                    </div>
                    <div class="g-card" style="border-color:rgba(255,176,32,0.3)">
                      <div class="g-name text-amber">CYC — Cyclothymic Disorder</div>
                      <div class="g-desc">≥2 years of hypomanic AND depressive periods not meeting full episode criteria. Symptoms present ≥50% of time. ICD-10: F34.0</div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <!-- ── TOPIC: DEPRESSIVE DISORDERS ───────────────────────────────── -->
          <div class="topic">
            <div class="topic-header">
              <span class="topic-icon">🌧️</span>
              <span class="topic-name">Depressive Disorders</span>
              <span class="topic-badge">DSM-5 · 4 DISORDERS</span>
              <span class="topic-chev">▶</span>
            </div>
            <div class="topic-body">
              <div class="concept-card">
                <div class="concept-label">Unipolar Depression · ICD-10 F32–F34</div>
                <div class="concept-title">Disorders of Persistent Low Mood &amp; Anhedonia</div>
                <div class="concept-desc">
                  Common feature: sad, empty, or irritable mood with somatic and cognitive changes
                  significantly affecting capacity to function. Differs by duration, timing, and
                  presumed etiology. No manic or hypomanic episodes.
                </div>
                <div class="dw">
                  <div class="dt">▸ MDD CORE SYMPTOMS (≥5 for ≥2 weeks, including A or B)</div>
                  <div class="kc-row row-cyan">
                    <div class="kc-num text-cyan">A</div>
                    <div class="kc-phase">Depressed Mood</div>
                    <div class="kc-desc">Most of the day, nearly every day — subjective or observed</div>
                  </div>
                  <div class="kc-row row-cyan">
                    <div class="kc-num text-cyan">B</div>
                    <div class="kc-phase">Anhedonia</div>
                    <div class="kc-desc">Markedly diminished interest or pleasure in all/most activities</div>
                  </div>
                  <div class="kc-row row-amber">
                    <div class="kc-num text-amber">C–I</div>
                    <div class="kc-phase">Additional Symptoms</div>
                    <div class="kc-desc">Weight/appetite change · sleep disturbance · psychomotor agitation or retardation · fatigue · worthlessness/guilt · concentration difficulty · suicidal ideation</div>
                  </div>
                  <div class="dt" style="margin-top:14px">▸ DISORDERS</div>
                  <div class="card-grid">
                    <div class="g-card" style="border-color:rgba(0,212,255,0.3)">
                      <div class="g-name text-cyan">MDD — Major Depressive Disorder</div>
                      <div class="g-desc">≥5 symptoms for ≥2 weeks including depressed mood or anhedonia. Single or recurrent episode. ICD-10: F32.x</div>
                    </div>
                    <div class="g-card" style="border-color:rgba(0,212,255,0.3)">
                      <div class="g-name text-cyan">PDD — Persistent Depressive Disorder (Dysthymia)</div>
                      <div class="g-desc">Depressed mood most of the day, more days than not, for ≥2 years. ≥2 symptoms: appetite change, insomnia/hypersomnia, low energy, low self-esteem, concentration difficulty, hopelessness. ICD-10: F34.1</div>
                    </div>
                    <div class="g-card" style="border-color:rgba(0,212,255,0.3)">
                      <div class="g-name text-cyan">DMDD — Disruptive Mood Dysregulation Disorder</div>
                      <div class="g-desc">Severe recurrent temper outbursts + persistent irritable/angry mood ≥3×/week for ≥12 months. Onset before age 10. Diagnosis not made before 6 or after 18. ICD-10: F34.8</div>
                    </div>
                    <div class="g-card" style="border-color:rgba(0,212,255,0.3)">
                      <div class="g-name text-cyan">PMDD — Premenstrual Dysphoric Disorder</div>
                      <div class="g-desc">Marked affective lability, irritability, dysphoria, anxiety in the final week before menses, improving after onset. ≥5 symptoms confirmed by prospective daily ratings. ICD-10: F32.81</div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <!-- ── TOPIC: ANXIETY DISORDERS ───────────────────────────────────── -->
          <div class="topic">
            <div class="topic-header">
              <span class="topic-icon">😰</span>
              <span class="topic-name">Anxiety Disorders</span>
              <span class="topic-badge">DSM-5 · 7 DISORDERS</span>
              <span class="topic-chev">▶</span>
            </div>
            <div class="topic-body">
              <div class="concept-card">
                <div class="concept-label">Anxiety Spectrum · ICD-10 F40–F41</div>
                <div class="concept-title">Excessive Fear, Anxiety &amp; Avoidance</div>
                <div class="concept-desc">
                  Share features of excessive fear and anxiety with related behavioral disturbances.
                  Differ from normal fear/anxiety by being excessive or persistent beyond
                  developmentally appropriate periods.
                  <strong style="color:var(--amber)">Fear</strong> is response to real/perceived
                  imminent threat; <strong style="color:var(--amber)">Anxiety</strong> is anticipation
                  of future threat.
                </div>
                <div class="dw">
                  <div class="dt">▸ DISORDERS</div>
                  <div class="card-grid">
                    <div class="g-card" style="border-color:rgba(255,176,32,0.3)">
                      <div class="g-name text-amber">GAD — Generalized Anxiety Disorder</div>
                      <div class="g-desc">Excessive worry about multiple domains more days than not for ≥6 months, difficult to control. ≥3 symptoms: restlessness, fatigue, concentration difficulty, irritability, muscle tension, sleep disturbance. ICD-10: F41.1</div>
                    </div>
                    <div class="g-card" style="border-color:rgba(255,176,32,0.3)">
                      <div class="g-name text-amber">PD — Panic Disorder</div>
                      <div class="g-desc">Recurrent unexpected panic attacks (abrupt surge of fear peaking within minutes). Followed by ≥1 month of persistent concern or maladaptive behavior change. ICD-10: F41.0</div>
                    </div>
                    <div class="g-card" style="border-color:rgba(255,176,32,0.3)">
                      <div class="g-name text-amber">AGO — Agoraphobia</div>
                      <div class="g-desc">Marked fear/anxiety about ≥2 situations: public transit, open spaces, enclosed spaces, lines/crowds, being outside alone. Avoided or endured with intense anxiety or need for companion. ICD-10: F40.00</div>
                    </div>
                    <div class="g-card" style="border-color:rgba(255,176,32,0.3)">
                      <div class="g-name text-amber">SAD — Social Anxiety Disorder</div>
                      <div class="g-desc">Marked fear of social situations where scrutinized by others, leading to fear of humiliation or rejection. Avoided or endured with intense anxiety. ≥6 months. ICD-10: F40.10</div>
                    </div>
                    <div class="g-card" style="border-color:rgba(255,176,32,0.3)">
                      <div class="g-name text-amber">SPH — Specific Phobia</div>
                      <div class="g-desc">Marked fear about a specific object or situation (animal, natural environment, blood-injection-injury, situational, other). Fear out of proportion; typically lasting ≥6 months. ICD-10: F40.2xx</div>
                    </div>
                    <div class="g-card" style="border-color:rgba(255,176,32,0.3)">
                      <div class="g-name text-amber">SEP — Separation Anxiety Disorder</div>
                      <div class="g-desc">Excessive fear about separation from attachment figures. ≥3 symptoms: distress when separated, worry about harm to figures, reluctance to leave home, nightmares of separation. ICD-10: F93.0</div>
                    </div>
                    <div class="g-card" style="border-color:rgba(255,176,32,0.3)">
                      <div class="g-name text-amber">SM — Selective Mutism</div>
                      <div class="g-desc">Consistent failure to speak in specific social situations (e.g., school) despite speaking in others. Interferes with educational achievement. Duration ≥1 month (not first month of school). ICD-10: F94.0</div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <!-- ── TOPIC: OCD & RELATED ────────────────────────────────────────── -->
          <div class="topic">
            <div class="topic-header">
              <span class="topic-icon">🔁</span>
              <span class="topic-name">Obsessive-Compulsive &amp; Related Disorders</span>
              <span class="topic-badge">DSM-5 · 5 DISORDERS</span>
              <span class="topic-chev">▶</span>
            </div>
            <div class="topic-body">
              <div class="concept-card">
                <div class="concept-label">OCD Spectrum · ICD-10 F42–F63</div>
                <div class="concept-title">Obsessions, Compulsions &amp; Repetitive Behaviors</div>
                <div class="concept-desc">
                  Characterized by obsessions and compulsions or related repetitive behaviors.
                  Grouped based on similarities in diagnostic validators and treatment response
                  (SRIs — serotonin reuptake inhibitors).
                </div>
                <div class="dw">
                  <div class="dt">▸ OCD CORE DEFINITIONS</div>
                  <table class="ref-table" style="margin-bottom:14px">
                    <tr><th>Term</th><th>Definition</th><th>Key Feature</th></tr>
                    <tr><td style="color:var(--red)">Obsession</td><td>Recurrent, persistent thoughts/urges/images causing marked anxiety, experienced as intrusive</td><td>Ego-dystonic — unwanted by the individual</td></tr>
                    <tr><td style="color:var(--red)">Compulsion</td><td>Repetitive behaviors or mental acts aimed at reducing distress caused by obsessions</td><td>Not realistically connected to feared event</td></tr>
                  </table>
                  <div class="dt">▸ DISORDERS</div>
                  <div class="card-grid">
                    <div class="g-card" style="border-color:rgba(255,77,109,0.3)">
                      <div class="g-name text-red">OCD — Obsessive-Compulsive Disorder</div>
                      <div class="g-desc">Obsessions + compulsions. Time-consuming (&gt;1 hr/day) or causing significant impairment. Insight specifier: good/fair, poor, or absent/delusional. ICD-10: F42</div>
                    </div>
                    <div class="g-card" style="border-color:rgba(255,77,109,0.3)">
                      <div class="g-name text-red">BDD — Body Dysmorphic Disorder</div>
                      <div class="g-desc">Preoccupation with ≥1 perceived defects in physical appearance (not noticeable to others). Repetitive behaviors (mirror-checking, grooming) or mental acts in response. ICD-10: F45.22</div>
                    </div>
                    <div class="g-card" style="border-color:rgba(255,77,109,0.3)">
                      <div class="g-name text-red">HD — Hoarding Disorder</div>
                      <div class="g-desc">Persistent difficulty discarding possessions regardless of value. Accumulation clutters living areas making them unusable. Causes significant distress/impairment. ICD-10: F42</div>
                    </div>
                    <div class="g-card" style="border-color:rgba(255,77,109,0.3)">
                      <div class="g-name text-red">TTM — Trichotillomania (Hair-Pulling Disorder)</div>
                      <div class="g-desc">Recurrent pulling out of one's hair resulting in hair loss. Repeated attempts to stop. Causes significant distress/functional impairment. ICD-10: F63.3</div>
                    </div>
                    <div class="g-card" style="border-color:rgba(255,77,109,0.3)">
                      <div class="g-name text-red">EXD — Excoriation (Skin-Picking) Disorder</div>
                      <div class="g-desc">Recurrent skin picking resulting in skin lesions. Repeated attempts to stop. Not attributable to substance, medical condition, or another mental disorder. ICD-10: L98.1</div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <!-- ── TOPIC: TRAUMA & STRESSOR-RELATED ──────────────────────────── -->
          <div class="topic">
            <div class="topic-header">
              <span class="topic-icon">💥</span>
              <span class="topic-name">Trauma- &amp; Stressor-Related Disorders</span>
              <span class="topic-badge">DSM-5 · 5 DISORDERS</span>
              <span class="topic-chev">▶</span>
            </div>
            <div class="topic-body">
              <div class="concept-card">
                <div class="concept-label">Trauma Spectrum · ICD-10 F43</div>
                <div class="concept-title">Disorders Requiring Traumatic / Stressful Exposure</div>
                <div class="concept-desc">
                  Exposure to a traumatic or stressful event is explicitly listed as a diagnostic
                  criterion. Psychological distress takes varied forms: intrusive re-experiencing,
                  avoidance, negative cognition/mood, hyperarousal, or dissociation.
                </div>
                <div class="dw">
                  <div class="dt">▸ PTSD FOUR SYMPTOM CLUSTERS</div>
                  <div class="card-grid" style="grid-template-columns:repeat(auto-fit,minmax(180px,1fr));margin-bottom:14px">
                    <div class="g-card" style="border-color:rgba(255,77,109,0.3)">
                      <div class="g-name text-red">B — Intrusion</div>
                      <div class="g-desc">Flashbacks, nightmares, intrusive memories, psychological/physiological reactivity to trauma cues</div>
                    </div>
                    <div class="g-card" style="border-color:rgba(255,77,109,0.3)">
                      <div class="g-name text-red">C — Avoidance</div>
                      <div class="g-desc">Avoidance of internal (memories, thoughts) and external (people, places, situations) trauma reminders</div>
                    </div>
                    <div class="g-card" style="border-color:rgba(255,77,109,0.3)">
                      <div class="g-name text-red">D — Negative Cognition/Mood</div>
                      <div class="g-desc">Persistent negative beliefs, distorted blame, persistent negative emotions, anhedonia, detachment, inability to experience positive affect</div>
                    </div>
                    <div class="g-card" style="border-color:rgba(255,77,109,0.3)">
                      <div class="g-name text-red">E — Alterations in Arousal</div>
                      <div class="g-desc">Irritability, reckless behavior, hypervigilance, exaggerated startle, concentration difficulty, sleep disturbance</div>
                    </div>
                  </div>
                  <div class="dt">▸ DISORDERS</div>
                  <div class="card-grid">
                    <div class="g-card" style="border-color:rgba(255,77,109,0.3)">
                      <div class="g-name text-red">PTSD — Posttraumatic Stress Disorder</div>
                      <div class="g-desc">Exposure to actual/threatened death, serious injury, or sexual violence. All four clusters (B–E). Duration &gt;1 month. ICD-10: F43.10</div>
                    </div>
                    <div class="g-card" style="border-color:rgba(255,77,109,0.3)">
                      <div class="g-name text-red">ASD — Acute Stress Disorder</div>
                      <div class="g-desc">Same trauma exposure; ≥9 symptoms across five clusters including dissociation. Duration 3 days–1 month. If persists beyond 1 month → PTSD. ICD-10: F43.0</div>
                    </div>
                    <div class="g-card" style="border-color:rgba(255,77,109,0.3)">
                      <div class="g-name text-red">ADJ — Adjustment Disorders</div>
                      <div class="g-desc">Emotional/behavioral symptoms in response to an identifiable stressor within 3 months. Marked distress out of proportion. Resolves within 6 months of stressor cessation. ICD-10: F43.2x</div>
                    </div>
                    <div class="g-card" style="border-color:rgba(255,77,109,0.3)">
                      <div class="g-name text-red">RAD — Reactive Attachment Disorder</div>
                      <div class="g-desc">Consistent pattern of inhibited, emotionally withdrawn behavior toward adult caregivers. Result of social neglect or insufficient early caregiving. ICD-10: F94.1</div>
                    </div>
                    <div class="g-card" style="border-color:rgba(255,77,109,0.3)">
                      <div class="g-name text-red">DSED — Disinhibited Social Engagement Disorder</div>
                      <div class="g-desc">Child actively approaches/interacts with unfamiliar adults without expected cultural reticence. Overly familiar verbal/physical behavior. ICD-10: F94.2</div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <!-- ── TOPIC: DISSOCIATIVE DISORDERS ──────────────────────────────── -->
          <div class="topic">
            <div class="topic-header">
              <span class="topic-icon">🪞</span>
              <span class="topic-name">Dissociative Disorders</span>
              <span class="topic-badge">DSM-5 · 3 DISORDERS</span>
              <span class="topic-chev">▶</span>
            </div>
            <div class="topic-body">
              <div class="concept-card">
                <div class="concept-label">Dissociative Spectrum · ICD-10 F44–F48</div>
                <div class="concept-title">Disruption of Consciousness, Identity &amp; Memory</div>
                <div class="concept-desc">
                  Disruption and/or discontinuity in the normal integration of
                  consciousness, memory, identity, emotion, perception, behavior, and sense of self.
                  Symptoms cause significant distress or functional impairment.
                  Often associated with trauma history.
                </div>
                <div class="dw">
                  <div class="dt">▸ DISORDERS</div>
                  <div class="card-grid">
                    <div class="g-card" style="border-color:rgba(168,85,247,0.3)">
                      <div class="g-name text-purple">DID — Dissociative Identity Disorder</div>
                      <div class="g-desc">Disruption of identity characterized by ≥2 distinct personality states (or, in some cultures, possession experiences). Recurrent gaps in recall of everyday events, personal information, or traumatic events. ICD-10: F44.81</div>
                    </div>
                    <div class="g-card" style="border-color:rgba(168,85,247,0.3)">
                      <div class="g-name text-purple">DA — Dissociative Amnesia</div>
                      <div class="g-desc">Inability to recall important autobiographical information, usually traumatic, inconsistent with ordinary forgetting. May include dissociative fugue: purposeful travel associated with amnesia. ICD-10: F44.0</div>
                    </div>
                    <div class="g-card" style="border-color:rgba(168,85,247,0.3)">
                      <div class="g-name text-purple">DPDR — Depersonalization/Derealization Disorder</div>
                      <div class="g-desc">Persistent/recurrent depersonalization (detachment from one's mental processes or body) and/or derealization (detachment from surroundings). Reality testing remains intact. ICD-10: F48.1</div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <!-- ── TOPIC: SOMATIC SYMPTOM DISORDERS ───────────────────────────── -->
          <div class="topic">
            <div class="topic-header">
              <span class="topic-icon">🤒</span>
              <span class="topic-name">Somatic Symptom &amp; Related Disorders</span>
              <span class="topic-badge">DSM-5 · 4 DISORDERS</span>
              <span class="topic-chev">▶</span>
            </div>
            <div class="topic-body">
              <div class="concept-card">
                <div class="concept-label">Somatic Spectrum · ICD-10 F45</div>
                <div class="concept-title">Prominent Somatic Symptoms with Psychological Features</div>
                <div class="concept-desc">
                  All have prominent somatic symptoms associated with significant distress and impairment.
                  DSM-5 emphasizes positive symptoms (distressing thoughts, feelings, behaviors) rather
                  than medically unexplained symptoms as the defining feature.
                </div>
                <div class="dw">
                  <div class="dt">▸ DISORDERS</div>
                  <div class="card-grid">
                    <div class="g-card" style="border-color:rgba(0,255,153,0.3)">
                      <div class="g-name text-green">SSD — Somatic Symptom Disorder</div>
                      <div class="g-desc">≥1 distressing somatic symptom + disproportionate/persistent thoughts about seriousness, high anxiety, or excessive time/energy devoted to symptoms. ≥6 months. ICD-10: F45.1</div>
                    </div>
                    <div class="g-card" style="border-color:rgba(0,255,153,0.3)">
                      <div class="g-name text-green">IAD — Illness Anxiety Disorder (Hypochondria)</div>
                      <div class="g-desc">Preoccupation with having or acquiring a serious illness. Somatic symptoms absent or mild. High health-related anxiety. Excessive health behaviors or maladaptive avoidance. ≥6 months. ICD-10: F45.21</div>
                    </div>
                    <div class="g-card" style="border-color:rgba(0,255,153,0.3)">
                      <div class="g-name text-green">FCD — Functional Neurological Symptom Disorder (Conversion)</div>
                      <div class="g-desc">≥1 symptom of altered voluntary motor or sensory function. Clinical findings incompatible with recognized neurological conditions. Includes non-epileptic seizures, functional weakness, sensory loss. ICD-10: F44.x</div>
                    </div>
                    <div class="g-card" style="border-color:rgba(0,255,153,0.3)">
                      <div class="g-name text-green">FAD — Factitious Disorder</div>
                      <div class="g-desc">Falsification of physical/psychological signs or induction of injury/disease, in self or another. Deceptive behavior evident even without obvious external rewards. ICD-10: F68.10</div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <!-- ── TOPIC: FEEDING & EATING DISORDERS ──────────────────────────── -->
          <div class="topic">
            <div class="topic-header">
              <span class="topic-icon">🍽️</span>
              <span class="topic-name">Feeding &amp; Eating Disorders</span>
              <span class="topic-badge">DSM-5 · 6 DISORDERS</span>
              <span class="topic-chev">▶</span>
            </div>
            <div class="topic-body">
              <div class="concept-card">
                <div class="concept-label">Eating Disorders · ICD-10 F50 / F98</div>
                <div class="concept-title">Disturbed Eating Behavior &amp; Body Image</div>
                <div class="concept-desc">
                  Persistent disturbance of eating or eating-related behavior that significantly impairs
                  physical health or psychosocial functioning. Among the highest mortality rates of any
                  psychiatric disorder (particularly Anorexia Nervosa).
                </div>
                <div class="dw">
                  <div class="dt">▸ DISORDERS</div>
                  <div class="card-grid">
                    <div class="g-card" style="border-color:rgba(255,176,32,0.3)">
                      <div class="g-name text-amber">AN — Anorexia Nervosa</div>
                      <div class="g-desc">Restriction of energy intake → significantly low body weight. Intense fear of gaining weight. Disturbed body image. Subtypes: Restricting; Binge-Eating/Purging. ICD-10: F50.0x</div>
                    </div>
                    <div class="g-card" style="border-color:rgba(255,176,32,0.3)">
                      <div class="g-name text-amber">BN — Bulimia Nervosa</div>
                      <div class="g-desc">Recurrent binge eating + recurrent compensatory behaviors (purging, fasting, excessive exercise). ≥1×/week × 3 months. Self-evaluation unduly influenced by body shape/weight. ICD-10: F50.2</div>
                    </div>
                    <div class="g-card" style="border-color:rgba(255,176,32,0.3)">
                      <div class="g-name text-amber">BED — Binge-Eating Disorder</div>
                      <div class="g-desc">Recurrent binge eating without compensatory behaviors. ≥3 of: eating rapidly, eating until uncomfortably full, eating when not hungry, eating alone from embarrassment, feeling disgusted/guilty. ≥1×/week × 3 months. ICD-10: F50.8</div>
                    </div>
                    <div class="g-card" style="border-color:rgba(255,176,32,0.3)">
                      <div class="g-name text-amber">ARFID — Avoidant/Restrictive Food Intake Disorder</div>
                      <div class="g-desc">Significant weight loss, nutritional deficiency, dependence on supplements, or marked psychosocial impairment. Not explained by food unavailability or cultural practice. Not driven by body image. ICD-10: F50.8</div>
                    </div>
                    <div class="g-card" style="border-color:rgba(255,176,32,0.3)">
                      <div class="g-name text-amber">PICA — Pica</div>
                      <div class="g-desc">Persistent eating of nonnutritive, nonfood substances (dirt, clay, paper, hair, chalk) ≥1 month. Inappropriate to developmental level. Not culturally normative. ICD-10: F98.3</div>
                    </div>
                    <div class="g-card" style="border-color:rgba(255,176,32,0.3)">
                      <div class="g-name text-amber">RD — Rumination Disorder</div>
                      <div class="g-desc">Repeated regurgitation of food ≥1 month. Regurgitated food may be re-chewed, re-swallowed, or spit out. Not due to a GI or medical condition. ICD-10: F98.21</div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <!-- ── TOPIC: SLEEP-WAKE DISORDERS ────────────────────────────────── -->
          <div class="topic">
            <div class="topic-header">
              <span class="topic-icon">😴</span>
              <span class="topic-name">Sleep-Wake Disorders</span>
              <span class="topic-badge">DSM-5 · 6 CATEGORIES</span>
              <span class="topic-chev">▶</span>
            </div>
            <div class="topic-body">
              <div class="concept-card">
                <div class="concept-label">Sleep Disorders · ICD-10 F51 / G47</div>
                <div class="concept-title">Dyssomnias, Parasomnias &amp; Sleep-Related Movement Disorders</div>
                <div class="concept-desc">
                  Dissatisfaction with sleep quality/quantity occurring alongside medical and mental
                  health conditions. Grouped as: <strong style="color:var(--cyan)">dyssomnias</strong>
                  (sleep amount/quality/timing),
                  <strong style="color:var(--cyan)">parasomnias</strong> (abnormal events during sleep),
                  and <strong style="color:var(--cyan)">sleep-related movement disorders</strong>.
                </div>
                <div class="dw">
                  <div class="dt">▸ DISORDERS</div>
                  <div class="card-grid">
                    <div class="g-card" style="border-color:rgba(0,212,255,0.3)">
                      <div class="g-name text-cyan">INS — Insomnia Disorder</div>
                      <div class="g-desc">Dissatisfaction with sleep with ≥1 symptom: difficulty initiating, maintaining sleep, or early-morning awakening. ≥3 nights/week × 3 months despite adequate opportunity. ICD-10: F51.01</div>
                    </div>
                    <div class="g-card" style="border-color:rgba(0,212,255,0.3)">
                      <div class="g-name text-cyan">HYP — Hypersomnolence Disorder</div>
                      <div class="g-desc">Excessive sleepiness despite ≥7 hrs sleep + ≥1 of: recurrent daytime sleep, prolonged non-restorative sleep (&gt;9 hrs), difficulty being fully awake after abrupt awakening. ≥3×/week × 3 months. ICD-10: F51.11</div>
                    </div>
                    <div class="g-card" style="border-color:rgba(0,212,255,0.3)">
                      <div class="g-name text-cyan">NAR — Narcolepsy</div>
                      <div class="g-desc">Recurrent lapses into sleep + cataplexy (brief loss of muscle tone triggered by emotions) or hypocretin deficiency. Sleep paralysis and hypnagogic/hypnopompic hallucinations. ICD-10: G47.4x</div>
                    </div>
                    <div class="g-card" style="border-color:rgba(0,212,255,0.3)">
                      <div class="g-name text-cyan">CRD — Circadian Rhythm Sleep-Wake Disorders</div>
                      <div class="g-desc">Persistent/recurrent disruption due to misalignment between endogenous circadian rhythm and required sleep-wake schedule. Types: delayed/advanced sleep phase, irregular, non-24-hour, shift work, jet lag. ICD-10: G47.2x</div>
                    </div>
                    <div class="g-card" style="border-color:rgba(0,212,255,0.3)">
                      <div class="g-name text-cyan">PARA — Parasomnias</div>
                      <div class="g-desc">Non-REM Arousal Disorders: sleepwalking, sleep terrors. REM Sleep Behavior Disorder: complex motor behaviors during REM. Nightmare Disorder: recurrent disturbing dreams. Restless Legs Syndrome: urge to move legs.</div>
                    </div>
                    <div class="g-card" style="border-color:rgba(0,212,255,0.3)">
                      <div class="g-name text-cyan">OSA — Sleep-Related Breathing Disorders</div>
                      <div class="g-desc">Obstructive Sleep Apnea: ≥15 obstructive apneas/hypopneas/hr (or ≥5 with symptoms). Central Sleep Apnea: repetitive cessation without respiratory effort. Sleep-Related Hypoventilation. ICD-10: G47.3x</div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <!-- ── TOPIC: DISRUPTIVE & IMPULSE-CONTROL ────────────────────────── -->
          <div class="topic">
            <div class="topic-header">
              <span class="topic-icon">💢</span>
              <span class="topic-name">Disruptive, Impulse-Control &amp; Conduct Disorders</span>
              <span class="topic-badge">DSM-5 · 5 DISORDERS</span>
              <span class="topic-chev">▶</span>
            </div>
            <div class="topic-body">
              <div class="concept-card">
                <div class="concept-label">Disruptive Disorders · ICD-10 F63 / F91</div>
                <div class="concept-title">Problems in Self-Regulation of Emotions &amp; Behaviors</div>
                <div class="concept-desc">
                  Behaviors violate the rights of others and/or conflict with major societal
                  norms or authority figures. More prevalent in males. Onset typically in
                  childhood/adolescence. Often co-occur with ADHD and mood disorders.
                </div>
                <div class="dw">
                  <div class="dt">▸ DISORDERS</div>
                  <div class="card-grid">
                    <div class="g-card" style="border-color:rgba(255,77,109,0.3)">
                      <div class="g-name text-red">ODD — Oppositional Defiant Disorder</div>
                      <div class="g-desc">Angry/irritable mood + argumentative/defiant behavior + vindictiveness. ≥4 symptoms for ≥6 months. Often precedes Conduct Disorder. ICD-10: F91.3</div>
                    </div>
                    <div class="g-card" style="border-color:rgba(255,77,109,0.3)">
                      <div class="g-name text-red">IED — Intermittent Explosive Disorder</div>
                      <div class="g-desc">Recurrent outbursts — failure to control aggressive impulses. Grossly out of proportion to provocation. ≥2×/week × 3 months (verbal) or 3 episodes in 12 months (physical). ICD-10: F63.81</div>
                    </div>
                    <div class="g-card" style="border-color:rgba(255,77,109,0.3)">
                      <div class="g-name text-red">CD — Conduct Disorder</div>
                      <div class="g-desc">Repetitive/persistent pattern violating basic rights of others or age-appropriate norms. ≥3 of 15 criteria across: aggression, property destruction, deceitfulness/theft, serious rule violations. ICD-10: F91.x</div>
                    </div>
                    <div class="g-card" style="border-color:rgba(255,77,109,0.3)">
                      <div class="g-name text-red">PYR — Pyromania</div>
                      <div class="g-desc">Deliberate fire setting ≥2 occasions. Tension/arousal before; fascination with fire; pleasure/relief when setting fires. Not for monetary gain, revenge, or political reasons. ICD-10: F63.1</div>
                    </div>
                    <div class="g-card" style="border-color:rgba(255,77,109,0.3)">
                      <div class="g-name text-red">KLP — Kleptomania</div>
                      <div class="g-desc">Recurrent failure to resist stealing objects not needed for personal use or monetary value. Increasing tension before; pleasure/relief at the time of theft. ICD-10: F63.2</div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <!-- ── TOPIC: SUBSTANCE-RELATED & ADDICTIVE ───────────────────────── -->
          <div class="topic">
            <div class="topic-header">
              <span class="topic-icon">💊</span>
              <span class="topic-name">Substance-Related &amp; Addictive Disorders</span>
              <span class="topic-badge">DSM-5 · 10 SUBSTANCES + GAMBLING</span>
              <span class="topic-chev">▶</span>
            </div>
            <div class="topic-body">
              <div class="concept-card">
                <div class="concept-label">Substance Use Disorders · ICD-10 F10–F19 / F63</div>
                <div class="concept-title">Impaired Control, Social Impairment &amp; Pharmacological Criteria</div>
                <div class="concept-desc">
                  DSM-5 merged "abuse" and "dependence" into a single Use Disorder diagnosis.
                  Severity: <strong style="color:var(--amber)">Mild</strong> (2–3 criteria) /
                  <strong style="color:var(--amber)">Moderate</strong> (4–5) /
                  <strong style="color:var(--amber)">Severe</strong> (≥6 of 11 criteria).
                </div>
                <div class="dw">
                  <div class="dt">▸ 11 DIAGNOSTIC CRITERIA (across 4 clusters)</div>
                  <table class="ref-table" style="margin-bottom:14px">
                    <tr><th>Cluster</th><th>Criteria</th></tr>
                    <tr><td style="color:var(--amber)">Impaired Control</td><td>Taking more than intended · Unsuccessful efforts to cut down · Great time spent · Craving</td></tr>
                    <tr><td style="color:var(--amber)">Social Impairment</td><td>Failure to fulfil major role obligations · Persistent social/interpersonal problems · Giving up activities</td></tr>
                    <tr><td style="color:var(--amber)">Risky Use</td><td>Use in physically hazardous situations · Use despite persistent physical/psychological problems</td></tr>
                    <tr><td style="color:var(--amber)">Pharmacological</td><td>Tolerance (markedly increased amounts for same effect) · Withdrawal symptoms</td></tr>
                  </table>
                  <div class="dt">▸ KEY SUBSTANCE DISORDERS</div>
                  <div class="card-grid">
                    <div class="g-card" style="border-color:rgba(255,176,32,0.3)">
                      <div class="g-name text-amber">AUD — Alcohol Use Disorder</div>
                      <div class="g-desc">Withdrawal: autonomic hyperactivity, tremor, insomnia, nausea, hallucinations, seizures. Life-threatening. ICD-10: F10.xx</div>
                    </div>
                    <div class="g-card" style="border-color:rgba(255,176,32,0.3)">
                      <div class="g-name text-amber">OUD — Opioid Use Disorder</div>
                      <div class="g-desc">Withdrawal: dysphoric mood, nausea, muscle aches, insomnia, fever. High overdose mortality. Treatments: buprenorphine, methadone, naltrexone. ICD-10: F11.xx</div>
                    </div>
                    <div class="g-card" style="border-color:rgba(255,176,32,0.3)">
                      <div class="g-name text-amber">SUD — Stimulant Use Disorder</div>
                      <div class="g-desc">Amphetamines, cocaine, other stimulants. Withdrawal: fatigue, vivid dreams, increased sleep/appetite, psychomotor retardation. ICD-10: F14.xx / F15.xx</div>
                    </div>
                    <div class="g-card" style="border-color:rgba(255,176,32,0.3)">
                      <div class="g-name text-amber">CUD — Cannabis Use Disorder</div>
                      <div class="g-desc">First recognized cannabis withdrawal in DSM-5: irritability, anxiety, sleep difficulty, decreased appetite, restlessness. ICD-10: F12.xx</div>
                    </div>
                    <div class="g-card" style="border-color:rgba(255,176,32,0.3)">
                      <div class="g-name text-amber">SedUD — Sedative, Hypnotic or Anxiolytic Use Disorder</div>
                      <div class="g-desc">Benzodiazepines, barbiturates, sleep aids. Withdrawal can be life-threatening: seizures, autonomic instability. Similar to alcohol withdrawal. ICD-10: F13.xx</div>
                    </div>
                    <div class="g-card" style="border-color:rgba(255,176,32,0.3)">
                      <div class="g-name text-amber">GD — Gambling Disorder</div>
                      <div class="g-desc">Only behavioral addiction in DSM-5. ≥4 of 9 criteria × 12 months: increasing bets, restless when cutting back, preoccupied, chases losses, lies, jeopardizes relationships. ICD-10: F63.0</div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <!-- ── TOPIC: NEUROCOGNITIVE DISORDERS ────────────────────────────── -->
          <div class="topic">
            <div class="topic-header">
              <span class="topic-icon">🧠</span>
              <span class="topic-name">Neurocognitive Disorders</span>
              <span class="topic-badge">DSM-5 · 3 CATEGORIES</span>
              <span class="topic-chev">▶</span>
            </div>
            <div class="topic-body">
              <div class="concept-card">
                <div class="concept-label">Neurocognitive · ICD-10 F02–F05 / G31</div>
                <div class="concept-title">Acquired Decline in Cognitive Performance</div>
                <div class="concept-desc">
                  Characterized by a <strong style="color:var(--cyan)">decline from a prior level</strong>
                  of cognitive performance in one or more cognitive domains:
                  complex attention, executive function, learning/memory, language,
                  perceptual-motor, or social cognition.
                </div>
                <div class="dw">
                  <div class="dt">▸ SIX COGNITIVE DOMAINS</div>
                  <div class="card-grid" style="grid-template-columns:repeat(auto-fit,minmax(160px,1fr));margin-bottom:14px">
                    <div class="g-card" style="border-color:rgba(0,212,255,0.2)"><div class="g-name text-cyan">Complex Attention</div><div class="g-desc">Sustained, divided, selective attention; processing speed</div></div>
                    <div class="g-card" style="border-color:rgba(0,212,255,0.2)"><div class="g-name text-cyan">Executive Function</div><div class="g-desc">Planning, decision-making, working memory, responding to feedback</div></div>
                    <div class="g-card" style="border-color:rgba(0,212,255,0.2)"><div class="g-name text-cyan">Learning &amp; Memory</div><div class="g-desc">Free recall, cued recall, recognition memory, semantic/autobiographical memory</div></div>
                    <div class="g-card" style="border-color:rgba(0,212,255,0.2)"><div class="g-name text-cyan">Language</div><div class="g-desc">Expressive language, naming, fluency, grammar, receptive language</div></div>
                    <div class="g-card" style="border-color:rgba(0,212,255,0.2)"><div class="g-name text-cyan">Perceptual-Motor</div><div class="g-desc">Visual perception, visuoconstructional ability, perceptual-motor integration</div></div>
                    <div class="g-card" style="border-color:rgba(0,212,255,0.2)"><div class="g-name text-cyan">Social Cognition</div><div class="g-desc">Recognition of emotions, theory of mind, insight into others' mental states</div></div>
                  </div>
                  <div class="dt">▸ DISORDERS</div>
                  <div class="card-grid">
                    <div class="g-card" style="border-color:rgba(0,212,255,0.3)">
                      <div class="g-name text-cyan">DEL — Delirium</div>
                      <div class="g-desc">Disturbance in attention and awareness developing over hours to days with additional cognitive disturbance. Fluctuates. Direct physiological cause (medical, substance, withdrawal). ICD-10: F05</div>
                    </div>
                    <div class="g-card" style="border-color:rgba(0,212,255,0.3)">
                      <div class="g-name text-cyan">MaND — Major Neurocognitive Disorder (Dementia)</div>
                      <div class="g-desc">Significant cognitive decline in ≥1 domain, interfering with independence. Etiological subtypes: Alzheimer's (most common), Vascular, Lewy Body, Frontotemporal, TBI, HIV, Parkinson's, Huntington's. ICD-10: F02.xx</div>
                    </div>
                    <div class="g-card" style="border-color:rgba(0,212,255,0.3)">
                      <div class="g-name text-cyan">MiND — Mild Neurocognitive Disorder (MCI)</div>
                      <div class="g-desc">Modest cognitive decline in ≥1 domain without interference with independence (but may require greater effort/compensatory strategies). Does not meet criteria for major NCD. ICD-10: G31.84</div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <!-- ── TOPIC: PERSONALITY DISORDERS ───────────────────────────────── -->
          <div class="topic">
            <div class="topic-header">
              <span class="topic-icon">🎭</span>
              <span class="topic-name">Personality Disorders</span>
              <span class="topic-badge">DSM-5 · 10 DISORDERS</span>
              <span class="topic-chev">▶</span>
            </div>
            <div class="topic-body">
              <div class="concept-card">
                <div class="concept-label">Personality Disorders · ICD-10 F60–F61</div>
                <div class="concept-title">Enduring Patterns of Inner Experience &amp; Behavior</div>
                <div class="concept-desc">
                  Enduring pattern deviating markedly from cultural expectations; pervasive and inflexible;
                  onset in adolescence or early adulthood; stable over time; causing distress or impairment.
                  Three clusters based on descriptive similarities.
                </div>
                <div class="dw">
                  <div class="dt">▸ THREE CLUSTERS</div>
                  <div class="card-grid">
                    <div class="g-card" style="border-color:rgba(168,85,247,0.3)">
                      <div class="g-name text-purple">Cluster A — Odd / Eccentric</div>
                      <div class="g-desc">
                        <strong>Paranoid PD (F60.0)</strong> — Pervasive distrust; others' motives interpreted as malevolent.<br>
                        <strong>Schizoid PD (F60.1)</strong> — Detachment from social relationships; restricted emotional expression.<br>
                        <strong>Schizotypal PD (F21)</strong> — Discomfort with close relationships + cognitive/perceptual distortions + eccentricities.
                      </div>
                    </div>
                    <div class="g-card" style="border-color:rgba(255,77,109,0.3)">
                      <div class="g-name text-red">Cluster B — Dramatic / Emotional / Erratic</div>
                      <div class="g-desc">
                        <strong>Antisocial PD (F60.2)</strong> — Disregard/violation of others' rights since age 15. Must be ≥18.<br>
                        <strong>Borderline PD (F60.3)</strong> — Instability in relationships, self-image, affect + impulsivity.<br>
                        <strong>Histrionic PD (F60.4)</strong> — Excessive emotionality and attention-seeking.<br>
                        <strong>Narcissistic PD (F60.81)</strong> — Grandiosity, need for admiration, lack of empathy.
                      </div>
                    </div>
                    <div class="g-card" style="border-color:rgba(0,212,255,0.3)">
                      <div class="g-name text-cyan">Cluster C — Anxious / Fearful</div>
                      <div class="g-desc">
                        <strong>Avoidant PD (F60.6)</strong> — Social inhibition, feelings of inadequacy, hypersensitivity to negative evaluation.<br>
                        <strong>Dependent PD (F60.7)</strong> — Excessive need to be cared for; submissive, clinging.<br>
                        <strong>OCPD (F60.5)</strong> — Preoccupation with orderliness, perfectionism, control (distinct from OCD).
                      </div>
                    </div>
                  </div>
                  <div class="dt" style="margin-top:14px">▸ GENERAL DIAGNOSTIC REQUIREMENTS</div>
                  <table class="ref-table">
                    <tr><th>Criterion</th><th>Requirement</th></tr>
                    <tr><td style="color:var(--purple)">Pattern</td><td>Enduring; manifests in ≥2 of: cognition, affectivity, interpersonal functioning, impulse control</td></tr>
                    <tr><td style="color:var(--purple)">Pervasiveness</td><td>Inflexible across a broad range of personal and social situations</td></tr>
                    <tr><td style="color:var(--purple)">Onset</td><td>Traced back at least to adolescence or early adulthood</td></tr>
                    <tr><td style="color:var(--purple)">Stability</td><td>Long duration; not due to another mental disorder, substance, or medical condition</td></tr>
                    <tr><td style="color:var(--purple)">Impairment</td><td>Significant distress or impairment in social, occupational, or other important areas of functioning</td></tr>
                  </table>
                </div>
              </div>
            </div>
          </div>

          <!-- /mental-disorders-dsm5 -->
'''

# ── patch logic ───────────────────────────────────────────────────────────────

def cleanup_old_injection(src):
    """Remove malformed topic-card blocks injected by patch_mental_disorders.py."""
    # Look for the old injection marker with any amount of leading whitespace
    pattern = re.compile(
        r'\n\s*<!-- ── Neurodevelopmental ── -->\s*\n.*?(?=\n</section>)',
        re.DOTALL
    )
    cleaned, count = pattern.subn('', src)
    return cleaned, count > 0


def patch_lifestyle(src):
    # Guard: already properly patched
    if GUARD in src:
        return src, False, 'already patched'

    # Step 1: clean up any previous wrong injection
    src, was_cleaned = cleanup_old_injection(src)
    cleanup_note = ' (removed old malformed injection)' if was_cleaned else ''

    # Step 2: find injection anchor
    if INJECT_AFTER not in src:
        return src, False, f'anchor "{INJECT_AFTER}" not found in file'

    # Step 3: inject after the anchor
    src = src.replace(INJECT_AFTER, INJECT_AFTER + '\n' + TOPICS_HTML, 1)
    return src, True, 'ok' + cleanup_note


# ── stage 1: P1 runner ────────────────────────────────────────────────────────

def run_p1(dry: bool) -> bool:
    """Apply this script's own DSM-5 base injection. Returns True on success."""
    if not TARGET.exists():
        print(f'[ERROR] {TARGET}: file not found')
        return False

    try:
        orig = read(TARGET)
        patched, changed, msg = patch_lifestyle(orig)

        status = 'CHANGED' if changed else 'SKIP'
        print(f'  [{status}] {TARGET.name}: {msg}')

        if changed and not dry:
            backup = TARGET.with_suffix('.html.bak')
            shutil.copy(TARGET, backup)
            write(TARGET, patched)
            print(f'         wrote {TARGET.name}  (backup: {backup.name})')

        return True

    except Exception as e:
        print(f'  [ERROR] {TARGET.name}: {e}')
        return False


# ── stage 2: sub-patch discovery & runner ─────────────────────────────────────

def discover_subpatches() -> list:
    """Return sorted list of patch_*.py files in this directory, excluding self."""
    this = Path(__file__).resolve()
    return sorted(
        p for p in HERE.glob('patch_*.py')
        if p.resolve() != this
    )


def run_subpatch(script: Path, dry: bool) -> bool:
    """
    Execute a sub-patch script. Each sub-patch uses absolute paths derived
    from its own __file__, so no cwd override is needed.
    Returns True if the script exited 0.
    """
    cmd = [sys.executable, str(script)]
    if dry:
        cmd.append('--dry-run')

    result = subprocess.run(cmd)
    return result.returncode == 0


# ── main ──────────────────────────────────────────────────────────────────────

def main():
    dry     = '--dry-run' in sys.argv
    p1_only = '--p1-only' in sys.argv

    root = HERE.parent
    mode = 'DRY RUN — no files will be written' if dry else 'APPLY mode'
    print(f'\n══ Mental Disorders patch runner  ({mode}) ══')
    print(f'   html : {root / "data" / "lifestyle.html"}')
    print(f'   css  : {root / "style.css"}')
    print(f'   js   : {root / "script.js"}')
    print(f'   patches: {HERE}\n')

    # ── Stage 1: P1 (this script) ─────────────────────────────────────────────
    print('── Stage 1: P1 base injection (patch_mental_disorders_lifestyle.py)')
    p1_ok = run_p1(dry)
    print()

    if p1_only:
        print('── --p1-only flag set, stopping after P1.')
        sys.exit(0 if p1_ok else 1)

    # ── Stage 2: sub-patches ──────────────────────────────────────────────────
    subpatches = discover_subpatches()
    if not subpatches:
        print('── Stage 2: no additional patch_*.py files found — done.\n')
        sys.exit(0 if p1_ok else 1)

    print(f'── Stage 2: running {len(subpatches)} sub-patch(es) (cwd → data/)\n')
    failures = []

    for script in subpatches:
        print(f'   ── {script.name}')
        ok = run_subpatch(script, dry)
        if not ok:
            # Non-zero exit is common when CSS/JS target files don't exist yet;
            # log as a warning and continue rather than aborting the chain.
            print(f'   [WARN] {script.name} exited non-zero '
                  f'(HTML changes may still have applied — check output above)')
            failures.append(script.name)
        print()

    # ── Summary ───────────────────────────────────────────────────────────────
    total   = 1 + len(subpatches)
    passed  = total - (0 if p1_ok else 1) - len(failures)
    print(f'══ Done: {passed}/{total} patches clean', end='')
    if failures:
        print(f'  |  warnings: {", ".join(failures)}', end='')
    print(' ══\n')

    if dry:
        print('-- dry run complete, no files written --\n')

    sys.exit(0 if (p1_ok and not failures) else 1)


if __name__ == '__main__':
    main()
