# Additional Child Tax Credit (ACTC) — Refundability Computation

The ACTC is the refundable portion of the Child Tax Credit. Unlike the non-refundable CTC (which reduces tax liability but cannot create a refund), the ACTC can result in a refund check even if the filer owes no income tax.

Authority: IRC §24(d), as modified by §24(h)(5) and §24(h)(6) (refundable cap, inflation-adjusted under §24(i)(1); $2,500 earned income threshold). Lines below are from the 2025 Schedule 8812 (Part II-A lines 15–20, Part II-B lines 21–26, Part II-C line 27); re-check the current revision at https://www.irs.gov/forms-pubs/about-schedule-8812-form-1040.

---

## When ACTC is in play

ACTC is available only when:

1. The filer has at least one qualifying child for CTC (qualifying child with an SSN valid for employment issued before the due date), and the filer (or one spouse if MFJ) has such an SSN too
2. The filer has earned income greater than $2,500
3. The credit on Schedule 8812 line 12 was not fully absorbed by the filer's tax liability (line 16a = line 12 − line 14 > 0)
4. The filer does not file Form 2555 (Part II-A caution)

If the filer has only "Other Dependents" (no qualifying children with SSN), there is **no ACTC** — ODC is non-refundable.

If the filer's tax liability fully absorbed the CTC, there's no leftover for ACTC.

---

## The earned income method

The standard ACTC computation:

```
Step 1. Earned income (line 18a) > $2,500?  If no, line 20 = $0.
Step 2. Line 19 = max(0, Earned income − $2,500)
Step 3. Line 20 = line 19 × 15%
Step 4. Line 16b = N_CTC × $1,700 (tax years 2025 and 2026)
Step 5. Line 16a = line 12 − line 14 (leftover after the non-refundable credit)
Step 6. Line 17 = min(line 16a, line 16b)
Step 7. Fewer than 3 children: ACTC (line 27) = min(line 17, line 20)
```

### Example: Head of household, one child, earned income $22,000 (2025)

- N_CTC = 1
- Line 12 = $2,200
- Taxable income: $22,000 − $23,625 standard deduction = $0 → tax before credits $0
- Line 14 = min($2,200, $0) = $0
- Line 16a = $2,200 − $0 = $2,200
- Line 16b = 1 × $1,700 = $1,700; line 17 = $1,700
- Line 19 = $22,000 − $2,500 = $19,500; line 20 = $19,500 × 15% = $2,925
- ACTC = min($1,700, $2,925) = **$1,700**

The filer gets $1,700 refunded as ACTC. The remaining $500 of the $2,200 credit is "lost" (not refundable; non-refundable was $0 because tax was $0).

### Example: Earned income exactly $2,500

- Earned income excess = $0
- Earned income method ACTC = $0
- ACTC = $0 regardless of leftover or per-child cap

The earned income test is a hard floor.

---

## The alternative method (3+ qualifying children)

For filers with **3 or more qualifying children**, IRC §24(d)(1)(B)(ii) allows an alternative computation: the **Social Security tax method** (Part II-B). Use whichever method produces the larger ACTC. The form routes the filer: if line 16b is $5,100 or more and line 20 is less than line 17, go to line 21; if line 20 ≥ line 17, line 27 = line 17 and Part II-B is skipped.

### Social Security tax method (Part II-B)

```
Line 21. Social security + Medicare (incl. Additional Medicare) tax withheld:
         W-2 box 4 + W-2 box 6, both spouses if MFJ
         (Additional Medicare Tax / tier 1 RRTA → instructions' worksheet)
Line 22. Schedule 1 line 15 (deductible half of SE tax)
         + Schedule 2 line 5 (Form 4137) + line 6 (Form 8919) + line 13
Line 23. Line 21 + line 22
Line 24. Form 1040 line 27a (EIC) + Schedule 3 line 11 (excess SS withheld)
Line 25. max(0, line 23 − line 24)
Line 26. larger of line 20 (earned income method) or line 25
Line 27. ACTC = min(line 17, line 26)
```

