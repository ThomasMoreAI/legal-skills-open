---
name: versicherungsfall-deckungspruefung-borghei
title: /versicherungsrecht:versicherungsfall-deckungspruefung
description: Dreistufige Deckungsprüfung im VVG – Versicherungsfall unter die AVB-Leistungsbeschreibung, kein Risikoausschluss, keine Leistungsfreiheit; AVB-Auslegung nach Empfängerhorizont des durchschnittlichen Versicherungsnehmers, Unklarheitenregel § 305c Abs. 2 BGB, AGB-Kontrolle §§ 307 ff. BGB. Use when ein Versicherer die Eintrittspflicht ablehnt oder eine Klausel der Allgemeinen Versicherungsbedingungen streitig ist (Wohngebäude, Hausrat, Berufsunfähigkeit, Rechtsschutz, Kasko).
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/versicherungsrecht/skills/versicherungsfall-deckungspruefung
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: insurance
language: de
---

# /versicherungsrecht:versicherungsfall-deckungspruefung

## Zweck

Der Skill prüft die Eintrittspflicht des Versicherers in **drei Stufen**: (1) Fällt das streitige Ereignis unter die Leistungsbeschreibung der AVB? (2) Greift ein Risikoausschluss? (3) Ist der Versicherer wegen Anzeigepflicht- oder Obliegenheitsverletzung leistungsfrei? Die AVB-Auslegung erfolgt nach dem Empfängerhorizont des durchschnittlichen Versicherungsnehmers; Unklarheiten gehen nach § 305c Abs. 2 BGB zu Lasten des Verwenders. Damit lassen sich Deckungsablehnungen außergerichtlich oder im Deckungsprozess strukturiert angreifen bzw. verteidigen.

## Eingaben

- Versicherungssparte (Wohngebäude / Hausrat / Berufsunfähigkeit / Rechtsschutz / Kasko / Haftpflicht / sonstige)
- Vertragsdaten (Versicherer, Beginn, AVB-Fassung mit Stand)
- streitige AVB-Klausel im Wortlaut
- Schadenhergang / Versicherungsfall (Datum, Ort, Ablauf, beteiligte Personen)
- Ablehnungsschreiben des Versicherers (Datum, Begründungstopoi)
- Korrespondenzstand, Schadennummer, ggf. Sachverständigengutachten

## Sub-Agent-Architektur

Researcher liefert VVG-/BGB-Statute, BGH IV. ZS-Rspr. zur AVB-Auslegung und zur Unklarheitenregel sowie Kommentarstellen (Prölss/Martin, MüKoVVG, BeckOK VVG). Drafter prüft die drei Stufen im Gutachtenstil, entwirft das Anspruchsschreiben oder den Klageschriftsatz und stuft das Risiko ein. Reviewer prüft Belehrungspflichten, Fristen (§ 8, § 21 VVG, § 124 BGB, §§ 195, 199 BGB), AGB-Kontrolle und ob die VVG-2008-Rechtslage durchgehalten ist.

## Ablauf

### 1. Sparten- und Vertragsbestimmung

Versicherungssparte, AVB-Fassung mit Stand, Versicherungsbeginn und Versicherungsumfang konkret benennen. Bei Altverträgen vor 01.01.2008: Übergangsregelungen (Art. 1 EGVVG) prüfen; das neue VVG gilt seit 01.01.2008 grundsätzlich auch für Altverträge.

### 2. Stufe I — Versicherungsfall unter die Leistungsbeschreibung

Positive Risikoabgrenzung: Bestimmt der Versicherungsschein iVm den AVB das streitige Ereignis als versichertes Risiko? Wortlaut der Leistungsbeschreibung zitieren und auslegen nach dem Verständnis eines **durchschnittlichen Versicherungsnehmers** ohne versicherungsrechtliche Sonderkenntnisse, der die AVB aufmerksam durchsieht und ihren Sinnzusammenhang würdigt (st. Rspr. BGH IV. ZS).

