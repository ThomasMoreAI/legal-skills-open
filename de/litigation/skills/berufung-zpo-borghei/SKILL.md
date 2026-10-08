---
name: berufung-zpo-borghei
title: /prozessrecht:berufung-zpo
description: Berufung im Zivilprozess nach §§ 511 ff. ZPO. Statthaftigkeit und Berufungssumme — Beschwer über 600 EUR oder Zulassung (§ 511 ZPO), Berufungsgründe Rechtsverletzung oder fehlerhafte Tatsachen (§ 513 ZPO), einmonatige Berufungsfrist (§ 517 ZPO), Berufungsbegründung binnen zwei Monaten (§ 520 ZPO). Use when ein erstinstanzliches Zivilurteil mit der Berufung angegriffen oder die Erfolgsaussicht einer Berufung geprüft wird.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/prozessrecht/skills/berufung-zpo
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: litigation
language: de
---

# /prozessrecht:berufung-zpo

## Zweck

Die Berufung ist das ordentliche Rechtsmittel gegen erstinstanzliche Endurteile. Sie prüft das Urteil auf Rechtsfehler und auf neue oder zu Unrecht gewürdigte Tatsachen, ist aber an enge Zulässigkeitsschranken gebunden: Beschwer, Frist, Begründung. Der Skill prüft die Statthaftigkeit, berechnet die Fristen und strukturiert die Berufungsbegründung. Eine versäumte Frist oder eine unzureichende Begründung führt zur Verwerfung der Berufung als unzulässig — ohne jede Sachprüfung.

## Eingaben

- Erstinstanzliches Urteil (Gericht, Datum, Tenor, Beschwer der Partei)
- Höhe der Beschwer (Wert des Unterliegens) oder Zulassung der Berufung im Urteil
- Zeitpunkt der Zustellung des vollständigen Urteils (für die Fristen)
- Gerügte Fehler: Rechtsverletzung und/oder fehlerhafte Tatsachenfeststellung
- Neue Angriffs- und Verteidigungsmittel (Zulassung nach § 531 ZPO?)
- Berufungsantrag (Umfang der Anfechtung)

## Sub-Agent-Architektur

Der Skill arbeitet mit drei gedanklichen Einheiten. Eine **Statthaftigkeits-Einheit** prüft, ob die Berufung nach § 511 ZPO eröffnet ist — Beschwer über 600 EUR oder ausdrückliche Zulassung durch das Erstgericht. Eine **Frist-Einheit** berechnet die einmonatige Berufungsfrist und die zweimonatige Begründungsfrist jeweils ab Zustellung des vollständigen Urteils und prüft die Wahrung der Notfristen. Eine **Begründungs-Einheit** ordnet die Rügen den Berufungsgründen des § 513 ZPO zu (Rechtsverletzung oder nach § 529 ZPO zugrunde zu legende Tatsachen) und formuliert die nach § 520 Abs. 3 ZPO erforderlichen bestimmten Berufungsanträge und Gründe. Die Einheiten arbeiten nacheinander.

## Ablauf

### 1. Statthaftigkeit und Berufungssumme ([§ 511 ZPO](https://www.gesetze-im-internet.de/zpo/__511.html))

- Die Berufung ist statthaft gegen die im ersten Rechtszug erlassenen Endurteile (§ 511 Abs. 1 ZPO).
- Zusätzlich erforderlich (§ 511 Abs. 2 ZPO):
  - Wert des Beschwerdegegenstands **über 600 EUR** (§ 511 Abs. 2 Nr. 1 ZPO), **oder**
  - **Zulassung** der Berufung durch das Gericht des ersten Rechtszugs (§ 511 Abs. 2 Nr. 2, Abs. 4 ZPO).
- Maßgeblich ist die **Beschwer** der Partei, also der Wert ihres Unterliegens.

### 2. Berufungsgründe ([§ 513 ZPO](https://www.gesetze-im-internet.de/zpo/__513.html))

- Die Berufung kann nur darauf gestützt werden, dass die Entscheidung auf einer **Rechtsverletzung** (§ 546 ZPO) beruht **oder** die nach § 529 ZPO zugrunde zu legenden **Tatsachen** eine andere Entscheidung rechtfertigen (§ 513 Abs. 1 ZPO).
- Die örtliche Zuständigkeit des Erstgerichts kann grundsätzlich nicht gerügt werden (§ 513 Abs. 2 ZPO).

