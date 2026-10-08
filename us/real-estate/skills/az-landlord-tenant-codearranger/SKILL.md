---
name: az-landlord-tenant-codearranger
title: Arizona Landlord-Tenant
description: 'Subject-matter bundle for Arizona residential landlord-tenant disputes — evictions ("special detainer" in Justice Court), predicate notices, security deposits, habitability, maintenance duties, repair-and-deduct, retaliation. Triggers: "eviction Arizona", "special detainer Arizona", "5-day notice Arizona rent", "10-day notice Arizona lease violation", "ARLTA A.R.S. 33-1301", "Arizona Residential Landlord and Tenant Act", "Arizona security deposit", "Arizona landlord tenant", "RPEA Arizona eviction", "forcible detainer Arizona", "writ of restitution Arizona", "Arizona habitability", "repair and deduct Arizona", "retaliation Arizona". Covers ARLTA (A.R.S. § 33-1301 et seq.), special detainer (§ 33-1377) under Rules of Procedure for Eviction Actions (RPEA), notice regime (§ 33-1368), security deposits (§ 33-1321), maintenance duty, repair-and-deduct (§ 33-1363), retaliation (§ 33-1381), Mobile Home Parks Act.'
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/az-court-docs/skills/az-landlord-tenant
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: real-estate
language: en
---

# Arizona Landlord-Tenant

> **NOT LEGAL ADVICE.** Arizona residential landlord-tenant law turns
> on the distinction between the **Arizona Residential Landlord and
> Tenant Act (ARLTA)** — the substantive obligation statute — and the
> **eviction process** ("special detainer" under A.R.S. § 33-1377,
> prosecuted under the **Rules of Procedure for Eviction Actions
> (RPEA)**). Statute numbers, notice day-counts, and the
> security-deposit cap change — verify every citation against the
> current Arizona Revised Statutes and the current RPEA before
> relying. Consult a licensed Arizona attorney about your specific
> case.

Use this subject-matter bundle for Arizona residential
landlord-tenant matters — most commonly an **eviction (special
detainer action)** defended by a tenant, but also security-deposit,
habitability, repair, and retaliation issues. The eviction forum is
the **Justice Court** — see `az-justice-courts` for venue, filing,
and the JP-precinct mechanics.

## At a glance — the things that move every AZ L/T case

1. **ARLTA governs.** Residential tenancies run under the **Arizona
   Residential Landlord and Tenant Act, A.R.S. § 33-1301 et seq.**
   Mobile-home-park tenancies run under a **separate** act (A.R.S.
   § 33-1401 et seq. — see below).
2. **Eviction = "special detainer."** Filed in **Justice Court**
   under **A.R.S. § 33-1377** and prosecuted under the **RPEA** — a
   distinct rule set. The timeline is **very fast**.
3. **Predicate notice is the gatekeeper.** A proper written notice
   under **A.R.S. § 33-1368** must precede the special detainer; the
   wrong period, wrong amount, or no service defeats it.
4. **Notice clocks** dominate: **5-day** for nonpayment of rent
   (§ 33-1368(B)); **10-day** cure for material noncompliance with the
   rental agreement (§ 33-1368(A)); a separate **5-day** cure for
   § 33-1341 noncompliance materially affecting health and safety
   (§ 33-1368(A)); and **immediate** for material-and-irreparable
   breach (§ 33-1368(A)). "Days" are calendar days (§ 33-1368(G)).
   Verify against the corpus.
5. **Security deposit** capped at **1-1/2 months' rent** (A.R.S.
   § 33-1321), with a **14-business-day** return-and-itemization
   rule. See corpus for the cap and the day-count.
6. **Writ of restitution** is the eviction order (§ 33-1377); it does
   not issue the instant judgment enters — confirm the timing in the
   RPEA / corpus.

## The eviction = special detainer action

