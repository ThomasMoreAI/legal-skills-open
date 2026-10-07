# Example: Freelance Writer Receiving Multiple 1099-NECs

A complete walkthrough of a freelance writer who received four Form 1099-NECs from different clients in 2026 and needs to reconcile them against records and report on Schedule C. This is the canonical "freelancer aggregating multiple direct clients" pattern.

## The recipient

- **Name**: Lena Okafor (sole proprietor; no LLC; uses SSN as TIN)
- **SSN**: 215-XX-XXXX
- **Business**: Freelance technical writing (B2B SaaS, developer tools)
- **Tax year**: 2026 (filing in early 2027)
- **First Schedule C year**: No (fourth year as a freelancer)

## 1099-NECs received

| Payer | Box 1 | Box 4 | Boxes 5-7 (state) |
|-------|-------|-------|--------------------|
| TechCorp Inc. | $24,000 | $0 | NY/$24,000 |
| DataFlow LLC | $11,500 | $0 | CA/$11,500 |
| DevDocs Co. | $8,750 | $0 | TX/$8,750 |
| Cloud Wave Inc. | $3,200 | $0 | NY/$3,200 |
| **Total Box 1 across all 1099-NECs** | **$47,450** | **$0** | |

## Lena's own records

| Source | Amount | Notes |
|--------|--------|-------|
| TechCorp invoices (matched) | $24,000 | All 6 invoices reconciled, paid via ACH |
| DataFlow invoices | $11,500 | Reconciled |
| DevDocs invoices | $8,750 | Reconciled |
| Cloud Wave invoices | $3,200 | Reconciled |
| Stripe direct invoices (separate small clients) | $9,400 | 1099-K only if Stripe's reporting threshold is met (more than $20,000 and 200 transactions for third-party network payments); report either way |
| Two cash clients (sub-threshold each) | $1,200 | No 1099, but Lena reports |
| **Total gross 2026 income** | **$58,050** | |

## Decision: Schedule C path or Schedule 1 Line 8 path?

Per [`payee-classification.md`](../references/payee-classification.md) and IRC §162 + Reg. §1.183-2(b):

- Lena writes regularly (50+ hours/week, year-round)
- Lena has a profit motive (this is her primary income)
- Lena has multiple clients (not employee-like dependence on one)
- Lena has a profit history (4 years of net income)

→ This is a **trade or business**. **Schedule C path** applies.

(If Lena were an academic writing one occasional honorarium per year while employed full-time elsewhere, that might be Schedule 1 Line 8z. Not Lena's case.)

## Reconciliation: Schedule C Line 1

| Source category | Amount |
|----------------|--------|
| Sum of all 1099-NECs Box 1a | $47,450 |
| Stripe payouts (no 1099-K expected below the threshold) | $9,400 |
| Cash payments (no 1099) | $1,200 |
| **Schedule C Line 1 (gross receipts)** | **$58,050** |

Lena reports the **full $58,050** on Schedule C Line 1, not the $47,450 sum of 1099-NECs alone. The IRS expects gross receipts to include ALL income — 1099-reported and not.

The cross-check: Schedule C Line 1 ≥ sum of all 1099s received ($47,450 of 1099-NECs, plus any 1099-K if one arrives). Lena's $58,050 exceeds this, which is correct ($9,400 of Stripe income and $1,200 of cash weren't on any 1099-NEC).

## Box 4 federal withholding handling

All four 1099-NECs have Box 4 = $0 (no backup withholding; Lena had valid W-9s on file with each client).

If Box 4 had been > $0 on any 1099-NEC, Lena would total the Box 4 amounts and report them on the Form 1040 line for withholding from Form(s) 1099 (**line 25b** on the 2025 Form 1040; confirm the line on the 2026 form).

## State income reconciliation

Lena lives in Texas (no state income tax). The Box 6/7 entries on each 1099-NEC show the state where the client is located (or where Lena performed services). Texas income tax: $0. New York and California have non-resident income tax obligations only if Lena physically performed work there or has nexus — for remote freelance writing performed entirely in Texas, generally no NY/CA filing required (each state has its own rules; consult state DOR or a CPA for non-resident state returns).

