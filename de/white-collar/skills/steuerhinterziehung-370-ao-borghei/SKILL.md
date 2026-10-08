---
name: steuerhinterziehung-370-ao-borghei
title: /wirtschafts-steuerstrafrecht:steuerhinterziehung-370-ao
description: Prüfung der Steuerhinterziehung nach § 370 AO – Tathandlungen des Abs. 1 (unrichtige oder unvollständige Angaben, pflichtwidriges In-Unkenntnis-Lassen, Unterlassen der Verwendung von Steuerzeichen), Erfolg der Steuerverkürzung und des nicht gerechtfertigten Steuervorteils, Vollendung und Versuch § 370 Abs. 2 AO, besonders schwerer Fall § 370 Abs. 3 AO, Kompensationsverbot § 370 Abs. 4 S. 3 AO, Verfolgungsverjährung §§ 376 AO, 78 StGB mit der verlängerten Frist von 15 Jahren, leichtfertige Steuerverkürzung § 378 AO sowie das Verhältnis von Steuerfestsetzung und Strafverfahren. Use when ein steuerstrafrechtlicher Vorwurf zu prüfen, eine Einlassung vorzubereiten oder die Verjährung eines Veranlagungszeitraums zu bestimmen ist.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/wirtschafts-steuerstrafrecht/skills/steuerhinterziehung-370-ao
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: white-collar
language: de
---

# /wirtschafts-steuerstrafrecht:steuerhinterziehung-370-ao

## Zweck

Das Steuerstrafverfahren wird in zwei Verfahren zugleich geführt: dem Strafverfahren und dem Besteuerungsverfahren. Wer nur eines von beiden bearbeitet, verliert im anderen. Dieser Skill prüft den Tatbestand des § 370 AO Veranlagungszeitraum für Veranlagungszeitraum, bestimmt Vollendungszeitpunkt und Verjährung und trennt sauber zwischen dem strafrechtlich relevanten Verkürzungsbetrag und der steuerlichen Festsetzung. Die strafbefreiende Selbstanzeige ist **nicht** Gegenstand dieses Skills — dafür ist [`steuerrecht/skills/selbstanzeige`](../../../steuerrecht/skills/selbstanzeige/SKILL.md) zuständig (§§ 371, 398a AO).

## Eingaben

- Steuerart und **jeder betroffene Veranlagungszeitraum einzeln** (jede Steuerart und jeder Zeitraum ist eine eigene Tat)
- Erklärungsverhalten: abgegeben, unrichtig, unvollständig, gar nicht abgegeben
- Bekanntgabedatum der jeweiligen Steuerbescheide (maßgeblich für die Vollendung)
- Verkürzungsbetrag je Tat, getrennt nach Steuerart
- Vorstellungsbild des Beschuldigten: Vorsatz, bedingter Vorsatz oder Leichtfertigkeit
- Regelbeispiele des § 370 Abs. 3 AO: großes Ausmaß, Amtsträger, gefälschte Belege, Bande, Drittstaat-Gesellschaft
- Verfahrensstand: Prüfungsanordnung, Einleitungsbekanntgabe, Durchsuchung, Selbstanzeige erwogen?
- Parallel laufendes Besteuerungsverfahren, Einspruchsfristen, geänderte Bescheide

## Sub-Agent-Architektur

Der **Researcher** ([`../../agents/researcher.md`](../../agents/researcher.md)) ordnet jeden Veranlagungszeitraum der einschlägigen Erklärungspflicht zu und belegt die Verjährungsregeln. Der **Drafter** ([`../../agents/drafter.md`](../../agents/drafter.md)) subsumiert im Gutachtenstil je Tat und formuliert die Einlassung oder die Verteidigungsschrift. Der **Reviewer** ([`../../agents/reviewer.md`](../../agents/reviewer.md)) prüft die Verjährungsberechnung, die Anwendung des Kompensationsverbots und die Abstimmung mit dem Besteuerungsverfahren.

## Ablauf

### 1. Tathandlung bestimmen ([§ 370 Abs. 1 AO](https://www.gesetze-im-internet.de/ao_1977/__370.html))

Drei abschließende Tathandlungen:

| Nr. | Handlung | Typische Konstellation |
|---|---|---|
| 1 | Unrichtige oder unvollständige Angaben über steuerlich erhebliche Tatsachen gegenüber den Finanzbehörden | Betriebsausgaben erfunden, Einnahmen verschwiegen |
| 2 | Pflichtwidriges In-Unkenntnis-Lassen der Finanzbehörden über steuerlich erhebliche Tatsachen | Steuererklärung gar nicht abgegeben trotz Erklärungspflicht |
| 3 | Pflichtwidriges Unterlassen der Verwendung von Steuerzeichen oder Steuerstemplern | Verbrauchsteuern |

