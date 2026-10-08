---
name: ermessensfehler-borghei
title: /verwaltungsrecht:ermessensfehler
description: Prüfung behördlicher Ermessensentscheidungen auf Ermessensfehler nach § 40 VwVfG und § 114 VwGO (Ermessensnichtgebrauch, Ermessensüberschreitung, Ermessensfehlgebrauch, Verhältnismäßigkeit, Ermessensreduzierung auf null). Use when ein Verwaltungsakt auf einer Ermessensnorm beruht und die Rechtmäßigkeit der Ermessensausübung geprüft werden soll.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/verwaltungsrecht/skills/ermessensfehler
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: administrative
language: de
---

# /verwaltungsrecht:ermessensfehler

## Zweck

Beruht ein Verwaltungsakt auf einer Ermessensnorm („kann", „darf", „ist befugt"), prüft das Gericht die Entscheidung nur eingeschränkt: Es kontrolliert die Rechtmäßigkeit der Ermessensausübung, nicht ihre Zweckmäßigkeit ([§ 114 VwGO](https://www.gesetze-im-internet.de/vwgo/__114.html)). Diese Skill systematisiert die Ermessensfehlerlehre, ordnet den konkreten Fehler einer Fallgruppe zu und bewertet die Erfolgsaussichten einer Anfechtung oder Verpflichtung.

## Eingaben

- Verwaltungsakt mit Begründung (Tenor, Sachverhalt, Erwägungen)
- Ermächtigungsgrundlage (Ermessensnorm: Wortlaut „kann"/„darf")
- Behördliche Begründung der Ermessensausübung ([§ 39 VwVfG](https://www.gesetze-im-internet.de/vwvfg/__39.html))
- Vorgetragene Belange des Betroffenen (Grundrechte, Härtefall)
- Verfahrensstand (vor/nach Widerspruch, Klage anhängig?)

## Sub-Agent-Architektur

Drei spezialisierte Prüfschritte arbeiten in Prosa zusammen. Der **Ermächtigungs-Agent** klärt, ob überhaupt Ermessen eröffnet ist (Rechtsfolgenermessen vs. gebundene Entscheidung vs. unbestimmter Rechtsbegriff mit Beurteilungsspielraum) und ob ein Fall des intendierten Ermessens vorliegt. Der **Fehler-Agent** subsumiert die behördlichen Erwägungen unter die drei Fallgruppen des § 114 VwGO und prüft die Verhältnismäßigkeit. Der **Rechtsfolgen-Agent** bewertet, ob eine Ermessensreduzierung auf null vorliegt, ob die Behörde nach § 114 Satz 2 VwGO nachbessern kann und welcher Klageantrag erfolgversprechend ist. Die Befunde werden zu einer Gesamtbewertung verdichtet.

## Ablauf

### 1. Ist Ermessen eröffnet? ([§ 40 VwVfG](https://www.gesetze-im-internet.de/vwvfg/__40.html))

- Rechtsfolgenseite der Norm prüfen: „kann"/„darf" = Ermessen; „ist zu" = gebundene Entscheidung
- Abgrenzung zum **unbestimmten Rechtsbegriff** auf der Tatbestandsseite (Beurteilungsspielraum, nicht Ermessen)
- **Intendiertes Ermessen**: Regel-Ausnahme-Verhältnis, bei dem die Begründung des Regelfalls entbehrlich ist; nur der atypische Fall ist begründungsbedürftig

### 2. Ermessensfehler-Fallgruppen ([§ 114 VwGO](https://www.gesetze-im-internet.de/vwgo/__114.html))

#### Ermessensnichtgebrauch (Ermessensausfall)

Die Behörde erkennt ihren Spielraum nicht und behandelt die Sache als gebundene Entscheidung. Indiz: die Begründung enthält keine Abwägung. Verstoß zugleich gegen die Begründungspflicht ([§ 39 VwVfG](https://www.gesetze-im-internet.de/vwvfg/__39.html)).

#### Ermessensüberschreitung

Die Behörde wählt eine Rechtsfolge außerhalb der gesetzlichen Grenzen des Ermessens (§ 114 VwGO: „die gesetzlichen Grenzen des Ermessens überschritten").

#### Ermessensfehlgebrauch (Ermessensmissbrauch)

Das Ermessen wird in einer dem Zweck der Ermächtigung nicht entsprechenden Weise ausgeübt: sachfremde Erwägungen, unvollständige Tatsachengrundlage, Verstoß gegen Grundrechte oder den Gleichheitssatz.

### 3. Verhältnismäßigkeit

Jede Ermessensausübung muss verhältnismäßig sein: geeignet, erforderlich, angemessen. Die Verhältnismäßigkeit ist Teil der gesetzlichen Grenzen des Ermessens; ihr Verstoß ist gerichtlich voll überprüfbar.

### 4. Ermessensreduzierung auf null

Ist nach den Umständen nur eine einzige Entscheidung rechtmäßig (Selbstbindung der Verwaltung, Grundrechtsbetroffenheit, Gefahr für hochrangige Rechtsgüter), verdichtet sich das Ermessen zur gebundenen Entscheidung. Folge: Verpflichtungsklage statt Bescheidungsklage; das Gericht kann zum Erlass des konkreten VA verurteilen.

### 5. Heilung und Nachschieben ([§ 114 Satz 2 VwGO](https://www.gesetze-im-internet.de/vwgo/__114.html))

Die Behörde kann Ermessenserwägungen im verwaltungsgerichtlichen Verfahren **ergänzen**, nicht aber erstmals nachholen. Ein vollständiger Ermessensausfall ist nicht nach § 114 Satz 2 VwGO heilbar.

### 6. Rechtsfolge und Antrag

- Anfechtungsklage bei belastendem VA; Aufhebung wegen Rechtswidrigkeit
- Bescheidungsklage (§ 113 Abs. 5 Satz 2 VwGO) bei verbleibendem Ermessen
- Verpflichtungsklage bei Ermessensreduzierung auf null

## Quellen

### Statute

- [§ 40 VwVfG](https://www.gesetze-im-internet.de/vwvfg/__40.html) (Ermessen)
- [§ 39 VwVfG](https://www.gesetze-im-internet.de/vwvfg/__39.html) (Begründungspflicht)
- [§ 114 VwGO](https://www.gesetze-im-internet.de/vwgo/__114.html) (gerichtliche Kontrolle, Satz 2: Ergänzung)
- [§ 113 Abs. 5 VwGO](https://www.gesetze-im-internet.de/vwgo/__113.html) (Bescheidungs-/Verpflichtungsurteil)

### Kommentare

- Kopp / Schenke, VwGO, 30. Aufl. 2024, § 114
- Stelkens / Bonk / Sachs, VwVfG, 10. Aufl. 2023, § 40
- Maurer / Waldhoff, Allgemeines Verwaltungsrecht, 20. Aufl.

### Rechtsprechung

- BVerwG, Urt. v. 16.06.1997 – 3 C 22.96 (Ermessensreduzierung) `[unverifiziert – prüfen]`
- BVerwG, Urt. v. 23.10.2007 – 1 C 10.07 (Nachschieben von Ermessenserwägungen) `[unverifiziert – prüfen]`

## Ausgabeformat

```
ERMESSENSFEHLER-PRÜFUNG — <Mandat> — <Datum>

I.    Ermächtigungsgrundlage
      Norm:                           <§ … >
      Ermessen eröffnet:              [ja / nein – gebundene Entscheidung]
      Intendiertes Ermessen:          [ja / nein]

II.   Ermessensfehler-Fallgruppen
      Ermessensnichtgebrauch:         [+ / – / Begründungsmangel]
      Ermessensüberschreitung:        [+ / –]
      Ermessensfehlgebrauch:          [+ / – / sachfremde Erwägung <…>]

III.  Verhältnismäßigkeit
      Geeignet / erforderlich / angemessen:  <…>

IV.   Ermessensreduzierung auf null      [ja / nein]

V.    Heilung § 114 Satz 2 VwGO          [möglich / ausgeschlossen]

VI.   Klageantrag
      Anfechtung / Bescheidung / Verpflichtung:  <gewählt>

Empfehlung: <…>
```

## Risiken / typische Fehler

- **Ermessensnichtgebrauch übersehen** — eine fehlende Abwägung in der Begründung ist der häufigste, oft heilungsfeste Fehler.
- **Begründungsmangel mit Ermessensausfall verwechselt** — ein bloßer Begründungsmangel ist nach § 45 VwVfG heilbar, ein echter Ermessensausfall nicht.
- **Nachschieben von Ermessenserwägungen falsch beurteilt** — § 114 Satz 2 VwGO erlaubt nur Ergänzung, nicht erstmalige Ausübung.
- **Ermessensreduzierung auf null nicht erkannt** — dann ist Verpflichtungs- statt Bescheidungsklage geboten; ein zu enger Antrag verschenkt Rechtsschutz.
