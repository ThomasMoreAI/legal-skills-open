---
name: transfer-quellenkarte
title: Transfer Quellenkarte
description: 'Für Transfer Quellenkarte: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt.'
author: Klotzkette
author_url: https://github.com/Klotzkette/claude-fuer-deutsches-recht/tree/main/datenschutzrecht/skills/transfer-quellenkarte
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

# Transfer Quellenkarte

## Zweck

Diese Quellenkarte sichert für **Datenschutzrecht DSGVO/BDSG** jede tragende Aussage ab: Norm, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor Ausgabe verifiziert.

## Tragende Normen (live prüfen)

- **DSGVO Art. 5, 6, 13, 15, 28, 32, 33, 35** — amtlichen Stand vor tragender Aussage prüfen
- **BDSG** — amtlichen Stand vor tragender Aussage prüfen
- **TTDSG** — amtlichen Stand vor tragender Aussage prüfen

## Zuständige Spruchkörper und Behörden

- BfDI Bund
- LfDI Länder
- EDSA

## Amtliche und frei zugängliche Datenbanken

- gesetze-im-internet.de (Bundesrecht amtlich)
- rechtsprechung-im-internet.de
- dejure.org / openJur (frei zugängliche Rechtsprechung)
- edpb.europa.eu (EDSA-Leitlinien)
- Datenschutzkonferenz DSK (Beschlüsse)
- CURIA (EuGH)

## Fristen mit Quellenrelevanz

- Art. 33 Meldung 72h
- Art. 12 Antrag 1 Monat
- Art. 15 Auskunft 1 Monat

## Prüfroute

1. Normtext gegen die amtliche Quelle prüfen (Fassung, Inkrafttreten, Übergangsrecht).
2. Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Fundstelle ausgeben; Senat/Spruchkörper benennen.
3. Behördenpraxis (Merkblätter, Erlasse, FAQ) mit Stand-Datum zitieren.
4. Ergebnis als Quellenmatrix: Aussage — Quelle — Stand — Tragweite — Restunsicherheit.

## Fehlerbremse

- Keine BeckRS-/juris-Blindzitate aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
- Zitierform nach `references/zitierweise.md`; Quellenhygiene nach `references/quellenhygiene.md`.
