---
name: quebec-legal-system-vezril
title: The Quebec legal system — access, courts, and finding the law
description: 'How the Quebec legal system works and how to get into it — legal aid, municipal courts, how regulations are made, why LégisQuébec is authoritative, and the 1994 Civil Code changeover. Quoted from the official LégisQuébec texts (à jour 1 April 2026, retrieved 2026-07) of four statutes: A-14 (Act respecting legal aid), c-72.01 (Act respecting municipal courts), R-18.1 (Regulations Act), R-2.2.0.0.2 (Act respecting the Compilation of Québec Laws and Regulations), plus CCQ-1992 (implementation of the Civil Code reform). LEGAL AID (A-14): the two independent tests — financial (gratuitous where income/liquidities/assets are below the regulated level, with last-resort-assistance recipients automatically eligible, vs contributory where only income is tested) and subject matter (indictable and youth matters automatic; summary/penal conditional on imprisonment, loss of livelihood, best interests or interests of justice; family, youth protection, tutorship, designated benefit appeals;
  residual liberty and livelihood valves); minors free regardless of means for all services; exclusions (defamation as plaintiff, elections, parking) and the s. 4.11 subsidiarity rule making legal aid a last resort behind insurance, unions and other services; the s. 69 private-bar diversion; that s. 8 means losing still exposes you to the other side''s costs; the s. 52 right to choose your own lawyer only if they accept the regulated tariff; the 30-day review under s. 74 which is final and without appeal under s. 79; a third party''s 15-day right to contest your eligibility; and four free hours for victims of sexual or domestic violence regardless of eligibility. NOTE the Act contains NO dollar thresholds and no indexation clause — all delegated to regulation.'
author: vezril
author_url: https://github.com/vezril/claude-toolkit/tree/main/skills/quebec-legal-system
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: ca
practice: litigation
language: en
sources:
- title: Courts Regulations Compilation
  path: references/courts-regulations-compilation.md
- title: Legal Aid
  path: references/legal-aid.md
---

# The Quebec legal system — access, courts, and finding the law

Four statutes that together answer the practical questions: **can I get a lawyer?** · **which court hears this?** · **is this regulation actually in force?** · **why is the text I'm reading authoritative?**

> ## Information, not legal advice
> I'm not a lawyer. This maps the statutes so you can find the right door and read the real text. For anything binding: your **community legal centre**, a lawyer, or a **notaire**. Quoted from the official LégisQuébec consolidation (**à jour 1 April 2026**), retrieved **2026-07**.

- **[references/legal-aid.md](references/legal-aid.md)** — **A-14** in depth: the two eligibility tests, what's covered and excluded, the **subsidiarity rule**, applying, the right to choose your lawyer, the **30-day review**, and the services available **regardless of means**.
- **[references/courts-regulations-compilation.md](references/courts-regulations-compilation.md)** — **municipal courts** (jurisdiction, appeals), the **Regulations Act** lifecycle (the 45 days, coming into force, what voids a regulation), the **Compilation Act** (why LégisQuébec is official), and the **1994 changeover**.

## Legal aid — the short version

**Two independent tests. You must pass both.**

**1. Money (s. 4).** **Free** if your income *and* **liquidities and assets** are under the regulated level — and **automatically free** if you (or a family member) receive **last-resort financial assistance**. **Contributory** (partly paid) if only your **income** is under the higher level. **Minors: free, always, for everything** (s. 4.0.1).

**2. Subject matter.**

| Matter | Covered? |
|---|---|
| **Indictable** charge · **youth (YCJA)** | ✅ **Automatic** |
| **Summary / penal** charge | ⚠️ **Only if** imprisonment or **loss of livelihood** is likely, or it's in your **best interests** / the **interests of justice** |
| Family · youth protection · tutorship/protection mandate · child abduction | ✅ |
| Appealing a **designated** benefit/compensation decision | ✅ (the program must be designated by regulation) |
| Anything seriously restricting **liberty** (s. 4.7(8)) or threatening **livelihood / essential needs** (s. 4.7(9)) | ✅ residual valves |
| **Defamation as plaintiff** · elections · **parking** | ❌ absolutely excluded |

> **No dollar figures exist in A-14.** Thresholds are entirely regulatory — **look up the current scale**. The only amounts in the Act are penal fines.

**Three traps worth knowing:**
- **Legal aid is a last resort** (**s. 4.11 ¶2**) — refused if the service is available "through **another government service or another body, under an insurance contract or through a union or association**." Check your insurance and union first.
- **s. 8 — winning isn't guaranteed protection:** "A recipient **who fails in the action is not exempt from condemnation to legal costs in favour of the adverse party**." Legal aid doesn't shield you from the other side's costs.
- **Your opponent can attack your eligibility** — **s. 75** gives "every interested party" a **15-day** window to contest it.

