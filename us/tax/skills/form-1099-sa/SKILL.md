---
name: form-1099-sa
title: Form 1099-SA — Distributions From an HSA, Archer MSA, or Medicare Advantage MSA
description: 'Use this skill when an individual taxpayer has RECEIVED a Form 1099-SA from the custodian of their HSA, Archer MSA, or Medicare Advantage MSA after taking distributions during the tax year and needs to report those distributions on Form 8889 (HSA) or Form 8853 (Archer / MA MSA). Triggers on phrases like "received Form 1099-SA", "HSA distribution tax form", "HSA reimbursement reporting", "non-qualified HSA distribution", "1099-SA distribution code 2", "what to do with 1099-SA", "report HSA withdrawal on taxes", or any request to interpret the boxes on a received 1099-SA. Do NOT use for: HSA contribution reporting (those go on Form 5498-SA from the custodian and Form 8889 Part I — different skill); Form 8889 Part I contribution computation in isolation (different skill); the calculation on Form 8889 Part II without a received 1099-SA (Form 8889 is the recipient-side calculation; this skill is specifically about reading and acting on the 1099-SA source document); 1099-SA filing
  by HSA custodians (issuer side — out of scope; this skill is for recipients).'
author: jupid-tax
author_url: https://github.com/jupid-tax/jupid-skills/tree/main/forms/form-1099-sa
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: tax
language: en
---

# Form 1099-SA — Distributions From an HSA, Archer MSA, or Medicare Advantage MSA

This skill helps a taxpayer who has received a Form 1099-SA in the mail (or as a downloadable PDF from their HSA custodian) interpret the boxes, classify each distribution as qualified or non-qualified, compute the taxable portion and any 20% additional tax, and report the result on Form 8889 (HSA) or Form 8853 (Archer / MA MSA).

The custodian sends Form 1099-SA by **January 31** of the year following the distribution year. The recipient files the recipient copy as supporting documentation (not attached to the return itself; e-filed returns retain it electronically). The actual tax reporting happens on Form 8889 Part II or Form 8853 Part II.

The agent's job: read the boxes, classify the distribution code, ask the user about qualified medical expenses, and produce a Form 8889 Part II (or Form 8853 Part II) draft.

---

## When to invoke

Engage this skill when **any** of the following is true:

- The user mentions receiving a Form 1099-SA (in the mail, by email PDF, or as a tax-document download from Fidelity / HealthEquity / Lively / Optum / WEX / etc.)
- The user took a withdrawal from their HSA during the tax year (even if they used the HSA debit card at a pharmacy — every swipe is a distribution)
- The user asks "what's a 1099-SA", "how do I report my HSA distribution", "I withdrew from my HSA, what now"
- The user is in the middle of completing Form 8889 and has reached Part II (Distributions)

Do **not** engage this skill when:

- The user wants to report HSA *contributions*, not distributions → that's **Form 5498-SA** received from the custodian and Form 8889 Part I (separate skill)
- The user asks about HSA contribution limits or eligibility → use the (forthcoming) `form-8889` skill, Part I
- The user is the HSA custodian filing 1099-SAs to the IRS for their account holders → out of scope; this skill is recipient-side only
- The user has a Health FSA or HRA distribution → those are NOT reported on Form 1099-SA; they're reported through the employer's Form W-2 and cafeteria plan reporting
- The user has an "MSA" but means a **Medical Savings Account** that isn't an Archer MSA or Medicare Advantage MSA → the term is sometimes used loosely; verify the account type from the 1099-SA Box 5 indicator

If the user describes a "withdrawal" but hasn't received any 1099-SA: ask whether the HSA custodian has issued a year-end tax document. If the HSA had any distributions, a 1099-SA must be issued by January 31.

---

## Prerequisites

Before producing anything, the agent must have these inputs. If any are missing, **ask for them explicitly** and stop until you get an answer.

1. **Tax year** the 1099-SA covers. The form's top-right corner lists the tax year. For tax year 2025 distributions, the 1099-SA arrives by January 31, 2026.
2. **Recipient information** from the 1099-SA: name, SSN/TIN, address. These should match the user's Form 1040 — if they don't, the user must contact the custodian to correct (Form W-9 update).
3. **All boxes from the 1099-SA**:
   - **Box 1** — Gross distribution (total dollar amount distributed)
   - **Box 2** — Earnings on excess contributions (if any; usually $0)
   - **Box 3** — Distribution code (1, 2, 3, 4, 5, or 6 — see [`references/distribution-codes.md`](./references/distribution-codes.md))
   - **Box 4** — FMV on date of death (only if the account holder died during the year)
   - **Box 5** — Account type indicator: **HSA**, **Archer MSA**, or **Medicare Advantage MSA**
