---
name: handelsregister-eintragungspflicht-borghei
title: /handelsrecht:handelsregister-eintragungspflicht
description: Prüfung der Kaufmannseigenschaft nach §§ 1–6 HGB, daraus folgender Eintragungspflicht im Handelsregister sowie der Publizitätswirkung § 15 HGB. Use when ein Mandant prüfen muss, ob er Ist-/Kann-/Formkaufmann ist, ob eine Anmeldung beim Registergericht ansteht oder welche Folgen aus einer (un)richtigen Eintragung gegenüber Dritten resultieren.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/handelsrecht/skills/handelsregister-eintragungspflicht
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: commercial
language: de
---

# /handelsrecht:handelsregister-eintragungspflicht

## Zweck

Der Skill prüft, ob der Mandant **Kaufmann** im Sinne des HGB ist und welche Eintragungs- und Firmenpflichten daraus folgen. Er adressiert zugleich die Publizitätswirkung des Handelsregisters nach § 15 HGB (negative und positive Publizität) und die kaufmannsspezifischen Folgewirkungen (Anwendbarkeit §§ 343 ff. HGB, Schweigen auf kaufmännisches Bestätigungsschreiben, Untersuchungs- und Rügepflicht §§ 377/378 HGB).

## Eingaben

- Rechtsform und Tätigkeit des Mandanten (Einzelunternehmen, GbR, OHG, KG, GmbH, AG, …)
- Umsatz und Beschäftigtenzahl der letzten Geschäftsjahre
- Art der Tätigkeit (Handel, Dienstleistung, Land-/Forstwirtschaft, freier Beruf)
- Vorhandensein einer kaufmännischen Organisation (Buchhaltung, Lager, Filialen)
- Aktueller Stand im Handelsregister (bereits eingetragen? Welche Abteilung A/B? Letzte Änderung?)
- Konkrete Frage (Pflicht zur Anmeldung? Folgen einer falschen Eintragung? Schutz Dritter?)

## Sub-Agent-Architektur

Researcher liefert HGB-Statute §§ 1–17, BGH-Rechtsprechung zu § 1 Abs. 2 HGB (kaufmännische Einrichtung) und § 15 HGB (Verkehrsschutz) sowie Standardkommentare. Drafter prüft im Gutachtenstil Kaufmannseigenschaft, Eintragungspflicht und Folgenseite. Reviewer prüft, ob alle Kaufmanns-Tatbestände (Ist/Kann/Form) durchgeprüft, Publizitätszeitpunkte sauber unterschieden und § 377 HGB-Folgewirkung adressiert sind.

## Ablauf

### 1. Kaufmannseigenschaft prüfen

