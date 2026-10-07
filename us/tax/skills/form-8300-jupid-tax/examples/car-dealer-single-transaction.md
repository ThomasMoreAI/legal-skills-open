# Example: Used Car Dealer — Single $14,500 Cash Transaction

A complete walkthrough of Form 8300 for a single-transaction trigger. This is the canonical "consumer durable retail sale" pattern — a buyer walks in, pays cash above the threshold, the dealer files within 15 days.

## The filer

- **Business**: Hector's Auto Sales LLC
- **Owner**: Hector Ramirez
- **Entity**: Single-member LLC formed in Arizona, taxed as a disregarded entity
- **Nature of business**: Used motor vehicle dealer
- **EIN**: 86-1234567
- **Address**: 4500 N Black Canyon Hwy, Phoenix AZ 85015
- **BSA E-Filing account**: Active since 2022; Hector is the Supervisory User
- **Filing channel**: e-file required (Hector confirms the LLC files more than 10 Forms W-2 and 1099 each year, so it meets the 10-information-return test in the Form 8300 instructions)
- **Year of filing**: 2026

## The transaction

**April 1, 2026.** A customer named Maria Garcia walks onto Hector's lot and decides to buy a 2018 Honda Civic LX listed at $14,500. She pays the full amount in $100 bills.

This is:

- A single payment (no aggregation)
- US currency (clearly cash under §6050I)
- More than $10,000 (threshold crossed)
- A retail sale of a consumer durable (designated reporting transaction)

**One 8300 must be filed within 15 days — by April 16, 2026.**

## Inputs gathered (Step 4 of workflow)

### Buyer identity (Part I)

At the moment of sale, Hector:

- Photocopies Maria's Arizona driver's license (front and back)
- Photocopies her US passport as a second ID (best practice for high-value cash sales, not strictly required)
- Records on the bill of sale:
  - Full legal name: Maria Elena Garcia
  - Address: 1234 Desert View Lane, Phoenix AZ 85032
  - DOB: 06/15/1988
  - Occupation: "Dental hygienist"
  - SSN: xxx-xx-1234 (collected verbally and recorded; Maria signs the bill of sale acknowledging the SSN provided)

ID document captured:

- Type: Arizona driver's license
- Number: D08123456
- Issued by: Arizona

### Person on whose behalf (Part II)

Hector asks: "Maria, are you buying this car for yourself, or for someone else?" Maria says it's for her own use. **Part II is N/A — Part I person is the principal.**

### Transaction details (Part III)

- Date cash received: 04/01/2026
- Total cash: $14,500
- Amount in $100 bills or higher: $14,500 (all in $100 bills)
- More than one payment: No
- Payment method: US currency
- Type of transaction: Personal property purchased
- Specific description: "2018 Honda Civic LX, VIN 1HGCV1F11JA123456"

### Filing business identity (Part IV)

- Business name: Hector's Auto Sales LLC
- EIN: 86-1234567
- SSN: the LLC is disregarded, so for federal tax purposes it is Hector's sole proprietorship, and the instructions say a sole proprietorship must enter the owner's SSN as well as any EIN. The agent asked Hector to confirm this treatment; he did, and provided xxx-xx-4321.
- Address: 4500 N Black Canyon Hwy, Phoenix AZ 85015
- Nature of business: Used motor vehicle dealer
- Signer / title: Hector Ramirez, Owner
- Contact person and phone: Hector Ramirez, (602) 555-0123

## Threshold and definition validation

The agent runs through the validation checklist:

