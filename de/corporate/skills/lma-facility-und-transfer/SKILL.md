---
name: lma-facility-und-transfer
title: 'Corporate: LMA Facility und Transfer'
description: 'Für Corporate: LMA Facility und Transfer: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt.'
author: Klotzkette
author_url: https://github.com/Klotzkette/claude-fuer-deutsches-recht/tree/main/corporate-kanzlei/skills/lma-facility-und-transfer
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: corporate
language: de
sources:
- title: Quellenhygiene
  path: references/quellenhygiene.md
- title: Zitierweise
  path: references/zitierweise.md
---

# Corporate: LMA Facility und Transfer

## Fachlicher Anker

- **Normen:** §§ 3, §§ 76, §§ 105.
- **Entscheidungs-/Quellenanker:** Tragende Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle einsetzen; keine Entscheidung aus Modellwissen erzwingen.
- **Quellenhygiene:** `references/quellenhygiene.md` und `references/zitierweise.md` beachten.

## Wofür dieser Arbeitsgang da ist

Der Skill übersetzt LMA-Marktstruktur in deutsche Deal- und Rechtsfolgen, ohne LMA-Mustertext zu reproduzieren.

## Rechts- und Praxisanker

BGB, Sicherheitenrecht, GmbHG/AktG Kapitalerhaltung, LMA-Upload, Steuer, Sanktionen.

## Workflow

1. Hochgeladenes Finanzierungsdokument, Schuldschein, Transfer Notice, LMA Facility Agreement oder NPL-Portfolio zuerst identifizieren.
2. Parteiperspektive, Deal-Ziel, Fristen, Consent-Erfordernisse, Sicherheiten und Datenschutzfragen klären.
3. Übertragungsweg, Rechtswirkung, offene Dokumente und Risiken in einer Closing-/Verfahrensmatrix darstellen.
4. Bei Insolvenz-/Krisenbezug Rang, Anfechtung, Planrechte, Enforcement und Geschäftsleiterpflichten gesondert prüfen.

## Qualitätsgate

- Keine Blindzitate: Rechtsprechung, Behördenpraxis und Schwellenwerte vor tragender Aussage live anhand amtlicher oder frei zugänglicher Quellen prüfen.
- Keine LMA-, Banken- oder Fondsformularsprache nacherzählen: Nutzer soll das aktuelle Dokument hochladen; der Skill arbeitet dann am konkreten Text.
- Jede Annahme sichtbar markieren, insbesondere Zahlen, Fristen, regulatorische Rollen, Genehmigungsstand und Parteiperspektive.
