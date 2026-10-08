---
name: fortsetzungsfeststellungsklage-borghei
title: /verwaltungsrecht:fortsetzungsfeststellungsklage
description: 'Prüfung der Fortsetzungsfeststellungsklage nach § 113 Abs. 1 Satz 4 VwGO bei erledigtem Verwaltungsakt: Erledigung, Fortsetzungsfeststellungsinteresse (Wiederholungsgefahr, Rehabilitierung, Präjudizinteresse) und analoge Anwendung. Use when sich ein angegriffener Verwaltungsakt vor oder während des Prozesses erledigt hat und der Mandant dessen Rechtswidrigkeit feststellen lassen will.'
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/verwaltungsrecht/skills/fortsetzungsfeststellungsklage
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: administrative
language: de
---

# /verwaltungsrecht:fortsetzungsfeststellungsklage

## Zweck

Erledigt sich ein Verwaltungsakt (Zeitablauf, Vollzug, Aufhebung), wird die Anfechtungsklage unzulässig, weil ihr das Rechtsschutzbedürfnis fehlt. Die Fortsetzungsfeststellungsklage nach [§ 113 Abs. 1 Satz 4 VwGO](https://www.gesetze-im-internet.de/vwgo/__113.html) erlaubt es, die Rechtswidrigkeit des erledigten VA gleichwohl gerichtlich feststellen zu lassen. Diese Skill prüft die besondere Sachurteilsvoraussetzung des berechtigten Feststellungsinteresses und ordnet die Fallkonstellation der direkten oder analogen Anwendung zu.

## Eingaben

- Ursprünglicher Verwaltungsakt (Inhalt, Belastung)
- Erledigungsereignis und -zeitpunkt (vor/nach Klageerhebung)
- Bisheriger Verfahrensstand (Widerspruch, Klage anhängig?)
- Interesse des Mandanten an der Feststellung (Schaden, Ruf, Wiederholung)
- Drohende künftige gleichartige Maßnahmen

## Sub-Agent-Architektur

Drei Prüfstränge wirken in Prosa zusammen. Der **Erledigungs-Agent** klärt, ob und wann sich der VA im Sinne des [§ 43 Abs. 2 VwVfG](https://www.gesetze-im-internet.de/vwvfg/__43.html) erledigt hat und ob die direkte (Erledigung nach Klageerhebung) oder die analoge Anwendung (Erledigung vor Klageerhebung, Verpflichtungssituation) einschlägig ist. Der **Interessen-Agent** prüft das Fortsetzungsfeststellungsinteresse anhand der vier anerkannten Fallgruppen Wiederholungsgefahr, Rehabilitierung, Präjudizinteresse und schwerwiegender Grundrechtseingriff. Der **Zulässigkeits-Agent** ordnet die übrigen Sachurteilsvoraussetzungen (Klagebefugnis, Frist, Vorverfahren) ein. Die Befunde werden zu einer Zulässigkeitsbewertung zusammengeführt.

## Ablauf

### 1. Erledigung des Verwaltungsakts ([§ 43 Abs. 2 VwVfG](https://www.gesetze-im-internet.de/vwvfg/__43.html))

Erledigung liegt vor, wenn der VA keine Regelungswirkung mehr entfaltet:

- **Zeitablauf** (befristete Maßnahme, Versammlungsverbot für einen Tag)
- **Vollzug** (Wegnahme einer Sache, Abschluss einer Durchsuchung)
- **Aufhebung / Rücknahme** durch die Behörde
- **anderweitige Erledigung** (Wegfall des Regelungsobjekts)

### 2. Direkte vs. analoge Anwendung ([§ 113 Abs. 1 Satz 4 VwGO](https://www.gesetze-im-internet.de/vwgo/__113.html))

- **Direkt**: Erledigung **nach** Klageerhebung in der Anfechtungssituation
- **Analog**: Erledigung **vor** Klageerhebung sowie in der Verpflichtungssituation (abgelehnter begünstigender VA, der sich erledigt)

### 3. Fortsetzungsfeststellungsinteresse

Berechtigtes Interesse an der Feststellung der Rechtswidrigkeit; anerkannte Fallgruppen:

- **Wiederholungsgefahr**: konkrete Gefahr, dass die Behörde unter im Wesentlichen unveränderten Umständen erneut so handelt
- **Rehabilitierung**: fortwirkende diskriminierende Wirkung, Beeinträchtigung des Ansehens (z. B. ehrenrührige Vorwürfe)
- **Präjudizinteresse**: Vorbereitung eines Amtshaftungs- oder Entschädigungsprozesses (nur wenn der Zivilprozess nicht offensichtlich aussichtslos und nicht ohnehin beim Zivilgericht zu klären ist)
- **Schwerwiegender Grundrechtseingriff**: tiefgreifender, sich typischerweise kurzfristig erledigender Eingriff (Art. 19 Abs. 4 GG, effektiver Rechtsschutz)

### 4. Übrige Sachurteilsvoraussetzungen

- **Klagebefugnis** analog § 42 Abs. 2 VwGO
- **Frist**: bei Erledigung nach Klageerhebung wahrt die fristgerechte Anfechtungsklage die Frist; bei Erledigung vor Klageerhebung ist die Klagefrist umstritten (h. M.: keine Bindung an § 74 VwGO, aber Verwirkung möglich)
- **Vorverfahren**: bei Erledigung vor Abschluss entbehrlich, soweit es seinen Zweck nicht mehr erfüllen kann

### 5. Begründetheit

Die Klage ist begründet, wenn der erledigte VA rechtswidrig war und den Kläger in seinen Rechten verletzte (Maßstab wie bei der Anfechtungsklage, bezogen auf den Zeitpunkt vor Erledigung).

## Quellen

### Statute

- [§ 113 Abs. 1 Satz 4 VwGO](https://www.gesetze-im-internet.de/vwgo/__113.html) (Fortsetzungsfeststellungsklage)
- [§ 42 VwGO](https://www.gesetze-im-internet.de/vwgo/__42.html) (Klagebefugnis, analog)
- [§ 43 Abs. 2 VwVfG](https://www.gesetze-im-internet.de/vwvfg/__43.html) (Wirksamkeit / Erledigung)
- [Art. 19 Abs. 4 GG](https://www.gesetze-im-internet.de/gg/art_19.html) (effektiver Rechtsschutz)

### Kommentare

- Kopp / Schenke, VwGO, 30. Aufl. 2024, § 113
- Schoch / Schneider, VwGO (Loseblatt), § 113
- Hufen, Verwaltungsprozessrecht, 12. Aufl.

### Rechtsprechung

- BVerwG, Urt. v. 16.05.2013 – 8 C 14.12 (Rehabilitierungsinteresse) `[unverifiziert – prüfen]`
- BVerfG, Beschl. v. 03.03.2004 – 1 BvR 461/03 (tiefgreifender Grundrechtseingriff) `[unverifiziert – prüfen]`

## Ausgabeformat

```
FORTSETZUNGSFESTSTELLUNGSKLAGE — <Mandat> — <Datum>

I.    Erledigung
      Ereignis / Zeitpunkt:           <Zeitablauf / Vollzug / …>  /  <Datum>
      Vor / nach Klageerhebung:       <…>

II.   Statthaftigkeit § 113 Abs. 1 Satz 4 VwGO
      Direkt / analog:                <…>

III.  Fortsetzungsfeststellungsinteresse
      Wiederholungsgefahr:            [+ / –]
      Rehabilitierung:                [+ / –]
      Präjudizinteresse:              [+ / –]
      Schwerwiegender Grundrechtseingriff: [+ / –]

IV.   Übrige Zulässigkeit
      Klagebefugnis / Frist / Vorverfahren:  <…>

V.    Begründetheit
      VA war rechtswidrig:            [+ / –]

Empfehlung: <…>
```

## Risiken / typische Fehler

- **Feststellungsinteresse fehlt** — ohne berechtigtes Interesse ist die Klage unzulässig; keine der vier Fallgruppen darf ungeprüft bleiben.
- **Präjudizinteresse zu Unrecht bejaht** — bei bereits anhängigem oder offensichtlich aussichtslosem Amtshaftungsprozess entfällt es.
- **Erledigung vor Klageerhebung mit direkter Anwendung behandelt** — dann ist § 113 Abs. 1 Satz 4 VwGO nur analog anwendbar.
- **Klagefrist falsch beurteilt** — bei Erledigung vor Klageerhebung droht Verwirkung; die Maßnahme nicht unbegrenzt aufschieben.
