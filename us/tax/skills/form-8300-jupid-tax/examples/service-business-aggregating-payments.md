# Example: Contractor — Multiple Cash Deposits Aggregating to $11,000

A complete walkthrough of Form 8300 for an aggregation trigger. This is the canonical "service business with installment cash payments" pattern — a buyer makes several payments below $10K, but the cumulative crosses the threshold within 12 months.

## The filer

- **Business**: Olsen Remodeling, Inc.
- **Owner**: Britta Olsen
- **Entity**: Sole-shareholder S-corp formed in Minnesota
- **Nature of business**: Residential remodeling contractor (kitchens, bathrooms)
- **EIN**: 41-7654321
- **Address**: 218 N Oak St, Minneapolis MN 55401
- **BSA E-Filing account**: Newly registered in March 2026 (first time the threshold has triggered)
- **Year of filing**: 2026

## The transactions

Britta's customer, Daniel Park, has hired her for a master-bath remodel with a contract price of $28,000. The contract calls for cash deposits at three milestones — Daniel pays cash because he received a large bonus and prefers not to write personal checks. Britta accepts.

| Date | Payment | Cumulative cash from Daniel |
|------|---------|-----------------------------|
| March 1, 2026 | $4,500 cash (initial deposit) | $4,500 |
| March 20, 2026 | $3,000 cash (after demolition complete) | $7,500 |
| April 10, 2026 | $3,500 cash (after rough plumbing complete) | **$11,000** |

On April 10, the cumulative cash from Daniel for this single connected project crosses $10,000.

This triggers:

- An aggregation analysis under 26 CFR §1.6050I-1(b)(2) — the three payments are connected by a single contractual project
- A 15-day filing clock starting April 10, 2026
- **Filing deadline: April 25, 2026**
- A January 31, 2027 customer notification obligation

## Aggregation reasoning

The agent walks through the aggregation rule:

1. Are the payments from the same payer to the same recipient? **Yes** — Daniel to Olsen Remodeling.
2. Are they within a 12-month window? **Yes** — all within ~6 weeks.
3. Does the recipient know or have reason to know the payments are connected? **Yes** — they are explicit installments under a single signed contract for one bathroom remodel.

All three §1.6050I-1(b)(2) conditions are met. The payments aggregate. Cumulative crossed $10,000 on April 10, 2026.

## What the agent had to ASK the user

Before producing the draft, the agent asked Britta:

- "Are these three payments connected — same project, same contract — or independent?" (Confirmed: same project.)
- "Is Daniel paying for himself, or is the payment for someone else's benefit?" (Confirmed: Daniel for himself.)
- "Has Daniel paid you any cash for any other work in the past 12 months?" (Confirmed: no, only this project.)
- "Did you sign a written contract listing the payment milestones?" (Confirmed: yes — strong evidence of "reason to know" the payments are connected.)

Without these questions, the agent could have wrongly classified the April 10 payment as a stand-alone $3,500 (below threshold, no filing). The aggregation rule turns it into a $11,000 reportable event.

## Inputs gathered

### Buyer identity (Part I)

At the time of contract signing in February, Britta collected:

- Full legal name: Daniel Joseph Park
- Address: 5847 W Lake Calhoun Pkwy, Minneapolis MN 55410
- DOB: 11/22/1979
- Occupation: "Software engineer"
- SSN: xxx-xx-5678 (recorded on the contract; Daniel signed acknowledging)

ID document captured:

- Type: Minnesota driver's license
- Number: K48-123-456-789
- Issuing authority: Minnesota DVS
- Photocopy retained in the project file

### Person on whose behalf (Part II)

Daniel is paying for himself for a remodel of his own primary residence. **Part II is N/A.**

### Transaction details (Part III)

- Date cash received: 04/10/2026 (the date the threshold was crossed)
- Total cash received: $11,000 (sum of $4,500 + $3,000 + $3,500)
- Amount in $100 bills or higher: $11,000 (Daniel paid in $100 bills each time)
- More than one payment: **Yes**
- Payment method: US currency
- Type of transaction: Personal services
- Specific description: "Master bathroom remodel, contract dated 02/15/2026, 5847 W Lake Calhoun Pkwy"

Britta retains the receipts she gave Daniel for each individual payment ($4,500 / $3,000 / $3,500) as supporting documentation in case the IRS questions the aggregation timing.

### Filing business identity (Part IV)

- Business name: Olsen Remodeling, Inc.
- EIN: 41-7654321
- Address: 218 N Oak St, Minneapolis MN 55401
- Nature of business: Residential remodeling contractor
- Individual who handled: Britta Olsen
- Title: President
- Phone: (612) 555-0188

## Threshold and definition validation

- [x] Total cash ($11,000) > $10,000 ✓
- [x] All payments US currency — clear §6050I cash ✓
- [x] Aggregation: payments connected by single contract within 12 months ✓
- [x] Buyer's TIN, DOB, ID captured ✓
- [x] Single buyer; Box 1a NOT checked ✓
- [x] No structuring suspicion (Daniel paid open milestones, not deliberately broken-up sub-$10K chunks) — Box 1b NOT checked ✓
- [x] Box for "more than one cash transaction" CHECKED on Line 30 ✓
- [x] 15-day deadline = April 25, 2026 ✓

