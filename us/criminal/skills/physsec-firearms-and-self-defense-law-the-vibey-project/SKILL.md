---
name: physsec-firearms-and-self-defense-law-the-vibey-project
title: 'Firearms and Self-Defense Law: Federal and South Carolina'
description: Use when a firearms or self-defense law question comes up, stated as of September 2026 and to be verified before relying on it — 18 U.S.C. § 922(g) and its prohibited categories including unlawful drug users, Form 4473 and NICS, Heller, McDonald, Bruen, Rahimi and United States v. Hemani, the 2026 NFA tax change and the Jensen v. ATF and Brown v. ATF litigation, FOPA interstate transport; and South Carolina's 2024 permitless-carry act with its location restrictions and alcohol-premises rule, the Protection of Persons and Property Act — castle doctrine, the protective-order presumption, stand your ground and the pretrial immunity hearing — the common-law elements, and the absence of a red-flag statute. Not legal advice. Skill 5 of 8 of the Physical Security, Self-Defense, Firearms and the ATF Substances reference.
author: the-vibey-project
author_url: https://github.com/the-vibey-project/vibey/tree/develop/src/vibey_tools/skills/plugins/physical-security-self-defense-and-firearms/skills/physsec-firearms-and-self-defense-law
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: criminal
language: en
---

# Firearms and Self-Defense Law: Federal and South Carolina

> **Skill 5 of 8** of the *Physical Security, Self-Defense, Firearms, and the "ATF Substances"* reference
> (plugin `physical-security-self-defense-and-firearms`), carrying the second half of source Part V, *Firearms*: §17–§18 — federal firearms law and South Carolina carry and self-defense law, as of September 2026. Sibling skills:
> `physsec-foundations-and-threat-modeling` (§0–§4 — how to read the reference, threat modeling, the security mindset, layered defense and CPTED),
> `physsec-securing-buildings` (§5–§8 — homes, home hardening, organizations and commercial buildings, and targeted violence),
> `physsec-personal-security-and-self-defense` (§9–§13 — personal security, the self-defense hierarchy, training evidence, less-lethal tools and Stop the Bleed),
> `physsec-firearms-mechanics-safety-and-carry` (§14–§16 — how firearms work (conceptual), safety, storage and the risk ledger, choosing, training and carrying),
> `physsec-alcohol-tobacco-and-cannabis` (§19–§23 — cannabis, alcohol and tobacco/nicotine on mechanism, medicine, harms, law and self-defense),
> `physsec-decision-tools-and-contested-questions` (§24–§26 and Part VIII — the personal security plan, spending priorities, the organizational checklist and the contested questions),
> `physsec-reference` (§27–§30 — training and references, the glossary, the currency notes and the sources).
>
> Section numbers are **the source's own and shared across the whole set**: a reference written
> as §N → `skill` points into that sibling skill.

> **Read this first — the source's own limits and tags** (in full at §0 →
> `physsec-foundations-and-threat-modeling`). **Not legal advice** (self-defense law is
> fact-specific and South Carolina case law is detailed — talk to a criminal-defense attorney
> before you need one). **Not medical advice** (no dosing, no regimens). **Not a substitute for
> hands-on training** — firearms handling, medical skills and physical self-defense cannot be
> learned from text. Evidence tags: **\[STRONG\]** replicated, large-sample, or randomized
> evidence; professional consensus · **\[MODERATE\]** consistent observational evidence;
> plausible mechanism · **\[WEAK\]** self-report surveys, small or industry-funded studies,
> expert opinion · **\[CONTESTED\]** serious researchers disagree; both positions presented ·
> **\[LAW-2026\]** legal state as of Sept 2026; verify before relying on it. The source was
> compiled on September 30, 2026 and has not been re-checked for this pack; what will go stale
> first is listed at §29 → `physsec-reference`.

> **If anyone in the household is in crisis**, the source's own list (§27 → `physsec-reference`):
> the **988** Suicide & Crisis Lifeline; the National DV Hotline **1-800-799-7233**; the SAMHSA
> National Helpline **1-800-662-4357**.

> **Pack orientation** (the pack's words, not the source's): The last two sections of Part V: federal law and South Carolina law, both tagged
> **\[LAW-2026\]** by the source — the legal state as of September 2026, to be verified
> before relying on it. The only state whose law the reference sets out is **South Carolina**.

## §17 Federal firearms law — 2026 state of play \[LAW-2026\]

