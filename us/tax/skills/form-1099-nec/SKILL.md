---
name: form-1099-nec
title: Form 1099-NEC — Nonemployee Compensation
description: 'Use this skill when a US business needs to issue Form 1099-NEC to a nonemployee (contractor, freelancer, gig worker, vendor) for services, OR when a recipient receives a Form 1099-NEC and needs to report it on Schedule C / Schedule 1. Triggers on phrases like "Form 1099-NEC", "issue 1099 to contractor", "report contractor payments", "received 1099-NEC", "1099-NEC threshold", "$2,000 1099 threshold", "1099 for freelancer", "nonemployee compensation reporting", "backup withholding on 1099-NEC". Do NOT use for: W-2 employees (use payroll-tax skills, not this — different form, different rules); rent payments to a landlord (use `form-1099-misc` Box 1); royalty payments (use `form-1099-misc` Box 2); attorney settlement payments to a plaintiff or attorney fees (use `form-1099-misc` Box 10); third-party-network platform payments (use `form-1099-k` — Stripe, PayPal, Venmo, etc. issue 1099-K, not 1099-NEC); interest / dividends (use 1099-INT / 1099-DIV); cancellation-of-debt income (use
  `form-1099-c`).'
author: jupid-tax
author_url: https://github.com/jupid-tax/jupid-skills/tree/main/forms/form-1099-nec
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: tax
language: en
---

# Form 1099-NEC — Nonemployee Compensation

This skill produces an audit-grade plan for Form 1099-NEC, on either side of the form:

- **Payor side** (a business that paid contractors): determine whether a 1099-NEC is required for each payee, gather W-9 data, populate the boxes, file with the IRS, and deliver a copy to the recipient by January 31.
- **Recipient side** (a contractor who received a 1099-NEC): reconcile the form against records and report the income on Schedule C (if business) or Schedule 1 Line 8 (if a one-off, non-business gig), with Box 4 federal withholding flowing to Form 1040 Line 25c.

The 1099-NEC was reissued in 2020 (split off from 1099-MISC Box 7) and is now the canonical information return under IRC §6041 and §6041A for service payments made to non-employees. The 2026 reporting threshold is **$2,000** per payee per year, raised from $600 by OBBBA Section 112201 (verify against current IRS guidance — the IRS may issue transitional notices).

The math is mechanical. The judgment is in **(a)** classifying each payee correctly (employee vs. contractor; corporation vs. individual/partnership/SMLLC), **(b)** determining whether the threshold is met when partial payments cross years, and **(c)** routing recipient income to the correct line.

