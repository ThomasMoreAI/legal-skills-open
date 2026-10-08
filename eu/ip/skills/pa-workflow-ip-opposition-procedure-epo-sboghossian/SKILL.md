---
name: pa-workflow-ip-opposition-procedure-epo-sboghossian
title: IP — EPO Opposition Procedure
description: Use when a patent attorney needs to draft an EPO opposition notice or response to an opposition against a European patent. Covers the grounds of opposition (novelty, inventive step, sufficiency of disclosure, extension beyond original application), prior art presentation, claim interpretation arguments, and the strict EPO time limits. A qualified European patent attorney must handle all filings. Triggers on EPO opposition proceedings.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/pa-workflow/pa-workflow-ip-opposition-procedure-epo
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: eu
practice: ip
language: en
---

# IP — EPO Opposition Procedure

EPO opposition is a cost-effective, centralised mechanism for challenging the validity of a European patent across all designated states. A successful opposition can revoke the patent entirely, or limit it to a narrower scope. It is also a formal adversarial proceeding before the EPO Opposition Division — procedural compliance is strict and late filings are typically inadmissible.

**Critical disclaimer:** EPO opposition proceedings involve hard statutory deadlines and formal procedural requirements. All filings must be handled by a qualified European patent attorney (EQE-qualified) or European patent agent. This skill produces working drafts to assist the attorney, not final filing documents.

## Purpose

Draft the key documents for an EPO opposition proceeding:
1. **Notice of Opposition**: the formal challenge filing (9-month deadline from grant)
2. **Written Submissions**: arguments in support of grounds of opposition
3. **Response to Opposition** (for patent owner): counterarguments defending the patent
4. **Auxiliary Requests**: claim sets for the patent owner to maintain patent in amended form

## The 9-month deadline — the most critical rule

Under EPC Rule 76, an opposition must be filed within **9 months of the date of grant** of the European patent (the B1 publication date). This is an absolute deadline — no extensions are available. Missing it permanently forecloses centralized EPO opposition (though national invalidity proceedings may still be available in individual EPC contracting states).

**Docket this date the moment the opponent decides to challenge.** See [[pa-workflow-ip-docketing-system-mcp-bridge]].

## Grounds of opposition (EPC Art. 100)

An opposition may be based on only three formal grounds:

| Ground | Legal basis | What must be shown |
|---|---|---|
| Lack of novelty or inventive step | EPC Art. 100(a) + Art. 54 / Art. 56 | The claimed invention is anticipated by, or obvious over, the prior art |
| Insufficiency of disclosure | EPC Art. 100(b) + Art. 83 | The patent does not disclose the invention clearly and completely enough for a skilled person to carry it out |
| Extension beyond original disclosure | EPC Art. 100(c) + Art. 123(2) | The claims or specification were amended after filing to include subject matter not present in the application as originally filed |

All three grounds may be raised cumulatively. Each must be substantiated — a bare assertion without supporting evidence is inadmissible.

## Notice of opposition — structure

```
TO: European Patent Office — Opposition Division

EUROPEAN PATENT:  EP [Number] B1
PATENTEE:         [Name]
TITLE:            [Title]
FILING DATE:      [Date of filing]
GRANT DATE:       [Date of B1 publication]
OPPOSITION FILED BY: [Opponent name and address]
PROFESSIONAL REPRESENTATIVE: [EQE-qualified attorney details]
FILING DATE OF OPPOSITION: [Today's date — must be within 9 months]

NOTICE OF OPPOSITION

The opponent hereby opposes the above-mentioned European patent in its entirety [or: claims X, Y, Z] on the following grounds:

1. GROUND 1: LACK OF INVENTIVE STEP (EPC Art. 100(a) + Art. 56)
   [see Section II below]

2. GROUND 2: LACK OF NOVELTY (EPC Art. 100(a) + Art. 54)
   [see Section III below]

STATEMENT OF GROUNDS AND EVIDENCE

I. PRIOR ART
[List all prior art references, with exhibit numbers]
  D1: [Full citation] (Exhibit D1)
  D2: [Full citation] (Exhibit D2)
  ...

II. GROUND 1 — INVENTIVE STEP
...

III. GROUND 2 — NOVELTY
...

CONCLUSION
[Request to revoke the patent in its entirety / in part]

EXHIBITS
[List of all exhibits filed with the Notice]
```

