---
name: haftpflicht-quellenkarte
title: Haftpflicht Quellenkarte
description: 'Für Haftpflicht Quellenkarte: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt.'
author: Klotzkette
author_url: https://github.com/Klotzkette/claude-fuer-deutsches-recht/tree/main/fachanwalt-versicherungsrecht/skills/haftpflicht-quellenkarte
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: insurance
language: de
sources:
- title: Quellenhygiene
  path: references/quellenhygiene.md
- title: Zitierweise
  path: references/zitierweise.md
---

# Haftpflicht Quellenkarte

## Zweck

Diese Quellenkarte sichert für **Fachanwalt Versicherungsrecht** jede tragende Aussage ab: Norm, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor Ausgabe verifiziert.

## Tragende Normen (live prüfen)

- **VVG** — amtlichen Stand vor tragender Aussage prüfen
- **PflVG** — amtlichen Stand vor tragender Aussage prüfen
- **ZPO/Versicherungs-Streit** — amtlichen Stand vor tragender Aussage prüfen
- **BGB** — amtlichen Stand vor tragender Aussage prüfen

## Zuständige Spruchkörper und Behörden

- Zivilgerichte
- BaFin
- Versicherungsombudsmann

## Amtliche und frei zugängliche Datenbanken

- gesetze-im-internet.de (Bundesrecht amtlich)
- rechtsprechung-im-internet.de
- dejure.org / openJur (frei zugängliche Rechtsprechung)

## Fristen mit Quellenrelevanz

- Paragrafen 195 und 199 BGB: regelmäßige Verjährung; Entstehung und Kenntnis fallbezogen bestimmen
- Paragraf 15 VVG: Hemmung nach Anmeldung des Anspruchs bis zum Zugang der Versichererentscheidung in Textform
- Paragraf 30 VVG und konkrete AVB: Anzeige des Versicherungsfalls und gegebenenfalls weitere vertragliche Meldeobliegenheiten

## Prüfroute

1. Normtext gegen die amtliche Quelle prüfen (Fassung, Inkrafttreten, Übergangsrecht).
2. Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Fundstelle ausgeben; Senat/Spruchkörper benennen.
3. Behördenpraxis (Merkblätter, Erlasse, FAQ) mit Stand-Datum zitieren.
4. Ergebnis als Quellenmatrix: Aussage — Quelle — Stand — Tragweite — Restunsicherheit.

## Fehlerbremse

- Keine BeckRS-/juris-Blindzitate aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
- Zitierform nach `references/zitierweise.md`; Quellenhygiene nach `references/quellenhygiene.md`.
