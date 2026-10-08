---
name: quebec-civil-code-vezril
title: The Civil Code of Québec
description: 'The Civil Code of Québec (CCQ, in force 1 January 1994, replacing the 1866 Civil Code of Lower Canada) — Quebec''s civil-law jus commune and the foundation of its private law. A navigation-and-orientation reference verified against the official consolidated text on LégisQuébec (retrieved 2026-07). Covers: what the Code is and the Preliminary Provision that makes it the general law of Québec, operating in harmony with the Charter of human rights and freedoms and serving as the foundation of all other laws; why Quebec is a CIVIL-LAW jurisdiction and how that differs from the common law of the other provinces (codified general principles reasoned deductively rather than binding precedent/stare decisis, no equity/trusts-by-tradition, different vocabulary); the map of all ten Books with article ranges — One Persons (1-364), Two The Family (365-612, incl. family patrimony), Three Successions (613-898), Four Property (898.1-1370, opening with ''animals are not things''), Five Obligations
  (1371-2643, the largest — contract formation, civil liability, and the nominate contracts incl. sale, lease at 1851-1978, employment, mandate, insurance), Six Prior Claims and Hypothecs (2644-2802), Seven Evidence (2803-2874.1), Eight Prescription (2875-2933, incl. the 3-year personal action and 10-year judgment rules), Nine Publication of Rights (2934-3075.1, the land register and RDPRM), Ten Private International Law (3076-3168); the Book/Title/Chapter/Section/Division hierarchy and why division scope matters; how to read an article''s legislative history (1991, c. 64 enactment, amendments, and decimal numbers signalling later insertions); the equally-authoritative French and English versions; public order vs suppletive rules; and common cross-Book chains for real problems. Use to find where a Quebec legal topic lives in the Code, decode an article citation, understand the civil-law approach, or orient before researching on LégisQuébec/CanLII.'
author: vezril
author_url: https://github.com/vezril/claude-toolkit/tree/main/skills/quebec-civil-code
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: ca
practice: contracts
language: en
sources:
- title: Book Map
  path: references/book-map.md
---

# The Civil Code of Québec

The **Civil Code of Québec** (CCQ, `1991, c. 64`) came into force **1 January 1994**, replacing the *Civil Code of Lower Canada* (1866). It runs **art. 1 → art. 3168** across **ten Books**, and it is the backbone of private law in Quebec: persons, family, property, contracts, and civil liability.

Its own **Preliminary Provision** tells you how to treat it: the Code governs persons, relations between persons, and property, **in harmony with the *Charter of human rights and freedoms* and the general principles of law**; it lays down the ***jus commune*** — **the general law of Québec** — expressly or by implication; and it is **"the foundation of all other laws,"** though other laws may complement it or make exceptions to it.

> ## Orientation, not legal advice
> I'm not a lawyer, and this skill is a **map of the Code**, not counsel on your situation. It helps you find **where a topic lives**, **decode a citation**, and **understand the civil-law frame** — so you can read the real text or brief a professional efficiently. The Code is **amended regularly**; verify on [LégisQuébec](https://www.legisquebec.gouv.qc.ca/en/document/cs/ccq-1991) and take anything binding to a **Quebec lawyer or notary**.

- **[references/book-map.md](references/book-map.md)** — the full **book-by-book map** with article ranges and what lives in each, the **Book→Title→Chapter→Section→Division** hierarchy, how to read an article's legislative history, and **common cross-Book chains** for real problems.

## Quebec is a civil-law jurisdiction — this is the thing to internalize

Quebec is the **only** Canadian province whose private law is **civil law** (a *droit civil* tradition descended from French law), while the other nine are **common law**. Canada is therefore **bijural**. Practically:

| | **Civil law (Quebec, private law)** | **Common law (rest of Canada)** |
|---|---|---|
| **Primary source** | **The Code** — general principles, stated abstractly and comprehensively | **Judicial precedent**, accreted case by case |
| **Reasoning** | **Deductive** — from the codified principle down to the facts | **Inductive** — from decided cases outward by analogy |
| **Precedent** | Persuasive; **no strict *stare decisis*** — case law *interprets* the Code, it isn't the source of the rule | **Binding** *stare decisis* |
| **Doctrine** | Scholarly writing carries real weight | Traditionally secondary |
| **Structure** | No law/equity split; **trusts exist but as a Code creature** (*patrimony by appropriation*) | Law vs equity heritage; trusts from equity |

So: **start from the article, not from the case.** Cases matter — they show how courts read a provision — but the rule's *home* is the text.

**Note the boundary:** civil law governs **private** law in Quebec. **Public law** (criminal, constitutional, administrative) is common law across the whole country — criminal law is federal and uniform. So a Quebec lawyer reasons civilly about your lease and commonly about a Charter/criminal question.

## The ten Books at a glance

