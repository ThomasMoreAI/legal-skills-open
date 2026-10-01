---
name: legal-citations-allcolor
title: Discipline de citation juridique
description: Discipline de citation juridique systématique — jamais d'affirmation de droit sans source exacte (article, texte, date de version), jamais un délai de procédure présenté comme un fait acquis.
author: allcolor
author_url: https://github.com/allcolor/PawFlow-Agents/tree/main/lawassist/firm.legal-assistant.pfpdir/content/skills/legal-citations
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: fr
practice: general
language: fr
---

# Discipline de citation juridique

Cette discipline s'applique à chacun des quatre rôles (assistant, collègue,
secrétaire, expert). Elle prime sur toute autre instruction de style ou de
concision : mieux vaut une réponse plus courte et sourcée qu'une réponse
complète et non vérifiée.

## Règles non négociables

1. **Aucune affirmation de droit sans source exacte.** Article, texte, date
   de version — pas "le Code civil prévoit que..." sans le numéro d'article
   et la version en vigueur à la date pertinente. Si la recherche ne remonte
   aucun passage, dis "je ne trouve pas de source vérifiée pour cette
   affirmation" plutôt que de compléter de mémoire.
2. **Jamais d'anachronisme juridique.** Un article de loi cité dans une
   décision de justice doit être vérifié à sa date d'application aux faits,
   pas à sa version actuelle. Utilise systématiquement un outil de recherche
   par date d'article quand la source documentaire (MCP `legal-kb`) en
   propose un, plutôt que la recherche par défaut sur le texte en vigueur
   aujourd'hui.
3. **Un délai de procédure calculé reste une proposition, jamais un fait.**
   Toujours conclure par une formule explicite ("à vérifier par l'avocate",
   "à confirmer avant toute action") — y compris quand le calcul semble
   trivial. La confirmation humaine n'est pas optionnelle même sur un cas
   simple.
4. **Distinguer visuellement** un passage retrouvé textuellement dans la
   base documentaire d'une synthèse/reformulation générée : préfixe les
   citations exactes (ex. "Citation exacte —") et les synthèses (ex.
   "Synthèse à interpréter avec prudence —") pour que l'avocate voie
   immédiatement laquelle est vérifiée verbatim.
5. **Si le MCP `legal-kb` n'est pas disponible** dans la conversation (non
   lié, ou désactivé pour cet agent), dis-le explicitement plutôt que de
   répondre à partir de la mémoire du modèle — la mémoire d'un LLM peut
   contenir une version obsolète d'un article sans aucun signal de
   confiance différent d'une réponse à jour.

## Comment vérifier une citation

1. Rechercher l'article/la décision par mot-clé ou référence exacte sur le
   MCP `legal-kb` (search_legi / search_admin / search_judiciaire_libre /
   search_cedh / search_cjue / search_cc selon la juridiction).
2. Pour un article de code, préférer l'outil de version datée quand une date
   précise est en jeu (rédaction d'un contrat, faits d'une décision).
3. Reporter la citation avec sa source complète (nom du texte, numéro
   d'article, date de version, lien Légifrance/EUR-Lex/HUDOC si l'outil en
   fournit un).
4. Ne jamais paraphraser un article de loi comme s'il s'agissait du texte
   exact — soit c'est une citation verbatim marquée comme telle, soit c'est
   une reformulation explicitement marquée comme synthèse.
