---
name: antragspflicht-15a-inso-borghei
title: /insolvenzrecht:antragspflicht-15a-inso
description: Prüfung der Insolvenzantragspflicht nach § 15a InsO bei juristischen Personen und Gesellschaften ohne Rechtspersönlichkeit. Zahlungsunfähigkeit § 17 InsO, drohende Zahlungsunfähigkeit § 18 InsO, Überschuldung § 19 InsO; 3-Wochen-Frist bei ZU, 6-Wochen-Frist bei Überschuldung; Außenhaftung Neugläubiger § 823 Abs. 2 BGB i.V.m. § 15a InsO; § 15b InsO Erstattungspflicht. Use when ein Mandant in der Krise ist oder ein Geschäftsführer auf Antragspflicht-Risiko geprüft wird.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/insolvenzrecht/skills/antragspflicht-15a-inso
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: bankruptcy
language: de
---

# /insolvenzrecht:antragspflicht-15a-inso

## Zweck

Die Insolvenzantragspflicht ist die schärfste Norm im Krisenrecht: persönliche zivilrechtliche Haftung gegenüber Neugläubigern, strafrechtliche Verfolgung nach § 15a Abs. 4 InsO (Vorsatz) bzw. Abs. 5 (Fahrlässigkeit), Erstattungspflicht für ab Insolvenzreife geleistete Zahlungen aus dem Gesellschaftsvermögen nach § 15b InsO. Dieser Skill prüft den Zeitpunkt der Insolvenzreife und die laufende Antragspflicht.

## Eingaben

- Rechtsform (GmbH, AG, GmbH & Co. KG, OHG ohne natürliche Person als persönlich haftender Gesellschafter)
- Aktuelle Liquiditätslage (Bankguthaben, Forderungen, fällige Verbindlichkeiten, Zahlungsstockungen)
- Bilanz und Fortbestehensprognose (siehe `fortbestehensprognose`)
- Zeitpunkt der Kenntniserlangung des Antragspflichtigen
- Gibt es Sanierungsbemühungen (StaRUG-Anzeige, Vergleichsverhandlungen, Investorensuche)?

## Ablauf

### 1. Adressat der Antragspflicht ([§ 15a Abs. 1, 2 InsO](https://www.gesetze-im-internet.de/inso/__15a.html))

- **Juristische Personen** (GmbH, AG, eG, Verein): Mitglieder des Vertretungsorgans.
- **Gesellschaften ohne Rechtspersönlichkeit ohne unbeschränkt haftende natürliche Person** (GmbH & Co. KG ohne Komplementär-natural Person): jeder organschaftliche Vertreter.
- **Abwickler/Liquidatoren** im Liquidationsstadium.

### 2. Insolvenzgründe

#### a) Zahlungsunfähigkeit ([§ 17 InsO](https://www.gesetze-im-internet.de/inso/__17.html))

Schuldner ist zahlungsunfähig, wenn er nicht in der Lage ist, fällige Zahlungspflichten zu erfüllen. Faustformel BGH (BGH, Beschl. v. 24.05.2005 – IX ZR 123/04, NJW 2005, 3062 `[unverifiziert – prüfen]`):

- **Liquiditätslücke ≥ 10 %** über mehr als drei Wochen → in der Regel Zahlungsunfähigkeit.
- Eine geringere Lücke kann bei abzusehender Nichtbehebung ebenfalls Zahlungsunfähigkeit begründen.
- Bloße **Zahlungsstockung** (< 3 Wochen) reicht nicht.

#### b) Drohende Zahlungsunfähigkeit ([§ 18 InsO](https://www.gesetze-im-internet.de/inso/__18.html))

Mit überwiegender Wahrscheinlichkeit kann der Schuldner seine bestehenden Zahlungspflichten **im Zeitpunkt der Fälligkeit** nicht erfüllen. Prognosezeitraum: **24 Monate** (§ 18 Abs. 2 S. 2 InsO, eingeführt durch StaRUG-Umsetzung 2021).

Drohende Zahlungsunfähigkeit ist **kein** Antragsgrund nach § 15a InsO (nur § 17, § 19). Sie eröffnet aber den Zugang zu StaRUG-Stabilisierungsinstrumenten.

