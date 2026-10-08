---
name: kb-corporate-law-lb-sboghossian
title: Knowledge Pack — Lebanon Corporate Law
description: Use when advising on Lebanese corporate law, including SAL (joint stock company), SARL (LLC), holding company and offshore company regimes, incorporation procedure, foreign ownership restrictions, governance requirements, beneficial ownership reforms, and the impact of the ongoing financial crisis on corporate practice. Also covers capital markets under Law 84/2018, commercial registry digitalization (Law 159/2020), and dispute resolution through Lebanese commercial courts.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/kb/kb-corporate-law-lb
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: lb
practice: corporate
language: en
---

# Knowledge Pack — Lebanon Corporate Law

## Scope

This pack covers Lebanese corporate law and practice. Lebanon's legal framework is French-derived; its Code of Commerce (Decree-Law 304/1942) closely follows the French Commercial Code. The Lebanese financial crisis since 2019 has had profound practical consequences for corporate transactions and operations in Lebanon. This pack covers both the legal framework and the crisis-context practical realities.

---

## Primary legislation

| Statute | Scope |
|---|---|
| **Code of Commerce** (Decree-Law 304/1942 as amended) | Primary corporate statute: SAL, SARL, partnerships |
| **Decree-Law 45/1983** | Holding company regime |
| **Decree-Law 46/1983** | Offshore company regime |
| **Law 159/2020** | Commercial registries reform: digital + UBO |
| **Law 81/2018** | E-signature recognition |
| **Law 84/2018** | Capital markets; financial instruments |
| **Law 126/2019** | E-commerce + corporate transparency |
| **Ministerial decrees** (MOET) | Implementing regulations for corporate matters |

---

## Entity types

### SAL (Société Anonyme Libanaise) — Joint Stock Company

The Lebanese equivalent of a public joint stock company. Used for larger enterprises, banks, listed companies, and companies requiring a corporate governance framework.

**Key features:**

- **Minimum shareholders**: 3
- **Minimum capital**: LBP 30,000,000 (note: with LBP devaluation, this is a nominal amount in USD terms)
- **Management**: Board of Directors (minimum 3 directors; Lebanese citizenship not generally required but may be sector-specific)
- **Annual General Meeting**: mandatory; within 6 months of year-end
- **Audited accounts**: mandatory for larger entities
- Shares (actions) — freely transferable; par value set in articles
- Bearer shares: prohibited post-2019 UBO reforms

### SARL (Société à Responsabilité Limitée) — Limited Liability Company

The most common form for SMEs, subsidiaries, and private businesses.

**Key features:**

- **Minimum members**: 3 (single-member SARL permitted under recent reforms for certain purposes — verify current implementing rules)
- **Maximum members**: 20
- **Minimum capital**: LBP 5,000,000 (nominal in USD terms post-crisis)
- **Management**: gérant(s) — one or more managers; can be non-members
- "Parts sociales" (quotas) rather than shares; transfer requires consent of majority of members representing 75% of capital
- No public filing of share ownership required (unlike SAL where shareholders may be publicly registered)

### Société en Commandite (Limited Partnership)

- General partners (unlimited liability) + limited partners (liability capped at contribution)
- Used for professional partnerships (lawyers, architects) and some fund structures

### Société en Nom Collectif (General Partnership)

- All partners jointly and severally liable for partnership debts
- Rarely used for commercial activities involving significant liability risk

### Holding company (Decree-Law 45/1983)

**Distinct regime** — the Lebanese holding company is specifically designed to hold shares in other companies.

**Key features:**

- Must be an SAL
- Must hold majority of shares in at least one other company, or hold 20%+ in multiple companies
- **Tax advantages**: exempt from tax on dividends received from subsidiaries; exempt from tax on capital gains on disposal of shares; low withholding tax on distributions
- Holding activities only (no commercial activities)
- Commonly used for family wealth structuring and MENA holding structures

**Important caveat**: The holding company regime is increasingly scrutinized under international tax transparency and AML/UBO rules. OECD BEPS-aligned reforms are progressively reducing pure tax-driven holding structures.

### Offshore company (Decree-Law 46/1983)

**Purpose**: companies operating exclusively outside Lebanon.

**Key features:**

- Must not conduct any business in Lebanon
- Exempt from Lebanese corporate income tax
- Low registration fees
- Used for trading companies, investment vehicles, and IP holding where activities are entirely outside Lebanon

**Practical status**: The offshore regime is under increasing pressure from:
- FATF requirements (UBO disclosure)
- OECD BEPS anti-avoidance rules
- Law 159/2020 UBO registration requirements

---

## Foreign ownership

### General rule

Lebanon generally permits significant foreign ownership:
- Foreign shareholders may hold more than two-thirds of capital in most commercial sectors
- Nationals of any country may invest (subject to reciprocity considerations)

### Restricted sectors

| Sector | Restriction |
|---|---|
| Banking | Specific BDL licensing requirements; significant foreign ownership permitted but BDL scrutiny |
| Insurance | Lebanese majority sometimes required |
| Media and publishing | Lebanese majority required |
| Land and real estate | Decree 11614/1969: restrictions on foreign ownership of real estate; limits on area foreigners can own without Council of Ministers approval; Sinai-equivalent restrictions near Israeli border |
| Defense and security | Closed to foreign investment |

