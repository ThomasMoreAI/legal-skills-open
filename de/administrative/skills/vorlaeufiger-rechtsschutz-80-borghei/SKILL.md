---
name: vorlaeufiger-rechtsschutz-80-borghei
title: 'Vorlaeufiger rechtsschutz 80'
description: Vorläufiger Rechtsschutz gegen Verwaltungsakte nach § 80 VwGO. Aufschiebende Wirkung und ihre Ausnahmen (Abs. 2), Anordnung/Wiederherstellung durch das Gericht (Abs. 5), Drittbetroffene § 80a VwGO. Use when ein belastender VA sofort vollziehbar ist und der Suspensiveffekt gesichert oder hergestellt werden soll.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/verwaltungsrecht/skills/vorlaeufiger-rechtsschutz-80
license: Apache-2.0
version: 0.1.1
execution_mode: open
jurisdiction: de
practice: administrative
language: de
---

# /verwaltungsrecht:vorlaeufiger-rechtsschutz-80

## Zweck

Der vorläufige Rechtsschutz nach § 80 VwGO sichert oder stellt die aufschiebende Wirkung von Widerspruch und Anfechtungsklage her, wenn ein belastender Verwaltungsakt sofort vollzogen werden soll. Er verhindert vollendete Tatsachen, bevor über die Hauptsache entschieden ist. Die Skill ordnet den Fall in die richtige Fallgruppe ein und formuliert den passenden Eilantrag.

## Eingaben

- Belastender Verwaltungsakt (Behörde, Inhalt, Datum)
- Sofortige Vollziehung angeordnet? (Begründung nach § 80 Abs. 3 VwGO vorhanden?)
- Art des VA (Abgabenbescheid, Polizeiverfügung, sonstiger VA)
- Stand des Rechtsbehelfs (Widerspruch/Klage erhoben?)
- Drei-Personen-Verhältnis (begünstigter Dritter betroffen?)
- Dringlichkeit / drohender Vollzug

## Sub-Agent-Architektur

Drei gedankliche Rollen wirken zusammen. Ein Einordnungs-Prüfer bestimmt, ob die aufschiebende Wirkung kraft Gesetzes entfällt (§ 80 Abs. 2 VwGO) oder durch behördliche Anordnung der sofortigen Vollziehung beseitigt wurde, und wählt danach Anordnung oder Wiederherstellung. Ein Abwägungs-Prüfer arbeitet die formelle Rechtmäßigkeit der Vollziehungsanordnung und die Interessenabwägung anhand der Erfolgsaussichten in der Hauptsache ab. Ein Verifizierer kontrolliert jede Norm gegen gesetze-im-internet.de und jede Entscheidung gegen das reale Aktenzeichen; Unbestätigtes wird mit `[unverifiziert - prüfen]` markiert oder weggelassen. Kein erfundenes Aktenzeichen.

## Ablauf

### 1. Grundsatz aufschiebende Wirkung ([§ 80 VwGO](https://www.gesetze-im-internet.de/vwgo/__80.html))

Widerspruch und Anfechtungsklage haben nach § 80 Abs. 1 VwGO grundsätzlich aufschiebende Wirkung (Suspensiveffekt). Der VA darf bis zur Bestandskraft nicht vollzogen werden.

### 2. Ausnahmen vom Suspensiveffekt ([§ 80 VwGO](https://www.gesetze-im-internet.de/vwgo/__80.html))

Die aufschiebende Wirkung entfällt nach § 80 Abs. 2 VwGO bei:

- Anforderung öffentlicher Abgaben und Kosten (Nr. 1)
- unaufschiebbaren Anordnungen und Maßnahmen von Polizeivollzugsbeamten (Nr. 2)
- bundes- oder landesgesetzlich angeordneten Fällen (Nr. 3, Nr. 3a)
- behördlich angeordneter sofortiger Vollziehung (Nr. 4)

Die Anordnung der sofortigen Vollziehung ist nach § 80 Abs. 3 VwGO schriftlich besonders zu begründen.

### 3. Statthafter Antrag ([§ 80 VwGO](https://www.gesetze-im-internet.de/vwgo/__80.html))

