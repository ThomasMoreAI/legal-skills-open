---
name: pa-workflow-ip-claim-drafting-from-disclosure-sboghossian
title: IP — Claim Drafting from Inventor Disclosure
description: Use when a patent attorney or IP team needs to draft patent claims from an inventor disclosure document. Produces independent claims, dependent claims, and method/system/apparatus variants from a technical disclosure, with a claim chart mapping to prior art. A qualified patent attorney must review all output before filing. Triggers on inventor disclosure documents and patent claim drafting requests.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/pa-workflow/pa-workflow-ip-claim-drafting-from-disclosure
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: ip
language: en
---

# IP — Claim Drafting from Inventor Disclosure

Patent claims are the legal boundaries of an invention — they define exactly what is protected and what is not. Well-drafted claims are broad enough to provide meaningful protection but narrow enough to be novel and inventive over the prior art. AI-assisted claim drafting from a disclosure document accelerates the attorney's drafting process significantly; the attorney's judgment and final review remain essential.

**Critical disclaimer:** All output from this skill must be reviewed and approved by a qualified patent attorney or patent agent licensed in the relevant jurisdiction before any filing. Claude cannot replace the legal judgment required for claim scope decisions, prior art clearance, or prosecution strategy.

## Purpose

From an inventor disclosure document, produce a first-draft claim set consisting of:
1. One or more independent claims (defining the broadest protectable scope)
2. Dependent claims adding specific features and fallback positions
3. Method, system, and apparatus variants where applicable
4. A claim chart identifying the novel elements against identified prior art

## Inputs

| Input | Why it matters |
|---|---|
| Inventor disclosure document | The technical description of the invention — the factual basis for the claims |
| Prior art search results | What exists in the field — shapes claim scope |
| Prosecution history of related patents | What has been argued before in this area |
| Target jurisdictions | US, EP, PCT, GCC — different claim drafting standards apply |
| Filing deadline | Urgency of the draft |
| Business priority | Which aspects of the invention are commercially most important to protect |

## Claim hierarchy

### Independent claims — the broadest scope

An independent claim must be:
- **Novel**: not anticipated by any single prior art reference
- **Inventive**: not obvious to a person skilled in the art from the prior art
- **Enabled**: supported by the specification
- **Definite**: clear and precisely bounded

Independent claims define the outer boundary of protection. Draft the broadest claims that the disclosure supports and that appear to be novel over the prior art. Do not narrow the independent claim unnecessarily — dependent claims add specificity.

Structure: `[Preamble] comprising / consisting of / including [claim elements].`

Example (illustrative — not a real invention):
> **Claim 1.** A computer-implemented method for automated contract analysis comprising: receiving a contract document in digital form; identifying one or more clauses within the document using a trained natural language processing model; classifying each identified clause by risk category based on a pre-defined risk taxonomy; and generating a risk report associating each classified clause with its risk category.

### Dependent claims — the fallback positions

Each dependent claim adds a specific feature to an independent (or earlier dependent) claim. Dependent claims serve two functions:
1. Narrowing fallback positions if the independent claim is invalidated
2. Adding specific preferred embodiments that may have commercial importance

Example (continuing the above):
> **Claim 2.** The method of claim 1, wherein the trained natural language processing model is fine-tuned on a corpus of legal contracts from at least one MENA jurisdiction.
> **Claim 3.** The method of claim 1, further comprising translating the contract document from Arabic to English prior to the identifying step.
> **Claim 4.** The method of any preceding claim, wherein the risk taxonomy comprises at least five risk categories including limitation of liability, governing law, IP ownership, termination, and indemnification.

### Method, system, and apparatus variants

For software and technical inventions, draft three parallel claim types:
- **Method claim**: the steps of the process
- **System claim**: the hardware/software components configured to perform the method
- **Computer-readable medium claim**: a non-transitory storage medium with instructions for the method

These three claim types provide protection across different potential infringers (those making the device vs those using the method).

## Claim chart

A claim chart maps each element of the independent claim(s) against:
1. The inventor disclosure (support for the claim)
2. Key prior art references (to show novelty/distinguishability)

| Claim element | Disclosure support | Prior Art Ref 1 | Prior Art Ref 2 | Distinguishing feature |
|---|---|---|---|---|
| Receiving a contract document | Disclosure § 3.1 | Taught | Taught | Not a distinguishing element |
| Classifying by risk category using NLP | Disclosure § 4.2–4.5 | Not taught | Similar but different taxonomy | Novel taxonomy + MENA training corpus |
| Generating risk report per clause | Disclosure § 5.1 | Not taught | Partial — per document, not per clause | Clause-level granularity is novel |

## Target jurisdiction considerations

| Jurisdiction | Claim drafting notes |
|---|---|
| US (USPTO) | First-to-file system; method, system, and CRM claims standard; means-plus-function claims permissible but narrow; claim language must be definite (35 USC § 112) |
| EP (EPO) | Technical character required; claims must specify technical features; no software claims "as such" — frame as a "computer-implemented method" or "computer program product" |
| PCT (international) | Follows the lead jurisdiction's standard initially; unity of invention important |
| GCC / ARIPO | Most GCC states (UAE, KSA, etc.) follow civil-law influenced patent systems; PCT designation typically used for GCC coverage; local filing requirements vary |
| UAE | UAE Federal Law on Industrial Property — patents valid for 20 years; software patents possible if framed as technical implementation |

## Quality bar

- Do not draft claims beyond what the disclosure supports — overreaching claims will be rejected and may compromise prosecution
- Do not fabricate prior art references — the claim chart must use actual, identified prior art
- Flag where disclosure is ambiguous: "The disclosure does not clearly describe [element] — attorney should clarify with the inventor before finalising this claim"
- The dependent claims should cover the commercially most valuable embodiments — ask the attorney or inventor to identify these

## Limits and human review

This skill produces a first-draft starting point. The patent attorney must:
- Review claim scope against the full prior art landscape
- Make prosecution strategy decisions (continuation, divisional, accelerated examination)
- Verify claim language against the specific formal requirements of the target patent office
- Sign and file the application

## Related skills

- [[pa-workflow-ip-office-action-response-drafter]]
- [[pa-workflow-ip-docketing-system-mcp-bridge]]
- [[pa-workflow-ip-opposition-procedure-epo]]
