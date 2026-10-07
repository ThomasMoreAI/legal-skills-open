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
- **Filing channel**: e-file required (Britta confirms the company files 16 Forms W-2 and 1099-NEC a year, above the 10-information-return threshold in the Form 8300 instructions)
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

- An aggregation analysis under 26 CFR §1.6050I-1(b)(2) — the initial payment was $10,000 or less, so payments for this single contractual project made within one year of the initial payment are added until the total exceeds $10,000
- A 15-day filing clock starting April 10, 2026
- **Filing deadline: Monday, April 27, 2026** (the 15th day, April 25, is a Saturday, so the deadline moves to the next business day per the Form 8300 instructions)
- A January 31, 2027 customer notification obligation

## Aggregation reasoning

The agent walks through the aggregation rule:

1. Are the payments from the same payer to the same recipient? **Yes** — Daniel to Olsen Remodeling.
2. Are they within a 12-month window? **Yes** — all within ~6 weeks.
3. Does the recipient know or have reason to know the payments are connected? **Yes** — they are explicit installments under a single signed contract for one bathroom remodel.

All three conditions are met (26 CFR §1.6050I-1(b)(2) for installments on one transaction; §1.6050I-1(c)(7)(ii) for related transactions). The payments aggregate. Cumulative crossed $10,000 on April 10, 2026.

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
- Number: K48-123-456-789 (entered on the form as K48123456789: the instructions say to enter the ID number without formatting or special characters)
- Issued by: Minnesota
- Photocopy retained in the project file

### Person on whose behalf (Part II)

Daniel is paying for himself for a remodel of his own primary residence. **Part II is N/A.**

### Transaction details (Part III)

- Date cash received: 04/10/2026 (the date the threshold was crossed)
- Total cash received: $11,000 (sum of $4,500 + $3,000 + $3,500)
- Amount in $100 bills or higher: $11,000 (Daniel paid in $100 bills each time)
- More than one payment: **Yes**
- Payment method: US currency
- Type of transaction: Personal services provided (box 33c)
- Specific description: "Master bathroom remodel, contract dated 02/15/2026, 5847 W Lake Calhoun Pkwy"

Britta retains the receipts she gave Daniel for each individual payment ($4,500 / $3,000 / $3,500) as supporting documentation in case the IRS questions the aggregation timing.

### Filing business identity (Part IV)

- Business name: Olsen Remodeling, Inc.
- EIN: 41-7654321
- Address: 218 N Oak St, Minneapolis MN 55401
- Nature of business: Residential remodeling contractor
- Signer / title: Britta Olsen, President
- Contact person and phone: Britta Olsen, (612) 555-0188

## Threshold and definition validation

- [x] Total cash ($11,000) > $10,000 ✓
- [x] All payments US currency — clear §6050I cash ✓
- [x] Aggregation: payments connected by single contract within 12 months ✓
- [x] Buyer's TIN, DOB, ID captured ✓
- [x] Single buyer; item 2 NOT checked ✓
- [x] No structuring suspicion (Daniel paid open milestones, not deliberately broken-up sub-$10K chunks) — item 1b NOT checked ✓
- [x] Item 30 ("received in more than one payment") CHECKED ✓
- [x] Item 32a ($11,000) equals item 29 ($11,000) ✓
- [x] 15-day deadline = April 25, 2026, a Saturday → Monday, April 27, 2026 ✓

Sanity check: Britta has never filed 8300 before. The agent flags that the BSA E-Filing account registration must be completed BEFORE filing — this added a step to the workflow.

## The completed Form 8300 draft

