# Form 1099-NEC Box-by-Box Reference

Complete lookup for every box on Form 1099-NEC and the payer/recipient header blocks. Use this when the agent needs to confirm what goes where.

Verified against **Form 1099-NEC (Rev. December 2026)** (2026 payments, filed early 2027) and the Instructions for Forms 1099-MISC and 1099-NEC (Rev. December 2026). For 2025 payments the **Rev. April 2025** form applies: same boxes except that nonemployee compensation is "Box 1" and there are no boxes 1b–1d. Re-check https://www.irs.gov/forms-pubs/about-form-1099-nec for the next revision.

## Header blocks

### Payer (top-left block)

| Field | What goes here | Notes |
|-------|----------------|-------|
| Payer's name, street address, room/suite, city or town, state or province, country, ZIP, phone | Payer's legal business name and primary mailing address | Separate entry boxes on the Rev. December 2026 form. Must match payer's IRS records (Form SS-4 EIN application) |
| Payer's TIN | Payer's EIN (preferred) | A sole proprietor with no EIN may use SSN, but rarely files 1099-NECs without EIN — encourage EIN |

### Recipient (left-center block)

| Field | What goes here | Notes |
|-------|----------------|-------|
| Recipient's name | Legal name from W-9 Line 1 | Individual: full legal name. SMLLC owned by an individual: owner's name, not LLC name (per W-9 instructions). Corporation: corporation name. |
| (Optional) DBA | Business / trade name from W-9 Line 2 | Below the legal name |
| Recipient's TIN | SSN, ITIN, or EIN from W-9 Part I | May be truncated on Copy B (last 4 only) per Reg. §301.6109-4; full TIN on Copy A to IRS |
| Recipient's street address | From W-9 Lines 5–6 | |
| Account number | Optional internal payer reference | Required if multiple 1099s for same recipient (e.g., split between contractor and rental relationship) |

### Special header items

| Field | What goes here | Notes |
|-------|----------------|-------|
| 2nd TIN not. | Check if IRS has notified payer 2x within 3 years that recipient's TIN is wrong | Triggers ongoing backup withholding; document on file |
| FATCA filing requirement | Check if filing under FATCA (rare; only foreign financial institutions reporting US accounts) | |
| CORRECTED | Check when filing a correction to a previously-filed 1099-NEC | |
| VOID | Check to invalidate a paper Copy A before submission (mistake during preparation) | Don't void Copy B — that's already been issued |

---

## Box-by-box

### Box 1a — Nonemployee compensation (Box 1 on the Rev. April 2025 form)

The most-used box. Total gross paid to the recipient for services performed in the calendar year.

