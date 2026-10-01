---
name: ouvrir-dossier-gauthier-huguenin
title: Ouvrir un dossier
description: Cadrer l'ouverture ou la reprise d'un dossier juridique, vérifier les risques liés aux données, inventorier les entrées, clarifier l'objectif et produire un manifest de travail. Utiliser avant toute analyse de pièces nouvelles, lors d'un transfert de dossier ou quand le périmètre, les parties, l'échéance ou les documents disponibles sont incertains.
author: Gauthier-Huguenin
author_url: https://github.com/Gauthier-Huguenin/skills-avocats-fr/tree/main/skills/ouvrir-dossier
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: fr
sources:
- title: Confidentialite
  path: references/confidentialite.md
- title: Manifest
  path: references/manifest.md
---

# Ouvrir un dossier

## Objectif

Créer un point de départ explicite et sûr. Ne pas analyser le fond tant que les conditions minimales de traitement ne sont pas réunies.

Lire [references/confidentialite.md](references/confidentialite.md) pour le prévol et [references/manifest.md](references/manifest.md) pour les règles de remplissage.

## Procédure

1. Reformuler la demande en une phrase sans ajouter d'objectif.
2. Identifier le demandeur, le destinataire du travail et l'échéance uniquement s'ils sont fournis.
3. Lister les parties sous des identifiants neutres et noter les rôles comme `declare` tant qu'ils ne sont pas confirmés.
4. Effectuer le prévol de confidentialité. Si l'environnement n'est pas confirmé, suspendre l'analyse du contenu sensible et demander une version pseudonymisée ou une validation.
5. Lister chaque fichier reçu avec son nom exact, son format, sa lisibilité et son statut de traitement.
6. Détecter les archives, pièces protégées, scans illisibles, liens non accessibles et fichiers en double apparent.
7. Noter les informations et documents explicitement annoncés mais absents.
8. Produire `manifest-dossier.md` à partir de [assets/manifest-dossier.md](assets/manifest-dossier.md).

## Règles

- Ne pas ouvrir un lien externe ou transférer un fichier sans nécessité et autorisation.
- Ne pas qualifier juridiquement le dossier à ce stade.
- Ne pas inférer la qualité procédurale d'une partie à partir du nom d'un fichier.
- Ne pas recopier dans le manifest les données personnelles inutiles.
- Ne pas indiquer `environnement_valide: oui` sans confirmation explicite.
- Utiliser `inconnu` plutôt qu'une valeur probable.

## Critère de sortie

Le manifest doit permettre à un autre agent de savoir ce qui est demandé, quelles données peuvent être traitées, quelles pièces existent, ce qui manque, ce qui bloque et quelle validation humaine est attendue.

Si un blocage de confidentialité ou de lisibilité empêche le travail, produire le manifest avec le statut `bloque` et s'arrêter.
