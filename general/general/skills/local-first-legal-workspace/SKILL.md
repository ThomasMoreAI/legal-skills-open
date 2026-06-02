---
name: local-first-legal-workspace
title: local-first-legal-workspace
description: Use when users say "is this legal AI app local-first", "what leaves the machine", "BYOK privacy", "audit network calls", "where are documents stored", or need a legal AI workspace reviewed for local storage, credentials, model-provider calls, conversion, and privacy boundaries.
author: LegalQuants
author_url: https://github.com/LegalQuants/lq-skills/tree/main/skills/local-first-legal-workspace
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: en
tags: [local-first, privacy, legal-ai, document-management, byok, security]
---

# local-first-legal-workspace

## When to Use

- A lawyer wants to use AI with confidential documents without adopting a hosted matter platform.
- A desktop or local web app stores legal documents and generated work product.
- The user needs to reason about BYOK model calls, local storage, workspace backups, or privacy boundaries.
- A workflow must explain exactly what leaves the machine.

This skill is a design and audit checklist. It is not a claim that local-first equals risk-free.

## Audience and Work Shape

Audience: legal-technology counsel, privacy/security-aware lawyers, and legal engineers reviewing a legal AI workspace with technical input where needed.

Work shape: pattern-matched audit when evidence exists; accretive design review when the user is designing a workflow. Keep those paths separate in the output.

## Legal Failure Modes

- Legal support, not legal advice: the skill maps data flows and uncertainty so a lawyer can assess risk; it does not certify privacy, security, privilege, or regulatory compliance.
- Privilege/confidentiality: model calls, document conversion, logs, and external lookups can affect privilege/work-product treatment. Include privilege/work-product implications in the disclosure note when legal matter data is involved.
- Accountability: the responsible lawyer, DPO, security lead, or system owner decides whether the workspace is acceptable for a matter or client.

## Access Modes

This skill works in three modes:

1. **Code/runtime evidence mode** - inspect repository code, configuration, dependencies, logs, network observations, or runtime behavior.
2. **User-supplied architecture mode** - use diagrams, README files, screenshots, settings exports, or descriptions supplied by the user.
3. **No-evidence mode** - produce an audit plan and questions only. Do not assert what stays local or what leaves the machine.

If code, runtime evidence, or provider documentation is unavailable, mark claims `unknown` or `not_observed_not_excluded`. Do not treat a product's privacy statement as verified architecture.

## How It Works

### 1. Define the workspace boundary

Identify where local data lives:

- Documents.
- Database or index.
- Generated files.
- Chat history.
- Settings.
- Logs.
- API keys or credential references.

Prefer one user-chosen workspace folder so backup, deletion, and migration are understandable.

### 2. Map all network paths

List every possible external call:

- Model providers.
- Citation or registry lookups.
- OCR or document conversion services.
- Telemetry, analytics, crash reporting, fonts, CDNs, update checks.

For each call, record:

| Field | Meaning |
|---|---|
| destination | host or service |
| trigger | what user action causes it |
| payload | what data is sent |
| credential | whose key or token is used |
| retention | known retention posture |
| opt-out | whether user can disable it |
| evidence | code path, config file, package, provider documentation, policy URL, or runtime observation supporting the row |
| retrieval_date | date external provider terms or documentation were checked |

Do not assert that there are no hidden network paths unless code, dependency, configuration, and runtime evidence has been checked. If a path is not observed but not exhaustively verified, mark `not_observed_not_excluded`; if unknown, mark `unknown`.

### 3. Confirm user control

Check:

- Workspace can be selected by the user.
- User can back up by copying the workspace.
- User can delete local state.
- API keys are BYOK or clearly scoped.
- Sensitive file paths are guarded against traversal.
- Generated exports are written where the user expects.

### 4. Prepare a disclosure note

For legal users, produce a short note:

- What stays local.
- What is sent out.
- What is optional.
- What logs exist.
- What the tool cannot guarantee.

Plain English matters. A lawyer should be able to explain the risk to a client, judge, supervisor, or DPO.

Output as:

1. `local_state_map` table: data type, path/location, sensitivity, deletion method, backup implication.
2. `external_calls` table using the fields above.
3. `credential_handling` summary.
4. `user_disclosure_note` in plain English.
5. `unknowns_and_verification_needed`.

Add an overall confidence band to `user_disclosure_note`:

- High: code, config, runtime, and provider evidence reviewed; material unknowns are closed.
- Medium: architecture or documentation reviewed but runtime or provider evidence is incomplete.
- Low: no-evidence or user-reported-only mode; output is an audit plan, not a conclusion.

## Confidence Bands

Apply the same High/Medium/Low band to the overall disclosure note and separately preserve row-level evidence states (`observed`, `user_reported`, `provider_documentation`, `unknown`, `not_observed_not_excluded`).

### 5. Review failure modes

Flag:

- Cloud auth or storage reintroduced by dependency.
- Remote document conversion.
- Model prompts containing entire confidential bundles when only excerpts are needed.
- API keys stored in plaintext files.
- Unbounded logs containing document text.
- Local app exposing services beyond localhost.

## Escalation

Stop and route to privacy counsel, a security engineer, or the system owner when plaintext credentials are found, marketing/privacy claims contradict code or runtime evidence, unexpected outbound destinations appear, provider retention terms are missing for client data, or the user wants a client-facing assurance without runtime evidence.

## Example

```text
Audit this legal AI app's privacy boundary. Tell me what stays local, what leaves the machine, and what the user must understand before processing confidential documents.
```

For a compact output pattern, see `examples/output.md`.
For workspace boundary, BYOK, network inventory, and conversion-risk conventions, see `references/local-first-model.md`.

## Limitations

- Local-first does not mean local-model-only.
- BYOK model providers may still retain or process submitted context under their terms.
- Malware, endpoint compromise, backups, and user sharing are outside the skill's control.
- This is not a formal security audit.
