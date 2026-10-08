---
name: durchsuchung-beschlagnahme-borghei
title: /strafrecht:durchsuchung-beschlagnahme
description: Prüfung von Durchsuchung und Beschlagnahme – Durchsuchung beim Beschuldigten § 102 StPO und bei Dritten § 103 StPO, Richtervorbehalt und Gefahr im Verzug § 105 StPO, Sicherstellung/Beschlagnahme § 94 StPO und Verfahren § 98 StPO, Beschlagnahmeverbote § 97 StPO. Use when eine Durchsuchungs- oder Beschlagnahmemaßnahme auf Rechtmäßigkeit und Verwertbarkeit zu prüfen ist.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/strafrecht/skills/durchsuchung-beschlagnahme
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: criminal
language: de
---

# /strafrecht:durchsuchung-beschlagnahme

## Zweck

Durchsuchung und Beschlagnahme sind grundrechtsintensive Zwangsmaßnahmen (Art. 13 GG, Art. 14 GG). Dieser Skill prüft die **Rechtmäßigkeit** der Anordnung — insbesondere den **Richtervorbehalt** —, die **Verhältnismäßigkeit** und die Folgen für die **Verwertung** sichergestellter Beweismittel. Er unterscheidet die Durchsuchung beim Beschuldigten von der beim unverdächtigen Dritten und prüft die Beschlagnahmeverbote.

## Eingaben

- Wer wurde durchsucht (Beschuldigter / Dritter)?
- Lag ein richterlicher Beschluss vor? Datum, Inhalt, Tatvorwurf
- Falls nein: Begründung für Gefahr im Verzug?
- Welche Gegenstände wurden sichergestellt / beschlagnahmt?
- Betroffen Berufsgeheimnisträger (Anwalt, Arzt, Geistlicher)?
- Wurde Widerspruch gegen die Beschlagnahme erklärt?

## Sub-Agent-Architektur

Der **Researcher** ordnet die Maßnahme den Ermächtigungsgrundlagen zu (§ 102 vs. § 103 StPO; § 94 StPO) und verifiziert jede Norm gegen gesetze-im-internet.de; Aktenzeichen werden nicht erfunden. Der **Drafter** formuliert den Antrag auf gerichtliche Entscheidung (§ 98 Abs. 2 StPO) bzw. die Beschwerde und arbeitet Richtervorbehalt, Verhältnismäßigkeit und Beschlagnahmeverbote heraus. Der **Reviewer** prüft gegenläufig, ob die Anordnungskompetenz gewahrt war, ob „Gefahr im Verzug" tatsächlich vorlag und ob ein Beweisverwertungsverbot greift; unbestätigte Rechtsprechung kennzeichnet er mit `[unverifiziert – prüfen]`.

## Ablauf

### 1. Ermächtigungsgrundlage der Durchsuchung

