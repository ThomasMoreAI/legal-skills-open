---
name: arzthaftung-aufklaerungspflicht-borghei
title: /medizinrecht:arzthaftung-aufklaerungspflicht
description: Prüfung der ärztlichen Aufklärungspflicht und der daraus folgenden zivilrechtlichen Arzthaftung – Selbstbestimmungsaufklärung § 630e BGB, Aufklärungsumfang, Form/Adressat, Bedenkzeit, Beweislast § 630h II BGB, hypothetische Einwilligung. Use when ein Patient einen Aufklärungsmangel rügt oder eine Behandlerseite (Arzt, Klinik, Haftpflichtversicherer) Aufklärung und Einwilligung verteidigen muss.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/medizinrecht/skills/arzthaftung-aufklaerungspflicht
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: healthcare
language: de
---

# /medizinrecht:arzthaftung-aufklaerungspflicht

## Zweck

Der Skill prüft, ob eine Aufklärung den Anforderungen des § 630e BGB genügt und welche zivilrechtlichen Folgen ein Aufklärungsmangel auslöst. Ohne wirksame Einwilligung ist der ärztliche Heileingriff nach BGH-Linie rechtswidrige Körperverletzung iSv §§ 823 I BGB, 223 StGB – auch bei lege artis durchgeführter Behandlung. Der Skill prüft zudem die Beweislastsonderregel § 630h II BGB und die enge Verteidigungslinie der hypothetischen Einwilligung.

## Eingaben

- Behandlungsverlauf (Diagnose, geplanter Eingriff, Aufklärungsgespräch mit Datum, Uhrzeit, Aufklärendem, Aufklärungsbogen, Einwilligungserklärung)
- Eingriffsart (diagnostisch / therapeutisch; vital indiziert / relativ indiziert / kosmetisch)
- bekannte / realisierte Risiken
- Position des Mandanten (Patient, Erbe, Arzt, Klinik, Haftpflichtversicherer)
- Frist- / Verjährungssituation

## Sub-Agent-Architektur

Researcher liefert §§ 630a–630h BGB, § 823 BGB, §§ 223 ff. StGB, BGH-VI.-Zivilsenat-Rspr. (Bedenkzeit, Adressat, hypothetische Einwilligung, grober Behandlungsfehler) sowie Kommentarstellen aus Laufs/Katzenmeier/Lipp, Spickhoff, MüKoBGB. Drafter prüft Aufklärung und Einwilligung in Gutachtenstil, arbeitet § 630h II BGB Schritt für Schritt ab und ordnet die hypothetische Einwilligung ein. Reviewer prüft 30-Jahre-Höchstfrist § 199 II BGB, alle fünf Absätze § 630h BGB und § 203 StGB-Berührungspunkte.

## Ablauf

### 1. Behandlungsvertrag und Pflichtenkreis

