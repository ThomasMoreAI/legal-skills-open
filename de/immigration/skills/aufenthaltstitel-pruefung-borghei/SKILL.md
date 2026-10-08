---
name: aufenthaltstitel-pruefung-borghei
title: /migrationsrecht:aufenthaltstitel-pruefung
description: Prüfung der einschlägigen Aufenthaltstitel-Art nach AufenthG (Visum § 6, Aufenthaltserlaubnis § 7, Niederlassungserlaubnis § 9, Daueraufenthalt-EU § 9a, Blaue Karte EU § 18b, Chancenkarte § 20a) und der allgemeinen Erteilungsvoraussetzungen § 5 AufenthG, Entwurf von Antrag und Begründung an die Ausländerbehörde. Use when ein Drittstaatsangehöriger erstmalig oder zum Zweckwechsel einen Aufenthaltstitel benötigt oder die Verlängerung beantragt.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/migrationsrecht/skills/aufenthaltstitel-pruefung
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: immigration
language: de
---

# /migrationsrecht:aufenthaltstitel-pruefung

## Zweck

Der Skill ordnet ein Aufenthaltsanliegen einem konkreten Titel des AufenthG zu, prüft die **speziellen Erteilungsvoraussetzungen** des Titelzwecks (§§ 16 ff. Studium, §§ 18 ff. Erwerb, §§ 25 ff. humanitär, §§ 27 ff. Familie) und die **allgemeinen Erteilungsvoraussetzungen § 5 AufenthG** und entwirft einen begründeten Antrag an die Ausländerbehörde. Er adressiert typische Versagungsgründe (Ausweisungsinteresse, fehlende Identitätsklärung) frühzeitig.

## Eingaben

- Staatsangehörigkeit, Geburtsdatum, derzeitiger Aufenthaltsstatus (kein Titel / Visum / AE / NE / Duldung / Gestattung)
- Zweck des Aufenthalts (Studium / Erwerb / Familie / humanitär / Bleiberecht)
- Lebenslauf in Deutschland (Einreisedatum, bisherige Titel, Erwerbszeiten)
- Lebensunterhalt: Einkommensnachweise, Krankenversicherung, Wohnraum
- Identitätspapiere: Pass / Passersatz, Geburtsurkunde, ggf. legalisierte / apostillierte Urkunden
- Vorstrafen, laufende Ermittlungsverfahren, Sozialleistungen
- Bei Familiennachzug: Status des Stammberechtigten (Deutscher § 28, Drittstaatsangehöriger § 29, anerkannter Schutzberechtigter § 36a), Sprachnachweis A1 (§ 30 I Nr. 2)
- Bei Erwerb: Arbeitsvertragsangebot, Gehalt, ggf. anerkannte Qualifikation

## Sub-Agent-Architektur

Researcher liefert AufenthG-Statute, BVerwG-Rspr. (insb. 1. Senat), EuGH-Rspr. zur Familienzusammenführungs-RL und Daueraufenthalt-RL sowie Kommentarstellen (Bergmann/Dienelt, Hailbronner). Drafter ordnet den Titel zu, prüft § 5 AufenthG und entwirft den Antrag. Reviewer prüft, ob § 5 I Nr. 2 (Ausweisungsinteresse) und § 5 I Nr. 1a (Identitätsklärung) als typische Blocker adressiert sind.

## Ablauf

### 1. Status- und Zwecksortierung

Aktueller Status klären (§ 4 AufenthG: Erfordernis Aufenthaltstitel). Zweck identifizieren und der Titelfamilie zuordnen:

| Zweck | Einschlägige Norm |
|---|---|
| Visum (Einreise) | § 6 AufenthG |
| Studium / Sprachkurs | § 16b, § 16f AufenthG |
| Erwerbstätigkeit qualifiziert | § 18a, § 18b (Blaue Karte EU), § 19c AufenthG; FEG-Reform 2023 |
| Chancenkarte | § 20a AufenthG |
| Selbständigkeit | § 21 AufenthG |
| Humanitär – Abschiebungsverbot | § 25 III AufenthG (iVm § 60 V/VII) |
| Humanitär – Jugendliche / nachhaltige Integration / Chancen | §§ 25a, 25b, 25c AufenthG |
| Familiennachzug zu Deutschen | § 28 AufenthG |
| Ehegattennachzug | § 30 AufenthG (Sprachnachweis A1) |
| Kindernachzug | §§ 32, 33 AufenthG |
| Niederlassungserlaubnis | § 9 AufenthG (Regelfall nach 5 Jahren) |
| Daueraufenthalt-EU | § 9a AufenthG (RL 2003/109/EG) |

