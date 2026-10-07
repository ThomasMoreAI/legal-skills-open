---
name: wcc-bih-jeannesulzer
title: WCC-BiH — War Crimes Chamber of the Court of Bosnia and Herzegovina
description: 'War Crimes Chamber of the Court of Bosnia and Herzegovina (WCC-BiH) — Section I (War Crimes) of the State Court — research, drafting, and analysis. Use whenever the conversation involves the Court of BiH war crimes docket, the Special Department for War Crimes (SDWC), ICTY Rule 11 bis referrals (Stanković, Janković, Mejakić), the ICTY Completion Strategy, the hybrid-to-national transition of the bench, the 2008 National War Crimes Processing Strategy, or the Maktouf-Damjanović lex mitior line. Distinct from entity-level prosecutions in the Federation, Republika Srpska and Brčko District. Enforces a verification-first discipline: every case-law, decision, indictment, or judgment citation must be verified against sudbih.gov.ba or institutional archives before appearing in any output. Foundational texts (Law on the Court of BiH, Criminal Code of BiH 2003, Criminal Procedure Code 2003) may be cited from project knowledge when present. Trigger on WCC, Sud BiH, State Court of Bosnia,
  Rule 11 bis, or SDWC.'
author: jeannesulzer
author_url: https://github.com/jeannesulzer/international-criminal-tribunals-skills/tree/main/wcc-bih
license: CC-BY-4.0
version: 0.1.1
execution_mode: open
jurisdiction: ba
practice: criminal
language: en
sources:
- title: Authoritative Sources
  path: references/authoritative-sources.md
- title: Citation Format
  path: references/citation-format.md
- title: Foundational Texts
  path: references/foundational-texts.md
- title: Jurisprudence Map
  path: references/jurisprudence-map.md
- title: Verification Workflow
  path: references/verification-workflow.md
---

# WCC-BiH — War Crimes Chamber of the Court of Bosnia and Herzegovina

This skill governs every output that touches the War Crimes Chamber of the Court of Bosnia and Herzegovina — known formally as **Section I (War Crimes) of the Criminal Division of the State Court of Bosnia and Herzegovina** (*Sud Bosne i Hercegovine*). The discipline is simple and the reason for it is concrete: the WCC-BiH is the **largest national war crimes prosecution apparatus** in the former Yugoslavia and operates as the principal complement to the ICTY's Completion Strategy. Its caseload — referrals from the ICTY under Rule 11 bis, plus locally-initiated cases — has produced the most substantial body of contemporary national jurisprudence on Yugoslav-conflict crimes.

## The discipline in one paragraph

For any case-specific document — judgment, decision, indictment, filing — verify before citing. "Verify" means `web_fetch` (or equivalent retrieval) to the **Court of BiH official website (sudbih.gov.ba)** or to a Tier 1 mirror (the OSCE Mission to BiH archive, ICTY referral documents on the IRMCT/ICTY archives, the ICC Legal Tools Database) in the current conversation. Foundational texts in project knowledge (Law on the Court of BiH 2002, Criminal Code of BiH 2003, Criminal Procedure Code of BiH 2003) are the exception; they may be cited directly. Nothing else.

## Verification is gradient, not binary

WCC-BiH has produced a very substantial caseload (hundreds of cases since 2005). Three levels:

- **Existence verified.** Case name, parties, date, chamber and document type confirmed against an authoritative source.
- **Content verified.** The fetched text confirms the proposition in substance.
- **Paragraph verified.** The specific cited paragraph or page contains the cited proposition.

Label the level where relevant. WCC-BiH judgments are typically structured by paragraph numbers in both BCS and English versions.

## Standard workflow

**Step 0 — Identify the document.** Before anything else, distinguish:

- **First-instance judgment** of the **Trial Panel** (originally 2 international + 1 national judges; from 2009, fully national)
- **Appeal judgment** of the **Appellate Panel** of the State Court of BiH
- **Indictment** of the **Special Department for War Crimes (SDWC)** of the Prosecutor's Office of BiH
- **Pre-trial decisions** including those on Rule 11 bis referrals from ICTY
- **Constitutional Court of BiH** decisions on WCC-BiH proceedings (notably on the application of the 2003 Criminal Code vs. the 1976 SFRY Criminal Code — see Trap 1 below)

