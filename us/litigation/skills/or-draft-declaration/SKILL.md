---
name: or-draft-declaration
title: Draft an Oregon Declaration
description: Use this skill when the user asks to draft a declaration for an Oregon court filing. Triggers include "draft a declaration", "declaration in support", "declaration of defendant", "declaration of plaintiff", "witness declaration", "affidavit" (Oregon uses declarations under penalty of perjury per ORCP 1 E in place of notarized affidavits for most filings), and "declaration with exhibits". Scaffolds a declaration with numbered paragraphs, verification clause (ORCP 1 E), signature block, and optional exhibit cover pages. Composes with `or-statewide-format` (always), `or-multcc` / `or-wccc` / `or-county-courts` (court-specific), and `or-pro-se` (if the declarant is pro se).
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/or-court-docs/skills/or-draft-declaration
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Draft an Oregon Declaration

Scaffold a new declaration that complies with UTCR 2.010 and
ORCP 1 E. The declaration should be ready to fill in, sign,
and file in support of a motion or other filing.

> **NOT LEGAL ADVICE.** This skill scaffolds a court document
> as a drafting aid. The user — not the skill — is the
> declarant, chooses what facts to swear to, and signs the
> declaration. Verify every rule, deadline, and citation against
> current law before filing. Pair with substantive review by
> counsel where stakes warrant.

## What this skill produces

A declaration with:

1. **Caption** (court header, parties, case number, document
   title: "DECLARATION OF [NAME] IN SUPPORT OF [MOTION
   TITLE]")
2. **Salutation**: "I, [Full Name], declare under penalty of
   perjury under the laws of the State of Oregon that the
   following is true and correct:"
3. **Numbered paragraphs** of substantive content
4. **Verification clause** (ORCP 1 E form): "I declare under
   penalty of perjury under the laws of the State of Oregon
   that the foregoing is true and correct."
