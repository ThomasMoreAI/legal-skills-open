---
name: form-1099-sa
title: Form 1099-SA — Distributions From an HSA, Archer MSA, or Medicare Advantage MSA
description: 'Use this skill when an individual taxpayer has RECEIVED a Form 1099-SA from the custodian of their HSA, Archer MSA, or Medicare Advantage MSA after taking distributions during the tax year and needs to report those distributions on Form 8889 (HSA) or Form 8853 (Archer / MA MSA). Triggers on phrases like "received Form 1099-SA", "HSA distribution tax form", "HSA reimbursement reporting", "non-qualified HSA distribution", "1099-SA distribution code 2", "what to do with 1099-SA", "report HSA withdrawal on taxes", or any request to interpret the boxes on a received 1099-SA. Do NOT use for: HSA contribution reporting (those go on Form 5498-SA from the custodian and Form 8889 Part I — use form-5498-sa / form-8889); Form 8889 Part I contribution computation in isolation (use form-8889); the calculation on Form 8889 Part II without a received 1099-SA (Form 8889 is the recipient-side calculation; this skill is specifically about reading and acting on the 1099-SA source document); 1099-SA
  filing by HSA custodians (issuer side — out of scope; this skill is for recipients).'
author: jupid-tax
author_url: https://github.com/jupid-tax/jupid-skills/tree/main/forms/form-1099-sa
license: MIT
version: 0.1.2
execution_mode: open
jurisdiction: us
practice: tax
language: en
sources:
- title: Archer and ma msa
  path: references/archer-and-ma-msa.md
- title: Box by box
  path: references/box-by-box.md
- title: Common mistakes
  path: references/common-mistakes.md
- title: Distribution codes
  path: references/distribution-codes.md
- title: Qualified medical expenses
  path: references/qualified-medical-expenses.md
---

# Form 1099-SA — Distributions From an HSA, Archer MSA, or Medicare Advantage MSA

This skill helps a taxpayer who has received a Form 1099-SA in the mail (or as a downloadable PDF from their HSA custodian) interpret the boxes, classify each distribution as qualified or non-qualified, compute the taxable portion and any 20% additional tax, and report the result on Form 8889 (HSA) or Form 8853 (Archer / MA MSA).

The custodian must furnish Form 1099-SA by **January 31** of the year following the distribution year (next business day when January 31 falls on a weekend; Pub. 1099, part M). The recipient keeps Copy B with their records; it is not attached to the return. The actual tax reporting happens on Form 8889 Part II (HSA) or Form 8853 Section A Part II / Section B (Archer MSA / MA MSA).

**Form revision.** Verified against Form 1099-SA (Rev. April 2025), the 2025 Instructions for Forms 1099-SA and 5498-SA (Mar 21, 2025), and the 2025 Form 8889 / Instructions (Nov 25, 2025). The Instructions (Rev. December 2026) keep the April 2025 Form 1099-SA for 2026 distributions furnished in early 2027. Re-check https://www.irs.gov/forms-pubs/about-form-1099-sa before use.

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
- The user asks about HSA contribution limits or eligibility → use the [`form-8889`](../form-8889/SKILL.md) skill, Part I
- The user is the HSA custodian filing 1099-SAs to the IRS for their account holders → out of scope; this skill is recipient-side only
- The user has a Health FSA or HRA distribution → those are NOT reported on Form 1099-SA; they're reported through the employer's Form W-2 and cafeteria plan reporting
- The user has an "MSA" but means a **Medical Savings Account** that isn't an Archer MSA or Medicare Advantage MSA → the term is sometimes used loosely; verify the account type from the 1099-SA Box 5 indicator

