---
name: buergschaft-pruefung-borghei
title: /bankrecht:buergschaft-pruefung
description: Prüfung einer Bürgschaft § 765 BGB auf Wirksamkeit. Schriftform § 766 BGB, Akzessorietät § 767 BGB, Einrede der Vorausklage § 771 BGB, Sittenwidrigkeit bei krasser finanzieller Überforderung naher Angehöriger § 138 BGB. Use when eine Bürgschaftserklärung auf Form und Sittenwidrigkeit geprüft oder die Inanspruchnahme eines Bürgen verteidigt wird.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/bankrecht/skills/buergschaft-pruefung
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: finance
language: de
---

# /bankrecht:buergschaft-pruefung

## Zweck

Bürgschaften scheitern in der Praxis häufig an der Form oder an der Sittenwidrigkeit. Die ständige Rechtsprechung kassiert Bürgschaften naher Angehöriger, die den Bürgen krass finanziell überfordern und allein aus emotionaler Verbundenheit übernommen wurden. Dieser Skill prüft Wirksamkeit, Einreden und Reichweite der Bürgenhaftung und identifiziert Verteidigungslinien.

## Eingaben

- Bürgschaftsurkunde (Wortlaut, Datum, Unterschrift)
- Hauptforderung (Gläubiger, Hauptschuldner, Betrag, Rechtsgrund)
- Art der Bürgschaft (gewöhnlich, selbstschuldnerisch, Höchstbetrag, global)
- Beziehung Bürge–Hauptschuldner (Ehegatte, Kind, Geschäftspartner)
- Einkommens- und Vermögensverhältnisse des Bürgen bei Übernahme
- Mitwirkung des Gläubigers/der Bank an der Übernahme

## Sub-Agent-Architektur

Der **Researcher** bestätigt §§ 765 ff. BGB über gesetze-im-internet.de und recherchiert die BGH-Rechtsprechung zur Sittenwidrigkeit krasser Überforderung; nicht gesicherte Aktenzeichen werden als `[unverifiziert – prüfen]` markiert. Der **Drafter** subsumiert Form, Akzessorietät und Einreden und prüft die Sittenwidrigkeitsindizien (krasse Überforderung, emotionale Verbundenheit, Gläubigerverhalten). Der **Reviewer** kontrolliert die Akzessorietätsfolgen, die Vollständigkeit der Einredenprüfung und stellt sicher, dass keine Tatsachen oder Entscheidungen erfunden wurden.

## Ablauf

### 1. Zustandekommen (§ 765 BGB)

