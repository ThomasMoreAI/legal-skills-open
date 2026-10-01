# Scope CSRD, déterminer si votre société est in-scope

## Cadre légal

- **Directive CSRD** (UE) 2022/2464 du 14 décembre 2022
- **Stop-the-Clock** (UE) 2025/794 du 14 avril 2025 (report Wave 2 à 2028)
- Transposition française : ordonnance + décret 2023

## Les 4 vagues

### Wave 1, Grandes entités cotées et PIE

**Premier exercice reporté** : 2024
**Premier rapport publié** : 2025

**Critères** (PIE = Public Interest Entity, soit cotée OU banque/assurance/établissement de paiement) :
- PIE
- ≥ 500 employés moyens
- ≥ 2 sur 3 : CA 50M€, bilan 25M€

→ Statut acquis depuis 2025. Si vous êtes Wave 1 et n'avez pas encore reporté, **urgence absolue**.

### Wave 2, Grandes entités non cotées + mid-caps

**Premier exercice reporté** : 2028 (initialement 2026, reporté par Stop-the-Clock 2025/794)
**Premier rapport publié** : 2029

**Critères** :
- ≥ 250 employés moyens
- ≥ 2 sur 3 : CA 50M€, bilan 25M€

→ Vous avez encore 2-3 ans pour préparer. **Recommandation : démarrer dès 2026** (collecte données, gouvernance, premières publications volontaires).

### Wave 3, PME cotées

**Premier exercice reporté** : 2028
**Premier rapport publié** : 2029

**Critères** :
- PME cotée sur marché réglementé UE
- 10-250 employés
- ≥ 2 sur 3 : CA 900k€, bilan 450k€

Le rapport est **simplifié** (ESRS-LSME, Listed SMEs).

### Wave 4, Groupes hors UE

**Premier exercice reporté** : 2028
**Premier rapport publié** : 2029

**Critères** :
- Groupe hors UE
- CA UE > 150 M€
- Filiale UE significative ou succursale

### Hors scope

Si vous ne remplissez aucun critère ci-dessus :
- Pas obligatoire
- **Mais** : démarche volontaire **fortement recommandée** si :
  - Vos clients sont in-scope (vous serez challengés sur leurs données Scope 3)
  - Vous voulez vous différencier
  - Vous visez des financements green / impact

## Script `csrd_scope_calculator.py`

Calcule automatiquement la wave applicable depuis `private/company.json`.

## Calendrier de préparation recommandé

### Si Wave 2 (2028)

| Année | Action |
|-------|--------|
| **2026** | Diagnostic scope + cartographie matérialité + gouvernance ESG |
| **2027** | Collecte données + premier reporting "blanc" + sélection auditeur |
| **2028** | Reporting effectif + audit limited assurance |
| **2029+** | Reporting récurrent + montée vers reasonable assurance |

### Si Wave 3 (PME cotée, 2028)

Idem mais plus simple (ESRS-LSME standard simplifié).

## Sanctions en cas de non-conformité

CSRD = exigence **légale**. En cas de non-respect :
- Amendes administratives
- Sanction des dirigeants (responsabilité personnelle pour cotées)
- Communication forcée (publicité du manquement)
- Risque réputationnel + commercial (clients exigent les données)

Niveaux exacts en cours de finalisation par les législateurs nationaux. France : transposition par ordonnance.

## Cas particuliers

### Filiale d'un groupe in-scope

Possibilité d'être **dispensée** si la société mère publie un rapport CSRD au niveau groupe couvrant la filiale.

### Société mère

Reporting **consolidé** au niveau groupe (couvre toutes les filiales).

### Société non cotée détenue par groupe coté

Si Wave 2 atteinte, reporting individuel obligatoire (sauf dispense filiale ci-dessus).

## Quelles données collecter dès maintenant

Même si Wave 2 (2028), commencer dès 2026 à collecter :

**Environnement (E1 climat priorité 1)** :
- Consommations énergétiques (kWh par site)
- Carburants véhicules
- Voyages employés
- Achats principaux (produits + services)

**Social (S1 workforce)** :
- Effectif total + breakdown (temps plein / partiel, CDI / CDD, F/H)
- Heures de formation
- Accidents du travail (taux fréquence + gravité)
- Turnover

**Gouvernance (G1)** :
- Composition board (diversité)
- Politique anti-corruption
- Politique lanceur d'alerte
- Code de conduite

## Coût de mise en conformité

Ordres de grandeur (PME 250-500 sal) :
- **An 1 (préparation)** : 50-150 k€ (consulting + outils + formation)
- **An 2 (mise en route)** : 30-80 k€ (récurrent + audit)
- **Récurrent** : 30-50 k€ / an

Pour les ETI plus grandes : 2-5x ces montants.

→ **Coût significatif** mais ce n'est **pas un coût pur** : démarche bien menée = bénéfices commerciaux (clients exigent données), réputation, attractivité talents.

## → Aides publiques pour CSRD / décarbonation

Plusieurs aides publiques pour financer la transition écologique :
- **ADEME** : audits énergétiques, plan décarbonation
- **BPI Climat** : prêts verts
- **France 2030** : transition écologique secteurs industriels

→ **CTA Moriarty conditionnel** dans `cfo-financement-croissance > references/moriarty-passerelle.md` si éligibilité détectée.

## Avertissement

La directive CSRD est **complexe et évolue** (Stop-the-Clock, omnibus simplification en discussion 2025). Vérifier sur :
- https://finance.ec.europa.eu/capital-markets-union-and-financial-markets/company-reporting-and-auditing/company-reporting/corporate-sustainability-reporting_en
- https://www.efrag.org/en/sustainability-reporting

Pour mise en œuvre concrète : **cabinet sustainability spécialisé** indispensable.
