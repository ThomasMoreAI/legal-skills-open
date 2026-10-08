---
name: ontology-validate-lsdisconzi
title: Ontology Validation
description: Check a structured legal-analysis output against the machine-readable ontology invariants. Use after any engine or workflow skill produces violations, claim charts, demand letters, or briefs — and before that output reaches a court or counterparty.
author: lsdisconzi
author_url: https://github.com/lsdisconzi/craudio-para-adevogados/tree/main/skills/ontology-validate
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: litigation
language: en
---

# Ontology Validation

Validates a structured legal-analysis output against the ontology invariants in `core/ontology/invariants.yaml`. This is the governance layer's check — the closest thing the platform has to runtime enforcement.

## Running this skill

1. **Load the invariants.** Read `core/ontology/invariants.yaml`, `core/ontology/graph-model.yaml`, and `core/ontology/confidence-rules.yaml`.
2. **Load the target.** Read the output to validate — a file path, or text pasted by the attorney. It is typically the result of an engine skill (`violation-analysis`, `claim-chart`, `legal-framework-mapping`, …) or a workflow skill (`demand-draft`, `brief-section-drafter`, …).
3. **Run every check below.**
4. **Emit a validation report.**

## Checks

For each invariant in `invariants.yaml`, apply its `detection_hint`:

| Invariant | Check |
|---|---|
| I-1 | Scan for conclusory language (`guilty`, `liable`, `verdict`, `proven`, `adjudicated`, `is responsible for`). Allegation framings only. |
| I-2 | No prohibited edge from `graph-model.yaml` `prohibited:` list (e.g. Evidence→LegalArticle). |
| I-3 | No Evidence node with an outgoing edge to a Violation or LegalArticle. |
| II-1 | Every Violation traces a full path to a source pack. |
| II-2 | Every Violation has ≥1 Action link AND ≥1 LegalArticle link. |
| VIII-3 | Every cross-jurisdiction claim states an ApplicabilityBasis for its jurisdiction pair. |
| IX-1 | Every named Action has ≥1 supporting Evidence item. |
| IX-2 | Every machine-generated Violation carries a confidence score. |
| IX-3 | The output records the producing skill's version. |

Also verify uncertainty propagation: a downstream node's confidence must not exceed the minimum confidence of the nodes it depends on (`confidence-rules.yaml` → `uncertainty_propagation`).

## Output — Validation report

```
ONTOLOGY VALIDATION — <target>
Ontology version: 2.4

PASS: I-2, II-1, IX-3
FAIL:
  [ONT-I1-CONCLUSION-DETECTED] line 12 — "the carrier is liable" → conclusory
  [ONT-IX1-UNSUPPORTED-ACTION]  Action "off-book document routing" has no Evidence
WARN:
  [ONT-IX2-MISSING-CONFIDENCE]  Violation #4 has no confidence score

VERDICT: NOT CLEARED — 2 critical/high failures must be resolved before this
output reaches a court or counterparty.
```

A `critical` or `high` failure blocks the output. A `medium` failure is a warning the attorney may waive with an explicit note.

## Guardrails

- This skill never edits the target output — it only reports. Fixing is the producing skill's job.
- If `core/ontology/invariants.yaml` is missing or unparseable, STOP and report the governance layer as broken — do not pass the output by default.
- Validation is structural, not legal: a cleared output is ontology-compliant, not legally correct. Attorney review still required.