### 2. Spezielle Erteilungsvoraussetzungen prüfen

Pro Titelzweck die spezifischen Tatbestandsmerkmale. Beispiele:

- **Blaue Karte EU § 18b**: anerkannter Hochschulabschluss; Arbeitsvertrag/-angebot mit Gehaltsschwelle (jährlich angepasst, FEG-Reform 2023 – Schwellen prüfen)
- **Familiennachzug § 30**: bestehende Ehe, einfache Deutschkenntnisse A1, gesicherter Lebensunterhalt grds. erforderlich
- **§ 25b**: nachhaltige Integration, sechs- bzw. achtjähriger Voraufenthalt, hinreichende Deutschkenntnisse, Lebensunterhaltsbeitrag
- **§ 25c (Chancen-Aufenthalt)**: 18-monatiger Probetitel für am 31.10.2022 Geduldete, um Voraussetzungen für § 25a/b zu schaffen

### 3. Allgemeine Erteilungsvoraussetzungen § 5 AufenthG

Pflichtprüfung jedes Aufenthaltstitels:

- **§ 5 I Nr. 1 + 1a**: gesicherter Lebensunterhalt (§ 2 III) **und** Identitätsklärung (echte Identität, Passpflicht)
- **§ 5 I Nr. 2**: kein Ausweisungsinteresse iSv § 54 AufenthG (besonders schwerwiegende / schwerwiegende Interessen)
- **§ 5 I Nr. 4**: Passpflicht (§ 3 AufenthG)
- **§ 5 III**: bei humanitären Titeln Sonderregeln (z. B. Verzicht auf Pass/Lebensunterhalt bei § 25 I–III)

Reviewer-Blocker:

- **§ 5 I Nr. 2 AufenthG** (Ausweisungsinteresse) – jede Vorstrafe und jedes laufende Ermittlungsverfahren bewerten; Bagatell-Grenze klären
- **§ 5 I Nr. 1a AufenthG** (Identitätsklärung) – ohne echten Pass oder zumutbare Passbeschaffungsbemühungen scheitert der Anspruch idR

### 4. Visumverfahren und beteiligte Behörden

Vorabklärung: aus dem Ausland einreisende Drittstaatsangehörige benötigen idR ein Visum (§ 6 III). Visumverfahren über deutsche Auslandsvertretung, bei Erwerb Beteiligung der Bundesagentur für Arbeit (§ 39 AufenthG iVm BeschV). Stille Zustimmung der BA nach Ablauf der Frist möglich.

### 5. Ermessen und Atypik

Bei Sollvorschriften (§ 5 I "soll", aber Regelfall des Bestehens): atypische Umstände prüfen (z. B. Kindeswohl Art. 6 GG / Art. 8 EMRK). Bei Ermessensvorschriften: Ermessensspielraum mit allen abwägungserheblichen Belangen darstellen.

### 6. Antragsentwurf

Adressat: zuständige Ausländerbehörde am Wohnort. Antrag mit Anlagenverzeichnis (Pass, Lebensunterhaltsnachweis, Krankenversicherung, Mietvertrag, ggf. Arbeitsvertrag / Immatrikulation / Heiratsurkunde, Sprachnachweise).

## Quellen und Zitierweise

Verbindlich: [`../../../references/zitierweise.md`](../../../references/zitierweise.md).

### Statute

