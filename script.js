/**
 * script.js  —  CompTIA & Tech Reference  |  2026 Edition
 * =========================================================
 * toggleDomain / toggleTopic / filter / toggleAll
 * toggleTheme / updateThemeUI
 * initSnapQuote / initCloudStack / initTouchFeedback
 * URL codec helpers
 */

// ── STATE ──────────────────────────────────────────────────────────────────
let allExpanded = false;

const QUOTES = [
  "The obstacle is the way. — Marcus Aurelius",
  "An unexamined life is not worth living. — Socrates",
  "Simplicity is the ultimate sophistication. — Leonardo da Vinci",
  "He who has a why can bear almost any how. — Nietzsche",
  "The Tao that can be told is not the eternal Tao. — Lao Tzu",
  "One must imagine Sisyphus happy. — Albert Camus",
  "We suffer more in imagination than in reality. — Seneca",
  "Before enlightenment, chop wood, carry water. — Zen proverb",
  "You have power over your mind, not outside events. — Marcus Aurelius",
  "The quieter you become, the more you can hear. — Ram Dass",
  "Amor fati — love your fate. — Nietzsche",
  "Water is the softest thing, yet it overcomes the hardest. — Lao Tzu",
  "To know yourself is the beginning of all wisdom. — Aristotle",
  "Security comes not from having things, but from releasing the need to control. — Epictetus",
  "In the middle of difficulty lies opportunity. — Albert Einstein",
  "Do not seek for things to happen the way you want them to. — Epictetus",
  "Peace comes from within. Do not seek it without. — Buddha",
  "The present moment always will have been. — Marcus Aurelius"
];

// ── ACCORDION ──────────────────────────────────────────────────────────────
function toggleDomain(h) {
  const b = h.nextElementSibling;
  const open = b.classList.toggle("open");
  h.classList.toggle("open", open);
}

function toggleTopic(h) {
  h.classList.toggle("open");
  h.nextElementSibling.classList.toggle("open");
}

// ── FILTER ─────────────────────────────────────────────────────────────────
function filter(domain, chip) {
  document.querySelectorAll(".chip").forEach(c => c.classList.remove("active"));
  chip.classList.add("active");
  document.querySelectorAll(".domain-section").forEach(s => {
    s.classList.toggle("hidden", domain !== "all" && s.dataset.domain !== domain);
  });
}

// ── EXPAND / COLLAPSE ALL ──────────────────────────────────────────────────
function toggleAll() {
  allExpanded = !allExpanded;
  document.querySelectorAll(".domain-header, .topic-header").forEach(h => h.classList.toggle("open", allExpanded));
  document.querySelectorAll(".domain-body, .topic-body").forEach(b => b.classList.toggle("open", allExpanded));
  const hdrBtn = document.getElementById("hdr-expand-btn");
  if (hdrBtn) {
    hdrBtn.title = allExpanded ? "Collapse all" : "Expand all";
    hdrBtn.setAttribute("aria-checked", allExpanded ? "true" : "false");
  }
}

// ── THEME ──────────────────────────────────────────────────────────────────
function toggleTheme() {
  const doc  = document.documentElement;
  const next = doc.getAttribute("data-theme") === "light" ? "dark" : "light";
  doc.setAttribute("data-theme", next);
  localStorage.setItem("theme", next);
  updateThemeUI(next);
}

function updateThemeUI(theme) {
  const btn = document.getElementById("hdr-theme-btn");
  if (btn) btn.setAttribute("aria-checked", theme === "light" ? "true" : "false");
}

// ── INIT THEME (prevent flash) ─────────────────────────────────────────────
(function () {
  const saved = localStorage.getItem("theme") || "dark";
  document.documentElement.setAttribute("data-theme", saved);
})();

// ── DOM READY ──────────────────────────────────────────────────────────────
document.addEventListener("DOMContentLoaded", () => {
  updateThemeUI(document.documentElement.getAttribute("data-theme"));
  initSnapQuote();
  initCloudStack();
  initTouchFeedback();

  // Filter chips — event delegation on the filter bar
  document.querySelector(".filter-bar")?.addEventListener("click", e => {
    const chip = e.target.closest(".chip");
    if (chip) filter(chip.dataset.domain || "all", chip);
  });

  // Accordion — event delegation on the container
  document.getElementById("domain-container")?.addEventListener("click", e => {
    const dh = e.target.closest(".domain-header");
    if (dh) { toggleDomain(dh); return; }
    const th = e.target.closest(".topic-header");
    if (th) toggleTopic(th);
  });

  // Header control buttons
  document.getElementById("hdr-theme-btn")?.addEventListener("click", toggleTheme);
  document.getElementById("hdr-expand-btn")?.addEventListener("click", toggleAll);
});

// ── SNAP QUOTE ─────────────────────────────────────────────────────────────
function initSnapQuote() {
  const el  = document.getElementById("sq-text");
  const box = document.getElementById("snap-quote");
  if (!el || !box) return;

  let idx = Math.floor(Math.random() * QUOTES.length);

  const show = (i) => {
    box.classList.remove("visible");
    setTimeout(() => {
      el.textContent = QUOTES[i % QUOTES.length];
      box.classList.add("visible");
    }, 600);
  };

  show(idx);
  setInterval(() => show(++idx), 8000);
}

// ── CLOUD RESPONSIBILITY MATRIX ────────────────────────────────────────────
function initCloudStack() {
  const container = document.getElementById("cloud-stack");
  if (!container) return;

  const layers = ["Applications","Data","Runtime","Middleware","OS","Virtualization","Servers","Storage","Networking"];
  const resp   = [[1,1,1,0],[1,1,1,0],[1,1,0,0],[1,1,0,0],[1,1,0,0],[1,0,0,0],[1,0,0,0],[1,0,0,0],[1,0,0,0]];

  layers.forEach((name, r) => {
    const row = document.createElement("div");
    row.className = "cloud-row";

    const lbl = document.createElement("div");
    lbl.className = "cloud-label";
    lbl.textContent = name;
    row.appendChild(lbl);

    resp[r].forEach((isCust, c) => {
      const cell = document.createElement("div");
      cell.className = `cloud-cell ${isCust ? `cloud-cell-c${c}` : "cloud-cell-provider"}`;
      cell.textContent = isCust ? "Customer" : "Provider";
      row.appendChild(cell);
    });
    container.appendChild(row);
  });
}

// ── TOUCH FEEDBACK ─────────────────────────────────────────────────────────
function initTouchFeedback() {
  document.querySelectorAll(".chip, .domain-header, .topic-header").forEach(el => {
    el.addEventListener("touchstart",  function() { this.classList.add("is-tapping");    }, { passive: true });
    el.addEventListener("touchend",    function() { this.classList.remove("is-tapping"); }, { passive: true });
    el.addEventListener("touchcancel", function() { this.classList.remove("is-tapping"); }, { passive: true });
  });
}

// ── URL CODEC WIDGET ───────────────────────────────────────────────────────
const _in  = () => document.getElementById("url-codec-input")?.value || "";
const _out = (v) => { const el = document.getElementById("url-codec-output"); if (el) el.value = v; };
const _msg = (txt, color = "var(--muted)") => {
  const el = document.getElementById("url-codec-msg");
  if (!el) return;
  el.textContent = txt;
  el.style.color = color;
  clearTimeout(el._t);
  el._t = setTimeout(() => el.textContent = "", 2500);
};

function urlToolEncode() {
  const raw = _in();
  if (!raw) return _msg("⚠ Nothing to encode.", "var(--amber)");
  try { _out(encodeURIComponent(raw)); _msg("✓ Encoded.", "var(--green)"); }
  catch (e) { _msg("✗ " + e.message, "var(--red)"); }
}

function urlToolDecode() {
  const raw = _in();
  if (!raw) return _msg("⚠ Nothing to decode.", "var(--amber)");
  try { _out(decodeURIComponent(raw.replace(/\+/g, " "))); _msg("✓ Decoded.", "var(--cyan)"); }
  catch (e) { _msg("✗ Malformed encoding.", "var(--red)"); }
}

function urlToolCopy() {
  const el = document.getElementById("url-codec-output");
  if (!el?.value) return _msg("⚠ Nothing to copy.", "var(--amber)");
  navigator.clipboard.writeText(el.value).then(() => _msg("✓ Copied.", "var(--green)"));
}

function urlToolClear() {
  const i = document.getElementById("url-codec-input");
  const o = document.getElementById("url-codec-output");
  if (i) i.value = "";
  if (o) o.value = "";
  _msg("");
}

