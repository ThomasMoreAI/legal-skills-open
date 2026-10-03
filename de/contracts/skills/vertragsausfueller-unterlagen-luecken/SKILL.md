---
name: vertragsausfueller-unterlagen-luecken
title: Unterlagen und Lücken
description: 'Für Unterlagen und Lücken: ordnet Akte, Belege und Lücken; Ergebnis: Dokumentenmatrix mit Nachforderungsliste. Fachgebiet: Vertragsausfüller.'
author: Klotzkette
author_url: https://github.com/Klotzkette/claude-fuer-deutsches-recht/tree/main/vertragsausfueller/skills/unterlagen-luecken
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: contracts
language: de
sources:
- title: Quellenhygiene
  path: references/quellenhygiene.md
- title: Zitierweise
  path: references/zitierweise.md
---

# Unterlagen und Lücken

## Einsatzlage

Diese Unterlagenprüfung für **Vertragsausfueller** benennt fehlende Dokumente, streitige Tatsachen, Beweisrisiken und die kürzeste sichere Nachforderung.

## Fachlandkarte dieses Plugins

- `altvertraege-dokumentenmatrix-und-lueckenliste` — Altvertraege Dokumentenmatrix und Lueckenliste
- `altvertrag-nachziehen` — Altvertrag Nachziehen
- `ausdruecklicher-fristennotiz-und-naechster-schritt` — Ausdruecklicher Fristennotiz und Naechster Schritt
- `batch-modus-docx-stripper-einfuehrung` — Batch Modus Docx Stripper Einfuehrung
- `bsag-mietvertrag-klauselentscheidung` — Bsag Mietvertrag Klauselentscheidung
- `changes-beweislast-docx-erkennen` — Changes Beweislast Docx Erkennen
- `clean-output` — Clean Output
- `docx-stripper` — Docx Stripper
- `docx-tatbestand-beweis-und-belege` — Docx Tatbestand Beweis und Belege
- `einfuehrung-prozess` — Einfuehrung Prozess
- `erkennen-schriftsatz-brief-und-memo-bausteine` — Erkennen Schriftsatz Brief und Memo Bausteine
- `erzeugen-red-fassungen-sonderfall-felder` — Erzeugen RED Fassungen Sonderfall Felder
- `fassungen-sonderfall-und-edge-case` — Fassungen Sonderfall und Edge Case
- `anschluss-routing` — Anschluss Routing
- `dokumente-intake` — Dokumente Intake

## Arbeitsweg

- Sollkatalog aufstellen: Welche Dokumente brauche ich für die konkrete Vertragsausfüller (Lückenschluss in Verträgen)-Frage zwingend (Mustervertrag, Termsheet, Klauselkatalog, Altvertrag, Vertragsentwurf mit Track Changes)?
- Ist-Abgleich: Welche Dokumente sind vorhanden, welche fehlen, welche sind unvollständig, undatiert oder ohne Unterschrift?
- Lückenliste priorisieren nach: fristrelevant (Vertragsspezifisch; § 195 BGB Regelverjährung 3 Jahre, § 14 BGB-InfoV Widerrufsfrist 14 Tage), beweisrelevant, formerheblich.
- Rückfrageschreiben an Mandant, Vertragspartner, Rechtsabteilung, Notar bei Formerfordernis entwerfen — Wer hat das Dokument, woher kann es beschafft werden, bis wann?
- Bei behördlichen Lücken: Akteneinsichtsrecht (z. B. § 29 VwVfG, § 147 StPO, § 25 SGB X) prüfen und nutzen.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
