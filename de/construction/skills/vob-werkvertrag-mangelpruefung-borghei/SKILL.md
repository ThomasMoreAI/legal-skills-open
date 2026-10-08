---
name: vob-werkvertrag-mangelpruefung-borghei
title: /baurecht:vob-werkvertrag-mangelpruefung
description: 'Mängelprüfung am Bauwerk: Vertragsregime klären (BGB-Werkvertrag §§ 631 ff., Bauvertrag §§ 650a ff., Verbraucherbauvertrag §§ 650i ff. vs. VOB/B), Abnahme § 640 BGB und ihre Wirkungen, Mängelrechte § 634 BGB in gesetzlicher Reihenfolge, Verjährung § 634a BGB (5/2 Jahre); bei VOB/B die AGB-Inhaltskontrolle der „im Ganzen"-Privilegierung. Use when ein Bauherr oder Auftragnehmer nach Abnahme über Mängel streitet, eine Mängelrüge formuliert werden soll, oder die Wirksamkeit einer VOB/B-Klausel zur Verjährung / Sicherheit / Zahlung geprüft wird.'
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/baurecht/skills/vob-werkvertrag-mangelpruefung
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: construction
language: de
---

# /baurecht:vob-werkvertrag-mangelpruefung

## Zweck

Der Skill prüft Mängelansprüche aus einem Bauvertrag und ordnet sie systematisch dem zutreffenden Vertragsregime zu. Er erzwingt vorab die Klärung, ob die VOB/B **im Ganzen** wirksam einbezogen ist – andernfalls greifen §§ 305 ff. BGB. Anschließend werden Abnahme, Mängelrechte des § 634 BGB in gesetzlicher Reihenfolge und die Verjährung nach § 634a BGB bzw. § 13 Nr. 4 VOB/B geprüft.

## Eingaben

- Parteien (Verbraucher? Unternehmer? Bauträger?)
- Vertragstext / -typ (BGB-Werkvertrag, Bauvertrag, Verbraucherbauvertrag, Architektenvertrag)
- Ob und wie die VOB/B einbezogen wurde (Verweisklausel? Übergabe? individuelle Abweichungen?)
- Datum / Form der Abnahme (förmlich, konkludent, fiktiv § 640 II BGB)
- Konkrete Mängel (Datum der Feststellung, Symptom, vermutete Ursache, Beweismittel)
- Bisherige Mängelrügen, Fristsetzungen, Selbstvornahme
- Sicherheiten (Bauhandwerkersicherheit § 650f BGB; Mängelsicherheit)

## Sub-Agent-Architektur

