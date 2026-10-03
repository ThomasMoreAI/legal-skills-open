# Common Schedule 8812 Mistakes (with Citations)

The audit-trip mistakes filers make on Child Tax Credit / ACTC / Credit for Other Dependents, with the IRC, Pub 972, or form authority showing why each is wrong.

---

## 1. Claiming a 17-year-old as a qualifying child

**The mistake**: parent's child turned 17 during the tax year (e.g., child born December 1, 2008 → age 17 on December 1, 2025). Parent claims them as qualifying child for CTC, getting $2,000.

**Why it's wrong**: IRC §24(c)(1) — qualifying child for CTC must be **under age 17** at the end of the tax year. A child who reached 17 during the year fails the test.

**Correct approach**: claim the child as Other Dependent for ODC ($500), not CTC ($2,000). The credit drops by $1,500.

**Authority**: IRC §24(c)(1).

---

## 2. Claiming CTC for a child with an ITIN

**The mistake**: parent's child has an ITIN (Individual Taxpayer Identification Number) instead of an SSN. Parent claims CTC for the child.

**Why it's wrong**: IRC §24(h)(7) — added by TCJA 2017 — requires the qualifying child to have a Social Security Number issued by the due date of the return (including extensions). ITIN does not qualify.

**Correct approach**: claim the child as Other Dependent for ODC ($500). ODC accepts ITIN, ATIN, or SSN.

**Authority**: IRC §24(h)(7); IRC §24(h)(4)(B).

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

**The mistake**: high-income filer (e.g., MFJ AGI $450,000) claims full $4,000 CTC for 2 children, ignoring the phase-out.

**Why it's wrong**: IRC §24(b) — phase-out begins at $200K (single) / $400K (MFJ) and reduces credit by $5 per $1,000 (rounded up) of MAGI above the threshold.

**Correct calculation** (MFJ, $450K MAGI, 2 children):
- Tentative: 2 × $2,000 = $4,000
- Excess: $50,000
- Reduction: $50,000 / 1,000 × $5 = $250
- Allowed: $4,000 − $250 = $3,750

**Authority**: IRC §24(b)(1).

---

## 5. Computing phase-out reduction without rounding excess up to next $1,000

**The mistake**: filer with MAGI $400,500 (MFJ) computes excess as $500 and reduction as $2.50.

**Why it's wrong**: IRS instructions and the statute round excess **up** to the next $1,000. Excess $500 becomes $1,000, reduction $5.

**Correct approach**: `Excess (rounded up) = ceiling(Excess MAGI / 1,000) × 1,000`. Always round up to the nearest $1,000.

**Authority**: IRC §24(b)(1); Schedule 8812 Instructions.

---

## 6. Claiming ACTC with earned income at or below $2,500

**The mistake**: filer with $2,000 earned income (very low income) claims ACTC.

**Why it's wrong**: IRC §24(d)(1)(B)(i) — ACTC requires earned income greater than $2,500. The 15% method computes from the excess over $2,500.

**Correct approach**: ACTC = $0 when earned income ≤ $2,500. The non-refundable CTC may still be available if there's tax liability, but no refund.

**Authority**: IRC §24(d)(1)(B)(i).

---

## 7. Forgetting the per-child refundable cap

**The mistake**: filer has 1 qualifying child, leftover credit of $2,000, earned income excess of $30,000. Claims $2,000 of ACTC.

**Why it's wrong**: IRC §24(h)(5) caps the refundable per-child amount at $1,700 (2025; verify 2026). Even with leftover $2,000 and earned income method showing $4,500, the cap is $1,700.

**Correct approach**: ACTC = min($2,000 leftover, $4,500 EI method, $1,700 per-child cap) = $1,700.

**Authority**: IRC §24(h)(5).

---

## 8. Confusing CTC with the Childcare Credit (Form 2441)

**The mistake**: filer thinks the "Child Tax Credit" covers daycare expenses they paid while working.

**Why it's wrong**: the Child Tax Credit is per-child (up to $2,000 each). The Child and Dependent Care Credit (Form 2441) is for daycare expenses while parent works. They are separate credits and computed on separate forms.

**Correct approach**: claim CTC on Schedule 8812 AND claim Childcare Credit on Form 2441 (if eligible). Both credits appear on different lines of Form 1040.

**Authority**: IRC §24 (CTC); IRC §21 (Child and Dependent Care Credit); Form 2441.

---

## 9. Claiming an elderly parent for CTC instead of ODC

**The mistake**: filer claims parent as a "qualifying child" — perhaps confusing dependent eligibility with the CTC age test.

**Why it's wrong**: a parent is never a "qualifying child" (qualifying child must be filer's descendant or sibling-related). Parents are qualifying relatives under IRC §152(d).

**Correct approach**: claim parent as Other Dependent for ODC ($500), not CTC. Parent must meet the gross income test ($5,200 for 2025; verify 2026) and the support test (filer provided > 50% of support).

**Authority**: IRC §152(c) (qualifying child relationship list); IRC §152(d) (qualifying relative); IRC §24(h)(4) (ODC).

---

## 10. Using AGI instead of MAGI when foreign income is excluded

**The mistake**: filer with foreign earned income exclusion (Form 2555) uses AGI for the phase-out test, getting a larger credit than allowed.

**Why it's wrong**: IRC §24(b)(2) — MAGI for CTC purposes includes the foreign earned income exclusion (and foreign housing exclusion/deduction) added back. Schedule 8812 Worksheet A walks through this.

**Correct approach**: MAGI = AGI + Form 2555 Line 45 (foreign earned income exclusion) + Form 2555 Line 50 (foreign housing exclusion) + certain Puerto Rico/territories income. Use MAGI for phase-out, not AGI.

**Authority**: IRC §24(b)(2); Schedule 8812 Instructions Worksheet A.

---

## 11. Failing to use the SS-tax method for 3+ qualifying children when it would help

**The mistake**: filer with 3+ qualifying children, low earned income (< $20,000), substantial Social Security/Medicare withholding. Uses only the 15% earned income method and gets a small ACTC.

**Why it's wrong**: IRC §24(d)(1)(B)(ii) — for 3+ qualifying children, the alternative SS-tax method (SS+Medicare+½SE − EITC) may produce a larger ACTC. The filer (or agent) should compute both and use the larger.

**Correct approach**: when N_CTC ≥ 3, compute both methods explicitly. Use the larger.

**Authority**: IRC §24(d)(1)(B)(ii); Schedule 8812 Part II-B.

---

## 12. Filing Schedule 8812 for a dependent who hasn't been included on Form 1040 as a dependent

**The mistake**: filer lists a child only on Schedule 8812 (the credit form) but forgets to list the child as a dependent in the dependents section of Form 1040.

**Why it's wrong**: a dependent must first be claimed on Form 1040 (with name, SSN, relationship, and CTC/ODC checkbox marked). Schedule 8812 then references the dependents already listed on Form 1040. If the dependent isn't on Form 1040, the IRS will not allow the credit.

**Correct approach**: list each dependent on Form 1040 with the appropriate CTC or ODC box checked, then complete Schedule 8812 to compute the credit value.

**Authority**: Form 1040 Instructions; Schedule 8812 Instructions.
