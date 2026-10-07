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
- **Filing channel**: e-file required (the firm files more than 10 Forms W-2 and 1099 a year)
- **Year of filing**: 2026

## The transaction

**June 5, 2026.** A man named Anthony Russo walks into Friedman & Associates' office and says he wants to retain Sarah to represent his nephew, Vincent Russo, on a federal indictment for securities fraud. Anthony delivers $25,000 in $100 bills as the retainer.

This raises two §6050I questions:

1. **Is the cash threshold met?** Yes — $25,000 in US currency exceeds $10,000.
2. **Who is the principal?** Anthony delivered the cash, but he is paying for legal services to be rendered for his nephew Vincent. Vincent is the client. Anthony is acting on Vincent's behalf, OR Anthony is a third-party gift-giver of the retainer.

The regulation is clear: when the recipient knows or has reason to know that the person delivering the cash is acting for someone else, the return must identify both; a return that does not is incomplete (26 CFR §1.6050I-1(e)(3)(ii)). The attorney files 8300 with **Part I = the individual who delivered the cash (Anthony)** AND **Part II = the person on whose behalf the transaction was conducted (Vincent)**.

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
- Number: M523-19284-67012 (entered as M5231928467012, without formatting)
- Issued by: New Jersey

### Principal / client (Part II — Vincent Russo)

- Full legal name: Vincent Anthony Russo
- Address: 1209 Park Ave, Apt 14C, New York NY 10128
- DOB: 08/03/1995
- Occupation: "Investment analyst"
- SSN: xxx-xx-3456

Vincent's ID document was captured at his intake last week and is kept in the matter file. Part II has no ID or date-of-birth fields; item 27 (alien identification) is used only for a person who is not required to furnish a TIN, so it stays blank for Vincent.

### Transaction details (Part III)

- Date cash received: 06/05/2026
- Total cash: $25,000
- Amount in $100 bills or higher: $25,000
- More than one payment: No (single delivery, single transaction)
- Payment method: US currency
- Type of transaction: Personal services provided (box 33c)
- Specific description: "Legal retainer — federal criminal defense, US v. Russo, EDNY case docket pending"

### Filing business identity (Part IV)

- Business name: Friedman & Associates, PLLC
- EIN: 13-9876543
- Address: 401 Broadway, Suite 1200, New York NY 10013
- Nature of business: Law firm — criminal defense
- Signer / title: Sarah Friedman, Principal Attorney
- Contact person and phone: Sarah Friedman, (212) 555-0145

## Threshold and definition validation

- [x] Total cash ($25,000) > $10,000 ✓
- [x] All US currency — clear §6050I cash ✓
- [x] Single payment, single transaction ✓
- [x] Anthony's TIN, DOB, ID captured at the moment of delivery ✓
- [x] Vincent's TIN, DOB, ID captured at intake ✓
- [x] Both individuals identified — Part I (Anthony) AND Part II (Vincent) filled ✓
- [x] Single deliverer (Anthony alone walked in) — item 2 NOT checked ✓
- [x] No structuring concern — item 1b NOT checked ✓
- [x] Item 32a ($25,000) equals item 29 ($25,000) ✓
- [x] 15-day deadline = June 20, 2026, a Saturday → Monday, June 22, 2026 ✓

Sanity check: large retainer in cash for a federal criminal case — Sarah considers whether item 1b (suspicious transaction) should be checked. After reflection, she concludes the cash source and delivery don't independently raise structuring suspicion (Anthony has documented restaurant business income, the amount is consistent with retainer norms in the practice). She leaves item 1b unchecked but documents her reasoning in her case file. The agent surfaces this consideration in the deliverable rather than making the decision for her.

## The completed Form 8300 draft

