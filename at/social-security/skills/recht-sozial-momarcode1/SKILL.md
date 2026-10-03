---
name: recht-sozial-momarcode1
title: /recht sozial — Sozialrechtliche Analyse
description: Austrian social security law analysis — health insurance (ASVG/GSVG/BSVG), pension (Pensionsrecht), unemployment benefits (AlVG), care allowance (BPGG), accident insurance, and Mindestsicherung. Analyzes entitlements, contribution obligations, and benefit calculations.
author: MoMarcode1
author_url: https://github.com/MoMarcode1/austrian-legal-claude/tree/main/skills/recht-sozial
license: MIT
version: 0.1.1
execution_mode: open
jurisdiction: at
practice: social-security
language: de
sources:
- title: Ris protocol
  path: references/ris-protocol.md
---

# /recht sozial — Sozialrechtliche Analyse

When the user describes a social security or welfare situation and wants to know their entitlements, obligations, or benefit calculations, follow these steps.

---

## Step 1: Gather the Facts

Read what the user has provided. You need:

1. **Employment status** — Angestellt (ASVG), selbständig (GSVG), landwirtschaftlich (BSVG), geringfügig, freier Dienstnehmer, Neue Selbständige?
2. **What benefit or issue?** — Pension, Krankengeld, Arbeitslosengeld, Pflegegeld, Unfallversicherung, Mindestsicherung?
3. **Insurance history** — Versicherungszeiten, Beitragsmonate, current employer/SVT
4. **Income** — Beitragsgrundlage, current earnings, Zuverdienstgrenzen relevant?
5. **Personal situation** — Age, health status, family (for Kinderbetreuungsgeld), care needs (for Pflegegeld)
6. **Dates** — When did insurance start/end? When was the claim filed? Any pending deadlines?
7. **Existing Bescheid** — Has a decision been issued? By which Sozialversicherungsträger (ÖGK, PVA, SVS, BVAEB, AMS)?

If critical information is missing, ask. Be specific:
> "Wie viele Versicherungsmonate haben Sie? Das ist entscheidend für die Anwartschaft."

---

## Step 2: RIS Verification

Before proceeding with analysis, follow the **RIS Verification Protocol** (`references/ris-protocol.md`):
1. Check RIS MCP availability
2. For every § you cite in this analysis, verify current wording via RIS
3. For case law references, retrieve via RIS Justiz (OGH Sozialrechtssachen)
4. Record verification status for the Quellenstatus block
5. If RIS is unavailable, follow the fallback ladder and flag all affected citations

---

## Step 3: Classify the Situation

Determine which insurance branch and benefit applies. Go through this systematically:

### A: Pflichtversicherung — Who is insured where?

| Personengruppe | Versicherungsträger | Rechtsgrundlage |
|---------------|---------------------|-----------------|
| Unselbständig Beschäftigte | ÖGK (Kranken), PVA (Pension), AUVA (Unfall) | §4 ASVG |
| Geringfügig Beschäftigte | Nur Unfallversicherung ex lege; Selbstversicherung möglich (§19a ASVG) | §5 Abs 2 ASVG |
| Gewerblich Selbständige | SVS | §2 Abs 1 GSVG |
| Neue Selbständige | SVS | §2 Abs 1 Z 4 GSVG |
| Landwirte | SVS | §2 BSVG |
| Beamte | BVAEB | B-KUVG |
| Freie Dienstnehmer | ÖGK/PVA/AUVA | §4 Abs 4 ASVG |

Check:
- **Geringfügigkeitsgrenze:** Aktuellen Wert nennen (wird jährlich angepasst). Liegt das monatliche Entgelt darunter → nur Unfallversicherung, aber Opt-in Selbstversicherung nach §19a ASVG möglich (KV + PV).
- **Mehrfachversicherung:** Mehrere Beschäftigungen → Beitragsgrundlagen werden zusammengerechnet bis zur Höchstbeitragsgrundlage. Überschreitung → Erstattung nach §70 ASVG.
- **Opt-out Kleinunternehmer (§4 Abs 1 Z 7 GSVG):** SVS-Befreiung unter bestimmten Umsatz-/Einkommensgrenzen möglich.

### B: Which benefit is at issue?

Check each area:

