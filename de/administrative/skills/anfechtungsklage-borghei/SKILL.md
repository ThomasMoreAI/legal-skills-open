---
name: anfechtungsklage-borghei
title: /verwaltungsrecht:anfechtungsklage
description: Anfechtungsklage gegen rechtswidrige belastende Verwaltungsakte. Klagebefugnis § 42 VwGO, Vorverfahren § 68 VwGO, Klagefrist § 74 VwGO, Aufhebung § 113 VwGO. Use when ein Mandant einen belastenden Verwaltungsakt aufheben lassen will und in eigenen Rechten verletzt ist.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/verwaltungsrecht/skills/anfechtungsklage
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: administrative
language: de
---

# /verwaltungsrecht:anfechtungsklage

## Zweck

Die Anfechtungsklage ist die zentrale Gestaltungsklage gegen einen belastenden Verwaltungsakt. Ziel ist dessen Aufhebung. Die Skill prüft Zulässigkeit und Begründetheit strukturiert und sichert die fristgebundenen Zugangsvoraussetzungen, deren Versäumung den Rechtsschutz endgültig abschneidet.

## Eingaben

- Verwaltungsakt (Behörde, Datum, Inhalt, Tenor der Belastung)
- Rechtsbehelfsbelehrung (vorhanden / korrekt?)
- Bekanntgabe-/Zustelldatum und -art
- Widerspruchsverfahren (durchgeführt? Widerspruchsbescheid mit Datum?)
- Geltend gemachte Rechtsverletzung (Eigentum, Berufsfreiheit, Gleichbehandlung …)
- Eilbedürftigkeit (sofortige Vollziehung angeordnet?)

## Sub-Agent-Architektur

Die Bearbeitung verteilt sich auf drei gedankliche Rollen, die nacheinander durchlaufen werden. Ein Zulässigkeits-Prüfer arbeitet Statthaftigkeit, Klagebefugnis, Vorverfahren und Frist ab und stoppt bei jedem K.-o.-Kriterium. Ein Begründetheits-Prüfer untersucht Ermächtigungsgrundlage, formelle und materielle Rechtmäßigkeit des VA sowie die Rechtsverletzung des Klägers. Ein Verifizierer kontrolliert jede zitierte Norm gegen gesetze-im-internet.de und jede Entscheidung gegen das tatsächliche Aktenzeichen; nicht bestätigte Fundstellen werden mit `[unverifiziert - prüfen]` markiert oder weggelassen. Keine Rolle erfindet Aktenzeichen.

## Ablauf

### 1. Statthaftigkeit ([§ 42 VwGO](https://www.gesetze-im-internet.de/vwgo/__42.html))

Die Anfechtungsklage (§ 42 Abs. 1 Alt. 1 VwGO) ist statthaft, wenn ein Verwaltungsakt (§ 35 VwVfG) aufgehoben werden soll. Abgrenzung zur Verpflichtungsklage (Begehren auf Erlass) und zur Fortsetzungsfeststellungsklage (VA hat sich erledigt, § 113 Abs. 1 S. 4 VwGO).

### 2. Klagebefugnis ([§ 42 VwGO](https://www.gesetze-im-internet.de/vwgo/__42.html))

§ 42 Abs. 2 VwGO verlangt die Geltendmachung einer eigenen Rechtsverletzung. Beim Adressaten eines belastenden VA folgt sie regelmäßig aus Art. 2 Abs. 1 GG (Adressatentheorie). Bei Drittbetroffenen ist eine drittschützende Norm darzulegen.

### 3. Vorverfahren ([§ 68 VwGO](https://www.gesetze-im-internet.de/vwgo/__68.html))

Vor der Anfechtungsklage ist grundsätzlich ein Widerspruchsverfahren erfolglos durchzuführen. Ausnahmen: § 68 Abs. 1 S. 2 VwGO sowie landesrechtliche Abschaffung. Fehlt das erforderliche Vorverfahren, ist die Klage unzulässig.

### 4. Klagefrist ([§ 74 VwGO](https://www.gesetze-im-internet.de/vwgo/__74.html))

