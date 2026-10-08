---
name: immigration-foia-codearranger
title: Immigration — FOIA / Privacy Act for Your Own Records
description: Use this skill to assemble Freedom of Information Act (FOIA) and Privacy Act requests to obtain a person's own immigration records — almost always the FIRST step before defending a removal case or filing any benefit request, because you cannot litigate a record you have not seen (the NTA, prior applications, officer notes, the charging history, the I-213). Triggers include "FOIA my immigration file", "get my A-file", "G-639", "Form G-639", "record of proceedings", "ROP", "EOIR FOIA", "request my immigration records", "ICE FOIA", "CBP FOIA", "I-213", "what's in my immigration file", "Privacy Act immigration", "get the NTA and prior filings", "USCIS FOIA portal", "expedite FOIA hearing date", "alien file request". The skill drafts a G-639-style USCIS A-file FOIA request, an EOIR Record-of-Proceedings FOIA request (with expedite language for an upcoming hearing), ICE and CBP FOIA request letters, and a "records I need" checklist. Documents, not advice.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/claude-legal-immigration-laws/skills/immigration-foia
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Immigration — FOIA / Privacy Act for Your Own Records

> **NOT LEGAL ADVICE.** This skill produces FOIA/Privacy Act request scaffolds and
> checklists — **not legal advice**, and no attorney-client relationship is created. A FOIA
> request does not pause any deadline: an upcoming hearing date, a BIA-appeal clock, or a
> petition-for-review clock keeps running while the agency processes the request. Verify the
> current form edition, the correct FOIA office address/portal, and every deadline against
> current law, and consider consulting a licensed immigration attorney or an EOIR-accredited
> representative.

## FOIA goes first

You usually cannot defend a case well — or even know what you are defending against — without
the underlying government record. The Notice to Appear (NTA), every prior application and its
adjudication, the inspecting officer's narrative (the **Form I-213, Record of Deportable /
Inadmissible Alien**), interview notes, the entry/inspection history, and any derogatory
information the government will rely on all live in agency files. Pulling them is the
foundation for `eoir-removal-defense`, `uscis-benefit-requests`, and any reopening motion.

**The record is split across agencies, and each has its own FOIA channel.** A single request
to one agency will not give you the whole picture — match the record you need to the office
that holds it.

## The four record sources

| Record | Agency / office | How to request | What you get |
|---|---|---|---|
| **A-file** (Alien File — the master file) | **USCIS** (DHS) | **Form G-639** via the USCIS FOIA online portal (FIRST) or by mail to the USCIS National Records Center | The consolidated immigration history: prior petitions/applications, approvals/denials, RFEs, biometrics, the NTA copy, interagency referrals |
| **Record of Proceedings (ROP)** | **EOIR** (DOJ) FOIA office | Written request (no special form) to EOIR's FOIA Service Center, by mail or the DOJ portal | What is actually before the immigration court / Board: the IJ's file, hearing record, filings, orders — the document set your removal case turns on |
| **Enforcement / detention records** | **ICE** (DHS) FOIA office | Letter or the DHS/ICE FOIA portal | Detention records, enforcement actions, custody/bond history, ICE narratives |
| **Entry / inspection records** | **CBP** (DHS) FOIA office | Letter or the CBP FOIA portal | Border-inspection and admission records, **the I-213**, travel/entry history, secondary-inspection notes |

Practical mechanics: file with **USCIS through the online FOIA portal** when possible (faster
intake and status tracking than mail); USCIS sorts requests into processing **tracks** (simple
vs. complex, plus an expedite track). **Always cite the A-number** (`A2NN-NNN-NNN`) on every
request — it is the file key across DHS and EOIR and prevents misrouting. If you do not yet
have the A-number, see `immigration-pro-se` for how to locate it.

## The legal basis

- **FOIA — 5 U.S.C. § 552** gives any person the right to request agency records.
- **Privacy Act — 5 U.S.C. § 552a** gives a U.S. citizen or lawful permanent resident the
  right to records the agency keeps about *them*, and is the stronger first-party access route
  where it applies.
- These two statutes are the *general* federal access framework; they are **not** part of this
  plugin's corpus, so cite them **by number** (do not link them as corpus files).
- The DHS-component disclosure framework is at **6 CFR part 5**, cross-referenced from the
  immigration regulations at **8 CFR § 103.42** (FOIA/Privacy Act rules) — see
  [`../../references/immigration-regulations/8CFR-103-powers-fees.md`](../../references/immigration-regulations/8CFR-103-powers-fees.md).
  Published precedent decisions are separately made available under **8 CFR § 103.10(e)**.
- **First-party records require identity verification + the requester's signature.** A G-639
  (or an equivalent letter) must include the requester's signed certification of identity; a
  request by someone other than the subject needs the subject's notarized/sworn consent or
  proof of authority (e.g., the representative's G-28). Without a valid signature/identity
  proof the agency will narrow the release to non-personal material or deny it.

## Expedite when there is a hearing date

EOIR runs an **expedited FOIA track for people with a scheduled hearing date**. State the
**date, time, and immigration-court location** prominently at the top of the EOIR ROP request
and ask for expedited processing on that basis. The same expedite ask can be made to USCIS,
ICE, and CBP when a near-term hearing or filing deadline creates urgency — but remember a FOIA
request **does not toll any deadline**, so file the substantive defense work in parallel; do
not wait on the records to act.

## Artifacts this skill drafts

- A **USCIS A-file FOIA request** in Form **G-639** style (signed identity certification;
  A-number; scope description), routable to the online portal or the National Records Center.
- An **EOIR Record-of-Proceedings FOIA request** to the EOIR FOIA Service Center, with
  **expedite language** keyed to the upcoming hearing date.
- **ICE** and **CBP FOIA request letters** for enforcement/detention and entry/inspection
  records (including a specific ask for the **I-213**).
- A **"records I need" checklist** — NTA, prior applications and adjudications, I-213,
  officer narratives, entry/inspection history, biometrics, prior orders — mapped to the
  agency that holds each.

## Related authority

- DHS FOIA/Privacy Act framework: **8 CFR § 103.42** (→ 6 CFR part 5) and **§ 103.10(e)** —
  [`../../references/immigration-regulations/8CFR-103-powers-fees.md`](../../references/immigration-regulations/8CFR-103-powers-fees.md).
- FOIA: **5 U.S.C. § 552**; Privacy Act: **5 U.S.C. § 552a** (cited by number; not in this
  plugin's corpus).
- INA / 8 U.S.C. (substance of the underlying matter):
  [`../../references/immigration-statutes/`](../../references/immigration-statutes/), with the
  INA ↔ 8 U.S.C. crosswalk in its README.

## Composition

Comes early — typically right after `immigration-pro-se` establishes the forum and the
A-number. Feeds the record it obtains into `eoir-removal-defense` (to plead to the NTA and
build relief applications), `uscis-benefit-requests` (to reconcile prior filings before a new
one), and any reopening work. Run `immigration-deadlines` in parallel, because the FOIA
request never stops the clock.
