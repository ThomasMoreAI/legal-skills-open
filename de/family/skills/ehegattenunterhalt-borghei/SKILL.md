---
name: ehegattenunterhalt-borghei
title: /familienrecht:ehegattenunterhalt
description: Prüfung und Berechnung des Ehegattenunterhalts – Trennungsunterhalt § 1361 BGB, nachehelicher Unterhalt und Unterhaltstatbestände §§ 1569–1576 BGB, Bedarf nach den ehelichen Lebensverhältnissen § 1578 BGB, Leistungsfähigkeit und Selbstbehalt, Befristung und Herabsetzung § 1578b BGB, Erwerbsobliegenheit. Use when nach Trennung oder Scheidung Anspruch, Höhe und Dauer des Ehegattenunterhalts zu prüfen sind.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/familienrecht/skills/ehegattenunterhalt
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: family
language: de
---

# /familienrecht:ehegattenunterhalt

## Zweck

Ehegattenunterhalt zerfällt in zwei rechtlich getrennte Phasen: den **Trennungsunterhalt** (§ 1361 BGB) bis zur Rechtskraft der Scheidung und den **nachehelichen Unterhalt** (§§ 1569 ff. BGB) danach. Beide folgen unterschiedlichen Maßstäben — vor allem gilt nach der Scheidung der Grundsatz der **Eigenverantwortung** (§ 1569 BGB), der einen eigenen Unterhaltstatbestand voraussetzt. Fehler bei Tatbestand, Bedarfsberechnung, Leistungsfähigkeit oder bei der Befristung kosten vier- bis fünfstellig pro Jahr. Dieser Skill strukturiert Anspruchsgrund, Höhe und Dauer.

## Eingaben

- Status: Getrenntleben oder rechtskräftig geschieden (Stichtag)
- Einkommen beider Ehegatten (bereinigtes Nettoeinkommen, Belege)
- Betreuung minderjähriger gemeinsamer Kinder (Alter, Betreuungsmodell)
- Ehedauer (Heirat bis Rechtshängigkeit Scheidungsantrag)
- Krankheit, Behinderung oder Alter eines Ehegatten
- Erwerbsbiografie (frühere Tätigkeit, Ausbildung, ehebedingte Nachteile)
- Bestehender Kindesunterhalt, weitere Unterhaltspflichten

## Sub-Agent-Architektur

Die Prüfung läuft als geordnete Kette: Ein Phasen-Agent fixiert zunächst, ob Trennungs- oder nachehelicher Unterhalt zu prüfen ist, da dies den gesamten Maßstab bestimmt. Bei nachehelichem Unterhalt ermittelt ein Tatbestands-Agent den konkreten Anspruchsgrund (§§ 1570–1573 BGB), denn ohne Tatbestand kein Anspruch. Ein Bedarfs-Agent berechnet Höhe und Halbteilung (§ 1578 BGB), ein Leistungsfähigkeits-Agent prüft Selbstbehalt und Bedürftigkeit gegen. Ein Billigkeits-Agent prüft abschließend Befristung und Herabsetzung (§ 1578b BGB). Die Agenten arbeiten sequentiell — jeder baut auf dem Ergebnis des vorigen auf.

## Ablauf

### 1. Phase bestimmen: Trennungs- oder nachehelicher Unterhalt

