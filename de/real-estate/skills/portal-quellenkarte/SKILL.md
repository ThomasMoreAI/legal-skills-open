---
name: portal-quellenkarte
title: Portal Quellenkarte
description: 'Für Portal Quellenkarte: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Einreichungsplan mit Form- und Nachweischeck.'
author: Klotzkette
author_url: https://github.com/Klotzkette/claude-fuer-deutsches-recht/tree/main/zwangsverwaltung-zvg/skills/portal-quellenkarte
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: real-estate
language: de
sources:
- title: Quellenhygiene
  path: references/quellenhygiene.md
- title: Zitierweise
  path: references/zitierweise.md
---

# Portal Quellenkarte

## Zweck

Diese Quellenkarte sichert für **Zwangsverwaltung ZVG** jede tragende Aussage ab: Norm, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor Ausgabe verifiziert.

## Tragende Normen (live prüfen)

- **ZVG §§ 146 ff.** — amtlichen Stand vor tragender Aussage prüfen
- **BGB §§ 1135 ff. Pflichten** — amtlichen Stand vor tragender Aussage prüfen

## Zuständige Spruchkörper und Behörden

- Amtsgericht Vollstreckungsgericht
- Zwangsverwalter

## Amtliche und frei zugängliche Datenbanken

- gesetze-im-internet.de (Bundesrecht amtlich)
- rechtsprechung-im-internet.de
- dejure.org / openJur (frei zugängliche Rechtsprechung)
- bverwg.de
- Landes-OVG-Datenbanken
- rechtsprechung-im-internet.de

## Fristen mit Quellenrelevanz

- Beschwerde gegen Anordnung
- Rechnungslegung

## Prüfroute

1. Normtext gegen die amtliche Quelle prüfen (Fassung, Inkrafttreten, Übergangsrecht).
2. Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Fundstelle ausgeben; Senat/Spruchkörper benennen.
3. Behördenpraxis (Merkblätter, Erlasse, FAQ) mit Stand-Datum zitieren.
4. Ergebnis als Quellenmatrix: Aussage — Quelle — Stand — Tragweite — Restunsicherheit.

## Fehlerbremse

- Keine BeckRS-/juris-Blindzitate aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
- Zitierform nach `references/zitierweise.md`; Quellenhygiene nach `references/quellenhygiene.md`.
