# 1099-NEC Threshold Rules

The reporting threshold determines whether a 1099-NEC is required for a given payee. The rules are simple in steady state but tricky in transition years (2025 → 2026), and tricky around backup withholding.

## Current threshold

**Tax year 2026: $2,000 per payee per calendar year.**

Source: P.L. 119-21 (One Big Beautiful Bill Act, July 4, 2025) §70433, which replaced "$600" with "$2,000" in IRC §6041(a), applied the same amount to §6041A and to backup withholding (§3406(b)(6)), and added §6041(h). The change applies to payments made after December 31, 2025 (Instructions for Forms 1099-MISC and 1099-NEC, Rev. December 2026, What's New; law.cornell.edu notes to §6041).

**2027 and later**: the $2,000 is adjusted for inflation beginning in calendar year 2027, rounded to $100 steps (IRC §6041(h); Pub. 1099 (2026)). Read the year's figure at IRS.gov/InflationAdjustment and https://www.irs.gov/forms-pubs/about-form-1099-nec before filing.

## Pre-2026 threshold

**Tax year 2025 and earlier: $600 per payee per calendar year.**

The $600 threshold has been in place since the original 1099 reporting regime was enacted (1954). OBBBA's $2,000 change is the first major adjustment in decades.

## How the threshold works

The threshold is **per payee**, **per calendar year**, **aggregated across all payments** for services from the payer to that payee.

### Aggregation rules

- Aggregate by payee TIN, not by invoice or project. Three projects of $800 each to the same contractor in 2026 = $2,400 total = exceeds $2,000 threshold = 1099-NEC required.
- Aggregate by **payer** (legal entity) — if a payer has multiple DBAs but one EIN, aggregate across all DBAs.
- Do NOT aggregate across calendar years. A contractor paid $1,500 in late 2026 and $700 in early 2027 = neither year crosses the threshold (the 2027 threshold is $2,000 adjusted for inflation, so it is at least $2,000).

### Cash basis vs. accrual

The threshold is measured on a **cash basis** for the payer. The trigger date is when the payer makes the payment, not when the contractor invoices.

- Payer mails a check on December 28, 2026 that the contractor cashes January 5, 2027 → counted in 2026 (when payer disbursed)
- Payer schedules an ACH for January 3, 2027 (initiated December 30, 2026) → typically counted on the settlement date — verify with the payer's accounting; both dates are defensible

If the payment date is unclear, use the date the payer's bank account was debited.

### Year-end timing trap

A common error: a contractor invoices December 15 for $1,800, the payer pays December 30, 2026. That payment is below the $2,000 2026 threshold. But if the same contractor billed an additional $400 invoice later in December, paid before year-end, the aggregate is $2,200 → 1099-NEC required.

The agent should aggregate **all** payments to a payee within the calendar year before applying the threshold.

## Backup withholding overrides the threshold

If the payer applied **any backup withholding** (24% under IRC §3406) to **any** payment to the payee during the year, a 1099-NEC must be issued **regardless of whether the threshold was met**.

Reason: the payer needs to report the withholding to the IRS so the payee gets credit for it (via Form 1040 Line 25b).

Example: payer paid contractor $1,500 in 2026 and applied 24% backup withholding on those payments because the contractor never returned a W-9. 1099-NEC is required (Box 1a = $1,500, Box 4 = $360) even though $1,500 < $2,000.

Note: after P.L. 119-21, backup withholding on contractor payments is generally required only once the payee's annual total reaches the $2,000 reporting amount, or if a 1099 was required (or backup withholding applied) for that payee in the prior year (IRC §3406(b)(6); Pub. 1099 (2026), What's New). If the payer withheld anyway, the form is still required.

## What counts toward the threshold

| Payment type | Counts toward Box 1 threshold? |
|--------------|--------------------------------|
| Service fees (consulting, design, freelance) | Yes |
| Commissions (non-employee sales) | Yes |
| Awards / prizes / bonuses for services | Yes |
| Termination payments to a non-employee | Yes |
| Travel reimbursement under non-accountable plan | Yes |
| Travel reimbursement under accountable plan (Reg. §1.62-2) | No |
| Goods / merchandise / inventory | No |
| Rent | No (use 1099-MISC Box 1) |
| Royalties | No (use 1099-MISC Box 2) |
| Attorneys' fees for legal services (even to an incorporated law firm) | Yes (Box 1a) |
| Gross proceeds paid to an attorney (e.g., settlement funds) | No (1099-MISC Box 10, $600 threshold) |
| Medical / health-care payments | No (use 1099-MISC Box 6, $2,000 for 2026) |
| Payments by credit/debit card or via Stripe / PayPal / Venmo Business / Square / Cash App for Business | No (reportable on Form 1099-K by the payment settlement entity) |
| Personal (non-business) payments | No |

## State threshold variations

States set their own information-return thresholds and may not follow the federal $2,000. This skill does not carry a verified state table: ask the user for the state(s) involved and check each state revenue department's current guidance before relying on the federal number.

If the payer has nexus in a state with a different threshold, the payer may need to file at the state level even if federal isn't required.

See the CF/SF Program section of Pub. 1099 (2026) (https://www.irs.gov/pub/irs-pdf/p1099.pdf) for the Combined Federal/State Filing program.

## What if the payer over-issues?

If a payer issues a 1099-NEC for an amount below the threshold (e.g., issues for $1,500 in 2026), the IRS won't reject it. The payee still has to report the income (Box 1 income is taxable regardless of whether 1099-NEC was issued). The payer doesn't face a penalty.

However, the payer creates work for themselves and the recipient. Best practice: aggregate carefully, apply the threshold, only issue when required.

## What if the payer fails to issue?

Penalties under IRC §6721 (failure to file with IRS) and §6722 (failure to furnish to recipient), charged separately for each:

| Returns due in | Up to 30 days late | 31 days late through Aug. 1 | After Aug. 1 or not filed | Intentional disregard |
|---|---|---|---|---|
| 2026 (2025 payments) | $60 | $130 | $340 | $680 |
| 2027 (2026 payments) | $60 | $130 | $340 | $690 |

Sources: https://www.irs.gov/payments/information-return-penalties (2026 row); Rev. Proc. 2025-32 §§4.57–4.58 (2027). Indexed for inflation; small businesses have lower annual maximums (Pub. 1099, part O).

The payee's deduction (the contractor expense on the payer's Schedule C / 1120 / 1120-S) generally remains deductible even if 1099-NEC isn't issued — the deduction depends on substantiation under IRC §162, not on 1099 compliance. But the payer may face a separate penalty.
