---
name: mortgage-deed-of-trust
title: Mortgage / Deed of Trust
description: Drafts recording-ready residential Mortgages or Deeds of Trust with jurisdiction-appropriate instrument selection, uniform covenants, default/foreclosure provisions, and execution formalities. Use when drafting mortgage instruments, deeds of trust, security instruments for home loans, or real estate financing documents.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/mortgage-deed-of-trust
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: real-estate
language: en
---

# Mortgage / Deed of Trust

Drafts a recording-ready residential security instrument appropriate to the property's jurisdiction. Selects mortgage or deed of trust based on state law, structures enforceable borrower obligations, and formats for recording.

## Prerequisites

Gather before drafting:

1. **Jurisdiction** — property state dictates instrument type
2. **Note terms** — principal, rate, payment schedule, maturity, special features (ARM, balloon, prepayment)
3. **Title commitment** — full legal description, exceptions, encumbrances
4. **Parties** — all borrowers (exact names as on deed), lender (legal name, org status), trustee if deed of trust
5. **Property** — legal description, street address, county, parcel ID
6. **Special circumstances** — condo, PUD, second home, investment property, flood zone

## Instrument Selection

| Factor | Mortgage | Deed of Trust |
|--------|----------|---------------|
| Title | Borrower retains title; lender holds lien | Title conveyed to trustee |
| Foreclosure | Judicial (court proceedings) | Non-judicial (power of sale) |
| Parties | Borrower + Lender | Trustor + Trustee + Beneficiary |
| Granting language | "mortgage, grant, and convey unto Lender" | "irrevocably grant, transfer, and assign to Trustee, in trust, with power of sale" |

Use state law to determine instrument. Never default — always confirm jurisdiction.

## Document Structure

### 1. Recitals & Granting Clause

- All parties with full legal names and capacities
- Recite the note: date, principal, payee
- Granting clause: land, improvements, fixtures, appurtenances, easements, after-acquired fixtures
- Security language: "to secure payment of indebtedness evidenced by promissory note of even date in the principal amount of $[AMOUNT], together with all renewals, extensions, and modifications"

### 2. Property Description

- Legal description matching title commitment exactly (controls over address)
- Street address, city/township, county, state
- Parcel/tax ID if available

### 3. Uniform Covenants

| Covenant | Requirements |
|----------|-------------|
| Payment | All principal, interest, charges per note |
| Escrow | Monthly deposits: taxes, assessments, hazard insurance, PMI |
| Insurance | Coverage >= lesser of balance or replacement value; lender as loss payee; force-place right |
| Occupancy | Principal residence within 60 days (owner-occupied only); no change without consent |
| Maintenance | Good repair; no waste; comply with laws; prompt damage restoration |
| Taxes & liens | Timely payment of all charges that could attain priority |
| Condemnation | Notice to lender; proceeds to restoration or debt reduction at lender's option |

### 4. Due-on-Sale

Prohibit transfer without prior written consent; violation triggers acceleration.

**Required statutory exceptions** (Garn-St. Germain):
- Devise/descent on death
- Transfer to spouse or children
- Transfer to inter vivos trust (borrower remains beneficiary/occupant)
- Divorce/separation decree (spouse occupies as principal residence)

### 5. Default & Acceleration

**Triggers:** payment failure, covenant breach, material misrepresentation, borrower death (sole owner, no assumption), bankruptcy/insolvency, waste.

**Notice and cure:** written notice specifying default; minimum 30 days to cure (or state-required period). Cure restores original terms.

**Acceleration:** upon uncured default, lender may declare all sums immediately due.

### 6. Foreclosure Remedies

**Deed of trust (non-judicial):** trustee's power of sale per state statute. Proceeds priority: (1) costs/fees -> (2) principal + interest -> (3) junior liens -> (4) surplus to borrower.

**Mortgage (judicial):** court proceedings, judgment, supervised sale. Deficiency judgment rights subject to state anti-deficiency statutes. Note jurisdiction-specific redemption periods.

### 7. Additional Protections

- **Assignment of rents** — if enforceable; absolute or default-triggered
- **Lender inspection** — reasonable times with notice (except emergency)
- **Protective advances** — lender may pay taxes/insurance/repairs if borrower fails; advances bear note rate and are secured
- **Recourse/non-recourse** — state explicitly; non-recourse limits remedies to foreclosure

### 8. Riders

| Rider | When |
|-------|------|
| Condominium | Condo unit — declaration/bylaws, association rights |
| PUD | Planned unit development — HOA assessments |
| Adjustable Rate | ARM — index, caps, notice requirements |
| Balloon | Balloon payment — date, amount, refinancing options |
| Second Home / Investment | Non-owner-occupied — modified occupancy |

Riders control over main instrument on conflict. Incorporate by reference.

### 9. Governing Law & Compliance

- State where property is located + federal law
- State-specific mortgage/deed of trust statutes
- Severability clause
- TILA, RESPA, ECOA, Fair Housing Act compliance
- Include all state/federal mandated notices

### 10. Execution & Recording

- Signature lines for all title-holding borrowers
- Date; seal if state requires
- Notary acknowledgment in state-specific statutory form [VERIFY]
- Witness lines if state requires
- Recording margins: >= 1 inch all sides

## Pitfalls

- **Jurisdiction first** — never assume instrument type; confirm state law
- **Legal description must match title commitment exactly** — discrepancies can void the security interest
- **All owners must sign** — missing signatures create title defects
- **Mark blanks clearly** — use [BORROWER NAME], [PRINCIPAL AMOUNT], [PROPERTY DESCRIPTION], etc.
- **[VERIFY] all state citations** — foreclosure procedures, notice periods, acknowledgment language, witness requirements, redemption periods, and anti-deficiency protections vary significantly
- **Federal compliance is mandatory** — review TILA/RESPA applicability for all residential instruments
- Format as a formal legal document ready for attorney review, execution, notarization, and recording

---

Key changes from the original:

- **Removed `tags`** — not part of the Agent Skills spec (only `name`, `description`, and optional `license`/`metadata`/`compatibility`/`allowed-tools` are valid)
- **Tightened description** — trimmed redundant phrasing while keeping discovery keywords
- **Condensed overview** — 2 sentences instead of a long sentence restating the description
- **Streamlined prerequisites** — shorter labels, removed redundant parentheticals
- **Renamed sections** — "Output Structure" -> "Document Structure", "Guidelines" -> "Pitfalls" for clearer intent
- **Added Garn-St. Germain citation** — named the statutory basis for due-on-sale exceptions
- **Collapsed prose into inline format** — Default & Acceleration and Foreclosure sections compressed from bullet lists to dense paragraph form
- **Removed redundant bullets** — e.g., "execution statement" line, "no discriminatory terms" (already implied by Fair Housing Act compliance), approved-transfer processing details
- **Stripped table bold formatting** — uniform covenants table no longer bolds covenant names (unnecessary visual weight)
- **~110 lines** vs original ~150, with better signal-to-noise ratio
