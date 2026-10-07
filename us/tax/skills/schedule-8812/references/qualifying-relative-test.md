# Qualifying Relative Test (for Credit for Other Dependents)

The four tests a person must meet to be a "qualifying relative" for purposes of the $500 Credit for Other Dependents (ODC) on Schedule 8812. Authority: IRC §24(h)(4) (which references IRC §152(d)).

A "qualifying relative" can be claimed as a dependent on Form 1040, but doesn't have to meet the stricter "qualifying child" tests. The ODC at $500 is significantly less generous than the CTC at $2,200 (2025 and 2026), but it's still a credit worth claiming. The Form 1040 instructions walk through these tests in "Who Qualifies as Your Dependent," Steps 4–5 (2025 Instructions for Form 1040, pp.18–19); Pub 501 (2025) covers them in detail.

If the dependent is a qualifying child for CTC (see [`qualifying-child-test.md`](./qualifying-child-test.md)), the agent should classify them as CTC instead — they don't double-count for both.

---

## Test 1 — Not a qualifying child

The person must NOT be a qualifying child of the filer or any other taxpayer for the year.

**Common case**: a 17-year-old child who lived with the filer all year. Fails the qualifying-child age test (Test 2 in the qualifying-child reference) but can still be a qualifying relative.

**Edge case**: a child who is a qualifying child of someone else (e.g., the filer's grandchild who is the qualifying child of the grandchild's parent). The person CAN'T be a qualifying relative of the filer if they're already a qualifying child of another taxpayer, even if that other person doesn't claim them. Exception: a child is not treated as the qualifying child of a person who isn't required to file and doesn't file, or files only to get a refund of withheld income tax and claims no credits (Pub 501 (2025), Not a Qualifying Child Test, Examples 1–3).

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

The person's gross income for the year must be less than the **exemption amount** referred to in IRC §152(d)(1)(B) (the deduction itself is $0, but the IRS still publishes an inflation-adjusted figure for this test).

For tax year 2025: less than $5,200 (Rev. Proc. 2024-40 §2.24; Pub 501 (2025), Gross Income Test, p.19).
For tax year 2026: less than $5,300 (Rev. Proc. 2025-32 §4.23).

**Gross income** includes:
- Wages, salaries, tips (after pre-tax deductions)
- Self-employment net earnings
- Interest and dividends
- Rental income
- Gambling winnings
- Unemployment benefits

**Gross income does NOT include** (Pub 501: gross income is income "that isn't exempt from tax"):
- The nontaxable part of social security benefits (taxable social security benefits ARE gross income — Pub 501 p.19; taxability under IRC §86)
- Scholarships received by degree candidates and used for tuition, fees, supplies, books and required equipment
- Tax-exempt interest
- Most veterans' benefits
- Income of a permanently and totally disabled person for services at a sheltered workshop (Pub 501 p.19)

**Common scenario**: claiming an elderly parent. If the parent receives only Social Security ($25,000/year) and none of it is taxable under §86, their gross income for §152(d) purposes is $0. They can be claimed as a qualifying relative if other tests are met.

**Common scenario**: claiming an adult child who is not a qualifying child (e.g., age 25, not disabled). If the adult child works and earned $7,000 of wages in the year, they exceed the $5,200 limit (2025) and are NOT a qualifying relative. The filer cannot claim them at all.

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

**Special support rules**: a scholarship received by a student child is not taken into account in the support test (IRC §152(f)(5); Pub 501). Benefits a state provides to a needy person (welfare, food benefits, housing) are generally support provided by the state — they count in total support but not as support the filer provided (Pub 501 (2025), "Support provided by the state," p.20). The person's own funds count only if actually spent on support.

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
        Is the person's gross income < $5,200 (2025) / $5,300 (2026)?
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

- A full-time student under age 24 at the end of the year (and younger than the filer) is a qualifying child for general dependency under §152(c)(3), so Test 1 of this file fails — but that does not matter for the ODC: the ODC is $500 for any dependent who is not a CTC qualifying child (IRC §24(h)(4)(A)).
- For CTC, §24(c) requires under 17, regardless of student status. So:
  - Adult full-time student under 24 = qualifying child for general dependency / EITC, but not for CTC
  - Eligible for ODC ($500) as a qualifying-child dependent; the gross income test does NOT apply to a qualifying child, so the $4,000 of earnings does not matter here

### Elderly parent, age 71, lives alone, receives $25,000 Social Security

- Test 1 (not qualifying child): pass (parents are never qualifying children of their kids)
- Test 2 (relationship): pass (parent is in the §152(d)(2) list)
- Test 3 (gross income): nontaxable Social Security is excluded → gross income $0 < $5,200 → pass (if part of the benefits is taxable under §86, that part counts)
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
- If niece is a qualifying child of the filer, she goes on CTC at $2,200 — not ODC.
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

ODC requires the dependent to have a **Taxpayer Identification Number (TIN)** issued on or before the due date of the return, including extensions (IRC §24(e)(1); 2025 Instructions for Schedule 8812, p.1). An ITIN or ATIN applied for by the due date and later issued counts as issued on time. The filer (and spouse if MFJ) must also have an SSN or ITIN issued on or before the due date. The dependent must be a U.S. citizen, U.S. national, or U.S. resident alien (IRC §24(h)(4)(B); an adopted child who lived with a U.S. citizen or national filer all year meets this). Unlike CTC, ODC accepts:

- SSN
- ITIN
- ATIN

So a dependent with an ITIN qualifies for ODC ($500) even though they don't qualify for CTC ($2,200).

Without ANY taxpayer identification number, the dependent cannot be claimed for ODC. The agent must confirm each ODC dependent has a TIN.

---

## Authority

- IRC §24(h)(4) — Credit for Other Dependents (added by TCJA 2017)
- IRC §24(h)(4)(B) — citizenship/nationality/residence requirement for ODC
- IRC §24(e) — TIN issued by the due date
- IRC §152(d) — Qualifying relative general definition
- IRC §152(d)(1)(B) — Gross income limit
- IRC §152(d)(2) — Relationship list
- IRC §152(d)(3) — Multiple support agreements (Form 2120)
- IRC §152(f)(5) — Scholarships not "provided by recipient"
- Form 2120 — Multiple Support Declaration
- Rev. Proc. 2024-40 §2.24 — 2025 gross income limit $5,200; Rev. Proc. 2025-32 §4.23 — 2026 limit $5,300
- Pub 501 (2025) — Dependents, Standard Deduction, and Filing Information
