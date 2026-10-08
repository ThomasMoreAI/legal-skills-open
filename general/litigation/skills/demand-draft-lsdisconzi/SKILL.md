---
name: demand-draft-lsdisconzi
title: Demand Draft
description: Draft jurisdiction-specific demand letters to each defendant in the matter. Language and forum come from jurisdiction packs; claims and demands come from the matter's violation analysis.
author: lsdisconzi
author_url: https://github.com/lsdisconzi/craudio-para-adevogados/tree/main/skills/demand-draft
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: litigation
language: en
---

# Demand Draft

Drafts jurisdiction-specific, evidence-anchored demand letters to each defendant in the matter. This workflow orchestrates engines and packs — it names no party itself: defendants come from the matter's party register; language and forum come from jurisdiction packs.

## Running this skill

1. **Load configuration.** Read the configured matter profile and firm profile from the plugin config directory (see CLAUDE.md `## Configuration Location`). If a file is missing, or a critical field still shows `[PLACEHOLDER]`, STOP — tell the attorney: "This plugin needs setup. Run the `cold-start-interview` skill."
2. **Apply the frame.** The Plugin Operating Rules, Shared Guardrails, Decision posture, Jurisdiction recognition, Retrieved-content trust, and Ontology Governance sections of CLAUDE.md govern this skill. The workflow below is a FLOOR, not a ceiling.
3. **Resolve vault paths.** Every `{vault root}` reference resolves against `## Vault location` in CLAUDE.md. Never hard-code an absolute path.
4. **Determine active packs.** Read which domain and jurisdiction packs the matter declares (matter profile `## Packs`).
5. **Apply the work-product header** from CLAUDE.md `## Outputs` to internal deliverables; strip it from the external notice.
6. **Run the workflow below.**
7. **Close** with the `⚠️ Reviewer note` block and the next-steps decision tree from CLAUDE.md `## Outputs`. Run the `ontology-validate` skill on each draft before it is sent.

---

## Workflow

### 1. Select defendant
Read the matter's party register. For each defendant, determine from the jurisdiction packs: the working language (`language-defaults.yaml`), the candidate forum (`courts.yaml`), and the engaged frameworks (`framework-index.yaml`). The claims against the defendant come from the matter's `violation-analysis` output.

### 2. Demand letter structure
- **Header** — firm letterhead, service method, date, reference line naming the matter and the addressed defendant.
- **Body** — (1) client identification; (2) factual narrative, chronological, with evidence citations; (3) legal basis — articles × facts with nexus reasoning; (4) damages claimed, moral and material, with calculation basis; (5) specific demands; (6) deadline to comply; (7) consequences of non-compliance.
- **Footer** — counsel signature block (bar registration as the jurisdiction requires).

Language and formal register follow the addressed jurisdiction's `language-defaults.yaml`.

### 3. Tailor the demands to the defendant
Tailor each demand to the defendant's role and the violations against it. Demand classes: corrective action (e.g. remove a restriction, correct a record), retraction of false statements, monetary compensation (moral and material), evidence preservation, and policy or structural change. Pull the specific corrective and compensation items from the matter's violations and the `prejudice-quantification` output.

### 4. Output
- A demand letter in `.docx` for each defendant, in the addressed jurisdiction's language.
- Working translations for the file.
- An internal copy with the reviewer note; an external copy with the work-product header stripped.

## Guardrails

- Settlement-privilege awareness: mark demands as settlement communications in the addressed jurisdiction's idiom.
- Send gate: confirm with counsel before any demand is sent.
- Apply the destination check before any draft leaves the firm.
- All cited evidence must be verified and hashed before issuance.
- Demand letters are pre-litigation instruments, not filed pleadings.
- Tone: firm but professional — never inflammatory.
- **Ontology compliance:** outputs must satisfy the litigation-relevant error codes in `core/ontology/error-catalog.md`. If an invariant violation is detected, flag with `[ONT-ERROR: <code>]` and do not produce confident output. I-1 is absolute: no conclusory language.
