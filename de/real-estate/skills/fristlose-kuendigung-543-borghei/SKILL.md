---
name: fristlose-kuendigung-543-borghei
title: /mietrecht:fristlose-kuendigung-543
description: Außerordentliche fristlose Kündigung des Mietverhältnisses aus wichtigem Grund – wichtiger Grund und Regelbeispiele § 543 Abs. 2 BGB, Zahlungsverzug § 543 Abs. 2 S. 1 Nr. 3 BGB, Abmahnung und Fristsetzung § 543 Abs. 3 BGB, ergänzende Wohnraumtatbestände § 569 BGB, Schonfristzahlung § 569 Abs. 3 Nr. 2 BGB, Form und Begründung § 569 Abs. 4, § 568 BGB, Verhältnis zur hilfsweise erklärten ordentlichen Kündigung § 573 Abs. 2 Nr. 1 BGB. Use when ein Vermieter wegen Zahlungsverzugs oder Pflichtverletzung fristlos kündigen will oder ein Mieter eine erhaltene fristlose Kündigung prüft.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/mietrecht/skills/fristlose-kuendigung-543
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: real-estate
language: de
---

# /mietrecht:fristlose-kuendigung-543

## Zweck

Die fristlose Kündigung beendet das Mietverhältnis sofort — und scheitert in der Praxis überwiegend an Formalien: fehlende Abmahnung, falsch gerechneter Rückstand, unvollständige Begründung. Diese Skill prüft den wichtigen Grund nach § 543 BGB, rechnet den Zahlungsrückstand deterministisch nach, klärt die Wirkung einer **Schonfristzahlung** und ordnet die praktisch stets mitzuerklärende **hilfsweise ordentliche Kündigung** ein.

## Eingaben

- **Kündigungsgrund**: Zahlungsverzug / unbefugte Gebrauchsüberlassung / erhebliche Gefährdung der Mietsache / nachhaltige Störung des Hausfriedens / sonstiges
- Bei Zahlungsverzug: **Mietkonto** mit Sollstellungen, Zahlungseingängen und Verrechnungsangaben; vereinbarter Fälligkeitstag
- **Abmahnungen** (Datum, Inhalt, Zugangsnachweis)
- **Kündigungsschreiben** (Wortlaut, Unterschriften, Zugangsdatum) bzw. Entwurf
- Ob eine **Schonfristzahlung** erfolgt oder eine Übernahmeerklärung des Sozialleistungsträgers vorliegt
- Ob **hilfsweise ordentlich** gekündigt wurde; Mietdauer für § 573c BGB

## Sub-Agent-Architektur

Die Prüfung wird in Prosa von spezialisierten Schritten getragen; einen `agents`-Block trägt diese Skill bewusst nicht (mietrecht-Konvention). Ein **Rückstands-Rechner** ermittelt zuerst rein arithmetisch, welcher Betrag zu welchem Stichtag offen war, und ordnet Zahlungen nach § 366 BGB zu. Ein **Tatbestands-Prüfer** subsumiert unter § 543 Abs. 2 BGB und § 569 BGB. Ein **Abmahnungs-Prüfer** klärt, ob eine Abmahnung erforderlich war und ob sie inhaltlich und im Zugang trägt. Ein **Form-Prüfer** kontrolliert Schriftform, Begründung und Vertretungsnachweis. Ein **Heilungs-Prüfer** bewertet Schonfristzahlung und Aufrechnung sowie die Fortwirkung auf die hilfsweise ordentliche Kündigung. Erst die Zusammenschau ergibt das Beendigungsdatum.

## Ablauf

### 1. Wichtiger Grund — Generalklausel ([§ 543 Abs. 1 BGB](https://www.gesetze-im-internet.de/bgb/__543.html))

Jede Vertragspartei kann aus **wichtigem Grund** außerordentlich fristlos kündigen. Ein wichtiger Grund liegt vor, wenn dem Kündigenden unter Berücksichtigung aller Umstände des Einzelfalls, insbesondere eines Verschuldens der Vertragsparteien, und unter Abwägung der beiderseitigen Interessen die Fortsetzung des Mietverhältnisses **bis zum Ablauf der Kündigungsfrist oder bis zur sonstigen Beendigung** nicht zugemutet werden kann. Die Abwägung ist stets vorzunehmen — auch beim Vorliegen eines Regelbeispiels.

