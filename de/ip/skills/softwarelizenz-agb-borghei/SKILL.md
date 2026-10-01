---
name: softwarelizenz-agb-borghei
title: /it-recht:softwarelizenz-agb
description: 'Prüfung von Software-Lizenz- und Nutzungs-AGB: Einräumung von Nutzungsrechten (§ 31 UrhG), zustimmungsbedürftige Handlungen und Erschöpfungsgrundsatz bei Gebrauchtsoftware (§ 69c UrhG, UsedSoft), AGB-Inhaltskontrolle von Weitergabe- und Audit-Klauseln (§§ 305, 307 BGB). Use when Lizenzbedingungen für Software gestaltet oder auf Wirksamkeit geprüft werden.'
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/it-recht/skills/softwarelizenz-agb
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: ip
language: de
---

# /it-recht:softwarelizenz-agb

## Zweck

Software-Lizenzbedingungen verbinden Urheberrecht und AGB-Recht: Sie räumen Nutzungsrechte ein und beschränken sie zugleich durch vorformulierte Klauseln. Dieser Skill prüft die wirksame Einräumung der Nutzungsrechte, die Grenzen des Erschöpfungsgrundsatzes beim Weiterverkauf von Gebrauchtsoftware und die AGB-Festigkeit von Weitergabe-, Audit- und Bindungsklauseln.

## Eingaben

- Rolle (Lizenzgeber / Lizenznehmer)
- Lizenzmodell (Kauf/Dauerlizenz, Miete/Abo, Volumen-/Konzernlizenz)
- Vertriebsweg (Datenträger / Download)
- streitige Klauseln (Weitergabeverbot, Aufspaltungsverbot, Audit-/Nachlizenzierung)
- Sachverhalt (Erstverkauf in der EU mit Zustimmung des Rechtsinhabers?)

## Sub-Agent-Architektur

Drei Rollen arbeiten zusammen. Ein **Rechteeinräumungs-Agent** prüft zunächst nach § 31 UrhG, welche Nutzungsrechte in welchem Umfang (einfach/ausschließlich, räumlich/zeitlich/inhaltlich) wirksam eingeräumt wurden, denn nur der eingeräumte Umfang bindet. Ein **Erschöpfungs-Agent** beurteilt sodann nach § 69c UrhG und der UsedSoft-Rechtsprechung, ob das Verbreitungsrecht erschöpft und der Weiterverkauf zulässig ist. Ein **AGB-Agent** kontrolliert schließlich die einschränkenden Klauseln (Weitergabe-, Aufspaltungs-, Audit-Klausel) an §§ 305, 307 BGB. Übergeben werden nur Befunde; Grundlage bleibt der konkrete Lizenztext und der Erwerbsvorgang.

## Ablauf

### 1. Einräumung von Nutzungsrechten (§ 31 UrhG)

Nach § 31 UrhG kann der Urheber einfache oder ausschließliche Nutzungsrechte einräumen und sie räumlich, zeitlich und inhaltlich beschränken. Unklare Reichweite ist nach der Zweckübertragungslehre (§ 31 Abs. 5 UrhG) im Zweifel eng zugunsten des Urhebers auszulegen. Für Computerprogramme gelten ergänzend die §§ 69a ff. UrhG.

### 2. Erschöpfungsgrundsatz und Gebrauchtsoftware (§ 69c UrhG)

Nach § 69c Nr. 3 S. 2 UrhG erschöpft sich das Verbreitungsrecht an einer Programmkopie, die mit Zustimmung des Rechtsinhabers im Gebiet der EU im Wege der Veräußerung in Verkehr gebracht wurde. Der EuGH hat klargestellt, dass dies auch für per **Download** veräußerte Kopien gilt, wenn der Ersterwerb gegen Entgelt auf unbegrenzte Zeit erfolgt (EuGH, Urt. v. 03.07.2012 – C-128/11 — UsedSoft, [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=EuGH&Datum=2012-07-03&Aktenzeichen=C-128/11); nachfolgend BGH, Urt. v. 17.07.2013 – I ZR 129/08 — UsedSoft II, [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2013-07-17&Aktenzeichen=I%20ZR%20129/08)). Voraussetzung der zulässigen Weiterveräußerung ist, dass der Ersterwerber seine eigene Kopie unbrauchbar macht; eine Aufspaltung von Volumenlizenzen ist unzulässig.

