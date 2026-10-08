---
name: datenpanne-meldung-borghei
title: /datenschutzrecht:datenpanne-meldung
description: Meldung einer Verletzung des Schutzes personenbezogener Daten nach Art. 33 und Art. 34 DSGVO – 72-Stunden-Meldung an die Aufsichtsbehörde, Risikobewertung, Benachrichtigung der Betroffenen bei hohem Risiko, Dokumentationspflicht Art. 33 Abs. 5 DSGVO, Bußgeldrisiko Art. 83 Abs. 4 DSGVO. Use when ein Verantwortlicher nach Kenntnis von einer Datenpanne die Meldepflichten und Fristen prüfen muss.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/datenschutzrecht/skills/datenpanne-meldung
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: data-protection
language: de
---

# /datenschutzrecht:datenpanne-meldung

## Zweck

Nach Kenntnis einer Datenpanne läuft eine kurze, harte Meldekette: Vorliegen prüfen → Risiko bewerten → binnen **72 Stunden** an die Aufsichtsbehörde melden (sofern ein Risiko besteht) → bei hohem Risiko zusätzlich die Betroffenen benachrichtigen → alles lückenlos dokumentieren. Dieser Skill führt den Verantwortlichen entlang dieser Kette, hält die Fristen nach und entwirft Melde- und Benachrichtigungstexte, ohne die Meldepflicht über- oder unterzubewerten.

## Eingaben

- Verantwortlicher (bzw. Auftragsverarbeiter, der den Vorfall meldet)
- Art des Vorfalls (Hack, Fehlversand, Verlust eines Datenträgers, Fehlkonfiguration, Innentäter)
- Betroffene Datenkategorien (Stammdaten, Zahlungsdaten, Gesundheitsdaten, besondere Kategorien Art. 9)
- Zahl der betroffenen Personen und Datensätze (geschätzt zulässig)
- Zeitpunkt der Kenntniserlangung (Fristbeginn der 72 Stunden)
- Bereits getroffene Sofortmaßnahmen / Eindämmung
- Beteiligung eines Auftragsverarbeiters

## Sub-Agent-Architektur

Der Skill arbeitet in Prosa-Schritten ohne separaten agents-Block. Sinnvoll ist eine gedankliche Dreiteilung: ein **Sachverhalts-Strang** rekonstruiert Hergang, Datenkategorien und Zahl der Betroffenen; ein **Risiko-Strang** bewertet anhand von Art und Sensibilität der Daten das Risiko für die Rechte und Freiheiten der betroffenen Personen (kein / normales / hohes Risiko); ein **Fristen- und Dokumentations-Strang** überwacht die 72-Stunden-Frist, formuliert die Meldung an die Aufsichtsbehörde und die Benachrichtigung der Betroffenen und legt die Dokumentation an. Die Stränge werden zu einem Meldeentwurf zusammengeführt.

## Ablauf

### 1. Vorliegen einer Datenpanne ([Art. 4 Nr. 12 DSGVO](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32016R0679))

Eine Verletzung des Schutzes personenbezogener Daten liegt vor bei **Vernichtung, Verlust, Veränderung** oder **unbefugter Offenlegung von bzw. unbefugtem Zugang** zu personenbezogenen Daten – ob unbeabsichtigt oder unrechtmäßig. Abzugrenzen von bloßen Beinahe-Vorfällen ohne Personenbezug. Auch ein Verlust der Verfügbarkeit (z. B. Ransomware-Verschlüsselung) ist erfasst.

### 2. Risikobewertung (kein / normales / hohes Risiko)

Maßstab ist das Risiko für die **Rechte und Freiheiten** der betroffenen Personen, abgeleitet aus Art und Sensibilität der Daten, Zahl der Betroffenen, Identifizierbarkeit und möglichen Folgen (Identitätsdiebstahl, Finanzschaden, Diskriminierung).

- **Kein Risiko** → keine Meldepflicht nach Art. 33 Abs. 1, aber Dokumentation (Schritt 5).
- **Normales Risiko** → Meldung an die Aufsichtsbehörde (Schritt 3), keine Benachrichtigung der Betroffenen.
- **Hohes Risiko** → Meldung **und** Benachrichtigung der Betroffenen (Schritt 4).

Zahlungs- oder Gesundheitsdaten und eine vierstellige Zahl Betroffener sprechen regelmäßig für ein **hohes Risiko**.

### 3. 72-Stunden-Meldung an die Aufsichtsbehörde ([Art. 33 Abs. 1 DSGVO](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32016R0679))

Die Meldung erfolgt **unverzüglich und möglichst binnen 72 Stunden** nach Kenntniserlangung – außer die Verletzung führt voraussichtlich **nicht** zu einem Risiko. Wird die Frist überschritten, ist die Verzögerung zu begründen.

Pflichtinhalt nach [Art. 33 Abs. 3 DSGVO](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32016R0679):

a) Art der Verletzung, soweit möglich mit Kategorien und ungefährer Zahl der betroffenen Personen sowie betroffenen Datensätze
b) Name und Kontaktdaten des Datenschutzbeauftragten oder einer sonstigen Anlaufstelle
c) wahrscheinliche Folgen der Verletzung
d) ergriffene oder vorgeschlagene Maßnahmen zur Behebung und Abmilderung

Liegen nicht alle Angaben vor, ist nach [Art. 33 Abs. 4 DSGVO](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32016R0679) eine **phasenweise** (schrittweise nachzureichende) Meldung zulässig – die Frist darf nicht abgewartet werden, bis alle Details geklärt sind.

