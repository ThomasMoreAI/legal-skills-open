---
name: prompt-pack-witness-statement-arbitration-sboghossian
title: Witness Statement (Arbitration)
description: Use when a legal team needs to draft a witness statement for international arbitration proceedings — following IBA Rules on the Taking of Evidence or applicable institutional rules (ICC, LCIA, DIAC, SIAC, ADCCAC). Covers background, factual narrative, exhibit referencing, statement of truth, and the specific structural and stylistic standards that distinguish arbitration witness statements from court statements. Particularly relevant for MENA-seated arbitrations (DIAC, ADCCAC, Bahrain Chamber) and international arbitrations involving MENA parties.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/prompt-pack/prompt-pack-witness-statement-arbitration
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: arbitration
language: en
---

# Witness Statement (Arbitration)

## When to use this

Use this skill to draft a witness statement for international arbitration proceedings. International arbitration witness statements differ materially from court-filed statements in several respects:

- They are almost universally written in English regardless of the seat (DIFC, ICC, LCIA, SIAC, DIAC all conduct proceedings in English as the default language)
- They follow the IBA Rules on the Taking of Evidence in International Arbitration (2020) as a widely accepted standard, even when not expressly adopted
- Exhibits are typically numbered as part of the claimant's or respondent's exhibit bundle (C-1, C-2... / R-1, R-2...) and the witness statement references them by exhibit number
- Witness statements substitute for oral direct examination; witnesses are presented for cross-examination only
- The tribunal may request a "hot tubbing" (concurrent expert or witness examination) format; this affects how the statement is structured

Use this skill for:
- Claimant or respondent witness statements in ICC, LCIA, DIAC, SIAC, ADCCAC, or ICSID arbitrations
- Investment arbitration witness statements (ICSID, UNCITRAL)
- Domestic arbitration where the parties have adopted international procedural rules (common in MENA commercial arbitrations)

For UAE onshore domestic arbitration under Law No. 6/2018 (Federal Arbitration Law), or KSA domestic arbitration under the Arbitration Law (Royal Decree M/34/2012), witness evidence procedures may be less formalized — adapt this structure accordingly.

## Required inputs

| Input | Why it matters | Sensible default |
|-------|---------------|-----------------|
| Witness full name, title, and current employer / role | Identifies the witness and establishes basis of knowledge | Prompt user |
| Arbitration reference / case number | Identifies the proceedings | Prompt user |
| Arbitral institution and seat | Governs procedural rules and language | Prompt user |
| Applicable rules (IBA Rules, UNCITRAL, institutional rules) | Shapes structure and content requirements | Default: IBA Rules 2020 |
| Statement number (First, Second, Rebuttal) | Determines whether this is direct evidence or responding to opposing evidence | Prompt user |
| Factual matters to be covered | The substance | Prompt user — provide briefing notes or interview summary |

## Optional inputs

- **Procedural timetable / Procedural Order No. 1** — confirms page limits, exhibit rules, language requirements
- **Opposing witness statements / expert reports** — if this is a rebuttal statement, provide for targeted response
- **Tribunal's specific instructions** — some tribunals require specific formatting (Times New Roman 12pt; numbered paragraphs; etc.)
- **Confidentiality order** — if the arbitration is under a confidentiality regime, confirm whether the statement may reference documents marked confidential

## Document structure

### Header block
```
INTERNATIONAL ARBITRATION
[CASE REFERENCE]

In the matter of an arbitration under [ICC/LCIA/DIAC/SIAC/UNCITRAL] Rules
Between:
[CLAIMANT] — Claimant
and
[RESPONDENT] — Respondent

WITNESS STATEMENT OF [FULL NAME]
[First / Second / Rebuttal] Witness Statement
Dated: [DATE]
```

### 1. Introduction
- Full name, nationality, current position and employer
- Length of time in current role; relevant professional background (brief — 2–4 sentences)
- "I am authorized by [Party] to make this statement on its behalf" (if corporate witness)
- "The facts set out in this statement are within my personal knowledge, except where otherwise indicated"
- Reference to documents reviewed in preparation: "In preparing this statement I have reviewed [list or general description: e.g., the correspondence in my files and documents disclosed in these proceedings]"
- If any part is based on information from colleagues / third parties, identify the source and explain why the witness cannot personally confirm

### 2. Background
- Witness's role at the company and how it relates to the dispute
- The project / transaction / contractual relationship at issue
- How and when the witness became involved in the relevant events
- Keep to 2–5 paragraphs — detailed chronology belongs in §3

### 3. Factual narrative
- Chronological account of the events the witness directly participated in or observed
- Paragraph-level granularity: one event or topic per paragraph
- Reference exhibits by bundle number: "[Exhibit C-15]" or "[Exhibit R-3]"
- Where a meeting or call took place: state who was present, when, where (phone/in person), and what was said / agreed / decided
- Where the witness sent or received a document: reference it as an exhibit; do not merely paraphrase
- Where the witness is aware of events they did not directly observe: state clearly "I was informed by [Name] that..." and explain the source
- Avoid characterizing events as "consistent with" or "proof of" — factual description only

