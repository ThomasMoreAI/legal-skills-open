---
name: zahlungsdiensthaftung-borghei
title: /bankrecht:zahlungsdiensthaftung
description: Haftungsverteilung bei nicht autorisierten Zahlungsvorgängen. Zahlungsdiensterahmen § 675c BGB, Erstattungsanspruch bei nicht autorisiertem Zahlungsvorgang § 675u BGB, Haftung des Zahlers bei grober Fahrlässigkeit § 675v BGB. Use when eine unautorisierte Abbuchung, ein Phishing- oder Kartenmissbrauchsfall bewertet und die Haftung zwischen Bank und Kunde verteilt wird.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/bankrecht/skills/zahlungsdiensthaftung
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: finance
language: de
---

# /bankrecht:zahlungsdiensthaftung

## Zweck

Bei nicht autorisierten Zahlungen (Phishing, Kartenmissbrauch, Kontomanipulation) stellt sich die Frage, wer den Schaden trägt. Das Gesetz weist das Risiko grundsätzlich dem Zahlungsdienstleister zu (§ 675u BGB) und lässt eine Kundenhaftung nur unter engen Voraussetzungen zu (§ 675v BGB). Dieser Skill prüft die Autorisierung, den Erstattungsanspruch und die Voraussetzungen einer ausnahmsweisen Kundenhaftung.

## Eingaben

- Art des Zahlungsvorgangs (Überweisung, Lastschrift, Kartenzahlung, Online-Banking)
- Vorgang autorisiert oder bestritten (§ 675j BGB)
- Hergang (Phishing, verlorene Karte, Drittzugriff, Social Engineering)
- Eingesetzte Authentifizierung (starke Kundenauthentifizierung, TAN-Verfahren)
- Verhalten des Kunden (Sorgfaltspflichten, Anzeige nach § 675l BGB)
- Zeitpunkt der Anzeige und der Erstattungsforderung

## Sub-Agent-Architektur

Der **Researcher** bestätigt §§ 675c ff. BGB über gesetze-im-internet.de und ordnet die Umsetzung der Zahlungsdiensterichtlinie (PSD2) ein; ungesicherte Aktenzeichen werden als `[unverifiziert – prüfen]` markiert. Der **Drafter** prüft zunächst die Autorisierung, dann den Erstattungsanspruch nach § 675u BGB und schließlich die Gegenrechte des Zahlungsdienstleisters nach § 675v BGB. Der **Reviewer** kontrolliert die Beweislastverteilung, die Behandlung der starken Kundenauthentifizierung und stellt sicher, dass keine Tatsachen erfunden wurden.

## Ablauf

### 1. Anwendungsbereich (§ 675c BGB)

