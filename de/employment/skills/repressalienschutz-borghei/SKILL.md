---
name: repressalienschutz-borghei
title: /hinweisgeberschutz:repressalienschutz
description: Schutz hinweisgebender Personen vor Benachteiligung nach §§ 33, 36, 37 HinSchG – Verbot von Repressalien, Beweislastumkehr nach § 36 Abs. 2 HinSchG, Schadensersatzanspruch des Hinweisgebers, Voraussetzungen des Schutzes. Use when ein Hinweisgeber nach einer Meldung eine berufliche Benachteiligung erleidet oder ein Arbeitgeber eine Personalmaßnahme gegen einen Hinweisgeber auf Repressalienrisiko prüfen lässt.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/hinweisgeberschutz/skills/repressalienschutz
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: employment
language: de
---

# /hinweisgeberschutz:repressalienschutz

## Zweck

Der materielle Kern des HinSchG ist das **Repressalienverbot**: Wer eine geschützte Meldung abgibt, darf dafür keine berufliche Benachteiligung erleiden. Die **Beweislastumkehr** verschiebt das Prozessrisiko auf den Arbeitgeber — erleidet der Hinweisgeber nach der Meldung einen Nachteil, wird die Repressalie vermutet. Dieses Skill prüft die Schutzvoraussetzungen, die Beweislage und den Schadensersatzanspruch.

## Eingaben

- Meldung / Offenlegung (Datum, Kanal, intern § 17 / extern § 28 / Offenlegung § 32)
- Gutgläubigkeit zum Zeitpunkt der Meldung (hinreichender Grund)
- Erlittene Maßnahme (Kündigung, Abmahnung, Versetzung, Nichtbeförderung, Mobbing)
- Zeitlicher Zusammenhang zwischen Meldung und Maßnahme
- Begründung des Arbeitgebers für die Maßnahme

## Sub-Agent-Architektur

Drei gedankliche Rollen arbeiten zusammen. Ein **Voraussetzungs-Agent** prüft, ob eine geschützte Meldung nach § 33 HinSchG vorliegt (zulässiger Meldeweg, hinreichender Grund, sachlicher Anwendungsbereich). Ein **Beweis-Agent** ordnet die erlittene Maßnahme als mögliche Repressalie ein und wendet die Beweislastumkehr nach § 36 Abs. 2 HinSchG an. Ein **Anspruchs-Agent** beziffert den Schadensersatz nach § 37 HinSchG und prüft flankierende arbeitsrechtliche Ansprüche. Der Voraussetzungs-Agent ist vorgeschaltet: Ohne geschützte Meldung greifen weder Beweislastumkehr noch Schadensersatz.

## Ablauf

### 1. Schutzvoraussetzungen § 33 HinSchG

- Geschützte Meldung über einen internen Meldeweg (§ 17), externen Meldeweg (§ 28) oder eine Offenlegung (§ 32).
- **Hinreichender Grund** zur Annahme, dass die gemeldete Information zum Zeitpunkt der Meldung der Wahrheit entsprach (§ 33 Abs. 1 Nr. 3 HinSchG) — Gutgläubigkeit genügt, Richtigkeit ist nicht erforderlich.
- Information betrifft Verstöße im sachlichen Anwendungsbereich (§ 2 HinSchG).

### 2. Verbot von Repressalien § 36 Abs. 1 HinSchG

- **Repressalien** gegen hinweisgebende Personen sind verboten, einschließlich Androhung und Versuch.
- Erfasst werden u. a. Kündigung, Abmahnung, Versetzung, Versagung einer Beförderung, Disziplinarmaßnahme, Diskriminierung, Rufschädigung.

### 3. Beweislastumkehr § 36 Abs. 2 HinSchG

- Erleidet der Hinweisgeber eine **Benachteiligung im Zusammenhang mit seiner beruflichen Tätigkeit** und macht er geltend, diese sei Folge der Meldung, so wird **vermutet**, dass die Benachteiligung eine Repressalie ist.
- Der Arbeitgeber muss dann **beweisen**, dass die Maßnahme auf hinreichend gerechtfertigten Gründen beruhte und nicht an die Meldung anknüpft.

