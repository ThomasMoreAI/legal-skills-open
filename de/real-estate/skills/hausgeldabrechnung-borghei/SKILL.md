---
name: hausgeldabrechnung-borghei
title: /wohnungseigentumsrecht:hausgeldabrechnung
description: Prüfung der Jahresabrechnung und der Beschlusskompetenz im Wohnungseigentumsrecht nach der WEMoG-Reform – Wirtschaftsplan und Vorschüsse § 28 Abs. 1 WEG, Nachschüsse und Abrechnungsspitze § 28 Abs. 2 WEG, Vermögensbericht § 28 Abs. 4 WEG, Verteilung nach Miteigentumsanteilen § 16 Abs. 2 WEG, Entziehung § 17 WEG als ultima ratio. Use when eine WEG-Jahresabrechnung oder ein Hausgeld-/Nachschussbeschluss auf Plausibilität und Beschlusskompetenz geprüft wird.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/wohnungseigentumsrecht/skills/hausgeldabrechnung
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: real-estate
language: de
---

# /wohnungseigentumsrecht:hausgeldabrechnung

## Zweck

Prüfung einer WEG-Jahresabrechnung auf zwei Ebenen: **Plausibilität** (rechnen die Zahlen, stimmt der Verteilungsschlüssel) und **Beschlusskompetenz** (durfte die Eigentümerversammlung überhaupt so beschließen).

Zentrale Neuerung der **WEMoG**-Reform (in Kraft seit 01.12.2020): Die Eigentümer beschließen nach § 28 Abs. 2 WEG nicht mehr „die Jahresabrechnung", sondern nur noch die **Abrechnungsspitze** — die Differenz zwischen geschuldetem Soll und bereits beschlossenen Vorschüssen. Wer „die Jahresabrechnung 2024" als Ganzes beschließt, überschreitet die Beschlusskompetenz; der Beschluss ist anfechtbar.

## Eingaben

- **Wirtschaftsplan** (Gesamt- und Einzelwirtschaftsplan) des betreffenden Jahres
- **Jahresabrechnung** (Gesamtabrechnung der Gemeinschaft)
- **Einzelabrechnung** des einzelnen Eigentümers
- **MEA-Schlüssel** / Verteilungsschlüssel laut Teilungserklärung (Miteigentumsanteile)
- der gefasste Beschluss im Wortlaut (Beschluss-Sammlung)
- ggf. Vermögensbericht des Verwalters

## Sub-Agent-Architektur

- **Researcher** liefert die einschlägigen Normen (§§ 16, 17, 28 WEG) und verifizierte BGH-Rechtsprechung zur Beschlusskompetenz nach WEMoG.
- **Drafter** erstellt die Plausibilitäts- und Kompetenzprüfung sowie ggf. den Entwurf einer Anfechtungsbegründung.
- **Reviewer** prüft, ob nur die Abrechnungsspitze beschlossen wurde, ob der Vermögensbericht vorliegt und ob der Verteilungsschlüssel der Teilungserklärung entspricht.

## Ablauf

### 1. Wirtschaftsplan und Vorschuss-Beschluss (§ 28 Abs. 1 WEG)

