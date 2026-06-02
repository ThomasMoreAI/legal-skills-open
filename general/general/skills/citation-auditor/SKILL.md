---
name: citation-auditor
title: Invocation Contexts
description: Audit a markdown file by chunking it, extracting claims with structured output, routing each claim to verifier skills, aggregating verdicts, and rendering annotated markdown.
author: kipeum86
author_url: https://github.com/kipeum86/game-legal-research/tree/main/.claude/skills/citation-auditor
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: en
---

Audit the markdown file at `$0`.

## Invocation Contexts

This skill is invoked in two distinct contexts:

- **Standalone `/audit` (default)**: user-triggered via the `/audit <file.md>` slash command on any existing markdown file. Uses **inline mode** — per-claim badges injected into the body plus a per-claim audit report at the end. Does not alter `output/checkpoint.json`.
- **Workflow Step 10 (automatic)**: invoked by the main orchestrator after Step 9 for Mode B/C/D or memo/opinion deliverables (see `CLAUDE.md` §5 Step 10). Uses **append mode** — body preserved with only `[Unverified]` / `[Partially Unverified]` tags on failing claims, plus a `## 부록: 검증 로그 (Citation Audit Log)` appendix table at the end. The rendered output is audited draft content that the orchestrator passes to the final save path.

The only procedural difference between the two contexts is the `--mode` flag passed to `render` in step 15 below. Steps 1–14 are identical.

## Procedure

1. Confirm `$0` exists and is a markdown file. If it does not, stop and ask for a valid path.
2. Run:
   `python3 -m citation_auditor chunk "$0" --max-tokens 3000`
3. Parse stdout as JSON with the schema `{ "chunks": [...] }`.
4. Run deterministic extraction first:
   `python3 -m citation_auditor extract "$0" --max-tokens 3000`
5. For each chunk, use the deterministic extraction output as the minimum claim set. If a chunk has sparse deterministic output, optionally add non-citation factual claims using structured output with this schema:
   - `text: string`
   - `sentence_span: { start: integer, end: integer }`
   - `claim_type: factual | citation | quantitative | temporal | other`
   - `suggested_verifier: string | null`
6. Do not extract speculation, forecasts, rumors, advocacy, or soft prediction language such as:
   - `전망이다`
   - `예상된다`
   - `업계 관계자에 따르면`
   - `가능성이 있다`
   Unless the sentence also contains a concrete verifiable factual assertion that stands on its own.
7. Keep claim offsets chunk-relative. Do not convert them to document offsets yourself.
8. Deduplicate deterministic and model-supplemented claims before routing.
9. Route each claim to verifier skills:
   - If `suggested_verifier` is set and exactly matches a loaded verifier skill name, use it.
   - Otherwise test the claim text against each specialized verifier skill frontmatter `patterns` using case-insensitive regex matching and use every match.
   - Set `verifier_name == "general-web"` only when specialized matches count is zero and no valid `suggested_verifier` exists.
   - Do not run `general-web` as a parallel verifier for a claim that already matched `korean-law`, `eu-law`, `us-law`, `uk-law`, `scholarly`, or `wikipedia`.
10. For each `(claim, verifier)` pair, use the Task tool to dispatch a subagent that loads that verifier skill and receives the claim JSON.
11. Require each verifier subagent to return only this JSON:
   `{ "label": "...", "rationale": "...", "supporting_urls": ["..."], "authority": 0.0 }`
12. `supporting_urls` may contain either clickable source URLs or plain-language source references when no stable URL exists. Preserve them verbatim and do not invent clickable URLs for non-linkable sources such as precedent search-result IDs.
13. Build aggregate input JSON locally. The exact top-level shape is `{ "verdicts": [ <bundle>, ... ] }` where each `<bundle>` covers one `(chunk, claim)` pair and holds all verifier candidates for that claim. Do not invent other top-level keys.

    **Exact schema (copy this structure):**
    ```json
    {
      "verdicts": [
        {
          "chunk": { "index": 0, "text": "<full chunk text>", "segments": [ { "chunk_start": 0, "chunk_end": 44, "document_start": 0, "document_end": 44 } ] },
          "claim": { "text": "<claim sentence>", "sentence_span": { "start": 64, "end": 268 }, "claim_type": "citation", "suggested_verifier": "us-law" },
          "candidates": [
            {
              "claim": { "text": "<same claim as above>", "sentence_span": { "start": 64, "end": 268 }, "claim_type": "citation", "suggested_verifier": "us-law" },
              "verifier_name": "us-law",
              "authority": 0.9,
              "label": "contradicted",
              "rationale": "<Korean rationale from verifier>",
              "evidence": [ { "url": "https://..." } ]
            }
          ]
        }
      ]
    }
    ```

    Rules:
    - One bundle per `(chunk, claim)` pair. If the same claim has two verifiers, put both candidates inside the same bundle's `candidates` array — do NOT create a second bundle for the same claim.
    - The top-level `claim` inside each bundle is the canonical claim; each candidate's `claim` must match it verbatim.
    - `evidence` items require a non-empty `url` string. If the verifier returned `supporting_urls: []`, emit `"evidence": []` — do not emit `[{"url": ""}]`.
    - `label` must be one of `verified` / `contradicted` / `unknown`.
    - `authority` must match the verifier skill's declared authority value.

14. Write that JSON to a temp file and run:
    `python3 -m citation_auditor aggregate <tmpfile>`
15. Write the aggregate output to a temp file and run:
    - Standalone `/audit`: `python3 -m citation_auditor render "$0" <aggfile>` (inline mode is default).
    - Workflow Step 10: `python3 -m citation_auditor render "$0" <aggfile> --mode=append`.
16. Return only the final annotated markdown unless the user explicitly asked for intermediate JSON. In the Step 10 context, the orchestrator treats this as audited draft content and then performs the final save according to the requested output format.
17. If model-supplemented claim extraction validation fails, retry once with a repair prompt. If it still fails, use deterministic extraction only and note it briefly.
18. If a verifier subagent returns invalid JSON, drop that candidate instead of inventing a verdict.
19. If a line was skipped because it is a forecast, opinion, rumor, or unattributed speculation, treat that as expected behavior rather than an extraction failure.
20. If the user asks why a forecast or opinion line was not audited, explain that this plugin audits verifiable factual claims and citations, not predictions or commentary.