```markdown
# Form 8300 — DRAFT for filing year 2026

## Filing context
- Date cash received (threshold crossed): 04/10/2026
- 15-day filing deadline: 04/27/2026 (day 15 is Saturday 04/25/2026; next business day)
- Filing channel: e-file required (16 other information returns)
- BSA E-Filing account status: Registered March 25, 2026 (first-time filer)

## Item 1
1a. Amends prior report: No
1b. Suspicious transaction: No

## Part I — Identity of Individual From Whom Cash Was Received
2.  More than one individual:  not checked
3.  Last name:                 Park
4.  First name:                Daniel
5.  M.I.:                      J
6.  TIN (SSN):                 xxx-xx-5678
7.  Address:                   5847 W Lake Calhoun Pkwy
8.  Date of birth:             11/22/1979
9.  City:                      Minneapolis
10. State:                     MN
11. ZIP code:                  55410
12. Country (if not U.S.):     (blank)
13. Occupation:                Software engineer
14a. ID type:                  Driver's license
14b. Issued by:                Minnesota
14c. Number:                   K48123456789

## Part II — Person on Whose Behalf
Skipped — Daniel acted on his own behalf.

## Part III — Description of Transaction and Method of Payment
28. Date cash received:                  04/10/2026 (payment that caused the total to exceed $10,000)
29. Total cash received:                 $11,000.00
30. Received in more than one payment:   checked
31. Total price if different from 29:    $28,000.00 (contract price)
32. a. U.S. currency:                    $11,000.00 (amount in $100 bills or higher: $11,000.00)
    (three payments: $4,500 on 03/01, $3,000 on 03/20, $3,500 on 04/10)
33. Type of transaction:                 c. Personal services provided
34. Specific description:                Master bathroom remodel, contract dated 02/15/2026, 5847 W Lake Calhoun Pkwy

## Part IV — Business That Received Cash
35. Name of business:                    Olsen Remodeling, Inc.
36. EIN:                                 41-7654321
37. Address:                             218 N Oak St
38. City:                                Minneapolis
39. State:                               MN
40. ZIP code:                            55401
41. Nature of your business:             Residential remodeling contractor
42. Signature / title:                   Britta Olsen, President
43. Date of signature:                   04/22/2026 (date of filing)
44. Contact person:                      Britta Olsen
45. Contact telephone number:            (612) 555-0188

## Comments
None.

## Required follow-ups
- [ ] File via FinCEN BSA E-Filing System by 04/27/2026
- [ ] Capture and save BSA tracking ID at submission
- [ ] Save PDF copy with Daniel's project file
- [ ] Retain receipts for all three individual cash payments ($4,500 / $3,000 / $3,500) for 5 years
- [ ] Send Daniel's statement by January 31, 2027 (a Sunday; Monday, February 1, 2027 is timely under IRC §7503, but send earlier)
- [ ] Continue to track Daniel's cumulative cash payments — additional cash from Daniel within 12 months of 04/10/2026 that itself crosses $10,000 triggers a NEW 8300

## Validation summary
- Threshold: passed (cumulative $11,000 > $10,000 on 04/10/2026)
- Aggregation rule applied correctly: three payments connected by single contract
- Identification: passed
- Deadline: 04/27/2026 (04/25 is a Saturday); status: future at time of draft
- Sanity warnings: First-time filer — BSA E-Filing account registration must precede filing

## Sources cited in this draft
- IRC §6050I(a) (cash receipts in trade or business)
- 26 CFR §1.6050I-1(b)(2) (installment payments aggregated within one year of the initial payment)
- 26 CFR §1.6050I-1(c)(7)(ii) (related transactions; recipient's reason to know)
- 26 CFR §1.6050I-1(c)(1) (cash definition)
- IRS Form 8300 (Rev. December 2023) and instructions
- IRS Publication 1544
```

## What if Daniel pays again later?

Daniel still owes $17,000 on the contract. Two scenarios:

**Scenario A: Remaining payments by personal check or wire.** No further 8300 obligation — those instruments are not cash under §6050I.

**Scenario B: Remaining $17,000 also paid in cash, in installments.** Britta must continue tracking. The first 8300 (filed April 22, 2026) covered the cumulative $11,000 through April 10. Previously unreported cash payments from Daniel within a 12-month period that themselves total over $10,000 trigger a new 8300 (26 CFR §1.6050I-1(b)(3)).

For example, if Daniel pays $6,000 cash on May 15 and another $6,000 cash on June 20, the additional cumulative cash crosses $10,000 again on June 20, and a second 8300 reporting the new $12,000 aggregate is due Monday, July 6, 2026 (the 15th day, July 5, is a Sunday). Daniel's single statement for 2026, due January 31, 2027, then shows $23,000 (both reports).

## Why this example matters

Aggregation is the most common 8300 failure mode for service businesses — contractors, attorneys, consultants — who take cash in installments rather than single lump sums. The recipient often "thinks in payment events" rather than "thinks in cumulative buyer totals," and never crosses the threshold mentally even when the math does.

The fix is a per-customer rolling 12-month cash tally, refreshed every time cash comes in. Once the tally crosses $10,000, the 15-day clock starts from that day's payment.

The pattern fails when the contractor:

- Treats each payment as an independent event without summing
- Ignores the contract context (which is exactly the "reason to know" the payments are connected)
- Files only on the largest single payment (the third one) without aggregating the prior two
- Misses the customer notification because no single payment "felt" like an 8300 event

Britta's process — collecting full ID at contract signing, tracking cumulative cash per project, registering BSA E-Filing as soon as cash deposits become possible — is what distinguishes compliant contractors from those who learn about §6050I from an audit letter.
