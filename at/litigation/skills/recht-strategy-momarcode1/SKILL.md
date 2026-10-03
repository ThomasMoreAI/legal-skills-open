---
name: recht-strategy-momarcode1
title: /recht strategy — Prozessstrategie
description: Litigation strategy for Austrian courts. Success probability, court selection, timeline estimation, settlement corridor, BATNA/WATNA, and recommended procedure.
author: MoMarcode1
author_url: https://github.com/MoMarcode1/austrian-legal-claude/tree/main/skills/recht-strategy
license: MIT
version: 0.1.1
execution_mode: open
jurisdiction: at
practice: litigation
language: de
sources:
- title: Ogh case presentation
  path: references/ogh-case-presentation.md
- title: Ris protocol
  path: references/ris-protocol.md
---

# /recht strategy — Prozessstrategie

When the user has a dispute and wants to know how to proceed, follow these steps.

---

## Step 1: Collect Context

You need the outputs from `/recht claim` and `/recht evidence`. If those haven't been run yet, do their analysis first (at least mentally — you don't need to output them separately).

Confirm you know:
- The viable claims (from claim analysis)
- The evidence strength (from evidence evaluation)
- The Streitwert
- The user's goal (money? performance? injunction? vindication?)
- Timeline constraints (urgent? Verjährung approaching?)

---

## Step 2: RIS Verification

Before proceeding with analysis, follow the **RIS Verification Protocol** (`references/ris-protocol.md`):
1. Check RIS MCP availability
2. For every § you cite in this analysis, verify current wording via RIS
3. For case law references, retrieve via RIS Justiz
4. Record verification status for the Quellenstatus block
5. If RIS is unavailable, follow the fallback ladder and flag all affected citations

Search RIS Justiz for 3-5 relevant OGH decisions per key legal issue. Present using format from `references/ogh-case-presentation.md`.

---

## Step 3: Determine the Court

### Sachliche Zuständigkeit — which level of court?

Check in this order:
1. Is there a **special court**?
   - Arbeitsrecht → ASG (Arbeits- und Sozialgericht) per ASGG
   - Handelsrecht → Handelsgericht / Handelssenat per §51 JN
   - Mietrecht (MRG, WEG) → BG regardless of Streitwert per §49 Abs 2 Z 5 JN
   - Familienrecht → BG per §49 Abs 2 JN

2. If no special court: **Streitwert decides**
   - ≤ €15.000 → Bezirksgericht (BG)
   - > €15.000 → Landesgericht (LG) per §49 JN

### Örtliche Zuständigkeit — which location?

Check in this order:
1. Is there a valid **Gerichtsstandsvereinbarung** (§104 JN)?
   - In B2C: Only valid per §14 KSchG if at user's Wohnsitz
2. Is there a **besonderer Gerichtsstand**?
   - Erfüllungsort (§88 JN), Schadenort (§92a JN), Liegenschaft (§81 JN)
3. Default: **Wohnsitz/Sitz des Beklagten** (§66 JN)

State: "Zuständig ist das [BG/LG] [Ort]."

---

## Step 4: Select the Best Procedure

Evaluate these options and recommend the best one:

**Option A: Außergerichtliche Einigung**
- When: Claims are clear, opponent seems reasonable, preserving relationship matters
- How: Mahnschreiben mit Fristsetzung (14 Tage)
- Cost: Almost zero
- Recommend this FIRST in most cases

**Option B: Mahnverfahren (§§244ff ZPO)**
- When: Geldforderung (money claim), ≤ €75.000, claim is unambiguous
- How: Antrag auf Zahlungsbefehl at BG/LG
- Advantage: Halbe Gerichtsgebühr, schnell (Zahlungsbefehl in ~2 Wochen)
- Risk: If opponent files Einspruch (4 weeks) → normal streitiges Verfahren
- Recommend this for undisputed monetary claims

**Option C: Klage (streitiges Verfahren, ZPO)**
- When: Claim is disputed, non-monetary, or Mahnverfahren failed
- Duration: 6-18 months (1. Instanz), +6-12 months if Berufung
- Cost: Full GGG + RATG

**Option D: Einstweilige Verfügung (§§378ff EO)**
- When: URGENT — danger of irreparable harm, need immediate protection
- How: Antrag at zuständiges Gericht, can be ex parte
- Requires: Bescheinigung (lower standard than Beweis) of claim + Gefährdung
- Duration: Days to weeks
- Note: User may need to provide Sicherheitsleistung (security)

