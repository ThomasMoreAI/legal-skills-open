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
- Issuing authority: Arizona MVD

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
- Address: 4500 N Black Canyon Hwy, Phoenix AZ 85015
- Nature of business: Used motor vehicle dealer
- Individual who handled: Hector Ramirez
- Title: Owner
- Phone: (602) 555-0123

## Threshold and definition validation

The agent runs through the validation checklist:

- [x] Total cash ($14,500) is **strictly greater than** $10,000 ✓
- [x] All payment is US currency ($100 bills) — fits §6050I cash definition ✓
- [x] No cashier's checks or money orders involved — no designated-reporting-transaction analysis needed ✓
- [x] Single payment, single transaction — no aggregation ✓
- [x] Buyer's TIN obtained at time of sale ✓
- [x] DOB present and valid ✓
- [x] One government-issued ID (driver's license) captured with type, number, and issuing authority ✓
- [x] Single buyer (Maria) physically delivered cash — Box 1a (multiple parties) NOT checked ✓
- [x] No suspicion of structuring or illicit activity — Box 1b NOT checked ✓
- [x] 15-day deadline = April 16, 2026 — in the future at time of draft ✓

No sanity warnings raised.

## The completed Form 8300 draft

```markdown
# Form 8300 — DRAFT for filing year 2026

## Filing context
- Date cash received: 04/01/2026
- 15-day filing deadline: 04/16/2026
- BSA E-Filing account status: Registered (Hector's Auto Sales LLC, Supervisory User: Hector Ramirez)

## Header boxes
1a. Multiple parties: No
1b. Suspicious transaction: No
Amendment to prior 8300: No

## Part I — Identity of Individual From Whom Cash Was Received
Last name:        Garcia
First name:       Maria
M.I.:             E
TIN (SSN):        xxx-xx-1234
Address:          1234 Desert View Lane
City/state/ZIP:   Phoenix, AZ 85032
Country:          United States
DOB:              06/15/1988
Occupation:       Dental hygienist
ID type:          Driver's license
ID number:        D08123456
Issuing authority: Arizona

## Part II — Person on Whose Behalf
N/A — Part I person is the principal.

## Part III — Description of Transaction
27. Date cash received:                  04/01/2026
28. Total cash received:                 $14,500
29. Amount in $100 bills or higher:      $14,500
30. More than one cash transaction:      No
31. Method of payment:
    - Currency: $14,500
32. Type of transaction:                 Personal property purchased
33. Specific description: 2018 Honda Civic LX, VIN 1HGCV1F11JA123456

## Part IV — Business That Received Cash
34. Business name:                       Hector's Auto Sales LLC
35. EIN:                                 86-1234567
36. Address:                             4500 N Black Canyon Hwy, Phoenix AZ 85015
37. Nature of business:                  Used motor vehicle dealer
38. Individual who handled:              Hector Ramirez
39. Title:                               Owner
40. Date signed:                         04/16/2026 (date of filing)
41. Phone:                               (602) 555-0123

## Required follow-ups
- [ ] File via FinCEN BSA E-Filing System by 04/16/2026
- [ ] Capture and save BSA tracking ID at submission
- [ ] Save PDF copy with Maria's customer file (5-year retention)
- [ ] Send customer notification by January 31, 2027
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
- IRS Form 8300 (current revision)
- IRS Publication 1544
```

## Filing day (April 16, 2026)

Hector logs into https://bsaefiling.fincen.treas.gov/, completes Form 8300 with the data above, and submits. The BSA E-Filing System returns tracking ID `2026XXXXXXXXXXXX`. He saves a screenshot and downloads the submitted PDF, filing both with Maria's bill of sale and ID copies in his customer records folder.

## Customer notification (January 31, 2027)

By January 31, 2027, Hector mails Maria a written notification:

> _Dear Maria Garcia,_
>
> _On April 16, 2026, we filed IRS Form 8300, Report of Cash Payments Over $10,000 Received in a Trade or Business. The form was filed because we received from you more than $10,000 in cash in 2026. The aggregate amount we reported was $14,500. The information was reported to the Internal Revenue Service._
>
> _Hector's Auto Sales LLC_
> _4500 N Black Canyon Hwy_
> _Phoenix AZ 85015_

Hector mails the notification first-class to the address on file from Maria's driver's license. He retains a copy of the letter in her customer file for the 5-year retention period.

## Why this example matters

This is the simplest and most common 8300 fact pattern: a single retail cash sale of a consumer durable. The compliance work is procedural — collect ID at the counter, file within 15 days, notify in January. The penalty exposure for skipping any step is high (~$330 per filing failure plus another ~$330 for the customer notification under current Rev. Proc. amounts), but the workflow itself is mechanical.

The pattern fails when the dealer:

- Lets the buyer leave without collecting full ID and TIN
- Forgets the 15-day clock and files months later
- Files the 8300 but forgets the January 31 notification
- Tries to "skip" filing because the buyer is a known regular

Each of those failures is its own §6721 or §6722 penalty. Hector's process — collect at the counter, file within a week, schedule the notification reminder — is the audit-proof default.