#### c) Überschuldung ([§ 19 InsO](https://www.gesetze-im-internet.de/inso/__19.html))

Vermögen deckt nicht mehr die bestehenden Verbindlichkeiten, **es sei denn**, die Fortführung des Unternehmens ist nach den Umständen überwiegend wahrscheinlich (**positive Fortbestehensprognose**, § 19 Abs. 2 S. 1 InsO).

Zwei-Stufen-Prüfung:

1. **Fortbestehensprognose** (siehe `fortbestehensprognose`): überwiegende Wahrscheinlichkeit (> 50 %) der Fortführungsfähigkeit über den Prognosezeitraum (12 Monate ab 2024-12, vorher 4 Monate während Krisenmodus).
2. Wenn negative Prognose: **Überschuldungsstatus** zu Liquidationswerten (kein Going-Concern-Ansatz).

### 3. Antragsfristen ([§ 15a Abs. 1 InsO](https://www.gesetze-im-internet.de/inso/__15a.html))

| Insolvenzgrund | Frist | Beginn |
|---|---|---|
| Zahlungsunfähigkeit § 17 | **3 Wochen** | Eintritt der Zahlungsunfähigkeit |
| Überschuldung § 19 | **6 Wochen** | Eintritt der Überschuldung |

**Achtung:** Die Frist beginnt mit dem **objektiven** Eintritt, nicht mit der Kenntnis. Eine spätere Kenntniserlangung kann zwar das Verschulden ausschließen, nicht aber die objektive Pflichtverletzung.

Innerhalb der Frist darf gehandelt werden, um die Insolvenz zu beseitigen (Investorensuche, Sanierungsgespräche). Die Frist darf nicht zur bloßen Hinauszögerung genutzt werden.

### 4. Folgen einer Verletzung der Antragspflicht

#### Strafbarkeit § 15a Abs. 4, 5 InsO

- Vorsatz: Freiheitsstrafe bis 3 Jahre oder Geldstrafe.
- Fahrlässigkeit: Freiheitsstrafe bis 1 Jahr oder Geldstrafe.

#### Außenhaftung gegenüber Neugläubigern

Aus § 823 Abs. 2 BGB i.V.m. § 15a InsO: Wer im Vertrauen auf die fortbestehende Solvenz mit der bereits insolvenzreifen Gesellschaft kontrahiert hat, erleidet einen Vertrauensschaden, für den der Geschäftsführer persönlich haftet. Schaden = Differenz zwischen tatsächlicher Erfüllung und hypothetischer Insolvenzquote.

Vgl. BGH, Urt. v. 27.04.2009 – II ZR 86/07, NJW 2009, 2454 `[unverifiziert – prüfen]`.

#### Erstattungspflicht für Zahlungen aus dem Gesellschaftsvermögen ([§ 15b InsO](https://www.gesetze-im-internet.de/inso/__15b.html))

Ab Eintritt der Insolvenzreife sind Zahlungen aus dem Gesellschaftsvermögen verboten, soweit sie die Insolvenzmasse mindern (§ 15b Abs. 1 InsO). Ausnahme: Zahlungen, die mit Sorgfalt eines ordentlichen Geschäftsmanns vereinbar sind (Aufrechterhaltung des Geschäftsbetriebs während der Antragsfrist).

Der Geschäftsführer haftet auf Erstattung, **persönlich** und **gesamtschuldnerisch** mit weiteren Geschäftsführern.

### 5. Verteidigungslinien

- **Keine Insolvenzreife eingetreten** (z. B. Liquiditätsstockung statt -unfähigkeit, positive Fortbestehensprognose, abgewendet).
- **Innerhalb der Antragsfrist gehandelt** (3 bzw. 6 Wochen) mit ernsthaften Sanierungsbemühungen.
- **Kein Verschulden** bei objektivem Vorliegen (selten erfolgreich).
- **Verjährung** § 15a Abs. 6 InsO i.V.m. allgemeinen Verjährungsregeln (regelmäßig 5 Jahre).
- **D&O-Versicherung** (in der Regel werden Insolvenzverschleppungsfälle aber als vorsätzliche Pflichtverletzung ausgeschlossen — Deckung prüfen).

### 6. Verzahnung mit StaRUG

