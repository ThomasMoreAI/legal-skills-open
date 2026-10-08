---
name: draft-joint-venture-sboghossian
title: Joint Venture Agreement
description: Use when drafting a joint venture agreement for two or more parties pursuing a shared business purpose, whether as a contractual cooperation or a newly incorporated entity (NewCo). Covers governance, contributions, profit sharing, reserved matters, deadlock resolution, exit mechanisms, and critical MENA-specific issues such as foreign-ownership restrictions and commercial agency law in UAE, KSA, and Lebanon. Triggers on "joint venture", "jv agreement", "joint company", or "shared enterprise" requests.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/draft/draft-joint-venture
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: corporate
language: en
---

# Joint Venture Agreement

## When to use this

Use this skill when two or more parties wish to combine resources — capital, IP, market access, or technical expertise — to pursue a defined business purpose while maintaining separate legal identities outside the JV. Common triggers:

- A foreign company and a local partner in KSA, UAE, or Lebanon combining to pursue a contract that requires local presence
- Two companies co-investing to build and operate a shared plant, facility, or platform
- A tech company and a regional distributor forming a local entity to market and support software
- Two firms pooling R&D resources for a defined innovation project without merging

If the agreement is primarily about governance of an existing company (rather than forming a new one), use [[draft-shareholders-agreement]] instead.

## Two fundamental structures

### 1. Contractual JV
No separate entity is created. Parties contract for cooperation: scope, contributions, cost and revenue sharing, governance. Faster to form, easier to unwind, but weaker on liability segregation.

Best for: short-term project collaboration, smaller-scale commercial cooperations, or situations where regulatory approval for a new entity is impractical.

### 2. Corporate JV
A new entity (NewCo) is incorporated. Parties hold shares per agreed ratio. The JV agreement governs the relationship between shareholders; the NewCo's corporate documents (articles/constitution) implement it.

Best for: long-term ventures, ventures requiring separate contracts with third parties, ventures involving shared assets, or situations where liability isolation matters.

