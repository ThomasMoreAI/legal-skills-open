# Qualifying Relative Test (for Credit for Other Dependents)

The four tests a person must meet to be a "qualifying relative" for purposes of the $500 Credit for Other Dependents (ODC) on Schedule 8812. Authority: IRC §24(h)(4) (which references IRC §152(d)).

A "qualifying relative" can be claimed as a dependent on Form 1040, but doesn't have to meet the stricter "qualifying child" tests. The ODC at $500 is significantly less generous than the CTC at $2,000, but it's still a credit worth claiming.

If the dependent is a qualifying child for CTC (see [`qualifying-child-test.md`](./qualifying-child-test.md)), the agent should classify them as CTC instead — they don't double-count for both.

---

## Test 1 — Not a qualifying child

The person must NOT be a qualifying child of the filer or any other taxpayer for the year.

**Common case**: a 17-year-old child who lived with the filer all year. Fails the qualifying-child age test (Test 2 in the qualifying-child reference) but can still be a qualifying relative.

**Edge case**: a child who is a qualifying child of someone else (e.g., the filer's grandchild who is the qualifying child of the grandchild's parent). The person CAN'T be a qualifying relative of the filer if they're already a qualifying child of someone else, even if that other person doesn't claim them.

The "tiebreaker" rules under IRC §152(c)(4) apply if multiple people could claim the child.

---

## Test 2 — Relationship OR Member-of-Household

The person must EITHER:

**(a) Be related to the filer** in one of these ways (IRC §152(d)(2)):

- Child or descendant (son, daughter, grandchild, great-grandchild, etc.) — note: under-17 children typically meet qualifying-child test, but a 17+ child or a child without SSN qualifies here as relative
- Sibling (brother, sister, half-sibling, step-sibling)
- Parent, grandparent, great-grandparent (or other ancestor)
- Stepparent
- Niece or nephew
- Aunt or uncle
- Son-in-law, daughter-in-law, father-in-law, mother-in-law, brother-in-law, sister-in-law

**Important**: cousins are NOT in this list. A cousin must meet the member-of-household test (b) instead.

**OR (b) Be a member of the filer's household** for the entire year as the filer's principal place of abode. This applies to:

- A boyfriend, girlfriend, or domestic partner (in most states; some states' relationships violate local law and the IRS won't honor the relationship)
- A friend living with the filer
- A cousin living with the filer

**Local law restriction**: if the relationship between filer and the person living in their household violates local law (e.g., living arrangement is illegal under state law where the home is located), the person is NOT a qualifying relative under the member-of-household test.

---

## Test 3 — Gross income limit

The person's gross income for the year must be less than the **exemption amount** (which became $0 under TCJA but, for §152(d) purposes, the IRS has continued to publish an inflation-adjusted figure).

For tax year 2025: $5,200 (Rev. Proc. 2024-40, table 22).
For tax year 2026: verify against the latest Revenue Procedure (typically issued in October-November of the prior year).

**Gross income** includes:
- Wages, salaries, tips (after pre-tax deductions)
- Self-employment net earnings
- Interest and dividends
- Rental income
- Gambling winnings
- Unemployment benefits

**Gross income does NOT include**:
- Social Security benefits (typically — though some Social Security may be taxable depending on overall income)
- Tax-free scholarships used for tuition
- Tax-exempt interest (usually)
- Most veterans' benefits

**Common scenario**: claiming an elderly parent. If the parent receives only Social Security ($25,000/year), their gross income for §152(d) purposes is $0 (Social Security excluded). They can be claimed as a qualifying relative if other tests are met.

**Common scenario**: claiming an adult child. If the adult child works and earned $7,000 of wages in the year, they exceed the $5,200 limit and are NOT a qualifying relative. The filer cannot claim them at all.

---

## Test 4 — Support

The filer must have provided **more than half** of the person's total support during the year.

