---
name: beweisverwertungsverbot-borghei
title: /strafrecht:beweisverwertungsverbot
description: Prüfung von Beweisverwertungsverboten im Strafprozess – verbotene Vernehmungsmethoden § 136a Abs. 3 StPO, körperliche Untersuchung und Blutprobe § 81a StPO, Belehrungspflicht § 136 StPO; Widerspruchslösung, unselbständige vs. selbständige Verwertungsverbote. Use when ein rechtswidrig erlangtes Beweismittel auf seine Verwertbarkeit in der Hauptverhandlung zu prüfen ist.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/strafrecht/skills/beweisverwertungsverbot
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: criminal
language: de
---

# /strafrecht:beweisverwertungsverbot

## Zweck

Nicht jeder Verfahrensfehler führt zum Beweisverwertungsverbot — aber wo eines greift, kann es ein Verfahren tragen oder zu Fall bringen. Dieser Skill prüft, ob ein Beweismittel rechtswidrig erlangt wurde (Beweiserhebungsfehler), ob daraus ein **Verwertungsverbot** folgt (unselbständig oder selbständig) und ob die **Widerspruchslösung** beachtet werden muss, damit das Verbot in der Revision durchgreift.

> Zero-Fabrication: BGH-/BVerfG-Entscheidungen werden hier nur generisch beschrieben oder mit `[unverifiziert – prüfen]` markiert. Erfinde **kein** Aktenzeichen und **keine** Fundstelle.

## Eingaben

- betroffenes Beweismittel (Geständnis, Aussage, Blutprobe, Durchsuchungsfund …)
- Art der Erlangung und behaupteter Fehler
- Belehrung erfolgt? (§ 136 StPO, § 163a StPO)
- richterliche Anordnung vorhanden / Gefahr im Verzug?
- Verfahrensstand (vor / in Hauptverhandlung), verteidigt durch RA?

## Sub-Agent-Architektur

Die Analyse läuft in drei Prosa-Schritten. Ein Erhebungs-Agent prüft, ob die Beweisgewinnung gegen eine konkrete Verfahrensnorm verstößt — Methodenverbot, fehlende Belehrung, fehlende Anordnung. Ein Verwertungs-Agent ordnet den Fehler ein: zwingendes selbständiges Verwertungsverbot, unselbständiges Verbot nach Abwägung (Schutzzweck der Norm, Schwere des Verstoßes, hypothetisch rechtmäßige Erlangung) oder kein Verbot. Ein Prozess-Agent sichert die Durchsetzung: Prüfung der Widerspruchsfrist und Formulierung des rechtzeitigen Widerspruchs bis zum Zeitpunkt nach § 257 StPO. Die Rollen sind gedankliche Arbeitsschritte, keine getrennten technischen Prozesse.

## Ablauf

### 1. Beweiserhebungsfehler identifizieren

