---
name: rechercher-droit-gauthier-huguenin
title: Rechercher le droit applicable
description: Rechercher une question de droit français ou européen à partir de faits qualifiés, en utilisant uniquement des sources officielles ouvertes et vérifiables, puis produire une note avec textes, décisions, portée, dates et liens. Utiliser lorsqu'un dossier nécessite une recherche juridique sourcée. Ne pas utiliser sans accès web ou sans question juridique suffisamment précise.
author: Gauthier-Huguenin
author_url: https://github.com/Gauthier-Huguenin/skills-avocats-fr/tree/main/skills/rechercher-droit
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: fr
practice: general
language: fr
sources:
- title: Methode Recherche
  path: references/methode-recherche.md
- title: Sources Officielles
  path: references/sources-officielles.md
---

# Rechercher le droit applicable

## Objectif

Produire une note de recherche vérifiable, pas une réponse de mémoire. Toute proposition juridique doit renvoyer à une source effectivement ouverte.

Lire [references/sources-officielles.md](references/sources-officielles.md) avant la recherche et [references/methode-recherche.md](references/methode-recherche.md) pour construire les requêtes et qualifier les résultats.

## Condition d'arrêt absolue

Si aucune source officielle ne peut être recherchée et ouverte dans la session en cours :

1. ne répondre à aucune question de fond ;
2. ne nommer aucun article, texte, arrêt, délai ou principe de mémoire ;
3. ne fournir aucune recommandation juridique générique ;
4. produire uniquement les questions à vérifier, les requêtes proposées, les domaines officiels à consulter et la mention `recherche_non_executee` ;
5. s'arrêter.

Cette règle s'applique même si la réponse parait connue ou évidente.

## Préconditions

1. Disposer d'une question juridique précise.
2. Disposer des faits utiles avec leur statut.
3. Disposer d'un accès web permettant d'ouvrir les pages sources.

Si l'accès web manque, appliquer la condition d'arrêt absolue.

## Procédure

1. Reformuler la question sans présumer la conclusion.
2. Identifier la matière, la juridiction, la période et les concepts alternatifs.
3. Rechercher d'abord les textes applicables, puis la jurisprudence et enfin les recommandations institutionnelles utiles.
4. Ouvrir chaque résultat retenu. Ne pas citer une page de résultats.
5. Vérifier la version et la date du texte, la juridiction, la formation, la date et le numéro de la décision.
6. Distinguer le principe, les conditions, les exceptions et les points non tranchés.
7. Relier les sources aux faits `F-xxx` sans décider à la place de l'avocat.
8. Produire `note-recherche.md` à partir du modèle.

## Sources

Utiliser uniquement les domaines listés dans la référence. Une source secondaire peut fournir un terme de recherche, mais ne doit pas être citée comme autorité dans la note V1.

## Citations

Pour chaque source `S-xxx`, conserver le titre officiel, l'autorité, la date, l'identifiant, l'URL directe, la date de consultation, le passage ou article utile et la portée exacte.

Limiter les citations verbatim. Préférer une reformulation fidèle avec localisation précise.

## Arrêts

S'arrêter et demander une validation si :

- plusieurs versions d'un texte semblent applicables ;
- la source officielle est inaccessible ;
- la décision n'est disponible que par un commentaire secondaire ;
- la question dépend d'un fait contesté ;
- la portée de la décision ne correspond pas clairement au dossier.
