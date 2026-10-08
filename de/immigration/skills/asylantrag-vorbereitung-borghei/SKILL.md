---
name: asylantrag-vorbereitung-borghei
title: /migrationsrecht:asylantrag-vorbereitung
description: Vorbereitung des Asylantrags und der BAMF-Anhörung § 25 AsylG – Triage Dublin-VO 604/2013, Flüchtlingseigenschaft § 3 AsylG, Asylberechtigung Art. 16a GG, subsidiärer Schutz § 4 AsylG, nationale Abschiebungsverbote § 60 V/VII AufenthG, Folgeantrag § 71 AsylG. Use when ein Asylantrag erstmalig gestellt werden soll, eine BAMF-Anhörung ansteht oder ein Folgeantrag wegen neuer Sachlage erwogen wird.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/migrationsrecht/skills/asylantrag-vorbereitung
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: immigration
language: de
---

# /migrationsrecht:asylantrag-vorbereitung

## Zweck

Der Skill bereitet einen Asylantrag und die BAMF-Anhörung nach § 25 AsylG vor: Dublin-Vorprüfung (§ 29 I Nr. 1 AsylG iVm VO (EU) Nr. 604/2013), Triage der Schutzformen (Flüchtlingseigenschaft § 3 AsylG → Asylberechtigung Art. 16a GG → subsidiärer Schutz § 4 AsylG → Abschiebungsverbote § 60 V/VII AufenthG), Strukturierung der Verfolgungsgeschichte und Aufbereitung der Beweismittel. Er adressiert ferner den Folgeantrag § 71 AsylG bei neuer Sachlage. Er ersetzt **nicht** die persönliche Anhörung; er strukturiert sie.

## Eingaben

- Staatsangehörigkeit, Herkunftsort, Volkszugehörigkeit, Religion, Geburtsdatum
- Einreisedatum, Einreiseweg (insb. EU-Drittstaaten zur Dublin-Prüfung), Eurodac-Treffer
- Verfolgungsgeschichte chronologisch (Wer? Wann? Wo? Was? Warum?)
- Beweismittel (Atteste, Dokumente, Zeugenangaben, Länderberichte, Fotos)
- Verfahrensstand BAMF (Antragstellung § 14 erfolgt? Anhörungstermin? Bescheid bereits ergangen?)
- Bei Folgeantrag: Neue Sachlage / neue Beweismittel; Datum Kenntnis (Frist § 71 IV AsylG iVm § 51 II, III VwVfG: 3 Monate)
- Gesundheitszustand: psychische / körperliche Erkrankungen, traumatherapeutische Befunde

## Sub-Agent-Architektur

Researcher liefert AsylG-Statute, Dublin-VO, Qualifikations- und Verfahrens-RL, BVerwG-, EuGH- und EGMR-Rspr. sowie Kommentarstellen (GK-AsylG, Marx, NK-AuslR Hofmann). Drafter strukturiert die Verfolgungsgeschichte chronologisch, prüft die Schutzformen-Triage und entwirft Schriftsätze / Stellungnahmen. Reviewer prüft Frist-Kalender (insb. Dublin-Überstellungsfristen und § 71 IV) und ob die Verfolgungsgeschichte ohne Suggestion strukturiert ist.

## Ablauf

### 1. Antragstellung und Zuständigkeit

- **Asylantrag § 13 AsylG**: schriftlich oder mündlich; gilt zugleich als Asylgesuch
- **Antragstellung beim BAMF § 14 AsylG**: persönliche Antragstellung in der zuständigen Außenstelle
- **Aufenthaltsgestattung § 55 AsylG** entsteht kraft Gesetz mit Asylgesuch
- Sprachmittler nach § 17 AsylG; Mandantenkommunikation idR über Dolmetscher

### 2. Dublin-Vorprüfung (VO (EU) Nr. 604/2013)

