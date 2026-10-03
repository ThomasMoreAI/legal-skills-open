---
name: screenreader-quellenkarte
title: Screenreader Quellenkarte
description: 'Für Screenreader Quellenkarte: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt.'
author: Klotzkette
author_url: https://github.com/Klotzkette/claude-fuer-deutsches-recht/tree/main/barrierefreiheit-web-checker/skills/screenreader-quellenkarte
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: regulatory
language: de
sources:
- title: Quellenhygiene
  path: references/quellenhygiene.md
- title: Zitierweise
  path: references/zitierweise.md
---

# Screenreader Quellenkarte

## Zweck

Diese Quellenkarte sichert für **Barrierefreiheit Web BFSG/WCAG** jede tragende Aussage ab: Norm, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor Ausgabe verifiziert.

## Tragende Normen (live prüfen)

- **BFSG** — amtlichen Stand vor tragender Aussage prüfen
- **BFSG-Verordnung** — amtlichen Stand vor tragender Aussage prüfen
- **WCAG 2.1 AA** — amtlichen Stand vor tragender Aussage prüfen
- **EU 2019/882** — amtlichen Stand vor tragender Aussage prüfen

## Zuständige Spruchkörper und Behörden

- BFA (Bundesfachstelle Barrierefreiheit)
- Marktüberwachungsbehörden Länder

## Amtliche und frei zugängliche Datenbanken

- gesetze-im-internet.de (Bundesrecht amtlich)
- rechtsprechung-im-internet.de
- dejure.org / openJur (frei zugängliche Rechtsprechung)

## Fristen mit Quellenrelevanz

- Gilt ab 28.06.2025
- BFSG-Berichtspflichten

## Prüfroute

1. Normtext gegen die amtliche Quelle prüfen (Fassung, Inkrafttreten, Übergangsrecht).
2. Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Fundstelle ausgeben; Senat/Spruchkörper benennen.
3. Behördenpraxis (Merkblätter, Erlasse, FAQ) mit Stand-Datum zitieren.
4. Ergebnis als Quellenmatrix: Aussage — Quelle — Stand — Tragweite — Restunsicherheit.

## Fehlerbremse

- Keine BeckRS-/juris-Blindzitate aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
- Zitierform nach `references/zitierweise.md`; Quellenhygiene nach `references/quellenhygiene.md`.
