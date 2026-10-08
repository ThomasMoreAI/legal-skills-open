---
name: prompt-pack-witness-statement-sboghossian
title: Witness Statement
description: Use when a legal team needs to draft a witness statement for court or tribunal proceedings — setting out a factual narrative, the witness's direct observations, and a jurisdiction-appropriate statement of truth. Covers chronological structure, factual vs. opinion boundaries, exhibit referencing, and form requirements across MENA (UAE, DIFC, ADGM, Lebanon, Egypt) and common-law (UK) litigation contexts. Distinct from the arbitration witness statement skill, which follows IBA Rules conventions.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/prompt-pack/prompt-pack-witness-statement
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: litigation
language: en
---

# Witness Statement

## When to use this

Use this skill to draft a witness statement for use in court or tribunal proceedings — not arbitration (see [[prompt-pack-witness-statement-arbitration]] for the arbitration-specific version).

A witness statement is the witness's evidence-in-chief in written form. In most DIFC, ADGM, and UK proceedings, the witness statement stands as the witness's oral testimony in the examination-in-chief; the witness is then cross-examined. In UAE onshore and Lebanese civil proceedings, witness evidence is typically oral, but written statements are used to organize and present the witness's testimony and may be submitted as a written memorial or preliminary statement. In KSA courts, testimony is primarily oral before the judge; written statements are used for preparation purposes.

## Required inputs

| Input | Why it matters | Sensible default |
|-------|---------------|-----------------|
| Witness full name and title / role | Identifies the witness and their basis for knowledge | Prompt user |
| Case name / number | Identifies the proceedings | Prompt user |
| Court / tribunal | Governs form requirements and statement of truth wording | Prompt user |
| Jurisdiction | Determines statement of truth form, language, and procedural requirements | Prompt user |
| Factual matters the witness speaks to | The substance of the statement | Prompt user — provide detailed briefing notes or interview summary |
| Date range of relevant events | Helps structure the chronological narrative | Prompt user |

## Optional inputs

- **Exhibit list** — documents the witness references; exhibits must be attached to the statement
- **Prior statements or communications** — prior witness statements, interview notes, contemporaneous correspondence
- **Expert report to respond to** — if the witness is a factual witness responding to an expert's characterization of events
- **Opposing party's pleading** — helps structure the statement around contested facts

## Document structure

1. **Heading** — court / case name; case number; name of witness; number of statement (First, Second, etc.); date; party on whose behalf the statement is made

2. **Introduction**
   - Full name, current address (or professional address if witness prefers for privacy), occupation / role
   - If the witness is an employee or officer of a party: state that and confirm they have been authorized to make the statement
   - "I make this statement from my own personal knowledge of the matters set out herein, save where I indicate otherwise, in which case I believe the facts to be true."
   - If any part is based on information provided by others, identify the source

3. **Background** — witness's role, how long they have been in the role, their involvement in the events at issue; keep brief (2–5 paragraphs)

4. **Factual narrative** — chronological account of the events the witness directly observed or participated in; each material event should have its own paragraph (or short group of paragraphs); reference exhibits as "[Exhibit A]" or "[WS-1]" per the applicable exhibit numbering convention; state what the witness saw, heard, said, did, or received — not their legal conclusions; where the witness has a document that records a conversation or meeting, refer to the document rather than paraphrasing it

5. **Response to disputed facts** (if applicable) — address the opposing party's specific factual allegations that the witness can speak to; label this section clearly so it is easy to navigate in cross-examination

6. **Statement of truth** — the precise wording required varies by jurisdiction (see below); failure to include the correct statement of truth may render the statement inadmissible or require an amended filing

---

**Statement of truth wording by jurisdiction:**

