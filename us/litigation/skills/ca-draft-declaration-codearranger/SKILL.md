---
name: ca-draft-declaration-codearranger
title: Draft a California Declaration
description: Use this skill when the user asks to draft a declaration for a California court filing. Triggers include "draft a declaration", "Code Civ. Proc. § 2015.5 declaration", "declaration in support", "declaration of defendant", "declaration of plaintiff", "witness declaration", "affidavit California" (the skill redirects to the declaration form — California uses declarations under penalty of perjury per CCP § 2015.5 in place of notarized affidavits for most filings), "declaration with exhibits". Scaffolds a declaration with numbered paragraphs, the CCP § 2015.5 penalty-of-perjury attestation, date and place of execution, signature block, and optional exhibit cover pages. Composes with `ca-statewide-format` (always), `ca-lasc` / `ca-sfsc` / `ca-county-courts` (court-specific), and `ca-pro-se` (if the declarant is pro se).
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/ca-court-docs/skills/ca-draft-declaration
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Draft a California Declaration

Scaffold a declaration that complies with CCP § 2015.5, CRC
2.111, and California evidence rules. The declaration should
be ready to fill in, sign, and file in support of a motion
or other filing.

## What this skill produces

A declaration with:

1. **Caption** (court header, parties, case number, document
   title: "DECLARATION OF [NAME] IN SUPPORT OF [MOTION
   TITLE]")
2. **Numbered paragraphs** of substantive content in the
   first person
3. **Penalty-of-perjury attestation** (CCP § 2015.5) at the
   close of the body, stating the place of execution
4. **Date and place of execution**
5. **Signature block**: full name + role
6. **Exhibit List** (if exhibits are attached)
7. **Exhibit cover pages** (labeled by letter: Exhibit A,
   Exhibit B, ...)

## Declarations vs. affidavits in California

**California uses "declarations" for most court filings.**
CCP § 2015.5 provides that a declaration under penalty of
perjury subscribed in the form specified in the statute has
the same force and effect as a sworn affidavit. A notarized
affidavit is only required in a narrow set of circumstances
(some probate filings, some federal forms). When in doubt
in California state court, use the declaration form.

The CCP § 2015.5 form:

> "I declare (or certify, verify, or state) under penalty of
> perjury under the laws of the State of California that the
> foregoing is true and correct."

**California adds the "place of execution" requirement.**
Unlike federal declarations (28 USC § 1746), CCP § 2015.5
requires that the declarant state the **place** (city and
state) where the declaration was signed. A declaration
missing the place is technically defective and subject to
objection.

## Inputs to ask the user

- **Caption**: court / county / parties / case number
- **Declarant name and role**: who is signing? (party,
  witness, expert, counsel, etc.)
- **Supporting motion**: what motion or filing does this
  declaration support? (incorporated in the document title)
- **Personal-knowledge facts**: what facts does the
  declarant have personal knowledge of?
- **Exhibits**: list of documents to be attached; assigned
  letter labels (Exhibit A, B, C, ...)

## Anatomy of a California declaration

### Caption (top of page)

Per CRC 2.111 — attorney / pro se info in upper left;
case information in upper right. See `ca-statewide-format`
for the full caption format. The document title appears below
the caption:

```
        DECLARATION OF JANE DOE IN SUPPORT OF
   DEFENDANT'S MOTION TO COMPEL FURTHER RESPONSES TO
     REQUESTS FOR PRODUCTION, SET ONE, UNDER CCP § 2031.310
```

### Numbered paragraphs

Each paragraph contains **one factual point**. Number with
bold Arabic numerals:

```
1.  Identity. I am the Defendant in the above-captioned
    action. I make this Declaration in support of my
    Motion to Compel Further Responses to Requests for
    Production, Set One, under CCP § 2031.310.

2.  Personal knowledge. Except where otherwise stated,
    the facts set forth in this Declaration are within my
    personal knowledge, and if called as a witness I could
    and would testify competently to those facts.

3.  Service of Requests for Production. On April 1, 2025,
    I served Requests for Production, Set One, Nos. 1–8,
    on Plaintiff's counsel via electronic service. A true
    and correct copy of those Requests is attached as
    Exhibit A.

4.  Plaintiff's Responses. On May 1, 2025, I received
    Plaintiff's Responses to my Requests for Production.
    Plaintiff interposed boilerplate objections to Requests
    Nos. 3, 5, and 6 and produced no responsive documents.
    A true and correct copy of Plaintiff's Responses is
    attached as Exhibit B.

5.  Meet-and-confer letter. On May 10, 2025, I sent
    Plaintiff's counsel a meet-and-confer letter under CCP
    §§ 2031.310(b) identifying the deficiencies in
    Plaintiff's responses and requesting supplementation.
    A true and correct copy of that letter is attached as
    Exhibit C.

6.  Telephone conference. On May 15, 2025, I spoke with
    Plaintiff's counsel by telephone for approximately 20
    minutes. We were unable to resolve the disputes
    regarding Requests Nos. 3, 5, and 6.

7.  Plaintiff's failure to supplement. As of the date of
    this Declaration, Plaintiff has not served supplemental
    responses or produced any documents responsive to
    Requests Nos. 3, 5, or 6.

8.  Prejudice from non-production. Without the documents
    requested in Requests Nos. 3, 5, and 6, I cannot
    evaluate whether Plaintiff has standing to bring this
    action or whether the alleged account exists.
```