**Includes**:
- Fees for services (consulting, design, freelance work, contract labor)
- Commissions paid to independent contractors (not employees)
- Awards / prizes / bonuses paid to non-employees for services rendered
- Benefits + cash payments to a non-employee director (board fees)
- Travel reimbursements paid to a contractor under a *non-accountable* plan (i.e., the contractor doesn't substantiate the expense)
- Attorneys' fees for legal services, including fees paid to an incorporated law firm (§6041A(a)(1))

**Excludes**:
- Reimbursements paid under an *accountable* plan (substantiated, returned excess) — Reg. §1.62-2
- Payments for goods / merchandise (not services)
- Rent (use 1099-MISC Box 1)
- Royalties (use 1099-MISC Box 2)
- Gross proceeds paid to an attorney, e.g., settlement funds (use 1099-MISC Box 10)
- Medical / health-care payments (use 1099-MISC Box 6 — even if to a corporation)
- Employee wages (use W-2)
- Payments to corporations for services (except legal services, which stay in box 1a, and medical payments, which go on 1099-MISC Box 6)
- Payments made by credit/debit card or through a third-party payment network (Stripe, PayPal goods/services, Venmo business, Square, Cash App for Business) — reportable on Form 1099-K by the payment settlement entity instead
- Personal payments unrelated to the payer's trade or business

**Threshold for tax year 2026**: $2,000 per payee (P.L. 119-21 §70433, raised from $600; inflation-adjusted from 2027 under IRC §6041(h)).

**Threshold for tax year 2025 and earlier**: $600 per payee.

If backup withholding was applied to **any** payment, issue 1099-NEC regardless of whether the threshold is met.

### Box 1b — Cash tips (Rev. December 2026)

Total amount designated as cash tips included in box 1a (cash or charged tips). Added for P.L. 119-21 §70201 tip reporting.

### Box 1c — Treasury Tipped Occupation Code(s) (TTOC) (Rev. December 2026)

Up to two TTOCs for the occupations in which the tips were received; enter "000" as one code if any tips came from a nonqualifying occupation (IRS.gov/TTOC).

### Box 1d — Overtime compensation (Rev. December 2026)

Qualified overtime compensation included in box 1a: only the amount above the regular rate required by FLSA §7 (the "half" of time-and-a-half). Added for P.L. 119-21 §70202.

### Box 2 — Direct sales of consumer products ≥$5,000

Check this box only if the payer made direct sales totaling $5,000+ of consumer products to the recipient on a buy-sell, deposit-commission, or other commission basis for resale. Common in multi-level marketing / direct-sales businesses (Mary Kay, Avon, etc.). The payer also has the option to report on 1099-MISC Box 7 instead of 1099-NEC Box 2 — same rule, two reporting paths. Most payers won't use this.

### Box 3 — Excess golden parachute payments

Excess parachute payments (the amount over the base amount, per Reg. §1.280G-1 Q/A-38 to Q/A-44) to a nonemployee. Moved here from Form 1099-MISC. Rare; the recipient owes a 20% excise tax reported on Schedule 2 (Form 1040), line 17k.

### Box 4 — Federal income tax withheld

Backup withholding amount, withheld at 24% (IRC §3406) when:

- The payer doesn't have a valid TIN for the recipient (W-9 missing or incorrect)
- The IRS has notified the payer that the recipient's TIN is wrong
- The IRS has notified the payer to withhold (C-notice for under-reporting interest/dividends, but applies generally)
- The recipient hasn't certified that they're not subject to backup withholding (W-9 Part II)

The withheld amount is deposited with the IRS by EFT (EFTPS, IRS Direct Pay, or business tax account), then reported on **Form 945** line 2 (backup withholding), filed by January 31 of the year after (February 1, 2027 for 2026).

There is no concept of voluntary withholding for 1099-NEC — if Box 4 > 0, it's backup withholding.

### Box 5 — State tax withheld

State income tax withheld, if any. Most 1099-NEC payments do not have state withholding; this box is mostly used in states with mandatory withholding on certain payments (e.g., California 7% withholding on payments to non-resident contractors performing services in CA — Form 592).

### Box 6 — State / Payer's state no.

State 2-letter abbreviation followed by the payer's state ID number issued by that state's tax department.

### Box 7 — State income

Amount of Box 1 attributable to that state (i.e., income earned by services performed in that state).

The form supports two state rows (Boxes 5/6/7 each twice — top and bottom). For more than two states, payer attaches a continuation or files multiple 1099-NECs with different state rows.

---

## Common edge cases

### Mid-year corporate conversion

If a payee was an SMLLC or sole proprietor for part of the year (1099-NEC required) and then incorporated mid-year (subsequent payments exempt), issue a 1099-NEC only for amounts paid before the incorporation date. The payee should provide a new W-9 with the new EIN at the time of conversion.

### Payee who works in multiple capacities

A payee may receive both nonemployee compensation (services) and rent in the same year from the same payer. Issue:
- One 1099-NEC for services (Box 1)
- One 1099-MISC for rent (Box 1)

Both forms can carry the same recipient name and TIN; the account number field distinguishes.

### Mid-year recipient name change

If the recipient changed their legal name (marriage, name change), the payer should obtain an updated W-9 with the new name *and* new TIN if applicable. The 1099-NEC should reflect the legal name as of issuance.

### Deceased recipient

If the recipient died during the year, issue 1099-NEC to the recipient's estate (with the estate's EIN) for amounts paid after death. Amounts paid before death use the recipient's SSN.

### Recipient is a foreign person

For payments to a non-US person, do NOT issue 1099-NEC. Instead, the payee provides Form W-8BEN (individual) or W-8BEN-E (entity), and the payer reports on **Form 1042-S** with potential withholding under chapter 3 (typically 30% on US-source FDAP income, reduced by treaty). Out of scope for this skill — different reporting regime.

### Recipient is a single-member LLC

SMLLCs are disregarded for federal tax purposes by default. Per W-9 instructions:
- W-9 Line 1: owner's legal name (NOT the LLC name)
- W-9 Line 2: optional DBA / LLC name
- W-9 Line 3: check "Individual / sole proprietor or single-member LLC"
- W-9 Line 4 (TIN): owner's SSN preferred (or owner's EIN if owner has one for the SMLLC; IRS prefers SSN for SMLLCs)

Issue 1099-NEC in the owner's name with the owner's SSN. Common error: issuing 1099-NEC to "ABC Designs LLC" with the LLC EIN — that mismatches IRS records (the LLC doesn't have a tax filing of its own; the income is reported on the owner's Schedule C).

If the SMLLC has elected corporate or S-corp tax treatment (Form 8832 or 2553), it's no longer disregarded — it's a corporation, exempt from 1099-NEC for services.
