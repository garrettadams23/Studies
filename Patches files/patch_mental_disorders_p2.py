#!/usr/bin/env python3
"""
Patch P2: fill DSM-5 gaps in Mental Disorders section
  - Expands Substance section (adds Caffeine, Hallucinogens, Inhalants, Tobacco)
  - Adds Medication-Induced Movement Disorders topic
  - Adds Other Conditions (V/Z-codes) topic
  - Adds Conditions for Further Study topic (Section III)
Requires Part 1 (patch_mental_disorders.py) to already be applied.
"""
import re, sys, shutil
from pathlib import Path

FILES  = {"html": "index.html", "css": "style.css", "js": "script.js"}
GUARD  = "mental-disorders-p2"
# Insert these new topics just before the closing domain sentinel
CLOSE_ANCHOR = "<!-- /mental-disorders-domain -->"

# ── additional substance cards ────────────────────────────────────────────────
# We inject these inside the existing Substance topic-body, after the GD card.
SUBSTANCE_ANCHOR = "<!-- /substance-cards -->"  # we also add this marker in p1's topic

# Since p1 doesn't have that sentinel, we target unique text near the GD card close
SUBSTANCE_INSERT_AFTER = '<span class="concept-label">GD</span>'  # first occurrence end of GD card

NEW_SUBSTANCE_CARDS = '''
        <div class="concept-card"><span class="concept-label">CUD-H</span><div class="concept-title">Hallucinogen Use Disorder</div><div class="concept-desc">Covers PCP (phencyclidine) and other hallucinogens (LSD, peyote, psilocybin). No clinically significant withdrawal syndrome for most. Unique complication: <strong>Hallucinogen Persisting Perception Disorder (HPPD)</strong> — re-experiencing perceptual symptoms (flashbacks) long after last use. ICD-10: F16.xx</div></div>
        <div class="concept-card"><span class="concept-label">IUD</span><div class="concept-title">Inhalant Use Disorder</div><div class="concept-desc">Problematic use of hydrocarbon-based inhalants (solvents, fuels, aerosols, nitrous oxide). Rapid CNS depression; no formal withdrawal syndrome. Associated with significant neurotoxicity and cognitive impairment. Higher prevalence in adolescents and low-income populations. ICD-10: F18.xx</div></div>
        <div class="concept-card"><span class="concept-label">TUD</span><div class="concept-title">Tobacco Use Disorder</div><div class="concept-desc">Problematic tobacco use with ≥2 criteria in 12 months. Withdrawal: irritability, anxiety, difficulty concentrating, increased appetite, restlessness, depressed mood, insomnia — onset within 24 hours of cessation. Specifiers: on maintenance therapy, in controlled environment. ICD-10: F17.2xx</div></div>
        <div class="concept-card"><span class="concept-label">CAF</span><div class="concept-title">Caffeine-Related Disorders</div><div class="concept-desc">No "Caffeine Use Disorder" in DSM-5 (listed for further study). <strong>Intoxication (F15.929):</strong> ≥250 mg → ≥5 of: restlessness, nervousness, insomnia, flushed face, diuresis, GI upset, tachycardia, psychomotor agitation. <strong>Withdrawal (F15.93):</strong> headache, fatigue, dysphoria, difficulty concentrating, flu-like symptoms within 24 hrs of cessation.</div></div>'''