- **Zuständigkeitskriterien** Art. 7 ff. Dublin III (Familienkriterien, vorheriges Visum, Ersteinreise, freier Aufenthalt)
- **Eurodac-Treffer Kat. 1 / Kat. 2** in anderem Mitgliedstaat? – Wiederaufnahmegesuch / Aufnahmegesuch
- **Selbsteintritt Art. 17 Dublin III**: politische Souveränität DE; in Praxis bei systemischen Mängeln (EuGH, Urt. v. 21.12.2011 – verb. Rs. C-411/10, C-493/10, N.S. u.a., [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=EuGH&Datum=2011-12-21&Aktenzeichen=C-411/10); EuGH, Urt. v. 19.03.2019 – Rs. C-163/17, Jawo, [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=EuGH&Datum=2019-03-19&Aktenzeichen=C-163/17)) oder bei Familieneinheit
- **Überstellungsfristen Art. 29 Dublin III**: **6 Monate** Standard; **12 Monate** bei Haft; **18 Monate** bei Flucht. Fristablauf = Zuständigkeitsübergang auf DE.
- Unzulässigkeitsentscheidung § 29 I Nr. 1 AsylG mit Abschiebungsanordnung § 34a → **1 Woche** Eilantrag § 80 V VwGO iVm § 34a II AsylG

### 3. Schutzformen-Triage

**Vorrangig prüfen (Standardreihenfolge BAMF):**

- **a) Flüchtlingseigenschaft § 3 AsylG** (RL 2011/95/EU)
  - Verfolgung wegen Rasse, Religion, Nationalität, politischer Überzeugung, Zugehörigkeit zu sozialer Gruppe (§ 3 I)
  - **Verfolgungshandlungen § 3a** (schwerwiegende Menschenrechtsverletzungen)
  - **Akteure § 3c**: Staat, Parteien/Organisationen, nichtstaatliche Akteure (wenn Staat/internat. Org. erwiesenermaßen nicht schutzfähig oder schutzwillig)
  - **Interner Schutz § 3e**: kein Anspruch, wenn vernünftiger Weise in anderen Landesteil ausweichbar
- **b) Asylberechtigung Art. 16a GG**
  - **Subsidiär gegenüber § 3 AsylG** und wegen **Drittstaatenregelung Art. 16a II GG / § 26a AsylG** in der Praxis selten einschlägig (Einreise aus EU = sicherer Drittstaat)
- **c) Subsidiärer Schutz § 4 AsylG** (RL 2011/95/EU)
  - **Ernsthafter Schaden**: (1) Todesstrafe, (2) Folter/unmenschliche oder erniedrigende Behandlung, (3) ernsthafte individuelle Bedrohung des Lebens / der Unversehrtheit infolge willkürlicher Gewalt im internen / internationalen bewaffneten Konflikt (EuGH, Urt. v. 17.02.2009 – Rs. C-465/07, Elgafaji, [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=EuGH&Datum=2009-02-17&Aktenzeichen=C-465/07))
- **d) Nationale Abschiebungsverbote**
  - **§ 60 V AufenthG**: Verstoß gegen EMRK (idR Art. 3) im Zielstaat
  - **§ 60 VII S. 1 AufenthG**: erhebliche konkrete Gefahr für Leib, Leben, Freiheit
  - **§ 60 VII S. 3, 4 AufenthG**: krankheitsbedingte Gefahr – **wesentliche Verschlechterung**; **qualifizierte ärztliche Bescheinigung** nach § 60a IIc, IId AufenthG erforderlich

### 4. Verfolgungsgeschichte strukturieren

Anforderungen an die Glaubhaftigkeit: **schlüssig, widerspruchsfrei, detailreich, ohne Suggestion**. Strukturieren entlang:

- Chronologisch (vor / während / nach den Ereignissen)
- Akteur (Wer hat verfolgt?)
- Anknüpfungsmerkmal § 3b AsylG (Rasse / Religion / politische Überzeugung etc.)
- Beweismittel pro Sachverhaltsknoten

**Wichtig:** Der Drafter **erfindet keine Fakten** und gibt **keine vorformulierten Antworten** für die Anhörung. Er strukturiert nur, was vom Mandanten kommt. Dolmetscher zwingend erforderlich.

### 5. Anhörungsvorbereitung § 25 AsylG

