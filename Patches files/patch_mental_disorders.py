#!/usr/bin/env python3
"""Patch: inject Mental Disorders (DSM-5) domain into index.html, style.css, script.js"""
import re, sys, shutil
from pathlib import Path

# ── config ──────────────────────────────────────────────────────────────────
FILES   = {"html": "index.html", "css": "style.css", "js": "script.js"}
GUARD   = "mental-disorders-domain"          # sentinel prevents double-injection
CHIP_ANCHOR   = 'data-domain="lifestyle"'    # insert new chip after this element
SECTION_ANCHOR= '</main>'                    # inject section before </main>
CSS_ANCHOR    = '/* end custom */'           # append CSS before this comment
JS_ANCHOR     = '// end domains'            # append JS before this comment

# ── HTML ─────────────────────────────────────────────────────────────────────
CHIP_HTML = '<button class="chip" data-domain="mental-disorders">🧠 Mental Disorders</button>'

SECTION_HTML = '''
<!-- mental-disorders-domain -->
<section class="domain-section" data-domain="mental-disorders">
  <h2 class="domain-title"><span class="domain-icon">🧠</span> Mental Disorders <span class="domain-sub">DSM-5</span></h2>

  <!-- ── Neurodevelopmental ── -->
  <div class="topic-card">
    <div class="topic-header">
      <span class="topic-icon">🧩</span>
      <span class="topic-name">Neurodevelopmental Disorders</span>
      <span class="topic-badge">7 disorders</span>
      <span class="chevron">▾</span>
    </div>
    <div class="topic-body">
      <p class="topic-desc">Conditions manifesting early in development, typically before school age, characterized by deficits in personal, social, academic, or occupational functioning.</p>
      <div class="card-grid">
        <div class="concept-card"><span class="concept-label">IDD</span><div class="concept-title">Intellectual Disability</div><div class="concept-desc">Deficits in intellectual functions (reasoning, problem-solving, planning) and adaptive behavior across conceptual, social, and practical domains. Onset during developmental period.</div></div>
        <div class="concept-card"><span class="concept-label">ASD</span><div class="concept-title">Autism Spectrum Disorder</div><div class="concept-desc">Persistent deficits in social communication/interaction across multiple contexts + restricted, repetitive behavior patterns. Symptoms present in early developmental period. ICD-10: F84.0</div></div>
        <div class="concept-card"><span class="concept-label">ADHD</span><div class="concept-title">Attention-Deficit/Hyperactivity Disorder</div><div class="concept-desc">Persistent pattern of inattention and/or hyperactivity-impulsivity interfering with functioning. Several symptoms present before age 12 in two+ settings. ICD-10: F90.x</div></div>
        <div class="concept-card"><span class="concept-label">SLD</span><div class="concept-title">Specific Learning Disorder</div><div class="concept-desc">Difficulties learning and using academic skills (reading, writing, arithmetic) despite targeted interventions, below expectations for age. Subtypes: dyslexia, dyscalculia.</div></div>
        <div class="concept-card"><span class="concept-label">DLD</span><div class="concept-title">Language / Communication Disorders</div><div class="concept-desc">Persistent difficulties in acquisition and use of language (spoken, written, sign) — includes Language Disorder, Speech Sound Disorder, Childhood-Onset Fluency Disorder (stuttering), Social (Pragmatic) Communication Disorder.</div></div>
        <div class="concept-card"><span class="concept-label">TIC</span><div class="concept-title">Tic Disorders / Tourette's</div><div class="concept-desc">Sudden, rapid, recurrent, nonrhythmic motor movement or vocalization. Tourette's: multiple motor + one or more vocal tics for >1 year. Persistent (chronic) or Provisional subtypes.</div></div>
        <div class="concept-card"><span class="concept-label">DCD</span><div class="concept-title">Motor Disorders</div><div class="concept-desc">Developmental Coordination Disorder: acquisition/execution of motor skills below age expectations. Stereotypic Movement Disorder: repetitive, seemingly driven, nonfunctional motor behavior.</div></div>
      </div>
    </div>
  </div>

  <!-- ── Schizophrenia Spectrum ── -->
  <div class="topic-card">
    <div class="topic-header">
      <span class="topic-icon">🌀</span>
      <span class="topic-name">Schizophrenia Spectrum &amp; Psychotic Disorders</span>
      <span class="topic-badge">5 disorders</span>
      <span class="chevron">▾</span>
    </div>
    <div class="topic-body">
      <p class="topic-desc">Defined by abnormalities in one or more of five domains: delusions, hallucinations, disorganized thinking, grossly disorganized/abnormal motor behavior, and negative symptoms.</p>
      <div class="card-grid">
        <div class="concept-card"><span class="concept-label">SCZ</span><div class="concept-title">Schizophrenia</div><div class="concept-desc">≥2 of: delusions, hallucinations, disorganized speech, disorganized/catatonic behavior, negative symptoms — for ≥1 month. Continuous signs ≥6 months. Significant functional decline. ICD-10: F20.9</div></div>
        <div class="concept-card"><span class="concept-label">SZA</span><div class="concept-title">Schizoaffective Disorder</div><div class="concept-desc">An uninterrupted period of major mood episode concurrent with Criterion A schizophrenia. Delusions or hallucinations ≥2 weeks without prominent mood symptoms. Bipolar or Depressive type.</div></div>
        <div class="concept-card"><span class="concept-label">SZF</span><div class="concept-title">Schizophreniform Disorder</div><div class="concept-desc">Meets Criterion A of schizophrenia but episode lasts 1–6 months. Diagnosis provisional until recovery or progression to schizophrenia.</div></div>
        <div class="concept-card"><span class="concept-label">DD</span><div class="concept-title">Delusional Disorder</div><div class="concept-desc">≥1 delusion for ≥1 month. Hallucinations not prominent. Functioning not markedly impaired apart from impact of delusion. Types: erotomanic, grandiose, jealous, persecutory, somatic, mixed.</div></div>
        <div class="concept-card"><span class="concept-label">BPD</span><div class="concept-title">Brief Psychotic Disorder</div><div class="concept-desc">Sudden onset of ≥1 positive psychotic symptom lasting ≥1 day but &lt;1 month, with full return to premorbid functioning. May be with/without marked stressor or postpartum onset.</div></div>
      </div>
    </div>
  </div>

  <!-- ── Bipolar ── -->
  <div class="topic-card">
    <div class="topic-header">
      <span class="topic-icon">⚡</span>
      <span class="topic-name">Bipolar &amp; Related Disorders</span>
      <span class="topic-badge">3 disorders</span>
      <span class="chevron">▾</span>
    </div>
    <div class="topic-body">
      <p class="topic-desc">Characterized by episodes of mania or hypomania, often alternating with depressive episodes. Bridge between schizophrenia spectrum and depressive disorders in terms of symptom profile, family history, and genetics.</p>
      <div class="card-grid">
        <div class="concept-card"><span class="concept-label">BPI</span><div class="concept-title">Bipolar I Disorder</div><div class="concept-desc">At least one manic episode (≥7 days or hospitalized); may be preceded or followed by hypomanic or major depressive episodes. Manic episode: elevated/expansive/irritable mood + increased goal-directed activity. ICD-10: F31.x</div></div>
        <div class="concept-card"><span class="concept-label">BPII</span><div class="concept-title">Bipolar II Disorder</div><div class="concept-desc">≥1 hypomanic episode + ≥1 major depressive episode; no full manic episode. Hypomanic episode ≥4 days; noticeable change in functioning but not severe enough to cause marked impairment. ICD-10: F31.81</div></div>
        <div class="concept-card"><span class="concept-label">CYC</span><div class="concept-title">Cyclothymic Disorder</div><div class="concept-desc">≥2 years of hypomanic AND depressive periods not meeting full criteria for hypomanic or major depressive episode. Symptoms present ≥50% of the time. ICD-10: F34.0</div></div>
      </div>
    </div>
  </div>

  <!-- ── Depressive ── -->
  <div class="topic-card">
    <div class="topic-header">
      <span class="topic-icon">🌧️</span>
      <span class="topic-name">Depressive Disorders</span>
      <span class="topic-badge">4 disorders</span>
      <span class="chevron">▾</span>
    </div>
    <div class="topic-body">
      <p class="topic-desc">Common feature: sad, empty, or irritable mood with somatic and cognitive changes significantly affecting capacity to function. Differs by duration, timing, and presumed etiology.</p>
      <div class="card-grid">
        <div class="concept-card"><span class="concept-label">MDD</span><div class="concept-title">Major Depressive Disorder</div><div class="concept-desc">≥5 symptoms for ≥2 weeks including depressed mood or anhedonia: weight change, sleep disturbance, psychomotor agitation/retardation, fatigue, worthlessness/guilt, concentration difficulty, suicidal ideation. ICD-10: F32.x</div></div>
        <div class="concept-card"><span class="concept-label">PDD</span><div class="concept-title">Persistent Depressive Disorder (Dysthymia)</div><div class="concept-desc">Depressed mood for most of the day, more days than not, for ≥2 years. ≥2 symptoms: poor appetite, insomnia/hypersomnia, low energy, low self-esteem, poor concentration, hopelessness. Consolidates chronic MDD and dysthymia. ICD-10: F34.1</div></div>
        <div class="concept-card"><span class="concept-label">DMDD</span><div class="concept-title">Disruptive Mood Dysregulation Disorder</div><div class="concept-desc">Severe recurrent temper outbursts + persistently irritable/angry mood between outbursts ≥3x/week for ≥12 months. Onset before 10 years; diagnosis not made before 6 or after 18. ICD-10: F34.8</div></div>
        <div class="concept-card"><span class="concept-label">PMDD</span><div class="concept-title">Premenstrual Dysphoric Disorder</div><div class="concept-desc">Marked affective lability, irritability, dysphoria, anxiety in the final week before menses, improving after onset. ≥5 symptoms confirmed by prospective daily ratings. ICD-10: F32.81</div></div>
      </div>
    </div>
  </div>

  <!-- ── Anxiety ── -->
  <div class="topic-card">
    <div class="topic-header">
      <span class="topic-icon">😰</span>
      <span class="topic-name">Anxiety Disorders</span>
      <span class="topic-badge">7 disorders</span>
      <span class="chevron">▾</span>
    </div>
    <div class="topic-body">
      <p class="topic-desc">Share features of excessive fear and anxiety with related behavioral disturbances. Differ from normal fear/anxiety by being excessive or persistent beyond developmentally appropriate periods.</p>
      <div class="card-grid">
        <div class="concept-card"><span class="concept-label">GAD</span><div class="concept-title">Generalized Anxiety Disorder</div><div class="concept-desc">Excessive anxiety/worry about multiple events occurring more days than not for ≥6 months, difficult to control. ≥3 symptoms: restlessness, fatigue, concentration difficulty, irritability, muscle tension, sleep disturbance. ICD-10: F41.1</div></div>
        <div class="concept-card"><span class="concept-label">PD</span><div class="concept-title">Panic Disorder</div><div class="concept-desc">Recurrent unexpected panic attacks (abrupt surge of fear peaking within minutes, ≥4 symptoms: palpitations, sweating, trembling, shortness of breath, chest pain, nausea, dizziness, chills, paresthesias, derealization, fear of losing control/dying). Followed by ≥1 month of persistent concern or maladaptive behavior change. ICD-10: F41.0</div></div>
        <div class="concept-card"><span class="concept-label">AGO</span><div class="concept-title">Agoraphobia</div><div class="concept-desc">Marked fear/anxiety about ≥2 of: public transit, open spaces, enclosed spaces, standing in lines/crowds, being outside the home alone. Situations avoided or endured with intense anxiety or require a companion. ICD-10: F40.00</div></div>
        <div class="concept-card"><span class="concept-label">SAD</span><div class="concept-title">Social Anxiety Disorder</div><div class="concept-desc">Marked fear/anxiety about social situations where the individual may be scrutinized by others, leading to fear of humiliation or rejection. Situations avoided or endured with intense anxiety. ≥6 months. ICD-10: F40.10</div></div>
        <div class="concept-card"><span class="concept-label">SPH</span><div class="concept-title">Specific Phobia</div><div class="concept-desc">Marked fear/anxiety about a specific object or situation (animal, natural environment, blood-injection-injury, situational, other). Fear out of proportion; typically lasting ≥6 months. ICD-10: F40.2xx</div></div>
        <div class="concept-card"><span class="concept-label">SEP</span><div class="concept-title">Separation Anxiety Disorder</div><div class="concept-desc">Excessive fear/anxiety about separation from attachment figures. ≥3 symptoms including distress when separated, worry about harm to figures, reluctance to leave, nightmares of separation. ICD-10: F93.0</div></div>
        <div class="concept-card"><span class="concept-label">SM</span><div class="concept-title">Selective Mutism</div><div class="concept-desc">Consistent failure to speak in specific social situations (school) despite speaking in others. Interferes with educational achievement. Duration ≥1 month (not first month of school). ICD-10: F94.0</div></div>
      </div>
    </div>
  </div>

  <!-- ── OCD ── -->
  <div class="topic-card">
    <div class="topic-header">
      <span class="topic-icon">🔁</span>
      <span class="topic-name">Obsessive-Compulsive &amp; Related Disorders</span>
      <span class="topic-badge">5 disorders</span>
      <span class="chevron">▾</span>
    </div>
    <div class="topic-body">
      <p class="topic-desc">Characterized by obsessions and compulsions or related repetitive behaviors. Grouped together based on putative similarities in diagnostic validators and treatment response (serotonin reuptake inhibitors).</p>
      <div class="card-grid">
        <div class="concept-card"><span class="concept-label">OCD</span><div class="concept-title">Obsessive-Compulsive Disorder</div><div class="concept-desc">Obsessions: recurrent, persistent thoughts/urges/images causing marked anxiety, experienced as intrusive. Compulsions: repetitive behaviors or mental acts aimed at reducing distress. Time-consuming (&gt;1 hr/day) or causing significant impairment. ICD-10: F42</div></div>
        <div class="concept-card"><span class="concept-label">BDD</span><div class="concept-title">Body Dysmorphic Disorder</div><div class="concept-desc">Preoccupation with ≥1 perceived defects in physical appearance (not noticeable to others). Repetitive behaviors (mirror checking, grooming) or mental acts in response. Causes significant distress/impairment. ICD-10: F45.22</div></div>
        <div class="concept-card"><span class="concept-label">HD</span><div class="concept-title">Hoarding Disorder</div><div class="concept-desc">Persistent difficulty discarding possessions regardless of value, due to a perceived need to save items and distress associated with discarding. Accumulation clutters living areas making them unusable. ICD-10: F42</div></div>
        <div class="concept-card"><span class="concept-label">TTM</span><div class="concept-title">Trichotillomania (Hair-Pulling)</div><div class="concept-desc">Recurrent pulling out of one's hair resulting in hair loss. Repeated attempts to stop. Causes significant distress/functional impairment. ICD-10: F63.3</div></div>
        <div class="concept-card"><span class="concept-label">EXD</span><div class="concept-title">Excoriation (Skin-Picking) Disorder</div><div class="concept-desc">Recurrent skin picking resulting in skin lesions. Repeated attempts to stop. Not attributable to substance, medical condition, or another mental disorder. ICD-10: L98.1</div></div>
      </div>
    </div>
  </div>

  <!-- ── Trauma ── -->
  <div class="topic-card">
    <div class="topic-header">
      <span class="topic-icon">💥</span>
      <span class="topic-name">Trauma- &amp; Stressor-Related Disorders</span>
      <span class="topic-badge">5 disorders</span>
      <span class="chevron">▾</span>
    </div>
    <div class="topic-body">
      <p class="topic-desc">Disorders where exposure to a traumatic or stressful event is explicitly listed as a diagnostic criterion. Psychological distress following exposure to a traumatic or stressful event takes varied forms.</p>
      <div class="card-grid">
        <div class="concept-card"><span class="concept-label">PTSD</span><div class="concept-title">Posttraumatic Stress Disorder</div><div class="concept-desc">Exposure to actual/threatened death, serious injury, or sexual violence. Intrusion symptoms, avoidance of trauma-related stimuli, negative alterations in cognition/mood, marked alterations in arousal/reactivity. Duration &gt;1 month. ICD-10: F43.10</div></div>
        <div class="concept-card"><span class="concept-label">ASD</span><div class="concept-title">Acute Stress Disorder</div><div class="concept-desc">Same trauma exposure as PTSD; ≥9 symptoms across intrusion, negative mood, dissociation, avoidance, and arousal clusters. Duration 3 days–1 month. If persists beyond 1 month → PTSD. ICD-10: F43.0</div></div>
        <div class="concept-card"><span class="concept-label">ADJ</span><div class="concept-title">Adjustment Disorders</div><div class="concept-desc">Emotional/behavioral symptoms in response to an identifiable stressor within 3 months of onset. Marked distress out of proportion to the severity of the stressor. Resolves within 6 months of stressor cessation. ICD-10: F43.2x</div></div>
        <div class="concept-card"><span class="concept-label">RAD</span><div class="concept-title">Reactive Attachment Disorder</div><div class="concept-desc">Consistent pattern of inhibited, emotionally withdrawn behavior toward adult caregivers — rarely seeks or responds to comfort. Result of social neglect or insufficient early caregiving. ICD-10: F94.1</div></div>
        <div class="concept-card"><span class="concept-label">DSED</span><div class="concept-title">Disinhibited Social Engagement Disorder</div><div class="concept-desc">Pattern of behavior in which a child actively approaches and interacts with unfamiliar adults without the reticence expected by culture. Overly familiar verbal/physical behavior. ICD-10: F94.2</div></div>
      </div>
    </div>
  </div>

  <!-- ── Dissociative ── -->
  <div class="topic-card">
    <div class="topic-header">
      <span class="topic-icon">🪞</span>
      <span class="topic-name">Dissociative Disorders</span>
      <span class="topic-badge">3 disorders</span>
      <span class="chevron">▾</span>
    </div>
    <div class="topic-body">
      <p class="topic-desc">Disruption and/or discontinuity in the normal integration of consciousness, memory, identity, emotion, perception, behavior, and sense of self. Symptoms cause significant distress or functional impairment.</p>
      <div class="card-grid">
        <div class="concept-card"><span class="concept-label">DID</span><div class="concept-title">Dissociative Identity Disorder</div><div class="concept-desc">Disruption of identity characterized by ≥2 distinct personality states (in some cultures: experience of possession). Recurrent gaps in recall of everyday events, personal information, or traumatic events. Associated with severe trauma history. ICD-10: F44.81</div></div>
        <div class="concept-card"><span class="concept-label">DA</span><div class="concept-title">Dissociative Amnesia</div><div class="concept-desc">Inability to recall important autobiographical information, usually traumatic, inconsistent with ordinary forgetting. May include dissociative fugue: apparently purposeful travel or bewildered wandering associated with amnesia. ICD-10: F44.0</div></div>
        <div class="concept-card"><span class="concept-label">DPDR</span><div class="concept-title">Depersonalization/Derealization Disorder</div><div class="concept-desc">Persistent/recurrent experiences of depersonalization (feeling detached from one's mental processes or body) and/or derealization (feeling detached from surroundings). Reality testing remains intact. ICD-10: F48.1</div></div>
      </div>
    </div>
  </div>

  <!-- ── Somatic ── -->
  <div class="topic-card">
    <div class="topic-header">
      <span class="topic-icon">🤒</span>
      <span class="topic-name">Somatic Symptom &amp; Related Disorders</span>
      <span class="topic-badge">4 disorders</span>
      <span class="chevron">▾</span>
    </div>
    <div class="topic-body">
      <p class="topic-desc">All have prominent somatic symptoms associated with significant distress and impairment. Emphasize diagnosis via positive symptoms and signs (distressing thoughts, feelings, behaviors) rather than medically unexplained symptoms.</p>
      <div class="card-grid">
        <div class="concept-card"><span class="concept-label">SSD</span><div class="concept-title">Somatic Symptom Disorder</div><div class="concept-desc">≥1 distressing somatic symptom causing disruption in daily life + disproportionate/persistent thoughts about seriousness, persistently high anxiety, or excessive time/energy devoted to symptoms. ≥6 months. ICD-10: F45.1</div></div>
        <div class="concept-card"><span class="concept-label">IAD</span><div class="concept-title">Illness Anxiety Disorder (Hypochondria)</div><div class="concept-desc">Preoccupation with having or acquiring a serious illness. Somatic symptoms absent or mild. High health-related anxiety. Excessive health-related behaviors or maladaptive avoidance. ≥6 months. ICD-10: F45.21</div></div>
        <div class="concept-card"><span class="concept-label">FCD</span><div class="concept-title">Functional Neurological Symptom (Conversion) Disorder</div><div class="concept-desc">≥1 symptom of altered voluntary motor or sensory function. Clinical findings provide evidence of incompatibility between the symptom and recognized neurological or medical conditions. ICD-10: F44.x</div></div>
        <div class="concept-card"><span class="concept-label">FAD</span><div class="concept-title">Factitious Disorder</div><div class="concept-desc">Falsification of physical or psychological signs/symptoms or induction of injury/disease in self or another (imposed on another). Deceptive behavior evident even in absence of obvious external rewards. ICD-10: F68.10</div></div>
      </div>
    </div>
  </div>

  <!-- ── Eating ── -->
  <div class="topic-card">
    <div class="topic-header">
      <span class="topic-icon">🍽️</span>
      <span class="topic-name">Feeding &amp; Eating Disorders</span>
      <span class="topic-badge">6 disorders</span>
      <span class="chevron">▾</span>
    </div>
    <div class="topic-body">
      <p class="topic-desc">Characterized by a persistent disturbance of eating or eating-related behavior that results in altered consumption or absorption of food and significantly impairs physical health or psychosocial functioning.</p>
      <div class="card-grid">
        <div class="concept-card"><span class="concept-label">AN</span><div class="concept-title">Anorexia Nervosa</div><div class="concept-desc">Restriction of energy intake → significantly low body weight. Intense fear of gaining weight or behavior that interferes with weight gain. Disturbed experience of body weight/shape. Restricting and binge-eating/purging subtypes. ICD-10: F50.0x</div></div>
        <div class="concept-card"><span class="concept-label">BN</span><div class="concept-title">Bulimia Nervosa</div><div class="concept-desc">Recurrent binge eating (large amount in ≤2 hrs + loss of control) + recurrent compensatory behaviors (purging, fasting, excessive exercise). ≥1x/week for ≥3 months. Self-evaluation unduly influenced by body shape/weight. ICD-10: F50.2</div></div>
        <div class="concept-card"><span class="concept-label">BED</span><div class="concept-title">Binge-Eating Disorder</div><div class="concept-desc">Recurrent binge eating without regular compensatory behaviors. ≥3 of: eating rapidly, eating until uncomfortably full, eating when not hungry, eating alone due to embarrassment, feeling disgusted/depressed/guilty. Marked distress. ≥1x/week × 3 months. ICD-10: F50.8</div></div>
        <div class="concept-card"><span class="concept-label">ARFID</span><div class="concept-title">Avoidant/Restrictive Food Intake Disorder</div><div class="concept-desc">Disturbance in eating/feeding: significant weight loss, nutritional deficiency, dependence on supplements, or marked psychosocial impairment. Not explained by food unavailability or culturally sanctioned practice. ICD-10: F50.8</div></div>
        <div class="concept-card"><span class="concept-label">PICA</span><div class="concept-title">Pica</div><div class="concept-desc">Persistent eating of nonnutritive, nonfood substances (dirt, clay, paper, hair, chalk) ≥1 month. Inappropriate to developmental level. Not culturally/socially normative. ICD-10: F98.3/F50.8</div></div>
        <div class="concept-card"><span class="concept-label">RD</span><div class="concept-title">Rumination Disorder</div><div class="concept-desc">Repeated regurgitation of food ≥1 month. Regurgitated food may be re-chewed, re-swallowed, or spit out. Not due to a GI or medical condition. ICD-10: F98.21</div></div>
      </div>
    </div>
  </div>

  <!-- ── Sleep-Wake ── -->
  <div class="topic-card">
    <div class="topic-header">
      <span class="topic-icon">😴</span>
      <span class="topic-name">Sleep-Wake Disorders</span>
      <span class="topic-badge">6 disorders</span>
      <span class="chevron">▾</span>
    </div>
    <div class="topic-body">
      <p class="topic-desc">Dissatisfaction with sleep quality/quantity occurring alongside medical and mental health conditions. Involve dyssomnias (sleep amount/quality/timing), parasomnias (abnormal events during sleep), and sleep-related movement disorders.</p>
      <div class="card-grid">
        <div class="concept-card"><span class="concept-label">INS</span><div class="concept-title">Insomnia Disorder</div><div class="concept-desc">Dissatisfaction with sleep quantity/quality with ≥1 symptom: difficulty initiating sleep, maintaining sleep, or early-morning awakening. ≥3 nights/week for ≥3 months despite adequate opportunity for sleep. ICD-10: F51.01</div></div>
        <div class="concept-card"><span class="concept-label">HYP</span><div class="concept-title">Hypersomnolence Disorder</div><div class="concept-desc">Excessive sleepiness despite ≥7 hours of sleep + ≥1 of: recurrent sleep periods in day, prolonged non-restorative main sleep episode (&gt;9 hrs), difficulty being fully awake after abrupt awakening. ≥3x/week × 3 months. ICD-10: F51.11</div></div>
        <div class="concept-card"><span class="concept-label">NAR</span><div class="concept-title">Narcolepsy</div><div class="concept-desc">Recurrent lapses into sleep + cataplexy (brief loss of muscle tone triggered by emotions) or hypocretin deficiency. Sleep paralysis and hypnagogic/hypnopompic hallucinations. ≥3x/week × 3 months. ICD-10: G47.4x</div></div>
        <div class="concept-card"><span class="concept-label">CRD</span><div class="concept-title">Circadian Rhythm Sleep-Wake Disorders</div><div class="concept-desc">Persistent/recurrent pattern of sleep disruption due to misalignment between endogenous circadian rhythm and external sleep-wake schedule. Types: delayed/advanced sleep phase, irregular, non-24-hour, shift work, jet lag. ICD-10: G47.2x</div></div>
        <div class="concept-card"><span class="concept-label">PARA</span><div class="concept-title">Parasomnias</div><div class="concept-desc">Non-REM Sleep Arousal: sleepwalking or sleep terrors. REM Sleep Behavior Disorder: repeated arousal with vocalization/complex motor behaviors. Nightmare Disorder: recurrent disturbing dreams. Restless Legs Syndrome: urge to move legs with unpleasant sensations.</div></div>
        <div class="concept-card"><span class="concept-label">OSA</span><div class="concept-title">Sleep-Related Breathing Disorders</div><div class="concept-desc">Obstructive Sleep Apnea: ≥15 obstructive apneas/hypopneas/hr (or ≥5 with symptoms). Central Sleep Apnea: repetitive cessation of breathing without respiratory effort. Sleep-Related Hypoventilation. ICD-10: G47.3x</div></div>
      </div>
    </div>
  </div>

  <!-- ── Disruptive ── -->
  <div class="topic-card">
    <div class="topic-header">
      <span class="topic-icon">💢</span>
      <span class="topic-name">Disruptive, Impulse-Control &amp; Conduct Disorders</span>
      <span class="topic-badge">5 disorders</span>
      <span class="chevron">▾</span>
    </div>
    <div class="topic-body">
      <p class="topic-desc">Problems in the self-regulation of emotions and behaviors. Behaviors violate the rights of others and/or conflict with major societal norms or authority figures. More common in males.</p>
      <div class="card-grid">
        <div class="concept-card"><span class="concept-label">ODD</span><div class="concept-title">Oppositional Defiant Disorder</div><div class="concept-desc">Pattern of angry/irritable mood (often loses temper, touchy, easily annoyed, angry/resentful) + argumentative/defiant behavior + vindictiveness. ≥4 symptoms for ≥6 months. ICD-10: F91.3</div></div>
        <div class="concept-card"><span class="concept-label">IED</span><div class="concept-title">Intermittent Explosive Disorder</div><div class="concept-desc">Recurrent behavioral outbursts representing failure to control aggressive impulses. Verbal/physical aggression grossly out of proportion to provocation. ≥2x/week × 3 months (verbal) or 3 episodes in 12 months (physical). ICD-10: F63.81</div></div>
        <div class="concept-card"><span class="concept-label">CD</span><div class="concept-title">Conduct Disorder</div><div class="concept-desc">Repetitive/persistent pattern violating basic rights of others or major age-appropriate societal norms. ≥3 of 15 criteria in 4 clusters: aggression to people/animals, destruction of property, deceitfulness/theft, serious rule violations. ICD-10: F91.x</div></div>
        <div class="concept-card"><span class="concept-label">PYR</span><div class="concept-title">Pyromania</div><div class="concept-desc">Deliberate and purposeful fire setting on ≥2 occasions. Tension/affective arousal before act; fascination with fire. Pleasure, gratification, or relief when setting fires. Not for monetary gain, revenge, or other purposes. ICD-10: F63.1</div></div>
        <div class="concept-card"><span class="concept-label">KLP</span><div class="concept-title">Kleptomania</div><div class="concept-desc">Recurrent failure to resist impulses to steal objects not needed for personal use or monetary value. Increasing tension immediately before committing the theft; pleasure/gratification/relief at the time. ICD-10: F63.2</div></div>
      </div>
    </div>
  </div>

  <!-- ── Substance ── -->
  <div class="topic-card">
    <div class="topic-header">
      <span class="topic-icon">💊</span>
      <span class="topic-name">Substance-Related &amp; Addictive Disorders</span>
      <span class="topic-badge">10 substances + gambling</span>
      <span class="chevron">▾</span>
    </div>
    <div class="topic-body">
      <p class="topic-desc">Grouped in four clusters: impaired control, social impairment, risky use, and pharmacological criteria (tolerance and withdrawal). Severity: mild (2–3 criteria), moderate (4–5), severe (≥6).</p>
      <div class="card-grid">
        <div class="concept-card"><span class="concept-label">AUD</span><div class="concept-title">Alcohol Use Disorder</div><div class="concept-desc">Problematic pattern of alcohol use causing impairment in ≥2 of 11 criteria within 12 months. Withdrawal: autonomic hyperactivity, tremor, insomnia, nausea, hallucinations, seizures. ICD-10: F10.xx</div></div>
        <div class="concept-card"><span class="concept-label">OUD</span><div class="concept-title">Opioid Use Disorder</div><div class="concept-desc">Problematic pattern of opioid use; characteristic withdrawal includes dysphoric mood, nausea, muscle aches, insomnia, fever. High overdose mortality risk. Buprenorphine/methadone maintenance treatments. ICD-10: F11.xx</div></div>
        <div class="concept-card"><span class="concept-label">SUD</span><div class="concept-title">Stimulant Use Disorder</div><div class="concept-desc">Covers amphetamine-type substances, cocaine, and other stimulants. Withdrawal: fatigue, vivid unpleasant dreams, increased sleep, increased appetite, psychomotor retardation or agitation. ICD-10: F14.xx/F15.xx</div></div>
        <div class="concept-card"><span class="concept-label">CUD</span><div class="concept-title">Cannabis Use Disorder</div><div class="concept-desc">Problematic cannabis use with ≥2 criteria. Withdrawal: irritability, anxiety, sleep difficulty, decreased appetite, restlessness. First recognized withdrawal syndrome in DSM-5. ICD-10: F12.xx</div></div>
        <div class="concept-card"><span class="concept-label">SedUD</span><div class="concept-title">Sedative, Hypnotic, or Anxiolytic Use Disorder</div><div class="concept-desc">Includes benzodiazepines, barbiturates, sleep aids. Withdrawal can be life-threatening: seizures, autonomic instability. Similar presentation to alcohol withdrawal. ICD-10: F13.xx</div></div>
        <div class="concept-card"><span class="concept-label">GD</span><div class="concept-title">Gambling Disorder</div><div class="concept-desc">Only behavioral addiction in DSM-5. Persistent/recurrent problematic gambling: needing increasing amounts, restless/irritable when cutting back, preoccupied, chases losses, lies, relies on others for money. ≥4 criteria × 12 months. ICD-10: F63.0</div></div>
      </div>
    </div>
  </div>

  <!-- ── Neurocognitive ── -->
  <div class="topic-card">
    <div class="topic-header">
      <span class="topic-icon">🧠</span>
      <span class="topic-name">Neurocognitive Disorders</span>
      <span class="topic-badge">3 categories</span>
      <span class="chevron">▾</span>
    </div>
    <div class="topic-body">
      <p class="topic-desc">Characterized by a decline from a prior level of cognitive performance in one or more cognitive domains (complex attention, executive function, learning/memory, language, perceptual-motor, social cognition).</p>
      <div class="card-grid">
        <div class="concept-card"><span class="concept-label">DEL</span><div class="concept-title">Delirium</div><div class="concept-desc">Disturbance in attention and awareness developing over a short period with additional cognitive disturbance. Tends to fluctuate over the day. Evidence from history/exam/labs of a direct physiological cause. ICD-10: F05</div></div>
        <div class="concept-card"><span class="concept-label">MaND</span><div class="concept-title">Major Neurocognitive Disorder (Dementia)</div><div class="concept-desc">Significant cognitive decline in ≥1 domain, interfering with independence in everyday activities. Subtypes by etiology: Alzheimer's (most common), Vascular, Lewy Body, Frontotemporal, TBI, HIV, Prion, Parkinson's, Huntington's. ICD-10: F02.xx</div></div>
        <div class="concept-card"><span class="concept-label">MiND</span><div class="concept-title">Mild Neurocognitive Disorder (MCI)</div><div class="concept-desc">Modest cognitive decline in ≥1 domain without interference with independence (but may require greater effort/compensatory strategies). Does not meet criteria for major NCD. ICD-10: G31.84</div></div>
      </div>
    </div>
  </div>

  <!-- ── Personality ── -->
  <div class="topic-card">
    <div class="topic-header">
      <span class="topic-icon">🎭</span>
      <span class="topic-name">Personality Disorders</span>
      <span class="topic-badge">10 disorders</span>
      <span class="chevron">▾</span>
    </div>
    <div class="topic-body">
      <p class="topic-desc">Enduring pattern of inner experience and behavior deviating markedly from cultural expectations, pervasive, inflexible, onset in adolescence/early adulthood, stable over time, causing distress/impairment. Three clusters based on descriptive similarities.</p>
      <div class="card-grid">
        <div class="concept-card"><span class="concept-label">ClA</span><div class="concept-title">Cluster A — Odd/Eccentric</div><div class="concept-desc"><strong>Paranoid (F60.0):</strong> Pervasive distrust/suspiciousness; others' motives interpreted as malevolent. <br><strong>Schizoid (F60.1):</strong> Detachment from social relationships; restricted emotional expression. <br><strong>Schizotypal (F21):</strong> Acute discomfort with close relationships + cognitive/perceptual distortions + eccentricities.</div></div>
        <div class="concept-card"><span class="concept-label">ClB</span><div class="concept-title">Cluster B — Dramatic/Emotional</div><div class="concept-desc"><strong>Antisocial (F60.2):</strong> Disregard/violation of others' rights since age 15. <br><strong>Borderline (F60.3):</strong> Instability in interpersonal relationships, self-image, affect + impulsivity. <br><strong>Histrionic (F60.4):</strong> Excessive emotionality and attention-seeking. <br><strong>Narcissistic (F60.81):</strong> Grandiosity, need for admiration, lack of empathy.</div></div>
        <div class="concept-card"><span class="concept-label">ClC</span><div class="concept-title">Cluster C — Anxious/Fearful</div><div class="concept-desc"><strong>Avoidant (F60.6):</strong> Social inhibition, feelings of inadequacy, hypersensitivity to negative evaluation. <br><strong>Dependent (F60.7):</strong> Excessive need to be taken care of; submissive, clinging. <br><strong>Obsessive-Compulsive (F60.5):</strong> Preoccupation with orderliness, perfectionism, control (distinct from OCD).</div></div>
      </div>
    </div>
  </div>

  <!-- ── Paraphilic ── -->
  <div class="topic-card">
    <div class="topic-header">
      <span class="topic-icon">⚠️</span>
      <span class="topic-name">Paraphilic Disorders</span>
      <span class="topic-badge">8 disorders</span>
      <span class="chevron">▾</span>
    </div>
    <div class="topic-body">
      <p class="topic-desc">A paraphilia is an intense/persistent sexual interest in atypical objects/situations/individuals. A paraphilic disorder requires that paraphilia cause distress/impairment to the individual OR the paraphilia involves harm/risk to others.</p>
      <div class="card-grid">
        <div class="concept-card"><span class="concept-label">VOY</span><div class="concept-title">Voyeuristic Disorder</div><div class="concept-desc">Recurrent, intense sexual arousal from observing an unsuspecting person who is naked, in the process of disrobing, or engaging in sexual activity. ≥6 months. ICD-10: F65.3</div></div>
        <div class="concept-card"><span class="concept-label">EXH</span><div class="concept-title">Exhibitionistic Disorder</div><div class="concept-desc">Recurrent sexual arousal from exposing genitals to unsuspecting person. ≥6 months. The person has acted on urges or is markedly distressed. ICD-10: F65.2</div></div>
        <div class="concept-card"><span class="concept-label">FRO</span><div class="concept-title">Frotteuristic Disorder</div><div class="concept-desc">Recurrent sexual arousal from touching/rubbing against a nonconsenting person. ≥6 months. Has acted on urges or is markedly distressed. ICD-10: F65.81</div></div>
        <div class="concept-card"><span class="concept-label">SM</span><div class="concept-title">Sexual Masochism / Sadism Disorder</div><div class="concept-desc">Masochism: arousal from being humiliated, beaten, bound, or made to suffer. Sadism: arousal from psychological/physical suffering of another. Disorder requires distress, impairment, or harm to nonconsenting others. ICD-10: F65.5x</div></div>
        <div class="concept-card"><span class="concept-label">PED</span><div class="concept-title">Pedophilic Disorder</div><div class="concept-desc">Intense/recurrent sexual urges/behaviors involving prepubescent children (≤13 yrs) for ≥6 months. Person is ≥16 yrs and ≥5 yrs older than child. Has acted on urges or urges cause marked distress. ICD-10: F65.4</div></div>
        <div class="concept-card"><span class="concept-label">FET</span><div class="concept-title">Fetishistic / Transvestic Disorder</div><div class="concept-desc">Fetishistic: intense sexual arousal from use of nonliving objects or highly specific non-genital body part. Transvestic: intense sexual arousal from cross-dressing. Disorder requires marked distress or psychosocial impairment. ICD-10: F65.0 / F65.1</div></div>
      </div>
    </div>
  </div>

  <!-- ── Elimination / Sexual / Gender ── -->
  <div class="topic-card">
    <div class="topic-header">
      <span class="topic-icon">🔬</span>
      <span class="topic-name">Additional DSM-5 Categories</span>
      <span class="topic-badge">3 categories</span>
      <span class="chevron">▾</span>
    </div>
    <div class="topic-body">
      <p class="topic-desc">Remaining DSM-5 diagnostic categories: Elimination Disorders, Sexual Dysfunctions, and Gender Dysphoria — each with distinct diagnostic criteria and clinical features.</p>
      <div class="card-grid">
        <div class="concept-card"><span class="concept-label">ELIM</span><div class="concept-title">Elimination Disorders</div><div class="concept-desc"><strong>Enuresis (F98.0):</strong> Repeated voiding of urine into bed/clothes ≥2x/week × 3 months in children ≥5 yrs (not due to substances or medical condition). Nocturnal, diurnal, or both subtypes. <br><strong>Encopresis (F98.1):</strong> Repeated defecation in inappropriate places (clothing, floor) in children ≥4 yrs, ≥1x/month × 3 months.</div></div>
        <div class="concept-card"><span class="concept-label">SXD</span><div class="concept-title">Sexual Dysfunctions</div><div class="concept-desc">Clinically significant disturbance in sexual response cycle or pain during sex. Includes: Delayed Ejaculation, Erectile Disorder, Female Orgasmic Disorder, Female Sexual Interest/Arousal Disorder, Genito-Pelvic Pain/Penetration Disorder, Male Hypoactive Sexual Desire, Premature Ejaculation. Lifelong vs. acquired; generalized vs. situational specifiers. ICD-10: F52.x</div></div>
        <div class="concept-card"><span class="concept-label">GD</span><div class="concept-title">Gender Dysphoria</div><div class="concept-desc">Marked incongruence between experienced/expressed gender and assigned gender of ≥6 months. In children: ≥6 of 8 specific manifestations. In adolescents/adults: ≥2 of 6 criteria. Associated with significant distress/impairment. ICD-10: F64.x. Note: DSM-5 focus is on dysphoria, not identity itself.</div></div>
      </div>
    </div>
  </div>

</section>
<!-- /mental-disorders-domain -->
'''