### 2. Regelbeispiele ([§ 543 Abs. 2 BGB](https://www.gesetze-im-internet.de/bgb/__543.html))

- **Nr. 1** — dem Mieter wird der vertragsgemäße Gebrauch ganz oder zum Teil nicht rechtzeitig gewährt oder wieder entzogen (Kündigungsrecht des **Mieters**).
- **Nr. 2** — der Mieter verletzt die Rechte des Vermieters dadurch erheblich, dass er die Mietsache durch **Vernachlässigung der Sorgfalt erheblich gefährdet** oder sie **unbefugt einem Dritten überlässt**.
- **Nr. 3** — der Mieter ist mit der Entrichtung der Miete **in Verzug**.

### 3. Zahlungsverzug ([§ 543 Abs. 2 S. 1 Nr. 3 BGB](https://www.gesetze-im-internet.de/bgb/__543.html))

Zwei alternative Tatbestände:

- **Buchstabe a** — der Mieter ist für **zwei aufeinander folgende Termine** mit der Entrichtung der Miete oder eines **nicht unerheblichen Teils** der Miete in Verzug. Nicht unerheblich ist ein Rückstand, der die Miete für **einen Monat** übersteigt (§ 569 Abs. 3 Nr. 1 BGB).
- **Buchstabe b** — der Mieter ist in einem **Zeitraum, der sich über mehr als zwei Termine erstreckt**, mit der Entrichtung der Miete in Höhe eines Betrages in Verzug, der die Miete für **zwei Monate** erreicht.

Maßgeblich ist die **Bruttomiete** einschließlich Vorauszahlungen. Verzug setzt Fälligkeit und Vertretenmüssen voraus; eine Mahnung ist bei kalendermäßig bestimmter Leistungszeit entbehrlich (§ 286 Abs. 2 Nr. 1 BGB). Berechtigte **Minderung** (§ 536 BGB) reduziert die geschuldete Miete und damit den Rückstand — hier liegt die häufigste Verteidigungslinie des Mieters.

### 4. Abmahnung und Fristsetzung ([§ 543 Abs. 3 BGB](https://www.gesetze-im-internet.de/bgb/__543.html))

Besteht der wichtige Grund in der **Verletzung einer Pflicht aus dem Mietvertrag**, ist die Kündigung erst **nach erfolglosem Ablauf einer zur Abhilfe bestimmten Frist oder nach erfolgloser Abmahnung** zulässig. Ausnahmen (Abs. 3 S. 2): Fristsetzung/Abmahnung offensichtlich erfolglos; sofortige Kündigung aus besonderen Gründen unter Abwägung gerechtfertigt; **Zahlungsverzug nach Abs. 2 Nr. 3** (Nr. 3 — hier ist eine Abmahnung entbehrlich). Die Abmahnung muss das beanstandete Verhalten konkret bezeichnen und die Kündigung in Aussicht stellen; Zugangsnachweis führen.

### 5. Ergänzende Wohnraumtatbestände ([§ 569 BGB](https://www.gesetze-im-internet.de/bgb/__569.html))

- **Abs. 1** — erhebliche Gesundheitsgefährdung als wichtiger Grund für den Mieter, auch wenn er den Zustand bei Vertragsschluss kannte.
- **Abs. 2** — **nachhaltige Störung des Hausfriedens** als wichtiger Grund für beide Seiten.
- **Abs. 2a** — Verzug mit einer **Sicherheitsleistung** nach § 551 BGB in Höhe von zwei Monatsmieten.
- **Abs. 3 Nr. 1** — Konkretisierung des „nicht unerheblichen Teils": Rückstand muss die Miete für einen Monat übersteigen.
- **Abs. 4** — der **Kündigungsgrund ist im Kündigungsschreiben anzugeben**.

### 6. Schonfristzahlung ([§ 569 Abs. 3 Nr. 2 BGB](https://www.gesetze-im-internet.de/bgb/__569.html))

