# JSON Schemas

Schémas de validation pour tous les fichiers `*/data/*.json` du dépôt.

Chaque schéma vérifie :
- la présence des champs obligatoires (`source`, `url`, `as_of`, etc.)
- les types de données (nombre, chaîne, tableau)
- les bornes raisonnables (taux entre 0 et 100, dates au format ISO)
- les énumérations fixes (formes juridiques, classes d'impôt)

**Validation :** `npm run validate:data` (ou `node scripts/validate-schemas.js`).

Ces schémas sont une garde-fou contre les erreurs de saisie (ex : `1400` au lieu de `14.00`) lors des mises à jour annuelles.