If the user describes a "withdrawal" but hasn't received any 1099-SA: ask whether the HSA custodian has issued a year-end tax document. If the HSA had any distributions, a 1099-SA must be furnished by January 31 (next business day if a weekend). A repaid mistaken distribution and a direct trustee-to-trustee transfer are not reported on Form 1099-SA.

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
5. **User's date of birth.** Determines the 20% additional tax exception: the 20% does not apply to distributions made after the account beneficiary turns 65 (IRC §223(f)(4)(C)), dies, or becomes disabled (§223(f)(4)(B)). In the year the user turns 65, ASK which distributions were made before the birthday.
6. **Disability status** at the time of distribution. Disability distributions (Code 3) are taxable to the extent not used for qualified medical expenses, but the 20% penalty does NOT apply (IRC §223(f)(4)(B)).
7. **Account holder's date of death and the user's relationship** (spouse, other individual, or estate) if Box 4 is filled or the code is 4 or 6. Determines which return reports the FMV and for which year.
8. **Whether the user has multiple HSAs.** Each custodian issues a separate 1099-SA. The user may need to aggregate distributions across all HSAs on a single Form 8889. Ask: "Do you have HSAs with more than one custodian, and if so, did each issue a 1099-SA?"

---

## Workflow

Execute these steps in order. Don't skip ahead even if the user pushes you to.

### Step 1 — Confirm the 1099-SA is for an HSA, Archer MSA, or MA MSA

Read Box 5 of the 1099-SA. The box has three checkboxes — one will be marked:
- **HSA** → recipient files Form 8889 Part II
- **Archer MSA** → recipient files Form 8853 Section A, Part II (lines 6a–9b)
- **Medicare Advantage MSA** → recipient files Form 8853 Section B (lines 10–13b)

The downstream form differs significantly by account type. This skill primarily covers the HSA case (most common); see [`references/archer-and-ma-msa.md`](./references/archer-and-ma-msa.md) for the Archer MSA / MA MSA branches.

### Step 2 — Classify the distribution code (Box 3)

Look up Box 3 in [`references/distribution-codes.md`](./references/distribution-codes.md). The six codes:

| Code | Meaning (2025 Instructions for Forms 1099-SA and 5498-SA, Box 3) | Tax treatment |
|------|---------|---------------|
| 1 | Normal distribution (also used for a spouse beneficiary after the year of death) | Taxable on non-qualified portion + 20% unless after 65, death, or disability |
| 2 | Excess contributions | Excess + earnings withdrawn by the due date incl. extensions go on Form 8889 Line 14b; Box 2 earnings are other income for the year received |
| 3 | Disability | Taxable on non-qualified portion; **no 20% penalty** |
| 4 | Death distribution other than code 6 (any payment in the year of death; payments to the estate later) | FMV at death (Box 4) is income to the beneficiary for the year of death, or on the decedent's final return if the estate is the beneficiary |
| 5 | Prohibited transaction | Account stops being an HSA as of January 1 of that year; FMV taxable, generally + 20% |
| 6 | Death distribution after the year of death to a nonspouse beneficiary (not an estate) | FMV at death is income for the year of death (amend if not reported); earnings after death (Box 1 − Box 4) taxable in year received |

The agent's path through Form 8889 Part II depends on this code.

### Step 3 — Gather qualified medical expenses (QME)

Ask the user (with a tight question): "Of the $[Box 1] distributed from your HSA in [tax year], how much went to qualified medical expenses? Examples of QME: doctor visits, prescription drugs, dental, vision, mental health therapy, hospital bills, qualified long-term care insurance premiums, COBRA premiums, Medicare premiums (Parts B/D, but NOT Medigap)."

Get a single dollar amount. If the user says "most of it" or "around $3,000", push for an exact number — they should have receipts or a year-end summary from the HSA portal. The IRS expects substantiation (receipts retained for at least 3 years per IRC §6501).

If the user can't quantify, suggest they pull the HSA portal's "Distribution by category" report — most custodians provide this.

### Step 4 — Compute taxable distribution amount (Form 8889 Lines 14a–16)

```
Line 14a = Total distributions (Box 1 from 1099-SA, summed across all of the user's HSA 1099-SAs)
Line 14b = Rollovers to another HSA + excess contributions (and earnings) withdrawn by the due date incl. extensions
Line 14c = Line 14a − Line 14b
Line 15  = Qualified medical expenses paid using HSA distributions (the QME number from Step 3)
Line 16  = Line 14c − Line 15, not less than 0   (taxable; → Schedule 1, Line 8f)
```

