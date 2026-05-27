---
name: icd-cpt-normalization
title: ICD-10 / CPT Code Normalization
description: Normalizes diagnostic and procedure codes from medical records into clean, attorney-readable form. Cross-walks ICD-9 to ICD-10-CM, expands ICD-10 codes to narrative descriptions, expands CPT codes to procedure descriptions, and flags bundling or unbundling oddities relevant to billing disputes. Use this skill any time medical codes appear in records being summarized for litigation use, including medical chronologies, demand letters, and billing review. Also use when the user asks what a specific medical code means.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/icd-cpt-normalization
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: personal-injury
language: en
tags: [litigation, analysis, research]
---

# ICD-10 / CPT Code Normalization

Medical records are full of codes that mean nothing to attorneys without translation. This skill normalizes ICD-10-CM diagnosis codes, ICD-9 codes (in older records), and CPT procedure codes into a form the attorney can actually use.

## When to use

Whenever a code appears in records being summarized:

- Diagnosis codes in encounter notes
- Procedure codes in operative reports and billing records
- Code lists in IME reports
- HCFA-1500 forms or itemized bills

## Lookup tool

Use the configured ICD-10 / CPT lookup tool available in the environment. The tool name varies by deployment; check the available tools list for one that handles medical code lookup.

If no lookup tool is available, fall back to the inline reference below for common codes. For uncommon codes without a lookup tool, mark the code with `[code description not verified]` and surface in the methodology section.

## ICD-10-CM normalization

### Format

ICD-10-CM codes are alphanumeric, 3 to 7 characters, often with a decimal point after the third character: `M54.5`, `S83.241A`. Records sometimes drop the decimal (`M545`) or add spaces (`M 54.5`); normalize to the standard format with the decimal.

### Expansion

For each code that appears, render it as:

```
[Code] - [Full narrative description from ICD-10-CM]
```

Example:

```
S83.241A - Other tear of medial meniscus, current injury, right knee, initial encounter
```

The seventh character (A, D, S, etc.) carries meaning and must be preserved:

- A: Initial encounter
- D: Subsequent encounter
- S: Sequela

A treating provider coding `S83.241A` (initial) on visit 1 and `S83.241D` (subsequent) on visit 5 is using the codes correctly. A provider still coding `A` after twelve visits may have a sloppy billing practice; flag for the attorney if this is a billing-relevant case.

### Laterality

ICD-10 distinguishes left, right, and unspecified. Records sometimes code "unspecified" when laterality was actually documented in the narrative. Cross-check:

```
Encounter narrative: "Right knee pain, status post MVA"
Code billed: M25.50 (Pain in unspecified joint)
```

This is a coding inaccuracy. Surface in Strategic Analysis if billing is at issue. The accurate code would be M25.561 (Pain in right knee).

## ICD-9 to ICD-10 cross-walk

ICD-9 was retired October 1, 2015. Records before that date use ICD-9; records after generally use ICD-10. Some legacy systems and some Workers Comp jurisdictions still emit ICD-9.

When ICD-9 codes appear:

1. Render the original ICD-9 code with its description
2. Cross-walk to the most specific ICD-10 equivalent using the General Equivalence Mappings (GEMs)
3. Note the cross-walk explicitly

Example:

```
847.2 (Sprain of lumbar) [ICD-9, encounter dated 2014-08-15]
Cross-walk: S33.5XXA - Sprain of ligaments of lumbar spine, initial encounter
```

GEMs are not always one-to-one. When the cross-walk is ambiguous, surface the alternatives:

```
787.91 (Diarrhea) [ICD-9]
Cross-walk: R19.7 (Diarrhea, unspecified) most likely; if context indicates
infection, A09 (Infectious gastroenteritis and colitis, unspecified)
```

## CPT normalization

### Format

CPT codes are 5-digit numeric codes (`99213`, `97110`, `64483`). Category II codes append `F` (`0001F`). Category III codes append `T` (`0042T`). Records occasionally use HCPCS Level II codes which start with a letter (`G0463`, `J0696`); these come from a different code set but appear alongside CPT in billing records and should be expanded the same way.

### Expansion

Render each code as:

```
[Code] - [Procedure description]
```

Example:

```
27447 - Arthroplasty, knee, condyle and plateau; medial AND lateral compartments
        with or without patella resurfacing (total knee arthroplasty)
99204 - Office or other outpatient visit for the evaluation and management of a
        new patient, requires a comprehensive history, comprehensive examination,
        and medical decision making of moderate complexity
```

### Modifiers

CPT modifiers are two-character suffixes that change the meaning of the procedure code. Common modifiers:

- 25: Significant, separately identifiable E/M service on the same day as a procedure
- 50: Bilateral procedure
- 51: Multiple procedures
- 59: Distinct procedural service (often controversial in billing disputes)
- LT/RT: Left side / right side
- XE, XS, XP, XU: More specific replacements for modifier 59 (X-modifiers)

Modifiers must be expanded just like the base code:

```
64483-LT - Injection, anesthetic agent and/or steroid, transforaminal
            epidural; lumbar or sacral, single level (left side)
```

### Bundling and unbundling