4. **Qualified medical expenses paid from the HSA during the year.** Ask the user: "How much of the $X distribution went to qualified medical expenses (per IRS Pub 502 — doctor visits, prescriptions, dental, vision, mental health, etc.)? Get a precise number, not 'most of it'. The remainder is taxable."
5. **User's age at year-end.** Determines the 20% additional tax exception (the 20% penalty does not apply if the user is age 65 or older at the time of distribution per IRC §223(f)(4)(B), or has died, or is disabled).
6. **Disability status** at the time of distribution. Disability distributions (Code 3) are taxable to the extent not used for qualified medical expenses, but the 20% penalty does NOT apply (IRC §223(f)(4)(B)).
7. **Account holder's date of death** if the distribution code is 4 or 6 (death of account holder). Determines who receives the 1099-SA (beneficiary or estate) and how the FMV is treated.
8. **Whether the user has multiple HSAs.** Each custodian issues a separate 1099-SA. The user may need to aggregate distributions across all HSAs on a single Form 8889. Ask: "Do you have HSAs with more than one custodian, and if so, did each issue a 1099-SA?"

---

## Workflow

Execute these steps in order. Don't skip ahead even if the user pushes you to.

### Step 1 — Confirm the 1099-SA is for an HSA, Archer MSA, or MA MSA

Read Box 5 of the 1099-SA. The box has three checkboxes — one will be marked:
- **HSA** → recipient files Form 8889 Part II
- **Archer MSA** → recipient files Form 8853 Part II Section A
- **Medicare Advantage MSA** → recipient files Form 8853 Part II Section B

The downstream form differs significantly by account type. This skill primarily covers the HSA case (most common); see [`references/archer-and-ma-msa.md`](./references/archer-and-ma-msa.md) for the Archer MSA / MA MSA branches.

### Step 2 — Classify the distribution code (Box 3)

Look up Box 3 in [`references/distribution-codes.md`](./references/distribution-codes.md). The six codes:

| Code | Meaning | Tax treatment |
|------|---------|---------------|
| 1 | Normal distribution | Taxable on non-qualified portion + 20% penalty if under 65 |
| 2 | Excess contribution + earnings | Earnings (Box 2) taxable + 6% excise on the excess (Form 5329) |
| 3 | Disability | Taxable on non-qualified portion; **no 20% penalty** |
| 4 | Death of account holder (paid to non-spouse beneficiary or estate) | Taxable to beneficiary; FMV in Box 4 |
| 5 | Prohibited transaction | Whole account distributed; taxable + penalty |
| 6 | Death — paid to spouse beneficiary | Spouse can keep the HSA as their own; not taxable to them |

The agent's path through Form 8889 Part II depends on this code.

### Step 3 — Gather qualified medical expenses (QME)

Ask the user (with a tight question): "Of the $[Box 1] distributed from your HSA in [tax year], how much went to qualified medical expenses? Examples of QME: doctor visits, prescription drugs, dental, vision, mental health therapy, hospital bills, qualified long-term care insurance premiums, COBRA premiums, Medicare premiums (Parts B/D, but NOT Medigap)."

Get a single dollar amount. If the user says "most of it" or "around $3,000", push for an exact number — they should have receipts or a year-end summary from the HSA portal. The IRS expects substantiation (receipts retained for at least 3 years per IRC §6501).

If the user can't quantify, suggest they pull the HSA portal's "Distribution by category" report — most custodians provide this.

### Step 4 — Compute taxable distribution amount (Form 8889 Line 14a / 14b)

```
Line 14a = Total distributions (Box 1 from 1099-SA, summed across all 1099-SAs if multiple HSAs)
Line 14b = Distributions used for qualified medical expenses (the QME number from Step 3)
Line 14c = Line 14a − Line 14b   (taxable portion)
```

If the user took a distribution and rolled it into another HSA (within 60 days, once per 12 months — IRC §223(f)(5)), the rollover does NOT count as a distribution. Subtract rollover amount from Line 14a per the form's instructions, with a notation.

Note: Form 8889 Line 14c is the **non-QME** distribution amount, NOT the taxable amount yet — Line 16 will become the actual taxable amount on Form 1040.

### Step 5 — Compute 20% additional tax (Form 8889 Line 17a/17b)

The 20% additional tax applies on Line 14c **unless an exception applies** (IRC §223(f)(4)):

- Account holder reached **age 65** (at any point during the year of distribution)
- Account holder is **disabled** (within meaning of IRC §72(m)(7))
- Account holder **died** during the year (the deceased is treated as disabled for this purpose)

