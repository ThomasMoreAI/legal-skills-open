---
title: Frontaliers
layout: default
parent: Modules
nav_order: 3
---

# Frontaliers — Net réel des résidents FR / BE / DE travaillant au LU

Calcule le **net effectif après fiscalité du pays de résidence** pour un frontalier français, belge ou allemand qui exerce une activité salariée au Luxembourg. Réutilise le module [`rts`](rts.md) pour la part luxembourgeoise (CSSS, IRPP, dépendance), puis applique la convention fiscale bilatérale du pays de résidence.

## En CLI

```bash
paperasse frontalier --brut 5000 --pays FR --classe 1
paperasse frontalier --brut 6500 --pays BE --classe 2 --commune-be 0.08
paperasse frontalier --brut 4500 --pays DE --classe 1a --jours-hors-lu 40
```

## Conventions fiscales bilatérales appliquées

| Pays | Convention | Méthode d'élimination | Ajustement modélisé |
|---|---|---|---|
| **FR** | LU–FR du 20 mars 2018 (en vigueur 2020) | Exonération avec progressivité (taux effectif) | **0 €** — net final = net LU |
| **BE** | LU–BE 1970, avenant 5 décembre 2017 | Exonération avec réserve de progressivité | **Centimes additionnels communaux** ≈ 7,5 % de l'IPP fédéral théorique |
| **DE** | LU–DE du 23 avril 2012 (en vigueur 2014) | Freistellung mit Progressionsvorbehalt | **0 €** — net final = net LU |

Dans les trois cas, le Luxembourg conserve le droit d'imposer le salaire (article 14 ou 15 de la convention selon les versions). Le pays de résidence exonère ces revenus mais les prend en compte pour calculer le taux effectif applicable aux **autres** revenus du foyer (pension, locatif, conjoint salarié local, etc.).

### Pourquoi un ajustement uniquement pour la Belgique ?

La Belgique est le seul des trois pays à conserver un prélèvement résiduel sur les revenus exonérés : les **centimes additionnels communaux** sont calculés comme si l'impôt fédéral avait été dû sur le revenu LU exonéré. Le taux varie de 0 à 9 % selon la commune (moyenne wallonne ≈ 7,5 %, ajustable via `--commune-be`).

## Régime des « jours hors LU »

Tant que le frontalier travaille au LU, le salaire entier reste imposé au LU. Au-delà d'un seuil annuel de jours travaillés ailleurs (télétravail, déplacements professionnels dans le pays de résidence ou un État tiers), la part proportionnelle bascule dans la fiscalité locale.

| Pays | Seuil historique | Seuil actuel | Source seuil actuel |
|---|---|---|---|
| **FR** | 19 jours (avenant 2014) | **34 jours** | Avenant LU-FR du 7 novembre 2022 (applicable 2023) |
| **BE** | 24 jours (avenant 2015) | **34 jours** | Avenant LU-BE du 31 août 2021 (applicable 2022) |
| **DE** | 19 jours (convention 2012) | **34 jours** | Accord amiable LU-DE 2023 (applicable 2024) |

Le module remonte un avertissement explicite si `--jours-hors-lu` dépasse le seuil actuel. Il **ne modélise pas** le reversement proportionnel au pays de résidence — un tel calcul exige la déclaration officielle.

## Avertissements automatiques

Chaque appel renvoie une liste `avertissements` contenant au minimum :

- `Calcul indicatif. Ne remplace pas la déclaration officielle dans le pays de résidence.`
- Le rappel du seuil jours (actuel + historique) avec sa source.
- Un message spécifique au pays (taux effectif FR, additionnels BE, Progressionsvorbehalt DE).
- En cas de dépassement du seuil : un avertissement de bascule fiscale.

## Limitations documentées

- Calcul indicatif, ne remplace pas la déclaration officielle (formulaires : **2042 + 2047** côté FR, déclaration **IPP** code 1250/2250 côté BE, **Anlage N-AUS** côté DE).
- Les autres revenus du foyer (qui modifient le taux effectif via la réserve de progressivité) ne sont pas modélisés.
- L'IPP belge utilisé pour la base communale est une approximation par barème 2025 simplifié, sans abattements personnels au-delà de la quotité exemptée standard (10 570 €).
- Ne modélise pas le reversement proportionnel en cas de dépassement du seuil jours.

## Sources

- Convention LU–FR du 20 mars 2018 (Mémorial A n° 1100 du 14 décembre 2018)
- Convention LU–BE du 17 septembre 1970, avenant du 5 décembre 2017
- Convention LU–DE du 23 avril 2012
- Avenants télétravail FR 2022, BE 2021, accord amiable DE 2023
- SPF Finances — barème IPP 2025 (revenus 2025, exercice 2026)
- ACD — [impotsdirects.public.lu](https://impotsdirects.public.lu)