### Penalty-of-perjury attestation (CCP § 2015.5)

The attestation must appear at the **close of the
declaration body**, before the signature:

```
I declare under penalty of perjury under the laws of the
State of California that the foregoing is true and correct.
```

This is the **mandatory language** under CCP § 2015.5.
Variations such as "I hereby declare" or "The above is true
and correct to the best of my knowledge" are **insufficient**
— they omit the explicit "under the laws of the State of
California" language that § 2015.5 requires for the
declaration to be valid in California state court proceedings.

### Date and place of execution

```
Executed on _______________, 20__, at [City], California.
```

Or, if executed outside California:

```
Executed on _______________, 20__, at [City], [State].
```

When executed outside California, the declaration remains
valid under CCP § 2015.5(b) if it states the facts "are
certified or declared to be true under penalty of perjury
under the laws of the State of California." The declarant
need not be physically in California.

### Signature block

```
_________________________________________
JANE DOE
Defendant, In Pro Per
[Address]
[Phone]
[Email]
```

For counsel:

```
_________________________________________
JANE DOE
[State Bar No. XXXXXX]
Attorney for Defendant [Client Name]
```

## Personal knowledge requirement

**Cal. Evid. Code § 702**: A witness may not testify to a
fact without evidence that the witness has personal
knowledge of that fact. Declarations are testimonial
evidence; the same rule applies.

At the top of the body, include a personal-knowledge
paragraph:

```
2.  Personal knowledge. Except where otherwise stated,
    the facts set forth in this Declaration are within
    my personal knowledge, and if called as a witness I
    could and would testify competently to those facts.
```

If the declarant is relying on documents or records rather
than first-hand observation, say so in the paragraph:

```
9.  Review of records. The dates and dollar amounts
    stated in paragraphs 5–7 are derived from my review
    of [source — account statements, correspondence, etc.],
    which I personally reviewed on [date]. True and correct
    copies are attached as Exhibits D and E.
```

## Opinion testimony limit

**Cal. Evid. Code § 800**: A lay witness may offer an
opinion only if it is: (1) rationally based on the
witness's perception, and (2) helpful to a clear
understanding of the testimony or the determination of a
fact in issue.

