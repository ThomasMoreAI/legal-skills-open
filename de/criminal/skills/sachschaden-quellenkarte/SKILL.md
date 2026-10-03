---
name: sachschaden-quellenkarte
title: Sachschaden Quellenkarte
description: 'Für Sachschaden Quellenkarte: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt.'
author: Klotzkette
author_url: https://github.com/Klotzkette/claude-fuer-deutsches-recht/tree/main/fachanwalt-verkehrsrecht/skills/sachschaden-quellenkarte
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

# Sachschaden Quellenkarte

## Zweck

Diese Quellenkarte sichert für **Fachanwalt Verkehrsrecht** jede tragende Aussage ab: Norm, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor Ausgabe verifiziert.

## Tragende Normen (live prüfen)

- **StGB §§ 142, 315c, 316** — amtlichen Stand vor tragender Aussage prüfen
- **StVG** — amtlichen Stand vor tragender Aussage prüfen
- **StVO** — amtlichen Stand vor tragender Aussage prüfen
- **OWiG, BKatV** — amtlichen Stand vor tragender Aussage prüfen
- **PflVG, BGB §§ 823 ff.** — amtlichen Stand vor tragender Aussage prüfen

## Zuständige Spruchkörper und Behörden

- AG (Bußgeld + Straf)
- Polizei
- Straßenverkehrsbehörde (FeV)
- Versicherer

## Amtliche und frei zugängliche Datenbanken

- gesetze-im-internet.de (Bundesrecht amtlich)
- rechtsprechung-im-internet.de
- dejure.org / openJur (frei zugängliche Rechtsprechung)
- KBA (FAER-Auskunft)
- bundesgerichtshof.de (4. Strafsenat, VI. Zivilsenat)

## Fristen mit Quellenrelevanz

- § 67 OWiG Einspruch 2 Wochen
- Strafbefehl 2 Wochen § 410 StPO
- Verjährung 3 Mon. OWi

## Prüfroute

1. Normtext gegen die amtliche Quelle prüfen (Fassung, Inkrafttreten, Übergangsrecht).
2. Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Fundstelle ausgeben; Senat/Spruchkörper benennen.
3. Behördenpraxis (Merkblätter, Erlasse, FAQ) mit Stand-Datum zitieren.
4. Ergebnis als Quellenmatrix: Aussage — Quelle — Stand — Tragweite — Restunsicherheit.

## Fehlerbremse

- Keine BeckRS-/juris-Blindzitate aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
- Zitierform nach `references/zitierweise.md`; Quellenhygiene nach `references/quellenhygiene.md`.
