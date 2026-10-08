---
name: fortbestehensprognose-borghei
title: /insolvenzrecht:fortbestehensprognose
description: Positive Fortbestehensprognose nach § 19 Abs. 2 S. 1 InsO. Überwiegende Wahrscheinlichkeit der Fortführungsfähigkeit (>50%) über 12 Monate (vorher 4 Monate in Krisenmodus). IDW-S-11-konforme Methodik, integriert mit Liquiditätsplanung. Use when ein Mandant überschuldet erscheint und geprüft werden muss, ob die rechnerische Überschuldung durch eine positive Fortbestehensprognose entfällt.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/insolvenzrecht/skills/fortbestehensprognose
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: bankruptcy
language: de
---

# /insolvenzrecht:fortbestehensprognose

## Zweck

Die positive Fortbestehensprognose (PFP) ist die einzige Möglichkeit, die **rechnerische Überschuldung** im Sinne § 19 Abs. 2 InsO **nicht** als Insolvenzgrund wirken zu lassen. Eine fehlerhafte oder ungeprüfte PFP führt direkt in die Antragspflicht und ist haftungstechnisch das größte Einfallstor.

## Eingaben

- Aktueller Status: Überschuldung rechnerisch (Aktiv-Passiv-Vergleich)
- Mehrjährige Finanzplanung (Plan-GuV, Plan-Bilanz, Plan-Cashflow über mindestens 24 Monate)
- 13-Wochen-Liquiditätsplanung (siehe `liquiditaetsplanung-13-wochen`)
- Vorhandene Sanierungskonzepte (intern, externe Beratung, IDW S 6)
- Anlässe und Auslöser der Krise

## Ablauf

### 1. Rechtsrahmen

