---
name: ny-submit-order
title: Post-Hearing Order Submission in New York
description: Use after a hearing or motion decision when the prevailing party needs to submit a proposed order for signature. Triggers include 'NY post-hearing order submission', 'settle order on notice', '22 NYCRR § 202.48 60-day rule', 'submit a proposed order to chambers in NY', 'counter- order', 'serve a settle-order packet', 'NY order on submission', 'how do I get the Justice to sign my order', 'transmittal letter to chambers'. Implements the 22 NYCRR § 202.48 settle-order procedure with the 60-day clock plus the 10-day notice + 5-day counter-order window. Handles the chambers transmittal letter and the post-signature NYSCEF Notice of Entry.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/ny-court-docs/skills/ny-submit-order
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Post-Hearing Order Submission in New York

> **NOT LEGAL ADVICE.** The 60-day settle-order clock is
> jurisdictional in many courts. Missing it forfeits the
> right to settle the order.

## When this skill applies

After the Justice rules on a motion, one of three things
happens:

1. **Short-form Decision and Order** — the Justice writes
   the decision on the proposed order itself; no further
   submission needed. The order is filed by chambers via
   NYSCEF.
2. **Decision directs settle order** — "Settle order on
   notice" or "Settle order on submission"; the prevailing
   party must submit a proposed order within 60 days.
3. **Decision is self-executing** — no order needed (rare).

This skill covers #2: the **settle-order procedure**.

## The 22 NYCRR § 202.48 framework

```
Day 0:    Justice issues Decision directing settle order
Day 0–60: Prevailing party drafts proposed order
Day X:    Prevailing party serves proposed order on opposing
          party (≥10 days before submission)
Day X+5:  Opposing party may serve a counter-order
Day X+10: Prevailing party submits proposed order to chambers,
          attaching counter-order (if served) and a cover
          letter discussing differences
Day ≤60:  Prevailing party submits to chambers; missing this
          deadline is fatal absent extension
```

### On notice v. on submission

| Direction | Procedure |
|-----------|-----------|
| **"Settle order on notice"** | Serve proposed order on opposing party 10 days before submission; opposing may serve counter-order within 5 days |
| **"Settle order on submission"** | Submit proposed order to chambers without separate service (NYSCEF service of the filing is sufficient) |

## Proposed-order content

The proposed order should **track the Justice's decision
exactly**:

- Use the decision's exact language for the relief granted
- Do not add relief not granted in the decision
- Do not omit relief granted in the decision
- Use the decretal "ORDERED that..." format

See `ny-draft-order` for the proposed-order template.

## Chambers transmittal letter

When submitting on notice (or on submission), include a
cover letter:

```
[Date]

Hon. [Justice Name], J.S.C.
Supreme Court, [County]
[Courthouse Address]

Re: [Caption], Index No. [#####/YYYY]
    Submission of Proposed Order

Dear Justice [Name]:

Enclosed for the Court's signature is a proposed Decision
and Order in the above-captioned matter, submitted on
notice pursuant to 22 NYCRR § 202.48 and the Court's
Decision dated [DATE]. The proposed order tracks the
Court's directives in [GRANTING / DENYING] Defendant's
motion under CPLR [SECTION].

[If on notice and opposing served a counter-order:]
A copy of the proposed order was served on Plaintiff's
counsel on [DATE] (attached as Exhibit 1). Plaintiff's
counsel served a counter-order on [DATE] (attached as
Exhibit 2). The principal difference between the two
proposed orders is [DESCRIBE]. The undersigned
respectfully submits that this Court's proposed order
should be entered because [REASON].

Respectfully submitted,

[Print Name]
Self-Represented Defendant
[Phone, email]
```

## Counter-order procedure

If the opposing party served a counter-order:

1. **Review both proposed orders** side by side
2. **Identify differences** — language, scope, conditions
3. **Submit both to chambers** with a cover letter
   discussing the differences
4. Chambers selects (or modifies) one of the proposed orders
   and enters it

## Post-signature: Notice of Entry

After the Justice signs and the order is entered (filed on
NYSCEF by the clerk):

1. **NYSCEF notifies all parties** automatically
2. **Prevailing party files a Notice of Entry** (CPLR
   5513(a)) — triggers the 30-day appeal clock
3. **Notice of Entry**:

```
SUPREME COURT OF THE STATE OF NEW YORK
COUNTY OF [COUNTY]
----------------------------------------- X
[CAPTION]                                  Index No. [#####/YYYY]
                                           Hon. [JUSTICE]
                          [Plaintiff(s),]
                                           NOTICE OF ENTRY
            -against-
                          [Defendant(s).]
----------------------------------------- X

PLEASE TAKE NOTICE that the annexed is a true copy of the
Decision and Order of the Hon. [Justice], dated [DATE], and
filed and entered in the Office of the Clerk of the Court
on [DATE].

Dated: [...]
[Signature]
```

Filed via NYSCEF as document type "Notice of Entry."

## Common errors

| Error | Consequence |
|-------|------------|
| Missing 60-day deadline | Right to settle order deemed abandoned (CPLR analog — *Funk v. Barry*, 89 NY2d 364) |
| Submitting order that goes beyond the decision | Justice rejects or modifies |
| Failing to serve 10 days before submission (on notice) | Justice may refuse to sign |
| Submitting without cover letter discussing counter-order differences | Justice can sign either; favorable side often loses |
| Failing to file Notice of Entry | 30-day appeal clock may run anyway upon NYSCEF entry |

## Composition with other ny- skills

- `ny-draft-order` — proposed-order content
- `ny-hearings` — post-hearing follow-up
- `ny-deadlines` — 60-day clock + appeal clock
- `ny-fact-check` — pre-submission QC
