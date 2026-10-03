# Markdown Output Template

Use this structure when producing a chronology in markdown for case.dev or other markdown-native rendering. The structure mirrors the docx template; only the rendering differs.

## Reference table of contents

- [Header block](#header-block)
- [Section 1: Case Information](#section-1-case-information)
- [Section 2: Provider Index](#section-2-provider-index)
- [Section 3: Pre-Incident Medical History](#section-3-pre-incident-medical-history)
- [Section 4: Chronological Summary](#section-4-chronological-summary)
- [Section 5: Diagnostic Studies Summary](#section-5-diagnostic-studies-summary)
- [Section 6: Medication History](#section-6-medication-history)
- [Section 7: Damages Summary](#section-7-damages-summary)
- [Section 8: Strategic Analysis](#section-8-strategic-analysis)
- [Section 9: Methodology and Limitations](#section-9-methodology-and-limitations)

## Header block

```
# Medical Record Chronology - [Patient Last Name]

**Patient:** [Full name]
**DOB:** [Date]
**Date of incident:** [Date]
**Case type:** [PI / Med Mal / Workers Comp / Disability]
**Records reviewed:** [Bates range, e.g., SMITH000001 - SMITH002847]
**Citation scheme:** Bates-stamped pages [or "PDF page references" if Bates unavailable]
**Prepared:** [Date]
```

## Section 1: Case Information

```
## Case Information

| Field | Value |
|-------|-------|
| Patient name | [Name] |
| DOB | [Date] |
| Date of incident | [Date] |
| Case type | [Type] |
| Pre-existing conditions | [Brief list, or "See Section 3"] |
| Claimed injuries | [Brief list] |
| Records reviewed | [Bates range] |
```

## Section 2: Provider Index

```
## Provider Index

| # | Provider / Facility | Type | Date Range | Records Status | Bates Range |
|---|--------------------|------|-----------|----------------|-------------|
| 1 | [Name] | [ER/PCP/Specialist/PT/Imaging/IME] | [First - Last] | Complete / Partial / Referenced only | [Range] |
```

If a provider is referenced in another provider's records but no records were produced, include them in the index marked "Referenced only" and note in the Bates Range column where the reference appears.

## Section 3: Pre-Incident Medical History

Chronological summary of relevant treatment before the incident. Use the same encounter format as Section 4 but only for pre-incident encounters relevant to claimed injuries or body parts.

If no pre-incident records were produced, state explicitly:

```
## Pre-Incident Medical History

No pre-incident records were produced. Defense counsel may argue this constitutes
incomplete production. Recommend requesting [primary care], [specialist],
[health insurance claims history] for the [N]-year period preceding the incident.
```

## Section 4: Chronological Summary

Each encounter follows this format:

```
### [YYYY-MM-DD] - [Provider Name] - [Facility] - [Visit Type]

**Chief complaint:** [Patient statement] [Bates]

**History:** [Mechanism, onset, prior treatment as documented] [Bates]

**Examination:** [Objective findings] [Bates]

**Diagnostic studies:** [Imaging, labs, results] [Bates]

**Diagnoses:**
- [ICD-10 code] [Narrative description] [Bates]
- [ICD-10 code] [Narrative description] [Bates]

**Treatment:**
- [CPT code] [Procedure description] [Bates]
- [Medication] [Dosage] [Bates]
- [Referral] [Bates]

**Restrictions:** [Work or activity limits] [Bates]

**Follow-up:** [Plan] [Bates]

**Causation language:** "[Direct quote from provider]" [Bates]
```

Omit subsections that do not apply to a given encounter rather than leaving them empty. The "Causation language" subsection should be included only when the provider made a causation statement; if absent, omit.

Encounters must appear in strict date order across all providers. Do not group by provider in this section.

## Section 5: Diagnostic Studies Summary

```
## Diagnostic Studies

| Date | Study | Body Part | Facility | Findings | Significance | Bates |
|------|-------|-----------|----------|----------|--------------|-------|
| [Date] | MRI | C-spine | [Facility] | [Brief] | [Why it matters] | [Bates] |
```

The "Significance" column is for the attorney's strategic value, not a clinical opinion. Examples: "Documents structural injury post-incident," "Pre-incident imaging showing baseline degenerative changes," "Negative finding undercuts plaintiff's claim of [X]."

## Section 6: Medication History

```
## Medication History

| Medication | Prescribed By | Start Date | End Date | Purpose | Bates |
|-----------|--------------|-----------|---------|---------|-------|
```

If a medication was discontinued, note discontinuation date and any documented reason. If escalated (dose increase, stronger medication in the same class), flag with a note.

## Section 7: Damages Summary

```
## Damages Summary

**Medical expenses by provider:**
- [Provider]: $[amount] [Bates]
- [Provider]: $[amount] [Bates]
- **Total billed:** $[amount]
- **Total paid (if available):** $[amount]

**Lost time from work:** [Date ranges and documentation source] [Bates]

**Functional limitations documented:** [Brief, with citations]

**MMI status:** [Reached on date / Not yet reached / Not addressed in records] [Bates]

**Future treatment recommended:** [List with citations]
```

If billing records were not produced, state so explicitly.

## Section 8: Strategic Analysis

```
## Strategic Analysis

### Favorable findings
- [Finding] [Bates]
- [Finding] [Bates]

### Adverse findings
- [Finding] [Bates]
- [Finding] [Bates]

### Gaps in records
- [Gap and recommended request]
- [Gap and recommended request]

### Inconsistencies
- [Description of inconsistency, with citations to both conflicting sources]

### Follow-up recommended
- [Action item]
- [Action item]
```

Both favorable and adverse findings must be present. A one-sided analysis section is a red flag.

## Section 9: Methodology and Limitations

```
## Methodology and Limitations

**Records reviewed:** [Description of corpus, Bates range]
**Citation scheme:** [Bates / PDF page / mixed]
**Verification scope:** [N] total citations; [N] independently page-verified via
PDF OCR/text-layer extraction; [N] vault-search-only; [N] spot-checked; [N]
flagged [UNVERIFIED]; [N] corrected or removed.
**Canonical Bates format:** [Prefix, spacing, digit count, range].
**Verification log:** [Path/name of auditable log, or "included below"].
Do not state that verification was completed unless the methods and counts above
are populated. Claims marked [UNVERIFIED] appear in the records but the
supporting page was not independently retrievable at the time of preparation.
Claims marked [CITATION UNAVAILABLE] were produced without source access.
**Limitations:** [Records not produced, ranges not received, etc.]
```

This section is short but mandatory. It is the chronology's chain of custody.
