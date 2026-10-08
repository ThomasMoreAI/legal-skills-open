---
name: revision-strafsachen-borghei
title: /strafrecht:revision-strafsachen
description: Prüfung und Begründung der Revision in Strafsachen – Statthaftigkeit § 333 StPO, Sprungrevision § 335 StPO, Rüge der Gesetzesverletzung § 337 StPO, absolute Revisionsgründe § 338 StPO, Einlegungsfrist § 341 StPO, Form und Begründungsfrist §§ 344, 345 StPO; Verfahrens- vs. Sachrüge. Use when gegen ein Strafurteil Revision zu prüfen, fristgerecht einzulegen oder zu begründen ist.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/strafrecht/skills/revision-strafsachen
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: criminal
language: de
---

# /strafrecht:revision-strafsachen

## Zweck

Die Revision überprüft ein Strafurteil **nur auf Rechtsfehler** — keine neue Tatsachenfeststellung, keine zweite Tatsacheninstanz. Dieser Skill prüft die Statthaftigkeit, wahrt die kurze **Einlegungsfrist von einer Woche** und die **Begründungsfrist von einem Monat**, und unterscheidet sauber zwischen **Verfahrensrüge** und **Sachrüge** — die häufigste Fehlerquelle der Revisionsbegründung.

## Eingaben

- angefochtenes Urteil (Gericht, Datum der Verkündung / Zustellung)
- erstinstanzlich oder Berufungsurteil? (für Sprungrevision relevant)
- behauptete Rechtsfehler (materiell / verfahrensrechtlich)
- Anwesenheit bei Verkündung, Zustellungsdatum des schriftlichen Urteils
- bereits Revision eingelegt? Fristenstand

## Sub-Agent-Architektur

Die Bearbeitung gliedert sich in drei Prosa-Rollen. Ein Statthaftigkeits-Agent klärt, ob gegen das konkrete Urteil die Revision (ggf. als Sprungrevision) eröffnet ist und wer revisionsberechtigt ist. Ein Fristen-Agent berechnet Einlegungs- und Begründungsfrist taggenau und überwacht die Form (Anwaltszwang, § 345 Abs. 2 StPO). Ein Rügen-Agent ordnet jeden Angriff entweder der Sachrüge oder der Verfahrensrüge zu und prüft bei letzterer die strengen Darlegungsanforderungen des § 344 Abs. 2 S. 2 StPO sowie das Vorliegen absoluter Revisionsgründe. Die Rollen sind gedankliche Arbeitsschritte, keine getrennten technischen Prozesse.

## Ablauf

### 1. Statthaftigkeit ([§ 333 StPO](https://www.gesetze-im-internet.de/stpo/__333.html))

Revision ist statthaft gegen Urteile der **Strafkammern** und **Schwurgerichte** sowie gegen erstinstanzliche Urteile der **Oberlandesgerichte**. Gegen amtsgerichtliche Urteile ist regelmäßig zunächst die Berufung eröffnet.

### 2. Sprungrevision ([§ 335 StPO](https://www.gesetze-im-internet.de/stpo/__335.html))

Ein Urteil, gegen das Berufung zulässig wäre (amtsgerichtliches Urteil), kann **statt mit Berufung unmittelbar mit Revision** angefochten werden (Sprungrevision). Legt eine Partei Berufung, die andere Sprungrevision ein, gilt zunächst das Berufungsverfahren (§ 335 Abs. 3 StPO).

### 3. Einlegungsfrist ([§ 341 StPO](https://www.gesetze-im-internet.de/stpo/__341.html))

**Eine Woche ab Urteilsverkündung**, bei Abwesenheit ab Zustellung. Einlegung schriftlich oder zu Protokoll der Geschäftsstelle beim **iudex a quo** (Gericht, dessen Urteil angefochten wird). Versäumung → Verwerfung als unzulässig; Wiedereinsetzung §§ 44 ff. StPO nur bei unverschuldeter Verhinderung.

### 4. Form und Begründungsfrist ([§ 344 StPO](https://www.gesetze-im-internet.de/stpo/__344.html), [§ 345 StPO](https://www.gesetze-im-internet.de/stpo/__345.html))

- **§ 345 Abs. 1 StPO:** Begründung binnen **eines Monats** nach Ablauf der Einlegungsfrist bzw. nach Zustellung des Urteils.
- **§ 345 Abs. 2 StPO:** Begründung nur durch **Anwaltsschriftsatz** oder zu Protokoll der Geschäftsstelle (Anwaltszwang).
- **§ 344 Abs. 1 StPO:** Erklärung, inwieweit das Urteil angefochten und seine Aufhebung beantragt wird (Revisionsanträge).
- **§ 344 Abs. 2 StPO:** Angabe, ob materielles Recht (**Sachrüge**) oder eine Verfahrensnorm (**Verfahrensrüge**) verletzt ist; bei der Verfahrensrüge sind die **den Mangel begründenden Tatsachen vollständig anzugeben** (§ 344 Abs. 2 S. 2 StPO).