- [§ 4 AufenthG](https://www.gesetze-im-internet.de/aufenthg_2004/__4.html) (Erfordernis Aufenthaltstitel)
- [§ 5 AufenthG](https://www.gesetze-im-internet.de/aufenthg_2004/__5.html) (allgemeine Erteilungsvoraussetzungen)
- [§ 7 AufenthG](https://www.gesetze-im-internet.de/aufenthg_2004/__7.html) (Aufenthaltserlaubnis)
- [§ 9 AufenthG](https://www.gesetze-im-internet.de/aufenthg_2004/__9.html) (Niederlassungserlaubnis)
- [§ 9a AufenthG](https://www.gesetze-im-internet.de/aufenthg_2004/__9a.html) (Daueraufenthalt-EU)
- [§ 16b AufenthG](https://www.gesetze-im-internet.de/aufenthg_2004/__16b.html) (Studium)
- [§ 18b AufenthG](https://www.gesetze-im-internet.de/aufenthg_2004/__18b.html) (Blaue Karte EU)
- [§ 20a AufenthG](https://www.gesetze-im-internet.de/aufenthg_2004/__20a.html) (Chancenkarte)
- [§ 25 AufenthG](https://www.gesetze-im-internet.de/aufenthg_2004/__25.html) (humanitäre Aufenthalte)
- [§ 25a AufenthG](https://www.gesetze-im-internet.de/aufenthg_2004/__25a.html) (Jugendliche, Heranwachsende)
- [§ 25b AufenthG](https://www.gesetze-im-internet.de/aufenthg_2004/__25b.html) (nachhaltige Integration)
- [§ 25c AufenthG](https://www.gesetze-im-internet.de/aufenthg_2004/__25c.html) (Chancen-Aufenthalt)
- [§ 28 AufenthG](https://www.gesetze-im-internet.de/aufenthg_2004/__28.html) (Familiennachzug Deutsche)
- [§ 30 AufenthG](https://www.gesetze-im-internet.de/aufenthg_2004/__30.html) (Ehegattennachzug)
- [§ 54 AufenthG](https://www.gesetze-im-internet.de/aufenthg_2004/__54.html) (Ausweisungsinteresse)
- [RL 2003/109/EG](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32003L0109) (Daueraufenthalt-RL)
- [RL 2003/86/EG](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32003L0086) (Familienzusammenführungs-RL)

### Kommentare

- Dienelt, in: Bergmann/Dienelt, AuslR, Stand 2024, § 5 AufenthG Rn. 1 ff.
- Hailbronner, AuslR, Stand 2024, § 5 AufenthG Rn. 1 ff.
- Hofmann, in: NK-AuslR, 3. Aufl. 2023, § 5 AufenthG Rn. 1 ff.
- Maor, in: Huber/Mantel, AufenthG/AsylG, 3. Aufl. 2021, § 18b AufenthG Rn. 1 ff.

### Rechtsprechung

1. BVerwG, Urt. v. 22.02.2017 – 1 C 3.16, BVerwGE 157, 325 = NVwZ 2017, 1883 (**Ausweisung eines anerkannten Flüchtlings wegen Unterstützung der PKK** — nicht Bleiberecht nach § 25b AufenthG), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BVerwG&Datum=2017-02-22&Aktenzeichen=1%20C%203.16)
2. BVerwG, Urt. v. 16.11.2010 – 1 C 17.09, BVerwGE 138, 122 = NVwZ 2011, 495 (**Nachholung des Visumverfahrens** bei Ehegatten Deutscher; „erforderliches" Visum richtet sich nach dem tatsächlich verfolgten Aufenthaltszweck — nicht Identitätsklärung), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BVerwG&Datum=2010-11-16&Aktenzeichen=1%20C%2017.09)
3. EuGH, Urt. v. 04.03.2010 – Rs. C-578/08, Chakroun (Familienzusammenführung, RL 2003/86/EG, Begriff der Sozialhilfe), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=EuGH&Datum=2010-03-04&Aktenzeichen=C-578/08)
4. EuGH, Urt. v. 27.06.2006 – Rs. C-540/03, Parlament/Rat (Familienzusammenführungs-RL 2003/86/EG, Kindeswohl und Achtung des Familienlebens), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=EuGH&Datum=2006-06-27&Aktenzeichen=C-540/03)
5. EGMR, Urt. v. 18.10.2006 – Nr. 46410/99, Üner ./. NL (Ausweisung, Art. 8 EMRK), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=EGMR&Datum=2006-10-18&Aktenzeichen=46410/99)

## Ausgabeformat

```
GUTACHTEN — Aufenthaltstitel-Prüfung
Mandant: <anonymisiert, Staatsangehörigkeit, Status>
Stand: <Datum>

I. Sachverhalt (knapp)

II. Frage(n)
    – Welche Titelart kommt in Betracht?
    – Sind die allgemeinen Voraussetzungen § 5 AufenthG erfüllt?
    – Welche Anlagen sind beizubringen?

III. Kurzantwort
     – Einschlägiger Titel: § N AufenthG
     – Voraussichtliche Erfolgsaussicht: 🟢 / 🟡 / 🔴

IV. Rechtliche Bewertung
    1. Aktueller Status (§ 4 AufenthG)
    2. Spezielle Voraussetzungen (Zweck, § ... AufenthG)
    3. Allgemeine Voraussetzungen § 5 AufenthG
       a) Lebensunterhalt § 2 III, § 5 I Nr. 1
       b) Identitätsklärung § 5 I Nr. 1a
       c) Ausweisungsinteresse § 5 I Nr. 2 iVm § 54
       d) Passpflicht § 5 I Nr. 4
    4. Ermessen / Atypik (§ 5 III, ggf. Härtefall)
    5. Verfahren (Visum § 6 III, Beteiligung BA § 39, Zuständigkeit ABH)

V. Antragsentwurf (separat unten)

VI. Anlagenverzeichnis

VII. Risiken / offene Punkte
     🟢 / 🟡 / 🔴 mit Begründung
     – Frist (Verlängerungsantrag rechtzeitig vor Ablauf des Vor-Titels!)

VIII. Quellenverzeichnis
```

## Beispiel (gekürzt)

> **Sachverhalt:** Mandantin M. (Indien, 32 J., Informatikerin) hat Arbeitsvertragsangebot eines deutschen IT-Unternehmens mit Bruttojahresgehalt 60.000 €. Hochschulabschluss (M.Sc.) wird durch ANABIN als H+ bewertet. Sie befindet sich derzeit in Indien.
>
> **Bewertung:** Einschlägig ist die **Blaue Karte EU nach § 18b AufenthG**. Anerkannter Hochschulabschluss (+); Arbeitsvertrag mit ausreichend hohem Bruttogehalt (Schwellenwert nach FEG-Reform 2023 prüfen – jährlich angepasst, vgl. BAMF-Tabelle) (+). Allgemeine Voraussetzungen § 5 AufenthG: Lebensunterhalt durch Gehalt gesichert (+); Pass vorhanden (+); kein Ausweisungsinteresse erkennbar (+).
>
> **Verfahren:** Visumverfahren über die Deutsche Botschaft Neu-Delhi (§ 6 III AufenthG); Vorabzustimmung der BA grds. nicht erforderlich, da Blaue Karte EU bei Schwellenüberschreitung zustimmungsfrei (§ 39 II AufenthG iVm BeschV).
>
> **Risikoeinstufung:** 🟢 niedrig.

## Risiken / typische Fehler

- **Übersehen des Ausweisungsinteresses § 5 I Nr. 2**: jede Vorstrafe, jedes laufende Ermittlungsverfahren bewerten; Bagatellgrenze klären.
- **Identitätsklärung § 5 I Nr. 1a nicht thematisiert**: häufiger Versagungsgrund, insb. bei Bestandsduldungen.
- **Veraltete Gehaltsschwellen** bei Blauer Karte EU (jährlich angepasst, FEG-Reform 2023).
- **Falsche Titelart**: § 25b und § 25c werden häufig verwechselt; § 25c ist 18-monatiger Probetitel, § 25b ist Bleiberecht bei bereits nachhaltiger Integration.
- **Sprachnachweis Ehegattennachzug § 30 I Nr. 2** vergessen oder Ausnahmen / Härtefall nicht geprüft.
- **Verlängerungsantrag verspätet**: nach Ablauf des Vor-Titels nur noch Fiktionsbescheinigung § 81 IV, bei verspätetem Antrag droht Lücke und ggf. Ausreisepflicht.
