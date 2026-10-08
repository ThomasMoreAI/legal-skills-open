---
name: data-act-anwendungsbereich-borghei
title: /datenwirtschaftsrecht:data-act-anwendungsbereich
description: Anwendungsbereich und Rollenzuordnung der EU-Datenverordnung (Data Act, VO (EU) 2023/2854) – vernetztes Produkt und verbundener Dienst Art. 2, Rollen Nutzer / Dateninhaber / Datenempfänger, Ausnahme für Kleinst- und Kleinunternehmen Art. 7 Abs. 1, gestaffelter Geltungsbeginn nach Art. 50 (12.09.2025 / 12.09.2026 / 12.01.2027 / 12.09.2027), Durchsetzung durch die Bundesnetzagentur §§ 2, 6 DADG und Bußgeldrahmen § 15 DADG sowie die Abgrenzung zu DSGVO, GeschGehG und Datenbankschutz. Use when zu klären ist, ob ein Unternehmen überhaupt Data-Act-Pflichten trifft, in welcher Rolle und ab wann.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/datenwirtschaftsrecht/skills/data-act-anwendungsbereich
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: eu
practice: data-protection
language: de
---

# /datenwirtschaftsrecht:data-act-anwendungsbereich

## Zweck

Der Skill beantwortet die Eingangsfrage jedes Data-Act-Mandats: Ist das Unternehmen betroffen, in welcher Rolle und ab welchem Datum. Er ordnet Produkte und Dienste den Begriffen der Verordnung zu, prüft die Ausnahme für Kleinst- und Kleinunternehmen und legt den nach Art. 50 gestaffelten Geltungsbeginn auf den konkreten Sachverhalt um. Er liefert außerdem die Zuständigkeits- und Sanktionslage nach dem deutschen Durchführungsgesetz.

## Eingaben

- Produkt- oder Dienstbeschreibung: Welche Daten entstehen, wo werden sie erhoben, wo gespeichert
- Rolle im Markt: Hersteller, Anbieter eines verbundenen Dienstes, Händler, Vermieter, Leasinggeber, Anbieter eines Datenverarbeitungsdienstes
- Unternehmensgröße nach Empfehlung 2003/361/EG einschließlich Partner- und verbundener Unternehmen
- Zeitpunkt des Inverkehrbringens des Produkts bzw. des Vertragsschlusses
- Bestehende Verträge: Laufzeit, unbefristet oder befristet, Enddatum
- Ob personenbezogene Daten betroffen sind und wer Verantwortlicher iSd Art. 4 Nr. 7 DSGVO ist
- Ob Geschäftsgeheimnisse iSd § 2 Nr. 1 GeschGehG in den Daten stecken

## Sub-Agent-Architektur

Ein Researcher zieht den Verordnungstext, das DADG und – soweit vorhanden – Leitlinien der Kommission und der Bundesnetzagentur heran. Ein Drafter ordnet den Sachverhalt den Legaldefinitionen des Art. 2 zu und rechnet die Fristen des Art. 50 aus. Ein Reviewer prüft, ob die Rollenzuordnung durchgehalten wurde, ob die Größenausnahme des Art. 7 Abs. 1 einschließlich der Partnerunternehmensregel geprüft ist und ob jede Aussage zur Sanktionshöhe auf § 15 DADG gestützt ist. Kein Beteiligter zitiert deutsche Rechtsprechung zum Data Act ohne Fundstelle.

## Ablauf

### 1. Sachlichen Anwendungsbereich klären (Art. 1, Art. 2 Data Act)

Zentral sind vier Begriffe:

| Begriff | Prüfpunkt |
|---|---|
| **Vernetztes Produkt** | Gegenstand, der Daten über seine Nutzung oder Umgebung erhält, generiert oder erhebt und diese über einen elektronischen Kommunikationsdienst, eine physische Verbindung oder einen geräteinternen Zugang übermitteln kann, und dessen Hauptfunktion nicht die Speicherung, Verarbeitung oder Übertragung von Daten für Dritte ist |
| **Verbundener Dienst** | Digitaler Dienst, der zum Zeitpunkt des Kaufs, der Miete oder des Leasings so mit dem Produkt verbunden ist, dass das Produkt ohne ihn eine oder mehrere Funktionen nicht ausführen könnte, oder der nachträglich verbunden wird |
| **Dateninhaber** | Wer nach der Verordnung, geltendem Unionsrecht oder nationalem Recht berechtigt oder verpflichtet ist, Daten zu nutzen und bereitzustellen |
| **Nutzer** | Natürliche oder juristische Person, die Eigentümerin eines vernetzten Produkts ist oder der vertraglich zeitweilige Rechte an dessen Nutzung übertragen wurden |

