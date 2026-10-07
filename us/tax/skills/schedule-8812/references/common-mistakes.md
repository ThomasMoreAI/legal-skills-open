# Common Schedule 8812 Mistakes (with Citations)

The audit-trip mistakes filers make on Child Tax Credit / ACTC / Credit for Other Dependents, with the IRC or form authority showing why each is wrong. Line numbers refer to the 2025 Schedule 8812 (re-check the current revision at https://www.irs.gov/forms-pubs/about-schedule-8812-form-1040).

---

## 1. Claiming a 17-year-old as a qualifying child

**The mistake**: parent's child turned 17 during the tax year (e.g., child born December 1, 2008 → age 17 on December 1, 2025). Parent claims them as qualifying child for CTC, getting $2,200.

**Why it's wrong**: IRC §24(c)(1) — qualifying child for CTC must be **under age 17** at the end of the tax year. A child who reached 17 during the year fails the test.

**Correct approach**: claim the child as Other Dependent for ODC ($500), not CTC ($2,200). The credit drops by $1,700.

**Authority**: IRC §24(c)(1).

---

## 2. Claiming CTC for a child with an ITIN

**The mistake**: parent's child has an ITIN (Individual Taxpayer Identification Number) instead of an SSN. Parent claims CTC for the child.

**Why it's wrong**: IRC §24(h)(7) requires the qualifying child to have a Social Security Number valid for employment issued before the due date of the return (including extensions). ITIN does not qualify.

**Correct approach**: claim the child as Other Dependent for ODC ($500) on line 6, if the child is a U.S. citizen, national, or resident alien. ODC accepts ITIN, ATIN, or SSN issued on or before the due date.

**Authority**: IRC §24(h)(7); IRC §24(h)(4)(C); 2025 Instructions for Schedule 8812, p.1.

---

## 3. Both parents claim the same child after a divorce

**The mistake**: divorced parents each list the same child as a dependent on their respective returns. Both claim CTC.

**Why it's wrong**: IRC §152(c)(4) tiebreaker rules. Only one taxpayer can claim a child. The IRS will reject the second-filed return with code R0000-507-01 ("dependent's SSN already used").

**Correct approach**: per IRC §152(e), the **custodial parent** generally has the right. The custodial parent can release the claim to the noncustodial parent via Form 8332. Without Form 8332, the noncustodial parent cannot claim CTC.

**Tiebreaker** if both parents claim and no Form 8332 is filed:
1. Parent with whom the child lived longer wins
2. If equal time, higher AGI wins

**Authority**: IRC §152(c)(4); IRC §152(e); Form 8332.

---

## 4. Forgetting to subtract for MAGI phase-out

**The mistake**: high-income filer (e.g., MFJ AGI $450,000) claims full $4,400 CTC for 2 children, ignoring the phase-out.

**Why it's wrong**: IRC §24(b)(1), §24(h)(3) — phase-out begins at $200K (all other statuses) / $400K (MFJ) and reduces the credit by $50 per $1,000 (or fraction) of MAGI above the threshold (Schedule 8812 lines 9–11: line 11 = 5% of line 10).

**Correct calculation** (MFJ, $450K MAGI, 2 children, 2025):
- Line 8: 2 × $2,200 = $4,400
- Line 10: $50,000
- Line 11: $50,000 × 5% = $2,500
- Line 12: $4,400 − $2,500 = $1,900

**Authority**: IRC §24(b)(1); Schedule 8812 lines 9–12.

---

## 5. Computing phase-out reduction without rounding excess up to next $1,000

**The mistake**: filer with MAGI $400,500 (MFJ) computes excess as $500 and reduction as $25.

**Why it's wrong**: the form (line 10) and the statute ("or fraction thereof") round excess **up** to the next $1,000. Excess $500 becomes $1,000, reduction $50.

**Correct approach**: `Excess (rounded up) = ceiling(Excess MAGI / 1,000) × 1,000`. Always round up to the nearest $1,000.

**Authority**: IRC §24(b)(1); 2025 Schedule 8812 line 10.

---

## 6. Claiming ACTC with earned income at or below $2,500

**The mistake**: filer with $2,000 earned income (very low income) claims ACTC.

**Why it's wrong**: IRC §24(d)(1)(B)(i) and §24(h)(6) — the 15% method computes from earned income over $2,500 (Schedule 8812 lines 19–20). With 3+ qualifying children, Part II-B can still produce an ACTC from social security and Medicare taxes.

**Correct approach**: line 20 = $0 when earned income ≤ $2,500, so ACTC = $0 for filers with fewer than 3 qualifying children. The non-refundable CTC may still be available if there's tax liability, but no refund.

**Authority**: IRC §24(d)(1)(B)(i); IRC §24(h)(6).

---

## 7. Forgetting the per-child refundable cap

**The mistake**: filer has 1 qualifying child, leftover credit of $2,200, earned income over $2,500 of $30,000. Claims $2,200 of ACTC.

**Why it's wrong**: IRC §24(h)(5) (indexed by §24(i)(1)) caps the refundable per-child amount at $1,700 for 2025 and 2026 (Schedule 8812 line 16b; Rev. Proc. 2025-32 §4.05(2)). Even with leftover $2,200 and earned income method showing $4,500, the cap is $1,700.

**Correct approach**: ACTC = min($2,200 leftover, $1,700 per-child cap, $4,500 EI method) = $1,700.

**Authority**: IRC §24(h)(5); IRC §24(i)(1).

---

## 8. Confusing CTC with the Childcare Credit (Form 2441)

**The mistake**: filer thinks the "Child Tax Credit" covers daycare expenses they paid while working.

**Why it's wrong**: the Child Tax Credit is per-child (up to $2,200 each). The Child and Dependent Care Credit (Form 2441) is for daycare expenses while parent works. They are separate credits and computed on separate forms.

**Correct approach**: claim CTC on Schedule 8812 AND claim Childcare Credit on Form 2441 (if eligible). The CTC goes on Form 1040 line 19; the dependent care credit goes on Schedule 3 line 2.

**Authority**: IRC §24 (CTC); IRC §21 (Child and Dependent Care Credit); Form 2441.

---

## 9. Claiming an elderly parent for CTC instead of ODC

**The mistake**: filer claims parent as a "qualifying child" — perhaps confusing dependent eligibility with the CTC age test.

**Why it's wrong**: a parent is never a "qualifying child" (qualifying child must be filer's descendant or sibling-related). Parents are qualifying relatives under IRC §152(d).

