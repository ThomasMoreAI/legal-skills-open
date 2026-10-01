---
name: ir-france-skill-optimnow
title: Déclaration d'Impôt sur le Revenu -- France
description: 'Guide complet pour la déclaration d''impôt sur le revenu en France (IR). Utilise cette skill dès qu''un utilisateur mentionne : déclaration d''impôts, impôt sur le revenu, formulaire 2042, revenus imposables en France, cases fiscales, barème IR, prélèvement à la source, crédit d''impôt, réduction d''impôt, quotient familial, BNC, BIC, revenus fonciers, plus-values, PFU, micro-entreprise, déclaration contrôlée, revenus de l''étranger, crypto fiscalité France, stock-options France, ou toute question liée au remplissage de la déclaration de revenus française. Couvre aussi les simulations de calcul d''IR et les choix d''optimisation fiscale (PFU vs barème, régime micro vs réel). Même si l''utilisateur ne dit pas explicitement "déclaration d''impôts", déclenche cette skill s''il pose des questions sur la fiscalité des revenus en France.'
author: OptimNow
author_url: https://github.com/OptimNow/ir-france-skill
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: fr
practice: tax
language: fr
sources:
- title: Bareme Et Seuils
  path: references/bareme-et-seuils.md
- title: Cas Speciaux
  path: references/cas-speciaux.md
- title: Erreurs Frequentes
  path: references/erreurs-frequentes.md
- title: Formulaires Mapping
  path: references/formulaires-mapping.md
- title: Plus Values
  path: references/plus-values.md
- title: Prelevements Sociaux
  path: references/prelevements-sociaux.md
- title: Reductions Credits
  path: references/reductions-credits.md
- title: Revenus Activite
  path: references/revenus-activite.md
- title: Revenus Capitaux
  path: references/revenus-capitaux.md
- title: Revenus Etrangers
  path: references/revenus-etrangers.md
- title: Revenus Fonciers
  path: references/revenus-fonciers.md
---

# Déclaration d'Impôt sur le Revenu -- France

## Vue d'ensemble

Cette skill guide le remplissage de la déclaration d'impôt sur le revenu (IR) en France.
Elle couvre les revenus courants et les cas spéciaux, fournit un parcours étape par étape,
et permet de simuler le montant d'IR pour aider aux choix d'optimisation.

**Année fiscale de référence** : revenus 2025, déclaration printemps 2026.
Vérifier le fichier `references/bareme-et-seuils.md` pour les mises à jour annuelles.

## Architecture de la skill

Le SKILL.md sert de routeur. Les détails fiscaux sont dans les fichiers de référence.
Charge uniquement le fichier pertinent pour la situation de l'utilisateur.

```
ir-france/
├── SKILL.md                          (ce fichier -- workflow et routage)
├── references/
│   ├── bareme-et-seuils.md           (barème IR, décote, seuils, plafonds -- MAJ annuelle)
│   ├── revenus-activite.md           (salaires, BNC, BIC, micro, déclaration contrôlée)
│   ├── revenus-capitaux.md           (dividendes, intérêts, PFU vs barème, assurance-vie)
│   ├── plus-values.md                (valeurs mobilières, immobilières, crypto-actifs)
│   ├── revenus-fonciers.md           (micro-foncier, régime réel, 2044)
│   ├── revenus-etrangers.md          (conventions fiscales, crédit d'impôt étranger, 2047)
│   ├── cas-speciaux.md               (stock-options, AGA, impatriation, carried interest)
│   ├── reductions-credits.md         (réductions, crédits d'impôt, charges déductibles)
│   ├── prelevements-sociaux.md       (CSG, CRDS, prélèvements sociaux, CSG déductible)
│   ├── formulaires-mapping.md        (correspondance revenus -> cases 2042 et annexes)
│   └── erreurs-frequentes.md         (pièges courants, points de vigilance, contrôle fiscal)
├── scripts/
│   └── simulateur-ir.py              (calcul IR : barème, décote, QF, PFU vs barème)
```

## Workflow principal

### Étape 0 : Collecter le contexte de l'utilisateur

Avant de commencer, rassembler les informations suivantes. Poser les questions une par une,
pas tout d'un bloc. Si l'utilisateur a déjà fourni des infos dans la conversation, les réutiliser.

