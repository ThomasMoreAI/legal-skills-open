---
name: untersuchungshaft-borghei
title: /strafrecht:untersuchungshaft
description: Prüfung der Untersuchungshaft – dringender Tatverdacht und Haftgründe § 112 StPO (Flucht, Fluchtgefahr, Verdunkelungsgefahr), Wiederholungsgefahr § 112a StPO, Aussetzung des Vollzugs § 116 StPO, Sechs-Monats-Haftprüfung §§ 121, 122 StPO. Use when ein Haftbefehl auf Rechtmäßigkeit, Verhältnismäßigkeit und Außervollzugsetzung zu prüfen ist.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/strafrecht/skills/untersuchungshaft
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: criminal
language: de
---

# /strafrecht:untersuchungshaft

## Zweck

Untersuchungshaft ist der schwerste Eingriff im Ermittlungsverfahren (Art. 2 Abs. 2, Art. 104 GG; Unschuldsvermutung). Dieser Skill prüft den Haftbefehl auf **dringenden Tatverdacht**, das Vorliegen eines **Haftgrundes**, die **Verhältnismäßigkeit** und die Möglichkeit der **Außervollzugsetzung** sowie die Fristen der besonderen Haftprüfung nach sechs Monaten.

## Eingaben

- Tatvorwurf, einschlägige Norm, Straferwartung
- Datum des Haftbefehls / Beginn der Untersuchungshaft
- Im Haftbefehl genannter Haftgrund
- Persönliche Verhältnisse (Wohnsitz, soziale Bindungen, Arbeit, Pass)
- Frühere Verstöße / einschlägige Vorstrafen
- Bereits gestellte Haftprüfungs- oder Beschwerdeanträge?

## Sub-Agent-Architektur

Der **Researcher** ordnet den im Haftbefehl genannten Haftgrund den Tatbeständen des § 112 bzw. § 112a StPO zu und verifiziert jede Norm gegen gesetze-im-internet.de; er erfindet keine Aktenzeichen. Der **Drafter** formuliert den Haftprüfungs- oder Haftbeschwerdeantrag und arbeitet Verhältnismäßigkeit sowie mildere Mittel nach § 116 StPO heraus. Der **Reviewer** prüft gegenläufig, ob der dringende Tatverdacht trägt, ob die Fluchtgefahr substantiiert ist und ob die Sechs-Monats-Frist läuft; unbestätigte Rechtsprechung kennzeichnet er mit `[unverifiziert – prüfen]`.

## Ablauf

### 1. Dringender Tatverdacht ([§ 112 StPO](https://www.gesetze-im-internet.de/stpo/__112.html))

**Hohe Wahrscheinlichkeit**, dass der Beschuldigte Täter oder Teilnehmer ist (mehr als hinreichender Tatverdacht). Beweislage konkret prüfen — trägt sie den dringenden Tatverdacht zum jeweiligen Verfahrensstand?

### 2. Haftgrund (§ 112 Abs. 2 StPO)

- **Flucht**: Der Beschuldigte ist flüchtig oder hält sich verborgen (Nr. 1).
- **Fluchtgefahr**: Bei Würdigung der Umstände droht das Entziehen vom Verfahren (Nr. 2) — Straferwartung allein genügt nicht; soziale Bindungen, Wohnsitz, Familie gegenrechnen.
- **Verdunkelungsgefahr**: Gefahr, dass Beweismittel vernichtet/verändert oder Zeugen beeinflusst werden (Nr. 3).
- **Schwerstkriminalität** (§ 112 Abs. 3 StPO) bei bestimmten Katalogtaten.

### 3. Wiederholungsgefahr ([§ 112a StPO](https://www.gesetze-im-internet.de/stpo/__112a.html))

Eigenständiger Haftgrund der **Wiederholungsgefahr** bei bestimmten Katalogtaten und der Gefahr weiterer erheblicher Straftaten gleicher Art — **subsidiär** gegenüber § 112 StPO.

### 4. Verhältnismäßigkeit

Untersuchungshaft darf nicht außer Verhältnis zur Bedeutung der Sache und zur erwartenden Strafe stehen (§ 112 Abs. 1 S. 2 StPO). **Verhältnismäßigkeit** und Beschleunigungsgrundsatz in Haftsachen sind durchgehend zu prüfen.

### 5. Aussetzung des Vollzugs ([§ 116 StPO](https://www.gesetze-im-internet.de/stpo/__116.html))

**Außervollzugsetzung** gegen mildere Mittel, z. B.:

- Meldeauflagen, Aufenthaltsbeschränkung
- Sicherheitsleistung (Kaution)
- Passabgabe, Kontaktverbote

Greift bei Fluchtgefahr und (eingeschränkt) Verdunkelungsgefahr, wenn der Zweck der Haft auch milder erreicht wird.

### 6. Sechs-Monats-Haftprüfung ([§ 121 StPO](https://www.gesetze-im-internet.de/stpo/__121.html), [§ 122 StPO](https://www.gesetze-im-internet.de/stpo/__122.html))

- Vollzug über **sechs Monate** nur, wenn besondere Schwierigkeit/Umfang der Ermittlungen oder ein anderer wichtiger Grund das Urteil noch nicht zugelassen haben (§ 121 StPO).
- Entscheidung trifft das **Oberlandesgericht** im besonderen Haftprüfungsverfahren (§ 122 StPO).
- Beschleunigungsgrundsatz: Verzögerungen der Justiz gehen zulasten der Fortdauer.

## Risiken

- **Dringender Tatverdacht** überschätzt — Beweislage trägt die Haft nicht.
- **Fluchtgefahr** allein aus Straferwartung abgeleitet, soziale Bindungen ignoriert.
- **Verhältnismäßigkeit** missachtet; mildere Mittel nach § 116 StPO nicht geprüft.
- **Sechs-Monats-Frist** und Beschleunigungsgrundsatz übersehen → Haft rechtswidrig.

## Ausgabeformat

```
UNTERSUCHUNGSHAFT — <Mandant-ID> — <Datum>
VERTRAULICH — STRAFVERTEIDIGUNG

I.    Dringender Tatverdacht          [§ 112 StPO]   [🟢 / 🟡 / 🔴]
II.   Haftgrund
      [ ] Flucht / Fluchtgefahr       [§ 112 StPO]
      [ ] Verdunkelungsgefahr         [§ 112 StPO]
      [ ] Wiederholungsgefahr         [§ 112a StPO]
III.  Verhältnismäßigkeit             [✅ / ⚠️]
IV.   Außervollzugsetzung             [§ 116 StPO]
      Mögliche Auflagen:              <Kaution / Meldeauflage / Passabgabe>
V.    Haftdauer
      Haft seit:                      <…>
      Sechs-Monats-Prüfung fällig:    <…>  [§§ 121, 122 StPO]

Empfehlung: <…>
Nächster Schritt: <Haftprüfung / Haftbeschwerde / Antrag § 116 StPO>
```

## Quellen

- [§ 112 StPO](https://www.gesetze-im-internet.de/stpo/__112.html), [§ 112a StPO](https://www.gesetze-im-internet.de/stpo/__112a.html), [§ 116 StPO](https://www.gesetze-im-internet.de/stpo/__116.html), [§ 121 StPO](https://www.gesetze-im-internet.de/stpo/__121.html), [§ 122 StPO](https://www.gesetze-im-internet.de/stpo/__122.html)
- Meyer-Goßner / Schmitt, StPO, 67. Aufl. 2024, § 112 Rn. 1 ff.
- Rechtsprechung zu Fluchtgefahr / Beschleunigungsgrundsatz: `[unverifiziert – prüfen]`
