---
name: legal-momarcode1
title: Austrian Legal Assistant — Rechtsassistent für österreichisches Recht
description: Austrian law assistant (Rechtsassistent) for Claude Code. Full case analysis, contract review, evidence evaluation, claim identification (Anspruchsprüfung), litigation strategy, cost estimation (GGG/RATG), statute of limitations (Verjährung), tax law (Steuerrecht), asylum/immigration (Asyl/Fremdenrecht), social security (Sozialrecht), legal research via RIS, and PDF reports. 34 skills, 6 parallel agents. Covers contracts, disputes, tax (EStG/KStG/UStG), asylum (AsylG/FPG/NAG), social security (ASVG/AlVG/BPGG), tenancy (MRG), employment (AngG/ArbVG), family law (EheG/Unterhalt), inheritance (Erbrecht/Pflichtteil), traffic (EKHG/StVO), consumer protection (KSchG/FAGG), debt/enforcement (EO/IO). Use this skill whenever the user mentions Austrian law or any Austrian statute.
author: MoMarcode1
author_url: https://github.com/MoMarcode1/austrian-legal-claude/tree/main/legal
license: MIT
version: 0.1.1
execution_mode: open
jurisdiction: at
practice: general
language: en
sources:
- title: Common output rules
  path: references/common-output-rules.md
- title: Ogh case presentation
  path: references/ogh-case-presentation.md
- title: Ris protocol
  path: references/ris-protocol.md
---

# Austrian Legal Assistant — Rechtsassistent für österreichisches Recht

AI-powered legal analysis for Austrian law. 34 specialized skills, 6 parallel agents.

> ⚠️ **Keine Rechtsberatung.** This tool provides preliminary legal analysis. It does not replace
> consultation with a licensed Austrian attorney (Rechtsanwalt).

---

## Commands

### Case & Dispute Analysis

| Command | What It Does |
|---------|-------------|
| `/recht review <file>` | **Flagship** — Full contract/document review with 5 parallel agents. Returns a Safety Score, clause analysis, and Austrian law compliance check. |
| `/recht risks <file>` | Deep risk analysis with severity scoring for every clause. Estimates financial exposure under Austrian law. |
| `/recht claim <facts>` | **Anspruchsprüfung** — Identifies all legal claims from facts. Maps each to specific §§, checks elements, defenses, and burden of proof. |
| `/recht evidence <file>` | **Beweiswürdigung** — Evaluates evidence strength per ZPO (Urkunden, Zeugen, Sachverständige, etc.). Flags gaps. |
| `/recht costs <streitwert>` | **Kostenrechner** — Calculates GGG court fees + RATG attorney fees for any Streitwert. Full cost/risk matrix. |
| `/recht strategy <facts>` | **Prozessstrategie** — Litigation strategy with success probability, court selection, timeline, and settlement corridor. |
| `/recht klage <facts>` | **Schriftsatz-Entwurf** — Drafts Klage, Klagebeantwortung, Berufung, Mahnschreiben, or einstweilige Verfügung. |
| `/recht verjährung <facts>` | **Verjährungsprüfung** — Checks all applicable limitation periods. Flags imminent deadlines. |

### Contract Tools

| Command | What It Does |
|---------|-------------|
| `/recht compare <file1> <file2>` | Side-by-side comparison of two contract versions. Flags changes and new risks. |
| `/recht plain <file>` | Translates legal German (Juristendeutsch) into plain language (Klartext). |
| `/recht negotiate <file>` | Generates counter-proposals with replacement language for unfavorable clauses. |
| `/recht missing <file>` | Finds clauses that SHOULD be in the contract under Austrian law but are missing. |

### Compliance & Reporting

| Command | What It Does |
|---------|-------------|
| `/recht compliance <file/url>` | Compliance analysis — KSchG, DSGVO, DSG, GewO, MRG, UGB, ArbVG. |
| `/recht report-pdf` | Professional PDF report with risk scores, cost estimates, and recommendations. |

### Steuerrecht (Tax Law)

| Command | What It Does |
|---------|-------------|
| `/recht steuer <facts>` | **Steueranalyse** — EStG, KStG, UStG, KommStG, with optimization recommendations. |
| `/recht steuer-verfahren <facts>` | **Abgabenverfahren** — Beschwerde, Vorlageantrag, BFG, Selbstanzeige, Stundung. |

### Asyl- & Fremdenrecht (Asylum & Immigration)