**Total support** = the dollar value of:
- Lodging (fair rental value of housing, including utilities, repairs, insurance attributable to the person's portion)
- Food
- Clothing
- Education
- Medical and dental care
- Recreation
- Transportation

Sum the total support, then determine what fraction the filer paid. If filer paid > 50%, this test passes.

**Multiple support agreements** (Form 2120, IRC §152(d)(3)): if no one person provided > 50% support, but a group of two or more taxpayers together provided > 50%, the group can agree that one of them claims the dependent. The other group members must file Form 2120 declaring they will not claim. Common case: siblings supporting an elderly parent — typically the sibling with the highest tax liability claims, while others sign Form 2120.

**Support that doesn't count**: scholarships received by a student (IRC §152(f)(5)), TANF and other welfare payments, food stamps. These reduce the total support amount but are not attributed to the recipient.

The agent must ASK: "Did you (and your spouse if MFJ) provide more than half of [name]'s support during the year?"

---

## Quick decision tree

```
Is the person a qualifying child of the filer or anyone else?
├── Yes → Qualifying child takes precedence; not a qualifying relative.
└── No
    Is the person related to the filer (per IRC §152(d)(2) list) OR a full-year household member?
    ├── No → Not a qualifying relative; cannot be claimed as dependent.
    └── Yes
        Is the person's gross income < $5,200 (2025; verify 2026)?
        ├── No → Not a qualifying relative.
        └── Yes
            Did the filer (and spouse if MFJ) provide > 50% of total support?
            ├── No → Check if Form 2120 multiple support agreement applies.
            │       If yes → Qualifying relative under multiple support rule.
            │       If no  → Not a qualifying relative.
            └── Yes → Qualifying relative for ODC ($500 credit).
```

---

## Common scenarios

### Adult child, age 22, full-time student living at home, earning $4,000

- Test 1 (not qualifying child): test fails for the qualifying-child relationship test if 22+ unless full-time student under 24 — *might be qualifying child* under §152(c)(3) (student exception extends to age 24). Verify before classifying as relative.
- If qualifying child (full-time student under 24), they go on CTC line **only if they're under 17 with SSN** — they're not, so ODC at $500.
- Wait — qualifying-child status for §24(c) requires under-17, regardless of student status. The student exception extends the qualifying-child *general* dependency to age 24, but for CTC specifically, the age cap is 17. So:
  - Adult full-time student under 24 = qualifying child for general dependency / EITC, but not for CTC
  - Eligible for ODC ($500) if all other tests met (gross income < $5,200, etc.)

### Elderly parent, age 71, lives alone, receives $25,000 Social Security

- Test 1 (not qualifying child): pass (parents are never qualifying children of their kids)
- Test 2 (relationship): pass (parent is in the §152(d)(2) list)
- Test 3 (gross income): Social Security typically excluded → gross income $0 < $5,200 → pass
- Test 4 (support): Did the filer pay > 50% of parent's total support? Including rent, food, utilities, medical, etc. Often yes if filer pays a major nursing home bill or assisted living. Verify with user.

If all 4 tests pass: Claim parent as ODC.

### Domestic partner, lives with filer all year, gross income $3,000

- Test 1 (not qualifying child): pass (adults aren't qualifying children typically)
- Test 2 (relationship): no relationship by blood/marriage → must qualify under member-of-household test. Lived with filer all year as principal abode → pass.
- Test 3 (gross income): $3,000 < $5,200 → pass
- Test 4 (support): If filer provided > 50% → pass

If all 4 tests pass and the relationship doesn't violate local law: Claim domestic partner as ODC.

### Niece, age 14, lives with filer all year, parent unable to care

- Test 1 (qualifying child): niece IS in the qualifying-child relationship list (descendant of sibling). Age 14 < 17 → potentially qualifying child if all 7 tests pass.
- If niece is a qualifying child of the filer, she goes on CTC at $2,000 — not ODC.
- Watch the SSN-by-due-date test (Test 7 of qualifying child) — if niece has SSN, she's CTC. If she has ITIN, she's ODC ($500).

---

## What the agent must ASK

For each dependent the user wants to claim as ODC, the agent must collect:

1. Relationship to filer (parent, grandparent, sibling, friend, etc.)
2. Did the person live with the filer all year? (For non-relatives only)
3. Person's gross income for the year
4. Did the filer (and spouse if MFJ) provide more than half of the person's total support?
5. Did the person file a joint return for the year?
6. Is the person a U.S. citizen, national, or resident alien?
7. (If multiple supporters) Are you using Form 2120 multiple support agreement?

Without these answers, ODC eligibility is a guess.

---

## Special: ODC SSN/ITIN/ATIN requirement

ODC under IRC §24(h)(4)(B) requires the dependent to have a **Taxpayer Identification Number (TIN)** issued by the due date of the return. Unlike CTC, ODC accepts:

- SSN
- ITIN
- ATIN

So a dependent with an ITIN qualifies for ODC ($500) even though they don't qualify for CTC ($2,000).

Without ANY taxpayer identification number, the dependent cannot be claimed for ODC. The agent must confirm each ODC dependent has a TIN.

---

## Authority

- IRC §24(h)(4) — Credit for Other Dependents (added by TCJA 2017)
- IRC §24(h)(4)(B) — TIN requirement for ODC
- IRC §152(d) — Qualifying relative general definition
- IRC §152(d)(1)(B) — Gross income limit
- IRC §152(d)(2) — Relationship list
- IRC §152(d)(3) — Multiple support agreements (Form 2120)
- IRC §152(f)(5) — Scholarships not "provided by recipient"
- Form 2120 — Multiple Support Declaration
- Rev. Proc. 2024-40 — 2025 inflation adjustments (gross income limit $5,200)
- Pub 501 — Dependents, Standard Deduction, and Filing Information
