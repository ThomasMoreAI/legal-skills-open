---
name: medical-record-chronology
title: Medical Record Chronology
description: Creates verified, Bates-cited chronological summaries of medical records for litigation. Extracts treatment timelines, providers, diagnoses, procedures, medications, and causation evidence with every clinical fact traceable to a specific Bates range. Identifies gaps, inconsistencies, pre-existing conditions, and records needing follow-up. Flags unverifiable claims rather than dropping them. Use this skill whenever the user asks for a medical chronology, medical summary, treatment timeline, or records review in a personal injury, medical malpractice, workers comp, or disability case, and any time medical records are produced for analysis, even if the user does not say the word 'chronology'.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/medical-record-chronology
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: personal-injury
language: en
tags: [litigation, analysis, summarization]
---

# Medical Record Chronology

Produce a chronological summary of medical records that an attorney can take into a deposition, mediation, or trial. Every clinical fact must be traceable to a Bates citation. Unverifiable claims must be flagged inline rather than silently dropped or fabricated.

This skill assumes a case.dev style environment where medical records have been ingested into a retrieval system and chunks are returned with Bates range metadata. If that is not the operating environment, see "Operating Environments" below.

## Required Reading Before Drafting

Always consult these companion skills as part of producing the chronology:

1. `bates-citation-verification` - citation format, the verification pass, and how to handle UNVERIFIED claims. This is non-negotiable, not a suggestion.
2. `icd-cpt-normalization` - normalize and expand any diagnostic or procedure codes that appear in the records.

If those skills are unavailable in the current environment, fall back to the inline rules in the "Citation Discipline" and "Code Normalization" sections of this file.

## Workflow

Run these phases in order. Do not skip ahead.

### Phase 1: Intake

Before retrieving anything, capture from the calling context or ask the user:

1. Patient name and DOB
2. Date of incident (or earliest event of interest)
3. Case type (PI, med mal, workers comp, disability, other)
4. Claimed injuries and body parts at issue
5. Output format preference if stated, otherwise apply the decision tree in "Output Format Selection"

If any of items 1 through 4 are missing and cannot be inferred, ask. Do not guess at the patient or the incident date. Both are anchors for the entire chronology and being wrong is a malpractice level error for the attorney downstream.

### Phase 2: Source Inventory

Build the Provider Index first. Retrieve broadly to identify every provider, facility, and date range present in the corpus. The goal of this phase is coverage, not depth. Producing the index before the chronology forces you to notice missing records (a provider mentioned in a referral but with no records produced) before they become invisible gaps in the narrative.

For each provider identified, record:

- Provider or facility name
- Type (ER, PCP, specialist, PT, imaging center, pharmacy, IME)
- First and last visit dates present in the records
- Whether records appear complete, partial, or referenced but missing
- Bates range covering this provider's records

### Phase 3: Pre-Incident Baseline

Before chronicling post-incident treatment, summarize relevant pre-incident medical history:

- Treatment to the same body parts or conditions claimed
- Prior injuries, accidents, or workers comp claims
- Active medications at the time of the incident
- Documented baseline functional status

Pre-incident records are where defense counsel lives. Treat this section with the same rigor as the post-incident chronology. If pre-incident records are absent from the production, say so explicitly. Their absence is itself a finding.

### Phase 4: Chronological Synthesis

Walk every encounter in strict date order, interleaving providers. Do not group by provider. The chronology's value comes from showing the actual sequence of care as it unfolded.

For each encounter, extract:

