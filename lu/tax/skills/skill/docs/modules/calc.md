---
title: Calc
layout: default
parent: Modules
nav_order: 8
---

# Calc — Impôts et calculs déterministes

Module historique du projet. Couvre :

- **IRC** — Impôt sur le Revenu des Collectivités (sociétés)
- **ICC** — Impôt Commercial Communal (multiplicateur par commune)
- **IF** — Impôt sur la Fortune
- **IRPP** — Impôt sur le Revenu des Personnes Physiques (renvoi vers [RTS]({{ site.baseurl }}/modules/rts) pour le détail salaires)
- **TVA** — taux 17 / 14 / 8 / 3 / 0 %
- **Succession ligne directe** — exonération sur biens situés au Luxembourg

## En CLI

```bash
npm run calc -- icc 100000 Luxembourg
npm run calc -- irpp 60000 1
npm run calc -- bellegen-akt 600000 2 lux-ville
```

19 tests dans [`scripts/test-deterministic-calculations.js`](https://github.com/gregherbe76/Luxembourg-Paperasse/blob/main/scripts/test-deterministic-calculations.js).
