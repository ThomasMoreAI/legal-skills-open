---
name: vorsorgevollmacht-patientenverfuegung-borghei
title: /betreuungsrecht:vorsorgevollmacht-patientenverfuegung
description: 'Prüfung der Vorsorgeinstrumente nach der Reform 2023: Vorsorgevollmacht § 1820 BGB, Patientenverfügung § 1827 BGB (Behandlungswunsch, mutmaßlicher Wille), betreuungsgerichtliche Genehmigung gefährlicher Maßnahmen § 1829 BGB, Vorrang vor Betreuung. Use when eine Vorsorgevollmacht oder Patientenverfügung erstellt, ausgelegt oder ihre Reichweite gegenüber einer Betreuung geprüft wird.'
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/betreuungsrecht/skills/vorsorgevollmacht-patientenverfuegung
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: family
language: de
---

# /betreuungsrecht:vorsorgevollmacht-patientenverfuegung

## Zweck

Vorsorgevollmacht und Patientenverfügung sind die zentralen Instrumente vorsorgender Selbstbestimmung. Eine wirksame Vorsorgevollmacht macht eine rechtliche Betreuung insoweit entbehrlich (Vorrang anderer Hilfen). Dieser Skill prüft Form und Reichweite der Vollmacht, die Bindungswirkung der Patientenverfügung und die betreuungsgerichtliche Genehmigung bei gefährlichen Maßnahmen.

## Eingaben

- Vorsorgevollmacht (Wortlaut, Datum, Form, erfasste Bereiche)
- Patientenverfügung (Wortlaut, Behandlungssituationen, Aktualität)
- Konkrete Behandlungs-/Lebenssituation der betroffenen Person
- Einwilligungs-/Entscheidungsfähigkeit zum Zeitpunkt der Errichtung
- Geplante Maßnahme (medizinischer Eingriff, Unterbringung, Wohnungsauflösung)
- Anhaltspunkte für entgegenstehenden Willen oder Missbrauch

## Sub-Agent-Architektur

Der **Researcher** bestätigt §§ 1820, 1827, 1829 BGB in der seit 2023 geltenden Fassung über gesetze-im-internet.de und ordnet das Verhältnis zur Betreuung ein; ungesicherte Aktenzeichen werden als `[unverifiziert – prüfen]` markiert. Der **Drafter** prüft Wirksamkeit und Reichweite der Vollmacht, die Anwendbarkeit der Patientenverfügung auf die konkrete Situation und das Genehmigungserfordernis. Der **Reviewer** kontrolliert, ob der Vorrang vor der Betreuung beachtet ist, ob der Behandlungswunsch/mutmaßliche Wille methodisch ermittelt wurde und ob keine Tatsachen erfunden wurden.

## Ablauf

### 1. Vorsorgevollmacht (§ 1820 BGB)