**Option E: Besitzstörungsverfahren (§§454ff ZPO)**
- When: Possession was disturbed
- ⚠️ **30 TAGE FRIST** — if more than 30 days since disturbance, this is gone
- Advantage: Schnellverfahren, no full Beweisaufnahme

**Option F: Mediation / Schlichtung**
- When: Relationship preservation important, both sides open to compromise
- Mandatory before BG-Klage in some Mietrecht cases (Schlichtungsstelle in Wien, Graz, etc.)
- Cost: €500-€3.000 for mediator

---

## Step 5: Assess Success Probability

For each claim, estimate probability based on:

1. **Legal basis strength** — Is the Anspruchsgrundlage solid? OGH precedent supporting?
2. **Evidence strength** — From evidence evaluation. Can user prove all elements?
3. **Defense risks** — What can the opponent argue? How strong are their defenses?
4. **Verjährung** — Any risk of time-bar?
5. **Judicial unpredictability** — Is this a grey area? Mixed OGH jurisprudence?

Rate: Probability of Obsiegen as percentage range.

---

## Step 6: Settlement Analysis

Calculate:

**BATNA (Best Alternative to Negotiated Agreement):**
= Expected value of winning at trial, minus litigation costs
= (probability of winning × amount won) - (GGG + RA costs)

**WATNA (Worst Alternative):**
= Amount lost if case fails + all litigation costs
= -(GGG + own RA + opponent RA + SV fees)

**Vergleichskorridor (Settlement Zone):**
= Range between WATNA and BATNA where settlement makes sense for both sides
= Typically: 40-70% of full claim value

State: "Ein Vergleich in der Höhe von €[low]-€[high] wäre wirtschaftlich sinnvoll."

---

## Step 7: Estimate Timeline

| Phase | Duration | What Happens |
|-------|----------|-------------|
| Außergerichtlich | 2-4 Wochen | Mahnschreiben, Verhandlungen |
| Klageeinbringung | 1 Woche | Klage einreichen |
| Klagebeantwortung | 4 Wochen | Frist für Beklagten |
| Vorbereitende Tagsatzung | 2-4 Monate | Gericht terminiert |
| Beweisaufnahme | 3-12 Monate | Zeugen, SV-Gutachten |
| Urteil 1. Instanz | 1-2 Monate | Nach Schluss der Verhandlung |
| Berufungsfrist | 4 Wochen | Ab Urteilszustellung |
| Berufungsverfahren | 4-8 Monate | Falls Berufung eingelegt |

Total realistic range: **6-24 Monate** for a typical civil case.

---

## Step 8: Present the Strategy

```markdown
# Prozessstrategie

**Sachverhalt:** [summary]
**Ihre Position:** [role]
**Streitwert:** €[amount]

## Empfohlene Vorgehensweise

### Phase 1: Außergerichtlich
- [Mahnschreiben senden mit Frist [x] Tage]
- [Optional: Mediationsangebot]

### Phase 2: Gerichtlich (falls nötig)
- **Verfahren:** [Mahnverfahren / Klage / EV]
- **Gericht:** [BG/LG] [Ort]
- **Verfahrensdauer:** ca. [x] Monate

## Erfolgsaussichten
| Anspruch | Grundlage | Wahrscheinl. | Begründung |
|----------|-----------|-------------|------------|
| [claim] | §[x] | [x]% | [reason] |

## Prozessrisiko-Matrix
| Szenario | Wahrscheinl. | Kosten | Dauer |
|----------|-------------|--------|-------|
| Vollständiges Obsiegen | [x]% | €[x] | [x] Mo. |
| Teilobsiegen | [x]% | €[x] | [x] Mo. |
| Unterliegen | [x]% | €[x] | [x] Mo. |
| Vergleich | [x]% | €[x] | [x] Mo. |

## Vergleichsanalyse
- **BATNA:** €[x]
- **WATNA:** -€[x]
- **Vergleichskorridor:** €[low] – €[high]
- **Empfehlung:** [Accept/reject settlement at €X]

## Zeitplan
[Timeline table from Step 6]

## ⚠️ Dringende Fristen
[Any imminent deadlines]

## Nächste Schritte
1. [First concrete action]
2. [Second]
3. [Third]

## Quellenstatus
| Kategorie | Status | Details |
|-----------|--------|---------|
| RIS MCP | 🟢 Verfügbar / 🔴 Nicht verfügbar | |
| Gesetze | RIS_VERIFIED / UNVERIFIED | [n] Normen geprüft |
| Judikatur | RIS_VERIFIED / UNVERIFIED | [n] Entscheidungen |
| Prüfdatum | [YYYY-MM-DD] | |

---
⚠️ Keine Rechtsberatung.
```
