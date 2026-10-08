---
name: or-draft-motion-codearranger
title: Draft an Oregon Motion + Supporting Memorandum
description: Use this skill when the user asks to draft a motion for an Oregon circuit court. Triggers include "draft a motion", "write a motion to compel", "I need to file a motion to dismiss", "motion for summary judgment", "motion to vacate", "motion for reconsideration", "motion for default", "motion to strike", "new motion". Scaffolds a motion with supporting memorandum that complies with UTCR 2.010, statewide motion practice, and the pro-se drafting framework for concise, fact-forward drafting. Composes with `or-statewide-format` (always), `or-multcc` / `or-wccc` / `or-county-courts` (court-specific), `or-pro-se` (if pro se), and `or-discovery` / `or-post-judgment` depending on the motion type.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/or-court-docs/skills/or-draft-motion
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Draft an Oregon Motion + Supporting Memorandum

Scaffold a motion and companion memorandum that complies with
UTCR 2.010, ORCP / UTCR statewide motion practice, and the
pro-se drafting framework.

> **NOT LEGAL ADVICE.** This skill scaffolds a court document
> as a drafting aid. The user — not the skill — chooses the
> motion type, theory of relief, and strategy. Verify every
> rule, deadline, and citation against current law before
> filing. Pair with substantive review by counsel where stakes
> warrant.

## What this skill produces

A motion with the following sections, ready for filling in:

1. **Caption** (court header, parties, case number, document
   title)
2. **MOTION** — short, declaratory: "Pursuant to ORCP [N],
   [party] respectfully moves the Court for an order [relief]."
3. **MEMORANDUM** — sections I–VII (pro-se drafting framework):
   - I. Relief Requested
   - II. Statement of Facts
   - III. Statement of Issues
   - IV. Evidence Relied Upon
   - V. Authorities
   - VI. Argument
   - VII. Conclusion
4. **Signature block**
5. **Certificate of Service**

## Inputs to ask the user

- **Court / county**: Multnomah? Washington Co? Other?
- **Case number**: e.g., `25CV12345`
- **Caption**: Plaintiff / Defendant party names
- **Motion type**: dismiss (ORCP 21 A(?)), compel (ORCP 46),
  SJ (ORCP 47), vacate (ORCP 71), strike (ORCP 21 E), etc.
- **The procedural authority**: which ORCP / ORS / UTCR /
  SLR section is being invoked
- **The relief requested**: specifically, what should the
  court order?
