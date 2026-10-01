---
name: quickstart-javimosch
title: Paperasse Plugin — French Bureaucracy AI Skills
description: Use this skill when the user needs help with French bureaucracy, accounting, tax, notary, audit, property management, or any French administrative paperwork.
author: javimosch
author_url: https://github.com/javimosch/supercli/tree/master/plugins/paperasse/skills/quickstart
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: fr
practice: tax
language: en
---

# Paperasse Plugin — French Bureaucracy AI Skills

Collection of 6 AI agent skills for French bureaucracy. Each skill turns your agent into an expert copilot for a specific French administrative profession.

## Installation

```bash
git clone https://github.com/romainsimon/paperasse.git
cd paperasse && npm install
cp company.example.json company.json
```

Then load skills:
```bash
sc skills get paperasse:quickstart --format skill.md
```

Also installable via [agentskill.sh](https://agentskill.sh/skillsets/paperasse).

## Tax Filing Workflow (Fiscaliste)

The **Fiscaliste** skill handles personal income tax (IR 2042), wealth tax (IFI), capital gains (PFU), crypto, rental income (LMNP), and equity compensation (RSU/BSPCE).

### Step 1 — Gather Your Documents

Before starting, collect these documents:
- **Tous les justificatifs** from 2025
- Last year's tax notice (avis d'imposition 2024 sur les revenus 2023)
- Salary slips (bulletins de salaire) and DSN summary
- Bank statements for interest, dividends, PEA movements
- Rental contracts (baux) and charges for rental properties
- Crypto transaction history (export from exchange)
- PEA/Assurance-vie statements (IFU or broker summary)
- RSU/BSPCE vesting and sale statements
- PER contribution receipts
- Loan statements (for IFI deductible debt)

### Step 2 — Tell the Agent

Use any of these prompts:

**Simple tax filing:**
> "Calculate my 2025 income tax. Salary: 55,000 EUR, célibataire, no children, no other income."

**Complex scenario:**
> "Help me fill my 2042 for 2025. I have salary (65k EUR), dividends (5k EUR from PEA), a micro-foncier rental (8k EUR), and I sold crypto for 20k EUR gain."

**RSU/equity:**
> "I had RSU vesting worth 50k EUR 2025, sold half. How do I declare?"

**LMNP:**
> "I have a furnished rental (LMNP réel) with 25k revenue and 30k charges. What do I declare?"

**IFI:**
> "Mon patrimoine immobilier net est de 1.8M EUR, suis-je redevable de l'IFI?"

### Step 3 — Follow the Calculation

The agent calculates step by step:
1. Revenu brut → RNI (after 10% abatement or frais réels)
2. RNI → Quotient familial (number of shares)
3. Quotient → Impôt brut per tranche
4. Impôt brut → Décote (if applicable)
5. Décote → Impôt net + CEHR
6. Impôt net → PAS (prélèvement à la source) reconciliation
7. Plus PFU vs barème option for capital income

### Step 4 — File