- **Anordnung der aufschiebenden Wirkung** (§ 80 Abs. 5 S. 1 Alt. 1 VwGO) in den Fällen des Abs. 2 S. 1 Nr. 1–3a (gesetzlicher Ausschluss)
- **Wiederherstellung der aufschiebenden Wirkung** (§ 80 Abs. 5 S. 1 Alt. 2 VwGO) im Fall des Abs. 2 S. 1 Nr. 4 (behördliche Anordnung)
- Vorrangig: behördlicher Aussetzungsantrag nach § 80 Abs. 4 VwGO

Der gerichtliche Eilantrag stützt sich damit stets auf § 80 Abs. 5 VwGO.

### 4. Zulässigkeit des Eilantrags

Statthaftigkeit (s.o.), Antragsbefugnis analog § 42 Abs. 2 VwGO, Rechtsschutzbedürfnis (Hauptsacherechtsbehelf erhoben oder noch möglich), zuständiges Gericht.

### 5. Begründetheit / Interessenabwägung ([§ 80 VwGO](https://www.gesetze-im-internet.de/vwgo/__80.html))

- Bei Wiederherstellung: formelle Rechtmäßigkeit der Vollziehungsanordnung (§ 80 Abs. 3 VwGO).
- Eigene Interessenabwägung des Gerichts: Aussetzungsinteresse des Antragstellers gegen das Vollzugsinteresse.
- Maßgeblich sind die summarisch geprüften Erfolgsaussichten in der Hauptsache: Ist der VA offensichtlich rechtswidrig, überwiegt das Aussetzungsinteresse; ist er offensichtlich rechtmäßig, überwiegt das Vollzugsinteresse.

### 6. Drittbetroffene ([§ 80a VwGO](https://www.gesetze-im-internet.de/vwgo/__80a.html))

Im Drei-Personen-Verhältnis (VA mit Doppelwirkung, z.B. Baugenehmigung zugunsten des Nachbarn) regelt § 80a VwGO den vorläufigen Rechtsschutz: Das Gericht kann auf Antrag des Drittbetroffenen die aufschiebende Wirkung anordnen oder Maßnahmen treffen. Maßgeblich ist die drittschützende Norm.

### 7. Entscheidung und Folgen

Beschluss des Gerichts; bei Erfolg darf der VA bis zur Hauptsacheentscheidung nicht vollzogen werden. Abänderung nach § 80 Abs. 7 VwGO bei veränderten Umständen möglich.

## Risiken

- **Sofortige Vollziehung übersehen** — der Suspensiveffekt fehlt, vollendete Tatsachen drohen ohne Eilantrag.
- **Falscher Antrag** — Anordnung statt Wiederherstellung (oder umgekehrt) je nach Fallgruppe des § 80 Abs. 2 VwGO.
- **Begründung der Vollziehungsanordnung nicht geprüft** — formeller Mangel nach § 80 Abs. 3 VwGO kann allein zum Erfolg führen.
- **Drittbetroffenheit verkannt** — im Drei-Personen-Verhältnis ist § 80a VwGO einschlägig, nicht allein § 80 VwGO.
- **Abgabenbescheid** — hier entfällt die aufschiebende Wirkung kraft Gesetzes (§ 80 Abs. 2 S. 1 Nr. 1 VwGO); vorrangig Aussetzungsantrag § 80 Abs. 4 VwGO.
- **Aktenzeichen erfunden** — jede Entscheidung verifizieren oder als `[unverifiziert - prüfen]` kennzeichnen.

## Ausgabeformat

```
VORLÄUFIGER RECHTSSCHUTZ § 80 VwGO — <Mandat> — <Datum>

I.   Verwaltungsakt
     Behörde / Inhalt:            <…>
     Sofortige Vollziehung:       [angeordnet am <Datum> / kraft Gesetzes / nein]
     Begründung § 80 Abs. 3:      [vorhanden / fehlt]

II.  Statthafter Antrag
     Fallgruppe § 80 Abs. 2:      [Nr. 1 Abgaben / Nr. 4 Anordnung / …]
     Antrag:                      [Anordnung / Wiederherstellung § 80 Abs. 5]
     Drittbetroffener (§ 80a):    [N/A / ja]

III. Zulässigkeit
     Antragsbefugnis / RSB:       [✓ / fraglich]

IV.  Begründetheit
     Formelle Anordnung:          [ordnungsgemäß / mangelhaft]
     Erfolgsaussicht Hauptsache:  <summarische Prüfung>
     Interessenabwägung:          [Aussetzungs- / Vollzugsinteresse überwiegt]

Ergebnis: <Erfolgsaussicht des Eilantrags>
Empfehlung: <…>
```
