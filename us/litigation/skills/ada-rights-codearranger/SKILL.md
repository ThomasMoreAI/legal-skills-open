---
name: ada-rights-codearranger
title: ADA Rights
description: 'Use this skill to help a person with a disability assert rights under the Americans with Disabilities Act (ADA) — drafting reasonable-accommodation and reasonable-modification requests, ADA grievances, DOJ ADA complaints, and EEOC charge intake worksheets — across the three substantive titles. Triggers include "ADA", "Americans with Disabilities Act", "reasonable accommodation", "reasonable modification", "accommodation request letter", "disability discrimination", "failure to accommodate", "interactive process", "undue hardship", "service animal", "auxiliary aids", "effective communication", "accessibility barrier", "architectural barrier", "website accessibility", "ADA complaint", "file an ADA complaint", "DOJ ADA complaint", "EEOC charge", "accommodation denied", "ADA retaliation". Routes by title: Title I employment (29 CFR 1630, EEOC); Title II state/local government (28 CFR 35); Title III public accommodations (28 CFR 36 + 2010 Standards). Produces documents, not legal
  advice.'
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/claude-legal-federal-laws/skills/ada-rights
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# ADA Rights

> **NOT LEGAL ADVICE.** This skill produces drafting aids and checklists. It is not legal advice
> and does not create an attorney-client relationship. Verify every deadline, threshold, and
> statutory citation against current law before relying on or filing anything.

## What the ADA covers — pick the right title first

The ADA splits into three substantive titles, each with its **own** enforcement scheme, its **own**
implementing regulation, and its **own** remedies. Getting the title right is the first decision —
it controls who you write to, what you can ask for, and what deadline runs.