Beispiele:
- Wohngebäude (VGB): Brand, Blitzschlag, Explosion, Leitungswasser, Sturm/Hagel — Leitungswasser nur, wenn aus "Zu- oder Ableitungsrohren der Wasserversorgung" bestimmungswidrig austretend
- Hausrat: Diebstahl, Einbruchdiebstahl iSv § 6 VHB; einfacher Diebstahl meist nicht versichert
- Berufsunfähigkeit (BU): bedingungsgemäße Berufsunfähigkeit, regelmäßig 50 % außerstande, den zuletzt ausgeübten Beruf auszuüben, voraussichtlich auf Dauer (mind. 6 Monate)
- Rechtsschutz (ARB): Rechtsschutzfall iSv § 4 ARB; Verstoßprinzip — der erste tatsächliche oder behauptete Verstoß löst Versicherungsfall aus
- Kasko (AKB): Beschädigung, Zerstörung, Verlust durch unmittelbare Einwirkung eines Ereignisses iSv A.2.2 AKB

### 3. Stufe II — Risikoausschluss

Negative Risikoabgrenzung: Greift ein **Ausschlusstatbestand** der AVB? Risikoausschlüsse sind eng auszulegen (st. Rspr. BGH IV. ZS), weil sie den durch die Leistungsbeschreibung eröffneten Versicherungsschutz wieder einschränken.

Prüfungspunkte:
- Wortlaut der Ausschlussklausel — entspricht der konkrete Sachverhalt der Klausel?
- Auslegung nach Empfängerhorizont des durchschnittlichen VN
- Unklarheitenregel § 305c Abs. 2 BGB zu Lasten des Versicherers, wenn nach Auslegung mindestens zwei vertretbare Lesarten verbleiben
- AGB-Kontrolle: § 307 BGB (unangemessene Benachteiligung; Transparenzgebot Abs. 1 Satz 2); §§ 308, 309 BGB praktisch selten einschlägig (vgl. § 310 Abs. 4 BGB)
- Abgrenzung zur **verhüllten Obliegenheit**: Eine als Risikoausschluss formulierte Klausel kann in Wahrheit eine Obliegenheit sein und unterliegt dann §§ 28, 32 VVG (halbzwingend) — Folge: Verstöße führen nicht zum Anspruchsausschluss, sondern nur zur Leistungsfreiheit unter Belehrungs- und Verschuldensvorbehalt

### 4. Stufe III — Leistungsfreiheit

Auch wenn Versicherungsfall vorliegt und kein Ausschluss greift, kann der Versicherer leistungsfrei sein:

- **Vorvertragliche Anzeigepflichtverletzung** §§ 19 ff. VVG (Rücktritt § 19 Abs. 2; Kündigung Abs. 3; Vertragsanpassung Abs. 4; Arglist § 22 iVm § 123 BGB) — Detailprüfung im Skill `obliegenheitsverletzung-vvg`
- **Verletzung vertraglicher Obliegenheiten** § 28 VVG (Vorsatz / grobe Fahrlässigkeit; Quotelung Abs. 2 Satz 2; Kausalitätsgegenbeweis Abs. 3; Belehrung Abs. 4)
- **Auskunftspflicht im Versicherungsfall** § 31 VVG
- **Herbeiführung des Versicherungsfalls** § 81 VVG (Vorsatz: vollständige Leistungsfreiheit; grobe Fahrlässigkeit: Quotelung)
- bei Haftpflicht: keine Anerkenntnisse ohne Zustimmung (vgl. § 105 VVG)

### 5. Anspruch und Beweislast

Anspruchsgrundlage: **§ 1 Satz 2 VVG iVm Versicherungsvertrag und AVB** (Leistungsanspruch des VN). In der Haftpflicht: **§ 100 VVG** (Befreiungsanspruch); in der Kfz-Haftpflicht: **§ 115 VVG** (Direktanspruch des geschädigten Dritten).

Beweislast (Faustregel):
- VN trägt Beweis für Versicherungsfall (Stufe I)
- Versicherer trägt Beweis für Risikoausschluss (Stufe II) und für die Voraussetzungen der Leistungsfreiheit (Stufe III), insb. Anzeigepflichtverletzung, Obliegenheitsverletzung, grobe Fahrlässigkeit / Vorsatz und ordnungsgemäße Belehrung
- VN trägt Kausalitätsgegenbeweis nach § 28 Abs. 3 VVG

### 6. Außergerichtliche oder gerichtliche Folgenseite