Erfasst sind **nicht** nur personenbezogene Daten. Der Data Act ist ein Zugangs- und Vertragsregime für **Produktdaten und verbundene Dienstdaten** unabhängig vom Personenbezug. Reine Softwareprodukte ohne Sensorik sind regelmäßig keine vernetzten Produkte; die Abgrenzung ist zu begründen, nicht zu behaupten.

### 2. Rollen zuordnen — und nur eine Rolle pro Datenstrom

Die Verordnung knüpft **je Datenstrom** an. Dasselbe Unternehmen kann Dateninhaber gegenüber dem Kunden und zugleich Datenempfänger gegenüber einem Zulieferer sein. Die Ausgangsprüfung nennt für jeden Datenstrom Nutzer, Dateninhaber und – falls vorhanden – Dritten nach [Art. 5](https://eur-lex.europa.eu/eli/reg/2023/2854/oj).

Ein nach Art. 3 der VO (EU) 2022/1925 benannter **Torwächter** ist nach Art. 5 Abs. 3 Data Act kein zugelassener Dritter; er darf Nutzer weder zur Weitergabe auffordern noch Daten aus Art. 4 Abs. 1 entgegennehmen. Diese Sperre ist bei jeder Datenweitergabe an große Plattformunternehmen zu prüfen.

### 3. Ausnahme für Kleinst- und Kleinunternehmen prüfen (Art. 7 Abs. 1)

Die Pflichten des Kapitels II gelten nicht für Daten aus vernetzten Produkten, die von einem **Kleinst- oder Kleinunternehmen** hergestellt oder konzipiert werden, bzw. aus verbundenen Diensten eines solchen Unternehmens. Zwei Rückausnahmen, die in der Praxis fast immer übersehen werden:

- Das Unternehmen hat ein **Partnerunternehmen oder verbundenes Unternehmen** iSd Art. 3 des Anhangs der Empfehlung 2003/361/EG, das kein Kleinst- oder Kleinunternehmen ist. Konzerntöchter fallen damit regelmäßig aus der Ausnahme heraus.
- Das Unternehmen wurde **als Unterauftragnehmer** mit der Herstellung oder Konzeption beauftragt.

Für ein Unternehmen, das seit weniger als einem Jahr als **mittleres Unternehmen** gilt, und für vernetzte Produkte binnen eines Jahres nach ihrem Inverkehrbringen durch ein mittleres Unternehmen gilt eine einjährige Übergangszeit (Art. 7 Abs. 1 UAbs. 2).

Nach Art. 7 Abs. 2 sind Vertragsklauseln, die die Rechte des Nutzers aus Kapitel II ausschließen, abbedingen oder abändern, **für den Nutzer nicht bindend** — eine gesetzliche Unwirksamkeitsanordnung, die neben §§ 305 ff. BGB tritt.

### 4. Zeitliche Geltung nach Art. 50 rechnen

| Regelung | Gilt ab / für |
|---|---|
| Verordnung insgesamt | **12.09.2025** |
| Konzeptionspflicht Art. 3 Abs. 1 | vernetzte Produkte und verbundene Dienste, die **nach dem 12.09.2026** in Verkehr gebracht wurden |
| Kapitel III (Pflichten kraft anderweitigen Unionsrechts) | nur für Bereitstellungspflichten, die **nach dem 12.09.2025** in Kraft treten |
| Kapitel IV (Missbrauchskontrolle Art. 13) | Verträge, die **nach dem 12.09.2025** geschlossen wurden |
| Kapitel IV für Altverträge | ab **12.09.2027**, wenn der Vertrag unbefristet ist oder seine Geltungsdauer frühestens 10 Jahre nach dem 11.01.2024 endet |
| Wegfall der Wechselentgelte Art. 29 Abs. 1 | **12.01.2027**; bis dahin nur ermäßigte, kostendeckende Entgelte (Art. 29 Abs. 2, 3) |

**Deterministische Berechnung** siehe unten.

### 5. Zuständigkeit und Sanktionen nach dem DADG bestimmen

Deutschland hat die Verordnung mit dem **Gesetz zur Anwendung und Durchsetzung der Datenverordnung ([DADG](https://www.gesetze-im-internet.de/dadg/))** durchgeführt.

- **Zuständige Behörde und Datenkoordinator** ist nach [§ 2 Abs. 1 DADG](https://www.gesetze-im-internet.de/dadg/__2.html) die **Bundesnetzagentur**. Sie ist zentrale Anlaufstelle, bearbeitet Beschwerden nach Art. 38 Data Act, lässt Streitbeilegungsstellen nach Art. 10 Abs. 5 zu und prüft Datenverlangen öffentlicher Stellen des Bundes.
- Für Geldbußen wegen Verstößen mit Bezug zu personenbezogenen Daten ist nach [§ 16 DADG](https://www.gesetze-im-internet.de/dadg/__16.html) iVm Art. 40 Abs. 4 Data Act die oder der **BfDI** zuständig.
- Ermittlungs-, Auskunfts- und Durchsetzungsbefugnisse folgen aus [§§ 6 bis 14 DADG](https://www.gesetze-im-internet.de/dadg/__6.html), einschließlich vorläufiger Anordnungen (§ 11) und des Schutzes von Geschäftsgeheimnissen im Verfahren (§ 10).

**Bußgeldrahmen nach [§ 15 Abs. 4 bis 6 DADG](https://www.gesetze-im-internet.de/dadg/__15.html):**

| Verstoß | Rahmen |
|---|---|
| § 15 Abs. 2 Nr. 9 (Torwächter-Sperre Art. 5 Abs. 3) | bis **5 Mio. EUR**; bei Gesamtumsatz über 250 Mio. EUR bis **2 % des weltweiten Gesamtumsatzes** (§ 15 Abs. 5, 6) |
| u. a. Art. 3 Abs. 1, Art. 4 Abs. 1 S. 1, Art. 5 Abs. 1 S. 1 | bis **500.000 EUR** |
| weitere benannte Verstöße und § 15 Abs. 3 | bis **100.000 EUR** |
| übrige Fälle des § 15 Abs. 2 | bis **50.000 EUR** |

Verwaltungsbehörde iSd § 36 Abs. 1 Nr. 1 OWiG ist nach § 15 Abs. 7 DADG die Bundesnetzagentur.

### 6. Verhältnis zu den Nachbarrechtsordnungen klären

- **DSGVO.** Der Data Act schafft **keine** eigene Rechtsgrundlage für die Verarbeitung personenbezogener Daten. Ist der Nutzer nicht die betroffene Person, dürfen personenbezogene Daten nach Art. 5 Abs. 7 Data Act nur bereitgestellt werden, wenn eine gültige Rechtsgrundlage nach [Art. 6 DSGVO](https://eur-lex.europa.eu/eli/reg/2016/679/oj) – ggf. Art. 9 DSGVO und Art. 5 Abs. 3 RL 2002/58/EG – vorliegt. Vertiefung: `/datenschutzrecht:avv-pruefung`.
- **Geschäftsgeheimnisse.** Art. 4 Abs. 6 bis 8 und Art. 5 Abs. 9 bis 11 sehen ein abgestuftes Verfahren vor: Kennzeichnung, Vereinbarung technischer und organisatorischer Maßnahmen, ausnahmsweise Verweigerung. Der Schutz nach [§ 2 GeschGehG](https://www.gesetze-im-internet.de/geschgehg/__2.html) entfällt nicht, er wird prozeduralisiert.
- **Datenbankschutz.** Nach Art. 43 Data Act gilt das Schutzrecht sui generis nach Art. 7 RL 96/9/EG nicht für Datenbanken, die Produktdaten oder verbundene Dienstdaten enthalten. Das ist die Antwort auf die verbreitete Verteidigung „unsere Telemetriedatenbank ist nach §§ 87a ff. UrhG geschützt".
- **DGA.** Für Datenvermittlungsdienste und Datenaltruismus gilt die VO (EU) 2022/868, durchgeführt durch das [DGG](https://www.gesetze-im-internet.de/dgg/); auch dort ist die Bundesnetzagentur zuständig.

## Deterministische Berechnung

Die Stichtage des Art. 50 sind kalendarische Fixdaten, keine Fristen im Sinne der §§ 187 ff. BGB. Zu rechnen ist nur der **Ablauf** vertraglicher Übergangszeiträume — etwa die Zweimonatsfrist der Kündigung nach Art. 25 Abs. 2 Buchst. d oder die 30-Kalendertage-Übergangsfrist nach Art. 25 Abs. 2 Buchst. a. Der Rechner in [`../../../scripts/legal_calc/`](../../../scripts/legal_calc/) macht nur die Arithmetik:

```bash
# Maximale Kündigungsfrist Art. 25 Abs. 2 Buchst. d: 2 Monate ab Wechselverlangen
python -m scripts.legal_calc.cli frist --ereignis 12.01.2027 --menge 2 --einheit monate --land BY

# Anschließende Übergangsfrist Art. 25 Abs. 2 Buchst. a: höchstens 30 Kalendertage
python -m scripts.legal_calc.cli frist --ereignis 12.03.2027 --menge 30 --einheit tage --land BY
```

Ob der Vertrag als Altvertrag unter Art. 50 UAbs. 6 fällt, ist eine juristische Wertung und keine Rechenaufgabe.

## Quellen

### Rechtsakte

- Verordnung (EU) 2023/2854 (Datenverordnung / Data Act), insbesondere Art. 1, 2, 3, 4, 5, 7, 13, 23–31, 37, 38, 40, 43, 50 — [EUR-Lex](https://eur-lex.europa.eu/eli/reg/2023/2854/oj)
- [DADG](https://www.gesetze-im-internet.de/dadg/) – [§ 2 DADG](https://www.gesetze-im-internet.de/dadg/__2.html), [§ 6](https://www.gesetze-im-internet.de/dadg/__6.html), [§ 15](https://www.gesetze-im-internet.de/dadg/__15.html), [§ 16](https://www.gesetze-im-internet.de/dadg/__16.html)
- Verordnung (EU) 2022/868 (Daten-Governance-Rechtsakt) — [EUR-Lex](https://eur-lex.europa.eu/eli/reg/2022/868/oj); [DGG](https://www.gesetze-im-internet.de/dgg/)
- Verordnung (EU) 2016/679 (DSGVO), Art. 6, 9, 20 — [EUR-Lex](https://eur-lex.europa.eu/eli/reg/2016/679/oj)
- [GeschGehG](https://www.gesetze-im-internet.de/geschgehg/), [§ 2](https://www.gesetze-im-internet.de/geschgehg/__2.html)
- Empfehlung 2003/361/EG (KMU-Definition)

### Kommentare und Literatur

- Specht-Riemenschneider/Hennemann, in: Data Act, Kommentar, Art. 2, Art. 7, Art. 50.
- Hennemann/Steinrötter, Data Act – Handkommentar, Art. 4, Art. 13.
- Wiebe, in: Wiebe/Schur, Datenrecht, Kap. zum Data Act.
- Sattler, Data Act und DSGVO, ZD 2024 (konkrete Fundstelle vor Verwendung prüfen) `[unverifiziert – prüfen]`

### Rechtsprechung

Zum Data Act existiert bislang **keine gefestigte deutsche oder unionsgerichtliche Rechtsprechung**. Jede Entscheidung, die ein Modell zu diesem Rechtsakt nennt, ist bis zum Beleg in juris, Beck-Online oder curia.europa.eu als `[unverifiziert – prüfen]` zu behandeln. Zur Auslegung heranzuziehen sind stattdessen die Erwägungsgründe der Verordnung, die Kommissionsleitlinien und die Verlautbarungen der Bundesnetzagentur.

## Ausgabeformat

```
DATA-ACT-BETROFFENHEIT — <Mandant> — <Datum>

I.   Sachlicher Anwendungsbereich
     Produkt:                 <Bezeichnung>
     Vernetztes Produkt:      [ja / nein — Begründung]
     Verbundener Dienst:      [ja / nein — Begründung]
     Datenkategorien:         <Produktdaten / verbundene Dienstdaten / abgeleitete Daten>
     Personenbezug:           [ja / nein / teilweise]

II.  Rollen je Datenstrom
     Datenstrom 1: Nutzer <…> | Dateninhaber <…> | Dritter <…>
     Torwächter beteiligt:    [ja — Art. 5 Abs. 3 sperrt / nein]

III. Größenausnahme Art. 7 Abs. 1
     Einstufung:              <Kleinst / Klein / Mittel / Groß>
     Partner-/verbundenes Unternehmen: [ja — Ausnahme entfällt / nein]
     Unterauftragnehmer:      [ja — Ausnahme entfällt / nein]
     Ergebnis:                [Kapitel II anwendbar / nicht anwendbar]

IV.  Zeitliche Geltung Art. 50
     Art. 3 Abs. 1:           [einschlägig ab <Datum> / nicht einschlägig]
     Kapitel IV:              [Neuvertrag ab 12.09.2025 / Altvertrag ab 12.09.2027 / nicht erfasst]
     Art. 29 Wechselentgelte: [ermäßigt bis 11.01.2027 / entgeltfrei ab 12.01.2027]

V.   Zuständigkeit und Sanktionsrisiko
     Behörde:                 Bundesnetzagentur (§ 2 Abs. 1 DADG)
     Bußgeldrahmen:           <Zuordnung zu § 15 Abs. 4 bis 6 DADG>
     BfDI-Zuständigkeit:      [ja § 16 DADG / nein]

VI.  Schnittstellen
     DSGVO:                   <Rechtsgrundlage / offen>
     Geschäftsgeheimnisse:    <gekennzeichnet? Maßnahmen vereinbart?>
     Art. 43 (Datenbankrecht): <sui-generis-Schutz gesperrt?>

VII. Handlungsbedarf und Fristen
VIII.Risiko: 🟢 / 🟡 / 🔴 <Begründung>
IX.  Quellenverzeichnis
```

## Risiken / typische Fehler

- **Data Act als Datenschutzthema behandelt.** Die Verordnung erfasst auch nicht personenbezogene Daten und schafft umgekehrt keine Rechtsgrundlage nach Art. 6 DSGVO. Beide Regime sind nebeneinander zu prüfen.
- **Größenausnahme ohne Konzernprüfung bejaht.** Art. 7 Abs. 1 entfällt, sobald ein Partner- oder verbundenes Unternehmen kein Kleinst- oder Kleinunternehmen ist.
- **Geltungsbeginn pauschal auf den 12.09.2025 gesetzt.** Die Konzeptionspflicht des Art. 3 Abs. 1 greift erst für Produkte, die nach dem 12.09.2026 in Verkehr gebracht werden; Kapitel IV erfasst Altverträge erst ab dem 12.09.2027.
- **Rollen vermischt.** Die Zuordnung erfolgt je Datenstrom; eine pauschale Selbsteinordnung als „Dateninhaber" trägt die Prüfung nicht.
- **Geschäftsgeheimnis als Totalverweigerungsgrund.** Art. 4 Abs. 6 ff. verlangt zunächst Kennzeichnung und Schutzmaßnahmen; die Verweigerung ist die begründungsbedürftige Ausnahme und der Bundesnetzagentur mitzuteilen.
- **Sui-generis-Datenbankschutz behauptet.** Art. 43 Data Act sperrt ihn für Datenbanken mit Produkt- und verbundenen Dienstdaten.
- **Sanktionshöhe frei geschätzt.** Die Rahmen stehen in § 15 Abs. 4 bis 6 DADG und sind zu zitieren, nicht zu runden.
- **Rechtsprechung erfunden.** Zum Data Act gibt es sie noch kaum; jede Entscheidung ist zu belegen oder als `[unverifiziert – prüfen]` zu kennzeichnen.
