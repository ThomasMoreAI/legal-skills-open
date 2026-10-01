---
name: nis2-radar-thewatcher01
title: NIS2 Radar
description: Détermine si une entité est concernée par la directive NIS2 en croisant son code NAF, son effectif et son CA avec la table de périmètre NIS2. Utiliser quand l'utilisateur demande si une entreprise est soumise à NIS2.
author: TheWatcher01
author_url: https://github.com/TheWatcher01/skills/tree/main/.claude/skills/nis2-radar
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: eu
practice: cybersecurity
language: fr
sources:
- title: Nis2 Scope
  path: references/nis2-scope.md
---

# NIS2 Radar

## Objectif

Déterminer le **statut NIS2** d'une entité (essentielle / importante / non concernée) en croisant ses données d'entreprise avec la table de référence NIS2 stockée dans `references/nis2-scope.md`.

Ce skill est un **knowledge skill** : il ne contient pas de script, le LLM utilise directement la table de référence pour produire l'analyse.

## Déclencheurs

- `/nis2 Airbus` ou `/nis2 44306184100047`
- "cette entreprise est-elle concernée par NIS2 ?"
- "NIS2 s'applique à cette boîte ?"
- "obligations NIS2 pour [nom entreprise]"

## Données nécessaires

Récupérer via le data-pipe `sirene` :
- **Code NAF** de l'entité
- **Effectif salarié** (tranche ou nombre exact)
- **Chiffre d'affaires** (si disponible via BODACC/bilan)
- **Secteur d'activité** descriptif

## Logique de décision

1. Vérifier si le **code NAF** correspond à un secteur NIS2 (voir `references/nis2-scope.md`)
2. Si oui, croiser avec les **seuils** :
   - **Entité essentielle** : >= 250 salariés OU CA >= 50 M EUR dans un secteur hautement critique
   - **Entité importante** : >= 50 salariés OU CA >= 10 M EUR dans un secteur critique ou hautement critique
   - **Non concernée** : en dessous des seuils OU secteur hors périmètre
3. Cas spéciaux : certaines entités sont essentielles quelle que soit leur taille (fournisseurs DNS, registres de noms de domaine, prestataires de confiance qualifiés)

## Format de sortie

```json
{
  "entite": "ACME SAS",
  "siret": "44306184100047",
  "statut_nis2": "importante",
  "secteur_nis2": "Infrastructures numériques",
  "code_naf": "6311Z",
  "effectif": 120,
  "rationale": "L'entité opère dans le secteur 'Infrastructures numériques' (NAF 6311Z — Traitement de données, hébergement) avec 120 salariés, dépassant le seuil de 50 pour les entités importantes.",
  "obligations": [
    "Mise en place de mesures de gestion des risques cyber (art. 21)",
    "Notification des incidents significatifs à l'ANSSI sous 24h (art. 23)",
    "Responsabilité de la direction (art. 20)",
    "Audits de sécurité réguliers",
    "Gestion de la sécurité de la chaîne d'approvisionnement"
  ],
  "echeances": {
    "transposition_france": "Octobre 2024 (directive) — transposition nationale en cours",
    "mise_en_conformite": "18 mois après transposition nationale"
  },
  "sanctions_potentielles": {
    "entite_essentielle": "Jusqu'à 10 M EUR ou 2% du CA mondial",
    "entite_importante": "Jusqu'à 7 M EUR ou 1,4% du CA mondial"
  }
}
```

## Approche commerciale

Selon le statut, adapter le discours :

| Statut | Approche |
|--------|----------|
| **Essentielle** | "Vous êtes dans le périmètre NIS2 au niveau le plus élevé. La direction est personnellement responsable. Un audit de maturité cyber est urgent." |
| **Importante** | "Votre entreprise est concernée par NIS2. Les obligations sont significatives. Un accompagnement structuré permet d'éviter les sanctions." |
| **Non concernée** | "NIS2 ne s'applique pas directement, mais vos donneurs d'ordre concernés vous demanderont des garanties (supply chain). Un label cyber est un avantage concurrentiel." |

## Règles

- Toujours croiser le code NAF avec la table `references/nis2-scope.md` — ne pas deviner.
- Si le code NAF est ambigu, lister les secteurs possibles et demander confirmation.
- Mentionner que la transposition française est en cours et que les seuils exacts peuvent évoluer.
- Ne jamais constituer un avis juridique — recommander une consultation juridique pour les cas limites.
