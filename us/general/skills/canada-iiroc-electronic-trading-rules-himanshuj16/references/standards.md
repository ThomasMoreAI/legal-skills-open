# Standards for CIRO (formerly IIROC) Electronic Trading Compliance

IIROC and the MFDA amalgamated on January 1, 2023; the amalgamated SRO was renamed the
**Canadian Investment Regulatory Organization (CIRO)** on June 1, 2023. CIRO administers
UMIR. "IIROC" survives only in historical notices and in the name of this skill.

| Control Element | Requirement | Source |
|---|---|---|
| Timing | Controls must be automated and applied **before** order entry; post-trade monitoring is required in addition, not instead. | NI 23-103 s.3(2) |
| Erroneous orders | Must prevent orders exceeding pre-determined **price or size parameters**. | NI 23-103 s.3(3)(a) |
| Credit / capital | Must prevent orders exceeding pre-determined **credit or capital thresholds**. | NI 23-103 s.3(3)(a) |
| Unexecuted orders | Must limit the **value or volume of unexecuted (open) orders** for a security or class of securities. | UMIR Rule 7.1 / Policy 7.1 |
| Pre-entry regulatory checks | Must prevent orders that fail marketplace and regulatory requirements which must be satisfied on a **pre-order-entry** basis. | NI 23-103 s.3(3)(b) |
| Short sale designation | A sale of a security the seller does not own must be designated **"short sale"** at entry. | UMIR 6.2(1)(b)(viii) |
| Short-marking exempt | A qualifying account (arbitrage accounts; directionally neutral automated-order-generation accounts) must designate **every** order — purchase and sale — **"short-marking exempt"**, and must not also designate it "short". Use is mandatory, not optional. | UMIR 6.2(1)(b)(ix) |
| Ownership and control | The participant must **directly and exclusively** set and adjust these controls, including any provided by a third party, and must regularly assess and document their adequacy. | NI 23-103 s.3(5), s.3(6) |
| Supervision | Written supervision and compliance policies must be detailed enough for a reasonably knowledgeable person to know when they apply and how to follow them. | UMIR Rule 7.1 and Policy 7.1 |
| Automated order systems | Must be tested before first use and at least annually, with the ability to immediately disable the system and prevent its orders reaching a marketplace. | NI 23-103 s.5(3) |

## Numeric thresholds

Neither NI 23-103 nor UMIR prescribes numeric values for any of the thresholds above.
CIRO's position is that appropriate limits cannot be determined generically for a
participant; the firm sets, documents, assigns responsibility for, and periodically
reassesses each limit. Any specific percentage or dollar figure in this skill's code or
examples is an illustrative default, not a regulatory minimum.

## Repealed provisions

**UMIR 3.1 (Restrictions on Short Selling)** — the tick test requiring a short sale to be
priced at or above the last sale price — was **repealed effective September 1, 2012**. Do
not cite it as authority for short-sale controls; the operative requirements are the
UMIR 6.2 designations and the pre-borrow provisions introduced by the same amendments.

## Sources

- National Instrument 23-103 *Electronic Trading and Direct Electronic Access to Marketplaces* — https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/61_2013
- CSA Staff Notice 23-314, *FAQ about NI 23-103* — https://www.osc.ca/en/securities-law/instruments-rules-policies/2/23-314/csa-staff-notice-23-314-frequently-asked-questions-about-national-instrument-23-103-electronic
- CIRO, UMIR 7.1 *Trading Supervision Obligations* — https://www.ciro.ca/rules-and-enforcement/universal-market-integrity-rules/71-trading-supervision-obligations
- CIRO, UMIR 6.2 *Designation and Identifiers* — https://www.ciro.ca/rules-and-enforcement/universal-market-integrity-rules/62-designation-and-identifiers
- CIRO, *Updated Guidance on "Short Sale" and "Short-Marking Exempt" Order Designations* — https://www.ciro.ca/newsroom/publications/updated-guidance-short-sale-and-short-marking-exempt-order-designations
- CIRO, UMIR 3.1 *Restrictions on Short Selling – Repealed* — https://www.ciro.ca/rules-and-enforcement/universal-market-integrity-rules/31-restrictions-short-selling-repealed
- CIRO, *Guidance Respecting Electronic Trading* — https://www.ciro.ca/newsroom/publications/guidance-respecting-electronic-trading