If any exception applies, Line 17b = $0.

If no exception, Line 17b = Line 14c × 0.20.

Line 17b flows to **Schedule 2 Line 17c → Form 1040 Line 23**.

### Step 6 — Handle special codes (2, 4, 5, 6)

- **Code 2 (excess contributions)**: Box 2 (earnings on excess) is taxable as ordinary income. The excess contribution itself was reported separately on Form 5329 in the contribution year. Do not double-count.
- **Code 4 (death — non-spouse beneficiary)**: The beneficiary or estate receives the distribution. The full Box 1 amount is taxable as ordinary income to the recipient; the QME exclusion is only available for medical expenses paid by the deceased *before* death. Box 4 FMV is the basis for any later sale.
- **Code 5 (prohibited transaction)**: The entire HSA is treated as distributed and lost — fully taxable + 20% penalty. Rare; usually self-dealing or pledging the HSA as collateral. Refer the user to a tax pro.
- **Code 6 (death — spouse beneficiary)**: The HSA passes to the surviving spouse as their own HSA (IRC §223(f)(8)(B)). No tax consequence at distribution time; the spouse continues filing Form 8889 for the account in future years. The 1099-SA in this case is essentially informational.

### Step 7 — Run validation checks

See **Validation** below.

### Step 8 — Produce the deliverable

See **Output format** below. The deliverable is a Form 8889 Part II draft (or Form 8853 Part II for Archer / MA MSA) that the user can transcribe to e-file software or paper.

### Step 9 — Hand off downstream

State the next forms the user will need:

- **Form 8889 Part II** filed with Form 1040 (HSA case)
- **Form 8853 Part II** filed with Form 1040 (Archer MSA or MA MSA case)
- **Schedule 2 Line 17c** — picks up the 20% additional tax (if applicable)
- **Form 1040 Line 23** — picks up Schedule 2 total
- **Form 5329** — only if Code 2 (to handle the 6% excess contribution excise on the contribution side, not the distribution side)
- **Receipts retention** — keep QME receipts for at least 3 years (IRS audit window) + indefinitely if used to support a future "shoebox" reimbursement

### Step 10 — File the return (optional)

If the agent has browser-automation tooling and the user explicitly authorizes filing, follow [`filing.md`](./filing.md). The 1099-SA itself is not filed — only the resulting Form 8889 / 8853 attaches to Form 1040.

---

## Line-by-line guidance

For the full reference, load [`references/box-by-box.md`](./references/box-by-box.md). High-level rules below.

### 1099-SA boxes

| Box | Field | What it means |
|-----|-------|----------------|
| (Payer) | Custodian info | The HSA / MSA custodian (Fidelity, HealthEquity, etc.). Informational only. |
| (Recipient) | Account holder info | The user's name, SSN, address. Should match Form 1040. |
| 1 | Gross distribution | Total $ withdrawn. Includes debit card swipes, ATM, checks, online transfers, claim reimbursements. |
| 2 | Earnings on excess contributions | Only populated if Box 3 = Code 2. The earnings on a returned excess contribution. Taxable as ordinary income. |
| 3 | Distribution code | 1, 2, 3, 4, 5, or 6. See [`references/distribution-codes.md`](./references/distribution-codes.md). |
| 4 | FMV on date of death | Only if the account holder died during the year. Used by the beneficiary or estate. |
| 5 | Account type | HSA / Archer MSA / Medicare Advantage MSA — determines which downstream form (8889 vs. 8853). |

### Form 8889 Part II (HSA distributions)

| Line | Field | Source |
|------|-------|--------|
| 14a | Total distributions | Box 1 (sum across all HSA 1099-SAs) |
| 14b | Distributions for QME | User-supplied QME total |
| 14c | Line 14a − Line 14b | Computed (non-QME portion) |
| 15 | Qualified medical expenses you paid using HSA distributions | Same as 14b in most cases |
| 16 | Taxable HSA distributions (Line 14a − Line 15) | Computed; flows to Schedule 1 Line 8f |
| 17a | Reason for exception (if applicable) | Age 65+ / disabled / died |
| 17b | Additional 20% tax | Line 16 × 0.20 (or $0 if exception) |

(Line 16 flows to Schedule 1 Line 8f → Form 1040 Line 8 → AGI. Line 17b flows to Schedule 2 Line 17c → Form 1040 Line 23.)

For Archer MSA or Medicare Advantage MSA, the analogous Form 8853 Part II computation uses similar logic with different line numbers — see [`references/archer-and-ma-msa.md`](./references/archer-and-ma-msa.md).

---

## Validation