---

## Incorporation procedure

1. **Name reservation** — application to MOET; name check against existing companies
2. **Drafting of Articles of Association (statuts)** — in Arabic (French translation acceptable); must include: company name, purpose, capital, shareholder names + contributions, governance
3. **Notarization** — statuts notarized by a Lebanese notary (Katib al-3adl)
4. **Capital deposit** — minimum capital deposited in a sealed bank account; certificate obtained
5. **Commercial Registry filing** — at the Registre du Commerce of the competent jurisdiction (Beirut, Mount Lebanon, etc.)
6. **Tax registration** — Ministry of Finance; obtain tax number
7. **NSSF registration** — National Social Security Fund; for employees
8. **Bank account opening** — separate account from capital deposit; subject to AML/KYC
9. **Publication in Official Gazette** — required for SAL; optional for SARL

**Timeline**: 3–6 weeks under normal conditions; delays possible in the current crisis environment (commercial registry backlogs, bank account opening difficulties).

---

## Capital and shares

### SAL

- Share par value: typically LBP 1,000 or LBP 10,000 (nominal value reduced in real terms with LBP devaluation)
- Bearer shares: prohibited (Law 159/2020 + AML reforms)
- Registered shares: each shareholder registered; transfer by endorsement + registration

### SARL

- "Parts sociales" — quotas denominated in LBP
- Transfer requires notarial deed + majority member approval (75% by value) + registration
- No public transfer mechanism

---

## Beneficial ownership (UBO) reforms

**Law 159/2020** and related AML reforms require:

- Disclosure of ultimate beneficial owners (natural persons with 25%+ economic interest, or effective control)
- Filing with the commercial registry
- Annual update
- Penalties for non-compliance

This reform significantly reduced the practical utility of nominee shareholder arrangements and offshore structures designed for opacity.

---

## Governance requirements

### SAL governance

- **Board**: minimum 3 directors; no maximum under code; chairman (PDG or separate chair + DG)
- **Annual General Meeting (AGM)**: within 6 months of year-end; statutory agenda
- **Extraordinary General Meeting**: for capital changes, amendments, dissolution; 75% quorum
- **Statutory auditor (Commissaire aux Comptes)**: mandatory for SAL; reviews accounts; report to AGM
- Shareholder register: maintained by company; bearer shares eliminated

### SARL governance

- **Gérant(s)**: appointed and removed by member resolution
- **Annual reporting**: accounts to members; simpler than SAL AGM requirements
- Unanimous consent for certain matters if articles specify

---

## Financial crisis impact on corporate practice

The 2019+ financial crisis has affected Lebanese corporate practice in material ways:

### Banking and payment challenges

- Companies face difficulties opening bank accounts for new entities
- Existing corporate accounts subject to withdrawal and transfer restrictions (de facto capital controls via BDL circulars)
- Payment of dividends, management fees, and inter-company loans effectively restricted
- USD transfers abroad require strong justification + BDL approval

### Capital contributions in crisis

- In LBP-denominated entities, the real value of statutory minimums has collapsed with LBP devaluation
- Investors effectively must make capital contributions in USD to have meaningful capital
- Currency-matching of contributions and obligations is critical

### Due diligence in M&A

For any acquisition of a Lebanese entity:
- Verify actual banking access — are accounts operational? Are there frozen funds?
- Assess regulatory compliance under crisis-era rules
- Check for claims from depositors or counterparties against company or its bank
- Governance documentation current (AGMs held? Minutes kept?)

---

## Capital markets

**Law 84/2018** created a capital markets framework for Lebanon. In practice, Lebanon's capital market remains limited:
- BSE (Beirut Stock Exchange) — small; primarily bank stocks before crisis
- Eurobond market: Lebanese sovereign defaulted March 2020 — restructuring ongoing
- CMA (Capital Markets Authority established under Law 84/2018): limited operational capacity in crisis

---

## Disputes

- **Commercial courts**: Tribunaux de Commerce — jurisdiction over corporate and commercial matters
- **Court of Appeal (Beirut)**: for major corporate disputes
- **Court of Cassation**: final appeal on points of law
- **Arbitration**: enforced under New York Convention; commonly ICC or DIAC for Lebanon-related international transactions

---

## How to use this pack

Load this pack when the user:
- Is advising on incorporating or restructuring a Lebanese entity
- Needs to understand SAL vs SARL vs holding vs offshore company for a Lebanese structure
- Is conducting M&A due diligence on a Lebanese target
- Has questions about UBO compliance for existing Lebanese entities
- Needs to understand the practical implications of the financial crisis on corporate governance

## Caveats & currency

Lebanese corporate law is technically in force but the financial crisis creates extraordinary practical complications. Ministry of Economy and BDL circulars change frequently. Commercial registry procedures have been partially digitalized under Law 159/2020 but implementation is uneven. Always verify current procedures directly with Lebanese counsel before advising on specific formations or transactions.

## Related skills

- [[kb-banking-regulation-bdl]] — BDL banking regulation and crisis context
- [[kb-aml-fatf-mena]] — AML/CFT and UBO disclosure requirements
- [[kb-corporate-law-fr]] — French corporate law (the source of Lebanese company law)
- [[kb-corporate-law-uae]] — UAE corporate law for comparison