| Command | What It Does |
|---------|-------------|
| `/recht asyl <facts>` | **Asylanalyse** — AsylG, FPG, NAG, RWR-Karte, subsidiärer Schutz, Familiennachzug. |
| `/recht asyl-beschwerde <facts>` | **Asylbeschwerde** — BFA-Bescheid anfechten, BVwG, VfGH/VwGH, aufschiebende Wirkung. |

### Sozialrecht (Social Security)

| Command | What It Does |
|---------|-------------|
| `/recht sozial <facts>` | **Sozialrechtsanalyse** — ASVG, Pension, AlVG, Pflegegeld, Mindestsicherung. |
| `/recht sozial-beschwerde <facts>` | **Sozialrechtsbeschwerde** — ASG-Klage, AMS-Sperre, Pflegestufe, §77 ASGG Kostenfreiheit. |

### Mietrecht (Tenancy)

| Command | What It Does |
|---------|-------------|
| `/recht miet <file/facts>` | **Mietrechtsanalyse** — MRG-Anwendbarkeit, Mietzins, Befristung, Kündigung, Erhaltung. |
| `/recht miet-verfahren <facts>` | **Mietrechtsverfahren** — Schlichtungsstelle, Mietzinsüberprüfung, Räumungsklage. |

### Arbeitsrecht (Employment)

| Command | What It Does |
|---------|-------------|
| `/recht arbeit <file/facts>` | **Arbeitsrechtsanalyse** — Vertrag, KollV, AZG, Kündigung, Konkurrenzklausel. |
| `/recht arbeit-verfahren <facts>` | **Arbeitsrechtsverfahren** — Kündigungsanfechtung, ASG, Entlassungsanfechtung. |

### Familienrecht (Family Law)

| Command | What It Does |
|---------|-------------|
| `/recht familie <facts>` | **Familienrechtsanalyse** — Scheidung, Unterhalt, Obsorge, Kontaktrecht, Aufteilung. |
| `/recht familie-verfahren <facts>` | **Familienrechtsverfahren** — Scheidungsantrag, Unterhaltsklage, einstweilige Verfügung. |

### Erbrecht (Inheritance)

| Command | What It Does |
|---------|-------------|
| `/recht erbe <facts>` | **Erbrechtsanalyse** — Erbfolge, Testament, Pflichtteil, Schenkungsanrechnung. |
| `/recht erbe-verfahren <facts>` | **Erbrechtsverfahren** — Verlassenschaft, Pflichtteilsklage, Testamentsanfechtung. |

### Verkehrsrecht (Traffic)

| Command | What It Does |
|---------|-------------|
| `/recht verkehr <facts>` | **Verkehrsrechtsanalyse** — Unfallhaftung, Führerschein, Strafen, Versicherung. |
| `/recht verkehr-verfahren <facts>` | **Verkehrsrechtsverfahren** — Einspruch, Schadenersatzklage, Führerscheinentzug. |

### Verbraucherrecht (Consumer Protection)

| Command | What It Does |
|---------|-------------|
| `/recht verbraucher <facts>` | **Verbraucherrecht** — Gewährleistung, FAGG-Rücktritt, KSchG, Produkthaftung. |
| `/recht verbraucher-verfahren <facts>` | **Verbraucherverfahren** — Mängelrüge, Rücktritt, Schlichtung, Klage. |

### Schulden & Exekution (Debt & Enforcement)

| Command | What It Does |
|---------|-------------|
| `/recht schulden <facts>` | **Schuldenanalyse** — Inkasso, Mahnverfahren, Insolvenz, Existenzminimum. |
| `/recht exekution <facts>` | **Exekutionsverfahren** — Lohnpfändung, Oppositionsklage, Privatinsolvenz. |

---

## How the Flagship `/recht review` Works

5 AI agents launch in parallel:

| Agent | Role | Weight |
|-------|------|--------|
| Klauselanalyst | Identifies and categorizes every clause, maps to Austrian law | 20% |
| Risikobewerter | Scores each clause for risk under Austrian standards | 25% |
| Compliance-Prüfer | Flags KSchG, DSGVO, MRG, UGB violations | 20% |
| Pflichten-Mapper | Maps obligations, deadlines, Fristen, and triggers | 15% |
| Empfehlungsmotor | Generates specific fixes with Austrian law citations | 20% |

Results are aggregated into a unified report with a **Vertragssicherheits-Score (0-100)**.

---

## Legal Areas Covered