Before declaring the form ready, run these checks. Surface anything that fails — don't silently fix.

### Math checks

- [ ] Line 14a = sum of Box 1 from all received HSA 1099-SAs
- [ ] Line 14c = Line 14a − Line 14b (and is ≥ 0 — never negative; if QME exceeds distribution, 14b is capped at 14a)
- [ ] Line 15 = Line 14b (in the standard case where QME paid = QME claimed)
- [ ] Line 16 = Line 14a − Line 15 (the taxable portion that flows to Schedule 1 Line 8f)
- [ ] Line 17b = Line 16 × 0.20 IF no exception applies; else $0
- [ ] If multiple 1099-SAs received, each Box 3 code is handled per its rules (a Code 2 mixed with Code 1 distributions across separate 1099-SAs is allowed)

### Sanity checks

Surface a warning, do not block, if any of these are true:

- [ ] Line 14c > 0 AND user is under age 65 AND no disability/death exception → 20% penalty applies; user should be aware
- [ ] User claims 100% of distribution as QME → ask for confirmation, especially if Box 1 is large (>$5K). The IRS may scrutinize.
- [ ] User has receipts for less than 100% of claimed QME → urge user to assemble receipts before filing
- [ ] Distribution code is 5 (prohibited transaction) → entire HSA is taxable + 20% penalty + the account is essentially terminated; refer to a tax pro
- [ ] Box 2 > 0 (excess contribution earnings) → Code 2 should be in Box 3; verify alignment
- [ ] User has multiple HSA 1099-SAs but only computed QME for one → confirm aggregation across all accounts
- [ ] Code 1 distribution but the user reports the funds were used to reimburse expenses from prior years → this is allowed (no time limit on QME reimbursement under IRS Notice 2004-50, Q&A 39), but the receipts must be from after the HSA was established

### Cross-form checks

- [ ] If Line 16 > 0, ensure Schedule 1 Line 8f picks up the taxable distribution
- [ ] If Line 17b > 0, ensure Schedule 2 Line 17c picks up the 20% additional tax
- [ ] Form 8889 must be filed even if all distributions were QME (Line 16 = 0) — the form serves as documentation
- [ ] If the user also made HSA contributions, ensure Form 8889 Part I is also completed (use the (forthcoming) `form-8889` skill for Part I)

---

## Output format

The agent's deliverable is a **filled draft** of Form 8889 Part II (or Form 8853 Part II) the user can transcribe to a paper form or paste into tax software. Format:

```markdown
# Form 8889 Part II — DRAFT for tax year YYYY

## 1099-SA(s) received

| Custodian | Box 1 (Gross) | Box 2 (Excess earn) | Box 3 (Code) | Box 4 (FMV death) | Box 5 (Type) |
|-----------|---------------|---------------------|--------------|-------------------|--------------|
| <name>    | $X,XXX        | $0                  | 1            | $0                | HSA          |
| ...       | ...           | ...                 | ...          | ...               | ...          |
| **Total** | $X,XXX        |                     |              |                   |              |

## Qualified medical expenses (QME) breakdown

| Category                     | Amount  | Receipts? |
|------------------------------|---------|-----------|
| Doctor visits / co-pays      | $X,XXX  | Yes       |
| Prescription drugs           | $X,XXX  | Yes       |
| Dental                       | $XXX    | Yes       |
| Vision                       | $XXX    | Yes       |
| Mental health                | $XXX    | Yes       |
| Other (specify)              | $XXX    | Yes       |
| **Total QME**                | $X,XXX  |           |

## Form 8889 Part II — line-by-line

14a. Total distributions:                              $X,XXX
14b. Distributions used for QME:                       $X,XXX
14c. Subtract 14b from 14a (non-QME portion):         $X,XXX
15.  Qualified medical expenses paid using HSA:       $X,XXX  (= 14b in standard case)
16.  Taxable HSA distributions (14a − 15):             $X,XXX  → Schedule 1 Line 8f
17a. Exception reason (if any):                        none | age 65+ | disabled | died
17b. Additional 20% tax (16 × 0.20):                   $X,XXX  → Schedule 2 Line 17c
                                                       (or $0 if exception applies)

## Required attachments
- [x] Form 8889 (full form, Parts I + II + III as applicable)
- [ ] Form 5329 — only if Code 2 (excess contributions)
- [ ] Form 8853 — N/A unless Archer / MA MSA

## Validation summary
- Math: all checks passed | <list failures>
- Sanity: <list any warnings raised>
- Next steps:
  - Schedule 1 Line 8f: $X,XXX (taxable HSA distribution → AGI)
  - Schedule 2 Line 17c: $X,XXX (additional 20% tax → Form 1040 Line 23)
  - Receipts retention: keep QME receipts for at least 3 years from filing date

## Sources cited in this draft
- IRS Form 1099-SA, Rev. <YYYY>
- IRS Instructions for Forms 1099-SA and 5498-SA, Rev. <YYYY>
- IRS Form 8889, Rev. <YYYY>
- IRS Publication 502 (qualified medical expenses)
- IRS Publication 969 (HSAs and other tax-favored health plans)
- IRC §223(f) (HSA distributions), §223(f)(4) (20% additional tax + exceptions)
```

