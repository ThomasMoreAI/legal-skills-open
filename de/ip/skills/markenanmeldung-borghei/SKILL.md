---
name: markenanmeldung-borghei
title: /gewerblicher-rechtsschutz:markenanmeldung
description: Prüfung der Eintragungsfähigkeit und Anmeldestrategie einer Marke nach §§ 3, 8, 9, 32, 47 MarkenG – markenfähige Zeichen, absolute und relative Schutzhindernisse, Anmeldung beim DPMA, Waren- und Dienstleistungsverzeichnis (Nizza), Schutzdauer. Use when ein Mandant ein Zeichen als Marke anmelden will und Eintragungsfähigkeit, Klassifizierung und Anmeldestrategie zu klären sind.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/gewerblicher-rechtsschutz/skills/markenanmeldung
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: ip
language: de
---

# /gewerblicher-rechtsschutz:markenanmeldung

## Zweck

Vor jeder Markenanmeldung steht die Doppelprüfung: Ist das Zeichen überhaupt **markenfähig** und frei von **absoluten Schutzhindernissen**, und kollidiert es mit **älteren Rechten** (relative Schutzhindernisse)? Eine Anmeldung ohne diese Prüfung verbrennt Gebühren, erzeugt löschungsreife Marken und provoziert Widersprüche oder Abmahnungen Dritter. Dieses Skill strukturiert die Eintragungsprüfung und die Anmeldestrategie beim DPMA.

## Eingaben

- Zeichen (Wortmarke, Wort-/Bildmarke, Bildmarke, 3D-Form, Farbe, Klang)
- Beabsichtigte Waren und Dienstleistungen (für Nizza-Klassifikation)
- Geografischer Schutzbereich (DE / EU-Unionsmarke / IR-Marke)
- Branche und Verkehrskreise (Fachpublikum vs. Endverbraucher)
- Vorhandene eigene Kennzeichen / Voranmeldungen
- Budget und Zeithorizont (Beschleunigung möglich)

## Sub-Agent-Architektur

Die Bearbeitung verteilt sich auf vier gedankliche Rollen, die nacheinander arbeiten. Ein **Recherche-Agent** ermittelt das Zeichen, die Waren/Dienstleistungen und führt die Identitäts- und Ähnlichkeitsrecherche in DPMAregister und EUIPO durch. Ein **Prüf-Agent** subsumiert die Markenfähigkeit nach § 3 MarkenG und die absoluten Schutzhindernisse nach § 8 MarkenG. Ein **Kollisions-Agent** bewertet die relativen Schutzhindernisse nach § 9 MarkenG (ältere Marken, Verwechslungsgefahr). Ein **Strategie-Agent** wählt Markenform, Klassen, Schutzgebiet und Anmeldeweg und erstellt das Anmeldeprotokoll. Konflikte zwischen Prüf- und Kollisions-Agent (z. B. schwache Kennzeichnungskraft trotz Eintragbarkeit) werden im Strategie-Agent aufgelöst.

## Ablauf

### 1. Markenfähigkeit § 3 MarkenG

- Abstrakte Unterscheidungseignung: Kann das Zeichen Waren/Dienstleistungen eines Unternehmens von denen anderer unterscheiden?
- Zulässige Markenformen: Wörter, Namen, Abbildungen, Buchstaben, Zahlen, Hörzeichen, 3D-Gestaltungen, Farben.
- Ausschluss reiner Warenform (§ 3 Abs. 2 MarkenG): durch Art der Ware bedingt, technisch notwendig, wertbestimmend.

### 2. Absolute Schutzhindernisse § 8 MarkenG

- **Fehlende Unterscheidungskraft** (§ 8 Abs. 2 Nr. 1): konkret für die beanspruchten Waren/Dienstleistungen.
- **Beschreibende Angabe / Freihaltebedürfnis** (§ 8 Abs. 2 Nr. 2): Art, Beschaffenheit, geografische Herkunft, Bestimmung.
- **Gattungsbezeichnung** (Nr. 3), **Täuschung** (Nr. 4), **Verstoß gegen öffentliche Ordnung** (Nr. 5).
- **Verkehrsdurchsetzung** § 8 Abs. 3 MarkenG kann Hindernis Nr. 1–3 überwinden.

### 3. Relative Schutzhindernisse § 9 MarkenG

