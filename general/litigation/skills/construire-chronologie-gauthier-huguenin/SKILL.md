---
name: construire-chronologie-gauthier-huguenin
title: Construire la chronologie
description: Construire une chronologie juridique sourcée à partir d'un registre de faits et de pièces, distinguer les dates certaines, alléguées, déduites ou contestées, et détecter les séquences manquantes. Utiliser pour préparer un entretien, une stratégie de recherche, une note, des écritures ou le contrôle temporel d'un dossier.
author: Gauthier-Huguenin
author_url: https://github.com/Gauthier-Huguenin/skills-avocats-fr/tree/main/skills/construire-chronologie
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: litigation
language: fr
sources:
- title: Regles Temporelles
  path: references/regles-temporelles.md
---

# Construire la chronologie

## Objectif

Produire une ligne du temps exploitable sans aplatir les incertitudes. Une chronologie n'est pas un récit : chaque événement doit conserver son statut et sa source.

Lire [references/regles-temporelles.md](references/regles-temporelles.md) avant de consolider des dates.

## Procédure

1. Reprendre les faits `F-xxx` et pièces `P-xxx`.
2. Créer un événement `E-xxx` pour chaque action, communication, échéance, émission, réception, paiement, livraison ou contestation utile.
3. Distinguer la date de l'événement de la date du document qui le rapporte.
4. Attribuer un statut temporel : `certaine`, `alleguee`, `deduite`, `intervalle` ou `contestee`.
5. Pour une date relative, conserver le texte source et calculer seulement si le point de départ est certain.
6. Relier les événements contradictoires au même sujet sans en supprimer un.
7. Identifier les intervalles sans information et les délais potentiellement pertinents, sans calculer de délai juridique non demandé ou non sourcé.
8. Produire `chronologie.md` à partir du modèle.

## Contrôles

- Chaque événement doit renvoyer à un fait et à une pièce, sauf événement explicitement `inconnu`.
- Une date déduite doit exposer son calcul.
- Une date contestée doit présenter les versions concurrentes.
- Une date de métadonnée ne doit pas remplacer une date indiquée dans le contenu sans justification.
- Ne pas ordonner arbitrairement deux événements du même jour sans heure fiable.

## Synthèse temporelle

Après le tableau, produire les séquences déterminantes, les contradictions de dates, les périodes non documentées, les échéances mentionnées dans les pièces et les questions à poser avant tout calcul juridique.
