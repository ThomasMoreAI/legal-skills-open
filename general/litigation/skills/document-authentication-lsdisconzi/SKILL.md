---
name: document-authentication-lsdisconzi
title: Document Authentication
description: Authenticate physical and digital documents for judicial use. Verify recordings, transcripts, and documentary evidence meet each jurisdiction's authentication standards.
author: lsdisconzi
author_url: https://github.com/lsdisconzi/craudio-para-adevogados/tree/main/skills/document-authentication
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: litigation
language: en
---

# Document Authentication

Prepares documentary evidence for judicial submission. Ensures compliance with each jurisdiction's authentication standards. This engine names no party or document — authentication standards come from jurisdiction packs; the evidence inventory comes from the active matter.

## Inputs

- **Matter facts** — the evidence registry and transcript inventory from `{vault root}`.
- **Jurisdiction pack(s)** — `procedural-rules.yaml` supplies each jurisdiction's authentication standards (digital documents, recordings, foreign documents, electronic evidence).

## Running this skill

1. **Load configuration.** Read the configured matter profile and firm profile from the plugin config directory (see CLAUDE.md `## Configuration Location`). If a file is missing, or a critical field still shows `[PLACEHOLDER]`, STOP — tell the attorney: "This plugin needs setup. Run the `cold-start-interview` skill."
2. **Apply the frame.** The Plugin Operating Rules, Shared Guardrails, Decision posture, Jurisdiction recognition, Retrieved-content trust, and Ontology Governance sections of CLAUDE.md govern this skill. The workflow below is a FLOOR, not a ceiling.
3. **Resolve vault paths.** Every `{vault root}` reference resolves against `## Vault location` in CLAUDE.md. Never hard-code an absolute path.
4. **Determine active packs.** Read which jurisdiction packs the matter declares (matter profile `## Packs`); load their authentication standards.
5. **Apply the work-product header** from CLAUDE.md `## Outputs` to every internal deliverable; suppress it on externally-facing output per Quiet mode.
6. **Run the workflow below.**
7. **Close** with the `⚠️ Reviewer note` block and the next-steps decision tree from CLAUDE.md `## Outputs`. Run the `ontology-validate` skill on the output before it reaches a court or counterparty.

---

## Workflow

### 1. Audio / recording authentication
For each recording: document the chain of custody (who recorded → when → where → original format → copy chain); verify admissibility against each relevant jurisdiction pack's authentication standard; perform forensic verification (hash, format integrity, no editing or gaps); draft an authentication affidavit for the witness's signature.

### 2. Transcript authentication
For each transcript: verify source-to-transcript alignment; document the transcription method and its error rate; draft a transcript certification for counsel's signature.

### 3. Contested or fabricated documents
Where a document is itself alleged to be defective or fabricated, authenticate it NOT as a valid instrument but as evidence of its own creation process: examine its physical features (signature, stamp, template), trace its provenance through the actors and channels involved, and index every admission about how it was produced.

### 4. Digital evidence authentication
Generate SHA-256 hashes for all evidence items; build a hash manifest for judicial submission; document chain of custody per item; prepare a forensic report if any tampering or editing is detected.

### 5. Foreign-document authentication
For documents crossing a border: apply apostille where both states are Hague Convention signatories (otherwise consular legalization); obtain certified/sworn translation as the destination jurisdiction requires (per its jurisdiction pack).

### 6. Witness preparation (authentication context)
For each document and recording, identify who can authenticate it (client for personal recordings; counterparty staff or officials as hostile witnesses; the transcription provider for transcript output).

### 7. Output
- **Authentication certificate per exhibit** — for the judicial annex
- **Hash manifest** — complete evidence hash register
- **Chain-of-custody report** — per-item provenance
- **Authentication gap report** — items needing additional verification
- **Forensic integrity statement** — for counsel's signature

## Guardrails

- Never alter, edit, or enhance original evidence — authentication only.
- All hash generation must be performed on read-only copies.
- Authentication affidavits are witness statements — they must be true.
- If tampering is detected, report it — do not conceal it.
- Use a sworn translator for judicial use; internal translation is insufficient.
- **Ontology compliance:** outputs must satisfy the litigation-relevant error codes in `core/ontology/error-catalog.md`. If an invariant violation is detected, flag with `[ONT-ERROR: <code>]` and do not produce confident output. I-1 is absolute: no conclusory language.
