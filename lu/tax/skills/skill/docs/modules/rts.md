---
title: RTS
layout: default
parent: Modules
nav_order: 2
---

# RTS — Retenue à la source sur salaires

Calcule la **retenue à la source mensuelle** sur traitements et salaires luxembourgeois selon le **barème IRPP 2025** (loi du 19 décembre 2024 — adaptation à l'inflation, +2,5 indice).

## En CLI

```bash
npm run rts -- --brut 5000 --classe 1
npm run rts -- --brut 8000 --classe 2
npm run rts -- --brut 4000 --classe 1a --cim
```

## Classes d'impôt

| Classe | Pour qui | Particularité |
|---|---|---|
| **1** | Célibataire sans enfant, divorcé | Barème direct |
| **1a** | Monoparental, veuf, ou >64 ans | Abattement extra-professionnel |
| **2** | Couple marié ou pacsé (imposition collective) | Splitting (barème sur revenu/2 × 2) |

## Barème IRPP 2025

23 tranches, taux marginal de **0 %** (jusqu'à 13 230 €) à **42 %** (au-delà de 234 870 €).

## Crédits d'impôt automatiques

- **CIS** (Crédit d'Impôt Salarié) : 70 €/mois — appliqué par défaut.
- **CIM** (Crédit d'Impôt Monoparental) : 188 €/mois — option `--cim`.
- Bornes : ne peut pas rendre l'impôt négatif.

## Cotisations sociales (CSSS)

| Cotisation | Taux part salarié |
|---|---|
| Assurance maladie | 2,80 % |
| Assurance pension | 8,00 % |
| **Total CSSS** | **10,80 %** |
| Contribution dépendance | 1,40 % (sur revenu - abattement ¼ × salaire min) |

## Frontaliers

La RTS LU reste identique pour un frontalier (BE, FR, DE). Le **net effectif après fiscalité du pays de résidence** peut différer — Paperasse Lux signale cette nuance via un avertissement et orientera vers un comparateur dédié dans une version future.

## Limitations documentées

- Méthode par extrapolation annuelle (≠ formule officielle ACD avec arrondis sur fiche). Écart typique ≤ 5 €/mois.
- Classe 1a : abattement extra-professionnel forfaitaire (4 500 €/an), non personnalisé.
- Avantages en nature (voiture, logement…) à intégrer en amont dans le brut.

## Sources

- L.I.R. (Loi de l'Impôt sur le Revenu), articles 136 et suivants
- Mémorial A n° 583 du 23 décembre 2024 (loi inflation 2025)
- Circulaire L.I.R. n° 137/1 (classes d'impôt)
- ACD — [impotsdirects.public.lu](https://impotsdirects.public.lu)
