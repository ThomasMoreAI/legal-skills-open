---
title: eCDF
layout: default
parent: Modules
nav_order: 4
---

# eCDF — Déclarations fiscales en ligne

Génère les XML eCDF (formulaires de la Centrale des Bilans / Déclarations Fiscales) pour dépôt sur le portail [ecdf.b2g.etat.lu](https://ecdf.b2g.etat.lu).

## En CLI

```bash
npm run ecdf -- examples/ecdf-input.json
```

## Voir aussi

- [`scripts/generate-ecdf.js`](https://github.com/gregherbe76/Luxembourg-Paperasse/blob/main/scripts/generate-ecdf.js)
- [`lib/ecdf/`](https://github.com/gregherbe76/Luxembourg-Paperasse/tree/main/lib/ecdf)
- 24 tests dans [`scripts/test-ecdf.js`](https://github.com/gregherbe76/Luxembourg-Paperasse/blob/main/scripts/test-ecdf.js)