**Step 1 — Plan citations.** List every citation and the proposition it supports. Distinguish ICTY-referred cases (Rule 11 bis) from locally-initiated cases.

**Step 2 — Verify with the fallback ladder.** sudbih.gov.ba → OSCE Mission to BiH archive → ICTY/IRMCT archives (for Rule 11 bis referral documents) → legal-tools.org → ICTJ reports → HRW reports → academic commentary → ask the user.

**Step 3 — Draft using verified material.** Use the citation format in `references/citation-format.md`.

**Step 4 — Self-audit.** Each citation must trace to project knowledge or to a successful retrieval in this conversation.

## Foundational texts (cite from project knowledge when present)

- **Law on the Court of Bosnia and Herzegovina** — adopted by the BiH Parliament 3 July 2002 (Official Gazette of BiH 49/09 consolidated). Establishes the Court of BiH with state-level jurisdiction; provides for Section I (War Crimes), Section II (Organized Crime, Corruption, Economic Crime), Section III (General Crime).
- **Law on the Prosecutor's Office of Bosnia and Herzegovina** — establishes the Special Department for War Crimes (SDWC).
- **Criminal Code of Bosnia and Herzegovina** — adopted 2003, in force from 1 March 2003 (Official Gazette of BiH 3/03 with amendments). Defines war crimes, crimes against humanity, genocide.
- **Criminal Procedure Code of Bosnia and Herzegovina** — adopted 2003. Defines proceedings before the State Court.
- **Rules of Procedure of the Court of Bosnia and Herzegovina** — internal court rules.
- **National War Crimes Processing Strategy** — adopted by the BiH Council of Ministers in December 2008 (revised 2018, 2020). Defines case-allocation criteria between State Court and entity/cantonal courts; sets timeframes (most complex cases within 7 years, others within 15).
- **ICTY Rules of Procedure and Evidence, Rule 11 bis** — the rule governing referrals from ICTY to national jurisdictions. Multiple WCC-BiH cases proceeded under this rule.

If not in project knowledge, retrieve from sudbih.gov.ba or legal-tools.org.

## The institutional architecture (get this right)

- **Established by:** Law on the Court of BiH of **3 July 2002** (Parliament); Court of BiH operational **January 2003**; **WCC officially began operations 9 March 2005** in Sarajevo.
- **Initiative origin:** Joint **OHR (Office of the High Representative) + ICTY** initiative. Recommended in 2002 as part of the ICTY Completion Strategy.
- **Seat:** Sarajevo, Bosnia and Herzegovina (within the Court of BiH building).
- **Structure:**
  - **Section I (War Crimes)** within the **Criminal Division of the State Court of BiH**
  - **Special Department for War Crimes (SDWC)** within the **Prosecutor's Office of BiH**
  - Separate appellate division within the Court of BiH
- **Composition — international/national transition:**
  - **Phase I (2005-2008):** Each trial and appeal panel = **2 international judges + 1 national judge**
  - **Phase II (2008-2009):** Gradual transition to **2 national judges + 1 international judge**
  - **Phase III (from 2009/2012):** Fully national composition. International judges phased out by end of 2012; international prosecutors phased out by end of 2009
- **President of the Court of BiH at WCC creation:** Meddžida Kreso
- **First Chief Prosecutor of BiH:** Marinko Jurčević
- **Mandate:** **no time limit**. The WCC-BiH continues to operate as a fully nationalised institution. As of 2026, hundreds of cases have been processed.
- **Distinguishing features:**
  - **Domestic-international hybrid model with a programmed phase-out** — designed from the outset to transition to fully national composition. Distinct from "permanent hybrid" models (ECCC, KSC).
  - **First national court with jurisdiction over international crimes in BiH** at state level (entity-level prosecutions already existed)
  - **Principal recipient of ICTY Rule 11 bis transfers** (alongside Croatian and Serbian War Crimes Chambers)
  - **State-level jurisdiction** alongside parallel **entity-level prosecutions** in the Federation of BiH (FBiH), Republika Srpska (RS), and Brčko District — the WCC-BiH is not the only forum for BiH war crimes prosecutions (this matters — see Trap 4 below)

## Source hierarchy