The 3+-children alternative was added because large families with low income often have substantial Social Security/Medicare withholding but little earned income above $2,500 — the SS-tax method can produce a larger refundable credit.

### Example: MFJ couple with 3 children, W-2 wages $35,000 (2025)

- N_CTC = 3
- Line 12 = 3 × $2,200 = $6,600
- Taxable income: $35,000 − $31,500 = $3,500 → tax $353 (2025 Tax Table)
- Line 14 = $353; line 16a = $6,600 − $353 = $6,247
- Line 16b = 3 × $1,700 = $5,100; line 17 = $5,100

Earned income method:
- Line 19 = $35,000 − $2,500 = $32,500
- Line 20 = $32,500 × 15% = $4,875 (less than line 17, and line 16b ≥ $5,100 → Part II-B)

SS-tax method:
- Line 21 = W-2 boxes 4 + 6 = $35,000 × 7.65% = $2,678
- Line 24 = EIC: about $7,090 for 3 children at $35,000 MFJ in 2025 (take the exact figure from the 2025 EIC Table; Rev. Proc. 2024-40 §2.06: maximum $8,046, phase-out from $30,470)
- Line 25 = max(0, $2,678 − $7,090) = $0

Line 26 = larger of $4,875 or $0 = $4,875. ACTC = min($5,100, $4,875) = **$4,875**.

### Example: MFJ couple with 4 children, W-2 wages $20,000, no EITC

(Hypothetically, due to other rules disqualifying EITC)

- N_CTC = 4
- Line 12 = 4 × $2,200 = $8,800
- Line 14 = $0 (taxable income $20,000 − $31,500 = $0); line 16a = $8,800
- Line 16b = 4 × $1,700 = $6,800; line 17 = $6,800

Earned income method:
- Line 19 = $20,000 − $2,500 = $17,500
- Line 20 = $17,500 × 15% = $2,625

SS-tax method:
- Line 21 = $20,000 × 7.65% = $1,530
- Line 24 (EIC) = $0
- Line 25 = $1,530

Line 26 = larger of $2,625 or $1,530 = $2,625. ACTC = min($6,800, $2,625) = **$2,625**.

---

## How to decide which method to use

The agent must compute **both** methods if N_CTC ≥ 3, then use the larger. If N_CTC < 3, only the earned income method is available.

```python
line16a = line12 - line14
line16b = N_CTC * 1700  # 2025 and 2026
line17 = min(line16a, line16b)
line20 = max(0, earned_income - 2500) * 0.15
if line16b < 5100 and not puerto_rico_resident:
    actc = min(line17, line20)
elif line20 >= line17:
    actc = line17
else:
    line25 = max(0, (w2_box4 + w2_box6) + (sch1_line15 + sch2_lines_5_6_13) - (eic_27a + sch3_line11))
    actc = min(line17, max(line20, line25))
```

The 2025 Schedule 8812 routes the filer between Part II-A and Part II-B with the question after line 20; follow it exactly.

---

## Combat pay

For the ACTC, nontaxable combat pay is **always** treated as earned income: IRC §24(d)(1) (flush language) treats amounts excluded under §112 as earned income, and the Earned Income Worksheet adds it on line 1b (also reported on Schedule 8812 line 18b). There is no election for the ACTC; the combat pay election exists only for the EITC, and the Earned Income Chart adds "all of your nontaxable combat pay if you did not elect to include it in earned income for the EIC."

Common scenario: a service member with $40,000 of nontaxable combat pay and $5,000 of regular wages:
- Earned income (line 18a) = $45,000 (combat pay included automatically)
- Line 19 = $42,500
- Line 20 = $6,375
- Leaving combat pay out would understate line 20 at $375.