// mental-disorders-p3
const DISORDER_DATA = {
  "IDD": {
    c: `A. Deficits in intellectual functions, such as reasoning, problem solving, planning, abstract thinking, judgment, academic learning, and learning from experience, confirmed by both clinical assessment and individualized, standardized intelligence testing. B. Deficits in adaptive functioning that result in failure to meet developmental and socio cultural standards for personal independence and social responsibility. Without ongo ing support, the adaptive deficits limit functioning in one or more activities of daily life, such as communication, social participation, and independent living, across multiple environments, such as home, school, work, and community. C. Onset of intellectual and adaptive deficits during the developmental period. Note: The diagnostic term intellectual disability is the equivalent term for the ICD-11 diag nosis of intellectual developmental disorders. Although the`,
    p: `Intellectual disability has an overall general population prevalence of approximately 1%, and prevalence rates vary by age. Prevalence for severe intellectual disability is approxi mately 6 per 1,000.`,
    r: `Genetic and physiological. Prenatal etiologies include genetic syndromes (e.g., se quence variations or copy number variants involving one or more genes; chromosomal disorders), inborn errors of metabolism, brain malformations, maternal disease (including placental disease), and environmental influences (e.g., alcohol, other drugs, toxins, terato gens). Perinatal causes include a variety of labor and delivery-related events leading to neonatal en`,
    d: `The diagnosis of intellectual disability should be made whenever Criteria A, B, and C are met. A diagnosis of intellectual disability should not be assumed because of a particular 40 Neurodevelopmental Disorders genetic or medical condition. A genetic syndrome linked to intellectual disability should be noted as a concurrent diagnosis with the intellectual disability. Major and mild neurocognitive disorders. Intellectual disability is categorized`,
  },
  "ASD": {
    c: `A. Persistent deficits in social communication and social interaction across multiple con texts, as manifested by the following, currently or by history (examples are illustrative, not exhaustive; see text): 1. Deficits in social-emotional reciprocity, ranging, for example, from abnormal social approach and failure of normal back-and-forth conversation; to reduced sharing of interests, emotions, or affect; to failure to initiate or respond to social interactions. 2. Deficits in nonverbal communicative behaviors used for social interaction, ranging, for example, from poorly integrated verbal and nonverbal communication; to abnor malities in eye contact and body language or deficits in understanding and use of gestures; to a total lack of facial expressions and nonverbal communication. 3. Deficits in developing, maintaining, and understanding relationships, ranging, for ex ample, from diff`,
    p: `In recent years, reported frequencies for autism spectrum disorder across U.S. and non U.S. countries have approached 1% of the population, with similar estimates in child and adult samples. It remains unclear whether higher rates reflect an expansion of the diag nostic criteria of DSM-IV to include subthreshold cases, increased awareness, differen`,
    r: `The best established prognostic factors for individual outcome within autism spectrum disorder are presence or absence of associated intellectual disability and language impair ment (e.g., functional language by age 5 years is a good prognostic sign) and additional mental health problems. Epilepsy, as a comorbid diagnosis, is associated with greater in tellectual disability and lower verbal ability. Environmental. A variety of nonspecific risk fa`,
    d: `for this disorder). First symptoms of autism spectrum disorder frequently involve delayed language de velopment, often accompanied by lack of social interest or unusual social interactions (e.g., pulling individuals by the hand without any attempt to look at them), odd play patterns (e.g., carrying toys around but never playing with them), and unusual communication patterns (e.g., knowing the alphabet but not responding to own name). Deafness may`,
  },
  "ADHD": {
    c: `A. A persistent pattern of inattention and/or hyperactivity-impulsivity that interferes with functioning or development, as characterized by (1) and/or (2): 1. Inattention: Six (or more) of the following symptoms have persisted for at least 6 months to a degree that is inconsistent with developmental level and that nega tively impacts directly on social and academic/occupational activities: Note: The symptoms are not solely a manifestation of oppositional behavior, defi ance, hostility, or failure to understand tasks or instructions. For older adolescents and adults (age 17 and older), at least five symptoms are required. a. Often fails to give close attention to details or makes careless mistakes in schoolwork, at work, or during other activities (e.g., overlooks or misses details, work is inaccurate). b. Often has difficulty sustaining attention in tasks or play activities (e.g., has d`,
    p: `Population surveys suggest that ADHD occurs in most cultures in about 5% of children and about 2.5% of adults. 62 Neurodevelopmental Disorders`,
    r: `Temperamental. ADHD is associated with reduced behavioral inhibition, effortful con trol, or constraint; negative emotionality; and/or elevated novelty seeking. These traits may predispose some children to ADHD but are not specific to the disorder. Environmental. Very low birth weight (less than 1,500 grams) conveys a twoto three fold risk for ADHD, but most children with low birth weight do not develop ADHD. Al though ADHD is correlated with smo`,
    d: `Oppositional defiant disorder. Individuals with oppositional defiant disorder may re sist work or school tasks that require self-application because they resist conforming to others' demands. Their behavior is characterized by negativity, hostility, and defiance. These symptoms must be differentiated from aversion to school or mentally demanding tasks due to difficulty in sustaining mental effort, forgetting instructions, and impulsivity in indiv`,
  },
  "SLD": {
    c: `A. Difficulties learning and using academic skills, as indicated by the presence of at least one of the following symptoms that have persisted for at least 6 months, despite the provision of interventions that target those difficulties: 1. Inaccurate or slow and effortful word reading (e.g., reads single words aloud incor rectly or slowly and hesitantly, frequently guesses words, has difficulty sounding out words). 2. Difficulty understanding the meaning of what is read (e.g., may read text accurately but not understand the sequence, relationships, inferences, or deeper meanings of what is read). 3. Difficulties with spelling (e.g., may add, omit, or substitute vowels or consonants). 4. Difficulties with written expression (e.g., makes multiple grammatical or punctua tion errors within sentences; employs poor paragraph organization; written expres sion of ideas lacks clarity). 5. Difficu`,
    p: `The prevalence of specific learning disorder across the academic domains of reading, writ ing, and mathematics is 5% 15% among school-age children across different languages and cultures. Prevalence in adults is unknown but appears to be approximately 4%.`,
    r: `Environmental. Prematurity or very low birth weight increases the risk for specific learning disorder, as does prenatal exposure to nicotine. Genetic and physiological. Specific learning disorder appears to aggregate in families, particularly when affecting reading, mathematics, and spelling. The relative risk of spe cific learning disorder in reading or mathematics is substantially higher (e.g., 4 8 times and 5 10 times higher, respectively) in `,
    d: `Normal variations in academic attainment. Specific learning disorder is distinguished from normal variations in academic attainment due to external factors (e.g., lack of edu cational opportunity, consistently poor instruction, learning in a second language), be cause the learning difficulties persist in the presence of adequate educational opportunity and exposure to the same instruction as the peer group, and competency in the language of instr`,
  },
  "SCZ": {
    c: `A. Two (or more) of the following, each present for a significant portion of time during a 1-month period (or less if successfully treated). At least one of these must be (1), (2), or (3): 1. Delusions. 2. Hallucinations. 3. Disorganized speech (e.g., frequent derailment or incoherence). 4. Grossly disorganized or catatonic behavior. 5. Negative symptoms (i.e., diminished emotional expression or avolition). B. For a significant portion of the time since the onset of the disturbance, level of function ing in one or more major areas, such as work, interpersonal relations, or self-care, is markedly below the level achieved prior to the onset (or when the onset is in childhood or adolescence, there is failure to achieve expected level of interpersonal, academic, or occupational functioning). C. Continuous signs of the disturbance persist for at least 6 months. This 6-month period must includ`,
    p: `The lifetime prevalence of schizophrenia appears to be approximately 0.3% 0.7%, al though there is reported variation by race/ethnicity, across countries, and by geographic origin for immigrants and children of immigrants. The sex ratio differs across samples and populations: for example, an emphasis on negative symptoms and longer duration of dis `,
    r: `Environmental. Season of birth has been linked to the incidence of schizophrenia, in cluding late winter/early spring in some locations and summer for the deficit form of the disease. The incidence of schizophrenia and related disorders is higher for children grow ing up in an urban environment and for some minority ethnic groups. Genetic and physiological. There is a strong contribution for genetic factors in deter mining risk for schizophrenia,`,
    d: `Major depressive or bipolar disorder with psychotic or catatonic features. The distinc tion between schizophrenia and major depressive or bipolar disorder with psychotic features or with catatonia depends on the temporal relationship between the mood distur bance and the psychosis, and on the severity of the depressive or manic symptoms. If de lusions or hallucinations occur exclusively during a major depressive or manic episode, the diagnosis is`,
  },
  "SZA": {
    c: `A. An uninterrupted period of illness during which there is a major mood episode (major depressive or manic) concurrent with Criterion A of schizophrenia. Note: The major depressive episode must include Criterion A1: Depressed mood. B. Delusions or hallucinations for 2 or more weeks in the absence of a major mood epi sode (depressive or manic) during the lifetime duration of the illness. C. Symptoms that meet criteria for a major mood episode are present for the majority of the total duration of the active and residual portions of the illness. D. The disturbance is not attributable to the effects of a substance (e.g., a drug of abuse, a medication) or another medical condition. 106 Schizophrenia Spectrum and Other Psychotic Disorders Specify whether: 295.70 (F25.0) Bipolar type: This subtype applies if a manic episode is part of the pre sentation. Major depressive episodes may also occur`,
    p: `Schizoaffective disorder appears to be about one-third as common as schizophrenia. Life time prevalence of schizoaffective disorder is estimated to be 0.3%. The incidence of 108 Schizophrenia Spectrum and Other Psychotic Disorders schizoaffective disorder is higher in females than in males, mainly due to an increased in cidence of the depressive ty`,
    r: `Genetic and physiological. Among individuals with schizophrenia, there may be an in creased risk for schizoaffective disorder in first-degree relatives. The risk for schizoaffec tive disorder may be increased among individuals who have a first-degree relative with schizophrenia, bipolar disorder, or schizoaffective disorder.`,
    d: `Other mental disorders and medical conditions. A wide variety of psychiatric and med ical conditions can manifest with psychotic and mood symptoms that must be considered in the differential diagnosis of schizoaffective disorder. These include psychotic disorder due to another medical condition; delirium; major neurocognitive disorder; substance/ medication-induced psychotic disorder or neurocognitive disorder; bipolar disorders with psychotic fe`,
  },
  "SZF": {
    c: `A. Two (or more) of the following, each present for a significant portion of time during a 1-month period (or less if successfully treated). At least one of these must be (1), (2), or (3): 1. Delusions. 2. Hallucinations. 3. Disorganized speech (e.g., frequent derailment or incoherence). 4. Grossly disorganized or catatonic behavior. 5. Negative symptoms (i.e., diminished emotional expression or avolition). Schizophreniform Disorder 97 B. An episode of the disorder lasts at least 1 month but less than 6 months. When the diagnosis must be made without waiting for recovery, it should be qualified as provi sional. C. Schizoaffective disorder and depressive or bipolar disorder with psychotic features have been ruled out because either 1) no major depressive or manic episodes have occurred concurrently with the active-phase symptoms, or 2) if mood episodes have occurred dur ing active-phase s`,
    p: `Incidence of schizophreniform disorder across sociocultural settings is likely similar to that observed in schizophrenia. In the United States and other developed countries, the in cidence is low, possibly fivefold less than that of schizophrenia. In developing countries, the incidence may be higher, especially for the specifier with good prognosti`,
    r: `Genetic and physiological. Relatives of individuals with schizophreniform disorder have an increased risk for schizophrenia.`,
    d: `Other mental disorders and medical conditions. A wide variety of mental and medical conditions can manifest with psychotic symptoms that must be considered in the differ ential diagnosis of schizophreniform disorder. These include psychotic disorder due to another medical condition or its treatment; delirium or major neurocognitive disorder; substance/medication-induced psychotic disorder or delirium; depressive or bipolar disorder with psychotic`,
  },
  "DD": {
    c: `A. The presence of one (or more) delusions with a duration of 1 month or longer. B. Criterion A for schizophrenia has never been met. Note: Hallucinations, if present, are not prominent and are related to the delusional theme (e.g., the sensation of being infested with insects associated with delusions of infestation). C. Apart from the impact of the delusion(s) or its ramifications, functioning is not markedly impaired, and behavior is not obviously bizarre or odd. D. If manic or major depressive episodes have occurred, these have been brief relative to the duration of the delusional periods. E. The disturbance is not attributable to the physiological effects of a substance or an other medical condition and is not better explained by another mental disorder, such as body dysmorphic disorder or obsessive-compulsive disorder.`,
    p: `The lifetime prevalence of delusional disorder has been estimated at around 0.2%, and the most frequent subtype is persecutory. Delusional disorder, jealous type, is probably more common in males than in females, but there are no major gender differences in the overall frequency of delusional disorder.`,
    r: `Temperamental. Preexisting personality disorders and traits (e.g., schizotypal person ality disorder; borderline personality disorder; or traits in the psychoticism domain, such as perceptual dysregulation, and the negative affectivity domain, such as suspiciousness) may predispose the individual to the development of the disorder.`,
    d: `Obsessive-compulsive and related disorders. If an individual with obsessive-compul sive disorder is completely convinced that his or her obsessive-compulsive disorder beliefs are true, then the diagnosis of obsessive-compulsive disorder, with absent insight/delu sional beliefs specifier, should be given rather than a diagnosis of delusional disorder. Similarly, if an individual with body dysmorphic disorder is completely convinced that his or her`,
  },
  "BPX": {
    c: `A. Presence of one (or more) of the following symptoms. At least one of these must be (1), (2), or (3): 1. Delusions. 2. Hallucinations. 3. Disorganized speech (e.g., frequent derailment or incoherence). 4. Grossly disorganized or catatonic behavior. Note: Do not include a symptom if it is a culturally sanctioned response. B. Duration of an episode of the disturbance is at least 1 day but less than 1 month, with eventual full return to premorbid level of functioning. C. The disturbance is not better explained by major depressive or bipolar disorder with psychotic features or another psychotic disorder such as schizophrenia or catatonia, and is not attributable to the physiological effects of a substance (e.g., a drug of abuse, a medication) or another medical condition.`,
    p: `In the United States, brief psychotic disorder may account for 9% of cases of first-onset psychosis. Psychotic disturbances that meet Criteria A and C, but not Criterion B, for brief psychotic disorder (i.e., duration of active symptoms is 1 6 months as opposed to remis sion within 1 month) are more common in developing countries than in developed `,
    r: `Temperamental. Preexisting personality disorders and traits (e.g., schizotypal person ality disorder; borderline personality disorder; or traits in the psychoticism domain, such as perceptual dysregulation, and the negative affectivity domain, such as suspiciousness) may predispose the individual to the development of the disorder.`,
    d: `Other medical conditions. A variety of medical disorders can manifest with psychotic symptoms of short duration. Psychotic disorder due to another medical condition or a de lirium is diagnosed when there is evidence from the history, physical examination, or lab oratory tests that the delusions or hallucinations are the direct physiological consequence of a specific medical condition (e.g., Cushing s syndrome, brain tumor) (see Psychotic Disorder`,
  },
  "BPI": {
    c: `A. A distinct period of abnormally and persistently elevated, expansive, or irritable mood and abnormally and persistently increased goal-directed activity or energy, lasting at least 1 week and present most of the day, nearly every day (or any duration if hospi talization is necessary). B. During the period of mood disturbance and increased energy or activity, three (or more) of the following symptoms (four if the mood is only irritable) are present to a sig nificant degree and represent a noticeable change from usual behavior: 1. Inflated self-esteem or grandiosity. 2. Decreased need for sleep (e.g., feels rested after only 3 hours of sleep). 3. More talkative than usual or pressure to keep talking. 4. Flight of ideas or subjective experience that thoughts are racing. 5. Distractibility (i.e., attention too easily drawn to unimportant or irrelevant external stimuli), as reported or obs`,
    p: `The 12-month prevalence estimate in the continental United States was 0.6% for bipolar I disorder as defined in DSM-IV. Twelve-month prevalence of bipolar I disorder across 11 countries ranged from 0.0% to 0.6%. The lifetime male-to-female prevalence ratio is ap proximately 1.1:1.`,
    r: `Environmental. Bipolar disorder is more common in high-income than in low-income countries (1.4 vs. 0.7%). Separated, divorced, or widowed individuals have higher rates of bipolar I disorder than do individuals who are married or have never been married, but the direction of the association is unclear. Genetic and physiological. A family history of bipolar disorder is one of the strongest and most consistent risk factors for bipolar disorders. Th`,
    d: `Major depressive disorder. Major depressive disorder may also be accompanied by hy pomanic or manic symptoms (i.e., fewer symptoms or for a shorter duration than required for mania or hypomania). When the individual presents in an episode of major depression, one must depend on corroborating history regarding past episodes of mania or hypoma nia. Symptoms of irritability may be associated with either major depressive disorder or bipolar disorder,`,
  },
  "BPII": {
    c: `A. A distinct period of abnormally and persistently elevated, expansive, or irritable mood and abnormally and persistently increased activity or energy, lasting at least 4 consec utive days and present most of the day, nearly every day. B. During the period of mood disturbance and increased energy and activity, three (or more) of the following symptoms have persisted (four if the mood is only irritable), represent a no ticeable change from usual behavior, and have been present to a significant degree: 1. Inflated self-esteem or grandiosity. 2. Decreased need for sleep (e.g., feels rested after only 3 hours of sleep). 3. More talkative than usual or pressure to keep talking. Bipolar II Disorder 133 4. Flight of ideas or subjective experience that thoughts are racing. 5. Distractibility (i.e., attention too easily drawn to unimportant or irrelevant external stimuli), as reported or observe`,
    p: `The 12-month prevalence of bipolar II disorder, internationally, is 0.3%. In the United States, 12-month prevalence is 0.8%. The prevalence rate of pediatric bipolar II disorder is difficult to establish. DSM-IV bipolar I, bipolar II, and bipolar disorder not otherwise spec ified yield a combined prevalence rate of 1.8% in U.S. and non-U.S. communi`,
    r: `Genetic and physiological. The risk of bipolar II disorder tends to be highest among rel atives of individuals with bipolar II disorder, as opposed to individuals with bipolar I dis order or major depressive disorder. There may be genetic factors influencing the age at onset for bipolar disorders. Course modifiers. A rapid-cycling pattern is associated with a poorer prognosis. Return to previous level of social function for individuals with bipol`,
    d: `Major depressive disorder. Perhaps the most challenging differential diagnosis to con sider is major depressive disorder, which may be accompanied by hypomanic or manic symptoms that do not meet full criteria (i.e., either fewer symptoms or a shorter duration than required for a hypomanic episode). This is especially true in evaluating individuals with symptoms of irritability, which may be associated with either major depressive dis order or bip`,
  },
  "CYC": {
    c: `A. For at least 2 years (at least 1 year in children and adolescents) there have been nu merous periods with hypomanic symptoms that do not meet criteria for a hypomanic episode and numerous periods with depressive symptoms that do not meet criteria for a major depressive episode. B. During the above 2-year period (1 year in children and adolescents), the hypomanic and depressive periods have been present for at least half the time and the individual has not been without the symptoms for more than 2 months at a time. C. Criteria for a major depressive, manic, or hypomanic episode have never been met. D. The symptoms in Criterion A are not better explained by schizoaffective disorder, schizophrenia, schizophreniform disorder, delusional disorder, or other specified or un specified schizophrenia spectrum and other psychotic disorder. E. The symptoms are not attributable to the physiologica`,
    p: `The lifetime prevalence of cyclothymic disorder is approximately 0.4% 1%. Prevalence in mood disorders clinics may range from 3% to 5%. In the general population, cyclothymic disorder is apparently equally common in males and females. In clinical settings, females with cyclothymic disorder may be more likely to present for treatment than males.`,
    r: `Genetic and physiological. Major depressive disorder, bipolar I disorder, and bipolar II disorder are more common among first-degree biological relatives of individuals with cyclo thymic disorder than in the general population. There may also be an increased familial risk of substance-related disorders. Cyclothymic disorder may be more common in the first-degree biological relatives of individuals with bipolar I disorder than in the general popul`,
    d: `Bipolar and related disorder due to another medical condition and depressive disorder due to another medical condition. The diagnosis of bipolar and related disorder due to another medical condition or depressive disorder due to another medical condition is made when the mood disturbance is judged to be attributable to the physiological effect of a specific, usually chronic medical condition (e.g., hyperthyroidism). This determination is based on`,
  },
  "MDD": {
    c: `A. Five (or more) of the following symptoms have been present during the same 2-week period and represent a change from previous functioning; at least one of the symptoms is either (1) depressed mood or (2) loss of interest or pleasure. Note: Do not include symptoms that are clearly attributable to another medical condition. 1. Depressed mood most of the day, nearly every day, as indicated by either subjec tive report (e.g., feels sad, empty, hopeless) or observation made by others (e.g., appears tearful). (Note: In children and adolescents, can be irritable mood.) 2. Markedly diminished interest or pleasure in all, or almost all, activities most of the day, nearly every day (as indicated by either subjective account or observation). Major Depressive Disorder 161 3. Significant weight loss when not dieting or weight gain (e.g., a change of more than 5% of body weight in a month), or decr`,
    p: `Twelve-month prevalence of major depressive disorder in the United States is approximately 7%, with marked differences by age group such that the prevalence in 18- to 29-year-old indi viduals is threefold higher than the prevalence in individuals age 60 years or older. Females ex perience 1.5- to 3-fold higher rates than males beginning in early ad`,
    r: `Temperamental. Neuroticism (negative affectivity) is a well-established risk factor for the onset of major depressive disorder, and high levels appear to render individuals more likely to develop depressive episodes in response to stressful life events. Environmental. Adverse childhood experiences, particularly when there are multiple experiences of diverse types, constitute a set of potent risk factors for major depressive dis order. Stressful l`,
    d: `Manic episodes with irritable mood or mixed episodes. Major depressive episodes with prominent irritable mood may be difficult to distinguish from manic episodes with irritable mood or from mixed episodes. This distinction requires a careful clinical evalua tion of the presence of manic symptoms. Mood disorder due to another medical condition. A major depressive episode is the appropriate diagnosis if the mood disturbance is not judged, based on `,
  },
  "PDD": {
    c: `A. Depressed mood for most of the day, for more days than not, as indicated by either subjective account or observation by others, for at least 2 years. Note: In children and adolescents, mood can be irritable and duration must be at least 1 year. B. Presence, while depressed, of two (or more) of the following: 1. Poor appetite or overeating. 2. Insomnia or hypersomnia. 3. Low energy or fatigue. 4. Low self-esteem. 5. Poor concentration or difficulty making decisions. 6. Feelings of hopelessness. C. During the 2-year period (1 year for children or adolescents) of the disturbance, the individ ual has never been without the symptoms in Criteria A and B for more than 2 months at a time. D. Criteria for a major depressive disorder may be continuously present for 2 years. E. There has never been a manic episode or a hypomanic episode, and criteria have never been met for cyclothymic disorder.`,
    p: `Persistent depressive disorder is effectively an amalgam of DSM-IV dysthymic disorder and chronic major depressive episode. The 12-month prevalence in the United States is approxi mately 0.5% for persistent depressive disorder and 1.5% for chronic major depressive disorder.`,
    r: `Temperamental. Factors predictive of poorer long-term outcome include higher levels of neuroticism (negative affectivity), greater symptom severity, poorer global functioning, and presence of anxiety disorders or conduct disorder. Environmental. Childhood risk factors include parental loss or separation. Genetic and physiological. There are no clear differences in illness development, course, or family history between DSM-IV dysthymic disorder an`,
    d: `Major depressive disorder. If there is a depressed mood plus two or more symptoms meeting criteria for a persistent depressive episode for 2 years or more, then the diagnosis of persistent depressive disorder is made. The diagnosis depends on the 2-year duration, which distinguishes it from episodes of depression that do not last 2 years. If the symptom Premenstrual Dysphoric Disorder 171 criteria are sufficient for a diagnosis of a major depress`,
  },
  "DMDD": {
    c: `A. Severe recurrent temper outbursts manifested verbally (e.g., verbal rages) and/or be haviorally (e.g., physical aggression toward people or property) that are grossly out of proportion in intensity or duration to the situation or provocation. B. The temper outbursts are inconsistent with developmental level. C. The temper outbursts occur, on average, three or more times per week. D. The mood between temper outbursts is persistently irritable or angry most of the day, nearly every day, and is observable by others (e.g., parents, teachers, peers). E. Criteria A D have been present for 12 or more months. Throughout that time, the indi vidual has not had a period lasting 3 or more consecutive months without all of the symptoms in Criteria A F. Criteria A and D are present in at least two of three settings (i.e., at home, at school, with peers) and are severe in at least one of these. G. T`,
    p: `Disruptive mood dysregulation disorder is common among children presenting to pedi atric mental health clinics. Prevalence estimates of the disorder in the community are un clear. Based on rates of chronic and severe persistent irritability, which is the core feature of the disorder, the overall 6-month to 1-year period-prevalence of disruptive moo`,
    r: `Temperamental. Children with chronic irritability typically exhibit complicated psy chiatric histories. In such children, a relatively extensive history of chronic irritability is 158 Depressive Disorders common, typically manifesting before full criteria for the syndrome are met. Such predi agnostic presentations may have qualified for a diagnosis of oppositional defiant disorder. Many children with disruptive mood dysregulation disorder have sy`,
    d: `Because chronically irritable children and adolescents typically present with complex histo ries, the diagnosis of disruptive mood dysregulation disorder must be made while consid ering the presence or absence of multiple other conditions. Despite the need to consider Disruptive Mood Dysregulation Disorder 159 many other syndromes, differentiation of disruptive mood dysregulation disorder from bi polar disorder and oppositional defiant disorder r`,
  },
  "PMDD": {
    c: `A. In the majority of menstrual cycles, at least five symptoms must be present in the final week before the onset of menses, start to improve within a few days after the onset of menses, and become minimal or absent in the week postmenses. B. One (or more) of the following symptoms must be present: 1. Marked affective lability (e.g., mood swings; feeling suddenly sad or tearful, or in creased sensitivity to rejection). 172 Depressive Disorders 2. Marked irritability or anger or increased interpersonal conflicts. 3. Marked depressed mood, feelings of hopelessness, or self-deprecating thoughts. 4. Marked anxiety, tension, and/or feelings of being keyed up or on edge. C. One (or more) of the following symptoms must additionally be present, to reach a total of five symptoms when combined with symptoms from Criterion B above. 1. Decreased interest in usual activities (e.g., work, school, frie`,
    p: `Twelve-month prevalence of premenstrual dysphoric disorder is between 1.8% and 5.8% of menstruating women. Estimates are substantially inflated if they are based on retro spective reports rather than prospective daily ratings. However, estimated prevalence based on a daily record of symptoms for 1 2 months may be less representative, as indi vidual`,
    r: `Environmental. Environmental factors associated with the expression of premenstrual dysphoric disorder include stress, history of interpersonal trauma, seasonal changes, and sociocultural aspects of female sexual behavior in general, and female gender role in par ticular. Genetic and physiological. Heritability of premenstrual dysphoric disorder is unknown. However, for premenstrual symptoms, estimates for heritability range between 30% and 80%, `,
    d: `Premenstrual syndrome. Premenstrual syndrome differs from premenstrual dysphoric disorder in that a minimum of five symptoms is not required, and there is no stipulation of affective symptoms for individuals who have premenstrual syndrome. This condition may be more common than premenstrual dysphoric disorder, although the estimated prevalence of premenstrual syndrome varies. While premenstrual syndrome shares the feature of symptom expression du`,
  },
  "GAD": {
    c: `A. Excessive anxiety and worry (apprehensive expectation), occurring more days than not for at least 6 months, about a number of events or activities (such as work or school performance). B. The individual finds it difficult to control the worry. C. The anxiety and worry are associated with three (or more) of the following six symp toms (with at least some symptoms having been present for more days than not for the past 6 months): Note: Only one item is required in children. 1. Restlessness or feeling keyed up or on edge. 2. Being easily fatigued. 3. Difficulty concentrating or mind going blank. 4. Irritability. 5. Muscle tension. 6. Sleep disturbance (difficulty falling or staying asleep, or restless, unsatisfying sleep). D. The anxiety, worry, or physical symptoms cause clinically significant distress or impair ment in social, occupational, or other important areas of functioning. E. T`,
    p: `The 12-month prevalence of generalized anxiety disorder is 0.9% among adolescents and 2.9% among adults in the general community of the United States. The 12-month preva lence for the disorder in other countries ranges from 0.4% to 3.6%. The lifetime morbid risk is 9.0%. Females are twice as likely as males to experience generalized anxiety disorde`,
    r: `Temperamental. Behavioral inhibition, negative affectivity (neuroticism), and harm avoidance have been associated with generalized anxiety disorder. Environmental. Although childhood adversities and parental overprotection have been associated with generalized anxiety disorder, no environmental factors have been identi fied as specific to generalized anxiety disorder or necessary or sufficient for making the di agnosis. Genetic and physiological.`,
    d: `Anxiety disorder due to another medical condition. The diagnosis of anxiety disorder associated with another medical condition should be assigned if the individual s anxiety and worry are judged, based on history, laboratory findings, or physical examination, to be a physiological effect of another specific medical condition (e.g., pheochromocytoma, hyperthyroidism). Substance/medication-induced anxiety disorder. A substance/medication-induced an`,
  },
  "PD": {
    c: `A. Recurrent unexpected panic attacks. A panic attack is an abrupt surge of intense fear or intense discomfort that reaches a peak within minutes, and during which time four (or more) of the following symptoms occur: Note: The abrupt surge can occur from a calm state or an anxious state. 1. Palpitations, pounding heart, or accelerated heart rate. 2. Sweating. 3. Trembling or shaking. 4. Sensations of shortness of breath or smothering. 5. Feelings of choking. 6. Chest pain or discomfort. 7. Nausea or abdominal distress. 8. Feeling dizzy, unsteady, light-headed, or faint. 9. Chills or heat sensations. 10. Paresthesias (numbness or tingling sensations). 11. Derealization (feelings of unreality) or depersonalization (being detached from one self). 12. Fear of losing control or going crazy. 13. Fear of dying. Note: Culture-specific symptoms (e.g., tinnitus, neck soreness, headache, uncontrol `,
    p: `In the general population, the 12-month prevalence estimate for panic disorder across the United States and several European countries is about 2% 3% in adults and adolescents. In the United States, significantly lower rates of panic disorder are reported among Latinos, African Americans, Caribbean blacks, and Asian Americans, compared with non-Lat`,
    r: `Temperamental. Negative affectivity (neuroticism) (i.e., proneness to experiencing neg ative emotions) and anxiety sensitivity (i.e., the disposition to believe that symptoms of anxiety are harmful) are risk factors for the onset of panic attacks and, separately, for worry about panic, although their risk status for the diagnosis of panic disorder is un known. History of fearful spells (i.e., limited-symptom attacks that do not meet full cri teri`,
    d: `Other specified anxiety disorder or unspecified anxiety disorder. Panic disorder should not be diagnosed if full-symptom (unexpected) panic attacks have never been experienced. In Panic Disorder 213 the case of only limited-symptom unexpected panic attacks, an other specified anxiety dis order or unspecified anxiety disorder diagnosis should be considered. Anxiety disorder due to another medical condition. Panic disorder is not diagnosed if the p`,
  },
  "AGO": {
    c: `A. Marked fear or anxiety about two (or more) of the following five situations: 1. Using public transportation (e.g., automobiles, buses, trains, ships, planes). 2. Being in open spaces (e.g., parking lots, marketplaces, bridges). 3. Being in enclosed places (e.g., shops, theaters, cinemas). 4. Standing in line or being in a crowd. 5. Being outside of the home alone. B. The individual fears or avoids these situations because of thoughts that escape might be difficult or help might not be available in the event of developing panic-like symp- 218 Anxiety Disorders toms or other incapacitating or embarrassing symptoms (e.g., fear of falling in the el derly; fear of incontinence). C. The agoraphobic situations almost always provoke fear or anxiety. D. The agoraphobic situations are actively avoided, require the presence of a companion, or are endured with intense fear or anxiety. E. The fear`,
    p: `Every year approximately 1.7% of adolescents and adults have a diagnosis of agoraphobia. Females are twice as likely as males to experience agoraphobia. Agoraphobia may occur in childhood, but incidence peaks in late adolescence and early adulthood. Twelve-month prevalence in individuals older than 65 years is 0.4%. Prevalence rates do not appear t`,
    r: `Temperamental. Behavioral inhibition and neurotic disposition (i.e., negative affectivity [neuroticism] and anxiety sensitivity) are closely associated with agoraphobia but are rel evant to most anxiety disorders (phobic disorders, panic disorder, generalized anxiety dis order). Anxiety sensitivity (the disposition to believe that symptoms of anxiety are harmful) is also characteristic of individuals with agoraphobia. Environmental. Negative even`,
    d: `When diagnostic criteria for agoraphobia and another disorder are fully met, both diagnoses should be assigned, unless the fear, anxiety, or avoidance of agoraphobia is attributable to the other disorder. Weighting of criteria and clinical judgment may be helpful in some cases. Agoraphobia 221 Specific phobia, situational type. Differentiating agoraphobia from situational specific phobia can be challenging in some cases, because these conditions `,
  },
  "SAD": {
    c: `A. Marked fear or anxiety about one or more social situations in which the individual is exposed to possible scrutiny by others. Examples include social interactions (e.g., hav ing a conversation, meeting unfamiliar people), being observed (e.g., eating or drink ing), and performing in front of others (e.g., giving a speech). Note: In children, the anxiety must occur in peer settings and not just during interac tions with adults. B. The individual fears that he or she will act in a way or show anxiety symptoms that will be negatively evaluated (i.e., will be humiliating or embarrassing; will lead to rejection or offend others). C. The social situations almost always provoke fear or anxiety. Note: In children, the fear or anxiety may be expressed by crying, tantrums, freezing, clinging, shrinking, or failing to speak in social situations. D. The social situations are avoided or endured wi`,
    p: `The 12-month prevalence estimate of social anxiety disorder for the United States is ap proximately 7%. Lower 12-month prevalence estimates are seen in much of the world us ing the same diagnostic instrument, clustering around 0.5% 2.0%; median prevalence in Europe is 2.3%. The 12-month prevalence rates in children and adolescents are comparable to`,
    r: `Temperamental. Underlying traits that predispose individuals to social anxiety disor der include behavioral inhibition and fear of negative evaluation. Environmental. There is no causative role of increased rates of childhood maltreatment or other early-onset psychosocial adversity in the development of social anxiety disorder. How ever, childhood maltreatment and adversity are risk factors for social anxiety disorder. Genetic and physiological. `,
    d: `Normative shyness. Shyness (i.e., social reticence) is a common personality trait and is not by itself pathological. In some societies, shyness is even evaluated positively. How ever, when there is a significant adverse impact on social, occupational, and other impor tant areas of functioning, a diagnosis of social anxiety disorder should be considered, and when full diagnostic criteria for social anxiety disorder are met, the disorder should be `,
  },
  "SPH": {
    c: `A. Marked fear or anxiety about a specific object or situation (e.g., flying, heights, animals, receiving an injection, seeing blood). Note: In children, the fear or anxiety may be expressed by crying, tantrums, freezing, or clinging. B. The phobic object or situation almost always provokes immediate fear or anxiety. C. The phobic object or situation is actively avoided or endured with intense fear or anxiety. D. The fear or anxiety is out of proportion to the actual danger posed by the specific object or situation and to the sociocultural context. E. The fear, anxiety, or avoidance is persistent, typically lasting for 6 months or more. F. The fear, anxiety, or avoidance causes clinically significant distress or impairment in social, occupational, or other important areas of functioning. G. The disturbance is not better explained by the symptoms of another mental disorder, including fear`,
    p: `In the United States, the 12-month community prevalence estimate for specific phobia is approximately 7% 9%. Prevalence rates in European countries are largely similar to those in the United States (e.g., about 6%), but rates are generally lower in Asian, African, and Latin American countries (2% 4%). Prevalence rates are approximately 5% in childr`,
    r: `Temperamental. Temperamental risk factors for specific phobia, such as negative affec tivity (neuroticism) or behavioral inhibition, are risk factors for other anxiety disorders as well. Environmental. Environmental risk factors for specific phobias, such as parental over protectiveness, parental loss and separation, and physical and sexual abuse, tend to pre dict other anxiety disorders as well. As noted earlier, negative or traumatic encounters`,
    d: `Agoraphobia. Situational specific phobia may resemble agoraphobia in its clinical pre sentation, given the overlap in feared situations (e.g., flying, enclosed places, elevators). If an individual fears only one of the agoraphobia situations, then specific phobia, situa tional, may be diagnosed. If two or more agoraphobic situations are feared, a diagnosis of agoraphobia is likely warranted. For example, an individual who fears airplanes and ele `,
  },
  "SEP": {
    c: `A. Developmentally inappropriate and excessive fear or anxiety concerning separation from those to whom the individual is attached, as evidenced by at least three of the following: 1. Recurrent excessive distress when anticipating or experiencing separation from home or from major attachment figures. Separation Anxiety Disorder 191 2. Persistent and excessive worry about losing major attachment figures or about pos sible harm to them, such as illness, injury, disasters, or death. 3. Persistent and excessive worry about experiencing an untoward event (e.g., getting lost, being kidnapped, having an accident, becoming ill) that causes separation from a major attachment figure. 4. Persistent reluctance or refusal to go out, away from home, to school, to work, or elsewhere because of fear of separation. 5. Persistent and excessive fear of or reluctance about being alone or without major attac`,
    p: `The 12-month prevalence of separation anxiety disorder among adults in the United States is 0.9% 1.9%. In children, 6- to 12-month prevalence is estimated to be approximately 4%. In adolescents in the United States, the 12-month prevalence is 1.6%. Separation anxiety disorder decreases in prevalence from childhood through adolescence and adulthood `,
    r: `Environmental. Separation anxiety disorder often develops after life stress, especially a loss (e.g., the death of a relative or pet; an illness of the individual or a relative; a change of schools; parental divorce; a move to a new neighborhood; immigration; a disaster that in volved periods of separation from attachment figures). In young adults, other examples of life stress include leaving the parental home, entering into a romantic relations`,
    d: `Generalized anxiety disorder. Separation anxiety disorder is distinguished from gener alized anxiety disorder in that the anxiety predominantly concerns separation from attach ment figures, and if other worries occur, they do not predominate the clinical picture. Panic disorder. Threats of separation may lead to extreme anxiety and even a panic at tack. In separation anxiety disorder, in contrast to panic disorder, the anxiety concerns the possib`,
  },
  "SM": {
    c: `A. Consistent failure to speak in specific social situations in which there is an expectation for speaking (e.g., at school) despite speaking in other situations. B. The disturbance interferes with educational or occupational achievement or with social communication. C. The duration of the disturbance is at least 1 month (not limited to the first month of school). D. The failure to speak is not attributable to a lack of knowledge of, or comfort with, the spoken language required in the social situation. E. The disturbance is not better explained by a communication disorder (e.g., childhood onset fluency disorder) and does not occur exclusively during the course of autism spectrum disorder, schizophrenia, or another psychotic disorder.`,
    p: `Selective mutism is a relatively rare disorder and has not been included as a diagnostic cat egory in epidemiological studies of prevalence of childhood disorders. Point prevalence using various clinic or school samples ranges between 0.03% and 1% depending on the set ting (e.g., clinic vs. school vs. general population) and ages of the individuals`,
    r: `Temperamental. Temperamental risk factors for selective mutism are not well identi fied. Negative affectivity (neuroticism) or behavioral inhibition may play a role, as may parental history of shyness, social isolation, and social anxiety. Children with selective mutism may have subtle receptive language difficulties compared with their peers, al though receptive language is still within the normal range. Environmental. Social inhibition on the p`,
    d: `Communication disorders. Selective mutism should be distinguished from speech dis turbances that are better explained by a communication disorder, such as language disorder, speech sound disorder (previously phonological disorder), childhood-onset fluency disorder (stuttering), or pragmatic (social) communication disorder. Unlike selec tive mutism, the speech disturbance in these conditions is not restricted to a specific social situation. Neurod`,
  },
  "OCD": {
    c: `A. Presence of obsessions, compulsions, or both: Obsessions are defined by (1) and (2): 1. Recurrent and persistent thoughts, urges, or images that are experienced, at some time during the disturbance, as intrusive and unwanted, and that in most individuals cause marked anxiety or distress. 2. The individual attempts to ignore or suppress such thoughts, urges, or images, or to neutralize them with some other thought or action (i.e., by performing a compulsion). Compulsions are defined by (1) and (2): 1. Repetitive behaviors (e.g., hand washing, ordering, checking) or mental acts (e.g., praying, counting, repeating words silently) that the individual feels driven to per form in response to an obsession or according to rules that must be applied rigidly. 2. The behaviors or mental acts are aimed at preventing or reducing anxiety or dis tress, or preventing some dreaded event or situation; `,
    p: `The 12-month prevalence of OCD in the United States is 1.2%, with a similar prevalence in ternationally (1.1% 1.8%). Females are affected at a slightly higher rate than males in adulthood, although males are more commonly affected in childhood.`,
    r: `Temperamental. Greater internalizing symptoms, higher negative emotionality, and behavioral inhibition in childhood are possible temperamental risk factors. Environmental. Physical and sexual abuse in childhood and other stressful or traumatic events have been associated with an increased risk for developing OCD. Some children 240 Obsessive-Compulsive and Related Disorders may develop the sudden onset of obsessive-compulsive symptoms, which has b`,
    d: `Anxiety disorders. Recurrent thoughts, avoidant behaviors, and repetitive requests for reassurance can also occur in anxiety disorders. However, the recurrent thoughts that are present in generalized anxiety disorder (i.e., worries) are usually about real-life concerns, whereas the obsessions of OCD usually do not involve real-life concerns and can include content that is odd, irrational, or of a seemingly magical nature; moreover, compulsions ar`,
  },
  "BDD": {
    c: `A. Preoccupation with one or more perceived defects or flaws in physical appearance that are not observable or appear slight to others. B. At some point during the course of the disorder, the individual has performed repetitive behaviors (e.g., mirror checking, excessive grooming, skin picking, reassurance seek ing) or mental acts (e.g., comparing his or her appearance with that of others) in re sponse to the appearance concerns. C. The preoccupation causes clinically significant distress or impairment in social, occu pational, or other important areas of functioning. D. The appearance preoccupation is not better explained by concerns with body fat or weight in an individual whose symptoms meet diagnostic criteria for an eating disorder. Body Dysmorphic Disorder 243`,
    p: `The point prevalence among U.S. adults is 2.4% (2.5% in females and 2.2% in males). Out side the United States (i.e., Germany), current prevalence is approximately 1.7% 1.8%, with a gender distribution similar to that in the United States. The current prevalence is 15% among dermatology patients, 7% 8% among U.S. cosmetic surgery patients, 3% 16% a`,
    r: `Environmental. Body dysmorphic disorder has been associated with high rates of child hood neglect and abuse. Genetic and physiological. The prevalence of body dysmorphic disorder is elevated in first-degree relatives of individuals with obsessive-compulsive disorder (OCD).`,
    d: `Normal appearance concerns and clearly noticeable physical defects. Body dysmor phic disorder differs from normal appearance concerns in being characterized by exces- 246 Obsessive-Compulsive and Related Disorders sive appearance-related preoccupations and repetitive behaviors that are time-consuming, are usually difficult to resist or control, and cause clinically significant distress or impair ment in functioning. Physical defects that are clea`,
  },
  "HD": {
    c: `A. Persistent difficulty discarding or parting with possessions, regardless of their actual value. B. This difficulty is due to a perceived need to save the items and to distress associated with discarding them. C. The difficulty discarding possessions results in the accumulation of possessions that congest and clutter active living areas and substantially compromises their intended use. If living areas are uncluttered, it is only because of the interventions of third parties (e.g., family members, cleaners, authorities). D. The hoarding causes clinically significant distress or impairment in social, occupa tional, or other important areas of functioning (including maintaining a safe environ ment for self and others). E. The hoarding is not attributable to another medical condition (e.g., brain injury, cere brovascular disease, Prader-Willi syndrome). F. The hoarding is not better explai`,
    p: `Nationally representative prevalence studies of hoarding disorder are not available. Com munity surveys estimate the point prevalence of clinically significant hoarding in the United States and Europe to be approximately 2% 6%. Hoarding disorder affects both males and females, but some epidemiological studies have reported a significantly greater p`,
    r: `Temperamental. Indecisiveness is a prominent feature of individuals with hoarding dis order and their first-degree relatives. Environmental. Individuals with hoarding disorder often retrospectively report stressful and traumatic life events preceding the onset of the disorder or causing an exacerbation. Genetic and physiological. Hoarding behavior is familial, with about 50% of individu als who hoard reporting having a relative who also hoards. T`,
    d: `Other medical conditions. Hoarding disorder is not diagnosed if the symptoms are judged to be a direct consequence of another medical condition (Criterion E), such as trau matic brain injury, surgical resection for treatment of a tumor or seizure control, cerebro vascular disease, infections of the central nervous system (e.g., herpes simplex encephalitis), or neurogenetic conditions such as Prader-Willi syndrome. Damage to the anterior ven trome`,
  },
  "TTM": {
    c: `A. Recurrent pulling out of one s hair, resulting in hair loss. B. Repeated attempts to decrease or stop hair pulling. C. The hair pulling causes clinically significant distress or impairment in social, occupa tional, or other important areas of functioning. D. The hair pulling or hair loss is not attributable to another medical condition (e.g., a der matological condition). E. The hair pulling is not better explained by the symptoms of another mental disorder (e.g., attempts to improve a perceived defect or flaw in appearance in body dysmorphic disorder).`,
    p: `In the general population, the 12-month prevalence estimate for trichotillomania in adults and adolescents is 1% 2%. Females are more frequently affected than males, at a ratio of approximately 10:1. This estimate likely reflects the true gender ratio of the condition, al though it may also reflect differential treatment seeking based on gender or `,
    r: `Genetic and physiological. There is evidence for a genetic vulnerability to trichotillo mania. The disorder is more common in individuals with obsessive-compulsive disorder (OCD) and their first-degree relatives than in the general population.`,
    d: `Normative hair removal/manipulation. Trichotillomania should not be diagnosed when hair removal is performed solely for cosmetic reasons (i.e., to improve one s physical ap pearance). Many individuals twist and play with their hair, but this behavior does not usu ally qualify for a diagnosis of trichotillomania. Some individuals may bite rather than pull hair; again, this does not qualify for a diagnosis of trichotillomania. Other obsessive-compu`,
  },
  "EXD": {
    c: `A. Recurrent skin picking resulting in skin lesions. B. Repeated attempts to decrease or stop skin picking. C. The skin picking causes clinically significant distress or impairment in social, occupa tional, or other important areas of functioning. D. The skin picking is not attributable to the physiological effects of a substance (e.g., co caine) or another medical condition (e.g., scabies). E. The skin picking is not better explained by symptoms of another mental disorder (e.g., delusions or tactile hallucinations in a psychotic disorder, attempts to improve a per ceived defect or flaw in appearance in body dysmorphic disorder, stereotypies in ste reotypic movement disorder, or intention to harm oneself in nonsuicidal self-injury).`,
    p: `In the general population, the lifetime prevalence for excoriation disorder in adults is 1.4% or somewhat higher. Three-quarters or more of individuals with the disorder are female. This likely reflects the true gender ratio of the condition, although it may also reflect dif ferential treatment seeking based on gender or cultural attitudes regardin`,
    r: `Genetic and physiological. Excoriation disorder is more common in individuals with obsessive-compulsive disorder (OCD) and their first-degree family members than in the general population.`,
    d: `Psychotic disorder. Skin picking may occur in response to a delusion (i.e., parasitosis) or tactile hallucination (i.e., formication) in a psychotic disorder. In such cases, excoriation disorder should not be diagnosed. Other obsessive-compulsive and related disorders. Excessive washing compulsions in response to contamination obsessions in individuals with OCD may lead to skin lesions, and skin picking may occur in individuals with body dysmorph`,
  },
  "PTSD": {
    c: `A. Exposure to actual or threatened death, serious injury, or sexual violence in one (or more) of the following ways: 1. Directly experiencing the traumatic event(s). 2. Witnessing, in person, the event(s) as it occurred to others. 3. Learning that the traumatic event(s) occurred to a close family member or close friend. In cases of actual or threatened death of a family member or friend, the event(s) must have been violent or accidental. 4. Experiencing repeated or extreme exposure to aversive details of the traumatic event(s) (e.g., first responders collecting human remains; police officers repeatedly exposed to details of child abuse). Note: Criterion A4 does not apply to exposure through electronic media, television, movies, or pictures, unless this exposure is work related. B. Presence of one (or more) of the following intrusion symptoms associated with the traumatic event(s), begin`,
    p: `In the United States, projected lifetime risk for PTSD using DSM-IV criteria at age 75 years is 8.7%. Twelve-month prevalence among U.S. adults is about 3.5%. Lower estimates are seen in Europe and most Asian, African, and Latin American countries, clustering around 0.5% 1.0%. Although different groups have different levels of exposure to traumatic`,
    r: `Risk (and protective) factors are generally divided into pretraumatic, peritraumatic, and posttraumatic factors. Pretraumatic factors Temperamental. These include childhood emotional problems by age 6 years (e.g., prior traumatic exposure, externalizing or anxiety problems) and prior mental disorders (e.g., panic disorder, depressive disorder, PTSD, or obsessive-compulsive disorder [OCD]). Environmental. These include lower socioeconomic status; `,
    d: `Adjustment disorders. In adjustment disorders, the stressor can be of any severity or type rather than that required by PTSD Criterion A. The diagnosis of an adjustment dis order is used when the response to a stressor that meets PTSD Criterion A does not meet all other PTSD criteria (or criteria for another mental disorder). An adjustment disorder is also diagnos`,
  },
  "ASD-T": {
    c: `A. Exposure to actual or threatened death, serious injury, or sexual violation in one (or more) of the following ways: 1. Directly experiencing the traumatic event(s). 2. Witnessing, in person, the event(s) as it occurred to others. 3. Learning that the event(s) occurred to a close family member or close friend. Note: In cases of actual or threatened death of a family member or friend, the event(s) must have been violent or accidental. 4. Experiencing repeated or extreme exposure to aversive details of the traumatic event(s) (e.g., first responders collecting human remains, police officers repeatedly exposed to details of child abuse). Note: This does not apply to exposure through electronic media, television, mov ies, or pictures, unless this exposure is work related. B. Presence of nine (or more) of the following symptoms from any of the five categories of intrusion, negative mood, dis`,
    p: `The prevalence of acute stress disorder in recently trauma-exposed populations (i.e., within 1 month of trauma exposure) varies according to the nature of the event and the context in which it is assessed. In both U.S. and non-U.S. populations, acute stress disorder tends to be identified in less than 20% of cases following traumatic events that do`,
    r: `Temperamental. Risk factors include prior mental disorder, high levels of negative af fectivity (neuroticism), greater perceived severity of the traumatic event, and an avoidant coping style. Catastrophic appraisals of the traumatic experience, often characterized by exaggerated appraisals of future harm, guilt, or hopelessness, are strongly predictive of acute stress disorder. Environmental. First and foremost, an individual must be exposed to a`,
    d: `Adjustment disorders. In acute stress disorder, the stressor can be of any severity rather than of the severity and type required by Criterion A of acute stress disorder. The diagnosis of an adjustment disorder is used when the response to a Criterion A event does not meet the cri teria for acute stress disorder (or another specific mental disorder) and when the symptom pat tern of acute stress disorder occurs in response to a stressor that does `,
  },
  "ADJ": {
    c: `A. The development of emotional or behavioral symptoms in response to an identifiable stressor(s) occurring within 3 months of the onset of the stressor(s). B. These symptoms or behaviors are clinically significant, as evidenced by one or both of the following: 1. Marked distress that is out of proportion to the severity or intensity of the stressor, taking into account the external context and the cultural factors that might influence symptom severity and presentation. 2. Significant impairment in social, occupational, or other important areas of functioning. C. The stress-related disturbance does not meet the criteria for another mental disorder and is not merely an exacerbation of a preexisting mental disorder. Adjustment Disorders 287 D. The symptoms do not represent normal bereavement. E. Once the stressor or its consequences have terminated, the symptoms do not persist for more tha`,
    p: `Adjustment disorders are common, although prevalence may vary widely as a function of the population studied and the assessment methods used. The percentage of individuals in outpatient mental health treatment with a principal diagnosis of an adjustment disorder ranges from approximately 5% to 20%. In a hospital psychiatric consultation setting, it`,
    r: `Environmental. Individuals from disadvantaged life circumstances experience a high rate of stressors and may be at increased risk for adjustment disorders.`,
    d: `Major depressive disorder. If an individual has symptoms that meet criteria for a major depressive disorder in response to a stressor, the diagnosis of an adjustment disorder is not applicable. The symptom profile of major depressive disorder differentiates it from ad justment disorders. Posttraumatic stress disorder and acute stress disorder. In adjustment disorders, the stressor can be of any severity rather than of the severity and type requir`,
  },
  "RAD": {
    c: `A. A consistent pattern of inhibited, emotionally withdrawn behavior toward adult caregiv ers, manifested by both of the following: 1. The child rarely or minimally seeks comfort when distressed. 2. The child rarely or minimally responds to comfort when distressed. B. A persistent social and emotional disturbance characterized by at least two of the following: 1. Minimal social and emotional responsiveness to others. 2. Limited positive affect. 3. Episodes of unexplained irritability, sadness, or fearfulness that are evident even during nonthreatening interactions with adult caregivers. C. The child has experienced a pattern of extremes of insufficient care as evidenced by at least one of the following: 1. Social neglect or deprivation in the form of persistent lack of having basic emotional needs for comfort, stimulation, and affection met by caregiving adults. 266 Traumaand Stressor-Re`,
    p: `The prevalence of reactive attachment disorder is unknown, but the disorder is seen rela tively rarely in clinical settings. The disorder has been found in young children exposed to severe neglect before being placed in foster care or raised in institutions. However, even in populations of severely neglected children, the disorder is uncommon, occu`,
    r: `Environmental. Serious social neglect is a diagnostic requirement for reactive attach ment disorder and is also the only known risk factor for the disorder. However, the ma jority of severely neglected children do not develop the disorder. Prognosis appears to depend on the quality of the caregiving environment following serious neglect.`,
    d: `Autism spectrum disorder. Aberrant social behaviors manifest in young children with reactive attachment disorder, but they also are key features of autism spectrum disorder. Specifically, young children with either condition can manifest dampened expression of positive emotions, cognitive and language delays, and impairments in social reciprocity. As a result, reactive attachment disorder must be differentiated from autism spectrum dis order. The`,
  },
  "DID": {
    c: `A. Disruption of identity characterized by two or more distinct personality states, which may be described in some cultures as an experience of possession. The disruption in identity involves marked discontinuity in sense of self and sense of agency, accompa nied by related alterations in affect, behavior, consciousness, memory, perception, cognition, and/or sensory-motor functioning. These signs and symptoms may be ob served by others or reported by the individual. B. Recurrent gaps in the recall of everyday events, important personal information, and/ or traumatic events that are inconsistent with ordinary forgetting. C. The symptoms cause clinically significant distress or impairment in social, occupa tional, or other important areas of functioning. D. The disturbance is not a normal part of a broadly accepted cultural or religious practice. Note: In children, the symptoms are not bet`,
    p: `The 12-month prevalence of dissociative identity disorder among adults in a small U.S. community study was 1.5%. The prevalence across genders in that study was 1.6% for males and 1.4% for females.`,
    r: `Environmental. Interpersonal physical and sexual abuse is associated with an increased risk of dissociative identity disorder. Prevalence of childhood abuse and neglect in the Dissociative Identity Disorder 295 United States, Canada, and Europe among those with the disorder is about 90%. Other forms of traumatizing experiences, including childhood medical and surgical procedures, war, childhood prostitution, and terrorism, have been reported. Cou`,
    d: `Other specified dissociative disorder. The core of dissociative identity disorder is the division of identity, with recurrent disruption of conscious functioning and sense of self. This central feature is shared with one form of other specified dissociative disorder, which may be distinguished from dissociative identity disorder by the presence of chronic or re current mixed dissociative symptoms that do not meet Criterion A for dissociative iden`,
  },
  "DA": {
    c: `A. An inability to recall important autobiographical information, usually of a traumatic or stressful nature, that is inconsistent with ordinary forgetting. Note: Dissociative amnesia most often consists of localized or selective amnesia for a specific event or events; or generalized amnesia for identity and life history. B. The symptoms cause clinically significant distress or impairment in social, occupa tional, or other important areas of functioning. C. The disturbance is not attributable to the physiological effects of a substance (e.g., al cohol or other drug of abuse, a medication) or a neurological or other medical condition (e.g., partial complex seizures, transient global amnesia, sequelae of a closed head in jury/traumatic brain injury, other neurological condition). D. The disturbance is not better explained by dissociative identity disorder, posttraumatic stress disorder, ac`,
    p: `The 12-month prevalence for dissociative amnesia among adults in a small U.S. commu nity study was 1.8% (1.0% for males; 2.6% for females).`,
    r: `Environmental. Single or repeated traumatic experiences (e.g., war, childhood maltreat ment, natural disaster, internment in concentration camps, genocide) are common ante- 300 Dissociative Disorders cedents. Dissociative amnesia is more likely to occur with 1) a greater number of adverse childhood experiences, particularly physical and/or sexual abuse, 2) interpersonal vio lence; and 3) increased severity, frequency, and violence of the trauma. `,
    d: `Dissociative identity disorder. Individuals with dissociative amnesia may report de personalization and auto-hypnotic symptoms. Individuals with dissociative identity dis order report pervasive discontinuities in sense of self and agency, accompanied by many other dissociative symptoms. The amnesias of individuals with localized, selective, and/ or systematized dissociative amnesias are relatively stable. Amnesias in dissociative iden tity disord`,
  },
  "DPDR": {
    c: `A. The presence of persistent or recurrent experiences of depersonalization, derealiza tion, or both: 1. Depersonalization: Experiences of unreality, detachment, or being an outside ob server with respect to one s thoughts, feelings, sensations, body, or actions (e.g., perceptual alterations, distorted sense of time, unreal or absent self, emotional and/ or physical numbing). 2. Derealization: Experiences of unreality or detachment with respect to surround ings (e.g., individuals or objects are experienced as unreal, dreamlike, foggy, life less, or visually distorted). B. During the depersonalization or derealization experiences, reality testing remains intact. C. The symptoms cause clinically significant distress or impairment in social, occupa tional, or other important areas of functioning. D. The disturbance is not attributable to the physiological effects of a substance (e.g., a dru`,
    p: `Transient depersonalization/derealization symptoms lasting hours to days are common in the general population. The 12-month prevalence of depersonalization/derealization disorder is thought to be markedly less than for transient symptoms, although precise es timates for the disorder are unavailable. In general, approximately one-half of all adults `,
    r: `Temperamental. Individuals with depersonalization/derealization disorder are charac terized by harm-avoidant temperament, immature defenses, and both disconnection and overconnection schemata. Immature defenses such as idealization/devaluation, projec tion and acting out result in denial of reality and poor adaptation. Cognitive disconnection schemata reflect defectiveness and emotional inhibition and subsume themes of abuse, ne glect, and depriv`,
    d: `Illness anxiety disorder. Although individuals with depersonalization/derealization dis order can present with vague somatic complaints as well as fears of permanent brain dam age, the diagnosis of depersonalization/derealization disorder is characterized by the presence of a constellation of typical depersonalization/derealization symptoms and the ab sence of other manifestations of illness anxiety disorder. Major depressive disorder. Feelings o`,
  },
  "IAD": {
    c: `A. Preoccupation with having or acquiring a serious illness. B. Somatic symptoms are not present or, if present, are only mild in intensity. If another medical condition is present or there is a high risk for developing a medical condition (e.g., strong family history is present), the preoccupation is clearly excessive or dispro portionate. C. There is a high level of anxiety about health, and the individual is easily alarmed about personal health status. D. The individual performs excessive health-related behaviors (e.g., repeatedly checks his or her body for signs of illness) or exhibits maladaptive avoidance (e.g., avoids doc tor appointments and hospitals). E. Illness preoccupation has been present for at least 6 months, but the specific illness that is feared may change over that period of time. F. The illness-related preoccupation is not better explained by another mental disorder,`,
    p: `Prevalence estimates of illness anxiety disorder are based on estimates of the DSM-III and DSM-IV diagnosis hypochondriasis. The 1- to 2-year prevalence of health anxiety and/or disease conviction in community surveys and population-based samples ranges from 1.3% to 10%. In ambulatory medical populations, the 6-month/1-year prevalence rates are be `,
    r: `Environmental. Illness anxiety disorder may sometimes be precipitated by a major life stress or a serious but ultimately benign threat to the individual s health. A history of child- Illness Anxiety Disorder 317 hood abuse or of a serious childhood illness may predispose to development of the disor der in adulthood. Course modifiers. Approximately one-third to one-half of individuals with illness anx iety disorder have a transient form, which is `,
    d: `Other medical conditions. The first differential diagnostic consideration is an underly ing medical condition, including neurological or endocrine conditions, occult malignan cies, and other diseases that affect multiple body systems. The presence of a medical condition does not rule out the possibility of coexisting illness anxiety disorder. If a med ical condition is present, the health-related anxiety and disease concerns are clearly dis propo`,
  },
  "AN": {
    c: `A. Restriction of energy intake relative to requirements, leading to significantly low body weight in the context of age, sex, developmental trajectory, and physical health. nificantly low weight is defined as a weight that is less than minimally normal or, for children and adolescents, less than that minimally expected. B. Intense fear of gaining weight or of becoming fat, or persistent behavior that interferes with weight gain, even though at a significantly low weight. Anorexia Nervosa 339 C. Disturbance in the way in which one s body weight or shape is experienced, undue in fluence of body weight or shape on self-evaluation, or persistent lack of recognition of the seriousness of the current low body weight. Coding note: The ICD-9-CM code for anorexia nervosa is 307.1, which is assigned re gardless of the subtype. The ICD-10-CM code depends on the subtype (see below).`,
    p: `The 12-month prevalence of anorexia nervosa among young females is approximately 0.4%. Less is known about prevalence among males, but anorexia nervosa is far less com mon in males than in females, with clinical populations generally reflecting approximately a 10:1 female-to-male ratio.`,
    r: `Temperamental. Individuals who develop anxiety disorders or display obsessional traits in childhood are at increased risk of developing anorexia nervosa. Environmental. Historical and cross-cultural variability in the prevalence of anorexia nervosa supports its association with cultures and settings in which thinness is valued. Oc cupations and avocations that encourage thinness, such as modeling and elite athletics, are also associated with incr`,
    d: `Other possible causes of either significantly low body weight or significant weight loss should be considered in the differential diagnosis of anorexia nervosa, especially when the presenting features are atypical (e.g., onset after age 40 years). Medical conditions (e.g., gastrointestinal disease, hyperthyroidism, occult malignan cies, and acquired immunodeficiency syndrome [AIDS]). Serious weight loss may oc cur in medical conditions, but indiv`,
  },
  "BN": {
    c: `A. Recurrent episodes of binge eating. An episode of binge eating is characterized by both of the following: 1. Eating, in a discrete period of time (e.g., within any 2-hour period), an amount of food that is definitely larger than what most individuals would eat in a similar period of time under similar circumstances. 2. A sense of lack of control over eating during the episode (e.g., a feeling that one cannot stop eating or control what or how much one is eating). B. Recurrent inappropriate compensatory behaviors in order to prevent weight gain, such as self-induced vomiting; misuse of laxatives, diuretics, or other medications; fasting; or excessive exercise. C. The binge eating and inappropriate compensatory behaviors both occur, on average, at least once a week for 3 months. D. Self-evaluation is unduly influenced by body shape and weight. E. The disturbance does not occur exclusive`,
    p: `Twelve-month prevalence of bulimia nervosa among young females is 1% 1.5%. Point prevalence is highest among young adults since the disorder peaks in older adolescence and young adulthood. Less is known about the point prevalence of bulimia nervosa in males, but bulimia nervosa is far less common in males than it is in females, with an ap proximate`,
    r: `Temperamental. Weight concerns, low self-esteem, depressive symptoms, social anxi ety disorder, and overanxious disorder of childhood are associated with increased risk for the development of bulimia nervosa. Environmental. Internalization of a thin body ideal has been found to increase risk for developing weight concerns, which in turn increase risk for the development of bulimia nervosa. Individuals who experienced childhood sexual or physical `,
    d: `Anorexia nervosa, binge-eating/purging type. Individuals whose binge-eating behav ior occurs only during episodes of anorexia nervosa are given the diagnosis anorexia ner vosa, binge-eating/purging type, and should not be given the additional diagnosis of bulimia nervosa. For individuals with an initial diagnosis of anorexia nervosa who binge and purge but whose presentation no longer meets the full criteria for anorexia nervosa, binge-eating/pur`,
  },
  "BED": {
    c: `A. Recurrent episodes of binge eating. An episode of binge eating is characterized both of the following: 1. Eating, in a discrete period of time (e.g., within any 2-hour period), an amount of food that is definitely larger than what most people would eat in a similar period of time under similar circumstances. 2. A sense of lack of control over eating during the episode (e.g., a feeling that one cannot stop eating or control what or how much one is eating). B. The binge-eating episodes are associated with three (or more) of the following: 1. Eating much more rapidly than normal. 2. Eating until feeling uncomfortably full. 3. Eating large amounts of food when not feeling physically hungry. 4. Eating alone because of feeling embarrassed by how much one is eating. 5. Feeling disgusted with oneself, depressed, or very guilty afterward. C. Marked distress regarding binge eating is present. D`,
    p: `Twelve-month prevalence of binge-eating disorder among U.S. adult (age 18 or older) fe males and males is 1.6% and 0.8%, respectively. The gender ratio is far less skewed in binge eating disorder than in bulimia nervosa. Binge-eating disorder is as prevalent among fe males from racial or ethnic minority groups as has been reported for white females`,
    r: `Genetic and physiological. Binge-eating disorder appears to run in families, which may reflect additive genetic influences.`,
    d: `Bulimia nervosa. Binge-eating disorder has recurrent binge eating in common with bu limia nervosa but differs from the latter disorder in some fundamental respects. In terms of clinical presentation, the recurrent inappropriate compensatory behavior (e.g., purging, driven exercise) seen in bulimia nervosa is absent in binge-eating disorder. Unlike in dividuals with bulimia nervosa, individuals with binge-eating disorder typically do not show mark`,
  },
  "ARFID": {
    c: `A. An eating or feeding disturbance (e.g., apparent lack of interest in eating or food; avoid ance based on the sensory characteristics of food; concern about aversive conse quences of eating) as manifested by persistent failure to meet appropriate nutritional and/or energy needs associated with one (or more) of the following: 1. Significant weight loss (or failure to achieve expected weight gain or faltering growth in children). 2. Significant nutritional deficiency. 3. Dependence on enteral feeding or oral nutritional supplements. 4. Marked interference with psychosocial functioning. B. The disturbance is not better explained by lack of available food or by an associated culturally sanctioned practice. C. The eating disturbance does not occur exclusively during the course of anorexia ner vosa or bulimia nervosa, and there is no evidence of a disturbance in the way in which s body weigh`,
    r: `Temperamental. Anxiety disorders, autism spectrum disorder, obsessive-compulsive disorder, and attention-deficit/hyperactivity disorder may increase risk for avoidant or restrictive feeding or eating behavior characteristic of the disorder. Environmental. Environmental risk factors for avoidant/restrictive food intake disor der include familial anxiety. Higher rates of feeding disturbances may occur in children of mothers with eating disorders. G`,
    d: `Appetite loss preceding restricted intake is a nonspecific symptom that can accompany a number of mental diagnoses. Avoidant/restrictive food intake disorder can be diagnosed concurrently with the disorders below if all criteria are met, and the eating disturbance re quires specific clinical attention. Other medical conditions (e.g., gastrointestinal disease, food allergies and intoler ances, occult malignancies). Restriction of food intake may o`,
  },
  "INS": {
    c: `A. A predominant complaint of dissatisfaction with sleep quantity or quality, associated with one (or more) of the following symptoms: 1. Difficulty initiating sleep. (In children, this may manifest as difficulty initiating sleep without caregiver intervention.) 2. Difficulty maintaining sleep, characterized by frequent awakenings or problems re turning to sleep after awakenings. (In children, this may manifest as difficulty return ing to sleep without caregiver intervention.) 3. Early-morning awakening with inability to return to sleep. B. The sleep disturbance causes clinically significant distress or impairment in social, oc cupational, educational, academic, behavioral, or other important areas of functioning. C. The sleep difficulty occurs at least 3 nights per week. D. The sleep difficulty is present for at least 3 months. E. The sleep difficulty occurs despite adequate opportunity`,
    p: `Population-based estimates indicate that about one-third of adults report insomnia symp toms, 10% 15% experience associated daytime impairments, and 6% 10% have symptoms Insomnia Disorder 365 that meet criteria for insomnia disorder. Insomnia disorder is the most prevalent of all sleep disorders. In primary care settings, approximately 10% 20% of i`,
    r: `While the risk and prognostic factors discussed in this section increase vulnerability to in somnia, sleep disturbances are more likely to occur when predisposed individuals are ex posed to precipitating events, such as major life events (e.g., illness, separation) or less severe but more chronic daily stress. Most individuals resume normal sleep patterns after the initial triggering event has disappeared, but others perhaps those more vulnerable`,
    d: `Normal sleep variations. Normal sleep duration varies considerably across individuals. Some individuals who require little sleep ( short sleepers ) may be concerned about their sleep duration. Short sleepers differ from individuals with insomnia disorder by the lack of difficulty falling or staying asleep and by the absence of characteristic daytime symptoms (e.g., fatigue, concentration problems, irritability). However, some short sleepers may d`,
  },
  "HYP": {
    c: `A. Self-reported excessive sleepiness (hypersomnolence) despite a main sleep period lasting at least 7 hours, with at least one of the following symptoms: 1. Recurrent periods of sleep or lapses into sleep within the same day. 2. A prolonged main sleep episode of more than 9 hours per day that is nonrestorative (i.e., unrefreshing). 3. Difficulty being fully awake after abrupt awakening. B. The hypersomnolence occurs at least three times per week, for at least 3 months. C. The hypersomnolence is accompanied by significant distress or impairment in cogni tive, social, occupational, or other important areas of functioning. D. The hypersomnolence is not better explained by and does not occur exclusively during the course of another sleep disorder (e.g., narcolepsy, breathing-related sleep disor der, circadian rhythm sleep-wake disorder, or a parasomnia). E. The hypersomnolence is not attrib`,
    p: `Approximately 5% 10% of individuals who consult in sleep disorders clinics with com plaints of daytime sleepiness are diagnosed as having hypersomnolence disorder. It is es timated that about 1% of the European and U.S. general population has episodes of sleep inertia. Hypersomnolence occurs with relatively equal frequency in males and females.`,
    r: `Environmental. Hypersomnolence can be increased temporarily by psychological stress and alcohol use, but they have not been documented as environmental precipitating factors. Viral infections have been reported to have preceded or accompanied hyper somnolence in about 10% of cases. Viral infections, such as HIV pneumonia, infectious mononucleosis, and Guillain-Barr syndrome, can also evolve into hypersomnolence within Hypersomnolence Disorder 371`,
    d: `Normative variation in sleep. Normal sleep duration varies considerably in the general population. Long sleepers (i.e., individuals who require a greater than average amount of sleep) do not have excessive sleepiness, sleep inertia, or automatic behavior when they obtain their required amount of nocturnal sleep. Sleep is reported to be refreshing. If social or occupational demands lead to shorter nocturnal sleep, daytime symptoms may appear. In h`,
  },
  "NAR": {
    c: `A. Recurrent periods of an irrepressible need to sleep, lapsing into sleep, or napping oc curring within the same day. These must have been occurring at least three times per week over the past 3 months. B. The presence of at least one of the following: 1. Episodes of cataplexy, defined as either (a) or (b), occurring at least a few times per month: a. In individuals with long-standing disease, brief (seconds to minutes) episodes of sudden bilateral loss of muscle tone with maintained consciousness that are precipitated by laughter or joking. Narcolepsy 373 b. In children or in individuals within 6 months of onset, spontaneous grimaces or jaw-opening episodes with tongue thrusting or a global hypotonia, without any obvious emotional triggers. 2. Hypocretin deficiency, as measured using cerebrospinal fluid (CSF) hypocretin-1 immunoreactivity values (less than or equal to one-third of valu`,
    p: `Narcolepsy-cataplexy affects 0.02% 0.04% of the general population in most countries. Narcolepsy affects both genders, with possibly a slight male preponderance.`,
    r: `Temperamental. Parasomnias, such as sleepwalking, bruxism, REM sleep behavior dis order, and enuresis, may be more common in individuals who develop narcolepsy. Indi viduals commonly report that they need more sleep than other family members. Environmental. Group A streptococcal throat infection, influenza (notably pandemic H1N1 2009), or other winter infections are likely triggers of the autoimmune process, pro- 376 Sleep-Wake Disorders ducing n`,
    d: `Other hypersomnias. Hypersomnolence and narcolepsy are similar with respect to the degree of daytime sleepiness, age at onset, and stable course over time but can be distin- Narcolepsy 377 guished based on distinctive clinical and laboratory features. Individuals with hypersom nolence typically have longer and less disrupted nocturnal sleep, greater difficulty awakening, more persistent daytime sleepiness (as opposed to more discrete sleep at tac`,
  },
  "ODD": {
    c: `A. A pattern of angry/irritable mood, argumentative/defiant behavior, or vindictiveness lasting at least 6 months as evidenced by at least four symptoms from any of the following cate gories, and exhibited during interaction with at least one individual who is not a sibling. Angry/Irritable Mood 1. Often loses temper. 2. Is often touchy or easily annoyed. 3. Is often angry and resentful. Argumentative/Defiant Behavior 4. Often argues with authority figures or, for children and adolescents, with adults. 5. Often actively defies or refuses to comply with requests from authority figures or with rules. 6. Often deliberately annoys others. 7. Often blames others for his or her mistakes or misbehavior. Vindictiveness 8. Has been spiteful or vindictive at least twice within the past 6 months. Note: The persistence and frequency of these behaviors should be used to distinguish a behavior that is`,
    p: `The prevalence of oppositional defiant disorder ranges from 1% to 11%, with an average prevalence estimate of around 3.3%. The rate of oppositional defiant disorder may vary depending on the age and gender of the child. The disorder appears to be somewhat more prevalent in males than in females (1.4:1) prior to adolescence. This male predominance i`,
    r: `Environmental. Individuals with a history of physical and emotional trauma during the first two decades of life are at increased risk for intermittent explosive disorder. 468 Disruptive, Impulse-Control, and Conduct Disorders Genetic and physiological. First-degree relatives of individuals with intermittent ex plosive disorder are at increased risk for intermittent explosive disorder, and twin studies have demonstrated a substantial genetic influ`,
    d: `Conduct disorder. Conduct disorder and oppositional defiant disorder are both related to conduct problems that bring the individual in conflict with adults and other authority figures (e.g., teachers, work supervisors). The behaviors of oppositional defiant disorder are typically of a less severe nature than those of conduct disorder and do not include ag gression toward people or animals, destruction of property, or a pattern of theft or deceit.`,
  },
  "IED": {
    c: `A. Recurrent behavioral outbursts representing a failure to control aggressive impulses as manifested by either of the following: 1. Verbal aggression (e.g., temper tantrums, tirades, verbal arguments or fights) or physical aggression toward property, animals, or other individuals, occurring twice weekly, on average, for a period of 3 months. The physical aggression does not re sult in damage or destruction of property and does not result in physical injury to animals or other individuals. 2. Three behavioral outbursts involving damage or destruction of property and/or physical assault involving physical injury against animals or other individuals occur ring within a 12-month period. B. The magnitude of aggressiveness expressed during the recurrent outbursts is grossly out of proportion to the provocation or to any precipitating psychosocial stressors. C. The recurrent aggressive outburs`,
    p: `One-year prevalence data for intermittent explosive disorder in the United States is about 2.7% (narrow definition). Intermittent explosive disorder is more prevalent among younger individuals (e.g., younger than 35 40 years), compared with older individuals (older than 50 years), and in individuals with a high school education or less.`,
    r: `Environmental. Individuals with a history of physical and emotional trauma during the first two decades of life are at increased risk for intermittent explosive disorder. 468 Disruptive, Impulse-Control, and Conduct Disorders Genetic and physiological. First-degree relatives of individuals with intermittent ex plosive disorder are at increased risk for intermittent explosive disorder, and twin studies have demonstrated a substantial genetic influ`,
    d: `A diagnosis of intermittent explosive disorder should not be made when Criteria A1 and/ or A2 are only met during an episode of another mental disorder (e.g., major depressive disorder, bipolar disorder, psychotic disorder), or when impulsive aggressive outbursts are attributable to another medical condition or to the physiological effects of a substance or medication. This diagnosis also should not be made, particularly in children and ado lesce`,
  },
  "CD": {
    c: `A. A repetitive and persistent pattern of behavior in which the basic rights of others or ma jor age-appropriate societal norms or rules are violated, as manifested by the presence of at least three of the following 15 criteria in the past 12 months from any of the cate gories below, with at least one criterion present in the past 6 months: Aggression to People and Animals 1. Often bullies, threatens, or intimidates others. 2. Often initiates physical fights. 3. Has used a weapon that can cause serious physical harm to others (e.g., a bat, brick, broken bottle, knife, gun). 470 Disruptive, Impulse-Control, and Conduct Disorders 4. Has been physically cruel to people. 5. Has been physically cruel to animals. 6. Has stolen while confronting a victim (e.g., mugging, purse snatching, extortion, armed robbery). 7. Has forced someone into sexual activity. Destruction of Property 8. Has deliber`,
    p: `One-year population prevalence estimates range from 2% to more than 10%, with a median of 4%. The prevalence of conduct disorder appears to be fairly consistent across various countries that differ in race and ethnicity. Prevalence rates rise from childhood to adoles cence and are higher among males than among females. Few children with impairing c`,
    r: `Temperamental. Temperamental risk factors include a difficult undercontrolled infant temperament and lower-than-average intelligence, particularly with regard to verbal IQ. Environmental. Family-level risk factors include parental rejection and neglect, inconsis tent child-rearing practices, harsh discipline, physical or sexual abuse, lack of supervision, early institutional living, frequent changes of caregivers, large family size, parental crim`,
    d: `Oppositional defiant disorder. Conduct disorder and oppositional defiant disorder are both related to symptoms that bring the individual in conflict with adults and other au- Conduct Disorder 475 thority figures (e.g., parents, teachers, work supervisors). The behaviors of oppositional defiant disorder are typically of a less severe nature than those of individuals with conduct disorder and do not include aggression toward individuals or animals,`,
  },
  "AUD": {
    c: `A. A problematic pattern of alcohol use leading to clinically significant impairment or dis tress, as manifested by at least two of the following, occurring within a 12-month period: 1. Alcohol is often taken in larger amounts or over a longer period than was intended. 2. There is a persistent desire or unsuccessful efforts to cut down or control alcohol use. Alcohol Use Disorder 491 3. A great deal of time is spent in activities necessary to obtain alcohol, use alcohol, or recover from its effects. 4. Craving, or a strong desire or urge to use alcohol. 5. Recurrent alcohol use resulting in a failure to fulfill major role obligations at work, school, or home. 6. Continued alcohol use despite having persistent or recurrent social or interpersonal problems caused or exacerbated by the effects of alcohol. 7. Important social, occupational, or recreational activities are given up or reduced `,
    p: `Alcohol use disorder is a common disorder. In the United States, the 12-month prevalence of alcohol use disorder is estimated to be 4.6% among 12- to 17-year-olds and 8.5% among adults age 18 years and older in the United States. Rates of the disorder are greater among adult men (12.4%) than among adult women (4.9%). Twelve-month prevalence of alco`,
    r: `Environmental. Environmental risk and prognostic factors may include cultural atti tudes toward drinking and intoxication, the availability of alcohol (including price), acquired personal experiences with alcohol, and stress levels. Additional potential medi ators of how alcohol problems develop in predisposed individuals include heavier peer substance use, exaggerated positive expectations of the effects of alcohol, and suboptimal ways of coping`,
    d: `Nonpathological use of alcohol. The key element of alcohol use disorder is the use of heavy doses of alcohol with resulting repeated and significant distress or impaired func tioning. While most drinkers sometimes consume enough alcohol to feel intoxicated, only a minority (less than 20%) ever develop alcohol use disorder. Therefore, drinking, even daily, in low doses and occasional intoxication do not by themselves make this diagnosis. Sedative,`,
  },
  "OUD": {
    c: `A. A problematic pattern of opioid use leading to clinically significant impairment or distress, as manifested by at least two of the following, occurring within a 12-month period: 1. Opioids are often taken in larger amounts or over a longer period than was in tended. 2. There is a persistent desire or unsuccessful efforts to cut down or control opioid use. 3. A great deal of time is spent in activities necessary to obtain the opioid, use the opi oid, or recover from its effects. 4. Craving, or a strong desire or urge to use opioids. 5. Recurrent opioid use resulting in a failure to fulfill major role obligations at work, school, or home. 6. Continued opioid use despite having persistent or recurrent social or interpersonal problems caused or exacerbated by the effects of opioids. 7. Important social, occupational, or recreational activities are given up or reduced be cause of opioid us`,
    p: `The 12-month prevalence of opioid use disorder is approximately 0.37% among adults age 18 years and older in the community population. This may be an underestimate because of the large number of incarcerated individuals with opioid use disorders. Rates are higher in males than in females (0.49% vs. 0.26%), with the male-to-female ratio typically be`,
    r: `Genetic and physiological. The risk for opiate use disorder can be related to individual, family, peer, and social environmental factors, but within these domains, genetic factors play a particularly important role both directly and indirectly. For instance, impulsivity and novelty seeking are individual temperaments that relate to the propensity to develop 544 Substance-Related and Addictive Disorders a substance use disorder but may themselves `,
    d: `Opioid-induced mental disorders. Opioid-induced disorders occur frequently in individ uals with opioid use disorder. Opioid-induced disorders may be characterized by symptoms (e.g., depressed mood) that resemble primary mental disorders (e.g., persistent depressive dis order [dysthymia] vs. opioid-induced depressive disorder, with depressive features, with on set during intoxication). Opioids are less likely to produce symptoms of mental disturba`,
  },
  "CUD": {
    c: `A. A problematic pattern of cannabis use leading to clinically significant impairment or dis tress, as manifested by at least two of the following, occurring within a 12-month period: 1. Cannabis is often taken in larger amounts or over a longer period than was intended. 2. There is a persistent desire or unsuccessful efforts to cut down or control cannabis use. 3. A great deal of time is spent in activities necessary to obtain cannabis, use canna bis, or recover from its effects. 4. Craving, or a strong desire or urge to use cannabis. 5. Recurrent cannabis use resulting in a failure to fulfill major role obligations at work, school, or home. 6. Continued cannabis use despite having persistent or recurrent social or interper sonal problems caused or exacerbated by the effects of cannabis. 7. Important social, occupational, or recreational activities are given up or reduced be cause of ca`,
    p: `Cannabinoids, especially cannabis, are the most widely used illicit psychoactive sub stances in the United States. The 12-month prevalence of cannabis use disorder (DSM-IV abuse and dependence rates combined) is approximately 3.4% among 12- to 17-year-olds and 1.5% among adults age 18 years and older. Rates of cannabis use disorder are greater amon`,
    r: `Temperamental. A history of conduct disorder in childhood or adolescence and antiso cial personality disorder are risk factors for the development of many substance-related disorders, including cannabis-related disorders. Other risk factors include externalizing 514 Substance-Related and Addictive Disorders or internalizing disorders during childhood or adolescence. Youths with high behavioral disinhibition scores show early-onset substance use d`,
    d: `Nonproblematic use of cannabis. The distinction between nonproblematic use of can nabis and cannabis use disorder can be difficult to make because social, behavioral, or psy chological problems may be difficult to attribute to the substance, especially in the context of use of other substances. Also, denial of heavy cannabis use and the attribution that can nabis is related to or causing substantial problems are common among individuals who are r`,
  },
  "TUD": {
    c: `A. A problematic pattern of tobacco use leading to clinically significant impairment or dis tress, as manifested by at least two of the following, occurring within a 12-month period: 1. Tobacco is often taken in larger amounts or over a longer period than was intended. 2. There is a persistent desire or unsuccessful efforts to cut down or control tobacco use. 3. A great deal of time is spent in activities necessary to obtain or use tobacco. 4. Craving, or a strong desire or urge to use tobacco. 5. Recurrent tobacco use resulting in a failure to fulfill major role obligations at work, school, or home (e.g., interference with work). 6. Continued tobacco use despite having persistent or recurrent social or interper sonal problems caused or exacerbated by the effects of tobacco (e.g., arguments with others about tobacco use). 7. Important social, occupational, or recreational activities are `,
    p: `Cigarettes are the most commonly used tobacco product, representing over 90% of to bacco/nicotine use. In the United States, 57% of adults have never been smokers, 22% are former smokers, and 21% are current smokers. Approximately 20% of current U.S. smok ers are nondaily smokers. The prevalence of smokeless tobacco use is less than 5%, and the pre`,
    r: `Temperamental. Individuals with externalizing personality traits are more likely to initiate tobacco use. Children with attention-deficit/hyperactivity disorder or conduct disorder, and adults with depressive, bipolar, anxiety, personality, psychotic, or other substance use disorders, are at higher risk of starting and continuing tobacco use and of to bacco use disorder. 574 Substance-Related and Addictive Disorders Environmental. Individuals wit`,
    d: `The symptoms of tobacco withdrawal overlap with those of other substance withdrawal syndromes (e.g., alcohol withdrawal; sedative, hypnotic, or anxiolytic withdrawal; stim ulant withdrawal; caffeine withdrawal; opioid withdrawal); caffeine intoxication; anxiety, depressive, bipolar, and sleep disorders; and medication-induced akathisia. Admission to smoke-free inpatient units or voluntary smoking cessation can induce withdrawal symp toms that mim`,
  },
  "GD": {
    c: `A. Persistent and recurrent problematic gambling behavior leading to clinically significant impairment or distress, as indicated by the individual exhibiting four (or more) of the fol lowing in a 12-month period: 1. Needs to gamble with increasing amounts of money in order to achieve the desired excitement. 2. Is restless or irritable when attempting to cut down or stop gambling. 3. Has made repeated unsuccessful efforts to control, cut back, or stop gambling. 4. Is often preoccupied with gambling (e.g., having persistent thoughts of reliving past gambling experiences, handicapping or planning the next venture, thinking of ways to get money with which to gamble). 5. Often gambles when feeling distressed (e.g., helpless, guilty, anxious, depressed). 6. After losing money gambling, often returns another day to get even ( chasing one losses). 7. Lies to conceal the extent of involvement wit`,
    p: `The past-year prevalence rate of gambling disorder is about 0.2% 0.3% in the general pop ulation. In the general population, the lifetime prevalence rate is about 0.4% 1.0%. For fe males, the lifetime prevalence rate of gambling disorder is about 0.2%, and for males it is about 0.6%. The lifetime prevalence of pathological gambling among African Am`,
    r: `Temperamental. Gambling that begins in childhood or early adolescence is associated with increased rates of gambling disorder. Gambling disorder also appears to aggregate with antisocial personality disorder, depressive and bipolar disorders, and other sub stance use disorders, particularly with alcohol disorders. Genetic and physiological. Gambling disorder can aggregate in families, and this effect appears to relate to both environmental and ge`,
    d: `Nondisordered gambling. Gambling disorder must be distinguished from professional and social gambling. In professional gambling, risks are limited and discipline is central. Social gambling typically occurs with friends or colleagues and lasts for a limited period of time, with acceptable losses. Some individuals can experience problems associated with gambling (e.g., short-term chasing behavior and loss of control) that do not meet the full crit`,
  },
  "DEL": {
    c: `A. A disturbance in attention (i.e., reduced ability to direct, focus, sustain, and shift atten tion) and awareness (reduced orientation to the environment). B. The disturbance develops over a short period of time (usually hours to a few days), rep resents a change from baseline attention and awareness, and tends to fluctuate in se verity during the course of a day. C. An additional disturbance in cognition (e.g., memory deficit, disorientation, language, visuospatial ability, or perception). D. The disturbances in Criteria A and C are not better explained by another preexisting, established, or evolving neurocognitive disorder and do not occur in the context of a severely reduced level of arousal, such as coma. E. There is evidence from the history, physical examination, or laboratory findings that the disturbance is a direct physiological consequence of another medical condition, sub s`,
    p: `The prevalence of delirium is highest among hospitalized older individuals and varies depending on the individuals characteristics, setting of care, and sensitivity of the detec tion method. The prevalence of delirium in the community overall is low (1% 2%) but in creases with age, rising to 14% among individuals older than 85 years. The prevalence`,
    r: `Environmental. Delirium may be increased in the context of functional impairment, im mobility, a history of falls, low levels of activity, and use of drugs and medications with psychoactive properties (particularly alcohol and anticholinergics). Genetic and physiological. Both major and mild NCDs can increase the risk for delir ium and complicate the course. Older individuals are especially susceptible to delirium compared with younger adults. Su`,
    d: `Psychotic disorders and bipolar and depressive disorders with psychotic features. Delirium that is characterized by vivid hallucinations, delusions, language disturbances, and agitation must be distinguished from brief psychotic disorder, schizophrenia, schizo phreniform disorder, and other psychotic disorders, as well as from bipolar and depres sive disorders with psychotic features. Acute stress disorder. Delirium associated with fear, anxiety,`,
  },
  "BPD-P": {
    c: `A pervasive pattern of instability of interpersonal relationships, self-image, and affects, and marked impulsivity, beginning by early adulthood and present in a variety of contexts, as indicated by five (or more) of the following: 1. Frantic efforts to avoid real or imagined abandonment. (Note: Do not include suicidal or self-mutilating behavior covered in Criterion 5.) 2. A pattern of unstable and intense interpersonal relationships characterized by alternat ing between extremes of idealization and devaluation. 3. Identity disturbance: markedly and persistently unstable self-image or sense of self. 4. Impulsivity in at least two areas that are potentially self-damaging (e.g., spending, sex, substance abuse, reckless driving, binge eating). (Note: Do not include suicidal or self mutilating behavior covered in Criterion 5.) 5. Recurrent suicidal behavior, gestures, or threats, or self-mu`,
    p: `The median population prevalence of borderline personality disorder is estimated to be 1.6% but may be as high as 5.9%. The prevalence of borderline personality disorder is about 6% in primary care settings, about 10% among individuals seen in outpatient mental health clinics, and about 20% among psychiatric inpatients. The prevalence of borderline`,
    r: `Genetic and physiological. Borderline personality disorder is about five times more common among first-degree biological relatives of those with the disorder than in the gen eral population. There is also an increased familial risk for substance use disorders, anti social personality disorder, and depressive or bipolar disorders.`,
    d: `Depressive and bipolar disorders. Borderline personality disorder often co-occurs with depressive or bipolar disorders, and when criteria for both are met, both may be diagnosed. Because the cross-sectional presentation of borderline personality disorder can be mimicked by an episode of depressive or bipolar disorder, the clinician should avoid giving an addi tional diagnosis of borderline personality disorder based only on cross-sectional presen`,
  },
  "NPD": {
    c: `A pervasive pattern of grandiosity (in fantasy or behavior), need for admiration, and lack of empathy, beginning by early adulthood and present in a variety of contexts, as indicated by five (or more) of the following: 1. Has a grandiose sense of self-importance (e.g., exaggerates achievements and talents, expects to be recognized as superior without commensurate achievements). 2. Is preoccupied with fantasies of unlimited success, power, brilliance, beauty, or ideal love. 3. Believes that he or she is special and unique and can only be understood by, or should associate with, other special or high-status people (or institutions). 4. Requires excessive admiration. 5. Has a sense of entitlement (i.e., unreasonable expectations of especially favorable treatment or automatic compliance with his or her expectations). 670 Personality Disorders 6. Is interpersonally exploitative (i.e., takes a`,
    p: `Prevalence estimates for narcissistic personality disorder, based on DSM-IV definitions, range from 0% to 6.2% in community samples.`,
    d: `Other personality disorders and personality traits. Other personality disorders may be confused with narcissistic personality disorder because they have certain features in 672 Personality Disorders common. It is, therefore, important to distinguish among these disorders based on differ ences in their characteristic features. However, if an individual has personality features that meet criteria for one or more personality disorders in addition to`,
  },
  "ASPD": {
    c: `A. A pervasive pattern of disregard for and violation of the rights of others, occurring since age 15 years, as indicated by three (or more) of the following: 1. Failure to conform to social norms with respect to lawful behaviors, as indicated by repeatedly performing acts that are grounds for arrest. 2. Deceitfulness, as indicated by repeated lying, use of aliases, or conning others for personal profit or pleasure. 3. Impulsivity or failure to plan ahead. 4. Irritability and aggressiveness, as indicated by repeated physical fights or assaults. 5. Reckless disregard for safety of self or others. 6. Consistent irresponsibility, as indicated by repeated failure to sustain consistent work behavior or honor financial obligations. 7. Lack of remorse, as indicated by being indifferent to or rationalizing having hurt, mistreated, or stolen from another. B. The individual is at least age 18 year`,
    p: `Twelve-month prevalence rates of antisocial personality disorder, using criteria from pre vious DSMs, are between 0.2% and 3.3%. The highest prevalence of antisocial personality disorder (greater than 70%) is among most severe samples of males with alcohol use dis order and from substance abuse clinics, prisons, or other forensic settings. Prevalen`,
    r: `Genetic and physiological. Antisocial personality disorder is more common among the first-degree biological relatives of those with the disorder than in the general population. The risk to biological relatives of females with the disorder tends to be higher than the risk to biological relatives of males with the disorder. Biological relatives of individuals with this disorder are also at increased risk for somatic symptom disorder and substance u`,
    d: `The diagnosis of antisocial personality disorder is not given to individuals younger than 18 years and is given only if there is a history of some symptoms of conduct disorder be fore age 15 years. For individuals older than 18 years, a diagnosis of conduct disorder is given only if the criteria for antisocial personality disorder are not met. Substance use disorders. When antisocial behavior in an adult is associated with a substance use disorde`,
  },
  "PPD": {
    c: `A. A pervasive distrust and suspiciousness of others such that their motives are inter preted as malevolent, beginning by early adulthood and present in a variety of con texts, as indicated by four (or more) of the following: 1. Suspects, without sufficient basis, that others are exploiting, harming, or deceiving him or her. 2. Is preoccupied with unjustified doubts about the loyalty or trustworthiness of friends or associates. 3. Is reluctant to confide in others because of unwarranted fear that the information will be used maliciously against him or her. 4. Reads hidden demeaning or threatening meanings into benign remarks or events. 5. Persistently bears grudges (i.e., is unforgiving of insults, injuries, or slights). 6. Perceives attacks on his or her character or reputation that are not apparent to oth ers and is quick to react angrily or to counterattack. 7. Has recurrent suspicion`,
    p: `A prevalence estimate for paranoid personality based on a probability subsample from Part II of the National Comorbidity Survey Replication suggests a prevalence of 2.3%, while the National Epidemiologic Survey on Alcohol and Related Conditions data suggest a prevalence of paranoid personality disorder of 4.4%.`,
    r: `Genetic and physiological. There is some evidence for an increased prevalence of par anoid personality disorder in relatives of probands with schizophrenia and for a more spe cific familial relationship with delusional disorder, persecutory type.`,
    d: `Other mental disorders with psychotic symptoms. Paranoid personality disorder can be distinguished from delusional disorder, persecutory type; schizophrenia; and a bipolar or depressive disorder with psychotic features because these disorders are all characterized by a period of persistent psychotic symptoms (e.g., delusions and hallucinations). For an additional diagnosis of paranoid personality disorder to be given, the personality disorder mus`,
  },
  "SZPD": {
    c: `A. A pervasive pattern of detachment from social relationships and a restricted range of expression of emotions in interpersonal settings, beginning by early adulthood and present in a variety of contexts, as indicated by four (or more) of the following: Schizoid Personality Disorder 653 1. Neither desires nor enjoys close relationships, including being part of a family. 2. Almost always chooses solitary activities. 3. Has little, if any, interest in having sexual experiences with another person. 4. Takes pleasure in few, if any, activities. 5. Lacks close friends or confidants other than first-degree relatives. 6. Appears indifferent to the praise or criticism of others. 7. Shows emotional coldness, detachment, or flattened affectivity. B. Does not occur exclusively during the course of schizophrenia, a bipolar disorder or depressive disorder with psychotic features, another psychotic d`,
    p: `Schizoid personality disorder is uncommon in clinical settings. A prevalence estimate for schizoid personality based on a probability subsample from Part II of the National Co morbidity Survey Replication suggests a prevalence of 4.9%. Data from the 2001 2002 National Epidemiologic Survey on Alcohol and Related Conditions suggest a prevalence of 3.`,
    r: `Genetic and physiological. Schizoid personality disorder may have increased preva lence in the relatives of individuals with schizophrenia or schizotypal personality disorder.`,
    d: `Other mental disorders with psychotic symptoms. Schizoid personality disorder can be distinguished from delusional disorder, schizophrenia, and a bipolar or depressive dis order with psychotic features because these disorders are all characterized by a period of persistent psychotic symptoms (e.g., delusions and hallucinations). To give an additional diagnosis of schizoid personality disorder, the personality disorder must have been present befor`,
  },
  "SZTP": {
    c: `A. A pervasive pattern of social and interpersonal deficits marked by acute discomfort with, and reduced capacity for, close relationships as well as by cognitive or perceptual distortions and eccentricities of behavior, beginning by early adulthood and present in a variety of contexts, as indicated by five (or more) of the following: 1. Ideas of reference (excluding delusions of reference). 2. Odd beliefs or magical thinking that influences behavior and is inconsistent with subcultural norms (e.g., superstitiousness, belief in clairvoyance, telepathy, or sixth sense ; in children and adolescents, bizarre fantasies or preoccupations). 3. Unusual perceptual experiences, including bodily illusions. 4. Odd thinking and speech (e.g., vague, circumstantial, metaphorical, overelaborate, or stereotyped). 5. Suspiciousness or paranoid ideation. 656 Personality Disorders 6. Inappropriate or const`,
    p: `In community studies of schizotypal personality disorder, reported rates range from 0.6% in Norwegian samples to 4.6% in a U.S. community sample. The prevalence of schizotypal personality disorder in clinical populations seems to be infrequent (0% 1.9%), with a higher estimated prevalence in the general population (3.9%) found in the National Epi d`,
    r: `Genetic and physiological. Schizotypal personality disorder appears to aggregate fa milially and is more prevalent among the first-degree biological relatives of individuals with schizophrenia than among the general population. There may also be a modest in crease in schizophrenia and other psychotic disorders in the relatives of probands with schizotypal personality disorder. Cultural-Related Diagnostic Issues Cognitive and perceptual distortion`,
    d: `Other mental disorders with psychotic symptoms. Schizotypal personality disorder can be distinguished from delusional disorder, schizophrenia, and a bipolar or depressive disorder with psychotic features because these disorders are all characterized by a period of persistent psychotic symptoms (e.g., delusions and hallucinations). To give an addi tional diagnosis of schizotypal personality disorder, the personality disorder must have been present`,
  },
  "HPD": {
    c: `A pervasive pattern of excessive emotionality and attention seeking, beginning by early adult hood and present in a variety of contexts, as indicated by five (or more) of the following: 1. Is uncomfortable in situations in which he or she is not the center of attention. 2. Interaction with others is often characterized by inappropriate sexually seductive or provocative behavior. 3. Displays rapidly shifting and shallow expression of emotions. 4. Consistently uses physical appearance to draw attention to self. 5. Has a style of speech that is excessively impressionistic and lacking in detail. 6. Shows self-dramatization, theatricality, and exaggerated expression of emotion. 7. Is suggestible (i.e., easily influenced by others or circumstances). 8. Considers relationships to be more intimate than they actually are.`,
    p: `Data from the 2001 2002 National Epidemiologic Survey on Alcohol and Related Condi tions suggest a prevalence of histrionic personality of 1.84%.`,
    d: `Other personality disorders and personality traits. Other personality disorders may be confused with histrionic personality disorder because they have certain features in common. It is therefore important to distinguish among these disorders based on differ ences in their characteristic features. However, if an individual has personality features that meet criteria for one or more personality disorders in addition to histrionic personal ity disor`,
  },
  "AVPD": {
    c: `A pervasive pattern of social inhibition, feelings of inadequacy, and hypersensitivity to neg ative evaluation, beginning by early adulthood and present in a variety of contexts, as in dicated by four (or more) of the following: 1. Avoids occupational activities that involve significant interpersonal contact because of fears of criticism, disapproval, or rejection. Avoidant Personality Disorder 673 2. Is unwilling to get involved with people unless certain of being liked. 3. Shows restraint within intimate relationships because of the fear of being shamed or ridiculed. 4. Is preoccupied with being criticized or rejected in social situations. 5. Is inhibited in new interpersonal situations because of feelings of inadequacy. 6. Views self as socially inept, personally unappealing, or inferior to others. 7. Is unusually reluctant to take personal risks or to engage in any new activities bec`,
    p: `Data from the 2001 2002 National Epidemiologic Survey on Alcohol and Related Condi tions suggest a prevalence of about 2.4% for avoidant personality disorder.`,
    d: `Anxiety disorders. There appears to be a great deal of overlap between avoidant person ality disorder and social anxiety disorder (social phobia), so much so that they may be alternative conceptualizations of the same or similar conditions. Avoidance also character izes both avoidant personality disorder and agoraphobia, and they often co-occur. Other personality disorders and personality traits. Other personality disorders may be confused with a`,
  },
  "DPD": {
    p: `Data from the 2001 2002 National Epidemiologic Survey on Alcohol and Related Condi tions yielded an estimated prevalence of dependent personality disorder of 0.49%, and de pendent personality was estimated, based on a probability subsample from Part II of the National Comorbidity Survey Replication, to be 0.6%.`,
    d: `Other mental disorders and medical conditions. Dependent personality disorder must be distinguished from dependency arising as a consequence of other mental disorders (e.g., depressive disorders, panic disorder, agoraphobia) and as a result of other medical conditions. 678 Personality Disorders Other personality disorders and personality traits. Other personality disorders may be confused with dependent personality disorder because they have cert`,
  },
  "OCPD": {
    c: `A pervasive pattern of preoccupation with orderliness, perfectionism, and mental and in terpersonal control, at the expense of flexibility, openness, and efficiency, beginning by early adulthood and present in a variety of contexts, as indicated by four (or more) of the following: 1. Is preoccupied with details, rules, lists, order, organization, or schedules to the extent that the major point of the activity is lost. 2. Shows perfectionism that interferes with task completion (e.g., is unable to complete a project because his or her own overly strict standards are not met). 3. Is excessively devoted to work and productivity to the exclusion of leisure activities and friendships (not accounted for by obvious economic necessity). 4. Is overconscientious, scrupulous, and inflexible about matters of morality, ethics, or values (not accounted for by cultural or religious identification). Obs`,
    p: `Obsessive-compulsive personality disorder is one of the most prevalent personality dis orders in the general population, with estimated prevalence ranging from 2.1% to 7.9%.`,
    d: `Obsessive-compulsive disorder. Despite the similarity in names, OCD is usually easily distinguished from obsessive-compulsive personality disorder by the presence of true ob sessions and compulsions in OCD. When criteria for both obsessive-compulsive person ality disorder and OCD are met, both diagnoses should be recorded. Hoarding disorder. A diagnosis of hoarding disorder should be considered especially when hoarding is extreme (e.g., accumulat`,
  },
  "VOY": {
    c: `A. Over a period of at least 6 months, recurrent and intense sexual arousal from observ ing an unsuspecting person who is naked, in the process of disrobing, or engaging in sexual activity, as manifested by fantasies, urges, or behaviors. B. The individual has acted on these sexual urges with a nonconsenting person, or the sexual urges or fantasies cause clinically significant distress or impairment in social, occupational, or other important areas of functioning. C. The individual experiencing the arousal and/or acting on the urges is at least 18 years of age.`,
    p: `Voyeuristic acts are the most common of potentially law-breaking sexual behaviors. The population prevalence of voyeuristic disorder is unknown. However, based on voyeuris- 688 Paraphilic Disorders tic sexual acts in nonclinical samples, the highest possible lifetime prevalence for voyeuris tic disorder is approximately 12% in males and 4% in femal`,
    r: `Temperamental. Voyeurism is a necessary precondition for voyeuristic disorder; hence, risk factors for voyeurism should also increase the rate of voyeuristic disorder. Environmental. Childhood sexual abuse, substance misuse, and sexual preoccupation/ hypersexuality have been suggested as risk factors, although the causal relationship to voyeurism is uncertain and the specificity unclear.`,
    d: `Conduct disorder and antisocial personality disorder. Conduct disorder in adolescents and antisocial personality disorder would be characterized by additional norm-breaking and antisocial behaviors, and the specific sexual interest in secretly watching unsuspect ing others who are naked or engaging in sexual activity should be lacking. Substance use disorders. Substance use disorders might involve single voyeuristic ep isodes by intoxicated indiv`,
  },
  "EXH": {
    c: `A. Over a period of at least 6 months, recurrent and intense sexual arousal from the ex posure of one s genitals to an unsuspecting person, as manifested by fantasies, urges, or behaviors. B. The individual has acted on these sexual urges with a nonconsenting person, or the sexual urges or fantasies cause clinically significant distress or impairment in social, occupational, or other important areas of functioning. Specify whether: Sexually aroused by exposing genitals to prepubertal children Sexually aroused by exposing genitals to physically mature individuals Sexually aroused by exposing genitals to prepubertal children and to physically mature individuals`,
    p: `The prevalence of exhibitionistic disorder is unknown. However, based on exhibitionistic sexual acts in nonclinical or general populations, the highest possible prevalence for exhi bitionistic disorder in the male population is 2% 4%. The prevalence of exhibitionistic dis order in females is even more uncertain but is generally believed to be much `,
    r: `Temperamental. Since exhibitionism is a necessary precondition for exhibitionistic dis order, risk factors for exhibitionism should also increase the rate of exhibitionistic disor der. Antisocial history, antisocial personality disorder, alcohol misuse, and pedophilic sexual preference might increase risk of sexual recidivism in exhibitionistic offenders. Frotteuristic Disorder 691 Hence, antisocial personality disorder, alcohol use disorder, and`,
    d: `Potential differential diagnoses for exhibitionistic disorder sometimes occur also as co morbid disorders. Therefore, it is generally necessary to evaluate the evidence for exhibi tionistic disorder and other possible conditions as separate questions. Conduct disorder and antisocial personality disorder. Conduct disorder in adolescents and antisocial personality disorder would be characterized by additional norm-breaking and antisocial behaviors,`,
  },
  "PED": {
    c: `A. Over a period of at least 6 months, recurrent, intense sexually arousing fantasies, sex ual urges, or behaviors involving sexual activity with a prepubescent child or children (generally age 13 years or younger). B. The individual has acted on these sexual urges, or the sexual urges or fantasies cause marked distress or interpersonal difficulty. C. The individual is at least age 16 years and at least 5 years older than the child or chil dren in Criterion A. Note: Do not include an individual in late adolescence involved in an ongoing sexual relationship with a 12- or 13-year-old. Specify whether: Exclusive type (attracted only to children) Nonexclusive type 698 Paraphilic Disorders Specify if: Sexually attracted to males Sexually attracted to females Sexually attracted to both Specify if: Limited to incest`,
    p: `The population prevalence of pedophilic disorder is unknown. The highest possible prev alence for pedophilic disorder in the male population is approximately 3% 5%. The pop ulation prevalence of pedophilic disorder in females is even more uncertain, but it is likely a small fraction of the prevalence in males. Pedophilic Disorder 699`,
    r: `Temperamental. There appears to be an interaction between pedophilia and antisocial ity, such that males with both traits are more likely to act out sexually with children. Thus, antisocial personality disorder may be considered a risk factor for pedophilic disorder in males with pedophilia. Environmental. Adult males with pedophilia often report that they were sexually abused as children. It is unclear, however, whether this correlation reflects`,
    d: `Many of the conditions that could be differential diagnoses for pedophilic disorder also sometimes occur as comorbid diagnoses. It is therefore generally necessary to evaluate the evidence for pedophilic disorder and other possible conditions as separate questions. Antisocial personality disorder. This disorder increases the likelihood that a person who is primarily attracted to the mature physique will approach a child, on one or a few occa sion`,
  },
  "GDX": {
    c: `A. A marked incongruence between one s experienced/expressed gender and assigned gender, of at least 6 months duration, as manifested by at least six of the following (one of which must be Criterion A1): 1. A strong desire to be of the other gender or an insistence that one is the other gen der (or some alternative gender different from one s assigned gender). 2. In boys (assigned gender), a strong preference for cross-dressing or simulating fe male attire; or in girls (assigned gender), a strong preference for wearing only typ ical masculine clothing and a strong resistance to the wearing of typical feminine clothing. 3. A strong preference for cross-gender roles in make-believe play or fantasy play. 4. A strong preference for the toys, games, or activities stereotypically used or en gaged in by the other gender. 5. A strong preference for playmates of the other gender. 6. In boys (assi`,
    p: `For natal adult males, prevalence ranges from 0.005% to 0.014%, and for natal females, from 0.002% to 0.003%. Since not all adults seeking hormone treatment and surgical reas signment attend specialty clinics, these rates are likely modest underestimates. Sex differ ences in rate of referrals to specialty clinics vary by age group. In children, sex`,
    r: `Temperamental. For individuals with gender dysphoria without a disorder of sex de velopment, atypical gender behavior among individuals with early-onset gender dyspho ria develops in early preschool age, and it is possible that a high degree of atypicality makes the development of gender dysphoria and its persistence into adolescence and adulthood more likely. Environmental. Among individuals with gender dysphoria without a disorder of sex de vel`,
    d: `Nonconformity to gender roles. Gender dysphoria should be distinguished from sim ple nonconformity to stereotypical gender role behavior by the strong desire to be of an other gender than the assigned one and by the extent and pervasiveness of gender-variant activities and interests. The diagnosis is not meant to merely describe nonconformity to stereotypical gender role behavior (e.g., tomboyism in girls, girly-boy behavior in boys, occasional c`,
  },
};

