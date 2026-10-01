---
name: quebec-municipal-law-vezril
title: The Municipal Code of Québec (C-27.1)
description: 'The Municipal Code of Québec (CQLR c. C-27.1) — the general statute for local (mainly rural) municipalities and regional county municipalities (RCMs/MRCs). Parsed from the current official LégisQuébec consolidation (retrieved 2026-07). THE SCOPE RULE (art. 1): the Code applies to every municipality subject to any inconsistent charter provision, but does NOT apply to a municipality governed by the Cities and Towns Act (c. C-19) or to northern, Cree or Naskapi villages — so Municipal Code and Cities and Towns Act are parallel regimes, not layers; art. 2 lets a municipality migrate by letters patent, and art. 4 deems a C-19 city to be a Code municipality for RCM purposes. THE ZONING TRAP: land-use planning and zoning are NOT in this Code — they are in the Act respecting land use planning and development (c. A-19.1). Verified: all 10 cross-references to A-19.1 in the Code are incidental (RCM governance, voting thresholds, withdrawal rights); none confers a planning power. But the
  ENFORCEMENT seam runs back here — art. 492 inspection, art. 455 fines, art. 437.3 access prohibition and arts. 689-692 annulment all apply to by-laws adopted under A-19.1. Covers: the by-law lifecycle (art. 445''s notice of motion, draft filing, passing at a different sitting no earlier than the second day, and the rule that contravening those paragraphs ENTAILS THE NULLITY of the by-law; art. 450 coming into force on publication; art. 451/431 publication by public notice posted at two places; art. 455 fine ceilings of $1,000/$2,000 first offence and $2,000/$4,000 subsequent); contesting a by-law (arts. 689-692 — annulment for illegality by any interested party on a $50 deposit, PRESCRIBED BY THREE MONTHS FROM PASSING, appeal to the Court of Appeal within 30 days); the council (art. 149 public sittings, art. 150''s statutory question period whose modalities but not existence may be shaped by by-law, art.'
author: vezril
author_url: https://github.com/vezril/claude-toolkit/tree/main/skills/quebec-municipal-law
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: ca
practice: administrative
language: en
sources:
- title: Bylaws Powers And Scope
  path: references/bylaws-powers-and-scope.md
---

# The Municipal Code of Québec (C-27.1)

Quebec's general statute for **local (mainly rural) municipalities** and **regional county municipalities (RCMs / MRCs)**. A heavily hollowed-out 1916 statute — **1,566 numbered sections**, a large fraction now `(Repealed)` as subject areas migrated to dedicated Acts.

> ## Information, not legal advice
> I'm not a lawyer. This is a map of the statute. Text parsed from the **current official LégisQuébec consolidation** (retrieved **2026-07**; the file's own modified date is 2025-11-03 — **re-check currency**). Note: **the Code is officially French**; the English is a translation, and **for litigation the French governs**.

- **[references/bylaws-powers-and-scope.md](references/bylaws-powers-and-scope.md)** — the scope rules, the **structure table**, the **by-law lifecycle**, **contesting a by-law**, the council and question period, officers, **art. 492 inspections**, taxation/finances, and RCM jurisdiction.

## ⚠️ Two traps, up front

### 1. Which regime applies? (art. 1)

> "This Code applies to every municipality of Québec, **subject to any inconsistent provision of the charter** of the municipality.
> However, **it does not apply to a municipality governed by the Cities and Towns Act (chapter C-19)** … **or to a northern, Cree or Naskapi village**."

**Municipal Code and the Cities and Towns Act are *parallel* regimes, not layers** — you read one or the other. Refinements: **charters win** (Montréal, Québec City have their own); **art. 2** lets a municipality **migrate by letters patent**; and **art. 4** deems a **C-19 city inside an RCM's territory to be a Code municipality** for the RCM's purposes — so the Code reaches into cities *via the RCM*. **Verify your municipality's regime; don't infer it from the name.**

### 2. Zoning is not in here

**Land-use planning and zoning live in the *Act respecting land use planning and development* (c. A-19.1 — the *LAU*)**, not the Municipal Code. Zoning by-laws, the urban plan, the RCM's *schéma d'aménagement*, subdivision and construction by-laws, minor variances (*dérogations mineures*), the *comité consultatif d'urbanisme*, and the **register/referendum** process for zoning changes are all A-19.1.

This was **verified, not assumed**: all **10** occurrences of "A-19.1" in the Code are **incidental** — RCM committee composition, voting thresholds, withdrawal rights. **None confers a planning or zoning power.**

**But the enforcement seam runs back here.** A zoning by-law is *adopted* under A-19.1 and then *enforced* through the Municipal Code:

| Municipal Code provision | Does |
|---|---|
| **art. 492** | the **inspection** power |
| **art. 455** | the **fine** ceilings |
| **art. 437.3** | the **access prohibition** |
| **arts. 689–692** | **annulment** of the by-law |

## The by-law lifecycle

**Adoption — art. 445**, a three-step, multi-sitting sequence: **notice of motion** → **filing of a draft** (copies made available to the public "as soon as possible") → **passing at a *different* sitting**, "**not earlier than the second day**" after the later of those sittings. Before passing, the clerk-treasurer or a member must **state the object and any differences** from the draft. Changes "**must not be such as to change the object**."

> **"Any contravention of the first, second, fourth or eighth paragraph entails the nullity of the by-law."**

That's the citizen's lever: procedural defects here are **not harmless** — they void it.

**In force — art. 450:** "every by-law comes into force … **on the day of its publication**", unless otherwise provided. **art. 452** — it "remains in force and is executory until … amended, repealed or annulled."