1. **Krankenversicherung (KV)**
   - e-card und Leistungsanspruch
   - Wahlarzt vs. Kassenarzt: Bei Wahlarzt Erstattung von max. 80% des Kassentarifs (§131 ASVG)
   - Krankengeld: §138ff ASVG — ab dem 4. Tag der Arbeitsunfähigkeit (nach Entgeltfortzahlung durch AG)
   - Wochengeld: §162 ASVG
   - Rehabilitationsgeld: §143a ASVG (seit 2014 statt befristeter Invaliditätspension für unter 50-Jährige)

2. **Pensionsversicherung (PV)**
   - Alterspension: §253 ASVG — Regelpensionsalter 65 (Männer) / wird schrittweise auf 65 angehoben (Frauen, ab 2024)
   - Korridorpension: §4 APG — ab 62 mit Abschlägen, mind. 40 Beitragsjahre
   - Schwerarbeitspension: §4 Abs 3 APG — ab 60, mind. 45 Versicherungsjahre, davon 10 Jahre Schwerarbeit in den letzten 20 Jahren
   - Invaliditätspension: §254 ASVG (Arbeiter) — Invalidität wenn Arbeitsfähigkeit auf weniger als die Hälfte gesunken
   - Berufsunfähigkeitspension: §271 ASVG (Angestellte) — Berufsschutz nach 120 Beitragsmonaten in den letzten 15 Jahren in qualifizierter Tätigkeit
   - Pensionskonto (APG): Kontoerstgutschrift + jährliche Kontogutschriften (1,78% der Beitragsgrundlage)
   - Hinterbliebenenpension: Witwen-/Witwerpension (§258 ASVG), Waisenpension (§260 ASVG)

3. **Unfallversicherung (UV)**
   - Arbeitsunfall: §174 ASVG — Unfall bei Ausübung der Beschäftigung
   - Wegunfall: §175 Abs 2 ASVG — Weg von/zur Arbeit
   - Berufskrankheit: §177 ASVG iVm Anlage 1 ASVG
   - Versehrtenrente: §203 ASVG — ab 20% MdE (Minderung der Erwerbsfähigkeit)

4. **Arbeitslosenversicherung (AlVG)**
   - Arbeitslosengeld: §7 AlVG — Anwartschaft + Arbeitsfähigkeit + Arbeitswilligkeit + Arbeitslosigkeit
   - Anwartschaft: §14 AlVG — 52 Wochen innerhalb der letzten 24 Monate (Erstantrag: 26 Wochen in 12 Monaten für unter 25-Jährige)
   - Bezugsdauer: §18 AlVG — 20 Wochen (Standard), 30 Wochen (ab 3 Jahre), 39 Wochen (ab 6 Jahre + Alter 40), 52 Wochen (ab 9 Jahre + Alter 50)
   - Notstandshilfe: §33 AlVG — nach Ablauf des Arbeitslosengeldes, unbefristet, Notlage + Bedürftigkeitsprüfung (Partnereinkommen!)
   - Sperren: §11 AlVG — Einstellung des Bezugs bei Ablehnung zumutbarer Beschäftigung (§9 AlVG), Lösung des Dienstverhältnisses ohne wichtigen Grund
   - Zumutbarkeit: §9 AlVG — Entgelt, Gesundheit, Betreuungspflichten, Wegzeit (bis 1,5 Stunden einfach)

5. **Pflegegeld (BPGG)**
   - 7 Stufen, abhängig von Pflegebedarf in Stunden pro Monat:
     - Stufe 1: mehr als 65 Stunden
     - Stufe 2: mehr als 95 Stunden
     - Stufe 3: mehr als 120 Stunden
     - Stufe 4: mehr als 160 Stunden
     - Stufe 5: mehr als 180 Stunden + dauernde Bereitschaft
     - Stufe 6: mehr als 180 Stunden + zeitlich nicht planbare Betreuung bei Tag und Nacht
     - Stufe 7: mehr als 180 Stunden + Funktionsunfähigkeit aller vier Extremitäten oder gleichzuachtender Zustand
   - Antrag: Beim zuständigen Sozialversicherungsträger (meist PVA)
   - Begutachtung: Ärztliches Sachverständigengutachten (§8 BPGG)
   - Nachstufung: Antrag auf Höherstufung bei Verschlechterung jederzeit möglich

