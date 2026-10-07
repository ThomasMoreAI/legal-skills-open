# Top 1099-NEC Mistakes (with citations and fixes)

The most common errors agents and payers make on Form 1099-NEC, with the underlying authority and the fix.

## 1. Failing to issue 1099-NEC because payee is "an LLC"

**Mistake**: Payer assumes any LLC is exempt because corporations are exempt.

**Why wrong**: A single-member LLC (SMLLC) is **disregarded** for federal tax purposes by default — it's treated as a sole proprietorship. The owner reports income on Schedule C. SMLLCs are NOT corporations, even though the name has "LLC" in it. Per W-9 instructions and Reg. §301.7701-3, a disregarded SMLLC's owner reports the income on their own return.

**Fix**: Get a W-9 — it tells you the entity's federal tax classification (Line 3a). If a disregarded SMLLC's W-9 shows its owner's classification ("Individual/sole proprietor"), the payee is treated as an individual for 1099-NEC purposes. Issue 1099-NEC if threshold is met.

**Citation**: W-9 instructions (Reg. §301.6109-1(d)(2)); Reg. §301.7701-3(b) (default classification of eligible entities).

## 2. Issuing 1099-NEC for payments routed through Stripe / PayPal / Venmo Business

**Mistake**: Payer pays a contractor via Stripe (or PayPal goods/services, etc.) AND issues a 1099-NEC for the same amount.

**Why wrong**: Card and third-party-network payments are reportable only on **1099-K** by the payment settlement entity. Third-party networks issue a 1099-K when a payee receives more than $20,000 and more than 200 transactions in the year — P.L. 119-21 restored that test retroactively, so the planned $600 phase-in never took effect (IRS FAQs on Form 1099-K under the One Big Beautiful Bill); card transactions have no minimum. Issuing 1099-NEC for the same payments creates **double-reporting**: the recipient's IRS account shows both forms, the recipient reports the income twice (or under-reports because they think both are the same), and an IRS notice often follows.

**Fix**: Exclude payments routed through third-party payment networks from the 1099-NEC issuance plan. Report only direct payments (cash, check, ACH bank-to-bank, Zelle).

**Citation**: IRC §6050W (1099-K reporting by third-party networks); IRS instructions for 1099-NEC and 1099-K (combined instructions warn against double-reporting).

## 3. Using the wrong threshold for the wrong year

**Mistake**: Payer applies $600 threshold for 2026 payments (because that's the rule they've always known).

**Why wrong**: P.L. 119-21 §70433 raised the threshold to $2,000 for payments made after December 31, 2025 (inflation-adjusted from 2027). Using the old $600 threshold causes over-issuance: forms issued for amounts that don't require reporting. Not technically wrong (no IRS penalty for over-reporting), but creates work and may confuse recipients.

**Fix**: Use $2,000 for 2026; the inflation-adjusted amount for 2027+ (IRS.gov/InflationAdjustment); $600 for 2025 and earlier.

**Citation**: P.L. 119-21 §70433, amending IRC §6041(a), §6041A, and §3406(b)(6) and adding §6041(h); Instructions for Forms 1099-MISC and 1099-NEC (Rev. December 2026), What's New.

## 4. Missing the recipient deadline (January 31)

**Mistake**: Payer thinks they have until February or March to deliver Copy B to recipients.

**Why wrong**: 1099-NEC is special — both Copy B (recipient) and Copy A (IRS) are due **January 31**. This is unique to 1099-NEC; 1099-MISC has a later IRS deadline (Feb 28 paper / Mar 31 electronic).

**Fix**: Set internal deadline of January 28 to allow buffer. Postmark recipient copies by January 31, file with IRS by January 31 (next business day on a weekend: February 1, 2027 for 2026 forms). Don't conflate with 1099-MISC schedule.

**Citation**: IRC §6071(c) (acceleration of due dates for 1099-NEC); Instructions for 1099-MISC and 1099-NEC, "When to file" section.

## 5. Putting attorneys' fees on 1099-MISC Box 10 (or skipping incorporated law firms)

**Mistake**: Payer pays a law firm $10,000 for legal work for the business and reports it on 1099-MISC Box 10, or skips the form because the firm is a PC or S corporation.

