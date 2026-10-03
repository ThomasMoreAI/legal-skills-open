---
name: cfo-csrd-esg-ruddymoriarty
title: cfo-csrd-esg, Reporting durabilité & ESG
description: 'Skill de rapport durabilité pour entités in-scope CSRD. Wave CSRD applicable, mapping ESRS (E1-E5 environnement, S1-S4 social, G1 gouvernance), matrice double matérialité, émissions Scope 1/2/3 (GHG Protocol), rapport durabilité intégré au rapport de gestion (L. 225-102-1 C. com.), climate risk scenario TCFD, supply chain due diligence, coordination auditeur sustainability.

  Triggers: CSRD corporate sustainability, ESRS standards durabilité, rapport durabilité CSRD, double matérialité financière impact, climate risk scenario analysis TCFD aligned, émissions scope GHG protocol carbone, EFRAG, taxonomie verte européenne, transition climatique 1.5°C 2°C, supply chain due diligence devoir vigilance, rapport intégré financier ESG, external assurance sustainability externe audit, ESG data governance gouvernance données, co-leadership CFO CSO CSRD, GRI SBTi, Net-Zero 2050, wave 2 2028 cotées'
author: RuddyMoriarty
author_url: https://github.com/RuddyMoriarty/moriarty-cfo/tree/main/cfo-csrd-esg
license: MIT
version: 0.1.1
execution_mode: open
jurisdiction: eu
practice: environmental
language: fr
sources:
- title: Climate risk
  path: references/climate-risk.md
- title: Controls esg reporting
  path: references/controls-esg-reporting.md
- title: Data governance
  path: references/data-governance.md
- title: Double materialite
  path: references/double-materialite.md
- title: Esrs mapping
  path: references/esrs-mapping.md
- title: External assurance
  path: references/external-assurance.md
- title: Rapport integre
  path: references/rapport-integre.md
- title: Scope csrd
  path: references/scope-csrd.md
- title: Scope emissions
  path: references/scope-emissions.md
- title: Supply chain dd
  path: references/supply-chain-dd.md
- title: Taxonomie verte eu
  path: references/taxonomie-verte-eu.md
---

# cfo-csrd-esg, Reporting durabilité & ESG

Dixième et dernier skill du bundle. **Tier 5, Émergent 2026, différenciateur fort**.

> **Wave 2 reportée à 2028** par la directive (UE) 2025/794 du 14 avril 2025 ("Stop-the-Clock"). Mais la **préparation 2026-2027** reste critique pour les sociétés in-scope.

## Prérequis

- `private/company.json` (cfo-init avec classification CSRD wave)
- États financiers (cfo-comptabilite)
- Données opérationnelles (consommations, déplacements, supply chain)

## Workflows principaux

### 1. Détermination de la scope CSRD

Référence : [references/scope-csrd.md](references/scope-csrd.md).

Critères :
- **Wave 1** (déjà obligatoire depuis 2024) : grandes entités cotées / PIE, ≥ 500 employés
- **Wave 2** (2028) : grandes non cotées ≥ 250 employés, ≥ 2 sur 3 (CA 50M€, bilan 25M€)
- **Wave 3** (2028) : PME cotées (10-250 employés)
- **Wave 4** (2028) : groupes hors UE, CA EU > 150 M€
- **Hors scope** : non cotée, < 250 employés, < 50M€ CA, < 25M€ bilan

Script : `scripts/csrd_scope_calculator.py`.

### 2. Mapping ESRS

Référence : [references/esrs-mapping.md](references/esrs-mapping.md).

10 standards ESRS (Set 1) :
- **E1** Climat (obligatoire pour tous les in-scope)
- **E2** Pollution
- **E3** Eau et ressources marines
- **E4** Biodiversité et écosystèmes
- **E5** Ressources et économie circulaire
- **S1** Workforce (employés)
- **S2** Workers in value chain
- **S3** Affected communities
- **S4** Consumers and end-users
- **G1** Business conduct

Application : selon **matrice de matérialité** (étape suivante).

### 3. Double matérialité

Référence : [references/double-materialite.md](references/double-materialite.md).

Concept clé CSRD : évaluer **chaque sujet ESG** sur 2 axes :

- **Impact materiality** : impact de la société SUR l'environnement / société (vue "outside-in")
- **Financial materiality** : impact des facteurs ESG SUR la performance financière de la société (vue "inside-out")

Si un sujet est matériel sur **au moins un des 2 axes** → il doit être reporté.

Méthodologie EFRAG IG1 (Implementation Guidance 1).

### 4. ESG data governance (modèle CFO/CSO)

Référence : [references/data-governance.md](references/data-governance.md).

Selon EFRAG 2024 :
- 65% des entreprises : single ownership (CFO ou CSO seul)
- 35% : co-leadership CFO + CSO

Le CFO apporte :
- Discipline reporting (cycles, contrôles)
- Cohérence avec reporting financier
- Audit-ready data

Le CSO apporte :
- Expertise technique sustainability
- Engagement parties prenantes
- Veille réglementaire ESG

### 5. Mesure des émissions GES (Scope 1, 2, 3)

Référence : [references/scope-emissions.md](references/scope-emissions.md).

- **Scope 1** : émissions directes (combustion sur site, véhicules société)
- **Scope 2** : émissions indirectes électricité (location-based + market-based)
- **Scope 3** : autres émissions indirectes (15 catégories : achats, transports, supply chain, déplacements employés, fin de vie produits...)