Use Form 1040 line 1i or [Form W-2 Box 12 with code Q](https://www.irs.gov/forms-pubs/about-form-w-2) for the combat pay figure.

The agent should ASK any military filer: "Did you receive nontaxable combat pay (W-2 box 12, code Q)? How much, for you and for your spouse?"

---

## Earned income — what counts

For ACTC purposes, **earned income** is figured on the Earned Income Chart / Earned Income Worksheet in the 2025 Schedule 8812 instructions (pp.7–8) and includes:

- Form 1040 line 1z (wages, salaries, tips and the other earned income on lines 1a–1h)
- Nontaxable combat pay (always included for the ACTC)
- Statutory employee income (Schedule C line 1)
- Net self-employment profit or loss (Schedule C line 31, Schedule K-1 (Form 1065) box 14 code A, Schedule F line 34), minus the deductible half of SE tax (Schedule 1 line 15)
- Medicaid waiver payments excluded on Schedule 1 line 8s only if the filer chooses to include them
- Filers claiming the EIC with EIC Worksheet B use its line 4b (plus nontaxable combat pay not elected for the EIC)

**Does NOT count as earned income for ACTC**:
- Pensions and annuities
- Social Security benefits
- Investment income (interest, dividends, capital gains)
- Unemployment compensation
- Alimony
- Child support
- Veterans' benefits
- Income excluded under a tax treaty (instructions, line 18a caution)

The agent should be precise about this. Tax software typically computes earned income automatically, but the agent should verify: a filer with $50K of Social Security and $5K of part-time wages has earned income of $5,000 (not $55,000).

---

## PATH Act and ACTC refund timing

Returns claiming ACTC (or EITC) are subject to additional fraud screening under the Protecting Americans from Tax Hikes (PATH) Act of 2015. The IRS can't issue refunds before mid-February for returns that properly claim the ACTC, and the hold applies to the entire refund, not just the ACTC portion (2025 Instructions for Schedule 8812, Reminders: "mid-February 2026").

If the user e-files in early February, the refund won't issue until late February at the earliest. This is a procedural delay, not a denial — but the user should be set the right expectation.

The IRS posts the year-specific PATH Act schedule at https://www.irs.gov/individuals/refund-timing.

---

## Validation checklist for ACTC

Before the agent declares the ACTC computation done:

- [ ] At least one qualifying child for CTC (with SSN before the due date), and the filer or one spouse has a valid SSN — otherwise ACTC = $0
- [ ] No Form 2555 — otherwise ACTC = $0
- [ ] Earned income > $2,500 — otherwise line 20 = $0
- [ ] Line 16b = N_CTC × $1,700 (2025 and 2026, Rev. Proc. 2025-32 §4.05(2))
- [ ] If line 16b ≥ $5,100 and line 20 < line 17, Part II-B computed; larger of line 20 / line 25 used
- [ ] ACTC ≤ line 16a (line 12 − line 14)
- [ ] ACTC ≤ line 16b
- [ ] Nontaxable combat pay included in earned income for military filers
- [ ] User informed about PATH Act delay (refund not before mid-February)

---

## Authority

- IRC §24(d) — Refundable Additional Child Tax Credit
- IRC §24(d)(1)(B)(i), §24(h)(6) — Earned income method (15% of earned income over $2,500)
- IRC §24(d)(1)(B)(ii), §24(d)(2) — Alternative social security tax method for 3+ qualifying children
- IRC §24(d)(1) flush language — combat pay excluded under §112 is earned income
- IRC §24(d)(3) — no refundable credit for a year in which the taxpayer excludes income under §911
- IRC §24(h)(5), §24(i)(1) — Refundable per-child cap, inflation-adjusted ($1,700 for 2025 and 2026)
- 2025 Schedule 8812 and Instructions — Part II-A, II-B, Earned Income Chart/Worksheet
- PATH Act of 2015 — refund timing for returns claiming ACTC/EITC
- Rev. Proc. 2024-40 §2.06 — 2025 EIC amounts; Rev. Proc. 2025-32 §4.05(2) — 2026 refundable cap $1,700
