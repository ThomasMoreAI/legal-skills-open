---
name: research-court-procedure-lookup-sboghossian
title: Court Procedure Lookup
description: Use when a lawyer or litigant needs a structured checklist of procedural requirements for a specific court and matter type — covering initial filings, fees, service of process, response deadlines, discovery regime, witness rules, cost frameworks, and appeal tracks. Covers DIFC Courts, ADGM Courts, UAE onshore civil courts, Saudi courts (General, Commercial, Labor, Administrative), Lebanese courts, English High Court, and leading MENA arbitration institutions (DIAC, LCIA, SCCA). MENA-first; distinguishes civil-law from common-law procedure.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/research/research-court-procedure-lookup
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: en
---

# Court Procedure Lookup

Structured procedural checklist for a given court and matter type. Covers the required filings, fees, deadlines, service rules, disclosure regime, witness framework, costs allocation, and appeal pathway. Designed for lawyers preparing to file or respond to proceedings, and for clients assessing forum options.

## When to use this

- Preparing to file a claim and needing a step-by-step filing checklist
- Advising a client on what to expect procedurally in a specific forum
- Comparing forums (e.g., DIFC arbitration vs DIAC vs English High Court) on procedural grounds
- Checking response deadlines after receiving a claim
- Understanding what discovery / disclosure the other side can compel
- Evaluating appeal timelines for deal structuring or enforcement strategy

## Inputs

| Input | Why it matters | Default |
|-------|---------------|---------|
| Court / forum | Procedure varies completely between forums | Required |
| Matter type | Commercial claim, employment, IP, real estate, family, criminal — each has a distinct track | Required |
| Amount in dispute (approximate) | Affects court track, filing fee, and whether arbitration carve-outs apply | Provide if known |
| Claimant or respondent perspective | Shapes which deadlines and requirements are immediately relevant | State perspective |
| Arbitration or litigation? | Fundamentally different regimes | Infer from context |

## Jurisdiction coverage and procedural frameworks

### DIFC Courts (Dubai International Financial Centre)

**Applicable rules**: DIFC Courts Practice Direction and Rules of Court (English common-law procedure); DIFC Law No. 10 of 2004 as amended.

| Procedural step | Details |
|----------------|---------|
| Initial filing | Claim Form (small claims: Form 1; full track: Form CF-1) + Particulars of Claim; filed via e-registry |
| Filing fee | Scaled by claim value (approx. 3–5% of claim value, capped); check DIFC Courts fee schedule for current amounts |
| Service | Service within DIFC: personal or by post to registered address; outside DIFC: service out requires court permission; may serve via Dubai courts or Hague Convention |
| Response deadline | 21 days after service (within UAE); 35 days (outside UAE); acknowledgment of service within 14 days |
| Pre-trial disclosure | English-style standard disclosure (relevant documents) — a key difference from civil-law forums |
| Witness evidence | Witness statements filed in advance; oral cross-examination at hearing |
| Costs | "Costs follow the event" — loser generally pays winner's costs (assessed on standard or indemnity basis) |
| Appeal | Court of Appeal within 28 days of judgment; permission may be required |
| Interim relief | Urgent injunctions available same-day; freezing orders widely used |

### ADGM Courts (Abu Dhabi Global Market)

**Applicable rules**: ADGM Courts, Civil Evidence, Judgments, Enforcement and Judicial Appointments Regulations 2015; ADGM Court Procedure Rules.

Procedure is substantially similar to DIFC Courts (English common-law base). Key differences:
- Enforcement directly within ADGM and via Abu Dhabi courts
- ADGM Court of First Instance and Appellate Body
- ADGM Arbitration Centre (ADGMAC) available for seat

### UAE Onshore Civil Courts (Federal / Emirate-level)

**Applicable rules**: UAE Civil Procedure Code (Federal Law No. 11 of 1992, as amended by Federal Decree-Law No. 42 of 2022); per-emirate implementing rules.

