---
name: prompt-pack-distribution-agreement-sboghossian
title: Distribution Agreement
description: Use when drafting a distribution agreement appointing a distributor for the sale and distribution of products in a defined territory. Covers exclusivity, minimum purchase commitments, pricing, marketing obligations, IP licensing, and termination. Particularly important in MENA (UAE, KSA, LB, EG) where commercial agency and distribution laws impose mandatory protections for local distributors that can survive contract termination. Trigger when a supplier or manufacturer needs to appoint a distributor, or when a distributor needs to protect its position.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/prompt-pack/prompt-pack-distribution-agreement
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: contracts
language: en
---

# Distribution Agreement

## When to use this

Use this skill when drafting or reviewing a distribution agreement — the contract by which a supplier (principal) appoints a distributor to sell and distribute products in a defined territory. Distribution agreements are commercial staples, but in MENA they carry elevated risk: most GCC states and Lebanon have mandatory commercial-agency laws that give local distributors statutory rights to compensation and continuation of the arrangement that cannot be waived by contract.

Typical triggers:
- Supplier appointing a first distributor in a new market
- Renegotiating or renewing an existing distribution arrangement
- Distributor seeking to document its rights and minimum protections
- Cross-border distribution with IP licensing components

## Required inputs

| Input | Why it matters | Default if omitted |
|---|---|---|
| Supplier/Principal name and jurisdiction | Identity and law governing its obligations | Ask |
| Distributor name and jurisdiction | Identity; determines applicability of local agency laws | Ask |
| Product description | Scope of what is being distributed | Ask |
| Territory | Geographic scope; exclusivity determination | Ask |
| Exclusive or non-exclusive | Fundamental commercial term | Ask |
| Governing law and dispute resolution | Critical for enforceability | Ask |

## Optional inputs

- Minimum purchase commitments (annual/quarterly) and consequences of shortfall
- Pricing mechanism (list price less discount, or FOB/CIF terms)
- Marketing / advertising obligations and spend commitments
- IP license scope (trademarks, patents, trade dress for territory)
- Sub-distribution rights (can distributor appoint sub-distributors?)
- Term (fixed vs. evergreen) and renewal conditions
- Post-termination obligations (stock buy-back, customer transition, IP return)

## Document structure

1. **Parties and recitals** — Supplier and distributor; background and purpose.

2. **Appointment and exclusivity**
   - Grant of right to distribute in the territory
   - Exclusive or non-exclusive; consequences of either
   - No-compete obligation on supplier not to sell directly in the territory (if exclusive)

3. **Products and territory**
   - Product schedule (reference by SKU or description)
   - Territory (map reference or country list)
   - Right of first refusal for additional products or territories (optional)

4. **Orders and supply**
   - Order procedures; lead times; acceptance of orders
   - Pricing (list price, discount table, currency, payment terms)
   - Minimum order quantities; minimum purchase commitments per period

5. **Distributor obligations**
   - Active promotion and sale of products; marketing spend commitment
   - Compliance with supplier's branding, packaging, and labeling standards
   - Maintenance of minimum inventory; storage conditions
   - Customer service and after-sales support
   - Reporting (monthly/quarterly sales reports, pipeline, market intelligence)

6. **Supplier obligations**
   - Supply continuity and lead times
   - Provision of marketing materials, training, and product information
   - Price protection notice period
   - Non-circumvention during term

7. **Intellectual property**
   - License to use supplier's trademarks and trade dress in the territory
   - No ownership rights conferred on distributor
   - Distributor to notify supplier of infringements
   - Post-termination cessation of IP use

8. **Pricing and payment**
   - Price list; right to revise with notice period
   - Payment terms (30/60/90 days from invoice)
   - Currency; withholding tax allocation

9. **Compliance**
   - Import/export licensing and customs clearance (who bears?)
   - Regulatory approvals for products (health, safety, sector-specific)
   - Anti-bribery / anti-corruption compliance (FCPA / Bribery Act / local laws)
   - Sanctions compliance