# ── new topic blocks to append before closing anchor ─────────────────────────
NEW_TOPICS_HTML = '''
  <!-- ── Medication-Induced Movement Disorders ── -->
  <div class="topic-card">
    <div class="topic-header">
      <span class="topic-icon">💉</span>
      <span class="topic-name">Medication-Induced Movement Disorders</span>
      <span class="topic-badge">7 conditions</span>
      <span class="chevron">▾</span>
    </div>
    <div class="topic-body">
      <p class="topic-desc">Not mental disorders per se but clinically significant conditions caused by medications (primarily antipsychotics, antidepressants, antiemetics). Included in DSM-5 because they must be differentiated from primary psychiatric disorders and affect clinical management.</p>
      <div class="card-grid">
        <div class="concept-card"><span class="concept-label">NMS</span><div class="concept-title">Neuroleptic Malignant Syndrome</div><div class="concept-desc">Life-threatening emergency from antipsychotic/dopamine-blocking agents. Hyperthermia + muscle rigidity + altered consciousness + autonomic instability. Onset within days–weeks of starting or increasing dose. ICD-10: G21.0</div></div>
        <div class="concept-card"><span class="concept-label">EPS</span><div class="concept-title">Medication-Induced Acute Dystonia</div><div class="concept-desc">Abnormal, sustained, or intermittent muscle contractions causing twisting postures — often cervical (torticollis), oculogyric crisis, or jaw/tongue. Typically minutes–hours after first dose of antipsychotic or increased dose. Responds to anticholinergics. ICD-10: G24.02</div></div>
        <div class="concept-card"><span class="concept-label">AKA</span><div class="concept-title">Medication-Induced Acute Akathisia</div><div class="concept-desc">Subjective complaint of restlessness + objective restless movements (pacing, rocking) following medication initiation/increase. Highly distressing; associated with treatment non-adherence and suicide risk. ICD-10: G25.71</div></div>
        <div class="concept-card"><span class="concept-label">TD</span><div class="concept-title">Tardive Dyskinesia / Dystonia / Akathisia</div><div class="concept-desc">Involuntary, repetitive movements developing after ≥3 months of dopamine-blocking agent exposure. Dyskinesia: choreiform/athetoid movements (orofacial most common). Tardive dystonia: sustained twisting. Tardive akathisia: persistent subjective restlessness. May be irreversible. ICD-10: G24.01/G24.09</div></div>
        <div class="concept-card"><span class="concept-label">TRM</span><div class="concept-title">Medication-Induced Postural Tremor</div><div class="concept-desc">Fine tremor (usually 8–12 Hz) occurring during attempts to maintain posture. Caused by lithium, valproate, antidepressants, stimulants, caffeine, corticosteroids. Distinguish from parkinsonian (rest) tremor and essential tremor. ICD-10: G25.1</div></div>
        <div class="concept-card"><span class="concept-label">PARK</span><div class="concept-title">Medication-Induced Parkinsonism</div><div class="concept-desc">Tremor, bradykinesia, rigidity, or postural instability caused by dopamine-blocking or dopamine-depleting medications. Develops within weeks of starting medication. Resolves with dose reduction or discontinuation. ICD-10: G21.11/G21.19</div></div>
        <div class="concept-card"><span class="concept-label">ADS</span><div class="concept-title">Antidepressant Discontinuation Syndrome</div><div class="concept-desc">Symptoms within days of stopping/reducing antidepressant: flu-like symptoms, insomnia, nausea, sensory disturbances ("brain zaps"), hyperarousal, anxiety. Most common with short half-life SSRIs/SNRIs (paroxetine, venlafaxine). Usually self-limiting in 1–2 weeks. ICD-10: T43.205x</div></div>
      </div>
    </div>
  </div>

  <!-- ── Other Conditions (V/Z-codes) ── -->
  <div class="topic-card">
    <div class="topic-header">
      <span class="topic-icon">📋</span>
      <span class="topic-name">Other Conditions That May Be a Focus of Clinical Attention</span>
      <span class="topic-badge">V/Z-codes</span>
      <span class="chevron">▾</span>
    </div>
    <div class="topic-body">
      <p class="topic-desc">Not mental disorders — these are clinically relevant problems or circumstances that warrant clinical attention, affect diagnosis and treatment, or contribute to the course of a mental disorder. Coded with ICD-9 V-codes / ICD-10 Z-codes.</p>
      <div class="card-grid">
        <div class="concept-card"><span class="concept-label">REL</span><div class="concept-title">Relational Problems</div><div class="concept-desc"><strong>Parent-Child (Z62.820):</strong> Maladaptive interaction patterns causing functional impairment. <strong>Partner Relationship Distress (Z63.0):</strong> Distressing problems in intimate partner relationship. <strong>Sibling (Z62.891) · Upbringing Away From Parents (Z62.29) · Parental Relationship Distress Affecting Child (Z62.898) · High Expressed Emotion in Family (Z63.8).</strong></div></div>
        <div class="concept-card"><span class="concept-label">ABU</span><div class="concept-title">Abuse &amp; Neglect</div><div class="concept-desc">Child Physical Abuse, Sexual Abuse, Psychological Abuse, Neglect (confirmed vs. suspected codes). Adult Physical/Sexual Abuse by Partner or Nonpartner. Each has separate codes for victim, perpetrator, and suspected/confirmed status. T/Z code system. Clinician must document basis for suspicion.</div></div>
        <div class="concept-card"><span class="concept-label">EDU</span><div class="concept-title">Educational &amp; Occupational Problems</div><div class="concept-desc"><strong>Academic/Educational Problem (Z55.9):</strong> Literacy/achievement difficulties not better explained by a learning disorder. <strong>Military Deployment (Z56.82) · Employment Problems (Z56.9):</strong> Unemployment, job dissatisfaction, stressful work environment, threat of job loss.</div></div>
        <div class="concept-card"><span class="concept-label">HSG</span><div class="concept-title">Housing &amp; Economic Problems</div><div class="concept-desc">Homelessness (Z59.0) · Inadequate Housing (Z59.1) · Lack of Adequate Food/Water (Z59.4) · Extreme Poverty (Z59.5) · Low Income (Z59.6) · Insufficient Social Insurance/Welfare (Z59.7). Documented as contributing factors to clinical presentation and treatment planning.</div></div>
        <div class="concept-card"><span class="concept-label">SOC</span><div class="concept-title">Social Environment Problems</div><div class="concept-desc">Phase of Life Problem (Z60.0) · Living Alone (Z60.2) · Acculturation Difficulty (Z60.3) · Social Exclusion/Rejection (Z60.4) · Discrimination/Persecution (Z60.5) · Problems Related to Crime/Legal System (Z65.0–Z65.3) · Victim of Crime (Z65.4).</div></div>
        <div class="concept-card"><span class="concept-label">HLT</span><div class="concept-title">Other Health &amp; Psychosocial Conditions</div><div class="concept-desc"><strong>Nonadherence to Medical Treatment (Z91.19) · Overweight/Obesity (E66.9) · Malingering (Z76.5) · Wandering (Z91.83) · Borderline Intellectual Functioning (R41.83)</strong>. Religious/spiritual problems, phase of life problems, and bereavement (Z63.4) also coded here rather than as formal disorders.</div></div>
      </div>
    </div>
  </div>

  <!-- ── Conditions for Further Study (Section III) ── -->
  <div class="topic-card">
    <div class="topic-header">
      <span class="topic-icon">🔭</span>
      <span class="topic-name">Conditions for Further Study <span style="font-size:0.75em;opacity:0.7">(Section III — Not Official Diagnoses)</span></span>
      <span class="topic-badge">Section III</span>
      <span class="chevron">▾</span>
    </div>
    <div class="topic-body">
      <p class="topic-desc">Proposed conditions requiring additional research before formal inclusion as official DSM diagnoses. Listed to stimulate research, provide a consistent framework, and alert clinicians to their possible clinical significance.</p>
      <div class="card-grid">
        <div class="concept-card"><span class="concept-label">ATTD</span><div class="concept-title">Attenuated Psychosis Syndrome</div><div class="concept-desc">Subthreshold psychotic symptoms: delusions, hallucinations, or disorganized speech — present at least once per week for one month, with relative preservation of reality testing. Onset or worsening in past year. Predicts conversion risk to full psychotic disorder.</div></div>
        <div class="concept-card"><span class="concept-label">DPMD</span><div class="concept-title">Depressive Episodes With Short-Duration Hypomania</div><div class="concept-desc">Lifetime history of ≥1 major depressive episode + ≥2 episodes of hypomania lasting 2–3 days (below the 4-day DSM-5 threshold). Not meeting criteria for Bipolar II. Proposed bridge category between unipolar depression and bipolar spectrum.</div></div>
        <div class="concept-card"><span class="concept-label">PRMD</span><div class="concept-title">Persistent Complex Bereavement Disorder</div><div class="concept-desc">Persistent grief ≥12 months after death of someone close; intense longing/yearning, difficulty accepting death, bitterness, inability to trust others. Causes significant impairment. Distinct from MDD and PTSD. Became <strong>Prolonged Grief Disorder</strong> in DSM-5-TR (2022).</div></div>
        <div class="concept-card"><span class="concept-label">IGD</span><div class="concept-title">Internet Gaming Disorder</div><div class="concept-desc">Persistent/recurrent use of internet games causing significant impairment/distress. ≥5 of 9 criteria: preoccupation, withdrawal, tolerance, failed attempts to control, loss of other interests, continued use despite problems, deception, escape, jeopardized relationships/opportunities. Duration: ≥12 months.</div></div>
        <div class="concept-card"><span class="concept-label">NSSI</span><div class="concept-title">Nonsuicidal Self-Injury</div><div class="concept-desc">On ≥5 days in the past year, intentional self-inflicted damage to body surface without suicidal intent. Associated with negative feelings/cognitions or interpersonal difficulties. Causes significant distress or functional impairment. Currently coded as a symptom of BPD, not a standalone disorder in DSM-5.</div></div>
        <div class="concept-card"><span class="concept-label">SBD</span><div class="concept-title">Suicidal Behavior Disorder</div><div class="concept-desc">A suicide attempt in the last 24 months — a self-initiated sequence of behaviors by a person who, at the time of initiation, expected it might lead to death. Excludes NSSI. Listed to promote consistent terminology and stimulate research into this distinct clinical entity.</div></div>
        <div class="concept-card"><span class="concept-label">NDPAE</span><div class="concept-title">Neurobehavioral Disorder Assoc. With Prenatal Alcohol Exposure</div><div class="concept-desc">Confirmed prenatal alcohol exposure + neurocognitive impairment (global intellectual impairment or specific deficits) + self-regulation impairment (mood/behavioral dysregulation) + adaptive functioning impairment. Overlaps with Fetal Alcohol Spectrum Disorders (FASD).</div></div>
        <div class="concept-card"><span class="concept-label">CUD-F</span><div class="concept-title">Caffeine Use Disorder</div><div class="concept-desc">Proposed: problematic caffeine use causing significant impairment with ≥3 of: tolerance, withdrawal, use in larger amounts than intended, failed attempts to control, use despite knowledge of harm, continued use despite physical/psychological problems. High prevalence but minimal clinical treatment seeking.</div></div>
      </div>
    </div>
  </div>

'''

