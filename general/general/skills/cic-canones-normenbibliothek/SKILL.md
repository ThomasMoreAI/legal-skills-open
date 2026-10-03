---
name: cic-canones-normenbibliothek
title: 1. CIC-Canones gezielt erschließen
description: Erschließt einen konkret bezeichneten Canon des CIC mit amtlichem Textabgleich, Systemstelle, Nachbarcanones, Tatbestand, Rechtsfolge und belastbarer Arbeitsausgabe.
author: Klotzkette
author_url: https://github.com/Klotzkette/claude-fuer-deutsches-recht/tree/main/roemisch-katholisches-kirchenrecht/skills/cic-canones-normenbibliothek
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: de
sources:
- title: Bereich 01
  path: references/bereich-01.md
- title: Bereich 02
  path: references/bereich-02.md
- title: Bereich 03
  path: references/bereich-03.md
- title: Bereich 04
  path: references/bereich-04.md
- title: Bereich 05
  path: references/bereich-05.md
- title: Bereich 06
  path: references/bereich-06.md
- title: Bereich 07
  path: references/bereich-07.md
- title: Bereich 08
  path: references/bereich-08.md
- title: Bereich 09
  path: references/bereich-09.md
- title: Bereich 10
  path: references/bereich-10.md
- title: Bereich 11
  path: references/bereich-11.md
- title: Bereich 12
  path: references/bereich-12.md
- title: Bereich 13
  path: references/bereich-13.md
- title: Bereich 14
  path: references/bereich-14.md
- title: Bereich 15
  path: references/bereich-15.md
- title: Bereich 16
  path: references/bereich-16.md
- title: Bereich 17
  path: references/bereich-17.md
- title: Bereich 18
  path: references/bereich-18.md
- title: Bereich 19
  path: references/bereich-19.md
- title: Bereich 20
  path: references/bereich-20.md
- title: Bereich 21
  path: references/bereich-21.md
- title: Bereich 22
  path: references/bereich-22.md
- title: Bereich 23
  path: references/bereich-23.md
- title: Bereich 24
  path: references/bereich-24.md
- title: Bereich 25
  path: references/bereich-25.md
- title: Bereich 26
  path: references/bereich-26.md
- title: Bereich 27
  path: references/bereich-27.md
- title: Bereich 28
  path: references/bereich-28.md
- title: Bereich 29
  path: references/bereich-29.md
- title: Bereich 30
  path: references/bereich-30.md
- title: Bereich 31
  path: references/bereich-31.md
- title: Bereich 32
  path: references/bereich-32.md
- title: Bereich 33
  path: references/bereich-33.md
- title: Bereich 34
  path: references/bereich-34.md
- title: Bereich 35
  path: references/bereich-35.md
- title: Bereich 36
  path: references/bereich-36.md
- title: Bereich 37
  path: references/bereich-37.md
- title: Bereich 38
  path: references/bereich-38.md
- title: Bereich 39
  path: references/bereich-39.md
- title: Bereich 40
  path: references/bereich-40.md
- title: Bereich 41
  path: references/bereich-41.md
- title: Bereich 42
  path: references/bereich-42.md
- title: Bereich 43
  path: references/bereich-43.md
- title: Index
  path: references/index.md
---

# 1. CIC-Canones gezielt erschließen

## 1.1 Zweck und Anwendungsfall

Dieser Skill bearbeitet eine konkret bezeichnete Vorschrift des CIC oder findet aus einem Sachproblem die einschlägige Norm. Die einzelnen Canones liegen als unterstützende Bereichsdateien vor und werden nur bei Bedarf gelesen; sie konkurrieren deshalb nicht als tausende eigenständige Einstiegswege.

## 1.2 Eingaben

Benötigt werden die Canon-Nummer oder das kirchenrechtliche Problem, die Beteiligtenrolle, der Verfahrensstand und das gewünschte Arbeitsprodukt. Liegt keine Nummer vor, grenze zuerst Buch, Titel und Regelungsgegenstand ein.

## 1.3 Ablauf

1. Öffne den [Bereichsindex](references/index.md) und bestimme genau die Datei, welche die gesuchte Canon-Nummer umfasst.
2. Suche in dieser Bereichsdatei nach dem exakten `Suchbegriff` und lies nur den bezeichneten Canon bis zur nächsten Überschrift. Öffne einen Nachbarbereich nur, wenn Verweisung, Ausnahme oder systematischer Zusammenhang dies erfordert.
3. Gleiche den aktuellen amtlichen Text und die maßgebliche Sprachfassung ab. Die hinterlegte Arbeitskarte ist Such- und Prüfstütze, kein Ersatz für den Textabgleich.
4. Trenne Tatbestand, Rechtsfolge, Zuständigkeit, Form, Frist, Beweisfrage und mögliche Spezialnorm.
5. Ordne das Verhältnis zu Partikularrecht, päpstlichen Sondernormen, Katechismus und staatlichem Recht nur ein, soweit der Fall dies verlangt.

## 1.4 Quellenpflicht

Nenne Textfassung, Fundstelle und Abrufstand. Behaupte keine aktuelle Normfassung oder Entscheidung ohne überprüfbare Quelle. Übersetzungsunterschiede werden sichtbar gemacht und nicht still geglättet.

## 1.5 Ausgabeformat

Liefere je nach Auftrag eine Normkarte, ein kanonistisches Kurzvotum, einen Aktenvermerk, einen Dekret- oder Briefbaustein oder eine verständliche Erklärung. Beginne mit Ergebnis und nächstem Schritt; die Detailbegründung folgt nur in der benötigten Tiefe.

## 1.6 Beispiel

Bei der Frage nach can. 17 wird ausschließlich der Bereich mit can. 1 bis 43 geöffnet. Danach werden Wortlaut, Auslegungsregeln, systematische Stellung und Bedeutung für den konkreten Sachverhalt verarbeitet.
