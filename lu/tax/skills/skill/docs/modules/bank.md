---
title: Banques LU
layout: default
parent: Modules
nav_order: 7
---

# Banques LU — Parseurs de relevés

Détection automatique de format et parsing des relevés bancaires des 4 grandes banques retail luxembourgeoises :

- **BCEE** (Banque et Caisse d'Épargne de l'État)
- **BIL** (Banque Internationale à Luxembourg)
- **Spuerkeess** (alias BCEE pour la marque commerciale)
- **ING Luxembourg**

Plus le format universel **CAMT.053** (XML SEPA).

## En CLI

```bash
npm run bank -- mon-releve.csv
```

Détection automatique : pas besoin de préciser la banque. Le module identifie les en-têtes et délimiteurs propres à chaque format.

18 tests dans [`scripts/test-bank-parsers.js`](https://github.com/gregherbe76/Luxembourg-Paperasse/blob/main/scripts/test-bank-parsers.js).
