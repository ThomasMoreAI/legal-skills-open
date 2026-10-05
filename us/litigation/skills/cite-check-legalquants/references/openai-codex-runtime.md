# Codex runner contract for `/cite-check`

The packaged runner is the normal cite-check path. Its purpose is simple: every prepared paragraph, footnote, table cell, heading, and other text unit gets one fresh model session.

The Python orchestration script starts one local `codex exec` process per unit. It does not batch several paragraphs into one model request. A host without that local runtime keeps the same one-unit assignments with its native workers or processes them one at a time.

## Execution order

Use this order without changing the legal method or result contract:

1. Packaged runner: one fresh `codex exec` session per prepared unit.
2. Native host workers with the same one-unit assignments when the packaged runner is unavailable.
3. One-at-a-time processing of the same units when workers are unavailable.

Run `scripts/probe_environment.py` before starting the packaged runner. The probe uses synthetic local data only; it does not read the target or authorities and makes no model call. A failed capability check means the host should use the one-unit fallback, not that the cite-check itself failed. The probe checks local file/process operations and the required CLI flags; plugin names, logo assets, provider manifests, and install paths do not determine eligibility. The same runner can execute from an installed package or a source checkout when those capabilities are present.

The probe is a diagnostic preflight, not authentication or permission approval. It cannot establish that a later model request will succeed. The runner still uses ephemeral, read-only workers, validates source/output boundaries, and reports actual startup, authentication, and outer-host permission failures. Keep the probe receipt for diagnostics; never change a failed capability to pass merely to launch workers.

## Per-unit contract

Every prepared unit receives the same review prompt, rubric, supplied-authority inventory, bounded document context, and strict output schema. Each session is fresh, ephemeral, and read-only. It returns exactly one terminal result for its assigned unit, including an explicit `no_citations_found` result when appropriate.

When an identifiable case was not supplied, the session searches an available public source using citation metadata only. It reports one of three outcomes: the environment could not search; the search did not find the case and it may be hallucinated; or the case was found but was not supplied for substantive checking.

The model makes the legal judgment. Deterministic code only checks the required fields and evidence links, then maps the result to the report colors. Missing or invalid evidence is amber; this check prevents it from appearing green but does not decide whether a proposition fairly states the law.

Give one targeted retry when evidence is mechanically incomplete: a missing excerpt, missing locator, invalid or out-of-authority source ID, malformed row, or inconsistent source-match fields. Do not retry substantive legal disagreement. Preserve both attempts. If the second attempt remains incomplete, keep the citation amber and continue.

## Run and report boundaries

Keep generated prompts, attempts, receipts, and reports inside a dedicated run directory. Do not modify the target or authority files. Preserve an explicit incomplete state when a unit never returns a valid terminal result.

Technical receipts may record the execution path, runtime observations, failures, and usage. Keep those details out of the lawyer-facing report. The report should focus on citation findings, source evidence, unresolved issues, and this one-sentence scope note: “Checks citations against the sources supplied for this run; it does not check later case history or replace full legal research.”
