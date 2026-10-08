---
name: versicherungsmaklerhaftung-borghei
title: /versicherungsrecht:versicherungsmaklerhaftung
description: Haftung des Versicherungsmaklers wegen Pflichtverletzung – Marktauswahl § 60 VVG, anlassbezogene Beratung § 61 VVG, Dokumentation/Beratungsprotokoll § 62 VVG, Schadensersatz § 63 VVG; Abgrenzung zum Versicherungsvertreter § 59 Abs. 2 VVG und § 34d GewO; Mitverschulden § 254 BGB; Verjährung §§ 195, 199 BGB. Use when ein Versicherungsnehmer Schadensersatz gegen den Makler verlangt (Unterversicherung, falsche Sparten-Empfehlung, fehlende Anlassprüfung, unvollständige Dokumentation).
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/versicherungsrecht/skills/versicherungsmaklerhaftung
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: insurance
language: de
---

# /versicherungsrecht:versicherungsmaklerhaftung

## Zweck

Der Versicherungsmakler ist "Sachwalter des Kunden" (BGH IVa ZR 190/83 (https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=22.05.1985&Aktenzeichen=IVa+ZR+190/83)) und unterliegt umfassenden Pflichten aus §§ 60–62 VVG: hinreichende Marktauswahl, anlassbezogene Beratung, Dokumentation. Bei Pflichtverletzung haftet er nach § 63 VVG auf Schadensersatz, daneben aus § 280 Abs. 1 BGB iVm Maklervertrag und § 311 Abs. 2 BGB. Der Skill prüft Pflichtumfang, Pflichtverletzung, Verschulden, Schaden, Kausalität, Mitverschulden § 254 BGB und Verjährung §§ 195, 199 BGB.

## Eingaben

- Maklervertrag / Maklerauftrag (schriftlich, mündlich, konkludent)
- Beratungsanlass und -gegenstand (Vertragsabschluss, -anpassung, Schadenfall-Begleitung)
- Beratungsdokumentation / Beratungsprotokoll § 62 VVG
- Vermittelter Versicherungsvertrag und tatsächlicher Versicherungsbedarf
- Schadensereignis und Schadenshöhe (insb. Differenz zwischen Versicherungsleistung und tatsächlichem Schaden bei Unterversicherung)
- Verhalten des VN (Mitwirkung, Angaben, Selbstinformation)
- Verjährungsrelevante Daten (Kenntnis von Pflichtverletzung und Schaden)

## Sub-Agent-Architektur

Researcher liefert VVG-Statute (§§ 59–63), GewO § 34d, BGB-Anker, BGH-Rspr. zur Sachwalterstellung des Maklers und Kommentarstellen (Prölss/Martin, MüKoVVG, BeckOK VVG, Beckmann/Matusche-Beckmann). Drafter prüft Pflichtenkatalog, Pflichtverletzung, Schaden, Kausalität, Mitverschulden und entwirft Anspruchsschreiben oder Klage. Reviewer prüft Verjährung (§§ 195, 199 BGB), Abgrenzung Makler/Vertreter, vollständigen Anspruchsaufbau und ob die IDD-Umsetzung (§§ 1a, 6, 7, 60 ff. VVG) berücksichtigt ist.

## Ablauf

### 1. Abgrenzung Makler / Vertreter

| Merkmal | Versicherungsmakler | Versicherungsvertreter |
|---|---|---|
| Legaldefinition | § 59 Abs. 3 VVG | § 59 Abs. 2 VVG |
| Lager | Sachwalter des **Kunden** | Lager des **Versicherers** |
| Erlaubnis | § 34d Abs. 1 Nr. 1 GewO | § 34d Abs. 1 Nr. 2 GewO |
| Pflichten | §§ 60–62 VVG (hinreichende Marktauswahl, anlassbezogene Beratung, Dokumentation) | § 6 VVG (Beratung); reduzierte Marktauswahlpflicht |
| Haftung | § 63 VVG; § 280 BGB iVm Maklervertrag | § 6 Abs. 5 VVG; ggf. Versichererhaftung |

Mehrfachvertreter, gebundene Vertreter und produktakzessorische Vermittler beachten (§ 34d Abs. 8 GewO).

### 2. Pflichtenkatalog §§ 60–62 VVG

**§ 60 VVG — hinreichende Marktauswahl:**

- Makler hat seinem Rat eine hinreichende Zahl von auf dem Markt angebotenen Versicherungsverträgen und von Versicherern zugrunde zu legen
- Beschränkt er sich auf eine kleinere Marktauswahl, muss er dies offenlegen (§ 60 Abs. 1 Satz 2 VVG)

