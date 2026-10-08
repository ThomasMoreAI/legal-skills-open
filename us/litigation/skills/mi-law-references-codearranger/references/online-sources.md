# Michigan Law — Canonical Online Sources

> **NOT LEGAL ADVICE.** Source directory only. Verify currency at the
> source before relying on any rule, statute, or form.

Canonical human-facing URLs for Michigan primary law and court
resources. For programmatic / API access see `legal-data-apis.md`.

---

## Court rules and evidence rules (MCR / MRE)

- **Michigan Courts — One Court of Justice**:
  https://www.courts.michigan.gov
- **Michigan Court Rules and Rules of Evidence** (current text, with
  staff comments and recent amendments): published under the Supreme
  Court / SCAO sections of courts.michigan.gov. The MCR and MRE are
  amended by Supreme Court administrative order; check the
  **"Proposed & Recently Adopted Court Rules / Administrative Orders"**
  pages for pending and effective amendments.
- **Michigan Rules of Evidence — 2024 restyling**: confirm the
  restyled text effective January 1, 2024 against the current posting.

---

## Statutes — Michigan Compiled Laws (MCL)

- **Michigan Legislature**: https://www.legislature.mi.gov
- **MCL section lookup** uses an **objectName** scheme. The pattern is
  `mcl-<chapter>-<section>` with hyphens replacing the dot — for
  example, MCL 600.5701 is `mcl-600-5701`:
  - `https://www.legislature.mi.gov/Laws/MCL?objectName=mcl-600-5701`
  - The renderable/printable document endpoint:
    `https://www.legislature.mi.gov/Home/Document?objectName=mcl-600-5701`
- The legislature site also hosts the **Michigan Court Rules** and
  **public acts**; the authoritative current MCL text is here.

---

## Forms

- **SCAO (State Court Administrative Office) approved forms**: the
  statewide fillable court forms (civil, family, landlord-tenant, small
  claims, fee-waiver MC 20, etc.) are published on courts.michigan.gov
  under the **"Forms"** / SCAO forms index. SCAO-approved forms are
  required for many filings — use the current revision.

---

## E-filing — MiFILE

- **MiFILE** is Michigan's statewide e-filing system (Tyler
  Technologies / Odyssey File & Serve), rolling out and mandatory in a
  growing set of courts: https://mifile.courts.michigan.gov
- Confirm whether e-filing is **mandatory** in the specific court and
  case type before filing; some courts and case types still accept or
  require paper.

---

## Local rules / Local Administrative Orders (LAOs)

- Individual courts' venue-specific procedures are set by **Local
  Administrative Orders** approved by SCAO and indexed on
  courts.michigan.gov. Check the LAO index for the filing court
  (motion-day scheduling, chambers copies, praecipe practice).

---

## Opinions

- **Michigan appellate opinions** (Supreme Court and Court of Appeals,
  published and unpublished) are posted on courts.michigan.gov under the
  opinions / case-search sections, and mirrored on **CourtListener**
  (see `legal-data-apis.md`).

---

## Cross-references

- `legal-data-apis.md` — programmatic access to the same sources
- `citation-format.md` — how to cite what you pull from these sources
- `court-rules/` and `mi-statutes-debt/` — the locally stored verbatim corpora
