#!/usr/bin/env node
// deliverable-fidelity-en - mechanical fidelity check (zero-dependency ESM).
// Usage: node fidelity-check.mjs <task.json>
// task.json: { findings: [ { id, severity, text, resolution? } ], deliverable }
// Checks whether the key terms of each finding appear in the deliverable.
// An omitted RED finding exits 1.
//
// This is the MECHANICAL half. Tone-downgrading (a RED finding present but described as
// a minor note) is only caught by the LLM spot-check - see SKILL.md.

import { readFileSync } from "node:fs";

const STOP = new Set([
  "the", "and", "or", "but", "nor", "for", "yet", "so", "that", "this", "these", "those",
  "is", "are", "was", "were", "be", "been", "being", "has", "have", "had", "having",
  "will", "would", "shall", "should", "may", "might", "must", "can", "could",
  "with", "without", "within", "from", "into", "onto", "upon", "under", "over", "between",
  "against", "during", "before", "after", "above", "below", "about", "through", "across",
  "not", "any", "all", "each", "such", "than", "then", "when", "where", "which", "while",
  "who", "whom", "whose", "what", "there", "here", "also", "only", "very", "more", "most",
  "its", "their", "they", "them", "your", "our", "his", "her", "it", "as", "at", "by",
  "in", "of", "on", "to", "an", "a", "if", "no", "does", "did", "do",
  // citation scaffolding carries no meaning on its own
  "art", "article", "sec", "section", "para", "paragraph", "clause", "cl", "subsection",
]);

function normalize(s) {
  if (s == null) return "";
  return String(s)
    .replace(/[„""»«’‘'`]/g, '"')
    .replace(/[—–]/g, "-")
    .toLowerCase()
    .replace(/\s+/g, " ")
    .trim();
}

// Key terms: words of 4+ characters that are not stop-words, plus retained
// numbers and docket-style figures (for example "473", "2019").
function keyTerms(text) {
  const norm = normalize(text);
  const raw = norm.split(/[^0-9a-z]+/).filter(Boolean);
  const terms = [];
  const seen = new Set();
  for (const w of raw) {
    if (seen.has(w)) continue;
    const isNum = /^\d{2,}$/.test(w);
    if (isNum || (w.length >= 4 && !STOP.has(w))) {
      terms.push(w);
      seen.add(w);
    }
  }
  return terms;
}

// English inflection is light, so this expands a term into its likely surface forms
// instead of truncating it. Truncation is the wrong tool here: cutting two characters
// off "clause" yields "clau", which matches "claustrophobia". A false match is the
// dangerous direction, because it silently passes an omitted RED finding.
function variants(t) {
  const v = new Set([t]);
  if (t.length >= 5) {
    if (t.endsWith("ies")) v.add(t.slice(0, -3) + "y");
    if (t.endsWith("es")) v.add(t.slice(0, -2));
    if (t.endsWith("s") && !t.endsWith("ss")) v.add(t.slice(0, -1));
    if (t.endsWith("ing")) {
      v.add(t.slice(0, -3));
      v.add(t.slice(0, -3) + "e");
    }
    if (t.endsWith("ed")) {
      v.add(t.slice(0, -2));
      v.add(t.slice(0, -1));
    }
    if (t.endsWith("y")) v.add(t.slice(0, -1) + "ies");
  }
  v.add(t + "s");
  return [...v].filter((x) => x.length >= 4);
}

function coverage(terms, deliverableNorm) {
  if (terms.length === 0) return { present: 0, total: 0, ratio: 1, missing: [] };
  let present = 0;
  const missing = [];
  for (const t of terms) {
    if (variants(t).some((x) => deliverableNorm.includes(x))) present += 1;
    else missing.push(t);
  }
  return { present, total: terms.length, ratio: present / terms.length, missing };
}

const THRESHOLD = 0.4; // at least 40% of a finding's key terms must appear

function main() {
  const path = process.argv[2];
  if (!path) {
    console.error("Usage: node fidelity-check.mjs <task.json>");
    process.exit(2);
  }
  const task = JSON.parse(readFileSync(path, "utf8").replace(/^﻿/, ""));
  const findings = Array.isArray(task.findings) ? task.findings : [];
  const deliv = normalize(task.deliverable);
  if (deliv.length === 0) {
    console.error("No deliverable to check");
    process.exit(2);
  }

  const results = findings.map((f) => {
    const terms = keyTerms(f.text);
    const cov = coverage(terms, deliv);
    const represented = cov.ratio >= THRESHOLD;
    let resolution = null;
    if (f.resolution && String(f.resolution).trim()) {
      const rTerms = keyTerms(f.resolution);
      const rCov = coverage(rTerms, deliv);
      resolution = { represented: rCov.ratio >= THRESHOLD, ratio: Number(rCov.ratio.toFixed(2)) };
    }
    return {
      id: f.id,
      severity: f.severity,
      represented,
      coverage: `${cov.present}/${cov.total}`,
      ratio: Number(cov.ratio.toFixed(2)),
      missing_terms: represented ? [] : cov.missing.slice(0, 8),
      resolution,
    };
  });

  const omittedRed = results.filter((r) => r.severity === "RED" && !r.represented);
  const redResolutionMissing = results.filter(
    (r) => r.severity === "RED" && r.resolution && !r.resolution.represented
  );
  const blocked = omittedRed.length > 0;

  const summary = {
    total: results.length,
    represented: results.filter((r) => r.represented).length,
    omitted_red: omittedRed.map((r) => r.id),
    red_resolutions_missing: redResolutionMissing.map((r) => r.id),
    heaviest_for_llm_spotcheck: results
      .filter((r) => r.severity === "RED")
      .slice(0, 3)
      .map((r) => r.id),
  };

  console.log(
    JSON.stringify(
      {
        summary,
        blocked,
        note: "mechanical check only - tone-downgrading is caught by the LLM spot-check",
        results,
      },
      null,
      2
    )
  );
  process.exit(blocked ? 1 : 0);
}

main();