**§ 61 VVG — Beratung, anlassbezogen und individuell:**

- Frage- und Beratungspflicht **nach Maßgabe der Schwierigkeit des Versicherungsbedarfs und der Erkennbarkeit der Beratungsbedürftigkeit**
- Erstreckt sich auf Risiken, Lücken, Über-/Unterversicherung
- Anlassbezogen: Reagiert auf Veränderungen (Umzug, Geschäftsausweitung, Personalwechsel)

**§ 62 VVG — Dokumentation:**

- Vor Abschluss in **Textform** klar und verständlich Beratungsanlass, Begründung des erteilten Rats und konkrete Versicherungsprodukte mit den wesentlichen Merkmalen darstellen
- Beratungsprotokoll muss dem VN **vor Abgabe der Vertragserklärung** ausgehändigt werden
- Ausnahme nur bei ausdrücklichem Verzicht des VN in gesonderter Erklärung in Textform (§ 61 Abs. 2 VVG)

**Sachwalter-Rechtsprechung** (BGH, Urt. v. 22.05.1985 – IVa ZR 190/83, BGHZ 94, 356 (https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=22.05.1985&Aktenzeichen=IVa+ZR+190/83)): Makler ist umfassend zu Beratung, Information und Betreuung verpflichtet; weitergehend als bloßer Vermittler. Pflichten gelten auch während der Vertragslaufzeit.

### 3. Schadensersatz § 63 VVG

**Anspruchsvoraussetzungen:**

1. **Schuldverhältnis** (Maklervertrag oder vorvertragliches Vertrauensverhältnis § 311 Abs. 2 BGB)
2. **Pflichtverletzung** iSv §§ 60, 61, 62 VVG
3. **Verschulden** — Makler hat zu vertretendes Verhalten zu verantworten (§ 276 BGB); Vermutung des Verschuldens § 280 Abs. 1 Satz 2 BGB
4. **Schaden** des VN — typische Konstellationen:
   - Unterversicherung → Differenz zwischen tatsächlichem Schaden und Versicherungsleistung
   - Falsche Sparten-Empfehlung → Eintrittspflicht eines Versicherers, der bei richtiger Beratung versichert worden wäre
   - Fehlende Anpassungsempfehlung → Differenz zwischen aktuellem und angepasstem Versicherungsschutz
5. **Kausalität** der Pflichtverletzung für den Schaden — Vermutung beratungsgerechten Verhaltens des VN bei Aufklärungspflichtverletzung (st. Rspr.; vgl. BGH XI ZR-Rspr. zur Anlageberatung, hier übertragbar `[unverifiziert – prüfen]`)
6. **Kein Mitverschulden** § 254 BGB (s. unten)

**Beweislast**: Pflichtverletzung trägt VN; Verschulden vermutet § 280 Abs. 1 Satz 2 BGB; bei fehlender / lückenhafter Dokumentation § 62 VVG: Beweislastumkehr / Beweiserleichterung zugunsten des VN (h.M.; vgl. Prölss/Martin, § 63 VVG; BGH `[unverifiziert – prüfen]`).

### 4. Mitverschulden § 254 BGB

- Unzutreffende oder zurückgehaltene Angaben des VN
- Eigenes Erkennen einer Lücke trotz Beratung
- Verletzung von Selbstinformationspflichten — restriktiv: VN ist regelmäßig auf den Sachverstand des Maklers angewiesen (BGH `[unverifiziert – prüfen]`)
- Übliche Quoten in der Praxis: Mitverschulden 0–30 %; bei evidenten Unrichtigkeiten höher

### 5. Verjährung §§ 195, 199 BGB

- **Regelverjährung 3 Jahre**, § 195 BGB
- Beginn mit Schluss des Jahres, in dem der Anspruch entstanden ist und VN Kenntnis von Pflichtverletzung und Schaden hat (oder grob fahrlässig nicht hat), § 199 Abs. 1 BGB
- Maximalfrist § 199 Abs. 3 BGB (10 Jahre ab Entstehung, 30 Jahre ab handlung)
- Bei laufendem Maklerverhältnis: Verjährungsbeginn kann durch Pflichtverletzung in jedem Jahr neu ausgelöst werden (Sekundärhaftungsrechtsprechung); kritisch prüfen

### 6. Verfahrens- und Beweissicherung

- Anforderung Beratungsprotokoll § 62 VVG vom Makler
- Anforderung E-Mail-Korrespondenz, Risikoanalyse, Angebotsvergleich
- Sachverständigengutachten zum Versicherungsbedarf und zur Schadenshöhe
- Klage am Sitz des Maklers (§§ 12, 17 ZPO); Streitwert: Differenz Versicherungsleistung / tatsächlicher Schaden

