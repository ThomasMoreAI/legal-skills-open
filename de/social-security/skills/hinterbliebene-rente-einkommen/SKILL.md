---
name: hinterbliebene-rente-einkommen
title: Hinterbliebenenrente und Einkommen
description: 'Für Hinterbliebenenrente und Einkommen: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt.'
author: Klotzkette
author_url: https://github.com/Klotzkette/claude-fuer-deutsches-recht/tree/main/rentenpruefer/skills/hinterbliebene-rente-einkommen
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: social-security
language: de
---

# Hinterbliebenenrente und Einkommen

Nutze diesen Skill, wenn nach einem Todesfall Rentenanspruch, Einkommensanrechnung oder Krankenversicherung unklar sind.

## Prüfraster

1. Familienstand, Ehezeit, Todesdatum und Kinder erfassen.
2. Rentenart bestimmen: kleine Witwen- oder Witwerrente, große Witwen- oder Witwerrente, Waisenrente, Sterbevierteljahr.
3. Einkommen trennen: eigene Rente, Arbeitslohn, Betriebsrente, private Rente, Kapitalleistung, Miete, Selbständigkeit.
4. Bescheid prüfen: Beginn, Abschlag, Freibetrag, Dynamisierung, Kranken- und Pflegeversicherung.
5. Korrekturweg bauen: fehlende Zeiten des Verstorbenen, falsches Einkommen, Versorgungsausgleich, Pflegezeiten, Zahlstellenmeldung.

## Output

Gib zuerst eine verständliche Monatsübersicht aus: Anspruch, Anrechnung, Netto, offener Punkt. Danach folgt ein Widerspruchs- oder Korrekturantrag mit konkreten Anlagen.

## Anker

- SGB VI zu Renten wegen Todes.
- SGB V und SGB XI für Nettoeffekte mit Kranken- und Pflegeversicherung.