6. **Mindestsicherung / Sozialhilfe**
   - Sozialhilfe-Grundsatzgesetz (SH-GG) des Bundes + Landesgesetze (seit 2019)
   - Subsidiarität: Erst wenn alle anderen Ansprüche (AlVG, ASVG, Unterhalt) ausgeschöpft sind
   - Keine einheitlichen Beträge — Ausführungsgesetze der Bundesländer beachten
   - Vermögensverwertung: Eigenvermögen muss (bis auf Schonvermögen) eingesetzt werden

7. **Kinderbetreuungsgeld (KBGG)**
   - Pauschales KBGG (Konto): Maximale Bezugsdauer variabel (365-851 Tage bei einem Elternteil, 456-1063 Tage bei Teilung)
   - Einkommensabhängiges KBGG: 80% des Wochengeldes, max. 12 Monate (+ 2 Monate Partnerbonus)
   - Zuverdienstgrenze: §2 Abs 1 Z 3 KBGG — pauschales KBG: individuell berechnet; einkommensabhängig: €7.800/Jahr
   - Familienzeitbonus: §2 FAMZG — 31 Tage, innerhalb der ersten 91 Tage nach Geburt

---

## Step 4: Check Entitlement Requirements

For the identified benefit, verify ALL requirements:

### Anwartschaft / Wartezeit
- List the specific requirements (Versicherungsmonate, Beitragsmonate, Rahmenfristen)
- Calculate: Hat die Person die Anwartschaft erfüllt?
- If borderline: check Sonderregelungen (z.B. Nachkauf von Versicherungszeiten, Kindererziehungszeiten §227a ASVG)

### Persönliche Voraussetzungen
- Alter (Pensionsalter, AlVG-Sonderregeln nach Alter)
- Gesundheitszustand (Invalidität, Pflegebedarf)
- Wohnsitz/gewöhnlicher Aufenthalt in Österreich
- Staatsbürgerschaft/Aufenthaltsberechtigung (relevant für Mindestsicherung)

### Formale Voraussetzungen
- Antragstellung: Wo? Wann? Formvorschriften?
- Fristen: Antragsfrist, Meldefrist beim AMS (§46 AlVG: unverzüglich nach Beendigung)
- Mitwirkungspflichten

---

## Step 5: Calculate Benefits

Where possible, provide concrete Berechnungen:

### Arbeitslosengeld-Berechnung
- Grundbetrag: 55% des täglichen Nettoeinkommens (§21 AlVG)
- Ergänzungsbetrag: Aufstockung auf Ausgleichszulagenrichtsatz bei niedrigem ALG
- Familienzuschlag: §20 Abs 2 AlVG — für unterhaltsberechtigte Angehörige

### Pensionsberechnung (Schätzung)
- Pensionskonto (APG): Gesamtgutschrift / 14 = monatliche Bruttopension
- Kontogutschrift pro Jahr: 1,78% der jährlichen Beitragsgrundlage
- Abschläge bei Korridorpension: 5,1% pro Jahr vor 65
- Ausgleichszulage: Aufstockung auf Mindestpension bei geringer Pension

### Pflegegeld-Beträge
- Aktuelle Beträge je Stufe angeben
- Berechnung: Pflegebedarf in Stunden/Monat → Zuordnung zur Stufe

### Krankengeld-Berechnung
- Höhe: §141 ASVG — 50% der Bemessungsgrundlage (ab 43. Tag: 60%)
- Dauer: §139 ASVG — max. 26 Wochen (52 Wochen bei mind. 6 Monaten Versicherung in letzten 12 Monaten)

---

## Step 6: Present Results

