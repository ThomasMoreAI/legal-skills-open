---
name: in-draft-declaration-codearranger
title: Draft an Indiana Declaration (or Affidavit)
description: 'This skill should be used when the user asks to "draft an Indiana declaration", "Indiana affidavit", "T.R. 11(B) verification", "Indiana sworn statement", "I affirm under penalties for perjury", "declaration in support of Indiana motion", "Indiana declaration template", "Indiana affidavit template", "Indiana verified statement", or any related sworn- statement drafting request. Scaffolds a declaration that satisfies Indiana Trial Rule 11(B), the IC 35-44.1-2-1 perjury standard, and the personal-knowledge requirement of Indiana Evidence Rule 602. Trigger phrases: "Indiana declaration", "T.R. 11(B)", "Indiana affidavit", "Indiana verified statement", "Indiana sworn declaration", "affirm under penalties for perjury".'
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/in-court-docs/skills/in-draft-declaration
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Draft an Indiana Declaration (or Affidavit)

A declaration is a sworn written statement that supports a
motion or other filing by providing the factual predicate the
movant relies on. Indiana practice uses both **declaration** (the
short form, signed under penalties for perjury per T.R. 11(B))
and **affidavit** (the longer form, traditionally notarized).
Both serve the same purpose; declarations are now standard
practice because notarization is no longer required by rule for
most submissions.

> **NOT LEGAL ADVICE.** Generated content is a drafting aid;
> false statements in a declaration are perjury under IC
> 35-44.1-2-1 — Class D felony. Verify every factual statement
> before signing.

## Verification language — Trial Rule 11(B) and IC 35-44.1-2-1

Indiana's statutory verification language differs from California
and other jurisdictions. **Do not import non-conforming
language.** The required formula:

> **"I affirm, under the penalties for perjury, that the foregoing
> representations are true."**

This phrase derives from IC 35-44.1-2-1(b) (the Indiana perjury
statute) and is the Indiana counterpart to a notarized oath
under T.R. 11(B) and IC 34-37-2-2. The phrase MUST appear
verbatim — Indiana courts have rejected variations like "I
declare ..." or "under penalty of perjury under the laws of the
State of Indiana ..."

If notarization is required (some statutes still require it —
e.g., the Affidavit of Indigency under IC 33-37-3-2 must be
sworn before a notary), use the traditional affidavit form:

```
STATE OF INDIANA   )
                   ) SS:
COUNTY OF [____]   )

I, [NAME], being first duly sworn upon my oath, depose and
state:
   ...
                              _______________________________
                              [NAME]

SUBSCRIBED AND SWORN TO before me, a notary public, this ____
day of _________, 20__.

                              _______________________________
                              Notary Public
                              [County, IN]
                              My commission expires: __________
```

## Personal knowledge — Indiana Evidence Rule 602

IRE 602 requires a witness to have **personal knowledge** of the
matter testified to. A declaration that contains hearsay,
speculation, or argumentation does not satisfy the foundation —
the court will disregard inadmissible portions on summary
judgment.

Best practices:

- Open the declaration with: "I have personal knowledge of the
  matters stated herein and, if called as a witness, could and
  would testify competently thereto."
- Avoid argumentation — declarations state FACTS, not legal
  conclusions
- Avoid "I believe" or "it is my understanding" — use "I
  observed" / "I received" / "I sent" instead
