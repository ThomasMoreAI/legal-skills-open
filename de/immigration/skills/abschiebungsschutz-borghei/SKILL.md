---
name: abschiebungsschutz-borghei
title: /migrationsrecht:abschiebungsschutz
description: Eilrechtsschutz gegen drohende Abschiebung und Duldungsantrag – § 80 V VwGO (insb. § 36 III AsylG 1-Wochen-Frist), § 123 VwGO, Duldung § 60a AufenthG, krankheitsbedingte Verbote § 60 VII AufenthG mit qualifizierter ärztlicher Bescheinigung § 60a IIc, Familienschutz Art. 6 GG / Art. 8 EMRK, EGMR Rule 39 als ultima ratio. Use when ein BAMF-Bescheid mit Abschiebungsandrohung zugestellt ist, eine Abschiebung unmittelbar droht oder Duldungsgründe entstanden sind.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/migrationsrecht/skills/abschiebungsschutz
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: immigration
language: de
---

# /migrationsrecht:abschiebungsschutz

## Zweck

Der Skill identifiziert den richtigen Eilrechtsbehelf gegen eine drohende Abschiebung (§ 80 V VwGO bei vollziehbarer Abschiebungsandrohung; § 123 VwGO bei drohender Abschiebung ohne anhängigen Verwaltungsakt; Duldung § 60a AufenthG bei rechtlicher oder tatsächlicher Unmöglichkeit), berechnet die zwingenden Fristen (insb. **§ 36 III AsylG 1 Woche**, § 74 I AsylG 2 Wochen, § 74 I VwGO 1 Monat) und entwirft den Antrag samt Begründung. Er adressiert zielstaatsbezogene Verbote (§ 60 V/VII AufenthG, Art. 3 EMRK) und inlandsbezogene Hindernisse (Reisefähigkeit, Familie Art. 6 GG / Art. 8 EMRK, Kindeswohl).

## Eingaben

- Aufenthaltsstatus (Gestattung / Duldung / kein Titel)
- Vorliegender Bescheid (BAMF mit Abschiebungsandrohung § 34 AsylG / Abschiebungsanordnung § 34a / ABH mit Versagung der AE und Ausreiseaufforderung)
- Zustellungsdatum des Bescheids (Frist!)
- Konkrete Abschiebungsmaßnahme (Termin bekannt? Abschiebungsversuch absehbar?)
- Gesundheitszustand, ärztliche Bescheinigungen (insb. § 60a IIc-konform)
- Familiäre Bindungen in DE (Ehegatte, minderjährige Kinder mit deutschem Pass oder gesichertem Status)
- Identitätspapiere, Passersatz
- Bei Dublin: Eurodac-Treffer, Überstellungsfrist Art. 29 VO 604/2013

## Sub-Agent-Architektur

Researcher liefert VwGO-, AsylG-, AufenthG-Statute, BVerwG- und EGMR-Rspr. (Soering, M.S.S., Üner / Boultif) sowie Kommentarstellen (Bergmann/Dienelt zu § 60, § 60a; Hailbronner). Drafter entwirft Antrag und Begründung, sortiert ziel- und inlandsbezogene Hindernisse. Reviewer prüft Frist-Kalender (**1 Woche § 36 III AsylG = Blocker**) und Vorliegen einer qualifizierten ärztlichen Bescheinigung bei § 60 VII-Argumentation.

## Ablauf

### 1. Antragsart bestimmen

