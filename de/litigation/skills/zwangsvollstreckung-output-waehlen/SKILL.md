---
name: zwangsvollstreckung-output-waehlen
title: Output wählen
description: 'Für Output wählen: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. Fachgebiet: Zwangsvollstreckung.'
author: Klotzkette
author_url: https://github.com/Klotzkette/claude-fuer-deutsches-recht/tree/main/zwangsvollstreckung/skills/output-waehlen
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

# Output wählen

## Einsatzlage

Diese Output-Weiche für **Zwangsvollstreckung** entscheidet, ob Memo, Antrag, Schriftsatz, Tabelle, Risikoampel, Fragenliste oder Mandantenbrief der richtige nächste Schritt ist.

## Fachlandkarte dieses Plugins

- `765a-fehlerkatalog` — 765a Fehlerkatalog
- `802l-verhandlung-vergleich-und-eskalation` — 802l Verhandlung Vergleich und Eskalation
- `abwehr-schuldner` — Abwehr Schuldner
- `arbeit-schriftsatz-brief-und-memo-bausteine` — Arbeit Schriftsatz Brief und Memo Bausteine
- `bank-haertefall-inso` — Bank Haertefall Inso
- `elektronische-zustellung-eu` — Elektronische Zustellung EU
- `eu-kontenpfaendung-655-2014` — EU Kontenpfaendung 655 2014
- `haertefall-mandantenkommunikation-entscheidungsvorlage` — Haertefall Mandantenkommunikation Entscheidungsvorlage
- `inso-internationaler-bezug-und-schnittstellen` — Inso Internationaler Bezug und Schnittstellen
- `kommandocenter` — Kommandocenter
- `kontenpfaendung-notar-interessen-online` — Kontenpfaendung Notar Interessen Online
- `kontensuche-drittschuldner` — Kontensuche Drittschuldner
- `kontensuche-quellenkarte` — Kontensuche Quellenkarte
- `anschluss-routing` — Anschluss Routing
- `dokumente-intake` — Dokumente Intake

## Arbeitsweg

- Ergebnistyp bestimmen: Schriftsatz an Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen, Mandantenmemo, Risikobericht, Vertragsentwurf, Entscheidungsvorlage, Behörden-Stellungnahme — was braucht der Mandant wirklich?
- Pflichtformate festlegen: Tenor / Antrag / Begründung (Anspruchsgrundlage, Tatbestand, Subsumtion, Ergebnis); konkrete Norm-Pinpoints im Zwangsvollstreckung (ZPO, § 201 InsO, ZVG, EU, § 765a H, § 800 ZPO Notar,, § 802l Kontensuche, Verm, §§ 704 ff) einarbeiten.
- Adressat-Klarheit: Sprache, Detailtiefe und juristische Vorbildung des Empfängers berücksichtigen; bei Mandant ohne Vorbildung Klartext-Zusammenfassung voranstellen.
- Beweis- und Anlagenstruktur planen (chronologisch, thematisch, K- und B-Anlagen); Bezugnahmen sauber kennzeichnen.
- Quellenfußnoten und Zitierweise sichern; offene Punkte und Annahmen explizit als solche kennzeichnen.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