- **Pro se or counsel?**: affects signature block
- **Estimated argument time**: 10, 15, 20, 30 minutes
- **Hearing mode**: in-person, WebEx, telephone (per
  assigned court's standing order)

## The pro-se drafting framework (in detail)

### I. Relief Requested (one paragraph)

What specifically the court should order. Bullet or sub-letter
the elements:

```
I.  RELIEF REQUESTED

    Defendant asks the Court to enter an order:
    (a) compelling Plaintiff to produce documents responsive
        to Requests Nos. 1–6 by [date certain];
    (b) overruling Plaintiff's objections; and
    (c) awarding Defendant reasonable expenses incurred in
        making this Motion under ORCP 46 A(4)(a).
```

### II. Statement of Facts (numbered paragraphs)

Each fact is a short sentence. Each is cited to the supporting
Declaration paragraph or Exhibit.

```
II. STATEMENT OF FACTS

    1.  Plaintiff filed the Complaint on January 14, 2025.
        (Decl. ¶ 1.)

    2.  On April 1, 2025, Defendant served First Requests
        for Production. (Decl. ¶ 2; Ex. 1.)

    3.  On May 1, 2025, Plaintiff served Responses,
        objecting on grounds of [grounds] without producing
        responsive documents. (Decl. ¶ 3; Ex. 2.)

    4.  ...
```

Keep facts to **one short sentence each**. Multi-clause
sentences in fact statements are harder for the judge to
follow.

### III. Statement of Issues (yes-or-no questions)

1–3 yes-or-no questions the court must answer to rule on the
motion:

```
III. STATEMENT OF ISSUES

     1. Whether documents proving the chain of title from
        the original creditor to a debt-buyer plaintiff are
        within ORCP 36 B(1) scope when the defendant denies
        the existence of the account.

     2. Whether Plaintiff's "possession" objection is valid
        when Plaintiff alleges it owns the account.

     3. Whether fee-shifting under ORCP 46 A(4)(a) is
        mandatory given Plaintiff's failure to produce was
        "without substantial justification".
```

Each issue should be answerable yes/no. Avoid open-ended
"whether the Court should..." formulations.

### IV. Evidence Relied Upon (list)

The supporting record:

```
IV. EVIDENCE RELIED UPON

    - Declaration of John Doe, filed herewith
    - Exhibit 1: First Requests for Production
    - Exhibit 2: Plaintiff's Responses and Objections
    - Exhibit 3: Meet-and-confer correspondence
    - Court file (Complaint, Answer)
```

### V. Authorities (list)

Rules, statutes, cases:

```
V.  AUTHORITIES

    - ORCP 36 B(1) — scope of discovery
    - ORCP 43 — requests for production
    - ORCP 46 A — motion to compel
    - ORCP 46 A(4)(a) — mandatory fee-shifting
    - Multnomah SLR 5.045 — meet-and-confer
    - Phillips v. Beaverton Aluminum Co., 314 Or App 257,
      498 P3d 814 (2021)
```

### VI. Argument (organized by issue)

Each issue gets its own subsection with a bold lead-in
heading:

```
VI. ARGUMENT

    A.  The documents are within ORCP 36 B(1) scope.

        [2–3 paragraphs. Cite the rule, cite the facts, draw
         the conclusion.]

    B.  Plaintiff's "possession" objection contradicts its
        Complaint.

        [2–3 paragraphs.]

    C.  Fee-shifting is mandatory under ORCP 46 A(4)(a).

        [2–3 paragraphs.]
```

### VII. Conclusion (one paragraph)

Restate the relief:

```
VII. CONCLUSION

     For the foregoing reasons, Defendant respectfully
     requests entry of the Proposed Order filed herewith.
```

## Motion-type quick reference

### Motion to dismiss

| Sub-rule | Use when |
|----------|----------|
| ORCP 21 A(1) | No subject-matter jurisdiction |
| ORCP 21 A(2) | No personal jurisdiction |
| ORCP 21 A(3) | Improper venue |
| ORCP 21 A(4) | Insufficient summons |
| ORCP 21 A(5) | Insufficient service |
| ORCP 21 A(6) | Not real party in interest |
| ORCP 21 A(7) | Failure to join party |
| ORCP 21 A(8) | Failure to state ultimate facts |
| ORCP 21 A(9) | Pendency of another action |
| ORCP 21 E | Motion to strike |

### Motion to compel discovery

- Authority: ORCP 46 A
- Prerequisite: meet-and-confer certification (UTCR / local
  SLR)
- Mandatory fee-shifting: ORCP 46 A(4)(a)

### Motion for summary judgment

- Authority: ORCP 47
- Timing: 60 days before trial; 20 days response; 5 days
  reply; 11 days before hearing
- Standard: no genuine issue of material fact + entitled to
  judgment as a matter of law

### Motion to vacate

- Authority: ORCP 71 B (grounds 1–6)
- Deadline: reasonable time; 1 year for grounds (1)–(3)
- Show: ground + diligence + meritorious defense + lack of
  prejudice

### Motion for reconsideration

- Authority: ORCP 64 (or analogous under recent rule
  development; verify current)
- Deadline: 10 days from judgment

### Motion for default

- Authority: ORCP 69
- For when defendant fails to answer in 30 days

### Motion for continuance

- Authority: UTCR 6.030
- Show: good cause

### Anti-SLAPP motion

- Authority: ORS 31.150
- Show: claim arises from protected expression; plaintiff
  fails to show probability of prevailing

## Oregon-specific drafting notes

### Cite the rule first in the Motion

The Oregon judge expects to see the procedural authority on
the first line of the Motion:

```
Pursuant to ORCP 46 A, Defendant moves the Court for an
order compelling Plaintiff to produce ...
```

NOT: "This Court has the power to compel..."

### Use exact ORCP subsection notation

`ORCP 21 A(8)`, not `ORCP 21(A)(8)`. Capital letters separated
by spaces, with parenthesized lower-case sub-elements.

### Oral argument designation

UTCR 5.050 requires noting whether oral argument is
requested. Format on the document title:

```
DEFENDANT'S MOTION TO COMPEL UNDER ORCP 46 A
(ORAL ARGUMENT REQUESTED — 20 MINUTES)
```

Some local SLRs require the oral-argument request in a
separate Notice of Hearing rather than the document title.
Check `or-multcc` / `or-wccc` / `or-county-courts`.

### Mandatory arbitration

If the case is in ORS 36.400 mandatory arbitration, motions
go to the **arbitrator**, not the judge. Title accordingly:

```
DEFENDANT'S MOTION TO COMPEL UNDER ORCP 46 A
(IN ARBITRATION PROCEEDING UNDER ORS 36.400)
```

### Meet-and-confer (discovery motions)

Multnomah SLR 5.045 / Washington Co SLR 5.046 / other county
SLRs require a meet-and-confer certification. Include it in
Section II (Facts) or as a separate Certification at the end.

### Page count

Target 4–6 pages for the memorandum. Anything longer should
split fact narrative into the declaration and keep the memo
tight.

## Layered composition

This skill ALWAYS composes with:

- **`or-statewide-format`** — caption, fonts, margins, footer,
  exhibits
- **The relevant court skill** — `or-multcc`, `or-wccc`, or
  `or-county-courts` — for local motion practice

It typically composes with:

- **`or-pro-se`** — pro-se drafting framework details, pro se
  signature block, service protocol
- **`or-draft-declaration`** — to draft the supporting
  declaration
- **`or-draft-order`** — to draft the proposed order
- **`or-draft-note`** — to draft the Notice of Hearing

For motion-type-specific guidance:

- **`or-discovery`** — for motions to compel
- **`or-post-judgment`** — for motions to vacate, garnishment-
  related motions
- **`or-first-30-days`** — for ORCP 21 motions in initial
  response

## Output

The skill produces a Markdown scaffold of the motion. The user
fills in:

- Specific facts (with declaration citations)
- Specific issues
- Specific argument
- Cites the user has verified

Optionally, `or-statewide-format/references/docx-generation.md`
shows how to convert the Markdown to `.docx` for filing.

## Quality checks

After scaffolding, run:

- **`or-quality-check`** — format pass (UTCR 2.010
  compliance)
- **`or-fact-check`** — citation and consistency pass

Before filing.

## Cross-references

- `or-statewide-format` — caption + UTCR 2.010
- `or-statewide-format/references/templates/motion-with-memo.md`
  — full scaffold template
- `or-pro-se/references/pro-se-drafting-framework.md` — Parker
  drafting principles
- `or-multcc` / `or-wccc` / `or-county-courts` — local
  motion practice
