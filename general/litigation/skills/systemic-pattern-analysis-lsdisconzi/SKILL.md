---
name: systemic-pattern-analysis-lsdisconzi
title: Systemic Pattern Analysis
description: Analyze the institutional pattern across incidents — recurring policies, document-handling practices, and dismissive culture. Distinguishes the systemic pattern from individual violations.
author: lsdisconzi
author_url: https://github.com/lsdisconzi/craudio-para-adevogados/tree/main/skills/systemic-pattern-analysis
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: litigation
language: en
---

# Systemic Pattern Analysis

Where a matter spans more than one incident, the institutional pattern — same organization, same culture, recurring across staff and locations — can be more powerful than any single violation. This engine maps the systemic architecture revealed across the incidents. It names no party or policy: the institutional policies are read from the active matter; the legal frameworks they engage come from packs.

## Inputs

- **Matter facts** — the matter's `systemic-policies` record (the catalogued institutional policies, each with its supporting transcript admissions), incident records, and violation index, from `{vault root}`.
- **Domain / jurisdiction pack(s)** — `norm-templates.yaml` and `framework-index.yaml` to map each policy to the legal frameworks it engages.

## Running this skill

1. **Load configuration.** Read the configured matter profile and firm profile from the plugin config directory (see CLAUDE.md `## Configuration Location`). If a file is missing, or a critical field still shows `[PLACEHOLDER]`, STOP — tell the attorney: "This plugin needs setup. Run the `cold-start-interview` skill."
2. **Apply the frame.** The Plugin Operating Rules, Shared Guardrails, Decision posture, Jurisdiction recognition, Retrieved-content trust, and Ontology Governance sections of CLAUDE.md govern this skill. The workflow below is a FLOOR, not a ceiling.
3. **Resolve vault paths.** Every `{vault root}` reference resolves against `## Vault location` in CLAUDE.md. Never hard-code an absolute path.
4. **Determine active packs.** Read which domain and jurisdiction packs the matter declares (matter profile `## Packs`).
5. **Apply the work-product header** from CLAUDE.md `## Outputs` to every internal deliverable; suppress it on externally-facing output per Quiet mode.
6. **Run the workflow below.**
7. **Close** with the `⚠️ Reviewer note` block and the next-steps decision tree from CLAUDE.md `## Outputs`. Run the `ontology-validate` skill on the output before it reaches a court or counterparty.

---

## Workflow

### 1. Identify the systemic policies
Read the matter's catalogued institutional policies. For each policy record: the policy statement, the supporting verbatim transcript admissions (with evidence anchors), the incidents in which it recurs, and its effect on the client's statutory rights. If the matter has no catalogued policies, derive candidates from recurring transcript admissions and flag them `[candidate policy — verify]`.

### 2. Pattern evidence aggregation
To establish a systemic pattern rather than isolated events, build a cross-incident consistency table: each evidence type as a row, each incident as a column, and the recurring institutional behaviour as the pattern. Every cell anchors to evidence (invariants II-1, IX-1).

### 3. Institutional architecture diagram
Draw the organization's structure and show, per unit, the practices the evidence exposes and the shared infrastructure that lets a practice recur across units and locations.

### 4. Legal implications
For each policy, map the frameworks it engages — distinct from the individual-violation mapping — using the norm templates and framework indexes from the active packs. A policy engages law differently than a single act does.

### 5. Pattern-litigation strategy
Assess: the admissibility of other-acts/pattern evidence in each forum (from each jurisdiction pack's procedural rules); whether the admissions bind the organization (authority of the speaking actor); and any continuing-violation doctrine that affects prescription.

### 6. Output
- **Policy-by-policy analysis** — each policy with evidence, legal basis, and effects
- **Pattern evidence matrix** — cross-incident consistency table
- **Institutional architecture map** — diagram of the organization's structure and practices
- **Legal implications grid** — Policy × Jurisdiction × Framework × Claim
- **Pattern-litigation strategy** — how to present the pattern in each forum

## Guardrails

- Systemic allegations are inferences from multiple data points — label them as such (invariant I-1: no conclusory language; II-1: traceable to evidence).
- Distinguish pattern evidence from individual-violation evidence (invariant I-2: no interpretive collapse).
- Policy admissions rest on actor statements — the actor's authority to bind the organization must be established.
- Pattern analysis supports, but does not replace, individual violation analysis.
- **Ontology compliance:** outputs must satisfy the litigation-relevant error codes in `core/ontology/error-catalog.md`. If an invariant violation is detected, flag with `[ONT-ERROR: <code>]` and do not produce confident output. I-1 is absolute: no conclusory language.
