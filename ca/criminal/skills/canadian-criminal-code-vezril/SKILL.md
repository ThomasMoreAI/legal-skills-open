---
name: canadian-criminal-code-vezril
title: The Criminal Code of Canada (C-46)
description: 'The Criminal Code of Canada (R.S.C. 1985, c. C-46) as a navigable map — how the statute is organized and how to find things in it. Built by parsing the official consolidated text (laws-lois.justice.gc.ca, current to 2026-05-26), with Part ranges extracted programmatically from the body and cross-checked against the TOC. Covers: the full Part structure I–XXVIII with section ranges (the substantive Parts I–XIII vs the procedural/sentencing Parts XIV–XXVIII), and why decimal Parts and sections are insertions so section numbers cannot be arithmetic (320.4 comes after 320.104); the CLASSIFICATION system that drives everything — indictable vs summary vs hybrid, where ''hybrid'' appears zero times in the Code and is expressed structurally as ''indictable … or … punishable on summary conviction'' (345 occurrences), the s. 787 default summary penalty ($5,000 / two years less a day, the penitentiary-vs-jail line), and the s. 786(2) 12-month limitation that applies only to summary proceedings,
  can be waived by agreement, and has no indictable counterpart; general principles (s. 2 definitions, the s. 8(3) preservation of common-law defences against s. 9''s bar on common-law offences, parties s. 21, counselling s. 22, accessory s. 23, attempts s. 24 where factual impossibility is no defence and the preparation line is a question of law); defences (self-defence s. 34 and its nine factors, defence of property s. 35, duress s. 17 whose ''immediate''/''present'' words were struck in Ruzic but still print, necessity as pure common law, provocation s. 232 as a partial defence narrowed in 2015, mental disorder s. 16 and NCRMD, extreme intoxication s. 33.1 rewritten after Brown); where offences live (assault 265 and why sexual assault 271 has no separate definition, theft 322/334, break and enter 348, fraud 380, mischief 430 incl. computer data); procedure (the s. 493.1 release principle, s. 515 bail and its three grounds, the s. 535 preliminary inquiry narrowed to 14+ years on request,
  the s.'
author: vezril
author_url: https://github.com/vezril/claude-toolkit/tree/main/skills/canadian-criminal-code
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: ca
practice: criminal
language: en
sources:
- title: Part Map
  path: references/part-map.md
- title: Principles Procedure Sentencing
  path: references/principles-procedure-sentencing.md
---

# The Criminal Code of Canada (C-46)

Canada's federal criminal statute — **one Code for the whole country**, because criminal law and procedure are exclusively federal (*Constitution Act, 1867*, s. 91(27)), while the **administration of justice is provincial** (s. 92(14)), so the provinces run the police, most prosecutions, and the courts.

It is enormous: **~2.5 million characters across 38 Parts**. This skill is a **map** — how it's organized, how classification drives everything, and how to find things. It cannot be a treatise, and it is not one.

> ## Orientation, not advice — and not a how-to
> I'm not a lawyer and this is not legal advice. It describes **how the statute is structured**, quoting provisions to show how they're *worded* — not to advise on conduct, and not as guidance for committing or evading offences. **If you're facing a charge, you need a lawyer** — see [[quebec-legal-system]] for legal aid (indictable charges qualify automatically in Quebec).
>
> **And the biggest caveat, which the Code itself won't tell you:** the printed text is **not the law**. s. 17 still prints words the Supreme Court struck in 2001. Mandatory minimums remain on the page after being declared of no force. **Always pair a provision with the Charter jurisprudence and the s. 8(3) common-law defences.**

- **[references/part-map.md](references/part-map.md)** — the **full Part structure with section ranges**, where common offences live, the key offence definitions (265, 322, 348, 380, 430), and the navigation rules.
- **[references/principles-procedure-sentencing.md](references/principles-procedure-sentencing.md)** — **classification** in depth, general principles (ss. 8(3), 21–24), **defences**, **procedure** (bail, prelim, the election, jury architecture), **sentencing** (718, 718.1, 718.2, discharges, CSOs, minimums), and the **Charter overlay**.

## The one concept that organizes everything: classification

Read the **penalty clause first**. It tells you the class, and the class determines the **court**, the **procedure**, the **maximum**, the **limitation period**, and the **appeal route**.

| Class | How you spot it | Consequences |
|---|---|---|
| **Indictable** | "is guilty of an indictable offence and liable to…" | Parts XIV–XXI · **no limitation period** · jury is the default (s. 471) |
| **Summary** | "is guilty of an offence punishable on summary conviction" | Part XXVII · provincial court, no jury, no prelim · **12-month limitation** (s. 786(2)) |
| **Hybrid** | **"indictable … *or* … punishable on summary conviction"** | **The Crown elects.** The largest modern category. |

**"Hybrid" appears zero times in the Code** — it's structural, not statutory language. ("Punishable on summary conviction" appears **345** times.) And the rule that a hybrid is **indictable until the Crown elects summary** isn't in the Code either — it's the ***Interpretation Act*, s. 34(1)(a)**.

## Two numbers that recur everywhere

- **Two years** — s. 787 default summary max (**two years less a day**); **s. 743.1** penitentiary vs. provincial jail; **s. 742.1** conditional-sentence eligibility.
- **$5,000** — **s. 334** theft · **s. 380** fraud · **s. 430(3)/(4)** mischief · **s. 553** absolute provincial-court jurisdiction.

## Fast answers

| Question | Answer |
|---|---|
| Is there a limitation period? | **Summary: 12 months** (s. 786(2)) — and the parties can agree to waive it. **Indictable: none.** |
| What's the default summary penalty? | **$5,000 fine / two years less a day** (s. 787), unless otherwise provided. |
| Where are the defences? | **s. 34** self-defence · **s. 35** property · **s. 17** duress · **s. 16** mental disorder · **s. 33.1** extreme intoxication · **s. 232** provocation (partial). **Necessity is pure common law**, preserved by **s. 8(3)**. |
| Where's sexual assault defined? | It isn't separately — **s. 265(2)**: the assault definition "applies to **all forms of assault, including sexual assault**." s. 271 is a penalty provision. |
| Can I choose judge alone on a murder charge? | **No** — s. 469 + **s. 473**: judge alone requires the consent of **both** the accused **and** the Attorney General. |
| When do I get a preliminary inquiry? | Only if the offence carries **14 years or more** **and** a party **requests** one (ss. 535, 536(4)) — narrowed by C-75 in 2019. |
| Where's the Charter? | **Not in the Code.** It's Part I of the *Constitution Act, 1982*, and it overrides. |
| Where's the pardon/record-suspension regime? | **Not here** — the *Criminal Records Act*. |

## Gotchas

- **Section numbers aren't arithmetic.** 320.4 comes *after* 320.104 — they're dotted identifiers.
- **The offence and its punishment are usually in different sections** (theft 322/334, attempt 24/463, accessory 23/463).
- **Check s. 2, then the Part's own interpretation section** (84, 214, 321, 493, 716…) — local definitions beat general ones.
- **Offences are codified; defences aren't** (ss. 8(3) + 9). That asymmetry is why necessity, entrapment, and officially induced error exist off-page.
- **A mandatory minimum does more than set a floor** — it blocks a **discharge** (s. 730) and blocks a **conditional sentence** (s. 742.1(b)).
- **DNA and SOIRA orders are in Part XV, not the sentencing Part.**

## Related

- [[quebec-legal-system]] — **legal aid** (indictable and youth matters qualify automatically), the courts, and municipal courts.
- [[quebec-charter-rights]] — Quebec's own Charter; note its **judicial rights (ss. 23–38)** parallel and in places exceed the federal Charter's legal rights.
- [[canadian-human-rights-act]] — the federal anti-discrimination statute (unrelated to criminal liability, but the other major federal rights instrument).
- [[cryptography]] · [[secure-coding]] — for the technical side of computer-related provisions (e.g. **s. 430(1.1)** mischief to computer data, Part VI interception).

Sources: *Criminal Code*, R.S.C. 1985, c. **C-46**, official consolidation at [laws-lois.justice.gc.ca](https://laws-lois.justice.gc.ca/eng/acts/c-46/) — **current to 2026-05-26, last amended 2026-03-26** — retrieved 2026-07 and parsed directly (Part ranges measured from the body, not asserted from the TOC). **Statutory extraction is solid; the case-law gloss (*Ruzic*, *Brown*, *Jordan*, *Grant*, *Nur*, *Gladue*/*Ipeelee*, etc.) is general knowledge, not independently verified — treat it as orientation and confirm on CanLII.** The Code changes constantly (C-75 2019, C-5 2022, S-12 2023); verify currency.