1. **Situation familiale** : célibataire, marié/pacsé, nombre de personnes à charge (enfants, rattachements), parent isolé
2. **Sources de revenus** : lister toutes les catégories (salaires, indépendant, foncier, mobilier, étranger, etc.)
3. **Régimes fiscaux en cours** : micro-BNC/BIC ou réel, PFU ou barème, micro-foncier ou réel
4. **Changements en 2025** : mariage, divorce, naissance, déménagement, début/fin d'activité
5. **Documents disponibles** : bulletins de paie, IFU, attestations, relevés Urssaf, etc.

### Étape 1 : Checklist documentaire

Sur la base du profil, générer une checklist personnalisée des documents à rassembler.
Consulter `references/formulaires-mapping.md` pour la correspondance documents -> cases.

Format de sortie :

```
## Checklist documents -- Déclaration IR 2025

### Obligatoires
- [ ] Avis d'imposition N-1
- [ ] Bulletins de paie décembre 2025 (ou attestation annuelle)
- [ ] IFU (Imprimé Fiscal Unique) de chaque banque/courtier
...

### Selon votre situation
- [ ] Attestation Urssaf / déclaration CA micro-entrepreneur
- [ ] Relevé 2047 (revenus de source étrangère)
...
```

### Étape 2 : Parcours de remplissage guidé

Suivre l'ordre de la déclaration en ligne (impots.gouv.fr) :

1. **État civil et situation familiale** (nombre de parts)
2. **Traitements, salaires, pensions** -> lire `references/revenus-activite.md`
3. **Revenus des professions non salariées** -> lire `references/revenus-activite.md` (section BNC/BIC)
4. **Revenus de capitaux mobiliers** -> lire `references/revenus-capitaux.md`
5. **Plus-values** -> lire `references/plus-values.md`
6. **Revenus fonciers** -> lire `references/revenus-fonciers.md`
7. **Revenus de source étrangère** -> lire `references/revenus-etrangers.md`
8. **Charges déductibles et réductions/crédits** -> lire `references/reductions-credits.md`

Pour chaque étape, indiquer :
- Les cases concernées (numéro exact, ex: 1AJ, 5HQ, 2DC...)
- Ce qu'il faut reporter et d'où vient le chiffre (quel document)
- Les erreurs fréquentes (consulter `references/erreurs-frequentes.md`)
- Les choix d'optimisation possibles (PFU vs barème, micro vs réel)

### Étape 3 : Simulation du montant d'IR

Utiliser `scripts/simulateur-ir.py` pour calculer :
- L'IR brut (barème progressif + quotient familial)
- La décote si applicable
- Les réductions et crédits d'impôt
- La contribution exceptionnelle sur les hauts revenus (CEHR) si applicable
- Les prélèvements sociaux
- Le comparatif PFU vs barème (si revenus de capitaux mobiliers)

Présenter le résultat sous forme de tableau récapitulatif.

### Étape 4 : Document récapitulatif

Si l'utilisateur le demande, produire un récapitulatif au format markdown ou docx contenant :
- Le résumé de la situation fiscale
- Les montants déclarés par catégorie avec les cases correspondantes
- Le montant estimé d'IR
- Les choix d'optimisation retenus et leur impact
- Les points de vigilance spécifiques

## Règles importantes

1. **Ne jamais se substituer à un conseil fiscal professionnel.** Toujours rappeler que
   les situations complexes (contrôle fiscal, optimisation patrimoniale, montages internationaux)
   nécessitent un expert-comptable ou un avocat fiscaliste.

2. **Sourcer les informations.** Quand on cite un seuil, un taux ou une règle, indiquer
   l'article du CGI ou le BOFiP correspondant quand c'est possible.

3. **Signaler l'incertitude.** Si un point dépend de la loi de finances en cours de discussion
   ou d'une doctrine administrative non stabilisée, le dire explicitement.

4. **Année fiscale.** Toujours vérifier que les seuils et barèmes utilisés correspondent
   à l'année de revenus déclarée. Le fichier `references/bareme-et-seuils.md` est la source
   de vérité pour les chiffres.

5. **Données personnelles.** Ne jamais stocker de données fiscales personnelles dans la skill.
   Tout le contexte personnel est fourni en conversation.

## Mise à jour annuelle

Chaque année, mettre à jour :
- `references/bareme-et-seuils.md` : barème, décote, plafond QF, seuils micro, abattements
- `scripts/simulateur-ir.py` : paramètres de calcul
- Vérifier si de nouvelles cases ou annexes ont été ajoutées
- Vérifier les changements introduits par la loi de finances

Sources de référence pour la mise à jour :
- Loi de finances : legifrance.gouv.fr
- BOFiP : bofip.impots.gouv.fr
- Brochure pratique IR : impots.gouv.fr
