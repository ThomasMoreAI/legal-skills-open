---
name: zwangsvollstreckung-grundlagen-borghei
title: /prozessrecht:zwangsvollstreckung-grundlagen
description: Prüfung der Zwangsvollstreckung im Zivilrecht – die drei Vollstreckungsvoraussetzungen Titel, Klausel und Zustellung §§ 704, 750 ZPO, Sachpfändung beweglicher Sachen § 803 ZPO, Forderungs- und Lohnpfändung mit Pfändungsschutz § 850 ZPO, Vollstreckungserinnerung § 766 ZPO. Use when aus einem Titel vollstreckt werden soll oder eine bereits begonnene Zwangsvollstreckung auf ihre Voraussetzungen und Rechtsbehelfe geprüft wird.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/prozessrecht/skills/zwangsvollstreckung-grundlagen
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: litigation
language: de
---

# /prozessrecht:zwangsvollstreckung-grundlagen

## Zweck

Ein obsiegendes Urteil ist wertlos, solange der Schuldner nicht zahlt. Die Zwangsvollstreckung setzt das titulierte Recht zwangsweise durch. Jede Vollstreckung steht auf **drei Voraussetzungen**: einem **Titel**, einer **Klausel** und der **Zustellung**. Fehlt eine, ist die Vollstreckung anfechtbar. Dieser Skill prüft die drei Voraussetzungen, wählt die Vollstreckungsart (Sachpfändung, Forderungs-/Lohnpfändung) und ordnet die Rechtsbehelfe gegen fehlerhafte Vollstreckung ein.

## Eingaben

- **Titel** (Urteil, Vollstreckungsbescheid, notarielle Urkunde, Vergleich)
- **Schuldner und Gläubiger** (Identität, Übereinstimmung mit dem Titel)
- **Vollstreckungsobjekt** (bewegliche Sachen, Konten, Arbeitseinkommen, Grundbesitz)
- **Forderungshöhe** (Hauptforderung, Zinsen, Kosten, bereits erbrachte Teilzahlungen)
- **Zustellnachweis** (wurde der Titel zugestellt? wann?)
- **Schuldnerverhältnisse** (Drittschuldner, Arbeitgeber, Unterhaltspflichten — für Pfändungsschutz)

## Sub-Agent-Architektur

Die Prüfung wird in drei gedankliche Prüfstränge zerlegt, die zusammengeführt werden. Ein erster Strang prüft die **allgemeinen Vollstreckungsvoraussetzungen** – Titel (§ 704 ZPO), vollstreckbare Ausfertigung mit Klausel und Zustellung an den Schuldner (§ 750 ZPO). Ein zweiter Strang wählt die **Vollstreckungsart** und das richtige Organ – Sachpfändung durch den Gerichtsvollzieher (§ 803 ZPO) oder Forderungs-/Lohnpfändung durch das Vollstreckungsgericht (§ 850 ZPO) – und prüft Pfändungsfreigrenzen. Ein dritter Strang ordnet die **Rechtsbehelfe** ein, insbesondere die Vollstreckungserinnerung gegen die Art und Weise (§ 766 ZPO) sowie die Vollstreckungsabwehr- und Drittwiderspruchsklage. Die Synthese empfiehlt das vorrangige Vollstreckungsobjekt und benennt Mängel der laufenden Vollstreckung.

## Ablauf

### 1. Titel ([§ 704 ZPO](https://www.gesetze-im-internet.de/zpo/__704.html))

- Vollstreckt wird aus **vollstreckbaren Endurteilen** (§ 704 ZPO) und den weiteren Titeln des § 794 ZPO (Vergleich, Vollstreckungsbescheid, notarielle Urkunde mit Unterwerfungsklausel).
- Der Titel muss einen **bestimmten, vollstreckungsfähigen Inhalt** haben (Leistung genau bezeichnet, Betrag beziffert).

### 2. Klausel und Zustellung ([§ 750 ZPO](https://www.gesetze-im-internet.de/zpo/__750.html))

- **Vollstreckungsklausel** (§ 724 ZPO): Die vollstreckbare Ausfertigung trägt die Klausel „Vorstehende Ausfertigung wird … zum Zwecke der Zwangsvollstreckung erteilt". Bei Rechtsnachfolge: titelumschreibende Klausel (§ 727 ZPO).
- **Zustellung** (§ 750 Abs. 1 ZPO): Die Vollstreckung darf erst beginnen, wenn Gläubiger und Schuldner im Titel/in der Klausel **namentlich bezeichnet** sind und der Titel dem Schuldner **zugestellt** ist (Klauselzustellung gleichzeitig oder vorher).
- Damit stehen die **drei Vollstreckungsvoraussetzungen** fest: Titel, Klausel, Zustellung.

### 3. Sachpfändung beweglicher Sachen ([§ 803 ZPO](https://www.gesetze-im-internet.de/zpo/__803.html))

- Die Vollstreckung in **bewegliche Sachen** erfolgt durch **Pfändung** seitens des Gerichtsvollziehers (§ 803 ZPO); gepfändet wird durch Inbesitznahme oder Anbringen des Pfandsiegels.
- Grenzen: Keine Pfändung über den zur Befriedigung und Kostendeckung nötigen Umfang hinaus (§ 803 Abs. 1 S. 2 ZPO – Verbot der Überpfändung); unpfändbare Sachen nach § 811 ZPO.

### 4. Forderungs- und Lohnpfändung ([§ 850 ZPO](https://www.gesetze-im-internet.de/zpo/__850.html))

