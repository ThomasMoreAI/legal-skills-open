---
name: interne-meldung-bearbeitung-borghei
title: /hinweisgeberschutz:interne-meldung-bearbeitung
description: Bearbeitung einer eingegangenen internen Meldung durch die Meldestelle nach §§ 8, 13, 17, 18 HinSchG – Eingangsbestätigung binnen 7 Tagen, Prüfung der Stichhaltigkeit, Folgemaßnahmen, Rückmeldung binnen 3 Monaten, Vertraulichkeitsgebot und Dokumentation. Use when eine interne Meldestelle eine eingegangene Hinweisgebermeldung verfahrenskonform bearbeiten und fristgerecht beantworten muss.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/hinweisgeberschutz/skills/interne-meldung-bearbeitung
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: employment
language: de
---

# /hinweisgeberschutz:interne-meldung-bearbeitung

## Zweck

Nach Einrichtung der Meldestelle entscheidet die **Bearbeitungsqualität** über die Wirksamkeit des Hinweisgeberschutzes. Fristverstöße, Vertraulichkeitsbrüche und unterlassene Folgemaßnahmen verlagern den Schutz auf die externe Meldestelle, schwächen die Beweisposition des Arbeitgebers im Repressalienstreit und können Bußgelder auslösen. Dieses Skill steuert die verfahrenskonforme Bearbeitung von der Eingangsbestätigung bis zur Rückmeldung.

## Eingaben

- Meldung (Kanal, Datum, anonym / offen, Inhalt)
- Sachlicher Anwendungsbereich (§ 2 HinSchG) — fällt der Verstoß darunter?
- Beteiligte Personen (Hinweisgeber, betroffene Person, Dritte)
- Bestehende Untersuchungs- und Eskalationsprozesse
- Frühere Meldungen / Zusammenhang

## Sub-Agent-Architektur

Drei gedankliche Rollen bearbeiten den Vorgang. Ein **Eingangs-Agent** erfasst die Meldung, hält Fristen nach (Eingangsbestätigung 7 Tage, Rückmeldung 3 Monate) und sichert die Vertraulichkeit nach § 8 HinSchG. Ein **Prüf-Agent** beurteilt die Stichhaltigkeit und den sachlichen Anwendungsbereich und wählt die Folgemaßnahmen nach § 18 HinSchG. Ein **Eskalations-Agent** prüft Interessenkonflikte, leitet bei Strafverdacht an zuständige Stellen weiter und dokumentiert nach § 11 HinSchG. Der Eingangs-Agent hat Vorrang bei Fristen und Vertraulichkeit; der Eskalations-Agent kann den Prüf-Agent bei Befangenheit der Meldestelle übersteuern.

## Ablauf

### 1. Eingang und Bestätigung § 17 Abs. 1 HinSchG

- **Eingangsbestätigung** an den Hinweisgeber binnen **7 Tagen** nach Eingang.
- Prüfung, ob der gemeldete Verstoß in den sachlichen Anwendungsbereich (§ 2 HinSchG) fällt.
- Kontakt zum Hinweisgeber aufrechterhalten, ggf. um weitere Informationen ersuchen.

### 2. Aufgaben der Meldestelle § 13 HinSchG

- Betrieb der Meldekanäle, Empfang in der gewählten Form.
- Prüfung der **Stichhaltigkeit** der Meldung.
- Auch anonyme Meldungen sollen bearbeitet werden.

### 3. Folgemaßnahmen § 18 HinSchG

- **Interne Untersuchung** beim Beschäftigungsgeber durchführen.
- Betroffene Personen und Arbeitseinheiten kontaktieren.
- Verweis des Hinweisgebers an **andere zuständige Stellen** (z. B. Behörde).
- **Verfahrenseinstellung** mangels Stichhaltigkeit oder aus anderen Gründen.
- Abgabe des Verfahrens an eine zuständige interne Stelle zur weiteren Untersuchung.

### 4. Rückmeldung § 17 Abs. 2 HinSchG

- **Rückmeldung** an den Hinweisgeber binnen **3 Monaten** nach der Eingangsbestätigung.
- Inhalt: geplante und ergriffene Folgemaßnahmen und deren Gründe — soweit interne Untersuchungen oder Rechte Dritter nicht entgegenstehen.