- Chief complaint (patient's stated reason)
- History as documented (mechanism of injury, symptom onset, prior treatment mentioned)
- Examination findings (objective: vitals, range of motion, neurological, palpation findings)
- Diagnostic studies (imaging, labs, EMG/NCV, with results)
- Diagnoses (narrative plus normalized codes via `icd-cpt-normalization`)
- Treatment provided (procedures via CPT, medications, injections, referrals)
- Restrictions or limitations (work status, activity limits)
- Follow-up plan
- Causation language: provider statements connecting injury to incident, in direct quotation, with Bates citation. Flag these prominently.

Every line of every encounter must end with a Bates citation. See "Citation Discipline."

### Phase 5: Cross-Cutting Sections

After the encounter-by-encounter chronology, produce:

- Diagnostic study table (every imaging or diagnostic study with date, facility, findings, significance)
- Medication history (every prescription with start, end, prescriber, purpose, changes)
- Damages summary (medical expenses by provider where billing is in the production, lost time documentation, functional limitations, MMI status, future treatment)

### Phase 6: Strategic Analysis

Surface what the attorney needs to know that is not obvious from the chronology itself:

- **Favorable findings**: evidence supporting causation and damages
- **Adverse findings**: pre-existing conditions, treatment gaps, inconsistent histories, non-compliance, symptom magnification language, secondary gain notations
- **Gaps in records**: providers referenced but not produced, unexplained treatment gaps, records to request
- **Inconsistencies**: conflicting mechanism-of-injury descriptions across providers, history discrepancies, chart contradictions
- **Follow-up needed**: additional records to request, providers to depose, IME considerations

Both favorable and adverse findings must be included. The attorney needs the complete picture to prepare for opposing counsel.

### Phase 7: Verification Pass

Before producing the final output, run the verification pass defined in `bates-citation-verification`. At minimum:

1. Extract canonical Bates prefix(es) and citation format from production header pages before checking citations.
2. Reject or mark `[UNVERIFIED]` any citation with a mismatched prefix, spacing, or digit pattern.
3. Verify each cited Bates page with independent page-level PDF OCR/text-layer extraction; vault search can support drafting but is not final verification.
4. Confirm the cited page exists, extract literal page text, and verify direct quotes verbatim or paraphrases as clearly supported.
5. Remove or correct contradicted claims; mark claims `[UNVERIFIED]` only when they appear in records but cannot be page-verified.
6. Create an auditable verification log with citation, claim, method used, Bates page, source date if visible, supporting excerpt, result, and corrective action.

Do not skip this phase. A chronology with fabricated or wrongly attributed facts is worse than no chronology because it gets relied on.

## Subagent Integrity

When using research or verification subagents, prepend each task with patient identifiers, canonical Bates prefix(es), case theory/body parts, and a rule that patient-identity mismatch is a retrieval failure, not content to summarize.

- The parent must spot-check 3 random claims from each subagent output against source before integration. If any spot-check fails, reject or rerun the full output.
- Research subagents (`vault-researcher`, `citation-verifier`, `case-researcher`, or equivalents) may not upload to the vault or matter via `vault_upload`, `casedev vault object upload`, `casedev vault upload`, or similar commands.
- If rejected subagent output may have uploaded artifacts, the parent must list matter/vault objects, delete the unreliable artifacts, and document the cleanup before continuing.

## Citation Discipline

Every clinical fact requires a Bates citation in square brackets at the end of the sentence or bullet:

```
Patient reported neck pain rated 8/10 radiating to the left shoulder. [SMITH00145]
MRI of the cervical spine on 03/14/2024 showed C5-C6 disc herniation with
left-sided foraminal narrowing. [SMITH00203-00205]
```

For citation format details, multi-source claims, quotation handling, and the verification pass, see `bates-citation-verification`.

### Balanced verification posture

This skill operates in balanced mode: cite all clinical facts, flag unverifiable claims as `[UNVERIFIED]` rather than dropping them. The attorney needs to know what was claimed in the records even if the supporting page was not produced. Removing the claim entirely hides information; flagging it surfaces a follow-up item.

Three categories:

| Category | Treatment |
|----------|-----------|
| Verified | Cite the Bates range, include in chronology |
| Unverified | Include in chronology, append `[UNVERIFIED - claim appears in records but specific page not retrievable]` |
| Contradicted | Remove the claim. If the contradiction is itself useful (impeachment material), surface it in Strategic Analysis with both source citations. |

Never invent a Bates range. If you cannot tie a specific fact to a specific page, mark it `[UNVERIFIED]`.

## Code Normalization

When a diagnosis or procedure code appears in the records, normalize it:

- ICD-9 codes seen in older records should be cross-walked to ICD-10-CM
- ICD-10 codes should be expanded to their full narrative description
- CPT codes should be expanded to their procedure description
- Flag any bundling or unbundling oddities for billing-relevant cases (med mal, fee disputes)

For the lookup protocol and code patterns, see `icd-cpt-normalization`.

## Output Format Selection

This skill produces either Word document or markdown output. Pick based on context:

| Signal | Output |
|--------|--------|
| User says "word doc," ".docx," "send to [attorney]," "for the file," "deliverable" | docx |
| User attaches a firm template or letterhead | docx using their template |
| Calling agent is rendering output in case.dev or another markdown-native UI | markdown |
| Output is intermediate (will be summarized further, fed to another agent) | markdown |
| Default when ambiguous | markdown, offer at end to convert |

For Word document generation, locate and use the document-generation capability available in the current runtime, preferring a `docx` or `documents` skill/tool when present. If the user requested a Word deliverable and no document-generation capability is available, do not silently downgrade; produce markdown only as an intermediate draft and flag Word generation as blocked. If document generation is available but fails, return a markdown fallback labeled `WORD GENERATION FAILED`, include the error or failure reason, and recommend retrying with the same content or providing a firm template if template loading caused the failure. For the canonical structure of each format, see:

- `references/output-template-markdown.md`
- `references/output-template-docx.md`

Both templates produce the same logical content; only the rendering differs.

## Operating Environments

The skill assumes Bates-cited, case.dev-native RAG retrieval. If operating elsewhere:

- **Local PDF files only, no retrieval system**: the calling agent should extract text with the PDF-extraction capability available in the runtime and produce a Bates index. If the records are not Bates-stamped, fall back to file-name-plus-page-number citations using the same square-bracket convention: `[smith_records.pdf p.45]`. State the citation scheme explicitly in the output header.
- **Mixed sources**: prefer Bates where available, fall back to file/page where not. Be consistent within a section.
- **No source access at all (records summarized in context only)**: this is a degraded mode. Produce the chronology but mark the entire output `[CITATION UNAVAILABLE - produced from in-context summary only]` at the top. Recommend the attorney rerun against full records.

## Causation Language Patterns

Causation language is the highest-value text in any medical record. The provider's opinion on whether the incident caused the injury determines damages. See `references/causation-language-patterns.md` for the patterns that signal causation opinions (favorable and adverse) and how to surface them in the chronology.

## Critical Rules

1. Strict chronological order. Interleave providers by date. Never group by provider in the main chronology.
2. Quote causation language verbatim. Provider opinions on causation are the most valuable text in the records. Quote exactly, in quotation marks, with Bates citation.
3. Flag every pre-existing mention. Same body part, prior injury, prior treatment. Defense counsel will find these whether you do or not.
4. Note treatment gaps. Opposing counsel argues gap equals no injury. The attorney needs to know about them now.
5. Track medication changes. Escalation suggests worsening, discontinuation suggests resolution or non-compliance.
6. Distinguish objective from subjective. Imaging and measurements are objective. Pain ratings and symptom reports are subjective. Both matter; conflating them weakens the chronology.
7. Note every mechanism-of-injury description. Inconsistencies across providers are impeachment material.
8. Never fabricate a citation. If you cannot verify it, flag it `[UNVERIFIED]`. Inventing Bates ranges is the fastest way to make the attorney sanctionable.
9. Include both favorable and adverse findings. A one-sided chronology is malpractice in waiting.
10. Run the verification pass before output. Phase 7 is not optional.

## Troubleshooting

- **Missing pre-incident records**: Say they were not produced, list the providers or date ranges to request, and do not imply a clean baseline.
- **Conflicting incident dates or mechanisms**: Preserve each version with its citation and surface the conflict under Strategic Analysis.
- **Unverified citations**: Keep the claim only if it appears in the records, mark it `[UNVERIFIED]`, and add it to follow-up needed.
- **Word deliverable blocked or failed**: Provide a markdown fallback labeled with the blocker or failure reason, then state what capability, retry, or template is needed.