### 4. Benachrichtigung der Betroffenen ([Art. 34 Abs. 1 DSGVO](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32016R0679))

Bei **voraussichtlich hohem Risiko** sind die betroffenen Personen unverzüglich in klarer und einfacher Sprache zu benachrichtigen; inhaltlich mind. die Angaben aus Art. 33 Abs. 3 lit. b–d.

Ausnahmen nach Art. 34 Abs. 3 DSGVO – keine Benachrichtigung erforderlich, wenn:

- die Daten durch geeignete technische Maßnahmen (insb. **Verschlüsselung**) für Unbefugte unzugänglich sind,
- nachträgliche Maßnahmen das hohe Risiko aller Wahrscheinlichkeit nach abgewendet haben, oder
- die Benachrichtigung unverhältnismäßigen Aufwand erfordert (dann öffentliche Bekanntmachung).

### 5. Dokumentation ([Art. 33 Abs. 5 DSGVO](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32016R0679))

**Alle** Datenpannen sind zu dokumentieren – auch die nicht meldepflichtigen. Festzuhalten sind die mit der Verletzung zusammenhängenden Fakten, ihre Auswirkungen und die ergriffenen Abhilfemaßnahmen. Diese Dokumentationspflicht dient der Nachprüfbarkeit durch die Aufsichtsbehörde (Rechenschaftspflicht).

### 6. Sofortmaßnahmen / Eindämmung

Parallel zur Meldung: betroffene Systeme isolieren, Zugangsdaten zurücksetzen, Sicherheitslücke schließen, Forensik sichern. Diese Maßnahmen fließen als „ergriffene Maßnahmen“ in Art. 33 Abs. 3 lit. d und ggf. in die Ausnahme nach Art. 34 Abs. 3 ein.

### 7. Fristencheck

- **Fristbeginn**: Zeitpunkt der **Kenntniserlangung** des Verantwortlichen – nicht der bloße Vorfallszeitpunkt.
- Meldet ein **Auftragsverarbeiter**, beginnt die 72-Stunden-Frist des Verantwortlichen mit dessen Unterrichtung (Art. 33 Abs. 2).
- Die 72 Stunden laufen **kalendarisch** (inkl. Wochenende/Feiertag) – eine am Freitagabend bekannt gewordene Panne ist regelmäßig bis Montagabend zu melden.

## Ausgabeformat

```
DATENPANNE – Meldeentwurf — <Verantwortlicher> — <Datum>

0.  Sachverhalt              <Hergang, Datenkategorien, Zahl Betroffener>
1.  Vorliegen Art. 4 Nr. 12  [✅ Datenpanne / ❌ kein Personenbezug]
2.  Risikobewertung          [kein / normales / hohes Risiko]  Begründung: <…>

3.  Meldung Aufsichtsbehörde (Art. 33)
    Kenntniserlangung:       <Datum, Uhrzeit>
    Fristende (+72 Std.):    <Datum, Uhrzeit>
    a) Art der Verletzung    <…>
    b) Kontaktstelle / DSB   <…>
    c) wahrscheinliche Folgen<…>
    d) ergriffene Maßnahmen  <…>
    Phasenweise (Abs. 4)?    [ja / nein]

4.  Benachrichtigung Betroffene (Art. 34)
    Erforderlich?            [ja – hohes Risiko / nein]
    Ausnahme Abs. 3?         [Verschlüsselung / Risiko abgewendet / Aufwand]
    Entwurf:                 <…>

5.  Dokumentation (Art. 33 Abs. 5)  Ablage: <…>

Empfehlung: <…>
```

Entscheidungsbaum:

```
Datenpanne (Art. 4 Nr. 12)?
  └─ nein → keine Meldung, ggf. interne Notiz
  └─ ja → Risiko für Rechte/Freiheiten?
        ├─ kein Risiko    → keine Meldung, NUR Dokumentation (Art. 33 Abs. 5)
        ├─ normales Risiko→ Meldung Aufsichtsbehörde (Art. 33) + Dokumentation
        └─ hohes Risiko   → Meldung (Art. 33) + Benachrichtigung (Art. 34) + Dokumentation
                              └─ Ausnahme Art. 34 Abs. 3? → Benachrichtigung entbehrlich
```

## Risiken / typische Fehler

- **72-Stunden-Frist** verpasst, weil auf vollständige Aufklärung gewartet wird → stattdessen phasenweise melden (Art. 33 Abs. 4).
- **hohes Risiko** verkannt → unterbliebene Benachrichtigung der Betroffenen (Art. 34) → eigenständiger Verstoß.
- **Dokumentationspflicht** (Art. 33 Abs. 5) übersehen, auch wenn nicht gemeldet wird → fehlende Nachweisbarkeit gegenüber der Aufsichtsbehörde.
- Fristbeginn falsch angesetzt (Vorfall statt Kenntniserlangung).
- **Bußgeld** nach [Art. 83 Abs. 4 DSGVO](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32016R0679) bei Verstoß gegen die Melde-, Benachrichtigungs- oder Dokumentationspflichten der Art. 33/34 (bis 10 Mio. EUR oder 2 % des weltweiten Jahresumsatzes).

## Quellen

### Statute

- [Art. 4 Nr. 12 DSGVO](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32016R0679) (Definition)
- [Art. 33 DSGVO](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32016R0679) (Meldung an die Aufsichtsbehörde)
- [Art. 34 DSGVO](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32016R0679) (Benachrichtigung der Betroffenen)
- [Art. 83 Abs. 4 DSGVO](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32016R0679) (Bußgeld)
