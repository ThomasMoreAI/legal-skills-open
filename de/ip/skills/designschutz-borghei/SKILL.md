---
name: designschutz-borghei
title: /gewerblicher-rechtsschutz:designschutz
description: Prüfung der Schutzvoraussetzungen eines eingetragenen Designs nach §§ 2, 6, 11, 27 DesignG – Neuheit und Eigenart, Neuheitsschonfrist, Anmeldung beim DPMA, Schutzdauer, Nichtigkeit sowie Abgrenzung Designschutz vs. Markenschutz. Use when ein Mandant ein Produktdesign anmelden oder ein bestehendes eingetragenes Design auf Bestand und Verletzung prüfen will.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/gewerblicher-rechtsschutz/skills/designschutz
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: ip
language: de
---

# /gewerblicher-rechtsschutz:designschutz

## Zweck

Das eingetragene Design (früher „Geschmacksmuster") schützt die Erscheinungsform eines Erzeugnisses. Anders als die Marke wird es ungeprüft eingetragen — Neuheit und Eigenart prüft das DPMA **nicht** vorab. Der Bestand entscheidet sich erst im Nichtigkeits- oder Verletzungsstreit. Dieses Skill prüft die materiellen Schutzvoraussetzungen, die Anmeldung und grenzt den Designschutz vom Markenschutz ab.

## Eingaben

- Erzeugnis / Produktabbildungen (Ansichten, Wiedergaben)
- Erste Offenbarung (Messe, Katalog, Online-Shop) mit Datum
- Vorbekannter Formenschatz / Wettbewerberprodukte
- Beabsichtigter Schutzbereich (DE / Gemeinschaftsgeschmacksmuster EU)
- Verhältnis zu Marke / technischer Funktion des Produkts

## Sub-Agent-Architektur

Drei gedankliche Rollen arbeiten zusammen. Ein **Neuheits-Agent** recherchiert den vorbekannten Formenschatz und prüft, ob ein identisches Design vor dem Anmeldetag offenbart wurde, einschließlich der Neuheitsschonfrist. Ein **Eigenart-Agent** beurteilt aus Sicht des informierten Benutzers den Gesamteindruck und den Gestaltungsspielraum des Entwerfers. Ein **Strategie-Agent** entscheidet über Anmeldeform, Sammelanmeldung, Schutzgebiet und die Abgrenzung zu Marken- oder Patentschutz und erstellt das Prüfprotokoll. Bei Spannung zwischen Neuheit (objektiv) und Eigenart (Gesamteindruck) priorisiert der Strategie-Agent die schwächere Voraussetzung als Risikohinweis.

## Ablauf

### 1. Schutzvoraussetzungen § 2 DesignG

- **Neuheit** (§ 2 Abs. 2 DesignG): kein identisches Design vor dem Anmeldetag offenbart; Unterschiede nur in unwesentlichen Einzelheiten sind unbeachtlich.
- **Eigenart** (§ 2 Abs. 3 DesignG): Der Gesamteindruck beim informierten Benutzer unterscheidet sich von dem vorbekannter Designs; der Gestaltungsspielraum des Entwerfers wird berücksichtigt.
- Ausschluss: ausschließlich **technisch bedingte Erscheinungsmerkmale** (§ 3 Abs. 1 Nr. 1 DesignG) und Verbindungselemente.

### 2. Neuheitsschonfrist § 6 DesignG

- Eigene Offenbarungen des Entwerfers in den **12 Monaten** vor dem Anmeldetag sind unschädlich.
- Offenbarungen Dritter oder vor Beginn der Schonfrist sind **neuheitsschädlich**.

### 3. Anmeldung beim DPMA § 11 DesignG

- Antrag mit Wiedergabe des Designs und Angabe der Erzeugnisse.
- **Sammelanmeldung** mehrerer Designs einer Warenklasse (Locarno-Klassifikation) möglich.
- Aufschiebung der Bekanntmachung (bis 30 Monate) zur Geheimhaltung möglich.
- Anmeldetag begründet den Zeitrang.

### 4. Schutzdauer § 27 DesignG

- Schutzdauer **bis zu 25 Jahre** ab Anmeldetag, in Fünfjahresabschnitten gegen Aufrechterhaltungsgebühr.

### 5. Nichtigkeit

- Fehlende Neuheit oder Eigenart führt zur **Nichtigkeit** (§ 33 DesignG) — feststellbar im Antrags- oder Verletzungsverfahren.
- Da keine Vorprüfung erfolgt, ist die eigene Recherche des Formenschatzes vor Anmeldung zentral.

### 6. Designschutz vs. Markenschutz

- **Design** schützt die Erscheinungsform unabhängig von Herkunftsfunktion, zeitlich begrenzt (max. 25 Jahre).
- **Marke** schützt die Herkunftsfunktion, zeitlich unbegrenzt verlängerbar, setzt aber Unterscheidungskraft voraus.
- 3D-Formen können kumulativ als 3D-Marke und als Design geschützt werden; technische Formen scheiden bei beiden aus.

## Risiken / typische Fehler

- **Neuheitsschädliche Vorveröffentlichung** durch eigenen Online-Shop oder Messe vor Beginn der Neuheitsschonfrist § 6 DesignG.
- **Eigenart** verneint, weil der Gesamteindruck dem vorbekannten Formenschatz entspricht — Nichtigkeit nach § 2 DesignG.
- **Technische Funktion**: ausschließlich technisch bedingte Erscheinungsmerkmale sind nicht schutzfähig.
- **Schutzdauer / Aufrechterhaltung** versäumt — Erlöschen nach § 27 DesignG.
- **Verwechslung mit Markenschutz** — Design verleiht keinen Herkunftsschutz, eine zusätzliche Marke kann nötig sein.

## Ausgabeformat

```
DESIGNSCHUTZ — PRÜFPROTOKOLL — <Mandant> — <Datum>

I.    Erzeugnis / Wiedergaben      <Ansichten, Locarno-Klasse>
II.   Neuheit § 2 Abs. 2           [✓ / 🟡 / ✗]  Vorbekannter Formenschatz: <…>
III.  Eigenart § 2 Abs. 3          Gesamteindruck informierter Benutzer: <…>
IV.   Neuheitsschonfrist § 6       Erste Offenbarung: <Datum>  innerhalb 12 Mon.: [✓/✗]
V.    Technische Bedingtheit § 3   [keine / teilweise / ausschließlich]
VI.   Anmeldung § 11               DPMA / EUIPO; Sammelanmeldung: [ja/nein]; Zeitrang: <…>
VII.  Schutzdauer § 27             max. 25 Jahre; nächste Gebühr: <Datum>
VIII. Abgrenzung Design/Marke      Empfehlung: <…>

Hinweis: Eingetragene Designs werden nicht auf Neuheit/Eigenart vorgeprüft.
```

## Quellen

### Statute

- [§ 2 DesignG](https://www.gesetze-im-internet.de/geschmmg_2004/__2.html) (Neuheit und Eigenart)
- [§ 6 DesignG](https://www.gesetze-im-internet.de/geschmmg_2004/__6.html) (Neuheitsschonfrist)
- [§ 11 DesignG](https://www.gesetze-im-internet.de/geschmmg_2004/__11.html) (Anmeldung)
- [§ 27 DesignG](https://www.gesetze-im-internet.de/geschmmg_2004/__27.html) (Schutzdauer)
- [§ 33 DesignG](https://www.gesetze-im-internet.de/geschmmg_2004/__33.html) (Nichtigkeit)
- [Verordnung (EG) Nr. 6/2002 (GGV)](https://eur-lex.europa.eu/eli/reg/2002/6/oj) (Gemeinschaftsgeschmacksmuster)

### Kommentare

- Eichmann / Jestaedt / Fink / Meiser, DesignG / GGV, 6. Aufl. 2023
- Günther / Beyerlein, DesignG, 4. Aufl. 2021
- BeckOK DesignG (Online)
