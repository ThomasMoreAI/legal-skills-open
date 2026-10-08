---
name: sgb-ii-leistungsanspruch-borghei
title: /sozialrecht:sgb-ii-leistungsanspruch
description: Vollprüfung des Bürgergeld-Anspruchs nach SGB II – Erwerbsfähigkeit § 8, Hilfebedürftigkeit § 9, Bedarfsgemeinschaft § 7 Abs. 3, anrechenbares Einkommen §§ 11 ff., Vermögen § 12, Regelbedarf § 20, Kosten der Unterkunft § 22, Mehrbedarfe § 21, Leistungsminderungen §§ 31 ff. nach Bürgergeld-Reform 2023. Use when Mandantin einen Erstantrag, eine Bedarfsneuberechnung oder eine Bescheidkontrolle benötigt.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/sozialrecht/skills/sgb-ii-leistungsanspruch
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: social-security
language: de
---

# /sozialrecht:sgb-ii-leistungsanspruch

## Zweck

Bürgergeld nach SGB II ist die Existenzsicherung für erwerbsfähige Leistungsberechtigte. Der Anspruch hängt an fünf Hauptvoraussetzungen (§ 7 Abs. 1 SGB II), wird in der Bedarfsgemeinschaft horizontal berechnet (§ 7 Abs. 3 SGB II) und durch Einkommen / Vermögen reduziert (§§ 11, 12 SGB II). Dieser Skill prüft Anspruchsdurchgang Schritt für Schritt und macht Lücken sichtbar.

## Eingaben

- Antragstellerin / Antragsteller: Alter, Staatsangehörigkeit, gewöhnlicher Aufenthalt
- Haushaltszusammensetzung (Partner, Kinder mit Alter, sonstige Mitbewohner)
- Erwerbsfähigkeit (gesundheitliche Einschränkungen?)
- Einkommen aller BG-Mitglieder (brutto / netto, Quelle, Frequenz)
- Vermögen (Konto, Tagesgeld, Wertpapiere, Auto, Immobilie, Versicherungen)
- Wohnsituation (Eigentum / Miete, Kaltmiete, Nebenkosten, Heizung, Wohnfläche, Ort)
- Besondere Bedarfe (Schwangerschaft, Alleinerziehung, Erwerbstätigkeit, Behinderung, kostenaufwändige Ernährung)
- Bisherige Sanktionen / Leistungsminderungen, Eingliederungsvereinbarung

## Sub-Agent-Architektur

Researcher liefert SGB-II-Normen, Bürgergeld-Reform-Materialien (Karenzzeit, Schonvermögen) und BSG-Rechtsprechung zu Bedarfsgemeinschaft / KdU / Einkommen. Drafter erstellt strukturierte Anspruchsprüfung samt Bedarfsberechnung. Reviewer prüft Fristen, Mitwirkungspflichten und Vollständigkeit.

## Ablauf

### 1. Persönliche Anspruchsvoraussetzungen ([§ 7 Abs. 1 SGB II](https://www.gesetze-im-internet.de/sgb_2/__7.html))

