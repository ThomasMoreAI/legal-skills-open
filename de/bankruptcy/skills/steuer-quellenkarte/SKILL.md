---
name: steuer-quellenkarte
title: Steuer Quellenkarte
description: 'Für Steuer Quellenkarte: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Schnittstellenkarte mit Zuständigkeits- und Nachweisfragen.'
author: Klotzkette
author_url: https://github.com/Klotzkette/claude-fuer-deutsches-recht/tree/main/tabellenreview-3d/skills/steuer-quellenkarte
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: bankruptcy
language: de
sources:
- title: Quellenhygiene
  path: references/quellenhygiene.md
- title: Zitierweise
  path: references/zitierweise.md
---

# Steuer Quellenkarte

## Zweck

Diese Quellenkarte sichert für **Tabellenreview (Excel/CSV)** jede tragende Aussage ab: Norm, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor Ausgabe verifiziert.

## Tragende Normen (live prüfen)

- **GoBD** — amtlichen Stand vor tragender Aussage prüfen
- **Tax compliance** — amtlichen Stand vor tragender Aussage prüfen

## Zuständige Spruchkörper und Behörden

- Finanzamt
- Wirtschaftsprüfer

## Amtliche und frei zugängliche Datenbanken

- gesetze-im-internet.de (Bundesrecht amtlich)
- rechtsprechung-im-internet.de
- dejure.org / openJur (frei zugängliche Rechtsprechung)

## Fristen mit Quellenrelevanz

- materielle und prozessuale Fristen des Sachgebiets

## Prüfroute

1. Normtext gegen die amtliche Quelle prüfen (Fassung, Inkrafttreten, Übergangsrecht).
2. Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Fundstelle ausgeben; Senat/Spruchkörper benennen.
3. Behördenpraxis (Merkblätter, Erlasse, FAQ) mit Stand-Datum zitieren.
4. Ergebnis als Quellenmatrix: Aussage — Quelle — Stand — Tragweite — Restunsicherheit.

## Fehlerbremse

- Keine BeckRS-/juris-Blindzitate aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
- Zitierform nach `references/zitierweise.md`; Quellenhygiene nach `references/quellenhygiene.md`.
