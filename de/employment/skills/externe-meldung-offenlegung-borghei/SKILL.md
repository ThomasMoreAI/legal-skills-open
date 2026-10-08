---
name: externe-meldung-offenlegung-borghei
title: /hinweisgeberschutz:externe-meldung-offenlegung
description: Externe Meldung und Offenlegung nach §§ 7, 19, 28, 32 HinSchG – Wahlrecht zwischen interner und externer Meldung, externe Meldestelle des Bundes beim Bundesamt für Justiz, Verfahren der externen Meldestelle, Voraussetzungen des Schutzes bei Offenlegung an die Öffentlichkeit. Use when ein Hinweisgeber zwischen interner und externer Meldung wählt oder prüfen will, ob eine Offenlegung gegenüber der Öffentlichkeit geschützt ist.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/hinweisgeberschutz/skills/externe-meldung-offenlegung
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: employment
language: de
---

# /hinweisgeberschutz:externe-meldung-offenlegung

## Zweck

Hinweisgeber haben ein **Wahlrecht** zwischen interner und externer Meldung — sie müssen nicht zuerst intern melden. Die **Offenlegung** gegenüber der Öffentlichkeit (Presse, Social Media) ist dagegen nur unter engen Voraussetzungen geschützt. Dieses Skill ordnet den richtigen Meldeweg, erläutert die externe Meldestelle des Bundes und prüft, ob eine geplante Offenlegung den Schutz des HinSchG behält.

## Eingaben

- Gegenstand des Verstoßes und sachlicher Anwendungsbereich (§ 2 HinSchG)
- Bisheriger Meldeweg (noch keine Meldung / intern gemeldet / Frist verstrichen)
- Risiko von Repressalien bei interner Meldung
- Dringlichkeit (Gefahr für öffentliches Interesse, Beweisvernichtung)
- Zuständige externe Meldestelle (Bund / Länder / spezialgesetzlich BaFin, BKartA)

## Sub-Agent-Architektur

Drei gedankliche Rollen arbeiten zusammen. Ein **Weg-Agent** wertet das Wahlrecht nach § 7 HinSchG aus und bestimmt die zuständige Meldestelle. Ein **Verfahrens-Agent** beschreibt das Verfahren der externen Meldestelle nach § 28 HinSchG (Eingangsbestätigung, Folgemaßnahmen) und die externe Meldestelle des Bundes nach § 19 HinSchG. Ein **Offenlegungs-Agent** prüft die strengen Voraussetzungen des Schutzes bei Offenlegung nach § 32 HinSchG. Der Weg-Agent ist vorgeschaltet; der Offenlegungs-Agent warnt vor verfrühter Veröffentlichung, wenn die Voraussetzungen des § 32 nicht erfüllt sind.

## Ablauf

### 1. Wahlrecht interne / externe Meldung § 7 HinSchG

- Der Hinweisgeber **wählt frei**, ob er sich an eine interne Meldestelle (§ 12) oder an eine externe Meldestelle (§§ 19–24) wendet.
- Eine interne Meldung **soll** bevorzugt werden, wenn intern wirksam abgeholfen werden kann und keine Repressalien drohen — eine Pflicht zur internen Vormeldung besteht jedoch nicht.
- Das Behindern einer Meldung ist verboten (§ 7 Abs. 2 HinSchG).

### 2. Externe Meldestelle des Bundes § 19 HinSchG

- Beim **Bundesamt für Justiz** ist eine externe Meldestelle des Bundes errichtet.
- Daneben bestehen besondere externe Meldestellen: **BaFin** (Finanzdienstleistungsaufsicht) und **Bundeskartellamt** (§§ 21, 22 HinSchG) sowie externe Meldestellen der Länder.

### 3. Verfahren der externen Meldestelle § 28 HinSchG

- **Eingangsbestätigung** unverzüglich, spätestens nach **7 Tagen**.
- Prüfung des sachlichen Anwendungsbereichs und der Stichhaltigkeit.
- **Folgemaßnahmen** und Rückmeldung an den Hinweisgeber (§ 29 HinSchG) in angemessener Frist, regelmäßig binnen 3 Monaten (verlängerbar auf 6 Monate).
- Wahrung der **Vertraulichkeit** der Identität (§ 8 HinSchG).

