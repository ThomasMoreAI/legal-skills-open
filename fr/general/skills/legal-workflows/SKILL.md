---
name: legal-workflows
title: Workflows sur demande
description: Workflows sur demande du cabinet d'avocat qui exigent un jugement (intake de dossier, relecture de brouillon, vérification de conflit d'intérêt, préparation d'audience, assemblage de courrier) — par opposition aux flows CRON automatiques.
author: allcolor
author_url: https://github.com/allcolor/PawFlow-Agents/tree/main/lawassist/firm.legal-assistant.pfpdir/content/skills/legal-workflows
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: fr
practice: general
language: en
---

# Workflows sur demande

Ces cinq workflows ne sont pas des flows CRON (contrairement à
`deadline-watch`/`weekly-digest`) : ils demandent un jugement au moment de
l'exécution, donc ils sont déclenchés explicitement par l'avocate ou un
agent, pas planifiés. Le garde-fou commun aux cinq : jamais d'envoi ni de
décision automatique, toujours une citation de source quand le workflow
touche du contenu juridique (skill `legal-citations`), toujours une
validation humaine avant toute action irréversible.

## Nouveau dossier (intake)

1. Déclenché manuellement ou vocalement ("nouveau dossier pour M./Mme X").
2. Structurer les entités de base dans la base SQLite locale — table
   `dossiers` (client, type_affaire, statut='actif', date_ouverture) — et
   dans la Knowledge Graph pour les relations qualitatives.
3. **Vérification de conflit d'intérêt** avant ouverture définitive :
   rechercher si une partie du nouveau dossier apparaît déjà côté adverse
   dans un autre dossier du cabinet (recherche transversale table
   `dossiers`/Knowledge Graph). Présenter le résultat comme une alerte à
   vérifier par l'avocate — jamais un blocage automatique : la décision de
   conflit d'intérêt reste un jugement professionnel.
4. Si des dates de procédure sont identifiées dès l'intake, proposer la
   création des entités "délai" correspondantes dans la table `delais`
   (déclenchera le prochain passage du flow `deadline-watch`) — toujours
   présentées à valider par l'avocate avant insertion, jamais actées
   automatiquement.

## Relecture de brouillon (rôle collègue)

1. Déclenché manuellement ("relire ce brouillon").
2. Charger le brouillon et les pièces du dossier (dates, montants, noms)
   depuis la table `pieces`/le filestore de la conversation.
3. Retour structuré : liste numérotée d'incohérences détectées + suggestions
   d'angle, jamais une édition directe du fichier source.

## Préparation d'audience

À J-2/J-1 d'une audience identifiée par une entrée de la table `delais` de
type "audience" : assembler un brief consultable (pièces du dossier,
chronologie reconstruite, dernières conclusions, points en délibéré) —
toujours comme support de préparation pour l'avocate, jamais comme document
à déposer.

## Assemblage de courrier

Rédaction assistée d'un premier jet (courrier, mise en demeure, conclusion) —
toujours présenté explicitement comme brouillon à revoir, jamais comme
document final. Si le package `platform.doc-templates` est installé, utiliser
son outil `render_template` pour partir d'un template existant du cabinet
plutôt que de rédiger depuis une page blanche ; sinon rédiger directement.
Relire systématiquement la cohérence dates/montants/noms de parties entre le
brouillon produit et les pièces du dossier avant de le présenter.

## Ce que ces cinq workflows ne font jamais

- N'envoient jamais un email ou un courrier à un tiers sans clic de
  validation humaine explicite.
- Ne créent ni ne modifient un événement calendrier ou une entrée `delais`
  sans confirmation de l'avocate.
- Ne concluent jamais un conflit d'intérêt ou un calcul de délai comme un
  fait acquis — toujours une alerte/proposition à vérifier.