Nach [§ 28 Abs. 1 WEG](https://www.gesetze-im-internet.de/woeigg/__28.html) beschließen die Wohnungseigentümer über die Einforderung der **Vorschüsse** auf Grundlage des Wirtschaftsplans. Prüfen:

- Liegt ein beschlossener Wirtschaftsplan für das Abrechnungsjahr vor?
- Decken sich die im Wirtschaftsplan veranschlagten Vorschüsse mit den in der Einzelabrechnung angesetzten Soll-Beträgen?

Der Wirtschaftsplan ist der **Maßstab**, an dem die spätere Abrechnungsspitze gemessen wird.

### 2. Jahresabrechnung und Abrechnungsspitze (§ 28 Abs. 2 WEG)

Nach Ablauf des Wirtschaftsjahres beschließen die Eigentümer nach [§ 28 Abs. 2 WEG](https://www.gesetze-im-internet.de/woeigg/__28.html) über die **Nachschüsse** bzw. die Anpassung der beschlossenen Vorschüsse — die sogenannte **Abrechnungsspitze**.

**Kernpunkt der Beschlusskompetenz:** Gegenstand des Beschlusses ist nur die Abrechnungsspitze, **nicht** die gesamte Jahresabrechnung. Die Abrechnung selbst ist nur Berechnungsgrundlage, nicht Beschlussgegenstand. Ein Nachschuss ergibt sich als Differenz:

```
Abrechnungsspitze = Soll laut Jahresabrechnung − beschlossene Vorschüsse (Wirtschaftsplan)
   positive Spitze → Nachschuss (Nachzahlung des Eigentümers)
   negative Spitze → Anpassung / Guthaben
```

Verifizierte Rechtsprechung: **BGH, Urt. v. 11.04.2025 – V ZR 96/24, NJW 2025, 1504 = NZM 2025, 351** ([dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=11.04.2025&Aktenzeichen=V%20ZR%2096/24)) — der Nachschuss-/Abrechnungsspitzen-Beschluss kann in Teilen angefochten werden; die Entscheidung bestätigt, dass post-WEMoG nur die Abrechnungsspitze Beschlussgegenstand ist, nicht die gesamte Abrechnung.

**Folge für die Praxis:** Wird „die Jahresabrechnung" als Ganzes beschlossen, ist der Beschluss kompetenzwidrig und auf Anfechtung hin (teilweise) für ungültig zu erklären. Die Anfechtung kann sich gezielt auf die fehlerhaften Teile der Abrechnungsspitze beschränken.

### 3. Vermögensbericht (§ 28 Abs. 4 WEG)

Nach [§ 28 Abs. 4 WEG](https://www.gesetze-im-internet.de/woeigg/__28.html) hat der Verwalter nach Ablauf des Kalenderjahres einen **Vermögensbericht** zu erstellen und den Eigentümern zur Verfügung zu stellen. Er stellt den Stand der gemeinschaftlichen Geldmittel (insb. der Erhaltungsrücklage) und eine Aufstellung des wesentlichen Gemeinschaftsvermögens dar.

Prüfen: Liegt ein Vermögensbericht vor? Sein Fehlen ist ein eigenständiger Mangel; der Vermögensbericht ist allerdings nicht selbst Gegenstand des Abrechnungsspitzen-Beschlusses, sondern eine gesonderte Pflicht des Verwalters.

### 4. Verteilungsschlüssel / Miteigentumsanteile (§ 16 Abs. 2 WEG)

Nach [§ 16 Abs. 2 WEG](https://www.gesetze-im-internet.de/woeigg/__16.html) tragen die Eigentümer die Kosten und Lasten nach dem Verhältnis ihrer **Miteigentumsanteile**, soweit nicht durch Beschluss oder Vereinbarung ein abweichender Schlüssel gilt.

Prüfen:

- Entspricht der angewandte Schlüssel der Teilungserklärung bzw. einem wirksamen Änderungsbeschluss?
- Sind verbrauchsabhängige Kosten (Heizung/Wasser) korrekt aus dem MEA-Schlüssel herausgenommen?
- Summieren sich die Einzelabrechnungen exakt auf die Gesamtabrechnung (Schlüssigkeitskontrolle)?

### 5. Fälligkeit (§ 28 Abs. 3 WEG)

Über Fälligkeit und Art der Zahlung beschließen die Eigentümer nach [§ 28 Abs. 3 WEG](https://www.gesetze-im-internet.de/woeigg/__28.html). Der Nachschuss wird grundsätzlich mit Beschlussfassung bzw. zum beschlossenen Termin fällig.

### 6. Verzug, Beitreibung und Entziehung (§ 17 WEG)

Zahlt der Eigentümer den fälligen Nachschuss nicht, kommt er in Verzug; die Gemeinschaft kann das Hausgeld gerichtlich beitreiben. Als **ultima ratio** kommt bei schwerwiegenden, wiederholten Pflichtverletzungen — insbesondere erheblichen Hausgeldrückständen — die **Entziehung** des Wohnungseigentums nach [§ 17 WEG](https://www.gesetze-im-internet.de/woeigg/__17.html) in Betracht. Voraussetzung ist eine derart schwere Verletzung, dass den übrigen Eigentümern die Fortsetzung der Gemeinschaft nicht zugemutet werden kann; in der Regel ist eine vorherige Abmahnung erforderlich. § 17 WEG ist nur letztes Mittel, nicht Regelinstrument der Beitreibung.

### 7. Ergebnis

Zusammenfassende Bewertung: (a) wahrt der Beschluss die Beschlusskompetenz (nur Abrechnungsspitze?), (b) ist die Abrechnung plausibel (Schlüssel, Summen, Vermögensbericht), (c) Empfehlung — bestätigen, nachbessern oder fristgerecht anfechten.

## Risiken / typische Fehler

- **Beschluss über „die ganze Jahresabrechnung"** statt nur über die Abrechnungsspitze → Überschreitung der **Beschlusskompetenz** nach § 28 Abs. 2 WEG, anfechtbar (vgl. **BGH, Urt. v. 11.04.2025 – V ZR 96/24**, [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=11.04.2025&Aktenzeichen=V%20ZR%2096/24)). Das ist der häufigste WEMoG-Fehler.
- **Fehlender Vermögensbericht** (§ 28 Abs. 4 WEG) → eigenständiger Mangel; Vermögensbericht nachfordern.
- **Falscher Verteilungsschlüssel** → Abweichung von den Miteigentumsanteilen ohne wirksamen Beschluss nach § 16 Abs. 2 WEG.
- **Anfechtungsfrist versäumt** → Monatsfrist des § 45 WEG beachten; danach wird auch der kompetenzwidrige Beschluss bestandskräftig.
- **Entziehung § 17 WEG vorschnell** angedroht → ultima ratio, nicht Druckmittel im laufenden Hausgeldstreit.

## Ausgabeformat

```
PRÜFUNG JAHRESABRECHNUNG / HAUSGELD — WEG (post-WEMoG)

I.   Beschlusskompetenz (§ 28 Abs. 2 WEG)
     - Beschlossen wurde: <Wortlaut>
     - Nur Abrechnungsspitze oder ganze Abrechnung? → <Bewertung>
     - Maßstab: BGH, Urt. v. 11.04.2025 – V ZR 96/24 ([dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2025-04-11&Aktenzeichen=V%20ZR%2096/24))

II.  Wirtschaftsplan & Vorschüsse (§ 28 Abs. 1 WEG)
     - Vorschuss-Soll: <…>  |  Wirtschaftsplan vorhanden: <ja/nein>

III. Abrechnungsspitze / Nachschuss (§ 28 Abs. 2 WEG)
     - Soll − Vorschüsse = Spitze: <Betrag>  → Nachschuss/Guthaben

IV.  Vermögensbericht (§ 28 Abs. 4 WEG): <vorhanden / fehlt>

V.   Verteilungsschlüssel (§ 16 Abs. 2 WEG)
     - Miteigentumsanteile korrekt angewandt: <ja/nein>
     - Einzelabrechnungen = Gesamtabrechnung: <ja/nein>

VI.  Fälligkeit (§ 28 Abs. 3 WEG): <Termin>

VII. Verzug / Beitreibung, ggf. Entziehung (§ 17 WEG, ultima ratio)

VIII.Ergebnis & Empfehlung: <bestätigen / nachbessern / anfechten,
     Frist § 45 WEG>
```
