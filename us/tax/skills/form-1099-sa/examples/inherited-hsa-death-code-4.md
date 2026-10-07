# Example: Inherited HSA — Non-Spouse Beneficiary (Code 4)

A beneficiary inherits an HSA after the original account holder dies. The beneficiary is **not the spouse** (in this example, an adult child), so the HSA stops being an HSA on the date of death and its fair market value on that date becomes ordinary income to the beneficiary for the year of death.

This case demonstrates Code 4 distribution treatment, the pre-death QME deduction, the absence of the 20% penalty (death exception), and the practical estate-planning ramifications.

## The filers

- **Decedent**: Robert Hayes (HSA account holder)
  - Died: March 18, 2025
  - Age at death: 67
  - HSA balance on date of death: $48,500
- **Beneficiary**: Sophie Hayes (Robert's adult daughter)
  - Age: 34
  - Filing status: Single
  - Tax year: 2025 (filing in 2026)
- **HSA custodian**: Lively (Robert's HSA was at Lively)
- **Robert's pre-death medical bills paid by Sophie**: $2,800 (specifically: a March 10 emergency room visit, prescription costs from January-March, and an unpaid co-pay from late February)

## Inputs gathered

### 1099-SA from Lively (issued in Sophie's name as beneficiary)

```
PAYER: Lively, <payer TIN as printed on the form>
RECIPIENT: Sophie Hayes, SSN ***-**-XXXX
(Note: Sophie's SSN; not Robert's — the 1099-SA issues in the recipient's name)

Box 1 (Gross distribution):                $48,500
Box 2 (Earnings on excess):                $0
Box 3 (Distribution code):                 4 (Death distribution other than code 6 — paid in the year of death)
Box 4 (FMV on date of death):              $48,500 (matches Box 1; distributed shortly after death)
Box 5 (Account type):                      [HSA checked]
```

### Distribution mechanics

Robert had named Sophie as his sole HSA beneficiary on his Lively beneficiary designation form. After Robert's death:

1. Sophie provided Lively with a death certificate (March 25, 2025)
2. Lively closed Robert's HSA and distributed $48,500 in cash to Sophie on April 8, 2025
3. The distribution arrived in Sophie's bank account; she now has it as ordinary cash

Sophie cannot keep the inherited HSA as an HSA — only a **spouse beneficiary** is treated as the new account holder (IRC §223(f)(8)(A)). For non-spouse beneficiaries (children, parents, siblings), the account stops being an HSA on the date of death (IRC §223(f)(8)(B)).

### Pre-death qualified medical expenses

Sophie used $2,800 of her own funds to pay Robert's pre-death medical bills:

| Date | Provider | Amount | What |
|------|----------|--------|------|
| Apr 5, 2025 | Memorial Hospital | $2,400 | Robert's March 10 ER visit (post-billing) |
| May 12, 2025 | CVS | $250 | Robert's January-March prescription refills (final bill) |
| Apr 22, 2025 | Dr. Patel | $150 | Unpaid co-pay from Feb 28 visit |
| **Total** | | **$2,800** | |

These are **Robert's** medical expenses incurred before his death (or for services rendered before death). Sophie paid them after his death using non-HSA funds.

Per IRC §223(f)(8)(B)(ii)(I), Sophie can subtract the deceased's pre-death QME (paid within 1 year after death) from her taxable inheritance.

## Step-by-step computation

### Step 1 — Confirm Box 5 = HSA → Form 8889

Yes.

### Step 2 — Box 3 = Code 4 (Death distribution, year of death)

Treatment:
- The FMV on the date of death (Box 4, $48,500) is **ordinary income** to Sophie for 2025, the year of death; earnings after death (Box 1 − Box 4) would be other income, here $0
- Sophie can subtract pre-death QME she paid within 1 year after death (here: $2,800)
- **No 20% additional tax** (death exception per IRC §223(f)(4)(B))
- **No 6% excise** (no excess contribution at issue)

### Step 3-5 — Form 8889 Part II computation

The 2025 Instructions for Form 8889 ("Death of Account Beneficiary") tell a non-spouse beneficiary to write "Death of HSA account beneficiary" across the top of Form 8889, enter their own name and SSN, skip Part I, and complete Part II. Sophie reports:

```
Line 14a (FMV of the HSA on the date of death):  $48,500
Line 14b (Rollovers):                        $0  (rollovers not available to non-spouse)
Line 14c (14a − 14b):                        $48,500
Line 15 (Robert's pre-death QME Sophie paid within 1 year after death): $2,800
Line 16 (Taxable distributions):             $45,700  (= $48,500 − $2,800)
Line 17a (Exception):                        Death exception
Line 17b (20% additional tax):               $0  (death exception applies)
```

The $2,800 on Line 15 is Sophie's payment of Robert's pre-death QME with non-HSA funds; the instructions put it on Line 15 for a beneficiary other than the estate. No separate statement is required by the instructions; keep the receipts and the death certificate.

## The completed Form 8889 Part II draft

```markdown
# Form 8889 Part II — DRAFT for tax year 2025
(Beneficiary's tax return — Sophie Hayes, inheritor of Robert Hayes's HSA)
Header text across the top: "Death of HSA account beneficiary"; Part I skipped

## 1099-SA(s) received

| Custodian | Box 1   | Box 2 | Box 3 | Box 4   | Box 5 |
|-----------|---------|-------|-------|---------|-------|
| Lively    | $48,500 | $0    | 4     | $48,500 | HSA   |
| **Total** | $48,500 |       |       |         |       |

## Pre-death QME breakdown (deceased's medical expenses paid by beneficiary within 1 year of death)

| Provider           | Date Paid | Amount | Service Date | Receipts? |
|--------------------|-----------|--------|--------------|-----------|
| Memorial Hospital  | Apr 5, 2025 | $2,400 | March 10, 2025 (pre-death) | Yes |
| CVS Pharmacy       | May 12, 2025 | $250 | Jan-Mar 2025 (pre-death)   | Yes |
| Dr. Patel          | Apr 22, 2025 | $150 | Feb 28, 2025 (pre-death)   | Yes |
| **Total**          |           | **$2,800** |                       |           |

## Form 8889 Part II — line-by-line

14a. FMV on date of death:                       $48,500
14b. Rollovers:                                  $0  (not available to non-spouse beneficiary)
14c. Subtract 14b from 14a:                      $48,500
15.  Qualified medical expenses (Robert's
     pre-death QME paid within 1 year):          $2,800
16.  Taxable HSA distributions (14c − 15):       $45,700  → Schedule 1 Line 8f
17a. Exception reason:                           Death of HSA holder (Robert Hayes, March 18, 2025)
17b. Additional 20% tax:                         $0  (death exception, IRC §223(f)(4)(B))

## Records to keep (not attached)
Death certificate, beneficiary designation, the custodian's distribution statement, and receipts for the $2,800 of pre-death QME paid within 1 year after death (IRC §223(f)(8)(B)(ii)(I)).

## Required attachments
- [x] Form 8889 (headed "Death of HSA account beneficiary")
- [ ] Form 5329 — N/A
- [ ] Form 8853 — N/A

## Validation summary
- Math: all checks passed
  - Line 14c = $48,500 ✓
  - Line 15 = $2,800 (substantiated, all within 1 year of death) ✓
  - Line 16 = $45,700 ✓
  - Line 17b = $0 (death exception) ✓
- Sanity:
  - Box 3 = 4 → non-spouse beneficiary; no rollover available ✓
  - Box 4 = $48,500 (FMV on date of death) — the amount entered on Line 14a; Box 1 − Box 4 = $0 earnings after death ✓
  - 20% penalty waived under death exception ✓
  - Pre-death QME within 1 year of death — all paid by April-May 2025, well within 1 year of March 18 death ✓
- Next steps:
  - Schedule 1 Line 8f: $45,700 (added to Sophie's AGI as ordinary income for tax year 2025)
  - Sophie's marginal rate: at her income (~$85K) she'll pay ~24% federal on the $45,700 = ~$10,968 in federal income tax
  - State income tax: depends on Sophie's state; most states tax ordinary income similarly
  - Schedule 2 Line 17c: $0 (no additional tax)
  - **Estate tax**: separately, Robert's estate may owe estate tax on Form 706 if his total estate exceeds the federal basic exclusion amount ($13,990,000 for 2025, Rev. Proc. 2024-40) — likely not applicable, but the executor confirms. Any estate tax attributable to the HSA is deductible by Sophie (IRC §223(f)(8)(B)(ii)(II))

## Sources cited in this draft
- IRS Form 1099-SA (Rev. April 2025)
- IRS Instructions for Forms 1099-SA and 5498-SA (2025)
- IRS Form 8889 (2025) and 2025 Instructions, "Death of Account Beneficiary"
- IRS Pub 969 (HSAs and Other Tax-Favored Health Plans)
- IRC §223(f)(8)(B) (non-spouse beneficiary; (ii)(I) deceased's QME paid within 1 year)
- IRC §223(f)(8)(A) (spouse beneficiary — not applicable here)
- IRC §223(f)(4)(B) (death exception to 20% tax)
```

## Why each non-obvious choice

**Why is the entire $48,500 taxable to Sophie?** When a non-spouse beneficiary inherits an HSA, the account stops being an HSA on the date of the account holder's death, and the FMV on that date is included in the beneficiary's income for the taxable year that includes the date of death (IRC §223(f)(8)(B)(i)). Compare to a spouse beneficiary, who is treated as the account holder and keeps the HSA (IRC §223(f)(8)(A)) — non-spouse beneficiaries have no such option.

**Why no 20% additional tax?** IRC §223(f)(4)(B) waives the 20% additional tax in the case of death. Sophie's 20% would have been $9,140 — significant savings, but the exception only applies to the 20% penalty, not to the underlying income tax.

**Why does the $2,800 reduction work?** IRC §223(f)(8)(B)(ii)(I) explicitly reduces a non-estate beneficiary's income by the deceased's QME incurred before death and paid within 1 year after death. This is a one-time, narrow rule designed to ease the tax burden when the deceased had unpaid medical bills at death.

**How does the IRS know Sophie is a beneficiary?** The heading "Death of HSA account beneficiary" across the top of Form 8889 tells it; the instructions call for that heading instead of an attached statement.

**Why does the death certificate matter?** It's the substantiation for the death exception. If audited, the IRS will request the death certificate. Sophie should retain a certified copy.

**Could Sophie disclaim the inheritance?** Yes, under IRC §2518 a beneficiary can disclaim within 9 months of death. The HSA would then pass to the contingent beneficiary or to Robert's estate. If the estate is the beneficiary, the FMV is included in Robert's own income on his final return (IRC §223(f)(8)(B)(i)(II)), and the 1-year QME reduction does not apply to the estate. Refer this choice to an estate attorney.

**What if Sophie hadn't paid Robert's pre-death medical bills?** She'd lose the $2,800 reduction. Line 16 would be the full $48,500. She'd pay tax on the full amount.

**What about state tax?** Most states follow the federal treatment, but not all: California does not conform to IRC §223, so HSA amounts are adjusted on Schedule CA (540) (FTB, Instructions for Schedule CA (540)). Verify Sophie's state's specific rule.

**Could Robert have done estate planning to avoid this?** Several options exist:
1. **Spend down the HSA before death**: if Robert knew his health was failing, he could have used the HSA aggressively for QME, reducing the balance.
2. **Name his spouse as beneficiary** (if he had one — Robert was apparently single or widowed, so this didn't apply).
3. **Name a charity as beneficiary**: a charity inherits the HSA tax-free at the entity level (charities don't pay income tax).
4. **Name his estate**: doesn't help — the FMV lands on Robert's final return instead.

This is **estate planning advice** — out of scope for Form 1099-SA / Form 8889 reporting. Refer Sophie or the family to an estate planner.

## Audit defense

If the IRS questioned Sophie's Form 8889:
1. Sophie presents Robert's death certificate (showing March 18, 2025)
2. Sophie presents the Lively account statement showing the $48,500 distribution to her bank account on April 8, 2025
3. Sophie presents receipts for the $2,800 in pre-death QME, all paid by her in April-May 2025 (within 1 year of death)
4. Sophie's Schedule 1 Line 8f shows $45,700 added to AGI, and Form 8889 carries the "Death of HSA account beneficiary" heading
5. Sophie's Schedule 2 Line 17c shows $0 (death exception applied)

The audit would close without changes. Sophie's record retention — death certificate, bank statements, QME receipts, beneficiary designation form — is the model for inherited-HSA reporting.
