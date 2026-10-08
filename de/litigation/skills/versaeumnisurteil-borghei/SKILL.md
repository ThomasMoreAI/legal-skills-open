---
name: versaeumnisurteil-borghei
title: /prozessrecht:versaeumnisurteil
description: Versäumnisurteil und Einspruch im Zivilprozess nach §§ 330 ff. ZPO. VU gegen Kläger (§ 330 ZPO) und Beklagten (§ 331 ZPO), Schlüssigkeitsprüfung, Einspruch (§ 338 ZPO), zweiwöchige Einspruchsfrist als Notfrist (§ 339 ZPO), Form des Einspruchs (§ 340 ZPO), zweites Versäumnisurteil. Use when bei Säumnis in der mündlichen Verhandlung ein Versäumnisurteil beantragt, abgewehrt oder per Einspruch angegriffen wird.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/prozessrecht/skills/versaeumnisurteil
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: litigation
language: de
---

# /prozessrecht:versaeumnisurteil

## Zweck

Erscheint eine Partei in der mündlichen Verhandlung nicht oder verhandelt sie nicht, kann gegen sie ein Versäumnisurteil ergehen. Der Skill prüft die Voraussetzungen für ein Versäumnisurteil gegen Kläger oder Beklagten, die Schlüssigkeit des Klägervortrags und die fristgerechte Einlegung des Einspruchs. Fehler — vor allem das Versäumen der zweiwöchigen Notfrist — führen zur Rechtskraft des Versäumnisurteils und zum endgültigen Prozessverlust ohne Sachprüfung.

## Eingaben

- Verfahrensstand (welcher Termin, welche Partei säumig)
- Welche Partei ist säumig: Kläger oder Beklagter
- Wurde ordnungsgemäß und rechtzeitig geladen (Ladungsfrist, § 274 ZPO)
- Klägervortrag und dessen Schlüssigkeit (bei VU gegen den Beklagten)
- Zeitpunkt der Zustellung des Versäumnisurteils (für die Fristberechnung)
- Liegt bereits ein erstes Versäumnisurteil vor (Frage des zweiten VU)
- Entschuldigungsgründe für die Säumnis

## Sub-Agent-Architektur

Der Skill arbeitet mit drei gedanklichen Prüfeinheiten. Eine **Säumnis-Einheit** stellt fest, welche Partei säumig ist und ob die formellen Voraussetzungen (ordnungsgemäße Ladung, kein Vertagungsgrund, keine Entschuldigung) für ein Versäumnisurteil vorliegen. Eine **Schlüssigkeits-Einheit** prüft bei Säumnis des Beklagten, ob der als zugestanden geltende Klägervortrag den Antrag trägt — denn ein unschlüssiger Vortrag führt trotz Säumnis zur Klageabweisung (unechtes Versäumnisurteil). Eine **Rechtsbehelfs-Einheit** berechnet die zweiwöchige Einspruchsfrist als Notfrist und prüft Form und Begründung des Einspruchs. Die Einheiten arbeiten nacheinander; ihre Ergebnisse fließen in den Ausgabeblock.

## Ablauf

### 1. Versäumnisurteil gegen den Kläger ([§ 330 ZPO](https://www.gesetze-im-internet.de/zpo/__330.html))

- Erscheint der Kläger im Termin nicht, ergeht auf Antrag des Beklagten ein **klageabweisendes Versäumnisurteil**.
- Es findet **keine Schlüssigkeitsprüfung** statt; die Klage wird allein wegen der Säumnis abgewiesen.

### 2. Versäumnisurteil gegen den Beklagten ([§ 331 ZPO](https://www.gesetze-im-internet.de/zpo/__331.html))

- Erscheint der Beklagte nicht, gilt das tatsächliche mündliche Vorbringen des Klägers als **zugestanden** (§ 331 Abs. 1 ZPO).
- **Schlüssigkeitsprüfung**: Nur wenn der zugestanden geltende Vortrag den Klageantrag rechtfertigt, ergeht ein stattgebendes Versäumnisurteil (§ 331 Abs. 2 ZPO).
- Trägt der Vortrag den Antrag nicht, wird die Klage durch **unechtes Versäumnisurteil** (streitiges Urteil) abgewiesen.

### 3. Einspruch ([§ 338 ZPO](https://www.gesetze-im-internet.de/zpo/__338.html))

- Gegen das Versäumnisurteil ist der **Einspruch** statthaft.
- Zulässiger Einspruch versetzt den Prozess in die Lage vor der Säumnis zurück (§ 342 ZPO).