Nr. 2 setzt eine **Rechtspflicht zur Offenbarung** voraus — sie folgt aus §§ 149, 150 AO, den Einzelsteuergesetzen und aus [§ 153 AO](https://www.gesetze-im-internet.de/ao_1977/__153.html) (Berichtigungspflicht bei nachträglichem Erkennen). Die Abgrenzung zwischen einer bloßen Berichtigung nach § 153 AO und einer Selbstanzeige nach § 371 AO ist der praktisch heikelste Punkt und regelmäßig entscheidend für die Frage, ob überhaupt eine Tat vorliegt.

### 2. Erfolg: Steuerverkürzung oder Steuervorteil ([§ 370 Abs. 4 AO](https://www.gesetze-im-internet.de/ao_1977/__370.html))

Steuern sind namentlich dann verkürzt, wenn sie **nicht, nicht in voller Höhe oder nicht rechtzeitig festgesetzt** werden. Das gilt auch, wenn die Steuer vorläufig oder unter Vorbehalt der Nachprüfung festgesetzt wird. Steuervorteile sind auch Steuervergütungen; sie sind erlangt, soweit sie zu Unrecht gewährt oder belassen werden.

### 3. Vollendung und Versuch ([§ 370 Abs. 2 AO](https://www.gesetze-im-internet.de/ao_1977/__370.html))

Der **Vollendungszeitpunkt** ist die zentrale Weichenstellung für die Verjährung und hängt von der Steuerart ab:

- **Veranlagungssteuern** (Einkommen-, Körperschaft-, Gewerbesteuer): Vollendung mit **Bekanntgabe des unrichtigen Steuerbescheids**. Bei Nichtabgabe: wenn die Veranlagungsarbeiten für den Bezirk im Wesentlichen abgeschlossen sind.
- **Anmeldungssteuern** (Umsatzsteuer-Voranmeldung, Lohnsteuer): Vollendung mit **Eingang der unrichtigen Anmeldung**, da diese einer Festsetzung unter Vorbehalt gleichsteht ([§ 168 AO](https://www.gesetze-im-internet.de/ao_1977/__168.html)). Bei Nichtabgabe: mit Ablauf der Anmeldefrist.

Der **Versuch ist strafbar** (§ 370 Abs. 2 AO). Das ist praktisch relevant, wenn die Erklärung eingereicht, der Bescheid aber noch nicht ergangen ist — dann kommt neben der Selbstanzeige auch der Rücktritt vom Versuch nach [§ 24 StGB](https://www.gesetze-im-internet.de/stgb/__24.html) in Betracht.

### 4. Besonders schwerer Fall ([§ 370 Abs. 3 AO](https://www.gesetze-im-internet.de/ao_1977/__370.html))

Strafrahmen: **Freiheitsstrafe von sechs Monaten bis zu zehn Jahren**. Die Regelbeispiele des Abs. 3 S. 2 Nr. 1 bis 6:

1. Steuerverkürzung **in großem Ausmaß**,
2. Amtsträger, der seine Befugnisse oder seine Stellung missbraucht,
3. Ausnutzung der Mithilfe eines solchen Amtsträgers,
4. fortgesetzte Verkürzung unter Verwendung **nachgemachter oder verfälschter Belege**,
5. **bandenmäßige** Verkürzung von Umsatz- oder Verbrauchsteuern,
6. Nutzung einer **Drittstaat-Gesellschaft** zur Verschleierung bei fortgesetzter Verkürzung.

Das „große Ausmaß" nach Nr. 1 ist ein betragsbezogener Schwellenwert, den die Rechtsprechung entwickelt hat; die maßgebliche Grenze und ihre Entwicklung sind vor jeder Verwendung zu verifizieren `[unverifiziert – prüfen]`. Die Beträge werden **je Tat** — also je Steuerart und Veranlagungszeitraum — bestimmt, nicht kumuliert über alle Jahre.

### 5. Kompensationsverbot ([§ 370 Abs. 4 S. 3 AO](https://www.gesetze-im-internet.de/ao_1977/__370.html))

Die Tatbestandsmerkmale sind auch dann erfüllt, wenn die Steuer, auf die sich die Tat bezieht, **aus anderen Gründen hätte ermäßigt oder der Steuervorteil aus anderen Gründen hätte beansprucht werden können**. Der Beschuldigte kann verschwiegene Einnahmen also nicht ohne Weiteres mit vergessenen Betriebsausgaben verrechnen.

Die Grenze des Verbots liegt dort, wo Vorteil und Nachteil in einem **unmittelbaren wirtschaftlichen Zusammenhang** mit demselben Vorgang stehen — dann gehören sie zur Berechnung des Verkürzungserfolgs und nicht zur verbotenen Kompensation. Die Reichweite dieser Ausnahme ist einzelfallabhängig und in der Rechtsprechung fortentwickelt worden `[unverifiziert – prüfen]`. Für die Verteidigung ist die Unterscheidung entscheidend: Sie verschiebt den strafrechtlich relevanten Betrag und damit potenziell die Schwelle des großen Ausmaßes.

### 6. Verfolgungsverjährung ([§ 376 AO](https://www.gesetze-im-internet.de/ao_1977/__376.html), [§ 78 StGB](https://www.gesetze-im-internet.de/stgb/__78.html))

- **Einfache Steuerhinterziehung** (§ 370 Abs. 1 AO): Verjährungsfrist **fünf Jahre** nach § 78 Abs. 3 Nr. 4 StGB, da die Höchststrafe fünf Jahre beträgt.
- **Besonders schwerer Fall** in den Konstellationen des § 370 Abs. 3 S. 2 Nr. 1 bis 6 AO: Verjährungsfrist **15 Jahre** (§ 376 Abs. 1 AO).
- **Absolute Grenze** in diesen Fällen: die Verfolgung verjährt spätestens, wenn seit dem Zeitpunkt des § 78a StGB das **Zweieinhalbfache der gesetzlichen Verjährungsfrist** verstrichen ist (§ 376 Abs. 3 AO).
- Der Fristbeginn richtet sich nach [§ 78a StGB](https://www.gesetze-im-internet.de/stgb/__78a.html) — **Beendigung der Tat**, die bei Veranlagungssteuern mit der Bekanntgabe des Bescheids zusammenfällt.
- Unterbrechung nach § 376 Abs. 2 AO und [§ 78c StGB](https://www.gesetze-im-internet.de/stgb/__78c.html), insbesondere durch die Bekanntgabe der Einleitung des Straf- oder Bußgeldverfahrens.

Die **steuerliche Festsetzungsverjährung** ist davon streng zu trennen: Sie beträgt nach [§ 169 Abs. 2 S. 2 AO](https://www.gesetze-im-internet.de/ao_1977/__169.html) bei Steuerhinterziehung zehn Jahre, bei leichtfertiger Steuerverkürzung fünf Jahre. Strafrechtliche und steuerliche Verjährung laufen unabhängig voneinander — ein Zeitraum kann strafrechtlich verjährt und steuerlich noch änderbar sein.

### 7. Leichtfertige Steuerverkürzung ([§ 378 AO](https://www.gesetze-im-internet.de/ao_1977/__378.html))

Handelt der Täter **leichtfertig**, liegt keine Straftat, sondern eine Ordnungswidrigkeit vor; die Geldbuße ist in § 378 Abs. 2 AO betragsmäßig begrenzt. Leichtfertigkeit ist ein erhöhter Grad von Fahrlässigkeit — der Täter lässt die Sorgfalt außer Acht, zu der er nach seinen persönlichen Fähigkeiten und Kenntnissen imstande ist. Für die Verteidigung ist § 378 AO das wichtigste Ausweichziel: Er entzieht dem Vorwurf die Vorsatzkomponente, führt zur Anwendung der kürzeren steuerlichen Festsetzungsfrist von fünf Jahren und eröffnet die Selbstanzeige nach § 378 Abs. 3 AO unter erleichterten Bedingungen.

### 8. Formulierungshilfe — Einlassung zur Vorsatzfrage

```
An die Staatsanwaltschaft <Ort> — Abteilung Wirtschaftsstrafsachen
(nachrichtlich: Finanzamt <Ort>, Straf- und Bußgeldsachenstelle)
Az. <…>

In dem Ermittlungsverfahren gegen <Mandant>
wegen des Vorwurfs der Steuerhinterziehung

nehme ich als Verteidiger wie folgt Stellung:

I.   Umfang der Einlassung
     Der Beschuldigte lässt sich zu den Veranlagungszeiträumen
     <…> ein und schweigt im Übrigen (§ 136 Abs. 1 S. 2 StPO).

II.  Sachverhalt aus Sicht des Beschuldigten
     <Chronologie: wer hat welche Unterlagen wann an wen gegeben;
      Rolle des steuerlichen Beraters; Buchführungsorganisation.>

III. Zur subjektiven Tatseite
     Der Beschuldigte hat die Erklärungen auf Grundlage der vom
     Steuerberater erstellten Unterlagen unterzeichnet. Ein
     Vorsatz — auch kein bedingter — lässt sich daraus nicht
     ableiten. In Betracht kommt allenfalls Leichtfertigkeit im
     Sinne des § 378 AO.

IV.  Zur Berechnung des Verkürzungsbetrages
     Die im Bericht angesetzten Beträge berücksichtigen den
     unmittelbar mit den Mehreinnahmen zusammenhängenden
     Aufwand nicht. Insoweit greift das Kompensationsverbot des
     § 370 Abs. 4 S. 3 AO nach zutreffender Auslegung nicht.

V.   Zur Verjährung
     Die Veranlagungszeiträume <…> sind nach § 78 Abs. 3 Nr. 4
     StGB verjährt; ein Regelbeispiel des § 370 Abs. 3 AO,
     das die Frist des § 376 Abs. 1 AO auslösen würde, liegt
     nicht vor.

VI.  Anträge
     1. Einstellung des Verfahrens nach § 170 Abs. 2 StPO,
        hilfsweise nach § 153a StPO.
     2. Akteneinsicht in die Handakten der Betriebsprüfung.

<Ort, Datum, Unterschrift — Rechtsanwalt, Fachanwalt für Steuerrecht>
```

## Quellen

### Statute

- [§ 370 AO](https://www.gesetze-im-internet.de/ao_1977/__370.html), [§ 376 AO](https://www.gesetze-im-internet.de/ao_1977/__376.html), [§ 378 AO](https://www.gesetze-im-internet.de/ao_1977/__378.html), [§ 153 AO](https://www.gesetze-im-internet.de/ao_1977/__153.html), [§ 168 AO](https://www.gesetze-im-internet.de/ao_1977/__168.html), [§ 169 AO](https://www.gesetze-im-internet.de/ao_1977/__169.html), [§ 149 AO](https://www.gesetze-im-internet.de/ao_1977/__149.html)
- [§ 78 StGB](https://www.gesetze-im-internet.de/stgb/__78.html), [§ 78a StGB](https://www.gesetze-im-internet.de/stgb/__78a.html), [§ 78c StGB](https://www.gesetze-im-internet.de/stgb/__78c.html), [§ 24 StGB](https://www.gesetze-im-internet.de/stgb/__24.html)
- [§ 385 AO](https://www.gesetze-im-internet.de/ao_1977/__385.html), [§ 393 AO](https://www.gesetze-im-internet.de/ao_1977/__393.html) (Verhältnis von Straf- und Besteuerungsverfahren, Zwangsmittelverbot), [§ 170 StPO](https://www.gesetze-im-internet.de/stpo/__170.html), [§ 153a StPO](https://www.gesetze-im-internet.de/stpo/__153a.html)

### Kommentare

- Joecks, in: Joecks / Jäger / Randt, Steuerstrafrecht, 9. Aufl. 2023, § 370 AO Rn. 1 ff.
- Ransiek, in: Kohlmann, Steuerstrafrecht, Loseblatt, § 370 AO Rn. 1 ff. (Kompensationsverbot)
- Klein / Jäger, AO, 17. Aufl. 2023, § 370 Rn. 1 ff. und § 376 Rn. 1 ff.
- Rolletschke, Steuerstrafrecht, 5. Aufl. 2021, Rn. 1 ff. (Vollendung nach Steuerarten)

### Rechtsprechung

- Rechtsprechung zur betragsmäßigen Bestimmung des „großen Ausmaßes" nach § 370 Abs. 3 S. 2 Nr. 1 AO `[unverifiziert – prüfen]`
- Rechtsprechung zur Reichweite des Kompensationsverbots bei unmittelbar zusammenhängenden Aufwendungen `[unverifiziert – prüfen]`
- Rechtsprechung zum Vollendungszeitpunkt bei Nichtabgabe von Veranlagungserklärungen `[unverifiziert – prüfen]`

> Aktenzeichen und Fundstellen sind vor Verwendung in juris, Beck-Online oder über die [BGH-Entscheidungsdatenbank](https://www.bundesgerichtshof.de/DE/Entscheidungen/entscheidungen_node.html) zu ermitteln. In diesem Skill wird bewusst keine Entscheidung benannt, die nicht extern verifiziert wurde.

## Ausgabeformat

```
STEUERHINTERZIEHUNG § 370 AO — <Az.> — <Datum>
VERTRAULICH — STRAFVERTEIDIGUNG — § 43a Abs. 2 BRAO

Gesamtbefund: [🟢 Einstellung erreichbar / 🟡 Verhandlungslösung /
               🔴 Anklage wahrscheinlich]

I.    Tatbegriff                    <Steuerart x Veranlagungszeitraum>
      Anzahl der Taten              <N>
II.   Je Tat
      Tathandlung                   [Abs. 1 Nr. 1 / Nr. 2 / Nr. 3]
      Erklärungspflicht             <§ 149 AO / Einzelsteuergesetz>
      Verkürzungsbetrag             <…> EUR
      Vollendung am                 <Datum>  [Bescheidbekanntgabe /
                                    Anmeldungseingang]
      Versuch § 370 Abs. 2 AO       [N/A / einschlägig]
III.  Subjektiver Tatbestand        [Vorsatz / bedingter Vorsatz /
                                    Leichtfertigkeit § 378 AO]
IV.   Besonders schwerer Fall       [nein / Abs. 3 S. 2 Nr. <…>]
      Großes Ausmaß je Tat          [🟢 nein / 🔴 ja]
V.    Kompensationsverbot           § 370 Abs. 4 S. 3 AO
      Unmittelbarer Zusammenhang    [geltend gemacht für <…>]
VI.   Verjährung
      Frist                         [5 Jahre § 78 StGB /
                                    15 Jahre § 376 Abs. 1 AO]
      Beginn § 78a StGB             <Datum>
      Unterbrechung § 78c StGB      <Datum, Maßnahme>
      Ergebnis je Zeitraum          <verjährt / offen>
VII.  Besteuerungsverfahren
      Festsetzungsfrist § 169 AO    [10 Jahre / 5 Jahre]
      Einspruchsfristen             <Datum>
      § 393 AO Zwangsmittelverbot   [beachtet]
VIII. Selbstanzeige                 [siehe steuerrecht/skills/selbstanzeige]

Empfehlung: <…>
Nächster Schritt: <Akteneinsicht / Einlassung / Verständigung>
```

## Risiken / typische Fehler

- **Taten nicht einzeln geprüft.** Jede Steuerart und jeder Veranlagungszeitraum ist eine eigene Tat; Verjährung, großes Ausmaß und Strafzumessung werden je Tat bestimmt, nicht über die Gesamtsumme.
- **Vollendungszeitpunkt falsch bestimmt.** Bei Anmeldungssteuern tritt Vollendung bereits mit Eingang der Anmeldung ein (§ 168 AO), nicht erst mit einem Bescheid — die Verjährung läuft entsprechend früher an.
- **Strafrechtliche und steuerliche Verjährung vermengt.** § 376 AO und § 169 AO haben unterschiedliche Fristen und Anknüpfungspunkte.
- **Verlängerte Frist des § 376 Abs. 1 AO vorschnell angenommen.** Sie greift nur in den Fällen des § 370 Abs. 3 S. 2 Nr. 1 bis 6 AO.
- **Kompensationsverbot § 370 Abs. 4 S. 3 AO übersehen** — verschwiegene Einnahmen lassen sich nicht ohne Weiteres mit vergessenen Aufwendungen verrechnen; umgekehrt wird der unmittelbare wirtschaftliche Zusammenhang zu selten geltend gemacht.
- **Leichtfertigkeit § 378 AO nicht als Verteidigungsziel verfolgt** — der Übergang zur Ordnungswidrigkeit verkürzt zugleich die steuerliche Festsetzungsfrist.
- **§ 393 AO ignoriert.** Im Besteuerungsverfahren sind Zwangsmittel unzulässig, soweit der Steuerpflichtige sich selbst belasten müsste; Mitwirkung im Besteuerungsverfahren darf nicht ungeprüft in das Strafverfahren durchschlagen.
- **Berichtigung nach § 153 AO als Selbstanzeige behandelt** oder umgekehrt — die Abgrenzung entscheidet über Sperrgründe und Zuschlag.
- **Einspruchsfristen im Besteuerungsverfahren versäumt**, während die Verteidigung sich auf das Strafverfahren konzentriert.