**Tier 1 (authoritative):**
- **sudbih.gov.ba** — the official website of the Court of BiH. Hosts all judgments, decisions, indictments. Available in BCS and English. The primary source for verification.
- **tuzilastvobih.gov.ba** — Prosecutor's Office of BiH official website. For indictments from the SDWC.
- **ICTY/IRMCT archives** (irmct.org, icty.org legacy) — for **Rule 11 bis referral documents** and related ICTY decisions concerning WCC-BiH cases.
- **legal-tools.org** — ICC Legal Tools Database mirror of key WCC-BiH decisions.
- **OHR archives** (ohr.int) — for the WCC Project Implementation Plan and related establishment documents.

**Tier 2 (secondary, must be labelled):**
- **OSCE Mission to BiH** (oscebih.org) — the OSCE has monitored WCC-BiH proceedings since establishment; produces detailed trial monitoring reports. **Tier 1-in-practice for procedural and structural observations**, given the OSCE's official monitoring mandate. Reports include *Witness Protection and Support* (2010), *Moving Towards a Harmonized Application of the Law* (2008), and the ongoing *War Crimes Justice in Bosnia and Herzegovina* series.
- **ICTJ** (International Center for Transitional Justice, ictj.org) — major analytical reports including *The War Crimes Chamber in Bosnia and Herzegovina: From Hybrid to Domestic Court* (2008) and *War Crimes Prosecutions in Bosnia: Looking Back, Looking Forward* (2014).
- **UNDP BiH** — implementation reports on the National War Crimes Processing Strategy.
- **Human Rights Watch** — *Looking for Justice: The War Crimes Chamber in Bosnia and Herzegovina* (2006); *Justice for Atrocity Crimes: Lessons of International Support for Trials before the State Court of Bosnia and Herzegovina* (2012).
- **Hybrid Justice project** (hybridjustice.com) — comparative analytical resource on the WCC-BiH and other hybrid mechanisms.
- **JusticeInfo.net** — ongoing coverage and analytical pieces.
- **Balkan Investigative Reporting Network (BIRN BiH)** — daily trial monitoring; **balkaninsight.com** publishes detailed court reports.

**Academic literature:**
- Olga Martin-Ortega, *Prosecuting War Crimes at the War Crimes Chamber in Bosnia and Herzegovina*, in *International Criminal Law Review* (multiple articles)
- David Tolbert and Aleksandar Kontić, *The International Criminal Tribunal for the former Yugoslavia and the Transfer of Cases and Materials to National Judicial Authorities*
- Bogdan Ivanišević, *The War Crimes Chamber in Bosnia and Herzegovina: From Hybrid to Domestic Court* (ICTJ 2008)
- Carsten Stahn and Larissa van den Herik (eds.), *Future Perspectives on International Criminal Justice* — chapters on BiH

**Never authoritative:** Wikipedia, Grokipedia, social media, AI-generated summaries.

See `references/authoritative-sources.md`.

## Citation format

WCC-BiH citations follow a hybrid of Bosnian civil-law conventions and international tribunal practice. Two pieces matter:

1. **The case designation** — formally *Prosecutor's Office of BiH v. [Defendant(s)]* or *Tužilaštvo BiH protiv [Defendant(s)]*. Case numbers follow the format **X-KR-XX/XX** (first-instance) and **X-KRŽ-XX/XX** (appellate).

2. **The chamber designation:**
   - **Court of Bosnia and Herzegovina, Section I for War Crimes** (first-instance trial panel)
   - **Court of Bosnia and Herzegovina, Appellate Division, Section I for War Crimes** (appellate panel)

**Worked examples:**

- *Prosecutor's Office of BiH v. Stupar et al.*, Court of BiH, Section I for War Crimes, First-Instance Verdict, Case No. X-KR-05/24, 29 July 2008.
- *Prosecutor's Office of BiH v. Mejakic et al.*, Court of BiH, Section I for War Crimes, First-Instance Verdict, Case No. X-KR-06/200, 30 May 2008. (Rule 11 bis case referred from ICTY.)
- *Prosecutor's Office of BiH v. Lukic and Lukic*, Court of BiH — note: this case was originally referred to BiH under Rule 11 bis but the ICTY revoked the referral in 2007; the trial proceeded at the ICTY itself.

See `references/citation-format.md` for the full convention.

## Audit mode

