---
name: prozesskostenhilfe-borghei
title: /prozessrecht:prozesskostenhilfe
description: Prüfung und Antrag auf Prozesskostenhilfe (PKH) – die drei Voraussetzungen Bedürftigkeit, hinreichende Erfolgsaussicht und fehlende Mutwilligkeit § 114 ZPO, Einsatz von Einkommen und Vermögen mit Ratenberechnung § 115 ZPO, Beiordnung eines Rechtsanwalts § 121 ZPO. Use when eine bedürftige Partei für einen Zivilprozess Prozesskostenhilfe beantragen will oder die Erfolgsaussichten eines PKH-Antrags zu beurteilen sind.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/prozessrecht/skills/prozesskostenhilfe
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: litigation
language: de
---

# /prozessrecht:prozesskostenhilfe

## Zweck

Prozesskostenhilfe (PKH) sichert den Zugang zum Recht für Parteien, die die Prozesskosten nicht aufbringen können (Art. 3, 20 GG – Rechtsschutzgleichheit). Sie hängt an **drei Voraussetzungen**: persönlich-wirtschaftlicher **Bedürftigkeit**, **hinreichender Erfolgsaussicht** und fehlender **Mutwilligkeit** (§ 114 ZPO). Liegen sie vor, übernimmt die Staatskasse die Kosten – ganz oder gegen Raten. Dieser Skill prüft die drei Voraussetzungen, berechnet einzusetzendes Einkommen und Vermögen und klärt die Anwaltsbeiordnung.

## Eingaben

- **Wirtschaftliche Verhältnisse** (Nettoeinkommen, Unterhaltspflichten, Wohnkosten, Vermögen)
- **Streitgegenstand** (Anspruch, Beweislage, Erfolgsaussichten der beabsichtigten Klage/Verteidigung)
- **Verfahrensart** (Anwaltszwang? sachliche Zuständigkeit AG/LG)
- **Belege** (Erklärung über persönliche und wirtschaftliche Verhältnisse – Formular PKHFV)
- **Gegenseite** (anwaltlich vertreten? Aussicht auf Vergleich?)
- **Bisherige Kostendeckung** (Rechtsschutzversicherung, vorrangige Hilfen)

## Sub-Agent-Architektur

Die Prüfung wird in drei gedankliche Prüfstränge zerlegt, die zusammengeführt werden. Ein erster Strang prüft die **Erfolgsaussicht und Mutwilligkeit** – ob die beabsichtigte Rechtsverfolgung bei summarischer Prüfung hinreichende Aussicht auf Erfolg bietet und nicht mutwillig ist (§ 114 Abs. 1 ZPO). Ein zweiter Strang berechnet die **Bedürftigkeit** – einzusetzendes Einkommen nach Abzug der Freibeträge und einzusetzendes Vermögen (§ 115 ZPO) sowie die daraus folgende Ratenhöhe oder ratenfreie Bewilligung. Ein dritter Strang klärt die **Beiordnung eines Rechtsanwalts** (§ 121 ZPO) und den Umfang der Kostenübernahme. Die Synthese fasst die Bewilligungschance zusammen und benennt die Mitwirkungs- und Mitteilungspflichten.

## Ablauf

### 1. Die drei Voraussetzungen ([§ 114 ZPO](https://www.gesetze-im-internet.de/zpo/__114.html))

- **Bedürftigkeit:** Die Partei kann die Kosten der Prozessführung nach ihren persönlichen und wirtschaftlichen Verhältnissen nicht, nur zum Teil oder nur in Raten aufbringen.
- **Hinreichende Erfolgsaussicht:** Bei **summarischer Prüfung** muss die Rechtsverfolgung/-verteidigung Aussicht auf Erfolg bieten; entscheidungserhebliche Tatsachen müssen schlüssig vorgetragen und beweisbar erscheinen. Schwierige, ungeklärte Rechtsfragen dürfen nicht zu Lasten der bedürftigen Partei vorab entschieden werden.
- **Keine Mutwilligkeit:** Mutwillig ist die Rechtsverfolgung, wenn eine **nicht bedürftige, verständige Partei** bei vernünftiger Würdigung von der Prozessführung absähe (§ 114 Abs. 2 ZPO).

### 2. Einsatz von Einkommen ([§ 115 ZPO](https://www.gesetze-im-internet.de/zpo/__115.html))

- Maßgeblich ist das **einzusetzende Einkommen**: vom Nettoeinkommen werden abgezogen Steuern/Sozialabgaben, **Freibeträge** für die Partei und unterhaltsberechtigte Angehörige, Wohnkosten und besondere Belastungen (§ 115 Abs. 1 ZPO).
- Aus dem verbleibenden Betrag werden **Monatsraten** bestimmt; übersteigen die Kosten voraussichtlich nicht vier Monatsraten, wird **ratenfreie** PKH bewilligt. Es sind höchstens **48 Monatsraten** zu zahlen.

### 3. Einsatz von Vermögen ([§ 115 Abs. 3 ZPO](https://www.gesetze-im-internet.de/zpo/__115.html))

