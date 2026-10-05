---
name: veille-antoineru
title: Veille — Réglementaire, Fiscale et Marchés
description: This skill should be used when the user invokes /veille, asks to "faire une veille", "quoi de neuf en fiscalité", "qu'est-ce qui a changé sur le PER", "résume la loi de finances", "impact de [loi/mesure] pour mes clients", "actualité AMF", "nouveautés réglementaires", "explique cette mesure fiscale", or needs any regulatory, fiscal, or market update summarized for CGP use. Always combine with cgp-persona. For live web searches, use the web-ctl plugin. For known facts within training data, answer directly.
author: AntoineRu
author_url: https://github.com/AntoineRu/CGP_plugin/tree/main/skills/veille
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: fr
practice: tax
language: fr
sources:
- title: Calendrier Fiscal
  path: references/calendrier-fiscal.md
---

# Veille — Réglementaire, Fiscale et Marchés

Ce skill gouverne la veille professionnelle du CGP : résumé de textes légaux, suivi des évolutions fiscales, actualités AMF, et implications pratiques pour les clients.

## Types de veille et processus

### Type 1 — Résumé d'un texte légal ou réglementaire
**Déclencheur :** "résume cette loi", "explique l'article X", "qu'est-ce que dit la directive MIF II sur Y"

**Processus :**
1. Lire et comprendre le texte (fourni par l'utilisateur ou trouvé via web-ctl)
2. Extraire les points essentiels pour un CGP
3. Formuler les implications pratiques concrètes

**Format de sortie :**
```
# Résumé — [Nom du texte]
**Date de publication :** [JJ/MM/AAAA]
**Source :** [AMF / Légifrance / Journal Officiel / etc.]

## Ce que dit le texte (en clair)
[Résumé en langage simple, 5-8 lignes maximum]

## Points clés pour le CGP
- [Point 1]
- [Point 2]
- [Point 3]

## Impact sur les clients
- **Clients concernés :** [Profils impactés]
- **Action recommandée :** [Ce que le CGP devrait faire / communiquer]
- **Délai :** [Date d'entrée en vigueur ou deadline]

⚠️ *Ce résumé est établi à titre informatif. Se référer au texte officiel pour toute application.*
```

---

### Type 2 — Point de situation sur un sujet fiscal
**Déclencheur :** "quoi de neuf sur le PER", "évolution du PFU", "nouveautés IFI 2024", "où en est la réforme de l'assurance-vie"

**Processus :**
1. Si la question porte sur des actualités récentes → utiliser web-ctl pour rechercher les dernières informations
2. Si la question porte sur des règles connues → répondre directement depuis les références
3. Structurer la réponse en trois niveaux : règle actuelle → évolutions récentes → perspectives

**Format de sortie :**
```
# Point fiscal — [Sujet]
*Mis à jour le : [date]*

## Règle actuelle
[État du droit en vigueur]

## Évolutions récentes
[Ce qui a changé dans les 12-24 derniers mois, avec date]

## Ce que ça change pour vos clients
[Implications concrètes : qui est concerné, quel impact chiffré si possible]

## Points de vigilance
- [Piège ou ambiguïté à connaître]

⚠️ *Vérifier sur les sources officielles pour les données les plus récentes.*
```

---

### Type 3 — Synthèse loi de finances annuelle
**Déclencheur :** "résume la loi de finances [année]", "quels changements fiscaux cette année", "nouveautés pour mes clients en [année]"

**Processus :**
1. Rechercher les mesures via web-ctl si la loi est récente
2. Filtrer uniquement les mesures pertinentes pour un CGP (patrimoine, épargne, succession, immobilier)
3. Classer par thème et par impact

**Format de sortie :**
```
# Loi de Finances [Année] — Ce qui change pour vos clients

## Épargne et placements
- [Mesure 1] : [Impact]
- [Mesure 2] : [Impact]

## Immobilier
- [Mesure] : [Impact]

## Succession et donation
- [Mesure] : [Impact]

## Fiscalité des revenus
- [Mesure] : [Impact]

## À communiquer en priorité à vos clients
1. [Message prioritaire 1 — clients concernés]
2. [Message prioritaire 2 — clients concernés]

⚠️ *Source : [Légifrance / PLF / BOFIP]. Données à date de publication.*
```

---

### Type 4 — Veille concurrentielle ou marché
**Déclencheur :** "quels fonds performent en ce moment", "tendances SCPI", "que font les concurrents sur [sujet]"

Pour ce type → utiliser systématiquement web-ctl pour les données actuelles (taux, performances, tendances).
Préciser toujours la date de la recherche et les sources consultées dans la réponse.

---

## Règles de la veille

- **Distinguer ce qui est su avec certitude** (règles fiscales stables) de **ce qui nécessite une vérification** (lois récentes, taux en cours)
- Pour toute donnée chiffrée (taux d'imposition, plafonds, performances) → toujours indiquer la date de référence
- **Ne jamais présenter comme certaine** une information sur une loi dont l'entrée en vigueur n'est pas confirmée
- Quand la recherche web est faite : citer la source et la date de consultation

## Sources de référence prioritaires (pour web-ctl)

- **Légifrance** : textes de loi officiels
- **BOFIP** (bofip.impots.gouv.fr) : doctrine fiscale de l'administration
- **AMF** (amf-france.org) : réglementation financière
- **Banque de France** : données macroéconomiques
- **ASPIM** (aspim.fr) : données SCPI et fonds immobiliers

## Ressources complémentaires

- **`references/calendrier-fiscal.md`** — Échéances fiscales et réglementaires de l'année
- **`cgp-persona/references/reglementation.md`** — Cadre réglementaire CGP de référence