**Correct approach**: claim parent as Other Dependent for ODC ($500), not CTC. Parent must meet the gross income test (less than $5,200 for 2025, $5,300 for 2026; Rev. Proc. 2024-40 §2.24, Rev. Proc. 2025-32 §4.23) and the support test (filer provided > 50% of support).

**Authority**: IRC §152(c) (qualifying child relationship list); IRC §152(d) (qualifying relative); IRC §24(h)(4) (ODC).

---

## 10. Using AGI instead of MAGI when foreign income is excluded

**The mistake**: filer with foreign earned income exclusion (Form 2555) uses AGI for the phase-out test, getting a larger credit than allowed.

**Why it's wrong**: IRC §24(b)(1) — MAGI for CTC purposes is AGI increased by amounts excluded under §911, §931, or §933. Schedule 8812 lines 2a–3 add these back.

**Correct approach**: line 3 = AGI (Form 1040 line 11a) + excluded Puerto Rico income (line 2a) + Form 2555 lines 45 and 50 (line 2b) + Form 4563 line 15 (line 2c). Use line 3 for the phase-out, not AGI. A Form 2555 filer also cannot claim the ACTC (Part II-A caution; IRC §24(d)(3)).

**Authority**: IRC §24(b)(1); 2025 Schedule 8812 lines 1–3.

---

## 11. Failing to use the SS-tax method for 3+ qualifying children when it would help

**The mistake**: filer with 3+ qualifying children, low earned income (< $20,000), substantial Social Security/Medicare withholding. Uses only the 15% earned income method and gets a small ACTC.

**Why it's wrong**: IRC §24(d)(1)(B)(ii) — for 3+ qualifying children, the alternative social security tax method (W-2 boxes 4 and 6 + Schedule 1 line 15 + Schedule 2 lines 5, 6, 13, minus the EIC and Schedule 3 line 11) may produce a larger ACTC. The form sends the filer to Part II-B when line 16b ≥ $5,100 and line 20 < line 17.

**Correct approach**: when N_CTC ≥ 3 and line 20 < line 17, complete lines 21–26 and use the larger of line 20 or line 25.

**Authority**: IRC §24(d)(1)(B)(ii); Schedule 8812 Part II-B.

---

## 12. Filing Schedule 8812 for a dependent who hasn't been included on Form 1040 as a dependent

**The mistake**: filer lists a child only on Schedule 8812 (the credit form) but forgets to list the child as a dependent in the dependents section of Form 1040.

**Why it's wrong**: a dependent must first be claimed on Form 1040 (with name, SSN, relationship, and CTC/ODC checkbox marked). Schedule 8812 then references the dependents already listed on Form 1040. If the dependent isn't on Form 1040, the IRS will not allow the credit.

**Correct approach**: list each dependent on Form 1040 with the appropriate CTC or ODC box checked in row (7) of the Dependents section, then complete Schedule 8812 to compute the credit value (lines 4 and 6 count those boxes).

**Authority**: 2025 Form 1040 Dependents section; 2025 Instructions for Schedule 8812, Lines 4 and 6.

---

## 13. Claiming the CTC when neither spouse has a valid SSN (new for 2025)

**The mistake**: parents who file with ITINs claim the CTC/ACTC for their U.S.-citizen child who has an SSN, as was allowed through 2024.

**Why it's wrong**: beginning with 2025 returns, the taxpayer (or at least one spouse on a joint return) must have an SSN valid for employment issued before the due date of the return (including extensions) to claim the CTC or ACTC; the other spouse needs an SSN or ITIN. This applies to original and amended 2025 returns.

**Correct approach**: if neither spouse has such an SSN, claim the ODC ($500) for each dependent instead (the filer needs an SSN or ITIN issued on or before the due date).

**Authority**: IRC §24(h)(7)(A)(i); 2025 Instructions for Schedule 8812, What's New and p.1.
