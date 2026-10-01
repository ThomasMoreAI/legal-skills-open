---
name: patentverletzung-pruefung-borghei
title: /gewerblicher-rechtsschutz:patentverletzung-pruefung
description: Verletzungsprüfung eines Patents nach §§ 9, 14, 139, 140b, 140c PatG – Wirkung des Patents, Bestimmung des Schutzbereichs durch die Patentansprüche, wortsinngemäße vs. äquivalente Verletzung, Unterlassungs- und Schadensersatzanspruch, Auskunfts- und Besichtigungsanspruch. Use when zu prüfen ist, ob ein angegriffenes Erzeugnis oder Verfahren ein Patent verletzt und welche Ansprüche dem Patentinhaber zustehen.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/gewerblicher-rechtsschutz/skills/patentverletzung-pruefung
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: ip
language: de
---

# /gewerblicher-rechtsschutz:patentverletzung-pruefung

## Zweck

Die Patentverletzungsprüfung vergleicht die Merkmale des Patentanspruchs mit der angegriffenen Ausführungsform. Maßgeblich ist der **Schutzbereich** nach den Patentansprüchen, ausgelegt im Licht von Beschreibung und Zeichnungen. Erfasst werden die **wortsinngemäße** und die **äquivalente** Verletzung. Dieses Skill führt durch die Merkmalsanalyse, die Anspruchsprüfung und die Bewertung der Verteidigungseinwände.

## Eingaben

- Patentschrift (Anspruchssatz, Beschreibung, Zeichnungen, Erteilungsstand)
- Angegriffene Ausführungsform (Produkt, Verfahren, Belege, Muster)
- Rechtsstand des Patents (erteilt, Einspruch, Nichtigkeitsklage anhängig?)
- Benutzungshandlungen (Herstellen, Anbieten, Inverkehrbringen, Einführen, Gebrauchen)
- Verschulden / Kenntnis des Verletzers; Verletzungszeitraum

## Sub-Agent-Architektur

Vier gedankliche Rollen greifen ineinander. Ein **Merkmals-Agent** gliedert den Patentanspruch in einzelne Merkmale (Merkmalsanalyse) und ordnet die Ausführungsform zu. Ein **Auslegungs-Agent** bestimmt den Schutzbereich nach § 14 PatG und prüft zunächst die wortsinngemäße, dann die äquivalente Verletzung. Ein **Verteidigungs-Agent** prüft Bestandsangriffe (Nichtigkeitsklage, Stand der Technik) und den Formstein-Einwand. Ein **Anspruchs-Agent** leitet aus § 9, § 139, § 140b, § 140c PatG die Rechtsfolgen ab und erstellt das Verletzungsprotokoll. Der Auslegungs-Agent priorisiert stets die wortsinngemäße Prüfung; nur bei deren Verneinung wird die Äquivalenzprüfung durchlaufen.

## Ablauf

### 1. Wirkung des Patents § 9 PatG

- Allein der Patentinhaber darf die Erfindung benutzen. Verboten sind insbesondere **Herstellen, Anbieten, Inverkehrbringen, Gebrauchen, Einführen, Besitzen** des Erzeugnisses sowie das Anwenden des geschützten Verfahrens.
- Mittelbare Patentverletzung (§ 10 PatG) bei Lieferung wesentlicher Mittel.

### 2. Schutzbereich und Auslegung § 14 PatG

- Der Schutzbereich wird durch die **Patentansprüche** bestimmt; Beschreibung und Zeichnungen sind zur Auslegung heranzuziehen.
- Maßstab ist der Fachmann; Auslegung weder am reinen Wortlaut haftend noch über die Ansprüche hinausgehend.

### 3. Merkmalsanalyse und wortsinngemäße Verletzung

- Anspruch in einzelne Merkmale zerlegen.
- **Wortsinngemäße Verletzung**: Die Ausführungsform verwirklicht jedes Merkmal nach dem Wortsinn (Verständnis des Fachmanns).

### 4. Äquivalente Verletzung

- Ersetzt die Ausführungsform ein Merkmal durch ein abgewandeltes Mittel, liegt **äquivalente Verletzung** vor, wenn die drei Schneidmesser-Fragen bejaht werden: gleichwirkend, auffindbar, gleichwertig (am Sinngehalt des Anspruchs orientiert).
- **Formstein-Einwand**: Keine Äquivalenz, soweit die abgewandelte Ausführung zum freien Stand der Technik gehört.