| Voraussetzung | Norm | Prüfpunkte |
|---|---|---|
| Vollendung 15. Lj., Altersgrenze § 7a SGB II nicht erreicht | § 7 Abs. 1 S. 1 Nr. 1 | Geburtsdatum, Regelaltersgrenze § 7a |
| Erwerbsfähigkeit | § 7 Abs. 1 S. 1 Nr. 2 i.V.m. [§ 8 SGB II](https://www.gesetze-im-internet.de/sgb_2/__8.html) | Mindestens 3 h täglich auf dem allgemeinen Arbeitsmarkt einsatzfähig |
| Hilfebedürftigkeit | § 7 Abs. 1 S. 1 Nr. 3 i.V.m. [§ 9 SGB II](https://www.gesetze-im-internet.de/sgb_2/__9.html) | Bedarf > Einkommen + zumutbar einzusetzendes Vermögen |
| Gewöhnlicher Aufenthalt in DE | § 7 Abs. 1 S. 1 Nr. 4 i.V.m. § 30 SGB I | Lebensmittelpunkt, Daueraufenthalt |
| Kein Ausschluss | § 7 Abs. 1 S. 2 ff. | Insb. § 7 Abs. 1 S. 2 Nr. 2 (Unionsbürger ohne Aufenthaltsrecht zur Arbeitsuche) |

### 2. Bedarfsgemeinschaft ([§ 7 Abs. 3 SGB II](https://www.gesetze-im-internet.de/sgb_2/__7.html))

BG-Mitglieder (abschließende Aufzählung):

- erwerbsfähige Leistungsberechtigte
- Partner (Ehe, eingetragene Lebenspartnerschaft, Verantwortungs-/Einstehensgemeinschaft § 7 Abs. 3 Nr. 3 lit. c)
- unverheiratete Kinder unter 25 J. im Haushalt der Eltern, soweit eigene Bedarfsdeckung fehlt
- Eltern eines unverheirateten Kindes unter 15 J. (Sozialgeldfall)

**Achtung Mischhaushalte:** § 27 SGB XII bzw. § 19 SGB II — Trennung erforderlich, wenn ein Mitglied nicht erwerbsfähig oder vom Bürgergeld ausgeschlossen ist.

### 3. Bedarfsberechnung

Gesamtbedarf der BG ([§ 19 SGB II](https://www.gesetze-im-internet.de/sgb_2/__19.html)):

| Bedarf | Norm | Anmerkung |
|---|---|---|
| Regelbedarf | [§ 20 SGB II](https://www.gesetze-im-internet.de/sgb_2/__20.html) | Regelbedarfsstufen 1–6 (RBEG); jährliche Fortschreibung. **Stand prüfen.** |
| Mehrbedarf | [§ 21 SGB II](https://www.gesetze-im-internet.de/sgb_2/__21.html) | Werdende Mütter, Alleinerziehende, Behinderung mit § 49 SGB IX-Leistung, kostenaufw. Ernährung |
| Kosten der Unterkunft & Heizung | [§ 22 SGB II](https://www.gesetze-im-internet.de/sgb_2/__22.html) | Tatsächliche Aufwendungen, soweit angemessen |
| Einmalige Bedarfe | [§ 24 SGB II](https://www.gesetze-im-internet.de/sgb_2/__24.html) | Erstausstattung Wohnung, Bekleidung, Schwangerschaft, Klassenfahrten |

**Karenzzeit § 22 Abs. 1 S. 2 SGB II:** Im 1. Jahr werden tatsächliche KdU anerkannt; danach Angemessenheit nach schlüssigem Konzept (BSG, Urt. v. 22.09.2009 – B 4 AS 18/09 R `[unverifiziert – prüfen]`).

### 4. Anrechenbares Einkommen ([§§ 11–11b SGB II](https://www.gesetze-im-internet.de/sgb_2/__11.html))

- Bruttoeinkommen aller BG-Mitglieder
- Abzüge nach § 11b SGB II (Steuern, SV-Beiträge, Werbungskosten-Pauschale, Versicherungspauschale 30 EUR, Riester, KFZ-Haftpflicht, Kindergeld-Sonderregel § 11 Abs. 1 S. 5)
- **Erwerbstätigenfreibetrag § 11b Abs. 3 SGB II**: 100 EUR Grundfreibetrag plus gestaffelter Freibetrag (20 % / 30 % / 10 %).
- Nicht anrechenbar nach § 11a SGB II: bestimmte zweckbestimmte Einnahmen, Schmerzensgeld, ausgewählte Aufwandsentschädigungen.

### 5. Vermögen ([§ 12 SGB II](https://www.gesetze-im-internet.de/sgb_2/__12.html), [§ 12a SGB II](https://www.gesetze-im-internet.de/sgb_2/__12a.html))

**Karenzzeit § 12 Abs. 3 SGB II (Bürgergeld-Reform 2023):**

- Im 1. Jahr ist Vermögen anrechnungsfrei bis zur "Erheblichkeitsgrenze" (40.000 EUR Hauptperson + 15.000 EUR je weiteres BG-Mitglied)
- Nach der Karenzzeit: Schonbetrag 15.000 EUR je BG-Mitglied
- Geschütztes Vermögen § 12 Abs. 1 SGB II: angemessener Hausrat, angemessenes KFZ je erwerbsfähigem BG-Mitglied (Faustregel: bis 15.000 EUR Verkehrswert `[unverifiziert – prüfen aktuelle BSG-Linie]`), selbstgenutzte angemessene Immobilie, Altersvorsorge nach § 12 Abs. 1 S. 1 Nr. 3, 4 SGB II
- § 12a SGB II: Inanspruchnahme vorrangiger Leistungen (Wohngeld, Kinderzuschlag, Unterhaltsvorschuss)

### 6. Leistungsminderung / Sanktionen ([§§ 31, 31a, 31b SGB II](https://www.gesetze-im-internet.de/sgb_2/__31.html))

Nach BVerfG, Urt. v. 05.11.2019 – 1 BvL 7/16, BVerfGE 152, 68 = NJW 2019, 3703 (Sanktionsurteil, [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BVerfG&Datum=05.11.2019&Aktenzeichen=1%20BvL%207/16)) und Bürgergeld-Reform:

- Pflichtverletzungen § 31 SGB II: Verweigerung zumutbarer Arbeit / Maßnahme, Pflichtverstoß gegen Kooperationsplan
- Leistungsminderung gestaffelt: 10 % / 20 % / 30 % (§ 31a SGB II), maximal 30 % bei mehrfacher Pflichtverletzung
- Härtefall § 31a Abs. 5 SGB II
- Meldeversäumnis § 32 SGB II: 10 % für 1 Monat

### 7. Rechtsfolge — konkrete Bedarfsberechnung

| Schritt | Inhalt |
|---|---|
| 1 | Gesamtbedarf BG (Σ Regelbedarfe + Mehrbedarfe + KdU) |
| 2 | abzgl. anrechenbares Einkommen (horizontale Verteilung § 9 Abs. 2 SGB II) |
| 3 | abzgl. einsetzbares Vermögen |
| 4 | = monatlicher Leistungsanspruch |

Bei Hilfebedürftigkeit < 0 EUR → kein Anspruch.

### 8. Mitwirkung und Antrag

- [§ 37 SGB II](https://www.gesetze-im-internet.de/sgb_2/__37.html): Antragserfordernis, Antrag wirkt auf den 1. des Monats zurück
- [§ 60 SGB I](https://www.gesetze-im-internet.de/sgb_1/__60.html): Angabe von Tatsachen; Vorlage Bescheinigungen
- Bewilligungszeitraum § 41 SGB II (regelmäßig 12 Monate)

## Quellen und Zitierweise

Verbindlich: [`../../references/zitierweise.md`](../../references/zitierweise.md).

### Statute

- [§ 7 SGB II](https://www.gesetze-im-internet.de/sgb_2/__7.html), [§ 8](https://www.gesetze-im-internet.de/sgb_2/__8.html), [§ 9](https://www.gesetze-im-internet.de/sgb_2/__9.html), [§ 11](https://www.gesetze-im-internet.de/sgb_2/__11.html), [§ 11a](https://www.gesetze-im-internet.de/sgb_2/__11a.html), [§ 11b](https://www.gesetze-im-internet.de/sgb_2/__11b.html), [§ 12](https://www.gesetze-im-internet.de/sgb_2/__12.html), [§ 19](https://www.gesetze-im-internet.de/sgb_2/__19.html), [§ 20](https://www.gesetze-im-internet.de/sgb_2/__20.html), [§ 21](https://www.gesetze-im-internet.de/sgb_2/__21.html), [§ 22](https://www.gesetze-im-internet.de/sgb_2/__22.html), [§ 31 ff.](https://www.gesetze-im-internet.de/sgb_2/__31.html), [§ 37](https://www.gesetze-im-internet.de/sgb_2/__37.html), [§ 41](https://www.gesetze-im-internet.de/sgb_2/__41.html) SGB II
- [§ 60 SGB I](https://www.gesetze-im-internet.de/sgb_1/__60.html); [§ 66 SGB I](https://www.gesetze-im-internet.de/sgb_1/__66.html)

### Kommentare

- Knickrehm/Hahn, in: Kassler Kommentar Sozialversicherungsrecht, Stand 2024, § 7 SGB II Rn. … (Bedarfsgemeinschaft)
- Geiger, in: LPK-SGB II, 8. Aufl. 2024, § 22 Rn. … (Kosten der Unterkunft, Karenzzeit)
- Söhngen, in: jurisPK-SGB II, 6. Aufl. 2023, § 12 Rn. … (Vermögen nach Bürgergeld-Reform)
- Aubel, in: BeckOK SozR, § 11 SGB II Rn. … (anrechenbares Einkommen)

### Rechtsprechung (`[unverifiziert – prüfen in juris / SozR]`)

1. BVerfG, Urt. v. 05.11.2019 – 1 BvL 7/16, BVerfGE 152, 68 (Sanktionsregime SGB II)
2. BSG, Urt. v. 22.09.2009 – B 4 AS 18/09 R, BSGE 104, 192 (schlüssiges Konzept KdU)
3. BSG, Urt. v. 11.07.2019 – B 14 AS 44/18 R (Bedarfsgemeinschaft / Einstehensgemeinschaft)
4. BSG, Urt. v. 12.10.2016 – B 4 AS 60/15 R (Vermögensschutz angemessenes Kfz)

## Ausgabeformat

```
PRÜFUNG BÜRGERGELD-ANSPRUCH — <Mandantin/Mandant, anonymisiert>
Stand: <Datum> — Risikoeinstufung: 🟢/🟡/🔴

A. Sachverhalt (anonymisiert)
   <…>

B. Anspruchsprüfung § 7 SGB II
   1. Vollendung 15. Lj. / Altersgrenze § 7a — ✅/⚠️/❌
   2. Erwerbsfähigkeit § 8 — ✅/⚠️/❌
   3. Hilfebedürftigkeit § 9 — (siehe Berechnung E)
   4. Gewöhnlicher Aufenthalt — ✅/⚠️/❌
   5. Kein Ausschluss § 7 Abs. 1 S. 2 — ✅/⚠️/❌

C. Bedarfsgemeinschaft § 7 Abs. 3
   Mitglieder: <…>

D. Bedarf
   Regelbedarf:    <…> EUR
   Mehrbedarf § 21: <…> EUR
   KdU § 22:       <…> EUR  (Karenzzeit ja/nein)
   Summe Bedarf:   <…> EUR

E. Einkommen / Vermögen
   Anrechenbares Einkommen: <…> EUR (Berechnung § 11b)
   Vermögen:               <…> EUR (Schonbetrag § 12 / Karenzzeit § 12 Abs. 3)

F. Leistungsanspruch
   Bedarf − Einkommen − einsetzbares Vermögen = <…> EUR/Monat
   ⇒ Anspruch besteht / besteht nicht / besteht teilweise

G. Verfahrenshinweise
   - Antrag § 37 SGB II beim örtlich zuständigen Jobcenter
   - Mitwirkung § 60 SGB I
   - Bewilligungszeitraum § 41 SGB II
   - Ggf. vorrangige Leistungen § 12a (Wohngeld / Kinderzuschlag)

H. Risiken / offene Punkte
   - <…>

I. Quellenverzeichnis
   <Statute / Kommentare / Rechtsprechung mit Markern>
```

## Beispiele

### Beispiel (gekürzter Auszug, Gutachtenstil)

> A. ist 38 Jahre alt, deutsche Staatsangehörige, erwerbsfähig im Sinne des § 8 SGB II. Sie lebt mit ihrem Partner B. (1.450 EUR netto aus abhängiger Beschäftigung) sowie zwei gemeinsamen Kindern (10 und 14 Jahre) in einer 90 m²-Mietwohnung (Bruttokaltmiete 900 EUR, Heizung 110 EUR).
>
> **I. Persönliche Voraussetzungen.** Nach § 7 Abs. 1 S. 1 Nr. 1 SGB II liegt A. zwischen Vollendung des 15. Lj. und der Altersgrenze § 7a. Erwerbsfähigkeit (§ 8 SGB II) ist gegeben — keine gesundheitlichen Einschränkungen vorgetragen. Gewöhnlicher Aufenthalt (§ 30 SGB I) im Bundesgebiet. Ausschlussgründe des § 7 Abs. 1 S. 2 SGB II sind nicht ersichtlich.
>
> **II. Bedarfsgemeinschaft.** B. ist Partner i.S.d. § 7 Abs. 3 Nr. 3 lit. a SGB II; die Kinder fallen unter § 7 Abs. 3 Nr. 4 SGB II.
>
> **III. Bedarf.** Regelbedarfsstufe 2 für A. und B. (je …) zzgl. Regelbedarf der Kinder (Stufen 4 und 5 je …); KdU nach § 22 Abs. 1 SGB II in Karenzzeit (§ 22 Abs. 1 S. 2 SGB II) anerkannt in tatsächlicher Höhe.
>
> **IV. Einkommen.** Aus B.s Erwerbstätigkeit ist nach § 11b SGB II der Grundfreibetrag von 100 EUR sowie der gestaffelte Freibetrag (20 % bis 1.000 EUR, 30 % bis 1.200 EUR) abzuziehen …
>
> **V. Ergebnis.** Es besteht voraussichtlich (Risiko 🟡 wegen offener Vermögensprüfung Tagesgeld) ein anteiliger Bürgergeld-Anspruch …

## Risiken / typische Fehler

- **Karenzzeit verwechselt:** § 22 (Unterkunft) und § 12 Abs. 3 (Vermögen) haben jeweils eigene 1-Jahres-Karenzregeln. Prüfen, ob es sich um den ersten Bewilligungszeitraum handelt.
- **Bedarfsgemeinschaft überdehnt:** WGs, Wohnzweck-Gemeinschaften und Pflege-Verhältnisse sind **keine** BG. Indizien des § 7 Abs. 3a SGB II prüfen.
- **Sanktionsregime veraltet:** Pre-Bürgergeld-Reform-Quoten (60 %, 100 %) sind nicht mehr anwendbar. Maximal 30 % (§ 31a SGB II) nach BVerfG-Vorgabe.
- **Kindergeld-Anrechnung:** § 11 Abs. 1 S. 5 SGB II — Kindergeld ist Einkommen des Kindes, soweit dort zur Bedarfsdeckung benötigt.
- **§ 12a SGB II übersehen:** Wohngeld, Kinderzuschlag, Unterhaltsvorschuss sind vorrangig. Jobcenter weist regelmäßig darauf hin (Erstattungspflicht).
- **Mitwirkungspflicht ignoriert:** § 60 SGB I — fehlende Unterlagen können zu Versagung (§ 66 SGB I) führen.