- Forderungen werden durch **Pfändungs- und Überweisungsbeschluss** des Vollstreckungsgerichts gepfändet (§§ 829, 835 ZPO); der **Drittschuldner** darf nicht mehr an den Schuldner leisten.
- **Arbeitseinkommen** ist nur in den Grenzen der §§ 850 ff. ZPO pfändbar: **Pfändungsfreigrenzen** nach § 850c ZPO (Pfändungstabelle), erhöht durch Unterhaltspflichten. Diese Schutzvorschriften sind von Amts wegen zu beachten.

### 5. Rechtsbehelfe gegen die Vollstreckung

- **Vollstreckungserinnerung** ([§ 766 ZPO](https://www.gesetze-im-internet.de/zpo/__766.html)): gegen die **Art und Weise** der Zwangsvollstreckung und Verfahrensverstöße des Vollstreckungsorgans (z. B. fehlende Zustellung, Überpfändung, Verstoß gegen Pfändungsschutz) – Entscheidung durch das Vollstreckungsgericht.
- **Vollstreckungsabwehrklage** (§ 767 ZPO): gegen den **materiellen Anspruch** (z. B. nachträgliche Erfüllung, Aufrechnung, Stundung).
- **Drittwiderspruchsklage** (§ 771 ZPO): wenn ein Dritter ein die Veräußerung hinderndes Recht (z. B. Eigentum) am gepfändeten Gegenstand geltend macht.
- **Sofortige Beschwerde** (§ 793 ZPO) gegen Entscheidungen im Vollstreckungsverfahren.

### 6. Strategie

- Vorrangig pfänden, was schnell verwertbar und werthaltig ist (Konten, Arbeitseinkommen); Sachpfändung ist oft unergiebig.
- Kombination mit Vermögensauskunft des Schuldners (§§ 802c ff. ZPO) zur Ermittlung von Vollstreckungsobjekten.

## Risiken / typische Fehler

- **Zustellung** des Titels unterblieben oder nicht nachweisbar: Die Vollstreckung ist auf Vollstreckungserinnerung aufzuheben (§ 750 ZPO).
- **Klausel** fehlt oder ist bei Rechtsnachfolge nicht umgeschrieben: Vollstreckung unzulässig.
- **Pfändungsschutz** des § 850 ZPO missachtet: Lohnpfändung über die Pfändungsfreigrenzen hinaus ist fehlerhaft und mit der Erinnerung angreifbar.
- **Überpfändung** bei der Sachpfändung: Es wird mehr gepfändet, als zur Befriedigung nötig ist (§ 803 Abs. 1 S. 2 ZPO).

## Ausgabeformat

```
ZWANGSVOLLSTRECKUNG — <Titel> — <Datum>

I.    Drei Voraussetzungen
      Titel § 704                  Art: <Urteil/VB/Vergleich/notar. Urkunde>
      Klausel § 724/§ 750          [erteilt? Rechtsnachfolge umgeschrieben?]
      Zustellung § 750             [an Schuldner zugestellt am <…>]
II.   Vollstreckungsart
      - Sachpfändung § 803         Organ: Gerichtsvollzieher [Überpfändung?]
      - Forderungs-/Lohnpfändung   PfÜB; Pfändungsschutz § 850c [Freigrenze]
III.  Forderungshöhe              Hauptforderung / Zinsen / Kosten: <…>
IV.   Rechtsbehelfe
      Erinnerung § 766             Art und Weise / Verfahrensverstoß
      Abwehrklage § 767            materielle Einwendung
      Drittwiderspruch § 771       Recht eines Dritten
V.    Strategie / vorrangiges Objekt  <…>

Ergebnis: <Vollstreckung zulässig / Mangel: …>
```

## Quellen

### Statute

- [§ 704 ZPO](https://www.gesetze-im-internet.de/zpo/__704.html) (vollstreckbare Endurteile), [§ 750 ZPO](https://www.gesetze-im-internet.de/zpo/__750.html) (Voraussetzungen / Zustellung)
- [§ 724 ZPO](https://www.gesetze-im-internet.de/zpo/__724.html), [§ 727 ZPO](https://www.gesetze-im-internet.de/zpo/__727.html) (Klausel), [§ 794 ZPO](https://www.gesetze-im-internet.de/zpo/__794.html) (weitere Titel)
- [§ 803 ZPO](https://www.gesetze-im-internet.de/zpo/__803.html) (Sachpfändung), [§ 811 ZPO](https://www.gesetze-im-internet.de/zpo/__811.html) (unpfändbare Sachen), [§ 829 ZPO](https://www.gesetze-im-internet.de/zpo/__829.html) (Forderungspfändung)
- [§ 850 ZPO](https://www.gesetze-im-internet.de/zpo/__850.html), [§ 850c ZPO](https://www.gesetze-im-internet.de/zpo/__850c.html) (Pfändungsschutz Arbeitseinkommen)
- [§ 766 ZPO](https://www.gesetze-im-internet.de/zpo/__766.html) (Vollstreckungserinnerung), [§ 767 ZPO](https://www.gesetze-im-internet.de/zpo/__767.html), [§ 771 ZPO](https://www.gesetze-im-internet.de/zpo/__771.html)

### Kommentare

- Lackmann, in: Musielak/Voit, ZPO, 22. Aufl. 2025, §§ 704 ff. Rn. 1 ff.
- Seibel, in: Zöller, ZPO, 36. Aufl. 2025, § 750 Rn. 1 ff.

### Rechtsprechung

- Zur Klauselumschreibung bei Rechtsnachfolge (§ 727 ZPO) und zum Pfändungsschutz besteht gefestigte BGH-Rechtsprechung (Aktenzeichen vor Zitat verifizieren) `[unverifiziert – prüfen]`