```markdown
# Form 8300 — DRAFT for filing year 2026

## Filing context
- Date cash received: 06/05/2026
- 15-day filing deadline: 06/22/2026 (day 15 is Saturday 06/20/2026; next business day)
- Filing channel: e-file required
- BSA E-Filing account status: Registered (Friedman & Associates, PLLC)

## Item 1
1a. Amends prior report: No
1b. Suspicious transaction: No
   (Note for the firm, not for the form: large cash retainer in a criminal case considered; no independent structuring or illicit-source indicators identified. Documented in matter file.)

## Part I — Identity of Individual From Whom Cash Was Received
2.  More than one individual:  not checked
3.  Last name:                 Russo
4.  First name:                Anthony
5.  M.I.:                      M
6.  TIN (SSN):                 xxx-xx-9012
7.  Address:                   89 Hudson St, Apt 4B
8.  Date of birth:             02/14/1968
9.  City:                      Hoboken
10. State:                     NJ
11. ZIP code:                  07030
12. Country (if not U.S.):     (blank)
13. Occupation:                Restaurant owner
14a. ID type:                  Driver's license
14b. Issued by:                New Jersey
14c. Number:                   M5231928467012

## Part II — Person on Whose Behalf This Transaction Was Conducted
15. More than one person:      not checked
16. Last name:                 Russo
17. First name:                Vincent
18. M.I.:                      A
19. TIN (SSN):                 xxx-xx-3456
20. DBA name / EIN:            (blank)
21. Address:                   1209 Park Ave, Apt 14C
22. Occupation:                Investment analyst
23. City:                      New York
24. State:                     NY
25. ZIP code:                  10128
26. Country (if not U.S.):     (blank)
27. Alien identification:      (blank — Vincent furnished a TIN)

## Part III — Description of Transaction and Method of Payment
28. Date cash received:                  06/05/2026
29. Total cash received:                 $25,000.00
30. Received in more than one payment:   not checked
31. Total price if different from 29:    (blank)
32. a. U.S. currency:                    $25,000.00 (amount in $100 bills or higher: $25,000.00)
33. Type of transaction:                 c. Personal services provided
34. Specific description:                Legal retainer — federal criminal defense, US v. Russo, EDNY case docket pending

## Part IV — Business That Received Cash
35. Name of business:                    Friedman & Associates, PLLC
36. EIN:                                 13-9876543
37. Address:                             401 Broadway, Suite 1200
38. City:                                New York
39. State:                               NY
40. ZIP code:                            10013
41. Nature of your business:             Law firm — criminal defense
42. Signature / title:                   Sarah Friedman, Principal Attorney
43. Date of signature:                   06/12/2026 (date of filing)
44. Contact person:                      Sarah Friedman
45. Contact telephone number:            (212) 555-0145

## Comments
None.

## Required follow-ups
- [ ] File via FinCEN BSA E-Filing System by 06/22/2026
- [ ] Capture and save BSA tracking ID at submission
- [ ] Save PDF copy in the matter file (US v. Russo)
- [ ] Send statements by January 31, 2027 (a Sunday; Monday, February 1, 2027 is timely under IRC §7503, but send earlier) to BOTH persons named on the form:
    - [ ] Anthony Russo (Part I individual)
    - [ ] Vincent Russo (Part II person on whose behalf)
- [ ] Retain ID copies, retainer agreement, and BSA tracking ID for 5 years
- [ ] Confirm New York state-bar disclosure requirements for third-party-funded representation are separately satisfied (out of §6050I scope)

## Validation summary
- Threshold: passed (cash $25,000 > $10,000)
- Identification: passed (Part I Anthony fully identified; Part II Vincent fully identified)
- Deadline: 06/22/2026 (06/20 is a Saturday); status: future
- Sanity warnings: large cash retainer in criminal case — item 1b considered, declined with documented reasoning

## Sources cited in this draft
- IRC §6050I (cash receipts in trade or business)
- 31 USC §5331 (BSA cash reporting)
- 26 CFR §1.6050I-1 (regulatory definitions)
- IRS Form 8300 (Rev. December 2023) and instructions
- IRS Publication 1544
- 26 CFR §1.6050I-1(e)(3)(ii) (a return that does not identify both the principal and the agent is incomplete)
```

## Customer statements (due January 31, 2027)

The Form 8300 instructions require a statement to **each person named** on the form, and 26 CFR §1.6050I-1(f)(1) says the same ("each person whose name is set forth in a return"). Sarah sends both in January 2027:

**To Anthony Russo (Part I):**

> _Dear Mr. Russo,_
>
> _On June 12, 2026, we filed IRS Form 8300, Report of Cash Payments Over $10,000 Received in a Trade or Business. The form was filed because we received from you more than $10,000 in cash in 2026. The aggregate amount of reportable cash we received from you in 2026 was $25,000. This information was reported to the Internal Revenue Service._
>
> _Friedman & Associates, PLLC_
> _401 Broadway, Suite 1200_
> _New York NY 10013_
> _Contact: Sarah Friedman, (212) 555-0145_

**To Vincent Russo (Part II, also named on the form, so also required):**

> _Dear Mr. Russo,_
>
> _On June 12, 2026, we filed IRS Form 8300, Report of Cash Payments Over $10,000 Received in a Trade or Business. The form was filed because we received cash on your behalf in 2026 in connection with our representation. The aggregate amount of reportable cash we received relating to you in 2026 was $25,000. This information was reported to the Internal Revenue Service._
>
> _Friedman & Associates, PLLC_
> _401 Broadway, Suite 1200_
> _New York NY 10013_
> _Contact: Sarah Friedman, (212) 555-0145_

Both notifications are mailed first-class to the addresses on file. Sarah retains copies in the matter file.

## Why this example matters

Three issues distinguish this pattern from a simple single-buyer transaction:

1. **Part II is required and often forgotten.** When a third party pays cash for someone else's services, the regulation requires identification of BOTH the deliverer (Part I) and the principal (Part II); without Part II the return is incomplete (26 CFR §1.6050I-1(e)(3)(ii)) and exposed to the §6721 penalty even if the rest of the form is correct.
2. **TIN collection for both parties.** Vincent's information must be on file in advance — collected at his intake — because by the time Anthony walks in with cash, the 15-day clock starts. Trying to retroactively get a principal's SSN after a third party paid cash is uncomfortable and time-pressured.
3. **The item 1b judgment call.** Large cash retainers in criminal-defense practice raise an obvious question of source-of-funds. The attorney must independently judge whether to check the suspicious-transaction box. The agent's role is to surface the question, not to decide it — item 1b is a facts-and-circumstances determination that requires legal judgment Sarah has and the agent does not.

The pattern fails when the firm:

- Files Form 8300 with only Part I (Anthony) and leaves Part II blank because "Anthony walked in"
- Tries to use Vincent's name in Part I because "the retainer is for him" (Part I is the physical deliverer of the cash, not the principal)
- Forgets the statements entirely, or sends one to only one of the two named persons
- Decides to "skip" the filing because attorney-client privilege seems to conflict — it does NOT; §6050I filing is a third-party reporting obligation, distinct from privileged communications

Sarah's process — collect IDs from both parties at intake, file within a week, document the item 1b reasoning, send statements to both — is the audit-defense standard for any practice that takes third-party-funded retainers in cash.
