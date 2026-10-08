---
name: draft-distribution-agreement-mena-extension-sboghossian
title: MENA Distribution Agreement — Jurisdiction Variants
description: Use as a companion to draft-distribution-agreement when the distribution arrangement involves MENA jurisdictions. Provides jurisdiction-specific variant clauses for KSA, UAE, Lebanon, and GCC contexts — including commercial agency registration risk mitigation, UAE Commercial Agencies Law (Federal Law 18/1981) analysis, KSA Saudi-national ownership requirements, Lebanese commercial agency law nuances, and GCC trademark exhaustion considerations.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/draft/draft-distribution-agreement-mena-extension
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: cross-jurisdiction
practice: contracts
language: en
---

# MENA Distribution Agreement — Jurisdiction Variants

## When to use this

Use this skill **in addition to** [[draft-distribution-agreement]] whenever the distributor is based in, or the territory includes, one or more MENA jurisdictions. The base distribution skill covers general structure; this extension provides the MENA-specific variant clauses, registration risk analysis, and local-law compliance checks that transform a generic agreement into a MENA-appropriate instrument.

The most important function of this skill is helping parties avoid the **commercial agency trap**: inadvertently creating a protected commercial agency relationship under local law, which can make termination extraordinarily expensive.

## UAE — Federal Law 18/1981 on Commercial Agency (as amended)

### What the law does
UAE Federal Law 18/1981 (Commercial Agencies Law) protects registered commercial agents: a UAE national or 100%-UAE-owned company appointed to distribute, sell, or offer goods or services on behalf of a foreign principal in the UAE.

Once registered with the Ministry of Economy as a commercial agent:
- The agent/distributor cannot be terminated without "material cause" (a high bar).
- On non-renewal at expiry, the agent may be entitled to compensation.
- UAE courts (not foreign courts or arbitral tribunals) have exclusive jurisdiction over disputes concerning the registered agency.
- The principal cannot appoint parallel agents/distributors for the same products in the same territory without terminating the existing registration.

### Drafting approach to minimize agency-law exposure

1. **Confirm the relationship is buy-resell** — include an explicit acknowledgment: "The Distributor acknowledges that it is an independent contractor purchasing Products for resale on its own account and at its own risk, and is not an agent, partner, employee, or joint venturer of the Supplier."

2. **Avoid registration** — if the parties do not register the agreement as a commercial agency with the Ministry of Economy, the full statutory protections are less likely to apply (though courts have in some cases applied protective provisions even to unregistered arrangements where the economic reality is that of an agent).

3. **No authority to bind** — the agreement must not give the Distributor authority to conclude contracts on the Supplier's behalf.

4. **Dispute resolution in DIFC / ADGM** — if the Supplier is a DIFC or ADGM entity, DIFC/ADGM court jurisdiction can offer a route around UAE federal commercial agency court jurisdiction.

5. **Non-exclusive preferred** — exclusive territory grants are the highest-risk factor. If exclusivity is commercially necessary, consider limiting it by product sub-category, channel, or customer type.

### Variant clause — UAE relationship acknowledgment
> "The Distributor is an independent business purchasing Products from the Supplier for resale in the Territory on the Distributor's own account and at the Distributor's own risk. The Distributor has no authority to create obligations binding on the Supplier or to act as the Supplier's legal representative. Nothing in this Agreement shall be construed as creating a commercial agency, joint venture, employment, or partnership relationship between the parties."

## KSA — Commercial Agency and Distribution

### Ownership requirement
Under KSA regulations, foreign companies may not directly distribute most products in the KSA market without a Saudi commercial partner. MISA (Ministry of Investment) licenses foreign-owned distribution companies in some sectors, but the historical default is:
- Distributor must be a Saudi national or a company with ≥51% Saudi ownership.
- The 2021 Company Law and ongoing Vision 2030 reforms allow 100% foreign ownership in many sectors; verify current rules for the specific product category.

### Commercial Agency Regulations
KSA commercial agents (registered with the Ministry of Commerce) enjoy statutory protections similar to UAE. Key differences:
- Registration with MCI required for statutory protection to attach formally.
- Compensation on termination / non-renewal is assessed by reference to the business generated.
- KSA courts have jurisdiction over registered commercial agency disputes.

