---
name: beweislast-borghei
title: /prozessrecht:beweislast
description: Darlegungs- und Beweislast im Zivilprozess nach §§ 138, 286 ff. ZPO. Freie Beweiswürdigung (§ 286 ZPO), gerichtliches Geständnis (§ 288 ZPO), Beweisaufnahme über streitige Tatsachen (§ 355 ZPO), prozessuale Wahrheits- und Erklärungspflicht (§ 138 ZPO), Anscheinsbeweis und sekundäre Darlegungslast. Use when geklärt werden soll, welche Partei welche Tatsache beweisen muss und wie der Beweis geführt oder erschüttert wird.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/prozessrecht/skills/beweislast
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: litigation
language: de
---

# /prozessrecht:beweislast

## Zweck

Wer eine für sich günstige Tatsache nicht beweisen kann, verliert insoweit den Prozess — die Beweislast entscheidet den Rechtsstreit, wenn eine Tatsache streitig und unaufklärbar bleibt (non liquet). Der Skill verteilt die Darlegungs- und Beweislast, prüft die Erklärungspflicht der Gegenseite und ordnet Beweiserleichterungen (Anscheinsbeweis, sekundäre Darlegungslast) ein. Fehler bei der Beweislastverteilung führen dazu, dass eine Partei für eine Tatsache beweisbelastet bleibt, für die sie es gar nicht ist — oder umgekehrt.

## Eingaben

- Streitige und unstreitige Tatsachen (Abgleich der Schriftsätze)
- Anspruchsgrundlage und ihre Tatbestandsmerkmale (für die Grundregel der Beweislast)
- Einwendungen und Einreden der Gegenseite (rechtshindernd, rechtsvernichtend, rechtshemmend)
- Beweismittel je Tatsache (Urkunde, Zeuge, Sachverständiger, Augenschein, Parteivernehmung)
- Typischer Geschehensablauf (für den Anscheinsbeweis)
- Informationsasymmetrie (für die sekundäre Darlegungslast)

## Sub-Agent-Architektur

Der Skill arbeitet mit drei gedanklichen Einheiten. Eine **Verteilungs-Einheit** wendet die Grundregel an: Jede Partei trägt die Beweislast für die tatsächlichen Voraussetzungen der ihr günstigen Norm; der Anspruchsteller beweist die anspruchsbegründenden, der Gegner die rechtshindernden, -vernichtenden und -hemmenden Tatsachen. Eine **Erklärungs-Einheit** prüft die prozessuale Wahrheits- und Erklärungspflicht nach § 138 ZPO (Geständnisfiktion bei Nichtbestreiten, sekundäre Darlegungslast bei Informationsasymmetrie). Eine **Würdigungs-Einheit** ordnet die Beweisaufnahme (§ 355 ZPO) und die freie Beweiswürdigung (§ 286 ZPO) ein und prüft Beweiserleichterungen wie den Anscheinsbeweis. Die Einheiten arbeiten nacheinander.

## Ablauf

### 1. Grundregel der Beweislast

- **Jede Partei trägt die Beweislast** für die Tatbestandsmerkmale der ihr günstigen Norm (Rosenberg’sche Normentheorie).
- Anspruchsteller: anspruchsbegründende Tatsachen; Gegner: rechtshindernde / rechtsvernichtende / rechtshemmende Tatsachen (z. B. Erfüllung, Verjährung).

### 2. Erklärungs- und Wahrheitspflicht ([§ 138 ZPO](https://www.gesetze-im-internet.de/zpo/__138.html))

- Die Parteien haben sich **vollständig und der Wahrheit gemäß** zu erklären (§ 138 Abs. 1 ZPO).
- Tatsachen, die nicht ausdrücklich bestritten werden, gelten als **zugestanden** (§ 138 Abs. 3 ZPO).
- Aus § 138 Abs. 2 ZPO folgt die **sekundäre Darlegungslast**: Steht die darlegungsbelastete Partei außerhalb des Geschehens, während der Gegner die Umstände kennt, muss der Gegner substantiiert erwidern.

### 3. Gerichtliches Geständnis ([§ 288 ZPO](https://www.gesetze-im-internet.de/zpo/__288.html))

- Das **gerichtliche Geständnis** macht die zugestandene Tatsache beweisbedürftigkeitsfrei (§ 288 ZPO); sie ist der Entscheidung ohne Beweis zugrunde zu legen.
- Widerruf nur unter den engen Voraussetzungen des § 290 ZPO.