CSS_ADDITIONS = '''
/* === Mental Disorders Domain === */
[data-domain="mental-disorders"] .topic-desc {
  font-size: 0.88rem;
  color: var(--text-muted);
  margin: 0 0 1rem;
  line-height: 1.5;
}
[data-domain="mental-disorders"] .concept-desc strong {
  color: var(--cyan);
}
body.light [data-domain="mental-disorders"] .topic-desc { color: #444; }
body.light [data-domain="mental-disorders"] .concept-title { color: #111; }
body.light [data-domain="mental-disorders"] .concept-label { color: #fff; }
'''

JS_ADDITIONS = ''  # no JS needed; accordion is handled by existing script

# ── patch logic ───────────────────────────────────────────────────────────────
import sys

def read(p):
    return Path(p).read_text(encoding='utf-8')

def write(p, txt):
    Path(p).write_text(txt, encoding='utf-8')

def patch_html(src):
    if GUARD in src:
        return src, False, 'already patched'
    # 1. add filter chip after lifestyle chip
    chip_pat = r'(data-domain="lifestyle"[^>]*>[^<]*</button>)'
    m = re.search(chip_pat, src)
    if m:
        src = src[:m.end()] + '\n      ' + CHIP_HTML + src[m.end():]
    else:
        # fallback: look for closing </nav> of chip bar
        src = src.replace('</nav>', CHIP_HTML + '\n  </nav>', 1)
    # 2. inject section before </main>
    if SECTION_ANCHOR not in src:
        return src, False, f'anchor "{SECTION_ANCHOR}" not found'
    src = src.replace(SECTION_ANCHOR, SECTION_HTML + SECTION_ANCHOR, 1)
    return src, True, 'ok'

def patch_css(src):
    if GUARD in src:
        return src, False, 'already patched'
    marked = f'/* {GUARD} */\n' + CSS_ADDITIONS
    if CSS_ANCHOR in src:
        src = src.replace(CSS_ANCHOR, marked + '\n' + CSS_ANCHOR, 1)
    else:
        src += '\n' + marked
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
            shutil.copy(fname, fname + '.bak')
            write(fname, patched)
            print(f'       wrote {fname} (backup: {fname}.bak)')
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