Keep declarant opinions limited to lay perceptions (e.g.,
"I observed that the caller identified herself as a
'Velocity' agent"). Avoid legal conclusions ("Plaintiff
violated the FDCPA") — those belong in the motion, not the
declaration.

## Hearsay traps in declarations

Declarations must avoid inadmissible hearsay (Cal. Evid.
Code § 1200). Common traps:

| Trap | Fix |
|---|---|
| "I was told by [third party] that..." | Have the third party sign their own declaration; or establish a hearsay exception |
| "According to the contract, ..." | Authenticate the contract as an exhibit; testify that the attached exhibit is a true copy |
| "Records show that..." | Lay business-record foundation (Evid. Code §§ 1270–1272) or authenticate personally |
| Quoting a letter without attaching it | Attach the letter as an exhibit; authenticate in the body |

## Exhibits

California convention uses **letter** labels (Exhibit A, B,
C, ...) — unlike Oregon (which uses numbers). Each exhibit:

- Is **authenticated in the declaration paragraph**
  introducing it: "A true and correct copy of [document] is
  attached hereto as Exhibit [A]."
- Has a **cover page** ("EXHIBIT A" centered in bold; short
  italic caption below)
- Appears in order at the end of the declaration after the
  signature block
- Is listed on an **Exhibit List** page between the
  signature block and the first exhibit cover page

```
                         EXHIBIT LIST

Exhibit A:   Defendant's Requests for Production, Set One,
             dated April 1, 2025

Exhibit B:   Plaintiff's Responses to Requests for
             Production, Set One, dated May 1, 2025

Exhibit C:   Defendant's meet-and-confer letter, dated
             May 10, 2025
```

See `ca-statewide-format/references/exhibit-handling.md` for
the full exhibit-handling guide.

## Declarations vs. motions — drawing the line

Declarations contain **sworn facts**. Motions contain
**argument**.

A common mistake: argument disguised as fact.

Wrong (in the declaration):

> Plaintiff is clearly a debt buyer that doesn't have proper
> chain of title and is trying to mislead the Court.

This is argument. It belongs in the Memorandum, not the
declaration.

Right (in the declaration):

> 7.  Plaintiff's corporate filing. Based on my review of
>     the California Secretary of State's business entity
>     search (Exhibit D), Plaintiff [Name] is registered as
>     a Delaware limited liability company with its principal
>     place of business listed as [City]. Plaintiff's
>     Complaint alleges it "acquired" my account through
>     an "assignment" but Plaintiff has produced no
>     assignment agreement in response to Requests for
>     Production.

The facts are sworn; the characterization ("trying to
mislead") is omitted. The Memorandum argues based on the
sworn facts.

## Cal. Evid. Code § 1271 — business records

For declarations supporting **business records** under Cal.
Evid. Code § 1271 (the state analog to FRE 803(6)), the
declarant should be a custodian or qualified witness
attesting that:

1. The record was made in the regular course of a business
2. It was the regular course of that business to make
   such records
3. The record was made at or near the time of the acts or
   events it records
4. The sources of information and method of preparation
   were trustworthy

For a debt-buyer plaintiff's declaration attempting to
authenticate the original creditor's records, this foundation
typically fails because the debt buyer's custodian did not
work for the original creditor when the records were made.
See `ca-consumer-debt/references/evidence-debt-buyer.md` for
foundational challenges.

## Scenario-specific sample components

### Motion to compel — declarant is moving party

Paragraphs should cover (in order):
- Identity and role (¶ 1)
- Personal knowledge statement (¶ 2)
- Service of discovery requests (¶ 3)
- Fact of responses (¶ 4)
- Each substantive objection and the meet-and-confer effort
  (¶¶ 5–7)
- Current status — no supplementation (¶ 8)
- Prejudice / need (¶ 9)
- Fee calculation (if requesting sanctions) (¶ 10)

### Opposition to demurrer — declarant is opposing party

Rare for demurrer oppositions (which turn on the face of the
pleading), but useful when the opposing party wants to
include facts not in the complaint. Paragraphs:
- Identity (¶ 1)
- Facts supporting each cause of action challenged by the
  demurrer (¶¶ 3+), demonstrating they are pleadable with
  particularity

### Summary judgment opposition — declarant creates triable issue

The SJ declaration is critical: it must create a **genuine
triable issue** of material fact (CCP § 437c(p)). Each
disputed fact in the Separate Statement of Disputed Facts
should be supported by a specific declaration paragraph and
exhibit.

Format:

```
5.  Account ownership. I reviewed the complaint. Plaintiff
    alleges it "acquired" my account (Complaint ¶ 6), but
    Plaintiff produced no assignment agreement, bill of sale,
    or forward-flow agreement in response to Requests for
    Production, Set One, Nos. 3, 5, and 6. (Exhibit B.)
    I am unable to verify that Plaintiff owns the account it
    claims.
```

This paragraph creates a triable issue of fact on standing.

## Layered composition

This skill ALWAYS composes with:

- **`ca-statewide-format`** — caption, format, line numbers,
  signature block, exhibit conventions

It typically composes with:

- **`ca-pro-se`** — for pro se declarants; omit Bar No.;
  "In Pro Per" in signature block
- **`ca-draft-motion`** — the declaration usually accompanies
  a motion
- **`ca-lasc` / `ca-sfsc` / `ca-county-courts`** — the court
  header in the caption reflects the venue

## Quality checks

Before filing:

- **`ca-quality-check`** — format pass (CRC 2.100–2.119)
- **`ca-fact-check`** — verifies that the declaration's
  facts are consistent with the motion and any exhibits

## Common pitfalls

| Pitfall | Consequence |
|---|---|
| Missing "under the laws of the State of California" in attestation | Declaration invalid under CCP § 2015.5 |
| Missing place of execution | Technically defective; subject to objection |
| Argument mixed in with facts | Subject to motion to strike; weakens both motion and declaration |
| Legal conclusions | Inadmissible opinion; opposing counsel will object |
| Facts beyond personal knowledge without foundation | Cal. Evid. Code § 702 objection |
| Numbered exhibits (1, 2, 3) | Wrong convention for California state court (use letters: A, B, C) |
| No exhibit list | Disorganized record; judge can't navigate |
| Attestation at the top rather than at the close | § 2015.5 requires attestation to follow the facts, not precede them |

## Cross-references

- `ca-statewide-format/references/exhibit-handling.md` —
  exhibit conventions
- `ca-pro-se` — pro-se drafting framework and pro se signature block
- `ca-draft-motion` — companion motion
- `ca-law-references/references/evidence-rules.md` —
  Cal. Evid. Code references

**NOT LEGAL ADVICE.** Generated content is a drafting aid;
verify against current rules and case law before filing.
