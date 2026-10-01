---
name: cfo-fiscalite-ruddymoriarty
title: cfo-fiscalite, Fiscalité & optimisation
description: 'Skill de fiscalité et optimisation fiscale. IS (acomptes trimestriels, solde, optimisation, résultat fiscal), TVA (CA3/CA12, intra-UE DEB/DES), CIR, CII, transfer pricing groupes multi-juridictions, déductibilité, liasse fiscale 2065 SAS et 2033 SARL, veille lois de finance, positions fiscales sécurisées auprès de la DGFiP. Renvoie à paperasse/controleur-fiscal pour le détail liasse et barème pénalités.

  Triggers: fiscalité, impôts, IS impôt société, acompte IS, solde IS, optimisation IS avant clôture fiscale, résultat fiscal, exercice fiscal, TVA CA3 CA12 déclaration, DEB DES intra-UE, CIR estimer crédit impôt recherche exercice, CII crédit impôt innovation, transfer pricing documentation groupe multi-juridictions, optimisation fiscale déductibilité, amortissement dérogatoire, liasse fiscale 2065 SAS, liasse 2033 SARL, BoFip CGI impots.gouv, DGFIP position fiscale sécurisée ruling, veille fiscale PLF projet loi finance'
author: RuddyMoriarty
author_url: https://github.com/RuddyMoriarty/moriarty-cfo/tree/main/cfo-fiscalite
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: fr
practice: tax
language: fr
sources:
- title: Bofip Index
  path: references/bofip-index.md
- title: Cgi Articles Cles
  path: references/cgi-articles-cles.md
- title: Cii
  path: references/cii.md
- title: Cir
  path: references/cir.md
- title: Deductibilite
  path: references/deductibilite.md
- title: Is
  path: references/is.md
- title: Transfer Pricing
  path: references/transfer-pricing.md
- title: Tva
  path: references/tva.md
- title: Veille Fiscale
  path: references/veille-fiscale.md
---

# cfo-fiscalite, Fiscalité & optimisation

Septième skill. Tier 2. Couvre IS, TVA, CIR/CII, transfer pricing, optimisation, veille fiscale.

**Composabilité** : renvoyer à [`paperasse/controleur-fiscal`](https://github.com/romainsimon/paperasse) pour le détail liasse 2033/2065 et le barème des pénalités.

## Prérequis

- `private/company.json` (cfo-init)
- `private/calendar-fiscal.json` (cfo-init)
- Balance comptable + détail charges / produits (cfo-comptabilite)

## Workflows principaux

### 1. IS, déclaration, acomptes, optimisation

Référence : [references/is.md](references/is.md).

- Acomptes IS : 15/03, 15/06, 15/09, 15/12 (clôture 31/12)
- Solde IS : 15/05
- Taux : 15% PME sur les 42 500 premiers €, 25% au-delà
- Optimisations légitimes : CIR/CII, amortissements dérogatoires, report en arrière, provisions déductibles

### 2. TVA, régimes et déclarations

Référence : [references/tva.md](references/tva.md).

- Régimes : franchise / simplifié / réel normal mensuel / réel normal trimestriel
- CA3 mensuelle : 24 du mois suivant (date selon 1er digit SIREN)
- CA12 annuelle : 3-5 mois après clôture
- DEB/DES pour intra-UE : trimestriel si CA HT intra-UE > 1M€

### 3. CIR, Crédit Impôt Recherche

Référence : [references/cir.md](references/cir.md).

- Éligibilité : activités R&D définies (art. 244 quater B CGI, BoFip BOI-BIC-RICI-10-10)
- Taux : 30% des dépenses < 100 M€, 5% au-delà
- Dépenses éligibles : salaires chercheurs × 2 (frais de fonctionnement inclus), sous-traitance agréée, amortissements, frais brevets
- Déclaration : 2069-A-SD + dossier justificatif (descriptif R&D, preuves de nouveauté)
- Remboursement : PME < 150k€ en 4 mois, autres en 3 ans (imputation sur IS)

### 4. CII, Crédit Impôt Innovation

Référence : [references/cii.md](references/cii.md).

- Éligible : PME au sens UE
- Scope : prototypes et installations pilotes de **produits nouveaux** (innovation ≠ R&D pure)
- Taux : 20% des dépenses dans la limite de 400 k€/an (donc 80 k€ max de CII)
- Articulation avec CIR : pas de double comptage

### 5. Transfer pricing (groupes)

Référence : [references/transfer-pricing.md](references/transfer-pricing.md).

- Principe pleine concurrence (art. 57 CGI)
- Documentation obligatoire > 400 M€ CA consolidé (art. 223 quinquies B)
- Méthodes OCDE : CUP, RPM, Cost+, TNMM, Profit Split
- Master file + Local file + CbCR (> 750 M€)

### 6. Optimisation déductibilité

Référence : [references/deductibilite.md](references/deductibilite.md).

- Limitations intérêts (art. 212 bis CGI) : ratio EBITDA
- Frais de déplacement, cadeaux, réceptions (art. 238 A)
- Relations avec paradis fiscaux
- Dépenses somptuaires (art. 39-4)

### 7. Veille fiscale (lois de finance)

Référence : [references/veille-fiscale.md](references/veille-fiscale.md).

- Loi de finance initiale : publiée fin décembre, applicable au 1er janvier
- Loi de finance rectificative : possible en cours d'année
- Sources officielles : Légifrance, BoFip, ANC, OCDE (BEPS Pillar 2)
- Programmation veille : tâche mensuelle via `mcp__scheduled-tasks__create_scheduled_task`

## Scripts

| Script | Usage |
|--------|-------|
| `scripts/cir_estimator.py` | Estime le CIR éligible sur un projet R&D |
| `scripts/is_simulator.py` | Calcule l'IS selon régime + réintégrations |
| `scripts/tva_checker.py` | Vérifie cohérence CA3 mensuelle vs balance |

## Templates

| Template | Usage |
|----------|-------|
| `templates/cir-dossier.md` | Structure dossier justificatif CIR |
| `templates/is-reconciliation.md` | Résultat comptable → fiscal |

## Références

| Référence | Sujet |
|-----------|-------|
| [references/is.md](references/is.md) | IS : déclaration, acomptes, optimisation |
| [references/tva.md](references/tva.md) | TVA : régimes, CA3/CA12, intra-UE |
| [references/cir.md](references/cir.md) | CIR détaillé + dossier justificatif |
| [references/cii.md](references/cii.md) | CII PME innovation |
| [references/transfer-pricing.md](references/transfer-pricing.md) | Transfer pricing groupes |
| [references/deductibilite.md](references/deductibilite.md) | Optimisation déductibilité |
| [references/veille-fiscale.md](references/veille-fiscale.md) | Veille lois de finance |

## Achievements

- `tva-on-time` (+25) : 1ère TVA respectée dans les délais
- `cir-hunter` (+50) : 1ère estimation CIR éligible
- `is-optimizer` (+40) : optimisation IS avant clôture

## Adaptation par audience

**Mode EC** : vous pilotez la liasse et les optimisations chez le client. Référencer BoFip, articles CGI.

**Mode PME** : vulgariser ("CIR = 30% des dépenses R&D remboursées par l'État"). Renvoyer systématiquement à l'EC pour la mise en œuvre.

## Avertissement

La fiscalité française évolue chaque année (lois de finance). Les règles et taux cités doivent être vérifiés avant toute communication externe ou décision engageante. Consulter **impots.gouv.fr**, **BoFip**, et votre EC/avocat fiscaliste.