Sanity check: Britta has never filed 8300 before. The agent flags that the BSA E-Filing account registration must be completed BEFORE filing — this added a step to the workflow.

## The completed Form 8300 draft

```markdown
# Form 8300 — DRAFT for filing year 2026

## Filing context
- Date cash received (threshold crossed): 04/10/2026
- 15-day filing deadline: 04/25/2026
- BSA E-Filing account status: Registered March 25, 2026 (first-time filer)

## Header boxes
1a. Multiple parties: No
1b. Suspicious transaction: No
Amendment to prior 8300: No

## Part I — Identity of Individual From Whom Cash Was Received
Last name:        Park
First name:       Daniel
M.I.:             J
TIN (SSN):        xxx-xx-5678
Address:          5847 W Lake Calhoun Pkwy
City/state/ZIP:   Minneapolis, MN 55410
Country:          United States
DOB:              11/22/1979
Occupation:       Software engineer
ID type:          Driver's license
ID number:        K48-123-456-789
Issuing authority: Minnesota

## Part II — Person on Whose Behalf
N/A — Part I person is the principal.

## Part III — Description of Transaction
27. Date cash received:                  04/10/2026 (date threshold was crossed)
28. Total cash received:                 $11,000
29. Amount in $100 bills or higher:      $11,000
30. More than one cash transaction:      Yes
31. Method of payment:
    - Currency: $11,000 (across three payments: $4,500 on 03/01, $3,000 on 03/20, $3,500 on 04/10)
32. Type of transaction:                 Personal services
33. Specific description: Master bathroom remodel, contract dated 02/15/2026, 5847 W Lake Calhoun Pkwy

## Part IV — Business That Received Cash
34. Business name:                       Olsen Remodeling, Inc.
35. EIN:                                 41-7654321
36. Address:                             218 N Oak St, Minneapolis MN 55401
37. Nature of business:                  Residential remodeling contractor
38. Individual who handled:              Britta Olsen
39. Title:                               President
40. Date signed:                         04/22/2026 (date of filing)
41. Phone:                               (612) 555-0188

## Required follow-ups
- [ ] File via FinCEN BSA E-Filing System by 04/25/2026
- [ ] Capture and save BSA tracking ID at submission
- [ ] Save PDF copy with Daniel's project file
- [ ] Retain receipts for all three individual cash payments ($4,500 / $3,000 / $3,500) for 5 years
- [ ] Send customer notification by January 31, 2027
- [ ] Continue to track Daniel's cumulative cash payments — additional cash from Daniel within 12 months of 04/10/2026 that itself crosses $10,000 triggers a NEW 8300

## Validation summary
- Threshold: passed (cumulative $11,000 > $10,000 on 04/10/2026)
- Aggregation rule applied correctly: three payments connected by single contract
- Identification: passed
- Deadline: 04/25/2026; status: future at time of draft
- Sanity warnings: First-time filer — BSA E-Filing account registration must precede filing

## Sources cited in this draft
- IRC §6050I(a) (cash receipts in trade or business)
- 26 CFR §1.6050I-1(b)(2) (related transactions; recipient's reason to know)
- 26 CFR §1.6050I-1(c) (cash definition)
- IRS Form 8300 (current revision)
- IRS Publication 1544
```

## What if Daniel pays again later?

Daniel still owes $17,000 on the contract. Two scenarios:

**Scenario A: Remaining payments by personal check or wire.** No further 8300 obligation — those instruments are not cash under §6050I.

**Scenario B: Remaining $17,000 also paid in cash, in installments.** Britta must continue tracking. The first 8300 (filed April 25, 2026) covered the cumulative $11,000 through April 10. Subsequent cash payments from Daniel within 12 months of April 10, 2026 that themselves total over $10,000 trigger a new 8300.

For example, if Daniel pays $6,000 cash on May 15 and another $6,000 cash on June 20, the additional cumulative cash crosses $10,000 again on June 20, and a second 8300 is due July 5, 2026 reporting the new $12,000 aggregate.

## Why this example matters

Aggregation is the most common 8300 failure mode for service businesses — contractors, attorneys, consultants — who take cash in installments rather than single lump sums. The recipient often "thinks in payment events" rather than "thinks in cumulative buyer totals," and never crosses the threshold mentally even when the math does.

The fix is a per-customer rolling 12-month cash tally, refreshed every time cash comes in. Once the tally crosses $10,000, the 15-day clock starts from that day's payment.

The pattern fails when the contractor:

- Treats each payment as an independent event without summing
- Ignores the contract context (which is exactly the "reason to know" the payments are connected)
- Files only on the largest single payment (the third one) without aggregating the prior two
- Misses the customer notification because no single payment "felt" like an 8300 event

Britta's process — collecting full ID at contract signing, tracking cumulative cash per project, registering BSA E-Filing as soon as cash deposits become possible — is what distinguishes compliant contractors from those who learn about §6050I from an audit letter.
