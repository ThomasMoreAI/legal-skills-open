---
name: einbuergerung-quellenkarte
title: Einbuergerung Quellenkarte
description: 'Für Einbürgerung Quellenkarte: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt.'
author: Klotzkette
author_url: https://github.com/Klotzkette/claude-fuer-deutsches-recht/tree/main/fachanwalt-migrationsrecht/skills/einbuergerung-quellenkarte
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: immigration
language: de
sources:
- title: Quellenhygiene
  path: references/quellenhygiene.md
- title: Zitierweise
  path: references/zitierweise.md
---

# Einbuergerung Quellenkarte

## Zweck

Diese Quellenkarte sichert für **Fachanwalt Migrationsrecht** jede tragende Aussage ab: Norm, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor Ausgabe verifiziert.

## Tragende Normen (live prüfen)

- **AufenthG, FreizügG/EU, AsylG, StAG** — amtlichen Stand vor tragender Aussage prüfen
- **Aufenthaltsverordnung** — amtlichen Stand vor tragender Aussage prüfen
- **EU-Familienzusammenführungs-RL** — amtlichen Stand vor tragender Aussage prüfen

## Zuständige Spruchkörper und Behörden

- Ausländerbehörde
- BAMF
- Verwaltungsgericht

## Amtliche und frei zugängliche Datenbanken

- gesetze-im-internet.de (Bundesrecht amtlich)
- rechtsprechung-im-internet.de
- dejure.org / openJur (frei zugängliche Rechtsprechung)
- BAMF-Entscheidungsdatenbank
- asyl.net (Rechtsprechungsdatenbank)
- EuGH CURIA

## Fristen mit Quellenrelevanz

- § 74 AsylG Klagefrist 2 Wochen / 1 Mon.
- Aufenthaltstitel-Verlängerung 8 Wochen vorher

## Prüfroute

1. Normtext gegen die amtliche Quelle prüfen (Fassung, Inkrafttreten, Übergangsrecht).
2. Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Fundstelle ausgeben; Senat/Spruchkörper benennen.
3. Behördenpraxis (Merkblätter, Erlasse, FAQ) mit Stand-Datum zitieren.
4. Ergebnis als Quellenmatrix: Aussage — Quelle — Stand — Tragweite — Restunsicherheit.

## Fehlerbremse

- Keine BeckRS-/juris-Blindzitate aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
- Zitierform nach `references/zitierweise.md`; Quellenhygiene nach `references/quellenhygiene.md`.
