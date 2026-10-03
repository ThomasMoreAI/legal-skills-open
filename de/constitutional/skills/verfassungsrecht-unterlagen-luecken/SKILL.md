---
name: verfassungsrecht-unterlagen-luecken
title: Unterlagen und Lücken
description: 'Für Unterlagen und Lücken: ordnet Akte, Belege und Lücken; Ergebnis: Dokumentenmatrix mit Nachforderungsliste. Fachgebiet: verfassungsrecht.'
author: Klotzkette
author_url: https://github.com/Klotzkette/claude-fuer-deutsches-recht/tree/main/verfassungsrecht/skills/unterlagen-luecken
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: constitutional
language: de
sources:
- title: Quellenhygiene
  path: references/quellenhygiene.md
- title: Zitierweise
  path: references/zitierweise.md
---

# Unterlagen und Lücken

## Einsatzlage

Diese Unterlagenprüfung für **Verfassungsrecht** benennt fehlende Dokumente, streitige Tatsachen, Beweisrisiken und die kürzeste sichere Nachforderung.

## Fachlandkarte dieses Plugins

- `acht-zahlen-schwellen-und-berechnung` — Acht Zahlen Schwellen und Berechnung
- `bundesverfassungsgericht-quellenkarte-check` — Bundesverfassungsgericht Quellenkarte Check
- `bverfg-rechtsprechung-recherchieren` — Bverfg Rechtsprechung Recherchieren
- `bverfg-verfahrenssicht-und-annahmerisiko` — Bverfg Verfahrenssicht und Annahmerisiko
- `formelle-mehrparteien-konflikt-und-interessen` — Formelle Mehrparteien Konflikt und Interessen
- `formelle-verfassungsmaessigkeit` — Formelle Verfassungsmaessigkeit
- `gesetzentwurf-gg-konformitaet-pruefen` — Gesetzentwurf GG Konformitaet Prüfen
- `gesetzgebungskompetenz-grundrechtspruefung` — Gesetzgebungskompetenz Grundrechtspruefung
- `gesetzgebungskompetenz-pruefen` — Gesetzgebungskompetenz Prüfen
- `grundgesetz-fristen-form-und-zustaendigkeit` — Grundgesetz Fristen Form und Zustaendigkeit
- `grundrechte-fehlerkatalog` — Grundrechte Fehlerkatalog
- `grundrechtspruefung-acht-formelle-interessen` — Grundrechtspruefung Acht Formelle Interessen
- `grundrechtspruefung-und-verhaeltnismaessigkeit` — Grundrechtspruefung und Verhältnismäßigkeit
- `anschluss-routing` — Anschluss Routing
- `dokumente-intake` — Dokumente Intake

## Arbeitsweg

- Sollkatalog aufstellen: Welche Dokumente brauche ich für die konkrete Verfassungsrecht-Frage zwingend (Verfassungsbeschwerde, Antrag auf einstweilige Anordnung, Annahmebeschluss, BVerfGE-Entscheidung)?
- Ist-Abgleich: Welche Dokumente sind vorhanden, welche fehlen, welche sind unvollständig, undatiert oder ohne Unterschrift?
- Lückenliste priorisieren nach: fristrelevant (§ 93 BVerfGG Verfassungsbeschwerde 1 Monat nach Rechtswegerschöpfung / 1 Jahr bei Gesetzen, § 32 BVerfGG einstweilige Anordnung), beweisrelevant, formerheblich.
- Rückfrageschreiben an Beschwerdeführer, BVerfG (1. und 2. Senat, Kammern), Landesverfassungsgerichte, EGMR entwerfen — Wer hat das Dokument, woher kann es beschafft werden, bis wann?
- Bei behördlichen Lücken: Akteneinsichtsrecht (z. B. § 29 VwVfG, § 147 StPO, § 25 SGB X) prüfen und nutzen.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
