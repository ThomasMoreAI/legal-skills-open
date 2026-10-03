# Top 1099-NEC Mistakes (with citations and fixes)

The most common errors agents and payers make on Form 1099-NEC, with the underlying authority and the fix.

## 1. Failing to issue 1099-NEC because payee is "an LLC"

**Mistake**: Payer assumes any LLC is exempt because corporations are exempt.

**Why wrong**: A single-member LLC (SMLLC) is **disregarded** for federal tax purposes by default — it's treated as a sole proprietorship. The owner reports income on Schedule C. SMLLCs are NOT corporations, even though the name has "LLC" in it. Per W-9 instructions and Reg. §301.7701-3, a disregarded SMLLC's owner reports the income on their own return.

**Fix**: Get a W-9 — it tells you the entity's federal tax classification (Line 3). If the W-9 shows "Individual / sole proprietor or single-member LLC", the payee is treated as an individual for 1099-NEC purposes. Issue 1099-NEC if threshold is met.

**Citation**: W-9 instructions (Reg. §301.6109-1(d)(2)); Reg. §301.7701-3(b) (default classification of eligible entities).

## 2. Issuing 1099-NEC for payments routed through Stripe / PayPal / Venmo Business

**Mistake**: Payer pays a contractor via Stripe (or PayPal goods/services, etc.) AND issues a 1099-NEC for the same amount.

**Why wrong**: Third-party payment networks issue **1099-K** for payments above their threshold ($600 for 2024+ under TFA, or $20,000 + 200 transactions under prior law — verify current). Issuing 1099-NEC for the same payments creates **double-reporting**: the recipient's IRS account shows both forms, the recipient reports the income twice (or under-reports because they think both are the same), and an IRS notice often follows.

**Fix**: Exclude payments routed through third-party payment networks from the 1099-NEC issuance plan. Report only direct payments (cash, check, ACH bank-to-bank, Zelle).

**Citation**: IRC §6050W (1099-K reporting by third-party networks); IRS instructions for 1099-NEC and 1099-K (combined instructions warn against double-reporting).

## 3. Using the wrong threshold for the wrong year

**Mistake**: Payer applies $600 threshold for 2026 payments (because that's the rule they've always known).

**Why wrong**: OBBBA Section 112201 raised the threshold to $2,000 effective for payments made in calendar year 2026 and later. Using the old $600 threshold causes over-issuance: forms issued for amounts that don't require reporting. Not technically wrong (no IRS penalty for over-reporting), but creates work and may confuse recipients.

**Fix**: Use $2,000 for 2026+; $600 for 2025 and earlier. Verify before each year's filing because Congress can change the threshold again.

**Citation**: OBBBA (One Big Beautiful Bill Act of 2025), Section 112201, amending IRC §6041(a) and §6041A.

## 4. Missing the recipient deadline (January 31)

**Mistake**: Payer thinks they have until February or March to deliver Copy B to recipients.

**Why wrong**: 1099-NEC is special — both Copy B (recipient) and Copy A (IRS) are due **January 31**. This is unique to 1099-NEC; 1099-MISC has a later IRS deadline (Feb 28 paper / Mar 31 electronic).

**Fix**: Set internal deadline of January 28 to allow buffer. Postmark recipient copies by January 31, file with IRS by January 31. Don't conflate with 1099-MISC schedule.

**Citation**: IRC §6071(c) (acceleration of due dates for 1099-NEC); Instructions for 1099-MISC and 1099-NEC, "When to file" section.

## 5. Issuing 1099-NEC for attorney fees instead of 1099-MISC Box 10

**Mistake**: Payer pays an attorney $10,000 for legal services and issues 1099-NEC.

**Why wrong**: Attorney legal-services payments go on **1099-MISC Box 10** (gross proceeds paid to an attorney) or **Box 1** (rents) for some specific cases — but generally Box 10 for fees and gross proceeds related to settlements. The special rule: 1099-MISC Box 10 reporting is required even if the attorney is incorporated (an exception to the corporate exemption).

**Fix**: For attorney legal services, use 1099-MISC Box 10. Issue 1099-NEC only for non-legal services payments.

**Citation**: IRC §6041 + Reg. §1.6041-3(c) (corporate exemption); Reg. §1.6041-1(d)(2) (special rule for attorneys).

## 6. Including reimbursements in Box 1

**Mistake**: Contractor invoices $5,000 for services + $1,200 for reimbursable travel expenses (with receipts). Payer reports $6,200 in Box 1.

**Why wrong**: If the reimbursement is under an **accountable plan** (Reg. §1.62-2 — substantiated, returned excess, business connection), it's NOT income to the contractor and shouldn't be on 1099-NEC. Only the $5,000 services portion is reportable.

