---
name: tn-landlord-tenant-codearranger
title: Tennessee Landlord-Tenant
description: Subject-matter bundle for Tennessee residential landlord-tenant disputes. Covers URLTA (§ 66-28) for counties over 75,000 population vs. general law (§ 66-7) for counties at or below 75,000; 14-day URLTA nonpayment notice (§ 66-28-505) with CARES Act 30-day overlay for federally-subsidized housing (Section 8, LIHTC, federally-backed mortgages); detainer-warrant practice in General Sessions (§ 29-18-101 et seq.) with 10-day de novo appeal to Circuit (§ 27-5-108) and possession bond (§ 29-18-130); security deposits (§ 66-28-301); warranty of habitability (§ 66-28-304); self-help-eviction prohibition (§ 66-28-504) with 3-month / 3x-damages remedy; retaliation presumption (§ 66-28-514); fair-housing (FHA, THRA); tenant-defense posture.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/tn-court-docs/skills/tn-landlord-tenant
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: real-estate
language: en
---

# Tennessee Landlord-Tenant

> **NOT LEGAL ADVICE.** Tennessee landlord-tenant law turns on which
> statutory scheme applies (URLTA vs. the general law), which depends
> on county population, plus the federal **CARES Act 30-day-notice**
> overlay for subsidized properties. Statute numbers, day counts,
> and the covered-county list change — verify every citation
> against the current Tenn. Code Ann. and the current census before
> relying. Consult a licensed Tennessee attorney about your specific
> case.

Use this subject-matter bundle for Tennessee residential
landlord-tenant matters — most commonly an **eviction (detainer
warrant)** defended by a tenant, but also security-deposit,
habitability, self-help-eviction, retaliation, and fair-housing
issues.

## At a glance — the six things that move every TN L/T case

1. **URLTA vs. § 66-7**: county-population threshold dictates the
   substantive scheme. Resolve **first**.
2. **General Sessions is the forum** for detainer warrants
   (§ 29-18-101 et seq.); 10-day **de novo appeal** to Circuit
   (§ 27-5-108).
3. **14-day URLTA nonpayment notice** under § 66-28-505 in
   URLTA counties; **30-day** for periodic tenancies under
   § 66-28-512 / § 66-7-109; **30-day CARES Act** for federally-
   subsidized housing (Section 8, LIHTC, federally-backed
   mortgages).
4. **Security deposit mechanics**: separate account under
   § 66-28-301; 30-day return with itemization; forfeiture
   waiver where landlord fails the procedure.
5. **Self-help eviction is prohibited** — lockouts, utility
   shutoffs, removal of belongings — both URLTA (§ 66-28-504 /
   -603) and § 66-7. Damages + injunction.
6. **Possession bond** under § 29-18-130(b): post to stay
   execution of possession judgment pending de novo appeal;
   case law has held appeal **not automatically dismissed** for
   bond default, but verify.

## Two statutory schemes — which one applies?

| Scheme | Statute | Coverage |
|---|---|---|
| **Uniform Residential Landlord and Tenant Act (URLTA)** | Tenn. Code Ann. § 66-28-101 et seq. | Counties with population **over 75,000** (decennial census; § 66-28-102) |
| **General landlord-tenant law** | Tenn. Code Ann. § 66-7-101 et seq. | Counties **at or below** 75,000 |

> **Do NOT hard-code the covered-county list.** The list of
> over-75,000 counties **shifts with each decennial census**. As of
> the 2020 census, approximately 23 of Tennessee's 95 counties
> exceeded the threshold (including Davidson, Shelby, Knox,
> Hamilton, Rutherford, Williamson, Montgomery, Sumner, Wilson,
> Blount, Bradley, Madison, Sevier, Washington, Maury, Anderson,
> Tipton, Hamblen, Putnam, Robertson, Greene, Cumberland, Bedford
> — confirm before pleading). The list shifts; the statute auto-
> updates with new census data.

The threshold question — **"Is this an URLTA county or a § 66-7
county?"** — should be the first thing resolved in any Tennessee
landlord-tenant matter. Getting it wrong changes the notice
periods, the security-deposit rules, the habitability framework,
and the available defenses.

## URLTA — key sections