| Procedural step | Details |
|----------------|---------|
| Initial filing | Statement of Claim (Arabic) filed at relevant court (Dubai Court, Abu Dhabi Court, etc.); exhibits attached |
| Filing fee | Set by court fee schedule; typically 5% of claim value (commercial); varies by emirate and court type |
| Service | Court-managed service; process server or court bailiff; publication if respondent cannot be located; electronic service now recognized |
| Response deadline | 15–30 days from service (varies by court); defenses filed in writing |
| Discovery / Disclosure | **Inquisitorial (civil-law)**: no pre-trial discovery as understood in common law; parties submit their own evidence; judge may request documents; expert witnesses appointed by the court |
| Witness evidence | Written testimony common; oral hearings less frequent in commercial courts; experts typically court-appointed |
| Costs | Each party typically bears own costs; adverse costs orders less common than in English courts |
| Appeal | Court of Appeal (within 30 days of judgment); Court of Cassation on points of law |
| DIFCCD | The Dubai International Financial Centre Court of First Instance has jurisdiction if the dispute "relates to or arises from" a DIFC contract even if parties are not DIFC-registered — check carefully |

### Saudi Arabia — Court System

Saudi Arabia has multiple specialized court tracks:

**General Courts** (civil / personal status)
- Civil Procedure Law (Royal Decree M/1 of 2000, as amended)
- Arabic proceedings; litigants must use Saudi-licensed advocates
- First instance → Court of Appeal → Supreme Court

**Commercial Courts** (established 2017, Royal Decree M/93)
- Handles commercial disputes including corporate, banking, and intellectual property
- Faster track than general courts; dedicated commercial bench
- Filing: Najiz e-filing portal; Arabic

**Labor Courts**
- Disputes between employees and employers
- Employee-favorable: no filing fee for employees
- Mandatory conciliation before hearing (Labour Ministry mediation first)
- Statute of limitations: 12 months from termination

**Administrative Courts (Diwan al-Mazalim / Board of Grievances)**
- Disputes with government entities and government contracts
- Increasingly important for construction, infrastructure, and public procurement disputes
- Separate procedural rules; specialized judges

**Saudi Center for Commercial Arbitration (SCCA)**
- Arbitration Rules (2023 revision); seat is Riyadh by default
- Arabic or English proceedings available
- SCCA awards enforced under Saudi Arbitration Law (Royal Decree M/34 of 2012)
- Not a signatory to the New York Convention as of latest available information — enforcement of foreign awards requires mutual treaty (Riyadh Convention / bilateral treaties)

### Lebanon — Court System

**Applicable rules**: Code of Civil Procedure (Decree-Law No. 90 of 1983, as amended).

| Track | Forum | Notes |
|-------|-------|-------|
| Civil | Juge des Référés (urgent), Tribunal Civil, Cour d'Appel, Cour de Cassation | French-influenced civil procedure |
| Commercial | Commercial Tribunals (Tribunaux de Commerce) in Beirut, Tripoli, Sidon | Faster track for commercial disputes |
| Labor | Labor courts per region | Employee-protective; mandatory conciliation |
| Administrative | Conseil d'État / Shura (administrative law) | Rare for private commercial disputes |
| Criminal | Juge d'instruction (investigating judge) → Criminal Court | Investigating judge system — distinct from common law |

**Practical reality note**: Lebanon's court system has been severely impacted by the economic and political crisis since 2019. Delays of several years are common. Many practitioners route to DIAC, ICC, or LCIA arbitration with execution in other jurisdictions to avoid Lebanese court delays.

### English High Court (Commercial)

**Applicable rules**: Civil Procedure Rules (CPR 1998) + Commercial Court Guide.