StaRUG ([Gesetz über den Stabilisierungs- und Restrukturierungsrahmen](https://www.gesetze-im-internet.de/starug/)) erlaubt eine **frühzeitige** Restrukturierung bei drohender Zahlungsunfähigkeit, ohne Eröffnung eines Insolvenzverfahrens. Die Anzeige nach § 31 StaRUG begründet **keine** Antragspflicht nach § 15a InsO; bei Eintritt von ZU oder Überschuldung greift § 15a InsO aber wieder.

Siehe Detail-Skill: `starug-restrukturierungsplan`.

## Quellen

### Statute

- [§ 15a InsO](https://www.gesetze-im-internet.de/inso/__15a.html), [§ 15b InsO](https://www.gesetze-im-internet.de/inso/__15b.html)
- [§ 17 InsO](https://www.gesetze-im-internet.de/inso/__17.html), [§ 18 InsO](https://www.gesetze-im-internet.de/inso/__18.html), [§ 19 InsO](https://www.gesetze-im-internet.de/inso/__19.html)
- [§ 823 Abs. 2 BGB](https://www.gesetze-im-internet.de/bgb/__823.html)
- [StaRUG](https://www.gesetze-im-internet.de/starug/)

### Kommentare

- Klöhn, in: MüKoInsO, 4. Aufl. 2024, § 15a Rn. 1 ff.
- Mock, in: Uhlenbruck, InsO, 16. Aufl. 2024, § 15a Rn. 1 ff.
- Schmidt-Karsten, ZIP 2023, 1 ff. (Aufsatz zur StaRUG-Reform und Antragspflicht)

### Rechtsprechung

- BGH, Beschl. v. 24.05.2005 – IX ZR 123/04, NJW 2005, 3062 (Liquiditätslücke) `[unverifiziert – prüfen]`
- BGH, Urt. v. 27.04.2009 – II ZR 86/07, NJW 2009, 2454 (Außenhaftung) `[unverifiziert – prüfen]`
- BGH, Urt. v. 16.03.2009 – II ZR 280/07, NJW 2009, 2127 (§ 64 GmbHG a.F. = heute § 15b InsO) `[unverifiziert – prüfen]`

## Ausgabeformat

```
INSOLVENZANTRAGSPFLICHT-PRÜFUNG — <Mandat> — <Datum>

I.   Adressat                        [GF / Liquidator / Vorstand]
II.  Insolvenzgrund-Check
     a) Zahlungsunfähigkeit § 17     [eingetreten am / nicht eingetreten]
        Liquiditätslücke %:           <…>
     b) Überschuldung § 19           [eingetreten / Prognose positiv]
III. Antragsfrist
     ZU: 3 Wochen ab <Datum> → Fristende <Datum>
     ÜS: 6 Wochen ab <Datum> → Fristende <Datum>
IV.  Status
     [🟢 keine Antragspflicht / 🟡 in der Frist / 🔴 Frist abgelaufen]
V.   Risikobewertung
     Strafrechtlich § 15a Abs. 4/5    [Risiko hoch / mittel / niedrig]
     Außenhaftung Neugläubiger        [exponiert / abgemildert]
     Erstattung § 15b                 [Zahlungen seit <Datum>: Liste]
VI.  Empfehlung
     - Sofortmaßnahmen: <…>
     - Sanierungsoption (StaRUG?): <…>
     - Antrag bis: <Datum>

Verteidigungsoptionen: <…>
```

## Risiken / typische Fehler

- **Frist falsch berechnet** — sie beginnt mit objektivem Eintritt, nicht mit Kenntnis.
- **Drohende ZU als Antragsgrund verstanden** — sie ist es nicht (nur Eröffnungsrecht des Schuldners + StaRUG-Zugang).
- **Sanierungsbemühungen ohne Liquiditätsanalyse** — § 17 InsO bleibt objektive Prüfung.
- **Zahlungen ab Insolvenzreife** ohne § 15b-Sorgfaltsmaßstab-Prüfung → persönliche Erstattung.
- **„Wir kämpfen seit Wochen, das wird schon"** — verlängert nicht die Antragsfrist.
- **D&O-Deckung angenommen** — Insolvenzverschleppung ist häufig vom Versicherungsschutz ausgeschlossen.
