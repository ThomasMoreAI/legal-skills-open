---
name: draft-witness-statement-sboghossian
title: Witness Statement
description: Use when drafting a witness statement — a first-person factual narrative used as evidence in court, arbitration, or regulatory proceedings. Covers the standard English-law common-law format (DIFC, ADGM, UK) with paragraph-by-paragraph chronological narrative and a statement of truth, contrasted with the civil-law approach (UAE onshore, KSA, Lebanon, France) where oral testimony at hearings predominates. Addresses international arbitration (IBA Rules) hybrid practice. Flags the cardinal rule that a witness statement must be in the witness's own voice, not lawyer-authored advocacy.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/draft/draft-witness-statement
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: litigation
language: en
---

# Witness Statement

A witness statement is the primary vehicle for a witness's direct evidence in common-law proceedings. It replaces the oral examination-in-chief — the witness's statement stands as their direct testimony, and cross-examination follows. A well-drafted witness statement tells the factual story in the witness's own words, addresses the key disputed facts, and equips counsel to cross-examine the opposing witnesses effectively.

## When to use this

- A fact witness needs to provide written evidence in a DIFC, ADGM, UK, or international arbitration proceeding
- The court or tribunal has ordered witness statements as part of its case management directions
- Pre-trial preparation in common-law jurisdictions
- International arbitration (ICC, DIAC, LCIA, ADGM Arbitration) following IBA Rules on Evidence

## Required inputs

| Input | Why it matters | Default |
|---|---|---|
| Witness identification (full name, address, occupation) | Heading and capacity in which the witness testifies | Must provide |
| Subject of dispute | Frames the statement's scope; witness's connection to the dispute | Must provide |
| Relevant time period | Chronological boundaries of the statement | Must provide |
| Facts the witness can personally attest to | The evidentiary heart; must be within personal knowledge | Must establish in instructions; cannot be reconstructed |
| Document references | Exhibits the statement will rely on; number them in advance | Collect all documents before drafting |
| Court / tribunal details | Formatting requirements vary | Must provide |

## Procedural Context: Common Law vs Civil Law

### Common-law jurisdictions (DIFC, ADGM, UK, US)
Witness statements are the standard form of direct evidence. The witness swears or affirms the truth of the statement, the statement stands as their direct evidence at trial, and the opposing party cross-examines. The quality of the statement largely determines the quality of the evidence — a rambling, vague, or internally inconsistent statement damages credibility.

### Civil-law jurisdictions (UAE onshore, KSA, Lebanon, France)
Oral witness testimony at hearings is the norm. Written witness declarations exist but carry less weight; courts may conduct their own witness examinations. Civil-law judges are more inquisitorial — they may ask their own questions. Prepared written statements are useful as supporting documents but are not substitutes for oral testimony in most civil-law MENA proceedings.

### International arbitration (IBA Rules on Evidence)
The IBA Rules on Taking Evidence in International Arbitration (2020 edition) are widely adopted in international proceedings. Under the IBA Rules:
- Written witness statements are submitted in advance of the hearing
- The witness then appears at the hearing for cross-examination and may be asked to confirm the statement
- The tribunal may allow direct examination if the statement does not address a particular point
- Both civil-law and common-law practices are accommodated

## Document Structure (Common-Law / DIFC / ADGM / UK)

### Heading Block

```
IN THE DIFC COURTS
[or: IN THE [ADGM / UK / ARBITRATION TRIBUNAL]

Case No: [X]

[Claimant Name]
— Claimant

v.

[Defendant Name]
— Defendant

WITNESS STATEMENT OF [FULL NAME]
[First Witness Statement / Second Witness Statement if a revised version]

Dated: [Date]
```

### Identification Paragraph

```
1. I am [Full Name]. I am [occupation/role]. I give this evidence on behalf
of [Claimant/Defendant/Third Party]. The facts set out in this statement are
within my own knowledge except where I indicate otherwise.
```

### Statement of Truth

```
I believe that the facts stated in this witness statement are true. I
understand that proceedings for contempt of court may be brought against
anyone who makes, or causes to be made, a false statement in a document
verified by a statement of truth without an honest belief in its truth.
```

(For DIFC: adapt to DIFC Courts Wording. For UK CPR: "I believe the facts stated in this witness statement are true.")

### Structure of the Body

The body must follow a coherent structure — typically chronological — with clear paragraph numbering. Each paragraph should address one topic or event.

**Standard body structure:**

1. **Introduction and background** (2–5 paragraphs)
   - Witness's role and connection to the matter
   - How they first became involved
   - Relevant professional or personal background that makes their evidence relevant and credible

2. **Chronological narrative** (the main body)
   - Date-anchored events in sequence
   - Each paragraph addresses one meeting, document, conversation, or event
   - Quote significant words spoken where accurately remembered; use "words to the effect of" if paraphrasing
   - Reference exhibits inline: "In support of this, I exhibit the email chain dated [date], exhibited as [Initials]-[Number]" (e.g., "JP-1")

3. **Response to specific allegations** (if required)
   - Address the opposing party's key factual claims directly
   - Do not ignore adverse facts — address them squarely and explain the context