A rollover is completed within 60 days, and an HSA can receive only one rollover contribution in a 1-year period (IRC §223(f)(5); 2025 Instructions for Form 8889, "Rollovers"). Direct trustee-to-trustee transfers never appear on Form 1099-SA or Line 14a.

### Step 5 — Compute 20% additional tax (Form 8889 Line 17a/17b)

The 20% additional tax applies to Line 16 **unless an exception applies** to the distribution (IRC §223(f)(4)):

- Made after the account beneficiary turned **age 65** (§223(f)(4)(C)); distributions before the 65th birthday in the same year are not covered
- Made after the account beneficiary became **disabled** (within meaning of IRC §72(m)(7)) (§223(f)(4)(B))
- Made after the account beneficiary **died** (§223(f)(4)(B))

If an exception applies to any part of Line 16, check Line 17a and enter on Line 17b 20% of only the part with no exception.

Line 17b flows to **Schedule 2 Line 17c → Form 1040 Line 23**.

### Step 6 — Handle special codes (2, 4, 5, 6)

- **Code 2 (excess contributions)**: If the excess and its earnings were withdrawn by the due date of the return including extensions, put both on Form 8889 Lines 14a and 14b, report Box 2 earnings as "Other income" (Schedule 1, Line 8z) for the year received, and the excess is not entered on Form 5329 (2025 Instructions for Form 5329, Line 47; IRC §223(f)(3)). If the excess came out after that date, the 6% tax applied for each year it stayed in ([`../form-5329/SKILL.md`](../form-5329/SKILL.md), Part VII) and the withdrawal is not a Line 14b amount.
- **Code 4 / Code 6 (death, non-spouse beneficiary or estate)**: The account stopped being an HSA on the date of death (IRC §223(f)(8)(B)). A beneficiary other than the estate writes "Death of HSA account beneficiary" across the top of their Form 8889, skips Part I, enters the FMV at the date of death (Box 4) on Line 14a, and on Line 15 the decedent's qualified medical expenses incurred before death that the beneficiary paid within 1 year after death. This income belongs to the **year of death**, even when the money arrives later (Code 6). Earnings after death (Box 1 − Box 4) are other income in the year received. No 20% tax. If the estate is the beneficiary, the FMV goes on the decedent's final return (2025 Instructions for Form 8889, "Death of Account Beneficiary").
- **Code 5 (prohibited transaction)**: The account stops being an HSA as of January 1 of the year of the transaction; its FMV on that date goes on Line 14a and is generally subject to the 20% tax (2025 Instructions for Form 8889, "Deemed Distributions From HSAs"). Rare; usually self-dealing or pledging the HSA as collateral. Refer the user to a tax pro.
- **Spouse beneficiary**: The HSA is treated as the surviving spouse's own HSA (IRC §223(f)(8)(A)); there is no taxable event at death. Later distributions to the spouse are coded 1 and reported on the spouse's own Form 8889.

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
- **Form 5329** — only if an excess contribution stayed in the HSA past the due date of the return (6% tax, Part VII); not for an excess withdrawn on time
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
| 2 | Earnings on excess contributions | Earnings on excess contributions withdrawn by the due date of the return; included in Box 1; Box 3 should be Code 2. Other income for the year received. |
| 3 | Distribution code | 1, 2, 3, 4, 5, or 6. See [`references/distribution-codes.md`](./references/distribution-codes.md). |
| 4 | FMV on date of death | Filled when the account holder died. For a non-spouse beneficiary in a later year (Code 6), reduced by the decedent's qualified medical expenses paid from the HSA within 1 year after death. |
| 5 | Account type | HSA / Archer MSA / Medicare Advantage MSA — determines which downstream form (8889 vs. 8853). |

### Form 8889 Part II (HSA distributions, 2025 form)

