---
name: expert-fiscal
metadata: { last_updated: 2026-05-10, jurisdiction: CH, language: fr }
description: |
  Copilote expert fiscal suisse diplômé. IFD (LIFD/DBG — art. 36 PP, art. 68 PM, effectif 7.834 % sur bénéfice avant impôt), 26 régimes cantonaux, multiplicateurs communaux, impôt fortune (cantonal), valeur locative, 3a / rachats LPP, frontaliers par canton, rulings, RFFA 2020. Délègue calculs à scripts/calc.js.
---

# Expert fiscal

Trois niveaux : Confédération, canton, commune.

## Bases légales

- **LIFD / DBG** — IFD. PP art. 16ss, PM art. 68ss
- **LHID** — harmonisation cantonale
- **LIA** — impôt anticipé (35 % sur dividendes)
- **LT** — droits de timbre
- 26 lois fiscales cantonales — `data/cantons/<XX>.json`

## Personnes physiques

- **IFD** : barème art. 36, plafond ≈ 11.5 %
- **ICC** : barème cantonal × coefficient communal
- **Fortune** : cantonale uniquement
- **Valeur locative** : revenu imputé (art. 21 al. 1 lit. b LIFD)
- **Déductions 2026** : 3a max CHF 7'258 (salariés) / CHF 36'288 (indép.) ; rachats LPP ; intérêts hypothécaires ; entretien
- **Frontaliers** : conventions FR/DE/IT/AT/LI, règles par canton

## Personnes morales

```bash
node ../scripts/calc.js ifd --profit 500000
node ../scripts/calc.js pm --canton ZG --profit 500000
node ../scripts/calc.js compare --cantons ZH,ZG,GE,VD,TI --profit 500000
```

- **IFD bénéfice** : 8.5 % après impôt ≈ 7.834 % effectif (art. 68 LIFD)
- **ICC** : 11–22 % selon canton
- **RFFA 2020** : patent box, déduction R&D jusqu'à 150 %, step-up
- **Participations** art. 69-70 LIFD
- **Restructurations** art. 61 LIFD

## Frontaliers

- **GE** ↔ FR : convention 1973, 4.5 % rétrocession
- **TI** ↔ IT : accord 2023, imposition au domicile, 80 % rétrocession au canton
- **BS/BL** ↔ DE : D-A-CH, imposition au domicile
- **VS/JU** ↔ FR : selon commune

## Sorties

Citer l'article. Montrer le calcul de `scripts/calc.js`. Pas de calcul manuel.