[§ 765 BGB](https://www.gesetze-im-internet.de/bgb/__765.html): Durch den Bürgschaftsvertrag verpflichtet sich der Bürge gegenüber dem Gläubiger, für die Erfüllung der Verbindlichkeit eines Dritten einzustehen. Voraussetzung sind eine bestimmte oder bestimmbare Hauptforderung und ein wirksamer Bürgschaftsvertrag.

### 2. Schriftform (§ 766 BGB)

[§ 766 BGB](https://www.gesetze-im-internet.de/bgb/__766.html): Die Erteilung der Bürgschaftserklärung bedarf der **Schriftform**; elektronische Form ist ausgeschlossen. Prüfen:

- Eigenhändige Unterschrift des Bürgen auf der Urkunde
- Hinreichende Bezeichnung von Gläubiger, Hauptschuldner und verbürgter Forderung
- Bei Kaufleuten: Formfreiheit nach § 350 HGB
- Heilung durch Erfüllung (§ 766 S. 3 BGB)

### 3. Akzessorietät (§ 767 BGB)

[§ 767 BGB](https://www.gesetze-im-internet.de/bgb/__767.html): Die Bürgschaftsschuld richtet sich nach dem jeweiligen Bestand der Hauptforderung. Folgen:

- Erlischt/mindert sich die Hauptforderung, sinkt die Bürgenhaftung
- Keine Erweiterung durch nachträgliches Verhalten des Hauptschuldners (§ 767 Abs. 1 S. 3 BGB)
- Der Bürge kann Einreden des Hauptschuldners geltend machen (§ 768 BGB)

### 4. Einrede der Vorausklage (§ 771 BGB)

[§ 771 BGB](https://www.gesetze-im-internet.de/bgb/__771.html): Der gewöhnliche Bürge kann die Befriedigung verweigern, solange der Gläubiger nicht erfolglos gegen den Hauptschuldner vollstreckt hat. Bei **selbstschuldnerischer** Bürgschaft (§ 773 Abs. 1 Nr. 1 BGB) entfällt diese Einrede — häufiger Bankstandard.

### 5. Sittenwidrigkeit (§ 138 BGB)

[§ 138 BGB](https://www.gesetze-im-internet.de/bgb/__138.html): Eine Bürgschaft naher Angehöriger ist nichtig, wenn

- der Bürge durch die verbürgte Summe **krass finanziell überfordert** ist (Indiz: pfändbares Einkommen deckt nicht einmal die laufenden Zinsen) **und**
- die Bürgschaft allein aus emotionaler Verbundenheit übernommen wurde (widerlegliche Vermutung verwerflicher Gesinnung des Gläubigers).

Korrektiv: eigenes wirtschaftliches Interesse des Bürgen oder Vermögensverschiebung kann die Vermutung entkräften.

## Risiken / typische Fehler

- **Schriftform übersehen** — Formmangel nach § 766 BGB macht die Bürgschaft nichtig, sofern keine Heilung durch Erfüllung vorliegt.
- **Sittenwidrigkeit nicht geprüft** — bei naher Angehörigen-Bürgschaft mit krasser Überforderung ist § 138 BGB die wichtigste Verteidigung; das Einkommen bei Übernahme muss konkret ermittelt werden.
- **Akzessorietät verkannt** — Einwendungen gegen die Hauptforderung werden nicht in die Bürgenhaftung übertragen.
- **Einrede der Vorausklage übersehen** — bei gewöhnlicher Bürgschaft kann der Bürge nach § 771 BGB auf vorrangige Vollstreckung verweisen; selbstschuldnerische Klausel prüfen.
- **Globalbürgschaft/Übersicherung ignoriert** — überraschende Erweiterung auf künftige Forderungen kann nach §§ 305c, 307 BGB unwirksam sein; ungesicherte Aktenzeichen als `[unverifiziert – prüfen]` kennzeichnen.

## Quellen

- [§ 765 BGB](https://www.gesetze-im-internet.de/bgb/__765.html), [§ 766 BGB](https://www.gesetze-im-internet.de/bgb/__766.html), [§ 767 BGB](https://www.gesetze-im-internet.de/bgb/__767.html)
- [§ 768 BGB](https://www.gesetze-im-internet.de/bgb/__768.html), [§ 771 BGB](https://www.gesetze-im-internet.de/bgb/__771.html), [§ 773 BGB](https://www.gesetze-im-internet.de/bgb/__773.html)
- [§ 138 BGB](https://www.gesetze-im-internet.de/bgb/__138.html), [§ 350 HGB](https://www.gesetze-im-internet.de/hgb/__350.html)
- BGH, Urt. v. 25.01.2005 – XI ZR 325/03 (krasse Überforderung) `[unverifiziert – prüfen]`
- BVerfG, Beschl. v. 19.10.1993 – 1 BvR 567/89 (Bürgschaft naher Angehöriger) `[unverifiziert – prüfen]`

## Ausgabeformat

```
BÜRGSCHAFTS-PRÜFUNG — <Mandat> — <Datum>

I.    Zustandekommen § 765 BGB           [wirksam / 🔴]
II.   Schriftform § 766 BGB              [✓ / 🔴 Formmangel]
III.  Akzessorietät § 767 BGB
      Bestand Hauptforderung:            <…>
      Einwendungen § 768 BGB:            <…>
IV.   Einrede der Vorausklage § 771 BGB  [besteht / entfallen (selbstschuldnerisch)]
V.    Sittenwidrigkeit § 138 BGB
      Krasse Überforderung:              [✓ / nein]
      Emotionale Verbundenheit:          [✓ / nein]
      Ergebnis:                          [nichtig / wirksam]

Empfehlung / Verteidigungslinie: <…>
```