### 4. Schutz bei Offenlegung § 32 HinSchG

Eine **Offenlegung** (Informationen der Öffentlichkeit zugänglich machen) ist nur geschützt, wenn der Hinweisgeber

- zuvor **extern gemeldet** hat und innerhalb der Frist keine geeigneten Folgemaßnahmen ergriffen wurden bzw. keine Rückmeldung erfolgte (§ 32 Abs. 1 Nr. 1), **oder**
- **hinreichenden Grund** zu der Annahme hatte, dass der Verstoß eine unmittelbare oder offenkundige Gefährdung des öffentlichen Interesses darstellt, Repressalien drohen oder Beweise unterdrückt werden könnten (§ 32 Abs. 1 Nr. 2).

### 5. Voraussetzungen des Schutzes § 33 HinSchG

- Auch bei externer Meldung und Offenlegung gelten die allgemeinen Schutzvoraussetzungen: zulässiger Meldeweg, hinreichender Grund, sachlicher Anwendungsbereich.

## Risiken / typische Fehler

- **Offenlegung** ohne Erfüllung der Voraussetzungen des § 32 HinSchG — Verlust des Schutzes, Haftungs- und Strafbarkeitsrisiko.
- **Frist** der externen Meldestelle abgewartet? Voreilige Veröffentlichung vor Ablauf der Reaktionsfrist gefährdet den Schutz.
- **Vertraulichkeit** der eigenen Identität bei Offenlegung selbst aufgegeben — danach keine Anonymität mehr.
- Belastende Reaktion des Arbeitgebers auf die externe Meldung — vermutete **Repressalie** nach § 36 HinSchG.
- Falsche externe Meldestelle adressiert — Zuständigkeit BaFin / BKartA / Länder nicht geprüft.

## Ausgabeformat

```
EXTERNE MELDUNG / OFFENLEGUNG — PRÜFPROTOKOLL — <Mandant> — <Datum>

I.    Anwendungsbereich § 2        [erfasst / nicht erfasst]
II.   Wahlrecht § 7                [interne / externe Meldung]  Empfehlung: <…>
III.  Zuständige Meldestelle       [BfJ § 19 / BaFin / BKartA / Land]
IV.   Verfahren § 28               Eingangsbestätigung ≤ 7 Tage; Rückmeldung: <…>
V.    Offenlegung § 32             Voraussetzung: [Nr. 1 Fristablauf / Nr. 2 Gefahr]
                                   geschützt: [✓ / 🟡 / ✗]
VI.   Schutzvoraussetzungen § 33   hinreichender Grund: [✓/✗]
VII.  Repressalienrisiko § 36      Schutzmaßnahmen: <…>

Hinweis: Offenlegung erst nach Prüfung des § 32 — sonst Schutzverlust.
```

## Quellen

### Statute

- [§ 7 HinSchG](https://www.gesetze-im-internet.de/hinschg/__7.html) (Wahlrecht interne/externe Meldung)
- [§ 19 HinSchG](https://www.gesetze-im-internet.de/hinschg/__19.html) (externe Meldestelle des Bundes)
- [§ 28 HinSchG](https://www.gesetze-im-internet.de/hinschg/__28.html) (Verfahren der externen Meldestelle)
- [§ 32 HinSchG](https://www.gesetze-im-internet.de/hinschg/__32.html) (Schutz bei Offenlegung)
- [§§ 21, 22, 29, 33 HinSchG](https://www.gesetze-im-internet.de/hinschg/) (BaFin/BKartA, Rückmeldung, Voraussetzungen)
- [Richtlinie (EU) 2019/1937](https://eur-lex.europa.eu/eli/dir/2019/1937/oj) (Art. 10, 15 externe Meldung/Offenlegung)

### Behörden

- BfJ – Externe Meldestelle des Bundes: https://www.bundesjustizamt.de/

### Sekundärliteratur

- Reufels, Hinweisgeberschutz, 1. Aufl. 2024
- Schmidt-Husson, HinSchG-Praxiskommentar, 2. Aufl. 2024
- BeckOK HinSchG (Online)