- Die Partei hat ihr **Vermögen einzusetzen**, soweit dies zumutbar ist (§ 115 Abs. 3 ZPO i. V. m. § 90 SGB XII – Schonvermögen).
- Geschützt sind angemessener Hausrat, ein angemessenes Kfz bei Erwerbstätigkeit, selbst genutztes angemessenes Wohneigentum und ein Notgroschen.

### 4. Beiordnung eines Rechtsanwalts ([§ 121 ZPO](https://www.gesetze-im-internet.de/zpo/__121.html))

- Besteht **Anwaltszwang** (Landgericht, § 78 ZPO), wird der Partei ein Rechtsanwalt ihrer Wahl **beigeordnet** (§ 121 Abs. 1 ZPO).
- Ohne Anwaltszwang erfolgt die Beiordnung, wenn die Vertretung **erforderlich** erscheint oder der Gegner anwaltlich vertreten ist (§ 121 Abs. 2 ZPO).
- Der beigeordnete Anwalt rechnet gegenüber der Staatskasse ab; die Beiordnung beschränkt sich grundsätzlich auf eine Instanz.

### 5. Antrag und Verfahren

- Der Antrag ist beim **Prozessgericht** zu stellen, nebst der **Erklärung über die persönlichen und wirtschaftlichen Verhältnisse** (amtliches Formular) und Belegen.
- Bewilligung wirkt grundsätzlich **nicht rückwirkend**; daher Antrag vor der Kostenauslösung stellen. Über die Erfolgsaussicht entscheidet das Gericht nach Anhörung des Gegners.

### 6. Folgen, Überprüfung und Aufhebung

- Die Bewilligung befreit nicht von **gegnerischen Kosten** im Unterliegensfall (§ 123 ZPO).
- Das Gericht kann die Verhältnisse innerhalb von **vier Jahren** überprüfen (§ 120a ZPO); verbesserte Einkommens-/Vermögensverhältnisse sind **unaufgefordert mitzuteilen**.
- Bei falschen Angaben oder unterlassener Mitteilung droht **Aufhebung** der Bewilligung (§ 124 ZPO) und Nachzahlung.

## Risiken / typische Fehler

- **Erfolgsaussicht** zu optimistisch eingeschätzt: Bei fehlender hinreichender Erfolgsaussicht wird der Antrag zurückgewiesen; die summarische Prüfung darf die Hauptsache nicht vorwegnehmen.
- **Mutwilligkeit** übersehen: aussichtsreiche, aber für eine verständige Partei unwirtschaftliche Prozessführung (Bagatelle, vorrangiger einfacherer Weg).
- **Vermögen** nicht offengelegt oder Schonvermögensgrenzen verkannt – führt zur Ablehnung oder späteren Aufhebung.
- **Mitteilungspflicht** des § 120a ZPO verletzt: verbesserte Verhältnisse nicht angezeigt – Aufhebung und Rückforderung.

## Ausgabeformat

```
PROZESSKOSTENHILFE — <Verfahren> — <Datum>

I.    Erfolgsaussicht § 114      summarische Prüfung: [hinreichend? ja/nein]
      Mutwilligkeit               [mutwillig? ja/nein — Begründung]
II.   Bedürftigkeit § 115
      einzusetzendes Einkommen    Netto / Freibeträge / Wohnkosten = <…>
      Monatsrate                  <EUR>  oder  ratenfrei
      einzusetzendes Vermögen     Schonvermögen § 90 SGB XII: <…>
III.  Beiordnung § 121           Anwaltszwang? [ja/nein] → RA beigeordnet
IV.   Antrag                     Formular PKHFV + Belege; vor Kostenauslösung
V.    Folgen                     gegnerische Kosten § 123 / Überprüfung § 120a

Ergebnis: [PKH ratenfrei / mit Raten / abgelehnt] — <Begründung>
```

## Quellen

### Statute

- [§ 114 ZPO](https://www.gesetze-im-internet.de/zpo/__114.html) (Voraussetzungen: Bedürftigkeit, Erfolgsaussicht, keine Mutwilligkeit)
- [§ 115 ZPO](https://www.gesetze-im-internet.de/zpo/__115.html) (Einsatz von Einkommen und Vermögen, Ratenberechnung)
- [§ 121 ZPO](https://www.gesetze-im-internet.de/zpo/__121.html) (Beiordnung eines Rechtsanwalts)
- [§ 120a ZPO](https://www.gesetze-im-internet.de/zpo/__120a.html) (Überprüfung), [§ 123 ZPO](https://www.gesetze-im-internet.de/zpo/__123.html) (gegnerische Kosten), [§ 124 ZPO](https://www.gesetze-im-internet.de/zpo/__124.html) (Aufhebung)
- [§ 90 SGB XII](https://www.gesetze-im-internet.de/sgb_12/__90.html) (Schonvermögen)

### Kommentare

- Fischer, in: Musielak/Voit, ZPO, 22. Aufl. 2025, §§ 114 ff. Rn. 1 ff.
- Schultzky, in: Zöller, ZPO, 36. Aufl. 2025, § 114 Rn. 1 ff.

### Rechtsprechung

- Zur summarischen Erfolgsaussichtsprüfung (keine Vorwegnahme der Hauptsache) besteht gefestigte BVerfG-/BGH-Rechtsprechung (Aktenzeichen vor Zitat verifizieren) `[unverifiziert – prüfen]`
