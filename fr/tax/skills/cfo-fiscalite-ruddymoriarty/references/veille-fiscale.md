# Veille fiscale

Surveillance continue des évolutions fiscales françaises et internationales.

## Sources officielles

### France

- **Légifrance** (https://www.legifrance.gouv.fr), textes législatifs et réglementaires
- **BoFip** (https://bofip.impots.gouv.fr), doctrine administrative
- **impots.gouv.fr**, communication DGFiP
- **ANC** (https://www.anc.gouv.fr), normes comptables françaises (qui peuvent impacter le fiscal)
- **AMF** (https://www.amf-france.org), sociétés cotées

### International

- **OCDE** (https://www.oecd.org), Pillar 2 (taxation minimale globale 15%), BEPS
- **Commission européenne**, directives fiscales UE
- **IASB** (https://www.iasb.org), IFRS (qui impactent le fiscal des groupes cotés)

## Cadence de veille

### Annuelle (obligatoire)

- **Loi de finance initiale** : publiée en Journal Officiel fin décembre, applicable au 1er janvier
- **Actualisation taux** : plafond SS, taux CSG, seuils TVA, barèmes IRPP
- **Évolutions CGI** : incorporations législatives

### Trimestrielle (recommandée)

- **Loi de finance rectificative** : possible en cours d'année (PLFR)
- **Lois de financement de la Sécurité sociale** (LFSS)
- **Publications BoFip** : instructions fiscales publiées en continu
- **Jurisprudence** : décisions du Conseil d'État, Cour de Cassation

### Mensuelle

- **Publications ANC** : règlements et recommandations comptables
- **BEPS / OCDE** : évolutions internationales

### Hebdomadaire

- Flux RSS Légifrance, BoFip
- Newsletters spécialisées (EFL, Lamy, Bulletin Fiscal Francis Lefebvre, Editions Législatives)

## Programmation via skill bundle

Le skill `cfo-risques-conformite` programme automatiquement une **veille hebdomadaire** (lundi 9h jittered) via `mcp__scheduled-tasks__create_scheduled_task`.

Le skill `cfo-fiscalite` programme :
- Une **veille annuelle** le 1er octobre (dépôt PLF)
- Une **veille trimestrielle** sur les CA3 (taux et seuils)

## Impacts typiques à surveiller

### Taux IS / IR

Rarement modifiés mais impact majeur. Dernière réforme majeure : baisse progressive IS 33% → 25% en 2022.

### Seuils PME / ETI

Impactent le régime TVA (franchise, simplifié, normal) et l'éligibilité au taux réduit IS.

### Crédits d'impôt

- **CIR** : taux, plafonds, dépenses éligibles évoluent régulièrement
- **CII** : extension du scope possible (services, innovation non produit)
- **Nouveaux crédits** : crédit d'impôt industrie verte (2023+), autres cleantech

### Lois "anti-abus"

- ATAD (Anti-Tax Avoidance Directive) : mise en œuvre UE, transposition FR
- DAC 6 / 7 / 8 : obligation de déclaration des montages fiscaux
- Lutte contre l'évasion fiscale : évolutions régulières

### Obligations déclaratives

- **DAS2** : honoraires / commissions > 1 200 € → obligation de déclaration
- **DAC6** : montages à risque → déclaration TRACFIN
- **CBCR** : country-by-country pour groupes > 750 M€

### Fiscalité locale

- **CFE** : évolution des taux par commune
- **CVAE** : taux et assiette évoluent
- **Taxe d'apprentissage** : évolutions régulières
- **Taxe TASCOM** : commerces > 400 m² (certains seuils)

## Méthodologie veille

### Étape 1, Sourcing

Abonnements :
- Gratuits : Légifrance (flux RSS), BoFip (newsletter)
- Payants : EFL (Editions Francis Lefebvre), Lamy Fiscal, Dictionnaire Permanent Fiscal

### Étape 2, Tri et priorisation

Filtrer selon :
- Pertinence sectorielle (société concernée)
- Matérialité financière (impact > 1% du résultat ?)
- Urgence (application immédiate vs progressive)

### Étape 3, Analyse d'impact

Pour chaque évolution retenue :
- Qualitatif : quel risque / opportunité ?
- Quantitatif : chiffrer l'impact sur le résultat / cash
- Actions : mise en œuvre nécessaire (changement process, nouvelle déclaration, mise à jour système)

### Étape 4, Communication

- Note interne au CODIR / CFO committee
- Intégration dans le prochain board pack si impact matériel
- Mise à jour des process internes (procédures comptables, formation équipe)

## Script de veille (v0.2)

À implémenter : `scripts/veille_fiscal.py` qui :
- Lit les flux RSS Légifrance + BoFip
- Filtre par mots-clés pertinents (IS, TVA, CIR, société, PME…)
- Produit une synthèse hebdomadaire automatique

Pour v0.1, la veille reste manuelle avec des rappels programmés.

## Avertissement

Ce document liste les grandes catégories d'évolutions à suivre. Il ne remplace pas **un abonnement professionnel** à une base fiscale (EFL, Lamy) et **l'assistance d'un EC / avocat fiscaliste** pour l'analyse d'impact.
