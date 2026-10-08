---
name: selbstanzeige-borghei
title: /steuerrecht:selbstanzeige
description: Prüfung der strafbefreienden Selbstanzeige bei Steuerhinterziehung – Wirksamkeitsvoraussetzungen und Vollständigkeitsgebot § 371 AO, Sperrgründe § 371 Abs. 2 AO (Prüfungsanordnung, Tatentdeckung, Bekanntgabe der Einleitung), fristgerechte Nachzahlung nebst Hinterziehungszinsen, Zuschlag und Absehen von Verfolgung § 398a AO, Abgrenzung zur Berichtigung § 153 AO. Use when eine strafbefreiende Selbstanzeige nach § 371 AO vorbereitet oder auf Wirksamkeit geprüft wird.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/steuerrecht/skills/selbstanzeige
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: tax
language: de
---

# /steuerrecht:selbstanzeige

## Zweck

Die strafbefreiende Selbstanzeige nach [§ 371 AO](https://www.gesetze-im-internet.de/ao_1977/__371.html) ist der einzige Weg, nach vollendeter Steuerhinterziehung ([§ 370 AO](https://www.gesetze-im-internet.de/ao_1977/__370.html)) noch Straffreiheit zu erlangen. Sie ist ein „Alles-oder-Nichts"-Instrument: Wirkt sie nicht vollständig, entfaltet sie keine Sperrwirkung gegen die Strafverfolgung und liefert der Behörde zugleich ein Geständnis. Dieser Skill prüft die Wirksamkeitsvoraussetzungen, identifiziert Sperrgründe und steuert die fristgerechte Nachzahlung.

## Eingaben

- Betroffene Steuerarten und Veranlagungsjahre (ESt, KSt, USt, ErbSt)
- Hinterziehungsvolumen je Tat / je Jahr (Schätzung der verkürzten Steuer)
- Laufende Prüfung, Ermittlung oder bereits bekannt gegebene Einleitung
- Vollständigkeit und Belegbarkeit der nachzuerklärenden Angaben
- Beteiligte (Steuerpflichtiger, Mittäter, Anstifter, Gehilfen)
- Liquidität zur fristgerechten Nachzahlung von Steuer, Zinsen und Zuschlag

## Sub-Agent-Architektur

Die Prüfung gliedert sich in drei gedankliche Rollen, die nacheinander durchlaufen werden. Ein Tatbestands-Prüfer klärt zunächst, ob überhaupt eine vorsätzliche Steuerhinterziehung vorliegt oder lediglich eine schlichte Berichtigung nach § 153 AO genügt — das entscheidet über den anwendbaren Regelungskreis. Ein Wirksamkeits-Prüfer rekonstruiert sodann das Vollständigkeitsgebot, durchmustert sämtliche Sperrgründe und bestimmt den Stichtag, zu dem die Selbstanzeige noch „rechtzeitig" abgegeben werden kann. Ein Folgen-Prüfer berechnet schließlich Nachzahlung, Hinterziehungszinsen und etwaigen Zuschlag nach § 398a AO und bewertet die Berater- und Berufsrechtsrisiken. Die Rollen arbeiten streng sequentiell, weil jede Stufe die nächste sperren kann.

## Ablauf

### 1. Abgrenzung Steuerhinterziehung § 370 AO vs. Berichtigung § 153 AO

- [§ 370 AO](https://www.gesetze-im-internet.de/ao_1977/__370.html) setzt **Vorsatz** voraus (Kennen und Wollen der Steuerverkürzung).
- [§ 153 AO](https://www.gesetze-im-internet.de/ao_1977/__153.html): nachträgliches Erkennen der Unrichtigkeit einer eigenen Erklärung ohne ursprünglichen Vorsatz → schlichte **Berichtigungspflicht**, keine Selbstanzeige nötig.
- Leichtfertige Steuerverkürzung (§ 378 AO) → bußgeldbefreiende Selbstanzeige nach § 378 Abs. 3 AO, mildere Sperrgründe.
- **Praxis**: Die Abgrenzung ist heikel. Im Zweifel wird die Erklärung so formuliert, dass sie zugleich als wirksame Selbstanzeige nach § 371 AO und als Berichtigung nach § 153 AO trägt.

### 2. Vollständigkeitsgebot ([§ 371 Abs. 1 AO](https://www.gesetze-im-internet.de/ao_1977/__371.html))

Das **Vollständigkeitsgebot** verlangt die Berichtigung, Ergänzung oder Nachholung der Angaben zu **allen** unverjährten Steuerstraftaten **einer Steuerart**, mindestens aber zu allen Straftaten dieser Steuerart der letzten **zehn Kalenderjahre**.

- Keine „Teilselbstanzeige": Wird auch nur ein Sachverhalt derselben Steuerart bewusst ausgespart, ist die gesamte Selbstanzeige unwirksam.
- Materielle Vollständigkeit: Die Angaben müssen so präzise sein, dass die Finanzbehörde ohne weitere Ermittlungen veranlagen kann; zulässig sind belastbare Schätzungen mit Sicherheitszuschlag.
- Zeitlicher Berichtigungsverbund: zehn Jahre auch dann, wenn einzelne Jahre strafrechtlich bereits verjährt, steuerlich aber noch offen sind.

### 3. Sperrgründe ([§ 371 Abs. 2 AO](https://www.gesetze-im-internet.de/ao_1977/__371.html))

Liegt ein **Sperrgrund** vor, tritt keine Straffreiheit ein. Die wichtigsten Sperrgründe:

- **Prüfungsanordnung** nach § 196 AO bekannt gegeben (sachlich/zeitlich umfassende Sperre).
- **Bekanntgabe der Einleitung** eines Straf- oder Bußgeldverfahrens.
- **Erscheinen des Prüfers** (Amtsträger) zur steuerlichen Prüfung oder zur Ermittlung einer Steuerstraftat.
- **Tatentdeckung**: Die Tat ist ganz oder teilweise bereits entdeckt und der Täter wusste dies oder musste damit rechnen.
- **Betragsgrenze**: verkürzte Steuer je Tat über **25.000 EUR** → Straffreiheit nur über § 398a AO (siehe Schritt 5).

Jeder Sperrgrund ist gesondert und je Tat zu prüfen; ein einziger greifender **Sperrgrund** kann die Straffreiheit für die betroffene Tat beseitigen.

### 4. Fristgerechte Nachzahlung nebst Zinsen ([§ 371 Abs. 3 AO](https://www.gesetze-im-internet.de/ao_1977/__371.html))

Straffreiheit tritt nur ein, wenn der Täter die hinterzogene Steuer **sowie** die Zinsen fristgerecht **nachzahlt**:

- **Hinterziehungszinsen** [§ 235 AO](https://www.gesetze-im-internet.de/ao_1977/__235.html) auf die verkürzten Beträge.
- Zinsen nach [§ 233a AO](https://www.gesetze-im-internet.de/ao_1977/__233a.html), soweit auf die Hinterziehungszinsen angerechnet.
- Die Finanzbehörde setzt eine **angemessene Frist**; Fristversäumnis lässt die Straffreiheit entfallen.
- Liquiditätsprüfung vorab: Reicht das Vermögen nicht, ist die Selbstanzeige zwar abzugeben, die Straffreiheit aber gefährdet — Ratenstundung mit der Bußgeld- und Strafsachenstelle frühzeitig klären.

### 5. Zuschlag und Absehen von Verfolgung ([§ 398a AO](https://www.gesetze-im-internet.de/ao_1977/__398a.html))

Übersteigt die verkürzte Steuer je Tat **25.000 EUR** oder liegt ein besonders schwerer Fall vor, ist die Selbstanzeige nach § 371 AO gesperrt. Von der Verfolgung wird gleichwohl abgesehen, wenn neben Steuer und Zinsen ein **Zuschlag** gezahlt wird ([§ 398a AO](https://www.gesetze-im-internet.de/ao_1977/__398a.html)):

- **10 %** der hinterzogenen Steuer bei Beträgen bis 100.000 EUR,
- **15 %** über 100.000 bis 1.000.000 EUR,
- **20 %** über 1.000.000 EUR.

Der **Zuschlag** wird je Tat berechnet und ist nicht erstattungsfähig. § 398a AO begründet ein Verfolgungshindernis, keinen Freispruch — bei späterer Unrichtigkeit kann das Verfahren wieder aufgenommen werden (§ 398a Abs. 3 AO).

### 6. Berater- und Berufsrechtsrisiken

- **Eigene Strafbarkeit des Beraters** (Beihilfe § 370 AO i. V. m. § 27 StGB) bei Mitwirkung an der ursprünglichen Hinterziehung gesondert prüfen.
- **Mandatsannahme**: Selbstanzeige nur nach klarer schriftlicher Beauftragung; Interessenkonflikte bei mehreren Beteiligten (§ 43a BRAO / § 6 StBerG).
- **Dokumentation**: Vollständigkeit der erhaltenen Unterlagen aktenkundig machen — der Berater haftet für Lücken nur im Rahmen des ihm Offengelegten.
- **Verschwiegenheit vs. Selbstanzeige Dritter**: keine eigenmächtige Offenbarung ohne Mandatsdeckung.

### 7. Ergebnis

- Wirksamkeit der Selbstanzeige (ja / nein / nur über § 398a AO) je Tat.
- Offene Sperrgründe und verbleibendes Zeitfenster.
- Bezifferte Nachzahlung: Steuer + Hinterziehungszinsen (+ Zuschlag).
- Empfehlung: sofortige Abgabe / Nachschärfung / Abstimmung mit Strafverteidiger.

## Risiken / typische Fehler

- **Teilselbstanzeige** — Aussparen eines Sachverhalts derselben Steuerart macht die gesamte Anzeige unwirksam (Vollständigkeitsgebot).
- **Wettlauf mit der Tatentdeckung** — verzögerte Abgabe lässt einen Sperrgrund (Prüfungsanordnung, Tatentdeckung) reifen.
- **Zu knappe Schätzung** — materielle Unvollständigkeit; stets Sicherheitszuschlag ansetzen.
- **Zinsen und Zuschlag übersehen** — Straffreiheit scheitert ohne fristgerechte Nachzahlung der Hinterziehungszinsen § 235 AO bzw. des Zuschlags § 398a AO.
- **Betragsgrenze 25.000 EUR verkannt** — § 371 AO gesperrt, Weg führt nur über § 398a AO.
- **§ 153 AO mit § 371 AO verwechselt** — bei fehlendem Vorsatz genügt schlichte Berichtigung, eine „Selbstanzeige" wäre überschießendes Geständnis.
- **Selbstanzeige ohne Strafverteidiger-Abstimmung** — Tatbestandsverlust und Eigenbelastung des Beraters riskiert.

## Quellen

### Statute

- [§ 371 AO](https://www.gesetze-im-internet.de/ao_1977/__371.html) (Selbstanzeige bei Steuerhinterziehung; Abs. 1 Vollständigkeit, Abs. 2 Sperrgründe, Abs. 3 Nachzahlung)
- [§ 398a AO](https://www.gesetze-im-internet.de/ao_1977/__398a.html) (Absehen von Verfolgung in besonderen Fällen — Zuschlag)
- [§ 370 AO](https://www.gesetze-im-internet.de/ao_1977/__370.html) (Steuerhinterziehung), [§ 378 AO](https://www.gesetze-im-internet.de/ao_1977/__378.html) (leichtfertige Steuerverkürzung)
- [§ 153 AO](https://www.gesetze-im-internet.de/ao_1977/__153.html) (Anzeige- und Berichtigungspflicht)
- [§ 235 AO](https://www.gesetze-im-internet.de/ao_1977/__235.html) (Verzinsung hinterzogener Steuern), [§ 233a AO](https://www.gesetze-im-internet.de/ao_1977/__233a.html)

### Verwaltungsanweisungen

- AEAO (Anwendungserlass zur Abgabenordnung), insb. zu § 153 AO
- Gleich lautende Ländererlasse zur Behandlung von Selbstanzeigen

### Kommentare

- Klein, AO, 16. Aufl. 2024, § 371, § 398a
- Joecks / Jäger / Randt, Steuerstrafrecht, 9. Aufl. 2023
- Schwarz / Pahlke / Keß, AO, § 371, § 398a

### Rechtsprechung

- BGH-Rechtsprechung zur Vollständigkeit und Tatentdeckung `[unverifiziert – prüfen]`

## Ausgabeformat

```
SELBSTANZEIGE — Wirksamkeitsprüfung — <Mandant> — <Datum>

I.    Tatbestand
      Steuerhinterziehung § 370 (Vorsatz):   [ja / nein → § 153 AO]
      Betroffene Steuerarten / Jahre:        <…>
      Hinterziehungsvolumen je Tat:          <EUR>

II.   Vollständigkeitsgebot § 371 Abs. 1
      Alle Taten einer Steuerart erfasst:    [✓ / ⚠️ Lücke: …]
      Zeitraum (mind. 10 Jahre):             <…>
      Materielle Vollständigkeit/Schätzung:  [✓ / nachschärfen]

III.  Sperrgründe § 371 Abs. 2
      Prüfungsanordnung:                     [nein / ja]
      Bekanntgabe Einleitung:                [nein / ja]
      Erscheinen des Prüfers:                [nein / ja]
      Tatentdeckung:                         [nein / ja]
      Betrag > 25.000 EUR:                   [nein / ja → § 398a]

IV.   Nachzahlung § 371 Abs. 3
      Hinterzogene Steuer:                   <EUR>
      Hinterziehungszinsen § 235:            <EUR>
      Zuschlag § 398a (10/15/20 %):          <EUR / —>
      Frist / Liquidität:                    <…>

V.    Beraterrisiken:                        <…>

Ergebnis:  [wirksam / unwirksam / nur über § 398a]
Folgemaßnahmen:  <sofort abgeben / nachschärfen / Strafverteidiger>
```