| Topic | Section | Notes |
|---|---|---|
| Applicability | § 66-28-102 | Over 75,000 population (current census) |
| Scope exclusions | § 66-28-104 | Hotels, public housing, owner-occupied 4-or-fewer-unit, charitable, etc. |
| Security deposit | § 66-28-301 | Separate account; itemized list within 60 days; return within 30 days |
| Disclosure of owner/agent | § 66-28-302 | Required at or before tenancy |
| Landlord obligations | § 66-28-304 | Comply with codes; maintain fit and habitable; common areas; services |
| Tenant obligations | § 66-28-401 | Comply with codes affecting health and safety; maintain unit clean and sanitary |
| Tenant remedies (material noncompliance) | § 66-28-501 | 14-day notice to landlord; if not cured, termination or repair-and-deduct |
| Wrongful failure to deliver | § 66-28-503 | Tenant remedies if landlord fails to deliver possession |
| Unlawful ouster / self-help | § 66-28-504 | Damages + injunction; **prohibits lockouts and utility cutoffs** |
| Nonpayment notice | § 66-28-505 | 14 days from receipt; if rent paid in 14, no termination |
| Noncompliance affecting health/safety | § 66-28-507 | 14-day cure; written notice |
| Landlord access | § 66-28-403 | Reasonable times; 24-hour notice (presumptive) |
| Termination of periodic tenancy | § 66-28-512 | 30-day notice for month-to-month |
| Holdover | § 66-28-513 | Landlord remedies; damages |
| Retaliation | § 66-28-514 | Presumption of retaliation if landlord acts within 1 year of protected activity |
| Application of Tenn. R. Civ. P. | § 66-28-516 | URLTA does **not** displace civil procedure in non-GS forums |

## Non-URLTA counties (§ 66-7 et seq.) — key differences

- **No statutory 14-day-cure protection** for nonpayment.
  Notice period is governed by lease + common law.
- **Periodic-tenancy notice**: 30 days under § 66-7-109 for
  month-to-month.
- **No statutory habitability standard** — implied common-law
  habitability is more limited. Defenses lean on lease + housing-
  code violations.
- **Security deposit**: no statutory framework — lease + common
  law. Defenses lean on contract + unjust enrichment.

## Eviction = detainer warrant (forcible entry & detainer)

Regardless of the substantive scheme, evictions proceed by
**detainer warrant** under Tenn. Code Ann. § 29-18-101 et seq.

### Forum and procedure

- **General Sessions Court** — unlimited subject-matter
  jurisdiction over **possession**, despite the ordinary $25,000
  civil cap; monetary judgment for rent / damages is **capped at
  $25,000** under § 16-15-501 (any larger arrears claim must
  pursue separately).
- **No formal discovery as of right** in General Sessions —
  Tenn. R. Civ. P. do not apply (§ 16-15-105 procedural
  informality).
- **Service** under § 29-18-115: personal service, residential
  service on persons of suitable age, or **posting** after
  diligent inquiry. Posting is a frequent service-quality issue
  for tenants who miss the warrant.
- **Return date** — six days after issuance under § 29-18-117;
  the docket call is typically same-day or next-day.
- **Hearing** is informal; landlord proves lease + breach + notice
  compliance; tenant raises defenses orally.
- **Judgment**: possession + arrears within the General Sessions
  cap.
- **Writ of possession** issued after the 10-day appeal window
  closes under § 27-5-108; sheriff executes typically within
  several days.

### De novo appeal to Circuit (§ 27-5-108)

- **10-day clock** from General Sessions judgment.
- **De novo trial in Circuit** under the full Tenn. R. Civ. P.
  — discovery, summary judgment, jury (if demanded).
- **Possession bond** under § 29-18-130(b): tenant must post
  bond equal to one year's rent to stay execution pending
  appeal; the bond is **stayed-execution-only**, not appeal-
  dismissal — case law (e.g., *Johnson v. Hopkins*, 432 S.W.3d
  840 (Tenn. 2013)) has held appeal not automatically dismissed
  for bond default, but verify.
- **Pauper's oath** (uniform indigency procedure) may substitute
  for bond on showing of indigency under § 20-12-127.
- Practical effect: **de novo appeal is the principal vehicle
  for accessing formal discovery and counsel-led litigation** in
  a Tennessee eviction defense.

### CARES Act 30-day notice overlay (federally-subsidized properties)

Under Section 4024(c) of the federal CARES Act (still in force),
**federally-subsidized rental properties** — Section 8 vouchers,
LIHTC tax-credit properties, USDA Rural Development, Section
202/811, and properties with federally-backed mortgages — require
**30 days' written notice** before filing for nonpayment,
displacing the URLTA 14-day rule.

