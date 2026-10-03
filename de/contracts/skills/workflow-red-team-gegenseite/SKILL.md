---
name: workflow-red-team-gegenseite
title: Red-Team Gegenseite BGB BT
description: 'Für Red-Team Gegenseite BGB BT: prüft Ergebnis, Beweislast und Gegenposition; Ergebnis: Gegenprüfung mit Beweis- und Fristencheck.'
author: Klotzkette
author_url: https://github.com/Klotzkette/claude-fuer-deutsches-recht/tree/main/bgb-bt-pruefer/skills/workflow-red-team-gegenseite
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: contracts
language: de
---

# Red-Team Gegenseite BGB BT

## Sofortstart

1. Kläre Rolle, Ziel, Gegner, Frist, Dokumente und gewünschtes Arbeitsprodukt.
2. Zerlege den Fall in Tatsachen, Normen, Streitpunkte, Beweisfragen und methodische Wertungen.
3. Liefere zuerst eine Kurzantwort mit Risikoampel, danach den Prüfpfad.
4. Schlage nach jedem Zwischenergebnis zwei bis fünf passende Anschluss-Skills aus demselben Plugin vor.

## Arbeitsweise

Liefere Top-10-Angriffe, Verteidigungsbausteine und Vergleichsdruckpunkte.

## Rechts- und Quellenanker

BGB amtlich prüfen: https://www.gesetze-im-internet.de/bgb/. Je nach Skill insbesondere §§ 241 ff., 249 ff., 280 ff., 433 ff., 488 ff., 535 ff., 581 ff., 611 ff., 631 ff., 662 ff., 675 ff., 677 ff., 765 ff., 812 ff., 823 ff. BGB.

## Stoppschilder

- Keine Kommentar-, Aufsatz- oder BeckRS/Juris-Blindzitate.
- Tragende Gesetzesstände live gegen amtliche/frei zugängliche Quellen prüfen.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und überprüfbarer Quelle verwenden.
- Bei Unsicherheit die Annahme ausdrücklich markieren und eine Rückfrage oder Quellenprüfung auslösen.

## Output

- Kurzantwort mit Risikoampel
- Anspruchsmatrix
- Prüfvermerk oder Gutachten
- Beweis- und Lückenliste
- Anschluss-Skill-Empfehlung


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