| Line | Field | Source |
|------|-------|--------|
| 14a | Total distributions | Box 1 (sum across all HSA 1099-SAs); FMV at death for a non-spouse beneficiary |
| 14b | Rollovers to another HSA + excess contributions and earnings withdrawn by the due date incl. extensions | Custodian records / Code 2 forms |
| 14c | Line 14a − Line 14b | Computed |
| 15 | Qualified medical expenses paid using HSA distributions | User-supplied QME total |
| 16 | Taxable HSA distributions (Line 14c − Line 15, not less than 0) | Computed; flows to Schedule 1 Line 8f |
| 17a | Checkbox: an exception applies to some or all of Line 16 | After 65 / disabled / died |
| 17b | Additional 20% tax | 20% of the part of Line 16 with no exception |

(Line 16 flows to Schedule 1 Line 8f → Form 1040 Line 8 → AGI. Line 17b flows to Schedule 2 Line 17c → Form 1040 Line 23.)

For Archer MSA or Medicare Advantage MSA, the analogous Form 8853 computation uses similar logic with different line numbers and destinations (Schedule 1 Line 8e; Schedule 2 Lines 17e / 17f) — see [`references/archer-and-ma-msa.md`](./references/archer-and-ma-msa.md).

---

## Validation

Before declaring the form ready, run these checks. Surface anything that fails — don't silently fix.

### Math checks

- [ ] Line 14a = sum of Box 1 from all received HSA 1099-SAs (non-spouse beneficiary: FMV at death)
- [ ] Line 14b = rollovers + timely withdrawn excess contributions and earnings only (never QME)
- [ ] Line 14c = Line 14a − Line 14b
- [ ] Line 16 = Line 14c − Line 15, not less than 0 (the taxable portion that flows to Schedule 1 Line 8f)
- [ ] Line 17b = 20% of the part of Line 16 with no exception
- [ ] If multiple 1099-SAs received, each Box 3 code is handled per its rules (a Code 2 mixed with Code 1 distributions across separate 1099-SAs is allowed)

### Sanity checks

Surface a warning, do not block, if any of these are true:

- [ ] Line 16 > 0 AND distribution made before age 65 AND no disability/death exception → 20% penalty applies; user should be aware
- [ ] User claims 100% of distribution as QME → ask for confirmation, especially if Box 1 is large (>$5K). The IRS may scrutinize.
- [ ] User has receipts for less than 100% of claimed QME → urge user to assemble receipts before filing
- [ ] Distribution code is 5 (prohibited transaction) → account ceased to be an HSA on January 1; FMV taxable, generally + 20%; refer to a tax pro
- [ ] Distribution code is 6 → income belongs to the year of death; check whether the beneficiary reported the Box 4 amount on that year's return
- [ ] Box 2 > 0 (excess contribution earnings) → Code 2 should be in Box 3; verify alignment
- [ ] User has multiple HSA 1099-SAs but only computed QME for one → confirm aggregation across all accounts
- [ ] Code 1 distribution but the user reports the funds were used to reimburse expenses from prior years → this is allowed (no time limit on QME reimbursement under IRS Notice 2004-50, Q&A 39), but the receipts must be from after the HSA was established

### Cross-form checks

- [ ] If Line 16 > 0, ensure Schedule 1 Line 8f picks up the taxable distribution
- [ ] If Line 17b > 0, ensure Schedule 2 Line 17c picks up the 20% additional tax
- [ ] Form 8889 must be filed even if all distributions were QME (Line 16 = 0) — the form serves as documentation
- [ ] If the user also made HSA contributions, ensure Form 8889 Part I is also completed (use the [`form-8889`](../form-8889/SKILL.md) skill for Part I)

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
14b. Rollovers + timely withdrawn excess (+ earnings): $X,XXX
14c. Subtract 14b from 14a:                            $X,XXX
15.  Qualified medical expenses paid using HSA:       $X,XXX
16.  Taxable HSA distributions (14c − 15):             $X,XXX  → Schedule 1 Line 8f
17a. Exception box (if any):                           none | after 65 | disabled | died
17b. Additional 20% tax (20% of non-excepted Line 16): $X,XXX  → Schedule 2 Line 17c

## Required attachments
- [x] Form 8889 (full form, Parts I + II + III as applicable)
- [ ] Form 5329 — only if an excess contribution remained after the due date of the return
- [ ] Form 8853 — N/A unless Archer / MA MSA

