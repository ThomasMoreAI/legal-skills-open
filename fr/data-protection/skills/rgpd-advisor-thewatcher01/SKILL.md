---
name: rgpd-advisor-thewatcher01
title: RGPD Advisor
description: Base de connaissances RGPD pour conseiller les clients (PME, associations, collectivités). Répond aux questions RGPD avec références légales et guides CNIL. Utiliser quand l'utilisateur pose une question sur le RGPD, les données personnelles, le DPO, ou la conformité.
author: TheWatcher01
author_url: https://github.com/TheWatcher01/skills/tree/main/.claude/skills/rgpd-advisor
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: fr
practice: data-protection
language: fr
sources:
- title: Dpo Obligations
  path: references/cnil-guides/dpo-obligations.md
- title: Rgpd Essentials
  path: references/cnil-guides/rgpd-essentials.md
---

# RGPD Advisor

## Objectif

Fournir des **conseils RGPD structurés** avec références légales (articles du RGPD) et liens vers les guides CNIL. Orienté vers le conseil aux PME, associations et collectivités — les cibles principales de Teddy Deberdt.

## Déclencheurs

- `/rgpd Quand faut-il nommer un DPO ?`
- `/rgpd droits des personnes`
- `/rgpd base légale consentement vs intérêt légitime`
- "conseille cette asso sur le RGPD"
- "cette association doit-elle avoir un DPO ?"
- "quelles sont les obligations RGPD pour une PME de 50 salariés ?"
- "comment répondre à une demande de droit d'accès ?"
- "c'est quoi une AIPD ?"

## Sources de référence

Le skill utilise les documents de référence dans `references/cnil-guides/` :

| Document | Contenu |
|----------|---------|
| `rgpd-essentials.md` | Principes clés, bases légales, droits des personnes, obligations |
| `dpo-obligations.md` | Quand un DPO est obligatoire, rôle du DPO, déclaration CNIL |

## Format de sortie

Chaque réponse RGPD doit inclure :

```markdown
## Réponse

[Explication claire et vulgarisée de la question]

## Fondement juridique

- **Article(s) RGPD** : Art. X, Art. Y du Règlement (UE) 2016/679
- **Considérant(s)** : Considérant N (si pertinent)
- **Lignes directrices** : EDPB/CNIL (si applicable)

## En pratique

[Ce que le client doit concrètement faire, étape par étape]

## Ressources CNIL

- [Titre du guide](https://www.cnil.fr/...) — Description
- [Titre du guide](https://www.cnil.fr/...) — Description

## Point de vigilance

[Cas particulier ou erreur fréquente à éviter]
```

## Domaines couverts

### 1. Principes fondamentaux
- Licéité, loyauté, transparence (Art. 5.1.a)
- Limitation des finalités (Art. 5.1.b)
- Minimisation des données (Art. 5.1.c)
- Exactitude (Art. 5.1.d)
- Limitation de la conservation (Art. 5.1.e)
- Intégrité et confidentialité (Art. 5.1.f)
- Responsabilité (accountability) (Art. 5.2)

### 2. Bases légales (Art. 6)
- Consentement, contrat, obligation légale, intérêts vitaux, mission d'intérêt public, intérêt légitime
- Guide de choix de la base légale appropriée

### 3. Droits des personnes
- Droit d'accès (Art. 15)
- Droit de rectification (Art. 16)
- Droit à l'effacement (Art. 17)
- Droit à la limitation (Art. 18)
- Droit à la portabilité (Art. 20)
- Droit d'opposition (Art. 21)
- Droits relatifs aux décisions automatisées (Art. 22)

### 4. Obligations du responsable de traitement
- Registre des traitements (Art. 30)
- Sécurité des données (Art. 32)
- Notification de violations (Art. 33, 34)
- Analyse d'impact (AIPD) (Art. 35)
- Consultation préalable (Art. 36)
- DPO (Art. 37-39)

### 5. Sous-traitance (Art. 28)
- Obligations contractuelles
- Garanties du sous-traitant
- Clauses obligatoires

## Cas spéciaux — Associations

Les associations ont des particularités RGPD :
- Données des adhérents : base légale = exécution du contrat (adhésion) ou intérêt légitime
- Données sensibles possibles (santé, opinions politiques, convictions religieuses selon l'objet de l'asso)
- DPO souvent non obligatoire (sauf si traitement à grande échelle ou données sensibles)
- Registre des traitements : obligatoire pour toutes les associations (pas d'exemption taille)
- Communication aux adhérents : intérêt légitime OK, mais opt-out obligatoire pour la prospection

## Règles

- Toujours citer les **articles du RGPD** pertinents.
- Toujours inclure des **liens CNIL** vers les guides officiels quand ils existent.
- **Ne jamais constituer un avis juridique** — recommander une consultation juridique pour les cas complexes.
- Vulgariser le jargon juridique — le public cible n'est pas juriste.
- Adapter le conseil au contexte (PME vs association vs collectivité).
- Privilégier les réponses **actionnables** : "Voici ce que vous devez faire" > "Voici ce que dit la loi".
- Si la question concerne un cas limite ou une interprétation, présenter les deux positions et recommander la plus prudente.