// ── Disorder Detail Panels (P3) ──────────────────────────────
(function initDisorderDetails() {
  const TAB_LABELS = { c: 'Criteria', p: 'Prevalence', r: 'Risk Factors', d: 'Differential' };

  function buildPanel(label) {
    const entry = DISORDER_DATA[label];
    if (!entry) return null;

    const tabs  = Object.keys(entry).filter(k => TAB_LABELS[k]);
    if (!tabs.length) return null;

    // expand button
    const btn = document.createElement('button');
    btn.className = 'disorder-expand-btn';
    btn.textContent = '▸ Details';

    // panel
    const panel = document.createElement('div');
    panel.className = 'disorder-detail-panel';

    // tab bar
    const tabBar = document.createElement('div');
    tabBar.className = 'detail-tabs';

    // content area
    const contentWrap = document.createElement('div');

    tabs.forEach((k, i) => {
      const tab = document.createElement('button');
      tab.className = 'detail-tab' + (i === 0 ? ' active' : '');
      tab.textContent = TAB_LABELS[k];
      tab.dataset.key = k;

      const content = document.createElement('div');
      content.className = 'detail-content' + (i === 0 ? ' active' : '');
      content.textContent = entry[k];
      content.dataset.key = k;

      tab.addEventListener('click', () => {
        tabBar.querySelectorAll('.detail-tab').forEach(t => t.classList.remove('active'));
        contentWrap.querySelectorAll('.detail-content').forEach(c => c.classList.remove('active'));
        tab.classList.add('active');
        content.classList.add('active');
      });

      tabBar.appendChild(tab);
      contentWrap.appendChild(content);
    });

    panel.appendChild(tabBar);
    panel.appendChild(contentWrap);

    btn.addEventListener('click', () => {
      const open = panel.classList.toggle('open');
      btn.classList.toggle('open', open);
      btn.textContent = open ? '▾ Details' : '▸ Details';
    });

    return { btn, panel };
  }

  document.querySelectorAll('[data-domain="mental-disorders"] .concept-card').forEach(card => {
    const labelEl = card.querySelector('.concept-label');
    if (!labelEl) return;
    const label = labelEl.textContent.trim();
    const built = buildPanel(label);
    if (!built) return;
    card.appendChild(built.btn);
    card.appendChild(built.panel);
  });
})();

