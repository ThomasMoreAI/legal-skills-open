---
name: mdr-745-specialist-aashutosh396
title: Classification (Annex VIII)
description: Use when classifying a medical device under MDR, building or gap-checking a technical file, planning clinical evaluation or PMS/PSUR cadence, or preparing for notified body review — covers Annex VIII rules, Annex II/III, Annex XIV, UDI, EUDAMED.
author: aashutosh396
author_url: https://github.com/aashutosh396/mindpalace/tree/main/mindpalace/skills/global/compliance/mdr-745-specialist
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: eu
practice: life-sciences
language: en
tags: [eu-mdr, mdr-2017-745, device-classification, annex-viii, technical-documentation, clinical-evaluation, pmcf, psur, eudamed, udi]
---

EU MDR compliance: classification, technical documentation, clinical evidence, post-market surveillance.

## Classification (Annex VIII)
Identify duration (transient/short/long-term) → invasiveness (non-invasive/orifice/surgical) → body-system contact (CNS, cardiac, other) → active device? → apply rules 1-22 → software via MDCG 2019-11 → document rationale. *Validation: confirmed with Notified Body.*
| Factor | Class I | IIa | IIb | III |
|---|---|---|---|---|
| Duration | Any | Short | Long | Long |
| Invasiveness | Non-invasive | Orifice | Surgical | Implantable |
| System | Any | Non-critical | Critical organs | CNS/cardiac |
**Software (MDCG 2019-11):** informs decision + non-serious = IIa · informs + serious = IIb · drives/treats + critical = III.
Examples: absorbable suture (Rule 8 long-term) = IIb · AI diagnostic of serious condition (Rule 11) = IIb · pacemaker (Rule 8 central circulatory) = III.

## Technical documentation (Annex II/III)
Device description (variants, accessories, intended purpose) · labeling (Art. 13, IFU) · design/manufacturing · GSPR compliance matrix · benefit-risk · V&V evidence · risk management file (ISO 14971) · clinical evaluation report.
GSPR checklist row: requirement · evidence · status (e.g., safe design GSPR 1-3 → risk file · chemical 10.1 → biocompatibility · infection 10.2 → sterilization validation · software 17 → IEC 62304 · labeling 23 → artwork/IFU).
**Conformity routes:** I = Annex II self-declaration · Is/Im = + IX/XI (sterile/measuring) · IIa = II + IX or XI · IIb = IX or X+XI · III = full QMS + dossier or type exam + production.

## Clinical evidence (Annex XIV)
Define claims/endpoints → systematic literature search → appraise data quality → assess equivalence (technical/biological/clinical) → identify gaps → determine if investigation needed → Clinical Evaluation Report. *Validation: CER reviewed by qualified evaluator (medical degree + 4yr clinical experience + CE methodology training).*
Evidence by class: I = risk-benefit · IIa = literature + post-market · IIb = systematic review (investigation often required) · III = comprehensive clinical data + investigation (Art. 61).
CER structure: exec summary · scope/intended purpose · clinical background (state of the art) · literature methodology · data appraisal · safety/performance conclusions · benefit-risk · PMCF plan.

## Post-market surveillance (Chapter VII)
PMS plan (Art. 84) · PSUR (Art. 86, Class IIa+) · PMCF plan (Annex XIV-B) · PMCF report (annual Class III) · vigilance (Arts 87-92). *Validation: audited annually.*
**PSUR schedule (Art. 86(1)):** Class III annually · IIb (incl. implantable) annually · IIa ≥ every 2 years · Class I no PSUR (PMS report instead, Art. 85).
**Serious incident reporting:** 2 days (serious public health threat) · 10 days (death/serious deterioration) · 15 days (other serious incidents).

## EUDAMED & UDI (Art. 27)
Obtain issuing-entity code (GS1/HIBCC/ICCBBA) → assign UDI-DI per variant → UDI-PI (production identifier) → apply carrier (AIDC + HRI) → register actor + devices in EUDAMED → upload certificates. UDI label (Art. 13): UDI-DI · UDI-PI (Class II+) · AIDC barcode/RFID · HRI human-readable · manufacturer name/address · lot/serial · expiration. EUDAMED modules: Actor · UDI/Device · Certificates (NB) · Clinical Investigation · Vigilance · Market Surveillance.

## NB pre-submission checklist
Technical documentation complete · GSPR matrix fully addressed · risk file current · CER complete · ISO 13485 certified · labeling/IFU finalized · internal gap assessment done.
