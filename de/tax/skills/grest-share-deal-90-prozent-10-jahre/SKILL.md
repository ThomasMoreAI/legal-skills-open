---
name: grest-share-deal-90-prozent-10-jahre
title: 'GrESt: Share Deal, 90 % und 10 Jahre'
description: 'Für GrESt: Share Deal, 90 % und 10 Jahre: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt.'
author: Klotzkette
author_url: https://github.com/Klotzkette/claude-fuer-deutsches-recht/tree/main/steuerrecht-anwalt-und-berater/skills/grest-share-deal-90-prozent-10-jahre
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: tax
language: de
sources:
- title: Quellenhygiene
  path: references/quellenhygiene.md
- title: Zitierweise
  path: references/zitierweise.md
---

# GrESt: Share Deal, 90 % und 10 Jahre

## Fachlicher Anker

- **Normen:** § 6a, § 1 Abs. 2a, § 1 Abs. 2b.
- **Entscheidungs-/Quellenanker:** Tragende Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle einsetzen; keine Entscheidung aus Modellwissen erzwingen.
- **Quellenhygiene:** `references/quellenhygiene.md` und `references/zitierweise.md` beachten.

## Datenmodell

Erstelle immer eine Tabelle:

| Datum | Vorgang | Erwerber | Veräußerer | Quote direkt | Quote mittelbar | Normrisiko |
|---|---|---|---|---:|---:|---|

## Normenroute

- **§ 1 Abs. 2a GrEStG**: Personengesellschaft, mindestens 90 % neue Gesellschafter innerhalb von 10 Jahren.
- **§ 1 Abs. 2b GrEStG**: Kapitalgesellschaft, mindestens 90 % neue Gesellschafter innerhalb von 10 Jahren.
- **§ 1 Abs. 3 GrEStG**: Anteilsvereinigung bei einer Person.
- **§ 1 Abs. 3a GrEStG**: wirtschaftliche Beteiligung über Ketten.
- **§ 19 GrEStG**: Anzeige.

## Typische Gestaltungen

| Struktur | Prüfen |
|---|---|
| 89,9 % Erwerb + 10,1 % Altgesellschafter | echte Unabhängigkeit, spätere Aufstockung, Nebenabreden |
| Co-Investor | wirtschaftliche Beteiligung, Treuhand, Call-/Put-Optionen |
| mehrstufige Holding | mittelbare Quote und Paralleltransaktionen |
| Forward Deal | Signing/Closing, Grundstückserwerb der Zielgesellschaft während Dealphase |
| Konzernumstrukturierung | § 6a GrEStG gesondert |