For this example: Lena files only federal + Texas franchise tax (which doesn't apply to her under the small-business threshold).

## Lena's Schedule C draft (excerpt)

```markdown
# Schedule C — DRAFT for tax year 2026

## Header
A. Principal business: Freelance technical writing
B. Business code: 711510 (Independent artists, writers, performers)
C. Business name: blank (Lena uses her personal name)
D. EIN: blank (uses SSN)
E. Address: Same as Form 1040
F. Accounting method: Cash
G. Material participation: Yes
H. Started this year: No
I. Made payments requiring Form(s) 1099: No
J. (N/A — I=No)

## Part I — Income
1.  Gross receipts:                $58,050
2.  Returns and allowances:        $0
3.  Subtract line 2 from 1:        $58,050
4.  Cost of goods sold:            $0       (service business; no Part III)
5.  Gross profit:                  $58,050
6.  Other income:                  $0
7.  Gross income:                  $58,050

## Part II — Expenses
(... Lena's expenses, not detailed in this 1099-NEC example ...)
28. Total expenses:                $11,200
29. Tentative profit:              $46,850
30. Home office (simplified):      $1,250  (250 sq ft × $5)
31. Net profit:                    $45,600

## Sources cited
- Four 1099-NECs received from clients (TechCorp, DataFlow, DevDocs, Cloud Wave)
- Stripe payout records for direct invoice clients (1099-K only if the platform's threshold is met)
- IRC §162 (trade or business deduction)
- IRC §1402 (SE tax for trade-or-business income)
```

## Validation summary

- **Math**: Schedule C Line 1 ($58,050) ≥ sum of 1099-NECs ($47,450). Difference = $9,400 Stripe + $1,200 cash, confirmed.
- **Sanity**:
  - All four 1099-NECs reconcile to Lena's records exactly. No discrepancies.
  - No backup withholding (Box 4 = $0 on all). No Form 1040 Line 25b entries from 1099s.
  - State boxes consistent with each client's location.
- **Next steps**:
  - Schedule SE: net SE income = $45,600 × 92.35% = $42,112; SE tax = $42,112 × 15.3% = $6,443
  - Half of SE tax ($3,222) deductible on Schedule 1 Line 15
  - Quarterly estimated taxes for 2027 should account for income trajectory

## Why each non-obvious choice

**Why include the $1,200 cash on Line 1?** Schedule C Line 1 is *all* gross receipts, regardless of 1099 issuance. The IRS expects Line 1 ≥ sum of 1099s; less = under-reporting. Cash income is taxable like any other.

**Why not deduct the expenses on the 1099-NEC itself?** 1099-NECs report **gross** (Box 1). Expenses go on Schedule C Lines 8-27a. The recipient nets income and expenses on Schedule C, not on the 1099 itself.

**Why aggregate four 1099-NECs into one Line 1?** Schedule C is a single business (Lena's freelance writing). Multiple 1099s from multiple clients all flow into the single Line 1 total. The 1099s themselves are NOT attached to Schedule C; the IRS already has copies.

**Why not separate state filings on the 1099s into separate Schedule C entries?** A single business + a single Schedule C, regardless of how many states the income comes from. State allocation happens on state returns, not Schedule C.

**What if a client never sent a 1099-NEC despite paying $4,000?** Lena still reports the $4,000 as income on Schedule C Line 1. Income is taxable regardless of whether the payer fulfilled their reporting obligation. (The payer faces a separate penalty for non-compliance under IRC §6721.)

## Sources cited
- IRS Form 1099-NEC, Rev. December 2026
- IRS Instructions for Forms 1099-MISC and 1099-NEC, Rev. December 2026
- IRC §162 (trade or business expenses), §1402 (SE tax), §6041 (1099 reporting)
- IRS Schedule C, Rev. 2026 (https://www.irs.gov/pub/irs-pdf/f1040sc.pdf)
- IRS Instructions for Schedule C, Rev. 2026 (https://www.irs.gov/pub/irs-pdf/i1040sc.pdf)
- Reg. §1.183-2(b) (nine-factor trade-or-business test)