// ─────────────────────────────────────────────────────────────────────────────
// SEARCH
// ─────────────────────────────────────────────────────────────────────────────

/** Stored original innerHTML for each searchable node (keyed by element). */
const _originals = new WeakMap();

/** Save original HTML before first search so we can restore highlights. */
function saveOriginal(el) {
  if (!_originals.has(el)) _originals.set(el, el.innerHTML);
}

/** Restore all saved originals (removes highlights). */
function restoreOriginals() {
  document.querySelectorAll("[data-search-marked]").forEach(el => {
    if (_originals.has(el)) el.innerHTML = _originals.get(el);
    el.removeAttribute("data-search-marked");
  });
}

/**
 * Highlight all occurrences of `term` in el.innerHTML.
 * Works on text nodes only — avoids mangling tag attributes.
 */
function highlightIn(el, term) {
  saveOriginal(el);
  const escaped = term.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
  const re = new RegExp(`(${escaped})`, "gi");
  el.innerHTML = el.innerHTML.replace(re, '<mark class="sh">$1</mark>');
  el.setAttribute("data-search-marked", "1");
}

/**
 * Main search handler — called on every keystroke.
 * @param {string} raw - Current value of the search input.
 */
function searchContent(raw) {
  const term = raw.trim();
  const clearBtn = document.getElementById("search-clear");
  const countEl  = document.getElementById("search-count");

  // Show/hide clear button
  if (clearBtn) clearBtn.classList.toggle("visible", term.length > 0);

  // Reset all previous highlights and visibility
  restoreOriginals();
  document.querySelectorAll(".topic.search-hidden, .domain-section.search-hidden")
    .forEach(el => el.classList.remove("search-hidden"));

  if (term.length < 2) {
    if (countEl) countEl.textContent = "";
    return;
  }

  const termLower = term.toLowerCase();
  let matchCount = 0;

  document.querySelectorAll(".domain-section").forEach(domain => {
    let domainHasMatch = false;

    domain.querySelectorAll(".topic").forEach(topic => {
      // Searchable nodes inside each topic
      const nodes = [
        ...topic.querySelectorAll(".topic-name, .concept-title, .concept-label, .concept-desc, .dw, .dt, .code-block"),
      ];

      const topicText = topic.textContent.toLowerCase();
      const matches   = topicText.includes(termLower);

      if (matches) {
        domainHasMatch = true;
        matchCount++;

        // Auto-expand the topic and its parent domain
        topic.querySelector(".topic-header")?.classList.add("open");
        topic.querySelector(".topic-body")?.classList.add("open");
        domain.querySelector(".domain-header")?.classList.add("open");
        domain.querySelector(".domain-body")?.classList.add("open");

        // Highlight in text-bearing nodes
        nodes.forEach(n => highlightIn(n, term));
      } else {
        topic.classList.add("search-hidden");
      }
    });

    if (!domainHasMatch) domain.classList.add("search-hidden");
  });

  if (countEl) countEl.textContent = matchCount ? `${matchCount} match${matchCount !== 1 ? "es" : ""}` : "no matches";
}

/** Clear search input and reset view. */
function clearSearch() {
  const input = document.getElementById("search-input");
  if (input) { input.value = ""; input.focus(); }
  searchContent("");
}

// ── NOTEPAD SLIDE TAB ────────────────────────────────────────────────────────
let _notepadMounted = false;

function toggleNotepad() {
  const panel = document.getElementById('notepad-panel');
  const tab   = document.getElementById('notepad-tab');
  const open  = panel.classList.toggle('open');
  tab.classList.toggle('open', open);

  if (open && !_notepadMounted) {
    _notepadMounted = true;
    // Load the JSX component via Babel standalone
    const script = document.createElement('script');
    script.type = 'text/babel';
    script.src  = 'notepad.jsx';
    script.setAttribute('data-presets', 'react');
    script.onload = () => {
      // notepad.jsx must call mountNotepad() or we mount via global
      if (window.__mountNotepad) window.__mountNotepad();
    };
    document.head.appendChild(script);
  }
}