- **Trennungsunterhalt** ([§ 1361 BGB](https://www.gesetze-im-internet.de/bgb/__1361.html)): ab Getrenntleben bis Rechtskraft der Scheidung. Kein eigener Tatbestand nötig — Anspruch besteht dem Grunde nach aus der fortbestehenden ehelichen Solidarität. Erwerbsobliegenheit ist im Trennungsjahr noch eingeschränkt.
- **Nachehelicher Unterhalt** ([§§ 1569 ff. BGB](https://www.gesetze-im-internet.de/bgb/__1569.html)): ab Rechtskraft der Scheidung. Es gilt der Grundsatz der **Eigenverantwortung** (§ 1569 BGB) — Unterhalt nur, soweit ein gesetzlicher Tatbestand greift.

### 2. Unterhaltstatbestand (nur nachehelich, §§ 1570–1573 BGB)

| Tatbestand | Norm | Voraussetzung |
|---|---|---|
| Betreuungsunterhalt | [§ 1570 BGB](https://www.gesetze-im-internet.de/bgb/__1570.html) | Betreuung gemeinsamen Kindes, mind. 3 Jahre ab Geburt, danach Verlängerung aus kind- oder elternbezogenen Gründen |
| Unterhalt wegen Alters | [§ 1571 BGB](https://www.gesetze-im-internet.de/bgb/__1571.html) | Erwerb wegen Alters nicht zumutbar |
| Unterhalt wegen Krankheit | [§ 1572 BGB](https://www.gesetze-im-internet.de/bgb/__1572.html) | Krankheit/Gebrechen verhindern Erwerb |
| Erwerbslosigkeit / Aufstockung | [§ 1573 BGB](https://www.gesetze-im-internet.de/bgb/__1573.html) | keine angemessene Stelle (Abs. 1) oder Einkommen deckt vollen Bedarf nicht (Aufstockungsunterhalt, Abs. 2) |

Ohne einschlägigen Tatbestand besteht **kein** nachehelicher Unterhaltsanspruch.

### 3. Bedarf nach den ehelichen Lebensverhältnissen (§ 1578 BGB)

- Maßstab ist der eheprägende Lebensstandard ([§ 1578 BGB](https://www.gesetze-im-internet.de/bgb/__1578.html)).
- Berechnung über das **Halbteilungsprinzip**: beide bereinigten Erwerbseinkommen werden zusammengeführt, der Bedarf liegt grundsätzlich bei der Hälfte der Summe.
- Bei Erwerbseinkommen wird regelmäßig ein Erwerbstätigenbonus abgesetzt (Quotenberechnung nach Leitlinien der OLG / Düsseldorfer Tabelle — Struktur, keine festen Beträge).
- Vorrangiger Kindesunterhalt wird vor der Quotenbildung abgezogen.

> Die konkreten Selbstbehalts- und Bedarfsbeträge der **Düsseldorfer Tabelle** ändern sich jährlich. Falls Eurobeträge genannt werden, mit `[unverifiziert – prüfen]` markieren und gegen die aktuelle Tabelle abgleichen.

### 4. Bedürftigkeit und Erwerbsobliegenheit

- **Bedürftigkeit**: Der Berechtigte kann den Bedarf nicht aus eigenem Einkommen oder Vermögen decken.
- **Erwerbsobliegenheit**: Nach der Scheidung trifft den Berechtigten grundsätzlich die Obliegenheit, eine angemessene Erwerbstätigkeit aufzunehmen (Ausfluss der Eigenverantwortung, § 1569 BGB). Reicht ein erzielbares oder fiktiv anzurechnendes Einkommen aus, entfällt oder mindert sich der Anspruch. Bei Kinderbetreuung ist die Erwerbsobliegenheit nach § 1570 BGB eingeschränkt (gestuftes Betreuungsmodell).

### 5. Leistungsfähigkeit und Selbstbehalt

- Der Pflichtige muss den Unterhalt zahlen können, ohne den eigenen angemessenen **Selbstbehalt** zu unterschreiten.
- Rangfolge mehrerer Unterhaltsberechtigter nach § 1609 BGB beachten (minderjährige Kinder vorrangig).
- Der konkrete Selbstbehalt folgt der Düsseldorfer Tabelle (jährlich angepasst) — bei Nennung von Beträgen `[unverifiziert – prüfen]`.

### 6. Befristung und Herabsetzung (§ 1578b BGB)

- [§ 1578b BGB](https://www.gesetze-im-internet.de/bgb/__1578b.html) erlaubt die **Herabsetzung** des Bedarfs auf den angemessenen Lebensbedarf und/oder die zeitliche **Befristung** des nachehelichen Unterhalts wegen Unbilligkeit.
- Zentrales Kriterium: **ehebedingte Nachteile** (z. B. Aufgabe der Erwerbstätigkeit wegen Kinderbetreuung). Solange solche Nachteile fortwirken, sind Herabsetzung und Befristung regelmäßig ausgeschlossen.
- Abwägung von Ehedauer, Rollenverteilung, Dauer der Kinderbetreuung. Gilt nicht für den Trennungsunterhalt (§ 1361 BGB).

### 7. Ergebnis

Anspruchsgrund (Tatbestand oder § 1361 BGB), Höhe (Quote/Halbteilung), gedeckt durch Leistungsfähigkeit, sowie Aussage zu Befristung/Herabsetzung zusammenführen.

## Risiken / typische Fehler

- **Phasen vermischt** — Trennungsunterhalt braucht keinen Tatbestand, nachehelicher Unterhalt schon (Eigenverantwortung, § 1569 BGB).
- **Tatbestand übersprungen** — ohne §§ 1570–1573 BGB kein nachehelicher Anspruch.
- **Erwerbsobliegenheit nicht geprüft** — fiktives Einkommen kann den Anspruch reduzieren oder ausschließen.
- **Selbstbehalt des Pflichtigen ignoriert** — Leistungsfähigkeit begrenzt den Anspruch.
- **Befristung § 1578b BGB nicht angesprochen** — gerade bei kurzer Ehe ohne ehebedingte Nachteile zentral.
- **Vorrang des Kindesunterhalts** (§ 1609 BGB) bei der Quotenbildung vergessen.
- **Feste Eurobeträge** aus veralteter Düsseldorfer Tabelle übernommen — jährlich prüfen, `[unverifiziert – prüfen]`.

## Ausgabeformat

```
EHEGATTENUNTERHALT-PRÜFUNG — <Mandat> — <Datum>

I.    Phase                          [Trennungsunterhalt § 1361 / nachehelich §§ 1569 ff.]
II.   Unterhaltstatbestand           [§ 1570 Betreuung / § 1571 Alter / § 1572 Krankheit /
                                      § 1573 Erwerbslosigkeit/Aufstockung]
III.  Bedarf (§ 1578 BGB)
      Einkommen Berechtigter:        <EUR bereinigt>
      Einkommen Pflichtiger:         <EUR bereinigt>
      Halbteilung / Quote:           <EUR Bedarf>
IV.   Bedürftigkeit / Erwerbsobliegenheit
      Eigenes/fiktives Einkommen:    <EUR>
      Obliegenheit:                  [erfüllt / Anrechnung fiktiv]
V.    Leistungsfähigkeit
      Selbstbehalt gewahrt:          [ja / nein]   <Betrag [unverifiziert – prüfen]>
VI.   Befristung/Herabsetzung § 1578b
      Ehebedingte Nachteile:         [ja / nein]
      Befristung:                    [erwogen / ausgeschlossen]

Ergebnis (Grund / Höhe / Dauer):     <…>
```

## Quellen

### Statute

- [§ 1361 BGB](https://www.gesetze-im-internet.de/bgb/__1361.html) (Unterhalt bei Getrenntleben / Trennungsunterhalt)
- [§ 1569 BGB](https://www.gesetze-im-internet.de/bgb/__1569.html) (Grundsatz der Eigenverantwortung)
- [§ 1570 BGB](https://www.gesetze-im-internet.de/bgb/__1570.html) (Betreuungsunterhalt)
- [§ 1571 BGB](https://www.gesetze-im-internet.de/bgb/__1571.html) (Unterhalt wegen Alters)
- [§ 1572 BGB](https://www.gesetze-im-internet.de/bgb/__1572.html) (Unterhalt wegen Krankheit)
- [§ 1573 BGB](https://www.gesetze-im-internet.de/bgb/__1573.html) (Aufstockungs- und Erwerbslosigkeitsunterhalt)
- [§ 1578 BGB](https://www.gesetze-im-internet.de/bgb/__1578.html) (Bedarf nach den ehelichen Lebensverhältnissen)
- [§ 1578b BGB](https://www.gesetze-im-internet.de/bgb/__1578b.html) (Herabsetzung und zeitliche Begrenzung wegen Unbilligkeit)
- [§ 1609 BGB](https://www.gesetze-im-internet.de/bgb/__1609.html) (Rangfolge mehrerer Unterhaltsberechtigter)

### Kommentare

- Maurer, in: MüKoBGB, 9. Aufl. 2024, § 1578 Rn. 1 ff.
- Schwab, Familienrecht, 32. Aufl. 2024
- Wendl / Dose, Das Unterhaltsrecht in der familienrichterlichen Praxis

### Hinweise

- Düsseldorfer Tabelle und Leitlinien der OLG: jährliche Anpassung der Selbstbehalts- und Bedarfssätze — vor Verwendung aktualisieren.