- Beim **Beschuldigten**: [§ 102 StPO](https://www.gesetze-im-internet.de/stpo/__102.html) — Auffinden von Beweismitteln oder Ergreifung; Anfangsverdacht genügt.
- Bei **anderen Personen** (Dritten): [§ 103 StPO](https://www.gesetze-im-internet.de/stpo/__103.html) — nur bei konkreten Tatsachen, dass sich gesuchte Spur/Gegenstand dort befindet; engere Voraussetzungen.

### 2. Anordnung — Richtervorbehalt ([§ 105 StPO](https://www.gesetze-im-internet.de/stpo/__105.html))

- **Grundsatz: Richtervorbehalt.** Anordnung durch den Richter.
- **Ausnahme: Gefahr im Verzug** → Staatsanwaltschaft und ihre Ermittlungspersonen. Gefahr im Verzug muss mit **einzelfallbezogenen Tatsachen** dokumentiert sein; eine bloße Routineannahme genügt nicht (Verhältnismäßigkeit, effektiver Grundrechtsschutz).
- Inhaltliche Anforderungen an den Beschluss: Tatvorwurf, zu suchende Beweismittel, Begrenzung — ein zu unbestimmter Beschluss ist rechtswidrig.

### 3. Beschlagnahme / Sicherstellung ([§ 94 StPO](https://www.gesetze-im-internet.de/stpo/__94.html), [§ 98 StPO](https://www.gesetze-im-internet.de/stpo/__98.html))

- Sicherstellung formlos; Beschlagnahme bei Gewahrsamsbruch (§ 94 StPO).
- **Richtervorbehalt** auch hier: Beschlagnahme nur durch das Gericht, bei Gefahr im Verzug durch StA / Ermittlungspersonen (§ 98 Abs. 1 StPO).
- Bei Anordnung ohne richterliche Bestätigung: binnen drei Tagen gerichtliche Bestätigung beantragen (§ 98 Abs. 2 StPO). Der Betroffene kann jederzeit die **gerichtliche Entscheidung** nach § 98 Abs. 2 S. 2 StPO beantragen.

### 4. Beschlagnahmeverbote ([§ 97 StPO](https://www.gesetze-im-internet.de/stpo/__97.html))

- Schriftverkehr zwischen Beschuldigtem und **Berufsgeheimnisträgern** (§ 53 StPO) ist beschlagnahmefrei.
- Aufzeichnungen, Mitteilungen und sonstige Gegenstände, auf die sich das Zeugnisverweigerungsrecht erstreckt.
- Reichweite und Ausnahmen (z. B. Tatbeteiligung des Geheimnisträgers) prüfen.

### 5. Verhältnismäßigkeit & Verwertung

- **Verhältnismäßigkeit**: Eignung, Erforderlichkeit, Angemessenheit; Zufallsfunde nach § 108 StPO gesondert prüfen.
- **Verwertung**: Bei schwerwiegendem, bewusstem Verstoß gegen den Richtervorbehalt oder bei Verletzung eines Beschlagnahmeverbots kommt ein **Beweisverwertungsverbot** in Betracht (Abwägungslehre; gefestigte Rechtsprechung nur mit Fundstelle zitieren, sonst `[unverifiziert – prüfen]`).

## Risiken

- **Gefahr im Verzug** zu Unrecht angenommen → Anordnung rechtswidrig, mögliches Beweisverwertungsverbot.
- **Unbestimmter Durchsuchungsbeschluss** (kein konkreter Tatvorwurf, keine Begrenzung) → rechtswidrig.
- **Beschlagnahmeverbot** nach § 97 StPO übersehen (Berufsgeheimnisträger) → unverwertbar.
- **Verhältnismäßigkeit** nicht dokumentiert; Zufallsfunde ohne § 108 StPO verwertet.
- Frist für den **Antrag auf gerichtliche Entscheidung** versäumt.

## Ausgabeformat

```
DURCHSUCHUNG / BESCHLAGNAHME — <Az.> — <Datum>
VERTRAULICH — STRAFVERTEIDIGUNG

I.    Maßnahme                        <Durchsuchung / Beschlagnahme>
      Betroffener:                    [Beschuldigter § 102 / Dritter § 103]
II.   Anordnung                       [§ 105 StPO]
      Richterlicher Beschluss:        [✅ / ❌]
      Gefahr im Verzug begründet:     [✅ / ⚠️ zweifelhaft]
III.  Beschlagnahme                   [§ 94 StPO / § 98 StPO]
      Gerichtliche Bestätigung:       [✅ / offen]
IV.   Beschlagnahmeverbote            [§ 97 StPO]
      Berufsgeheimnisträger:          [ja / nein]
V.    Verhältnismäßigkeit / Verwertung
      Verwertungsverbot:              [🟢 nein / 🔴 prüfen]

Empfehlung: <…>
Nächster Schritt: <Antrag § 98 Abs. 2 StPO / Beschwerde>
```

## Quellen

- [§ 102 StPO](https://www.gesetze-im-internet.de/stpo/__102.html), [§ 103 StPO](https://www.gesetze-im-internet.de/stpo/__103.html), [§ 105 StPO](https://www.gesetze-im-internet.de/stpo/__105.html)
- [§ 94 StPO](https://www.gesetze-im-internet.de/stpo/__94.html), [§ 97 StPO](https://www.gesetze-im-internet.de/stpo/__97.html), [§ 98 StPO](https://www.gesetze-im-internet.de/stpo/__98.html), [§ 108 StPO](https://www.gesetze-im-internet.de/stpo/__108.html)
- Meyer-Goßner / Schmitt, StPO, 67. Aufl. 2024, § 105 Rn. 1 ff.
- Rechtsprechung zu Gefahr im Verzug / Verwertungsverbot: `[unverifiziert – prüfen]`