Ein Monat ab Zustellung des Widerspruchsbescheids (§ 74 Abs. 1 S. 1 VwGO); ist kein Vorverfahren nötig, ab Bekanntgabe des VA. Bei fehlender oder unrichtiger Rechtsbehelfsbelehrung gilt die Jahresfrist (§ 58 Abs. 2 VwGO). Versäumnis: Wiedereinsetzung § 60 VwGO prüfen.

### 5. Allgemeine Sachurteilsvoraussetzungen

Verwaltungsrechtsweg (§ 40 VwGO), Beteiligten- und Prozessfähigkeit (§§ 61, 62 VwGO), zuständiges Gericht, Rechtsschutzbedürfnis.

### 6. Begründetheit ([§ 113 VwGO](https://www.gesetze-im-internet.de/vwgo/__113.html))

Maßstab § 113 Abs. 1 S. 1 VwGO: Die Klage ist begründet, soweit der VA rechtswidrig **und** der Kläger dadurch in seinen Rechten verletzt ist.

- **Ermächtigungsgrundlage** vorhanden und wirksam?
- **Formelle Rechtmäßigkeit**: Zuständigkeit, Verfahren (Anhörung § 28 VwVfG), Form/Begründung § 39 VwVfG
- **Materielle Rechtmäßigkeit**: Tatbestand erfüllt, Rechtsfolge fehlerfrei, bei Ermessen § 114 VwGO (Ermessensfehler)
- **Rechtsverletzung**: Verletzung subjektiv-öffentlicher Rechte des Klägers

### 7. Tenor und Vollzugsfolgen

Bei Begründetheit hebt das Gericht den VA und den Widerspruchsbescheid auf (§ 113 Abs. 1 S. 1 VwGO). Bereits vollzogener VA: Vollzugsfolgenbeseitigung nach § 113 Abs. 1 S. 2 VwGO, soweit spruchreif.

### 8. Eilrechtsschutz parallel

Bei sofortiger Vollziehung oder gesetzlichem Ausschluss der aufschiebenden Wirkung Antrag nach § 80 Abs. 5 VwGO gesondert stellen.

## Risiken

- **Klagefrist verpasst** — Bestandskraft tritt ein, Klage unzulässig; ohne Wiedereinsetzung kein Rechtsschutz mehr.
- **Vorverfahren übersprungen** — fehlt ein erforderliches Widerspruchsverfahren, ist die Klage unzulässig.
- **Klagebefugnis fehlt** — bloße Interessenbetroffenheit ohne subjektives Recht genügt nicht (§ 42 Abs. 2 VwGO).
- **Rechtsverletzung nicht geprüft** — ein nur objektiv rechtswidriger VA führt ohne Verletzung eigener Rechte nicht zur Aufhebung (§ 113 Abs. 1 S. 1 VwGO).
- **Erledigung übersehen** — bei erledigtem VA ist auf Fortsetzungsfeststellung umzustellen.
- **Aktenzeichen erfunden** — jede Entscheidung verifizieren oder als `[unverifiziert - prüfen]` kennzeichnen.

## Ausgabeformat

```
ANFECHTUNGSKLAGE — <Mandat> — <Datum>

I.   Streitgegenstand
     Angegriffener VA:        <Behörde / Datum / Inhalt>
     Widerspruchsbescheid:    <Datum / N/A>

II.  Zulässigkeit
     Statthaftigkeit (§ 42):  [✓ Anfechtungsklage]
     Klagebefugnis:           [✓ / fraglich: <…>]
     Vorverfahren (§ 68):     [durchgeführt / entbehrlich / FEHLT]
     Klagefrist (§ 74):       läuft bis <Datum>

III. Begründetheit (§ 113 Abs. 1 S. 1)
     Ermächtigungsgrundlage:  <…>
     Formelle Fehler:         <Anhörung / Zuständigkeit / …>
     Materielle Fehler:       <Tatbestand / Ermessen / …>
     Rechtsverletzung:        [bejaht / verneint]

IV.  Eilrechtsschutz
     § 80 Abs. 5 erforderlich: [ja / nein]

Ergebnis: <Erfolgsaussicht>
Empfehlung: <…>
```
