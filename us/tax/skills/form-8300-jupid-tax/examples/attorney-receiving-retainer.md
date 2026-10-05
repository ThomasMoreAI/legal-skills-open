# Example: Attorney — $25,000 Cash Retainer Delivered by Third Party

A complete walkthrough of Form 8300 for a transaction where the person handing over the cash is **not** the principal client. This is the canonical "Part II is filled" pattern — common in legal practice when a relative or employer pays a retainer on behalf of the actual client.

## The filer

- **Business**: Friedman & Associates, PLLC
- **Owner / Principal Attorney**: Sarah Friedman
- **Entity**: Multi-member professional LLC formed in New York
- **Nature of business**: Law firm — criminal defense
- **EIN**: 13-9876543
- **Address**: 401 Broadway, Suite 1200, New York NY 10013
- **BSA E-Filing account**: Active since 2018; Sarah is the Supervisory User; her associate Ben Walker has filing rights
- **Year of filing**: 2026

## The transaction

**June 5, 2026.** A man named Anthony Russo walks into Friedman & Associates' office and says he wants to retain Sarah to represent his nephew, Vincent Russo, on a federal indictment for securities fraud. Anthony delivers $25,000 in $100 bills as the retainer.

This raises two §6050I questions:

1. **Is the cash threshold met?** Yes — $25,000 in US currency exceeds $10,000.
2. **Who is the principal?** Anthony delivered the cash, but he is paying for legal services to be rendered for his nephew Vincent. Vincent is the client. Anthony is acting on Vincent's behalf, OR Anthony is a third-party gift-giver of the retainer.

The Treasury regulations and IRS guidance for attorneys are clear: when a third party pays a legal retainer for another person, the attorney files 8300 with **Part I = the person who delivered the cash (Anthony)** AND **Part II = the principal on whose behalf the cash was paid (Vincent)**.

