---
name: agg-entschaedigung-borghei
title: /arbeitsrecht:agg-entschaedigung
description: 'Entschädigung und Schadensersatz wegen Benachteiligung nach § 15 AGG – Benachteiligungsverbot §§ 1, 3, 7 AGG, Rechtfertigung §§ 8–10 AGG, Indizienbeweis und Beweislastumkehr § 22 AGG, zweistufiges Fristenregime (§ 15 Abs. 4 AGG: 2 Monate schriftliche Geltendmachung; § 61b Abs. 1 ArbGG: 3 Monate Klagefrist), Bewerberfälle und Deckelung § 15 Abs. 2 S. 2 AGG, kein Einstellungsanspruch § 15 Abs. 6 AGG, AGG-Hopping als Rechtsmissbrauchseinwand. Use when ein abgelehnter Bewerber oder ein Beschäftigter Entschädigung geltend macht oder ein Arbeitgeber eine AGG-Forderung abwehrt.'
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/arbeitsrecht/skills/agg-entschaedigung
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: employment
language: de
---

# /arbeitsrecht:agg-entschaedigung

## Zweck

AGG-Verfahren werden fast nie über die Diskriminierung entschieden, sondern über zwei Vorfragen: Ist die **2-Monats-Frist** des § 15 Abs. 4 AGG gewahrt, und reichen die vorgetragenen **Indizien** für die Vermutungswirkung des § 22 AGG? Dieser Skill arbeitet beide Fragen zuerst ab und bewertet erst danach Höhe und Rechtfertigung.

## Eingaben

