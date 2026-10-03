---
name: notare-quellenkarte
title: Notare Quellenkarte
description: 'Für Notare Quellenkarte: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt.'
author: Klotzkette
author_url: https://github.com/Klotzkette/claude-fuer-deutsches-recht/tree/main/berufsrecht-ki-vertragspruefung/skills/notare-quellenkarte
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: data-protection
language: de
sources:
- title: Quellenhygiene
  path: references/quellenhygiene.md
- title: Zitierweise
  path: references/zitierweise.md
---

# Notare Quellenkarte

## Zweck

Diese Quellenkarte sichert für **Berufsrechts-KI bei Vertragsprüfung** jede tragende Aussage ab: Norm, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor Ausgabe verifiziert.

## Tragende Normen (live prüfen)

- **§ 43a BRAO** — amtlichen Stand vor tragender Aussage prüfen
- **§ 50 BRAO Aktenführung** — amtlichen Stand vor tragender Aussage prüfen
- **DSGVO Art. 28 AVV** — amtlichen Stand vor tragender Aussage prüfen
- **KI-VO Art. 6, 50** — amtlichen Stand vor tragender Aussage prüfen

## Zuständige Spruchkörper und Behörden

- RAK
- Datenschutzaufsicht

## Amtliche und frei zugängliche Datenbanken

- gesetze-im-internet.de (Bundesrecht amtlich)
- rechtsprechung-im-internet.de
- dejure.org / openJur (frei zugängliche Rechtsprechung)

## Fristen mit Quellenrelevanz

- Rechtzeitige Mandatsannahme
- Schriftform-Erfordernisse

## Prüfroute

1. Normtext gegen die amtliche Quelle prüfen (Fassung, Inkrafttreten, Übergangsrecht).
2. Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Fundstelle ausgeben; Senat/Spruchkörper benennen.
3. Behördenpraxis (Merkblätter, Erlasse, FAQ) mit Stand-Datum zitieren.
4. Ergebnis als Quellenmatrix: Aussage — Quelle — Stand — Tragweite — Restunsicherheit.

## Fehlerbremse

- Keine BeckRS-/juris-Blindzitate aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
- Zitierform nach `references/zitierweise.md`; Quellenhygiene nach `references/quellenhygiene.md`.