- Anspruchsschreiben mit Fristsetzung (idR 14 Tage), Berufung auf konkrete AVB-Klausel und einschlägige BGH-Rspr.
- Bei Ablehnung: Leistungsklage vor dem zuständigen ZG (§§ 215, 216 VVG zur örtlichen Zuständigkeit beachten — VN kann am Wohnsitz klagen)
- Streitwert: konkrete Leistung; bei wiederkehrenden Leistungen (BU-Rente) § 9 ZPO (3,5-facher Jahresbetrag)
- Ggf. Ombudsmannverfahren (Versicherungsombudsmann e. V.) vor Klage; Verjährungshemmung § 204 Abs. 1 Nr. 4 BGB

## Quellen und Zitierweise

Verbindlich: [`../../../references/zitierweise.md`](../../../references/zitierweise.md).

### Statute

- [§ 1 VVG](https://www.gesetze-im-internet.de/vvg_2008/__1.html) (Vertragsdefinition, Leistungspflicht)
- [§ 6 VVG](https://www.gesetze-im-internet.de/vvg_2008/__6.html) (Beratung des Versicherungsnehmers)
- [§ 7 VVG](https://www.gesetze-im-internet.de/vvg_2008/__7.html) (Information des Versicherungsnehmers)
- [§ 8 VVG](https://www.gesetze-im-internet.de/vvg_2008/__8.html) (Widerruf, 14 Tage)
- [§ 28 VVG](https://www.gesetze-im-internet.de/vvg_2008/__28.html) (Verletzung vertraglicher Obliegenheiten, Quotelung, Kausalitätsgegenbeweis)
- [§ 81 VVG](https://www.gesetze-im-internet.de/vvg_2008/__81.html) (Herbeiführung des Versicherungsfalls)
- [§ 100 VVG](https://www.gesetze-im-internet.de/vvg_2008/__100.html) (Haftpflichtversicherung — Befreiungsanspruch)
- [§ 115 VVG](https://www.gesetze-im-internet.de/vvg_2008/__115.html) (Direktanspruch in der Kfz-Haftpflicht)
- [§ 305c Abs. 2 BGB](https://www.gesetze-im-internet.de/bgb/__305c.html) (Unklarheitenregel)
- [§ 307 BGB](https://www.gesetze-im-internet.de/bgb/__307.html) (Inhaltskontrolle, Transparenzgebot)
- [Art. 1 EGVVG](https://www.gesetze-im-internet.de/egvvg/art_1.html) (Übergangsrecht zur VVG-Reform 2008)

### Kommentare

- Armbrüster, in: Prölss/Martin, VVG, 32. Aufl. 2024, § 1 VVG Rn. 1 ff., § 28 VVG Rn. 1 ff.
- Looschelders, in: MüKoVVG, 3. Aufl. 2024, § 28 VVG Rn. 1 ff.
- Marlow/Spuhl, in: BeckOK VVG, Stand 2024, § 1 VVG Rn. 1 ff.
- Beckmann/Matusche-Beckmann, Versicherungsrechts-Handbuch, 4. Aufl. 2022, § 10 (AVB-Auslegung).

### Rechtsprechung (`[unverifiziert – prüfen in juris/Beck-Online/openjur]`)

1. BGH, Urt. v. 23.06.1993 – IV ZR 135/92, BGHZ 123, 83 (Empfängerhorizont des durchschnittlichen VN bei AVB-Auslegung) (https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=23.06.1993&Aktenzeichen=IV+ZR+135/92)
2. BGH, Urt. v. 17.03.1999 – IV ZR 218/97, VersR 1999, 748 (enge Auslegung von Risikoausschlüssen) `[unverifiziert – prüfen]`
3. BGH, Urt. v. 14.04.2010 – IV ZR 135/08, VersR 2010, 760 (Transparenzgebot § 307 BGB in der AVB-Kontrolle) (https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=14.04.2010&Aktenzeichen=IV+ZR+135/08)

## Ausgabeformat

```
DECKUNGSGUTACHTEN — <Sparte>
Versicherer: <…>  Versicherungsschein-Nr.: <…>
Schadenhergang vom <Datum>  Schadennummer: <…>

I. Sachverhalt (knapp)

II. Frage
    Besteht Eintrittspflicht des Versicherers aus dem Vertrag iVm AVB?

III. Kurzantwort
     Eintrittspflicht: [ja / nein / quotal]
     Risiko der Position: 🟢 / 🟡 / 🔴

IV. Rechtliche Bewertung — Dreistufige Deckungsprüfung
    1. Versicherungsfall unter die Leistungsbeschreibung
       (Wortlaut der AVB-Klausel, Auslegung nach Empfängerhorizont)
    2. Kein Risikoausschluss
       a) Wortlaut der Ausschlussklausel
       b) Auslegung nach Empfängerhorizont
       c) § 305c Abs. 2 BGB
       d) § 307 BGB / Transparenzgebot
       e) Abgrenzung verhüllte Obliegenheit?
    3. Keine Leistungsfreiheit
       a) §§ 19 ff. VVG (Anzeigepflicht)
       b) § 28 VVG (Obliegenheiten)
       c) § 31 VVG (Auskunft)
       d) § 81 VVG (Herbeiführung)

V. Anspruch und Beweislast
   – Anspruchsgrundlage: § 1 Satz 2 VVG iVm Vertrag und AVB
   – Beweislastverteilung

VI. Risiken / offene Punkte und Fristenkalender
    – § 8 VVG (Widerruf, soweit relevant)
    – § 21 VVG (1 Monat; Versichererfrist)
    – §§ 195, 199 BGB (3-Jahres-Verjährung)
    – § 124 BGB (Arglistanfechtung)

VII. Empfehlung
     – Anspruchsschreiben / Klage / Ombudsmann
     – Fristsetzung

VIII. Quellenverzeichnis
```

## Beispiel

Wohngebäude (VGB), Leitungswasser. AVB-Klausel: "Versichert sind Schäden durch bestimmungswidrig austretendes Leitungswasser aus Zu- und Ableitungsrohren der Wasserversorgung; Nässeschäden infolge Abnutzung sind ausgeschlossen." Wasserschaden durch undichte Duschsilikonfuge.

**Stufe I**: Tritt das Wasser bestimmungswidrig aus einem "Zu- oder Ableitungsrohr"? Eine Duschfuge ist kein Rohr; der Versicherungsnehmer versteht "Rohr" als geschlossenes Leitungssystem (BGH IV. ZS, AVB-Empfängerhorizont) — Versicherungsfall wohl nicht eröffnet.

**Stufe II** (hilfsweise): Selbst wenn Stufe I bejaht würde, greift der Ausschluss "Nässeschäden infolge Abnutzung". Eng auszulegen; "Abnutzung" iSd Klausel meint allmählichen Verschleiß durch bestimmungsgemäßen Gebrauch. Falls Schaden auf plötzlichem Bruch beruht, greift Ausschluss nicht; bei langsam undicht gewordener Fuge greift er regelmäßig. § 305c Abs. 2 BGB zugunsten des VN, soweit beide Lesarten vertretbar.

**Stufe III**: Keine Anhaltspunkte für Anzeige- oder Obliegenheitsverletzung; § 81 VVG idR nicht einschlägig bei bloßer Fugenabnutzung.

**Empfehlung**: Außergerichtliches Schreiben mit Sachverständigengutachten zur Schadenursache; bei plötzlichem Bruch Deckung anmahnen; bei Abnutzung keine Erfolgsaussicht. Risiko: 🟡.

## Risiken / typische Fehler

- **Auslegung nach juristischem Verständnis** statt nach Empfängerhorizont des durchschnittlichen VN.
- **Unklarheitenregel § 305c Abs. 2 BGB übersehen**, obwohl mindestens zwei vertretbare Lesarten der AVB-Klausel verbleiben.
- **Risikoausschluss extensiv ausgelegt**, obwohl Risikoausschlüsse eng auszulegen sind.
- **Verhüllte Obliegenheit** nicht erkannt — als Risikoausschluss formulierte Klausel ist in Wahrheit Obliegenheit, unterliegt § 28 VVG (halbzwingend, Belehrung, Quotelung, Kausalitätsgegenbeweis).
- **Beweislast verkannt**: VN beweist Versicherungsfall, Versicherer beweist Ausschluss und Leistungsfreiheit; Kausalitätsgegenbeweis § 28 Abs. 3 VVG liegt beim VN.
- **VVG aF zitiert** (z. B. § 6 VVG aF Alles-oder-Nichts) — gilt nicht mehr für Versicherungsfälle ab 01.01.2008.
