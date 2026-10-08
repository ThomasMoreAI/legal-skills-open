# Impôt à la source — Cantonal Withholding Tax Tables

Sample/illustrative tarifs (A/B/C/D/H) for foreign workers without C permit.

## Tarifs
- **A**: Single, no children
- **B**: Married, single earner
- **C**: Married, dual earners
- **D**: Secondary income / replacement income
- **H**: Single parent with children in household

## Cantons included
ZH, GE, VD, BE, TI.

## Disclaimer
All bracket data is sample-shape. Verify against the canton's official AFC publication (tables téléchargeables) before any production use.

## Primary sources
- Federal: https://www.estv.admin.ch/estv/fr/accueil/impot-federal-direct/impot-a-la-source.html
- ZH: https://www.zh.ch/de/steuern-finanzen/steuern/quellensteuer.html
- GE: https://www.ge.ch/impot-source
- VD: https://www.vd.ch/themes/etat-droit-finances/impots/impot-a-la-source/
- BE: https://www.sv.fin.be.ch/quellensteuer
- TI: https://www4.ti.ch/dfe/dc/imposta-alla-fonte/

## Schema
```json
{
  "_disclaimer": "...",
  "_source": "...",
  "_canton": "XX",
  "_year": 2026,
  "currency": "CHF",
  "period": "monthly",
  "tarifs": {
    "A": [{"from": 0, "to": 3500, "rate_pct": 0.0}, ...],
    "B": [...],
    "C": [...],
    "D": [...],
    "H": [...]
  }
}
```