5. **Date and place of execution** ("DATED this ... Executed
   at [city], Oregon")
6. **Signature block**
7. **Exhibit List** (if exhibits)
8. **Exhibit cover pages**

## Inputs to ask the user

- **Caption**: court / county / parties / case number
- **Declarant name and role**: who is signing? (party,
  witness, expert, etc.)
- **Supporting motion**: what motion does this declaration
  support? (the document title incorporates this)
- **Personal-knowledge facts**: what facts is the declarant
  swearing to?
- **Exhibits**: list of documents that go with the
  declaration

## Anatomy of a declaration

### Salutation (top of body)

```
I, John Doe, declare under penalty of perjury under the laws
of the State of Oregon that the following is true and
correct:
```

This is the ORCP 1 E form. Some practitioners prefer the
shorter:

```
I, John Doe, hereby declare under penalty of perjury the
following:
```

Either is acceptable. The ORCP 1 E form is cleaner.

### Numbered paragraphs

Each paragraph contains **one factual point**. Number with bold
Arabic numerals followed by a period and tab:

```
1.  Identity. I am the Defendant in the above-captioned
    action. I am 42 years old, an Oregon resident, and I make
    this Declaration in support of Defendant's Motion to
    Compel under ORCP 46 A.

2.  Personal knowledge. The facts stated in this Declaration
    are based on my personal knowledge, except where I
    explicitly state otherwise.

3.  Service of First Requests for Production. On April 1,
    2025, I served First Requests for Production Nos. 1–6 on
    Plaintiff's counsel via File and Serve. A true and
    correct copy of the Requests is attached as Exhibit 1.

4.  Plaintiff's Responses. On May 1, 2025, I received
    Plaintiff's Responses via File and Serve. Plaintiff
    objected on grounds of "relevance, burden, and
    possession" and did not produce documents responsive to
    Requests Nos. 3, 5, and 6. A true and correct copy of
    Plaintiff's Responses is attached as Exhibit 2.

5.  Meet-and-confer letter. On May 10, 2025, I sent
    Plaintiff's counsel a meet-and-confer letter identifying
    the objections and requesting supplementation. A true
    and correct copy is attached as Exhibit 3.

6.  Phone conference. On May 14, 2025, I spoke with
    Plaintiff's counsel by phone for approximately 30
    minutes. I memorialized the call by email the same day;
    a true and correct copy of that email is attached as
    Exhibit 4.

7.  Plaintiff's position. As of the date of this Declaration,
    Plaintiff has not supplemented as to Requests Nos. 3, 5,
    and 6. Plaintiff maintains its objections.

8.  Damages from non-production. Without these documents, I
    cannot evaluate whether Plaintiff has standing to bring
    this action.
```

### Verification clause (end of body, before signature)

```
I declare under penalty of perjury under the laws of the
State of Oregon that the foregoing is true and correct.
```

### Date and place

```
DATED this ____ day of ___________, 20__.

Executed at Portland, Oregon.
```

If executed outside Oregon, change to:

```
Executed at [City, State].
```

(28 USC § 1746 form requires identifying the state.)

### Signature block

```
______________________________________
JOHN DOE
Defendant, pro se
[Address]
[Phone]
[Email]
```

## ORCP 1 E — declarations in lieu of affidavits

**ORCP 1 E**: A "declaration under penalty of perjury" in the
prescribed form may be used in lieu of a notarized affidavit.
The acceptable form:

> "I hereby declare that the above statement is true to the
> best of my knowledge and belief, and that I understand it
> is made for use as evidence in court and is subject to
> penalty for perjury."

OR the shorter:

> "I declare under penalty of perjury under the laws of the
> State of Oregon that the foregoing is true and correct."

Either form is accepted statewide. Most pro se filers use the
shorter form.

## OEC 602 — Personal knowledge

Under OEC 602, the declarant must have **personal knowledge**
of every stated fact, OR must specify the basis for belief.

If the declarant is testifying about facts they did not
personally observe, say so:

```
9.  Reliance on records. The amounts and dates in
    paragraphs 3–6 are derived from my review of [source —
    bank statements, invoices, etc.]. I personally
    reviewed these records on [date]; true and correct
    copies are attached as Exhibits 5 and 6.
```

A declaration that includes facts beyond the declarant's
personal knowledge, without specifying the basis, is subject
to objection under OEC 602 and may be struck on motion under
ORCP 47 D (for SJ practice) or its analog.

## Exhibits

For declarations with exhibits, follow these conventions:

- **Number them** (Exhibit 1, Exhibit 2, ...) — Oregon
  convention
- **Reference each exhibit by number** in the paragraph
  introducing it
- **Authenticate** each exhibit: "A true and correct copy is
  attached as Exhibit [N]"
- **List all exhibits** on an Exhibit List page after the
  signature block
- **Each exhibit gets a cover page** ("EXHIBIT [N]" centered,
  with a short italic caption)

See `or-statewide-format/references/exhibit-handling.md` for
the full exhibit-handling guide.

## Declarations vs. motions — drawing the line

Declarations contain **sworn facts**. Motions contain
**argument**.

A common mistake: putting argument in the declaration.

❌ Wrong (in the declaration):

> Plaintiff is clearly a debt buyer that doesn't have proper
> chain of title and is trying to mislead the Court.

This is argument. It belongs in the motion, not the
declaration.

✅ Right (in the declaration):

> 4. Plaintiff's status. Based on my review of the public
> filings of [Plaintiff entity name] with the Oregon
> Secretary of State (Exhibit 5), Plaintiff is a debt-buying
> entity that purchases charged-off accounts. Plaintiff's
> Complaint alleges it "acquired" my account through an
> "assignment" but has not produced any document evidencing
> that assignment in response to Requests for Production.

The facts are sworn; the characterization ("clearly trying to
mislead") is omitted. The motion can argue the
characterization based on these facts.

## Declarations and the OEC 803(6) business-records pattern

For declarations supporting **business records** under OEC
803(6) (the analog to FRE 803(6)), the declarant should be a
"custodian or other qualified witness" attesting to:

1. The record was made at or near the time of the events
2. The record was made by, or from information transmitted
   by, a person with knowledge
3. The record was kept in the course of regularly conducted
   business activity
4. It was the regular practice of the business to make such
   records

This is the foundation pattern for OEC 902(11) certified
business records.

For a debt-buyer plaintiff's declaration attempting to
authenticate the original creditor's records, the declaration
typically fails because the declarant is the debt buyer's
custodian, not the original creditor's. See `or-consumer-debt/
references/evidence-debt-buyer.md` for the foundational
challenges.

## Layered composition

This skill ALWAYS composes with:

- **`or-statewide-format`** — caption, format, signature block,
  exhibits

It typically composes with:

- **`or-pro-se`** — for pro se declarants
- **`or-draft-motion`** — the declaration usually accompanies
  a motion
- **`or-multcc` / `or-wccc` / `or-county-courts`** — the
  court header reflects the venue

## Quality checks

Before filing:

- **`or-quality-check`** — format pass
- **`or-fact-check`** — verifies that the declaration's facts
  are consistent with the motion and any exhibits

## Common pitfalls

| Pitfall | Consequence |
|---------|-------------|
| Missing the perjury clause | Declaration is invalid; may need to re-execute |
| Argument mixed in with facts | Subject to objection; weakens both motion and decl |
| Facts beyond personal knowledge without basis | OEC 602 objection |
| Wrong jurisdiction in salutation ("California" / "Washington") | Invalid form |
| Lettered exhibits (A, B, C) | Wrong convention for Oregon |
| Static date in the body | Use fill-in blanks for handwritten date |
| No exhibit list | Disorganized record; judge can't navigate |

## Cross-references

- `or-statewide-format/references/templates/declaration.md` —
  full template
- `or-statewide-format/references/exhibit-handling.md` —
  exhibit conventions
- `or-pro-se/references/pro-se-drafting-framework.md` — drafting
  principles
- `or-draft-motion` — companion motion
- `or-law-references/references/evidence-rules.md` — OEC
  references
