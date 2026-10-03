---
name: phishing-vorfall-pruefer-output-waehlen
title: Output wählen
description: 'Für Output wählen: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. Fachgebiet: Phishing-Vorfall-Prüfer.'
author: Klotzkette
author_url: https://github.com/Klotzkette/claude-fuer-deutsches-recht/tree/main/phishing-vorfall-pruefer/skills/output-waehlen
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: finance
language: de
sources:
- title: Quellenhygiene
  path: references/quellenhygiene.md
- title: Zitierweise
  path: references/zitierweise.md
---

# Output wählen

## Einsatzlage

Diese Output-Weiche für **Phishing Vorfall Prüfer** entscheidet, ob Memo, Antrag, Schriftsatz, Tabelle, Risikoampel, Fragenliste oder Mandantenbrief der richtige nächste Schritt ist.

## Fachlandkarte dieses Plugins

- `675u-675w-banking` — 675u 675w Banking
- `675v-quellenkarte` — 675v Quellenkarte
- `675w-zahlen-schwellen-und-berechnung` — 675w Zahlen Schwellen und Berechnung
- `arbeitnehmer-haftung-bgb-675u-phish-ceo` — Arbeitnehmer Haftung BGB 675u Phish CEO
- `aufsicht-bafin-bank-strategie-banking-app` — Aufsicht Bafin Bank Strategie Banking APP
- `banking-behoerden-gericht-und-registerweg` — Banking Behoerden Gericht und Registerweg
- `bankpflichten-beweislast-bgb` — Bankpflichten Beweislast BGB
- `bea-notfall-bgb-675v-erstkontakt-mandant` — BEA Notfall BGB 675v Erstkontakt Mandant
- `beweislast-mandantenkommunikation-entscheidungsvorlage` — Beweislast Mandantenkommunikation Entscheidungsvorlage
- `bgb-schriftsatz-brief-und-memo-bausteine` — BGB Schriftsatz Brief und Memo Bausteine
- `call-interessen-faelle-freistehender` — Call Interessen Faelle Freistehender
- `faelle-abschlussprodukt-und-uebergabe` — Faelle Abschlussprodukt und Übergabe
- `fahrlaessigkeit-fehlerkatalog` — Fahrlaessigkeit Fehlerkatalog
- `anschluss-routing` — Anschluss Routing
- `dokumente-intake` — Dokumente Intake

## Arbeitsweg

- Ergebnistyp bestimmen: Schriftsatz an Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen, Mandantenmemo, Risikobericht, Vertragsentwurf, Entscheidungsvorlage, Behörden-Stellungnahme — was braucht der Mandant wirklich?
- Pflichtformate festlegen: Tenor / Antrag / Begründung (Anspruchsgrundlage, Tatbestand, Subsumtion, Ergebnis); konkrete Norm-Pinpoints im Phishing Vorfall Prüfer (BGB, § 675u,, § 675v,, § 675w, pushTAN, Call) einarbeiten.
- Adressat-Klarheit: Sprache, Detailtiefe und juristische Vorbildung des Empfängers berücksichtigen; bei Mandant ohne Vorbildung Klartext-Zusammenfassung voranstellen.
- Beweis- und Anlagenstruktur planen (chronologisch, thematisch, K- und B-Anlagen); Bezugnahmen sauber kennzeichnen.
- Quellenfußnoten und Zitierweise sichern; offene Punkte und Annahmen explizit als solche kennzeichnen.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
