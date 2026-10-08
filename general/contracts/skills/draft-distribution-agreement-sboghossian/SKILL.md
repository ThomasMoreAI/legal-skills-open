---
name: draft-distribution-agreement-sboghossian
title: Distribution Agreement
description: Use when drafting a distribution agreement appointing a distributor to sell and resell a supplier's products in a defined territory. Covers exclusivity variants, minimum purchase commitments, marketing obligations, IP/trademark use, and the critical MENA-specific trap of commercial agency registration under UAE, KSA, and Egyptian commercial agency laws that can trigger statutory termination indemnity. Pair with the MENA extension skill for jurisdiction-specific variant clauses.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/draft/draft-distribution-agreement
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: contracts
language: en
---

# Distribution Agreement

## When to use this

A distribution agreement governs the relationship between a **supplier/manufacturer** (who makes or owns the product) and a **distributor** (who buys the product and resells it in a defined territory). The distributor is not an agent — it takes title to goods, bears inventory risk, and sells on its own account.

Use this skill when:

- A manufacturer is entering a new market and wants a local partner to carry its products.
- An existing distribution relationship needs to be formalized or renegotiated.
- A supplier is considering granting exclusivity in a territory and needs to understand the commercial and legal implications.
- A cross-border product launch in a MENA jurisdiction requires a local distributor.

**Critical distinction:** the word "agent" must be avoided in distribution agreements in MENA jurisdictions where Commercial Agency Laws exist. Using agency language, even inadvertently, can trigger statutory protections and termination indemnities that are expensive and difficult to exit. See Jurisdictional Notes.

## Required inputs

| Input | Why it matters | Default |
|-------|----------------|---------|
| Supplier / Manufacturer (full legal name + jurisdiction) | Party bearing performance obligations on product quality, supply | — |
| Distributor (full legal name + jurisdiction) | Party carrying inventory and sales obligations | — |
| Products (with SKU / description) | Scope must be precise; ambiguity leads to disputes on whether new product lines are included | Schedule A |
| Territory (countries, regions, or channels) | Exclusivity and minimum-purchase obligations are territory-specific | — |
| Exclusivity type | Exclusive / sole / non-exclusive | Non-exclusive default |
| Term (initial + renewal) | Determines notice-period and indemnity exposure | 2 years + auto-renew |
| Pricing mechanism | Wholesale price list, update mechanism, currency | Schedule B |
| Minimum purchase commitment (MPC) | Commercial anchor; miss consequences must be defined | Schedule C |

## Optional inputs

