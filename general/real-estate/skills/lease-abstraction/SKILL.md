---
name: lease-abstraction
title: Commercial Lease Abstraction
description: Extract a structured abstract from a commercial lease PDF — tenant/landlord identification, premises description + RSF/USF, lease term + commencement/expiration, renewal options (count, notice windows, fair-market rent reset), base rent schedule + escalations (fixed %, CPI-linked, step-up, percentage rent breakpoints), operating expense structure (NNN, modified gross, full service, base year, expense stops, gross-ups), CAM provisions + caps + audit rights, tenant improvement allowance, security deposit (cash/LOC/burn-down), use restrictions, co-tenancy + exclusivity, assignment/sublet rights, recapture, termination/default provisions, kick-outs, options to expand/contract, holdover, insurance/indemnification, estoppel + SNDA. Outputs a standardized abstract JSON + CSV + Markdown summary + critical-dates calendar (rent escalation alerts at 60/30 days, option exercise windows, expiration alerts). 80-90% reduction in processing time per industry benchmarks. TRIGGER on "lease abstract",
  "lease abstraction", "CRE lease", "commercial lease summary", "lease key terms", "rent roll setup", "lease review", "tenant rep prep", "Argus import", "lease database", "lease admin".
author: tinh2
author_url: https://github.com/tinh2/skills-hub-registry/tree/main/analysis/lease-abstraction
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: real-estate
language: en
---

# Commercial Lease Abstraction

You convert a lease PDF (and amendments) into a structured abstract. Manual lease abstraction takes 4-12 hours per document depending on complexity; AI-assisted reduces that to 20-40 minutes of human review on top of a generated draft. The standardization matters as much as the speed — every abstracted lease should fit the same schema so a portfolio can be queried.

============================================================
=== PRE-FLIGHT ===
============================================================

- [ ] **Lease document(s)**: original lease PDF + ALL amendments + side letters + work letters. Missing amendments = wrong financial picture.
- [ ] **Lease type**: office, retail, industrial, ground lease, residential (CA Civil Code §1947 differs), medical office, mixed-use. Drives which clauses to expect.
- [ ] **Output schema target**: VTS, Visual Lease, MRI, Yardi, ProLease, Excel template, or generic JSON. Each system has slightly different field names.
- [ ] **Reporting purpose**: lease admin (operational), tenant rep (negotiation prep), landlord acquisition DD, ASC 842/IFRS 16 accounting capture.

Recovery:

- Missing amendments: refuse to publish a final abstract; output draft + flag "amendments missing — DO NOT rely on for accounting."
- For complex retail leases (% rent + CAM gross-ups + exclusivity webs), surface complexity to a human reviewer; the abstract is a draft.

============================================================
=== PHASE 1: DOCUMENT INTAKE + OCR ===
============================================================

PDF preprocessing:

- If image-only PDF, OCR via `pytesseract` or AWS Textract (better for table extraction).
- Split lease into named sections (definitions, basic terms, rent, additional rent, options, default, indemnity).
- Extract embedded tables (rent schedule, CAM exhibit) as structured data, not flowed text.

Persist `lease.text.json` with section anchors so the abstract can cite source page+section per extracted field.

VALIDATION: Page count > 0, no all-white pages, text extraction confidence per section ≥ 80%.

============================================================
=== PHASE 2: STANDARDIZED FIELD EXTRACTION ===
============================================================

Extract into this schema (camelCase JSON):

```json
{
  "parties": {"tenant": "...", "landlord": "...", "guarantor": "...", "broker": "..."},
  "premises": {"address": "...", "suite": "...", "rsf": 12500, "usf": 11700, "load_factor": 0.068},
  "term": {
    "commencement_date": "2024-04-01",
    "expiration_date": "2034-03-31",
    "term_months": 120,
    "rent_commencement_date": "2024-06-01",
    "free_rent_months": 2
  },
  "rent_schedule": [
    {"period": "Year 1", "start": "2024-04-01", "end": "2025-03-31", "monthly_rent_psf": 4.50, "monthly_rent_total": 56250.00, "annual_rent_total": 675000},
    ...
  ],
  "escalations": {"type": "fixed_pct", "pct": 0.03, "annual_review_date": "anniversary"},
  "options": [
    {"type": "renewal", "count": 2, "term_months": 60, "notice_window_months": 12, "rent_basis": "FMR", "rent_floor_pct": null}
  ],
  "additional_rent": {
    "expense_structure": "modified_gross",
    "base_year": 2024,
    "expense_stop_psf": null,
    "tenant_share_pct": 0.085,
    "cap": {"type": "cumulative_5pct_year_over_year", "applies_to": "controllable_only"},
    "gross_up_provision": true,
    "audit_rights": {"window_months": 12, "self_help": false}
  },
  "ti_allowance": {"amount_psf": 75.00, "total": 937500, "unused_treatment": "rent_credit"},
  "security_deposit": {"type": "letter_of_credit", "amount": 250000, "burn_down": [{"month": 36, "to": 125000}, {"month": 60, "to": 0}]},
  "use_restriction": "general office and ancillary uses; no medical, retail, or industrial",
  "co_tenancy": null,
  "exclusivity": null,
  "assignment_sublet": {"consent_standard": "not_unreasonably_withheld", "permitted_transfers": ["affiliates", "merger_consolidation"]},
  "termination_rights": {"tenant_kick_out_year": 7, "notice_months": 12, "termination_fee": "9 months base rent + unamortized TI/commissions"},
  "expansion_rights": {"type": "ROFO", "size_sf": null, "notice": "60 days"},
  "holdover": {"rate_pct_of_holdover": 1.50, "consent_required": false},
  "insurance": {"tenant_liability_minimum": 3000000, "additional_insureds": ["landlord", "property_manager"]},
  "default": {"monetary_cure_days": 5, "non_monetary_cure_days": 30, "late_fee_pct": 0.05, "interest_rate": "prime + 4%"},
  "estoppel_sndaa": {"estoppel_required": true, "snda_attached": true},
  "amendments_incorporated": ["Amendment 1 (2024-09-15)", "Amendment 2 (2025-03-01)"]
}
```

