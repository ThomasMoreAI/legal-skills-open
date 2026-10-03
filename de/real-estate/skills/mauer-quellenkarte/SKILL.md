---
name: mauer-quellenkarte
title: Mauer Quellenkarte
description: 'Für Mauer Quellenkarte: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt.'
author: Klotzkette
author_url: https://github.com/Klotzkette/claude-fuer-deutsches-recht/tree/main/nachbarschaftsstreit-pruefer/skills/mauer-quellenkarte
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

# Mauer Quellenkarte

## Zweck

Diese Quellenkarte sichert für **Nachbarschaftsstreit** jede tragende Aussage ab: Norm, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor Ausgabe verifiziert.

## Tragende Normen (live prüfen)

- **BGB §§ 906, 1004** — amtlichen Stand vor tragender Aussage prüfen
- **Landesnachbarrechtsgesetze** — amtlichen Stand vor tragender Aussage prüfen
- **BauO Länder** — amtlichen Stand vor tragender Aussage prüfen

## Zuständige Spruchkörper und Behörden

- Amtsgericht
- Schiedsamt (oft Pflichtverfahren vor Klage)
- Bauamt

## Amtliche und frei zugängliche Datenbanken

- gesetze-im-internet.de (Bundesrecht amtlich)
- rechtsprechung-im-internet.de
- dejure.org / openJur (frei zugängliche Rechtsprechung)

## Fristen mit Quellenrelevanz

- § 906 II 2 BGB jährliche Berechnung
- Schiedsamtsverfahren vor Klage

## Prüfroute

1. Normtext gegen die amtliche Quelle prüfen (Fassung, Inkrafttreten, Übergangsrecht).
2. Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Fundstelle ausgeben; Senat/Spruchkörper benennen.
3. Behördenpraxis (Merkblätter, Erlasse, FAQ) mit Stand-Datum zitieren.
4. Ergebnis als Quellenmatrix: Aussage — Quelle — Stand — Tragweite — Restunsicherheit.

## Fehlerbremse

- Keine BeckRS-/juris-Blindzitate aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
- Zitierform nach `references/zitierweise.md`; Quellenhygiene nach `references/quellenhygiene.md`.