**Companion guide for end users:** [1099-NEC Guide 2026](https://jupid.com/blog/1099-nec-guide-2026) on the Jupid blog. Same rules, narrative-style explanation. Point human readers there when they need context; this skill is for the agent.

---

## When to invoke

Engage this skill when **any** of the following is true:

- The user explicitly mentions Form 1099-NEC, "1099-NEC", or "1099 NEC"
- A business owner asks "do I need to send a 1099 to my contractor / freelancer / VA / bookkeeper?"
- A business owner is preparing year-end information returns and has paid one or more individuals for services
- A recipient asks "I got a 1099-NEC, what do I do with it?"
- A recipient asks where to report nonemployee compensation income
- The user mentions the $2,000 threshold or asks whether their payment to a contractor crosses it
- The user mentions backup withholding (24%) and a missing or incorrect W-9

Do **not** engage this skill when:

- The payment is to a **W-2 employee** — that's a wage payment, reported on Form W-2 with payroll tax withholding; use payroll skills
- The payment is **rent** to a landlord — use `form-1099-misc` Box 1
- The payment is a **royalty** — use `form-1099-misc` Box 2
- The payment is **attorney fees from a settlement** to a plaintiff or **gross proceeds paid to an attorney** — use `form-1099-misc` Box 10 (special rule applies even if attorney is incorporated)
- The payment was made through a **third-party payment network** (Stripe, PayPal goods/services, Venmo business, Square) — that platform issues a **1099-K** and you do NOT also issue a 1099-NEC for the same payment (anti-double-reporting rule)
- The payment is **interest** (1099-INT), **dividends** (1099-DIV), **cancellation of debt** (1099-C), or **digital-asset broker proceeds** (1099-DA)

If the user's payee status is ambiguous (employee vs. contractor), redirect to `form-w9` and `form-ss-8` (worker-classification determination) before continuing. Misclassification penalties are substantial — IRC §3509 + §6651.

For the recipient's downstream form (Schedule C), see [`schedule-c/`](../schedule-c/SKILL.md). For the payor's pre-1099 W-9 collection workflow, see [`form-w9/`](../form-w9/SKILL.md).

---

## Prerequisites

Before producing anything, the agent must have these inputs. If any are missing, **ask for them explicitly** and stop until you get an answer.

### Payor side (issuing 1099-NECs)

1. **Payor's legal name, EIN, and address** — appears on every 1099-NEC issued.
2. **Tax year** the 1099s cover. The threshold and forms differ year-to-year.
3. **List of every payee** who received any payment for services during the year, with:
   - Payee name (legal name, not DBA, unless an SMLLC reports under a DBA EIN)
   - Payee Tax ID (SSN, ITIN, or EIN) — collected via Form W-9 *before* paying
   - Payee mailing address
   - Total gross paid in the calendar year (cash + check + ACH + Zelle direct bank-to-bank — NOT third-party-network payments, those go on 1099-K issued by the platform)
   - Whether the payee is incorporated (C-corp or S-corp = generally exempt; LLC may or may not be — depends on tax election, see W-9 Line 3)
   - Whether backup withholding applies (24% if W-9 missing or TIN doesn't match)
4. **Filing channel** — IRS FIRE, IRIS (Information Returns Intake System, free), or a third-party service (Track1099, Tax1099, QuickBooks). Required: the payor must file electronically if issuing 10+ information returns total in the year (aggregated across all 1099 types — TFA 2019).
5. **State filing requirements** — most states piggyback on the federal Combined Federal/State Filing Program (CF/SF), but some states (e.g., Pennsylvania) require separate state filing. Confirm with [`references/state-filing.md`](./references/state-filing.md) (or IRS Pub. 1220 for the CF/SF list).

### Recipient side (received a 1099-NEC)

1. **Filer's legal name and SSN/ITIN** — for Schedule C header or 1040.
2. **Form copy** — Box 1 (gross nonemployee compensation), Box 4 (federal income tax withheld), Boxes 5-7 (state income / state tax / payer state ID).
3. **Underlying activity** — was this a trade or business (regular, continuous, profit-motive — Schedule C) or a one-off gig (Schedule 1 Line 8z, "Activity not for profit" or one-off "Other earned income")?
4. **The recipient's own records** — what services were performed, what was the total billed, and does it match Box 1? Discrepancies are the most common error mode.
5. **Any business expenses** related to earning the income — only relevant if Schedule C path.

For a recipient who is also a sole proprietor / SMLLC, the income flows directly to Schedule C Line 1 along with other gross receipts. For a one-off recipient (e.g., paid honorarium for a single speaking engagement), the income flows to Schedule 1 Line 8z and is **not** subject to self-employment tax (because it's not a trade or business).

If the recipient classification (business vs. one-off) is ambiguous, ask before routing. The most common mistake: a freelancer with one client who reports on Schedule 1 Line 8 instead of Schedule C, missing the SE tax obligation and the deduction opportunity.

---

## Workflow

### Payor side workflow

#### Step 1 — Confirm the payee universe

Pull every payment made for services during the calendar year. Exclude:

- W-2 wages (those go on W-2)
- Reimbursements substantiated under an accountable plan (not reportable)
- Payments to corporations except for: medical/health-care services, attorney legal services (these are reportable on 1099-MISC Box 6 or Box 10 even if incorporated)
- Payments made via third-party payment network (Stripe, PayPal goods/services, Square, Venmo business, Cash App for Business) — the platform issues 1099-K
- Personal payments (not for the trade or business)

Net list: every individual / partnership / SMLLC paid for services in the calendar year.

#### Step 2 — Apply the threshold

For tax year 2026, issue a 1099-NEC to any non-corporate payee paid **≥ $2,000** in aggregate for services during the calendar year (OBBBA §112201, raised from $600). Verify the threshold against current IRS guidance before filing — the IRS may publish transitional rules. See [`references/threshold-rules.md`](./references/threshold-rules.md).

For tax year 2025 and prior: the threshold is **$600**.

If backup withholding was applied, issue a 1099-NEC regardless of amount (any amount of backup withholding requires the form).

#### Step 3 — Verify W-9 data for each payee crossing the threshold

For each payee that crosses the threshold:

- Confirm a current Form W-9 is on file
- Confirm payee's TIN is present (SSN or EIN)
- Confirm the legal-name / TIN combination matches IRS records (use the IRS TIN Matching service via e-Services)
- If W-9 is missing: solicit (Form W-9 second-request letter); apply backup withholding (24%) on future payments until received
- If TIN mismatch: send the IRS B-Notice (Notice 2100), request corrected W-9; apply backup withholding if the second match also fails

See [`references/backup-withholding.md`](./references/backup-withholding.md).

#### Step 4 — Populate each box on Form 1099-NEC

Per [`references/line-by-line.md`](./references/line-by-line.md):

- **Payer** block (top-left): payer's name, address, phone
- **Payer's TIN**: payer's EIN
- **Recipient's TIN**: payee's SSN or EIN from W-9
- **Recipient's name and address**: from W-9
- **Box 1**: total gross paid for services during calendar year (do not net against expenses or refunds)
- **Box 2**: payer made direct sales totaling ≥ $5,000 of consumer products to recipient for resale (rare; consumer-product direct-sales businesses)
- **Box 3**: reserved (currently unused)
- **Box 4**: federal income tax withheld (backup withholding amount, if any)
- **Boxes 5-7**: state-level reporting (state income tax withheld, state name + payer state ID, state income)

#### Step 5 — Distribute copies

Each 1099-NEC has multiple copies:

- **Copy A** — to IRS (paper or electronic via FIRE / IRIS)
- **Copy B** — to recipient (mail or e-deliver with consent)
- **Copy C** — payer's records
- **Copy 1** — to state tax department (if state requires)
- **Copy 2** — to recipient for state filing

**Recipient copy (Copy B): due January 31** following the tax year (postmarked or e-delivered).

**IRS copy (Copy A): due January 31** (same as recipient copy — note 1099-NEC is special; it's earlier than 1099-MISC's IRS deadline). Paper or electronic — same date.

If filing electronically and submitting **10 or more information returns total** across all types in the calendar year, electronic filing is **mandatory** (TFA 2019, codified at IRC §6011(e)).

#### Step 6 — File state copies

If the state isn't on the IRS Combined Federal/State Filing program, file separately with the state. Refer to the state's department of revenue. Some require electronic filing through state portals (e.g., Pennsylvania myPATH).

#### Step 7 — Hand off to filing.md

For browser-driven filing through IRS IRIS or FIRE, see [`filing.md`](./filing.md).

### Recipient side workflow

#### Step R1 — Classify the activity

Was the payment from a trade or business activity (regular, continuous, profit-motive)?

- **Yes** → Schedule C path
- **No** (one-off honorarium, occasional gig) → Schedule 1 Line 8z path

If ambiguous, ask the user. The IRS factors for "trade or business" are at IRC §162 and Reg. §1.183-2(b) (nine-factor test).

#### Step R2 — Schedule C path

The Box 1 amount becomes part of the user's gross receipts on Schedule C Line 1 (alongside other 1099s, 1099-Ks, cash, and other income). Do NOT line-item each 1099-NEC separately on the form — Line 1 is the aggregate.

The recipient's own records should match or exceed each Box 1 amount. If records are less than Box 1, investigate (the payor may have included payments that didn't reach the recipient, or there's a year-end timing difference).

Then run the [`schedule-c/`](../schedule-c/SKILL.md) skill for the rest of the return.

#### Step R3 — Schedule 1 path (one-off gig)

If the activity isn't a trade or business:

- Box 1 amount → Schedule 1 Line 8 (specific 8z if "Other earned income" applies)
- No Schedule SE (not subject to SE tax — IRC §1402(a))
- No Schedule C
- Expenses generally **not deductible** (post-TCJA, miscellaneous 2% itemized deductions suspended through 2025)

#### Step R4 — Box 4 federal withholding

If Box 4 > 0 (backup withholding was applied):

- The amount goes on Form 1040 Line 25c (Other forms — including any federal income tax withheld from a 1099)
- The recipient gets credit for the withheld amount against their total federal income tax liability

#### Step R5 — Box 5-7 state items

State income on Box 7 ties to the state return. Box 5 (state tax withheld) gets credited on the state return. Most state returns mirror the federal flow.

#### Step R6 — Validate and produce deliverable

See **Validation** below.

---

## Line-by-line guidance

For the full reference, load [`references/line-by-line.md`](./references/line-by-line.md). High-level rules below.

### Header (payer/recipient blocks)

- **Payer's name, address, phone**: top-left. Must match payer's IRS records.
- **Payer's TIN**: EIN preferred; SSN if a sole proprietor with no EIN issuing 1099s (rare).
- **Recipient's TIN**: from W-9. Truncate on Copy B (recipient copy) per Reg. §301.6109-4 — show only last 4 digits — but full TIN on Copy A (IRS copy).
- **Recipient's name and address**: legal name from W-9 Line 1; DBA (if any) from W-9 Line 2 below the legal name.
- **Account number**: optional internal payer reference; required if filing multiple 1099s for the same recipient.

### Box-by-box (the core)

| Box | Field | What goes here | What does NOT go here |
|-----|-------|----------------|------------------------|
| 1 | Nonemployee compensation | Total gross paid for services in the calendar year | Reimbursements under an accountable plan; payments via 1099-K platform; goods (not services) |
| 2 | Direct sales of consumer products ≥$5,000 | Check box if applicable (rare) | |
| 3 | (reserved) | (unused) | |
| 4 | Federal income tax withheld | Backup withholding amount (24%), if any | Voluntary withholding (no such thing on 1099-NEC) |
| 5 | State tax withheld | State income tax withheld, if any | Federal withholding (Box 4) |
| 6 | State / Payer's state no. | State 2-letter abbreviation + payer's state ID number | |
| 7 | State income | Amount of Box 1 attributable to that state | |

### Handling multi-state payees

If the payer paid the recipient who works across multiple states, complete one 1099-NEC with multi-row state breakdown in Boxes 5-7 (the form supports two state rows; for more, the payer attaches a continuation).

---

## Validation

Before declaring the form ready, run these checks. Surface anything that fails — don't silently fix.

### Math checks (payor side)

- [ ] Sum of all 1099-NECs Box 1 issued = total payments to payees ≥ threshold (with no backup withholding) + total payments to payees with any backup withholding
- [ ] Sum of all 1099-NECs Box 4 = total backup withholding remitted to IRS via Form 945
- [ ] Number of 1099-NECs filed reported on Form 1096 (paper) matches actual count

### Sanity checks (payor side)

- [ ] Any payee paid ≥ $2,000 (2026) without a W-9 on file → triggers backup withholding obligation
- [ ] Any payee with an EIN → confirm not a corporation (corporations are exempt for services unless medical/legal); use [`references/payee-classification.md`](./references/payee-classification.md)
- [ ] Any payee paid via Stripe / PayPal / Venmo business / Square → exclude (1099-K from platform)
- [ ] Any reimbursement included in Box 1 → confirm the reimbursement is NOT under an accountable plan (if accountable, exclude)
- [ ] Total information returns (1099-NEC + 1099-MISC + 1099-K + 1099-INT + 1099-DIV + W-2) ≥ 10 → e-filing mandatory

### Math checks (recipient side)

- [ ] Schedule C Line 1 ≥ sum of all 1099s received (NEC + K + MISC + others reporting receipts)
- [ ] If Box 4 > 0, Form 1040 Line 25c reflects it
- [ ] Schedule 1 Line 8 (one-off path) = Box 1 amount

### Sanity checks (recipient side)

- [ ] Recipient's records match Box 1 within ~$200 → if not, investigate timing or missing income
- [ ] Recipient's classification (business vs. one-off) confirmed → SE tax treatment depends on it
- [ ] No double-reporting: if same income also on a 1099-K (rare but happens with Stripe + direct check from same client), only count once

---

## Output format

### Payor-side deliverable: 1099-NEC issuance plan

```markdown
# Form 1099-NEC — Issuance Plan for tax year YYYY
Payer: <Legal Name> (EIN: XX-XXXXXXX)

## Payees requiring 1099-NEC

| Payee Name | TIN (last 4) | Address | Box 1 Total | Box 4 Withhold | State Boxes |
|------------|--------------|---------|-------------|----------------|-------------|
| ...        | XXX-XX-1234  | ...     | $X,XXX      | $0             | ...         |

Total 1099-NECs to issue: N
Total Box 1: $X,XXX
Total Box 4 (to remit on Form 945): $X,XXX

## Excluded (with reason)

| Payee Name | Reason for exclusion |
|------------|----------------------|
| Acme Inc.  | C-corp (services, non-medical, non-legal) — exempt |
| ...        | Paid via Stripe — covered by 1099-K |

## Filing checklist

- [ ] Recipient copies (Copy B) postmarked or e-delivered by January 31
- [ ] IRS copies (Copy A) filed by January 31 (electronic via IRIS or paper with Form 1096)
- [ ] State copies filed (if state not in CF/SF program)
- [ ] Form 945 filed if any backup withholding remitted
- [ ] Records retained for 4 years (IRC §6501(a) statute of limitations + buffer)

## Sources cited
- IRS Form 1099-NEC, Rev. <year>
- IRS Instructions for Forms 1099-MISC and 1099-NEC, Rev. <year>
- IRC §6041, §6041A, §3406 (backup withholding)
- OBBBA Section 112201 (2026 threshold raise to $2,000)
- Reg. §301.6109-4 (TIN truncation)
```

### Recipient-side deliverable: reconciliation summary

```markdown
# Form 1099-NEC — Recipient Reconciliation for tax year YYYY
Recipient: <Legal Name> (SSN: XXX-XX-XXXX)

## 1099-NEC details
Payer: <Legal Name> (EIN: XX-XXXXXXX)
Box 1 (Nonemployee compensation): $X,XXX
Box 4 (Federal tax withheld): $X,XXX
Boxes 5-7 (State): <state>: $X,XXX

## Classification: <Trade or Business | One-off gig>

## Reporting destination
- [Schedule C path]
  - Box 1 → Schedule C Line 1 (part of aggregate gross receipts: $X,XXX total)
  - Box 4 → Form 1040 Line 25c
  - Subject to SE tax via Schedule SE
- [Schedule 1 path]
  - Box 1 → Schedule 1 Line 8z ("Other earned income — <description>")
  - Box 4 → Form 1040 Line 25c
  - NOT subject to SE tax

## Reconciliation
Per recipient records: $X,XXX gross billed
Per 1099-NEC Box 1: $X,XXX
Difference: $XXX <explanation: timing, refund, etc.>

## Validation summary
- Math: passed | <list failures>
- Sanity: <warnings>
- Next steps: <Schedule C / Schedule 1 / SE>

## Sources cited
- IRS Form 1099-NEC, Rev. <year>
- IRS Instructions for Forms 1099-MISC and 1099-NEC, Rev. <year>
- IRC §6041, §1402 (SE tax for trade-or-business income)
```

---

## References

Loaded on demand based on the user's situation.

- [`references/line-by-line.md`](./references/line-by-line.md) — Complete box-by-box reference for Form 1099-NEC
- [`references/payee-classification.md`](./references/payee-classification.md) — Employee vs. contractor; corporation vs. SMLLC vs. partnership; W-9 entity types
- [`references/threshold-rules.md`](./references/threshold-rules.md) — $2,000 (2026) vs. $600 (2025 and prior) threshold mechanics, backup withholding regardless of amount
- [`references/backup-withholding.md`](./references/backup-withholding.md) — IRC §3406, B-Notices, Form 945 deposit rules
- [`references/common-mistakes.md`](./references/common-mistakes.md) — Top filer errors with citations and fixes
- [`filing.md`](./filing.md) — Browser-automation playbook for IRIS / FIRE / paper filing

## Examples

End-to-end worked 1099-NEC scenarios.

- [`examples/payor-web-designer.md`](./examples/payor-web-designer.md) — Small business issuing a 1099-NEC for $3,500 paid to a freelance web designer (crosses 2026 $2,000 threshold)
- [`examples/recipient-freelance-writer.md`](./examples/recipient-freelance-writer.md) — Freelancer receiving multiple 1099-NECs and reporting aggregate on Schedule C
- [`examples/backup-withholding-missing-w9.md`](./examples/backup-withholding-missing-w9.md) — Recipient noting Box 4 backup withholding on a 1099-NEC due to missing W-9 history, reconciling Form 1040 Line 25c

## Sources

Authoritative sources used by this skill. Always re-verify these against the IRS site for the tax year being filed — the IRS revises forms and instructions each cycle.

- [1099-NEC Guide 2026](https://jupid.com/blog/1099-nec-guide-2026) — Jupid's narrative companion to this skill, written for human readers
- [Form 1099-NEC (latest)](https://www.irs.gov/pub/irs-pdf/f1099nec.pdf) — the form itself
- [Instructions for Forms 1099-MISC and 1099-NEC (latest)](https://www.irs.gov/pub/irs-pdf/i1099mec.pdf) — combined IRS instructions
- [About Form 1099-NEC](https://www.irs.gov/forms-pubs/about-form-1099-nec) — IRS landing page
- [Publication 1220](https://www.irs.gov/pub/irs-pdf/p1220.pdf) — Specifications for Electronic Filing of Information Returns
- [Information Returns Intake System (IRIS)](https://www.irs.gov/filing/e-file-information-returns) — IRS free e-file portal
- [Form 945](https://www.irs.gov/forms-pubs/about-form-945) — Annual Return of Withheld Federal Income Tax (for backup withholding)
- [Form W-9](https://www.irs.gov/pub/irs-pdf/fw9.pdf) — Request for Taxpayer Identification Number and Certification
- IRC §6041 (general info-return obligation), §6041A (services > $600 historically; threshold raised by OBBBA), §3406 (backup withholding), §6011(e) (mandatory e-file threshold), §6109 (TIN reporting), §1402 (SE tax)
- OBBBA (One Big Beautiful Bill Act of 2025), Section 112201 — raised 1099-NEC / 1099-MISC threshold from $600 to $2,000 effective tax year 2026 (verify current IRS guidance)
- Reg. §301.6109-4 — TIN truncation on payee statements
- Notice 2100 — IRS B-Notice template for TIN mismatches
- Taxpayer First Act of 2019, codified at IRC §6011(e)(2) — 10-return e-file threshold

## Disclaimer

This skill encodes procedural guidance based on publicly available IRS forms and publications. It is not tax advice. It does not establish a CPA-client relationship. The agent invoking this skill should remind the user, when producing a draft, that the output is a starting point and that complex situations (worker misclassification disputes, multi-state allocation, payments to attorneys with split plaintiff/attorney portions) warrant a licensed tax professional's review.