### 4. Response to opposing party's factual allegations (rebuttal statement only)
- If this is a rebuttal, address the specific paragraphs of the opposing witness statements that the witness disputes
- Cross-reference: "In [Name]'s First Witness Statement, paragraph [X], [Name] states [quote]. This is incorrect. [Witness's account]."
- Focus on matters within the witness's direct knowledge; do not speculate about the opposing witness's credibility or motivations

### 5. Statement of truth
The IBA Rules 2020 do not prescribe exact wording but the following is standard practice in international arbitration:

> "I, [FULL NAME], hereby certify that the facts stated in this witness statement are true and accurate to the best of my knowledge, information, and belief."

Some institutions or tribunals specify language; where a Procedural Order addresses the statement of truth, use that language verbatim.

If the witness is in a jurisdiction where a notarized affidavit is customary (e.g., KSA), confirm with the tribunal whether notarization is required or whether a signed statement is sufficient.

### 6. Signature block
- Date and place of signing
- Witness signature
- Full name printed below

---

## IBA Rules on the Taking of Evidence — key provisions

| Article | Content | Practical note |
|---|---|---|
| Art. 4 | Witness statements — form and content | Must contain full name, address, employer, present-tense facts, references to documents, and statement of truth |
| Art. 4(5) | Simultaneous exchange vs. sequential | Many tribunals order simultaneous exchange of first witness statements; rebuttal statements follow |
| Art. 4(6) | Tribunal may limit number of witnesses | Tribunals sometimes cap witness statements at a page limit; check Procedural Order |
| Art. 4(7) | Request to appear for cross-examination | Either party may request that a witness appear; witness who does not appear may have their statement excluded or given no weight |
| Art. 4(8) | Witnesses not testifying at hearing | If a witness cannot attend, statement may still be admitted but will receive less weight |
| Art. 8 | Evidentiary hearing | Witness examination order; cross-examination follows direct; re-examination on new matters only |

## Jurisdictional notes

**DIAC (Dubai International Arbitration Centre):** DIAC Arbitration Rules 2022 apply by default; IBA Rules commonly adopted as guidance. Seat typically Dubai; English is predominant language; Arabic translation may be required for Arabic-speaking witnesses. Dubai Federal Courts (not DIFC) have supervisory jurisdiction over DIAC awards.

**DIFC-LCIA (now DIAC):** Following the merger of DIFC-LCIA into DIAC in 2021, new arbitrations are filed under DIAC Rules 2022. DIFC Courts have supervisory jurisdiction over arbitrations seated in the DIFC.

**ADCCAC (Abu Dhabi Commercial Conciliation and Arbitration Centre):** Now rebranded; ADCCAC Rules 2013 still referenced in older arbitration clauses; procedural rules similar to international norms; Abu Dhabi courts supervise.

**ICC:** Most common seat for major MENA commercial arbitrations; ICC Rules 2021; no specific witness statement requirements beyond Art. 25(3) (parties may submit written statements signed by witnesses); IBA Rules often adopted as supplement.

**LCIA:** LCIA Rules 2020 Art. 20; similar flexibility; witness statements common.

**Investment arbitration (ICSID):** ICSID Arbitration Rules 2022 Rule 36 — tribunal may request fact witnesses; no mandatory statement form; in practice, detailed written statements following international commercial practice are submitted.

**KSA domestic arbitration (Royal Decree M/34/2012):** Domestic arbitration law modernized and aligns broadly with UNCITRAL Model Law; witness evidence practice is developing; for international-standard MENA arbitrations, parties often elect DIAC or ICC rules regardless of seat.

## Drafting standards

- **Numbered paragraphs are mandatory** — arbitration witness statements must have consecutive paragraph numbers (¶1, ¶2, etc.) so that parties can cross-reference in skeleton arguments and the tribunal can refer to specific paragraphs in the award
- **Exhibit references must map to the exhibit bundle** — confirm exhibit numbers with the legal team before finalizing; a mismatch between statement references and exhibit bundle is a significant error
- **Avoid opinion and legal argument** — the tribunal knows the law; factual witnesses should not explain what an event "means legally"; reserve legal characterizations for briefs and memorials
- **Length discipline** — tribunals frequently set page or word limits; aim for concision; a long statement that does not add weight over a short one actively harms credibility
- **Witness review and sign-off is essential** — the statement is the witness's evidence, not the lawyer's; the witness must understand and genuinely adopt every paragraph before signing

## Common mistakes

- **Paragraphs that characterize documents** — "This email shows that..." is argument; the statement should describe what the witness saw, sent, or received, not what it proves
- **Hearsay not flagged** — in international arbitration, hearsay is generally admissible but should be identified; hidden hearsay undermines credibility
- **No exhibit numbers** — references to "the email of 15 March" without an exhibit number are ambiguous and difficult to trace in a large bundle
- **Missing statement of truth** — technically curable but creates procedural delays and may affect weight given to the statement
- **Not tailored to IBA Rules / institutional rules** — generic court-style witness statements may not comply with the procedural order; always check the tribunal's specific instructions

## Related skills

- [[prompt-pack-witness-statement]]
- [[prompt-pack-expert-report]]
- [[prompt-pack-arbitration-clause]]
- [[kb-arbitration-mena]]
- [[heuristic-always-state-jurisdiction-first]]