| Tatbestand | Norm | Voraussetzungen |
|---|---|---|
| **Istkaufmann** | [§ 1 HGB](https://www.gesetze-im-internet.de/hgb/__1.html) | Betrieb eines Handelsgewerbes; nach § 1 Abs. 2 HGB: jeder Gewerbebetrieb, **es sei denn**, das Unternehmen erfordert nach Art oder Umfang **keinen in kaufmännischer Weise eingerichteten Geschäftsbetrieb**. Indizien: Umsatz, Mitarbeiterzahl, Geschäftsvolumen, Filialen, Anlage- und Umlaufvermögen, Kreditbedarf. |
| **Kannkaufmann (Kleingewerbe)** | [§ 2 HGB](https://www.gesetze-im-internet.de/hgb/__2.html) | Kleingewerbetreibender kann sich freiwillig eintragen lassen; mit Eintragung wird er Kaufmann. |
| **Land-/Forstwirt** | [§ 3 HGB](https://www.gesetze-im-internet.de/hgb/__3.html) | Land-/forstwirtschaftliches Unternehmen ist nur dann Kaufmann, wenn es nach § 1 Abs. 2 HGB einen kaufmännischen Geschäftsbetrieb erfordert **und** sich eintragen lässt. |
| **Formkaufmann** | [§ 6 HGB](https://www.gesetze-im-internet.de/hgb/__6.html) | Handelsgesellschaften (OHG, KG, GmbH, AG, KGaA, SE) sind allein kraft Rechtsform Kaufleute, unabhängig vom Gegenstand. |

Freie Berufe (Anwalt, Arzt, Architekt, Steuerberater) sind grundsätzlich **kein** Gewerbe und damit nicht Istkaufmann, st. Rspr. `[unverifiziert – prüfen in juris]`. Belegstelle: Hopt, in: Baumbach/Hopt HGB, § 1 Rn. 19.

### 2. Eintragungspflicht und Anmeldung

- **Istkaufmann (§ 1 HGB):** Anmeldepflicht zum Handelsregister gem. § 29 HGB (Firma anmelden) i.V.m. § 31 HGB.
- **Kannkaufmann (§ 2 HGB):** keine Pflicht, aber Eintragung wirkt **konstitutiv** für Kaufmannseigenschaft.
- **Formkaufmann:** Eintragung ist gesellschaftsrechtlich konstitutiv (GmbH/AG) bzw. deklaratorisch (OHG/KG ab Geschäftsbeginn nach außen, § 123 HGB).

Anmeldung erfolgt in **öffentlich beglaubigter Form** (§ 12 HGB) beim Amtsgericht – Registergericht.

### 3. Inhalte der Eintragung

Mindestinhalte (vgl. § 29 HGB i.V.m. HRV):

- Firma (§§ 17–37a HGB – Grundsätze: Unterscheidungskraft, keine Irreführung, Rechtsformzusatz)
- Niederlassungsort
- Inhaber bzw. vertretungsberechtigte Personen
- ggf. Prokura (§ 53 HGB), ggf. Zweigniederlassung (§ 13 HGB)

### 4. Publizitätswirkung § 15 HGB

Drei Stufen:

| Abs. | Wirkung | Kurzformel |
|---|---|---|
| **§ 15 Abs. 1 HGB** | **Negative Publizität** – Solange eine eintragungspflichtige Tatsache nicht eingetragen **und** bekanntgemacht ist, kann sie einem gutgläubigen Dritten nicht entgegengehalten werden. | "Nicht eingetragen = nicht da gegen Dritte" |
| **§ 15 Abs. 2 HGB** | Nach Eintragung und Bekanntmachung **muss** der Dritte die Tatsache gegen sich gelten lassen (außer in den ersten 15 Tagen bei Nachweis fehlender Kenntnismöglichkeit). | Eintragung = Verkehrsbekanntheit |
| **§ 15 Abs. 3 HGB** | **Positive Publizität** – Eine unrichtig bekanntgemachte Tatsache kann ein gutgläubiger Dritter gegen sich gelten lassen, wenn er sich darauf verlassen hat. | Vertrauensschutz auf den Registerinhalt |

Voraussetzung jeweils: **Gutgläubigkeit** des Dritten (Beleg: Hopt, Baumbach/Hopt HGB, § 15 Rn. 8 ff.).

### 5. Rechtsfolgen der Kaufmannseigenschaft

- **§§ 343 ff. HGB** (Handelsgeschäfte) anwendbar
- **§ 346 HGB** Handelsbrauch
- **§ 347 HGB** kaufmännische Sorgfalt (strenger Maßstab)
- **§§ 362, 363 HGB** Schweigen als Annahme bei Antrag auf Geschäftsbesorgung; kaufmännisches Bestätigungsschreiben (Gewohnheitsrecht)
- **§§ 377, 378 HGB** Untersuchungs- und Rügepflicht beim beidseitigen Handelskauf
- **§§ 238 ff. HGB** Buchführungspflicht; § 241a HGB Befreiung kleiner Einzelkaufleute (Schwellen)
- **Prokura** § 48 HGB nur durch Kaufmann erteilbar

## Quellen und Zitierweise

Verbindlich: [`../../../references/zitierweise.md`](../../../references/zitierweise.md).

### Statute

- [§ 1 HGB](https://www.gesetze-im-internet.de/hgb/__1.html) (Istkaufmann)
- [§ 2 HGB](https://www.gesetze-im-internet.de/hgb/__2.html) (Kannkaufmann)
- [§ 3 HGB](https://www.gesetze-im-internet.de/hgb/__3.html) (Land-/Forstwirt)
- [§ 6 HGB](https://www.gesetze-im-internet.de/hgb/__6.html) (Formkaufmann)
- [§ 8 HGB](https://www.gesetze-im-internet.de/hgb/__8.html) (Handelsregister)
- [§ 12 HGB](https://www.gesetze-im-internet.de/hgb/__12.html) (Anmeldung in öffentlich beglaubigter Form)
- [§ 15 HGB](https://www.gesetze-im-internet.de/hgb/__15.html) (Publizität)
- [§ 17 HGB](https://www.gesetze-im-internet.de/hgb/__17.html) (Firma)
- [§ 29 HGB](https://www.gesetze-im-internet.de/hgb/__29.html) (Anmeldepflicht)
- [§ 238 HGB](https://www.gesetze-im-internet.de/hgb/__238.html) (Buchführungspflicht), [§ 241a HGB](https://www.gesetze-im-internet.de/hgb/__241a.html)
- [§§ 343, 344 HGB](https://www.gesetze-im-internet.de/hgb/__343.html) (Handelsgeschäfte, Vermutung)
- [§§ 377, 378 HGB](https://www.gesetze-im-internet.de/hgb/__377.html) (Untersuchungs- und Rügepflicht)

### Kommentare

- Hopt, in: Baumbach/Hopt HGB, 42. Aufl. 2023, § 1 Rn. 1 ff., § 15 Rn. 1 ff.
- K. Schmidt, in: MüKoHGB, 5. Aufl. 2021, § 1 HGB Rn. 1 ff.
- Krafka, in: MüKoHGB, 5. Aufl. 2021, § 15 HGB Rn. 1 ff.
- Burgard, in: Staub HGB, 6. Aufl. 2023, § 1 HGB Rn. 1 ff.
- Bergmann, in: EBJS HGB, 4. Aufl. 2020, § 15 Rn. 1 ff.

### Rechtsprechung (`[unverifiziert – prüfen in juris]`)

1. BGH, Urt. v. 27.10.2008 – II ZR 158/06 (Kaufmannsbegriff § 1 Abs. 2 HGB, kaufmännische Einrichtung)
2. BGH, Urt. v. 01.12.2003 – II ZR 161/02 (§ 15 HGB Publizitätswirkung)
3. BGH, Urt. v. 14.02.2019 – IX ZR 149/16 (freie Berufe / Gewerbebegriff)

## Ausgabeformat

```
GUTACHTEN — Kaufmannseigenschaft und Handelsregister
Mandant: <anonymisiert>

I. Sachverhalt (knapp)
II. Frage(n)
    – Kaufmannseigenschaft (welcher Tatbestand)?
    – Anmeldepflicht?
    – Folgen einer (Nicht-)Eintragung gegenüber Dritten?
III. Kurzantwort
IV. Rechtliche Bewertung
    1. Kaufmannseigenschaft
       a) § 1 HGB Istkaufmann (Indizienprüfung kaufmännische Einrichtung)
       b) § 2 HGB Kannkaufmann
       c) § 3 HGB Land-/Forstwirt
       d) § 6 HGB Formkaufmann
    2. Eintragungspflicht und Anmeldung
       (§§ 12, 29, 31 HGB)
    3. Publizitätswirkung § 15 HGB
       a) Abs. 1 negative Publizität
       b) Abs. 2 Eintragung + Bekanntmachung
       c) Abs. 3 positive Publizität
    4. Folgewirkungen der Kaufmannseigenschaft
       (§§ 343 ff., 346, 347, 362, 377/378 HGB)
V. Gesamtergebnis
VI. Risiken / offene Punkte
    🟢 / 🟡 / 🔴 <Einstufung mit Begründung>
VII. Quellenverzeichnis
```

## Beispiel (Auszug Gutachtenstil)

> "Die Mandantin betreibt einen Online-Handel mit Industriebedarf. Bei einem Jahresumsatz von rund 2,4 Mio. EUR, sechs Beschäftigten und externer Lagerlogistik ist nach Art und Umfang des Geschäftsbetriebs eine kaufmännische Einrichtung erforderlich (Buchhaltung, Forderungsmanagement, Bestandsführung, Vertragswesen). Damit liegt ein Handelsgewerbe iSv § 1 Abs. 2 HGB vor; die Mandantin ist Istkaufmann nach § 1 Abs. 1 HGB. Die fehlende Eintragung ändert daran nichts (deklaratorische Wirkung der Eintragung beim Istkaufmann, vgl. Hopt, Baumbach/Hopt HGB, § 1 Rn. 8). Folge: Anmeldepflicht nach §§ 29, 31 HGB; Anwendbarkeit der §§ 343 ff. HGB; insb. greift bei beidseitigem Handelsgeschäft auch die Untersuchungs- und Rügepflicht § 377 HGB …"

## Risiken / typische Fehler

- **Übersehen des Istkaufmann-Status** bei nicht eingetragenen Einzelunternehmern oder GbRs, die längst Handelsgewerbe betreiben — alle § 377 HGB-Folgen werden dann verkannt.
- **Falsche Annahme, die Eintragung sei für den Istkaufmann konstitutiv.** Sie ist deklaratorisch; Kaufmannseigenschaft tritt mit Erreichen der Schwelle automatisch ein.
- **Pauschale Anwendung § 15 HGB auf nicht eintragungspflichtige Tatsachen** — § 15 HGB schützt nur bezüglich **eintragungspflichtiger** Tatsachen.
- **Verwechselung von Gutglaubensschutz** (§ 15 HGB) und materiellem Bestand des Rechts.
- **Freie Berufe als Kaufleute behandeln** — Anwälte, Ärzte, Architekten sind keine Gewerbetreibenden, fallen daher nicht unter § 1 HGB.