CSS_ADDITIONS = '''
/* === Mental Disorders P2 — Conditions for Further Study label === */
[data-domain="mental-disorders"] .topic-name span[style] {
  font-weight: 400;
}
'''

def read(p):  return Path(p).read_text(encoding='utf-8')
def write(p, txt): Path(p).write_text(txt, encoding='utf-8')

def patch_html(src):
    if GUARD in src:
        return src, False, 'already patched'
    if CLOSE_ANCHOR not in src:
        return src, False, f'anchor "{CLOSE_ANCHOR}" not found — run part 1 first'

    # 1. Inject new substance cards after the GD (Gambling Disorder) card closing div
    #    Find the GD card block and the closing </div></div> after it, then insert
    gd_idx = src.find('<span class="concept-label">GD</span>')
    if gd_idx < 0:
        return src, False, 'GD card anchor not found'
    # Find the end of the GD card (closing </div></div>)
    card_end = src.find('</div></div>', gd_idx)
    if card_end < 0:
        return src, False, 'GD card end not found'
    card_end += len('</div></div>')
    src = src[:card_end] + NEW_SUBSTANCE_CARDS + src[card_end:]

    # 2. Inject new topics before closing sentinel
    src = src.replace(CLOSE_ANCHOR, NEW_TOPICS_HTML + CLOSE_ANCHOR, 1)

    # 3. Stamp the guard
    src = src.replace(CLOSE_ANCHOR, f'<!-- {GUARD} -->\n' + CLOSE_ANCHOR, 1)
    return src, True, 'ok'

def patch_css(src):
    if GUARD in src:
        return src, False, 'already patched'
    src += f'\n/* {GUARD} */\n' + CSS_ADDITIONS
    return src, True, 'ok'

def patch_js(src):
    return src, True, 'no JS changes needed'

patches = [
    (FILES['html'], patch_html),
    (FILES['css'],  patch_css),
    (FILES['js'],   patch_js),
]

dry = '--dry-run' in sys.argv
errors = []

for fname, fn in patches:
    try:
        orig = read(fname)
        patched, changed, msg = fn(orig)
        status = 'CHANGED' if changed else 'SKIP'
        print(f'[{status}] {fname}: {msg}')
        if changed and not dry:
            shutil.copy(fname, fname + '.bak2')
            write(fname, patched)
            print(f'       wrote {fname} (backup: {fname}.bak2)')
    except FileNotFoundError:
        errors.append(f'NOT FOUND: {fname}')
        print(f'[ERROR] {fname}: file not found')
    except Exception as e:
        errors.append(str(e))
        print(f'[ERROR] {fname}: {e}')

if dry:
    print('\n-- dry run complete, no files written --')
if errors:
    sys.exit(1)