- Ältere identische oder ähnliche Marke + Waren-/Dienstleistungsähnlichkeit = **Verwechslungsgefahr**.
- Diese werden nicht von Amts wegen geprüft, sondern nur auf **Widerspruch** des Inhabers der älteren Marke. Eigene Recherche ist daher Pflicht.
- Bekannte Marke: erweiterter Schutz auch außerhalb der Warenähnlichkeit.

### 4. Waren- und Dienstleistungsverzeichnis

- Klassifizierung nach **Nizza-Klassifikation** (45 Klassen).
- Präzise, nicht zu breite Formulierung — überbreite Verzeichnisse erhöhen Benutzungsdruck und Kollisionsrisiko.

### 5. Anmeldung beim DPMA § 32 MarkenG

- Antrag mit Angaben zur Person, Wiedergabe der Marke, Waren-/Dienstleistungsverzeichnis.
- Anmeldetag begründet den Zeitrang (Priorität).
- Gebühren (Grundgebühr + Klassengebühren); beschleunigte Prüfung möglich.

### 6. Schutzdauer und Verlängerung § 47 MarkenG

- Schutzdauer **10 Jahre** ab Anmeldetag, beliebig oft um 10 Jahre verlängerbar.
- Verlängerung gegen Gebühr; Fristversäumnis führt zum Schutzverlust.

### 7. Benutzungspflicht

- Nach Ablauf der **Benutzungsschonfrist von 5 Jahren** (§ 25, § 26 MarkenG) droht Verfall bei Nichtbenutzung.

## Risiken / typische Fehler

- **Beschreibende Angabe** als Wortmarke angemeldet — Zurückweisung nach § 8 Abs. 2 Nr. 2 MarkenG.
- **Verwechslungsgefahr** mit älterer Marke übersehen — Widerspruch und Löschung nach § 9 MarkenG.
- **Bösgläubige Anmeldung** (Sperrmarke ohne Benutzungsabsicht) — Nichtigkeit und Schadensersatzrisiko.
- **Benutzungspflicht** nicht eingeplant — überbreites Verzeichnis wird nach 5 Jahren angreifbar.
- **Schutzdauer / Verlängerungsfrist** versäumt — Marke erlischt nach § 47 MarkenG.
- **Warenform** als 3D-Marke trotz technischer Bedingtheit (§ 3 Abs. 2) — nicht markenfähig.

## Ausgabeformat

```
MARKENANMELDUNG — PRÜFPROTOKOLL — <Mandant> — <Datum>

I.    Zeichen / Markenform        [Wort / Wort-Bild / Bild / 3D / Farbe / Klang]
II.   Markenfähigkeit § 3          [✓ / 🟡 / ✗]  Begründung: <…>
III.  Absolute Hindernisse § 8     Unterscheidungskraft / Freihaltebedürfnis: <…>
IV.   Relative Hindernisse § 9     Recherche DPMAregister/EUIPO: <Treffer / frei>
                                   Verwechslungsgefahr: [hoch / mittel / gering]
V.    Waren/Dienstleistungen       Nizza-Klassen: <…>
VI.   Anmeldung § 32               DPMA / EUIPO / IR; Zeitrang: <Datum>
VII.  Schutzdauer § 47             10 Jahre ab Anmeldung; Verlängerung: <Datum>
VIII. Strategie-Empfehlung         <Markenform, Klassen, Schutzgebiet, Beschleunigung>

Hinweis: Rechercheergebnisse zu älteren Rechten sind tagesaktuell zu prüfen.
```

## Quellen

### Statute

- [§ 3 MarkenG](https://www.gesetze-im-internet.de/markeng/__3.html) (markenfähige Zeichen)
- [§ 8 MarkenG](https://www.gesetze-im-internet.de/markeng/__8.html) (absolute Schutzhindernisse)
- [§ 9 MarkenG](https://www.gesetze-im-internet.de/markeng/__9.html) (relative Schutzhindernisse)
- [§ 32 MarkenG](https://www.gesetze-im-internet.de/markeng/__32.html) (Anmeldung)
- [§ 47 MarkenG](https://www.gesetze-im-internet.de/markeng/__47.html) (Schutzdauer / Verlängerung)
- [§§ 25, 26 MarkenG](https://www.gesetze-im-internet.de/markeng/) (Benutzungspflicht)
- [Verordnung (EU) 2017/1001 (UMV)](https://eur-lex.europa.eu/eli/reg/2017/1001/oj) (Unionsmarke)

### Kommentare

- Ströbele / Hacker, MarkenG, 14. Aufl. 2023
- Ingerl / Rohnke, Markengesetz, 4. Aufl. 2022
- BeckOK MarkenG (Online)