| If the barrier is at… | ADA title | Regulation | Where to read |
|---|---|---|---|
| **A job** (your employer, applying for work) | **Title I** | 29 C.F.R. Part 1630 (EEOC) | [`../../references/ada-laws/EEOC-Title-I-29-CFR-1630.md`](../../references/ada-laws/EEOC-Title-I-29-CFR-1630.md) |
| **A state or local government** (DMV, courts, public schools, transit, police, public benefits) | **Title II** | 28 C.F.R. Part 35 (DOJ) | [`../../references/ada-laws/DOJ-Title-II-28-CFR-35.md`](../../references/ada-laws/DOJ-Title-II-28-CFR-35.md) |
| **A private business open to the public** (stores, restaurants, hotels, doctors' offices, websites of such businesses) | **Title III** | 28 C.F.R. Part 36 + 2010 Standards (DOJ) | [`../../references/ada-laws/DOJ-Title-III-28-CFR-36.md`](../../references/ada-laws/DOJ-Title-III-28-CFR-36.md) |

The statute itself is [`../../references/ada-laws/ADA.md`](../../references/ada-laws/ADA.md) (42 U.S.C.
§§ 12101–12213). Cite to it; do not paraphrase from memory.

## Threshold — is this a covered disability?

Under **§ 12102** (as amended by the **ADA Amendments Act of 2008**), "disability" means a physical
or mental impairment that **substantially limits** a major life activity, a **record** of such an
impairment, or being **regarded as** having one. The ADAAA made the bar deliberately broad:

- "Substantially limits" is **construed in favor of broad coverage** — it is not a demanding standard.
- The analysis ignores the **ameliorative effects of mitigating measures** (medication, hearing aids,
  prosthetics, assistive tech) — *except* ordinary eyeglasses/contacts, which are considered.
- An impairment that is **episodic or in remission** counts if it would substantially limit a major
  life activity **when active**.

Do not pre-screen a person out on the "are they disabled enough" question — post-ADAAA the focus is
on whether discrimination occurred, not on a searching disability analysis. Quote § 12102 from the
statute file when the request or complaint needs to establish coverage.

## Track I — Title I (employment)

**The ask:** a **reasonable accommodation** (29 C.F.R. § 1630.2(o)) — a change to the job, workplace,
or how things are usually done so a qualified employee can perform essential functions or enjoy equal
benefits. Examples: modified schedule, leave, assistive equipment, reassignment to a vacant position,
telework, a quieter workspace.

- **Covered employers:** 15 or more employees. (Smaller employers may be reached by **state** fair-
  employment law — flag that and route to the state plugin.)
- **The interactive process.** A request triggers a duty to engage in an **interactive process** to
  identify an effective accommodation. *Document every step* — the request, the employer's response,
  each meeting — because a breakdown in the process is itself evidence. Build the log into the artifact.
- **Undue hardship** (§ 1630.2(p)) is the employer's defense — significant difficulty or expense — and
  it is the employer's burden, not yours. A flat "no" without that showing is a red flag.
- **The EEOC charge is mandatory before suit, and the clock is short.** A charge must be filed with the
  EEOC (or a dual-filing state/local FEPA) within **180 days** of the discriminatory act — extended to
  **300 days** in a "deferral" state that has its own fair-employment agency. **Diary this deadline
  immediately.** You generally cannot file an ADA Title I lawsuit until you have a **Notice of Right to
  Sue**, and you then have **90 days** from that notice to sue.

## Track II — Title II (state & local government)

**The ask:** a **reasonable modification** of policies, practices, or procedures (28 C.F.R. § 35.130(b)(7)),
**program access**, and **effective communication**.

- **Effective communication / auxiliary aids** (§ 35.160): qualified interpreters, captioning, materials
  in accessible formats; the public entity must give **primary consideration** to the person's expressed
  preference.
- **Service animals** (§ 35.136): a dog (or, in some cases, a miniature horse) individually trained to do
  work or perform tasks. Staff may ask only **two questions** — is it required because of a disability,
  and what task is it trained to perform — and may **not** demand documentation or ask the nature of the
  disability. **Emotional-support animals are not service animals** under the ADA (a separate Fair Housing
  Act / housing analysis may apply — see [`../../references/federal-debt-laws/FHA.md`](../../references/federal-debt-laws/FHA.md)).
- **ADA Coordinator & grievance procedure** (§ 35.107): entities with **50+ employees** must designate an
  ADA Coordinator and adopt a grievance procedure. Address the **internal grievance** there first.
- **Defenses to know:** **fundamental alteration** of the program and **undue financial/administrative
  burden** — the entity's burden to prove.
- **Enforcement:** file a complaint with **DOJ** (civilrights.justice.gov) or the relevant federal
  funding agency; you may **also** sue in court — there is generally **no administrative-exhaustion
  requirement** to bring a private Title II suit. Title II allows **compensatory damages** (but not
  punitive — *Barnes v. Gorman*). The limitations period is **borrowed from the analogous state statute**;
  confirm it for the state and diary it.

## Track III — Title III (public accommodations)

**The ask:** a **reasonable modification** of policies (28 C.F.R. § 36.302), **removal of architectural
barriers** where **readily achievable** in existing buildings (§ 36.304), **auxiliary aids** for effective
communication (§ 36.303), and compliance with the **2010 ADA Standards for Accessible Design** for new
construction and alterations (rendered in the Title III reg file).

- **Service animals** (§ 36.302(c)): same two-question rule and same "ESAs are not service animals" point
  as Title II.
- **Websites and apps** of public accommodations are increasingly treated as covered; if accessibility
  (e.g., screen-reader compatibility) is the issue, frame it as a § 36.303 effective-communication / full-
  and-equal-enjoyment problem and **research the controlling circuit's case law** via `case-law-research`
  before asserting a position — the law varies by circuit.
- **Remedies are the big difference.** A **private** Title III plaintiff can get **injunctive relief and
  attorney's fees — but NOT money damages.** Only the **DOJ** can seek civil penalties and monetary relief.
  Set expectations accordingly, and check whether **state** law (e.g., a state public-accommodations or
  civil-rights act) supplies damages — route to the state plugin for that.
- **Enforcement:** a demand letter to the business often resolves barrier issues; otherwise a DOJ complaint
  and/or a private injunctive suit. Limitations period is **borrowed from state law**.

## Cross-cutting — retaliation & coercion (§ 12203)

It is independently unlawful to **retaliate** against someone for asserting ADA rights or to **coerce/
intimidate** them. This applies across **all** titles. If an accommodation request or complaint was
followed by an adverse action (discipline, firing, eviction from a program, harassment), plead/document
the § 12203 retaliation claim alongside the underlying title — and preserve the timeline as evidence.

## Artifacts this skill drafts

- **Title I reasonable-accommodation request letter** — to the employer/HR, citing § 1630.2(o), framing the
  essential-function link, requesting the interactive process, paired with an **interactive-process log**.
- **EEOC charge intake worksheet** — captures the facts for the charge, flags the **180/300-day** deadline
  and dual-filing with the state FEPA, and the **90-day** post-right-to-sue clock.
- **Title II reasonable-modification / effective-communication / auxiliary-aids request + ADA grievance** —
  to the entity's ADA Coordinator, citing 28 C.F.R. Part 35.
- **Title III barrier-removal / reasonable-modification demand letter** — to the business, citing 28 C.F.R.
  Part 36 and the relevant 2010 Standards provision.
- **DOJ ADA complaint** (Title II or III) — structured for civilrights.justice.gov, with the facts, the
  regulation cited, and the relief sought.
- **§ 12203 retaliation timeline / documentation** — the adverse-action chronology tied to the protected
  activity.

Each artifact ends with the `NOT LEGAL ADVICE` disclaimer.

## Related federal authority

- **Section 504 of the Rehabilitation Act** (29 U.S.C. § 794) — bars disability discrimination by
  recipients of federal funds and by federal agencies; frequently pleaded alongside Title II. Not in this
  corpus — research it live via `case-law-research`.
- **Fair Housing Act** — disability discrimination and reasonable-accommodation/modification in **housing**
  (not public accommodations) lives in
  [`../../references/federal-debt-laws/FHA.md`](../../references/federal-debt-laws/FHA.md). Use it for a
  landlord/HOA/housing-provider matter; emotional-support-animal requests in housing run through the FHA,
  not the ADA.

## Composition

- Verify any ADA holding before citing it → **`case-law-research`** (never cite a case from memory; the
  website-accessibility and "regarded as" areas are circuit-split — check the controlling circuit).
- Build the proof trail, communication log, and damages ledger → **`consumer-harm-documentation`**.
- To actually **file suit** (Title II/III, or Title I after the right-to-sue letter), hand the matter to the
  state plugin: the **`*-pro-se`** drafting framework and the **`*-draft-*`** scaffolders for the complaint,
  declaration, and motions, and the state **`*-deadlines`** skill to confirm the borrowed limitations period.
- Smaller employers / broader state coverage / Title III money damages → the **state** civil-rights or fair-
  employment statute via the state plugin.
