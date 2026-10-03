# Additional Child Tax Credit (ACTC) — Refundability Computation

The ACTC is the refundable portion of the Child Tax Credit. Unlike the non-refundable CTC (which reduces tax liability but cannot create a refund), the ACTC can result in a refund check even if the filer owes no income tax.

Authority: IRC §24(d), as modified by §24(h)(5) (refundable cap, inflation-adjusted).

---

## When ACTC is in play

ACTC is available only when:

1. The filer has at least one qualifying child for CTC (qualifying child, with SSN by due date)
2. The filer has earned income greater than $2,500
3. The full $2,000-per-child CTC was not absorbed by the filer's tax liability (i.e., there's leftover credit after Form 1040 Line 19)

If the filer has only "Other Dependents" (no qualifying children with SSN), there is **no ACTC** — ODC is non-refundable.

If the filer's tax liability fully absorbed the CTC, there's no leftover for ACTC.

---

## The earned income method

The standard ACTC computation:

```
Step 1. Earned income > $2,500?  If no, ACTC = $0.
Step 2. Earned income excess = max(0, Earned income − $2,500)
Step 3. Earned income method ACTC = Earned income excess × 15%
Step 4. Per-child cap = N_CTC × $1,700 (tax year 2025; verify 2026)
Step 5. Leftover from CTC = Allowed credit − Non-refundable credit
Step 6. ACTC = min(Earned income method, Per-child cap, Leftover)
```

### Example: Single parent, one child, earned income $30,000

- N_CTC = 1
- Allowed credit = $2,000
- Tax before credits: $0 (low income, standard deduction wipes out)
- Non-refundable CTC = min($2,000, $0) = $0
- Leftover = $2,000 − $0 = $2,000
- Earned income excess = $30,000 − $2,500 = $27,500
- Earned income method ACTC = $27,500 × 15% = $4,125
- Per-child cap = 1 × $1,700 = $1,700
- ACTC = min($4,125, $1,700, $2,000) = **$1,700**

The filer gets $1,700 refunded as ACTC. The remaining $300 of the $2,000 credit is "lost" (not refundable; non-refundable was already $0 because tax was $0).

### Example: Earned income exactly $2,500

- Earned income excess = $0
- Earned income method ACTC = $0
- ACTC = $0 regardless of leftover or per-child cap

The earned income test is a hard floor.

---

## The alternative method (3+ qualifying children)

For filers with **3 or more qualifying children**, IRC §24(d)(1)(B)(ii) allows an alternative computation: the **Social Security tax method**. Use whichever method produces the larger ACTC.

### Social Security tax method

```
Step 1. Compute "SS+Medicare+½SE tax":
        = Filer's Social Security tax (1040 Line 25a or W-2 Box 4)
        + Filer's Medicare tax (1040 Line 25b or W-2 Box 6)
        + Half of self-employment tax (Schedule SE Line 13, deductible portion)

Step 2. Subtract Earned Income Credit (EITC, if claimed):
        = Step 1 result − EITC from Form 1040 Line 27

Step 3. SS-tax method ACTC = max(0, Step 2 result)

Step 4. ACTC = min(max(EI method, SS method), Per-child cap, Leftover)
```

The 3+-children alternative was added because large families with low income often have substantial Social Security/Medicare withholding but little earned income above $2,500 — the SS-tax method can produce a larger refundable credit.

### Example: MFJ couple with 3 children, earned income $35,000, SS+Medicare $2,678

- N_CTC = 3
- Allowed credit = $6,000
- Tax before credits: $0 (low income)
- Non-refundable = $0
- Leftover = $6,000
- Per-child cap = 3 × $1,700 = $5,100

Earned income method:
- EI excess = $35,000 − $2,500 = $32,500
- EI method ACTC = $32,500 × 15% = $4,875

SS-tax method:
- SS+Medicare = $35,000 × 7.65% = $2,678
- (Assume EITC = $6,500 for the example — large family, low income)
- SS-tax method = max(0, $2,678 − $6,500) = $0

In this case, the EI method ($4,875) wins. ACTC = min($4,875, $5,100, $6,000) = **$4,875**.

### Example: MFJ couple with 4 children, earned income $20,000, SS+Medicare $1,530, no EITC eligibility

(Hypothetically, due to other rules disqualifying EITC)

- N_CTC = 4
- Allowed credit = $8,000
- Per-child cap = 4 × $1,700 = $6,800
- Leftover = $8,000 (assuming no tax liability)

Earned income method:
- EI excess = $20,000 − $2,500 = $17,500
- EI method ACTC = $17,500 × 15% = $2,625

