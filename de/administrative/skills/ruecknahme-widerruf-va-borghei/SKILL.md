---
name: ruecknahme-widerruf-va-borghei
title: /verwaltungsrecht:ruecknahme-widerruf-va
description: 'Aufhebung bestandskräftiger Verwaltungsakte durch die Behörde: Rücknahme rechtswidriger VA § 48 VwVfG (Vertrauensschutz, Jahresfrist) und Widerruf rechtmäßiger VA § 49 VwVfG. Use when eine Behörde einen bereits erlassenen Verwaltungsakt aufheben will und die Bestandskraft durchbrochen werden soll.'
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/verwaltungsrecht/skills/ruecknahme-widerruf-va
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: administrative
language: de
---

# /verwaltungsrecht:ruecknahme-widerruf-va

## Zweck

§§ 48, 49 VwVfG erlauben der Behörde, einen bereits erlassenen Verwaltungsakt nachträglich aufzuheben und damit dessen Bestandskraft zu durchbrechen. Die Weichenstellung lautet: rechtswidriger VA → Rücknahme (§ 48 VwVfG), rechtmäßiger VA → Widerruf (§ 49 VwVfG). Bei begünstigenden VA schützen Vertrauensschutz und Fristen den Adressaten. Die Skill ordnet den Fall ein und prüft Voraussetzungen, Vertrauensschutz und Fristen.

## Eingaben

- Aufzuhebender Verwaltungsakt (Inhalt, Datum, Adressat)
- Rechtmäßig oder rechtswidrig? (Fehler bei Erlass?)
- Begünstigend oder belastend? (Geldleistung / teilbare Sachleistung?)
- Vertrauensbetätigung des Adressaten (Verbrauch, Vermögensdisposition?)
- Kenntnis der Behörde von den Aufhebungsgründen (seit wann?)
- Wirkung der Aufhebung (für die Zukunft / Vergangenheit?)

## Sub-Agent-Architektur

Drei gedankliche Rollen wirken zusammen. Ein Einordnungs-Prüfer bestimmt, ob der VA rechtswidrig (§ 48 VwVfG) oder rechtmäßig (§ 49 VwVfG) und ob er begünstigend oder belastend ist, und wählt die einschlägige Norm. Ein Voraussetzungs-Prüfer arbeitet Tatbestand, Vertrauensschutz, Ermessen, Fristen und etwaige Erstattungs-/Entschädigungsfolgen ab. Ein Verifizierer kontrolliert jede Norm gegen gesetze-im-internet.de und jede Entscheidung gegen das reale Aktenzeichen; Unbestätigtes wird mit `[unverifiziert - prüfen]` markiert oder weggelassen. Kein erfundenes Aktenzeichen.

## Ablauf

### 1. Weichenstellung: Rechtmäßigkeit des VA

