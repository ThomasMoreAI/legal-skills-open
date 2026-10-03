---
name: charta-quellenkarte
title: Charta Quellenkarte
description: 'Für Charta Quellenkarte: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt.'
author: Klotzkette
author_url: https://github.com/Klotzkette/claude-fuer-deutsches-recht/tree/main/europarecht-kompass/skills/charta-quellenkarte
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: eu
practice: regulatory
language: de
sources:
- title: Quellenhygiene
  path: references/quellenhygiene.md
- title: Zitierweise
  path: references/zitierweise.md
---

# Charta Quellenkarte

## Einsatzlage

Diese Quellenkarte sichert im Bereich **Europarecht Kompass** tragende Normen, Rechtsprechung, Behördenpraxis, Register, Formulare und aktuelle Leitlinien ab.

## Suchraster

- `allgemein-anschluss-router-workflow-chronologie`
- `beihilfen-drafting-europarecht`
- `er-vorlageverfahren-eur-kommissionsverfahren-eur-mandant`
- `eur-anrufung-eur-state-beihilfen-vergaben`
- `europarecht-delegierte-durchfuehrungsakte-deutscher-denkfehler`
- `europarecht-europarecht-mandantenmemo-quality-gate`
- `europarecht-grundfreiheiten-binnenmarkt-grundrechte-charta`
- `europarecht-richtlinie-umsetzung-simulation-behoerde-verordnung`
- `gegen-grundfreiheiten-livecheck-sonderfall`
- `kommissionsverfahren-vorlageverfahren-interessen`
- `nationales-verfahren-vorlageverfahren-art-denkfehler`
- `petitionsausschuss-mandantenentscheidung-richtlinien`

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