[§ 1820 BGB](https://www.gesetze-im-internet.de/bgb/__1820.html): Die Vorsorgevollmacht ermächtigt eine Vertrauensperson, die Angelegenheiten der vollmachtgebenden Person zu besorgen.

- **Schriftliche Spezialvollmacht** für besonders eingriffsintensive Maßnahmen erforderlich (§ 1820 Abs. 2 BGB): Einwilligung/Nichteinwilligung in Maßnahmen nach § 1829 BGB, freiheitsentziehende Unterbringung und ärztliche Zwangsmaßnahmen.
- **Vorrang vor Betreuung:** Soweit die Vollmacht reicht und wirksam ausgeübt wird, ist eine Betreuung nicht erforderlich (§ 1814 Abs. 3 BGB).
- **Kontrollbetreuung (§ 1820 Abs. 3 BGB):** möglich bei konkreten Anhaltspunkten für vollmachtswidriges Handeln.
- **Widerruf/Verbot der Ausübung** durch das Gericht bei Gefahr (§ 1820 Abs. 4, 5 BGB).

### 2. Patientenverfügung (§ 1827 BGB)

[§ 1827 BGB](https://www.gesetze-im-internet.de/bgb/__1827.html): Eine einwilligungsfähige volljährige Person legt schriftlich fest, ob sie in bestimmte, noch nicht unmittelbar bevorstehende Untersuchungen, Behandlungen oder Eingriffe einwilligt oder sie untersagt.

- **Bindungswirkung:** Trifft die Festlegung auf die aktuelle Lebens- und Behandlungssituation zu, ist ihr Geltung zu verschaffen.
- **Behandlungswünsche/mutmaßlicher Wille (§ 1827 Abs. 2 BGB):** Liegt keine (passende) Patientenverfügung vor, sind Behandlungswünsche oder der **mutmaßliche Wille** anhand konkreter Anhaltspunkte (frühere Äußerungen, Wertvorstellungen) zu ermitteln.
- **Kein Errichtungszwang** und kein Bedingen von Leistungen an eine Patientenverfügung.

### 3. Betreuungsgerichtliche Genehmigung (§ 1829 BGB)

[§ 1829 BGB](https://www.gesetze-im-internet.de/bgb/__1829.html): Die Einwilligung, Nichteinwilligung oder der Widerruf des Bevollmächtigten/Betreuers in eine ärztliche Maßnahme bedarf der **Genehmigung des Betreuungsgerichts**, wenn die begründete Gefahr besteht, dass die Person infolge der Maßnahme stirbt oder einen schweren, länger dauernden gesundheitlichen Schaden erleidet.

- **Keine Genehmigung nötig**, wenn Bevollmächtigter/Betreuer und behandelnder Arzt einig sind, dass die Entscheidung dem nach § 1827 BGB festgestellten Willen entspricht.
- Bei Bevollmächtigten gilt das Erfordernis nur bei wirksamer schriftlicher Bevollmächtigung (§ 1820 Abs. 2 BGB).

### 4. Zusammenspiel und Auslegung

- Reichweitenkontrolle: erfasst die Vollmacht die konkrete Maßnahme?
- Aktualitätsprüfung der Patientenverfügung
- Dokumentation des ermittelten Willens

## Risiken / typische Fehler

- **Vorrang vor Betreuung übersehen** — eine wirksame Vorsorgevollmacht macht die Betreuung nach § 1814 Abs. 3 BGB insoweit entbehrlich; dennoch wird ein Betreuer bestellt.
- **Schriftliche Spezialvollmacht fehlt** — ohne ausdrückliche Befugnis nach § 1820 Abs. 2 BGB darf der Bevollmächtigte in gefährliche oder freiheitsentziehende Maßnahmen nicht einwilligen.
- **Patientenverfügung pauschal angewandt** — passt sie nicht auf die aktuelle Situation, ist der Behandlungswunsch/mutmaßliche Wille nach § 1827 BGB zu ermitteln.
- **Genehmigung übergangen** — bei Lebensgefahr/schwerem Schaden ist die betreuungsgerichtliche Genehmigung nach § 1829 BGB einzuholen, sofern kein Konsens mit dem Arzt besteht.
- **Missbrauch der Vollmacht unbeachtet** — bei Anhaltspunkten ist eine Kontrollbetreuung zu prüfen; ungesicherte Aktenzeichen als `[unverifiziert – prüfen]` kennzeichnen.

## Quellen (Reform 2023)

- [§ 1820 BGB](https://www.gesetze-im-internet.de/bgb/__1820.html) (Vorsorgevollmacht, Kontrollbetreuung)
- [§ 1827 BGB](https://www.gesetze-im-internet.de/bgb/__1827.html) (Patientenverfügung, mutmaßlicher Wille)
- [§ 1829 BGB](https://www.gesetze-im-internet.de/bgb/__1829.html) (betreuungsgerichtliche Genehmigung)
- [§ 1814 BGB](https://www.gesetze-im-internet.de/bgb/__1814.html) (Vorrang anderer Hilfen)
- [§ 1831 BGB](https://www.gesetze-im-internet.de/bgb/__1831.html) (freiheitsentziehende Unterbringung)
- BMJ-Informationen zur Betreuungsrechtsreform 2023

## Ausgabeformat

```
VORSORGE-INSTRUMENTE — <betroffene Person> — <Datum>

I.    Vorsorgevollmacht § 1820 BGB
      Form / Reichweite:                  <…>
      Spezialvollmacht (Abs. 2):          [vorhanden / fehlt]
      Vorrang vor Betreuung:              [✓ → Betreuung entbehrlich]
II.   Patientenverfügung § 1827 BGB
      Passt auf aktuelle Situation:       [✓ / 🔴 → mutmaßlicher Wille]
      Behandlungswunsch / Wille:          <…>
III.  Genehmigung § 1829 BGB
      Lebensgefahr / schwerer Schaden:    [ja → Genehmigung]
      Konsens mit Arzt (§ 1827):          [ja → keine Genehmigung]
IV.   Kontrolle / Missbrauch              [Kontrollbetreuung prüfen?]

Empfehlung: <…>
```
