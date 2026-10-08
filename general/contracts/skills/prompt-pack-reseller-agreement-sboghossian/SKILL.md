---
name: prompt-pack-reseller-agreement-sboghossian
title: Reseller Agreement
description: Use when a vendor and a reseller need to formalize a distribution arrangement, covering authorized products, territory, pricing and discount structures, minimum order quantities or targets, marketing and branding obligations, trademark usage, warranty pass-through, and exit terms. Particularly relevant for MENA distribution channels where commercial agency law (UAE, KSA, LB, EG) creates mandatory protections for local agents and distributors that can be difficult to unwind.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/prompt-pack/prompt-pack-reseller-agreement
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: contracts
language: en
---

# Reseller Agreement

## When to use this

Use this skill when:
- A manufacturer or vendor wants to appoint a reseller to purchase its products and on-sell them to end customers.
- A technology company is appointing a value-added reseller (VAR) to bundle its software with services.
- A company is appointing a regional distributor in a MENA country and needs to avoid accidentally creating a commercial agency relationship (which triggers mandatory statutory protections).
- An existing distribution relationship needs to be formalized with a written contract.

**CRITICAL MENA WARNING:** In the UAE, KSA, Lebanon, and Egypt, a reseller or distributor who also represents the vendor's interests may qualify as a "commercial agent" under mandatory commercial agency law. If that law applies, the agent acquires statutory rights — including the right to compensation on termination and potentially the right to continue the arrangement — that cannot be contracted out of. Carefully assess before drafting whether this agreement creates a commercial agency relationship. See Jurisdictional notes below.

## Required inputs

| Input | Why it matters | Default if omitted |
|---|---|---|
| **Vendor (supplier) details** | Party granting the resale rights | Ask |
| **Reseller details** | Party authorized to purchase and resell | Ask |
| **Products authorized for resale** | The scope of what can be resold | Ask; list specifically — vagueness leads to disputes |
| **Territory** | Geographic scope of the reseller's authorization | Ask; exclusive vs. non-exclusive has major commercial and legal consequences |
| **Exclusivity** | Exclusive appointment in territory vs. non-exclusive | Ask; default: non-exclusive (exclusive requires competition law analysis) |
| **Jurisdiction / governing law** | Determines whether commercial agency law applies | Ask; this is the highest-risk question in MENA context |

## Optional inputs

- **Minimum purchase commitments or sales targets** — if targets are minimum order requirements, address what happens on failure (loss of exclusivity, termination).
- **Pricing and discount schedule** — can be in a schedule rather than the main agreement body so it can be updated without amending the contract.
- **Sub-reseller rights** — whether the reseller may appoint sub-resellers.
- **Marketing development fund (MDF)** — vendor funding for the reseller's marketing activities.

## Document structure

1. **Appointment and scope**
   - Grant of authority: vendor appoints reseller as [exclusive / non-exclusive] reseller for the [Products] in the [Territory].
   - Scope of products: attach a product schedule; update by written agreement.
   - Exclusivity mechanics: if exclusive, does the vendor retain the right to sell directly to named accounts (house accounts)?
   - Non-circumvention: vendor agrees not to sell the Products directly to customers in the Territory except through the reseller (if exclusive).

2. **Reseller obligations**
   - Minimum purchase commitments or minimum sales targets (annual, quarterly, or both).
   - Active promotion and marketing of the Products in the Territory.
   - Compliance with vendor's brand guidelines and marketing standards.
   - Prohibition on reselling outside the Territory.
   - Prohibition on modifying or repackaging Products without written consent.
   - Compliance with applicable export controls.
   - Maintenance of qualified sales and technical staff.

3. **Ordering and fulfillment**
   - Purchase order process: form, acceptance, lead times.
   - Delivery terms: Incoterms (e.g., DAP, DDP, FCA) — specify.
   - Inspection and acceptance: timeframe for the reseller to inspect and reject defective Products.
   - Title and risk of loss: typically on delivery per the agreed Incoterms.

