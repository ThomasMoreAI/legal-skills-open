---
name: transcript-segment-analysis-lsdisconzi
title: Transcript Segment Analysis
description: Deep mining of the transcript corpus — extract verbatim quotes, identify key admissions, map speaker patterns, and cross-reference segments to specific violations.
author: lsdisconzi
author_url: https://github.com/lsdisconzi/craudio-para-adevogados/tree/main/skills/transcript-segment-analysis
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: litigation
language: en
---

# Transcript Segment Analysis

Performs deep analysis of the matter's transcript corpus — extracting verbatim admissions, identifying speaker patterns, and cross-referencing transcript segments to legal violations. This is a retrieval engine — it surfaces and indexes what the transcripts contain; it names no party or case.

## Running this skill

1. **Load configuration.** Read the configured matter profile and firm profile from the plugin config directory (see CLAUDE.md `## Configuration Location`). If a file is missing, or a critical field still shows `[PLACEHOLDER]`, STOP — tell the attorney: "This plugin needs setup. Run the `cold-start-interview` skill."
2. **Apply the frame.** The Plugin Operating Rules, Shared Guardrails, Decision posture, Jurisdiction recognition, Retrieved-content trust, and Ontology Governance sections of CLAUDE.md govern this skill. The workflow below is a FLOOR, not a ceiling.
3. **Resolve vault paths.** Every `{vault root}` reference resolves against `## Vault location` in CLAUDE.md. Never hard-code an absolute path.
4. **Apply the work-product header** from CLAUDE.md `## Outputs` to every internal deliverable; suppress it on externally-facing output per Quiet mode.
5. **Run the workflow below.**
6. **Close** with the `⚠️ Reviewer note` block and the next-steps decision tree from CLAUDE.md `## Outputs`. Run the `ontology-validate` skill on the output before it reaches a court or counterparty.

---

## Workflow

### 1. Load transcript
- Read the transcript from `{vault root}/02-transcripts/<incident>/<file>`.
- Load the rendered HTML version from `{vault root}/awareness/shared/transcripts_rendered/` if available (better speaker diarization).
- Extract all segments with timestamps and speaker labels.

### 2. Key admission extraction
Identify and extract verbatim statements that constitute:
- **Direct admissions** — an actor concedes a fact adverse to their interest
- **Institutional policy statements** — an actor describes a counterparty practice or policy
- **Contradictions** — statements inconsistent with each other or with other evidence
- **Exculpatory findings** — statements that undercut an allegation against the client
- **Procedural violations** — statements showing a required procedure was skipped
- **Identification statements** — an actor self-identifying or naming another

### 3. Speaker pattern analysis
- Map speakers across transcripts (the same voice appearing in multiple files).
- Identify authority relationships (who gives orders, who follows).
- Detect coordination patterns between actors.
- Assess credibility indicators (consistency, contradiction, evasiveness).

### 4. Segment-to-violation cross-reference
- For each violation, identify all segments that support or contradict the allegation.
- Verify that every `Key Action` in a violation record has a verbatim transcript anchor.
- Flag violations with unsupported claims.

### 5. Timeline verification
- Extract all timestamped events from transcripts.
- Cross-reference with the canonical incident timeline.
- Flag temporal inconsistencies or gaps.

### 6. Output
- **Key admissions index** — all verbatim admissions organized by actor and violation
- **Speaker map** — cross-transcript speaker identification
- **Segment evidence matrix** — violation × transcript segment grid
- **Admission strength assessment** — per-admission probative value

## Verbatim quote protocol

- **Quotation marks ONLY when the exact text is in the transcript before you.** Never approximate.
- **Cite format:** `(<transcript-key> seg-N at MM:SSs) "verbatim text"`
- **Speaker attribution:** use the named actor if confirmed, `SPEAKER_XX` otherwise.
- **Multi-language:** preserve the original language; provide a translation in brackets.
- **Flagged quotes:** mark `[verify exact quote against rendered HTML]` if working from memory.

## Guardrails

- No paraphrase inside quotation marks — verbatim or no quotes.
- No gap-filling — missing words stay missing.
- Tag all unverified speaker attributions `[speaker identity — verify]`.
- Cross-reference against rendered HTML for the most accurate speaker diarization.
- **Ontology compliance:** outputs must satisfy the litigation-relevant error codes in `core/ontology/error-catalog.md`. If an invariant violation is detected, flag with `[ONT-ERROR: <code>]` and do not produce confident output. I-1 is absolute: no conclusory language.
