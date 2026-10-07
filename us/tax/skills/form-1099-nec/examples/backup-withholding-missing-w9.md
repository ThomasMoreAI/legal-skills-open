# Example: Recipient with Backup Withholding from Missing W-9

A complete walkthrough of a contractor who received a 1099-NEC with backup withholding in Box 4 because they never returned a valid W-9 to a client. Shows reconciliation, Form 1040 Line 25b handling, and how to prevent this going forward.

## The recipient

- **Name**: Marcus Whitfield (sole proprietor, freelance video editor)
- **SSN**: 605-XX-XXXX
- **Tax year**: 2026
- **Situation**: Marcus moved between three apartments in 2026. A new client (Streamline Media) sent W-9 requests to two of his outdated email addresses, both of which Marcus had abandoned. By the time he saw the third request, Streamline Media had already started backup withholding.

## The 1099-NEC received from Streamline Media

```
PAYER: Streamline Media LLC
  EIN: 91-3522XXX

RECIPIENT: Marcus Whitfield
  TIN (truncated on Copy B): XXX-XX-XXXX
  Address: 2104 Galena Ave, Denver, CO 80205

Form 1099-NEC (Rev. December 2026), calendar year 2026
Box 1a — Nonemployee compensation:       $7,500.00
Box 1b–1d — Cash tips / TTOC / Overtime:  (blank)
Box 2 — Direct sales ≥ $5,000:           ☐
Box 3 — Excess golden parachute payments: (blank)
Box 4 — Federal income tax withheld:      $1,800.00
Box 5 — State tax withheld:               $0.00
Box 6 — State / Payer's state no.:        CO / 91-3522XXX
Box 7 — State income:                     $7,500.00
```

## What happened from Streamline Media's side

1. April 8, 2026: Streamline Media sent W-9 request via email. No response.
2. April 22, 2026: Second W-9 request sent. No response.
3. April 30, 2026: Streamline began applying 24% backup withholding on all subsequent payments.
4. May 15, 2026 — September 30, 2026: Streamline paid Marcus $7,500 gross across multiple invoices. Backup withholding: $7,500 × 24% = $1,800.
5. October 5, 2026: Marcus emailed an updated W-9 (after seeing the third request and noticing the withholding on his bank deposits).
6. October 8, 2026: Streamline TIN-matched the new W-9 successfully. Stopped backup withholding for future payments (zero further payments occurred in 2026 — the project ended).

Streamline deposited the $1,800 with the IRS via EFTPS on the next deposit deadline. Streamline filed Form 945 in January 2027 reporting the $1,800. Streamline issued the 1099-NEC above.

## Marcus's records vs. the 1099-NEC

| Source | Per Marcus's invoices | Per 1099-NEC | Per Marcus's bank deposits |
|--------|----------------------|--------------|----------------------------|
| Streamline payments | $7,500 (5 invoices) | $7,500 (Box 1) | $5,700 ($7,500 − $1,800 BUW) |

**Reconciliation**: Box 1 shows the **gross** ($7,500), not the net deposit. Marcus's records (invoices) show $7,500 gross, matching Box 1. The $1,800 difference between gross and net-deposit is the backup withholding.

This is correct behavior — the IRS expects Box 1 to be gross, with Box 4 separately showing the withholding. Marcus reports $7,500 as gross income on Schedule C Line 1.

## Routing on Marcus's tax return

### Schedule C
- Marcus is a trade or business (regular freelance video editing) → Schedule C path
- Streamline's $7,500 → Schedule C Line 1 (along with all other 2026 income from other clients)
- No special handling needed on Schedule C for the backup withholding

### Form 1040
- The $1,800 backup withholding → **Form 1040 Line 25b** (federal income tax withheld from Form(s) 1099)
- This is treated identically to W-2 withholding — it counts against Marcus's total federal income tax liability