When the user supplies a document:
- **Working drafts**: audit citations for accuracy. WCC-BiH citations often confuse the State Court level with entity-level prosecutions (FBiH, RS, Brčko) — flag any such confusion.
- **Final WCC-BiH records**: inventory and spot-check.

In either mode, Step 0 (identify the chamber, period, and case type) comes first. The most common confusion is between the **Court of BiH (state level)** and **entity-level courts (FBiH, RS, Brčko)** — see Trap 4.

## Substantive doctrine — pointers

The skill does not encode doctrine line by line. Starting points:

- **Applicable substantive law — the 2003 vs 1976 Criminal Code debate.** The WCC-BiH has applied the 2003 BiH Criminal Code retroactively to conduct from the 1992-1995 war. The European Court of Human Rights, in *Maktouf and Damjanović v. Bosnia and Herzegovina* (Grand Chamber, 18 July 2013), held that this **violated Article 7 of the ECHR** (no punishment without law) where the 1976 SFRY Criminal Code (which was in force at the time of the conduct and prescribed lighter sentences for certain offences) should have been applied. This is a **central doctrinal and practical issue** in WCC-BiH practice — see Trap 1.

- **Rule 11 bis referrals from ICTY.** The WCC-BiH received and tried multiple cases transferred under Rule 11 bis. Each referral was governed by an ICTY Referral Bench decision specifying conditions. The WCC-BiH was required to report periodically to the ICTY on the progress of referred cases. **Notable Rule 11 bis cases at WCC-BiH:** Stanković, Janković, Mejakic et al., Trbić, Rašević and Todović. The Lukić and Lukić referral was revoked in 2007 (case returned to ICTY).

- **Genocide jurisprudence — Srebrenica.** The WCC-BiH has produced substantial jurisprudence on the Srebrenica genocide of July 1995 (notably *Stupar et al.* (Kravica), *Trbić*, *Vuković*, *Erdemović* (the latter at ICTY but factually overlapping)). The findings are consistent with the ICTY's *Krstić* and *Popović et al.* jurisprudence but apply BiH-specific procedural and evidentiary frameworks.

- **Sexual violence as crime against humanity and war crime.** Significant body of case-law including *Janković* (Foča), *Samardžić*, *Kurtović*, and others.

- **Command responsibility / superior responsibility.** Applied in numerous cases following ICTY and ICTR jurisprudence.

For each, verify the specific decision through the workflow.

## Sensitive contexts

The Bosnian war of 1992-1995 produced approximately **100,000 deaths** and over **2 million displaced persons**. The Srebrenica genocide of July 1995 (approximately 8,000 victims) and the Sarajevo siege are emblematic. WCC-BiH judgments touch on ethnically-contested narratives in a state where ethnic tensions remain politically salient.

Approach with care:
- Use the terminology of the WCC-BiH judgments themselves (Bosniak, Croat, Serb, where these characterisations appear in findings)
- Avoid uncritical reproduction of ethnic terminology where the underlying judgment uses more neutral formulations (e.g., "civilian victims")
- The WCC-BiH operates in a state where political parties contest its legitimacy on ethnic grounds (notably Republika Srpska political leadership has contested WCC-BiH jurisdiction over RS-territory crimes); this institutional context is **factual** but not a substantive critique of WCC-BiH findings

## What this skill is not

- Not legal advice.
- Not a substitute for the Court of BiH's records.
- Not endorsed by the Court of BiH, the Prosecutor's Office of BiH, the OHR, the ICTY/IRMCT, or any of the entities.
- Not a position on the contested doctrinal questions (the 2003 vs 1976 Criminal Code question is described, not resolved).

## Reference files

- `references/authoritative-sources.md` — source hierarchy and URLs
- `references/citation-format.md` — case-name conventions, chamber designations, case-number formats
- `references/verification-workflow.md` — fallback ladder, WCC-BiH-specific traps
- `references/foundational-texts.md` — Law on the Court of BiH 2002, Criminal Code of BiH 2003, CPC of BiH 2003, National War Crimes Processing Strategy 2008
- `references/jurisprudence-map.md` — topic-by-topic map of WCC-BiH holdings
- `examples/example-verification.md` — verifying one WCC-BiH citation end-to-end
- `examples/example-audit.md` — auditing user-supplied documents
