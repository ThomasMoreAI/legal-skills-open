---
name: prompt-pack-agency-agreement-sboghossian
title: Agency Agreement
description: Use when drafting a commercial agency agreement appointing an agent to solicit orders or sell products/services in a defined territory on behalf of a principal. Covers corporate/commercial practice across all jurisdictions, with particular attention to mandatory MENA commercial agency laws (UAE, KSA, Lebanon, Egypt) that override contractual freedom and create registration and termination obligations.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/prompt-pack/prompt-pack-agency-agreement
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: contracts
language: en
---

# Agency Agreement

## When to use this

Use this skill when a principal wants to appoint a commercial agent to:
- Solicit orders and/or conclude sales on the principal's behalf
- Represent the principal's products or services in a defined territory
- Act as exclusive or non-exclusive agent for a product line or geography

This skill is particularly important in the MENA context because most MENA jurisdictions have **mandatory commercial agency laws** that apply regardless of what the agreement says — a governing-law clause pointing to English law does not dis-apply UAE Federal Commercial Agencies Law, for example.

---

## Prompt template

> Draft a commercial agency agreement appointing [Agent] to [solicit orders for/sell] [products/services] in [territory] on behalf of [Principal]. Include commission structure, reporting obligations, exclusivity terms, and compliance with local agency laws of [jurisdiction].

Use [[conversation-clarifying-questions]] to elicit `[bracketed]` inputs before drafting.

---

## Required inputs

| Input | Why it matters | Default if omitted |
|-------|---------------|-------------------|
| Principal name and jurisdiction | Governs registration requirements; determines home-country law | Ask |
| Agent name and jurisdiction | Critical for mandatory agency-law applicability (must agent be a national?) | Ask |
| Territory | Defines exclusivity scope; overlapping territories in agency networks create disputes | Ask |
| Products/services | Registration and exclusivity rules often apply per-product | Ask |
| Commission structure | Core economic term; percentage, base, calculation method, payment timing | Ask |
| Exclusivity (yes/no) | Determines agent's rights on termination under mandatory law | Ask; note mandatory-law implications |
| Governing law | Sets the contractual framework; note that MENA mandatory laws apply anyway | Ask |

---

## Optional inputs

- Duration (fixed term vs. indefinite): critical — in many MENA jurisdictions, indefinite agreements are harder to terminate
- Sub-agency rights
- Minimum purchase/sales targets
- Marketing obligations on agent
- Dispute resolution mechanism (arbitration seat, institution)
- IP licensing linked to agency (agent's use of principal's marks)

---

## Document structure

1. **Parties and recitals** — full legal names, jurisdiction of incorporation, registered addresses; recital describing the principal's products and the purpose of the agency relationship
2. **Appointment and territory** — scope of appointment; territory definition (precise geographic boundaries or named countries); exclusivity or non-exclusivity; carve-outs (direct sales by principal, key accounts)
3. **Scope of authority** — what the agent may and may not do: solicit orders only vs. conclude contracts; authority limits (order size, price range, credit terms); no authority to bind principal beyond these limits
4. **Commission** — commission rate; calculation basis (net revenue, invoice value, collected amounts?); payment timing (on order, on invoice, on collection?); deductions permitted; clawback on cancellation; reporting obligations of principal to agent
5. **Obligations of agent** — due diligence; minimum activity commitments; reporting obligations to principal; compliance with laws; not to represent competing products (exclusivity obligation)
6. **Obligations of principal** — provide agent with samples, marketing materials, product information; commission payment; not to solicit directly in territory (if exclusive)
7. **IP and confidentiality** — license of principal's marks for the territory; restrictions on use; return of materials on termination; confidentiality obligations
8. **Term and termination** — fixed vs. indefinite; notice period; termination for cause; effect of mandatory law (see jurisdictional notes); post-termination obligations
9. **Compensation on termination** — where mandatory law applies, specify and do not attempt to contract out
10. **Governing law and dispute resolution** — governing law; arbitration clause (seat, institution, language, number of arbitrators); note that mandatory local law may apply regardless
11. **Miscellaneous** — entire agreement; amendment; notices; severability; language

---

## Jurisdictional notes

### UAE
UAE Federal Commercial Agencies Law (Federal Law 18/1981 as amended) applies to commercial agents who are UAE nationals or UAE-national-owned companies registered with the Ministry of Economy Commercial Agencies Register. Key mandatory terms:
- Agent must be UAE national (individual) or UAE-national-majority company
- Exclusivity is the statutory default once registered
- Compensation on unjustified termination is mandated regardless of contractual provisions
- Disputes often go to the Commercial Agencies Committee before court

A non-UAE agent acting as a commercial agent (distributing, not just soliciting) may not qualify for the mandatory law's protections but should take legal advice on whether the law applies.

### KSA
Commercial Agency Regulation (Royal Decree M/11/1962 and successor regulations under Ministry of Commerce) requires registration. Saudi agents must be Saudi nationals or Saudi-majority companies. The agent has statutory termination compensation rights. Sharia-law prohibition on interest affects commission payment timing and penalties for late payment.

### Lebanon
Commercial Code provisions on agency; no separate mandatory commercial agency registration law equivalent to UAE, but agency agreements with Lebanese agents benefit from certain protections under general contract law and labour-analogous protections for long-standing agents.

### Egypt
Commercial Agency Law No. 120/1982 applies to distribution and agency. Egyptian agent must be Egyptian national or Egyptian-majority company. Registration at Egyptian Commercial Agency Registry required. Unilateral termination compensation applies.

### DIFC / ADGM
Contract law governs. No mandatory commercial agency registration. Freedom of contract applies. Termination governed entirely by the agreement and DIFC/ADGM Contract Law. Much more flexible than UAE onshore.

### France
Law No. 91-593 of June 25, 1991 (transposing EU Directive 86/653/EEC) gives commercial agents mandatory indemnity rights on termination. Parties cannot contract out. The indemnity is typically one to two years of average commission.

---

## Drafting standards

- Do not use "at will" termination without a notice period — in all MENA civil-law jurisdictions, abrupt termination without notice triggers damages
- Do not attempt to exclude mandatory law protections in the termination clause — such clauses are unenforceable and create false comfort
- In civil-law jurisdictions, a penalty/liquidated-damages clause for agent breach must be proportionate; disproportionate penalties may be judicially reduced
- State the commission calculation method precisely — disputes over commission calculation are the most common commercial agency disputes
- Address the treatment of orders placed before termination but executed after — this is a frequent gap

---

## Common mistakes

- Using a US-style "independent contractor" agreement format without adapting for MENA mandatory agency law
- Assuming the governing-law clause displaces the local mandatory agency law — it does not
- Indefinite term with no notice period — creates termination liability exposure
- No carve-out for direct sales by principal to key accounts (named accounts list should be attached)
- Commission payable "on collection" with no provision for principal-caused non-collection

---

## Related skills

- [[prompt-pack-agreement-legal-draft-review]] — review an existing agency agreement
- [[heuristic-always-state-jurisdiction-first]] — jurisdiction-first drafting rule
- [[heuristic-no-us-style-boilerplate-in-civil-law-jx]] — avoid US boilerplate in civil-law jurisdictions
- [[kb-commercial-agency-mena]] — knowledge base on MENA commercial agency laws
- [[draft-distribution-agreement]] — when the agent takes title (distribution vs. agency)
