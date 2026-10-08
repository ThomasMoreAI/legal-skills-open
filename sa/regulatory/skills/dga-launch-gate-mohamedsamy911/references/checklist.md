# DGA go-live checklist

Tickable form of `SKILL.md`. Attach the completed copy to the go-live approval.

**Service:** ______________________  **Date:** __________  **Signed off by:** ______________

## 0 · Registration — start in week one, these have lead times

- [ ] DGA registration number obtained
- [ ] Entity License Number obtained
- [ ] Digital Stamp populated with both
- [ ] Domain correct for entity type (an authority is `gov.sa`; see DGA's domain table)
- [ ] HTTPS live and verifiable through the Digital Stamp

## 1 · On every page

- [ ] Feedback: "Was this page useful?" + Yes/No + **reason options**
- [ ] Last modified date — **page**
- [ ] Last modified date — **platform**
- [ ] Skip-to-content link at the start of the header
- [ ] Accessibility Tools in the footer (font size, contrast)
- [ ] Accessibility Tools **first in tab order**
- [ ] Header and footer unmodified — original structure, colours, fonts
- [ ] Page exists in **both** `ar` and `en`
- [ ] Language toggle reloads every element, interactive content included

## 2 · Required pages

- [ ] Home · [ ] Contact us · [ ] Help & Support · [ ] FAQs · [ ] Sitemap
- [ ] 404 with friendly message + "Back to homepage" CTA
- [ ] Search · [ ] Content
- [ ] About the Entity (§3) · [ ] e-Participation (§4)
- [ ] Cookies banner — message, Privacy Policy link, Accept All, Reject All, Manage Preferences
- [ ] Cookies: Strictly Necessary always on and uneditable
- [ ] Nav path `Homepage > About the Entity > e-Participation` reflected in the sitemap
- [ ] Nav path `Homepage > About the Entity > Contact us` reflected in the sitemap

## 3 · About the Entity — transparency mandate

- [ ] Senior management: photos, official info, bio links, contacts, unified format
- [ ] All departments, each expanding in place
- [ ] Organisational diagram — **built as a diagram, NOT an image**
- [ ] Sister entities
- [ ] National platform links: my.gov.sa · data.gov.sa · istitlaa.ncc.gov.sa · Tafaul ·
      boe.gov.sa · etimad.gov.sa · Jadaara
- [ ] Strategies listed + linked, archived marked `[Archived]`
- [ ] Policies: core · SLA · **Privacy** · **Freedom of Information** · **Data Sharing** ·
      **Open Data** · **E-Participation** · **Sustainable Development**
- [ ] Regulations and bylaws page
- [ ] Budgets — current **plus last five**, each linked to MoF National Budget + open dataset
- [ ] Tenders via Etimad — planned, open, completed, with access instructions
- [ ] Partnerships × 5 categories, each with objectives/groups/benefits/timeline/outcomes
- [ ] UN SDGs — overview, all 17, up to 5 the entity contributes to, tied to Vision 2030
- [ ] Careers — planned, open, Jadarat links, volunteering if applicable
- [ ] News newest-first + filterable; events filterable

## 4 · e-Participation and Open Data

- [ ] e-Participation page, on homepage and in top nav
- [ ] Open Data section referencing the National Open Data Platform
- [ ] Entity section linked on **open.data.gov.sa**
- [ ] Open Data Policy, aligned with NDMO legislation
- [ ] Open Data Library — datasets, publication frequency, platform link
- [ ] Open Data Use Cases
- [ ] Open Data Request form — process, mechanism, response time
- [ ] Request form sends an **automatic acknowledgement**
- [ ] Performance statistics page, reachable from the footer
- [ ] Stats: previous year from 1 January, from Google Analytics
- [ ] "Was this page useful?" as a pie chart, percentages visible **without hover**
- [ ] Totals and per-reason counts shown
- [ ] Support tables ≤ 10 rows × 10 columns

## 5 · Design and accessibility

- [ ] `dga-design-review` run on every template — zero Blockers
- [ ] `dga-a11y` run against the built app in **both** locales — zero Blockers
- [ ] Contrast pairings checked against `CONTRAST-AUDIT.md`
- [ ] `prefers-reduced-motion` respected; no animation above 3 flashes/second

## 6 · Measurement

- [ ] DGA Assessment Criteria checklist completed
- [ ] Digital Transformation Measurement Indicator reviewed
- [ ] Digital Experience Maturity Indicator reviewed

> ⚠️ §6 is **incomplete in this kit** — the two indicators are published outside
> design.dga.gov.sa and have not been harvested. Do not treat §6 as sufficient coverage.

## 7 · DGA Assessment Criteria — the four Mandatory criteria

DGA: failing these *"typically cannot proceed to deployment"*. Keep the hedge when reporting.

Full rubric and the Recommended set: `assessment-criteria.md`.

- [ ] **Design System Compliance** — Platforms Code correctly implemented
- [ ] **Typography and Color Standards** — approved text and functional colours
      (⚠️ `text.secondary` #dba102 is 2.30:1 — use `secondary-gold.800` or darker for gold text)
- [ ] **Layout and Spacing** — wireframe dimensions, **mobile-first**, spacing grid
- [ ] **Mobile Usability** — touch interactions, viewport sizing, navigation on small screens

Timing, not a tickbox:

- [ ] Assessment submitted **at least two weeks** before the desired review date
- [ ] Evidence pack prepared per criterion — references, screenshots, code snippets
- [ ] Checklist reviewed by **someone other than its author** before submission