### 3. AGB-Kontrolle von Weitergabe- und Audit-Klauseln (§§ 305, 307 BGB)

Vorformulierte Lizenzbedingungen sind AGB (§ 305 BGB). An § 307 BGB scheitern insbesondere:

- vollständige **Weitergabe**verbote, die eine kraft Erschöpfung zulässige Veräußerung untersagen — unwirksam, weil sie die gesetzliche Erschöpfung aushebeln;
- **Audit**-Klauseln, die dem Lizenzgeber unangemessen weite, jederzeitige Zutritts- und Einsichtsrechte einräumen — am Maßstab der Verhältnismäßigkeit und des Datenschutzes zu prüfen;
- automatische Nachlizenzierung zu Listenpreisen als pauschalierter Schadensersatz ohne Gegenbeweis (§ 309 Nr. 5 BGB).

## Risiken

- **Weitergabe**verbot trotz eingetretener Erschöpfung — Klausel unwirksam (§ 307 BGB); zugleich Kartell-/AGB-Risiko für den Lizenzgeber.
- **Audit**-Klausel zu weit (jederzeitiger Zutritt, Selbstbezichtigung, Kostenlast) — Verstoß gegen § 307 BGB und Datenschutz.
- **Erschöpfung** verkannt: Weiterverkauf zu Unrecht untersagt oder zu Unrecht angenommen, obwohl Erstverkauf außerhalb der EU oder als bloße Miete/Abo erfolgte.
- **Nutzungsrecht** über die Zweckübertragungslehre (§ 31 Abs. 5 UrhG) hinaus angenommen — eingeräumt ist nur, was der Vertragszweck erfordert.
- Aufspaltung einer Volumenlizenz beim Weiterverkauf — von der Erschöpfung nicht gedeckt, Urheberrechtsverletzung (§ 97 UrhG).

## Ausgabeformat

```
SOFTWARELIZENZ-AGB-PRÜFUNG — <Produkt/Lizenz> — <Datum>

I.   Nutzungsrechte (§ 31 UrhG)        [Umfang / Zweckübertragung — eng?]
II.  Lizenzmodell                      [Kauf/Dauer / Miete/Abo]
III. Erschöpfung (§ 69c UrhG)          [eingetreten? EU-Erstverkauf, Entgelt, unbefristet]
     Weiterverkauf zulässig:           [✓ / ❌ — Begründung, UsedSoft]
IV.  AGB-Kontrolle (§§ 305, 307 BGB)
     Weitergabeklausel:                [✓ / ❌ unwirksam]
     Audit-/Nachlizenzklausel:         [✓ / ⚠️ / ❌]

Empfehlung:                            <…>
```

## Quellen

- [§ 31 UrhG](https://www.gesetze-im-internet.de/urhg/__31.html), [§ 69c UrhG](https://www.gesetze-im-internet.de/urhg/__69c.html), [§ 69d UrhG](https://www.gesetze-im-internet.de/urhg/__69d.html), [§ 97 UrhG](https://www.gesetze-im-internet.de/urhg/__97.html)
- [§ 305 BGB](https://www.gesetze-im-internet.de/bgb/__305.html), [§ 307 BGB](https://www.gesetze-im-internet.de/bgb/__307.html), [§ 309 BGB](https://www.gesetze-im-internet.de/bgb/__309.html)
- EuGH, Urt. v. 03.07.2012 – C-128/11, NJW 2012, 2565 = GRUR 2012, 904 (UsedSoft), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=EuGH&Datum=2012-07-03&Aktenzeichen=C-128/11)
- BGH, Urt. v. 17.07.2013 – I ZR 129/08, GRUR 2014, 264 = NJW 2014, 777 (UsedSoft II), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2013-07-17&Aktenzeichen=I%20ZR%20129/08)