## Validation summary
- Math: all checks passed | <list failures>
- Sanity: <list any warnings raised>
- Next steps:
  - Schedule 1 Line 8f: $X,XXX (taxable HSA distribution → AGI)
  - Schedule 2 Line 17c: $X,XXX (additional 20% tax → Form 1040 Line 23)
  - Receipts retention: keep QME receipts for at least 3 years from filing date

## Sources cited in this draft
- IRS Form 1099-SA (Rev. April 2025)
- IRS Instructions for Forms 1099-SA and 5498-SA (2025, or Rev. December 2026 for 2026 distributions)
- IRS Form 8889, Rev. <YYYY>
- IRS Publication 502 (qualified medical expenses)
- IRS Publication 969 (HSAs and other tax-favored health plans)
- IRC §223(f) (HSA distributions), §223(f)(4)(B)–(C) (20% additional tax exceptions)
```

The draft is **not** the final filed form. The user still has to enter it into Form 1040 e-file software or paper Form 8889. The deliverable's value is that every line is computed and traceable.

---

## References

Loaded on demand based on what the user's situation needs.

- [`references/box-by-box.md`](./references/box-by-box.md) — Complete table of every 1099-SA box with rules and edge cases
- [`references/distribution-codes.md`](./references/distribution-codes.md) — All six distribution codes (1, 2, 3, 4, 5, 6) with tax treatment per code
- Sibling skills: [`form-8889`](../form-8889/SKILL.md) (full Form 8889), [`form-5498-sa`](../form-5498-sa/SKILL.md) (contribution side), [`form-5329`](../form-5329/SKILL.md) (6% excess-contribution tax)
- [`references/qualified-medical-expenses.md`](./references/qualified-medical-expenses.md) — What counts as QME under IRC §213(d) and Pub 502; gray-area items
- [`references/archer-and-ma-msa.md`](./references/archer-and-ma-msa.md) — Differences for Archer MSA and Medicare Advantage MSA distributions (Form 8853 Part II)
- [`references/common-mistakes.md`](./references/common-mistakes.md) — Top audit-trip mistakes with citations and fixes
- [`filing.md`](./filing.md) — Browser-automation playbook for filing Form 8889 (with 1099-SA inputs) alongside Form 1040

## Examples

End-to-end worked Form 8889 Part II drafts. Use these as patterns when the user's situation is similar.

- [`examples/all-qualified-3200.md`](./examples/all-qualified-3200.md) — Standard case: $3,200 distribution, all qualified medical, no taxable amount, no penalty
- [`examples/partial-non-qualified-5k.md`](./examples/partial-non-qualified-5k.md) — Mixed: $5,000 distributed, $4,000 qualified, $1,000 non-qualified, taxable + 20% penalty (under age 65)
- [`examples/inherited-hsa-death-code-4.md`](./examples/inherited-hsa-death-code-4.md) — Non-spouse beneficiary inherits HSA; FMV at death (Box 4) less pre-death medical bills paid within 1 year is ordinary income; no 20% tax

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
- IRC §223 (HSAs) — §223(d) account requirements, §223(e)(2) account termination, §223(f) distributions, §223(f)(3) excess returned by due date, §223(f)(4) 20% additional tax + exceptions, §223(f)(5) rollover, §223(f)(8)(A) spouse / (B) other beneficiaries
- [Pub. 1099 (General Instructions for Certain Information Returns)](https://www.irs.gov/publications/p1099) — furnishing dates for Form 1099-SA
- IRC §220 (Archer MSAs) — §220(f) distributions
- IRC §138 (Medicare Advantage MSA) — §138(c) distributions
- IRC §213(d) — definition of medical care
- IRC §6501 — IRS audit window (3 years general rule for receipts retention)

## Disclaimer

This skill encodes procedural guidance based on publicly available IRS forms and publications. It is not tax advice. It does not establish a CPA-client relationship. The agent invoking this skill should remind the user, when producing a draft, that the output is a starting point and that complex situations (inherited HSAs, prohibited transactions, multi-year reimbursement claims) warrant a licensed tax professional's review.
