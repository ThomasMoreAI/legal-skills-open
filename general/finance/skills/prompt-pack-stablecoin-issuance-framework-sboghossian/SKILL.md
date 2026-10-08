---
name: prompt-pack-stablecoin-issuance-framework-sboghossian
title: Stablecoin Issuance Framework
description: Use when a company planning to issue a stablecoin needs a legal framework memo covering reserve requirements, regulatory classification, redemption rights, audit obligations, consumer disclosures, and the applicable regulatory regime. Covers MENA-specific frameworks including UAE VARA Virtual Assets Regulation and CBUAE Payment Token Services Regulation, DIFC/ADGM virtual asset frameworks, EU MiCA, and the general architecture of stablecoin regulation globally.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/prompt-pack/prompt-pack-stablecoin-issuance-framework
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: finance
language: en
---

# Stablecoin Issuance Framework

## When to use this

Use this skill when:
- A company is planning to issue a stablecoin (fiat-referenced, commodity-backed, or algorithmic) and needs to understand the regulatory framework before committing to a jurisdiction.
- A legal team is preparing a regulatory gap analysis memo for a proposed stablecoin product.
- A client needs to compare jurisdictions (UAE vs. DIFC/ADGM vs. EU vs. UK) for stablecoin issuance.
- A virtual asset service provider (VASP) needs to understand how adding a stablecoin product to its offering changes its regulatory obligations.
- A company is responding to a regulatory inquiry about its stablecoin product.

**Currency and caveats:** Stablecoin regulation is among the fastest-moving areas of financial services law. This skill reflects the regulatory framework as of early 2026; specific thresholds, licensing requirements, and reserve rules change frequently. Always verify current rules with the relevant regulator before advising.

## Legal framework structure

A stablecoin issuance legal framework memo should address the following topics:

### 1. Classification of the stablecoin

The regulatory treatment of a stablecoin depends on its design:

| Stablecoin type | Reserve basis | Key regulatory implication |
|---|---|---|
| Fiat-referenced (e.g., USD-pegged) | Held fiat currency + short-term government debt | Most regulated; classified as e-money or payment token in most jurisdictions |
| Commodity-backed (e.g., gold-backed) | Physical commodities or commodity contracts | Variable; may require commodity trading license |
| Crypto-backed (e.g., DAI) | Collateralized by other crypto assets | Often treated as complex financial product; higher regulatory scrutiny |
| Algorithmic (no collateral) | Algorithmic supply mechanism | Highly scrutinized post-Terra/LUNA collapse; banned or heavily restricted in most major jurisdictions |

**Classification determines:**
- Which regulator has jurisdiction.
- What license category applies.
- What reserve and redemption rules apply.
- What consumer protection rules apply.

### 2. Jurisdiction selection

#### UAE — VARA (Virtual Assets Regulatory Authority)
- VARA was established in 2022 as Dubai's standalone virtual assets regulator (covers Dubai mainland + free zones except DIFC/ADGM).
- VARA Virtual Assets and Related Activities Regulations 2023 + activity-specific rulebooks (including a dedicated Stablecoin Rulebook).
- **Payment tokens (fiat-referenced stablecoins):** classified as Virtual Assets under VARA; issuance requires a VARA license (Category: VASP with issuance activity).
- Reserve requirements: 100% backing by high-quality liquid assets; assets held with regulated custodians; daily reconciliation.
- Redemption: issuers must honor redemption at par on demand.
- Audit: mandatory quarterly reserve audits by approved auditors.
- **CBUAE Payment Token Services Regulation:** the Central Bank of UAE issued a separate regulatory framework in June 2023 covering payment token services (dirham-referenced stablecoins and foreign currency payment tokens used in UAE). This regulation operates alongside VARA; issuers may need both CBUAE and VARA authorization depending on the token's use case and the entity's structure.
- Dirham-backed stablecoin (AED-pegged): falls under CBUAE's framework; the CBUAE must approve any dirham-backed stablecoin before it can be issued.

#### DIFC (Dubai International Financial Centre)
- DFSA is the regulator.
- The DFSA introduced a regulatory framework for Crypto Tokens (including Stablecoins) under the DFSA Rulebook (Crypto Token Module).
- A DFSA-licensed Crypto Token issuer must hold a Category 3 license with Crypto Token issuance permission.
- Reserve: 100% fiat backing; assets held with DFSA-approved custodians.
- Redemption: on-demand at par.

#### ADGM (Abu Dhabi Global Market)
- FSRA is the regulator.
- ADGM's Virtual Asset Framework (2018, updated 2022+) covers Virtual Asset Services including stablecoin issuance.
- FSRA requires Virtual Asset Service Providers to hold an FSP (Financial Services Permission) with a virtual asset endorsement.
- Reserve and redemption requirements broadly similar to DIFC.

#### KSA
- Saudi Arabia does not (as of 2026) have a comprehensive licensed stablecoin issuance framework.
- SAMA has issued guidance on digital currencies and virtual assets; issuing a stablecoin for use in Saudi Arabia by a Saudi entity requires SAMA approval.
- CAPA (Capital Market Authority) may also be relevant if the stablecoin has investment characteristics.
- The preferred approach for KSA-targeted stablecoins is to incorporate in a permitted offshore jurisdiction (DIFC, ADGM) and obtain approval for cross-border service provision.