[§ 675c BGB](https://www.gesetze-im-internet.de/bgb/__675c.html): Auf Zahlungsdienste und den Zahlungsdiensterahmenvertrag sind die §§ 663 ff. BGB sowie die besonderen §§ 675c–676c BGB anwendbar. Klärung von Zahler, Zahlungsempfänger und Zahlungsdienstleister.

### 2. Autorisierung (§ 675j BGB)

[§ 675j BGB](https://www.gesetze-im-internet.de/bgb/__675j.html): Ein Zahlungsvorgang ist nur wirksam, wenn der Zahler ihm zugestimmt hat. Fehlt die Zustimmung, liegt ein **nicht autorisierter Zahlungsvorgang** vor. Beweislast: Der Zahlungsdienstleister muss die Autorisierung und die ordnungsgemäße Aufzeichnung nachweisen (§ 675w BGB); die Aufzeichnung allein genügt nicht.

### 3. Erstattungsanspruch (§ 675u BGB)

[§ 675u BGB](https://www.gesetze-im-internet.de/bgb/__675u.html): Bei einem nicht autorisierten Zahlungsvorgang hat der Zahlungsdienstleister

- **keinen Anspruch** auf Erstattung seiner Aufwendungen und
- den Zahlungsbetrag **unverzüglich**, spätestens bis zum Ende des folgenden Geschäftstags nach Kenntnis, zu erstatten und das Konto wieder auf den Stand ohne Belastung zu bringen.

### 4. Kundenhaftung (§ 675v BGB)

[§ 675v BGB](https://www.gesetze-im-internet.de/bgb/__675v.html): Ausnahmsweise haftet der Zahler:

- **bis 50 EUR** bei Nutzung eines verlorenen, gestohlenen oder missbräuchlich verwendeten Zahlungsinstruments (Abs. 1)
- **in voller Höhe** bei betrügerischem Handeln oder bei Vorsatz bzw. grobe Fahrlässigkeit bei der Verletzung der Sorgfalts-/Anzeigepflichten (Abs. 3)
- **keine Haftung**, wenn der Zahlungsdienstleister keine **starke Kundenauthentifizierung** verlangt hat (Abs. 4), sofern der Zahler nicht betrügerisch handelte
- **keine Haftung** für Verfügungen nach der Verlustanzeige (§ 675l BGB)

### 5. Sorgfalts- und Anzeigepflichten (§ 675l BGB)

[§ 675l BGB](https://www.gesetze-im-internet.de/bgb/__675l.html): Geheimhaltung der personalisierten Sicherheitsmerkmale (PIN, TAN) und unverzügliche Anzeige bei Verlust/Missbrauch. Maßstab der groben Fahrlässigkeit: Weitergabe von TAN an Dritte trotz Warnhinweisen wiegt schwer; bloßes Phishing-Opfer ohne Sorgfaltsverstoß haftet nicht.

## Risiken / typische Fehler

- **Autorisierung ungeprüft unterstellt** — die Bank trägt die Beweislast nach § 675w BGB; die bloße Aufzeichnung der Authentifizierung beweist die Autorisierung nicht.
- **Erstattungsfrist missachtet** — der Erstattungsanspruch nach § 675u BGB ist unverzüglich zu erfüllen; verspätete Erstattung begründet Verzug.
- **Grobe Fahrlässigkeit vorschnell angenommen** — die Hürde des § 675v BGB ist hoch; Social Engineering ohne Sorgfaltsverstoß genügt nicht.
- **Starke Kundenauthentifizierung übersehen** — fehlt sie, entfällt die Kundenhaftung ganz (§ 675v Abs. 4 BGB).
- **Anzeigezeitpunkt nicht dokumentiert** — nach der Verlustanzeige (§ 675l BGB) haftet der Zahler nicht mehr; ungesicherte Aktenzeichen als `[unverifiziert – prüfen]` kennzeichnen.

## Quellen

- [§ 675c BGB](https://www.gesetze-im-internet.de/bgb/__675c.html), [§ 675j BGB](https://www.gesetze-im-internet.de/bgb/__675j.html), [§ 675l BGB](https://www.gesetze-im-internet.de/bgb/__675l.html)
- [§ 675u BGB](https://www.gesetze-im-internet.de/bgb/__675u.html), [§ 675v BGB](https://www.gesetze-im-internet.de/bgb/__675v.html), [§ 675w BGB](https://www.gesetze-im-internet.de/bgb/__675w.html)
- [Richtlinie (EU) 2015/2366 (PSD2)](https://eur-lex.europa.eu/eli/dir/2015/2366/oj)
- BGH, Urt. v. 26.01.2016 – XI ZR 91/14 (Anscheinsbeweis Online-Banking) `[unverifiziert – prüfen]`

## Ausgabeformat

```
ZAHLUNGSDIENST-HAFTUNG — <Mandat> — <Datum>

I.    Anwendungsbereich § 675c BGB        [Zahlungsdienst ✓]
II.   Autorisierung § 675j BGB            [autorisiert / nicht autorisiert]
      Beweislast § 675w BGB:              [Bank / erfüllt?]
III.  Erstattungsanspruch § 675u BGB
      Anspruch dem Grunde nach:           [✓ / 🔴]
      Frist (Ende Folge-Geschäftstag):    <…>
IV.   Kundenhaftung § 675v BGB
      Verlust/Diebstahl bis 50 EUR:       [N/A / einschlägig]
      Grobe Fahrlässigkeit / Vorsatz:     [✓ / nein]
      Starke Kundenauthentifizierung:     [vorhanden / fehlt → keine Haftung]
      Anzeige § 675l BGB:                 <Zeitpunkt>

Ergebnis Haftungsverteilung: <…>
```
