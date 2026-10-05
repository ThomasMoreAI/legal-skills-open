---
name: fr-fiscalite-particulier-builderced
title: Fiscalite Personnelle France (IR)
description: Guide French personal income tax (IR) — tax brackets, deductions, credits, micro-entrepreneur, rental income, capital gains, crypto, and family quotient.
author: BuilderCed
author_url: https://github.com/BuilderCed/agent-skills/tree/main/skills/metier-fr/fr-fiscalite-particulier
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: fr
practice: tax
language: fr
---

# Fiscalite Personnelle France (IR)

> **AVERTISSEMENT** : Ce skill fournit des orientations generales. Il ne remplace pas un conseiller fiscal. Les montants et seuils changent chaque annee — verifiez sur impots.gouv.fr.

## Quand Utiliser

- Comprendre sa declaration de revenus
- Estimer son impot sur le revenu
- Choisir entre PFU (flat tax) et bareme progressif
- Optimiser ses reductions et credits d'impot
- Declarer des revenus specifiques (freelance, location, crypto, plus-values)

## Bareme IR 2026 (Revenus 2025)

Revalorise de 0.9% (Loi de finances 2026). Applique par part de quotient familial.

| Tranche | Revenu par part | Taux marginal |
|---------|----------------|---------------|
| 1 | 0 a 11 600 EUR | 0% |
| 2 | 11 601 a 29 579 EUR | 11% |
| 3 | 29 580 a 84 577 EUR | 30% |
| 4 | 84 578 a 181 917 EUR | 41% |
| 5 | Au-dela de 181 917 EUR | 45% |

### Quotient Familial

| Situation | Nombre de parts |
|-----------|----------------|
| Celibataire | 1 |
| Couple marie/pacse | 2 |
| + 1er enfant | +0.5 |
| + 2eme enfant | +0.5 |
| + 3eme enfant et suivants | +1 chacun |
| Parent isole | +0.5 supplementaire |

Plafond avantage par demi-part : 1 791 EUR (2026).

### Calcul Simplifie

1. Revenu brut - abattements = Revenu net imposable
2. Revenu net / nombre de parts = Revenu par part
3. Appliquer le bareme progressif = Impot par part
4. Impot par part x nombre de parts = Impot brut
5. Impot brut - reductions/credits = Impot net

## Abattement Forfaitaire Salaries

- Abattement automatique de **10%** sur les salaires
- Minimum : 509 EUR
- Maximum : 14 555 EUR
- Alternative : frais reels (si superieur au forfait)

## Reductions et Credits d'Impot (les plus courants)

### Credits d'Impot (rembourses meme si non imposable)
| Credit | Montant | Conditions |
|--------|---------|-----------|
| Emploi a domicile | 50% des depenses, max 12 000 EUR/an | Menage, garde, jardinage, soutien scolaire |
| Frais de garde enfant < 6 ans | 50%, max 3 500 EUR/enfant | Creche, assistante maternelle |
| Transition energetique (MaPrimeRenov') | Variable | Travaux residence principale |
| Dons aux associations | 66% (75% pour aide aux personnes) | Max 20% du revenu imposable |

### Reductions d'Impot (non remboursees)
| Reduction | Montant | Conditions |
|-----------|---------|-----------|
| Investissement locatif (Denormandie) | 12-21% sur 6-12 ans | Logement ancien renove en zone tendue (Pinel termine fin 2024) |
| PER (Plan Epargne Retraite) | Deductible du revenu imposable | Plafond : 10% des revenus N-1 |
| Investissement PME | 25% des sommes versees | Max 50 000 EUR (100 000 couple) |

## Regimes Speciaux

### Micro-Entrepreneur / Auto-Entrepreneur

| Activite | Plafond CA | Abattement forfaitaire |
|----------|-----------|----------------------|
| Vente de marchandises | 188 700 EUR | 71% |
| Prestations BIC | 77 700 EUR | 50% |
| Prestations BNC (liberal) | 77 700 EUR | 34% |

Option : versement liberatoire (1%, 1.7% ou 2.2% du CA) si revenu fiscal < seuil.

### Revenus Fonciers (Location Nue)

| Regime | Condition | Calcul |
|--------|-----------|--------|
| Micro-foncier | Revenus < 15 000 EUR/an | Abattement 30% automatique |
| Reel | Revenus > 15 000 EUR ou choix | Charges reelles deductibles (travaux, interets, assurance) |

Location meublee (LMNP) : regime BIC, pas revenus fonciers.

### Plus-Values Mobilieres

| Option | Taux | Quand choisir |
|--------|------|--------------|
| PFU (Prelevement Forfaitaire Unique) | 30% (12.8% IR + 17.2% PS) | TMI >= 30% |
| Bareme progressif | TMI + 17.2% PS | TMI = 0% ou 11% |

### Crypto-Monnaies

PFU 30% ou bareme progressif sur les plus-values (cessions > 305 EUR/an).
Detail complet (calcul, methode PMP, staking, declaration) : voir skill `fr-fiscalite-investissement`.

### IFI (Impot sur la Fortune Immobiliere)

Seuil : patrimoine immobilier net > **1 300 000 EUR**

| Tranche | Taux |
|---------|------|
| 0 a 800 000 EUR | 0% |
| 800 001 a 1 300 000 EUR | 0.50% |
| 1 300 001 a 2 570 000 EUR | 0.70% |
| 2 570 001 a 5 000 000 EUR | 1% |
| 5 000 001 a 10 000 000 EUR | 1.25% |
| > 10 000 000 EUR | 1.50% |

## Calendrier Fiscal 2026

| Date | Echeance |
|------|----------|
| Avril 2026 | Ouverture declaration en ligne |
| Mai-Juin 2026 | Date limite selon departement |
| Juillet 2026 | Avis d'imposition |
| Septembre 2026 | Prelevement solde (si reste a payer) |
| Janvier-Decembre | Prelevement a la source mensuel |

## Outils Officiels

| Outil | URL | Usage |
|-------|-----|-------|
| Simulateur IR | simulateur-ir-ifi.impots.gouv.fr | Estimer son impot |
| BOFiP | bofip.impots.gouv.fr | Textes officiels detailles |
| Service-public.gouv.fr | service-public.gouv.fr/particuliers | Baremes, droits |
| impots.gouv.fr | impots.gouv.fr | Declaration, paiement |

## Ce Que Ce Skill Ne Fait PAS

- Ne remplace pas un conseiller fiscal ou expert-comptable
- Ne fait pas la declaration a votre place
- Ne calcule pas les cotisations sociales (URSSAF)
- Ne couvre pas l'impot sur les societes (IS)
- Ne gere pas les cas internationaux (conventions fiscales)
- Ne constitue pas un conseil en investissement