| Konstellation | Eilrechtsbehelf |
|---|---|
| BAMF-Ablehnung als offensichtlich unbegründet § 30 AsylG + Abschiebungsandrohung § 34 | § 80 V VwGO iVm § 36 III AsylG – **1 Woche** ab Zustellung |
| BAMF-Unzulässigkeit Dublin § 29 I Nr. 1 + Abschiebungsanordnung § 34a | § 80 V VwGO iVm § 34a II AsylG – **1 Woche** |
| BAMF-Ablehnung als unbegründet § 31 (nicht "offensichtlich") | Klage § 74 I AsylG **2 Wochen**; aufschiebende Wirkung kraft Gesetzes § 75 I |
| ABH-Bescheid (z. B. Versagung AE-Verlängerung mit Ausreiseaufforderung) | § 80 V VwGO; Frist 1 Monat § 74 VwGO; **§ 84 AufenthG-Liste** prüfen (sofortige Vollziehbarkeit kraft Gesetz) |
| Drohende Abschiebung ohne anhängigen Verwaltungsakt | § 123 VwGO (einstweilige Anordnung); Sicherungs- oder Regelungsanordnung |
| Bei der Ausländerbehörde: Duldungsantrag | § 60a AufenthG (rechtliche / tatsächliche Unmöglichkeit) |
| Letzter Notfall (Flug innerhalb von Stunden) | EGMR Rule 39 (interim measure) – ultima ratio |

### 2. Frist-Block (zwingend in jedem Entwurf)

- **§ 36 III AsylG: 1 Woche** Eilantrag + 1 Woche Klage bei offensichtlich unbegründet § 30
- **§ 34a II AsylG: 1 Woche** Eilantrag bei Dublin-Abschiebungsanordnung
- **§ 74 I AsylG: 2 Wochen** Klagefrist (bzw. 1 Woche bei § 36-Fällen)
- **§ 74 I VwGO: 1 Monat** Klagefrist bei AufenthG-Verwaltungsakten
- **Wiedereinsetzung § 60 VwGO** prüfen, wenn Frist versäumt – aber strikte Voraussetzungen
- **Dublin-Überstellungsfrist Art. 29 VO 604/2013 (6 / 12 / 18 Monate)** – Fristablauf = Zuständigkeitsübergang

### 3. Zielstaatsbezogene Abschiebungsverbote

- **§ 60 V AufenthG iVm Art. 3 EMRK** – unmenschliche oder erniedrigende Behandlung im Zielstaat (EGMR, Urt. v. 07.07.1989 – Nr. 14038/88, Soering ./. UK, [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=EGMR&Datum=1989-07-07&Aktenzeichen=14038/88); EGMR, Urt. v. 21.01.2011 – Nr. 30696/09, M.S.S. ./. Belgien und Griechenland, [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=EGMR&Datum=2011-01-21&Aktenzeichen=30696/09))
- **§ 60 VII S. 1 AufenthG** – erhebliche konkrete Gefahr für Leib, Leben, Freiheit
- **§ 60 VII S. 3, 4 AufenthG (krankheitsbedingt)** – wesentliche Verschlechterung lebensbedrohlicher / schwerwiegender Erkrankungen
  - **Qualifizierte ärztliche Bescheinigung § 60a IIc / IId AufenthG** zwingend: aktuelle ärztliche Diagnose, Behandlungsbedarf, Folgen bei Unterbrechung, fehlende Behandlungsmöglichkeit im Zielstaat
  - Atteste eines Hausarztes ohne diese Spezifika genügen idR **nicht**

### 4. Inlandsbezogene Abschiebungshindernisse

- **Reisefähigkeit** (medizinisch): nicht zielstaat-, sondern reisebezogen
- **Familie Art. 6 GG / Art. 8 EMRK**: Ehegatte / minderjährige Kinder mit deutscher Staatsangehörigkeit oder gesichertem Aufenthalt; Verhältnismäßigkeit (EGMR, Urt. v. 18.10.2006 – Nr. 46410/99, Üner ./. NL, [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=EGMR&Datum=2006-10-18&Aktenzeichen=46410/99); EGMR, Urt. v. 02.08.2001 – Nr. 54273/00, Boultif ./. CH, [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=EGMR&Datum=2001-08-02&Aktenzeichen=54273/00))
- **Kindeswohl** Art. 24 GRCh, UN-KRK
- **Passersatzbeschaffung / Identitätsklärung**: tatsächliche Unmöglichkeit → § 60a II Duldung

### 5. Duldungsantrag § 60a AufenthG

Bei rechtlicher oder tatsächlicher Unmöglichkeit der Abschiebung. Wichtige Untertypen:

- **Ausbildungsduldung § 60c**
- **Beschäftigungsduldung § 60d**
- **Duldung für Personen mit ungeklärter Identität § 60b** (verschärfte Folgen)
- Übergang zu **Chancen-Aufenthalt § 25c** prüfen

