---
name: draft-prenup-sboghossian
title: Prenuptial Agreement (Premarital / Antenuptial Agreement)
description: Use when drafting a prenuptial (premarital) agreement governing property division and financial obligations before marriage. Covers jurisdictional recognition rules (strong in DIFC, ADGM, UK, France; variable in LB by confession; Sharia-constrained in KSA; expanded for non-Muslims in UAE under Federal Law 41/2022), recommended content, procedural enforceability requirements (full disclosure, independent counsel, voluntariness, notarization), and what a prenup cannot override (child support, Sharia inheritance). Triggers on "prenup", "prenuptial", "premarital agreement", "contrat de mariage", or "marriage settlement" requests.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/draft/draft-prenup
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: family
language: en
---

# Prenuptial Agreement (Premarital / Antenuptial Agreement)

## When to use this

A prenuptial agreement is a contract entered into before marriage that establishes each spouse's rights and obligations in respect of property, finances, and support, particularly upon divorce or death. Use this skill when:

- One or both prospective spouses have significant pre-marital assets (real estate, business interests, investments, inheritance)
- One or both parties has children from a prior relationship whose interests must be protected
- There is a significant wealth disparity between the parties
- The parties intend to keep certain assets or family businesses separate throughout the marriage
- The marriage has an international dimension (parties from different countries, property in multiple jurisdictions)

**Legal caution**: prenuptial agreement law is among the most jurisdiction-specific areas of family law. A prenuptial agreement valid in France may be unenforceable in Lebanon. An agreement valid for non-Muslim UAE residents under the new civil personal-status law may have no effect for Muslims. Always verify with a family-law practitioner in the relevant jurisdiction(s) before finalizing.

## Jurisdictional recognition — overview