- Marketing spend obligation (percentage of Distributor's revenue)
- Sub-distribution rights (Distributor may appoint sub-distributors)
- E-commerce / online channel restrictions
- Territorial channel split (brick-and-mortar vs. digital)
- Right of first refusal on new products
- Parent/group guarantee from Distributor

## Exclusivity variants explained

| Type | What it means | MENA risk level |
|---|---|---|
| **Exclusive** | Only Distributor may sell in territory; Supplier cannot sell directly or appoint others | Highest — if relationship treated as commercial agency, indemnity on exit |
| **Sole** | Distributor is sole third-party appointee; Supplier may still sell directly in territory | Medium |
| **Non-exclusive** | Supplier may appoint multiple distributors; Distributor competes with others | Lowest |

For MENA jurisdictions, **prefer non-exclusive or sole** arrangements to reduce the risk of meeting the threshold for commercial agency protection. If exclusivity is commercially necessary, ensure the agreement is structured clearly as a buy-resell arrangement.

## Standard clauses

### 1. Appointment and territory
Supplier appoints Distributor as [exclusive / sole / non-exclusive] distributor of Products within Territory for the Term. Define Territory with specificity (list countries; specify whether territory includes online sales targeting Territory-based customers).

### 2. Product scope + modification rights
Define Products precisely in Schedule A. Include Supplier's right to add or remove products with [30/60/90] days' notice. Address new product lines: are they automatically included or subject to separate written agreement?

### 3. Minimum purchase commitments (MPC)
Specify quarterly or annual purchase minimums in Schedule C. State the consequence of missing MPC:
- Option A: Supplier's right to terminate exclusivity (converting to non-exclusive or sole) without penalties.
- Option B: Supplier's right to terminate Agreement entirely with [X] days' notice after miss.
- Option C: Cure period — Distributor may make up shortfall within [30] days of quarter end.

Avoid liquidated damages for MPC miss unless carefully calibrated; an excessive penalty may be unenforceable.

### 4. Pricing and payment terms
- Wholesale price per Schedule B (subject to update by Supplier with [60] days' notice).
- Payment terms: L/C, TT within [X] days of invoice, or prepayment.
- Currency: specify. Address exchange-rate risk allocation.
- Late-payment interest at [rate]% per annum or applicable statutory rate.

### 5. Marketing obligations
- Minimum annual marketing spend by Distributor ([X]% of annual net purchases).
- Approved marketing materials: Distributor uses Supplier-approved materials; new materials require Supplier sign-off.
- Trade show participation obligations.
- Reporting on marketing activities.

### 6. Distributor reporting
- Monthly sales reports (product, channel, geography, end-customer categories).
- Quarterly inventory reports.
- Prompt reporting of market intelligence, competitor activity, and regulatory changes.

### 7. IP and trademarks
- Grant of limited, non-exclusive license to use Supplier's trademarks and trade names solely for distribution of Products in Territory.
- No sublicensing without prior written consent.
- Quality control: Distributor's use of marks must meet Supplier's brand guidelines.
- On termination: immediate cessation of use; return of all branded materials.
- **Do not** grant Distributor any ownership rights in marks.
- MENA: address GCC trademark exhaustion — parallel imports from adjacent GCC markets may be an issue.

### 8. Confidentiality
Standard mutual NDA provisions. Include pricing, customer lists, and supplier terms as Confidential Information.

### 9. Limitation of liability
- Consequential, indirect, and loss-of-profit damages excluded from both sides.
- Aggregate liability cap at [12 months' fees / purchase value paid in preceding 12 months].
- Carve-outs: death/personal injury from Supplier's products; fraud; IP infringement indemnity.

### 10. Term and termination
- **Expiry**: Agreement expires at end of Term unless renewed by written agreement.
- **Convenience termination**: either party with [90/180] days' written notice (longer notice = more goodwill; shorter = more agility; calibrate to jurisdiction).
- **Cause termination**: immediate on: insolvency, material breach (with [30]-day cure period for curable breaches), criminal act by Distributor's principals, loss of required licenses.

### 11. Post-termination obligations
- Customer transition: Distributor cooperates in orderly transition; introductions to end customers.
- Inventory buyback: Supplier's option (at original purchase price) to repurchase unsold conforming inventory within [60] days post-termination.
- Non-compete: Distributor shall not distribute directly competing products in Territory for [12] months post-termination. Must be narrowly defined; excessive scope is unenforceable, particularly under EU competition law.
- Return of confidential materials, marketing assets, branded items.

## Jurisdictional notes

### MENA — Commercial Agency Laws (the critical trap)

Many MENA jurisdictions have Commercial Agency Laws that grant statutory protections to "commercial agents" — protections that survive in some form even in a "distribution" agreement if the relationship is characterized as one where the distributor promotes and sells on the supplier's behalf rather than purely buying and reselling.

| Jurisdiction | Law | Key protection | Threshold |
|---|---|---|---|
| **UAE** | Federal Law 18/1981 on Commercial Agency (as amended) | Registered commercial agents cannot be terminated without cause; compensation on non-renewal; exclusive jurisdiction of UAE courts; foreign supplier may not conduct business in UAE without registered agent in some sectors | If registered; also attaches to de facto exclusive selling arrangements in some court interpretations |
| **KSA** | Commercial Agency Regulations | Saudi agent/distributor must be Saudi national or 100% Saudi-owned company; exclusive agents protected on termination | Registration with MCI |
| **Egypt** | Commercial Agency Law 120/1982 | Compensation on termination; Egyptian courts have jurisdiction | Registered agents |
| **Qatar** | Law 8/2002 on Commercial Agencies | Similar protections | Registration |

**Practical rule:** if your distributor is exclusive, registered, and has been operating for years, it is at high risk of being characterized as a commercial agent regardless of contract language. Seek local counsel before terminating any long-standing exclusive MENA distribution relationship.

**Drafting mitigation:**
- Use "distributor" consistently; never use "agent", "representative", or "sales agent".
- Include a clear acknowledgment that the relationship is buy-resell, not agency.
- Do not give Distributor authority to bind Supplier to contracts.
- Consider registering the agreement as a "distribution agreement" not as a commercial agency.

### EU — Competition law (Vertical Agreements)

- EU Block Exemption Regulation 2022/720 on vertical restraints applies to distribution agreements below the 30% market-share threshold.
- **Hardcoded restrictions** (void and not block-exempted): fixing resale prices (RPM), absolute territorial protection (passive-sales restriction), restricting sales to end-users, and anti-competitive most-favored-nation clauses.
- Exclusive territory grants are permitted under the BER but must permit passive sales (responding to unsolicited orders from outside territory).
- Online sales restrictions: tight restrictions on online selling are no longer block-exempted post-2022.

### UK post-Brexit
- UK Vertical Agreements Block Exemption Order 2022 mirrors EU BER but applies to UK market.

## Anti-traps

1. **Never use "agent" language** in a distribution agreement — see MENA Agency Law table above.
2. **Non-compete post-term** — in EU jurisdictions, post-term non-compete in vertical agreements is limited to 1 year and must relate to competing goods in the same territory. Longer terms are not block-exempted.
3. **Jurisdiction clause** — always specify a neutral arbitration seat (ICC Paris, LCIA London, DIAC Dubai) for international distribution agreements; avoiding submission to MENA courts reduces the risk of agency-law characterization by a local court applying its own protective laws.
4. **Currency and price escalation** — in high-inflation environments (LB, EG), price-list update with [30]-day notice allows Supplier to maintain margins.

## Related skills

- [[draft-distribution-agreement-mena-extension]] — additional MENA-specific variant clauses for UAE, KSA, LB, and GCC contexts
- [[draft-agency-agreement]] — if the relationship is genuinely one of agency (solicitation on Supplier's behalf)
- [[draft-franchise-agreement]] — if the relationship involves a branded operating system, not just product resale
- [[review-commercial-contracts]] — review an existing distribution agreement for legal risk
- [[kb-commercial-agency-mena]] — reference pack on commercial agency law across MENA