- Confirmed in *Schiminger v. Cooperage Project, LLC*, M2023-
  01281-COA-R3-CV (Tenn. Ct. App. 2024).
- Landlord must affirmatively comply; tenant should plead
  defective notice if 14-day URLTA notice was given on a
  federally-subsidized property.
- Plaintiff cannot remedy by amending notice mid-case; defective
  notice **defeats the action**.

## Security deposits

URLTA imposes specific mechanics:

- **Separate account** at a Tennessee bank or other federally-
  insured institution (§ 66-28-301(a)).
- **Itemized statement** of deductions to tenant within **60
  days** of move-out.
- **Return of balance** within **30 days** after itemization
  (effectively a 30-day return-after-itemization, or 60+30 =
  effectively 60 days from move-out for full process).
- **Failure to provide itemized list within 60 days** → landlord
  **forfeits the right to retain** any portion of the deposit
  (§ 66-28-301(g)). Strong tenant remedy.
- **Damages**: tenant may recover the deposit + attorney's fees
  (where lease allows or under common-law unjust enrichment).

## Warranty of habitability and the repair obligation

URLTA imposes statutory maintenance duties:

- **Comply with applicable building / housing codes** materially
  affecting health and safety (§ 66-28-304(a)(1)).
- **Maintain fit and habitable condition** (§ 66-28-304(a)(2)).
- **Common areas and shared facilities** maintained in safe
  condition (§ 66-28-304(a)(3)).
- **Essential services**: running water, hot water, heat in
  appropriate weather (§ 66-28-304(a)(5)-(6)).

**Tenant remedies under § 66-28-501**:

1. **14-day written notice** to landlord specifying the
   noncompliance.
2. If not cured within 14 days, tenant may:
   - **Terminate** the rental agreement and recover deposit;
   - **Recover damages** for the noncompliance;
   - **Obtain injunctive relief** in Chancery or Circuit (not
     General Sessions).

**Limited repair-and-deduct**: Tennessee does **not** have a
broad statutory repair-and-deduct remedy comparable to
California's; the URLTA framework relies on notice-and-cure +
termination + damages.

In **non-URLTA counties**, habitability lives in common law
(*Tennessee Real Estate Comm'n v. Potts*, 537 S.W.2d 433 (Tenn.
1976) — pre-URLTA implied warranty) and is materially weaker.

## Retaliation — § 66-28-514

URLTA prohibits landlord retaliation:

- **Presumptively retaliatory acts within 1 year** of protected
  tenant activity:
  - complaint to housing authority / public agency about code
    violation;
  - complaint to landlord about noncompliance;
  - joining or organizing a tenants' union;
  - exercising any URLTA right.
- **Retaliatory acts barred**: increase in rent, decrease in
  services, eviction, refusal to renew.
- **Exceptions** at § 66-28-514(b): landlord may evict for
  nonpayment, criminal activity, or substantial damage, even
  during the 1-year presumption window.
- **Damages**: 3 months' rent or actual damages, whichever is
  greater + attorney's fees.

Non-URLTA counties have **no statutory retaliation protection**;
analysis runs through public-policy / federal Fair Housing Act
retaliation.

## Self-help eviction is prohibited

Under URLTA § 66-28-504 and § 66-28-603 and parallel common-law
rules in § 66-7 counties:

- **No lockouts** — landlord cannot change locks without writ
  of possession.
- **No utility shutoffs** — landlord cannot terminate water,
  electricity, gas, or heat to force vacancy.
- **No removal of tenant's belongings** without writ + sheriff.

**Tenant remedy under § 66-28-504(b)**: damages **+ 3 months'
rent or three times the actual damages**, whichever is greater +
costs + attorney's fees + injunctive relief.

This is a **plaintiff's claim** that flips the eviction-defense
posture into an affirmative case for damages and injunction.

## Fair-housing overlay

| Source | Protections | Coverage |
|---|---|---|
| Federal Fair Housing Act (42 U.S.C. § 3601 et seq.) | Race, color, national origin, religion, sex, familial status, disability | All housing with limited exceptions |
| **Tennessee Human Rights Act** (Tenn. Code Ann. § 4-21-601) | Race, color, creed, religion, sex, age, disability, national origin | 8+ unit threshold for some THRA protections |
| **Memphis Source of Income Ordinance** | Section 8 voucher holders | Memphis only |
| Nashville | **No source-of-income protection** as of current ordinance status — verify |