In MENA corporate JVs, the instrument stack typically comprises:
- **JV Agreement** (master relationship document)
- **Shareholders' Agreement / Subscription Agreement** (NewCo governance)
- **Articles of Association / Constitutional Document** (NewCo's organic rules)
- **IP License or Service Agreements** between each parent and the NewCo

## Required inputs

| Input | Why it matters | Default |
|-------|---------------|---------|
| Parties — names, types, roles (operator / financial / technical) | Determines governance design | — must supply |
| JV purpose — precisely defined | Defines the venture's scope and what's excluded; limits liability | — must supply |
| Structure — contractual or corporate; if corporate, jurisdiction of NewCo | Determines entire legal framework | Corporate NewCo unless deal is transient |
| Contributions — cash / IP / services / market access per party | Drives valuation, equity split, and future capital calls | — must supply |
| Ownership — % equity, voting rights, preferential rights | Core governance | Pro rata to contribution |
| Governance — board composition, management, reserved matters, deadlock resolution | Prevents operational paralysis | See governance section below |
| Profit/loss allocation — pro rata or separate formula | Cash flows determine partner incentives | Pro rata to equity |
| Exit mechanisms — buy-sell, drag/tag, IPO, dissolution | Allows the JV to end or restructure cleanly | See exit section below |

## Document structure

1. **Recitals** — Each party's background, the rationale for the JV, the mutual intent.
2. **Definitions** — JV Business, Parties, NewCo (if applicable), Contributions, Reserved Matters, Deadlock.
3. **Formation / structure** — Contractual vs corporate; if corporate, NewCo jurisdiction, capital structure, share classes.
4. **Contributions** — Tabular schedule per party: cash (amount, timing), IP (describe with ownership), services (scope, valuation), market access (customer relationships, licenses). Contribution failure provisions.
5. **Governance**
   - **Board / management committee composition** — e.g., 2 seats per party for a 50/50 JV; tie-breaking mechanism
   - **Day-to-day management** — who is CEO/MD? How appointed? Dismissal
   - **Reserved matters** (see below) — requiring supermajority or unanimity
   - **Information rights** — quarterly financials, annual audited accounts, board observer rights
6. **Reserved matters list** — Actions requiring heightened approval (all parties or specified majority), typically:
   - New capital raising / dilution of either party beyond X%
   - Any acquisition or disposal above a threshold (e.g., > USD 500k)
   - Change of core business
   - Related-party transactions above threshold
   - Taking on debt beyond approved limits
   - Appointing or removing auditors
   - Amendments to the JV Agreement or NewCo constitution
   - Settlement of any claim above threshold
7. **IP arrangements**
   - Pre-existing ("background") IP: each party licenses to the JV for the venture's purpose only; ownership stays with the contributing party
   - Foreground IP (developed in the JV): who owns? Often NewCo, but parties should agree on license-back rights if the JV dissolves
   - Survival: IP licenses granted to the JV must terminate or be dealt with on dissolution
8. **Financial provisions**
   - Initial capital contributions: timing, form
   - Future capital calls: process, consent thresholds, consequences of default (dilution, forced sale)
   - Profit distribution: declaration policy, frequency, currency, withholding
   - Loss funding: are parties obligated to fund losses beyond initial contributions?
9. **Deadlock resolution** — When a reserved-matter vote is tied or blocked:
   - Stage 1: Escalation to senior management (30 days)
   - Stage 2: Mediation (30 days)
   - Stage 3: Deadlock-breaking mechanism — choose one:
     - **Texas / Russian roulette**: Party A names a price; Party B must buy at that price or sell at that price. Creates fair-value discipline.
     - **Dutch auction / sealed bid**: Both parties submit sealed bids; highest bidder buys out the other at that price.
     - **Put/call options**: One party has the right to compel sale at a formula price after deadlock persists for X months.
   - Consider which mechanism best suits the relative power balance of the parties.
10. **Transfer restrictions**
    - Lock-up period (no transfers for X years)
    - Right of first refusal / offer (ROFO / ROFR) before any transfer to a third party
    - Drag-along: majority can require minority to sell alongside
    - Tag-along: minority can require inclusion in any majority sale
    - Change-of-control (no transfer of control in a party without JV consent)
11. **Non-compete** — Each party agrees not to compete with the JV within the defined JV Business during the JV term and typically for 12-24 months post-termination. Scope must be carefully limited to the JV purpose to be enforceable.
12. **Term and dissolution**
    - Fixed term (e.g., 10 years) or project-completion-based
    - Dissolution events: expiry, party insolvency, persistent deadlock, agreed exit
    - Winding-up process: pay creditors, return capital, distribute assets
    - Goodwill on dissolution: expressly allocate (especially important in LB and FR civil-law contexts)
13. **Governing law and dispute resolution** — For cross-border MENA JVs: DIAC arbitration at DIFC or ADGM seat is common; neutral seat plus English-language proceedings avoids local court complications.
14. **Boilerplate** — see [[draft-boilerplate-clauses]].

## Jurisdictional notes

| Jurisdiction | Key issues |
|---|---|
| **DIFC / ADGM** | Standard common-law JV norms; stack JV Agreement + SHA + Subscription Agreement; Companies Law DIFC Law No. 5 of 2018 / ADGM Companies Regulations 2015; full contractual freedom on governance |
| **UAE federal (mainland)** | Foreign ownership: UAE Commercial Companies Law (Federal Decree-Law 26/2021) eliminated general 51% local ownership requirement for most sectors — 100% foreign ownership now possible in most activities; but certain "strategic" sectors remain restricted. Commercial agencies: if the JV appoints one party as the exclusive promoter or distributor, UAE Commercial Agency Law (Fed Law 3/1987) may characterize the arrangement as a protected agency. Mainland LLC minimum capital AED 300k |
| **KSA** | Foreign-ownership rules controlled by the Foreign Investment Law (Royal Decree M/1/2000 as amended); MISA licensing required for foreign-investment vehicles. Some sectors restricted to Saudi nationals or require majority Saudi ownership (healthcare, media, etc.). Sharia: JV profit-sharing structures (mudaraba / musharaka) may be preferred for partners operating under Islamic finance principles |
| **LB** | Civil-law société commune (partnership) for contractual JV; offshore holding structure common for corporate JV due to Lebanese corporate law complexity. Goodwill (fonds de commerce) accrual is a significant factor: on dissolution, a party operating the JV business may claim goodwill compensation |
| **GCC generally** | Consider whether any GCC registered commercial agent relationship exists with any JV party — these can create unexpected entanglements on dissolution |

## Critical clauses — checklist

- [ ] Reserved matters list drafted specifically for this deal (not a generic template)
- [ ] Deadlock mechanism selected with clear procedure and timing
- [ ] IP license to NewCo: scope, exclusivity, termination right on JV dissolution
- [ ] Future capital call mechanics: notice, cure, dilution formula
- [ ] Non-compete scope limited to JV Business (over-breadth will not be enforced)
- [ ] Governing law and arbitration clause with named seat and rules
- [ ] Change-of-control provision (what happens if a party is acquired by a competitor)

## Common mistakes

- Using a generic 50/50 JV structure without a deadlock mechanism — the venture stalls on the first real disagreement
- Failing to document IP contributions with registration numbers; "contributing our technology" without specifics creates ownership disputes
- Setting reserved-matter thresholds too low, requiring unanimous consent for routine decisions, leading to operational paralysis
- Omitting the goodwill-on-dissolution clause in civil-law jurisdictions (LB, FR) — operational party may claim significant goodwill not reflected in equity ratio
- Not verifying that neither party's existing commercial agency relationships in the target country are inadvertently affected by the JV

## Related skills

- [[draft-shareholders-agreement]]
- [[draft-distribution-agreement]]
- [[draft-msa]]
- [[draft-nda-mutual]]
- [[draft-ip-licensing]]
