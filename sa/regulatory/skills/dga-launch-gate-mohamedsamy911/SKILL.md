---
name: dga-launch-gate-mohamedsamy911
title: DGA launch gate
description: Pre-launch DGA compliance gate for a Saudi government digital service — the transparency, content, registration and platform-integration requirements beyond design. Use before go-live, for a compliance audit, or when asked what a Saudi government site must publish.
author: mohamedsamy911
author_url: https://github.com/mohamedsamy911/dga-kit/tree/master/skills/dga-launch-gate
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: sa
practice: regulatory
language: en
sources:
- title: Assessment Criteria
  path: references/assessment-criteria.md
- title: Checklist
  path: references/checklist.md
---

# DGA launch gate

Wider than design. This is the go-live checklist: what a Saudi government platform must
**publish and integrate**, not how it must look. Design compliance is `dga-design-review`'s job;
accessibility is `dga-a11y`'s. This skill owns everything else.

Sourced from DGA's template guidelines, chiefly **About the Entity** and **e-Participation** —
the two pages carrying the transparency mandate. Full detail in
`../dga-design-system/references/patterns.md`.

## Run in this order — registration first

### 1 · Registration and identity (start early — these have lead times)
- [ ] **DGA registration number** obtained, tied to the entity's **License Number**
- [ ] **Digital Stamp** component present and populated with both
- [ ] Domain correct for entity type — authorities and ministries are **`gov.sa`**
- [ ] HTTPS, verifiable through the Digital Stamp

> 🚩 The registration number is a procurement dependency, not a build task. Chase it in week one.

### 2 · Required on every page
- [ ] **Feedback section** — "Was this page useful?" with Yes/No **and** reason options
- [ ] **Last modified date for the page** *and* **for the platform** (both, not one)
- [ ] **Skip-to-content link** at the start of the header
- [ ] **Accessibility Tools** in the footer — font size and contrast controls, **first in tab order**
- [ ] Header and footer unmodified — original structure, colours and fonts
- [ ] Both locales exist; language toggle reloads **every** element including interactive content

### 3 · Required pages
- [ ] Home · Contact us · Help & Support · FAQs · Sitemap · **404** · Search · Content
- [ ] **About the Entity** (see §4) · **e-Participation** (see §5)
- [ ] **Cookies banner** — message, Privacy Policy link, Accept All, Reject All, Manage
      Preferences; Strictly Necessary always on and uneditable
- [ ] Prescribed navigation paths, reflected in the sitemap:
      `Homepage > About the Entity > e-Participation` and `… > Contact us`

### 4 · About the Entity — the transparency mandate
- [ ] Senior management: photos, official information, biography links, contact details, unified format
- [ ] All departments, each expanding in place to a one-or-two sentence description
- [ ] **Organisational diagram built as a real diagram, NOT an image** (readability and accessibility)
- [ ] Sister entities
- [ ] Links to the national platforms: `my.gov.sa` · `data.gov.sa` · `istitlaa.ncc.gov.sa` ·
      Tafaul · `boe.gov.sa` · `etimad.gov.sa` · Jadaara
- [ ] Strategies listed and linked, archived ones marked `[Archived]`
- [ ] Policies published: core functional · **Service Level Agreement** · **Privacy Policy** ·
      **Freedom of Information** · **Data Sharing** · **Open Data** · **E-Participation** ·
      **Sustainable Development**; plus regulations and bylaws
- [ ] **Budgets: current plus the last five**, each linked to the MoF National Budget page *and*
      its open dataset
- [ ] Tenders via **Etimad** — planned, open and completed, each with step-by-step access instructions
- [ ] Partnerships across five categories (international, government, private, civil society,
      academic), each with objectives, target groups, benefits, timeline, projects, outcomes
- [ ] UN SDGs: overview, all 17 listed, **up to 5** the entity contributes to, tied to Vision 2030
- [ ] Careers: planned recruitment, open vacancies, **Jadarat** links, volunteering if applicable
- [ ] News newest-first and filterable; events filterable by category, date or alphabetically

### 5 · e-Participation and Open Data
- [ ] e-Participation page, visible on the homepage and in the top nav
- [ ] Open Data section referencing the **National Open Data Platform**, linking the entity's
      section on **open.data.gov.sa**
- [ ] **Open Data Policy** aligned with National Data Management Office legislation
- [ ] **Open Data Library** — datasets, publication frequency, national platform link
- [ ] **Open Data Use Cases**
- [ ] **Open Data Request** form — process, mechanism, response time, **automatic acknowledgement**
- [ ] **Performance statistics page**, reachable from the footer, previous year from 1 January,
      from Google Analytics; "Was this page useful?" as a pie chart with percentages visible
      without hover; totals and per-reason counts; support tables **≤10 rows × 10 columns**

### 6 · Measurement regimes
The entity is scored against these; adopting Platforms Code feeds both:
- [ ] **Digital Transformation Measurement Indicator**
- [ ] **Digital Experience Maturity Indicator**
- [ ] DGA's own **Assessment Criteria** — `/AssessmentCriteria`, captured 2026-08-27

> `TODO(harvest)` — the **two indicators** are published **outside** design.dga.gov.sa and have
> NOT been captured. This skill is not complete until they are.
>
> ## The verdict is INCOMPLETE, not PASS
>
> While the two indicators are uncaptured, **this skill may not issue a PASS.** The permitted
> overall verdicts are:
>
> | Verdict | When |
> |---|---|
> | **FAIL** | any checked item fails. A failure found against a partial rubric is still a real failure. |
> | **INCOMPLETE** | everything checked passes, but the two Measurement Indicators were not scored because the kit does not hold them. |
>
> **PASS is unavailable.** It would assert that the platform meets DGA's requirements, and this
> skill cannot see two of the regimes it is scored against — so a PASS would be an unearned
> go-live approval carrying this kit's name. Report INCOMPLETE, name the two missing inputs, and
> say plainly that clearing them requires the entity's own reading of the indicators. A green
> artefact that quietly excludes part of the rubric is worse than no artefact: it gets forwarded
> to people who will not read this paragraph.

**The Assessment Criteria are published.** Full rubric in `references/assessment-criteria.md` —
read it before any go-live call. In short:

- **Four scored categories:** Accessibility · Consistency · Design · Usability
- **Four Mandatory criteria** — DGA's page groups them under the heading *Essential*: Design
  System Compliance · Typography and Color Standards · Layout and Spacing (mobile-first, spacing
  grid) · Mobile Usability. DGA's stated consequence, verbatim:
  a project failing these **"*typically* cannot proceed to deployment"**. Report it with the hedge — DGA describes the
  normal outcome and names no exception process, so this gate must not upgrade it to a guarantee
- **Four Recommended criteria**, including *"Ensure an **Arabic-first content strategy**"* — DGA's
  own words, so cite `/AssessmentCriteria` rather than presenting Arabic-first as this kit's
  inference
- **Optional** is named but has no published criteria. Do not invent them
- Submit **two weeks ahead**; the review runs **~20 days** with a revision cycle built in. Budget
  five weeks from "done" to approval
- Scored 1–100 in ten named bands. **No passing threshold is published** — do not quote a target

> The downloadable checklist *file* is still **not obtained**. The page is captured; the file is
> separate. Do not claim item-level coverage of the checklist.

## Output

Pass/fail per item, with evidence links and a named owner for every open item. This is the
artefact attached to the go-live approval.
