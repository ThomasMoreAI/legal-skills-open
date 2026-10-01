---
name: preparer-entretien-client-gauthier-huguenin
title: Préparer l'entretien client
description: Préparer un entretien avec un client à partir des pièces, faits et contradictions du dossier, en hiérarchisant les questions, les documents à demander et les points sensibles sans orienter les réponses. Utiliser avant un premier rendez-vous, un entretien de suivi, une reprise de dossier ou une réunion destinée à compléter des faits manquants.
author: Gauthier-Huguenin
author_url: https://github.com/Gauthier-Huguenin/skills-avocats-fr/tree/main/skills/preparer-entretien-client
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: fr
practice: general
language: fr
sources:
- title: Questionnement
  path: references/questionnement.md
---

# Préparer l'entretien client

## Objectif

Donner à l'avocat un brief actionnable qui réduit le temps de préparation sans contaminer le récit du client.

Lire [references/questionnement.md](references/questionnement.md) pour construire les questions.

## Procédure

1. Reprendre l'objectif du rendez-vous, le registre de faits et la chronologie.
2. Identifier ce qui est établi, allégué, contesté ou inconnu.
3. Hiérarchiser les questions selon leur impact et leur urgence.
4. Commencer par des questions ouvertes, puis utiliser des questions de précision.
5. Pour chaque contradiction, préparer des questions neutres pour chaque version.
6. Lister les documents à demander avec la raison précise.
7. Identifier les sujets sensibles à traiter avec prudence.
8. Produire `brief-entretien.md` à partir du modèle.

## Interdictions

- Ne pas suggérer au client la réponse attendue.
- Ne pas présenter une hypothèse de l'agent comme un souvenir possible.
- Ne pas dévoiler inutilement la stratégie ou les éléments d'une autre partie dans la formulation des premières questions.
- Ne pas transformer une question juridique en affirmation.
- Ne pas créer une checklist interminable : limiter le premier niveau aux questions qui changent réellement l'analyse.

## Après l'entretien

Ne pas mettre à jour automatiquement un fait comme `etabli_document`. Une déclaration recueillie reste `allegue_partie` jusqu'à confirmation par une pièce ou validation explicite de sa qualification.