### 4. Schadensersatz § 37 HinSchG

- Bei Verstoß gegen das Repressalienverbot ist der Verursacher zum **Ersatz des entstehenden Schadens** verpflichtet (§ 37 Abs. 1).
- Kein Anspruch auf Begründung eines Arbeitsverhältnisses oder Beförderung (§ 37 Abs. 2).
- Daneben: arbeitsrechtliche Unwirksamkeit der Kündigung, allgemeine Ansprüche.

### 5. Grenzen des Schutzes

- Kein Schutz bei **vorsätzlich oder grob fahrlässig falscher Meldung** (§ 38 HinSchG: umgekehrter Schadensersatzanspruch des Betroffenen).
- Keine Privilegierung bei bewusst unrichtigen Angaben.

## Risiken / typische Fehler

- **Beweislastumkehr** verkannt — der Arbeitgeber trägt nach § 36 Abs. 2 HinSchG die Beweislast, nicht der Hinweisgeber.
- **Repressalie** zeitnah zur Meldung ausgesprochen — enger zeitlicher Zusammenhang stützt die Vermutung.
- **Hinreichender Grund** des Hinweisgebers ignoriert — Schutz besteht auch bei objektiv unzutreffender, aber gutgläubiger Meldung.
- **Frist** und Form arbeitsrechtlicher Gegenwehr (z. B. 3-Wochen-Frist der Kündigungsschutzklage) versäumt.
- Maßnahme ohne dokumentierte, von der Meldung unabhängige Gründe — Beweisführung des Arbeitgebers scheitert.

## Ausgabeformat

```
REPRESSALIENSCHUTZ — PRÜFPROTOKOLL — <Mandant> — <Datum>

I.    Geschützte Meldung § 33      Weg: [intern § 17 / extern § 28 / Offenlegung § 32]
II.   Hinreichender Grund § 33 Abs. 1 Nr. 3  [gutgläubig / zweifelhaft / fehlend]
III.  Maßnahme                     [Kündigung / Versetzung / Abmahnung / …]
IV.   Zeitlicher Zusammenhang      Meldung: <Datum>  Maßnahme: <Datum>
V.    Repressalienverbot § 36 Abs.1 [einschlägig / nicht einschlägig]
VI.   Beweislastumkehr § 36 Abs.2  Vermutung greift: [✓/✗]  Gegenbeweis AG: <…>
VII.  Schadensersatz § 37          Position: <Verdienstausfall / immateriell / …>
VIII. Flankierende Ansprüche       [Kündigungsschutzklage / Weiterbeschäftigung]

Hinweis: Bei vorsätzlich falscher Meldung droht Gegenanspruch nach § 38 HinSchG.
```

## Quellen

### Statute

- [§ 33 HinSchG](https://www.gesetze-im-internet.de/hinschg/__33.html) (Voraussetzungen für den Schutz)
- [§ 33 Abs. 1 Nr. 3 HinSchG](https://www.gesetze-im-internet.de/hinschg/__33.html) (Hinreichender Grund zur Annahme der Wahrheit)
- [§ 36 HinSchG](https://www.gesetze-im-internet.de/hinschg/__36.html) (Verbot von Repressalien, Abs. 2 Beweislastumkehr)
- [§ 37 HinSchG](https://www.gesetze-im-internet.de/hinschg/__37.html) (Schadensersatz)
- [§ 38 HinSchG](https://www.gesetze-im-internet.de/hinschg/__38.html) (Schadensersatz bei falscher Meldung)
- [Richtlinie (EU) 2019/1937](https://eur-lex.europa.eu/eli/dir/2019/1937/oj) (Art. 19–21 Schutzmaßnahmen)

### Sekundärliteratur

- Reufels, Hinweisgeberschutz, 1. Aufl. 2024
- Schmidt-Husson, HinSchG-Praxiskommentar, 2. Aufl. 2024
- BeckOK HinSchG (Online)
