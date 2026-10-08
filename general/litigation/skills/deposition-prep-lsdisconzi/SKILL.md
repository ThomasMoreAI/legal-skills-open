---
name: deposition-prep-lsdisconzi
title: Deposition Prep
description: Build deposition and witness-examination outlines for the matter's key actors. The witness list comes from the matter's actor register.
author: lsdisconzi
author_url: https://github.com/lsdisconzi/craudio-para-adevogados/tree/main/skills/deposition-prep
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: litigation
language: en
---

# Deposition Prep

Prepares deposition and witness-examination outlines. Each witness gets a tailored outline tied to the case theory, with document-impeachment references and anticipated responses. This workflow names no witness itself — the actor register comes from the matter.

## Running this skill

1. **Load configuration.** Read the configured matter profile and firm profile from the plugin config directory (see CLAUDE.md `## Configuration Location`). If a file is missing, or a critical field still shows `[PLACEHOLDER]`, STOP — tell the attorney: "This plugin needs setup. Run the `cold-start-interview` skill."
2. **Apply the frame.** The Plugin Operating Rules, Shared Guardrails, Decision posture, Jurisdiction recognition, Retrieved-content trust, and Ontology Governance sections of CLAUDE.md govern this skill. The workflow below is a FLOOR, not a ceiling.
3. **Resolve vault paths.** Every `{vault root}` reference resolves against `## Vault location` in CLAUDE.md. Never hard-code an absolute path.
4. **Determine active packs.** Read which jurisdiction packs the matter declares (matter profile `## Packs`) — they govern the available examination mechanism.
5. **Apply the work-product header** from CLAUDE.md `## Outputs` to every internal deliverable.
6. **Run the workflow below.**
7. **Close** with the `⚠️ Reviewer note` block and the next-steps decision tree from CLAUDE.md `## Outputs`.

---

## Workflow

### 1. Build the witness list
Read the matter's actor register. Classify each actor:
- **Friendly witness** — the client and aligned witnesses. Focus: a consistent, documented narrative; emotional management; document familiarity.
- **Hostile witness** — counterparty staff, opposing parties, officials. Focus: locking in admissions; establishing impeachment.
- **Organizational representative** — for institutional-policy and document discovery.

### 2. Per-witness outline
For each witness, build:
- **Examination focus** — what this witness must establish or concede.
- **Key topics** — the questions, grouped by theme.
- **Impeachment** — the witness's own recorded statements (transcript excerpts with timestamps) and any documents that contradict them.
- **Document binder** — every document the witness may be shown: their own statements, counterparty policies, contested documents, relevant legal texts.
- **Anticipated responses** — likely answers and defenses, with follow-ups.

### 3. Strategy and order
Assign each witness a strategy (preparation, impeachment, foundation, pattern discovery) and a primary goal. Sequence the depositions so that foundational admissions are locked in before the witnesses who would be confronted with them.

### 4. Output
- **Per-witness outline** — topics, questions, impeachment documents, anticipated responses
- **Cross-examination plan** — per hostile witness: themes, traps, documents
- **Exhibit list** — documents to be shown to each witness
- **Scheduling order** — witness sequence with the strategic rationale

## Guardrails

- Deposition outlines are preparation tools — not scripts.
- All document references must be authenticated before use.
- Hostile-witness strategies anticipate, but cannot control, testimony.
- Per Ontology Invariant I-1: questions explore allegations, they do not assume guilt.
- Adapt to the forum: where the jurisdiction uses judge-led examination instead of party depositions, prepare written questions (interrogatories / quesitos) per the jurisdiction pack.
- **Ontology compliance:** outputs must satisfy the litigation-relevant error codes in `core/ontology/error-catalog.md`. If an invariant violation is detected, flag with `[ONT-ERROR: <code>]` and do not produce confident output. I-1 is absolute: no conclusory language.
