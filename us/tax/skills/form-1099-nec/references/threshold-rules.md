# 1099-NEC Threshold Rules

The reporting threshold determines whether a 1099-NEC is required for a given payee. The rules are simple in steady state but tricky in transition years (2025 → 2026), and tricky around backup withholding.

## Current threshold

**Tax year 2026 and later: $2,000 per payee per calendar year.**

Source: One Big Beautiful Bill Act of 2025 (OBBBA), Section 112201, which amended IRC §6041(a) and §6041A. The change is effective for payments made in calendar years beginning after December 31, 2025.

**Verify before filing**: the IRS may publish transitional notices or implementation guidance. Check https://www.irs.gov/forms-pubs/about-form-1099-nec for the latest.

## Pre-2026 threshold

**Tax year 2025 and earlier: $600 per payee per calendar year.**

The $600 threshold has been in place since the original 1099 reporting regime was enacted (1954). OBBBA's $2,000 change is the first major adjustment in decades.

## How the threshold works

The threshold is **per payee**, **per calendar year**, **aggregated across all payments** for services from the payer to that payee.

### Aggregation rules

- Aggregate by payee TIN, not by invoice or project. Three projects of $800 each to the same contractor in 2026 = $2,400 total = exceeds $2,000 threshold = 1099-NEC required.
- Aggregate by **payer** (legal entity) — if a payer has multiple DBAs but one EIN, aggregate across all DBAs.
- Do NOT aggregate across calendar years. A contractor paid $1,500 in late 2026 and $700 in early 2027 = neither year crosses the threshold (assuming the $2,000 threshold continues unchanged for 2027).

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

Reason: the payer needs to report the withholding to the IRS so the payee gets credit for it (via Form 1040 Line 25c).

Example: payer paid contractor $1,500 in 2026 and applied 24% backup withholding on those payments because the contractor never returned a W-9. 1099-NEC is required (Box 1 = $1,500, Box 4 = $360) even though $1,500 < $2,000.

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
| Attorney fees | No (use 1099-MISC Box 10) |
| Medical / health-care services | No (use 1099-MISC Box 6) |
| Payments via Stripe / PayPal / Venmo Business / Square / Cash App for Business | No (platform issues 1099-K) |
| Personal (non-business) payments | No |

## State threshold variations

States may have lower thresholds for state 1099-NEC filing than federal.

For 2026, examples (verify each year):

- California: $600 threshold for state filing (FTB Form 592)
- New York: federal threshold for state filing
- Pennsylvania: $5,000 threshold for state filing (slightly different rules)

If the payer has nexus in a state with a different threshold, the payer may need to file at the state level even if federal isn't required.

See https://www.irs.gov/pub/irs-pdf/p1220.pdf Section B for the Combined Federal/State Filing program list.

## What if the payer over-issues?

If a payer issues a 1099-NEC for an amount below the threshold (e.g., issues for $1,500 in 2026), the IRS won't reject it. The payee still has to report the income (Box 1 income is taxable regardless of whether 1099-NEC was issued). The payer doesn't face a penalty.

However, the payer creates work for themselves and the recipient. Best practice: aggregate carefully, apply the threshold, only issue when required.

## What if the payer fails to issue?

Penalties under IRC §6721 (failure to file with IRS) and §6722 (failure to furnish to recipient):

- $60 per form if filed within 30 days after due date
- $130 per form if filed after 30 days but before August 1
- $330 per form if filed after August 1 or not at all
- $660 per form for intentional disregard

These are the 2025 amounts; they're indexed for inflation. Verify current year at https://www.irs.gov/government-entities/federal-state-local-governments/penalty-amounts-for-information-returns.

The payee's deduction (the contractor expense on the payer's Schedule C / 1120 / 1120-S) generally remains deductible even if 1099-NEC isn't issued — the deduction depends on substantiation under IRC §162, not on 1099 compliance. But the payer may face a separate penalty.
