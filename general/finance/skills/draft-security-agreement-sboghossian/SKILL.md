---
name: draft-security-agreement-sboghossian
title: Security Agreement
description: Use when drafting a security agreement, charge, pledge, mortgage, or any instrument that grants a secured creditor rights over specific collateral to secure an underlying obligation. Covers asset-based lending, real property mortgages, share pledges, floating charges, and Sharia-compliant security structures across DIFC, ADGM, UAE onshore, KSA, LB, UK, and EU. Flags perfection requirements per jurisdiction — missing perfection renders security subordinate in insolvency.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/draft/draft-security-agreement
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: finance
language: en
---

# Security Agreement

A security agreement creates a proprietary interest — called a security interest, charge, pledge, mortgage, or hypothec depending on the jurisdiction — that entitles a creditor to look to specific assets for satisfaction of an obligation in priority to unsecured creditors and, critically, in insolvency proceedings. Drafting without regard to perfection requirements renders the security commercially worthless when it is most needed.

## When to use this

- Secured lending transactions (bank loans, mezzanine finance, bridge lending)
- Trade-finance structures with collateral support
- Earn-out or deferred-consideration arrangements secured on shares
- Intra-group financing with asset-backed security
- Sharia-compliant structures using ijara, murabaha, or musharaka with embedded security

## Required inputs

| Input | Why it matters | Default |
|---|---|---|
| Debtor (collateral owner) | Legal entity granting the security; must have title to the collateral | Must provide |
| Secured Party (creditor) | Entity receiving the benefit of the security | Must provide |
| Collateral description | Specific or general (floating); must be identifiable | Must provide |
| Underlying obligation | What is being secured (loan amount, facility limit, guarantee) | Must provide |
| Jurisdiction | Determines perfection mechanism, enforceability rules | Must provide |
| Default conditions | Events that trigger enforcement | Cross-default with principal agreement; plus bespoke events |
| Remedies | Sale, possession, appointment of receiver, set-off | All available remedies under governing law |

## Optional inputs

- Sharia-compliance requirement (KSA, MENA Islamic banking)
- Cross-collateral scope (whether security extends to other facilities between same parties)
- Subordination agreement (multiple secured creditors, intercreditor terms)
- Insurance requirements on the collateral

## Collateral Types and Instrument Names

| Collateral | Common instrument |
|---|---|
| Real property | Mortgage (common law) / Hypothec (civil law) / Rahn (Islamic) |
| Receivables / book debts | Assignment by way of security; equitable charge |
| Inventory and goods | Floating charge / pledge over goods / gage commercial |
| Intellectual property | Security interest filed with IP registrar |
| Shares in a company | Share pledge / charge over shares; corporate consent required |
| Bank accounts / deposits | Charge over bank account; control agreement with depositary bank |
| All assets (general) | Debenture (UK) / floating charge / General Security Agreement (GSA) |
| Murabaha commodities | Constructive possession plus registration under applicable law |

## Document Structure

1. **Parties and recitals** — identify Debtor, Secured Party, and the underlying obligation (by reference to the loan or facility agreement)
2. **Granting clause** — Debtor hereby charges / pledges / grants a security interest in favor of Secured Party over the Collateral
3. **Collateral description** — specific identification (serial number, land registration reference, share certificates); for floating charges, generic description with crystallization trigger
4. **Obligations secured** — define the secured obligations precisely; include cross-default with related agreements if applicable
5. **Representations and warranties** — Debtor's title to collateral; no prior charges; no restrictions on grant; no litigation affecting collateral
6. **Affirmative covenants** — maintain, repair, and insure the collateral; notify Secured Party of any adverse claim; provide updated valuations on request
7. **Negative covenants** — no disposal of collateral; no further encumbrance; no material change without consent
8. **Events of default** — cross-default with loan agreement plus bespoke triggers (insolvency, enforcement by third party, breach of covenant)
9. **Remedies on default** — sale (public or private), taking possession, appointment of receiver/administrator, set-off, appropriation; specify that Secured Party is not required to give notice before exercising remedies unless mandatory by law
10. **Receiver / administrator appointment** — where available (common law jurisdictions); powers of receiver; Secured Party not liable for receiver's acts
11. **Release** — upon satisfaction of all secured obligations, Secured Party shall execute release and cooperate with de-registration
12. **Power of attorney** — Debtor irrevocably appoints Secured Party as attorney to execute documents required for perfection and enforcement
13. **Governing law and perfection** — designate governing law; identify applicable perfection steps and confirm they will be completed by closing