## Tenant-defense posture in a detainer case

1. **Which scheme applies** — URLTA (§ 66-28) or general law
   (§ 66-7)? County population.
2. **CARES Act 30-day notice** — is the property federally
   subsidized? If yes, the 14-day URLTA notice is defective.
3. **Defective predicate notice** — no written notice; wrong
   notice period; wrong amount demanded; bundled late fees /
   charges; demand for accelerated rent.
4. **Defective service / process** of the detainer warrant —
   posting where personal service was possible; service on a
   minor or non-resident.
5. **Rent paid / tendered** before judgment, or improper charges
   bundled.
6. **Breach of habitability / maintenance** under § 66-28-304
   raised defensively + as counterclaim under § 66-28-501.
7. **Retaliation** under § 66-28-514 — protected act within 1
   year + adverse action.
8. **Self-help eviction** under § 66-28-504 — counterclaim for
   lockouts / shutoffs / belongings removal.
9. **Fair-housing discrimination** — protected-class
   adverse action.
10. **Procedural relief**: the 10-day **de novo appeal** under
    § 27-5-108 is the gateway to formal discovery; consider
    indigency oath in lieu of bond.

## Affirmative tenant claims (when the tenant brings the case)

- **Wrongful eviction / self-help** — § 66-28-504 damages + 3
  months' rent / 3x actual + fees.
- **Security-deposit forfeiture** — § 66-28-301(g) damages.
- **Habitability damages** — § 66-28-501 termination + damages.
- **Retaliation damages** — § 66-28-514 damages.
- **Fair-housing damages** — FHA / THRA.

## Drafting checklist

- [ ] Confirm county population — URLTA or § 66-7?
- [ ] If subsidized property, confirm CARES Act 30-day notice
      was given; otherwise plead defective notice.
- [ ] Pull the **lease + notice + payment records + photos** at
      intake — the General Sessions hearing is fast and
      evidence-poor.
- [ ] If filing detainer warrant: use AOC civil-warrant form;
      file in proper General Sessions venue (where property
      located); confirm 6-day return-date scheduling.
- [ ] If defending: appear at the return date (failure to
      appear = default possession judgment); raise notice
      defects orally; preserve appeal rights.
- [ ] If appealing de novo: file notice within 10 days under
      § 27-5-108; address bond (§ 29-18-130) or pauper's oath
      (§ 20-12-127).
- [ ] If pursuing affirmative claims (self-help, habitability,
      retaliation, security deposit): consider filing in
      Chancery or Circuit for the equitable remedies and
      potential class certification under Tenn. R. Civ. P. 23.

## Composition

- For statewide format: `tn-statewide-format`
- For General Sessions venue + 10-day appeal: `tn-general-sessions`
- For Chancery / Circuit venue on affirmative tenant claims:
  `tn-davidson`, `tn-shelby`, `tn-knox`, `tn-hamilton`,
  `tn-county-courts`
- For first response triage in detainer: `tn-first-30-days`
- For drafting motions / declarations / orders: `tn-draft-motion`,
  `tn-draft-declaration`, `tn-draft-order`
- For 10-day appeal clock + deadlines: `tn-deadlines`
- For fair-housing employment-discrimination overlap: `tn-employment`
- For post-judgment / writ-of-possession execution: `tn-post-judgment`
- For QC: `tn-quality-check`, `tn-fact-check`

## References

- `tn-law-references` — Tenn. Code Ann., Tenn. R. Civ. P., and
  federal symlinks
- Tenn. Code Ann. § 66-28-101 et seq. — URLTA
- Tenn. Code Ann. § 66-7-101 et seq. — general L/T (non-URLTA)
- Tenn. Code Ann. § 29-18-101 et seq. — detainer warrants (FED)
- Tenn. Code Ann. § 27-5-108 — 10-day de novo appeal
- Tenn. Code Ann. § 29-18-130 — possession bond
- Tenn. Code Ann. § 4-21-601 — Tennessee Human Rights Act fair-
  housing
- CARES Act § 4024(c) (P.L. 116-136) — 30-day notice for
  federally-subsidized housing
- *Schiminger v. Cooperage Project, LLC* (Tenn. App. 2024) —
  CARES 30-day notice still in force
- *Johnson v. Hopkins*, 432 S.W.3d 840 (Tenn. 2013) — possession
  bond + appeal dismissal
