---
name: aerzte-quellenkarte
title: Aerzte Quellenkarte
description: 'Für Ärzte Quellenkarte: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt.'
author: Klotzkette
author_url: https://github.com/Klotzkette/claude-fuer-deutsches-recht/tree/main/fachanwalt-medizinrecht/skills/aerzte-quellenkarte
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: personal-injury
language: de
sources:
- title: Quellenhygiene
  path: references/quellenhygiene.md
- title: Zitierweise
  path: references/zitierweise.md
---

# Aerzte Quellenkarte

## Einsatzlage

Diese Quellenkarte sichert im Bereich **Fachanwalt Medizinrecht** tragende Normen, Rechtsprechung, Behördenpraxis, Register, Formulare und aktuelle Leitlinien ab.

## Suchraster

- `aerztewerbung-innovative-therapie`
- `anaesthesie-hochrisiko-approbation-digitales-arzt-anstellung`
- `apothekenrecht-interessen-aufklaerung-beweislast`
- `atmp-chain-atmp-classification`
- `atmp-pharmakovigilanz-aufklaerungsfehler-beweisstrategie`
- `aufklaerungsfehler`
- `berufsrecht-bgb-einwilligung-sonderfall-fachanwalt`
- `beweislast-hightech-medizin`
- `cannabis-medizinisch-combined-atmp-companion-diagnostic`
- `car-t-haftung-klinik`
- `crispr-base-editing-einwilligung`
- `dokumentationsaudit-630f-einwilligungsunfaehigkeit-ablehnung`

## Prüfroute

1. Normenstand über amtliche oder frei zugängliche Primärquellen sichern.
2. Rechtsprechung nach passendem Gericht, Datum, Aktenzeichen und Entscheidungsform suchen.
3. Behördenpraxis, Formulare, Verwaltungshinweise und Register nur mit Quellenstand ausgeben.
4. Ergebnis als Quellenmatrix dokumentieren: Aussage, Quelle, Stand, Tragweite, Unsicherheit.

## Fehlerbremse

- Keine BeckRS- oder juris-Blindzitate aus Modellwissen.
- Keine Literaturfundstellen behaupten, die nicht aus Nutzerquelle oder frei prüfbarer Quelle stammen.
- Bei dynamischen Materien immer sagen, ob der Stand live geprüft wurde.
- Quellenhygiene: `references/quellenhygiene.md`; Zitierweise: `references/zitierweise.md`.
