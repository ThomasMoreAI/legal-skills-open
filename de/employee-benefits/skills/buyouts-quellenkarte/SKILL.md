---
name: buyouts-quellenkarte
title: Buyouts Quellenkarte
description: 'Für Buyouts Quellenkarte: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt.'
author: Klotzkette
author_url: https://github.com/Klotzkette/claude-fuer-deutsches-recht/tree/main/bav-strategie-konzern/skills/buyouts-quellenkarte
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: employee-benefits
language: de
sources:
- title: Quellenhygiene
  path: references/quellenhygiene.md
- title: Zitierweise
  path: references/zitierweise.md
---

# Buyouts Quellenkarte

## Zweck

Diese Quellenkarte sichert für **Betriebliche Altersversorgung im Konzern** jede tragende Aussage ab: Norm, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor Ausgabe verifiziert.

## Tragende Normen (live prüfen)

- **BetrAVG** — amtlichen Stand vor tragender Aussage prüfen
- **§ 1 BetrAVG Zusage** — amtlichen Stand vor tragender Aussage prüfen
- **§ 16 BetrAVG Anpassung** — amtlichen Stand vor tragender Aussage prüfen
- **EStG § 3 Nr. 63, § 6a** — amtlichen Stand vor tragender Aussage prüfen

## Zuständige Spruchkörper und Behörden

- BaFin (PSV)
- Finanzamt
- Arbeitsgericht

## Amtliche und frei zugängliche Datenbanken

- gesetze-im-internet.de (Bundesrecht amtlich)
- rechtsprechung-im-internet.de
- dejure.org / openJur (frei zugängliche Rechtsprechung)

## Fristen mit Quellenrelevanz

- Anpassungsprüfung alle 3 Jahre § 16 BetrAVG
- Insolvenzsicherung PSV

## Prüfroute

1. Normtext gegen die amtliche Quelle prüfen (Fassung, Inkrafttreten, Übergangsrecht).
2. Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Fundstelle ausgeben; Senat/Spruchkörper benennen.
3. Behördenpraxis (Merkblätter, Erlasse, FAQ) mit Stand-Datum zitieren.
4. Ergebnis als Quellenmatrix: Aussage — Quelle — Stand — Tragweite — Restunsicherheit.

## Fehlerbremse

- Keine BeckRS-/juris-Blindzitate aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
- Zitierform nach `references/zitierweise.md`; Quellenhygiene nach `references/quellenhygiene.md`.
