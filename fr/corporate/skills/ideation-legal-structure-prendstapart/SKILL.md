---
name: ideation-legal-structure-prendstapart
title: Legal Structure
description: Utiliser quand l'utilisateur veut choisir le statut juridique adapté à son projet (parcours idéation StartupsForge).
author: PrendsTaPart
author_url: https://github.com/PrendsTaPart/Plugin-Claude-MCP-BraindCode-/tree/main/rapido-forge/skills/ideation-legal-structure
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: fr
practice: corporate
language: fr
tags: [juridique]
---

# Legal Structure

**Catégorie** : Idéation  
**Durée** : 30-45 min

## Pourquoi

Le choix du statut juridique impacte ta fiscalité, ta responsabilité et ta capacité à lever des fonds. Un mauvais choix coûte cher à corriger.

## Objectif

Choisir le statut juridique adapté à ton projet.

## Livrable attendu

Recommandation statut + tableau comparatif

## Étape 0 — Contexte (obligatoire)

Charger `./rapido-kb/` — surtout `./rapido-kb/startup/` (vision, persona,
offre, hypothèses construits par `dossier-startup-360` et
`interview-business-plan`). La KB PRIME : ne jamais redemander une
information déjà validée, la reformuler pour confirmation. Les chiffres
réels viennent des MCP — jamais de mémoire ; tout chiffre sans source datée
porte la mention « hypothèse fondateur, confiance faible ».

## Étapes

1. **Évaluer tes besoins** — Associés ? Levée de fonds ? Patrimoine ?
   > Prompt: Compare SAS, SARL, et auto-entrepreneur pour [ACTIVITÉ] avec [X] associés et [MONTANT]€ de CA prévu.
2. **Comparer les options** — SAS, SARL, EURL, auto-entrepreneur
3. **Analyser la fiscalité** — IR vs IS, charges sociales
4. **Considérer l'évolution** — Comment transformer si besoin
5. **Valider avec un expert** — Expert-comptable ou avocat

## Pro tips

- La SAS est le standard pour lever des fonds
- L'auto-entrepreneur pour tester sans risque
- Consulte toujours un expert avant de te lancer

## Erreurs fréquentes

- Choisir auto-entrepreneur quand on veut lever
- Ignorer les implications sociales
- Ne pas anticiper les besoins futurs

## Données & serveurs MCP

- **RapidoCRM** (`rapidocrm`) — données réelles, lecture d'abord

## Livrable — toujours dans la KB du client

Écrire le livrable daté dans
`./rapido-kb/startup/forge/ideation/ideation-legal-structure.md` (le dossier du client,
dans SON répertoire de travail — jamais dans le plugin). Si des chiffres
clés en sortent, proposer de mettre à jour
`./rapido-kb/startup/business-plan/hypotheses.md` (source + date).