```markdown
# Sozialrechtliche Analyse

**Sachverhalt:** [2-3 Sätze Zusammenfassung]
**Ihre Situation:** [Beschäftigungsstatus, relevanter SVT]
**Betroffene Rechtsgebiete:** [KV/PV/UV/AlVG/BPGG/Mindestsicherung/KBGG]

## Versicherungsstatus

| Versicherungszweig | Status | Grundlage |
|-------------------|--------|-----------|
| Krankenversicherung | [pflichtversichert/selbstversichert/mitversichert/nicht versichert] | §[x] [ASVG/GSVG/BSVG] |
| Pensionsversicherung | [pflichtversichert/...] | §[x] |
| Unfallversicherung | [pflichtversichert] | §[x] |
| Arbeitslosenversicherung | [pflichtversichert/nicht versichert] | §[x] AlVG |

## Anspruchsprüfung: [Bezeichnung des Anspruchs]

### Voraussetzungen
| Voraussetzung | Status | Details |
|--------------|--------|---------|
| [Anwartschaft] | ✅ / ❌ / ❓ | [Begründung] |
| [Persönliche Voraussetzung] | ✅ / ❌ / ❓ | [Begründung] |
| [Formale Voraussetzung] | ✅ / ❌ / ❓ | [Begründung] |

### Berechnung
[Konkrete Berechnung des Leistungsanspruchs mit Beträgen]

**Voraussichtlicher Anspruch:** ca. €[Betrag] [monatlich/täglich/einmalig]
**Bezugsdauer:** [Dauer]
**Anspruchsbeginn:** [Datum]

## Weitere Ansprüche
[Zusätzliche Leistungen, die der Person zustehen könnten — z.B. Familienzuschlag, Ausgleichszulage, Rezeptgebührenbefreiung]

## Handlungsbedarf

### Sofortige Schritte
1. [Erster konkreter Schritt — z.B. "Antrag bei PVA einbringen"]
2. [Zweiter Schritt]

### Fristen
| Frist | Datum | Konsequenz bei Versäumung |
|-------|-------|--------------------------|
| [z.B. AMS-Meldung] | [Datum] | [z.B. Verlust des ALG-Anspruchs] |

### Optionale Optimierungen
- [z.B. Nachkauf von Versicherungszeiten, Selbstversicherung nach §19a ASVG]

## Quellenstatus
| Kategorie | Status | Details |
|-----------|--------|---------|
| RIS MCP | 🟢 Verfügbar / 🔴 Nicht verfügbar | |
| Gesetze | RIS_VERIFIED / UNVERIFIED | [n] Normen geprüft |
| Judikatur | RIS_VERIFIED / UNVERIFIED | [n] Entscheidungen |
| Prüfdatum | [YYYY-MM-DD] | |

---
⚠️ **Keine Rechtsberatung.** Diese Analyse ersetzt nicht die Beratung durch einen Rechtsanwalt oder eine Sozialrechtsberatung (z.B. Arbeiterkammer, Gewerkschaft). Auskünfte des zuständigen Sozialversicherungsträgers sind verbindlich — diese Analyse ist es nicht. Insbesondere bei Pensionsberechnungen und Pflegestufen-Einstufungen handelt es sich um Schätzungen.
```

---

## Critical Rules

1. **Always cite specific §§** — Never "laut Sozialrecht..." without die exakte Gesetzesbestimmung (z.B. §253 ASVG, §7 AlVG, §2 BPGG).
2. **Beträge und Grenzwerte vorsichtig angeben** — Sozialversicherungswerte werden jährlich angepasst (Geringfügigkeitsgrenze, Höchstbeitragsgrundlage, Pflegegeld-Beträge, Ausgleichszulagenrichtsatz). Immer darauf hinweisen, dass aktuelle Werte beim SVT zu erfragen sind.
3. **Fristen prominent hervorheben** — Versäumte Fristen (AMS-Meldung, Bescheid-Beschwerde, Antragstellung) können zum vollständigen Anspruchsverlust führen.
4. **Arbeiterkammer-Hinweis** — Bei Arbeitnehmer-Themen immer auf die kostenlose Beratung durch AK und Gewerkschaft hinweisen.
5. **Landesrecht bei Mindestsicherung** — Das Sozialhilfe-Grundsatzgesetz wird durch 9 verschiedene Landesgesetze ausgeführt. Immer nach dem Bundesland fragen.
6. **Rehabilitationsgeld statt Invaliditätspension** — Seit 2014 erhalten Personen unter 50 Jahren bei vorübergehender Invalidität Rehabilitationsgeld (§143a ASVG) statt einer befristeten Invaliditätspension. Nicht verwechseln.
7. **Mehrfachversicherung beachten** — Bei mehreren Beschäftigungsverhältnissen oder Kombination selbständig/unselbständig die Beitragsgrundlagen zusammenrechnen.
8. **Match user's language** — German in = German out. English in = English out. Gesetze immer in deutscher Originalform zitieren.
9. **Bei Pflegegeld: Pflege-Stunden zählen** — Die Einstufung hängt von den konkreten Verrichtungen und dem dafür anerkannten Zeitbedarf ab. Detailliert aufschlüsseln, nicht pauschal einschätzen.
10. **Kindererziehungszeiten nicht vergessen** — §227a ASVG: Bis zu 48 Monate pro Kind als Ersatzzeiten in der PV. Für die Pensionsberechnung hochrelevant.