Access the online filing portal at [impots.gouv.fr](https://impots.gouv.fr), or tell the agent:
> "Génère un récapitulatif de ma déclaration 2042 pour 2025 avec toutes les cases"

## Quick Reference — Revenus 2025 (déclaration 2026)

### Barème IR (par part)
| Tranche | Taux |
|---------|------|
| 0 € à 11 600 € | 0 % |
| 11 600 € à 29 579 € | 11 % |
| 29 579 € à 84 577 € | 30 % |
| 84 577 € à 181 917 € | 41 % |
| > 181 917 € | 45 % |

### Décote
| Situation | Seuil | Formule |
|-----------|-------|---------|
| Célibataire | impôt brut < 1 982 € | 897 − 0.4525 × impôt brut |
| Couple | impôt brut < 3 277 € | 1 483 − 0.4525 × impôt brut |

### PFU vs Barème Option for 2025
| Income Type | PFU Rate | Barème Rate |
|-------------|----------|-------------|
| Dividendes | 30 % (12.8% IR + 17.2% PS) | 40% abattement + IR + 17.2% PS |
| PV mobilières (CTO) | 31.4 % (12.8% IR + 18.6% PS) | Barème IR + 18.6% PS |
| Intérêts, PEA exit | 30 % | Barème IR + 17.2% PS |
| Crypto (PAMC) | 31.4 % | n/a (PFU obligatoire) |

### IFI 2025
- **Seuil**: 1 300 000 € patrimoine net
- **Résidence principale**: abattement 30 %
- **Décote d'entrée** (1.3-1.4 M€): 17 500 − 1.25% × patrimoine net
- **Barème**: 0% (0-800k), 0.5% (800k-1.3M), 0.7% (1.3-2.57M), 1% (2.57-5M), 1.25% (5-10M), 1.5% (>10M)

## The 6 Skills

### Fiscaliste (Fiscalité Particuliers)
**Use for: income tax, IFI, PFU, PEA, assurance-vie, LMNP, RSU, BSPCE, crypto, PER.**
Personal taxation for French residents. Covers all 2042 forms, IR calculation with QF/décote/plafonnement, PFU vs barème optimisation, rental income (micro/réel, LMNP, SCI IR), equity compensation (RSU, BSPCE, stock-options, PEE/PERCO), crypto (PAMC, 2086 form), IFI, CEHR, CDHR, PER deductions, niche fiscales.

### Comptable (Expert-Comptable)
**Use for: business accounting, VAT, IS, closing, FEC, liasse fiscale, invoices.**
800+ PCG account entries, VAT declarations, IS/IR, full annual closing in 12 steps, FEC 18-column export, liasse fiscale (2033/2065), invoicing (mentions, e-invoicing 2026, Factur-X, PDP, e-reporting), bank reconciliation.

### Notaire
**Use for: real estate purchase/sale, succession, donation, SCI, PACS.**
Frais de notaire (old/new property), capital gains on real estate, successions (spouse, children), donations (monthly, manual, usufruct), SCI creation (IR/IS), diagnostics, PACS.

### Syndic de Copropriété
**Use for: AG, budget, charges, travaux, unpaid collections.**
AG convocation, budget prévisionnel, appel de fonds, votes, accounting (décret 2005), works management, supplier management, unpaid collections, syndic transition, multi-property dashboard.

### Commissaire-aux-Comptes (CAC)
**Use for: statutory audit, FEC review, certification, opinion.**
Audit in 7 NEP phases: acceptance, risk assessment, internal control testing, substantive procedures, FEC analysis, cross-validation balance/income/tax return, certification/qualification/refusal opinion.

### Contrôleur Fiscal
**Use for: DGFIP tax audit simulation, penalty estimation, compliance check.**
Audit simulation on 8 axes: accounting analysis, cash review, professional vs personal expenses, international transactions, corporate benefit, tax credits, penalty calculation with CGI legal basis.

## Helper Scripts

```bash
npm run calc        # Deterministic calculations (CCA, amortization, IS, VAT)
npm run fec         # Generate FEC 18-column export
npm run statements  # Generate balance sheet, P&L, trial balance
npm run pdfs        # Generate professional PDFs
npm run closing     # Run full closing workflow (FEC + statements + PDFs)
npm run facture     # Generate Factur-X invoice
npm run fetch       # Fetch Qonto + Stripe transactions
```

## Prompt Templates

### Personal Tax
- "Calculate my 2025 IR: salary [amount], [situation (célibataire/marié/enfants)], [other income]"
- "PFU or barème? I have [dividends/intérêts/PV] of [amount] in 2025"
- "I sold crypto in 2025 for [total] with cost basis [cost]. What do I declare?"
- "My patrimoine is [amount] with [debt]. Do I owe IFI?"
- "I have RSU/BSPCE vesting of [amount]. Explain the tax treatment"

### Business/Accounting
- "J'ai [X] transactions bancaires, catégorise-les et génère les écritures"
- "Fais la clôture annuelle de ma société pour l'exercice 2025"
- "Simule un contrôle fiscal sur mes comptes 2025"

### Notary
- "Calculate frais de notaire for a [price] EUR property in [city]"
- "Ma mère est décédée, nous sommes [X] enfants. Calcule les droits de succession"

## Integrations

- **Qonto**: Automatic bank transaction fetch
- **Stripe**: Automatic payment fetch (multi-account, Stripe Connect)
- Configure via `company.json` + API keys in `.env`

## Guardrails

- Each skill validates company info before proceeding
- Tax deadlines shown at every conversation
- Skills check data freshness (>6 months triggers online verification)
- Legal disclaimer: These skills do not replace certified professionals. For complex situations (litigation, tax audits in progress), consult a professional with RC Pro insurance
