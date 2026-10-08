---
name: urheberrechtsverletzung-abmahnung-borghei
title: /urheber-medienrecht:urheberrechtsverletzung-abmahnung
description: Prüfung einer Urheberrechtsverletzung und Entwurf einer § 97a UrhG-konformen Abmahnung mit dreifacher Schadensberechnung, Auskunftsanspruch § 101 UrhG (insb. Provider-Auskunft § 101 IX) und Reaktionsoptionen (modifizierte Unterlassungserklärung, negative Feststellungsklage). Use when der Mandant eine eigene Urheberrechtsverletzung geltend machen will oder eine Abmahnung erhalten hat, einschließlich Filesharing- und Plattform-Konstellationen (UrhDaG).
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/urheber-medienrecht/skills/urheberrechtsverletzung-abmahnung
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: ip
language: de
---

# /urheber-medienrecht:urheberrechtsverletzung-abmahnung

## Zweck

Der Skill prüft systematisch eine behauptete Urheberrechtsverletzung (Werkqualität, Aktivlegitimation, Verletzungshandlung, Schranken) und entwirft eine **§ 97a UrhG-konforme Abmahnung** mit Unterlassungsforderung, Schadensersatzberechnung (dreifache Methode), Auskunftsanspruch und Frist. Er adressiert zugleich Filesharing-Besonderheiten und Plattformkonstellationen (UrhDaG, DSA) sowie die Reaktionsseite (modifizierte Unterlassungserklärung, negative Feststellungsklage).

## Eingaben

- Werk (Art: Lichtbildwerk / Lichtbild, Sprachwerk, Musikwerk, Filmwerk, Software, Werk der angewandten Kunst, Datenbank etc.)
- Schöpfungsdatum, Erstveröffentlichung, ggf. Urheberbezeichnung (§ 10 UrhG-Vermutung)
- Rechtsinhaberschaft (Urheber / Rechtsnachfolger / exklusiver Lizenznehmer)
- Konkrete Verletzungshandlung (Vervielfältigung, Verbreitung, öffentliche Zugänglichmachung iSv § 19a UrhG, etc.) — mit Datum, URL, Screenshot-Beleg
- Verletzergröße (privater Verbraucher iSv § 97a III UrhG / Gewerbetreibender / Plattform)
- Vorhergehende Lizenzanfrage / Lizenzangebote (relevant für Lizenzanalogie)
- Position des Mandanten: Verletzter (Abmahnung versendet) oder Empfänger einer Abmahnung (Reaktion)

## Sub-Agent-Architektur

Researcher liefert Statute (§§ 2, 15, 72, 97, 97a, 101, 102 UrhG; UrhDaG), die einschlägige BGH I. ZS-Rspr. zur dreifachen Schadensberechnung, EuGH-Linie zur Schöpfungshöhe (Cofemel, Brompton), Filesharing-Rspr. (Sommer unseres Lebens, BearShare, Loud) sowie MFM-Bildhonorartabellen für die Lizenzanalogie. Drafter prüft die Verletzung im Gutachtenstil und entwirft die Abmahnung mit Unterlassungserklärung (vorformuliert + Hinweis nach § 97a II Nr. 4 UrhG). Reviewer prüft § 97a-Inhaltsanforderungen, § 97a III-Deckelung und Wahlrecht der Schadensberechnung.

## Ablauf

### 1. Werkqualität § 2 UrhG / verwandte Schutzrechte

- Subsumtion unter § 2 II UrhG (eigene geistige Schöpfung – EuGH-Linie: „Cofemel" C-683/17, [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=EuGH&Datum=2019-09-12&Aktenzeichen=C-683/17); „Brompton" C-833/18, [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=EuGH&Datum=2020-06-11&Aktenzeichen=C-833/18)).
- Bei fehlender Schöpfungshöhe: Prüfung verwandter Schutzrechte — Lichtbild § 72 UrhG (50 J Schutzdauer ab Erscheinen), ausübende Künstler §§ 73 ff., Tonträgerhersteller § 85, Sendeunternehmen § 87, Datenbankhersteller § 87a (eigenständiger sui-generis-Schutz), Filmhersteller § 94.
- Bei Werken angewandter Kunst (Industriedesign): nach BGH „Geburtstagszug" (Urt. v. 13.11.2013 – I ZR 143/12, BGHZ 199, 52, [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2013-11-13&Aktenzeichen=I%20ZR%20143/12)) keine erhöhten Anforderungen mehr; ggf. Schnittstelle Designrecht (`gewerblicher-rechtsschutz`).
- Schutzdauer § 64 UrhG: 70 Jahre pma; ggf. Gemeinfreiheit prüfen.