Die Kündigung wegen Zahlungsverzugs wird **unwirksam**, wenn der Vermieter spätestens **bis zum Ablauf von zwei Monaten nach Eintritt der Rechtshängigkeit des Räumungsanspruchs** hinsichtlich der fälligen Miete und der fälligen Entschädigung nach § 546a Abs. 1 BGB **befriedigt** wird oder sich eine **öffentliche Stelle zur Befriedigung verpflichtet**. Die Heilung tritt **nicht** ein, wenn ihr bereits **zwei Jahre** zuvor eine Schonfristzahlung vorausgegangen ist. Ebenso wird die Kündigung unwirksam, wenn der Mieter vor Zugang **aufgerechnet** und dies unverzüglich erklärt hat (§ 543 Abs. 2 S. 3 BGB).

**Entscheidende Reichweite:** Die Schonfristzahlung beseitigt nach der Rechtsprechung des VIII. Zivilsenats nur die **fristlose**, nicht die zugleich hilfsweise erklärte **ordentliche** Kündigung (BGH, Urt. v. 13.10.2021 – VIII ZR 91/20, https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2021-10-13&Aktenzeichen=VIII%20ZR%2091/20). Das ist der Grund, weshalb in der Praxis stets beide Kündigungen erklärt werden.

### 7. Form und Begründung ([§ 568 BGB](https://www.gesetze-im-internet.de/bgb/__568.html), § 569 Abs. 4 BGB)

Die Kündigung eines Wohnraummietverhältnisses bedarf der **Schriftform** (§ 568 Abs. 1 BGB, § 126 BGB) — Textform genügt hier **nicht**. Sie muss von **allen Vermietern** an **alle Mieter** gerichtet und unterschrieben sein; bei Vertretung ist die Originalvollmacht beizufügen (§ 174 BGB). Der Kündigungsgrund ist nach § 569 Abs. 4 BGB **im Schreiben anzugeben** — bei Zahlungsverzug genügt regelmäßig die Angabe des Gesamtrückstands und der Zahlungsperioden. Auf die Möglichkeit des Widerspruchs ist bei ordentlicher Kündigung hinzuweisen (§ 568 Abs. 2 BGB).

### 8. Hilfsweise ordentliche Kündigung ([§ 573 Abs. 2 Nr. 1 BGB](https://www.gesetze-im-internet.de/bgb/__573.html))

