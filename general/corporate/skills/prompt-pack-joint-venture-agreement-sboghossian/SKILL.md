---
name: prompt-pack-joint-venture-agreement-sboghossian
title: Joint Venture Agreement
description: Use when drafting a joint venture agreement between two or more parties establishing a shared commercial enterprise. Covers ownership structure, capital contributions, management, profit and loss allocation, exit mechanisms, deadlock resolution, and non-compete obligations. Applies to contractual and corporate JV structures across MENA, GCC, EU, and common-law jurisdictions, with special attention to foreign ownership restrictions and Sharia-compliant considerations.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/prompt-pack/prompt-pack-joint-venture-agreement
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: corporate
language: en
---

# Joint Venture Agreement

## When to use this

Use this skill when two or more parties want to collaborate on a defined commercial project or ongoing business activity through a jointly controlled structure. The JV may be:
- **Contractual** (no new entity — parties act under a partnership or contractual arrangement)
- **Corporate** (parties establish a new company — LLC, JSC, or SPV)

Triggers:
- "We want to set up a 50/50 company in the UAE with a local partner."
- "Draft a JV agreement for a construction consortium in Saudi Arabia."
- "We need a contractual JV for a real estate development project in Lebanon."

## Required inputs

| Input | Why it matters | Default if omitted |
|---|---|---|
| Party A and Party B names, jurisdictions, ownership | Determines applicable law, capacity, shareholding | Ask user |
| JV purpose / project description | Defines scope and limits activities | Ask user |
| Ownership percentages | Drives profit/loss allocation and voting rights | 50/50 unless stated |
| Capital contributions | Amount, type (cash/in-kind/IP), timing | Ask user |
| JV structure | Contractual vs corporate; if corporate, entity type | Ask user |
| Governing law | Critical for enforceability, form requirements | Jurisdiction where JV operates |
| Duration | Fixed term or indefinite | Indefinite with exit triggers |

## Optional inputs

- Sharia-compliance requirement (profit-sharing structure under mudaraba or musharaka principles)
- Deadlock mechanism preference (casting vote, Russian roulette, buy-sell, mediation)
- Dispute resolution preference (court or arbitration; institutional rules)
- Non-compete scope and duration
- IP ownership and licensing-back arrangements for contributed technology

## Document structure

1. **Recitals** — describe the parties, the intended JV, and the purpose for entering the agreement.

2. **Definitions** — define key terms: "Affiliate," "Business," "JV Company," "Confidential Information," "Net Profit," "Deadlock."

3. **Establishment of the JV** — if corporate: obligation to incorporate the JV Company, jurisdiction of incorporation, timeline; if contractual: declare the contractual JV and its scope.

4. **Ownership and shareholding** — ownership percentages; any preference rights, anti-dilution provisions, or reserved matters requiring supermajority.

5. **Capital contributions** — initial contributions by each party; obligation to make further capital calls; consequences of default on a call (dilution or compulsory transfer).

6. **Governance and management**
   - Board composition and appointment rights (proportional to shareholding)
   - Reserved matters requiring unanimous or supermajority board approval (e.g., major capex, new debt, material contracts, budget approval, change of business)
   - Day-to-day management: appointing a General Manager or CEO; reporting obligations

7. **Profit and loss allocation** — pro-rata to ownership unless Sharia-compliant structure requires agreed profit ratios independent of capital ratio (note: in musharaka, profit ratio can differ from ownership but loss must mirror capital contribution).

8. **Transfer restrictions**
   - Lock-up period (typical: 2–3 years from incorporation)
   - Right of first refusal (ROFR) in favor of the non-transferring party
   - Tag-along and drag-along rights
   - Change-of-control provisions (deemed transfer if parent company changes)