| Fallgruppe | Norm | typischer Fehler |
|---|---|---|
| Vernehmungsmethode | [§ 136a StPO](https://www.gesetze-im-internet.de/stpo/__136a.html) | Täuschung, Drohung, Zwang, Ermüdung, Versprechen unzulässiger Vorteile |
| Belehrung | [§ 136 StPO](https://www.gesetze-im-internet.de/stpo/__136.html) | keine Belehrung über Schweigerecht / Verteidigerkonsultation |
| körperlicher Eingriff | [§ 81a StPO](https://www.gesetze-im-internet.de/stpo/__81a.html) | Blutprobe ohne (erforderliche) Anordnung, kein Arzt |

### 2. Verbotene Vernehmungsmethoden (§ 136a StPO)

§ 136a Abs. 1, 2 StPO verbietet die Beeinträchtigung der Willensentschließung durch Misshandlung, Ermüdung, körperlichen Eingriff, Verabreichung von Mitteln, Quälerei, Täuschung oder Hypnose sowie Drohung und Versprechen gesetzlich nicht vorgesehener Vorteile.

**§ 136a Abs. 3 S. 2 StPO ordnet ein absolutes Verwertungsverbot an:** So gewonnene Aussagen dürfen **auch mit Zustimmung des Beschuldigten nicht verwertet** werden. Es handelt sich um ein **selbständiges, zwingendes** Verwertungsverbot — keine Abwägung, kein Widerspruchserfordernis.

### 3. Belehrungsfehler (§ 136 StPO)

Unterbleibt die Belehrung über das Schweigerecht und das Recht auf Verteidigerkonsultation (§ 136 Abs. 1 StPO), ist die Aussage grundsätzlich unverwertbar. Dieses Verbot ist jedoch **unselbständig und disponibel**: Es greift in der Revision nur, wenn der verteidigte Angeklagte der Verwertung rechtzeitig **widerspricht** (Widerspruchslösung). Bei qualifizierter Belehrung über ein vorangegangenes Verfahrensgeschehen gelten Sonderregeln.

### 4. Körperliche Untersuchung / Blutprobe (§ 81a StPO)

Blutentnahme und sonstige körperliche Eingriffe sind nach § 81a StPO **ohne Einwilligung** zulässig, wenn von einem Arzt nach den Regeln der ärztlichen Kunst durchgeführt und kein Gesundheitsnachteil zu befürchten ist. Die Anordnung steht dem Richter zu; bei Gefahr im Verzug auch StA und ihren Ermittlungspersonen. Für bestimmte Verkehrsdelikte ist der **Richtervorbehalt entfallen**. Ein Verstoß führt nur nach **Abwägung** (Schutzzweck, Schwere, Willkür) zum Verwertungsverbot — nicht automatisch.

### 5. Selbständige vs. unselbständige Verwertungsverbote

- **Unselbständig:** knüpfen an einen Beweiserhebungsfehler an (z. B. § 136 StPO, § 81a StPO). Reichweite über Abwägung; meist Widerspruchslösung.
- **Selbständig:** bestehen unabhängig von der Erhebung, schützen einen verfassungsrechtlichen Kernbereich (z. B. § 136a Abs. 3 StPO, Kernbereich privater Lebensgestaltung). Zwingend, keine Abwägung.

### 6. Widerspruchslösung

Bei disponiblen (unselbständigen) Verboten muss der **verteidigte** Angeklagte der Verwertung **bis zu dem nach § 257 StPO bezeichneten Zeitpunkt** (nach Vernehmung/Verlesung) widersprechen. Unterbleibt der Widerspruch, ist der Verfahrensfehler in der Revision präkludiert. Beim absoluten Verbot des § 136a Abs. 3 StPO ist **kein** Widerspruch erforderlich.

## Quellen

### Statute

- [§ 136 StPO](https://www.gesetze-im-internet.de/stpo/__136.html), [§ 136a StPO](https://www.gesetze-im-internet.de/stpo/__136a.html), [§ 81a StPO](https://www.gesetze-im-internet.de/stpo/__81a.html)
- § 163a StPO (Vernehmung Beschuldigter im Ermittlungsverfahren), § 257 StPO (Erklärungsrecht), § 252 StPO (Verlesungsverbot)

### Kommentare

- Meyer-Goßner / Schmitt, StPO, 67. Aufl. 2024, § 136a Rn. 1 ff., Einl. Rn. 50 ff.
- Schuhr, in: MüKo-StPO, 2. Aufl. 2023, § 136a Rn. 1 ff.
- Beulke, Strafprozessrecht, 15. Aufl. 2023, Rn. 454 ff.

### Rechtsprechung

- BGH (Großer Senat), Grundsatzentscheidung zur Widerspruchslösung bei § 136 StPO — Aktenzeichen `[unverifiziert – prüfen]`
- BVerfG zur Reichweite des Richtervorbehalts bei § 81a StPO — Aktenzeichen `[unverifiziert – prüfen]`
- BGH zur Tragweite des § 136a Abs. 3 StPO — Aktenzeichen `[unverifiziert – prüfen]`

## Ausgabeformat

```
BEWEISVERWERTUNGSVERBOT — <Mandant-ID> — <Datum>
VERTRAULICH — STRAFVERTEIDIGUNG

I.    Beweismittel               <Aussage / Blutprobe / …>
II.   Erhebungsfehler            [§ 136a / § 136 / § 81a StPO]
III.  Verbotstyp
      selbständig/zwingend?       [✅ § 136a Abs. 3 / —]
      unselbständig (Abwägung)?   [✅ / —]
IV.   Abwägung (falls unselbständig)
      Schutzzweck:                <…>
      Schwere des Verstoßes:      [🔴 / 🟡 / 🟢]
V.    Durchsetzung
      Widerspruch erforderlich?   [ja → Frist § 257 StPO / nein]
      Widerspruch erhoben?        [✅ / ⚠️ Präklusion]

Ergebnis: [Verwertungsverbot (+) / (–)]
Nächster Schritt: <…>
```

## Risiken / typische Fehler

- **Widerspruch versäumt** — bei unselbständigem Verbot (§ 136 StPO, § 81a StPO) ist die Rüge in der Revision präkludiert. Frist nach § 257 StPO zwingend wahren.
- **§ 136a Abs. 3 StPO mit Abwägung verwechselt** — dort gilt ein **absolutes** Verwertungsverbot ohne Abwägung und ohne Widerspruch.
- **Fernwirkung überschätzt** — eine automatische „fruit of the poisonous tree"-Doktrin kennt das deutsche Recht nicht; Folgebeweise sind nur ausnahmsweise erfasst.
- **Aktenzeichen erfunden** — niemals eine BGH-Fundstelle behaupten, die nicht verifiziert ist; `[unverifiziert – prüfen]` setzen.
- **Hypothetisch rechtmäßige Erlangung** ignoriert — schwächt das Verwertungsverbot bei § 81a StPO.