- **Rolle:** abgelehnter Bewerber / Beschäftigter / Arbeitgeber (Abwehr)
- **Merkmal** nach [§ 1 AGG](https://www.gesetze-im-internet.de/agg/__1.html): Rasse oder ethnische Herkunft, Geschlecht, Religion oder Weltanschauung, Behinderung, Alter, sexuelle Identität
- **Benachteiligungshandlung:** Ablehnung, Nichtbeförderung, Entgeltdifferenz, Belästigung, Kündigung
- **Zeitpunkt des Zugangs der Ablehnung** bzw. der Kenntniserlangung — Fristauslöser des § 15 Abs. 4 S. 2 AGG
- **Indizien:** Ausschreibungstext, Absageschreiben, Gesprächsprotokolle, Statistik, Zeugen
- Bruttomonatsentgelt bzw. hypothetisches Einstiegsgehalt (für die Bemessung)

## Sub-Agent-Architektur

1. **Researcher** ([`../../agents/researcher.md`](../../agents/researcher.md)) liefert AGG- und ArbGG-Normen mit URL, EuGH-Linien zu Richtlinie 2000/78/EG und 2006/54/EG, Kommentarstellen (ErfK, BeckOK, MüKoBGB).
2. **Drafter** ([`../../agents/drafter.md`](../../agents/drafter.md)) erstellt das Geltendmachungsschreiben bzw. die Klageschrift oder — auf Arbeitgeberseite — die Erwiderung.
3. **Reviewer** ([`../../agents/reviewer.md`](../../agents/reviewer.md)) prüft zuerst beide Fristen, dann Indizienkette und Bezifferung.

## Ablauf

### 1. Anwendungsbereich und Benachteiligung ([§ 7 AGG](https://www.gesetze-im-internet.de/agg/__7.html), [§ 3 AGG](https://www.gesetze-im-internet.de/agg/__3.html))

Beschäftigte im Sinne des § 6 AGG sind auch **Bewerber** — unabhängig davon, ob sie objektiv geeignet waren. Zu unterscheiden sind:

- **Unmittelbare Benachteiligung** (§ 3 Abs. 1 AGG): ungünstigere Behandlung wegen eines Merkmals.
- **Mittelbare Benachteiligung** (§ 3 Abs. 2 AGG): neutrales Kriterium mit typisierender Benachteiligungswirkung — rechtfertigungsfähig bei sachlichem Ziel und Verhältnismäßigkeit.
- **Belästigung** (§ 3 Abs. 3 AGG) und **sexuelle Belästigung** (§ 3 Abs. 4 AGG).
- **Anweisung** zur Benachteiligung (§ 3 Abs. 5 AGG).

Rechtfertigung nur nach [§ 8 AGG](https://www.gesetze-im-internet.de/agg/__8.html) (wesentliche berufliche Anforderung), § 9 AGG (Religionsgemeinschaften), § 10 AGG (zulässige Altersdifferenzierung) oder § 5 AGG (positive Maßnahmen).

### 2. Indizienbeweis und Beweislastumkehr ([§ 22 AGG](https://www.gesetze-im-internet.de/agg/__22.html))

§ 22 AGG verlangt **kein** Vollbeweis der Diskriminierung. Beweist die benachteiligte Partei Indizien, die eine Benachteiligung wegen eines Merkmals **vermuten** lassen, trägt der Arbeitgeber die Beweislast dafür, dass kein Verstoß vorlag.

Anerkannte Indizien in der Praxis:

| Indiz | Merkmal |
|---|---|
| Ausschreibung „junges, dynamisches Team", „Berufseinsteiger" | Alter |
| Ausschreibung nicht geschlechtsneutral (fehlendes „(m/w/d)") | Geschlecht |
| Frage nach Schwangerschaft oder Kinderwunsch im Vorstellungsgespräch | Geschlecht |
| Absage unmittelbar nach Offenlegung einer Schwerbehinderung | Behinderung |
| Verstoß des öffentlichen Arbeitgebers gegen die Einladungspflicht schwerbehinderter Bewerber (§ 165 S. 3 SGB IX) | Behinderung |
| Statistische Auffälligkeit in Verbindung mit weiteren Umständen | alle |

**Auf Arbeitgeberseite** ist die Widerlegung nur über einen lückenlos dokumentierten, merkmalsneutralen Auswahlprozess zu führen: Anforderungsprofil vor Sichtung, einheitliche Bewertungsmatrix, Aufbewahrung der Bewerbungsunterlagen (im Spannungsfeld zu Art. 5 Abs. 1 lit. e DSGVO — Aufbewahrung für die Dauer des Fristenregimes ist zulässig und geboten).

### 3. Fristenregime — die eigentliche Hürde

**Stufe 1 — [§ 15 Abs. 4 AGG](https://www.gesetze-im-internet.de/agg/__15.html):** Der Anspruch muss innerhalb von **zwei Monaten schriftlich geltend gemacht** werden, sofern Tarifvertragsparteien nichts anderes vereinbart haben. Fristbeginn:

- bei Bewerbung oder beruflichem Aufstieg: **Zugang der Ablehnung**,
- in allen anderen Fällen: Kenntnis von der Benachteiligung.

Schriftform bedeutet hier § 126 BGB in der Auslegung der Praxis; eine bloße E-Mail ist riskant. Die Geltendmachung muss den Anspruch nach Grund und ungefährer Höhe erkennen lassen — eine Bezifferung ist nicht zwingend, aber empfehlenswert.

**Stufe 2 — [§ 61b Abs. 1 ArbGG](https://www.gesetze-im-internet.de/arbgg/__61b.html):** Die Entschädigungsklage muss innerhalb von **drei Monaten, nachdem der Anspruch schriftlich geltend gemacht worden ist**, erhoben werden. Die Frist läuft ab der Geltendmachung, **nicht** ab der Ablehnung — beide Fristen sind getrennt zu berechnen.

§ 61b Abs. 2, 3 ArbGG enthält zudem eine Konzentrationszuständigkeit bei mehreren Bewerberklagen und die Möglichkeit des Arbeitgebers, die mündliche Verhandlung um bis zu sechs Monate hinauszuschieben.

### 4. Rechtsfolgen ([§ 15 AGG](https://www.gesetze-im-internet.de/agg/__15.html))

- **§ 15 Abs. 1 AGG — Schadensersatz** für Vermögensschäden; setzt Vertretenmüssen voraus.
- **§ 15 Abs. 2 S. 1 AGG — Entschädigung** für immaterielle Schäden; **verschuldensunabhängig**. Bemessung nach Art und Schwere, Dauer, Anlass, Beweggrund und Sanktionszweck; die Praxis bewegt sich häufig zwischen einem und drei Bruttomonatsgehältern.
- **§ 15 Abs. 2 S. 2 AGG — Deckelung:** Bei Nichteinstellung höchstens **drei Monatsgehälter**, wenn der Bewerber auch bei benachteiligungsfreier Auswahl nicht eingestellt worden wäre. Trägt der Arbeitgeber diese hypothetische Kausalität vor, ist er dafür darlegungs- und beweisbelastet.
- **§ 15 Abs. 3 AGG:** Bei Anwendung kollektivrechtlicher Vereinbarungen Entschädigung nur bei Vorsatz oder grober Fahrlässigkeit.
- **§ 15 Abs. 6 AGG:** **Kein** Anspruch auf Begründung eines Beschäftigungsverhältnisses oder auf Beförderung. Ein Antrag auf Einstellung ist unbegründet.

### 5. Einwand des Rechtsmissbrauchs — „AGG-Hopping"

Der Arbeitgeber kann dem Anspruch nach [§ 242 BGB](https://www.gesetze-im-internet.de/bgb/__242.html) entgegenhalten, der Bewerber habe sich nicht ernsthaft beworben, sondern gezielt die Entschädigung angestrebt (subjektives Element). Der EuGH hat den Missbrauchseinwand im Grundsatz anerkannt, verlangt aber eine Gesamtwürdigung; die bloße Vielzahl von Bewerbungen genügt nicht (EuGH-Rspr. zur Bewerbereigenschaft und zum Rechtsmissbrauch `[unverifiziert – prüfen]`).

Indizien, die der Arbeitgeber vortragen kann:

- Bewerbungen ausschließlich auf Stellen mit erkennbar fehlerhafter Ausschreibung,
- Bewerbungsunterlagen, die auf die Merkmalsoffenlegung zugeschnitten sind,
- Serienbewerbungen bei überregional gestreuten, offensichtlich ungeeigneten Positionen,
- vorformulierte Geltendmachungsschreiben, die vor der Absage erstellt wurden,
- bekannte Vorprozesse desselben Bewerbers.

Die Darlegungslast für den Missbrauch trägt der **Arbeitgeber**; der Einwand ist eine Ausnahme, kein Regelverteidigungsmittel.

### 6. Formulierungshilfe — Geltendmachungsschreiben (§ 15 Abs. 4 AGG)

```
Einschreiben mit Rückschein

<Arbeitgeber, Anschrift>

Geltendmachung von Ansprüchen nach § 15 AGG
Ihre Absage vom <Datum>, zugegangen am <Datum>
Bewerbung um die Stelle als <Position>, Ausschreibung vom <Datum>

Sehr geehrte Damen und Herren,

in vorbezeichneter Angelegenheit zeige ich die Vertretung von
Herrn/Frau <Name> an. Ordnungsgemäße Bevollmächtigung wird
anwaltlich versichert.

Namens und in Vollmacht meiner Mandantschaft mache ich hiermit
fristwahrend Ansprüche auf Entschädigung nach § 15 Abs. 2 AGG
sowie auf Schadensersatz nach § 15 Abs. 1 AGG geltend.

Die Benachteiligung wegen des Merkmals <Merkmal, § 1 AGG> ergibt
sich aus folgenden Indizien im Sinne des § 22 AGG:
  1. <Ausschreibungstext im Wortlaut, Datum, Fundstelle>
  2. <Äußerung im Vorstellungsgespräch, Datum, Zeugen>
  3. <weiteres Indiz>

Die Entschädigung wird auf <Betrag> EUR beziffert; dies entspricht
<N> Bruttomonatsgehältern des ausgeschriebenen Einstiegsgehalts.

Ich fordere Sie auf, den Betrag bis zum <Datum, mind. 2 Wochen>
auf das Konto <…> zu zahlen. Nach fruchtlosem Fristablauf ist
Klage zum Arbeitsgericht <Ort> beabsichtigt; auf die Klagefrist
des § 61b Abs. 1 ArbGG weise ich vorsorglich hin.

Mit freundlichen Grüßen
<Name>, Rechtsanwältin / Rechtsanwalt
```

## Deterministische Berechnung

Beide Fristen sind Ereignisfristen nach [§ 187 Abs. 1 BGB](https://www.gesetze-im-internet.de/bgb/__187.html) mit Verschiebung des Endes nach [§ 193 BGB](https://www.gesetze-im-internet.de/bgb/__193.html). Der Rechner in [`../../../scripts/legal_calc/`](../../../scripts/legal_calc/) leistet **nur die Arithmetik** — der Zugangszeitpunkt der Ablehnung, der Zeitpunkt der Kenntniserlangung und die Frage, ob ein Tarifvertrag eine abweichende Frist setzt, sind vorgelagerte juristische Wertungen.

```bash
# Stufe 1: Absage zugegangen am 12.02.2026
#          → 2 Monate schriftliche Geltendmachung, § 15 Abs. 4 AGG
python -m scripts.legal_calc.cli frist --ereignis 12.02.2026 --menge 2 --einheit monate --land HE

# Stufe 2: Geltendmachung zugegangen am 20.03.2026
#          → 3 Monate Klagefrist, § 61b Abs. 1 ArbGG
python -m scripts.legal_calc.cli frist --ereignis 20.03.2026 --menge 3 --einheit monate --land HE

# Monatsende-Überlauf (§ 188 Abs. 3 BGB) prüfen, z. B. Absage am 31.12.2025
python -m scripts.legal_calc.cli frist --ereignis 31.12.2025 --menge 2 --einheit monate --land HE --json
```

Der zweite Aufruf hängt vom **Zugang der Geltendmachung** ab, nicht vom Absagedatum — das ist der am häufigsten falsch gerechnete Punkt des gesamten AGG-Mandats.

## Quellen

### Statute

- [§ 1 AGG](https://www.gesetze-im-internet.de/agg/__1.html), [§ 2 AGG](https://www.gesetze-im-internet.de/agg/__2.html), [§ 3 AGG](https://www.gesetze-im-internet.de/agg/__3.html), [§ 7 AGG](https://www.gesetze-im-internet.de/agg/__7.html), [§ 8 AGG](https://www.gesetze-im-internet.de/agg/__8.html), [§ 11 AGG](https://www.gesetze-im-internet.de/agg/__11.html), [§ 15 AGG](https://www.gesetze-im-internet.de/agg/__15.html), [§ 22 AGG](https://www.gesetze-im-internet.de/agg/__22.html)
- [§ 61b ArbGG](https://www.gesetze-im-internet.de/arbgg/__61b.html), [§ 12a ArbGG](https://www.gesetze-im-internet.de/arbgg/__12a.html)
- [§ 187 BGB](https://www.gesetze-im-internet.de/bgb/__187.html), [§ 193 BGB](https://www.gesetze-im-internet.de/bgb/__193.html), [§ 242 BGB](https://www.gesetze-im-internet.de/bgb/__242.html)
- Richtlinie 2000/78/EG (Rahmenrichtlinie Beschäftigung), Richtlinie 2006/54/EG (Gleichbehandlung Geschlecht)

### Kommentare

- Schlachter, in: ErfK, 24. Aufl. 2024, § 15 AGG Rn. 1 ff.
- Thüsing, in: MüKoBGB, 9. Aufl. 2023, § 15 AGG Rn. 1 ff. (Bemessung der Entschädigung)
- Bauer / Krieger / Günther, AGG, 6. Aufl. 2022, § 22 Rn. 1 ff. (Indizienbeweis)
- Roloff, in: BeckOK Arbeitsrecht, § 61b ArbGG Rn. 1 ff.

### Rechtsprechung

- st. Rspr. des BAG zu § 22 AGG (Indizien müssen die Benachteiligung mit überwiegender Wahrscheinlichkeit nahelegen) `[unverifiziert – prüfen]`
- st. Rspr. des BAG zu § 165 S. 3 SGB IX (unterbliebene Einladung schwerbehinderter Bewerber beim öffentlichen Arbeitgeber als Indiz) `[unverifiziert – prüfen]`
- st. Rspr. des BAG zu § 15 Abs. 4 AGG (Wahrung der Schriftform und Inhalt der Geltendmachung) `[unverifiziert – prüfen]`
- EuGH-Rspr. zur Bewerbereigenschaft und zum Rechtsmissbrauch bei nicht ernsthaften Bewerbungen `[unverifiziert – prüfen]`

> Aktenzeichen sind vor Verwendung in juris, Beck-Online, [curia.europa.eu](https://curia.europa.eu) oder der [BAG-Entscheidungsdatenbank](https://www.bundesarbeitsgericht.de/entscheidungen/) zu ermitteln.

## Ausgabeformat

```
AGG-ENTSCHÄDIGUNG — <Mandat-ID> — <Datum>
VERTRAULICH — MANDATSGEHEIMNIS — § 43a Abs. 2 BRAO

⚠️ FRISTBLOCK
    Zugang der Ablehnung:        <Datum>
    Ende § 15 Abs. 4 AGG:        <Datum>  [scripts/legal_calc]
    Geltendmachung zugegangen:   <Datum>
    Ende § 61b Abs. 1 ArbGG:     <Datum>  [scripts/legal_calc]

I.    Beschäftigteneigenschaft § 6 AGG      [🟢 / 🔴]
II.   Merkmal § 1 AGG                       <…>
III.  Benachteiligungsform § 3 AGG          [unmittelbar / mittelbar /
                                             Belästigung / Anweisung]
IV.   Indizien § 22 AGG                     [🟢 tragfähig / 🟡 / 🔴 dünn]
      1. <…>
      2. <…>
V.    Rechtfertigung §§ 8–10 AGG            [N/A / greift / greift nicht]
VI.   Fristen                               [🟢 gewahrt / 🔴 versäumt]
VII.  Bezifferung
      Grundlage:                            <Bruttomonatsgehalt>
      Forderung § 15 Abs. 2 AGG:            <Betrag>
      Deckelung § 15 Abs. 2 S. 2 AGG:       [greift / greift nicht]
      Schadensersatz § 15 Abs. 1 AGG:       <Betrag / keiner>
VIII. Kein Einstellungsanspruch § 15 Abs. 6 AGG — Mandant belehrt am <Datum>
IX.   Einwand AGG-Hopping                   [nicht erhoben / erhoben —
                                             Indizien: <…>]

Offene Tatsachenfragen: <…>
Empfehlung: <…>
```

## Risiken / typische Fehler

- **2-Monats-Frist des § 15 Abs. 4 AGG versäumt** — der Anspruch ist dann ausgeschlossen, unabhängig davon, wie eindeutig die Diskriminierung war.
- **Klagefrist § 61b ArbGG ab dem Absagedatum gerechnet** statt ab der schriftlichen Geltendmachung — die beiden Fristen laufen versetzt.
- **Geltendmachung per einfacher E-Mail** — die Schriftform des § 15 Abs. 4 AGG ist streitig ausgelegt; Einschreiben oder Botenzustellung wählen.
- **Einstellungsanspruch geltend gemacht** — § 15 Abs. 6 AGG schließt ihn aus; der Antrag ist unbegründet und verteuert nur das Verfahren.
- **Indizien nur behauptet, nicht bewiesen** — § 22 AGG verlangt den **Beweis** der Indizien; erst dann kehrt sich die Beweislast um.
- **Arbeitgeberseitig: Bewerbungsunterlagen zu früh gelöscht** — die Widerlegung nach § 22 AGG wird ohne Dokumentation unmöglich; Aufbewahrung bis Ablauf der Fristen ist datenschutzrechtlich zulässig.
- **Ausschreibung nicht merkmalsneutral** — „(m/w/d)" fehlt, Altersangaben, „Muttersprachler" — jede dieser Formulierungen ist ein Indiz nach § 11 AGG i.V.m. § 22 AGG.
- **AGG-Hopping-Einwand ohne Tatsachenvortrag** erhoben — der Missbrauchseinwand ist darlegungsbedürftig und scheitert regelmäßig an bloßen Vermutungen.
- **§ 12a ArbGG übersehen** — auch der obsiegende Arbeitgeber erhält in erster Instanz keine Anwaltskosten erstattet; das ist bei der Vergleichsbewertung einzupreisen.