Arizona residential evictions proceed as a **special detainer
action** under **A.R.S. § 33-1377**, filed in **Justice Court** and
governed by the **Rules of Procedure for Eviction Actions (RPEA)** —
a fast, special statutory proceeding, not an ordinary civil action.
The older general **forcible entry / forcible detainer** statute
(**A.R.S. § 12-1171 et seq.**) supplies the background possessory
framework and still applies to non-ARLTA possession disputes; ARLTA
residential evictions run through § 33-1377 + the RPEA.

### The compressed timeline (A.R.S. § 33-1377)

- The **summons** commands the defendant to appear and answer at a
  time and place **not more than six nor less than three days** from
  the date of the summons. Verify against the current statute + RPEA.
- For a **material-and-irreparable breach** case, the **trial date
  and return date are set no later than the third day** following
  the filing of the complaint.
- The **return date is the trial date** — the tenant must appear and
  be ready; there is no leisurely answer period as in ordinary civil
  practice. Failure to appear → **default judgment for possession**.
- If the plaintiff prevails, the court **grants a writ of
  restitution**; confirm the issuance timing + any stay in the RPEA
  and the corpus.

See `az-justice-courts` for the precinct, e-filing (AZTurboCourt),
and JP-court mechanics that wrap around the RPEA process.

## Predicate notices — A.R.S. § 33-1368

The written notice is the gatekeeper to a special detainer. ARLTA
defines three notice tracks (verify exact day-counts in the corpus):

| Ground | Statute | Notice (verify in corpus) |
|---|---|---|
| **Nonpayment of rent** | A.R.S. § 33-1368(B) | **5-day** written notice; tenant may **pay to cure** within the period |
| **Material noncompliance** with the rental agreement (incl. material falsification on the application) | A.R.S. § 33-1368(A) | **10-day** notice with a **cure right** — terminates if not remedied in 10 days |
| **Noncompliance with § 33-1341 materially affecting health and safety** | A.R.S. § 33-1368(A) | **5-day** notice with a **cure right** — terminates if not remedied in 5 days |
| **Material and irreparable breach** | A.R.S. § 33-1368(A) | **Immediate** written notice for termination — no cure period |

Nonpayment (§ 33-1368(B)): written notice that the agreement
terminates if rent is unpaid **within 5 days**; the tenant keeps a
**pay-to-cure** right in that window. Material noncompliance with the
rental agreement (§ 33-1368(A), first paragraph): a material breach
(including material falsification on the application) terminates on a
date **not less than 10 days** after receipt if not remedied in 10
days. A separate track — noncompliance with **§ 33-1341** materially
affecting health and safety (§ 33-1368(A)) — carries the shorter
**5-day** cure. Material-and-irreparable breach (§ 33-1368(A)): serious
conduct (e.g., serious property damage, criminal/violent acts) →
**immediate** termination, no cure. Note § 33-1368(G) defines "days"
as **calendar days**. Service modes + exact day-count math live in the
corpus — verify.

## Security deposits — A.R.S. § 33-1321

| Topic | Rule (verify exact counts in corpus) |
|---|---|
| **Cap** | Security (including prepaid rent) **shall not exceed 1-1/2 months' rent** |
| **Move-in inspection** | Tenant may request a move-in inspection / itemized statement of existing damage |
| **Return + itemization** | Within **14 days, excluding Saturdays, Sundays, and legal holidays** (i.e., **14 business days**) after termination, delivery of possession, **and** the tenant's demand, the landlord must provide an **itemized list of all deductions** + pay the balance due |
| **Wrongful-retention remedy** | A landlord who fails to comply with § 33-1321(D) is liable for the property/money due **plus damages equal to twice the amount wrongfully withheld** (§ 33-1321(E)) |