- Attach exhibits with foundation (e.g., "Attached as Exhibit A
  is a true and accurate copy of [the contract / the letter / the
  statement]")

## Scaffolded declaration

```
                     STATE OF INDIANA
                  IN THE [COURT NAME] COURT
              [COUNTY NAME] COUNTY, INDIANA

[PLAINTIFF NAME],                   )
                                    )
            Plaintiff,              )    Cause No. [###]
                                    )
        v.                          )
                                    )
[DEFENDANT NAME],                   )
                                    )
            Defendant.              )

   DECLARATION OF [SIGNER NAME] IN SUPPORT OF DEFENDANT'S
              MOTION TO [RELIEF]

   I, [SIGNER NAME], state the following:

   1. I am the [Defendant / Plaintiff / declarant role] in the
above-captioned action. I have personal knowledge of the matters
stated herein and, if called as a witness, could and would
testify competently thereto.

   2. [First fact, narrated in the first person.]

   3. [Second fact.]

   4. Attached as Exhibit A is a true and accurate copy of [the
document]. I [authored / received / am familiar with] the
document and its contents.

   5. [Continue with numbered factual paragraphs.]

I affirm, under the penalties for perjury, that the foregoing
representations are true.


Date: _______________      _______________________________
                              [SIGNER NAME]
                              [Street Address]
                              [City, IN ZIP]
                              Telephone: (___) ___-____
                              Email: ________________________
```

## Exhibits

Declarations are the standard vehicle for getting exhibits into
the record. Foundation for each exhibit:

| Document type | Foundation language |
|---------------|---------------------|
| Contract / agreement | "Attached as Exhibit A is a true and accurate copy of [the contract] between [parties], dated [date]. I [signed / received / have personal knowledge of the execution of] this contract." |
| Letter | "Attached as Exhibit B is a true and accurate copy of a letter I received from [sender] on or about [date]." |
| Email | "Attached as Exhibit C is a true and accurate copy of an email I received from [sender] on [date] at [time]." |
| Bank statement | "Attached as Exhibit D is a true and accurate copy of my [bank] account statement for [period]." |
| Payment record | "Attached as Exhibit E is a true and accurate copy of my payment record showing payments made to Plaintiff between [start] and [end]." |
| Photograph | "Attached as Exhibit F is a true and accurate copy of a photograph I took on [date] depicting [subject]." |
| Business record (when filed by custodian) | "Attached as Exhibit G is a true and accurate copy of [record]. The record was made at or near the time of the events described, by a person with knowledge, in the course of [organization]'s regularly conducted business activity, and it was the regular practice of [organization] to make such records (IRE 803(6))." |

Use **lettered exhibits** (A, B, C ...) — Indiana convention is
lettered, not numbered.

## Witness vs. party declarations

- **Party declarations**: signed by the party (plaintiff,
  defendant). The party has personal knowledge of their own
  conduct, communications they received, and documents they
  signed.
- **Witness declarations**: signed by a third party (e.g., a
  manager who was present at the meeting). Must affirmatively
  state how the witness has personal knowledge.
- **Expert declarations**: subject to IRE 702-705; require a
  statement of qualifications, a summary of opinions, and the
  basis for each opinion.

## When a declaration is required

Indiana practice requires a supporting declaration whenever a
motion relies on facts not apparent from the pleadings:

| Motion | Declaration required? |
|--------|----------------------|
| T.R. 12(B)(6) Motion to Dismiss | NO — confined to the Complaint |
| T.R. 12(B)(2) Lack of Personal Jurisdiction | YES — facts about contacts |
| T.R. 12(B)(4)/(5) Insufficient Process / Service | YES — facts about service defect |
| T.R. 56 Motion for Summary Judgment | YES — Statement of Material Facts must cite admissible evidence |
| T.R. 60(B)(1) Motion to Vacate Default | YES — facts showing excusable neglect + meritorious defense |
| T.R. 65 Preliminary Injunction | YES — facts showing irreparable harm |
| Motion to Compel Discovery | YES (for meet-and-confer certificate) |
| Motion to Continue under T.R. 53.5 | OPTIONAL — required when facts outside the record are relied on |

## Composition

- `in-statewide-format` for T.R. 5(E) format + T.R. 10 caption
- `in-marion` / `in-lake` / `in-county-courts` for venue
- `in-pro-se` for self-represented signature block
- `in-draft-motion` for the motion the declaration supports
- `in-fact-check` to verify every factual statement before
  signing (perjury risk under IC 35-44.1-2-1)

## References

- `references/declaration-template.md` — full scaffolded
  declaration
- `references/affidavit-template.md` — notarized-form affidavit
  template
- `references/exhibit-foundation.md` — foundation language by
  document type
- `references/perjury-statute.md` — IC 35-44.1-2-1 text

**NOT LEGAL ADVICE.** Generated content is a drafting aid; verify
against current rules and case law before filing.