**Why wrong**: Attorneys' fees for legal services paid in the course of the payer's business go in **1099-NEC box 1a** (box 1 for 2025) at the $2,000 threshold (2026), even when the law firm is incorporated. **1099-MISC Box 10** is only for **gross proceeds** paid to an attorney, such as settlement funds where the attorney is the conduit; that threshold stays at $600.

**Fix**: Legal fees → 1099-NEC box 1a. Settlement or other gross proceeds paid to a claimant's attorney → 1099-MISC Box 10. Get the attorney's TIN either way; an attorney must furnish it even if incorporated.

**Citation**: Instructions for Forms 1099-MISC and 1099-NEC (Rev. December 2026), "Payments to attorneys" and "Payments to corporations for legal services"; IRC §6041A(a)(1), §6045(f).

## 6. Including reimbursements in Box 1

**Mistake**: Contractor invoices $5,000 for services + $1,200 for reimbursable travel expenses (with receipts). Payer reports $6,200 in Box 1.

**Why wrong**: If the reimbursement is under an **accountable plan** (Reg. §1.62-2 — substantiated, returned excess, business connection), it's NOT income to the contractor and shouldn't be on 1099-NEC. Only the $5,000 services portion is reportable.

**Fix**: Distinguish service fees from accountable-plan reimbursements. Box 1 = service fees only. If the contractor doesn't substantiate (non-accountable plan), the reimbursement is includable.

**Citation**: Reg. §1.62-2(c) (definition of accountable plan); IRS instructions for 1099-NEC ("Reimbursements" exclusion).

## 7. Wrong recipient name on 1099-NEC for SMLLC

**Mistake**: Payer issues 1099-NEC to "ABC Designs LLC" with the LLC's EIN.

**Why wrong**: For a disregarded SMLLC, the W-9 requires the *owner's* legal name on Line 1 and the *owner's* SSN (or the owner's EIN, if the owner has one) in Part I — never the disregarded entity's EIN. The IRS doesn't have a tax filing under the LLC's name (because the LLC is disregarded — its activity rolls up to the owner's Schedule C). A 1099-NEC issued to the LLC name with the LLC EIN will likely fail TIN matching.

**Fix**: Issue 1099-NEC in the owner's name with the owner's SSN. The LLC name can go on the optional second line (DBA) but the legal name and TIN are the owner's.

**Citation**: W-9 instructions, "How to complete Line 1" for SMLLC; Reg. §301.7701-3.

## 8. Failing to file electronically when required

**Mistake**: Payer files 12 paper 1099s with paper Form 1096.

**Why wrong**: Under IRC §6011(e) and T.D. 9972, a payer filing **10 or more** information returns total in a calendar year must e-file, aggregating across ALL types (1099-NEC + 1099-MISC + 1099-K + W-2 + others). Paper filing when e-file is mandatory is treated as a failure to file under IRC §6721 ($340 per return for returns due in 2026 and 2027), but only for the returns beyond 10 (Pub. 1099 (2026), part F, "Penalty").

**Fix**: Use IRIS (free; the only IRS e-file intake for information returns from filing season 2027, when FIRE is retired) or a paid third-party service. Aggregate across all forms — a payer with 5 1099-NECs + 4 1099-MISCs + 2 W-2s = 11 returns = e-file required.

**Citation**: IRC §6011(e); Reg. §301.6011-2 (mandatory electronic filing thresholds, as amended by T.D. 9972); Pub. 1099 (2026), part F.

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

**Fix**: File Form 945 by January 31 (or February 10 if all deposits were on time); February 1, 2027 for 2026. Backup withholding goes on line 2.

**Citation**: IRC §3406(c) (deposit and reporting of backup withholding); Form 945 instructions.

## 12. Forgetting state filing requirements

**Mistake**: Payer files federal 1099-NEC via IRIS but doesn't file state copies.

**Why wrong**: The IRS Combined Federal/State Filing (CF/SF) program forwards 1099 data to participating states, but not every state participates and some participating states still require their own filing. Missing state filings can trigger state penalties.

**Fix**: Check the CF/SF Program section of Pub. 1099 (2026) and each state revenue department's current requirements; file separately where the state requires it. This skill does not keep a verified state list — ask the user which states are involved.

**Citation**: Pub. 1099 (2026), CF/SF Program; state DOR websites.
