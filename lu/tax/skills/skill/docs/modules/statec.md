---
title: Indice STATEC + SSM
layout: default
parent: Modules
nav_order: 9
---

# Indice STATEC + Salaire Social Minimum

Le Luxembourg est l'un des **rares pays au monde** à pratiquer l'**échelle mobile des salaires** : dès que l'indice semestriel des prix à la consommation national (IPCN) dépasse un seuil, **tous les salaires, pensions et prestations sociales sont automatiquement majorés de +2,5 %**.

Ce module suit l'historique des tranches d'indexation déclenchées et calcule le **Salaire Social Minimum (SSM)** en vigueur à toute date donnée.

## En CLI

```bash
# SSM courant
paperasse statec ssm
paperasse statec ssm --qualifie

# SSM à une date passée ou future
paperasse statec ssm --date 2024-06-01

# SSM jeune travailleur (apprenti ou < 18 ans)
paperasse statec ssm-jeune --tranche 17-18

# Tranches d'indexation déclenchées
paperasse statec tranches
paperasse statec tranches --depuis 2022-01-01

# Indexer un salaire signé à une date passée
paperasse statec indexer --brut 5000 --depuis 2022-01-01

# Historique complet du SSM
paperasse statec historique
```

## Exemple concret

Vous avez signé un CDI à **5 000 € brut le 1er janvier 2022**. Votre employeur respecte la loi et applique l'indexation. Combien devez-vous toucher aujourd'hui ?

```bash
paperasse statec indexer --brut 5000 --depuis 2022-01-01
```

→ Réponse : **5 656 € brut** (5 tranches × +2,5 %, facteur 1,1314).

Si votre fiche de paie affiche encore 5 000 €, vous êtes en sous-paiement légal — le mécanisme est **automatique** et **non négociable**.

## SSM 2025

| Catégorie | Mensuel | Horaire (173 h) |
|---|---:|---:|
| Non qualifié | **2 703,74 €** | 15,63 € |
| Qualifié | **3 244,49 €** | 18,75 € |
| Jeune 17-18 ans (80 %) | 2 162,99 € | 12,50 € |
| Jeune 15-17 ans (75 %) | 2 027,80 € | 11,72 € |

Valeurs au **1er mai 2025** (après indexation).

## Tranches d'indexation récentes

| Date | Source officielle |
|---|---|
| 1er octobre 2021 | Mémorial A n° 754 du 23 sept 2021 |
| 1er avril 2022 | Mémorial A n° 191 du 30 mars 2022 |
| 1er août 2022 | Mémorial A n° 367 du 22 juil 2022 |
| 1er février 2023 | Mémorial A n° 22 du 23 janv 2023 |
| 1er septembre 2023 | Mémorial A n° 553 du 24 août 2023 |
| 1er mai 2025 | Mémorial A n° 178 du 22 avril 2025 |

## Ce que le module ne fait PAS

- **Prédire** la prochaine tranche : la date dépend des chiffres mensuels publiés par STATEC. Pour une estimation, voir [statec.lu](https://statistiques.public.lu).
- Recalculer la prime de fin d'année ou le 13ᵉ mois (si applicable dans votre convention collective).
- Gérer les avantages en nature (voiture, logement) qui ne sont pas indexés automatiquement.

## Sources

- **STATEC** — [statistiques.public.lu](https://statistiques.public.lu/fr/themes/economie-finances/prix.html) — IPCN base 100 = 2015.
- **ITM** — [itm.public.lu](https://itm.public.lu) — Inspection du Travail et des Mines, valeurs SSM officielles.
- **Loi modifiée du 25 mars 2015** sur les salaires.
- **Loi du 19 décembre 2024** — revalorisation SSM 2025.