9. **Deadlock resolution**
   - Definition of deadlock (typically: board resolution fails to pass on a reserved matter twice within [30/60] days)
   - Steps: escalation to senior management, then mediation, then buy-sell mechanism
   - Buy-sell (shotgun): either party may offer to buy the other's interest at a stated price; the other party must elect to sell or to buy the offering party's interest at the same price

10. **Exit mechanisms**
    - Voluntary exit: notice period and buy-out pricing (fair market value or agreed formula)
    - Dissolution triggers: insolvency, regulatory prohibition, material breach
    - Liquidation waterfall: priority of distributions on wind-up

11. **Non-compete and non-solicitation**
    - Scope: activities competing with the JV's defined business
    - Territory: jurisdictions where the JV operates
    - Duration: typically 2 years post-exit (note enforceability varies — see below)

12. **IP** — each party's background IP remains its property; any IP created by or for the JV vests in the JV entity (or is jointly owned per agreed ratio); licence-back arrangements if background IP is used.

13. **Confidentiality** — mutual; survives termination for 3–5 years.

14. **Governing law, dispute resolution, language** — critical for MENA cross-border JVs.

## Jurisdictional notes

| Jurisdiction | Key issues |
|---|---|
| **UAE (onshore)** | Foreign ownership up to 100% now permitted in most sectors under the 2021 Commercial Companies Law reforms; however, certain "strategic sectors" still require UAE national majority. GCC national as local partner has different treatment. Arabic contract text may be required for official registration. |
| **KSA** | SAGIA/MISA licensing required for foreign investment; certain sectors have mandatory Saudi partner requirements. JV entities typically LLC (SRC). Sharia compliance may require profit-sharing structure. |
| **DIFC / ADGM** | 100% foreign ownership; English-law governed; no Arabic requirement for registration. DIFC / ADGM Courts available. Popular for regional holding JVs. |
| **Lebanon** | Foreign ownership of commercial companies generally permitted at 100%; real estate sector subject to restrictions. SAL (société anonyme libanaise) for corporate JV. High risk of currency and political instability — include force majeure and currency provisions. |
| **Egypt** | Foreign investment governed by Investment Law No. 72 of 2017; some sectors restricted. Profit repatriation protection available under investment law guarantees. |
| **France / EU** | EU foreign direct investment screening may apply for strategic assets. Société en participation (contractual JV) is a commonly used civil-law structure. |

**Non-compete enforceability note**: In civil-law jurisdictions (LB, EG, FR), courts apply a reasonableness standard to non-competes; overly broad restrictions will be reduced or struck down. In UAE, non-compete clauses are enforceable if limited in time, geography, and scope (Labour Law for employees; Commercial Code for commercial parties). In KSA, courts may assess non-competes under principles of harm prevention.

**Deadlock / dissolution note**: DIFC and ADGM law provide reliable judicial dissolution remedies. In UAE onshore, Ministry of Economy winding-up procedures are more bureaucratic; contractual deadlock mechanisms and exit routes are especially important.

## Common mistakes

- **Missing reserved matters list**: Without a defined list, majority party can make unilateral decisions that minority considers fundamental.
- **Vague profit distribution formula**: "Pro-rata" is unclear if parties contribute capital at different times or in different forms; specify the accounting basis and distribution frequency.
- **No buy-out pricing mechanism**: If parties cannot agree fair market value at exit, the JV can become deadlocked indefinitely; include an expert determination fallback.
- **Ignoring local foreign ownership rules**: Agreeing to a 60/40 structure that violates a sectoral restriction can render the JV registration impossible.
- **No governing law clause**: In MENA cross-border JVs, choice of law is often disputed. An express clause choosing a neutral forum (e.g., DIFC, ADGM, English law) avoids costly jurisdictional disputes.

## Related skills

- [[prompt-pack-memorandum-of-understanding]]
- [[prompt-pack-letter-of-intent]]
- [[prompt-pack-merger-agreement]]
- [[prompt-pack-non-compete-agreement]]
- [[prompt-pack-master-services-agreement]]