[§ 630a BGB](https://www.gesetze-im-internet.de/bgb/__630a.html) begründet den Behandlungsvertrag. Pflicht zur Behandlung nach den zum Zeitpunkt der Behandlung bestehenden, allgemein anerkannten fachlichen Standards (Abs. 2). Nebenpflichten: Information ([§ 630c BGB](https://www.gesetze-im-internet.de/bgb/__630c.html)), Aufklärung ([§ 630e BGB](https://www.gesetze-im-internet.de/bgb/__630e.html)), Einwilligung ([§ 630d BGB](https://www.gesetze-im-internet.de/bgb/__630d.html)), Dokumentation ([§ 630f BGB](https://www.gesetze-im-internet.de/bgb/__630f.html)), Akteneinsicht ([§ 630g BGB](https://www.gesetze-im-internet.de/bgb/__630g.html)).

### 2. Selbstbestimmungsaufklärung vs. Sicherungsaufklärung

| Art | Funktion | Rechtsfolge der Verletzung |
|---|---|---|
| **Selbstbestimmungsaufklärung** (§ 630e BGB) | Patient soll informiert über Eingriff entscheiden | Einwilligung unwirksam → rechtswidriger Heileingriff → § 823 I BGB, § 223 StGB |
| **Sicherungs- / therapeutische Aufklärung** (§ 630c II BGB) | Patient soll sich verhaltensgemäß therapietreu verhalten (Medikamenteneinnahme, Nachsorge) | Behandlungsfehler (haftungsbegründend, nicht Einwilligungsmangel) |

Die Abgrenzung ist klausur- und praxisentscheidend – Aufklärungsmangel wirkt sich anders auf Beweislast und Tatbestand aus als Behandlungsfehler.

### 3. Aufklärungsumfang (§ 630e Abs. 1 BGB)

Der Patient ist aufzuklären über:

- **Art** des Eingriffs (was wird konkret gemacht)
- **Umfang** (Dauer, Ausmaß)
- **Durchführung**
- **zu erwartende Folgen** und **Risiken** (auch sehr seltene, wenn sie eingriffstypisch und für die Lebensführung des Patienten von Bedeutung sind)
- **Notwendigkeit, Dringlichkeit, Eignung und Erfolgsaussichten**
- **Alternativen** mit wesentlich unterschiedlichen Belastungen, Risiken oder Heilungschancen (echte Behandlungsalternativen)

Faustregel: Je weniger dringlich der Eingriff (kosmetische Operation, Vorsorgeuntersuchung), desto strenger die Aufklärung. Je dringlicher (vital indizierte Notfall-OP), desto enger die Anforderungen, in Notlagen ggf. mutmaßliche Einwilligung § 630d Abs. 1 S. 4 BGB.

### 4. Form, Adressat, Sprache, Aushändigung (§ 630e Abs. 2 BGB)

- **Mündlich** durch den Behandelnden selbst oder durch eine Person, die über die zur Durchführung der Maßnahme notwendige Ausbildung verfügt (also nicht durch eine medizinische Fachangestellte).
- Schriftliche **Unterlagen, die der Patient unterzeichnet, sind ihm in Abschrift auszuhändigen**.
- Aufklärung in für den Patienten verständlicher Sprache (ggf. Dolmetscher bei sprachlicher Barriere).
- Adressat: der einwilligungsfähige Patient persönlich. Bei nicht einwilligungsfähigen Patienten: gesetzlicher Vertreter / Betreuer / Bevollmächtigter, ergänzend Anhörung des Patienten in Maßen seines Verständnisses (§ 630d Abs. 2 BGB).

### 5. Aufklärungszeitpunkt und Bedenkzeit

Die Aufklärung muss so rechtzeitig erfolgen, dass der Patient seine Entscheidung **wohlüberlegt** treffen kann (§ 630e Abs. 2 Nr. 2 BGB). Bei ambulanten Eingriffen ist eine Aufklärung am Tag des Eingriffs noch akzeptabel; bei stationären, elektiven Eingriffen idR am Vortag, jedenfalls vor der prämedikativen Sedierung – BGH-Linie zur Bedenkzeit, vgl. BGH, Urt. v. 28.01.2014 – VI ZR 143/13 (https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=28.01.2014&Aktenzeichen=VI+ZR+143/13).

### 6. Beweislast § 630h Abs. 2 BGB

[§ 630h Abs. 2 BGB](https://www.gesetze-im-internet.de/bgb/__630h.html): „Der Behandelnde hat zu beweisen, dass er eine Einwilligung gemäß § 630d eingeholt und entsprechend den Anforderungen des § 630e aufgeklärt hat." → **Behandlerseite trägt die volle Beweislast** für ordnungsgemäße Aufklärung und Einwilligung. Aufklärungsbogen allein genügt nicht, er ist nur Indiz. Praktisch entscheidend: Dokumentation des Aufklärungsgesprächs nach § 630f BGB.

### 7. Hypothetische Einwilligung

Verteidigungslinie der Behandlerseite: Bei nachgewiesenem Aufklärungsmangel kann sich die Behandlerseite darauf berufen, dass der Patient bei ordnungsgemäßer Aufklärung gleichwohl eingewilligt hätte (§ 630h Abs. 2 S. 2 BGB). **Voraussetzungen restriktiv** (BGH):

- Patient muss substantiierten **Entscheidungskonflikt** plausibel machen (niedrige Schwelle: bloße Behauptung „ich hätte mich anders entschieden" reicht);
- erst dann muss Behandlerseite beweisen, dass Patient auch bei richtiger Aufklärung eingewilligt hätte.

In der Praxis selten erfolgreich – Drafter sollte hypothetische Einwilligung nicht als Hauptverteidigung positionieren.

### 8. Rechtsfolge bei Aufklärungsmangel

Ohne wirksame Einwilligung ist der ärztliche Heileingriff – auch bei lege artis Durchführung – rechtswidrige tatbestandsmäßige Körperverletzung iSv § 223 StGB; zivilrechtlich Anspruch aus § 823 I BGB (Körper, Gesundheit), § 823 II iVm § 223 StGB, ggf. Vertrag § 280 I iVm § 630a BGB. Schmerzensgeld nach § 253 II BGB. Bei Klinikbehandlung Haftung des Trägers über § 31 / § 831 BGB sowie vertraglich § 278 BGB.

## Quellen und Zitierweise

Verbindlich: [`../../../references/zitierweise.md`](../../../references/zitierweise.md).

### Statute

- [§ 630a BGB](https://www.gesetze-im-internet.de/bgb/__630a.html) (Behandlungsvertrag)
- [§ 630c BGB](https://www.gesetze-im-internet.de/bgb/__630c.html) (Informationspflicht / Sicherungsaufklärung)
- [§ 630d BGB](https://www.gesetze-im-internet.de/bgb/__630d.html) (Einwilligung)
- [§ 630e BGB](https://www.gesetze-im-internet.de/bgb/__630e.html) (Selbstbestimmungsaufklärung)
- [§ 630f BGB](https://www.gesetze-im-internet.de/bgb/__630f.html) (Dokumentation)
- [§ 630h BGB](https://www.gesetze-im-internet.de/bgb/__630h.html) (Beweislast)
- [§ 823 BGB](https://www.gesetze-im-internet.de/bgb/__823.html), [§ 253 BGB](https://www.gesetze-im-internet.de/bgb/__253.html), [§ 280 BGB](https://www.gesetze-im-internet.de/bgb/__280.html), [§ 278 BGB](https://www.gesetze-im-internet.de/bgb/__278.html)
- [§ 199 BGB](https://www.gesetze-im-internet.de/bgb/__199.html) (insb. Abs. 2 – 30-Jahre-Höchstfrist)
- [§ 223 StGB](https://www.gesetze-im-internet.de/stgb/__223.html), [§ 222 StGB](https://www.gesetze-im-internet.de/stgb/__222.html)

### Kommentare

- Wagner, in: MüKoBGB, 9. Aufl. 2024, § 630e Rn. 1 ff., § 630h Rn. 1 ff.
- Katzenmeier, in: BeckOK BGB, Stand 2024, § 630e Rn. 1 ff.
- Spickhoff, in: Spickhoff, Medizinrecht, 4. Aufl. 2022, § 630e BGB Rn. 1 ff.
- Pauge/Offenloch, Arzthaftungsrecht, 14. Aufl. 2018, Rn. 400 ff. (Aufklärung)
- Laufs/Katzenmeier/Lipp, Handbuch des Arztrechts, 8. Aufl. 2021, Kap. V (Aufklärung)

### Rechtsprechung

1. BGH, Urt. v. 28.01.2014 – VI ZR 143/13 (Aufklärungszeitpunkt / Bedenkzeit am Vortag) (https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=28.01.2014&Aktenzeichen=VI+ZR+143/13)
2. BGH, Urt. v. 30.09.2014 – VI ZR 443/13 (Adressat der Aufklärung, persönliches Gespräch) (https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=30.09.2014&Aktenzeichen=VI+ZR+443/13)
3. BGH, Urt. v. 15.03.2005 – VI ZR 313/03 (hypothetische Einwilligung, Entscheidungskonflikt) (https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=15.03.2005&Aktenzeichen=VI+ZR+313/03)
4. BGH, Urt. v. 14.03.2006 – VI ZR 279/04 (Aufklärung über Behandlungsalternativen) (https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=14.03.2006&Aktenzeichen=VI+ZR+279/04)
5. BGH, Urt. v. 11.10.2016 – VI ZR 462/15 (Aufklärungsumfang bei seltenen Risiken) (https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=11.10.2016&Aktenzeichen=VI+ZR+462/15)

## Ausgabeformat

```
GUTACHTEN — Aufklärungspflicht und Arzthaftung
Mandat:  <anonymisiert>
Eingriff: <Bezeichnung>, <Datum>

I.   Sachverhalt (knapp)
II.  Frage(n)
III. Kurzantwort
     – Aufklärung wirksam: [ja / nein / teilweise]
     – Haftung dem Grunde nach: [ja / nein / Beweisfragen]

IV.  Rechtliche Bewertung
     1. Behandlungsvertrag § 630a BGB
     2. Aufklärungspflicht § 630e BGB
        a) Umfang (Art, Risiken, Alternativen)
        b) Form, Adressat, Aushändigung § 630e II BGB
        c) Rechtzeitigkeit / Bedenkzeit
     3. Einwilligung § 630d BGB
     4. Beweislast § 630h II BGB
     5. Hypothetische Einwilligung § 630h II 2 BGB
     6. Anspruchsgrundlagen
        a) § 280 I iVm § 630a BGB
        b) § 823 I BGB (Körper, Gesundheit)
        c) § 823 II iVm § 223 StGB
        d) Schmerzensgeld § 253 II BGB
     7. Verjährung §§ 195, 199 BGB
        – Regelfrist 3 Jahre
        – Höchstfrist 30 Jahre § 199 II BGB (Körper / Gesundheit)

V.   Risiken / offene Punkte
     🟢 / 🟡 / 🔴 <Einstufung mit Begründung>
     – Sachverständigenbedarf:
     – Offene Tatsachen:

VI.  Quellenverzeichnis
```

## Risiken / typische Fehler

- **Verwechslung Selbstbestimmungs- und Sicherungsaufklärung** – Aufklärungsmangel ≠ Behandlungsfehler. Folgen weichen ab.
- **Aufklärungsbogen als alleiniger Nachweis** – genügt nicht; das Gespräch ist zu dokumentieren (§ 630f BGB).
- **Aufklärung im OP-Vorbereitungsraum nach Sedierung** – verspätet, Einwilligung unwirksam.
- **Aufklärung durch nicht qualifiziertes Personal** (MFA, Praktikant) – § 630e Abs. 2 Nr. 1 BGB verletzt.
- **Aufklärung in nicht verständlicher Sprache ohne Dolmetscher** – Einwilligung unwirksam.
- **Hypothetische Einwilligung als Hauptverteidigung** – BGH-Linie ist restriktiv, niedrige Schwelle für Entscheidungskonflikt.
- **Übersehen der 30-Jahre-Höchstfrist § 199 II BGB** bei Körperverletzungen – Regelfrist 3 Jahre wird oft fehlerhaft als absolute Grenze behandelt.
