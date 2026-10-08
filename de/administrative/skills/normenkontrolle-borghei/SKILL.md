---
name: normenkontrolle-borghei
title: /verwaltungsrecht:normenkontrolle
description: 'Prüfung des prinzipalen Normenkontrollantrags nach § 47 VwGO vor dem Oberverwaltungsgericht gegen untergesetzliche Normen (insbesondere Bebauungspläne und Satzungen): Statthaftigkeit, Antragsbefugnis und Antragsfrist von einem Jahr. Use when ein untergesetzliches Regelwerk wie ein Bebauungsplan oder eine kommunale Satzung unmittelbar angegriffen werden soll.'
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/verwaltungsrecht/skills/normenkontrolle
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: administrative
language: de
---

# /verwaltungsrecht:normenkontrolle

## Zweck

Die prinzipale Normenkontrolle nach [§ 47 VwGO](https://www.gesetze-im-internet.de/vwgo/__47.html) erlaubt es, eine untergesetzliche Rechtsnorm – vor allem einen Bebauungsplan oder eine kommunale Satzung – unmittelbar und mit Wirkung für jedermann (inter omnes) vom Oberverwaltungsgericht überprüfen zu lassen. Diese Skill prüft die Zulässigkeit des Antrags, insbesondere die Statthaftigkeit gegen die richtige Normart, die Antragsbefugnis und die einjährige Antragsfrist, und ordnet die Begründetheitsfragen ein.

## Eingaben

- Angegriffene Norm (Bebauungsplan, Satzung, Rechtsverordnung)
- Bekanntmachungsdatum der Norm
- Betroffenheit des Antragstellers (Eigentum, Nutzung, Nachbarstellung)
- Geltend gemachter Rechtsverstoß (Verfahrens-, Abwägungs-, materieller Fehler)
- Landesrecht zur Zuständigkeit nach § 47 Abs. 1 Nr. 2 VwGO

## Sub-Agent-Architektur

Drei Prüfstränge arbeiten in Prosa. Der **Statthaftigkeits-Agent** ordnet die angegriffene Norm § 47 Abs. 1 Nr. 1 VwGO (Satzungen nach BauGB, insbesondere Bebauungsplan) oder Nr. 2 (sonstige im Rang unter dem Landesgesetz stehende Rechtsvorschriften, soweit das Landesrecht es bestimmt) zu. Der **Antragsbefugnis-Agent** prüft die Möglichkeit einer Rechtsverletzung nach § 47 Abs. 2 Satz 1 VwGO, insbesondere bei mittelbar Planbetroffenen das abwägungserhebliche private Interesse. Der **Fristen-Agent** kontrolliert die einjährige Ausschlussfrist ab Bekanntmachung. Die Stränge werden zu einer Zulässigkeitsbewertung und einer Einschätzung der Begründetheit verdichtet.

## Ablauf

### 1. Statthaftigkeit ([§ 47 Abs. 1 VwGO](https://www.gesetze-im-internet.de/vwgo/__47.html))

- **Nr. 1**: Satzungen nach dem Baugesetzbuch (insbesondere **Bebauungsplan**) und Rechtsverordnungen aufgrund des § 246 Abs. 2 BauGB
- **Nr. 2**: andere im Rang unter dem Landesgesetz stehende Rechtsvorschriften, **soweit das Landesrecht** dies bestimmt (nicht alle Länder eröffnen den Weg)
- Zuständig ist das **Oberverwaltungsgericht** (in einigen Ländern Verwaltungsgerichtshof)

### 2. Antragsbefugnis ([§ 47 Abs. 2 Satz 1 VwGO](https://www.gesetze-im-internet.de/vwgo/__47.html))

Antragsbefugt ist, wer geltend macht, durch die Rechtsvorschrift oder ihre Anwendung in eigenen Rechten verletzt zu sein oder in absehbarer Zeit verletzt zu werden, sowie jede Behörde.

- **Plangebiet-Eigentümer**: regelmäßig antragsbefugt (Art. 14 GG)
- **Mittelbar Betroffene**: Antragsbefugnis, wenn ein abwägungserhebliches privates Interesse besteht, das die Gemeinde bei der Abwägung (§ 1 Abs. 7 BauGB) hätte berücksichtigen müssen

### 3. Antragsfrist – ein Jahr ([§ 47 Abs. 2 Satz 1 VwGO](https://www.gesetze-im-internet.de/vwgo/__47.html))

- Der Antrag ist **innerhalb eines Jahres** nach Bekanntmachung der Rechtsvorschrift zu stellen
- Es handelt sich um eine **Ausschlussfrist**; Wiedereinsetzung nach § 60 VwGO ist nach h. M. nicht möglich
- Fristbeginn ist die ortsübliche Bekanntmachung des (Satzungs-)Beschlusses

### 4. Weitere Zulässigkeit

- **Antragsgegner**: die Körperschaft, die die Norm erlassen hat (§ 47 Abs. 2 Satz 2 VwGO)
- **Rechtsschutzbedürfnis**: entfällt, wenn die Unwirksamkeit dem Antragsteller keinen rechtlichen Vorteil bringt
- **Einstweilige Anordnung** nach § 47 Abs. 6 VwGO bei dringenden Gründen

### 5. Begründetheit

Der Antrag ist begründet, wenn die Norm gegen höherrangiges Recht verstößt:

- **Formelle Fehler**: Zuständigkeit, Verfahren (Auslegung, Beteiligung), Form
- **Abwägungsfehler** (§ 1 Abs. 7 BauGB): Abwägungsausfall, -defizit, -fehlgewichtung, -disproportionalität
- **Materielle Fehler**: Verstoß gegen BauGB, BauNVO, Fachrecht
- Rechtsfolge: Unwirksamkeitserklärung mit allgemeinverbindlicher Wirkung (§ 47 Abs. 5 Satz 2 VwGO)

## Quellen

### Statute

- [§ 47 VwGO](https://www.gesetze-im-internet.de/vwgo/__47.html) (Normenkontrolle; Abs. 2: Antragsbefugnis und Jahresfrist)
- [§ 1 Abs. 7 BauGB](https://www.gesetze-im-internet.de/bbaug/__1.html) (Abwägungsgebot)
- [§ 10 BauGB](https://www.gesetze-im-internet.de/bbaug/__10.html) (Bebauungsplan als Satzung)
- [Art. 14 GG](https://www.gesetze-im-internet.de/gg/art_14.html) (Eigentum)

### Kommentare

- Kopp / Schenke, VwGO, 30. Aufl. 2024, § 47
- Schoch / Schneider, VwGO (Loseblatt), § 47
- Battis / Krautzberger / Löhr, BauGB, 15. Aufl.

### Rechtsprechung

- BVerwG, Urt. v. 24.09.1998 – 4 CN 2.98 (Antragsbefugnis, abwägungserheblicher Belang) `[unverifiziert – prüfen]`
- BVerwG, Urt. v. 30.04.2004 – 4 CN 1.03 (Antragsfrist) `[unverifiziert – prüfen]`

## Ausgabeformat

```
NORMENKONTROLLE § 47 VwGO — <Mandat> — <Datum>

I.    Angegriffene Norm
      Art:                            [Bebauungsplan / Satzung / RVO]
      Bekanntmachung:                 <Datum>
      Gericht:                        OVG / VGH <Land>

II.   Statthaftigkeit
      § 47 Abs. 1 Nr. 1 / Nr. 2:      <…>
      Landesrechtliche Eröffnung:     [erforderlich? ja/nein]

III.  Antragsbefugnis § 47 Abs. 2 VwGO
      Eigentum / mittelbare Betroffenheit:  <…>
      Abwägungserheblicher Belang:    [+ / –]

IV.   Antragsfrist
      Ein-Jahres-Frist:               läuft bis <Datum>
      Ausschlussfrist gewahrt:        [ja / nein]

V.    Begründetheit
      Formelle / Abwägungs- / materielle Fehler:  <…>

Empfehlung: <…>
```

## Risiken / typische Fehler

- **Antragsfrist von einem Jahr versäumt** — die Ausschlussfrist nach § 47 Abs. 2 VwGO lässt keine Wiedereinsetzung zu; danach ist nur noch Inzidentkontrolle möglich.
- **Antragsbefugnis bei mittelbar Betroffenen überschätzt** — ohne abwägungserheblichen eigenen Belang fehlt sie.
- **Statthaftigkeit nach Nr. 2 ohne Landesrechtsprüfung bejaht** — § 47 Abs. 1 Nr. 2 VwGO greift nur, soweit das Landesrecht es bestimmt.
- **Falscher Antragsgegner** — Antragsgegner ist die normerlassende Körperschaft, nicht die Genehmigungsbehörde.