Die schuldhafte, nicht unerhebliche Vertragsverletzung ist zugleich ein **berechtigtes Interesse** für die ordentliche Kündigung. Sie ist mit derselben Erklärung **hilfsweise** auszusprechen, damit eine Schonfristzahlung nicht das gesamte Verfahren entwertet. Für sie gelten die Fristen des [§ 573c BGB](https://www.gesetze-im-internet.de/bgb/__573c.html) (3 / 6 / 9 Monate) und die **Sozialklausel** der §§ 574 ff. BGB; vgl. `/mietrecht:sozialklausel-widerspruch`. Anders als bei der fristlosen Kündigung ist hier eine **Abmahnung** regelmäßig erforderlich.

### 9. Durchsetzung

Nach Ablauf des Kündigungstermins besteht ein Rückgabeanspruch aus [§ 546 BGB](https://www.gesetze-im-internet.de/bgb/__546.html); bis zur Rückgabe schuldet der Mieter Nutzungsentschädigung nach [§ 546a BGB](https://www.gesetze-im-internet.de/bgb/__546a.html). Zur Klage: `/mietrecht:raeumungsklage`.

## Deterministische Berechnung

Der Zahlungsrückstand trägt ab Verzugseintritt Zinsen nach [§ 288 BGB](https://www.gesetze-im-internet.de/bgb/__288.html) i.V.m. [§ 247 BGB](https://www.gesetze-im-internet.de/bgb/__247.html). Der Rechner in [`../../../scripts/legal_calc/`](../../../scripts/legal_calc/) macht **nur die Arithmetik** — der Verzugsbeginn, die Frage der Verbraucherbeteiligung (5 statt 9 Prozentpunkte) und eine berechtigte Minderung bleiben juristische Eingaben. Der Basiszinssatz ist Pflichteingabe und gegen die Veröffentlichung der Deutschen Bundesbank zu prüfen.

```bash
# Rückstand 2.400 EUR (zwei Bruttomonatsmieten), Verzug seit 05.01.2026
python -m scripts.legal_calc.cli verzugszinsen --betrag 2400 \
    --verzug-ab 05.01.2026 --bis 21.07.2026 --basiszins 01.01.2026:1.10

# Zinslauf über einen Basiszins-Wechsel: segmentweise Rechnung
python -m scripts.legal_calc.cli verzugszinsen --betrag 2400 \
    --verzug-ab 05.01.2026 --bis 15.09.2026 \
    --basiszins 01.01.2026:1.10 --basiszins 01.07.2026:1.20

# Schonfristzahlung: 2 Monate ab Rechtshängigkeit (Zustellung 10.03.2026)
python -m scripts.legal_calc.cli frist --ereignis 10.03.2026 --menge 2 --einheit monate --land NW
```

`--json` liefert die Rechenschritte samt Normzitat. **Nie** den Gesamtrückstand ohne Abgleich mit dem Mietkonto und ohne Prüfung von Minderung und Aufrechnung in die Kündigung schreiben — ein zu hoch angesetzter Rückstand macht die Kündigung angreifbar.

## Quellen

### Statute

- [§ 543 BGB](https://www.gesetze-im-internet.de/bgb/__543.html), [§ 569 BGB](https://www.gesetze-im-internet.de/bgb/__569.html), [§ 568 BGB](https://www.gesetze-im-internet.de/bgb/__568.html)
- [§ 573 BGB](https://www.gesetze-im-internet.de/bgb/__573.html), [§ 573c BGB](https://www.gesetze-im-internet.de/bgb/__573c.html), [§ 574 BGB](https://www.gesetze-im-internet.de/bgb/__574.html)
- [§ 546 BGB](https://www.gesetze-im-internet.de/bgb/__546.html), [§ 546a BGB](https://www.gesetze-im-internet.de/bgb/__546a.html), [§ 551 BGB](https://www.gesetze-im-internet.de/bgb/__551.html)
- [§ 286 BGB](https://www.gesetze-im-internet.de/bgb/__286.html), [§ 288 BGB](https://www.gesetze-im-internet.de/bgb/__288.html), [§ 247 BGB](https://www.gesetze-im-internet.de/bgb/__247.html), [§ 366 BGB](https://www.gesetze-im-internet.de/bgb/__366.html)

### Kommentare

- Blank, in: Schmidt-Futterer, Mietrecht, 15. Aufl. 2023, § 543 BGB Rn. 1 ff.
- Streyl, in: Schmidt-Futterer, Mietrecht, 15. Aufl. 2023, § 569 BGB Rn. 1 ff.
- Bieber, in: MüKoBGB, 9. Aufl. 2023, § 543 Rn. 1 ff.
- Weidenkaff, in: Grüneberg, BGB, 84. Aufl. 2025, § 543 Rn. 1 ff.

### Rechtsprechung

- BGH, Urt. v. 13.10.2021 – VIII ZR 91/20 (Schonfristzahlung wirkt nur auf die fristlose, nicht auf die hilfsweise ordentliche Kündigung) — verifiziert: https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2021-10-13&Aktenzeichen=VIII%20ZR%2091/20
- BGH, Urt. v. 24.08.2016 – VIII ZR 261/15 (Ausschluss der fristlosen Kündigung wegen Zahlungsverzugs) — verifiziert: https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2016-08-24&Aktenzeichen=VIII%20ZR%20261/15
- Zur Berechnung des „nicht unerheblichen Teils" und zur Wirkung berechtigter Minderung auf den Rückstand ist die einschlägige BGH-Rechtsprechung heranzuziehen `[unverifiziert - prüfen]`.

## Formulierungshilfe — Fristlose Kündigung wegen Zahlungsverzugs

```
Einschreiben / Bote

Sehr geehrte Frau …, sehr geehrter Herr …,

hiermit kündige ich das Mietverhältnis über die Wohnung <Anschrift, Lage im
Haus> gemäß § 543 Abs. 1, Abs. 2 S. 1 Nr. 3 lit. b BGB, § 569 Abs. 3 BGB
fristlos, hilfsweise ordentlich zum nächstzulässigen Termin gemäß
§ 573 Abs. 2 Nr. 1 BGB.

Begründung (§ 569 Abs. 4 BGB): Sie befinden sich mit der Zahlung der
Bruttomiete in Verzug. Offen sind:

   Monat <…>:  <Betrag> EUR
   Monat <…>:  <Betrag> EUR
   Monat <…>:  <Betrag> EUR
   Gesamtrückstand zum <Datum>: <Betrag> EUR

Der Rückstand erreicht damit die Miete für zwei Monate. Eine Abmahnung ist
nach § 543 Abs. 3 S. 2 Nr. 3 BGB entbehrlich.

Ich fordere Sie auf, die Wohnung bis zum <Datum> geräumt und in
vertragsgemäßem Zustand herauszugeben (§ 546 Abs. 1 BGB). Bis zur Rückgabe
schulden Sie Nutzungsentschädigung nach § 546a Abs. 1 BGB.

Auf die Möglichkeit, die fristlose Kündigung durch vollständige Zahlung
innerhalb der Schonfrist des § 569 Abs. 3 Nr. 2 BGB unwirksam werden zu
lassen, weise ich hin. Die hilfsweise erklärte ordentliche Kündigung bleibt
davon unberührt.

Mit freundlichen Grüßen
<Unterschrift aller Vermieter — Vollmacht in Urschrift anbei>
```

## Ausgabeformat

```
FRISTLOSE KÜNDIGUNG § 543 BGB — Prüfung — <Mandat-ID> — <Datum>

I.    Kündigungsgrund                   [Zahlungsverzug / Gebrauchsüberlassung /
                                         Gefährdung / Hausfrieden / sonst.]
II.   Rückstandsberechnung              Sollstellungen: <Betrag>
                                        Zahlungen:      <Betrag>
                                        Minderung:      <Betrag / keine>
                                        Rückstand:      <Betrag> = <…> Monatsmieten
      Tatbestand § 543 Abs. 2 Nr. 3     [lit. a / lit. b / nicht erfüllt]
III.  Interessenabwägung (§ 543 Abs. 1) [zumutbar / unzumutbar]
IV.   Abmahnung (§ 543 Abs. 3)          [erforderlich+erfolgt / entbehrlich / fehlt ❌]
V.    Form (§ 568, § 569 Abs. 4)        [✅ / ❌]
      - Schriftform, Unterschriften     [✅ / ❌]
      - Alle Vermieter / alle Mieter    [✅ / ❌]
      - Grund angegeben                 [✅ / ⚠️]
VI.   Schonfristzahlung (§ 569 Abs. 3 Nr. 2) [nicht erfolgt / erfolgt / Sperre 2 Jahre]
      Wirkung                           [fristlos geheilt / ordentlich bleibt]
VII.  Hilfsweise ordentliche Kündigung  [erklärt / nicht erklärt ⚠️]
      Frist § 573c BGB                  [3 / 6 / 9 Monate] → Ende <Datum>
VIII. Verzugszinsen (§§ 288, 247)       <Betrag> (Rechner, Stand <Datum>)

Ergebnis: <Mietverhältnis beendet zum … / fortbestehend>
Risiko Räumungsklage: [🟢 / 🟡 / 🔴]
```

## Risiken / typische Fehler

- **Rückstand zu hoch angesetzt** — berechtigte Minderung, Aufrechnung oder falsche Tilgungsreihenfolge (§ 366 BGB) nicht berücksichtigt; die Kündigung wird dadurch insgesamt angreifbar.
- **Abmahnung fehlt** — bei allen Gründen außer Zahlungsverzug regelmäßig zwingend (§ 543 Abs. 3 BGB); auch für die hilfsweise ordentliche Kündigung erforderlich.
- **Hilfsweise ordentliche Kündigung nicht erklärt** — eine Schonfristzahlung entwertet dann das gesamte Verfahren.
- **Schriftform verfehlt** — E-Mail oder Fax genügen für die Wohnraumkündigung nicht (§ 568 Abs. 1 BGB); fehlende Unterschrift eines Mitvermieters macht die Kündigung unwirksam.
- **Vollmacht nicht in Urschrift beigefügt** — Zurückweisung nach § 174 BGB.
- **Zwei-Jahres-Sperre der Schonfristzahlung übersehen** — eine erneute Heilung tritt nicht ein.
- **Kündigungsgrund im Schreiben nicht angegeben** (§ 569 Abs. 4 BGB) — Nachschieben von Gründen ist nur eingeschränkt möglich.
- **Interessenabwägung unterlassen** — auch beim Regelbeispiel ist § 543 Abs. 1 BGB zu prüfen, insbesondere bei langjährigen Mietverhältnissen und geringem Verschulden.
