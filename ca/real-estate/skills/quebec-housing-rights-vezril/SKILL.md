---
name: quebec-housing-rights-vezril
title: Quebec housing rights (tenants & landlords)
description: 'Quebec residential tenancy — the rights and obligations of tenants (lessees) and landlords (lessors) under the Civil Code of Québec, adjudicated by the Tribunal administratif du logement (TAL, formerly the Régie du logement). A query-answering reference distilled from Éducaloi''s English renting capsules, quebec.ca, and tal.gouv.qc.ca (fetched 2026-07) via multi-agent research. Covers: the lease (the mandatory TAL form, verbal leases, French-language rule, void clauses, the lowest-rent-in-12-months disclosure notice and the 10-day/2-month deadlines to contest); money (only first month''s rent may be required — security/key deposits and demanded post-dated cheques are ILLEGAL; what a landlord may and may not ask for; rent due the 1st, late the 2nd; the 3-week rule; paying before judgment stops eviction; co-tenancy where JOINT is the default and solidary must be written in); discrimination (Charter grounds, CDPDJ); rent increases and automatic renewal (the 3-6 month notice window,
  the 1-month reply where SILENCE = ACCEPTANCE, the landlord applying to the TAL to fix rent, CPI-based criteria); assignment vs subletting (assignment releases you and since Feb 2024 a landlord refusing it cancels the lease; sublet needs a serious reason; 15 days, silence = consent); living in the dwelling (landlord''s habitability/peaceful-enjoyment/guarantee-of-use duties; the tenant''s duty of prudence and diligence and NOT to change the form or destination/use of the unit — a two-condition test of consent AND zoning; access notice of 24h/10 days with visits 9-9 and work 7-7; repairs and repair-and-deduct; heating where ~21C is a TAL practice standard not a statutory minimum; poor conditions and the unfit-dwelling recourse; pets, where no-pet clauses ARE valid in Quebec); ending a lease (keeping repossession vs eviction vs termination-for-fault distinct — notice periods, silence = REFUSAL, the landlord bears the burden and must apply to the TAL, the eviction indemnity formula, senior
  protectio'
author: vezril
author_url: https://github.com/vezril/claude-toolkit/tree/main/skills/quebec-housing-rights
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: ca
practice: real-estate
language: en
sources:
- title: Civil Code Articles
  path: references/civil-code-articles.md
- title: Ending The Lease
  path: references/ending-the-lease.md
- title: Lease And Money
  path: references/lease-and-money.md
- title: Living In The Dwelling
  path: references/living-in-the-dwelling.md
- title: Tal Process
  path: references/tal-process.md
---

# Quebec housing rights (tenants & landlords)

Quebec residential tenancy runs on the **Civil Code of Québec**, and almost every dispute is decided by the **Tribunal administratif du logement (TAL)** — the specialized tribunal formerly called the *Régie du logement*. Quebec's rules differ sharply from the rest of Canada (deposits are illegal, leases renew automatically, no-pet clauses are enforceable), so **don't import intuitions from Ontario or elsewhere.**

> ## This is information, not legal advice
> I'm not a lawyer and this skill isn't a substitute for one. It's here to help you **understand your position, decode a notice, find the right deadline, and know what to ask** — so you arrive at the TAL, a lawyer, legal aid, or a *comité logement* already oriented. For anything binding, go to those people. Two honesty notes that shape everything here:
> - **The law moved materially in 2024** (assignment refusal, senior protections, a three-year eviction ban, representation rules) and some of it is **time-limited**. Check currency.
> - **TAL fees are re-indexed every 1 April.** Any figure here is a dated snapshot.
>
> **On sources:** the plain-language layer comes from Éducaloi, which cites no article numbers; the **statutory layer is quoted from the actual Civil Code text** on LégisQuébec and cross-checked against the TAL's own citation map. Nothing is invented — but verify anything decision-critical on [LégisQuébec](https://www.legisquebec.gouv.qc.ca/en/document/cs/ccq-1991) directly.

Load a reference for depth:

- **[references/civil-code-articles.md](references/civil-code-articles.md)** — **the statutory layer**: the actual text of the key lease articles (**1851–1978**), the scope article **1892** (incl. *accessories and dependencies*), the mandatory-provisions article **1893**, the obligations (**1854/1855/1856**), and the remedies article **1863** — plus the TAL's own obligation→article map and a worked walkthrough of a **change-of-use** notice.
- **[references/lease-and-money.md](references/lease-and-money.md)** — the lease (mandatory form, verbal leases, French rule, **void clauses**), the **rent-disclosure notice** + deadlines to contest, **illegal deposits**, what a landlord may/may not ask, paying rent and the **3-week rule**, **co-tenancy** (joint vs solidary), discrimination, **renewal & rent increases**, and **assignment vs subletting**.
- **[references/living-in-the-dwelling.md](references/living-in-the-dwelling.md)** — both sides' obligations, **the form/destination (change-of-use) rule**, **access & visits** (24h/10 days; visits 9–9, work 7–7), repairs & **repair-and-deduct**, heating, **poor conditions / unfit dwellings**, pets, and the **silence-defaults trap**.
- **[references/ending-the-lease.md](references/ending-the-lease.md)** — **repossession vs eviction vs termination-for-fault** kept distinct, notice periods, the **eviction indemnity formula**, **senior protection**, the **June 2024 eviction ban**, and early termination (HLM / seniors' care / handicap / **spousal or sexual violence**).
- **[references/tal-process.md](references/tal-process.md)** — jurisdiction, **filing + the 45-day deadline**, fees, evidence & burden of proof, **representation** (incl. an Éducaloi error corrected against the TAL), hearings, **correction/revocation/review/appeal**, executory dates, and bailiff enforcement.

## The mental model

- **Almost everything runs through the TAL.** A landlord **cannot evict you themselves** — only the TAL can end a lease, and only a **bailiff** executes it. A demand letter is a *first step*, not a legal act.
- **The dwelling rules are public order** (**art. 1893**): a lease clause inconsistent with them is **without effect**. You cannot sign away these protections, and a clause in your lease saying otherwise is simply void.
- **Specific performance is the default remedy, not termination** (**art. 1863**): breach entitles the other party to an **order to comply** plus damages; **resiliation requires *serious injury***.
- **The landlord usually bears the burden.** On repossession, eviction, and termination-for-fault, it's the landlord who must apply to the TAL and **prove** their case — and for fault they must show **serious prejudice**.
- **Leases renew automatically.** Ending or changing one requires a specific notice in a specific window; doing nothing usually favours the tenant staying.
- **Deadlines are the whole game**, and **silence means different things** depending on the notice. Get that backwards and you lose rights by doing nothing.
- **Termination isn't the only outcome.** The TAL can **order compliance** or **grant time to comply** instead of ending a lease.

## ⚠️ The silence trap

| Notice you receive | What doing nothing means |
|---|---|
| **Rent increase / lease modification** | **Acceptance** |
| **Repossession or eviction notice** | **Refusal** |
| **Notice to vacate for major works** | **Refusal** |
| **Landlord says an unfit unit is fit again** | **The lease is cancelled** |
| **Assignment / sublet request** *(landlord's silence, 15 days)* | **Consent** |

When in doubt: **respond in writing, keep proof of sending.**

## Fast answers

| Question | Answer |
|---|---|
| Can a landlord take a damage/security/key deposit? | **No.** Only the **first month's rent** at signing. |
| Can they demand post-dated cheques? | **No** — they can't *demand* them. |
| Are "no pet" clauses valid? | **Yes** in Quebec (the Civil Code is silent; it's ordinary contract). Assistance animals override via the Charter. |
| Is there a minimum indoor temperature? | **No statutory minimum.** ~**21 °C** is a TAL practice standard. |
| Rent increase notice window (12-month lease)? | **3–6 months** before the end; you have **1 month** to reply; **silence = acceptance**; if you refuse, **the landlord** applies to the TAL. |
| How late before I can lose the lease? | **More than 3 weeks** — but paying **rent + interest + costs before the decision** stops the eviction. |
| Can I get out of my lease? | Non-renewal · agreement · **sublet** · **assignment** (releases you) · a special situation (HLM/seniors' care/handicap = **2 months**; violence = **2 months** + DPCP attestation) · TAL authorization. |
| Landlord wants the unit back for family? | **Repossession** — 6 months' notice, **silence = refusal**, **landlord** must go to the TAL, **no automatic compensation**. |

## Getting real help

- **TAL** — [tal.gouv.qc.ca](https://www.tal.gouv.qc.ca): model notice forms, the **rent-fixing calculator**, filing, and a **free conciliation service**.
- **Comité logement** — local tenants' rights committees; free, know the local TAL, and will help you draft. Usually the highest-value first call for a tenant.
- **Legal aid (aide juridique)** / the **Barreau** referral service / a **notaire** for lease questions.
- **CDPDJ** — for discrimination.
- **LégisQuébec / CanLII** — the actual Civil Code text and TAL decisions, when you need the authority rather than a summary.

## Related

- [[canadian-business-registration]] — the sibling Quebec/Canada civic-process skill (REQ/NEQ, CRA); same educates-but-isn't-professional-advice framing.
- [[personal-finance]] · [[canadian-registered-accounts]] — the money side of housing decisions (rent-vs-buy, budgeting).
- [[calvin-voice]] — for drafting a reply or demand letter in your own voice once you know your position.

Sources: [Éducaloi — Renting](https://educaloi.qc.ca/en/categories/renting/) (the English capsules on leases, signing, rent, co-tenants, discrimination, landlord/tenant responsibilities, visits, repairs, heating, poor conditions, pets, renewal & increases, unpaid rent, assignment/subletting, leaving early, specific needs, violence, eviction, repossession, and the five TAL capsules); [quebec.ca — Rights and obligations of the lessor and lessee](https://www.quebec.ca/en/housing-territory/renting/rights-and-obligations-of-the-lessor-and-lessee); and [tal.gouv.qc.ca](https://www.tal.gouv.qc.ca) (jurisdiction, filing, costs, representation, contesting, executing). Fetched **2026-07** via parallel research agents; where Éducaloi and the TAL conflicted, the TAL governs and the difference is flagged in the references. Éducaloi is a legal-education nonprofit writing plain-language summaries — excellent orientation, **not the statute**. Verify anything decision-critical against the Civil Code, the TAL, and qualified counsel.
