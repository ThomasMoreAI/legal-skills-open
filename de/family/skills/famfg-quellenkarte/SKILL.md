---
name: famfg-quellenkarte
title: Famfg Quellenkarte
description: 'Für FamFG Quellenkarte: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt.'
author: Klotzkette
author_url: https://github.com/Klotzkette/claude-fuer-deutsches-recht/tree/main/fachanwalt-familienrecht/skills/famfg-quellenkarte
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: family
language: de
sources:
- title: Quellenhygiene
  path: references/quellenhygiene.md
- title: Zitierweise
  path: references/zitierweise.md
---

# Famfg Quellenkarte

## Zweck

Diese Quellenkarte sichert für **Fachanwalt Familienrecht** jede tragende Aussage ab: Norm, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor Ausgabe verifiziert.

## Tragende Normen (live prüfen)

- **BGB Paragrafen 1297 ff.** — amtlichen Stand vor tragender Aussage prüfen
- **FamFG** — amtlichen Stand vor tragender Aussage prüfen
- **VersAusglG** — amtlichen Stand vor tragender Aussage prüfen
- **KindUVO** — amtlichen Stand vor tragender Aussage prüfen

## Zuständige Spruchkörper und Behörden

- Familiengericht (AG)
- Jugendamt

## Amtliche und frei zugängliche Datenbanken

- gesetze-im-internet.de (Bundesrecht amtlich)
- rechtsprechung-im-internet.de
- dejure.org / openJur (frei zugängliche Rechtsprechung)

## Fristen mit Quellenrelevanz

- Trennungsjahr Paragraf 1565 BGB
- Beschwerde 1 Monat Paragraf 63 FamFG

## Prüfroute

1. Normtext gegen die amtliche Quelle prüfen (Fassung, Inkrafttreten, Übergangsrecht).
2. Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Fundstelle ausgeben; Senat/Spruchkörper benennen.
3. Behördenpraxis (Merkblätter, Erlasse, FAQ) mit Stand-Datum zitieren.
4. Ergebnis als Quellenmatrix: Aussage — Quelle — Stand — Tragweite — Restunsicherheit.

## Fehlerbremse

- Keine BeckRS-/juris-Blindzitate aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
- Zitierform nach `references/zitierweise.md`; Quellenhygiene nach `references/quellenhygiene.md`.