SS-tax method:
- SS+Medicare = $20,000 × 7.65% = $1,530
- EITC = $0
- SS-tax method = $1,530

EI method ($2,625) wins. ACTC = min($2,625, $6,800, $8,000) = **$2,625**.

---

## How to decide which method to use

The agent must compute **both** methods if N_CTC ≥ 3, then use the larger. If N_CTC < 3, only the earned income method is available.

```python
if N_CTC >= 3:
    ei_method = max(0, earned_income - 2500) * 0.15
    ss_method = max(0, ss_medicare_half_se - eitc)
    method_result = max(ei_method, ss_method)
else:
    method_result = max(0, earned_income - 2500) * 0.15
    
per_child_cap = N_CTC * 1700  # verify 2026
actc = min(method_result, per_child_cap, leftover)
```

The IRS instructions to Schedule 8812 walk through both methods in Part II-A and Part II-B; the filer (and the agent) just enter both and take the larger.

---

## Combat pay election

Nontaxable combat pay can be **elected** to be included in earned income for ACTC purposes. This is a one-way election: by including, the filer increases their earned income (and thus their EI method ACTC) but doesn't otherwise change taxability of combat pay.

Common scenario: a service member with $40,000 of nontaxable combat pay and $5,000 of regular wages. Without combat pay election:
- Earned income = $5,000
- EI excess = $2,500
- EI method ACTC = $375 (very low)

With combat pay election:
- Earned income = $45,000
- EI excess = $42,500
- EI method ACTC = $6,375 (substantially higher)

The election is made on Schedule 8812 by including the combat pay amount in the "earned income" line. Use [Form W-2 Box 12 with code Q](https://www.irs.gov/forms-pubs/about-form-w-2) for the combat pay figure.

The agent should ASK any military filer: "Do you have nontaxable combat pay? If yes, would you like to elect to include it in earned income for the ACTC computation?"

---

## Earned income — what counts

For ACTC purposes, **earned income** includes:

- Wages, salaries, tips (Form 1040 Line 1a)
- Net self-employment earnings (Schedule SE Line 4 minus half SE tax — i.e., the deductible portion of SE tax is subtracted)
- Statutory employee earnings (boxed on Schedule SE)
- Combat pay (if elected)
- Tax-free disability pay treated as earned income for some Code purposes (verify Pub 596 Worksheet B)

**Does NOT count as earned income for ACTC**:
- Pensions and annuities
- Social Security benefits
- Investment income (interest, dividends, capital gains)
- Unemployment compensation
- Alimony
- Child support
- Veterans' benefits (other than as elected)

The agent should be precise about this. Tax software typically computes earned income automatically, but the agent should verify: a filer with $50K of Social Security and $5K of part-time wages has earned income of $5,000 (not $55,000).

---

## PATH Act and ACTC refund timing

Returns claiming ACTC (or EITC) are subject to additional fraud screening under the Protecting Americans from Tax Hikes (PATH) Act of 2015. The IRS holds these refunds until at least mid-February each year.

If the user e-files in early February, the refund won't issue until late February at the earliest. This is a procedural delay, not a denial — but the user should be set the right expectation.

The IRS posts the year-specific PATH Act schedule at https://www.irs.gov/individuals/refund-timing.

---

## Validation checklist for ACTC

Before the agent declares the ACTC computation done:

- [ ] At least one qualifying child for CTC (with SSN by due date) — otherwise ACTC = $0
- [ ] Earned income > $2,500 — otherwise ACTC = $0
- [ ] Per-child cap = N_CTC × $1,700 (2025); verify 2026 figure against latest Rev. Proc.
- [ ] If N_CTC ≥ 3, both EI method and SS-tax method computed; larger used
- [ ] ACTC ≤ Leftover (Allowed credit − Non-refundable credit)
- [ ] ACTC ≤ Per-child cap
- [ ] Combat pay election considered for military filers
- [ ] User informed about PATH Act delay (refund not before mid-February)

---

## Authority

- IRC §24(d) — Refundable Additional Child Tax Credit
- IRC §24(d)(1)(A) — Earned income method (15% of earned income excess over $2,500)
- IRC §24(d)(1)(B)(ii) — Alternative SS-tax method for 3+ qualifying children
- IRC §24(h)(5) — Refundable per-child cap, inflation-adjusted ($1,700 for 2025; verify 2026)
- PATH Act of 2015 — refund timing for returns claiming ACTC/EITC
- Pub 596 — Earned Income Credit (parallel earned-income definitions)
- Rev. Proc. 2024-40 — 2025 inflation adjustments (refundable cap $1,700)
