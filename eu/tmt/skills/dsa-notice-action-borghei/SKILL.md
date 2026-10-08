---
name: dsa-notice-action-borghei
title: /dsa-dma:dsa-notice-action
description: Prüfung und Gestaltung des Melde- und Abhilfeverfahrens (Notice-and-Action) nach Art. 16 DSA samt Begründungspflicht Art. 17 DSA und Haftungsprivileg des Hosting-Anbieters Art. 6 DSA – Meldewege, Kenntniserlangung, Reaktionsfristen, Folgen für die Haftung. Use when ein Hosting-Anbieter oder eine Online-Plattform eine Meldung über (angeblich) rechtswidrige Inhalte erhält oder sein Meldesystem DSA-konform gestalten will.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/dsa-dma/skills/dsa-notice-action
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: eu
practice: tmt
language: de
---

# /dsa-dma:dsa-notice-action

## Zweck

Der Notice-and-Action-Mechanismus nach **Art. 16 DSA** ([VO (EU) 2022/2065](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32022R2065)) ist das zentrale Scharnier zwischen Meldung rechtswidriger Inhalte, Reaktionspflicht der Plattform und dem **Haftungsprivileg nach Art. 6 DSA**. Eine ordnungsgemäße Meldung kann die "tatsächliche Kenntnis" auslösen, die das Privileg entfallen lässt. Dieser Skill prüft, ob ein Meldesystem konform ist und ob auf eine konkrete Meldung richtig reagiert wurde.

## Eingaben

- Rolle des Mandanten (Hosting-Anbieter, Online-Plattform, Online-Marktplatz i.S.v. Art. 3 DSA)
- Inhalt und Form der eingegangenen Meldung (Notice)
- Behauptete Rechtswidrigkeit (nationaler/europäischer Rechtsverstoß)
- Bestehendes Meldesystem (elektronisch, leicht zugänglich?)
- Bisherige Reaktion (Entfernung, Sperrung, keine Maßnahme)

## Sub-Agent-Architektur

Die Bearbeitung folgt drei gedanklichen Rollen. Ein **Melde-Prüfer** untersucht, ob die eingegangene Notice die inhaltlichen Anforderungen von Art. 16 Abs. 2 DSA erfüllt und damit überhaupt geeignet ist, Kenntnis zu vermitteln. Ein **Haftungs-Analyst** beurteilt parallel, ob und ab wann das Haftungsprivileg nach Art. 6 DSA entfällt und welche Reaktionsfrist ("zügig", "unverzüglich") gilt. Ein **Begründungs-Redakteur** stellt sicher, dass jede getroffene Maßnahme eine Begründung nach Art. 17 DSA erhält und der Meldende über Rechtsbehelfe informiert wird. Die Rollen werden nacheinander durchlaufen; Konflikte (z. B. unklare Rechtswidrigkeit) werden an den Haftungs-Analysten zurückgespielt.

## Ablauf

### 1. Anwendungsbereich (Art. 16 Abs. 1 DSA)

Pflicht trifft **Hosting-Anbieter**. Sie müssen Mechanismen einrichten, über die jede Person elektronisch und einfach das Vorhandensein vermeintlich rechtswidriger Inhalte melden kann.

### 2. Inhalt einer wirksamen Meldung (Art. 16 Abs. 2 DSA)

Die Notice muss enthalten:

a) hinreichend begründete Erläuterung, warum der Inhalt rechtswidrig ist
b) genaue elektronische Angabe des Speicherorts (z. B. exakte URL)
c) Name und E-Mail-Adresse des Meldenden (außer bei mutmaßlichen Straftaten gegen die sexuelle Selbstbestimmung)
d) Erklärung über Gutgläubigkeit und Richtigkeit

### 3. Kenntniserlangung und Haftung (Art. 16 Abs. 3 i.V.m. Art. 6 DSA)

Eine Meldung, die alle Elemente nach Abs. 2 enthält, **begründet die Vermutung tatsächlicher Kenntnis** für die Zwecke von Art. 6 DSA. Ab diesem Zeitpunkt entfällt das Haftungsprivileg, wenn der Anbieter nicht **zügig** tätig wird (Entfernung oder Sperrung des Zugangs). Bei Online-Marktplätzen für Verbraucher kann das Privileg von vornherein eingeschränkt sein.

### 4. Bestätigung und Bearbeitung (Art. 16 Abs. 4–6 DSA)

- Empfangsbestätigung an den Meldenden (Abs. 4)
- Mitteilung der Entscheidung samt Rechtsbehelfshinweis (Abs. 5)
- Bearbeitung zeitnah, sorgfältig, frei von Willkür, objektiv; Offenlegung automatisierter Mittel (Abs. 6)

### 5. Begründung jeder Maßnahme (Art. 17 DSA)

Wird der Inhalt eingeschränkt, ist dem betroffenen Nutzer eine klare Begründung ("Statement of Reasons") nach **Art. 17 DSA** zu erteilen und an die DSA-Transparenzdatenbank zu übermitteln. Der Hinweis auf interne Beschwerde nach Art. 20 DSA und auf vertrauenswürdige Hinweisgeber Art. 22 DSA gehört dazu.

### 6. Behördliche Anordnungen (Art. 9 DSA)

Liegt der Inhaltsbeanstandung eine behördliche Anordnung gegen illegale Inhalte nach **Art. 9 DSA** zugrunde, gelten besondere Form- und Reaktionsregeln, die dem Notice-and-Action-Verfahren vorgehen.

## Risiken

- **Verschleppte Reaktion** — Untätigkeit nach wirksamer Meldung lässt das Haftungsprivileg nach Art. 6 DSA entfallen; Schadensersatz droht.
- **Overblocking** — vorschnelle Entfernung nicht eindeutig rechtswidriger Inhalte verletzt Nutzerrechte und Art. 17 DSA.
- **Unvollständige Meldung als Kenntnis behandelt** — eine Notice ohne die Elemente des Art. 16 Abs. 2 DSA löst die Kenntnisvermutung gerade nicht aus.
- **Begründung vergessen** — jede Maßnahme braucht ein Statement of Reasons nach Art. 17 DSA; Fehlen ist eigenständiger Verstoß.

## Ausgabeformat

```
DSA NOTICE-AND-ACTION-PRÜFUNG — <Plattform> — <Datum>

I.   Rolle (Art. 16 DSA)            [Hosting / Online-Plattform / Marktplatz]
II.  Meldung vollständig (Art. 16 Abs. 2 DSA)  [ja / nein — fehlende Elemente]
III. Kenntnisvermutung (Art. 16 Abs. 3 DSA)    [ausgelöst / nicht ausgelöst]
IV.  Haftungsprivileg (Art. 6 DSA)             [besteht / entfallen ab <Datum>]
V.   Reaktionsfrist                            [zügig — bis <…>]
VI.  Begründung erforderlich (Art. 17 DSA)     [ja — Inhalt / nein]
VII. Behördliche Anordnung (Art. 9 DSA)        [ja / nein]

Empfehlung: <…>
Nächste Schritte: <…>
```

## Quellen

### Statute

- [VO (EU) 2022/2065 (DSA)](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32022R2065) — Volltext
- Art. 6 DSA (Haftungsprivileg Hosting), Art. 9 DSA (Anordnungen), Art. 16 DSA (Notice-and-Action), Art. 17 DSA (Begründung), Art. 22 DSA (vertrauenswürdige Hinweisgeber)

### Sekundärliteratur

- Spindler/Schmitz, DSA-Kommentar, 1. Aufl. 2024
- BeckOK DSA (Online)