#### EU — MiCA (Markets in Crypto-Assets Regulation, Regulation (EU) 2023/1114)
- MiCA came into full effect in December 2024 (with transition periods).
- **E-Money Tokens (EMTs):** fiat-referenced stablecoins; issuer must be an authorized credit institution or e-money institution; must publish a white paper approved by the national regulator.
- **Asset-Referenced Tokens (ARTs):** backed by a basket of assets; subject to authorization by EU national competent authority; must be significant token authorization from EBA if large.
- Reserve requirements (Art. 36): issuers of EMTs must maintain reserve assets equivalent to at least 100% of outstanding tokens; reserve assets must be segregated, invested in approved instruments.
- Redemption: holders can redeem at par at any time.
- Consumer disclosures: white paper mandatory; must include all material information about the token and issuer.
- "Significant" token rules: EMTs/ARTs exceeding thresholds (1 million holders or EUR 5 billion reserve) trigger enhanced EBA oversight.
- **Algorithmic stablecoins:** banned under MiCA if they claim to maintain a stable value without reserve assets.

#### UK
- UK HM Treasury consultation on crypto assets (2023–2024) has resulted in fiat-backed stablecoins being classified as regulated "payment arrangements" under the Financial Services and Markets Act 2000 (as amended by the Financial Services and Markets Act 2023).
- FCA is the regulator for stablecoin issuers.
- Regime is being finalized; check FCA published consultation papers for the latest.

#### US
- No federal stablecoin legislation as of early 2026 (multiple draft bills: STABLE Act, GENIUS Act in circulation).
- State money transmission licenses required in most states for fiat-backed stablecoin issuers.
- SEC has asserted jurisdiction over certain stablecoins; CFTC over others; the jurisdictional boundary is unresolved.
- OCC guidance permits national banks to hold stablecoin reserves.
- Not suitable for MENA-first product without dedicated US legal advice.

### 3. Reserve requirements

Across most regulated jurisdictions, a fiat-backed stablecoin issuer must maintain:
- **Quantity:** 100% backing of outstanding tokens at all times.
- **Quality:** reserves must consist of: cash deposits at regulated banks; central bank reserves; short-term government bonds (typically ≤ 90 days maturity); money market funds (institutional grade).
- **Segregation:** reserve assets must be held separately from the issuer's operating assets; held in trust or in a dedicated account.
- **Custody:** reserve assets must be held by an approved custodian (varies by jurisdiction).
- **Reporting and audit:** typically quarterly or more frequent independent audits; results published publicly.

### 4. Redemption rights

- Holders of fiat-backed stablecoins must be able to redeem at par (1 token = 1 USD / 1 AED / etc.) on demand or within a defined short settlement window.
- Redemption fees: may be permitted within limits; cannot effectively prevent redemption.
- Redemption gates (temporary suspension): only permitted in defined emergency circumstances; must be pre-approved by the regulator.
- **Consumer protection:** redemption right is the primary consumer protection in stablecoin regulation; any restriction must be disclosed prominently in the white paper.

### 5. Consumer and investor disclosures

All major frameworks require a white paper or prospectus equivalent that discloses:
- Full description of the stablecoin (type, backing, mechanics).
- Issuer identity and regulatory status.
- Reserve composition and custody arrangements.
- Redemption terms and any restrictions.
- Risk factors.
- Technical and cybersecurity information.
- Rights of token holders.
- Governance of the issuer.
- AML/CFT controls.

The white paper must be accurate, not misleading, and updated on material change.

### 6. AML/CFT requirements

All VASP frameworks require:
- KYC/AML program compliant with FATF standards.
- Transaction monitoring.
- Suspicious transaction reporting.
- Sanctions screening.
- Travel rule compliance for transfers above the applicable threshold.

FATF has issued guidance specifically on virtual assets and VASPs; the Travel Rule (Recommendation 16) is a key compliance area for stablecoin issuers.

### 7. Cross-border issuance

A stablecoin distributed globally creates multi-jurisdictional regulatory exposure. Consider:
- Which jurisdiction(s) are users located in?
- Does the issuer need local registration or licensing in each user's jurisdiction?
- Are there restrictions on receiving fiat-backed stablecoins from foreign issuers (KSA, EG)?
- Does the issuer need a UAE VARA license even if incorporated in DIFC?

## Memo structure (output format)

The legal framework memo should be organized as:

1. **Executive summary:** Jurisdiction recommendation and key regulatory requirements in bullet form.
2. **Product description:** Summary of the proposed stablecoin's structure and intended market.
3. **Regulatory classification:** Which category the stablecoin falls into in each relevant jurisdiction.
4. **Licensing requirements:** Step-by-step path to authorization in the recommended jurisdiction(s).
5. **Reserve and redemption requirements:** Operational requirements.
6. **Consumer disclosure obligations:** White paper / prospectus requirements.
7. **AML/CFT obligations:** Framework and controls required.
8. **Cross-border considerations:** Multi-jurisdictional exposure map.
9. **Open questions and next steps:** Items requiring further regulatory clarity or direct regulator engagement.

## Common mistakes

- **Choosing a jurisdiction based on marketing considerations rather than regulatory fit.** "Launching in Dubai because it's crypto-friendly" without assessing whether VARA or CBUAE (or both) licensing is needed for the specific product.
- **Treating algorithmic stablecoins as equivalent to fiat-backed.** They face an entirely different (and in most jurisdictions, prohibited or severely restricted) regulatory treatment post-MiCA.
- **Underestimating operational requirements for reserve management.** 100% reserve backing, daily reconciliation, quarterly audit, and custodian requirements require significant operational infrastructure.
- **Missing CBUAE requirements for AED-pegged tokens.** Many UAE-based projects assume VARA is the only regulator; CBUAE's Payment Token Services framework is mandatory for AED-pegged or UAE-payment-focused stablecoins.

## Related skills

- [[prompt-pack-regulatory-change-impact-assessment]]
- [[prompt-pack-regulatory-filing-checklist]]
- [[prompt-pack-privacy-policy]]
- [[heuristic-always-state-jurisdiction-first]]