| Jurisdiction | Recognition level | Key requirement |
|---|---|---|
| **DIFC** | Strong — full contractual enforcement | DIFC law applies; common-law principles; fair, voluntary, full disclosure |
| **ADGM** | Strong | Same as DIFC |
| **UK** | Strong (with caveats) | Not automatically binding but courts give "decisive weight" to a fair agreement with full disclosure and independent advice (*Radmacher v Granatino* [2010] UKSC 42); courts retain overriding discretion |
| **France** | Strong | "Contrat de mariage" — fully enforceable if made before a notaire; civil Code allows parties to choose their matrimonial regime (séparation de biens, communauté universelle, etc.) |
| **Germany** | Enforceable | Civil-law tradition; notarization required; court may review for fairness at enforcement |
| **US (most states)** | Enforceable per UPAA/UPMAA | Full financial disclosure; independent counsel; voluntary; not unconscionable |
| **UAE (non-Muslim)** | Now available under Federal Law 41/2022 | Civil personal-status court for non-Muslims; written agreement governable by home-country law or UAE civil law |
| **UAE (Muslim)** | Sharia governs | Sharia courts apply Islamic personal-status law; limited scope for prenuptial variation of Sharia rules (mahr, inheritance, custody) |
| **KSA** | Sharia governs | Marriage is a contract (عقد الزواج) under Sharia; parties may agree certain terms (e.g., wife's right to employment, additional mahr) but cannot override Sharia inheritance, divorce rights, or child custody |
| **Lebanon (LB)** | Heavily fragmented by confession | Each religious community's personal-status court applies its own rules; civil prenups rarely enforceable for religiously governed divorces; Druze, Greek Orthodox, Maronite, Sunni, Shia, Armenian — each confessional court has its own family law system |
| **Egypt (EG)** | Limited | Sharia governs for Muslims (Personal Status Law); Coptic church law for Copts; agreement terms that conflict with personal-status law are void |

## Required inputs

| Input | Why it matters |
|-------|---------------|
| Both prospective spouses (full identification) | Parties; capacity to contract |
| Jurisdiction of intended marital domicile | Primary governing law |
| Property situs jurisdictions | Separate analysis may be needed for each location of real property |
| Religion / confession | Controls which court will have jurisdiction in LB, KSA, and EG |
| Current assets of each party (full disclosure) | Inadequate disclosure is the primary ground for invalidation |
| Anticipated children | Confirm that no waiver of child support is being attempted |
| Specific provisions wanted | What each party wants protected |

## Recommended content

### 1. Identification of parties and capacity
Full legal names, nationalities, passports/IDs, domicile, and capacity declaration. Confirm each party is entering freely and voluntarily.

### 2. Recitals
- Statement of intent to marry
- Acknowledgment that each party is entering of their own free will
- Acknowledgment of full and mutual financial disclosure
- Statement that each party has had independent legal advice

### 3. Asset disclosure schedule
A complete schedule (Exhibit A for each party) listing all material assets:
- Real estate (title deed numbers, estimated value)
- Business interests (company name, jurisdiction, % ownership, estimated value)
- Bank accounts (institution, currency, approximate balance)
- Investments (brokerage accounts, securities portfolios, estimated value)
- Retirement accounts / pension
- Debts and liabilities
- Expected inheritances (if relevant and known)

**Critical**: inadequate disclosure is the single most common ground for invalidating a prenuptial agreement. Courts look at whether each party had a realistic picture of the other's financial position. Do not understate or omit material assets.

### 4. Property division rules

**Pre-marital property (each party's separately owned assets)**
Default: pre-marital property remains the separate property of the party who owned it before the marriage; no claim by the other spouse on divorce.

**Post-marital property**
The most negotiated provision. Options:
- **Full separation of property**: all assets acquired by either party during the marriage remain that party's separate property
- **Community of acquisitions**: all assets acquired during the marriage (by either party, except gifts and inheritances) become jointly owned
- **Custom hybrid**: certain categories (e.g., the family home) are jointly owned; other assets remain separate; professional income above a threshold is separately held
- **Jurisdictional default**: parties opt into their jurisdiction's default matrimonial property regime

**Gifts and inheritances**: universally, gifts given to and inheritances received by one spouse remain that spouse's separate property (even in community-property regimes). State this expressly.

### 5. Treatment of the matrimonial home
The family home is often the most sensitive asset. Options:
- Jointly owned from date of acquisition
- One party retains sole ownership but the other has a right of occupation during the marriage
- On divorce: sold with proceeds split per agreed formula; or one party can buy out the other at RICS valuation

### 6. Spousal support / maintenance on dissolution
- Full waiver of maintenance claims (not permissible in all jurisdictions — French law limits freedom to waive; some common-law courts will override an unconscionable waiver)
- Lump-sum payment in lieu of periodic maintenance
- Periodic maintenance for a defined period (income-replacement for non-working spouse during marriage)
- Maintenance tied to income differential

### 7. Estate planning provisions
A prenuptial agreement typically does not replace a will — it addresses the rights between spouses on divorce; death is governed by the will and the applicable succession law. Reference the parties' intention to execute wills; state that the prenup does not affect inheritance rights beyond what is expressly stated.

For Sharia jurisdictions: the prenup cannot override the fixed shares (fard) in Islamic inheritance law for heirs. Mahr (dowry) provisions in the marriage contract (not the prenup) may be addressed.

### 8. What a prenup CANNOT do

In all jurisdictions:
- **Child support and custody**: cannot be agreed in advance; child support is determined by the court at the time of divorce based on the child's best interests
- **Basic spousal maintenance waivers**: in some civil-law jurisdictions and for economically vulnerable spouses, courts will not enforce a complete maintenance waiver
- **Sharia inheritance shares (KSA, Muslim-governed UAE/LB/EG)**: the forced share system cannot be contracted out of
- **Illegal provisions**: the agreement cannot require either party to perform illegal acts or waive public-order rights

### 9. Choice of law and forum
Specify:
- Which law governs the agreement and its interpretation
- Which court or tribunal has jurisdiction for disputes
- For international couples: consider a reciprocal enforceability clause (if the agreement is valid under law X, the parties agree not to challenge it in any other court on public-policy grounds — this has limited effect but signals the parties' intent)

### 10. Severability and amendment
- If any provision is found unenforceable, the remaining provisions survive
- Amendment requires written agreement signed by both parties before a notary (or equivalent formality)

### 11. Notarization and witness requirements
- France: notarial form is mandatory (without the notaire, the "contrat de mariage" is void)
- UAE (non-Muslim civil court): written form; may require notarization depending on the courts' current practice
- KSA: consult local family-law attorney; written form plus witness requirements
- Lebanon: each confessional court has its own requirements — consult counsel for the applicable court
- UK: while notarization is not legally required, having the agreement signed before a notary and witnessed improves enforceability

## Procedural requirements for maximum enforceability

1. **Full financial disclosure** — both parties disclose all material assets and liabilities; this is documented in the disclosure schedule (Exhibit A for each party)
2. **Independent legal counsel** — each party retains their own separate family-law attorney who advises on the agreement; do not use the same attorney for both parties
3. **Voluntariness** — no duress; agreement signed well before the wedding (not the night before — courts frequently treat last-minute signatures as constructively coerced)
4. **Reasonable fairness** — the agreement must not be unconscionable; a provision leaving one spouse with nothing after a 20-year marriage may not survive judicial scrutiny
5. **Specific notarization** per the jurisdiction requirements
6. **Counterparts** — each party retains a signed original

## Common anti-patterns

- **Last-minute signature** (within 1-2 weeks before the wedding date) — creates duress claims; sign at least 30 days before, ideally more
- **One lawyer for both parties** — professional conflict; invalidates the "independent advice" protection
- **Sham asset disclosure** — understating assets is fraud; if discovered, the entire agreement is vulnerable
- **Attempting to waive child support** — courts will ignore this provision but it may affect the agreement's overall enforceability
- **Using a US-style agreement for a LB confessional court** — the court will simply apply its own rules regardless

## Related skills

- [[draft-power-of-attorney]]
- [[draft-will]]
- [[draft-property-sale-agreement]]
- [[review-estate-planning]]
