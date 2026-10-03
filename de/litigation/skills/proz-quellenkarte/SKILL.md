---
name: proz-quellenkarte
title: Proz Quellenkarte
description: 'Für Proz Quellenkarte: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt.'
author: Klotzkette
author_url: https://github.com/Klotzkette/claude-fuer-deutsches-recht/tree/main/prozessrecht/skills/proz-quellenkarte
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: litigation
language: de
sources:
- title: Quellenhygiene
  path: references/quellenhygiene.md
- title: Zitierweise
  path: references/zitierweise.md
---

# Proz Quellenkarte

## Zweck

Diese Quellenkarte sichert für **Prozessrecht (ZPO/VwGO/StPO/SGG)** jede tragende Aussage ab: Norm, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor Ausgabe verifiziert.

## Tragende Normen (live prüfen)

- **ZPO, VwGO, StPO, SGG, FGO, FamFG** — amtlichen Stand vor tragender Aussage prüfen

## Zuständige Spruchkörper und Behörden

- Erste Instanz / Rechtsmittelgerichte

## Amtliche und frei zugängliche Datenbanken

- gesetze-im-internet.de (Bundesrecht amtlich)
- rechtsprechung-im-internet.de
- dejure.org / openJur (frei zugängliche Rechtsprechung)

## Fristen mit Quellenrelevanz

- Berufung 1 Mon. Paragraf 517 ZPO
- Revision 1 Mon.
- Klagefrist Paragraf 74 VwGO 1 Mon.
- Anhörungsrüge 2 Wochen Paragraf 321a

## Prüfroute

1. Normtext gegen die amtliche Quelle prüfen (Fassung, Inkrafttreten, Übergangsrecht).
2. Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Fundstelle ausgeben; Senat/Spruchkörper benennen.
3. Behördenpraxis (Merkblätter, Erlasse, FAQ) mit Stand-Datum zitieren.
4. Ergebnis als Quellenmatrix: Aussage — Quelle — Stand — Tragweite — Restunsicherheit.

## Fehlerbremse

- Keine BeckRS-/juris-Blindzitate aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
- Zitierform nach `references/zitierweise.md`; Quellenhygiene nach `references/quellenhygiene.md`.
