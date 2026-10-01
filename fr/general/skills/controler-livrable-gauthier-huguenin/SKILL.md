---
name: controler-livrable-gauthier-huguenin
title: Contrôler le livrable
description: Effectuer une revue contradictoire et traçable d'un projet de courrier, note, consultation ou trame d'écritures avant validation humaine. Contrôler les faits, pièces, dates, montants, citations, sources juridiques, demandes, omissions et incertitudes. Utiliser systématiquement avant qu'un livrable assisté par IA soit remis, envoyé ou utilisé professionnellement.
author: Gauthier-Huguenin
author_url: https://github.com/Gauthier-Huguenin/skills-avocats-fr/tree/main/skills/controler-livrable
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: fr
practice: general
language: fr
sources:
- title: Grille Controle
  path: references/grille-controle.md
---

# Contrôler le livrable

## Objectif

Chercher activement ce qui peut rendre le projet faux, trompeur, incomplet, incohérent ou dangereux. Ne pas simplement relire pour améliorer le style.

Lire [references/grille-controle.md](references/grille-controle.md) et produire [assets/rapport-controle.md](assets/rapport-controle.md).

## Procédure

1. Identifier la version exacte du projet contrôlé.
2. Reprendre la table de traçabilité, les registres et la note de recherche.
3. Contrôler chaque nom, qualité, date, montant, pièce, citation et source juridique.
4. Rechercher les affirmations sans référence et les références qui ne soutiennent pas l'affirmation.
5. Comparer le projet aux faits contraires et contradictions du dossier.
6. Vérifier que les réserves utiles n'ont pas disparu pendant la rédaction.
7. Vérifier les demandes, délais, concessions, engagements et destinataires.
8. Tester une lecture adverse : relever les ambiguïtés et les points facilement contestables.
9. Classer les anomalies et produire un verdict.

## Gravité

- `bloquante` : source inventée ou inaccessible, fait déterminant non sourcé, identité ou montant incertain, contradiction masquée, demande non validée, divulgation sensible ou conclusion incompatible avec les sources.
- `majeure` : formulation trop affirmative, portée juridique exagérée, pièce manquante importante, ambiguïté susceptible de changer le sens.
- `mineure` : forme, cohérence éditoriale ou précision sans effet probable sur le fond.

## Verdict

Utiliser un seul verdict :

- `refuse` : au moins une anomalie bloquante.
- `a_corriger` : aucune anomalie bloquante, mais au moins une anomalie majeure.
- `pret_pour_validation_humaine` : aucune anomalie bloquante ou majeure connue.

Ne jamais utiliser `valide`, `conforme`, `pret_a_envoyer` ou une formulation équivalente. La décision finale appartient à l'avocat.

## Règles

- Ne pas corriger silencieusement une anomalie de fond dans le rapport.
- Proposer une correction séparée et conserver le constat.
- Ne pas confirmer une source en se fondant sur le texte du projet.
- Ne pas évaluer les chances de succès.
- Ne pas minimiser une anomalie parce que le projet parait convaincant.