### 4. Beweisaufnahme ([§ 355 ZPO](https://www.gesetze-im-internet.de/zpo/__355.html))

- Über **streitige, entscheidungserhebliche** Tatsachen ist Beweis zu erheben (§ 355 ZPO, Grundsatz der Unmittelbarkeit).
- Strengbeweis durch die fünf Beweismittel: Augenschein, Zeugen, Sachverständige, Urkunden, Parteivernehmung.

### 5. Freie Beweiswürdigung ([§ 286 ZPO](https://www.gesetze-im-internet.de/zpo/__286.html))

- Das Gericht entscheidet **nach freier Überzeugung**, ob eine Tatsachenbehauptung für wahr zu erachten ist (§ 286 Abs. 1 ZPO).
- Erforderlich ist ein für das praktische Leben brauchbarer Grad an Gewissheit, der Zweifeln Schweigen gebietet (kein naturwissenschaftlicher Vollbeweis).

### 6. Beweiserleichterungen

- **Anscheinsbeweis**: Bei typischem Geschehensablauf schließt das Gericht von einem feststehenden Sachverhalt auf die Ursache/das Verschulden; der Gegner kann ihn durch ernsthafte Möglichkeit eines atypischen Verlaufs erschüttern.
- **Beweislastumkehr**: in Sonderkonstellationen (z. B. grober Behandlungsfehler, Produzentenhaftung).

## Risiken

- **Beweislast falsch verteilt** — wer für eine rechtsvernichtende Tatsache (Erfüllung) beweisbelastet ist, ist nicht der Anspruchsteller, sondern der Gegner.
- **Anscheinsbeweis verkannt** — bei typischem Geschehensablauf genügt der Vollbeweis nicht; der Anschein muss erschüttert werden.
- **Sekundäre Darlegungslast übersehen** — bei Informationsasymmetrie trifft den Gegner nach § 138 Abs. 2 ZPO eine substantiierte Erklärungspflicht.
- **Geständnis unterschätzt** — ein gerichtliches Geständnis (§ 288 ZPO) bindet und ist nur eingeschränkt widerruflich.

## Ausgabeformat

```
BEWEISLAST-ANALYSE — <Mandat> — <Datum>

Anspruchsgrundlage: <Norm>

I.   Tatsachen-Abgleich (§ 138 ZPO)
     Unstreitig: <…>
     Streitig:   <…>
     Nicht bestritten → zugestanden (§ 138 Abs. 3 ZPO): <…>

II.  Beweislastverteilung
     Anspruchsbegründend (Kläger): <Tatsachen>
     Rechtshindernd/-vernichtend/-hemmend (Beklagter): <Tatsachen>

III. Erklärungs-/Darlegungslast
     Sekundäre Darlegungslast (§ 138 Abs. 2 ZPO)? <…>
     Gerichtliches Geständnis (§ 288 ZPO)? <…>

IV.  Beweisaufnahme (§ 355 ZPO)
     Je streitige Tatsache: Beweismittel + Beweisführer

V.   Würdigung (§ 286 ZPO) / Beweiserleichterung
     Anscheinsbeweis: <typischer Geschehensablauf? Erschütterung?>

Ergebnis (non liquet → zu Lasten der beweisbelasteten Partei): <…>
<Datum>, <Unterschrift Rechtsanwalt>
```

## Quellen

### Statute

- [§ 138 ZPO](https://www.gesetze-im-internet.de/zpo/__138.html), [§ 286 ZPO](https://www.gesetze-im-internet.de/zpo/__286.html), [§ 288 ZPO](https://www.gesetze-im-internet.de/zpo/__288.html), [§ 355 ZPO](https://www.gesetze-im-internet.de/zpo/__355.html)
- [§ 290 ZPO](https://www.gesetze-im-internet.de/zpo/__290.html)

### Kommentare

- Prütting, in: Münchener Kommentar zur ZPO, 7. Aufl. 2025, § 286 Rn. 1 ff.
- Greger, in: Zöller, ZPO, 36. Aufl. 2025, § 138 Rn. 1 ff. (sekundäre Darlegungslast)

### Rechtsprechung

- BGH, Urt. v. 18.01.2018 – I ZR 100/16 (sekundäre Darlegungslast) `[unverifiziert – prüfen]`
- BGH, Urt. v. 19.03.2019 – VI ZR 33/18 (Anscheinsbeweis) `[unverifiziert – prüfen]`