### Cash flow effect
- Marcus's actual cash deposits in 2026: $5,700 (net of withholding)
- His taxable income reflects $7,500 (gross — what's on Schedule C)
- The $1,800 acts like an early federal tax payment

If Marcus's total 2026 federal income tax (calculated from total taxable income across all clients) is $9,200:
- Schedule SE adds SE tax of, say, $5,800 (15.3% on net SE earnings)
- Total federal liability: $15,000
- Subtract $1,800 in Box 4 backup withholding from Streamline = $13,200 still owed
- Marcus will owe the $13,200 less any quarterly estimated taxes already paid

If Marcus's total 2026 federal income tax is only $1,200 (low-income year):
- Subtract $1,800 in backup withholding = ($600) overpayment
- Marcus gets a $600 refund

## Marcus's Form 1040 Line 25 area

```
Line 25 — Federal income tax withheld
  25a  W-2 forms (Box 2):              $0       (Marcus has no W-2 income)
  25b  Form(s) 1099:                   $1,800   (from Streamline 1099-NEC Box 4)
  25c  Other forms:                    $0
  25d  Total:                          $1,800
```

(Line numbers from the 2025 Form 1040; verify against the 2026 Form 1040 when it is released.)

## Validation summary

- **Math**:
  - Schedule C Line 1 includes $7,500 from Streamline (gross, not net)
  - Form 1040 Line 25b = $1,800 (Box 4 from Streamline 1099-NEC)
  - Net cash deposit ($5,700) reconciles: $7,500 − $1,800 = $5,700
- **Sanity**:
  - Marcus's records and the 1099-NEC reconcile exactly to gross
  - Backup withholding correctly reflected in Box 4
  - Marcus is on track to receive credit for the $1,800 against his federal tax liability
- **Next steps for Marcus**:
  - Update mailing address with all current and future clients
  - Set up a single business email (not personal apartment-tied emails) for W-9 requests
  - For 2027, ensure W-9 is sent BEFORE the first invoice to any new client to prevent recurrence

## Why each non-obvious choice

**Why is Box 1 gross instead of net?** Because Marcus's *income* is the gross — that's what he earned. The backup withholding is a *prepayment* of his federal tax, like W-2 withholding. The IRS wants to see gross income on Schedule C and the withholding separately on Form 1040.

**Why doesn't Marcus deduct the $1,800 as an expense?** Backup withholding is not an expense. It's a tax payment. Tax payments don't reduce income — they reduce the tax bill. (Federal income taxes are explicitly NOT deductible per Schedule C Line 23 rules.)

**What if Marcus's bank deposits don't match $5,700?** Common causes:
- Some Streamline payments hit late December 2026 / early January 2027 — that's a payor-side timing question. The 1099-NEC reflects what Streamline disbursed in calendar 2026; Marcus's deposits may lag by a few days for the late-year items. Reconcile by payment date, not deposit date.
- Bank fees on incoming wires — those don't reduce the gross. Marcus deducts bank fees separately on Schedule C Line 27a if they're business-related.

**What if Marcus disputes the backup withholding?** He can:
- Verify with Streamline that the withholding was applied correctly
- Ask Streamline for a corrected 1099-NEC if he believes the form is wrong, and report the correct amounts with records to support them (Form 4852 substitutes only for Forms W-2 and 1099-R, not 1099-NEC)
- Contact the IRS for a transcript of his account to confirm the $1,800 was deposited

In Marcus's case, the withholding was legitimately applied (he didn't return a W-9 in time). He just needs to claim the credit on Form 1040.

**Why didn't Marcus get the money refunded by Streamline?** Once Streamline deposited the $1,800 with the IRS, the only path to refund is Marcus's own tax return. Streamline cannot reverse the deposit. Marcus claims credit on Form 1040 Line 25b; if his total tax is less than the credit, the IRS refunds the excess.

## Lessons for prevention

For a contractor like Marcus going forward:
1. **Maintain a single, stable business email** that doesn't change when you move
2. **Submit W-9s proactively** before the first invoice, not in response to a request
3. **Use a virtual mailbox or P.O. box** as your business address to avoid client mail going to outdated addresses
4. **Monitor bank deposits weekly** to catch withholding shortfalls early — backup withholding is visible (deposit is 24% smaller than invoice)

## Sources cited
- IRS Form 1099-NEC, Rev. December 2026
- IRS Instructions for Forms 1099-MISC and 1099-NEC, Rev. December 2026
- IRC §3406 (backup withholding); §3406(c) (deposit and reporting)
- IRC §6402 (refunds; credit for excess withholding)
- IRS Form 945 (Annual Return of Withheld Federal Income Tax)
- IRS Form 1040 (2025), Line 25b ("Federal income tax withheld from Form(s) 1099")
- IRS Pub. 2108-A (TIN Matching Program)
