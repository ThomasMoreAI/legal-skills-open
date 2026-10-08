---
name: pa-workflow-litigation-deposition-binder-builder-sboghossian
title: Deposition Binder Builder
description: Use when litigation counsel needs a structured preparation binder for a deposition or witness interview. Assembles the witness's CV and role profile, a topic-by-topic questioning outline, indexed relevant documents, prior statements and testimony, and cross-examination wedge points. Applicable in international arbitration and common-law courts (DIFC, ADGM, UK, US) as well as civil-law proceedings where pre-hearing witness interviews are permitted (LB, EG, UAE).
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/pa-workflow/pa-workflow-litigation-deposition-binder-builder
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: eu
practice: litigation
language: en
---

# Deposition Binder Builder

## Purpose

Depositions and adversarial witness interviews are the highest-leverage fact-gathering events in litigation. This workflow produces a structured, indexed binder so that counsel walks in with every document, prior statement, and potential contradiction mapped and ready to use — reducing preparation time from days to hours.

## Inputs

| Input | Required | Notes |
|---|---|---|
| Witness name and role | Yes | Current and prior roles relevant to the matter |
| Case summary / fact pattern | Yes | |
| Document production (discovery set) | Recommended | The workflow indexes and tabs relevant documents |
| Prior deposition transcripts | If available | Basis for contradiction analysis |
| Witness's prior statements (filings, press, email) | If available | |
| Deposition objectives | Recommended | What must be locked down; what admissions are sought |
| Expert report (if expert witness) | If expert | See [[pa-workflow-litigation-expert-witness-prep-memo]] for full expert prep |

## Binder Structure

### Tab 1 — Witness Profile

- **Identity**: full name, employer, title, tenure
- **Role in the matter**: relationship to the dispute, decisions the witness made, documents the witness authored or received
- **Professional background**: career history relevant to credibility (note: over-qualification or gaps may be usable)
- **Personal motive / interest**: any financial interest in the outcome, prior relationship with parties

### Tab 2 — Deposition Objectives

List 5–10 specific factual propositions to establish or foreclose during this deposition:
- What must be confirmed (supporting client's theory)
- What must be pinned down to prevent later shifting (harmful to client)
- What admissions are achievable based on the documents
- What areas to avoid (do not educate the witness)

### Tab 3 — Questioning Outline

Organized by topic, not chronologically. For each topic:

```
Topic: Authorization for Project X
Goal: Establish that witness approved the payment on [date]

Q1: Were you responsible for approving payments over $X during Q1 2024?
  Documents: Ex. 12 (witness email), Ex. 45 (approval form)
  Expected answer: Yes / No
  If YES → proceed to Q2
  If NO → pivot to Q3 (who else had authorization)

Q2: Did you review this payment request before approving it?
  Expected answer: Yes (document shows his signature)
  Key exhibit: Ex. 45, p. 3
```

Structure: funnel from broad (to lock in general statements) to specific (to confront with documents).

### Tab 4 — Document Index (Tabbed)

For each document to be used at the deposition:
- Exhibit number
- Date, author, recipients
- One-line summary
- Topic(s) it addresses
- Questions that rely on this exhibit

Tabs ordered by topic (matching the questioning outline), not by exhibit number.

### Tab 5 — Prior Statements and Testimony

| Statement | Date | Forum | Key Passage | Potential Contradiction |
|---|---|---|---|---|
| Deposition (Matter X) | 2022-03-15 | DIFC Court | "I never reviewed that document" | Conflicts with Ex. 12 — his signature appears on it |
| Email to Board | 2023-06-01 | Internal | "I approved all Q2 payments personally" | Contradicts planned testimony of limited role |

Flag: run [[pa-workflow-litigation-witness-contradiction-finder]] before the deposition to ensure all contradictions are mapped.

### Tab 6 — Cross-Examination Wedge Points

Specific impeachment sequences — each wedge has:
1. The prior inconsistent statement
2. The exhibit or transcript reference
3. The confrontation question sequence
4. What to do if witness explains away the inconsistency

Example:
- **Wedge**: Witness claims he had no authority over the account; prior deposition states he approved all wire transfers
- **Exhibit**: Depo transcript p. 47, lines 12–19; Ex. 23 (wire approval log)
- **Sequence**: "You testified in 2022 that you approved all wire transfers. I'm showing you Exhibit 23. Is that your signature?"

### Tab 7 — Defensive / Rehabilitation (Own Witnesses)

If preparing a favorable witness, include:
- Anticipated cross-examination topics by opposing counsel
- Coaching notes (consistent with ethical rules — factual framing, not coaching answers)
- Documents the witness should be familiar with
- Topics to avoid volunteering

## Jurisdictional Notes

- **US**: Federal Rule of Civil Procedure 30 governs depositions. Deposition testimony is admissible at trial for impeachment or if witness is unavailable. Counsel may instruct witness not to answer only on privilege grounds.
- **UK / DIFC / ADGM**: Depositions as in the US are not standard. Witness statements are served in advance. Cross-examination occurs at the hearing. Use this binder for hearing preparation and cross-examination planning.
- **International Arbitration (ICC, LCIA, DIAC, ADCCAC)**: IBA Rules on the Taking of Evidence govern most arbitrations. Document production is more limited than US discovery. Witness statements replace direct examination. Cross-examination planning is the primary use of this binder.
- **UAE onshore / KSA / LB / EG**: Civil-law proceedings typically do not include formal depositions. Witness examination occurs before the court or a commissioned judge. Written witness statements or judicial questioning are the norm. This binder is adapted for hearing preparation and formulating written questions submitted through the court.
- **KSA**: Commercial courts use written pleadings and sessions before judges. Expert witnesses (khabir) are court-appointed, not party-appointed. Planning cross-examination of a court expert requires different focus — challenge methodology and assumptions, not credibility.

## Common Mistakes

- Organizing the binder chronologically rather than by topic — wastes time at deposition pivoting through documents
- Including too many objectives — pick 5–8 achievable goals; covering 20 topics produces superficial coverage
- Failing to map all prior statements before the deposition — witnesses exploit unmapped inconsistencies
- Not planning wedge sequences in advance — unplanned impeachment often fails because the document is not at hand
- Ethical violation: coaching a witness on what to say rather than what to review (the line: review documents = acceptable; rehearse answers = not acceptable)

## Related Skills

- [[pa-workflow-litigation-witness-contradiction-finder]]
- [[pa-workflow-litigation-transcript-search-q-and-a-indexing]]
- [[pa-workflow-litigation-expert-witness-prep-memo]]
- [[pa-workflow-litigation-case-theory-simulator]]
- [[pa-workflow-litigation-discovery-first-pass-tagging]]
