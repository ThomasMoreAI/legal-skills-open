---
name: einstweilige-anordnung-123-borghei
title: /verwaltungsrecht:einstweilige-anordnung-123
description: Vorläufiger Rechtsschutz außerhalb der Anfechtungssituation durch einstweilige Anordnung § 123 VwGO. Sicherungs- und Regelungsanordnung, Anordnungsanspruch und Anordnungsgrund, Glaubhaftmachung, Abgrenzung zu § 80 VwGO. Use when ein Mandant eine Leistung oder Sicherung im Eilverfahren begehrt und kein Anfechtungsfall vorliegt.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/verwaltungsrecht/skills/einstweilige-anordnung-123
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: administrative
language: de
---

# /verwaltungsrecht:einstweilige-anordnung-123

## Zweck

Die einstweilige Anordnung nach § 123 VwGO ist der vorläufige Rechtsschutz in allen Fällen, die nicht der Anfechtungssituation des § 80 VwGO unterfallen, also vor allem bei Verpflichtungs- und Leistungsbegehren. Sie sichert einen bestehenden Zustand oder regelt vorläufig ein streitiges Rechtsverhältnis. Die Skill grenzt die Anordnungsart ab und prüft Anordnungsanspruch und Anordnungsgrund.

## Eingaben

- Begehren des Antragstellers (Leistung, Sicherung, vorläufige Regelung)
- Art des zugrunde liegenden Hauptsacherechtsbehelfs (Verpflichtungs-/Leistungsklage)
- Drohende Rechtsbeeinträchtigung (Veränderung des Zustands? wesentliche Nachteile?)
- Dringlichkeit und drohender Schaden
- Glaubhaftmachungsmittel (eidesstattliche Versicherung, Urkunden)
- Liegt eine Anfechtungssituation vor? (dann § 80 VwGO)

## Sub-Agent-Architektur

Drei gedankliche Rollen wirken zusammen. Ein Abgrenzungs-Prüfer klärt zunächst, ob § 123 VwGO statthaft ist oder ob die Anfechtungssituation des § 80 VwGO vorliegt, und bestimmt die Anordnungsart (Sicherung oder Regelung). Ein Begründetheits-Prüfer arbeitet Anordnungsanspruch und Anordnungsgrund samt Glaubhaftmachung ab und beachtet das Verbot der Vorwegnahme der Hauptsache. Ein Verifizierer kontrolliert jede Norm gegen gesetze-im-internet.de und jede Entscheidung gegen das reale Aktenzeichen; Unbestätigtes wird mit `[unverifiziert - prüfen]` markiert oder weggelassen. Kein erfundenes Aktenzeichen.

## Ablauf

### 1. Abgrenzung zu § 80 VwGO ([§ 123 VwGO](https://www.gesetze-im-internet.de/vwgo/__123.html))