### 2. Aktivlegitimation

- **Urheber** § 7 UrhG (natürliche Person, ggf. § 10 UrhG-Vermutung bei Urhebernennung).
- **Miturheber** § 8 UrhG (gemeinsame Schöpfung, gesamthänderische Bindung).
- **Rechtsnachfolger** durch Erbgang (§ 28 UrhG) oder durch Einräumung ausschließlicher Nutzungsrechte (§ 31 III UrhG).
- **Exklusiver Lizenznehmer** ist eigenständig aktivlegitimiert; einfacher Lizenznehmer nur in Prozessstandschaft (BGH-Linie `[unverifiziert]`).

### 3. Verletzungshandlung §§ 15–24 UrhG

- Vervielfältigung § 16 UrhG (auch transiente RAM-Vervielfältigung).
- Verbreitung § 17 UrhG (Erschöpfungsgrundsatz im EWR).
- Öffentliche Zugänglichmachung § 19a UrhG (Online-Bereitstellung); maßgeblich EuGH „Svensson" (C-466/12, [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=EuGH&Datum=2014-02-13&Aktenzeichen=C-466/12)), „GS Media" (C-160/15, [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=EuGH&Datum=2016-09-08&Aktenzeichen=C-160/15)), „Renckhoff" (C-161/17, [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=EuGH&Datum=2018-08-07&Aktenzeichen=C-161/17)), „YouTube/Cyando" (C-682/18, C-683/18, [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=EuGH&Datum=2021-06-22&Aktenzeichen=C-682/18)).
- Senderecht § 20 UrhG.
- Bearbeitungs-/Umgestaltungsrecht § 23 UrhG (mit § 23 II UrhG Anpassung 2021 zur „hinreichenden Abstand"-Doktrin).

### 4. Schranken §§ 44a ff. UrhG

- § 51 UrhG Zitat (Belegfunktion erforderlich, Quellenangabe § 63 UrhG).
- § 51a UrhG Karikatur/Parodie/Pastiche (Umsetzung Art. 17 VII DSM-RL, 2021 in Kraft) — Schutz auch für UGC mit transformativer Verwendung.
- § 53 UrhG Privatkopie (nicht aus offensichtlich rechtswidriger Quelle, § 53 I 1 UrhG).

### 5. Rechtsfolgen §§ 97 ff. UrhG

- **Unterlassung** § 97 I UrhG — verschuldensunabhängig, Wiederholungsgefahr indiziert durch Verletzung.
- **Schadensersatz** § 97 II UrhG bei Verschulden — **dreifache Berechnungsmethode** (Wahlrecht des Verletzten):

| Methode | Norm | Bemerkung |
|---|---|---|
| Entgangener Gewinn | § 252 BGB iVm § 97 II 1 UrhG | Selten praktikabel ohne Marktdaten |
| Verletzergewinn | § 97 II 2 UrhG | „Gemeinkostenanteil"-Rspr.: nur ausschließlich variable Kosten abzugsfähig (BGH, Urt. v. 02.11.2000 – I ZR 246/98, BGHZ 145, 366, [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2000-11-02&Aktenzeichen=I%20ZR%20246/98)) |
| Lizenzanalogie | § 97 II 3 UrhG | Bei Lichtbildern idR MFM-Bildhonorartabellen, ggf. 100 %-Aufschlag bei fehlender Urhebernennung (BGH-Linie `[unverifiziert]`) |

- **Beseitigung** § 98 UrhG (Vernichtung, Rückruf).
- **Auskunft** § 101 UrhG (Hersteller / Verbreitungsweg / Mengen / Preise), **§ 101 IX** insb. Provider-Auskunft mit Richtervorbehalt (TMG-Schnittstelle).
- **Verjährung** § 102 UrhG: 3 Jahre ab Kenntnis (§§ 195, 199 BGB), bei Bereicherung 10/30 Jahre (§ 102 S. 2 iVm § 852 BGB).

### 6. Abmahnung § 97a UrhG

Inhaltsanforderungen § 97a II UrhG (alle vier zwingend, sonst unwirksam, § 97a IV UrhG-Rückforderungsanspruch):

1. Name oder Firma des Verletzten,
2. genaue Bezeichnung der Rechtsverletzung,
3. Aufschlüsselung der geltend gemachten Zahlungsansprüche (Unterlassungsanspruch + Schadensersatz),
4. Hinweis, soweit eine vorformulierte Unterlassungsverpflichtungserklärung beigefügt ist, **wenn** und **inwieweit** diese über die abgemahnte Rechtsverletzung hinausgeht.

**§ 97a III UrhG Kostendeckelung:** Bei erstmaliger Abmahnung **gegenüber einer natürlichen Person**, die nicht für gewerbliche/selbständige Tätigkeit handelt, und bei einfacher Rechtsverletzung außerhalb des Geschäftsbetriebs gilt für den Unterlassungsanspruch ein Gegenstandswert von **1.000 EUR** (Anwaltsgebühren entsprechend gedeckelt). Ausnahme nur bei „unbilligem" Ergebnis.

**Filesharing-Spezifika:**

- Täterhaftung Anschlussinhaber: tatsächliche Vermutung, widerlegbar durch sekundäre Darlegungslast (BGH „Loud", Urt. v. 30.03.2017 – I ZR 19/16, GRUR 2017, 1233, [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2017-03-30&Aktenzeichen=I%20ZR%2019/16)).
- Familienanschlüsse: keine generelle Belehrungspflicht volljähriger Familienmitglieder (BGH „BearShare", Urt. v. 08.01.2014 – I ZR 169/12, BGHZ 200, 76, [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2014-01-08&Aktenzeichen=I%20ZR%20169/12)).
- WLAN-Privatperson: Aufklärungspflicht bei Standardkonfiguration nicht erforderlich (BGH „Sommer unseres Lebens", Urt. v. 12.05.2010 – I ZR 121/08, BGHZ 185, 330, [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2010-05-12&Aktenzeichen=I%20ZR%20121/08); in der Folge präzisiert).

**UrhDaG (Plattformkonstellation):** Bei Verletzung auf großen Diensteanbietern iSv § 2 UrhDaG primär Plattformhaftung gemäß §§ 1–10 UrhDaG, Beschwerdemechanismus § 14 UrhDaG, Pastiche-Schranke § 5 UrhDaG (Schnittstelle § 51a UrhG).

### 7. Reaktionsoptionen (wenn Mandant Empfänger der Abmahnung)

- **Modifizierte Unterlassungserklärung** (Anpassung von Reichweite, Vertragsstrafe, Geltungsbereich).
- **Schutzschrift** beim ZAV/Gericht zur Abwehr einstweiliger Verfügung.
- **Negative Feststellungsklage** § 256 ZPO — Risiko: Kostenfolge, wenn Abmahnung berechtigt war.
- **§ 97a IV UrhG-Rückforderung** bei unwirksamer Abmahnung.

## Quellen und Zitierweise

Verbindlich: [`../../../references/zitierweise.md`](../../../references/zitierweise.md).

### Statute

- [§ 2 UrhG](https://www.gesetze-im-internet.de/urhg/__2.html) (Werkbegriff)
- [§ 15 UrhG](https://www.gesetze-im-internet.de/urhg/__15.html) (Verwertungsrechte)
- [§ 19a UrhG](https://www.gesetze-im-internet.de/urhg/__19a.html) (öffentliche Zugänglichmachung)
- [§ 23 UrhG](https://www.gesetze-im-internet.de/urhg/__23.html) (Bearbeitung/Umgestaltung)
- [§ 51 UrhG](https://www.gesetze-im-internet.de/urhg/__51.html) (Zitat)
- [§ 51a UrhG](https://www.gesetze-im-internet.de/urhg/__51a.html) (Karikatur, Parodie, Pastiche)
- [§ 72 UrhG](https://www.gesetze-im-internet.de/urhg/__72.html) (Lichtbildschutz)
- [§ 97 UrhG](https://www.gesetze-im-internet.de/urhg/__97.html) (Unterlassungs- und Schadensersatzanspruch)
- [§ 97a UrhG](https://www.gesetze-im-internet.de/urhg/__97a.html) (Abmahnung)
- [§ 101 UrhG](https://www.gesetze-im-internet.de/urhg/__101.html) (Auskunftsanspruch, insb. Abs. IX Provider-Auskunft)
- [§ 102 UrhG](https://www.gesetze-im-internet.de/urhg/__102.html) (Verjährung)
- [UrhDaG](https://www.gesetze-im-internet.de/urhdag/) (Urheberrechts-Diensteanbieter-Gesetz)
- [Art. 17 DSM-RL (EU) 2019/790](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32019L0790)

### Kommentare

- Specht-Riemenschneider, in: Dreier/Schulze, UrhG, 7. Aufl. 2022, § 97 Rn. 1 ff., § 97a Rn. 1 ff. `[unverifiziert – aktuelle Auflage prüfen]`
- v. Wolff, in: Wandtke/Bullinger, Praxiskommentar Urheberrecht, 6. Aufl. 2022, § 97 UrhG Rn. 1 ff. `[unverifiziert]`
- Schricker/Loewenheim, Urheberrecht, 6. Aufl. 2020, § 97 UrhG Rn. 1 ff. `[unverifiziert]`
- BeckOK UrhG/Reber, Stand 2024, § 97 Rn. 1 ff.

### Rechtsprechung

1. BGH, Urt. v. 17.06.1992 – I ZR 107/90, BGHZ 119, 20 = GRUR 1993, 55 – „Tchibo/Rolex II" (dreifache Schadensberechnung: Wahlrecht zwischen den drei Berechnungsarten), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=1992-06-17&Aktenzeichen=I%20ZR%20107/90)
2. BGH, Urt. v. 02.11.2000 – I ZR 246/98, BGHZ 145, 366 = GRUR 2001, 329 – „Gemeinkostenanteil", [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2000-11-02&Aktenzeichen=I%20ZR%20246/98)
3. BGH, Urt. v. 12.05.2010 – I ZR 121/08, BGHZ 185, 330 = GRUR 2010, 633 – „Sommer unseres Lebens" (Filesharing), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2010-05-12&Aktenzeichen=I%20ZR%20121/08)
4. BGH, Urt. v. 08.01.2014 – I ZR 169/12, BGHZ 200, 76 = GRUR 2014, 657 – „BearShare", [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2014-01-08&Aktenzeichen=I%20ZR%20169/12)
5. BGH, Urt. v. 30.03.2017 – I ZR 19/16, GRUR 2017, 1233 – „Loud", [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2017-03-30&Aktenzeichen=I%20ZR%2019/16)
6. BGH, Urt. v. 13.11.2013 – I ZR 143/12, BGHZ 199, 52 = GRUR 2014, 175 – „Geburtstagszug", [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2013-11-13&Aktenzeichen=I%20ZR%20143/12)
7. BGH, Urt. v. 15.11.2012 – I ZR 74/12, GRUR 2013, 511 – „Morpheus" (Aufsichtspflicht bei Minderjährigen), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2012-11-15&Aktenzeichen=I%20ZR%2074/12)
8. EuGH, Urt. v. 12.09.2019 – Rs. C-683/17, ECLI:EU:C:2019:721 – Cofemel, [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=EuGH&Datum=2019-09-12&Aktenzeichen=C-683/17)
9. EuGH, Urt. v. 11.06.2020 – Rs. C-833/18, ECLI:EU:C:2020:461 – Brompton Bicycle, [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=EuGH&Datum=2020-06-11&Aktenzeichen=C-833/18)
10. EuGH, Urt. v. 22.06.2021 – Rs. C-682/18, C-683/18, ECLI:EU:C:2021:503 – YouTube/Cyando, [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=EuGH&Datum=2021-06-22&Aktenzeichen=C-682/18)
11. EuGH, Urt. v. 16.07.2009 – Rs. C-5/08, ECLI:EU:C:2009:465 – Infopaq (Werkbegriff), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=EuGH&Datum=2009-07-16&Aktenzeichen=C-5/08)

## Ausgabeformat

```
GUTACHTEN — Urheberrechtsverletzung
Werk: <Werkbezeichnung>     Verletzungshandlung: <Art, URL, Datum>
Mandant: <Rechtsinhaber / Verletzter / Empfänger Abmahnung>

I. Sachverhalt (knapp)
II. Frage(n)
III. Kurzantwort
     – Verletzung: [ja / nein / streitig]
     – Empfehlung: [Abmahnung / mod. UE / neg. Feststellungsklage / Schutzschrift]

IV. Rechtliche Bewertung
    1. Werkqualität / verwandtes Schutzrecht
    2. Schutzdauer
    3. Aktivlegitimation
    4. Verletzungshandlung §§ 15–24 UrhG
    5. Schranken §§ 44a ff. UrhG (insb. §§ 51, 51a, 53)
    6. Rechtsfolgen §§ 97 ff. UrhG
       a) Unterlassung
       b) Schadensersatz (dreifache Berechnung – Vergleich aller drei Methoden)
       c) Auskunft / Beseitigung
       d) Verjährung § 102 UrhG

V. Abmahnung nach § 97a UrhG (Entwurf)
    – Inhaltsanforderungen § 97a II UrhG (vier Punkte)
    – ggf. § 97a III UrhG-Deckelung (Verbraucher)
    – Vorformulierte Unterlassungserklärung mit Hinweis

VI. Risiken / offene Punkte
    🟢 / 🟡 / 🔴 <Einstufung mit Begründung>
    Fristkalender: <§ 102 UrhG-Verjährung; Reaktionsfrist; Schutzschrift>

VII. Quellenverzeichnis
```

### Vorlage Abmahnungsanschreiben

```
<Anwaltsbriefkopf>

An <Verletzer>
<Datum>

In Sachen <Mandant> ./. <Verletzer>
wegen Urheberrechtsverletzung — Abmahnung nach § 97a UrhG

Sehr geehrte Damen und Herren,

I. Anzeige der Vertretung
   Wir vertreten Herrn/Frau <Mandant> ([§ 97a II Nr. 1 UrhG]).
   Eine ordnungsgemäße Vollmacht ist beigefügt.

II. Rechtsverletzung ([§ 97a II Nr. 2 UrhG])
    Sie haben am <Datum> unter <URL> das Werk <konkrete Bezeichnung>
    unserer Mandantschaft ohne Erlaubnis öffentlich zugänglich gemacht
    (§ 19a UrhG). Beleg: <Screenshot, Anlage K1>.
    Das Werk genießt Schutz als <Werkart> nach § <Norm> UrhG.

III. Ansprüche ([§ 97a II Nr. 3 UrhG])
     1. Unterlassungsanspruch nach § 97 I UrhG
        Gegenstandswert: <Wert> EUR
        [bei Verbraucher: Gegenstandswert gemäß § 97a III UrhG 1.000 EUR]
     2. Schadensersatzanspruch nach § 97 II UrhG
        Lizenzanalogie nach <MFM 20XX>: <Betrag> EUR
        [Zuschlag 100 % wegen fehlender Urhebernennung: <Betrag> EUR]
     3. Aufwendungsersatz § 97a III UrhG / RVG
        Anwaltsgebühren: <Betrag> EUR
     ─────────────────────────────────
     Gesamt: <Betrag> EUR

IV. Forderung
    Wir fordern Sie auf, bis zum <Datum +14 Tage>
      a) die beigefügte strafbewehrte Unterlassungserklärung
         unterzeichnet zurückzusenden,
      b) den Schadensersatzbetrag i.H.v. <…> EUR und
      c) die Aufwendungserstattung i.H.v. <…> EUR
    auf unser Konto <…> zu zahlen.

V. Hinweis nach § 97a II Nr. 4 UrhG
   Die vorformulierte Unterlassungserklärung [geht / geht nicht] über
   die abgemahnte konkrete Rechtsverletzung hinaus, da <…>.

Mit freundlichen Grüßen
<Anwalt>

Anlagen: K1 Screenshot, K2 Vorformulierte Unterlassungserklärung, K3 Vollmacht
```

## Risiken / typische Fehler

- **Fehlende Inhaltsanforderungen § 97a II UrhG** → unwirksame Abmahnung → § 97a IV UrhG-Rückforderung des Abgemahnten.
- **Pauschale § 97a III-Deckelung** bei Gewerbetreibendem oder umgekehrt volle Gebühr bei Verbraucher → § 43a BRAO-Verstoß.
- **Schadensersatz nur nach einer Methode** geltend gemacht, ohne das Wahlrecht des Verletzten zu erläutern.
- **Übersehen der EuGH-Schöpfungshöhenlinie** (Cofemel/Brompton) bei Werken angewandter Kunst.
- **Übersehen der Schranke § 51a UrhG (Pastiche)** bei UGC und Memes.
- **Filesharing-Anschlussinhaber** automatisch als Täter behandelt — sekundäre Darlegungslast prüfen.
- **Plattformkonstellation** ohne UrhDaG-Prüfung abgemahnt → falscher Anspruchsgegner.
- **Verjährung § 102 UrhG** übersehen — bei Kenntnis länger als 3 Jahre ist Klage unzulässig.
- **Lizenzanalogie ohne Datenbasis** (MFM, gerichtsbekannte Lizenzsätze) — Streitwert nicht haltbar.