**Fix**: Distinguish service fees from accountable-plan reimbursements. Box 1 = service fees only. If the contractor doesn't substantiate (non-accountable plan), the reimbursement is includable.

**Citation**: Reg. §1.62-2(c) (definition of accountable plan); IRS instructions for 1099-NEC ("Reimbursements" exclusion).

## 7. Wrong recipient name on 1099-NEC for SMLLC

**Mistake**: Payer issues 1099-NEC to "ABC Designs LLC" with the LLC's EIN.

**Why wrong**: For a disregarded SMLLC, the W-9 (Line 1) requires the *owner's* legal name and the *owner's* SSN (preferred) or EIN. The IRS doesn't have a tax filing under the LLC's name (because the LLC is disregarded — its activity rolls up to the owner's Schedule C). A 1099-NEC issued to the LLC name with the LLC EIN will likely fail TIN matching.

**Fix**: Issue 1099-NEC in the owner's name with the owner's SSN. The LLC name can go on the optional second line (DBA) but the legal name and TIN are the owner's.

**Citation**: W-9 instructions, "How to complete Line 1" for SMLLC; Reg. §301.7701-3.

## 8. Failing to file electronically when required

**Mistake**: Payer files 12 paper 1099s with paper Form 1096.

**Why wrong**: TFA 2019 (codified at IRC §6011(e)(2)) requires electronic filing if the payer issues **10 or more** information returns total in a calendar year, aggregating across ALL types (1099-NEC + 1099-MISC + 1099-K + W-2 + others). Paper filing when e-file is mandatory triggers a $310-per-form penalty under IRC §6721 plus potential intentional-disregard escalation.

**Fix**: Use IRIS (free) or FIRE (free, requires Transmitter Control Code) or a paid third-party service. Aggregate across all forms — a payer with 5 1099-NECs + 4 1099-MISCs + 2 W-2s = 11 returns = e-file required.

**Citation**: IRC §6011(e)(2); Reg. §301.6011-2 (mandatory electronic filing thresholds); TFA 2019.

## 9. Missing TIN-matching before filing

**Mistake**: Payer files 1099-NECs without verifying recipient TINs against IRS records first. Many forms come back with TIN-mismatch errors and trigger CP2100 / CP2100A B-Notices.

**Why wrong**: TIN mismatches create cleanup work (B-Notice process, possible backup withholding). The IRS provides a free TIN Matching service through e-Services that can catch mismatches before filing.

**Fix**: Use IRS TIN Matching (e-Services) before filing 1099-NEC. For each recipient, submit name + TIN; if mismatch, request a corrected W-9 from the recipient before filing.

**Citation**: IRS Pub. 2108-A (TIN Matching Program); e-Services TIN Matching (https://www.irs.gov/tax-professionals/taxpayer-identification-number-tin-matching).

## 10. Treating Zelle like a third-party network

**Mistake**: Payer pays contractor $4,000 via Zelle in 2026 and assumes Zelle issues 1099-K, so no 1099-NEC needed.

**Why wrong**: Zelle's position is that Zelle is a bank-to-bank rail, not a third-party payment network. Zelle does not issue 1099-K. Therefore the payer's 1099-NEC obligation stands.

**Fix**: For Zelle payments, treat the same as direct ACH or check. Aggregate, apply $2,000 threshold, issue 1099-NEC if applicable.

**Citation**: Zelle's terms of service (Early Warning Services) and FAQs; IRS guidance (informal, in FAQs and Pub. 5717) treats bank-direct rails as outside §6050W.

## 11. Forgetting to file Form 945 for backup withholding

**Mistake**: Payer applied backup withholding on a contractor for $300 during the year, deposited it via EFTPS, but didn't file Form 945.

**Why wrong**: Form 945 (Annual Return of Withheld Federal Income Tax) is required whenever the payer withholds backup withholding (or non-payroll federal income tax). Failure to file triggers IRC §6651 (failure-to-file penalty) plus IRC §6656 (failure-to-deposit penalty if deposits were not on schedule).

**Fix**: File Form 945 by January 31 (or February 10 if all deposits were on time). The form is a single-page reconciliation.

**Citation**: IRC §3406(c) (deposit and reporting of backup withholding); Form 945 instructions.

## 12. Forgetting state filing requirements

**Mistake**: Payer files federal 1099-NEC via IRIS but doesn't file state copies.

**Why wrong**: Most states are part of the IRS Combined Federal/State Filing (CF/SF) program, which forwards 1099 data to participating states automatically — but **not all**. Pennsylvania, for example, requires separate filing through myPATH. Missing state filings can trigger state penalties.

**Fix**: Check IRS Pub. 1220 Section B for the CF/SF state list. For non-participating states (currently includes Oregon, Pennsylvania, others — verify each year), file separately with the state's department of revenue.

**Citation**: IRS Pub. 1220, Section B (CF/SF Program); state DOR websites.
