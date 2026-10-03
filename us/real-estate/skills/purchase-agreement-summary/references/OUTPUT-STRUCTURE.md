# Purchase Agreement Summary — Output Structure

The deliverable contains 15 sections in this order. Every section appears, even if its content is "Not stated" or "None identified." Silent omission obscures coverage.

## 1. Header

- Property address (full)
- State
- Documents received (label every instrument: "PA", "Amendment #1", "Inspection Addendum", "Counteroffer #2", etc., with execution dates)
- Effective date (date of last signature / acceptance)
- Summary date
- Required disclaimer (verbatim — see SKILL.md)

## 2. Deal Snapshot

Two-column quick-reference table:

| Field | Value |
|---|---|
| Buyers | (Exact legal names, entity designations, suffixes) |
| Sellers | (Same) |
| Property | (Address + APN/legal cite) |
| Price | (Current controlling) |
| Total EMD | (Sum across all deposits) |
| Closing Date | (Calendar date) |
| Possession | (Date and time) |
| Loan Type / Amount | (Cash / Conv / FHA / VA / etc. + dollar amount) |
| Title Co. | (Name) |
| HOA | (Yes / No / Pending docs) |
| Special Assessments | (Stated / Not stated / Pending) |
| Key Flags | (Count by severity) |

## 3. Parties & Contacts

Full extraction per Step 2 of SKILL.md workflow. Buyer(s) and seller(s) exactly as written, including middle initials, suffixes, entity designations, "and/or assigns," trust names with trustee identifiers. Contact info if available. Brokers, agents, transaction coordinators.

Flag spouse missing in community-property states; corporate signer without officer title; name discrepancies between documents; marital/vesting language.

## 4. Property Details

- Street address (incl. unit/city/state/zip)
- Parcel ID / APN / PIN
- Legal description or exhibit reference
- County
- Additional parcels / outlots / common elements
- Personal property included / excluded
- Note any items requiring a separate Bill of Sale

Flag missing parcel ID or legal description as a title-search risk.

## 5. Price, Earnest Money & Credits

**Price:**
- Current controlling purchase price
- Price history if amended (each price + source citation)
- Escalation clause terms (if any)

**Earnest money:**
- Each deposit: amount, holder, deadline, method
- Refundability triggers and exceptions
- TX option fee separately captured (paid to seller, not escrow)

**Credits / concessions:**
- Seller concessions / closing-cost credits
- Repair credits (separate from general — lenders treat differently)
- Rate buy-down credits
- Other concessions

Flag any seller credit with "Confirm lender acceptability."

## 6. Financing & Appraisal

- Loan type (Cash / Conv / FHA / VA / Other)
- Loan amount or maximum LTV
- Down payment
- Loan application deadline
- Loan commitment / approval deadline
- Appraisal contingency: deadline, threshold (price-based or low-appraisal trigger), remedy

## 7. Contingencies

For each contingency: condition, responsible party, deadline (calendar date), remedy if unsatisfied.

Standard list:
- Inspection (TREC option, attorney inspection, etc.)
- Repair request and resolution
- Appraisal
- Financing
- Title
- Survey
- HOA documents review
- Sale of buyer's property (if applicable)
- Zoning approvals (commercial / development)
- Tenant estoppels (with leased property)

## 8. Title, Survey & Closing Documentation

**Title:**
- Title company selection (who selects, who pays)
- Owner's policy required? Who pays?
- Permitted exceptions
- Commitment / objection / cure timelines
- Termination rights on title objections

**Survey:**
- Type (boundary / ALTA / existing accepted)
- Cost allocation
- Deadline
- Standards (TLTA, ALTA/NSPS)

**Closing documents:**
- Form of deed (warranty / special warranty / quitclaim / grant)
- Bills of sale (for personalty)
- Affidavits (debts and liens, FIRPTA, etc.)
- Settlement statement and (if applicable) Closing Disclosure

## 9. HOA & Condominium

- Association name and contact
- Required disclosures and delivery deadline
- Buyer review period and termination right
- Transfer fees / move-in fees / capital contributions allocation
- Master insurance and any owner-policy requirements (condo)

Flag if HOA documents or fees are unclear or undelivered.

## 10. Closing Date, Possession & Occupancy

- Closing date (with time-is-of-the-essence flag if applicable)
- Possession date and time
- Rent-back / use-and-occupancy terms (if any)
- Per diem rate, holdback / deposit
- Utility transfer responsibility

Flag post-closing possession as heightened risk requiring an occupancy agreement.

## 11. Closing Costs, Taxes & Prorations

**Cost allocations** (extract who pays each):
- Owner's title policy
- Lender's title policy
- Escrow / closing fee
- Recording fees
- Transfer taxes / doc stamps
- Survey
- Pest / termite inspection
- Home warranty

**Prorations:**
- Tax proration method (calendar vs. fiscal; current vs. last-available bill) — extract verbatim
- HOA dues
- Rents (if leased)
- Utilities

## 12. Addenda & Amendments Inventory

| # | Name / Label | Date executed | Signing status | What it modifies | Source pages |
|---|---|---|---|---|---|

Cover every instrument referenced or attached. Flag if a referenced addendum is not in the file.

## 13. Critical Dates & Deadlines

The chronological table from Step 5 of the SKILL.md workflow:

| Item | Deadline (as written) | Computed Date | Status | Source |
|---|---|---|---|---|

**Status values:** Passed / Due within 48 hrs / Due within 7 days / Future / Unknown.

Flag closing on Sunday or federal holiday; ambiguous effective date; undefined day-count convention; "Time is of the Essence" provisions; amendments resetting deadlines.

## 14. Flags & Follow-Up

Categorized by severity:

- **Critical** — blocking issues that prevent reliance on the summary or that must be resolved before closing.
- **High** — issues that will likely delay or complicate closing.
- **Medium** — needs clarification but not blocking.
- **Low** — informational; document for the record.

Each flag has: description, source pointer, recommended action, owner.

## 15. Source Map

For each summary category: document label + page or section. Allows the reader to trace any value back to its source quickly.

| Category | Source |
|---|---|
| Buyers | PA p. 1; Amendment #2 p. 1 |
| Price | PA § 3; Amendment #2 § 1 (modified) |
| EMD | PA § 5; Amendment #1 § 2 (additional) |
| ... | ... |

Every value in the summary must be traceable here. If a value lacks a source, it does not belong in the summary.