- [x] Total cash ($14,500) is **strictly greater than** $10,000 ✓
- [x] All payment is US currency ($100 bills) — fits §6050I cash definition ✓
- [x] No cashier's checks or money orders involved — no designated-reporting-transaction analysis needed ✓
- [x] Single payment, single transaction — no aggregation ✓
- [x] Buyer's TIN obtained at time of sale ✓
- [x] DOB present and valid ✓
- [x] One government-issued ID (driver's license) captured with type, number, and issuing authority ✓
- [x] Single buyer (Maria) physically delivered cash — item 2 (more than one individual) NOT checked ✓
- [x] No suspicion of structuring or illicit activity — item 1b NOT checked ✓
- [x] Item 32a ($14,500) equals item 29 ($14,500) ✓
- [x] 15-day deadline = April 16, 2026 — in the future at time of draft ✓

No sanity warnings raised.

## The completed Form 8300 draft

```markdown
# Form 8300 — DRAFT for filing year 2026

## Filing context
- Date cash received: 04/01/2026
- 15-day filing deadline: 04/16/2026
- BSA E-Filing account status: Registered (Hector's Auto Sales LLC, Supervisory User: Hector Ramirez)

## Item 1
1a. Amends prior report: No
1b. Suspicious transaction: No

## Part I — Identity of Individual From Whom Cash Was Received
2.  More than one individual:  not checked
3.  Last name:                 Garcia
4.  First name:                Maria
5.  M.I.:                      E
6.  TIN (SSN):                 xxx-xx-1234
7.  Address:                   1234 Desert View Lane
8.  Date of birth:             06/15/1988
9.  City:                      Phoenix
10. State:                     AZ
11. ZIP code:                  85032
12. Country (if not U.S.):     (blank)
13. Occupation:                Dental hygienist
14a. ID type:                  Driver's license
14b. Issued by:                Arizona
14c. Number:                   D08123456

## Part II — Person on Whose Behalf
Skipped — Maria acted on her own behalf.

## Part III — Description of Transaction and Method of Payment
28. Date cash received:                  04/01/2026
29. Total cash received:                 $14,500.00
30. Received in more than one payment:   not checked
31. Total price if different from 29:    (blank — price equals cash received)
32. a. U.S. currency:                    $14,500.00 (amount in $100 bills or higher: $14,500.00)
33. Type of transaction:                 a. Personal property purchased
34. Specific description:                2018 Honda Civic LX, VIN 1HGCV1F11JA123456

## Part IV — Business That Received Cash
35. Name of business:                    Hector's Auto Sales LLC
36. EIN:                                 86-1234567   (SSN box: xxx-xx-4321, owner of disregarded LLC)
37. Address:                             4500 N Black Canyon Hwy
38. City:                                Phoenix
39. State:                               AZ
40. ZIP code:                            85015
41. Nature of your business:             Used motor vehicle dealer
42. Signature / title:                   Hector Ramirez, Owner
43. Date of signature:                   04/16/2026 (date of filing)
44. Contact person:                      Hector Ramirez
45. Contact telephone number:            (602) 555-0123

## Comments
None.

## Required follow-ups
- [ ] File via FinCEN BSA E-Filing System by 04/16/2026
- [ ] Capture and save BSA tracking ID at submission
- [ ] Save PDF copy with Maria's customer file (5-year retention)
- [ ] Send Maria's statement by January 31, 2027 (a Sunday; Monday, February 1, 2027 is timely under IRC §7503, but send earlier)
- [ ] Retain ID copies, bill of sale, and BSA tracking ID for 5 years

## Validation summary
- Threshold: passed (cash $14,500 > $10,000)
- Identification: passed (TIN, DOB, ID all captured)
- Deadline: 04/16/2026; status: future
- Sanity warnings: none

## Sources cited in this draft
- IRC §6050I (cash receipts in trade or business)
- 31 USC §5331 (BSA cash reporting)
- 26 CFR §1.6050I-1 (regulatory definitions)
- IRS Form 8300 (Rev. December 2023) and instructions
- IRS Publication 1544
```

## Filing day (April 16, 2026)

Hector logs into https://bsaefiling.fincen.treas.gov/, completes Form 8300 with the data above, and submits. The BSA E-Filing System returns tracking ID `2026XXXXXXXXXXXX`. He saves a screenshot and downloads the submitted PDF, filing both with Maria's bill of sale and ID copies in his customer records folder.

## Customer statement (due January 31, 2027)

In January 2027, Hector mails Maria the written statement required by IRC §6050I(e) and 26 CFR §1.6050I-1(f):

> _Dear Maria Garcia,_
>
> _On April 16, 2026, we filed IRS Form 8300, Report of Cash Payments Over $10,000 Received in a Trade or Business. The form was filed because we received from you more than $10,000 in cash in 2026. The aggregate amount of reportable cash we received from you in 2026 was $14,500. This information was reported to the Internal Revenue Service._
>
> _Hector's Auto Sales LLC_
> _4500 N Black Canyon Hwy_
> _Phoenix AZ 85015_
> _Contact: Hector Ramirez, (602) 555-0123_

Hector mails the notification first-class to the address on file from Maria's driver's license. He retains a copy of the letter in her customer file for the 5-year retention period.

## Why this example matters

This is the simplest and most common 8300 fact pattern: a single retail cash sale of a consumer durable. The compliance work is procedural — collect ID at the counter, file within 15 days, notify in January. The penalty exposure for skipping any step is real ($340 for the missed return due in 2026 under Rev. Proc. 2024-40, plus $340 for the missed statement due in 2027 under Rev. Proc. 2025-32, and far more if the IRS finds intentional disregard), but the workflow itself is mechanical.

The pattern fails when the dealer:

- Lets the buyer leave without collecting full ID and TIN
- Forgets the 15-day clock and files months later
- Files the 8300 but forgets the January 31 notification
- Tries to "skip" filing because the buyer is a known regular

Each of those failures is its own §6721 or §6722 penalty. Hector's process — collect at the counter, file within a week, schedule the notification reminder — is the audit-proof default.
