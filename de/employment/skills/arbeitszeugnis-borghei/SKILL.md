---
name: arbeitszeugnis-borghei
title: /arbeitsrecht:arbeitszeugnis
description: Erteilung, Prüfung und Berichtigung des Arbeitszeugnisses – Anspruch auf einfaches und qualifiziertes Zeugnis § 109 GewO, § 630 BGB, Gebot der Zeugnisklarheit und Verbot verdeckter Aussagen § 109 Abs. 2 GewO, Notenstufen der Zeugnissprache und Geheimcodes, Verteilung der Darlegungslast (ab der Note 'befriedigend' trägt der Arbeitnehmer die Darlegungslast für eine bessere Beurteilung), Zwischenzeugnis, Berichtigungs- und Erfüllungsklage, Form und Ausstellungsdatum. Use when ein Arbeitnehmer ein Zeugnis verlangt oder ein erteiltes Zeugnis auf verdeckte Abwertungen prüfen lässt, oder wenn ein Arbeitgeber ein rechtssicheres Zeugnis formulieren will.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/arbeitsrecht/skills/arbeitszeugnis
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: employment
language: de
---

# /arbeitsrecht:arbeitszeugnis

## Zweck

Das Arbeitszeugnis ist der einzige Bereich des Arbeitsrechts, in dem eine überwiegend außergesetzliche, von der Praxis entwickelte Kunstsprache über den Marktwert eines Menschen entscheidet. Der Gesetzestext ([§ 109 GewO](https://www.gesetze-im-internet.de/gewo/__109.html)) umfasst drei Absätze; der Streit dreht sich fast immer um eine Formulierung, die dort nicht steht. Dieser Skill übersetzt die Zeugnissprache in Noten, prüft auf verdeckte Abwertungen und formuliert Berichtigungsverlangen.

## Eingaben

- Zeugnisart: **einfaches** (Art und Dauer) oder **qualifiziertes** Zeugnis (zusätzlich Leistung und Verhalten)
- Anlass: Beendigung / Zwischenzeugnis (Vorgesetztenwechsel, Versetzung, Elternzeit, Bewerbung) / vorläufiges Zeugnis
- Tätigkeitsbeschreibung, Dauer, Position, wesentliche Projekte und Verantwortungsbereiche
- Vorliegendes Zeugnis im Volltext (bei Prüfung)
- Vorhandene Leistungsbeurteilungen, Zielerreichungen, frühere Zwischenzeugnisse — die Beweismittel für eine überdurchschnittliche Note
- Beendigungsgrund (steuert die Zulässigkeit einer Beendigungsangabe)

## Sub-Agent-Architektur

1. **Researcher** ([`../../agents/researcher.md`](../../agents/researcher.md)) liefert § 109 GewO, § 630 BGB und die BAG-Linien zur Darlegungslast und zur Schlussformel.
2. **Drafter** ([`../../agents/drafter.md`](../../agents/drafter.md)) erstellt den Zeugnistext bzw. das Berichtigungsverlangen mit konkreter Ersatzformulierung.
3. **Reviewer** ([`../../agents/reviewer.md`](../../agents/reviewer.md)) prüft Notenkonsistenz, Vollständigkeit, Form und Datierung.

## Ablauf

### 1. Anspruchsgrundlage und Inhalt ([§ 109 GewO](https://www.gesetze-im-internet.de/gewo/__109.html), [§ 630 BGB](https://www.gesetze-im-internet.de/bgb/__630.html))

Bei Beendigung des Arbeitsverhältnisses besteht Anspruch auf ein **schriftliches** Zeugnis (§ 109 Abs. 1 S. 1 GewO). Es muss mindestens Art und Dauer der Tätigkeit enthalten (einfaches Zeugnis, S. 2); auf Verlangen erstreckt es sich auf **Leistung und Verhalten** (**qualifiziertes Zeugnis**, S. 3). § 630 BGB enthält die parallele Regelung für das Dienstverhältnis.

**Form:** Schriftform. Die elektronische Form ist **ausgeschlossen**, es sei denn, der Arbeitnehmer willigt ein (§ 109 Abs. 3 GewO). Ein per PDF übersandtes Zeugnis ohne Einwilligung erfüllt den Anspruch nicht.

Der Anspruch ist eine **Holschuld** am Betriebssitz; auf Verlangen und bei zumutbaren Umständen kommt eine Übersendung in Betracht (§ 241 Abs. 2 BGB).

### 2. Zeugnisklarheit und das Verbot verdeckter Aussagen ([§ 109 Abs. 2 GewO](https://www.gesetze-im-internet.de/gewo/__109.html))

Das Zeugnis muss klar und verständlich formuliert sein. Es darf **keine Merkmale oder Formulierungen enthalten, die den Zweck haben, eine andere als die aus der äußeren Form oder dem Wortlaut ersichtliche Aussage zu treffen.** Das ist die gesetzliche Absage an Geheimcodes — die in der Praxis dennoch fortleben, weil die Kunstsprache selbst als „ersichtlich" gilt, sobald sie branchenüblich ist.

Zwei Leitprinzipien, die aus § 109 Abs. 2 GewO und dem allgemeinen Rücksichtnahmegebot ([§ 241 Abs. 2 BGB](https://www.gesetze-im-internet.de/bgb/__241.html)) folgen:

- **Wahrheitspflicht** gegenüber dem künftigen Arbeitgeber, und
- **Wohlwollenspflicht** gegenüber dem Arbeitnehmer — das Zeugnis darf das berufliche Fortkommen nicht unnötig erschweren.

Bei Konflikt geht die Wahrheit vor; der Spielraum ist die Auswahl und Gewichtung, nicht die Erfindung.

### 3. Notenstufen der Zeugnissprache

Die Leistungsbeurteilung folgt einer Skala, die über das Adverb und den Zufriedenheitsgrad gebildet wird:

| Note | Standardformulierung Leistung |
|---|---|
| sehr gut (1) | „…stets zu unserer **vollsten** Zufriedenheit" |
| gut (2) | „…stets zu unserer **vollen** Zufriedenheit" |
| befriedigend (3) | „…zu unserer **vollen** Zufriedenheit" |
| ausreichend (4) | „…zu unserer Zufriedenheit" |
| mangelhaft (5) | „…**im Großen und Ganzen** zu unserer Zufriedenheit" |
| ungenügend (6) | „…hat sich **bemüht**, die Aufgaben zu unserer Zufriedenheit zu erledigen" |

Für das **Verhalten** gilt eine eigene Reihung; entscheidend ist zusätzlich die **Reihenfolge der Genannten**:

| Note | Formulierung |
|---|---|
| sehr gut | „Sein Verhalten gegenüber Vorgesetzten, Kollegen und Kunden war stets vorbildlich." |
| gut | „…war stets einwandfrei." |
| befriedigend | „…war einwandfrei." |
| ausreichend | „…gab zu keiner Zeit Anlass zu Beanstandungen." |

**Reihenfolgen-Code:** Werden die Vorgesetzten **nach** den Kollegen genannt oder ganz weggelassen, liest die Praxis das als Hinweis auf Konflikte mit der Führungsebene. Die korrekte Reihung ist Vorgesetzte → Kollegen → Kunden.

### 4. Geheimcodes — Prüfraster

| Formulierung | Gelesene Bedeutung |
|---|---|
| „stets bemüht" | Leistung ungenügend |
| „hat alle Aufgaben mit großem Fleiß und Interesse erledigt" | Eifrig, aber erfolglos |
| „war gesellig und trug zur Verbesserung des Betriebsklimas bei" | Alkohol- oder Geselligkeitsproblem |
| „zeigte für seine Arbeit Verständnis" | Ohne eigene Initiative |
| „durch seine Geselligkeit trug er zur Auflockerung bei" | Störend, nicht leistungsbezogen |
| „war stets pünktlich" (als einziges Lob) | Beredtes Schweigen zur Leistung |
| „verließ uns im gegenseitigen Einvernehmen" | Trennung auf Arbeitgeberinitiative |
| „aus betriebsbedingten Gründen" ohne weitere Wertung | neutral, unbedenklich |

**Beredtes Schweigen:** Der schwerwiegendste und am schwersten anzugreifende Code. Fehlt in einem Zeugnis für eine Vertriebskraft jede Aussage zum Umsatz, für eine Führungskraft jede Aussage zur Mitarbeiterführung, ist das eine Abwertung. Anzugreifen ist es über den Vollständigkeitsgrundsatz: Das qualifizierte Zeugnis muss alle für die künftige Verwendung wesentlichen Tätigkeiten und Leistungen abbilden.

### 5. Darlegungs- und Beweislast

Die Verteilung folgt einer Schwelle:

- Der Arbeitgeber schuldet **grundsätzlich** eine Beurteilung; erteilt er eine **unterdurchschnittliche** Note (schlechter als „befriedigend"), muss **er** die zugrunde liegenden Tatsachen darlegen und beweisen.
- Verlangt der Arbeitnehmer eine **bessere als die Note „befriedigend"**, trägt **er** die Darlegungs- und Beweislast für die überdurchschnittliche Leistung (BAG, Urt. v. 18.11.2014 – 9 AZR 584/13, BAGE 150, 66 = NZA 2015, 435; [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BAG&Datum=18.11.2014&Aktenzeichen=9%20AZR%20584/13) — die Formulierung „zur vollen Zufriedenheit" entspricht der Note „befriedigend", nicht „gut").
- Der Ausgangspunkt „befriedigend" ist **keine gesetzliche Vermutung**, sondern eine von der Rechtsprechung gesetzte Beweislastschwelle. Der Einwand, in der Praxis würden überwiegend gute und sehr gute Zeugnisse erteilt, hat sich als Argument für eine Verschiebung dieser Schwelle nicht durchgesetzt `[unverifiziert – prüfen]`.

Beweismittel des Arbeitnehmers: Zwischenzeugnisse, schriftliche Beurteilungen, Zielvereinbarungen mit dokumentierter Zielerreichung, Bonusabrechnungen, Beförderungen, Zeugen aus der Führungsebene.

### 6. Zwischenzeugnis

Ein Anspruch auf Zwischenzeugnis ist gesetzlich nicht ausdrücklich geregelt; er folgt aus § 241 Abs. 2 BGB bei **berechtigtem Interesse**. Anerkannte Anlässe: Wechsel des Vorgesetzten, Versetzung, Betriebsübergang, bevorstehende Elternzeit, konkrete eigene Bewerbung, Kündigung des Arbeitsverhältnisses vor Ablauf der Kündigungsfrist, unsichere wirtschaftliche Lage des Arbeitgebers.

**Bindungswirkung:** Ein erteiltes Zwischenzeugnis bindet den Arbeitgeber bei der späteren Endzeugniserteilung für den abgedeckten Zeitraum. Eine Abweichung nach unten muss er durch neue Tatsachen begründen. Für Arbeitnehmer ist das Zwischenzeugnis daher das wirksamste Beweismittel für eine gute Endnote — und für Arbeitgeber ein Grund, es sorgfältig zu formulieren.

### 7. Aufbau und Formulierungshilfe

```
<Briefkopf des Arbeitgebers>

                          ZEUGNIS

Frau <Vorname Nachname>, geboren am <Datum> in <Ort>, war vom
<Eintritt> bis zum <Austritt> in unserem Unternehmen als
<Position> beschäftigt.

<Unternehmensbeschreibung — 1–2 Sätze, Branche, Größe.>

Zu ihren Aufgaben gehörten insbesondere:
  - <Aufgabe 1, absteigend nach Bedeutung>
  - <Aufgabe 2>
  - <Aufgabe 3>
  - <Verantwortungsbereiche: Budget, Personalverantwortung für
     N Mitarbeitende, Projektleitungen>

Frau <Name> verfügt über ein fundiertes und breites Fachwissen,
das sie stets sicher und praxisgerecht einsetzte. Sie arbeitete
äußerst sorgfältig, zielgerichtet und eigenverantwortlich. Auch
bei hohem Arbeitsanfall zeigte sie stets eine überdurchschnittliche
Belastbarkeit.

<Besondere Erfolge konkret benennen: Projekt, Zeitraum, Ergebnis.>

Frau <Name> erledigte die ihr übertragenen Aufgaben stets zu
unserer vollsten Zufriedenheit.                        [Note 1]

Ihr Verhalten gegenüber Vorgesetzten, Kollegen und Kunden war
stets vorbildlich.                                     [Note 1]

Das Arbeitsverhältnis endet zum <Datum> auf eigenen Wunsch von
Frau <Name>.                                    [nur mit ihrer
                                                 Zustimmung!]

Wir bedanken uns für die stets sehr guten Leistungen und die
angenehme Zusammenarbeit. Für ihren weiteren beruflichen und
privaten Lebensweg wünschen wir ihr alles Gute und weiterhin
viel Erfolg.                                    [Schlussformel]

<Ort>, <Ausstellungsdatum = letzter Tag des Arbeitsverhältnisses>

<Unterschrift>
<Name, Funktion — ranghöher als der Beurteilte>
```

**Schlussformel:** Auf Dank, Bedauern und Zukunftswünsche besteht **kein einklagbarer Anspruch** — sie ist Ausdruck persönlicher Empfindung des Arbeitgebers (st. Rspr. des BAG zur Schlussformel `[unverifiziert – prüfen]`). Ihr **Fehlen** wertet ein sonst gutes Zeugnis in der Lesart der Praxis jedoch ab. Konsequenz für die Verhandlung: Die Schlussformel ist nicht erzwingbar, aber ein regelmäßiger und lohnender Gegenstand des Vergleichs im Kündigungsschutzverfahren.

**Beendigungsgrund:** darf nur mit Zustimmung des Arbeitnehmers aufgenommen werden. Eine ungefragte Angabe („wurde betriebsbedingt gekündigt") ist zu entfernen.

### 8. Durchsetzung: Erfüllungs- und Berichtigungsklage

Zwei zu trennende Ansprüche:

- **Erfüllungsanspruch** (§ 109 Abs. 1 GewO): Es wurde überhaupt kein oder kein qualifiziertes Zeugnis erteilt. Antrag: Verurteilung zur Erteilung eines qualifizierten Zeugnisses.
- **Berichtigungsanspruch**: Ein Zeugnis liegt vor, ist aber unrichtig oder unvollständig. Antrag auf Erteilung eines Zeugnisses mit **konkret formuliertem** Inhalt — das Gericht kann keinen Text erfinden, der Kläger muss ihn liefern.

**Formulierungshilfe — Klageantrag Berichtigung:**

```
Die Beklagte wird verurteilt, der Klägerin ein qualifiziertes
Arbeitszeugnis zu erteilen, das unter dem Datum des <letzter Tag
des Arbeitsverhältnisses> ausgestellt ist und in Bezug auf die
Leistungsbeurteilung die Formulierung enthält:
"Frau <Name> erledigte die ihr übertragenen Aufgaben stets zu
unserer vollen Zufriedenheit."
sowie in Bezug auf die Verhaltensbeurteilung die Formulierung:
"Ihr Verhalten gegenüber Vorgesetzten, Kollegen und Kunden war
stets einwandfrei."
```

Zuständig ist das Arbeitsgericht ([§ 2 ArbGG](https://www.gesetze-im-internet.de/arbgg/__2.html)). Zu beachten sind **tarifliche und arbeitsvertragliche Ausschlussfristen** — der Zeugnisanspruch ist ein Anspruch aus dem Arbeitsverhältnis und kann verfallen; die dreijährige Regelverjährung nach [§ 195 BGB](https://www.gesetze-im-internet.de/bgb/__195.html) ist die äußere Grenze. Der Anspruch kann zudem **verwirken**, wenn er lange nach Beendigung erstmals geltend gemacht wird.

## Quellen

### Statute

- [§ 109 GewO](https://www.gesetze-im-internet.de/gewo/__109.html)
- [§ 630 BGB](https://www.gesetze-im-internet.de/bgb/__630.html), [§ 241 BGB](https://www.gesetze-im-internet.de/bgb/__241.html), [§ 195 BGB](https://www.gesetze-im-internet.de/bgb/__195.html), [§ 626 BGB](https://www.gesetze-im-internet.de/bgb/__626.html)
- [§ 2 ArbGG](https://www.gesetze-im-internet.de/arbgg/__2.html), [§ 12a ArbGG](https://www.gesetze-im-internet.de/arbgg/__12a.html)
- [§ 83 BetrVG](https://www.gesetze-im-internet.de/betrvg/__83.html) (Personalakte, Gegendarstellung)

### Kommentare

- Müller-Glöge, in: ErfK, 24. Aufl. 2024, § 109 GewO Rn. 1 ff.
- Henssler, in: MüKoBGB, 9. Aufl. 2023, § 630 Rn. 1 ff.
- Schaub, Arbeitsrechts-Handbuch, 20. Aufl. 2023, § 146 (Zeugnis)
- Tschöpe, Arbeitsrecht Handbuch, Teil 2 F (Zeugnisrecht)

### Rechtsprechung

- BAG, Urt. v. 18.11.2014 – 9 AZR 584/13, BAGE 150, 66 = NZA 2015, 435 (Darlegungslast bei der Zeugnisnote: ab Verlangen einer besseren Note als „befriedigend" trägt der Arbeitnehmer die Darlegungslast; „zur vollen Zufriedenheit" = befriedigend), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BAG&Datum=18.11.2014&Aktenzeichen=9%20AZR%20584/13)
- st. Rspr. des BAG zur Schlussformel (kein einklagbarer Anspruch auf Dank und Zukunftswünsche) `[unverifiziert – prüfen]`
- st. Rspr. des BAG zu § 109 Abs. 2 GewO (Verbot verdeckter Aussagen, Wahrheits- und Wohlwollenspflicht) `[unverifiziert – prüfen]`
- st. Rspr. des BAG zur Bindungswirkung eines erteilten Zwischenzeugnisses für das Endzeugnis `[unverifiziert – prüfen]`

> Aktenzeichen sind vor Verwendung in juris, Beck-Online oder der [BAG-Entscheidungsdatenbank](https://www.bundesarbeitsgericht.de/entscheidungen/) zu ermitteln.

## Ausgabeformat

```
ARBEITSZEUGNIS — <Erteilung / Prüfung> — <Mandat-ID> — <Datum>
VERTRAULICH — MANDATSGEHEIMNIS — § 43a Abs. 2 BRAO

Gesamtbefund: [🟢 unbedenklich / 🟡 berichtigungsfähig / 🔴 abwertend]

I.    Zeugnisart                      [einfach / qualifiziert /
                                       Zwischenzeugnis]
II.   Formprüfung
      Schriftform § 109 I GewO        [🟢 / 🔴]
      Ausstellungsdatum               <Datum>  [🟢 / 🔴 Rückdatierung]
      Unterzeichner                   <Name, Funktion>  [🟢 / 🔴 rangniedrig]
      Briefkopf, kein Knick, sauber   [🟢 / 🔴]
III.  Vollständigkeit
      Tätigkeitsbeschreibung          [🟢 / 🔴 lückenhaft: <…>]
      Verantwortungsbereiche          [🟢 / 🔴]
      Beredtes Schweigen              [keines / 🔴 zu: <…>]
IV.   Leistungsbeurteilung
      Zitat:                          "<Wortlaut>"
      Entspricht Note:                <1–6>
      Angestrebte Note:               <…>
V.    Verhaltensbeurteilung
      Zitat:                          "<Wortlaut>"
      Reihenfolge Vorgesetzte/Kollegen/Kunden  [🟢 / 🔴]
      Entspricht Note:                <1–6>
VI.   Codes / verdeckte Aussagen      <Fundstelle + Lesart>
VII.  Beendigungsangabe               [fehlt / zulässig / 🔴 ohne Zustimmung]
VIII. Schlussformel                   [vorhanden / fehlt — nicht einklagbar,
                                       Vergleichsgegenstand]
IX.   Darlegungslast                  <wer trägt sie für die Zielnote>
      Beweismittel:                   <Zwischenzeugnisse, Beurteilungen…>
X.    Ausschlussfristen / Verwirkung  [🟢 / ⚠️ Frist bis <Datum>]

Vorgeschlagene Ersatzformulierungen:
  <Wortlaut 1>
  <Wortlaut 2>
Empfehlung: <außergerichtliches Berichtigungsverlangen / Klage / Vergleich>
```

## Risiken / typische Fehler

- **„stets bemüht"** oder eine andere Bemühensformel verwendet — sie ist die schwerste Abwertung der Zeugnissprache und im Prozess kaum zu verteidigen.
- **Rückdatierung** unterlassen: Das Zeugnis muss auf den letzten Tag des Arbeitsverhältnisses datiert sein. Ein deutlich späteres Datum signalisiert Streit und wertet ab.
- **Zeugnis vom nicht ranghöheren Unterzeichner** — die Unterschrift muss von einer Person stammen, die dem Beurteilten gegenüber weisungsbefugt oder ranghöher war; die Sachbearbeitung Personal genügt regelmäßig nicht.
- **Beredtes Schweigen** zu einer für die Position zentralen Tätigkeit — die Lücke wirkt stärker als jede negative Formulierung.
- **Erfüllungsanspruch mit Berichtigungsanspruch verwechselt** — bei einem bereits erteilten Zeugnis ist der konkrete Wunschtext in den Antrag aufzunehmen; ein Antrag auf „ein wohlwollendes Zeugnis" ist unbestimmt.
- **Note gefordert, ohne die Darlegungslast zu bedienen** — oberhalb von „befriedigend" muss der Arbeitnehmer die überdurchschnittliche Leistung mit Tatsachen und Beweismitteln unterlegen.
- **Beendigungsgrund ohne Zustimmung** aufgenommen — insbesondere der Hinweis auf eine verhaltensbedingte Kündigung oder auf § 626 BGB ist zu streichen.
- **Elektronische Erteilung ohne Einwilligung** (§ 109 Abs. 3 GewO) — der Anspruch ist damit nicht erfüllt.
- **Zwischenzeugnis leichtfertig sehr gut formuliert** — es bindet den Arbeitgeber für den abgedeckten Zeitraum beim Endzeugnis.
- **Ausschlussfrist übersehen** — auch der Zeugnisanspruch unterliegt tariflichen und vertraglichen Verfallklauseln.