### 4. Einspruchsfrist ([§ 339 ZPO](https://www.gesetze-im-internet.de/zpo/__339.html))

- Die Einspruchsfrist beträgt **zwei Wochen** und ist eine **Notfrist** (§ 339 Abs. 1 ZPO).
- Sie beginnt mit der **Zustellung** des Versäumnisurteils.
- Versäumte Notfrist: nur Wiedereinsetzung in den vorigen Stand (§§ 233 ff. ZPO) hilft.

### 5. Form und Inhalt des Einspruchs ([§ 340 ZPO](https://www.gesetze-im-internet.de/zpo/__340.html))

- Der Einspruch wird durch **Einspruchsschrift** beim Prozessgericht eingelegt (§ 340 Abs. 1 ZPO).
- Inhalt: Bezeichnung des angefochtenen Urteils und Erklärung, dass Einspruch eingelegt wird (§ 340 Abs. 2 ZPO).
- Angriffs- und Verteidigungsmittel sollen rechtzeitig vorgebracht werden (§ 340 Abs. 3 ZPO).

### 6. Zweites Versäumnisurteil (§ 345 ZPO)

- Bleibt die Partei auch im Einspruchstermin säumig, ergeht ein **zweites Versäumnisurteil**.
- Dagegen ist kein erneuter Einspruch möglich; die Berufung ist nur auf den Vorwurf gestützt, es habe kein Fall der Säumnis vorgelegen (§ 514 Abs. 2 ZPO).

## Risiken

- **Einspruchsfrist versäumt** — die zweiwöchige Notfrist (§ 339 ZPO) läuft ab Zustellung; danach wird das Versäumnisurteil rechtskräftig.
- **Schlüssigkeitsprüfung übersehen** — bei Säumnis des Beklagten kein automatischer Sieg; ein unschlüssiger Klägervortrag führt zum unechten Versäumnisurteil.
- **Zweites Versäumnisurteil** — erneute Säumnis im Einspruchstermin schneidet jeden weiteren Sachvortrag ab.
- **Formfehler beim Einspruch** — fehlende Bezeichnung des Urteils oder fehlende Unterschrift macht den Einspruch unzulässig.

## Ausgabeformat

```
VERSÄUMNISURTEIL / EINSPRUCH — <Mandat> — <Datum>

Verfahrensstand: <Termin, säumige Partei>

I.   Säumnis-Prüfung
     Säumige Partei: <Kläger / Beklagter>
     Ordnungsgemäße Ladung: <ja/nein, § 274 ZPO>
     Entschuldigung / Vertagungsgrund: <…>

II.  Art des Versäumnisurteils
     [ ] VU gegen Kläger — Klageabweisung (§ 330 ZPO)
     [ ] VU gegen Beklagten — Schlüssigkeitsprüfung (§ 331 ZPO)
         Schlüssig: <ja → stattgebendes VU / nein → unechtes VU>

III. Einspruch (§ 338 ZPO)
     Zustellung des VU am: <Datum>
     Einspruchsfrist (zwei Wochen, Notfrist, § 339 ZPO): bis <Datum>
     Form (§ 340 ZPO): Einspruchsschrift, Bezeichnung des Urteils

IV.  Risiko zweites Versäumnisurteil (§ 345 ZPO)
     <Hinweis auf Erscheinens- und Verhandlungspflicht im Einspruchstermin>

Ergebnis / Empfehlung: <…>
<Datum>, <Unterschrift Rechtsanwalt>
```

## Quellen

### Statute

- [§ 330 ZPO](https://www.gesetze-im-internet.de/zpo/__330.html), [§ 331 ZPO](https://www.gesetze-im-internet.de/zpo/__331.html), [§ 338 ZPO](https://www.gesetze-im-internet.de/zpo/__338.html), [§ 339 ZPO](https://www.gesetze-im-internet.de/zpo/__339.html), [§ 340 ZPO](https://www.gesetze-im-internet.de/zpo/__340.html)
- [§ 342 ZPO](https://www.gesetze-im-internet.de/zpo/__342.html), [§ 345 ZPO](https://www.gesetze-im-internet.de/zpo/__345.html)

### Kommentare

- Prütting, in: Prütting / Gehrlein, ZPO, 17. Aufl. 2025, § 331 Rn. 1 ff.
- Herget, in: Zöller, ZPO, 36. Aufl. 2025, § 339 Rn. 1 ff.

### Rechtsprechung

- BGH, Urt. v. 06.10.2010 – VIII ZR 271/09 (Schlüssigkeit beim VU) `[unverifiziert – prüfen]`
