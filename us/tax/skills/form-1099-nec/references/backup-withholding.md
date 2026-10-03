# Backup Withholding for 1099-NEC

Backup withholding is the IRS's enforcement tool for ensuring contractors report their income. When a payer can't verify the contractor's TIN, the payer must withhold 24% of every payment and remit it to the IRS. This file explains when, how, and how to recover from common errors.

## When backup withholding applies

Per IRC §3406, the payer must apply 24% backup withholding when **any** of these conditions exist:

1. **No TIN provided** — the payee hasn't returned a W-9, or returned a W-9 without a TIN
2. **Wrong TIN format** — TIN provided isn't a valid SSN / ITIN / EIN format (e.g., 8 digits instead of 9, or includes letters)
3. **TIN mismatch (B-Notice)** — IRS notifies payer that the recipient's TIN doesn't match IRS records (CP2100 or CP2100A notice received by payer)
4. **Under-reporting (C-Notice)** — IRS notifies payer that recipient under-reported interest / dividend income (rare for 1099-NEC contractors)
5. **W-9 not certified** — recipient checked W-9 Part II box stating they ARE subject to backup withholding (very rare; means recipient has been instructed by IRS)

## Withholding rate

**24%** of each payment (IRC §3406(a)). This is the rate effective 2018 onward (TCJA changed it from 28% to 24%).

The rate applies to the gross payment, not the net. If payer is paying $1,000 for services with backup withholding active:

- Gross payment: $1,000
- Backup withholding: $1,000 × 24% = $240
- Net to recipient: $760

## When backup withholding starts and stops

### Starts

For the **no-TIN / wrong-TIN-format** case: immediately on the first payment after the W-9 issue is identified.

For the **B-Notice (TIN mismatch)** case: payer receives CP2100 or CP2100A from the IRS, sends a B-Notice (first or second) to the recipient, and:
- **First B-Notice**: gives recipient 30 business days to respond with a corrected W-9 (Form W-9 with proper certification). If no response within 30 business days, payer begins backup withholding on the **31st business day** after sending the B-Notice.
- **Second B-Notice** (received from IRS within 3 calendar years for the same recipient): payer cannot rely on a new W-9; recipient must provide IRS Letter 147C (verification of TIN from IRS) or SSA Form SSA-7028. Failure → backup withholding starts immediately and continues until the verification is received.

### Stops

Backup withholding stops when:
- Valid TIN is received and verified (e.g., via TIN Matching service confirming match)
- The IRS rescinds the C-Notice
- Recipient certifies on W-9 Part II that they are no longer subject to backup withholding

## Payer obligations

When backup withholding is active, the payer must:

1. **Withhold 24% from each payment** to the affected recipient
2. **Deposit the withheld amount with the IRS** via EFTPS, on the deposit schedule applicable to the payer (monthly or semi-weekly under Reg. §31.6302-1)
3. **File Form 945** (Annual Return of Withheld Federal Income Tax) by January 31 of the following year, reporting all backup withholding for the year. Form 945 is separate from Form 941 (which is for employee withholding).
4. **Issue Form 1099-NEC** to each affected recipient with Box 1 = total gross payments, Box 4 = total backup withholding amount, regardless of whether the gross crosses the $2,000 threshold (backup withholding requires a 1099-NEC).
5. **File Copy A with IRS** along with all other 1099-NECs.

## Recipient consequences

The recipient who had backup withholding applied:

- Receives 1099-NEC with Box 4 > 0
- Reports the gross income (Box 1) on Schedule C or Schedule 1
- Claims credit for the withheld amount on **Form 1040 Line 25c** (federal income tax withheld from forms 1099)
- The withheld amount counts against the recipient's federal income tax liability — same as if it were W-2 withholding

Backup withholding is **not** a penalty to the recipient (the money is credited against their actual tax). It's a cash-flow inconvenience and a signal to the recipient to fix the underlying TIN issue.

## How to avoid backup withholding (payer's playbook)

1. **Get a W-9 BEFORE the first payment**. Don't pay until W-9 is on file with TIN.
2. **Verify the W-9 via TIN Matching**. The IRS offers a free TIN Matching service through e-Services for payers who file 1099s. Submit the recipient's name + TIN and get a match / no-match response in real time.
3. **Apply backup withholding immediately** if the W-9 is missing, incomplete, or fails TIN matching. The payer is liable for the 24% even if they didn't withhold (i.e., if no W-9 was on file and payer paid full amount, payer owes the IRS the 24% out of payer's own pocket).
4. **Document everything**. Keep W-9s, TIN matching responses, B-Notices, and recipient correspondence. The B-Notice process has strict timelines and the documentation is the payer's defense.

## How to fix backup withholding errors

### Error: payer didn't withhold but should have

Payer is liable for the 24% withholding amount. Pay it via Form 945 (or Form 945-X to amend a prior-year filing). The recipient was paid 100% gross — the payer eats the 24% as an out-of-pocket cost unless they can recover from the recipient.

### Error: payer withheld too much

Refund to the recipient via reduced future payments, or issue a refund and adjust Form 945 (next-year filing) to claim a credit. Don't try to amend 1099-NEC unless the year is still open — issue a Corrected 1099-NEC if amount changed.

### Error: payer withheld for the wrong reason (e.g., misunderstood the W-9)

If withholding was applied but shouldn't have been, file Corrected 1099-NEC reducing Box 4. Refund recipient. Adjust Form 945 in the next filing.

## Example: recipient with no W-9 history

Payer Acme Corp pays freelance writer Jamie $5,000 for an article in 2026. Jamie never returned a W-9 despite multiple requests.

- Gross paid to Jamie: $5,000
- Backup withholding (24%): $1,200
- Net to Jamie: $3,800
- Acme deposits $1,200 with IRS via EFTPS
- Acme files Form 945 by January 31, 2027, reporting $1,200 backup withholding
- Acme issues 1099-NEC to Jamie: Box 1 = $5,000, Box 4 = $1,200
- Jamie reports $5,000 on Schedule C (or Schedule 1 if not a business), claims $1,200 on Form 1040 Line 25c

If Jamie's actual federal income tax for 2026 is, say, $900 (low-income year), the $1,200 backup withholding generates a $300 refund.

## Form 945 mechanics

Form 945 is the annual reconciliation for backup withholding (and for non-payroll federal income tax withholding more generally — like withholding on pension distributions, gambling winnings, etc.).

- Form 945 Line 1: federal income tax withheld from non-payroll payments (sum of all Box 4 across all 1099s)
- Form 945 Line 2: backup withholding (subset of Line 1 that's specifically backup withholding)
- Line 4-6: reconcile against deposits made via EFTPS
- Line 7: balance due or overpayment

Form 945 is due **January 31** following the calendar year. If all deposits were made on time, the deadline extends to **February 10**.

Source: https://www.irs.gov/forms-pubs/about-form-945

## State backup withholding

Some states have their own backup withholding regimes. California Form 592 / Form 593 implement state withholding on payments to non-residents performing services in California (7% rate, separate from federal 24%). Check the state's franchise tax board for state rules.