### 5. Rügearten

| Rüge | Norm | Anforderung |
|---|---|---|
| **Sachrüge** | [§ 337 StPO](https://www.gesetze-im-internet.de/stpo/__337.html) | „Verletzung materiellen Rechts" — formlos; Urteil wird auf Subsumtions- und Strafzumessungsfehler geprüft |
| **Verfahrensrüge** | § 337 StPO i. V. m. § 344 Abs. 2 S. 2 StPO | Verstoß gegen Verfahrensnorm; lückenloser Tatsachenvortrag, sonst unzulässig |
| **absolute Revisionsgründe** | [§ 338 StPO](https://www.gesetze-im-internet.de/stpo/__338.html) | Beruhen des Urteils wird unwiderleglich vermutet (z. B. nicht vorschriftsmäßig besetztes Gericht, ausgeschlossener Richter, Verletzung der Öffentlichkeit) |

### 6. Beruhensgrundsatz

Bei der **relativen** Sach- und Verfahrensrüge (§ 337 StPO) muss das Urteil **auf** dem Fehler beruhen. Bei den **absoluten** Gründen des § 338 StPO wird das Beruhen unwiderleglich vermutet — hier liegt die strategische Stärke der Verfahrensrüge.

## Quellen

### Statute

- [§ 333 StPO](https://www.gesetze-im-internet.de/stpo/__333.html), [§ 335 StPO](https://www.gesetze-im-internet.de/stpo/__335.html), [§ 337 StPO](https://www.gesetze-im-internet.de/stpo/__337.html), [§ 338 StPO](https://www.gesetze-im-internet.de/stpo/__338.html), [§ 341 StPO](https://www.gesetze-im-internet.de/stpo/__341.html), [§ 344 StPO](https://www.gesetze-im-internet.de/stpo/__344.html), [§ 345 StPO](https://www.gesetze-im-internet.de/stpo/__345.html)
- §§ 44 ff. StPO (Wiedereinsetzung)

### Kommentare

- Meyer-Goßner / Schmitt, StPO, 67. Aufl. 2024, § 337, § 344 Rn. 1 ff.
- Gericke, in: KK-StPO, 9. Aufl. 2023, § 337 Rn. 1 ff.
- Beulke, Strafprozessrecht, 15. Aufl. 2023, Rn. 561 ff.

### Rechtsprechung

- BGH zur Darlegungslast der Verfahrensrüge nach § 344 Abs. 2 S. 2 StPO — Aktenzeichen `[unverifiziert – prüfen]`
- BVerfG zum Beruhen bei absoluten Revisionsgründen § 338 StPO — Aktenzeichen `[unverifiziert – prüfen]`

## Ausgabeformat

```
REVISION STRAFSACHEN — <Mandant-ID> — <Datum>
VERTRAULICH — STRAFVERTEIDIGUNG

I.    Angefochtenes Urteil       <Gericht / Datum>
II.   Statthaftigkeit            [§ 333 / Sprungrevision § 335 StPO]
III.  Fristen
      Einlegung (1 Woche):       Verkündung <…> → Ende <…> [🟢/🔴]
      Begründung (1 Monat):      Ende <…> [🟢/🔴]
      Anwaltszwang § 345 II:     [beachtet ✅]
IV.   Rügen
      Sachrüge (§ 337):          [erhoben / —]
      Verfahrensrüge (§ 344 II): [erhoben — Tatsachenvortrag vollständig? ✅/⚠️]
      Absolute Gründe (§ 338):   <Nr. … / keine>
V.    Beruhen                    [relativ zu prüfen / absolut vermutet]

Erfolgsaussicht: <…>
Nächster Schritt: <…>
```

## Risiken / typische Fehler

- **Einlegungsfrist (eine Woche) versäumt** — Revision wird als unzulässig verworfen; Wiedereinsetzung selten.
- **Verfahrensrüge unzulässig** — Tatsachenvortrag nach § 344 Abs. 2 S. 2 StPO unvollständig; häufigster Verwerfungsgrund.
- **Anwaltszwang** der Begründung (§ 345 Abs. 2 StPO) übersehen — eigenhändige Begründung des Angeklagten genügt nicht.
- **Sach- und Verfahrensrüge verwechselt** — pauschale „Sachrüge" deckt keinen Verfahrensfehler ab.
- **Beruhen** nicht dargelegt, obwohl kein absoluter Grund nach § 338 StPO vorliegt.
