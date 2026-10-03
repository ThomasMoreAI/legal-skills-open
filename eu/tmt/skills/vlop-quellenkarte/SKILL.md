---
name: vlop-quellenkarte
title: Vlop Quellenkarte
description: 'Für Vlop Quellenkarte: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt.'
author: Klotzkette
author_url: https://github.com/Klotzkette/claude-fuer-deutsches-recht/tree/main/dsa-dma-digitalregulierung/skills/vlop-quellenkarte
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: eu
practice: tmt
language: de
sources:
- title: Quellenhygiene
  path: references/quellenhygiene.md
- title: Zitierweise
  path: references/zitierweise.md
---

# Vlop Quellenkarte

## Zweck

Diese Quellenkarte sichert für **DSA/DMA Digitalregulierung** jede tragende Aussage ab: Norm, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor Ausgabe verifiziert.

## Tragende Normen (live prüfen)

- **DSA EU 2022/2065** — amtlichen Stand vor tragender Aussage prüfen
- **DMA EU 2022/1925** — amtlichen Stand vor tragender Aussage prüfen
- **P2B EU 2019/1150** — amtlichen Stand vor tragender Aussage prüfen

## Zuständige Spruchkörper und Behörden

- EU-Kommission
- BNetzA als DSC
- Koordinator Digitale Dienste

## Amtliche und frei zugängliche Datenbanken

- gesetze-im-internet.de (Bundesrecht amtlich)
- rechtsprechung-im-internet.de
- dejure.org / openJur (frei zugängliche Rechtsprechung)

## Fristen mit Quellenrelevanz

- DSA Risikoberichte jährlich
- VLOP/VLOSE-Designation
- Notice-and-Action

## Prüfroute

1. Normtext gegen die amtliche Quelle prüfen (Fassung, Inkrafttreten, Übergangsrecht).
2. Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Fundstelle ausgeben; Senat/Spruchkörper benennen.
3. Behördenpraxis (Merkblätter, Erlasse, FAQ) mit Stand-Datum zitieren.
4. Ergebnis als Quellenmatrix: Aussage — Quelle — Stand — Tragweite — Restunsicherheit.

## Fehlerbremse

- Keine BeckRS-/juris-Blindzitate aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
- Zitierform nach `references/zitierweise.md`; Quellenhygiene nach `references/quellenhygiene.md`.