4. **Conclusion** (optional — 1 paragraph)
   - Summary of the witness's position; what relief they support

### Exhibit Schedule

At the end of the statement, list all exhibits:

```
JP-1   Email from [sender] to [recipient] dated [date] (2 pages)
JP-2   Agreement dated [date] signed by [parties] (5 pages)
JP-3   [etc.]
```

## Drafting Principles

### First person, narrative — always
"I attended the meeting on 15 March 2023 at the Company's offices in DIFC, together with [Name] and [Name]. During that meeting, [Person] said [words or words to the effect of]."

**Never**: "The witness attended..." or "It is the position of the Claimant that..." — this is not a witness statement; it is a legal submission.

### Personal knowledge only
Distinguish what the witness personally saw, heard, or did from what they were told or inferred. Where the witness is relying on what they were told, state: "I was informed by [Person] that... I cannot personally confirm this but..."

Hearsay: in some proceedings (arbitration, UK civil cases), hearsay is admissible but must be identified as hearsay. In others (some US federal proceedings), it is inadmissible. Know the applicable rules.

### Chronological and specific
- Dates (specific dates are better than "approximately mid-2022")
- Times (where relevant)
- Places (specific rooms, locations)
- Names (specific persons, not "a colleague")

Vagueness ("at some point during the project...") invites aggressive cross-examination and gives the opposing advocate latitude to fill in the vagueness against the witness.

### Avoid opinion (unless expert)
A lay witness testifies to facts; opinion is reserved for expert witnesses. "The building was in disrepair" is opinion. "When I visited on [date], I observed cracked tiles on the floor, water stains on the ceiling, and [witness describes what they saw specifically]" is fact.

### Do not argue the case
The witness provides facts; counsel argues from those facts. A witness statement that says "the Defendant clearly breached the contract" or "it is obvious that the Claimant's position is correct" weakens the statement — it reads as lawyer-authored advocacy rather than genuine witness evidence.

### Address counter-narratives proactively
If the opposing party's statement of case makes specific factual allegations, address them in the witness statement rather than leaving them for cross-examination. A statement that ignores significant adverse facts appears evasive.

### The statement must be in the witness's voice
The lawyer drafts; the witness owns. The final statement must:
- Use the witness's natural vocabulary and sentence structure (not legal boilerplate)
- Accurately reflect the witness's actual recollection (not a "best version" constructed by the lawyer)
- Be read and understood by the witness before signature — the witness will be cross-examined on every word

**Do not have a witness sign a statement they have not read carefully.** The witness must be prepared to stand behind every sentence.

## Exhibit Numbering Convention

Use a consistent convention: the witness's initials + sequential number.
- First witness statement of John Patterson: JP-1, JP-2, JP-3...
- Second witness statement: JP-4, JP-5... (or restart JP2-1, JP2-2 for clarity)
- Attach exhibits in order; paginate the exhibit bundle continuously or separately as required by court/tribunal directions

## Jurisdictional Notes

### DIFC and ADGM
Witness statements follow the English CPR model closely. DIFC Rules of Court Part 29 governs evidence; statement of truth required. Electronic signature acceptable for filing purposes. Exhibits submitted separately to the court's case management system.

### UK (CPR Part 32)
Statement of truth in prescribed form (CPR PD 22); exhibits formally introduced using a certificate of exhibit (not just listed); witness summaries available if the witness is unavailable.

### International Arbitration (IBA Rules on Evidence 2020)
- Witness statements submitted by a date set in the Procedural Order
- The statement must identify the witness's qualifications and connection to the case
- "Hot-tubbing" (concurrent evidence): some tribunals ask witnesses from different parties to testify simultaneously on a common issue; prepare for this
- Witness who has given a statement must attend the hearing unless the tribunal directs otherwise; failure to appear = statement may be disregarded

### Lebanon and UAE onshore
Written witness declarations (شهادة خطية) exist but are supplementary to oral testimony. In Lebanese civil procedure, witnesses are examined directly by the judge; in UAE federal courts, the judge may request witness examination through the court's own process. Preparing a clear written declaration in advance helps organize the witness's oral testimony but is not treated as direct evidence in the way a DIFC statement would be.

## Common Mistakes

- **Lawyer language, not witness language** — if the statement sounds like a pleading, it will be challenged on cross-examination as artificial
- **Vague dates** — "sometime in 2022" is weaker than "15 March 2022"; check calendar, emails, and documents before drafting
- **No exhibits attached** — the statement references "the contract" but no exhibit is attached; the tribunal has nothing to refer to
- **Inconsistency with prior statements** — if the witness has made prior statements (in investigations, police reports, employment grievances), the new statement must be consistent or explicitly address the discrepancy
- **Statement too long** — a 200-paragraph witness statement for a simple commercial dispute buries the key facts in noise; edit to the essentials
- **Missing statement of truth** — without the statement of truth, the statement is not verified evidence; in DIFC and UK, it is a formal deficiency

## Related skills

- [[draft-statement-of-defense]]
- [[draft-settlement-agreement]]
- [[review-litigation-risk]]
- [[kb-litigation-procedure-mena]]