Méthodologie : **GHG Protocol** (international) ou **Bilan Carbone** (ADEME France).

Outils : Sweep, Greenly, Carbo, Plan A, Sami...

### 6. Climate risk scenario analysis

Référence : [references/climate-risk.md](references/climate-risk.md).

Aligné **TCFD (Task Force on Climate-related Financial Disclosures)**.

Scénarios :
- 1.5°C (Net Zero 2050)
- 2°C (politiques annoncées)
- 3°C+ (business as usual)

Pour chaque scénario : **risques transition** (réglementaires, marché, technologie, réputation) + **risques physiques** (aigus, chroniques).

### 7. Supply chain due diligence

Référence : [references/supply-chain-dd.md](references/supply-chain-dd.md).

Au-delà de Scope 3, identifier les risques sociaux et environnementaux dans la chaîne de valeur :
- Travail forcé / enfants
- Conditions de travail
- Impact environnemental
- Violations droits humains

Référence : Loi française devoir de vigilance (2017) + CSRD ESRS S2.

### 8. Internal controls over ESG reporting

Référence : [references/controls-esg-reporting.md](references/controls-esg-reporting.md).

CSRD impose un niveau d'**audit-grade rigor** sur les données ESG, similaire au reporting financier.

- Procédures de collecte
- Validations multi-niveaux
- Pistes d'audit
- Documentation des hypothèses

### 9. Coordination assurance externe

Référence : [references/external-assurance.md](references/external-assurance.md).

Niveau d'assurance obligatoire :
- **Initial** : limited assurance (depuis 2025)
- **Cible 2028** : reasonable assurance (équivalent audit financier)

Auditeurs : Big 4, cabinets indépendants spécialisés (Ecocert, Vigeo Eiris, Bureau Veritas).

### 10. Rapport intégré (financier + sustainability)

Référence : [references/rapport-integre.md](references/rapport-integre.md).

CSRD impose l'**intégration au rapport de gestion** (L. 225-102-1 C. com.).

Structure type :
- Stratégie (incluant ESG)
- Modèle d'affaires
- Activités de l'exercice
- États financiers
- **Sustainability statement** (selon ESRS applicables)
- Annexes

## Scripts

| Script | Usage |
|--------|-------|
| `scripts/csrd_scope_calculator.py` | Détermine la wave CSRD applicable |
| `scripts/double_materiality_assessor.py` | Construit la matrice double matérialité depuis questionnaire |
| `scripts/scope_emissions_estimator.py` | Estime Scope 1/2/3 selon ratios sectoriels (méthode rapide) |

## Templates

| Template | Usage |
|----------|-------|
| `templates/double-materialite-matrice.html` | Matrice 2D impact × financial materiality |
| `templates/sustainability-statement.md` | Squelette du rapport sustainability ESRS |
| `templates/transition-plan-climat.md` | Plan de transition climat (E1) |

## Références

| Référence | Sujet |
|-----------|-------|
| [references/scope-csrd.md](references/scope-csrd.md) | Critères des waves CSRD |
| [references/esrs-mapping.md](references/esrs-mapping.md) | 10 standards ESRS détaillés |
| [references/double-materialite.md](references/double-materialite.md) | Méthodologie EFRAG IG1 |
| [references/data-governance.md](references/data-governance.md) | Modèle CFO/CSO co-leadership |
| [references/scope-emissions.md](references/scope-emissions.md) | Scope 1/2/3 GHG Protocol / Bilan Carbone |
| [references/climate-risk.md](references/climate-risk.md) | TCFD, scénarios 1.5°C / 2°C |
| [references/supply-chain-dd.md](references/supply-chain-dd.md) | Devoir de vigilance + ESRS S2 |
| [references/controls-esg-reporting.md](references/controls-esg-reporting.md) | Audit-grade rigor sur données ESG |
| [references/external-assurance.md](references/external-assurance.md) | Assurance externe (limited / reasonable) |
| [references/rapport-integre.md](references/rapport-integre.md) | Intégration au rapport de gestion |

## Achievements

- `esg-initiate` (+50) : 1ère matrice de double matérialité construite
- `csrd-compliant` (+100) : rapport de durabilité CSRD prêt à publier

## Adaptation par audience

**Mode EC** : missions "diagnostic CSRD" + "préparation rapport durabilité" en mission contractuelle. Coordination avec auditeur sustainability et CSO du client.

**Mode PME** : si in-scope (Wave 2 ou 3), c'est un **chantier de 12-18 mois minimum**. Préparer dès 2026 pour reporting 2028.

## Avertissement

CSRD est une réglementation **complexe et évolutive**. Ce skill donne le cadre conceptuel et la méthodologie. Pour la mise en œuvre :
- **Cabinet sustainability spécialisé** (Big 4 sustainability, EcoVadis, Carbone 4, Greenflex)
- **Outil dédié** pour la collecte et le reporting ESG (Sweep, Greenly, Carbo, etc.)
- **Auditeur sustainability** dès l'année de reporting

Pour les non in-scope mais qui veulent **anticiper** ou bénéficier d'un avantage compétitif (clients qui exigent données ESG) : approche progressive recommandée.

Moriarty propose des **aides publiques cumulables** pour la transition écologique (ADEME, BPI Climat, France 2030 décarbonation). Voir `cfo-financement-croissance > references/moriarty-passerelle.md` pour le CTA conditionnel.