## Quellen und Zitierweise

Verbindlich: [`../../../references/zitierweise.md`](../../../references/zitierweise.md).

### Statute

- [§ 59 VVG](https://www.gesetze-im-internet.de/vvg_2008/__59.html) (Begriffe Vermittler, Vertreter, Makler)
- [§ 60 VVG](https://www.gesetze-im-internet.de/vvg_2008/__60.html) (Beratungsgrundlage des Versicherungsmaklers)
- [§ 61 VVG](https://www.gesetze-im-internet.de/vvg_2008/__61.html) (Beratungs- und Dokumentationspflichten)
- [§ 62 VVG](https://www.gesetze-im-internet.de/vvg_2008/__62.html) (Zeitpunkt und Form der Information)
- [§ 63 VVG](https://www.gesetze-im-internet.de/vvg_2008/__63.html) (Schadensersatzpflicht)
- [§ 6 VVG](https://www.gesetze-im-internet.de/vvg_2008/__6.html) (Beratung des Versicherers; Abgrenzung)
- [§ 7 VVG](https://www.gesetze-im-internet.de/vvg_2008/__7.html) (Informationspflichten)
- [§ 34d GewO](https://www.gesetze-im-internet.de/gewo/__34d.html) (Erlaubnispflicht Versicherungsvermittler)
- [§ 280 BGB](https://www.gesetze-im-internet.de/bgb/__280.html) (Schadensersatz wegen Pflichtverletzung)
- [§ 311 Abs. 2 BGB](https://www.gesetze-im-internet.de/bgb/__311.html) (c.i.c.)
- [§ 254 BGB](https://www.gesetze-im-internet.de/bgb/__254.html) (Mitverschulden)
- [§ 195 BGB](https://www.gesetze-im-internet.de/bgb/__195.html), [§ 199 BGB](https://www.gesetze-im-internet.de/bgb/__199.html) (Verjährung)
- [RL (EU) 2016/97 (IDD)](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32016L0097) (Insurance Distribution Directive)

### Kommentare

- Reiff, in: Prölss/Martin, VVG, 32. Aufl. 2024, § 60 VVG Rn. 1 ff., § 63 VVG Rn. 1 ff.
- Dörner, in: MüKoVVG, 3. Aufl. 2024, §§ 59 ff. VVG.
- Marlow/Spuhl, in: BeckOK VVG, Stand 2024, §§ 60–63 VVG.
- Beckmann/Matusche-Beckmann, Versicherungsrechts-Handbuch, 4. Aufl. 2022, § 5 (Versicherungsvermittlung).
- Schwintowski, in: Bruck/Möller, VVG, 9. Aufl., §§ 59 ff. VVG.

### Rechtsprechung (`[unverifiziert – prüfen in juris/Beck-Online/openjur]`)

1. BGH, Urt. v. 22.05.1985 – IVa ZR 190/83, BGHZ 94, 356 ("Sachwalter des Kunden") (https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=22.05.1985&Aktenzeichen=IVa+ZR+190/83)
2. BGH, Urt. v. 10.03.2016 – I ZR 147/14, NJW 2016, 3445 (Pflichten des Versicherungsmaklers; IDD-Vorgriff) (https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=10.03.2016&Aktenzeichen=I+ZR+147/14)
3. BGH, Urt. v. 14.01.2016 – I ZR 107/14, VersR 2016, 786 (Maklerhaftung bei unzureichender Bedarfsermittlung) (https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=14.01.2016&Aktenzeichen=I+ZR+107/14)
4. BGH, Urt. v. 13.11.2014 – III ZR 544/13, VersR 2015, 187 (Beweisanforderungen § 62 VVG) (https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=13.11.2014&Aktenzeichen=III+ZR+544%2F13)

## Ausgabeformat

```
GUTACHTEN — Versicherungsmaklerhaftung
Makler: <Name, ggf. Vermittlerregister-Nr. § 11a GewO>
Vermittelter Vertrag: <Versicherer, Sparte, VS-Nr.>
Schadenereignis: <Datum, Ablauf>

I. Sachverhalt (knapp)

II. Frage
    Hat der Makler gegen seine Pflichten verstoßen und ist er nach
    § 63 VVG zum Schadensersatz verpflichtet?

III. Kurzantwort
     Anspruch: [ja / nein / quotal] — Risiko: 🟢 / 🟡 / 🔴

IV. Rechtliche Bewertung
    1. Abgrenzung Makler / Vertreter (§ 59 VVG, § 34d GewO)
    2. Maklervertrag und Schuldverhältnis (§ 311 Abs. 2 BGB)
    3. Pflichtenkatalog
       a) § 60 VVG — hinreichende Marktauswahl
       b) § 61 VVG — anlassbezogene Beratung
       c) § 62 VVG — Dokumentation in Textform vor Vertragsabschluss
    4. Pflichtverletzung — konkrete Subsumtion
    5. Verschulden (§ 276 BGB, Vermutung § 280 Abs. 1 Satz 2 BGB)
    6. Schaden — Differenzhypothese
    7. Kausalität — Vermutung beratungsgerechten Verhaltens
    8. Mitverschulden § 254 BGB
    9. Schadensersatz nach § 63 VVG / § 280 BGB
   10. Verjährung §§ 195, 199 BGB

V. Ergebnis und Empfehlung
   – Anspruchsschreiben mit Fristsetzung
   – Beweissicherung Beratungsprotokoll § 62 VVG
   – Ggf. Klage

VI. Fristenkalender und Risiken
    – §§ 195, 199 BGB (3-Jahres-Verjährung kenntnisabhängig)
    – § 199 Abs. 3 BGB (Maximalfrist 10 Jahre)

VII. Quellenverzeichnis
```

## Beispiel

Gewerbekunde betreibt Lager, Warenbestand ca. 1,2 Mio €. Makler hat im Risikofragebogen 2020 Versicherungssumme 600.000 € empfohlen, Beratungsprotokoll unterschrieben aber inhaltsleer ("Sachversicherung gewünscht, Inhaltsdeckung empfohlen"). Brand im August 2024, Schaden 980.000 €, Versicherer zahlt unter Berücksichtigung von Unterversicherung (50 %) nur 490.000 €. Kunde verlangt 490.000 € vom Makler.

**§ 60 VVG**: Marktauswahl wohl nicht streitig.

**§ 61 VVG — Bedarfsermittlung**: Aktuelle Warenbestände im Maklergespräch ermittelt? Empfehlung 600.000 € für Bestand 1,2 Mio € indiziert Pflichtverletzung — entweder Bedarf falsch ermittelt oder Empfehlung sachwidrig. Beratungsverhältnis als Sachwalter (BGH) verlangt Tiefenprüfung.

**§ 62 VVG**: Beratungsprotokoll inhaltsleer — Pflichtverletzung. Folge: Beweiserleichterung zugunsten VN; Makler muss darlegen, dass und wie er beraten hat.

**Schaden**: Unterversicherungsdifferenz 490.000 €.

**Kausalität**: Hätte Makler 1,2 Mio empfohlen, hätte VN aller Voraussicht nach diesen Schutz abgeschlossen (Vermutung beratungsgerechten Verhaltens) — sofern VN nicht aus Prämiengründen ausdrücklich reduziert hat. Prüfen.

**Mitverschulden § 254 BGB**: Hat VN die zu geringe Versicherungssumme aktiv gewollt oder ohne Nachfrage hingenommen? Praxisquoten 0–30 %.

**Verjährung §§ 195, 199 BGB**: Schaden eingetreten August 2024; Kenntnis von Unterversicherung wohl bei Ablehnung des Versicherers — Verjährung läuft ab Schluss 2024, endet 31.12.2027.

**Empfehlung**: Anspruchsschreiben mit Frist 4 Wochen; bei Ablehnung Klage. Risiko 🟡 → 🟢, sofern Inhaltsleere des Beratungsprotokolls bewiesen.

## Risiken / typische Fehler

- **Abgrenzung Makler / Vertreter** nicht geklärt — gebundener Vertreter haftet anders (§ 6 Abs. 5 VVG; ggf. Versichererhaftung).
- **Beratungsprotokoll § 62 VVG nicht angefordert** — entscheidendes Beweismittel.
- **Vermutung beratungsgerechten Verhaltens** übersehen — Kausalitätsbeweis wird sonst dem VN aufgebürdet.
- **Verjährung verschlafen** — §§ 195, 199 BGB Beginn mit Kenntnis von Pflichtverletzung **und** Schaden; bei laufendem Maklerverhältnis Sekundärhaftung prüfen.
- **Mitverschulden pauschal mit 50 % angesetzt** — Sachwalter-Rechtsprechung des BGH spricht eher gegen hohes Mitverschulden des Laien-VN.
- **§ 34d GewO mit § 4 RDG verwechselt** — Rechtsanwälte beraten nicht nach § 34d GewO; Versicherungsmakler beraten nicht rechtlich nach RDG (§ 5 RDG: Nebenleistung).
- **IDD-Umsetzung übersehen** — §§ 1a, 6, 7, 60 ff. VVG seit 23.02.2018 in der durch IDD geprägten Fassung; ältere Kommentarstellen kritisch lesen.