| Jurisdiction | Required wording |
|---|---|
| DIFC Courts | "I believe the facts stated in this witness statement are true. I understand that proceedings for contempt of court may be brought against anyone who makes, or causes to be made, a false statement in a document verified by a statement of truth." |
| ADGM Courts | Same as DIFC (based on ADGM Court Procedure Rules) |
| English High Court / UK | "I believe the facts stated in this witness statement are true. I understand that proceedings for contempt of court may be brought against anyone who makes, or causes to be made, a false statement in a document verified by a statement of truth without an honest belief in its truth." (Civil Procedure Rules r. 22.1) |
| UAE onshore courts | Arabic-language proceedings; witness oath administered orally before the court; written statement may be submitted as a preliminary written memorial but formal witness examination is typically oral — confirm with local counsel |
| Lebanon | Civil procedure before the Courts of First Instance; witness examination is oral; written statements used for preparation; no formal CPR-equivalent statement of truth |
| Egypt | Civil procedure (Code of Civil Procedure Law 13/1968); oral testimony; written statements used as preparation documents |
| KSA | Sharia-based proceedings; testimony given orally before the court; written statements used for preparation; no Western-style statement of truth requirement |

7. **Exhibits** — list all exhibits referenced in the statement; exhibits are typically labeled with the witness's initials and a number (e.g., "WS-1," "JD-1"); attach originals or certified copies; in DIFC proceedings, exhibits form part of the trial bundle

---

## Jurisdictional notes

**DIFC / ADGM:** Common-law procedure; witness statements are the standard form of evidence-in-chief; stand as oral testimony; witness is cross-examined; DIFC Practice Direction 2 governs format and content requirements. Statements must be in English; Arabic translations may be filed for bilingual witnesses.

**UAE onshore:** Civil procedure is inquisitorial; judges take a more active role in questioning witnesses; detailed factual witness statements in the Western sense are less common; focus instead on preparing structured witness preparation notes and brief written summaries. Statements are in Arabic (or translated).

**Lebanon:** French-influenced civil procedure; notarial affidavits (affidavit notarié) are used in commercial litigation; witnesses examined by the judge; written witness statements used as preparation documents; Arabic (and sometimes French) required.

**Egypt:** Civil procedure derived from French model; oral testimony before the court; written witness memos submitted to support the oral testimony; Arabic required.

**KSA:** Judicial system based on Islamic jurisprudence (Sharia); witnesses must meet Sharia competency requirements (adala); testimony oral before the judge; women's testimony historically subject to weight considerations (though Saudi legal reforms since 2017 have modernized some aspects of commercial litigation); in SAGIA and commercial courts, written evidence is increasingly accepted in practice.

**UK courts:** CPR Part 32 and Practice Direction 32 govern witness statements; must include the witness's own words; no "lawyer language" substituted for the witness's own account; practice direction specifies page limits in some courts.

## Drafting standards

- **First person, direct observation** — write "I saw," "I heard," "I received," not "the Claimant observed" or "evidence establishes"
- **No legal conclusions** — legal argument belongs in written submissions, not witness statements; flag any clause in the briefing notes that contains legal conclusions and rewrite as factual observations
- **Each paragraph = one topic** — courts and opposing counsel navigate statements by paragraph number; mixed-topic paragraphs create cross-examination difficulty
- **Exhibit references must be accurate** — a statement referencing an exhibit that does not exist or is mislabeled creates procedural problems at trial
- **Language consistency** — use the witness's natural language register; an obviously "lawyerized" statement may be challenged in cross-examination or by the court
- **Statement of truth is non-negotiable** — include the jurisdiction-correct version verbatim; do not paraphrase

## Common mistakes

- **Legal conclusions embedded in factual narrative** — "The defendant breached its duty" is for the pleading, not the witness statement
- **Hearsay not identified** — if the witness is recounting what someone else told them, state who said it, when, and in what context; hearsay that is not acknowledged can be challenged on admissibility
- **Outdated statement of truth wording** — UK CPR statement of truth was updated in 2020; verify the current wording
- **Missing exhibit schedule** — every document referenced in the statement must be attached and numbered
- **Overlapping with expert evidence** — witness statements address facts; if the witness is also giving opinion evidence, they need to be qualified as an expert (different formal requirements)

## Related skills

- [[prompt-pack-witness-statement-arbitration]]
- [[prompt-pack-expert-report]]
- [[review-pleading]]
- [[heuristic-always-state-jurisdiction-first]]