The draft is **not** the final filed form. The user still has to enter it into Form 1040 e-file software or paper Form 8889. The deliverable's value is that every line is computed and traceable.

---

## References

Loaded on demand based on what the user's situation needs.

- [`references/box-by-box.md`](./references/box-by-box.md) — Complete table of every 1099-SA box with rules and edge cases
- [`references/distribution-codes.md`](./references/distribution-codes.md) — All six distribution codes (1, 2, 3, 4, 5, 6) with tax treatment per code
- [`references/qualified-medical-expenses.md`](./references/qualified-medical-expenses.md) — What counts as QME under IRC §213(d) and Pub 502; gray-area items
- [`references/archer-and-ma-msa.md`](./references/archer-and-ma-msa.md) — Differences for Archer MSA and Medicare Advantage MSA distributions (Form 8853 Part II)
- [`references/common-mistakes.md`](./references/common-mistakes.md) — Top audit-trip mistakes with citations and fixes
- [`filing.md`](./filing.md) — Browser-automation playbook for filing Form 8889 (with 1099-SA inputs) alongside Form 1040

## Examples

End-to-end worked Form 8889 Part II drafts. Use these as patterns when the user's situation is similar.

- [`examples/all-qualified-3200.md`](./examples/all-qualified-3200.md) — Standard case: $3,200 distribution, all qualified medical, no taxable amount, no penalty
- [`examples/partial-non-qualified-5k.md`](./examples/partial-non-qualified-5k.md) — Mixed: $5,000 distributed, $4,000 qualified, $1,000 non-qualified, taxable + 20% penalty (under age 65)
- [`examples/inherited-hsa-death-code-4.md`](./examples/inherited-hsa-death-code-4.md) — Non-spouse beneficiary inherits HSA; full Box 1 taxable as ordinary income; FMV in Box 4

## Sources

Authoritative sources used by this skill. Always re-verify these against the IRS site for the tax year being filed — the IRS revises the form and the Pub 969 dollar amounts each cycle.

- [Form 1099-SA](https://www.irs.gov/pub/irs-pdf/f1099sa.pdf) — the form itself
- [Instructions for Forms 1099-SA and 5498-SA](https://www.irs.gov/pub/irs-pdf/i1099sa.pdf) — combined custodian and recipient guidance
- [About Form 1099-SA](https://www.irs.gov/forms-pubs/about-form-1099-sa) — IRS landing page
- [Form 8889](https://www.irs.gov/pub/irs-pdf/f8889.pdf) — HSA recipient-side form
- [Instructions for Form 8889](https://www.irs.gov/pub/irs-pdf/i8889.pdf)
- [Form 8853](https://www.irs.gov/pub/irs-pdf/f8853.pdf) — Archer MSA / MA MSA / LTC contracts
- [Publication 502](https://www.irs.gov/publications/p502) — Medical and Dental Expenses (defines QME)
- [Publication 969](https://www.irs.gov/publications/p969) — HSAs and Other Tax-Favored Health Plans (HSA + Archer MSA + MA MSA + Health FSA + HRA)
- [Notice 2004-50](https://www.irs.gov/pub/irs-drop/n-04-50.pdf) — Q&A on HSA rules including timing of QME reimbursement (Q&A 39: no time limit)
- IRC §223 (HSAs) — §223(d) account requirements, §223(f) distributions, §223(f)(4) 20% additional tax + exceptions, §223(f)(5) rollover, §223(f)(8) death of account holder
- IRC §220 (Archer MSAs) — §220(f) distributions
- IRC §138 (Medicare Advantage MSA) — §138(c) distributions
- IRC §213(d) — definition of medical care
- IRC §6501 — IRS audit window (3 years general rule for receipts retention)

## Disclaimer

This skill encodes procedural guidance based on publicly available IRS forms and publications. It is not tax advice. It does not establish a CPA-client relationship. The agent invoking this skill should remind the user, when producing a draft, that the output is a starting point and that complex situations (inherited HSAs, prohibited transactions, multi-year reimbursement claims) warrant a licensed tax professional's review.
