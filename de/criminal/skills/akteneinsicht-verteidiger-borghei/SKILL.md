---
name: akteneinsicht-verteidiger-borghei
title: /strafrecht:akteneinsicht-verteidiger
description: Prüfung des Akteneinsichtsrechts des Verteidigers nach § 147 StPO – Umfang, Versagung bei Gefährdung des Untersuchungszwecks (§ 147 Abs. 2), Akteneinsicht des unverteidigten Beschuldigten (§ 147 Abs. 4), Form der Gewährung § 32f StPO. Use when Akteneinsicht beantragt, verweigert oder beschränkt wurde und Umfang, Zeitpunkt und Rechtsschutz zu klären sind.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/strafrecht/skills/akteneinsicht-verteidiger
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: criminal
language: de
---

# /strafrecht:akteneinsicht-verteidiger

## Zweck

Effektive Verteidigung setzt Aktenkenntnis voraus (Grundsatz des fairen Verfahrens, Art. 6 EMRK; rechtliches Gehör). Dieser Skill prüft das **Akteneinsichtsrecht des Verteidigers** nach [§ 147 StPO](https://www.gesetze-im-internet.de/stpo/__147.html): **Umfang**, die **Versagungsgründe** im laufenden Ermittlungsverfahren, den **Zeitpunkt** und die Sonderlage des unverteidigten Beschuldigten.

## Eingaben

- Verfahrensstand (Ermittlungsverfahren / Abschlussvermerk erfolgt / nach Anklage)
- Ist der Beschuldigte verteidigt oder unverteidigt?
- Wurde Akteneinsicht beantragt? Datum, Reaktion der StA
- Begründung einer etwaigen Versagung?
- Untersuchungshaft anhängig?
- Betroffene besonders sensible Aktenteile?

## Sub-Agent-Architektur

Der **Researcher** ordnet den Sachverhalt den Absätzen des § 147 StPO zu (Umfang, Versagung, unverteidigter Beschuldigter) und verifiziert jede Norm gegen gesetze-im-internet.de; er erfindet keine Aktenzeichen. Der **Drafter** formuliert den Antrag auf Akteneinsicht bzw. den Antrag auf gerichtliche Entscheidung und arbeitet Umfang und Versagungsgründe heraus. Der **Reviewer** prüft gegenläufig, ob die Versagung „Gefährdung des Untersuchungszwecks" trägt, ob bei Untersuchungshaft die haftrelevanten Informationen offenzulegen sind und ob der Zeitpunkt gewahrt ist; unbestätigte Rechtsprechung kennzeichnet er mit `[unverifiziert – prüfen]`.

## Ablauf

### 1. Umfang des Akteneinsichtsrechts ([§ 147 Abs. 1 StPO](https://www.gesetze-im-internet.de/stpo/__147.html))

Der Verteidiger ist befugt, **die Akten einzusehen**, die dem Gericht vorliegen oder ihm im Falle der Anklageerhebung vorzulegen wären, sowie amtlich verwahrte Beweisstücke zu besichtigen. **Umfang**: vollständige Verfahrensakte einschließlich Spurenakten, soweit verfahrensrelevant.

### 2. Versagungsgründe im Ermittlungsverfahren ([§ 147 Abs. 2 StPO](https://www.gesetze-im-internet.de/stpo/__147.html))

- Solange der **Abschluss der Ermittlungen** noch nicht in den Akten vermerkt ist, kann die Einsicht **versagt** werden, soweit sie den **Untersuchungszweck** gefährden kann.
- **Sonderregel Untersuchungshaft**: Sind dem Beschuldigten in Haft relevante Informationen für die Beurteilung der Rechtmäßigkeit der Haft erforderlich, sind diese zugänglich zu machen (Waffengleichheit im Haftrecht).

### 3. Akteneinsicht des unverteidigten Beschuldigten ([§ 147 Abs. 4 StPO](https://www.gesetze-im-internet.de/stpo/__147.html))

- Der **Beschuldigte ohne Verteidiger** kann grundsätzlich selbst Akteneinsicht nehmen bzw. Auskünfte und Kopien erhalten, soweit der Untersuchungszweck nicht gefährdet wird und überwiegende schutzwürdige Interessen Dritter nicht entgegenstehen.
- Das Recht, sich eines Verteidigers zu bedienen, folgt aus [§ 137 StPO](https://www.gesetze-im-internet.de/stpo/__137.html).

### 4. Zeitpunkt

- **Zeitpunkt**: kein generelles Recht auf Einsicht „jederzeit"; nach Abschlussvermerk besteht der volle Anspruch.
- Frühzeitiger Antrag sichert die Verteidigung; verweigerte Einsicht ist zu dokumentieren.

### 5. Form der Gewährung ([§ 32f StPO](https://www.gesetze-im-internet.de/stpo/__32f.html))

- Bei elektronischer Akte: Bereitstellung zum Abruf oder Übermittlung; bei Papierakte: Einsicht in den Diensträumen oder Aktenversand.
- Beschränkungen des Weitergabe-/Verwendungszwecks beachten (Datenschutz, Persönlichkeitsrechte Dritter, vgl. [§ 406e StPO](https://www.gesetze-im-internet.de/stpo/__406e.html) für die Verletztenseite).

### 6. Rechtsschutz

- Gegen die Versagung: Antrag auf **gerichtliche Entscheidung**; im Ermittlungsverfahren nach § 147 Abs. 5 StPO.
- Bei Untersuchungshaft besonders dringlich (Haftprüfung).

## Risiken

- **Versagung** pauschal mit „Gefährdung des Untersuchungszwecks" begründet, ohne konkrete Tatsachen.
- Bei **Untersuchungshaft** haftrelevante Aktenteile vorenthalten → Verstoß gegen Waffengleichheit.
- **Umfang** zu eng — Spurenakten / Beiakten nicht herausgegeben.
- **Zeitpunkt** verkannt: nach Abschlussvermerk kein Versagungsgrund mehr, dennoch verzögert.

## Ausgabeformat

```
AKTENEINSICHT — <Az.> — <Datum>
VERTRAULICH — STRAFVERTEIDIGUNG

I.    Verfahrensstand                 <Ermittlung / Abschlussvermerk / Anklage>
II.   Antrag gestellt am:             <…>
III.  Umfang                          [§ 147 Abs. 1 StPO]
      Vollständige Akte + Beiakten:   [✅ / ⚠️]
IV.   Versagung                       [§ 147 Abs. 2 StPO]
      Begründung trägt:               [✅ / 🔴 pauschal]
      Untersuchungshaft → Offenlegung:[erforderlich / nicht einschlägig]
V.    Unverteidigter Beschuldigter    [§ 147 Abs. 4 StPO]   [einschlägig / nein]

Empfehlung: <…>
Nächster Schritt: <Antrag auf gerichtliche Entscheidung § 147 Abs. 5 StPO>
```

## Quellen

- [§ 147 StPO](https://www.gesetze-im-internet.de/stpo/__147.html), [§ 137 StPO](https://www.gesetze-im-internet.de/stpo/__137.html), [§ 32f StPO](https://www.gesetze-im-internet.de/stpo/__32f.html), [§ 406e StPO](https://www.gesetze-im-internet.de/stpo/__406e.html)
- Meyer-Goßner / Schmitt, StPO, 67. Aufl. 2024, § 147 Rn. 1 ff.
- Rechtsprechung zur Versagung bei Untersuchungshaft: `[unverifiziert – prüfen]`
