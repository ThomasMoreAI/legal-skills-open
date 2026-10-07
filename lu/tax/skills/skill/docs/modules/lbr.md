---
title: LBR
layout: default
parent: Modules
nav_order: 5
---

# LBR — Registre de Commerce et des Sociétés

Aide aux dépôts au **Luxembourg Business Registers** (anciennement RCS). Validation des numéros RCS, checklists par type d'opération, calendrier des dépôts obligatoires, tarifs 2026.

## En CLI

```bash
npm run lbr -- valider B12345
npm run lbr -- checklist creation_sarl
npm run lbr -- calendrier 2025-12-31
npm run lbr -- tarifs
```

## Catégories RCS

| Lettre | Catégorie |
|---|---|
| B | Sociétés commerciales (SARL, SA, SCS, SCA) |
| F | Fonds d'investissement |
| G | GIE (Groupement d'intérêt économique) |
| E | Sociétés européennes |
| K | Succursales |
| X | ASBL et fondations |

## Pourquoi pas de scraping direct ?

Le portail [lbr.lu](https://www.lbr.lu) utilise des sessions JSP instables. Le module fournit à la place des **URL de recherche profonde** que l'utilisateur ouvre dans son navigateur, plus une checklist exhaustive de pièces à préparer.

25 tests dans [`scripts/test-lbr.js`](https://github.com/gregherbe76/Luxembourg-Paperasse/blob/main/scripts/test-lbr.js).