| Procedural step | Details |
|----------------|---------|
| Initial filing | Claim Form (N1) + Particulars of Claim; Queen's Bench Division / Commercial Court (CPR Part 7 or 8) |
| Filing fee | Scaled to claim value (up to £10,000 for largest claims; see current HMCTS fee schedule) |
| Service | Personal service or first-class post to last known address; 4 months to serve within England; longer for service out |
| Response deadline | 14 days (acknowledgment); 28 days (full defence) |
| Disclosure | Disclosure Pilot (PD 57AD): disclosure review documents, less than full Peruvian Guano; high-value cases may require Extended Disclosure |
| Witness evidence | Witness statements; cross-examination; expert evidence requires court permission |
| Costs | Costs follow the event (loser pays); detailed assessment if disputed |
| Appeal | Court of Appeal within 21 days of judgment; permission required |

### Arbitration Institutions (MENA Focus)

| Institution | Rules | Seat options | Language | Notes |
|---|---|---|---|---|
| **DIAC** (Dubai International Arbitration Centre) | 2022 Rules | Dubai (Onshore or DIFC) | Arabic / English | Post-2021 absorbed DIFC-LCIA caseload; active MENA institution |
| **LCIA** (London Court of International Arbitration) | 2020 Rules | London default; any seat | English | Popular for international commercial disputes; recognized globally |
| **DIAC-LCIA** (now DIAC 2022) | — | Dubai | Arabic / English | DIFC-LCIA officially merged into DIAC in 2021 |
| **SCCA** (Saudi Center for Commercial Arbitration) | 2023 Rules | Riyadh default | Arabic / English | Growing caseload for KSA-nexus disputes |
| **ICC** (International Chamber of Commerce) | 2021 Rules | Any | Any | Gold standard for very large cross-border transactions |
| **HKIAC** | 2018 Rules | Hong Kong | Any | Popular for Asia-nexus; some MENA usage |
| **SIAC** | 2016 Rules | Singapore | Any | Popular for Asia-MENA transactions |

**Number of arbitrators rule of thumb**: 1 arbitrator for disputes < USD 5 million; 3 arbitrators for disputes ≥ USD 5 million. Override for complexity or party agreement.

**New York Convention**: UAE (including DIFC/ADGM) is a signatory; Lebanon is a signatory; KSA is NOT a party to the New York Convention — enforcement of foreign awards in KSA requires the Riyadh Arab Convention or a bilateral treaty.

## Output structure

For the requested forum and matter type, produce:

```
## [Forum] — [Matter Type] — Procedural Checklist

**Applicable rules**: [cite the current procedural code]

**Immediate deadlines**:
- [N days] from [trigger event] to [filing/response required]

**Required initial filings**:
1. [Document name] — [description, form number if applicable]
2. …

**Filing fees**: [amount or formula, with link to current schedule]

**Service rules**: [how, by whom, to whom, within what timeframe]

**Disclosure / discovery regime**: [inquisitorial or adversarial; scope; timeline]

**Witness rules**: [written statements / oral / expert appointment]

**Costs framework**: [loser pays / each side bears / judicial discretion]

**Appeal track**: [court / arbitral appeal body] within [N days] of [judgment / award]

**Interim relief available**: [yes/no; form; timeframe for emergency relief]

**Practical notes**: [jurisdiction-specific traps or efficiencies]

**Citations**: [court rules + procedural law with article/rule numbers]
```

## Limits and escalation

- Court fee schedules change; always verify current amounts from the court's official website before filing.
- Procedural rules are amended periodically; verify currency of cited rules via [[research-recent-amendments-tracker]].
- This checklist does not substitute for jurisdiction-qualified legal advice on strategy, pleading standards, or evidence admissibility.
- For multi-jurisdictional parallel proceedings (e.g., simultaneous DIFC and onshore Dubai proceedings), escalate to [[research-deep-research-orchestrator]] for a coordinated analysis.

## Related skills

- [[research-case-law-search]]
- [[research-statute-of-limitations-lookup]]
- [[review-dispute-resolution-mechanism-fit]]
- [[research-regulation-lookup]]
- [[research-recent-amendments-tracker]]