**Publication — art. 451:** note the mechanism — what's published is a **public notice** "mentioning the object of the by-law, the date of the passing thereof, and **the place where communication thereof may be had**", **not the by-law text**. "Ordinary manner" per **art. 431** = posted at **two different places** (failing a resolution: the municipal office + one other public place). General notice timing: **art. 434**, at least **seven clear days**.

**Penalties — art. 455:** the maximum fine for a **first offence** cannot exceed **$1,000** (natural person) / **$2,000** (legal person); **second or subsequent**: **$2,000** / **$4,000**.

## ★ Contesting a by-law — and the deadline that kills claims

**art. 689:** "**Any by-law, procès-verbal, roll, resolution or other ordinance** of the municipality or act of municipal officers **may be annulled, on the ground of illegality**, with legal costs against the municipality."

**art. 690:** by application under the **judicial-review rules of the CCP**; "**Any interested party** is competent to take such suit"; a **$50 deposit** as security for costs.

**art. 691:** the court may annul **in whole or in part**. Appeal to the **Court of Appeal within 30 days**, heard **by preference**; that judgment is **final**.

> **art. 692 — the headline:** "the right of recourse granted by article 689 **is prescribed by three months from the passing of the act or proceeding attacked**."

**Three months, running from *passing*** — not from publication, not from when you found out. Standing is broad, entry is cheap ($50), partial annulment is available — but the clock is short and starts early. *(And art. 452 means the by-law stays executory meanwhile.)*

**Separate, much faster recourse — arts. 437.3/437.4:** the council may **prohibit access** to an immovable for **≤90 days** where an activity/use runs without a required permit and endangers life/health or risks serious damage. The decision must **contain reasons** and be notified. **Contest within 10 days before the Court of Québec** — and the application **does not suspend** the decision unless a judge so orders.

## ★ art. 492 — the inspection power

**There is no "municipal inspector" in the Code** — the word appears **zero times**. The power is a **by-law power over the municipality's "officers"**:

> "Every local municipality may make … by-laws **to authorize its officers, between 7:00 a.m. and 7:00 p.m., to visit and examine all movable and immovable property, as well as the interior or exterior of any house, building or edifice whatsoever, to ascertain if the by-laws are carried out** … and **to compel the owners, tenants or occupants … to receive its officers, and to answer all questions put to them** relative to the carrying out of the by-laws."

Practical reading if you're facing an inspection:
- **It is not self-executing.** It exists only if the municipality **actually passed an art. 492 by-law**. **First question: *which by-law authorizes this?***
- **Hard window: 7:00 a.m. – 7:00 p.m.**
- Covers **interior and exterior**.
- The duty to **receive** and **answer** is real — but tied to "**the carrying out of the by-laws**."
- **art. 678** lets an **RCM** adopt the same power.

## The council — and your right to speak

**art. 149** — "The sittings are **public**, and the proceedings must be **audible and intelligible**."

**art. 150 — the question period is statutory:** "The sitting of the council **includes a period during which the persons attending may put oral questions to the council members**." The council may **by by-law** prescribe its **length, timing and procedure**, and give **precedence to residents**, owners of an immovable, or occupants of a business establishment. **The right itself is unconditional — only its modalities are delegated. A municipality can shape it, not abolish it.**

**art. 148** — local councils sit **at least monthly**; RCM councils **at least every two months**. Decision-useful documents to **members** at least **72 hours** before (*to members, not the public*). **art. 145** — the sitting place must be "in the **most public place** in the territory", and **never where alcohol is sold**. **art. 164** — every member present **is bound to vote** unless exempted by interest.

**Access to documents:** the **clerk-treasurer** is custodian (art. 199) and certified copies are proof (art. 267.1) — but **the Code confers no general public right of access**. That lives in the **Act respecting access to documents held by public bodies (c. A-2.1)**.

## Fast answers

| Question | Answer |
|---|---|
| Does this Code apply to my city? | **Not if it's governed by the Cities and Towns Act (C-19)** — and charters override. Verify. |
| Where are the zoning rules? | **Not here — A-19.1.** But enforcement (inspection, fines, annulment) is here. |
| Can I challenge a by-law? | **Yes** — art. 689, any interested party, **$50** — but **within 3 months of its passing** (art. 692). |
| When does a by-law bite? | **On publication** (art. 450) — and what's published is a **notice**, not the text (art. 451). |
| Max by-law fine? | **$1,000 / $2,000** first offence; **$2,000 / $4,000** subsequent (art. 455). |
| Can an officer enter my home? | Only **7 a.m.–7 p.m.**, and only if the municipality **passed an art. 492 by-law**. Ask which one. |
| Do I get to ask the council questions? | **Yes — art. 150.** It's statutory; only the format is by-law. |

## Related

- [[quebec-legal-system]] — **municipal courts** (which prosecute by-law offences), and why **municipal by-laws are excluded from the Regulations Act** (R-18.1, s. 3¶2) — they run on this Code instead.
- [[quebec-civil-code]] — the *jus commune*; art. 423 of CCQ-1992 is why "municipal corporation" now reads "municipality".
- [[quebec-housing-rights]] — where a municipal angle meets a lease (e.g. CCQ art. 1856 change-of-**destination** requires **zoning** compliance — which is A-19.1, enforced via art. 492 here).
- [[quebec-charter-rights]] — the Charter binds the State, including municipalities (s. 54).

Sources: *Municipal Code of Québec*, CQLR c. **C-27.1**, current official consolidation on [LégisQuébec](https://www.legisquebec.gouv.qc.ca/en/document/cs/C-27.1), retrieved **2026-07** and parsed directly (1,566 sections; structure and ranges extracted from the body). The **French text is official**; the English is a translation. **Not analyzed:** the Schedule (Forms 1–23), and Titles XVI–XVIII.2, XXV and XXVIII beyond their headings.
