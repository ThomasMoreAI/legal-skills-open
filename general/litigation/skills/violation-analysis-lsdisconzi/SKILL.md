---
name: violation-analysis-lsdisconzi
title: Violation Analysis
description: Process candidate violations across all jurisdictions through the structured pipeline — evidence → norms → nexus → confidence → jurisprudence enrichment. Use when analyzing any violation or running a comprehensive violation sweep.
author: lsdisconzi
author_url: https://github.com/lsdisconzi/craudio-para-adevogados/tree/main/skills/violation-analysis
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: litigation
language: en
---

# Violation Analysis

Runs the structured legal violation analysis pipeline against any candidate violation in the active matter. This is a probabilistic reasoning engine: it consumes facts from the matter and legal knowledge from packs, and emits candidate violations with confidence scores. It names no statute, party, or case — all legal knowledge is loaded from packs.

## Inputs

- **Matter facts** — actions, actors, evidence, and existing violation records from the active matter folder (`{matter root}/`).
- **Domain pack(s)** — `packs/domain/<id>/norm-templates.yaml` supplies the normalized norm templates (each with `norm_type`, `required_elements`, `evidence_hints`, `severity_default`).
- **Jurisdiction pack(s)** — `packs/jurisdiction/<id>/framework-index.yaml` resolves each norm template to concrete statutory articles; `citation-format.yaml` governs how they are cited.
- **Ontology** — `core/ontology/invariants.yaml`, `graph-model.yaml`, `confidence-rules.yaml`.

## Running this skill

1. **Load configuration.** Read the configured matter profile and firm profile from the plugin config directory (see CLAUDE.md `## Configuration Location`). If a file is missing, or a critical field still shows `[PLACEHOLDER]`, STOP — tell the attorney: "This plugin needs setup. Run the `cold-start-interview` skill."
2. **Apply the frame.** The Plugin Operating Rules, Shared Guardrails, Decision posture, Jurisdiction recognition, Retrieved-content trust, and Ontology Governance sections of CLAUDE.md govern this skill. The workflow below is a FLOOR, not a ceiling.
3. **Resolve matter paths.** Every `{matter root}` reference resolves against `## Vault location` in CLAUDE.md. Never hard-code an absolute path.
4. **Determine active packs.** Read which domain and jurisdiction packs the matter declares (matter profile `## Packs`). Load their norm templates and framework indexes.
5. **Apply the work-product header** from CLAUDE.md `## Outputs` to every internal deliverable; suppress it on externally-facing output per Quiet mode.
6. **Run the workflow below.**
7. **Close** with the `⚠️ Reviewer note` block and the next-steps decision tree from CLAUDE.md `## Outputs`. Run the `ontology-validate` skill on the output before it reaches a court or counterparty.

---

## Workflow

### For a single violation

1. **Load the violation record** from `{matter root}/01-violations/<jurisdiction>/<id>.md`.
2. **Run the violation pipeline** (via the `violation-refiner` MCP if connected, otherwise perform each step directly):
   - **Evidence layer** — anchor every asserted fact to a matter evidence item via `SUPPORTS_ACTION`. Every Action needs ≥1 evidence item (invariant IX-1).
   - **Norms layer** — match the conduct to norm templates in the active domain pack(s); resolve each template to statutory articles via the active jurisdiction pack's `framework-index.yaml`.
   - **Nexus layer** — connect each fact to each norm element with explicit reasoning.
   - **Confidence** — score per `core/ontology/confidence-rules.yaml`; propagate uncertainty Evidence → Action → Violation (downstream confidence ≤ min upstream).
   - **Jurisprudence enrichment** — find supporting precedent via the jurisprudence MCP named in the active jurisdiction pack.
3. **Cross-reference related violations** — check the `related_violations` field and verify consistency.
4. **Output:** Structured analysis with:
   - Allegation summary (non-conclusory per Ontology Invariant I-1)
   - Legal basis table (article → nexus)
   - Legal reasoning (applicable framework, factual subsumption, fact-norm nexus, evidentiary strength, severity, procedural integrity)
   - Key actions / admissions with verbatim transcript quotes
   - Cross-references to related violations
   - Open questions for discovery
   - Source bundle reference and confidence score

### For all violations (sweep)

1. **Index all violation files** from `{matter root}/01-violations/<jurisdiction>/` across every jurisdiction the matter declares.
2. **Sort by severity** (per the severity vocabulary in CLAUDE.md) and jurisdiction.
3. **Process in batches** of 10-15 per run.
4. **Aggregate findings:** severity distribution matrix, cross-reference network map, evidence overlap analysis, legal-framework coverage check.
5. **Output:** Comprehensive sweep report with dashboard.

### For a jurisdiction subset

Run the sweep filtered to a single jurisdiction's violations only. Use for jurisdiction-specific briefs or demand letters.

## Integration with other skills

- After violation analysis, run `cross-jurisdiction-nexus` to map connections across jurisdictions.
- Run `jurisprudence-search` on any violation with an unresolved framework mapping.
- Run `chronology` after completing violation analysis to sync the timeline.
- Run `claim-chart` to construct element-by-element claims from violation findings.

## Ontology graph vocabulary

This skill produces nodes and edges per `core/ontology/graph-model.yaml`. Edges it creates: `SCOPES_VIOLATION`, `GROUNDED_IN_ACTION`, `VIOLATES_ARTICLE`, `SUPPORTS_ACTION`, `INVOLVES_ACTOR`, `PERFORMED_BY`.

**Direction is sacred:** Evidence → Action → Violation → LegalArticle. Never reverse it (invariants I-2, I-3).

## Guardrails

- All findings are allegations, not adjudicated facts (Ontology Invariant I-1).
- Confidence scores are pipeline-assigned — attorney review required.
- Statutory articles come from the active packs; verify cross-jurisdictional articles against primary sources.
- Jurisprudence citations carry their session-provenance tag (`[juris-<jurisdiction>]` or `[model knowledge — verify]`).
- Severity assessments are analytical, not judicial.
- **Ontology compliance:** outputs must satisfy the litigation-relevant error codes in `core/ontology/error-catalog.md`. If an invariant violation is detected, flag with `[ONT-ERROR: <code>]` and do not produce confident output. I-1 is absolute: no conclusory language.