## Jurisdictional Perfection Mechanisms

| Jurisdiction | Instrument | Perfection step | Notes |
|---|---|---|---|
| DIFC | Security under DIFC Security Law 2005 + Personal Property Security Regulations 2019 (PPSR) | File financing statement with DIFC registrar | Failure to file = unperfected; subordinate in insolvency |
| ADGM | Similar PPSR regime | File with ADGM registrar | Same risk |
| UAE onshore | Federal Decree-Law 4/2020 (Movable Securities Law) | Register with UAE Movable Securities Register | Applies to movables; real property through Dubai Land Dept / relevant land registry |
| KSA | Pledges / Liens on Movable Properties Law | Unified Register of Real Rights (Nafetha) | Sharia-compliant structures may use different instruments |
| LB | Lebanese Commercial Code | Gage commercial registration with Commercial Court; notarization for real property | Formal requirements strictly enforced |
| UK | Companies Act 2006 | File at Companies House within 21 days of creation | Failure = void against liquidator and other creditors |
| EU | Member-state specific; Insolvency Regulation 2015 provides cross-border framework | Varies by member state and collateral type | EMIR / financial collateral arrangements may apply for financial instruments |

## Critical Drafting Points

### Perfection is a process, not a clause

Writing "the security interest shall be perfected" in the agreement does not perfect the security. Perfection requires registration, filing, notification, or possession (depending on collateral type and jurisdiction) as a separate physical step after signing. Build a closing checklist that maps each collateral type to its perfection step and assigns responsibility.

### Cross-collateral arrangements

Where the same collateral secures multiple facilities (or the same facility includes security from multiple debtors), an intercreditor agreement governing priority, enforcement, and sharing of proceeds is essential. Without it, each creditor may race to enforce independently.

### Insolvency carve-outs

Most jurisdictions impose a moratorium on enforcement once insolvency proceedings commence. In UAE and KSA, the insolvency laws (UAE Federal Decree-Law 9/2016 on Bankruptcy; KSA Bankruptcy Law of 2018) provide frameworks for secured creditor rights, but enforcement timelines extend significantly compared to out-of-court enforcement.

### Sharia-compliant structures

In KSA and Islamic banking contexts throughout MENA, direct interest-bearing security arrangements conflict with Sharia principles. Equivalent security is achieved through:
- **Murabaha**: cost-plus sale with deferred payment and title retained by financier
- **Ijara**: leasing structure with purchase option; lessor retains title as security
- **Kafalah**: personal guarantee as Sharia-compliant equivalent of surety
- **Rahn**: pledge of asset; physical or constructive possession transferred to creditor

The security agreement must use the appropriate instrument terminology; using conventional security language in a Sharia transaction creates invalidity risk.

### Share pledges — corporate consent

Pledging shares in a MENA company (particularly onshore UAE and KSA WLL/LLC structures) requires corporate approval, sometimes shareholder approval, and registration in the company's share register. Foreign ownership restrictions may also limit the enforceability of share pledges.

## Common Mistakes

- **No post-signing perfection plan** — agreement signed, security never registered; unperfected on day of insolvency
- **Collateral description too vague** — "all assets" in a jurisdiction that requires specific identification results in an unenforceable floating charge
- **Missing insurance obligation** — if the collateral (equipment, real property) is destroyed without insurance obligation, the security evaporates with it
- **No crystallization trigger for floating charges** — floating charges need an express trigger event (insolvency filing, enforcement event) to crystallize into a fixed charge over specific assets
- **Share pledge without articles review** — target company articles may restrict share transfers; pledge enforcement (deemed transfer) may be void if articles not complied with

## Related skills

- [[draft-loan-agreement]]
- [[draft-guarantee]]
- [[draft-debenture]]
- [[draft-share-purchase-agreement]]
- [[kb-banking-finance-mena]]
- [[draft-intercreditor-agreement]]
