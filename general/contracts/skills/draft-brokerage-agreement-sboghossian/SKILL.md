---
name: draft-brokerage-agreement-sboghossian
title: Draft — Brokerage / Commercial Agency Agreement
description: 'Use when asked to draft a brokerage or commercial agency agreement under which a broker or intermediary introduces transactions or customers to a principal in exchange for commission. Covers appointment type, territory, commission structure, non-circumvention, authority limits, and MENA-specific statutory protections under UAE Commercial Agencies Law (FDL 3/2022), KSA Commercial Agencies Law, Lebanon Decree-Law 34/1967, and Egypt Law 120/1982. Critical: if the client wishes to avoid statutory agent protections, structure as a service contract instead.'
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/draft/draft-brokerage-agreement
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: contracts
language: en
---

# Draft — Brokerage / Commercial Agency Agreement

## When to use this

Use this skill when:
- A principal (seller or service provider) wishes to engage a broker or intermediary to introduce customers or close transactions in exchange for commission.
- A party needs a **non-circumvention** protection: the broker must be protected from the principal going directly to the introduced customers.
- The arrangement needs to be structured carefully in MENA to either preserve statutory agent protections (if the agent wants them) or avoid them (if the principal wants to avoid a large termination indemnity).

**Key preliminary question**: Is this a registered commercial agency (strong statutory protections for agent) or an ordinary intermediary / services arrangement (contractual rights only)? See the jurisdictional notes below.

## Required inputs

| Input | Notes |
|---|---|
| Principal and broker identification | Full legal names, nationalities, jurisdictions |
| Territory | Geographic scope of the broker's engagement |
| Products / services in scope | Precise description; changes require amendment |
| Exclusivity | Exclusive (one broker per territory) or non-exclusive |
| Commission structure | % of deal value, flat fee per introduction, retainer + success fee |
| Commission calculation basis | Gross contract value, net revenue, cash received? |
| Commission payment timing | On signing, on payment by customer, on milestone? |
| Non-circumvention scope and duration | Protection against principal going direct; typical: 2 years post-introduction |
| Term and termination | Fixed term, rolling, notice for termination |
| Governing law | Critical given MENA statutory regime choice |

## Document structure

### 1. Appointment
- Exclusive or non-exclusive appointment of broker for the defined Territory and Products/Services.
- Statement of whether this is a registered commercial agency or an ordinary intermediary arrangement.
- Broker's capacity: acts as an intermediary only; does not contract on Principal's behalf unless a separate Power of Attorney is granted.

### 2. Scope — territory and products/services
- Precise geographic territory definition (e.g., "the Kingdom of Saudi Arabia" not just "the Gulf").
- Specific products or service categories in scope.
- Mechanism for adding new products (amendment or automatic inclusion — define clearly).

### 3. Commission
- **Rate**: percentage of [Gross Contract Value / Net Revenue / Cash Received] per introduced transaction.
- **Trigger**: when does commission become payable? At contract execution by the customer? At payment by customer? At project completion?
- **Commission statement**: Principal to provide monthly/quarterly commission statements; broker's right to audit.
- **Disputed commissions**: procedure for raising disputes; payment of undisputed amounts; resolution mechanism.
- **Post-termination commission tail**: broker retains commission rights on introductions made during the term that close after termination (specify the tail period, e.g., 6–12 months).

### 4. Non-circumvention
A well-drafted non-circumvention clause is often the broker's most valuable protection:

> *"The Principal shall not, during the term of this Agreement and for a period of [two (2) years] after termination, directly or indirectly enter into any agreement with, solicit, or engage in any business with any customer introduced by the Broker under this Agreement, without the Broker's prior written consent. Any such direct engagement shall entitle the Broker to the agreed commission as if the transaction had been introduced through the Broker."*

- Duration: 2 years is market standard; longer may be challenged.
- Scope: define "introduced" carefully — the Broker's list of introduced customers should be maintained as a schedule, updated regularly.

### 5. Authority limits
Unless a Power of Attorney is expressly granted (and recorded where required):
- Broker has no authority to enter into contracts on Principal's behalf.
- Broker has no authority to bind Principal to pricing or delivery commitments.
- All customer agreements must be executed directly between Principal and customer.
- Broker may negotiate on Principal's behalf as an intermediary only, subject to Principal's written approval of final terms.

### 6. Reporting obligations
- Periodic reporting (monthly/quarterly): pipeline of opportunities, progress on introductions.
- Customer contact log: names, contact details, meetings held.
- Conflict of interest disclosure: Broker must disclose if acting for competing principals.

