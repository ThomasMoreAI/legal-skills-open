---
name: nachfrage-quellenkarte
title: Nachfrage Quellenkarte
description: 'Für Nachfrage Quellenkarte: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt.'
author: Klotzkette
author_url: https://github.com/Klotzkette/claude-fuer-deutsches-recht/tree/main/kartellrecht-marktabgrenzung-pruefung/skills/nachfrage-quellenkarte
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: antitrust
language: de
sources:
- title: Quellenhygiene
  path: references/quellenhygiene.md
- title: Zitierweise
  path: references/zitierweise.md
---

# Nachfrage Quellenkarte

## Zweck

Diese Quellenkarte sichert für **Kartellrecht-Marktabgrenzung** jede tragende Aussage ab: Norm, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor Ausgabe verifiziert.

## Tragende Normen (live prüfen)

- **§§ 18-19 GWB Marktbeherrschung** — amtlichen Stand vor tragender Aussage prüfen
- **§§ 35 ff. GWB Fusionskontrolle** — amtlichen Stand vor tragender Aussage prüfen
- **Art. 101, 102 AEUV** — amtlichen Stand vor tragender Aussage prüfen
- **FKVO 139/2004** — amtlichen Stand vor tragender Aussage prüfen

## Zuständige Spruchkörper und Behörden

- BKartA
- EU-Kommission DG COMP
- OLG Düsseldorf Kartellsenat

## Amtliche und frei zugängliche Datenbanken

- gesetze-im-internet.de (Bundesrecht amtlich)
- rechtsprechung-im-internet.de
- dejure.org / openJur (frei zugängliche Rechtsprechung)
- bundeskartellamt.de (Fallberichte, Entscheidungen)
- EU-Kommission DG COMP (Case Search)

## Fristen mit Quellenrelevanz

- FKVO 25 Arbeitstage Phase I
- Beschwerdefrist BKartA-Beschluss 1 Monat

## Prüfroute

1. Normtext gegen die amtliche Quelle prüfen (Fassung, Inkrafttreten, Übergangsrecht).
2. Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Fundstelle ausgeben; Senat/Spruchkörper benennen.
3. Behördenpraxis (Merkblätter, Erlasse, FAQ) mit Stand-Datum zitieren.
4. Ergebnis als Quellenmatrix: Aussage — Quelle — Stand — Tragweite — Restunsicherheit.

## Fehlerbremse

- Keine BeckRS-/juris-Blindzitate aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
- Zitierform nach `references/zitierweise.md`; Quellenhygiene nach `references/quellenhygiene.md`.