Researcher liefert die BGB-/VOB/B-Normen, BGH VII. Zivilsenat-Leitentscheidungen (insb. zur „im Ganzen"-Privilegierung und konkludenten Abnahme) und Kommentarstellen (Werner/Pastor; Kniffka/Koeble; Ingenstau/Korbion). Drafter prüft im Gutachtenstil von Vertragsregime über Abnahme zu Mängelrechten und Verjährung und entwirft die Mängelrüge mit Fristsetzung. Reviewer prüft das Vertragsregime, die AGB-Kontrolle der VOB/B, die Reihenfolge der Mängelrechte und die Verjährungsberechnung.

## Ablauf

### 1. Vertragsregime einordnen

Vorab klären, welches Regime gilt:

- **Reiner BGB-Werkvertrag** §§ 631 ff. (z. B. einzelne Reparatur)
- **Bauvertrag** § 650a I BGB (Vertrag über Herstellung, Wiederherstellung, Beseitigung oder Umbau eines Bauwerks oder Teils davon, soweit für die Standfestigkeit von wesentlicher Bedeutung) → Sonderregeln §§ 650b ff. (Anordnungsrecht des Bestellers § 650b; Bauhandwerkersicherheit § 650f; Zustandsfeststellung § 650g; Schriftform der Kündigung § 650h)
- **Verbraucherbauvertrag** § 650i BGB (Verbraucher als Besteller; Errichtung eines neuen Gebäudes oder erhebliche Umbaumaßnahmen) → Baubeschreibung § 650j; Widerrufsrecht § 650l; Abschlagsregelung § 650m; Erwerbsrecht an Planungsunterlagen § 650n
- **Architekten-/Ingenieurvertrag** §§ 650p–t BGB (eigene Phase / Werk; § 650q HOAI-Bezug; § 650s gesamtschuldnerische Haftung mit dem ausführenden Unternehmer für Überwachungsmängel)

### 2. VOB/B-Einbeziehung prüfen

Die VOB/B ist **AGB**. Die Privilegierung gegenüber den §§ 305 ff. BGB greift nur, wenn sie **„im Ganzen" ohne ins Gewicht fallende Abweichungen** vereinbart ist (st. Rspr. BGH; Grundsatzentscheidung BGHZ 96, 129 ff.; weitergeführt zB BGH, Urt. v. 22.01.2004 – VII ZR 419/02 (https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=22.01.2004&Aktenzeichen=VII+ZR+419/02)).

Ist der Besteller **Verbraucher**, scheidet die Privilegierung von vornherein aus – die VOB/B unterliegt vollumfänglich der Inhaltskontrolle nach §§ 305 ff. BGB (BGH, Urt. v. 24.07.2008 – VII ZR 55/07 (https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=24.07.2008&Aktenzeichen=VII+ZR+55/07)). Belastende Klauseln (§ 13 Nr. 4 VOB/B kürzere Verjährung, § 16 VOB/B Zahlungsmodalitäten, § 17 VOB/B Sicherheiten) sind dann an § 307 BGB zu messen.

> **Reviewer-Hinweis:** Wird die VOB/B in einem Verbraucherbauvertrag als „wirksam" einbezogen behandelt, ist das ein Blocker.

### 3. Abnahme und ihre Wirkungen

Die **Abnahme** (§ 640 BGB) ist zentral:

- **Vergütungsfälligkeit** § 641 I BGB
- **Beweislastumkehr** für Mängel: ab Abnahme trägt der Besteller die Beweislast für den Mangel und dessen Verursachung durch den Unternehmer (vgl. § 640 II BGB für Mangelrechte trotz Kenntnis; Rspr. zur Beweislast nach Abnahme)
- **Gefahrübergang** § 644 BGB
- **Beginn der Verjährung** § 634a II BGB

Formen: ausdrücklich, **konkludent** (durch Ingebrauchnahme nach Mangelfreiheit-Anschein; BGH-st. Rspr. `[unverifiziert]`), **fiktiv** nach § 640 II BGB (Fristsetzung des Unternehmers + keine Verweigerung wegen wesentlichen Mangels). Bei VOB/B zusätzlich förmliche Abnahme § 12 Nr. 4 VOB/B; fiktive Abnahme § 12 Nr. 5 VOB/B.

### 4. Mangelbegriff § 633 BGB

Sach- oder Rechtsmangel, Soll-/Ist-Vergleich, vorrangig **vereinbarte Beschaffenheit**, hilfsweise vertraglich vorausgesetzte Verwendung, hilfsweise gewöhnliche Verwendung. Anerkannte Regeln der Technik (a.R.d.T.) zur Zeit der Abnahme – nicht zwingend identisch mit DIN-Normen.

### 5. Mängelrechte § 634 BGB – gesetzliche Reihenfolge

1. **Nacherfüllung** § 634 Nr. 1 iVm § 635 BGB – Wahlrecht des Unternehmers (Mängelbeseitigung oder Neuherstellung). **Fristsetzung** zur Nacherfüllung (§ 636) ist Voraussetzung für die weiteren Rechte (außer bei Entbehrlichkeit § 636).
2. **Selbstvornahme** § 634 Nr. 2 iVm § 637 BGB – Aufwendungsersatz, ggf. Vorschuss.
3. **Rücktritt** § 634 Nr. 3 iVm §§ 636, 323, 326 V BGB – nicht bei unerheblichem Mangel (§ 323 V 2).
4. **Minderung** § 634 Nr. 3 iVm § 638 BGB – Wahlrecht des Bestellers.
5. **Schadensersatz statt der Leistung** § 634 Nr. 4 iVm §§ 280, 281 BGB; Aufwendungsersatz § 284 BGB.

Bei VOB/B parallel: § 13 Nr. 5 VOB/B (Nacherfüllung), § 13 Nr. 6 (Minderung), § 13 Nr. 7 (Schadensersatz).

### 6. Verjährung

- **§ 634a I Nr. 2 BGB**: **5 Jahre** für Arbeiten an einem **Bauwerk** und für Planungs-/Überwachungsleistungen, soweit auf das Bauwerk bezogen
- **§ 634a I Nr. 1 BGB**: **2 Jahre** für Werke, deren Erfolg in der Herstellung, Wartung oder Veränderung einer Sache (nicht Bauwerk) liegt
- **§ 634a II BGB**: Beginn mit **Abnahme**; ohne Abnahme allgemeine §§ 195, 199 BGB (BGH-Linie zum Verjährungsbeginn ohne Abnahme `[unverifiziert]`)
- **§ 634a III BGB**: arglistig verschwiegener Mangel – §§ 195, 199 BGB (Höchstfristen 10/30 Jahre)
- **§ 13 Nr. 4 VOB/B**: **4 Jahre** bei Bauwerken; AGB-Inhaltskontrolle ggü. Verbraucher → diese kürzere Verjährung dürfte nicht standhalten

### 7. Mängelrüge entwerfen

Eine wirksame Mängelrüge enthält:

- konkrete Bezeichnung von Ort und Symptom des Mangels (kein Tatsachenkern offen lassen)
- Verweis auf den Vertrag / die a.R.d.T. / die vereinbarte Beschaffenheit
- **Aufforderung zur Nacherfüllung** mit **angemessener Frist** (Faustregel: 2–4 Wochen je nach Mangelschwere und Bauablauf)
- Hinweis auf Folgen (Selbstvornahme, Minderung, Rücktritt, Schadensersatz)
- ggf. Aufforderung zur **Mängelbeseitigungssicherheit** (§ 650f gilt aF; arg.: Druckmittel)

## Quellen und Zitierweise

Verbindlich: [`../../../references/zitierweise.md`](../../../references/zitierweise.md).

### Statute

- [§ 631 BGB](https://www.gesetze-im-internet.de/bgb/__631.html) (Werkvertrag)
- [§ 633 BGB](https://www.gesetze-im-internet.de/bgb/__633.html) (Sach- und Rechtsmangel)
- [§ 634 BGB](https://www.gesetze-im-internet.de/bgb/__634.html) (Mängelrechte)
- [§ 634a BGB](https://www.gesetze-im-internet.de/bgb/__634a.html) (Verjährung)
- [§ 635 BGB](https://www.gesetze-im-internet.de/bgb/__635.html) (Nacherfüllung)
- [§ 636 BGB](https://www.gesetze-im-internet.de/bgb/__636.html) (Entbehrlichkeit der Fristsetzung)
- [§ 637 BGB](https://www.gesetze-im-internet.de/bgb/__637.html) (Selbstvornahme)
- [§ 638 BGB](https://www.gesetze-im-internet.de/bgb/__638.html) (Minderung)
- [§ 640 BGB](https://www.gesetze-im-internet.de/bgb/__640.html) (Abnahme)
- [§ 641 BGB](https://www.gesetze-im-internet.de/bgb/__641.html) (Fälligkeit der Vergütung)
- [§ 650a BGB](https://www.gesetze-im-internet.de/bgb/__650a.html) (Bauvertrag)
- [§ 650b BGB](https://www.gesetze-im-internet.de/bgb/__650b.html) (Anordnungsrecht)
- [§ 650f BGB](https://www.gesetze-im-internet.de/bgb/__650f.html) (Bauhandwerkersicherheit)
- [§ 650g BGB](https://www.gesetze-im-internet.de/bgb/__650g.html) (Zustandsfeststellung)
- [§ 650i BGB](https://www.gesetze-im-internet.de/bgb/__650i.html) (Verbraucherbauvertrag)
- [§ 650l BGB](https://www.gesetze-im-internet.de/bgb/__650l.html) (Widerrufsrecht)
- [§ 650p BGB](https://www.gesetze-im-internet.de/bgb/__650p.html) (Architektenvertrag)
- [§ 650s BGB](https://www.gesetze-im-internet.de/bgb/__650s.html) (gesamtschuldnerische Haftung)
- [§§ 305 ff. BGB](https://www.gesetze-im-internet.de/bgb/__305.html) (AGB)
- VOB/B (DIN 1961:2019) – Vertragsanlage, kein gesetze-im-internet.de-Eintrag; § 13 VOB/B (Mängelansprüche)

### Kommentare

- Busche, in: MüKoBGB, 9. Aufl. 2023, §§ 633, 634, 634a Rn. 1 ff.
- Schwenker, in: MüKoBGB, 9. Aufl. 2023, §§ 650a ff. Rn. 1 ff.
- Werner/Pastor, Der Bauprozess, 17. Aufl. 2024, Rn. 1500 ff. (Mängelrechte) und Rn. 2000 ff. (Verjährung)
- Kniffka/Koeble/Jurgeleit/Sacher, Kompendium des Baurechts, 5. Aufl. 2020, 6. Teil (Mängelrechte)
- Ingenstau/Korbion, VOB Teile A und B, 22. Aufl. 2023, § 13 VOB/B Rn. 1 ff.
- Messerschmidt/Voit, Privates Baurecht, 4. Aufl. 2022, §§ 634, 634a BGB Rn. 1 ff.

### Rechtsprechung (`[unverifiziert – prüfen in juris/BeckOnline]`)

1. BGH, Urt. v. 16.12.1982 – VII ZR 92/82, BGHZ 96, 129 (VOB/B „im Ganzen"-Privilegierung – Grundsatz)
2. BGH, Urt. v. 22.01.2004 – VII ZR 419/02 (Weiterentwicklung der „im Ganzen"-Linie)
3. BGH, Urt. v. 24.07.2008 – VII ZR 55/07 (keine Privilegierung ggü. Verbraucher)
4. BGH, Urt. v. 25.01.1996 – VII ZR 26/95 (konkludente Abnahme)
5. BGH, Urt. v. 08.11.2007 – VII ZR 183/05 (Beweislastumkehr nach Abnahme)
6. BGH, Urt. v. 04.07.2019 – VII ZR 332/17, BGHZ 222, 287 (Schadensersatz statt Leistung – fiktive Mängelbeseitigungskosten)

## Ausgabeformat

```
GUTACHTEN — Mängelprüfung Bauvertrag
Mandant: <…>   Vertragspartner: <…>
Bauvorhaben: <Adresse, Bauteil>

I. Sachverhalt (knapp)

II. Frage(n)

III. Kurzantwort
     - Vertragsregime: [BGB-Werkvertrag / Bauvertrag § 650a / Verbraucherbau § 650i / Architekt § 650p]
     - VOB/B-Einbeziehung: [im Ganzen wirksam / nicht wirksam – AGB-Kontrolle / ggü. Verbraucher nicht privilegiert]
     - Empfehlung: [Mängelrüge mit Frist / Rücktritt / Minderung / Schadensersatz / Selbstvornahme nach Vorschussklage]

IV. Rechtliche Bewertung
    1. Vertragsregime
    2. VOB/B-Einbeziehung und AGB-Kontrolle
    3. Abnahme und ihre Wirkungen
    4. Mangelbegriff (§ 633 BGB) – Soll/Ist
    5. Mängelrechte § 634 BGB
       a) Nacherfüllung + Fristsetzung
       b) ggf. Selbstvornahme / Rücktritt / Minderung / Schadensersatz
    6. Verjährung
       – § 634a I Nr. 2 BGB (5 Jahre, Bauwerk) ab Abnahme
       – ggf. § 13 Nr. 4 VOB/B (4 Jahre) – AGB-Kontrolle
       – arglistige Verschweigung §§ 195, 199 BGB

V. Entwurf Mängelrüge / Schreiben
   – konkrete Mangelbeschreibung
   – Aufforderung zur Nacherfüllung mit Frist (Datum)
   – Sanktionsandrohung (Selbstvornahme / Rücktritt / Minderung / SE)

VI. Fristen-Box
    – Mängelverjährung: <Datum>
    – Frist Nacherfüllung: <Datum>
    – ggf. Bauhandwerkersicherheit § 650f BGB

VII. Risiken / offene Punkte
     <Einstufung mit Begründung; offene Tatsachenfragen>

VIII. Quellenverzeichnis
```

## Beispiel (verkürzt, Gutachtenstil)

**Sachverhalt.** Privater Bauherr B beauftragt Unternehmer U mit Errichtung eines Einfamilienhauses. Vertrag verweist pauschal auf die VOB/B und enthält daneben individuelle Klauseln zur Schlusszahlung. Abnahme am 14.03.2021 förmlich. Im Februar 2026 zeigen sich Risse im Estrich. B fordert Beseitigung; U weist die Forderung „wegen Verjährung nach § 13 Nr. 4 VOB/B" zurück.

**I. Vertragsregime.** Der Vertrag ist Bauvertrag iSv § 650a I BGB; B ist Verbraucher (§ 13 BGB), Vertrag damit Verbraucherbauvertrag § 650i BGB.

**II. VOB/B-Einbeziehung.** Die VOB/B ist AGB. Ggü. Verbrauchern entfällt die Privilegierung der „im Ganzen"-Einbeziehung (BGH, Urt. v. 24.07.2008 – VII ZR 55/07 (https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=24.07.2008&Aktenzeichen=VII+ZR+55/07)). § 13 Nr. 4 VOB/B (4 Jahre statt 5 Jahre) ist nach § 307 BGB zu prüfen und stellt eine unangemessene Verkürzung gegenüber dem dispositiven Recht (§ 634a I Nr. 2 BGB) dar – unwirksam.

**III. Verjährung.** Maßgeblich daher § 634a I Nr. 2 BGB: 5 Jahre ab Abnahme. Abnahme 14.03.2021 → Verjährungseintritt 14.03.2026. Die Mängelrüge im Februar 2026 liegt vor Verjährungseintritt. Empfehlung: sofortige verjährungshemmende Maßnahme (§ 203 BGB Verhandlungen / § 204 I Nr. 1 BGB Klage).

**IV. Mängelrechte § 634 BGB.** Vorrangig Nacherfüllung mit angemessener Frist (§§ 634 Nr. 1, 635). Erst danach Selbstvornahme / Rücktritt / Minderung / Schadensersatz.

## Risiken / typische Fehler

- **VOB/B-Privilegierung pauschal annehmen** ohne Einbeziehungs- und AGB-Test → falsche Verjährung, falsche Vergütungsmodalitäten.
- **Mängelrüge ohne Fristsetzung** → keine Selbstvornahme, kein Rücktritt, kein Schadensersatz statt der Leistung.
- **Verjährung verkennen**: § 634a I Nr. 1 (2 Jahre, nicht-Bauwerk) statt Nr. 2 (5 Jahre, Bauwerk) – häufig bei Sanierungs- und Wartungsverträgen.
- **Abnahme als reine Formalie behandeln** – sie löst Beweislastumkehr, Vergütungsfälligkeit und Verjährungsbeginn aus.
- **Architektenhaftung übersehen**: § 650s BGB – gesamtschuldnerische Haftung ausführender Unternehmer und Architekt bei Überwachungsmängeln.
- **Bauhandwerkersicherheit § 650f BGB** ausblenden, obwohl Auftragnehmer mandatiert.
