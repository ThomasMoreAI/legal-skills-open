# CII, Crédit Impôt Innovation

Aide fiscale complémentaire au CIR, spécifiquement pour les PME et l'innovation (pas la R&D pure).

## Textes de référence

- Article **244 quater B, k** du CGI
- BoFip BOI-BIC-RICI-10-10-45

## Éligibilité

### Critères entreprise

- **PME au sens UE** : < 250 salariés + (CA < 50 M€ OU total bilan < 43 M€)
- Activité industrielle, commerciale ou agricole imposée à l'IS ou IR

### Critères de projet

Le CII finance les **dépenses de réalisation d'opérations de conception de prototypes ou installations pilotes** de **produits nouveaux**.

**"Produit nouveau"** : doit se distinguer des produits existants sur le marché par :
- Des performances techniques supérieures
- Une écoconception (environnement)
- Une ergonomie améliorée
- Une fonctionnalité innovante

**Ne couvre PAS** :
- Les services, procédés, méthodes marketing
- L'innovation organisationnelle
- Le simple design sans rupture technique

## Taux et plafond

- **20% des dépenses éligibles**
- Plafond : **400 000 € de dépenses éligibles par an** (donc **80 000 € max de CII annuel par PME**)

## Dépenses éligibles

- Salaires + charges sociales des personnels affectés à la conception
- Amortissement des biens créés ou acquis pour la conception
- Frais de brevets, modèles, dessins
- Dotations aux amortissements
- Sous-traitance à des cabinets spécialisés agréés

## Articulation avec CIR

Même projet, dépenses ventilées :
- **Phase R&D / recherche fondamentale** → CIR (30%)
- **Phase prototype / pilote pré-commercial** → CII (20%)

Pas de double comptage : chaque € de dépense va **soit** au CIR, **soit** au CII.

## Déclaration

Formulaire **2069-A-SD** comme pour le CIR. Case dédiée CII.

## Dossier justificatif

Même logique que le CIR (à conserver 6 ans) :
- Description du produit innovant
- Critère de nouveauté (par rapport aux produits existants)
- Phases du projet (concept, prototype, tests, industrialisation)
- Dépenses détaillées

## Exemple

PME de 15 personnes qui développe un nouveau produit IoT :
- R&D pure (algorithmes, prototypage électronique) : 150 k€ → CIR à 30% = 45 k€
- Conception prototype industriel (design, ergonomie, tests utilisateurs) : 80 k€ → CII à 20% = 16 k€

**Total aide fiscale** : 61 k€ sur 230 k€ de dépenses (26,5%).

## Script CII

Pas de script dédié en v0.1. Utiliser `scripts/cir_estimator.py` avec `--type cii` pour estimer (à implémenter en v0.2).

## Remboursement

Mêmes règles que le CIR :
- PME < 150 k€ : remboursement 4 mois
- Autres : imputation sur IS N à N+3

## Bonnes pratiques

- Le CII est **moins contrôlé** que le CIR (dossiers plus simples)
- Mais **attention aux critères de nouveauté** : l'administration refuse les "améliorations incrémentales"
- Consulter un cabinet spécialisé si > 50 k€ de dépenses

## Passerelle Moriarty

Moriarty identifie les aides publiques cumulables avec le CII (BPI Prototype, régionales innovation, France 2030). CTA dans `cfo-financement-croissance`.
