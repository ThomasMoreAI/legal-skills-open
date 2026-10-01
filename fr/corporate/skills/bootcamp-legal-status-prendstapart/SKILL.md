---
name: bootcamp-legal-status-prendstapart
title: Choix du Statut Juridique
description: Utiliser quand l'utilisateur veut choisir la forme juridique adaptée (bootcamp 5 jours StartupsForge — Jour 5).
author: PrendsTaPart
author_url: https://github.com/PrendsTaPart/Plugin-Claude-MCP-BraindCode-/tree/main/rapido-forge/skills/bootcamp-legal-status
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: fr
practice: corporate
language: fr
tags: [juridique]
---

# Choix du Statut Juridique

**Bootcamp 5 jours — Jour 5**  
**Catégorie** : Juridique  
**Framework** : Legal Structure Decision Tree  
**Durée** : 25 min

## Objectif

Choisis la forme juridique adaptée

## Étape 0 — Contexte (obligatoire)

Charger `./rapido-kb/` — surtout `./rapido-kb/startup/` (vision, persona,
offre, hypothèses construits par `dossier-startup-360` et
`interview-business-plan`). La KB PRIME : ne jamais redemander une
information déjà validée, la reformuler pour confirmation. Les chiffres
réels viennent des MCP — jamais de mémoire ; tout chiffre sans source datée
porte la mention « hypothèse fondateur, confiance faible ».

## Étapes

1. **Lister les critères qui comptent** — associés, levée prévue, protection du patrimoine, régime social du dirigeant, fiscalité
2. **Comparer 3 statuts pertinents** — typiquement SASU/SAS vs EURL/SARL vs micro (si test)
3. **Trancher selon la trajectoire** — levée envisagée → SAS quasi systématique ; expliquer pourquoi
4. **Chiffrer** — coûts de création, comptabilité annuelle, charges du dirigeant selon statut
5. **⚠️ Valider avec un professionnel** — ce travail prépare le RDV expert-comptable/avocat, il ne le remplace pas

## Données & serveurs MCP

- **RapidoCRM** (`rapidocrm`) — données réelles, lecture d'abord

## Livrable — toujours dans la KB du client

Écrire le livrable daté dans
`./rapido-kb/startup/forge/bootcamp/bootcamp-legal-status.md` (le dossier du client,
dans SON répertoire de travail — jamais dans le plugin). Si des chiffres
clés en sortent, proposer de mettre à jour
`./rapido-kb/startup/business-plan/hypotheses.md` (source + date).

## Voir aussi (skills plus riches du marketplace)

- `rapido-forge:ideation-legal-structure` — comparatif des statuts
