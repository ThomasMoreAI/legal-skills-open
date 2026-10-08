---
name: notaire-cantonal
metadata: { last_updated: 2026-05-10, jurisdiction: CH, language: fr }
description: |
  Copilote notariat suisse. NON unifié — trois systèmes : latin (GE, VD, VS, FR, NE, JU, TI), libre (ZH, SH, AR), mixte (autres). Actes authentiques (CC 657 immobilier, CC 712d PPE, CO 620ss SA / 772ss Sàrl), successions (CC 457–640, réforme 2023 réserve descendants 1/2), régimes matrimoniaux (CC 181–251), impôt successoral cantonal. **Identifier le canton AVANT.**
---

# Notaire cantonal

Notariat suisse **non unifié**. **Identifier le canton d'abord.**

## Trois systèmes

| Système | Cantons | Caractéristique |
|---------|---------|-----------------|
| **Latin** | GE, VD, VS, FR, NE, JU, TI | Officier public indépendant, tarif |
| **Libre** | ZH, SH, AR | Notaires privés en concurrence |
| **Mixte / étatique** | BE, SO, LU, ZG, BS, BL, AG, … | Fonctionnaires ou semi-publics |

→ `data/cantons/<XX>.json` champ `notariat`.

## Domaines

### Immobilier
- **Vente** : forme authentique (CC 657)
- **Cédules hypothécaires** (CC 842ss)
- **Servitudes** (CC 730ss)
- **PPE** : règlement, acte constitutif (CC 712d)
- **Droits de mutation** : cantonaux, 0 % (ZH, ZG) à 3.3 % (VD)

```bash
node ../scripts/calc.js mutation --canton GE --price 1200000
```

### Successions (CC 457–640)
- **Réforme 2023** : réserve descendants 1/2 (était 3/4)
- **Conjoint** : 1/2 succession, dont 1/4 réservataire
- **Pacte successoral** vs testament olographe vs testament public
- **Exécuteur testamentaire**
- **Impôt successoral** : cantonal, exonération conjoint et descendants dans la plupart des cantons (sauf VD, NE pour collatéraux)

### Régimes matrimoniaux (CC 181–251)
Participation aux acquêts (défaut) / séparation / communauté.

### Sociétés
- **SA** (CO 620ss) : capital min 100'000, libération 20 % min 50'000
- **Sàrl** (CO 772ss) : capital min 20'000, libéré intégralement
- **Augmentation/réduction**
- **Fusion/scission/transformation** (LFus)

## Sortie

Canton + système / base légale (CC/CO) / honoraires estimés / pièces requises.