- Aufklärung des Mandanten über Ablauf, Dauer, Rolle des Dolmetschers, Mitwirkungspflicht § 15 AsylG
- Trauma-sensible Vorbereitung (Pausen, ggf. weibliche Anhörerin / Dolmetscherin nach § 17a)
- Hinweis: § 25 V – Niederschrift wird rückübersetzt; Korrekturpflicht
- Beweismittel / Atteste vor der Anhörung beim BAMF einreichen

### 6. Folgeantrag § 71 AsylG

- **Frist 3 Monate ab Kenntnis** der neuen Sachlage / Beweismittel (§ 71 IV iVm § 51 III VwVfG)
- Voraussetzungen § 51 I VwVfG: nachträgliche Sachlagenänderung; neue Beweismittel; Wiederaufnahmegründe
- Kein Anspruch auf Anhörung; aber Möglichkeit einer schriftlichen Stellungnahme
- Risiko: Ablehnung als unzulässig § 29 I Nr. 5 → 1-Wochen-Eilantrag bei Abschiebungsandrohung

### 7. Bescheid-Ausblick und Folgefristen

- Stattgabe → Aufenthaltserlaubnis § 25 I (Asyl), II (Flüchtling / subsidiärer Schutz), III (Abschiebungsverbot) AufenthG
- Ablehnung als unbegründet § 31 II → **2 Wochen** Klagefrist § 74 I AsylG; aufschiebende Wirkung der Klage § 75 I
- Ablehnung als **offensichtlich unbegründet § 30** → **1 Woche** Klage und Eilantrag § 36 III AsylG
- Dublin-Unzulässigkeit § 29 I Nr. 1 → **1 Woche** Eilantrag § 34a II AsylG

## Quellen und Zitierweise

Verbindlich: [`../../../references/zitierweise.md`](../../../references/zitierweise.md).

### Statute