The clock runs from termination + delivery of possession + the
tenant's **demand**; a landlord who keeps the deposit without the
statutory itemization exposes itself to the § 33-1321(E)
wrongful-retention remedy of the amount wrongfully withheld **plus
damages equal to twice that amount**. Note also the **60-day**
tenant-dispute window in § 33-1321(D): if the tenant does not dispute
the itemized list within 60 days after it is mailed, the amounts are
deemed valid and final. Verify the cap, the day-count, and the
remedy in the corpus.

## Habitability + the landlord's maintenance duty — A.R.S. § 33-1324

A.R.S. § 33-1324 imposes the landlord's **duty to maintain fit
premises** — comply with applicable building and health codes
materially affecting health and safety, make all repairs to keep the
premises in a fit and habitable condition, maintain common areas, and
supply running water, reasonable heat, and essential services. This
is the habitability hook for tenant defenses and affirmative claims.

### Tenant remedies for a habitability breach

- **Repair-and-deduct (A.R.S. § 33-1363)**: for a minor-defect /
  failure-to-repair scenario, the tenant may — after the statutory
  written notice and waiting period — have the work done and **deduct
  the cost from rent**, subject to the statute's dollar/fraction cap.
  Verify the notice period, cap, and prerequisites in the corpus.
- **Other ARLTA remedies**: depending on the breach — termination,
  rent-abatement, self-help essential services (§ 33-1364), or
  damages. Frame these through the specific ARLTA section; Arizona
  does **not** recognize a freestanding rent-withholding self-help
  right outside the statutory mechanisms — verify which applies.

## Retaliation — A.R.S. § 33-1381

A landlord may not **retaliate** by raising rent, decreasing
services, or bringing or threatening an eviction after a tenant's
**protected activity** — e.g., complaining to a governmental agency
about a building/health-code violation, complaining to the landlord
about a § 33-1324 maintenance failure, or organizing/joining a
tenants' union.

- Evidence of a protected complaint **within six months** prior to the
  alleged retaliatory act creates a **presumption** of retaliation
  (§ 33-1381(B)); the presumption does **not** arise if the tenant
  complained after notice of termination. The remedies are those in
  § 33-1367, plus a defense to possession.
- Statutory **exceptions** let the landlord still proceed for genuine
  nonpayment or a serious, non-retaliatory ground — verify.
- Retaliation is a **defense to possession** in the special detainer,
  not merely a damages theory.

## Judgment, the writ of restitution, and appeal

1. **Judgment for possession** at the return-date trial states the
   amount due and the basis for possession.
2. **Pay-to-cure / reinstatement** in a nonpayment case: the tenant
   may retain possession by paying rent + statutory costs within the
   window the statute allows — confirm in § 33-1368(B) + the RPEA.
3. **Writ of restitution (A.R.S. § 33-1377)** directs the
   constable/sheriff to restore possession to the landlord; it does
   not necessarily issue the instant judgment enters — confirm the
   issuance timing + any stay in the RPEA / corpus.
4. **Appeal** runs from Justice Court to **Superior Court** (see
   `az-justice-courts`); a stay on appeal generally requires a bond /
   escrow of accruing rent. Verify the appeal period + bond rule.

## Tenant-defense posture in a special detainer

1. **Defective predicate notice** — no written notice; wrong period
   (5-day nonpayment vs. 10-day noncompliance vs. immediate); wrong
   amount; bundled late fees / non-rent charges; wrong ground.
2. **Defective service** of the notice or the summons/complaint.
3. **Rent paid / tendered to cure** within the § 33-1368(B) window.
4. **Breach of the § 33-1324 maintenance duty** as defense / setoff
   and counterclaim; repair-and-deduct compliance (§ 33-1363).
5. **Retaliation** (§ 33-1381) — protected activity + adverse action
   within the presumption window.
6. **Security-deposit counterclaim** — § 33-1321 itemization failure.
7. **Fair-housing discrimination** — federal FHA + Arizona Fair
   Housing Act (verify coverage).
8. **Procedural relief** — appear at the **return-date trial**
   (failure = default possession); challenge the writ timing.

