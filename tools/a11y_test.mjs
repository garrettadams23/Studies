/**
 * a11y_test.mjs — axe-core against the built page, in both themes.
 *
 * Separate from smoke_test.mjs on purpose. The smoke test asserts that specific
 * behaviour still works and is expected to pass on every commit; this one runs
 * a third-party rule set that can legitimately grow new rules between versions,
 * and mixing the two would make a smoke failure ambiguous.
 *
 * What it checks, and where it stops:
 *
 *   * The shell at load, in dark and light. This is what every visitor sees
 *     first and it must be clean.
 *   * One opened domain with a topic expanded — the accordion, the tool
 *     buttons, the tables and the code blocks — again in both themes.
 *   * A study modal, because a dialog is where keyboard and focus problems
 *     actually live.
 *
 * It does *not* sweep all thirty domains. Content markup is generated from the
 * same conventions everywhere, so the thirtieth domain tests the same rules as
 * the first at thirty times the cost — and `lint_content.py` is what keeps the
 * conventions uniform.
 *
 * Usage:
 *   npm install axe-core playwright && node tools/a11y_test.mjs
 *   node tools/a11y_test.mjs --all      # every violation, not just serious+
 */

import { readFileSync } from "node:fs";
import { createRequire } from "node:module";

const require = createRequire(import.meta.url);
const PAGE = "file://" + process.cwd() + "/index.html";
const ALL = process.argv.includes("--all");

// Same resolution dance as the smoke test: a local install in CI, a global one
// on a developer machine.
const chromium = await (async () => {
  try {
    return (await import("playwright")).chromium;
  } catch {
    // Same list as smoke_test.mjs — this project has no package.json to hang a
    // dependency off, so both scripts look in the usual global roots.
    const bases = [
      "/opt/node22/lib/node_modules",
      "/usr/lib/node_modules",
      "/usr/local/lib/node_modules",
    ];
    for (const base of bases) {
      try {
        return (await import(`${base}/playwright/index.mjs`)).chromium;
      } catch { /* try the next one */ }
    }
    console.error("Could not find playwright. Run: npm install playwright");
    process.exit(2);
  }
})();

const axeSource = (() => {
  const roots = ["", "/opt/node22/lib/node_modules/", "/usr/lib/node_modules/",
                 "/usr/local/lib/node_modules/"];
  for (const root of roots) {
    try {
      return readFileSync(root ? `${root}axe-core/axe.min.js`
                               : require.resolve("axe-core/axe.min.js"), "utf-8");
    } catch { /* try the next root */ }
  }
  {
    console.error("Could not find axe-core. Run: npm install axe-core");
    process.exit(2);
  }
})();

const results = [];
const record = (name, violations) => {
  const kept = ALL ? violations
    : violations.filter(v => v.impact === "serious" || v.impact === "critical");
  results.push({ name, violations: kept });
  const mark = kept.length ? "FAIL" : "ok  ";
  console.log(`${mark} : ${name}` + (kept.length ? `  — ${kept.length} violation(s)` : ""));
  kept.forEach(v => {
    console.log(`        [${v.impact}] ${v.id}: ${v.help}`);
    v.nodes.slice(0, 3).forEach(n => console.log(`          ${n.target.join(" ")}`));
    if (v.nodes.length > 3) console.log(`          …and ${v.nodes.length - 3} more`);
  });
};

const browser = await chromium.launch();
const page = await browser.newPage();

const scan = async () => {
  await page.evaluate(axeSource);
  return page.evaluate(async () => {
    // Colour-contrast needs real rendering; the rest are structural.
    const r = await window.axe.run(document, {
      resultTypes: ["violations"],
      rules: { "color-contrast": { enabled: true } },
    });
    return r.violations.map(v => ({
      id: v.id, impact: v.impact, help: v.help,
      nodes: v.nodes.map(n => ({ target: n.target })),
    }));
  });
};

const setTheme = t => page.evaluate(theme => {
  document.documentElement.setAttribute("data-theme", theme);
}, t);

for (const theme of ["dark", "light"]) {
  await page.goto(PAGE, { waitUntil: "load" });
  await setTheme(theme);
  await page.waitForTimeout(200);
  record(`shell at load (${theme})`, await scan());

  await page.evaluate(() => {
    const first = document.querySelector(".domain-section").dataset.domain;
    openDomain(domainSection(first));
  });
  await page.waitForTimeout(300);
  await page.evaluate(() => document.querySelector(".domain-body.open .topic-header")?.click());
  await page.waitForTimeout(300);
  record(`an open domain with an expanded topic (${theme})`, await scan());

  await page.evaluate(() => stOpenProgress());
  await page.waitForTimeout(300);
  record(`a study dialog (${theme})`, await scan());
}

await browser.close();

const failed = results.filter(r => r.violations.length);
const total = results.reduce((n, r) => n + r.violations.length, 0);
console.log(`\n${results.length - failed.length}/${results.length} scans clean` +
            (total ? `, ${total} violation(s)` : "") + ".");
process.exit(failed.length ? 1 : 0);