| Book | Subject | Articles |
|---|---|---|
| **One** | **Persons** — personality, capacity, tutorship, legal persons | 1–364 |
| **Two** | **The Family** — marriage/civil union, family patrimony, filiation, support, parental authority | 365–612 |
| **Three** | **Successions** — devolution, wills, liquidation, partition | 613–898 |
| **Four** | **Property** — movable/immovable, ownership, co-ownership, servitudes, trusts | 898.1–1370 |
| **Five** | **Obligations** — contracts, civil liability, and the **nominate contracts** (sale, **lease 1851–1978**, employment, mandate, insurance…) | 1371–2643 |
| **Six** | **Prior Claims and Hypothecs** — security on property | 2644–2802 |
| **Seven** | **Evidence** — burden, means of proof, admissibility | 2803–2874.1 |
| **Eight** | **Prescription** — acquiring by time, losing by inaction | 2875–2933 |
| **Nine** | **Publication of Rights** — the land register, the RDPRM | 2934–3075.1 |
| **Ten** | **Private International Law** — conflicts, jurisdiction, foreign judgments | 3076–3168 |

**Book Five is the giant** and where most everyday disputes live.

## Vocabulary that trips up common-law readers

| Quebec term | What it means |
|---|---|
| **Patrimony** | The totality of a person's rights and obligations, as an economic whole. No common-law equivalent. |
| **Movable / immovable** | Personal property / real property. |
| **Real right vs personal right** | A right *in a thing* (ownership, hypothec) vs a right *against a person* (a claim). |
| **Hypothec** | Security on property — a mortgage is one kind. |
| **Prescription** | Limitation period — **extinctive** (lose a right by inaction) or **acquisitive** (gain by possession). |
| **Resiliation vs resolution** | Ending a contract **for the future** vs **retroactively**. Leases are *resiliated*. |
| **Lessor / lessee** | Landlord / tenant — the Code's own words. |
| **Suppletive vs public order** | A rule parties **may contract around** vs one they **may not** — a clause contrary to a public-order rule is **without effect**. |
| **Jus commune** | The general background law the Code supplies when nothing more specific applies. |
| **Solidary** | Joint *and several* — each debtor liable for the whole. |
| **Superior force** | *Force majeure*. |

## Public order — the rule that decides whether your contract clause survives

Some Code rules are **suppletive** (defaults you can vary by agreement); others are **of public order** (mandatory — you cannot contract out, and a clause trying to is **without effect**). Whole regimes are protective in this way: the dwelling-lease rules say so expressly (**art. 1893** voids clauses inconsistent with the listed articles). **Before relying on a contract clause, ask whether the underlying rule is suppletive or public order** — the answer decides whether the clause means anything.

## Reading a citation

`art. 1856 C.C.Q.` → Book Five → Nominate Contracts → Lease. On LégisQuébec each article is followed by its history: `1991, c. 64, a. 1856` (enacted by the Code itself), plus amendments (`; 2002, c. 19, s. 15`) and integration notes (`; I.N. 2014-05-01`). A **decimal** article (**1978.1**, **898.1**, **2874.1**) was **inserted by a later amendment** — a quick tell that the rule postdates 1994.

**French and English are both official and equally authoritative** — Quebec statutes are enacted in both. An apparent divergence is a genuine interpretive question, not a translation error.

## Where to read it

- **[LégisQuébec — CCQ](https://www.legisquebec.gouv.qc.ca/en/document/cs/ccq-1991)** — the official consolidated text, FR/EN toggle. The authority.
- **[CanLII](https://www.canlii.org/en/qc/)** — the Code plus the case law interpreting it (courts and tribunals).
- **[Éducaloi](https://educaloi.qc.ca/en/)** — plain-language explanations (no article citations, but excellent orientation).
- **[SOQUIJ](https://soquij.qc.ca)** — Quebec's judicial-decisions service.
- **Notaries** handle non-contentious civil matters (wills, real estate, mandates) — often the right professional in Quebec, not a lawyer.

## Related

- [[quebec-housing-rights]] — **residential tenancy in depth** (arts 1851–1978 + the TAL): the lease, rent, obligations, eviction, and the tribunal. The Code chapter this skill only points at.
- [[canadian-business-registration]] — incorporating/registering in Quebec (the REQ/NEQ); Book One's *legal persons* is the Code backdrop.
- [[canadian-registered-accounts]] · [[personal-finance]] — the money side of successions, family patrimony, and property decisions.

Sources: the **official consolidated text** of the *Civil Code of Québec* on [LégisQuébec](https://www.legisquebec.gouv.qc.ca/en/document/cs/ccq-1991) (English content), with the ten-Book structure, article ranges, and the Preliminary Provision verified directly against it — retrieved **2026-07**. The Code is amended regularly; article ranges shift as decimal articles are inserted. Verify before relying, and consult a Quebec lawyer or notary for advice.