## Affirmative tenant claims (when the tenant brings the case)

- **Security-deposit wrongful retention** — A.R.S. § 33-1321.
- **Habitability / maintenance-duty damages** — A.R.S. § 33-1324.
- **Unlawful ouster / self-help eviction** — ARLTA prohibits
  landlord self-help (lockouts, utility shutoffs, removing
  belongings) and gives the tenant a damages remedy — verify the
  controlling ARLTA section.
- **Fair-housing damages** — FHA / Arizona Fair Housing Act.

## Mobile home parks — A.R.S. § 33-1401 et seq.

A tenancy in a **mobile-home park** (where the tenant owns the home
and rents the lot) is **not** governed by ARLTA. It runs under the
**Arizona Mobile Home Parks Residential Landlord and Tenant Act,
A.R.S. § 33-1401 et seq.**, which has its **own** notice periods,
deposit rules, and termination grounds. When the matter involves a
mobile-home-park lot tenancy, work from the § 33-1401 act — **not**
the § 33-1301 ARLTA sections above — and verify the distinct
day-counts in the corpus.

## Drafting checklist

- [ ] Identify the **ground** and confirm the matching § 33-1368
      notice track (5-day nonpayment / 10-day noncompliance /
      immediate irreparable).
- [ ] Confirm the predicate notice was **properly served** and the
      period **expired** before the special detainer was filed.
- [ ] Pull the **lease + notice + ledger + photos** at intake — the
      return-date trial is fast and evidence-light.
- [ ] Confirm the forum is the correct **Justice Court precinct**
      (see `az-justice-courts`) and the RPEA governs procedure.
- [ ] If defending: appear at the **return-date trial**; raise notice
      defects; assert § 33-1324 + repair-and-deduct (§ 33-1363);
      plead retaliation (§ 33-1381) where applicable.
- [ ] Security-deposit dispute: confirm the tenant's **demand**, the
      **1-1/2-month** cap, and the **14-business-day** itemization
      window (§ 33-1321).
- [ ] Mobile-home-park lot tenancy → switch to the **§ 33-1401 act**.
- [ ] After judgment: track the **writ of restitution** timing
      (§ 33-1377) and the Superior Court appeal + bond.

## Composition

- Statewide format: `az-statewide-format`
- Eviction forum (Justice Court, RPEA, precinct, e-filing):
  `az-justice-courts`
- First-response triage: `az-first-30-days`
- Drafting: `az-draft-motion`, `az-draft-declaration`,
  `az-draft-order`, `az-draft-note`
- Deadlines / notice arithmetic: `az-deadlines`
- Post-judgment / writ-of-restitution execution: `az-post-judgment`
- QC: `az-quality-check`, `az-fact-check`

## References

- `az-law-references` — A.R.S., court rules, and federal symlinks
- A.R.S. § 33-1301 et seq. — Arizona Residential Landlord and Tenant
  Act (ARLTA)
- A.R.S. § 33-1377 — special detainer action + writ of restitution
- Rules of Procedure for Eviction Actions (RPEA) — eviction procedure
- A.R.S. § 12-1171 et seq. — forcible entry and detainer (background
  possessory framework)
- A.R.S. § 33-1368 — notices (5-day nonpayment per (B); 10-day
  material-noncompliance cure and 5-day § 33-1341 health-and-safety
  cure per (A); immediate material-and-irreparable breach per (A);
  "days" = calendar days per (G))
- A.R.S. § 33-1321 — security deposits (1-1/2-month cap,
  14-business-day itemization, wrongful-retention remedy)
- A.R.S. § 33-1324 — landlord's duty to maintain fit premises
- A.R.S. § 33-1363 — repair-and-deduct; § 33-1364 — essential services
- A.R.S. § 33-1381 — retaliatory conduct prohibited
- A.R.S. § 33-1401 et seq. — Mobile Home Parks Residential Landlord
  and Tenant Act
