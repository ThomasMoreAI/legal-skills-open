---
name: hauptverhandlung-quellenkarte
title: Hauptverhandlung Quellenkarte
description: 'Für Hauptverhandlung Quellenkarte: entwickelt Ziel, Vergleich und Eskalation; Ergebnis: Verhandlungs- oder Eskalationslinie.'
author: Klotzkette
author_url: https://github.com/Klotzkette/claude-fuer-deutsches-recht/tree/main/fachanwalt-strafrecht/skills/hauptverhandlung-quellenkarte
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: criminal
language: de
sources:
- title: Quellenhygiene
  path: references/quellenhygiene.md
- title: Zitierweise
  path: references/zitierweise.md
---

# Hauptverhandlung Quellenkarte

## Zweck

Diese Quellenkarte sichert für **Fachanwalt Strafrecht** jede tragende Aussage ab: Norm, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor Ausgabe verifiziert.

## Tragende Normen (live prüfen)

- **StGB** — amtlichen Stand vor tragender Aussage prüfen
- **StPO** — amtlichen Stand vor tragender Aussage prüfen
- **JGG** — amtlichen Stand vor tragender Aussage prüfen
- **BtMG** — amtlichen Stand vor tragender Aussage prüfen
- **StGB-Nebengesetze** — amtlichen Stand vor tragender Aussage prüfen

## Zuständige Spruchkörper und Behörden

- Staatsanwaltschaft
- AG/LG/OLG
- BGH

## Amtliche und frei zugängliche Datenbanken

- gesetze-im-internet.de (Bundesrecht amtlich)
- rechtsprechung-im-internet.de
- dejure.org / openJur (frei zugängliche Rechtsprechung)

## Fristen mit Quellenrelevanz

- Revision 1 Woche/1 Mon. § 341 StPO
- Berufung 1 Woche § 314 StPO
- Akteneinsicht jederzeit

## Prüfroute

1. Normtext gegen die amtliche Quelle prüfen (Fassung, Inkrafttreten, Übergangsrecht).
2. Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Fundstelle ausgeben; Senat/Spruchkörper benennen.
3. Behördenpraxis (Merkblätter, Erlasse, FAQ) mit Stand-Datum zitieren.
4. Ergebnis als Quellenmatrix: Aussage — Quelle — Stand — Tragweite — Restunsicherheit.

## Fehlerbremse

- Keine BeckRS-/juris-Blindzitate aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
- Zitierform nach `references/zitierweise.md`; Quellenhygiene nach `references/quellenhygiene.md`.