| Area | Key Laws |
|------|----------|
| Zivilrecht | ABGB, KSchG |
| Unternehmensrecht | UGB, GmbHG, AktG |
| Arbeitsrecht | AngG, AVRAG, ArbVG, AZG, UrlG, GlBG, ASVG |
| Mietrecht | MRG, WEG, ABGB §§1090ff |
| Strafrecht | StGB, StPO, SMG |
| Verwaltungsrecht | AVG, VwGVG, GewO, BauO |
| Datenschutz/IP | DSG, DSGVO, UrhG, MSchG, PatG |
| Familienrecht | ABGB 2. Teil, EheG, KindNamRÄG |
| Erbrecht | ABGB 5. Teil, AußStrG |
| Insolvenzrecht | IO, URG |
| Exekutionsrecht | EO |
| Verfahrensrecht | ZPO, JN, ASGG, AußStrG |

---

## RIS Integration

This skill works best with the **RIS MCP Server** for live Austrian law lookup:
- GitHub: https://github.com/philrox/ris-mcp-ts
- 12 tools: Bundesnormen, Landesnormen, Justiz (OGH/VfGH/VwGH), BGBl, and more

If RIS MCP is unavailable, skills fall back to web search on https://www.ris.bka.gv.at

---

## Bilingual Support

- Accepts input in German or English
- Output language matches input language
- Legal terms always include German original: "statute of limitations (Verjährung)"
- Statutes cited in official form: §922 ABGB, not "Section 922 Civil Code"

---

## Command Routing

When the user types a `/recht` command, route to the corresponding sub-skill:

### Case & Dispute Analysis
```
/recht review      → skills/recht-review/SKILL.md
/recht risks       → skills/recht-risks/SKILL.md
/recht claim       → skills/recht-claim/SKILL.md
/recht evidence    → skills/recht-evidence/SKILL.md
/recht costs       → skills/recht-costs/SKILL.md
/recht strategy    → skills/recht-strategy/SKILL.md
/recht klage       → skills/recht-klage/SKILL.md
/recht verjährung  → skills/recht-verjährung/SKILL.md
```

### Contract Tools
```
/recht compare     → skills/recht-compare/SKILL.md
/recht plain       → skills/recht-plain/SKILL.md
/recht negotiate   → skills/recht-negotiate/SKILL.md
/recht missing     → skills/recht-missing/SKILL.md
```

### Compliance & Reporting
```
/recht compliance  → skills/recht-compliance/SKILL.md
/recht report-pdf  → skills/recht-report-pdf/SKILL.md
```

### Steuerrecht (Tax Law)
```
/recht steuer           → skills/recht-steuer/SKILL.md
/recht steuer-verfahren → skills/recht-steuer-verfahren/SKILL.md
```

### Asyl- & Fremdenrecht (Asylum & Immigration)
```
/recht asyl             → skills/recht-asyl/SKILL.md
/recht asyl-beschwerde  → skills/recht-asyl-beschwerde/SKILL.md
```

### Sozialrecht (Social Security)
```
/recht sozial           → skills/recht-sozial/SKILL.md
/recht sozial-beschwerde → skills/recht-sozial-beschwerde/SKILL.md
```

### Mietrecht (Tenancy)
```
/recht miet             → skills/recht-miet/SKILL.md
/recht miet-verfahren   → skills/recht-miet-verfahren/SKILL.md
```

### Arbeitsrecht (Employment)
```
/recht arbeit           → skills/recht-arbeit/SKILL.md
/recht arbeit-verfahren → skills/recht-arbeit-verfahren/SKILL.md
```

### Familienrecht (Family Law)
```
/recht familie           → skills/recht-familie/SKILL.md
/recht familie-verfahren → skills/recht-familie-verfahren/SKILL.md
```

### Erbrecht (Inheritance)
```
/recht erbe             → skills/recht-erbe/SKILL.md
/recht erbe-verfahren   → skills/recht-erbe-verfahren/SKILL.md
```

### Verkehrsrecht (Traffic)
```
/recht verkehr           → skills/recht-verkehr/SKILL.md
/recht verkehr-verfahren → skills/recht-verkehr-verfahren/SKILL.md
```

### Verbraucherrecht (Consumer Protection)
```
/recht verbraucher           → skills/recht-verbraucher/SKILL.md
/recht verbraucher-verfahren → skills/recht-verbraucher-verfahren/SKILL.md
```

### Schulden & Exekution (Debt & Enforcement)
```
/recht schulden    → skills/recht-schulden/SKILL.md
/recht exekution   → skills/recht-exekution/SKILL.md
```

### Shared References
All skills MUST follow:
- `references/ris-protocol.md` — RIS verification workflow
- `references/ogh-case-presentation.md` — OGH case law format
- `references/common-output-rules.md` — shared output standards

If no command is specified, analyze the user's request and route to the most appropriate skill.
If the request spans multiple skills, orchestrate them in sequence.