- Rechtswidriger VA → Rücknahme nach [§ 48 VwVfG](https://www.gesetze-im-internet.de/vwvfg/__48.html)
- Rechtmäßiger VA → Widerruf nach [§ 49 VwVfG](https://www.gesetze-im-internet.de/vwvfg/__49.html)

### 2. Begünstigend oder belastend?

Begünstigend ist ein VA, der ein Recht oder einen rechtlich erheblichen Vorteil begründet oder bestätigt (§ 48 Abs. 1 S. 2 VwVfG). Für die Aufhebung begünstigender VA gelten erhöhte Anforderungen; belastende VA können freier aufgehoben werden.

### 3. Rücknahme rechtswidriger VA ([§ 48 VwVfG](https://www.gesetze-im-internet.de/vwvfg/__48.html))

- **Belastender rechtswidriger VA**: Rücknahme nach § 48 Abs. 1 S. 1 VwVfG grundsätzlich ohne Vertrauensschutz möglich (Ermessen).
- **Begünstigender rechtswidriger VA**: § 48 Abs. 1 S. 2, Abs. 2–4 VwVfG.
  - Bei Geldleistungen / teilbaren Sachleistungen (§ 48 Abs. 2 VwVfG): Rücknahme ausgeschlossen, soweit der Begünstigte auf den Bestand vertraut hat und sein Vertrauen schutzwürdig ist (Vermögensdisposition, Verbrauch). Kein Vertrauensschutz bei Arglist, Täuschung, Drohung oder Kenntnis der Rechtswidrigkeit (§ 48 Abs. 2 S. 3 VwVfG).
  - Sonstige begünstigende VA (§ 48 Abs. 3 VwVfG): Bestand bleibt, aber Vermögensnachteil ist auszugleichen.

### 4. Vertrauensschutz ([§ 48 VwVfG](https://www.gesetze-im-internet.de/vwvfg/__48.html))

Abwägung des Vertrauens des Begünstigten gegen das öffentliche Interesse an der Rücknahme (§ 48 Abs. 2 VwVfG). Schutzwürdig ist das Vertrauen regelmäßig, wenn der Begünstigte Leistungen verbraucht oder eine nicht mehr rückgängig zu machende Vermögensdisposition getroffen hat.

### 5. Jahresfrist ([§ 48 VwVfG](https://www.gesetze-im-internet.de/vwvfg/__48.html))

Nach § 48 Abs. 4 VwVfG ist die Rücknahme nur innerhalb eines Jahres ab Kenntnis der Behörde von den die Rücknahme rechtfertigenden Tatsachen zulässig (Entscheidungsfrist, nicht Bearbeitungsfrist).

### 6. Widerruf rechtmäßiger VA ([§ 49 VwVfG](https://www.gesetze-im-internet.de/vwvfg/__49.html))

- **Belastender rechtmäßiger VA**: Widerruf nach § 49 Abs. 1 VwVfG grundsätzlich möglich.
- **Begünstigender rechtmäßiger VA**: Widerruf nur unter den engen Voraussetzungen des § 49 Abs. 2 VwVfG (z.B. Widerrufsvorbehalt, Auflagenverstoß, nachträgliche Tatsachen- oder Rechtsänderung, schwere Nachteile für das Gemeinwohl). Vertrauensschutz über Entschädigung nach § 49 Abs. 6 VwVfG. Auch hier gilt die Jahresfrist (§ 49 Abs. 2 S. 2 i.V.m. § 48 Abs. 4 VwVfG).

### 7. Ermessen und Folgen

Sowohl Rücknahme als auch Widerruf stehen im pflichtgemäßen Ermessen (§ 40 VwVfG). Bei Aufhebung eines Leistungsbescheids für die Vergangenheit: Erstattung nach § 49a VwVfG.

## Risiken

- **Falsche Norm gewählt** — Rücknahme (§ 48 VwVfG) setzt Rechtswidrigkeit voraus, Widerruf (§ 49 VwVfG) Rechtmäßigkeit des VA.
- **Vertrauensschutz übergangen** — bei begünstigenden VA sperrt schutzwürdiges Vertrauen die Rücknahme (§ 48 Abs. 2 VwVfG).
- **Jahresfrist versäumt** — nach Ablauf der Jahresfrist des § 48 Abs. 4 VwVfG ist die Aufhebung unzulässig.
- **Ermessen nicht ausgeübt** — fehlende oder fehlerhafte Ermessensausübung macht die Aufhebung rechtswidrig.
- **Erstattungsfolge übersehen** — § 49a VwVfG und etwaige Entschädigung nach § 49 Abs. 6 VwVfG beachten.
- **Aktenzeichen erfunden** — jede Entscheidung verifizieren oder als `[unverifiziert - prüfen]` kennzeichnen.

## Ausgabeformat

```
RÜCKNAHME / WIDERRUF — <VA> — <Datum>

I.   Verwaltungsakt
     Inhalt / Adressat:           <…>
     Rechtmäßig:                  [nein → § 48 / ja → § 49]
     Begünstigend:                [ja / nein]

II.  Einschlägige Norm
     [§ 48 VwVfG Rücknahme / § 49 VwVfG Widerruf]

III. Voraussetzungen
     Tatbestand:                  <…>
     Vertrauensschutz (§ 48 II):  [schutzwürdig / kein Vertrauen]
     Ausschlussgründe:            [Täuschung / Kenntnis / N/A]

IV.  Fristen / Ermessen
     Jahresfrist (§ 48 IV):       [gewahrt bis <Datum> / versäumt]
     Ermessen:                    <Abwägung>
     Erstattung (§ 49a):          [ja / nein]

Ergebnis: <Zulässigkeit der Aufhebung>
Empfehlung: <…>
```