### 6. Schriftsatzentwurf

Adressat: zuständiges Verwaltungsgericht (in Asylsachen idR Gericht am Sitz der Außenstelle BAMF). Antrag voran (Urteilsstil), dann chronologische Begründung. Beweismittel: ärztliche Bescheinigung (§ 60a IIc-konform), Heiratsurkunde, Geburtsurkunde, Schulbescheinigung Kinder, Sprachstandsnachweise, Länderberichte (BFA, ACCORD, ECOI).

### 7. EGMR Rule 39 (ultima ratio)

Nur wenn drohende, irreversible Verletzung Art. 2 / 3 EMRK und innerstaatlicher Rechtsweg erschöpft / nicht effektiv. Antrag an EGMR per Fax / sicherem Kanal mit Begründung und Bescheid; idR innerhalb von Stunden.

## Quellen und Zitierweise

Verbindlich: [`../../../references/zitierweise.md`](../../../references/zitierweise.md).

### Statute

- [§ 60 AufenthG](https://www.gesetze-im-internet.de/aufenthg_2004/__60.html) (Verbot der Abschiebung)
- [§ 60a AufenthG](https://www.gesetze-im-internet.de/aufenthg_2004/__60a.html) (Duldung; insb. Abs. IIc, IId – qualifizierte ärztliche Bescheinigung)
- [§ 60b AufenthG](https://www.gesetze-im-internet.de/aufenthg_2004/__60b.html) (Duldung bei ungeklärter Identität)
- [§ 60c AufenthG](https://www.gesetze-im-internet.de/aufenthg_2004/__60c.html) (Ausbildungsduldung)
- [§ 60d AufenthG](https://www.gesetze-im-internet.de/aufenthg_2004/__60d.html) (Beschäftigungsduldung)
- [§ 34 AsylG](https://www.gesetze-im-internet.de/asylvfg_1992/__34.html), [§ 34a](https://www.gesetze-im-internet.de/asylvfg_1992/__34a.html), [§ 36](https://www.gesetze-im-internet.de/asylvfg_1992/__36.html) (Abschiebungsandrohung / -anordnung / Eilrechtsschutz)
- [§ 74 AsylG](https://www.gesetze-im-internet.de/asylvfg_1992/__74.html) (Klagefrist), [§ 75](https://www.gesetze-im-internet.de/asylvfg_1992/__75.html) (aufschiebende Wirkung)
- [§ 80 VwGO](https://www.gesetze-im-internet.de/vwgo/__80.html) (aufschiebende Wirkung / Anordnung), [§ 80a](https://www.gesetze-im-internet.de/vwgo/__80a.html), [§ 80b](https://www.gesetze-im-internet.de/vwgo/__80b.html)
- [§ 123 VwGO](https://www.gesetze-im-internet.de/vwgo/__123.html) (einstweilige Anordnung)
- [§ 74 VwGO](https://www.gesetze-im-internet.de/vwgo/__74.html), [§ 60](https://www.gesetze-im-internet.de/vwgo/__60.html) (Wiedereinsetzung)
- [§ 84 AufenthG](https://www.gesetze-im-internet.de/aufenthg_2004/__84.html) (keine aufschiebende Wirkung bestimmter AufenthG-Akte)
- [Art. 6 GG](https://www.gesetze-im-internet.de/gg/art_6.html), [Art. 19 IV GG](https://www.gesetze-im-internet.de/gg/art_19.html)
- [Art. 3 EMRK](https://www.echr.coe.int/documents/d/echr/convention_deu), Art. 8 EMRK
- [Art. 29 VO (EU) 604/2013](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32013R0604) (Überstellungsfristen)

### Kommentare

- Bauer, in: Bergmann/Dienelt, AuslR, Stand 2024, § 60a AufenthG Rn. 1 ff. (Duldung)
- Bergmann, in: Bergmann/Dienelt, AuslR, Stand 2024, § 60 AufenthG Rn. 1 ff. (Abschiebungsverbote)
- Hailbronner, AuslR, Stand 2024, § 60 AufenthG Rn. 1 ff.
- Hofmann, in: NK-AuslR, 3. Aufl. 2023, § 60 AufenthG Rn. 1 ff.
- Funke-Kaiser, in: GK-AsylG, Stand 2024, § 36 Rn. 1 ff.

### Rechtsprechung

1. EGMR, Urt. v. 07.07.1989 – Nr. 14038/88, Soering ./. UK (Art. 3 EMRK, drohende Misshandlung im Zielstaat), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=EGMR&Datum=1989-07-07&Aktenzeichen=14038/88)
2. EGMR, Urt. v. 21.01.2011 – Nr. 30696/09, M.S.S. ./. Belgien und Griechenland (Art. 3 und Art. 13 EMRK, systemische Mängel des griechischen Asylsystems), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=EGMR&Datum=2011-01-21&Aktenzeichen=30696/09)
3. EGMR, Urt. v. 18.10.2006 – Nr. 46410/99, Üner ./. NL (Art. 8 EMRK, Ausweisung langjährig Aufhältiger), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=EGMR&Datum=2006-10-18&Aktenzeichen=46410/99)
4. EGMR, Urt. v. 02.08.2001 – Nr. 54273/00, Boultif ./. CH (Verhältnismäßigkeit Ausweisung, Art. 8 EMRK), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=EGMR&Datum=2001-08-02&Aktenzeichen=54273/00)
5. BVerwG, Urt. v. 25.11.1997 – 9 C 58.96, BVerwGE 105, 383 = NVwZ 1998, 524 (zielstaatsbezogenes Abschiebungshindernis bei unzureichenden Behandlungsmöglichkeiten; ergangen zu § 53 Abs. 6 S. 1 AuslG, heute § 60 VII AufenthG), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BVerwG&Datum=1997-11-25&Aktenzeichen=9%20C%2058.96)
6. BVerwG, Urt. v. 17.10.2006 – 1 C 18.05, BVerwGE 127, 33 = NVwZ 2007, 712 (Abschiebungsverbot § 60 VII AufenthG wegen Verschlimmerung einer Erkrankung im Zielstaat — **zielstaatsbezogen**, nicht inlandsbezogene Reisefähigkeit), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BVerwG&Datum=2006-10-17&Aktenzeichen=1%20C%2018.05)
7. BVerfG, Beschl. v. 17.09.2014 – 2 BvR 939/14, NVwZ 2014, 1511 (Dublin-Überstellung nach Italien; Pflicht zur Prüfung ziel- **und** inlandsbezogener Abschiebungshindernisse, ggf. Zusicherung des Zielstaats), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BVerfG&Datum=2014-09-17&Aktenzeichen=2%20BvR%20939/14)

## Ausgabeformat

```
EILANTRAG / SCHRIFTSATZ — Abschiebungsschutz
An: <Verwaltungsgericht>
Mandant: <anonymisiert, Az.>
Zustellungsdatum des Bescheids: <Datum>
Frist-Ablauf: <Datum + 1 Woche / 2 Wochen / 1 Monat>

I. Anträge
   1. Die aufschiebende Wirkung der Klage gegen den Bescheid des BAMF
      vom <Datum>, Az. <…>, wird angeordnet (§ 80 V S. 1 Alt. 1 VwGO
      iVm § 36 III AsylG).
   2. Hilfsweise: einstweilige Anordnung gem. § 123 VwGO, dass die
      Antragsgegnerin keine Abschiebung in <Zielstaat> vor
      rechtskräftiger Entscheidung in der Hauptsache vollzieht.

II. Begründung

   1. Zulässigkeit
      – Statthafte Antragsart (§ 80 V VwGO / § 123 VwGO)
      – Antragsfrist (§ 36 III AsylG – Tag der Zustellung + 1 Woche)
      – Antragsbefugnis § 42 II VwGO analog

   2. Begründetheit
      a) Ernstliche Zweifel an der Rechtmäßigkeit des Bescheids
         (§ 36 IV AsylG)
      b) Zielstaatsbezogene Hindernisse
         – § 60 V AufenthG iVm Art. 3 EMRK
         – § 60 VII S. 1 / S. 3 AufenthG (krankheitsbedingt)
      c) Inlandsbezogene Hindernisse
         – Reisefähigkeit
         – Art. 6 GG / Art. 8 EMRK
         – Kindeswohl
      d) Dublin-Überstellungsfrist Art. 29 VO 604/2013 (sofern relevant)

III. Beweismittel / Anlagen
   – qualifizierte ärztliche Bescheinigung (§ 60a IIc AufenthG)
   – Heiratsurkunde / Geburtsurkunde Kinder
   – Sprachstandsnachweise, Schulbescheinigungen
   – Länderberichte (BFA, ACCORD, ECOI)

IV. Frist-Block
   – Eilantrag: spätestens <Datum>
   – Hauptsacheklage: spätestens <Datum>
   – Dublin-Überstellungsfrist-Ablauf: <Datum>

V. Risikoeinstufung
   🟢 / 🟡 / 🔴 mit Begründung

VI. Quellenverzeichnis
```

## Beispiel (gekürzt)

> **Sachverhalt:** Der Bescheid des BAMF vom <Datum>, zugestellt am <Datum>, lehnt den Asylantrag als offensichtlich unbegründet (§ 30 AsylG) ab und droht die Abschiebung in den Iran an (§ 34 AsylG). Der Mandant leidet ausweislich qualifizierter ärztlicher Bescheinigung an einer schweren koronaren Herzerkrankung mit Reanimationsbedürftigkeit; eine adäquate Behandlung im Zielstaat ist nicht gesichert.
>
> **Antragsart und Frist:** Eilantrag § 80 V VwGO iVm **§ 36 III AsylG, Frist 1 Woche** ab Zustellung. Frist-Ablauf: <Datum>. **Hochrisiko-Frist (🔴)** – Eintrag in Fristenkalender mit Wiedervorlage zwei Tage vor Ablauf.
>
> **Begründetheit:** Ernstliche Zweifel an der Rechtmäßigkeit des Bescheids (§ 36 IV AsylG) bestehen, weil das BAMF die qualifizierte ärztliche Bescheinigung im Sinne § 60a IIc AufenthG nicht hinreichend gewürdigt hat. § 60 VII S. 3 AufenthG (krankheitsbedingtes Abschiebungsverbot) ist tragfähig: lebensbedrohliche Erkrankung; wesentliche Verschlechterung bei Behandlungsunterbrechung; keine gesicherte Behandlungsmöglichkeit im Zielstaat (Beleg: aktueller BFA-Länderbericht Iran, Kapitel Gesundheitsversorgung, S. ...).

## Risiken / typische Fehler

- **1-Wochen-Frist § 36 III AsylG übersehen** – häufigster und tödlichster Fehler.
- **Ärztliche Bescheinigung nicht § 60a IIc-konform** (Hausarzt-Attest ohne Diagnose-/Folgenangabe) → Bescheinigung untauglich.
- **§ 84 AufenthG-Liste übersehen**: bei dort genannten Verwaltungsakten besteht **keine** aufschiebende Wirkung kraft Gesetz – § 80 V VwGO **zwingend** zu stellen.
- **§ 123 VwGO statt § 80 V VwGO** (oder umgekehrt) – Antragsart sorgfältig wählen.
- **Dublin-Überstellungsfrist** nicht bewacht – Fristablauf führt zum Zuständigkeitsübergang; Versäumnis schadet dem Mandanten in der prozessualen Argumentation.
- **EGMR Rule 39** als Routinetool eingesetzt → wird vom EGMR nur in echten Notfällen gewährt; Reputation des Verfahrensbevollmächtigten.
- **Wiedereinsetzung § 60 VwGO** nach versäumter Frist nur unter sehr strikten Voraussetzungen; Verschulden des Bevollmächtigten wird zugerechnet.
- **Verhältnismäßigkeit Art. 8 EMRK** ohne konkrete Üner / Boultif-Kriterien (Dauer Aufenthalt, Integration, familiäre Bindung, Schwere der Pflichtverletzung) nicht überzeugend.