### Drafting approach for KSA
1. Use an unregistered distribution structure where commercially viable.
2. Include Saudization / Nitaqat compliance acknowledgment from the Distributor (Distributor maintains required Saudization ratio in its workforce).
3. Consider a Memorandum of Understanding for the initial pilot period before formalizing a long-term distribution commitment.
4. Specify Riyadh Regional Court or SCCA arbitration (Saudi Center for Commercial Arbitration) as dispute resolution to demonstrate confidence in Saudi legal system while maintaining predictability.

### Variant clause — KSA Nitaqat compliance
> "The Distributor warrants that it is in compliance with applicable Saudization (Nitaqat) requirements and shall maintain such compliance throughout the Term. The Distributor shall promptly notify the Supplier of any change in its Nitaqat rating that could affect its ability to engage in commerce in the Kingdom."

## Lebanon — Commercial Agency Law

### Applicable law
Lebanon's commercial agency regime is governed by the Code of Commerce (Legislative Decree 304/1942 and subsequent amendments) and specific provisions applicable to commercial agents.

Key features:
- A commercial agent who contributes to building the principal's clientele may claim an "indemnity of clientele" on termination, representing the value of the customer base developed — even where the contract is for a fixed term.
- The indemnity claim exists regardless of the agent/distributor's characterization in the agreement if the economic substance is that of a commercial agency.
- Lebanese courts apply the substance-over-form principle.

### Drafting approach for Lebanon
1. Explicitly characterize the relationship as a purchase-resale arrangement.
2. Include a buy-back clause for termination scenarios (Distributor receives fair-market value for inventory rather than an open-ended "clientele" claim).
3. Arbitration in a neutral seat (Paris ICC, London LCIA) — Lebanese courts apply Lebanese agency-law protections even where a foreign-law choice is made, so neutral arbitration is preferred.
4. Shorter initial terms (1–2 years) with renewal at Supplier's discretion to reduce the "expected continuation" argument for indemnity.

## GCC — Trademark and Parallel Imports

### Exhaustion of trademark rights
GCC trademark law generally follows a **national exhaustion** model (not international exhaustion), meaning:
- A trademark owner's rights in Saudi Arabia are not exhausted by a legitimate sale in UAE (or vice versa).
- A KSA-authorized distributor can theoretically block parallel imports of the same product sold by a UAE distributor, even if both are authentic goods.

### Practical impact on distribution drafting
- Exclusive distributors in one GCC state may be exposed to parallel imports from adjacent GCC states where the product is sold at lower prices.
- Include a **parallel import restriction clause**: "Distributor shall not, and shall not permit any sub-distributor to, sell or distribute Products outside the Territory or to any person known or reasonably believed to intend resale outside the Territory."
- Consider whether a GCC-wide distribution agreement (covering all six GCC states) is more practical than state-by-state exclusivity.

## Egypt — Law 120/1982 on Commercial Agents

Egyptian commercial agent protection is robust:
- Agents registered with the Commercial Agents Registry at the Egyptian General Authority for Investment (GAFI) receive statutory protection.
- Termination indemnity is mandatory; quantum is assessed by courts on equitable grounds considering the volume of business generated.
- The exclusive nature of the relationship is not required for protection to attach; economic dependence of the agent on the principal suffices.

**Drafting approach:** follow the same buy-resell structure as UAE. Avoid registration. Include Egyptian arbitration (Cairo Regional Centre for International Commercial Arbitration) or foreign-seated arbitration with Egyptian enforcement provisions.

## Cross-GCC checklist

Before finalizing any MENA distribution agreement, confirm:

- [ ] Is the distributor nationality/ownership compliant with local foreign-ownership rules?
- [ ] Has the parties' legal relationship been characterized explicitly as buy-resell (not agency)?
- [ ] Is the agreement intended to be registered as a commercial agency? (Yes/No decision must be deliberate.)
- [ ] Has the governing law and dispute resolution been set to minimize exposure to local commercial agency court jurisdiction?
- [ ] Is the GCC parallel-import issue addressed?
- [ ] Does the agreement include a practical inventory buyback at termination to preempt clientele indemnity claims?
- [ ] Has local counsel in the distributor's jurisdiction reviewed the agreement?

## Related skills

- [[draft-distribution-agreement]] — base distribution agreement structure and standard clauses
- [[draft-agency-agreement]] — for relationships that are genuinely commercial agency (agent solicits orders on principal's behalf)
- [[kb-commercial-agency-mena]] — full reference pack on commercial agency laws across MENA
- [[draft-franchise-agreement]] — if the relationship involves a branded operating system