10. **Term and termination**
    - Initial term; renewal mechanics
    - Termination for convenience (with notice period)
    - Termination for cause (material breach, insolvency, change of control)
    - Consequences of termination: stock buy-back, run-off, non-solicitation

11. **Limitation of liability and indemnity**
    - Mutual indemnity for breach; product liability indemnity from supplier
    - Consequential loss exclusion

12. **Governing law and dispute resolution** — Arbitration clause (ICC, DIAC, LCIA) recommended for cross-border; choice of seat.

## Jurisdictional notes

### MENA — Mandatory Commercial Agency Laws (Critical)

| Jurisdiction | Key law | Critical protections | Cannot be waived? |
|---|---|---|---|
| **UAE** | Commercial Agencies Law (Federal Law No. 18 of 1981, as amended) | Registered agent/distributor entitled to compensation on termination regardless of cause; exclusivity assumed if registered | Only registered agents benefit; registration with MoEI is optional but determines whether the law applies |
| **KSA** | Commercial Agencies Regulation (Royal Decree M/11, 1962, as amended) | Similar protections; Saudi national or entity required to be the agent; Ministry of Commerce registry | Yes; termination compensation mandatory if registered |
| **Kuwait / Qatar / Bahrain** | Equivalent GCC commercial agency laws | Similar mandatory compensation and continuation rights | Yes |
| **Lebanon** | Legislative Decree No. 34 of 1967 (Commercial Agency Law) | Exclusive distributor entitled to compensation on termination for lost goodwill | Compensation obligation survives contract terms to contrary |
| **Egypt** | Commercial Code Art. 282; Commercial Agency Law | Similar agency protections; commercial registry | Partial; parties may agree on notice but compensation for goodwill survives |
| **DIFC / ADGM** | Common law; no mandatory agency law applies within the free zone | Freedom of contract; termination for convenience effective | No mandatory protections |

### Practical Consequence
In UAE, KSA, and Lebanon, if the distributor registers the arrangement under the local commercial agency law, the supplier may be unable to terminate the agreement without paying substantial compensation — even if the contract expressly allows termination on notice. Suppliers should: (a) seek legal advice before appointing a registered agent, (b) consider keeping the distributor relationship outside the scope of the mandatory agency laws by structuring as a non-exclusive supply arrangement or operating through a free zone entity.

### EU / UK
The EU Commercial Agents Directive (86/653/EEC) gives commercial agents (but not distributors acting as principal) statutory compensation or indemnity on termination. In a distribution arrangement (distributor buys and resells as principal), the Directive typically does not apply — confirm the structure.

## Drafting standards

- Define "Products" by reference to a schedule, not generically — avoids scope disputes.
- Minimum purchase commitments should specify consequences: reduction from exclusive to non-exclusive (not termination) is a proportionate remedy that courts are more likely to uphold.
- Include a price protection clause: distributor should have advance notice of price increases to protect already-placed orders.
- Anti-corruption clause: mirror FCPA/UK Bribery Act standards if either party operates in high-risk markets; include a right to audit distributor's books.
- Specify that the distributor is not an agent and has no authority to bind the supplier.

## Common mistakes

- **Not checking mandatory agency law**: Failing to assess whether the local commercial agency law applies before signing is the single most costly mistake in MENA distribution deals.
- **Vague exclusivity**: "Exclusive distributor" without defining what "exclusive" means (no direct sales? no parallel importers? no online sales?) leads to disputes.
- **No minimum purchase commitment**: Without a commitment, exclusivity has no commercial quid pro quo and the supplier cannot justify terminating for poor performance.
- **Missing post-termination stock buy-back**: Distributor left holding inventory on termination will claim damages; address this in advance.
- **Ignoring import/customs obligations**: Who obtains import licenses? Who bears tariffs? In KSA/UAE, these obligations need to be explicit.

## Related skills

- [[prompt-pack-franchise-agreement]]
- [[prompt-pack-independent-contractor-agreement]]
- [[prompt-pack-full-contract-risk-review]]
- [[prompt-pack-engagement-letter]]
