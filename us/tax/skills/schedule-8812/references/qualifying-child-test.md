# Qualifying Child Test (for Child Tax Credit)

The seven tests a person must meet to be a "qualifying child" for purposes of the Child Tax Credit on Schedule 8812. Authority: IRC §24(c) (which cross-references §152(c)) plus the additional SSN-by-due-date requirement under IRC §24(h)(7).

If any one test fails, the dependent is NOT a qualifying child for CTC. They may still be a qualifying relative for the Credit for Other Dependents (ODC) — see [`qualifying-relative-test.md`](./qualifying-relative-test.md).

---

## Test 1 — Relationship

The child must be the filer's:

- Son or daughter (biological, adopted, or foster)
- Stepson or stepdaughter
- Brother, sister, half-brother, half-sister, stepbrother, stepsister
- Descendant of any of the above (e.g., grandchild, niece, nephew, great-grandchild)

**Adopted child**: an adopted child is treated the same as a biological child for all CTC purposes. A child placed for adoption with the filer (not yet finalized) also qualifies if living with the filer.

**Foster child**: must be placed by an authorized placement agency or by judgment, decree, or other order of any court of competent jurisdiction.

**Not eligible by relationship**:
- Cousins
- Aunts and uncles
- Domestic partner's child (unless they meet stepchild test through marriage)
- A child the filer cares for informally without legal placement

---

## Test 2 — Age

The child must be **under age 17** at the end of the tax year.

**Critical distinction**: "under 17" means the child cannot have reached age 17 during the year. A child born December 30, 2008 reaches age 17 on December 30, 2025 — they are NOT a qualifying child for tax year 2025 CTC. They may still be a qualifying relative for ODC.

A child who turned 17 during the year:
- Was a qualifying child for CTC for the year they were 16
- Is now an "Other Dependent" for ODC purposes ($500 credit)

**Edge case**: a child born on December 31 of the tax year is age 0 for the entire year and qualifies if all other tests are met.

---

## Test 3 — Residency

The child must have lived with the filer for **more than half** of the tax year (more than 183 days, with leap-year adjustments).

**Temporary absences** count as residency: education, illness, business, vacation, military service, juvenile detention. The child still "resides" with the filer during these absences.

**Birth or death during the year**: a child born OR dying during the year is treated as having lived with the filer for the entire year, provided the home was the child's home from birth (or until death).

**Children of divorced or separated parents**: the special rule under IRC §152(e) applies. The custodial parent generally claims the child, but they can release the claim to the noncustodial parent via Form 8332. The noncustodial parent (with Form 8332 attached) can then claim CTC for the released year. The custodial parent retains the right to:
- Filing status (Head of Household if otherwise eligible)
- Earned Income Tax Credit
- Child and Dependent Care Credit (Form 2441)

**Tiebreaker rules** under IRC §152(c)(4) when two taxpayers each claim the same child:
1. If only one is the parent, the parent wins
2. If both are parents and they file jointly together, no tiebreaker needed
3. If both are parents and they don't file jointly, the parent with whom the child lived longer wins; if equal time, higher AGI wins
4. If neither is the parent, highest AGI wins

The agent must ASK if the user is divorced/separated or shares custody.

---

## Test 4 — Support

The child must NOT have provided more than half of their own support during the year.

**Support** includes: lodging, food, clothing, education, medical expenses, recreation, and transportation. Calculated as the dollar value of total support, of which the child's own contribution is the relevant fraction.

**Common scenarios**:
- A teenage child who works a part-time job — typically does not provide >50% of own support; their wages are usually for personal items, not full living costs
- A college-age child living at home — typically does not provide >50% if parents pay rent/food/tuition
- A child who received scholarships — scholarships do NOT count as "support provided by the child" under IRC §152(f)(5)
- A child who received support from a third party (e.g., grandparent, government program) — that support is not "provided by the child"

If the child is age 17+ and earns substantial income, the support test may be a problem. But age 17+ already disqualifies them for CTC anyway (Test 2). For CTC, this test typically passes for under-17 children.

---

## Test 5 — Joint return

The child must NOT have filed a joint return for the year, **unless** the joint return was filed only to claim a refund of withheld income tax or estimated tax paid.

**Common case**: a 16-year-old who married (legally somewhere). If they file jointly with their spouse and they had taxes withheld, and they filed jointly to get the refund, the child can still be claimed. If they filed jointly because they had any non-zero tax liability beyond getting refund, they are disqualified.