### 3. Berufungsfrist ([§ 517 ZPO](https://www.gesetze-im-internet.de/zpo/__517.html))

- Die Berufungsfrist beträgt **einen Monat**; sie ist eine **Notfrist** und beginnt mit der **Zustellung des vollständigen Urteils**, spätestens fünf Monate nach Verkündung (§ 517 ZPO).
- Einlegung durch Berufungsschrift beim **Berufungsgericht** (§ 519 ZPO).

### 4. Berufungsbegründung ([§ 520 ZPO](https://www.gesetze-im-internet.de/zpo/__520.html))

- Die Begründungsfrist beträgt **zwei Monate** ab Zustellung des vollständigen Urteils (§ 520 Abs. 2 ZPO), verlängerbar.
- Die Begründung muss enthalten (§ 520 Abs. 3 ZPO): den **bestimmten Berufungsantrag**, die Bezeichnung der Umstände, aus denen sich die Rechtsverletzung ergibt, und die Bezeichnung konkreter Anhaltspunkte für Zweifel an den Tatsachenfeststellungen.

## Risiken

- **Berufungssumme nicht erreicht** — bei Beschwer bis 600 EUR ist die Berufung ohne Zulassung nach § 511 ZPO unstatthaft.
- **Berufungsfrist versäumt** — die einmonatige Notfrist (§ 517 ZPO) läuft ab Zustellung; danach wird das Urteil rechtskräftig.
- **Begründung unzureichend** — fehlt der bestimmte Berufungsantrag oder die konkrete Auseinandersetzung mit dem Urteil (§ 520 Abs. 3 ZPO), wird die Berufung verworfen.
- **Neuer Vortrag präkludiert** — neue Angriffs- und Verteidigungsmittel sind nur unter den engen Voraussetzungen des § 531 ZPO zuzulassen.

## Ausgabeformat

```
BERUFUNG — <Mandat> — <Datum>

An das <Berufungsgericht>

Angefochtenes Urteil: <Gericht, Datum, Az.>
Zustellung des vollständigen Urteils am: <Datum>
Beschwer der Partei: <EUR>

I.   Statthaftigkeit (§ 511 ZPO)
     [ ] Beschwer über 600 EUR   [ ] Zulassung durch Erstgericht

II.  Fristen
     Berufungsfrist (ein Monat, Notfrist, § 517 ZPO): bis <Datum>
     Begründungsfrist (zwei Monate, § 520 Abs. 2 ZPO): bis <Datum>

III. Berufungsantrag (§ 520 Abs. 3 ZPO)
     <bestimmter Antrag, Umfang der Anfechtung>

IV.  Berufungsgründe (§ 513 ZPO)
     1. Rechtsverletzung: <Norm, fehlerhafte Anwendung>
     2. Tatsachen (§ 529 ZPO): <konkrete Anhaltspunkte für Zweifel>

V.   Neuer Vortrag (§ 531 ZPO)
     <Zulassungsgrund, falls einschlägig>

<Datum>, <Unterschrift Rechtsanwalt>
```

## Quellen

### Statute

- [§ 511 ZPO](https://www.gesetze-im-internet.de/zpo/__511.html), [§ 513 ZPO](https://www.gesetze-im-internet.de/zpo/__513.html), [§ 517 ZPO](https://www.gesetze-im-internet.de/zpo/__517.html), [§ 520 ZPO](https://www.gesetze-im-internet.de/zpo/__520.html)
- [§ 519 ZPO](https://www.gesetze-im-internet.de/zpo/__519.html), [§ 529 ZPO](https://www.gesetze-im-internet.de/zpo/__529.html), [§ 531 ZPO](https://www.gesetze-im-internet.de/zpo/__531.html)

### Kommentare

- Heßler, in: Zöller, ZPO, 36. Aufl. 2025, § 511 Rn. 1 ff.
- Ball, in: Musielak / Voit, ZPO, 22. Aufl. 2025, § 520 Rn. 1 ff.

### Rechtsprechung

- BGH, Beschl. v. 23.10.2012 – XI ZB 25/11 (Anforderungen an die Berufungsbegründung) `[unverifiziert – prüfen]`