(Note: separate from §6050I, attorneys have additional ethical and disclosure obligations under state bar rules when a third party funds a client's representation. Those are out of scope here, but Sarah handles them in parallel.)

## What the agent had to ASK

Before producing the draft, the agent asked Sarah:

- "Who delivered the cash to your office today?" (Anthony Russo)
- "Who is the actual client — the person who will receive the legal services?" (Vincent Russo)
- "Is Anthony being reimbursed by Vincent, or is this a gift-funded retainer from Anthony?" (Sarah confirms: gift-funded; Anthony is Vincent's uncle and is paying for the defense.)
- "Did Anthony provide his own ID and TIN at the office?" (Yes — driver's license + SSN.)
- "Do you have Vincent's identifying information?" (Yes — Vincent had his initial intake call last week and provided full ID, SSN, DOB.)

The agent confirms: Part I = Anthony, Part II = Vincent. Both must be fully identified.

## Inputs gathered

### Buyer / cash deliverer (Part I — Anthony Russo)

- Full legal name: Anthony Michael Russo
- Address: 89 Hudson St, Apt 4B, Hoboken NJ 07030
- DOB: 02/14/1968
- Occupation: "Restaurant owner"
- SSN: xxx-xx-9012

ID document:

- Type: New Jersey driver's license
- Number: M523-19284-67012
- Issuing authority: New Jersey MVC

### Principal / client (Part II — Vincent Russo)

- Full legal name: Vincent Anthony Russo
- Address: 1209 Park Ave, Apt 14C, New York NY 10128
- DOB: 08/03/1995
- Occupation: "Investment analyst (currently suspended pending case)"
- SSN: xxx-xx-3456

Vincent's ID document was captured at his intake last week and is on file:

- Type: New York driver's license
- Number: 123-456-789
- Issuing authority: New York DMV

### Transaction details (Part III)

- Date cash received: 06/05/2026
- Total cash: $25,000
- Amount in $100 bills or higher: $25,000
- More than one payment: No (single delivery, single transaction)
- Payment method: US currency
- Type of transaction: Personal services (the regulation's "personal services" box covers attorney services to an individual)
- Specific description: "Legal retainer — federal criminal defense, US v. Russo, EDNY case docket pending"

### Filing business identity (Part IV)

- Business name: Friedman & Associates, PLLC
- EIN: 13-9876543
- Address: 401 Broadway, Suite 1200, New York NY 10013
- Nature of business: Law firm — criminal defense
- Individual who handled: Sarah Friedman
- Title: Principal Attorney
- Phone: (212) 555-0145

## Threshold and definition validation

- [x] Total cash ($25,000) > $10,000 ✓
- [x] All US currency — clear §6050I cash ✓
- [x] Single payment, single transaction ✓
- [x] Anthony's TIN, DOB, ID captured at the moment of delivery ✓
- [x] Vincent's TIN, DOB, ID captured at intake ✓
- [x] Both individuals identified — Part I (Anthony) AND Part II (Vincent) filled ✓
- [x] Single deliverer (Anthony alone walked in) — Box 1a NOT checked ✓
- [x] No structuring concern — Box 1b NOT checked ✓
- [x] 15-day deadline = June 20, 2026 ✓

Sanity check: large retainer in cash for a federal criminal case — Sarah considers whether Box 1b (suspicious transaction) should be checked. After reflection, she concludes the cash source and delivery don't independently raise structuring suspicion (Anthony has documented restaurant business income, the amount is consistent with retainer norms in the practice). She leaves Box 1b unchecked but documents her reasoning in her case file. The agent surfaces this consideration in the deliverable rather than making the decision for her.

## The completed Form 8300 draft

```markdown
# Form 8300 — DRAFT for filing year 2026

## Filing context
- Date cash received: 06/05/2026
- 15-day filing deadline: 06/20/2026
- BSA E-Filing account status: Registered (Friedman & Associates, PLLC)

## Header boxes
1a. Multiple parties: No
1b. Suspicious transaction: No
   (Note: large cash retainer in a criminal case considered; no independent structuring or illicit-source indicators identified. Documented in matter file.)
Amendment to prior 8300: No

## Part I — Identity of Individual From Whom Cash Was Received
Last name:        Russo
First name:       Anthony
M.I.:             M
TIN (SSN):        xxx-xx-9012
Address:          89 Hudson St, Apt 4B
City/state/ZIP:   Hoboken, NJ 07030
Country:          United States
DOB:              02/14/1968
Occupation:       Restaurant owner
ID type:          Driver's license
ID number:        M523-19284-67012
Issuing authority: New Jersey

## Part II — Person on Whose Behalf
Last name:        Russo
First name:       Vincent
M.I.:             A
TIN (SSN):        xxx-xx-3456
Address:          1209 Park Ave, Apt 14C
City/state/ZIP:   New York, NY 10128
Country:          United States
DOB:              08/03/1995
Occupation:       Investment analyst (currently suspended pending case)
ID type:          Driver's license
ID number:        123-456-789
Issuing authority: New York

## Part III — Description of Transaction
27. Date cash received:                  06/05/2026
28. Total cash received:                 $25,000
29. Amount in $100 bills or higher:      $25,000
30. More than one cash transaction:      No
31. Method of payment:
    - Currency: $25,000
32. Type of transaction:                 Personal services
33. Specific description: Legal retainer — federal criminal defense, US v. Russo, EDNY case docket pending

## Part IV — Business That Received Cash
34. Business name:                       Friedman & Associates, PLLC
35. EIN:                                 13-9876543
36. Address:                             401 Broadway, Suite 1200, New York NY 10013
37. Nature of business:                  Law firm — criminal defense
38. Individual who handled:              Sarah Friedman
39. Title:                               Principal Attorney
40. Date signed:                         06/12/2026 (date of filing)
41. Phone:                               (212) 555-0145

## Required follow-ups
- [ ] File via FinCEN BSA E-Filing System by 06/20/2026
- [ ] Capture and save BSA tracking ID at submission
- [ ] Save PDF copy in the matter file (US v. Russo)
- [ ] Send customer notifications by January 31, 2027 to BOTH:
    - [ ] Anthony Russo (Part I individual)
    - [ ] (Defensive practice) Vincent Russo (Part II principal)
- [ ] Retain ID copies, retainer agreement, and BSA tracking ID for 5 years
- [ ] Confirm New York state-bar disclosure requirements for third-party-funded representation are separately satisfied (out of §6050I scope)

## Validation summary
- Threshold: passed (cash $25,000 > $10,000)
- Identification: passed (Part I Anthony fully identified; Part II Vincent fully identified)
- Deadline: 06/20/2026; status: future
- Sanity warnings: large cash retainer in criminal case — Box 1b considered, declined with documented reasoning

## Sources cited in this draft
- IRC §6050I (cash receipts in trade or business)
- 31 USC §5331 (BSA cash reporting)
- 26 CFR §1.6050I-1 (regulatory definitions)
- IRS Form 8300 (current revision)
- IRS Publication 1544
- IRS guidance for attorneys: cash retainers paid by third parties require Part I (deliverer) and Part II (principal/client) identification
```

## Customer notification (January 31, 2027)

Sarah sends written notifications by January 31, 2027:

**To Anthony Russo (required under IRC §6050I(e)(2)):**

> _Dear Mr. Russo,_
>
> _On June 12, 2026, we filed IRS Form 8300, Report of Cash Payments Over $10,000 Received in a Trade or Business. The form was filed because we received from you more than $10,000 in cash in 2026. The aggregate amount we reported was $25,000. The information was reported to the Internal Revenue Service._
>
> _Friedman & Associates, PLLC_
> _401 Broadway, Suite 1200_
> _New York NY 10013_

**To Vincent Russo (defensive — not strictly required by statute since §6050I(e)(2) names only the Part I individual, but many practitioners notify the Part II principal as well):**

> _Dear Mr. Russo,_
>
> _On June 12, 2026, we filed IRS Form 8300, Report of Cash Payments Over $10,000 Received in a Trade or Business. The form was filed because we received cash on your behalf in 2026 in connection with our representation. The aggregate amount we reported was $25,000. The information was reported to the Internal Revenue Service._
>
> _Friedman & Associates, PLLC_

Both notifications are mailed first-class to the addresses on file. Sarah retains copies in the matter file.

## Why this example matters

Three issues distinguish this pattern from a simple single-buyer transaction:

1. **Part II is required and often forgotten.** When a third party pays cash for someone else's services, §6050I requires identification of BOTH the deliverer (Part I) and the principal (Part II). Skipping Part II is a §6721 incomplete-information failure even if the rest of the form is correct.
2. **TIN collection for both parties.** Vincent's information must be on file in advance — collected at his intake — because by the time Anthony walks in with cash, the 15-day clock starts. Trying to retroactively get a principal's SSN after a third party paid cash is uncomfortable and time-pressured.
3. **The Box 1b judgment call.** Large cash retainers in criminal-defense practice raise an obvious question of source-of-funds. The attorney must independently judge whether to check the suspicious-transaction box. The agent's role is to surface the question, not to decide it — Box 1b is a fact-and-circumstances determination that requires legal judgment Sarah has and the agent does not.

The pattern fails when the firm:

- Files Form 8300 with only Part I (Anthony) and leaves Part II blank because "Anthony walked in"
- Tries to use Vincent's name in Part I because "the retainer is for him" (Part I is the physical deliverer of the cash, not the principal)
- Forgets the customer notification entirely, or sends it only to one of the two parties
- Decides to "skip" the filing because attorney-client privilege seems to conflict — it does NOT; §6050I filing is a third-party reporting obligation, distinct from privileged communications

Sarah's process — collect IDs from both parties at intake, file within a week, document the Box 1b reasoning, notify both — is the audit-defense standard for any practice that takes third-party-funded retainers in cash.