4. **Pricing and payment**
   - Reseller purchase price: list price minus discount percentage (stated in Schedule or set by vendor's published reseller price list, as updated from time to time).
   - Payment terms: net 30 / net 60 from invoice date.
   - Currency.
   - Late payment interest.
   - Right to adjust pricing on [X days'] written notice (specify minimum notice period).
   - Prohibited: reseller undercutting vendor's direct sales price (if this is the commercial intent; address RPM competition law risks).

5. **Intellectual property and trademark use**
   - Vendor grants reseller a limited, non-exclusive, non-transferable license to use vendor's trademarks solely to market and resell the Products in the Territory.
   - Reseller must comply with vendor's trademark and brand guidelines.
   - All goodwill in vendor's IP accrues to vendor.
   - No modification of vendor's products, packaging, or documentation.
   - Reseller may use its own trade name alongside vendor's brand.

6. **Warranty and product liability**
   - Vendor's standard end-customer warranty: whether it passes through to reseller's customers or whether reseller provides its own.
   - Reseller is responsible for customer-facing warranty claims; reseller has back-to-back rights against vendor for product defects.
   - Product liability: indemnification chain from vendor to reseller for product defects; reseller indemnifies vendor for claims arising from reseller's own modifications or representations.

7. **Term and renewal**
   - Initial term: typically 1–3 years.
   - Renewal: automatic renewal for 1-year periods unless either party gives [90 days'] written notice of non-renewal.
   - **Note for MENA:** long auto-renewal clauses can entrench a commercial agency relationship; set a finite term with active renewal decisions.

8. **Termination**
   - Termination for cause (breach, insolvency, sanctions list hit, change of control of reseller).
   - Termination for convenience: notice period of [90/180 days] for non-exclusive; longer for exclusive.
   - Effect of termination: reseller must cease using vendor's IP, return unsold stock (or vendor repurchases at invoice price), complete orders in transit.
   - **No compensation on termination** (for non-agency arrangements): include an express no-compensation clause and ensure the agreement does not trigger agency law (see Jurisdictional notes).

9. **Anti-corruption and compliance**
   - Reseller represents and warrants compliance with applicable anti-bribery laws (UAE Federal Penal Code, Saudi Anti-Bribery Law, UK Bribery Act, US FCPA as applicable).
   - Reseller agrees not to make any payment on vendor's behalf to any government official.
   - Vendor's right to audit reseller's compliance with anti-corruption provisions.
   - Sanctions compliance: reseller will not resell to sanctioned parties or jurisdictions.

10. **Confidentiality**
    - Standard mutual confidentiality for pricing, customer lists, trade secrets.

11. **Governing law and dispute resolution**
    - For MENA reseller agreements where commercial agency law risk is present: choose a governing law carefully — some jurisdictions will apply their commercial agency law regardless of choice-of-law clause if the agent operates there.
    - Arbitration preferred for cross-border disputes.

## Jurisdictional notes

### UAE — Commercial Agency Law (Federal Law No. 18 of 1981, amended by Law No. 13 of 2006 and subsequent amendments)
- The UAE Commercial Agency Law applies to any arrangement where a UAE national or UAE-national-owned company is appointed as an agent or distributor of a foreign principal's products for commercial or industrial activities.
- Key protections: (1) the agent can only be terminated for a valid reason agreed in the contract; (2) the agent is entitled to compensation on termination; (3) the agent can be registered with the Ministry of Economy's commercial agency register, and a registered agent can block imports of the principal's products into the UAE.
- **How to avoid:** appoint a reseller who buys and sells in its own name, on its own risk, for its own profit — this is a straightforward buy-sell distribution relationship, not agency. Document this clearly: the reseller takes title to goods, bears credit risk, and is not acting as the vendor's representative.
- Even with careful drafting, UAE courts have looked past form to substance; if the reseller is economically dependent on one principal, a commercial agency relationship may be implied.

### KSA — Commercial Agency Law (Royal Decree M/11 of 1962)
- Similar mandatory agent protections; local agent (Saudi national or Saudi-owned company) acquires statutory rights on appointment.
- Agents are registered with the Ministry of Commerce.
- Terminating a registered agent without compensation is prohibited; compensation is typically equivalent to 2 years of commission/profit.
- Non-exclusivity is sometimes used to limit exposure but registered agents can still assert rights.

### Lebanon — Commercial Agency Law (Legislative Decree No. 34 of 1967)
- Lebanese commercial agents have strong statutory protections including the right to continue the arrangement and damages on unjustified termination.
- Lebanese courts interpret "commercial agent" broadly.

### Egypt — Commercial Agency Regulation (Law No. 120 of 1982)
- Foreign companies must appoint a registered Egyptian agent; the agent has termination compensation rights.
- Import activity requires an approved commercial agent.

### EU (generally)
- EU Commercial Agents Directive (86/653/EEC): applies to agents who negotiate or conclude contracts on behalf of a principal. A reseller who buys and sells for its own account is **not** an agent under the Directive.
- Competition law: EU and GCC competition rules restrict resale price maintenance, territorial restrictions, and selective distribution; obtain competition law advice before including territorial exclusivity or price floor provisions.

### UK (post-Brexit)
- UK Commercial Agents Regulations 1993 mirror the EU Directive; same scope exclusion for buy-sell resellers.
- Post-Brexit: UK and EU apply their own competition rules separately.

## Drafting standards

- The title "Reseller Agreement" (not "Agency Agreement" or "Distribution and Agency Agreement") matters — use it deliberately.
- Include an express clause: "Reseller purchases Products in its own name and for its own account and risk. Reseller is not an agent of Vendor and has no authority to bind Vendor to any contract or obligation with any third party."
- If commercial agency law of a MENA jurisdiction may apply regardless, include a severability clause and a clause stating that the parties intend a buy-sell distribution relationship, not an agency.
- Define the Territory with precision: "United Arab Emirates" (all seven emirates) vs. "Dubai and Abu Dhabi only" vs. "GCC" — vagueness generates disputes.

## Common mistakes

- **Accidentally creating a commercial agency relationship.** Using language like "represent," "act on behalf of," "promote as our agent" in correspondence or side letters can override the contract's buy-sell characterization.
- **Exclusive territory without competition law analysis.** Exclusive distribution agreements can raise competition concerns in many jurisdictions; get competition law sign-off before granting an exclusive.
- **Minimum purchase commitments without cure/remedy mechanism.** If targets are missed, the contract must say what happens: grace period, loss of exclusivity, right to terminate. Without this, failure creates deadlock.
- **No product update/removal mechanism.** Products change; the agreement must allow vendor to add new products to or remove products from the reseller's authorized list.
- **Trademark license surviving termination.** Ensure the IP license automatically terminates with the agreement; otherwise the reseller may continue to use the vendor's brand post-termination.

## Related skills

- [[prompt-pack-service-agreement]]
- [[prompt-pack-supply-agreement]]
- [[prompt-pack-technology-licensing-agreement]]
- [[prompt-pack-standard-nda]]
- [[heuristic-always-state-jurisdiction-first]]
- [[heuristic-no-us-style-boilerplate-in-civil-law-jx]]
