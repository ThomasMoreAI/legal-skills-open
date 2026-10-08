---
name: draft-agency-agreement-sboghossian
title: Draft — Commercial Agency Agreement
description: Use when asked to draft a commercial agency agreement appointing an agent to sell goods or services on a principal's behalf, particularly in MENA jurisdictions where statutory agent-protection regimes create significant termination indemnity exposure. Covers agent authority, commission, exclusivity, reporting, IP, termination compensation, and the critical decision of whether to structure as a registered commercial agency or an ordinary services contract.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/draft/draft-agency-agreement
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: contracts
language: en
---

# Draft — Commercial Agency Agreement

## When to use this

Use this skill when a principal (manufacturer, service provider, or franchisor) appoints an agent to:
- Solicit orders or make sales on the principal's behalf in a defined territory.
- Represent the principal's brand and products with customers.
- Earn commission on transactions introduced or concluded.

**Critical first question**: Does the client want a *registered* commercial agency or an *ordinary* services agreement? These have profoundly different consequences in MENA jurisdictions — a registered commercial agency creates mandatory statutory protections for the agent that are expensive to terminate.

## Required inputs

| Input | Why it matters | Default if absent |
|---|---|---|
| Principal name and jurisdiction | Determines which law applies to the principal's side | Must ask |
| Agent name, nationality, jurisdiction | KSA and UAE require Saudi/UAE nationals for registered agencies | Must ask |
| Territory | Defines agent's exclusive scope; any sale outside territory is not commissionable | Ask; default to one country |
| Products / services in scope | Narrowing scope limits agent's claim on adjacent products | Ask |
| Commission rate and structure | Determines agent's economic interest | Ask; note common range 3–15% |
| Exclusivity (or not) | Exclusive agencies have stronger termination indemnity in most MENA laws | Ask |
| Term | Fixed-term vs indefinite; affects renewal and indemnity calculations | Ask |
| Governing law and dispute resolution | Onshore UAE vs DIFC vs KSA courts/arbitration | Must ask |

## Optional inputs

- Minimum performance targets (failure → termination trigger)
- Reporting format and frequency
- Marketing support obligations from principal
- Sub-agency rights (default: none)
- Non-compete scope post-termination

## Document structure

1. **Parties** — full legal names, registration numbers, authorized signatories
2. **Appointment** — exclusive or non-exclusive; registered or unregistered; territory
3. **Products/services scope** — precise list; mechanism for adding new products
4. **Agent's authority** — solicitation authority only (no authority to contract on principal's behalf unless expressly granted by Power of Attorney)
5. **Commission** — rate; calculation base (net vs gross); payment timing; disputed commissions; commission on post-termination orders introduced during term
6. **Performance obligations** — minimum sales targets (if any); reporting; customer relationship management
7. **Marketing and support** — principal's obligation to supply samples, literature, training
8. **Confidentiality and IP** — agent does not acquire any IP rights; brand use guidelines
9. **Non-competition** — scope and duration post-termination (enforceability varies — see jurisdictional notes)
10. **Term and renewal** — initial term; auto-renewal mechanism; notice for non-renewal
11. **Termination** — for cause (material breach, insolvency); for convenience; consequences
12. **Termination indemnity** — see jurisdictional notes; often the most heavily negotiated clause
13. **Governing law and dispute resolution**
14. **Boilerplate** — see [[draft-boilerplate-clauses]]

## Jurisdictional notes — termination indemnity (the critical risk)

### UAE — Federal Decree-Law 3/2022 (Commercial Agencies Law)
- **Registered** commercial agents have mandatory statutory protection.
- Termination without cause (or non-renewal) triggers indemnity even if the contract is silent.
- Indemnity calculation: profits earned over life of agreement; disputed and often large.
- **Non-registered** arrangements: treated as ordinary contracts; agent has only contractual rights.
- **Practical advice**: if the principal does not want statutory exposure, structure the agreement as an ordinary services or distribution contract rather than registering as a commercial agency with the Ministry of Economy.

### KSA — Royal Decree M/8 (1962, amended)
- Agent must be a Saudi national (individual) or Saudi-owned company.
- Commercial Agency Register with the Ministry of Commerce: mandatory for distribution/sales arrangements.
- Non-registration does not eliminate statutory protections — courts apply them anyway.
- Termination indemnity: courts award significant amounts; minimum one year's average commission is a common baseline.
- **Sharia note**: Interest on overdue commission is structurally awkward; use "delay compensation" language tied to actual loss.

### Lebanon — Decree-Law 34/1967
- Commercial agents and representatives with exclusive arrangements have mandatory renewal rights and indemnity on termination.
- Indemnity = two years' average annual commission (minimum statutory baseline).
- Courts are pro-agent; contractual exclusions of indemnity are generally void.

### Egypt — Law 120/1982
- Commercial agents registered with the Commercial Agents Registry.
- Termination indemnity: courts have wide discretion; typically one to two years' commission.

### DIFC / ADGM
- Common-law principles apply; no statutory commercial agency protection.
- Termination governed by contract; agency principles from English law (apparent authority, secret profits, fiduciary duties).
- Much lower termination risk than onshore MENA jurisdictions.

## Drafting standards

- Define "Commission" and "Net Sales Price" with precision — ambiguous definitions are the most common source of post-termination disputes.
- State explicitly whether the agent has authority to bind the principal in contract; if not, make clear in writing.
- For onshore UAE/KSA/LB: draft in Arabic (primary language) with English translation; Arabic controls.
- For DIFC/ADGM: English sufficient; Arabic not required.
- If using Tawqi3i (Lebanese e-signature notarization): see [[inst-tawqi3i-esignature-bridge]].

## Common mistakes

- **Calling it an "agency" when you want a service contract**: use this label only deliberately in MENA; it triggers statutory protections.
- **No minimum performance targets**: without them, termination for underperformance is contestable.
- **Vague territory definition**: disputes arise over online sales, inbound customers from outside territory, customers with operations in multiple countries.
- **Omitting post-termination commission tail**: agent who introduces a deal before termination typically retains commission if the sale closes after termination — define this.
- **Penalty clauses for late payment in KSA**: draft as pre-estimate of loss, not penalty.

## Related skills

- [[draft-brokerage-agreement]]
- [[draft-consulting-agreement]]
- [[draft-boilerplate-clauses]]
- [[draft-bilingual-ar-en-side-by-side]]