- [§ 3 AsylG](https://www.gesetze-im-internet.de/asylvfg_1992/__3.html) (Flüchtlingseigenschaft)
- [§ 3a–3e AsylG](https://www.gesetze-im-internet.de/asylvfg_1992/__3a.html) (Verfolgungshandlungen / Gründe / Akteure / interner Schutz)
- [§ 4 AsylG](https://www.gesetze-im-internet.de/asylvfg_1992/__4.html) (subsidiärer Schutz)
- [§ 13 AsylG](https://www.gesetze-im-internet.de/asylvfg_1992/__13.html), [§ 14](https://www.gesetze-im-internet.de/asylvfg_1992/__14.html) (Antragstellung)
- [§ 17 AsylG](https://www.gesetze-im-internet.de/asylvfg_1992/__17.html) (Sprachmittler)
- [§ 25 AsylG](https://www.gesetze-im-internet.de/asylvfg_1992/__25.html) (Anhörung)
- [§ 29 AsylG](https://www.gesetze-im-internet.de/asylvfg_1992/__29.html) (Unzulässigkeit, Dublin)
- [§ 30 AsylG](https://www.gesetze-im-internet.de/asylvfg_1992/__30.html) (offensichtlich unbegründet)
- [§ 34, § 34a, § 36 AsylG](https://www.gesetze-im-internet.de/asylvfg_1992/__36.html) (Abschiebungsandrohung / -anordnung / Eilrechtsschutz)
- [§ 71 AsylG](https://www.gesetze-im-internet.de/asylvfg_1992/__71.html) (Folgeantrag)
- [§ 74 AsylG](https://www.gesetze-im-internet.de/asylvfg_1992/__74.html) (Klagefrist)
- [§ 60 AufenthG](https://www.gesetze-im-internet.de/aufenthg_2004/__60.html) (Abschiebungsverbote V, VII)
- [Art. 16a GG](https://www.gesetze-im-internet.de/gg/art_16a.html)
- [VO (EU) Nr. 604/2013](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32013R0604) (Dublin III)
- [RL 2011/95/EU](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32011L0095) (Qualifikations-RL)
- [RL 2013/32/EU](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32013L0032) (Asylverfahrens-RL)
- GFK 1951 + Zusatzprotokoll 1967

### Kommentare

- Marx, AsylG, 11. Aufl. 2024, § 3 Rn. 1 ff. / § 4 Rn. 1 ff. / § 25 Rn. 1 ff.
- Bergmann, in: Bergmann/Dienelt, AuslR, Stand 2024, § 3 AsylG Rn. 1 ff.
- GK-AsylG, Stand 2024, § 25 Rn. 1 ff. / § 29 Rn. 1 ff.
- Hofmann, in: NK-AuslR, 3. Aufl. 2023, § 60 AufenthG Rn. 1 ff.

### Rechtsprechung

1. EuGH, Urt. v. 17.02.2009 – Rs. C-465/07, Elgafaji (subsidiärer Schutz, Art. 15 lit. c RL 2004/83/EG, willkürliche Gewalt), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=EuGH&Datum=2009-02-17&Aktenzeichen=C-465/07)
2. EuGH, Urt. v. 21.12.2011 – verb. Rs. C-411/10, C-493/10, N.S. u.a. (systemische Mängel; ergangen noch zur Dublin-II-VO 343/2003), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=EuGH&Datum=2011-12-21&Aktenzeichen=C-411/10)
3. EuGH, Urt. v. 19.03.2019 – Rs. C-163/17, Jawo (Dublin III, Begriff des „Flüchtigseins", Art. 4 GRCh), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=EuGH&Datum=2019-03-19&Aktenzeichen=C-163/17)
4. EuGH, Urt. v. 07.11.2013 – verb. Rs. C-199/12 bis C-201/12, X, Y und Z (Verfolgung wegen sexueller Orientierung; keine Verweisung auf Verheimlichung), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=EuGH&Datum=2013-11-07&Aktenzeichen=C-199/12)
5. BVerwG, Urt. v. 04.07.2019 – 1 C 33.18, NVwZ 2020, 161 (Flüchtlingsanerkennung syrischer Antragsteller; Maßstab der beachtlichen Wahrscheinlichkeit und gerichtliche Aufklärungspflicht) — Bezug auf **§ 3e AsylG (interner Schutz)** ist der Quelle nicht zu entnehmen `[unverifiziert – Einschlägigkeit für internen Schutz prüfen]`, [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BVerwG&Datum=2019-07-04&Aktenzeichen=1%20C%2033.18)
6. EGMR, Urt. v. 21.01.2011 – Nr. 30696/09, M.S.S. ./. Belgien und Griechenland (Dublin, Art. 3 EMRK), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=EGMR&Datum=2011-01-21&Aktenzeichen=30696/09)

## Ausgabeformat

```
GUTACHTEN — Asylantrag-Vorbereitung
Mandant: <anonymisiert, Staatsangehörigkeit, Eingangsdatum>
Stand: <Datum>

I. Sachverhalt (chronologisch, ohne Suggestion)

II. Frage(n)
    – Welche Schutzform ist tragfähig?
    – Bestehen Dublin-Risiken?
    – Welche Beweismittel sind beizubringen?

III. Kurzantwort
     – Vorrangige Schutzform: § N AsylG
     – Dublin-Status: zuständig DE / Übergang nach Art. 29 / Wiederaufnahmegesuch erwartet
     – Erfolgsaussicht: 🟢 / 🟡 / 🔴

IV. Rechtliche Bewertung
    1. Antragstellung § 13, § 14 AsylG
    2. Dublin-Vorprüfung § 29 I Nr. 1 AsylG iVm VO 604/2013
       a) Zuständigkeit Art. 7 ff.
       b) Überstellungsfrist Art. 29 (6 / 12 / 18 Monate)
       c) Selbsteintritt Art. 17
    3. Schutzformen-Triage
       a) § 3 AsylG – Flüchtlingseigenschaft
          – Verfolgungshandlung § 3a
          – Anknüpfungsmerkmal § 3b
          – Akteur § 3c
          – Interner Schutz § 3e
       b) Art. 16a GG (idR ausgeschlossen wg. Drittstaaten)
       c) § 4 AsylG – subsidiärer Schutz
       d) § 60 V AufenthG (EMRK)
       e) § 60 VII AufenthG (krankheitsbedingt, qualifizierte ärztl. Bescheinigung)
    4. Beweislage und Beweismittelangebot

V. Anhörungsvorbereitung
   – Struktur der Befragung (chronologisch, akteur-, anknüpfungsmerkmalbezogen)
   – Beweismittel (Liste)
   – Dolmetscher (§ 17 AsylG)
   – Mitwirkungspflicht (§ 15 AsylG)

VI. Folgeantrag (sofern relevant)
   – Neue Sachlage / Beweise
   – Frist § 71 IV AsylG iVm § 51 III VwVfG (3 Monate ab Kenntnis)

VII. Frist-Block
   – Anhörungstermin: <Datum>
   – Dublin-Überstellungsfrist-Ablauf: <Datum>
   – Klage- / Eilantragsfrist nach Bescheid: 1 / 2 Wochen ab Zustellung

VIII. Risiken / offene Punkte
     🟢 / 🟡 / 🔴 mit Begründung

IX. Quellenverzeichnis
```

## Beispiel (gekürzt)

> **Sachverhalt:** Mandant K. (Syrien, 28 J., sunnitischer Muslim aus Idlib) reiste über Griechenland und die Balkanroute am 15.03.2024 ein, Asylgesuch am 18.03.2024. Eurodac-Treffer Kat. 1 in Griechenland. BAMF-Anhörung in 3 Wochen.
>
> **Dublin-Vorprüfung:** Voraussichtlich Wiederaufnahmegesuch DE → GR nach Art. 18 I lit. b Dublin III. Indes liegt zu GR EGMR-Rechtsprechung zu systemischen Mängeln vor (EGMR, Urt. v. 21.01.2011 – Nr. 30696/09, M.S.S. ./. Belgien und Griechenland, [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=EGMR&Datum=2011-01-21&Aktenzeichen=30696/09); aktuelle Lage zu prüfen via aktuellen Länderberichten). Argumentation für Selbsteintritt Art. 17 / Abschiebungsverbot § 60 V AufenthG iVm Art. 3 EMRK tragfähig. **Überstellungsfrist 6 Monate** ab Zustimmung GR – Mandantenkalender.
>
> **Schutzformen-Triage:** § 3 AsylG vorrangig – Verfolgungsmerkmal politische Überzeugung / Religion (Idlib, Konflikt zwischen Regierung und nichtstaatlichen Akteuren), Akteure Staat und nichtstaatlich (§ 3c Nr. 3). Hilfsweise § 4 I Nr. 3 AsylG (willkürliche Gewalt im internen bewaffneten Konflikt) – BVerwG- und EuGH-Linie zu Syrien zu prüfen.
>
> **Risikoeinstufung:** 🟡 mittel – Dublin-Verfahren laufend.

## Risiken / typische Fehler

- **Suggestive Vorbereitung der Anhörung** (vorgegebene Antworten) → Glaubwürdigkeitsproblem, Ablehnung als offensichtlich unbegründet § 30 III AsylG möglich.
- **Übersehen der Dublin-Frist Art. 29**: 6 / 12 / 18 Monate. Bei Ablauf Zuständigkeitsübergang DE – muss prozessual geltend gemacht werden.
- **Krankheitsbedingtes Abschiebungsverbot ohne qualifizierte ärztliche Bescheinigung** § 60a IIc / IId AufenthG → wird in der Praxis fast immer abgelehnt.
- **Folgeantrag verspätet**: 3 Monate ab Kenntnis der neuen Sachlage; ohne Frist keine Verfahrenseröffnung.
- **Verfahren-RL-Verstöße** durch BAMF (Anhörungsdauer, Pausen, Dolmetscher-Qualität) nicht protokolliert → später schwer zu rekonstruieren.
- **Einreise aus EU-Drittstaat** ausgeblendet → Art. 16a GG nach Drittstaatenregelung idR versperrt.
- **Mitwirkungspflicht § 15 AsylG** und Identitätsklärung nicht angesprochen → Bescheid wegen fehlender Mitwirkung.