**Choosing your own lawyer (s. 52):** a real right — **but only if that lawyer agrees** to take the mandate at the **regulated tariff**. No one can be conscripted.

**Refused? s. 74 — 30 days** to seek review. **s. 79: the review decision is "final and without appeal."**

**Free regardless of means:** **four hours** of legal assistance for **victims of sexual or domestic violence** (s. 83.0.1), court-ordered State-funded counsel (s. 83.1), and counsel to cross-examine where you'd otherwise face the other party yourself (s. 83.1.1).

**Where to go:** a regional centre — by law its name includes "**community legal centre**" (s. 30).

## Which court?

| Forum | Hears |
|---|---|
| **Municipal court** *(optional — s. 3)* | **Municipal by-law** offences; money **owed to the municipality**; municipal leases **under $30,000** (**not housing**). Never **demolition** (s. 29). |
| **Court of Québec** | Most civil (incl. Small Claims), criminal, youth |
| **Superior Court** | Inherent jurisdiction; larger civil; **judicial review**; s. 469 criminal |
| **Court of Appeal** | Appeals — incl. **directly** from a municipal court where the object exceeds **$15,000** (s. 80) |
| **TAL** | Residential leases → [[quebec-housing-rights]] |
| **Human Rights Tribunal** | ss. 80–82 C-12 applications → [[quebec-charter-rights]] |

Municipal courts are **not** small-claims courts — **the municipality is always a party**.

## Is that regulation actually in force — and valid?

1. **Find it in the *Gazette officielle du Québec*** (s. 15 requires publication).
2. **In force 15 days after publication** (s. 17), unless a later date is set — **or sooner** under s. 18 for **urgency**/fiscal norms, in which case **the reason must be published with it**.
3. **Validity:** **s. 25** — only breaches of the **publication** duties (ss. 8, 10, 13, 15, 18¶2) invalidate. **Breaching the 45-day comment period does *not*.**
4. **Municipal by-laws don't run on this Act at all** (s. 3¶2) — see [[quebec-municipal-law]].

## Why LégisQuébec is authoritative

**s. 7** of the Compilation Act: "**Publication of the compilation … by the Québec Official Publisher, *whatever the medium used*, confers official status on the texts.**" The online text is as official as print — that's the "**Ce document a valeur officielle**" stamp. Laws got official status **1 Jan 2010**, regulations **1 Jan 2012** (s. 17). The annual **1 April** archive (s. 8) is why pages say "**À jour au 1er avril**."

**s. 5 — the rule people miss:** new provisions govern **events on or after** the update; **former provisions govern earlier events**. **Read the version in force when your events happened**, not today's.

## Gotchas

- **A-14 has no dollar amounts.** Don't quote thresholds from the Act — they're regulatory and change.
- **Municipal courts have no Criminal Code jurisdiction under c-72.01** — the Act doesn't grant it (ss. 63/31(2) merely presuppose it). The grant is elsewhere (likely the Courts of Justice Act).
- **A proposed regulation can be amended after consultation without republication** (s. 14) — the final text may not be what you commented on.
- **Legal-aid certificates are per-remedy** (s. 66) — appealing needs a **fresh application**.
- **Conditional certificates** (s. 67): if no definitive certificate follows, **you pay** for the conservatory acts.
- **Situations straddling 1 Jan 1994** need CCQ-1992: old law for what's done, new law for what's ongoing — and **contracts keep their old suppletive rules** (s. 4).

## Related

- [[quebec-civil-code]] — the *jus commune* itself; CCQ-1992 Title III translates old CCLC citations into it.
- [[quebec-charter-rights]] — the Charter and the CDPDJ/Tribunal route.
- [[quebec-housing-rights]] — the TAL (a "court" for A-14 purposes: s. 3 includes quasi-judicial bodies).
- [[quebec-municipal-law]] — municipal by-laws (excluded from the Regulations Act) and the courts that enforce them.
- [[canadian-criminal-code]] — what an indictable vs summary charge means for automatic legal-aid coverage.

Sources: official LégisQuébec consolidations ("Ce document a valeur officielle", **à jour au 1 avril 2026**) of **A-14**, **c-72.01**, **R-18.1**, **R-2.2.0.0.2**, and **CCQ-1992**, retrieved **2026-07** and parsed directly. Two things deliberately **not** asserted: legal-aid **dollar thresholds** (not in A-14 — regulatory) and municipal courts' **Criminal Code jurisdiction** (not granted by c-72.01).
