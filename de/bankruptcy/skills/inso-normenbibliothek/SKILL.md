---
name: inso-normenbibliothek
title: 'Vorschriften der Insolvenzordnung gezielt erschließen'
description: Erschließt eine konkret bezeichnete Vorschrift der Insolvenzordnung mit aktuellem Wortlaut, Systemstelle, Tatbestandsmerkmalen, Rechtsfolge, Fristen, Belegen und Verfahrensbezug.
author: Klotzkette
author_url: https://github.com/Klotzkette/claude-fuer-deutsches-recht/tree/main/fachanwalt-insolvenz-sanierungsrecht/skills/inso-normenbibliothek
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: bankruptcy
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
- title: Index
  path: references/index.md
---

# 1. Vorschriften der Insolvenzordnung gezielt erschließen

## 1.1 Zweck und Anwendungsfall

Dieser Skill liefert den normbezogenen Einstieg, wenn eine Vorschrift der Insolvenzordnung genannt ist oder aus dem Sachverhalt ermittelt werden muss. Vertiefte Prüfungen wie Zahlungsunfähigkeit, Überschuldung, Anfechtung, Eigenverwaltung oder Insolvenzplan bleiben Aufgabe der hierfür vorhandenen Fachworkflows.

## 1.2 Eingaben

Benötigt werden Norm oder Fallfrage, Beteiligtenrolle, Verfahrensstadium, Fristlage und gewünschter Output. Aus der Akte sind nur diejenigen Unterlagen heranzuziehen, welche Tatbestand, Beweis oder Rechtsfolge der konkreten Vorschrift tragen.

## 1.3 Ablauf

1. Öffne den [Bereichsindex](references/index.md) und wähle genau die Datei mit der gesuchten Vorschrift.
2. Suche in dieser Bereichsdatei nach dem exakten `Suchbegriff` und lies nur den einschlägigen Normabschnitt bis zur nächsten Überschrift. Weitere Bereiche werden erst bei einer ausdrücklichen Verweisung oder notwendigen Schnittstelle geöffnet.
3. Prüfe den aktuellen Gesetzeswortlaut und ordne die Vorschrift in Verfahrensabschnitt, Beteiligtenrolle und Rechtsfolge ein.
4. Trenne Zulässigkeit, Tatbestand, Beweismaß, Darlegungs- und Beweislast, Frist, Zuständigkeit und Rechtsmittel.
5. Wenn der Fall eine eigenständige wirtschaftliche oder prozessuale Vollprüfung verlangt, wechsle anschließend zu genau einem passenden Fachskill und übergib ihm das Normergebnis samt Aktenfundstellen.

## 1.4 Quellenpflicht

Gesetzesstand und tragende Rechtsprechung sind aktuell und aus überprüfbaren Quellen zu verifizieren. Eine hinterlegte Arbeitskarte darf weder veralteten Wortlaut noch eine ungesicherte Fundstelle ersetzen.

## 1.5 Ausgabeformat

Liefere eine knappe Normkarte mit Tatbestand, Rechtsfolge, Verfahrensposition, Belegbedarf, Frist, stärkster Gegenposition und nächstem Arbeitsschritt. Bei einem Schriftsatzauftrag wird daraus unmittelbar ein ausformulierter Baustein mit konkreten Aktenfundstellen.

## 1.6 Beispiel

Bei einer Frage zu Paragraf 17 InsO wird zunächst nur der Bereich mit dieser Vorschrift geöffnet. Ergibt sich daraus eine vollständige Insolvenzreifeprüfung, wird das Normergebnis an den spezialisierten Zahlungsunfähigkeits-Workflow übergeben, ohne weitere Normskills parallel zu laden.