Every field has a `source` sub-field with `{page, section, confidence}`.

VALIDATION: Schema fields present (null OK if absent in lease — don't fabricate). Rent schedule sum reconciles to total committed rent over term.

============================================================
=== PHASE 3: AMBIGUITY & FLAG DETECTION ===
============================================================

Some lease clauses are inherently ambiguous; flag for human review:

- **Gross-up provision boundaries**: which expenses can be grossed up to 95%/100% occupancy? Listed expressly or implicit?
- **CAM cap**: cumulative vs annual? Applies to all expenses or controllable only? Taxes/insurance excluded?
- **Tenant share**: pro rata by RSF or fixed percentage? Adjustable on changes to building size?
- **Renewal rent basis**: FMR with floor? Pre-negotiated rate? Greater of (X, Y)?
- **Assignment consent**: "consent not unreasonably withheld" vs absolute discretion vs deemed-consent if no response in N days.
- **Termination fee**: includes unamortized TI? Brokerage commissions? Free rent? At what discount rate?

Flag each as `{field, ambiguity, suggested_interpretation, reviewer_action}`.

VALIDATION: At least 1 flag per lease (if zero, the abstraction is too confident and worth a second pass).

============================================================
=== PHASE 4: CRITICAL DATES CALENDAR ===
============================================================

Emit a calendar file (`critical_dates.ics` + `critical_dates.csv`) with reminders:

- Rent escalation date (60-day and 30-day pre-alerts)
- Renewal option exercise window opening + closing (1 year and 6 month pre-alerts)
- Lease expiration (24 / 12 / 6 / 3 month pre-alerts)
- Termination right exercise window (if applicable)
- Expansion/ROFO/ROFR triggers
- Security deposit burn-down dates
- CAM audit window (typically 12 months after year-end statement)
- Estoppel/SNDA delivery deadlines

VALIDATION: Calendar imports into Google/Outlook/iCal without errors.

============================================================
=== PHASE 5: ABSTRACT OUTPUTS ===
============================================================

Final deliverable directory:

```
lease-{tenant-slug}-{address-slug}/
├── README.md                # what each file is and where it goes
├── abstract.json            # full schema (Phase 2)
├── abstract.csv             # flat row for portfolio rollup
├── abstract.md              # human-readable summary
├── critical_dates.ics
├── critical_dates.csv
├── flags.md                 # ambiguities (Phase 3)
├── source_lease.pdf         # original (link, not copy)
└── audit_trail.json         # extraction confidence per field
```

The Markdown summary is a one-pager: parties, premises, term, rent, escalations, options, key flags. Designed for handoff to a broker / attorney / portfolio manager.

VALIDATION: All files render. CSV imports into Excel without column drift.

============================================================
=== SELF-REVIEW ===
============================================================

Score 1–5:

- **Complete**: All schema fields populated or explicitly null?
- **Robust**: Amendments incorporated? Rent reconciliation passes?
- **Clean**: Markdown summary fits one page? Critical dates calendar correct?
- **CRE-credible**: Would a lease admin or tenant-rep broker accept the abstract as a working draft?

Common gap: forgetting to incorporate amendments. The "original" lease's rent schedule is often superseded by an amendment.

============================================================
=== LEARNINGS CAPTURE ===
============================================================

Append to `~/.claude/skills/lease-abstraction/LEARNINGS.md`:

## <YYYY-MM-DD> — <asset type, lease length, complexity>

- **What worked / awkward / patch / verdict.**

============================================================
=== STRICT RULES ===
============================================================

- Never publish a final abstract without incorporating all amendments.
- Never fabricate a field. Null is acceptable; invented values are a tort.
- Never auto-import to Argus / VTS without reviewer sign-off. Wrong rent schedule = wrong valuation = lawsuit.
- Always preserve source citations per field for auditability.
- Always run the critical-dates calendar — missing a renewal notice can lose a tenant a premises.
