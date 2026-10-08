---
name: pa-workflow-ip-office-action-response-drafter-sboghossian
title: IP — Office Action Response Drafter
description: Use when a patent attorney needs to draft a response to a patent office action — addressing examiner rejections, making claim amendments, and advancing distinguishing arguments over cited prior art. Covers non-final rejections, final rejections, requirement for restriction, and obviousness/novelty arguments. A qualified patent attorney must review and file all responses. Triggers on a received office action document.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/pa-workflow/pa-workflow-ip-office-action-response-drafter
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: ip
language: en
---

# IP — Office Action Response Drafter

An office action response is among the most consequential documents in patent prosecution: it determines the scope of what is ultimately granted. A poorly argued response narrows claims unnecessarily; an overly aggressive response may create file-wrapper estoppel that limits enforcement later. This skill assists patent attorneys in preparing first-draft responses — the attorney's strategic judgment and final review are mandatory.

**Critical disclaimer:** All office action responses must be reviewed, revised as necessary, and filed by a qualified patent attorney or patent agent authorised to practice before the relevant patent office. Deadlines are statutory — failure to file on time results in abandonment.

## Purpose

From a received office action and the application file, produce a first-draft response that:
1. Identifies and addresses each rejection or objection
2. Drafts claim amendments to overcome formal rejections
3. Prepares arguments distinguishing the claimed invention from cited prior art
4. Identifies whether affidavit or declaration support is needed
5. Advises on prosecution strategy (interview, continuation, RCE, appeal)

## Inputs

| Input | Why it matters |
|---|---|
| Office action document | The examiner's rejections and objections — the document being responded to |
| Application as filed | Current claims, specification, and drawings |
| Prior art cited by examiner | The references being distinguished |
| Prosecution history | What has been argued before — avoid inconsistency, avoid new estoppel |
| Attorney's strategy notes | Broad? Narrow? Accelerate? Interview first? |
| Deadline | The statutory or extended deadline for the response |

## Response structure

### 1. Remarks header

```
IN THE UNITED STATES PATENT AND TRADEMARK OFFICE

Application No.:    [18/XXXXXX]
Filed:              [Date]
Title:              [Invention Title]
Examiner:           [Name]
Art Unit:           [XXXX]
Docket No.:         [Internal docket number]

RESPONSE TO OFFICE ACTION DATED [DATE]
```

### 2. Amendments to the claims (if needed)

Present all claim amendments in the standard claim amendment format for the applicable patent office:

**USPTO format:**
- Amended claims: new text in underline, deleted text in strikethrough
- Clean copy of all claims must follow (or use USPTO Online system)

**EPO format:**
- Claims filed as complete replacement set (no tracked changes)
- Indicate basis in the application for each added feature (required by EPC Art. 123(2))

**Key principle:** only amend claims when necessary to overcome a rejection. Unnecessary amendments narrow scope without benefit and may create prosecution history estoppel that limits the patent's coverage in litigation.

### 3. Remarks section — structure

The remarks section is the attorney's argument to the examiner. Structure per rejection:

```
## Response to Rejection Under [Section/Rule]

### A. [Name of rejection, e.g., "35 USC § 102(a)(1) — Anticipation by Reference A"]

Summary of examiner's rejection:
[One paragraph restating what the examiner said — confirms you have understood it]

Applicant's response:
[Argument — see below]

### B. [Next rejection]
...

## Conclusion
[Brief statement that all rejections have been addressed; request for allowance]
```

## Rejection types and argument patterns

### Novelty rejection (anticipation)

**35 USC § 102 / EPC Art. 54**

Examiner says: a single prior art reference discloses every element of the claimed invention.

**Argument structure:**
1. Identify which claim element the reference allegedly discloses
2. Quote the exact passage from the reference cited by the examiner
3. Show that the reference does not actually teach the claimed element — typically by pointing to a specific definitional or functional difference
4. If necessary, amend the claim to add a feature that is not in the reference (taking care not to narrow unnecessarily)

**Common winning argument:** the reference discloses a functionally different embodiment, or uses a term that sounds similar but has a different technical meaning in the relevant field.

### Obviousness rejection

**35 USC § 103 / EPC Art. 56**

Examiner says: combining two or more references would have been obvious to a person skilled in the art.

**Argument structure (using KSR International Co. v. Teleflex analysis for US):**
1. The combination does not teach all elements of the claim, or
2. There was no motivation to combine the references as proposed, or
3. The combination as proposed would not have worked as the examiner suggests, or
4. The claimed invention achieves an unexpected result over the combination

**Technical declaration:** if the obviousness rejection is strong, consider whether a declaration from the inventor or an expert (35 USC § 132 declaration) attesting to unexpected results would overcome the rejection.

### Enablement / written description

**35 USC § 112(a) / EPC Art. 83, 84**

**Argument:** the specification does provide sufficient disclosure, pointing to specific pages, figures, and paragraphs. If the rejection is about claim breadth, consider whether a narrowing amendment is warranted.

### Restriction requirement (USPTO only)

**37 CFR § 1.142**

Examiner says: the application claims multiple inventions — elect one.

**Strategy:** elect the group with the broadest commercial value for the initial prosecution. File divisional applications for the non-elected groups before the application issues (non-elected inventions can still be pursued as divisionals).

## Affidavit and declaration support

If the argument alone is insufficient, affidavit support may be needed:

- **37 CFR § 1.132 Declaration**: inventor or third party attests to unexpected results, commercial success, long-felt need, or failure of others — secondary considerations that can overcome an obviousness rejection
- **37 CFR § 1.131 Declaration**: swearing behind a prior art reference by establishing an earlier invention date (pre-AIA; limited application under AIA)
- **EPO Rule 132 declaration**: similar function under EPC

## Prosecution strategy advice

After preparing the response draft, flag the strategy choice for the attorney:

| Option | When to consider |
|---|---|
| File response without amendment | Rejection is clearly wrong; strong non-anticipation argument |
| File with narrow amendments | Rejection has some merit; amendments preserve core scope |
| Request examiner interview | Complex obviousness rejection; in-person discussion more efficient |
| File RCE (Request for Continued Examination) | After final rejection; allows continuation of prosecution |
| File Appeal | Examiner has issued a final rejection and the law supports the original claims |
| Continuation application | Capture additional scope not in current claims; file before issue |
| Abandon | Claims cannot be meaningfully salvaged or the technology is no longer commercially relevant |

## Jurisdiction-specific notes

| Office | Key differences |
|---|---|
| USPTO | 3-month statutory deadline (extendable to 6 months with fees); interview practice common; RCE available after final rejection |
| EPO | Oral proceedings (not interviews) may be requested; appeal to Technical Board of Appeal; no RCE equivalent — response to examination report has strict claim support requirements |
| WIPO (PCT) | Written Opinion at ISA/IPEA stage; responses influence national phase examinations |
| GCC Patent Office | Examination based on USPTO/EPO examination results; national phase filings in Arabic |
| UAE (MOEI) | Examination follows EPO-style practice; Arabic responses |

## Related skills

- [[pa-workflow-ip-claim-drafting-from-disclosure]]
- [[pa-workflow-ip-opposition-procedure-epo]]
- [[pa-workflow-ip-docketing-system-mcp-bridge]]
- [[output-inline-citations-with-pinpoints]]
