---
name: stb-bwa-sus-bilanz-pruefung
title: BWA-, SuSa- und Bilanzpruefung bei Krisensignalen
description: 'Für BWA-, SuSa- und Bilanzprüfung bei Krisensignalen: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Tatbestands- oder Anspruchsmatrix.'
author: Klotzkette
author_url: https://github.com/Klotzkette/claude-fuer-deutsches-recht/tree/main/steuerrecht-anwalt-und-berater/skills/stb-bwa-sus-bilanz-pruefung
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: tax
language: de
sources:
- title: Hinweisschreiben 102 starug
  path: references/hinweisschreiben-102-starug.md
- title: Insolvenzreife checkliste
  path: references/insolvenzreife-checkliste.md
---

# BWA-, SuSa- und Bilanzpruefung bei Krisensignalen

Dieser Skill prueft Rechnungswesenunterlagen einer GmbH, UG oder haftungsbeschraenkten Struktur auf insolvenz- und haftungsrechtliche Warnsignale. Er ist fuer Steuerberatung und anwaltliche Krisenfrueherkennung gedacht, wenn BWA, Summen- und Saldenliste, OPOS, Bankdaten oder Bilanzentwurf vorliegen.

## Normenanker

- §§ 17, 18, 19 InsO fuer Zahlungsunfaehigkeit, drohende Zahlungsunfaehigkeit und Ueberschuldung.
- § 15a InsO fuer Antragspflicht.
- Paragraf 102 StaRUG nur bei Jahresabschlusserstellung, offenkundigen Anhaltspunkten und vermuteter Unkenntnis des Mandanten; BWA und SuSa sind lediglich mögliche Belegquellen.
- §§ 34, 69 AO fuer steuerliche Vertreter- und Haftungsrisiken.
- § 43 GmbHG fuer Geschaeftsfuehrerpflichten.

## Arbeitsgang

1. Pruefe Liquiditaet, faellige Verbindlichkeiten, Banklinien, OPOS und rueckstaendige Steuern/Sozialabgaben.
2. Pruefe Eigenkapital, stille Lasten, Rangruecktritte und Fortbestehensprognose.
3. Nutze `references/insolvenzreife-checkliste.md` und `references/hinweisschreiben-102-starug.md`.
4. Trenne reine Plausibilitaet von rechtlicher Insolvenzreifepruefung und markiere Beratungsgrenzen.

## Ergebnis

Erstelle einen Krisenvermerk mit Ampel, Zahlenbasis, fehlenden Unterlagen, Warnhinweis an Mandant oder Geschaeftsfuehrung und naechstem Pruefschritt.