Most under-17 children have never married; this test usually trivially passes.

---

## Test 6 — Citizenship

The child must be a:

- U.S. citizen
- U.S. national (e.g., from American Samoa or some Northern Mariana Islands residents)
- U.S. resident alien (i.e., met the substantial presence test under IRC §7701(b))

**Not eligible**:
- Nonresident alien (NRA), even if living in the U.S.
- Resident of Mexico or Canada who lived in the U.S. less than half the year (special rules apply for some adopted children — see Pub 501)

**Adopted child special rule (IRC §152(b)(3)(B))**: an adopted child who is not a U.S. citizen, national, or resident alien generally qualifies if they lived with the filer all year as a member of the filer's household and the filer is a U.S. citizen or national.

---

## Test 7 — SSN by due date (CTC-specific, IRC §24(h)(7))

This is the test that applies to CTC but NOT to general dependency. A qualifying child for CTC purposes must have a **Social Security Number issued by the due date of the return** (including extensions).

**Required**: SSN. Not eligible: ITIN, ATIN.

**Why this matters**: a child with an ITIN can still be claimed as a dependent on Form 1040 (and counts for ODC = $500), but cannot be a qualifying child for CTC.

**Common scenarios**:
- Newborn whose SSN application is pending — the parent should apply for the SSN ASAP. If the SSN is issued before the original April 15 due date or by the October 15 extended due date, CTC is available. If not, ODC instead.
- An adopted child who was issued an ATIN (Adoption Taxpayer ID Number) — ATIN does not qualify for CTC; ODC only. After adoption finalizes and SSN issues, future years can claim CTC.
- A non-citizen child who has an ITIN — ITIN does not qualify for CTC; ODC if otherwise eligible as a dependent.

The agent must explicitly ASK the user: "Does each child you're claiming have a Social Security Number that was issued by the due date of your tax return (including any extension you filed)?" If the answer is "ITIN" or "still waiting for SSN past October 15," the child cannot be claimed for CTC for the year — only ODC.

---

## Quick decision tree

```
Is the dependent the filer's son, daughter, brother, sister, or descendant?
├── No → Not a qualifying child. Check qualifying-relative-test.md for ODC.
└── Yes
    Is the dependent under age 17 on December 31?
    ├── No → Not a qualifying child. Likely qualifying relative for ODC.
    └── Yes
        Did the dependent live with the filer more than half the year?
        ├── No → Not a qualifying child (with exceptions for divorced parents).
        └── Yes
            Did the dependent provide > 50% of their own support?
            ├── Yes → Not a qualifying child.
            └── No
                Did the dependent file a joint return (other than for refund only)?
                ├── Yes → Not a qualifying child.
                └── No
                    Is the dependent a U.S. citizen, national, or resident alien?
                    ├── No → Not a qualifying child (with adopted-child exception).
                    └── Yes
                        Does the dependent have an SSN issued by the due date?
                        ├── No → Qualifying relative for ODC, not CTC.
                        └── Yes → Qualifying child for CTC + ODC.
```

---

## What the agent must ASK

For each dependent the user claims, the agent must collect:

1. Relationship (son, daughter, niece, etc.)
2. Birthdate
3. Did the child live with you more than half the year?
4. Did you provide more than half of their support?
5. Did the child file a joint return for the year?
6. Is the child a U.S. citizen, national, or resident alien?
7. Does the child have an SSN issued by the due date of the return?
8. (If divorced/separated) Are you the custodial parent? Have you signed Form 8332 releasing the claim?

Without these answers, the classification is a guess. The agent must NOT default to "yes, qualifying child" without confirmation.

---

## Authority

- IRC §24(c) — Definition of qualifying child for CTC
- IRC §24(h)(7) — SSN-by-due-date requirement (added by TCJA 2017)
- IRC §152(c) — Qualifying child general definition
- IRC §152(c)(4) — Tiebreaker rules
- IRC §152(e) — Children of divorced or separated parents
- IRC §152(b)(3)(B) — Adopted child citizenship exception
- Form 8332 — Release/Revocation of Release of Claim to Exemption for Child by Custodial Parent
- Pub 501 — Dependents, Standard Deduction, and Filing Information
- Pub 596 — Earned Income Credit (parallel qualifying child test)
- Pub 972 — Child Tax Credit (historical reference)
