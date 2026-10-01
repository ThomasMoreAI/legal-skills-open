# CIR, Crédit Impôt Recherche

Aide fiscale la plus connue en France pour les activités de R&D.

## Textes de référence

- Article **244 quater B** du CGI
- BoFip BOI-BIC-RICI-10-10
- Arrêté du 1er juillet 2009 (MAR, Ministère de la Recherche)

## Taux

- **30% des dépenses éligibles** jusqu'à 100 M€ par an
- **5%** au-delà (rare pour PME)

## Éligibilité des activités

### Activités éligibles

- **Recherche fondamentale** : travaux théoriques sans application pratique directe
- **Recherche appliquée** : recherche orientée sur un objectif pratique
- **Développement expérimental** : prototype, amélioration significative d'un produit/process existant

### Critères de nouveauté

- **Novelty** : caractère nouveau par rapport à l'état de l'art
- **Difficulté technique** : résolution de problèmes non triviaux (incertitude technique)
- **Méthode scientifique** : approche systématique

### Activités NON éligibles

- Études de marché
- Amélioration cosmétique / incrémentale sans rupture technique
- Mise en œuvre de technologies existantes
- Formation du personnel
- Recherche documentaire seule

## Dépenses éligibles

### Salaires de personnel R&D

- Salaires bruts + charges patronales des **chercheurs et techniciens** affectés à la R&D
- **Forfait frais de fonctionnement** : +43% des salaires chercheurs (équivalent à doubler le salaire)
- Pour PME : +75% depuis 2025 (à vérifier)

### Sous-traitance R&D

- Sous-traitance à des organismes **publics** (universités, CNRS, CEA…) : plafond 2× dépenses internes
- Sous-traitance **privée agréée** (liste sur impots.gouv.fr) : plafond 2× dépenses internes
- Non agréée : NON éligible

### Amortissements

Amortissements des immobilisations affectées à la R&D (laboratoires, équipements, licences logicielles).

### Frais de brevets

- Dépôt et maintenance des brevets
- Avocats en PI
- Défense contre contrefaçon

### Veille technologique

Jusqu'à 60 k€ / an (abonnements bases de données scientifiques, congrès…).

## Déclaration

Formulaire **2069-A-SD** à joindre à la liasse fiscale. Champs clés :
- Identification entreprise
- Montant total des dépenses éligibles
- Ventilation par type de dépense
- Identification des chercheurs (noms, qualifications)

## Dossier justificatif

**Non obligatoire** au dépôt mais **à constituer et conserver 6 ans** en cas de contrôle.

Structure :
1. **Présentation de l'entreprise** et de son activité R&D
2. **Projets R&D éligibles** (1 fiche par projet) :
   - Objectifs scientifiques
   - État de l'art de référence
   - Verrous techniques à lever
   - Méthodologie
   - Résultats obtenus
   - Moyens mobilisés (personnel, équipements, sous-traitance)
3. **Dépenses détaillées** (salaires avec feuilles de temps, factures sous-traitance, etc.)
4. **Justificatifs** : publications, brevets, communications

## Script `cir_estimator.py`

Estime le CIR éligible à partir d'un projet R&D :

Input : salaires chercheurs + sous-traitance + amortissements + frais brevets + veille
Output : CIR estimé + avertissements sur les points à risque

## Contrôle fiscal CIR

- Administration fiscale + Ministère de la Recherche (MESRI) pour l'éligibilité technique
- Délai de contrôle : 3 ans après dépôt (prorogé à 10 ans en cas de fraude)
- Pénalités en cas de rejet : reversement + intérêts de retard 0,4%/mois + éventuelles sanctions

## Remboursement

- **PME < 150 000 €** de CIR : remboursement **sous 4 mois** après demande (via formulaire 2573-SD)
- **Autres** : imputation sur IS N+1 à N+3, remboursement du solde après 3 ans
- **JEI** et nouvelles entreprises : remboursement anticipé possible

## Bonnes pratiques

- **Formaliser les projets R&D en début d'exercice** (pas ex post uniquement)
- **Feuilles de temps chercheurs** : indispensables pour justifier les salaires
- **Implication d'un consultant spécialisé** (cabinet CIR) pour les dossiers > 100 k€
- **Ne pas surestimer** : mieux vaut 80 k€ de CIR validé que 200 k€ contestés

## Articulation avec autres aides

- **CIR + subvention** : la subvention finançant une partie des dépenses doit être déduite des dépenses éligibles
- **CIR + CII** : pas de double comptage (dépenses R&D → CIR, innovations → CII)
- **CIR + JEI** : cumulable (exonération IS totale + CIR sur les dépenses R&D)

## Passerelle Moriarty

Un diagnostic Moriarty peut identifier les aides publiques cumulables avec le CIR (JEI, BPI, France 2030, régionales). Voir `cfo-financement-croissance` pour le CTA.