- **Gun Control Act (1968), 18 U.S.C. § 922(g)** prohibits nine categories from possessing firearms — including felons, fugitives, "unlawful users of or addicted to any controlled substance" \[(g)(3)\], people adjudicated mentally defective or involuntarily committed, those under qualifying DV restraining orders, and those convicted of misdemeanor domestic violence.
- **Background checks**: licensed dealers use ATF Form 4473 and NICS. Form 4473 still asks about unlawful drug use (including marijuana).
- **Key Supreme Court cases**: *Heller* (2008, individual right), *McDonald* (2010, applies to states), *Bruen* (2022, text-and-history test), *Rahimi* (2024, upheld disarming people found by a court to be a credible threat), and ***United States v. Hemani* (June 18, 2026)** — see §20 → `physsec-alcohol-tobacco-and-cannabis`.
- **NFA changes**: the One Big Beautiful Bill Act reduced the **$200 tax to $0** for suppressors, short-barreled rifles and shotguns, and AOWs effective **January 1, 2026** — but **registration and ATF approval remained** in the statute. Machine guns and destructive devices kept the $200 tax. On **August 5, 2026**, a federal judge in the Northern District of Texas (*Jensen v. ATF*) held the remaining registration scheme unconstitutional for those zero-tax items — **but that relief is limited to the parties/protected members, is subject to appeal, and parallel cases exist** (e.g., *Brown v. ATF*). Do not assume you can skip NFA registration; get current legal advice.
- **Interstate transport**: 18 U.S.C. § 926A (FOPA) protects transport through states where you can't lawfully possess, if unloaded and inaccessible — but some states and airports have tangled with travelers anyway.

## §18 South Carolina firearms and self-defense law \[LAW-2026\]

**Carry — the 2024 Constitutional Carry / Second Amendment Preservation Act (H.3594, effective March 7, 2024):**

- Adults **18+** who can legally possess a handgun may carry **openly or concealed without a permit**. The Concealed Weapons Permit (CWP) still exists and remains useful for **reciprocity** in other states.
- Location restrictions survived. Carry is prohibited (permit or not, with narrow exceptions) in places such as: law enforcement, correctional and detention facilities; courthouses; polling places on election day; city/county/state government office buildings; school and college athletic events; daycare facilities; churches/religious sanctuaries without permission; hospitals and medical facilities without permission; another person's residence without permission; K-12 school property (with a vehicle-storage exception); and **any premises posted with a compliant "no weapons" sign** (§ 23-31-235). Federal restrictions (post offices, federal buildings) apply separately.
- **Alcohol**: under the amended § 16-23-465 you may carry into a restaurant/bar that serves alcohol on premises **only if you do not consume alcohol while there**. Violation is a misdemeanor (up to $2,000 and/or 2 years) and CWP holders face a five-year permit revocation.
- The act also **increased penalties for illegal possession by felons and repeat offenders**.

**Self-defense — the Protection of Persons and Property Act (S.C. Code §§ 16-11-410 to -450, 2006):**

- **Castle doctrine** (§ 16-11-440(A)): a person is **presumed** to have a reasonable fear of death or great bodily injury when using deadly force against someone unlawfully and forcibly entering (or who has entered) a dwelling, residence or occupied vehicle, or trying to remove someone from one. Exceptions exist (e.g., the person has a right to be there, law enforcement acting lawfully, you're engaged in criminal activity).
- **Protective orders** (§ 16-11-440(E)): forcible entry in violation of an order of protection, restraining order or bond condition is presumed to be with intent to commit an unlawful act — even against a co-owner/co-lessee.
- **Stand your ground** (§ 16-11-440(C)): a person **not engaged in unlawful activity**, attacked in a place they have a right to be, has **no duty to retreat** and may use deadly force if they reasonably believe it necessary to prevent death, great bodily injury, or a violent crime.
- **Immunity** (§ 16-11-450): justified use of force brings immunity from criminal prosecution and civil action. Immunity is decided by a **judge at a pretrial hearing**, where the defendant must prove entitlement by a **preponderance of the evidence**. If the case goes to trial instead, once self-defense is properly raised the **State must disprove it beyond a reasonable doubt**.
- **Common-law elements still matter** — especially **not being at fault in bringing on the difficulty** (you can't start or escalate a fight and then claim self-defense), actual and reasonable fear, and (where the Act doesn't apply) no other probable means of avoidance. SC courts have held the Act isn't retroactive and doesn't apply where the claimant was engaged in unlawful activity or wasn't lawfully present.
- **Evidence note**: RAND's evidence synthesis rates the research as **supportive** that stand-your-ground laws are associated with *increased* firearm homicides — a public-policy finding that is **\[CONTESTED\]** by some researchers and doesn't change your individual legal rights, but is worth knowing.

**Medical and "red flag" context:** South Carolina has no extreme-risk protection order (red flag) statute as of this writing; voluntary temporary storage is therefore the main crisis-access tool.

## Where to go next (pack navigation, not source text)

- **Cannabis and § 922(g)(3) after *Hemani*, in full** — §20 → `physsec-alcohol-tobacco-and-cannabis`.
- **Police encounters while armed and the aftermath of a defensive incident** — §16 → `physsec-firearms-mechanics-safety-and-carry`.
- **What will change first** — §29 → `physsec-reference`.