§ 123 Abs. 5 VwGO: Die einstweilige Anordnung ist nur statthaft, soweit nicht § 80 VwGO einschlägig ist. Faustregel: Geht es um die Abwehr eines belastenden, vollziehbaren VA, gilt [§ 80 VwGO](https://www.gesetze-im-internet.de/vwgo/__80.html); geht es um eine Leistung, Sicherung oder Verpflichtung, gilt § 123 VwGO.

### 2. Anordnungsart ([§ 123 VwGO](https://www.gesetze-im-internet.de/vwgo/__123.html))

- **Sicherungsanordnung** (§ 123 Abs. 1 S. 1 VwGO): Sicherung des bestehenden Zustands, wenn die Gefahr besteht, dass durch eine Veränderung des Status quo die Verwirklichung eines Rechts vereitelt oder wesentlich erschwert wird.
- **Regelungsanordnung** (§ 123 Abs. 1 S. 2 VwGO): vorläufige Regelung eines streitigen Rechtsverhältnisses, vor allem zur Abwendung wesentlicher Nachteile (Erweiterung der Rechtsstellung).

### 3. Zulässigkeit des Antrags

Statthaftigkeit (s.o.), Antragsbefugnis analog § 42 Abs. 2 VwGO, allgemeine Sachentscheidungsvoraussetzungen, zuständiges Gericht (Gericht der Hauptsache).

### 4. Anordnungsanspruch ([§ 123 VwGO](https://www.gesetze-im-internet.de/vwgo/__123.html))

Der Anordnungsanspruch ist der materielle Anspruch, der in der Hauptsache verfolgt wird (z.B. Anspruch auf die begehrte Leistung oder Genehmigung). Er ist nach Maßgabe des § 123 Abs. 3 VwGO i.V.m. §§ 920, 294 ZPO glaubhaft zu machen.

### 5. Anordnungsgrund ([§ 123 VwGO](https://www.gesetze-im-internet.de/vwgo/__123.html))

Der Anordnungsgrund ist die besondere Dringlichkeit: Ohne die einstweilige Anordnung drohen die Vereitelung des Rechts oder wesentliche Nachteile, die ein Zuwarten bis zur Hauptsacheentscheidung unzumutbar machen. Auch er ist glaubhaft zu machen.

### 6. Glaubhaftmachung ([§ 123 VwGO](https://www.gesetze-im-internet.de/vwgo/__123.html))

Nach § 123 Abs. 3 VwGO i.V.m. §§ 920 Abs. 2, 294 ZPO genügt die überwiegende Wahrscheinlichkeit; Mittel ist insbesondere die eidesstattliche Versicherung. Voller Beweis ist nicht erforderlich.

### 7. Verbot der Vorwegnahme der Hauptsache

Die einstweilige Anordnung darf die Hauptsache grundsätzlich nicht vorwegnehmen. Ausnahme nur, wenn der Antragsteller ohne die Vorwegnahme schwere, unzumutbare Nachteile erlitte und ein hoher Erfolgsgrad in der Hauptsache besteht (Gebot effektiven Rechtsschutzes, Art. 19 Abs. 4 GG).

### 8. Entscheidung

Beschluss des Gerichts; Inhalt nach pflichtgemäßem Ermessen (§ 123 Abs. 3 VwGO i.V.m. § 938 ZPO). Vorläufiger Charakter; Aufhebung/Abänderung bei veränderten Umständen.

## Risiken

- **Falsche Verfahrensart** — bei Anfechtungssituation ist § 80 VwGO einschlägig, nicht § 123 VwGO (§ 123 Abs. 5 VwGO).
- **Anordnungsgrund fehlt** — ohne besondere Dringlichkeit bleibt der Antrag erfolglos.
- **Glaubhaftmachung unzureichend** — bloße Behauptung ohne eidesstattliche Versicherung genügt nicht.
- **Vorwegnahme der Hauptsache** — unzulässig, außer bei schweren Nachteilen und hoher Erfolgswahrscheinlichkeit.
- **Anordnungsanspruch nicht dargelegt** — der materielle Hauptsacheanspruch muss schlüssig vorgetragen sein.
- **Aktenzeichen erfunden** — jede Entscheidung verifizieren oder als `[unverifiziert - prüfen]` kennzeichnen.

## Ausgabeformat

```
EINSTWEILIGE ANORDNUNG § 123 VwGO — <Mandat> — <Datum>

I.   Begehren
     Antragsziel:                 <Leistung / Sicherung / Regelung>
     Hauptsache:                  <Verpflichtungs-/Leistungsklage>

II.  Abgrenzung
     § 80 VwGO einschlägig:       [nein → § 123 statthaft / ja → falsche Verfahrensart]
     Anordnungsart:               [Sicherungs- / Regelungsanordnung]

III. Zulässigkeit
     Antragsbefugnis / Zuständigkeit: [✓ / fraglich]

IV.  Begründetheit
     Anordnungsanspruch:          [glaubhaft / fraglich]
     Anordnungsgrund:             [Dringlichkeit bejaht / verneint]
     Glaubhaftmachung:            [eidesstattliche Versicherung / Urkunden]
     Vorwegnahme der Hauptsache:  [keine / ausnahmsweise zulässig]

Ergebnis: <Erfolgsaussicht>
Empfehlung: <…>
```