### 7. Confidentiality and IP
- Broker receives confidential product/pricing information; standard confidentiality obligations apply.
- No IP rights pass to Broker; brand use guidelines apply.

### 8. Term and termination
- Initial term and auto-renewal (if desired).
- Notice for termination: 30–90 days; longer for registered agencies.
- Termination for cause (material breach, insolvency, loss of required license).
- Effect of termination: post-termination commission tail; return of confidential materials.

### 9. Governing law and dispute resolution
- See [[draft-boilerplate-clauses]] for standard options.
- For MENA: governing law choice directly affects whether statutory agency protections apply (see below).

## MENA statutory protections — critical analysis

### UAE — Federal Decree-Law 3/2022 (Commercial Agencies Law)

**Registered commercial agency**:
- Agent must be a UAE national (individual) or UAE-nationally-owned company.
- Registration with the Ministry of Economy (Commercial Agencies Register).
- Once registered, the agent has **statutory protection on termination or non-renewal**:
  - Principal cannot terminate without compensation even if contract is silent.
  - Compensation = amount determined by the Commercial Agencies Committee or courts; typically significant (often multiple years' profit/commission).
  - The Committee has exclusive jurisdiction before any court/arbitration proceeding can be initiated.
- **Exclusivity is automatic** for registered agencies within the registered territory and products.

**Non-registered arrangement**:
- Ordinary contract; agent has only contractual rights.
- No mandatory statutory compensation on termination.
- Can be structured under general civil/commercial law.

**Principal's strategy**: if the principal is a foreign company wanting MENA representation without the statutory indemnity exposure, structure as a non-registered services/distribution arrangement rather than a registered commercial agency.

### KSA — Commercial Agencies Law (Royal Decree M/8 1962, as amended)

- Agent must be a Saudi national (individual or Saudi-owned company).
- Registration with Ministry of Commerce mandatory for ongoing representation.
- **Statutory protections**:
  - Termination without cause triggers indemnity.
  - Courts commonly award 1–3 years' average commission as minimum.
  - KSA courts are consistently pro-agent.
- Arbitration clauses in agency agreements are frequently challenged in KSA courts, which assert jurisdiction notwithstanding the clause.

### Lebanon — Decree-Law 34/1967

- Commercial agents and representatives with exclusive arrangements have mandatory indemnity rights on termination.
- Statutory indemnity: two years' average annual commission (minimum statutory baseline; courts may award more).
- Courts strictly enforce; contractual exclusions of indemnity are void.

### Egypt — Law 120/1982

- Commercial agents registered with the Commercial Agents Registry.
- Termination indemnity: courts have discretion; typically 1–2 years' commission.
- Egyptian courts tend to be pro-agent.

### DIFC / ADGM — no statutory protection
- Common-law agency principles apply.
- No statutory commercial agency protection regime.
- Termination governed entirely by the contract.
- Much lower risk for principals.

## Avoiding statutory protections — structural alternatives

If the principal does not want the MENA statutory agency exposure, consider:

1. **Service contract / consultancy agreement**: Broker is engaged as a consultant for introductions; not characterized as a commercial agent. See [[draft-consulting-agreement]].
2. **Distributor agreement**: Broker buys and resells; not an agent. Distributor protections exist separately but are generally weaker.
3. **Non-exclusive arrangement**: statutory protections attach more strongly to exclusive agencies; non-exclusive reduces (but does not eliminate) exposure in some jurisdictions.
4. **DIFC / ADGM governing law and jurisdiction**: if parties can agree to DIFC/ADGM law, statutory MENA agency protections do not apply.

## Common mistakes

- **Using the word "agency" loosely**: in MENA, calling an arrangement an "agency" without understanding the statutory consequence is the source of many large indemnity claims.
- **No post-termination commission tail**: a broker who invested time in a relationship deserves commission on deals they introduced, even if they close after termination.
- **No introduced-customer list**: without a documented list, "circumvention" claims are difficult to prove.
- **Vague commission base**: "5% of the deal" — deal value, net revenue, cash received, or something else? Ambiguity always resolves against the drafter.
- **KSA arbitration clause without realistic expectation**: KSA courts may override an arbitration clause in commercial agency disputes; factor this into the governing law choice.

## Related skills

- [[draft-agency-agreement]]
- [[draft-consulting-agreement]]
- [[draft-boilerplate-clauses]]
- [[draft-bilingual-ar-en-side-by-side]]
