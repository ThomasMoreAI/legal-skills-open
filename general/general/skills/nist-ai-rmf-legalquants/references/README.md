# References — routing index

Read this file first. It tells you which reference files to load for which kind of question, so you don't burn context on files that don't apply.

## What's here

Two layers of NIST source material:

- **`core/`** — NIST AI 100-1 (AI Risk Management Framework 1.0, January 2023). The general framework. Applies to any AI system. Uses Subcategory IDs like `GOVERN 1.1`, `MAP 2.3`.
- **`gai-profile/`** — NIST AI 600-1 (Generative AI Profile, July 2024). The GenAI-specific overlay. Adds Suggested Actions coded like `GV-1.2-001`, `MS-2.7-005` that map back to Core Subcategories. Use *in addition to* `core/` when the system is generative.

Plus two helpers:

- **`templates/`** — output templates for the three skill modes (`consult.md`, `governance-plan.md`, `assessment.md`). Load the one matching the current mode when drafting output; do not load all three.
- **`crosswalk.md`** — maps NIST risk names to common policy-taxonomy aliases (e.g., "Confabulation" ↔ "Hallucination"). Useful when bridging NIST language and a user's existing policy.

## Routing by question type

| Question | Load |
|---|---|
| "What does the AI RMF say I should do for this AI system?" | `core/functions.md`, then the relevant `core/<function>.md`. If generative, also the matching `gai-profile/actions-<function>.md`. |
| "What governance plan / policies should we have?" | `core/govern.md` + `core/trustworthy-characteristics.md`. If generative, also `gai-profile/actions-govern.md`. |
| "What testing / evaluation / measurement?" | `core/measure.md` + (if generative) `gai-profile/actions-measure.md`. |
| "What incident response / monitoring?" | `core/manage.md` + (if generative) `gai-profile/actions-manage.md`. |
| "What context / impact analysis up front?" | `core/map.md` + (if generative) `gai-profile/actions-map.md`. |
| "What risks does NIST identify?" (GenAI) | `gai-profile/risks.md` + `crosswalk.md`. |
| "What are the trustworthy AI characteristics?" | `core/trustworthy-characteristics.md`. |
| "Define [term]" | `core/glossary.md` first, then `gai-profile/glossary.md`. |
| "Is this system GenAI?" | Decide from the system description. If it generates text, images, audio, video, or other synthetic content using a foundation model or generative architecture, treat as GenAI. Otherwise, Core only. |
| Drafting consult output | `templates/consult.md` (only when about to emit a consult). |
| Drafting governance plan | `templates/governance-plan.md` (only when about to emit a plan). |
| Drafting full assessment | `templates/assessment.md` (only when about to emit an assessment). |

## Routing by document

Pick one of three modes before loading:

- **General AI system** (e.g., credit scoring on XGBoost, fraud detection on a classifier, demand forecasting): load `core/` only. Cite Subcategories like `MEASURE 2.11`. **Do not pull in GAI Profile actions** — they assume generative behavior and will not all apply.
- **Generative AI system** (e.g., LLM-powered chatbot, image generator, RAG application, text summarizer): load `core/` for the framework + `gai-profile/` for the GenAI overlay. Cite both Core Subcategories and Profile Action IDs.
- **Mixed / pipeline with both** (e.g., a pipeline that uses an LLM for one step and a classifier for another): treat the GenAI components per Profile, the rest per Core.

## How to cite from these references

When emitting output, cite verbatim:

- **Core Subcategory:** `**GOVERN 1.1** — Legal and regulatory requirements involving AI are understood, managed, and documented.` (NIST AI 100-1)
- **GAI Profile Action:** `\`GV-1.2-001\` — Establish transparency policies and processes for documenting the origin and history of training data and generated data for GAI applications…` (NIST AI 600-1)

Don't paraphrase the verbatim text — preserve the wording. The framework's authority comes from being a NIST publication; rewording strips that.

## When to consult `crosswalk.md`

If the user's organization already has a policy that names risks differently (e.g., calls "Confabulation" by "Hallucination," or splits "Harmful Bias and Homogenization" into "Discrimination" and "Fairness"), use `crosswalk.md` to translate NIST → their terms in the output. This keeps the user's existing policy language intact rather than forcing them to adopt NIST's exact vocabulary.

## Sources

The verbatim extracts in `core/` and `gai-profile/` are produced from NIST AI 100-1 (January 2023) and NIST AI 600-1 (July 2024). Re-extraction tooling and the frozen source HTMLs are maintained outside this distribution; see `CHANGELOG.md` for the snapshot version this build corresponds to.