## Substantiating grounds

### Novelty (Art. 54)

Apply the "gold standard" anticipation test: a single prior art document must disclose, directly and unambiguously, every feature of the claim.

Structure:
1. Identify the prior art reference (D1, D2, etc.)
2. Provide a feature-by-feature claim chart showing where each claim element is disclosed in the reference
3. For any element not explicitly taught, argue implicit disclosure
4. If any element is genuinely missing, concede novelty for that claim and pursue inventive step instead

### Inventive Step (Art. 56) — Problem-Solution Approach

The EPO requires the Problem-Solution Approach (PSA), not the US-style "teaching, suggestion, motivation" test:

1. **Identify the closest prior art** (the reference most similar to the claimed invention)
2. **Determine the objective technical problem**: what technical problem does the invention actually solve compared to the closest prior art? (May differ from the problem stated in the specification)
3. **Assess whether the skilled person would have arrived at the solution**: could they have combined the closest prior art with a secondary reference or common general knowledge to solve the objective problem, with a reasonable expectation of success?

**Filing tip for opponents:** the closest prior art is not necessarily the reference with the most features in common — it is the starting point a skilled person would actually choose. Choose strategically.

### Sufficiency of Disclosure (Art. 83)

The patent must enable a skilled person to carry out the invention across the full scope of the claims. Challenge sufficiency when:
- The claim covers a broad genus but the specification only enables a narrow species
- The examples in the specification do not reproduce the claimed results
- The patent relies on parameters that are not defined precisely enough to be measured reproducibly

### Extension beyond original disclosure (Art. 123(2))

If the claims or description were amended after the original filing date (or the priority date if priority is claimed), any added matter not directly and unambiguously disclosed in the original application is impermissible.

Check: does each feature in the current claims have clear support in the originally filed specification (not just the published application, which may have been amended)?

## Response to opposition — for patent owner

The patent owner's Response (under EPC Rule 79) must be filed within **4 months** of the communication of the Notice of Opposition. The response should:

1. Challenge each ground of opposition on the merits
2. File **Auxiliary Requests** (amended claim sets) as fallback positions
3. Request oral proceedings if the opposition cannot be resolved on the written record

### Auxiliary requests strategy

File multiple sets of increasingly narrow claims as auxiliary requests:
- **Main Request**: the granted claims, defended as-is
- **Auxiliary Request 1**: minor narrowing amendment to overcome the most specific attack
- **Auxiliary Request 2**: further narrowing, eliminating the weakest claims
- **Auxiliary Request 3+**: core of the invention in its narrowest commercially essential form

The order matters: the Opposition Division will consider the main request first; only if it fails does it consider AR1, then AR2, etc.

## Oral proceedings

Either party may request oral proceedings (Art. 116 EPC). The Opposition Division may also summon the parties to oral proceedings of its own motion. In practice, most contested oppositions go to oral proceedings.

Key preparation:
- File a pre-oral proceedings submission summarising your best arguments
- Prepare claim amendments to be tabled at oral proceedings if main request fails
- Attend with the EQE-qualified representative

## Time limits summary

| Step | Deadline |
|---|---|
| File Notice of Opposition | 9 months from grant (B1) |
| Opponent's substantiation (if not included) | May be filed within 9-month period |
| Patent owner's response | 4 months from communication of opposition |
| Further submissions | Set by Opposition Division communication |
| Summons to oral proceedings | Typically 2+ months' notice |
| Pre-oral proceedings submissions | Normally 4 weeks before oral proceedings |
| Appeal (if opposition decision unsatisfactory) | 2 months from decision (EPC Art. 108) |

## Related skills

- [[pa-workflow-ip-office-action-response-drafter]]
- [[pa-workflow-ip-claim-drafting-from-disclosure]]
- [[pa-workflow-ip-docketing-system-mcp-bridge]]
- [[output-timeline-builder]]
