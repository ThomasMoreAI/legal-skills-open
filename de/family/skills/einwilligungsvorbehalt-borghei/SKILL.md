---
name: einwilligungsvorbehalt-borghei
title: /betreuungsrecht:einwilligungsvorbehalt
description: 'Prüfung der Anordnung eines Einwilligungsvorbehalts § 1825 BGB (Reform 2023): Abwehr einer erheblichen Gefahr für Person oder Vermögen, Verhältnismäßigkeit, Reichweite und Ausnahmen. Use when geprüft wird, ob ein Einwilligungsvorbehalt angeordnet, beschränkt oder aufgehoben werden soll.'
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/betreuungsrecht/skills/einwilligungsvorbehalt
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: family
language: de
---

# /betreuungsrecht:einwilligungsvorbehalt

## Zweck

Der Einwilligungsvorbehalt ist der schwerste Eingriff des Betreuungsrechts in die Handlungsfreiheit: Willenserklärungen der betreuten Person werden von der Einwilligung des Betreuers abhängig gemacht. Nach der Reform 2023 ist er nur als letztes Mittel zur Abwehr einer erheblichen Gefahr zulässig. Dieser Skill prüft Voraussetzungen, Verhältnismäßigkeit und Reichweite.

## Eingaben

- Bestehende Betreuung und ihre Aufgabenbereiche (§ 1815 BGB)
- Konkrete erhebliche Gefahr für Person oder Vermögen
- Bisherige mildere Maßnahmen und deren Wirkungslosigkeit
- Geäußerter Wille der betreuten Person
- Vorgesehener Umfang des Vorbehalts (Vermögens-/Personenangelegenheiten)
- Ärztliche/sachverständige Einschätzung zur Gefahrenlage

## Sub-Agent-Architektur

Der **Researcher** bestätigt § 1825 BGB in der seit 2023 geltenden Fassung über gesetze-im-internet.de und ordnet die flankierenden §§ 1814, 1815 BGB ein; ungesicherte Aktenzeichen werden als `[unverifiziert – prüfen]` markiert. Der **Drafter** prüft die erhebliche Gefahr, die Verhältnismäßigkeit (Erforderlichkeit milderer Mittel) und die Reichweite einschließlich der gesetzlichen Ausnahmen. Der **Reviewer** kontrolliert, ob der Verhältnismäßigkeitsgrundsatz konsequent durchgehalten ist, ob die Ausnahmebereiche beachtet sind und ob keine Tatsachen erfunden wurden.

## Ablauf

### 1. Voraussetzungen (§ 1825 Abs. 1 BGB)

[§ 1825 BGB](https://www.gesetze-im-internet.de/bgb/__1825.html): Das Betreuungsgericht ordnet an, dass die betreute Person zu Willenserklärungen, die den Aufgabenbereich des Betreuers betreffen, dessen Einwilligung bedarf, **soweit dies erforderlich ist, um eine erhebliche Gefahr für die Person oder das Vermögen** abzuwenden.

- **Erhebliche Gefahr:** nicht jede nachteilige Entscheidung genügt; gefordert ist eine gewichtige, konkrete Gefahr.
- **Akzessorietät zum Aufgabenbereich:** der Vorbehalt kann nur innerhalb eines bestehenden Aufgabenbereichs (§ 1815 BGB) angeordnet werden.
- **Kein Vorbehalt gegen den freien Willen** (Verweis auf § 1814 Abs. 2 BGB).

### 2. Verhältnismäßigkeit

Als schwerster Eingriff unterliegt der Vorbehalt strenger Verhältnismäßigkeit:

- **Geeignetheit:** der Vorbehalt muss die Gefahr tatsächlich abwenden können
- **Erforderlichkeit:** mildere Mittel (Beratung, Kontowarnungen, Teil-Vorbehalt) müssen ausgeschöpft sein
- **Angemessenheit:** Eingriffstiefe in Relation zur Gefahr

### 3. Reichweite und Ausnahmen (§ 1825 Abs. 2, 3 BGB)

Der Vorbehalt erstreckt sich **nicht** auf:

- Willenserklärungen über Eheschließung/Lebenspartnerschaft
- Verfügungen von Todes wegen (Testament, Erbvertrag)
- Erklärungen, zu denen ein beschränkt Geschäftsfähiger keiner Zustimmung bedarf

Außerdem ist die Einwilligung **nicht** erforderlich für Geschäfte, die der betreuten Person lediglich einen rechtlichen Vorteil bringen, oder für geringfügige Angelegenheiten des täglichen Lebens (§ 1825 Abs. 3 BGB), sofern das Gericht nichts anderes anordnet.

### 4. Rechtsfolgen

- Ohne Einwilligung vorgenommene Geschäfte sind schwebend unwirksam (Verweis auf §§ 108 ff. BGB analog)
- Genehmigung durch den Betreuer möglich
- Regelmäßige Überprüfung und Aufhebung bei Wegfall der Gefahr von Amts wegen

## Risiken / typische Fehler

- **Erhebliche Gefahr nicht belegt** — der Vorbehalt nach § 1825 BGB setzt eine konkrete, gewichtige Gefahr voraus; bloß unvernünftige Entscheidungen genügen nicht.
- **Verhältnismäßigkeit übersprungen** — mildere Mittel müssen ausgeschöpft sein, bevor der schwerste Eingriff angeordnet wird.
- **Reichweite zu weit gefasst** — die gesetzlichen Ausnahmebereiche (Ehe, Testament, lediglich vorteilhafte Geschäfte) dürfen nicht erfasst werden.
- **Freier Wille missachtet** — gegen den freien Willen ist der Vorbehalt unzulässig.
- **Keine Befristung/Überprüfung** — der Vorbehalt ist bei Wegfall der Gefahr aufzuheben; ungesicherte Aktenzeichen als `[unverifiziert – prüfen]` kennzeichnen.

## Quellen (Reform 2023)

- [§ 1825 BGB](https://www.gesetze-im-internet.de/bgb/__1825.html) (Einwilligungsvorbehalt)
- [§ 1814 BGB](https://www.gesetze-im-internet.de/bgb/__1814.html) (Voraussetzungen der Betreuung)
- [§ 1815 BGB](https://www.gesetze-im-internet.de/bgb/__1815.html) (Aufgabenbereiche)
- [§ 1821 BGB](https://www.gesetze-im-internet.de/bgb/__1821.html) (Wünsche der betreuten Person)
- BMJ-Informationen zur Betreuungsrechtsreform 2023

## Ausgabeformat

```
EINWILLIGUNGSVORBEHALT § 1825 BGB — <betroffene Person> — <Datum>

I.    Anknüpfung an Aufgabenbereich § 1815 BGB    [vorhanden ✓]
II.   Erhebliche Gefahr (Abs. 1)
      Person / Vermögen:                  <Beschreibung>
      Konkret und gewichtig:              [✓ / 🔴]
III.  Verhältnismäßigkeit
      Mildere Mittel ausgeschöpft:        [✓ / 🔴]
      Angemessenheit:                     <…>
IV.   Reichweite / Ausnahmen (Abs. 2, 3)
      Ehe / Testament ausgenommen:        [✓]
      Lediglich vorteilhaft / Alltag:     [ausgenommen]
V.    Befristung / Überprüfung           <…>

Empfehlung: <…>
```