[§ 19 Abs. 2 S. 1 InsO](https://www.gesetze-im-internet.de/inso/__19.html) (StaRUG-Reform 2021):

> Überschuldung liegt vor, wenn das Vermögen des Schuldners die bestehenden Verbindlichkeiten nicht mehr deckt, **es sei denn, die Fortführung des Unternehmens ist nach den Umständen überwiegend wahrscheinlich.**

**Prognosezeitraum:**
- **Regelfall: 12 Monate** ab Stichtag (§ 19 Abs. 2 S. 1 InsO, durch StaRUG-Reform).
- In außerordentlichen Krisenzeiten (z. B. Bundesgesetz zur Verkürzung wegen Pandemie / Energiepreiskrise): vorübergehend kürzere Zeiträume gewährt.

### 2. Methodik nach IDW S 11

#### a) Erfassung der Tatsachenbasis

- Geschäftsmodell-Beschreibung
- Krisenursachenanalyse
- Sanierungsmaßnahmen (eingeleitet, geplant, möglich)
- Stakeholder-Position (Banken, Lieferanten, Kunden)

#### b) Integriertes Planungsmodell

Plan-GuV, Plan-Bilanz, Plan-Cashflow über mindestens den Prognosezeitraum, vorzugsweise 24 Monate.

#### c) Bewertungsstufen

1. **Zahlungsfähigkeit im Prognosezeitraum** — keine Lücke, die nicht abgedeckt ist.
2. **Bestand der Eigenkapitalbasis** — keine Eigenkapitalvernichtung, die zu Zahlungsunfähigkeit führt.
3. **Verfügbarkeit von Liquiditätsquellen** — bestehende oder zumutbar erreichbare Kreditlinien, Investorenbeiträge.

#### d) Mehrere Szenarien

- Base Case
- Stress Case mit Maßnahmen
- Worst Case (unmittelbare Plausibilitätsprüfung)

### 3. Bewertungsmaßstab „Überwiegende Wahrscheinlichkeit"

Über 50 %. **Nicht** „nachhaltige Sicherheit". Plausibilität, Belegtheit und Konsistenz der Annahmen sind entscheidend.

Wenn die Wahrscheinlichkeit < 50 % oder die Annahmen nicht plausibel: keine positive Prognose → Überschuldungsstatus zu **Liquidationswerten** zu erstellen.

### 4. Liquidations- vs. Going-Concern-Ansatz

- **Positive Prognose**: Going-Concern-Bewertung der Aktiva (oft günstiger).
- **Negative Prognose**: Liquidationswerte (Zerschlagungswert, häufig deutlich niedriger) → Überschuldung tritt nahezu immer ein → Antragspflicht.

### 5. Dokumentation

Pflichtbestandteile:

- Schriftliche Niederlegung
- Stichtag eindeutig
- Methodik beschrieben
- Annahmen und Quellen offengelegt
- Sensitivitätsanalysen
- Beauftragung externer Prüfer (in Hochrisiko-Fällen IDW S 6 / S 11)

### 6. Verzahnung mit Antragspflicht § 15a InsO

- Positive PFP → keine Überschuldung im Sinn § 19 InsO → keine Antragspflicht aus diesem Grund.
- § 17 InsO (Zahlungsunfähigkeit) bleibt **unberührt**: auch bei positiver Fortbestehensprognose kann eine Antragspflicht aus § 17 InsO eintreten.

## Quellen

### Statute / Standards

- [§ 19 InsO](https://www.gesetze-im-internet.de/inso/__19.html), [§ 15a InsO](https://www.gesetze-im-internet.de/inso/__15a.html)
- IDW S 11 (Beurteilung des Vorliegens von Insolvenzeröffnungsgründen)
- IDW S 6 (Anforderungen an Sanierungskonzepte)

### Rechtsprechung

- BGH, Urt. v. 19.11.2013 – II ZR 229/11, NJW 2014, 1238 (PFP-Anforderungen) `[unverifiziert – prüfen]`
- BGH, Urt. v. 18.10.2010 – II ZR 151/09, NZG 2011, 178 `[unverifiziert – prüfen]`

### Kommentare

- Klöhn, in: MüKoInsO, 4. Aufl. 2024, § 19 Rn. 1 ff.
- Schmidt, Sanierungsrecht, 4. Aufl. 2023
- Hölzle, in: Bork / Hölzle, § 19 InsO Rn. 1 ff.

## Ausgabeformat

```
FORTBESTEHENSPROGNOSE — <Mandat> — Stichtag <Datum>

I.   Rechnerische Überschuldung      [ja / nein]
     Aktiv-Passiv-Saldo:               <EUR>

II.  Tatsachenbasis
     Krisenursachen:                   <…>
     Sanierungsmaßnahmen geplant:      <…>
     Stakeholder-Zusagen:              <…>

III. Integriertes Planungsmodell
     Prognosezeitraum:                 <12-24 Monate>
     Methodik:                         IDW S 11

IV.  Szenarien
     Base Case:       Zahlungsfähigkeit gesichert: [✓ / 🔴]
     Stress Case:     Zahlungsfähigkeit gesichert: [✓ / 🔴 → Maßnahmen]
     Worst Case:      Zahlungsfähigkeit gesichert: [✓ / 🔴 → Antragspflicht]

V.   Bewertung
     Überwiegende Wahrscheinlichkeit der Fortführung > 50 %:
       [POSITIV → keine Überschuldung § 19 InsO]
       [NEGATIV → Liquidationswerte-Bilanz → Überschuldung → Antragspflicht]

VI.  Restrisiken
     § 17 InsO Zahlungsunfähigkeit:    [geprüft, kein Eintritt / Risiko]

Empfehlung:
  - Fortbestehensprognose: <ja / nein>
  - Dokumentation:          <…>
  - Externe Bestätigung:    <IDW S 11-Gutachter bei Bedarf>
  - Wiedervorlage:          <Quartalsweise>
```

## Risiken / typische Fehler

- **Unplausible Annahmen** — Auftragseingang verdoppelt sich nicht in der Krise.
- **Stakeholder-Zusagen ohne Schriftform** — verbale Zusagen reichen nicht für PFP.
- **§ 17 InsO unberücksichtigt** — positive PFP rettet nicht vor Zahlungsunfähigkeit.
- **Going-Concern-Bewertung der Aktiva ohne PFP** — Bewertungslogik verkehrt.
- **Dokumentation rudimentär** — keine PFP, sondern Wunschdenken.
- **Maßnahmen ohne Umsetzbarkeit** — Investor-Term-Sheet ohne Closing → Risiko.