### 5. Ansprüche § 139 PatG

- **Unterlassungsanspruch** bei Wiederholungs-/Erstbegehungsgefahr (§ 139 Abs. 1).
- **Schadensersatzanspruch** bei Vorsatz/Fahrlässigkeit (§ 139 Abs. 2) — drei Berechnungsmethoden: konkreter Schaden, Verletzergewinn, Lizenzanalogie.
- Vernichtung und Rückruf (§ 140a PatG).

### 6. Auskunft und Besichtigung

- **Auskunftsanspruch** über Herkunft und Vertriebsweg (§ 140b PatG).
- **Besichtigungsanspruch** zur Sicherung des Verletzungsnachweises (§ 140c PatG), oft im Wege der einstweiligen Verfügung.

### 7. Verteidigung und Verjährung

- Bestandsangriff durch **Nichtigkeitsklage** (§ 81 PatG) oder Einspruch; ggf. Aussetzung des Verletzungsverfahrens.
- **Verjährung** der Ansprüche nach § 141 PatG i.V.m. §§ 195, 199 BGB.

## Risiken / typische Fehler

- **Äquivalenz** ohne wortsinngemäße Vorprüfung behauptet — die Merkmalsanalyse muss zuerst den Wortsinn ausschließen.
- **Formstein-Einwand** übersehen — keine Äquivalenzverletzung im freien Stand der Technik.
- **Verjährung** nicht geprüft — § 141 PatG i.V.m. §§ 195, 199 BGB.
- **Nichtigkeitsklage** des Gegners nicht eingeplant — Aussetzungsrisiko und unberechtigte Verwarnung bei rechtsbeständigem Angriff.
- Schutzbereich allein am Wortlaut ohne Auslegung nach § 14 PatG bestimmt.

## Ausgabeformat

```
PATENTVERLETZUNG — PRÜFPROTOKOLL — <Mandant> — <Datum>

I.    Patent / Anspruch            <Az., Anspruch Nr., Rechtsstand>
II.   Merkmalsanalyse              M1 / M2 / M3 … : verwirklicht? [✓/✗]
III.  Schutzbereich § 14           Auslegung: <…>
IV.   Wortsinngemäße Verletzung    [ja / nein]  Begründung: <…>
V.    Äquivalente Verletzung       Schneidmesser-Fragen: <…>  Formstein: [greift/nein]
VI.   Benutzungshandlung § 9       [Herstellen/Anbieten/Inverkehrbringen/Einführen]
VII.  Ansprüche § 139              Unterlassung [✓]; SE-Methode: <Lizenzanalogie/…>
VIII. Auskunft § 140b / Besichtigung § 140c   [ja/nein]
IX.   Verteidigung / Verjährung    Nichtigkeitsklage: <…>; Verjährung: <…>

Hinweis: Erteilungs- und Rechtsstand des Patents tagesaktuell prüfen.
```

## Quellen

### Statute

- [§ 9 PatG](https://www.gesetze-im-internet.de/patg/__9.html) (Wirkung des Patents)
- [§ 14 PatG](https://www.gesetze-im-internet.de/patg/__14.html) (Schutzbereich / Auslegung)
- [§ 139 PatG](https://www.gesetze-im-internet.de/patg/__139.html) (Unterlassung und Schadensersatz)
- [§ 140b PatG](https://www.gesetze-im-internet.de/patg/__140b.html) (Auskunftsanspruch)
- [§ 140c PatG](https://www.gesetze-im-internet.de/patg/__140c.html) (Besichtigungsanspruch)
- [§§ 10, 140a, 141 PatG](https://www.gesetze-im-internet.de/patg/) (mittelbare Verletzung, Vernichtung, Verjährung)

### Kommentare

- Benkard, Patentgesetz, 12. Aufl. 2023
- Schulte, Patentgesetz, 11. Aufl. 2022
- BeckOK PatR (Online)

### Rechtsprechung

- BGH, Urt. v. 12.03.2002 – X ZR 168/00, GRUR 2002, 515 (Schneidmesser I) `[unverifiziert – prüfen]`
- BGH, Urt. v. 29.04.1986 – X ZR 28/85, GRUR 1986, 803 (Formstein) `[unverifiziert – prüfen]`
