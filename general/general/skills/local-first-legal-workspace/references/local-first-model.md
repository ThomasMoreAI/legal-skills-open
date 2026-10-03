# Local-First Legal Workspace Model

Use this reference when auditing or designing a local-first legal AI workspace.

## Core Principle

Local-first means the user's workspace is the primary system of record. It does not mean no network traffic, no cloud model calls, or no legal/privacy risk.

## Workspace Boundary

Map where these live:

- documents,
- generated files,
- local database or JSON indexes,
- chat history,
- extracted text,
- conversion outputs,
- logs,
- settings,
- credentials or credential references,
- runtime metadata.

Prefer one user-chosen workspace folder so backup, migration, deletion, and client disclosure are understandable.

## Local Auth and Runtime

Check whether the app uses:

- local password or OS credential storage,
- local API on loopback,
- dynamic local port,
- local database,
- local filesystem storage,
- signed local URLs,
- path traversal protections,
- symlink/junction handling,
- workspace-inside-install-directory guard.

Do not describe these as present unless evidenced by code, config, runtime capture, or user-supplied documentation.

## BYOK Reality

Bring-your-own-key does not mean local-only. It usually means:

- user's key is used,
- selected prompts/documents/excerpts are sent to the model provider,
- provider terms govern retention/confidentiality,
- enterprise settings may change privacy posture.

State exactly what is known and unknown.

## Network Inventory

For each possible external call, record:

- destination host,
- trigger,
- payload,
- credential,
- retention evidence,
- opt-out,
- source of evidence,
- retrieval date.

Classify unknowns:

- `observed`
- `not_observed_not_excluded`
- `unknown`
- `user_reported`
- `provider_documentation`

## Document Conversion

Identify conversion routes:

- browser extraction,
- local server conversion,
- bundled office converter,
- external conversion service,
- OCR,
- scanned PDF no OCR.

Conversion can leak data if remote. It can also create local artifacts that need deletion/backups.

## Privacy Disclosure Note

A useful disclosure note says:

- what stays in the workspace,
- what leaves the machine,
- who receives it,
- what action triggers it,
- whether the user can disable it,
- what was not verified.

Avoid absolute claims like "nothing leaves your computer" unless runtime and code evidence supports them.

## Output Contract

Use:

```yaml
local_state_map: []
external_calls: []
credential_handling: {}
document_conversion: []
unknowns_and_verification_needed: []
user_disclosure_note: string
```
