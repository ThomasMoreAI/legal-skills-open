---
name: evidence-chain-verification-lsdisconzi
title: Evidence Chain Verification
description: Verify the authenticity, chain of custody, and forensic integrity of all evidence items. Check hashes, source-to-transcript alignment, speaker diarization accuracy, and identify gaps requiring preservation orders.
author: lsdisconzi
author_url: https://github.com/lsdisconzi/craudio-para-adevogados/tree/main/skills/evidence-chain-verification
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: litigation
language: en
---

# Evidence Chain Verification

Systematic verification of the evidentiary record's forensic integrity. Ensures every piece of evidence is authenticated, hashed, and chain-of-custody documented before use in any filing. This is a deterministic engine — it names no party or case; it operates over whatever evidence registry the active matter declares.

## Running this skill

1. **Load configuration.** Read the configured matter profile and firm profile from the plugin config directory (see CLAUDE.md `## Configuration Location`). If a file is missing, or a critical field still shows `[PLACEHOLDER]`, STOP — tell the attorney: "This plugin needs setup. Run the `cold-start-interview` skill."
2. **Apply the frame.** The Plugin Operating Rules, Shared Guardrails, Decision posture, Jurisdiction recognition, Retrieved-content trust, and Ontology Governance sections of CLAUDE.md govern this skill. The workflow below is a FLOOR, not a ceiling.
3. **Resolve vault paths.** Every `{vault root}` reference resolves against `## Vault location` in CLAUDE.md. Never hard-code an absolute path.
4. **Apply the work-product header** from CLAUDE.md `## Outputs` to every internal deliverable; suppress it on externally-facing output per Quiet mode.
5. **Run the workflow below.**
6. **Close** with the `⚠️ Reviewer note` block and the next-steps decision tree from CLAUDE.md `## Outputs`. Run the `ontology-validate` skill on the output before it reaches a court or counterparty.

---

## Workflow

### 1. Inventory check
- Load every evidence item from `{vault root}/03-evidence/`.
- Cross-reference with the transcript note map at `{vault root}/02-transcripts/transcript_note_map.json`.
- Flag any evidence item not found in the vault at its declared path.

### 2. Hash verification
- Items marked `UNHASHED` or `UNHASHED_ATTACHMENT_REF`: generate a SHA-256 hash.
- Items marked `INDEX_MAP_VERIFIED`: confirm the hash matches the registry.
- Items with missing source files: flag for client/curator action.
- **Command:** `sha256sum <path>` on all media files.

### 3. Transcript-to-source alignment
For each transcript with a media source, verify:
- Duration matches between transcript metadata and the media file
- Speaker count is consistent
- Segment timestamps fall within the media duration
- No unexplained gaps longer than 10 seconds
- Flag any transcript without a verified media source.

### 4. Chain of custody
For each evidence item, verify the custody chain is documented: who recorded it, when, where it is stored, who has accessed it (curation log), and that no modifications were made to original evidence. Flag any break in the chain.

### 5. Speaker identification
- Cross-reference speaker labels across transcripts.
- Map `SPEAKER_XX` labels to named actors where identified.
- Flag transcripts where critical speakers are not yet identified.

### 6. Gap analysis
Identify evidence gaps requiring action. For each gap, record: what is missing, why it matters to the case theory, the jurisdiction-appropriate mechanism to obtain it (preservation order, information request, discovery request), and the deadline pressure. Common gap classes: counterparty-held recordings, official records held by a public body, internal counterparty documents, personnel records of named actors.

### 7. Output
- **Evidence integrity report** — per-item hash and chain status
- **Gap matrix** — what is missing, why it matters, how to obtain it
- **Preservation action list** — immediate steps with deadlines (feeds the `legal-hold` workflow)
- **Authentication certificate** — for items ready for judicial use

## Guardrails

- Never alter original evidence files.
- Hash all evidence before any court submission.
- Document every access and transformation.
- Flag any integrity concern immediately.
- Chain-of-custody breaks must be reported, not concealed.
- **Ontology compliance:** outputs must satisfy the litigation-relevant error codes in `core/ontology/error-catalog.md`. If an invariant violation is detected, flag with `[ONT-ERROR: <code>]` and do not produce confident output. I-1 is absolute: no conclusory language.