### 5. Vertraulichkeit § 8 HinSchG

- Identität von Hinweisgeber, betroffener Person und Dritten ist **vertraulich** zu behandeln (Vertraulichkeitsgebot).
- Offenbarung nur in den engen Ausnahmen des § 9 HinSchG (Einwilligung, gesetzliche Pflicht, Strafverfolgung).

### 6. Interessenkonflikt und Unabhängigkeit

- Die mit der Bearbeitung betraute Person muss unabhängig und frei von **Interessenkonflikt** sein.
- Betrifft die Meldung die zuständige Person selbst, ist der Vorgang abzugeben.

### 7. Dokumentation § 11 HinSchG

- Vorgang dokumentieren; Aufbewahrung **3 Jahre** nach Verfahrensabschluss, dann Löschung.

## Risiken / typische Fehler

- **Frist** für Eingangsbestätigung (7 Tage) oder Rückmeldung (3 Monate) versäumt — Verstoß gegen § 17 HinSchG, Hinweisgeber darf extern melden.
- **Vertraulichkeit** gebrochen (Weitergabe der Identität an Vorgesetzte) — Verstoß gegen § 8 HinSchG, bußgeldbewehrt.
- **Interessenkonflikt** der bearbeitenden Person nicht erkannt — Vorgang hätte abgegeben werden müssen.
- Belastende Maßnahme gegen den Hinweisgeber während der Bearbeitung — vermutete **Repressalie** nach § 36 HinSchG.
- Anonyme Meldung ungeprüft verworfen — Verstoß gegen die Bearbeitungspflicht.

## Ausgabeformat

```
INTERNE MELDUNG — BEARBEITUNGSPROTOKOLL — <Meldestelle> — <Datum>

I.    Eingang                      Kanal: <…>  Datum: <…>  anonym: [ja/nein]
II.   Eingangsbestätigung § 17     versendet am: <Datum>  (≤ 7 Tage: [✓/✗])
III.  Anwendungsbereich § 2        [erfasst / nicht erfasst]
IV.   Stichhaltigkeit § 13         [stichhaltig / offen / unbegründet]
V.    Folgemaßnahmen § 18          [interne Untersuchung / Verweis / Einstellung]
VI.   Rückmeldung § 17 Abs. 2      Frist: <Datum, ≤ 3 Monate>
VII.  Vertraulichkeit § 8          Zugriffsbeschränkung / Pseudonymisierung: <…>
VIII. Interessenkonflikt           [keiner / Abgabe an: …]
IX.   Dokumentation § 11           Ablage; Löschung nach 3 Jahren: <Datum>

Hinweis: Belastende Personalmaßnahmen während der Bearbeitung vermeiden (§ 36).
```

## Quellen

### Statute

- [§ 8 HinSchG](https://www.gesetze-im-internet.de/hinschg/__8.html) (Vertraulichkeitsgebot)
- [§ 13 HinSchG](https://www.gesetze-im-internet.de/hinschg/__13.html) (Aufgaben der internen Meldestelle)
- [§ 17 HinSchG](https://www.gesetze-im-internet.de/hinschg/__17.html) (Verfahren bei internen Meldungen)
- [§ 18 HinSchG](https://www.gesetze-im-internet.de/hinschg/__18.html) (Folgemaßnahmen)
- [§ 11 HinSchG](https://www.gesetze-im-internet.de/hinschg/__11.html) (Dokumentation)
- [§§ 2, 9, 36 HinSchG](https://www.gesetze-im-internet.de/hinschg/) (Anwendungsbereich, Ausnahmen, Repressalien)
- [Richtlinie (EU) 2019/1937](https://eur-lex.europa.eu/eli/dir/2019/1937/oj) (EU-Whistleblower-Richtlinie)

### Sekundärliteratur

- Reufels, Hinweisgeberschutz, 1. Aufl. 2024
- Schmidt-Husson, HinSchG-Praxiskommentar, 2. Aufl. 2024
- BeckOK HinSchG (Online)