In billing-relevant cases (med mal damages, fee disputes, lien negotiations), flag:

- **Modifier 59 or X-modifier overuse**: applied to procedures that should bundle
- **NCCI edits**: pairs of codes that should not be billed together per the National Correct Coding Initiative
- **E/M codes billed alongside procedure codes** without modifier 25 documentation

These are surfaced in Strategic Analysis, not the chronology itself. The chronology states what was done; the analysis interprets whether the billing was clean.

## Output format in chronologies

In a medical chronology encounter entry, codes appear in the Diagnoses and Treatment subsections:

```
Diagnoses:
- S83.241A - Other tear of medial meniscus, current injury, right knee, initial encounter [SMITH00147]
- M17.11 - Unilateral primary osteoarthritis, right knee [SMITH00147]

Treatment:
- 99204 - New patient evaluation, comprehensive [SMITH00147]
- 73721 - MRI any joint of lower extremity, without contrast (referred) [SMITH00147]
```

If a code is in the records but you cannot verify its description (lookup tool unavailable, code is non-standard), render as:

```
- 99204 [code description not verified] [SMITH00147]
```

Surface in methodology that some codes were not verified.

## Inline reference: high-frequency codes in PI / Med Mal

These appear repeatedly in personal injury and medical malpractice records. Use as a fallback if the lookup tool is unavailable. This is not a substitute for proper lookup on production cases.

### ICD-10 - Spine

- M54.5 - Low back pain (deprecated 2021; replaced by M54.50, M54.51, M54.59)
- M54.50 - Low back pain, unspecified
- M54.51 - Vertebrogenic low back pain
- M54.59 - Other low back pain
- M54.2 - Cervicalgia
- M54.6 - Pain in thoracic spine
- M51.26 - Other intervertebral disc displacement, lumbar region
- M50.20 - Other cervical disc displacement, unspecified cervical region
- S13.4XXA - Sprain of ligaments of cervical spine, initial encounter
- S33.5XXA - Sprain of ligaments of lumbar spine, initial encounter

### ICD-10 - Extremities

- S83.241A - Other tear of medial meniscus, current injury, right knee, initial encounter
- S83.242A - Other tear of medial meniscus, current injury, left knee, initial encounter
- S43.401A - Unspecified sprain of right shoulder joint, initial encounter
- M25.561 - Pain in right knee
- M25.562 - Pain in left knee
- M75.101 - Unspecified rotator cuff tear or rupture of right shoulder, not specified as traumatic

### ICD-10 - Head / TBI

- S06.0X0A - Concussion without loss of consciousness, initial encounter
- S06.0X1A - Concussion with loss of consciousness of 30 minutes or less, initial encounter
- F07.81 - Postconcussional syndrome
- G44.301 - Post-traumatic headache, unspecified, intractable
- G44.309 - Post-traumatic headache, unspecified, not intractable

### CPT - Evaluation and Management

- 99202-99205 - New patient office visits (level 2 through 5)
- 99211-99215 - Established patient office visits (level 1 through 5)
- 99221-99223 - Initial hospital care
- 99281-99285 - Emergency department visits

### CPT - PT / Rehab

- 97110 - Therapeutic exercise (15 min)
- 97112 - Neuromuscular reeducation (15 min)
- 97140 - Manual therapy (15 min)
- 97530 - Therapeutic activities (15 min)
- 97161-97163 - PT evaluation, low / moderate / high complexity

### CPT - Imaging

- 73030 - X-ray shoulder, complete (min 2 views)
- 73721 - MRI lower extremity joint without contrast
- 72148 - MRI lumbar spine without contrast
- 72141 - MRI cervical spine without contrast
- 70450 - CT head/brain without contrast
- 70551 - MRI brain without contrast

### CPT - Pain procedures

- 64483 - Transforaminal epidural injection, lumbar/sacral, single level
- 64493 - Facet joint injection, lumbar/sacral, single level
- 20610 - Major joint injection (knee, shoulder, hip)
- 20550 - Tendon sheath / ligament injection

### CPT - Surgery (orthopedic, common)

- 29881 - Knee arthroscopy with meniscectomy (medial OR lateral)
- 29888 - Knee arthroscopy, anterior cruciate ligament repair/augmentation/reconstruction
- 27447 - Total knee arthroplasty
- 23410 - Repair of ruptured musculotendinous cuff (rotator cuff repair)
- 63030 - Lumbar laminotomy with discectomy, single interspace
- 22612 - Arthrodesis, posterior or posterolateral technique, single level lumbar

This list is incomplete by design. Use the lookup tool for anything not on it.

## Troubleshooting

- **Lookup tool unavailable**: Use the inline high-frequency reference only for listed codes; otherwise mark `[code description not verified]`.
- **ICD-9 crosswalk is ambiguous**: Preserve the original ICD-9 code, list plausible ICD-10 alternatives, and explain what clinical context would resolve the mapping.
- **Modifier meaning conflicts with documentation**: Expand the modifier, cite the documented procedure details, and flag the conflict for attorney or billing-expert review.
- **Narrative diagnosis and billed code disagree**: Report both with citations and surface the mismatch in Strategic Analysis when billing or causation is at issue.
