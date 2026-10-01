# Legal-readiness manifest schema

## Contents

- [Top-level contract](#top-level-contract)
- [Evidence](#evidence)
- [Claims](#claims)
- [Controls and risks](#controls-and-risks)
- [Lifecycle](#lifecycle)
- [Surfaces](#surfaces)

The JSON manifest is an evidence-routing contract. Passing validation means the
record is structurally complete enough for review; it is not a legal opinion.

## Top-level contract

| Field | Required meaning |
|---|---|
| `schema_version` | Integer `1`. |
| `project` | `name`; optional `repository` and `base_url`. |
| `project.template` | Starts `true`; validation also rejects the initialization marker and bundled placeholder values, so changing this flag alone cannot pass. |
| `scope.operator` | `verified` only with registry or counsel evidence; otherwise `unverified`. |
| `scope.jurisdictions` | Name, status, factual basis, evidence, and next gate when unresolved. |
| `scope.channels` | Web, native iOS, native Android, API, marketplace, etc. |
| `scope.customer_types` | Consumer, business, enterprise, developer, public sector, etc. |
| `scope.data_roles` | Controller, processor, service provider, recipient-controller, unknown, etc. |
| `scope.sales_territories` | Supported, excluded, or unresolved markets. |
| `sources` | Current official/counsel source ledger. |
| `coverage` | Complete required claim-surface and issue-area ledger, each audited, not audited, or inapplicable. |
| `claims` | Complete claim universe with verdicts. |
| `controls` | Implemented, partial, open, blocked, or not-applicable controls. |
| `residual_risks` | At least one bounded risk with status, owner, and required closure evidence; use a real uncertainty rather than inventing one. |
| `launch_disposition` | Structured `blocked`, `limited`, `not-assessed`, or `ready-for-counsel-review`; open P0 risks force blocked/limited. |
| `lifecycle` | Current state plus immutable receipts. |
| `completion_statement` | Exact checker-defined boundary derived from `launch_disposition.status`; free-form closure prose is refused. |
| `legal_boundary` | Explicit issue-spotting/not-legal-advice boundary. |
| `surfaces` | Optional mechanical web probes. |

The bundled coverage IDs are a required cross-product floor, not a closed
taxonomy. Add sector-specific rows with IDs such as
`sector:health-medical-device` or `custom:employment` and a non-empty
`description`; the required baseline rows must remain present.

## Evidence

Every evidence row has an accountable verifier, non-future timestamp, and
SHA-256 digest:

```json
{
  "kind": "repo",
  "locator": "app/api/checkout/route.ts:44",
  "observed_at": "2026-08-09T18:00:00-05:00",
  "verified_by": "named reviewer or accountable role",
  "sha256": "<64 lowercase hexadecimal characters>"
}
```

Allowed kinds: `repo`, `live`, `test`, `law`, `regulator`, `registry`,
`contract`, `counsel`, `dashboard`, `policy`, `invoice`, `other`.

All kinds require a non-future timezone-aware `observed_at` no more than 370
days old. Re-observe and re-hash an older artifact rather than changing its
original date; `observed_at` is the review time, not the artifact's creation
date. A digest binds the recorded artifact; it does not prove that the verifier,
locator, or contents are authentic.
Use stable locators: exact file and line/commit, official URL, contract
ID/version, registry receipt, dashboard
export, test artifact, deployment URL, or PR/merge identifier. Never put a
secret, raw personal data, legal advice, or privileged communication in the
manifest. Store only authorized sanitized conclusions, private record IDs,
digests, dates, and verifier identity. A digest binds an assertion; it does not
authenticate its contents by itself.

Source rows distinguish `authority_type` (legislation, regulation, court,
regulator guidance, standard, counsel, contract, other), `binding_status`, and
`provision_or_scope`; they also retain retrieval time and a content digest.
Each source names the accountable verifier who checked the instrument metadata
and links to manifest `jurisdiction_ids`. A claim may use a source only when the
source and claim share a declared jurisdiction nexus.
Counsel evidence likewise carries explicit `jurisdiction_ids`; a source or
counsel record may support only the jurisdictions it names. Multi-jurisdiction
legal claims and inapplicability decisions require coverage for every linked
jurisdiction, not merely one overlapping jurisdiction.
Source retrieval must likewise be rechecked within 370 days so a historical
instrument cannot silently stand in for a current-law review.
Supported/qualified/inapplicable legal-obligation verdicts need binding primary
law/court material or counsel evidence, plus an explicit jurisdiction ID.

## Claims

Each claim records:

- stable `id`;
- exact `claim` and its `surface`;
- `type`: `factual`, `legal-obligation`, `commercial`, `security-control`, or
  `recommendation`;
- verdict: `supported`, `qualified`, `contradicted`, `unverified`,
  `not-audited`, or `not-applicable`;
- factual `applicability` predicate;
- `source_ids` for relevant official sources;
- evidence, owner, and next gate.

Supported/qualified claims need evidence. Supported/qualified legal-obligation
claims also need a primary-source reference or law/regulator/counsel evidence.
Contradicted claims need contrary evidence. Unverified/not-audited claims need a
next gate. Every unresolved claim links a residual risk. `not-applicable` is an
evidenced conclusion, never the cheap default.
`qualified` is explicitly unresolved: it requires the exact `qualification`, a
typed `qualification_type`, a structured `gate` (`action`, `target`, `owner`),
a human-readable `next_gate`, and at least one linked non-closed residual risk.

Do not use the claim ledger to launder a conclusion. A row saying “fully
compliant” remains unsupported even if it cites the checker.

## Controls and risks

Control statuses are `implemented`, `partial`, `open`, `blocked-external`, and
`not-applicable`. `implemented` requires evidence. Every unresolved control
requires an owner and next gate. Every `not-applicable` claim, control, or
coverage row declares `basis_kind` as `factual-absence` or
`legal-determination`, links jurisdictions and sources, and supplies evidence
appropriate to that basis. An unrelated repository artifact cannot establish a
legal inapplicability decision.

Residual risks use severity `p0` through `p3`, status `open`, `accepted`, or
`closed`, a concrete risk statement, a named owner, and exact closure evidence.
P0 cannot be accepted. An unverified operator requires an open P0 operator risk
so the unknown cannot disappear in prose or a free-text completion statement.

The completion statement is deliberately fixed:

```text
Overall legal compliance is not claimed. Launch disposition: <status>. See the claim, coverage, control, residual-risk, and lifecycle records.
```

Put detail in the structured rows and the human report. This prevents a
free-text sentence from contradicting the launch and risk records.

The launch rationale is also checker-defined. `limited` is not a prose escape:
each constraint is an object with an ID, restriction, owner, open-P0 `risk_ids`,
implemented `control_ids`, and enforcement evidence. Every open P0 must be
covered by such a constraint, and every referenced implemented control must
link that same risk. `effect` is one of `disabled-feature`,
`geofenced-territory`, `blocked-processing`, `read-only-mode`,
`restricted-customer-type`, or `restricted-channel`; the
`enforcement_predicate` states the machine-observable restriction. Otherwise
use `blocked`.
The constraint also records structured `target`, `action`, and `enforced_value`;
its `enforcement_predicate` must exactly match the referenced implemented
control, as must the full structured tuple. Disable/deny effects require a false
value; read-only requires `"read-only"`; geofence/restrict effects require a
non-empty bounded value. Constraints may also cover linked open P1-P3 risks,
while every open P0 still must be covered to use `limited`.

## Lifecycle

Lifecycle is monotonic only when the receipts exist:

| State | Required receipt kinds |
|---|---|
| `worktree` | none |
| `committed` | `commit` |
| `pr-open` | `commit`, `pull-request` |
| `merged` | above + `merge` |
| `deployed` | above + `deployment` |
| `live-verified` | above + `live-probe` |

Each receipt requires a recognized `kind`, kind-appropriate locator, common
`release_id`, issuer, non-future `observed_at`, and SHA-256 digest. Required
receipts are unique and ordered from commit through live probe. A CI smoke job that
ran before the deployment is not evidence of that deployment. A live route
receipt proves only what it observed.

## Surfaces

Each surface has an absolute route, expected status, expected header fragments,
optional content type, and optional `allow_redirects`. Redirects fail by default
so a legal surface that silently lands on login cannot pass as public:

```json
{
  "path": "/.well-known/security.txt",
  "expect_status": 200,
  "expect_content_type": "text/plain",
  "expect_headers": {"Content-Type": "text/plain"}
}
```

The probe validates the manifest before I/O, refuses non-global addresses by
default, pins the connection to the exact addresses that passed the safety
check, verifies the connected peer, constrains routes and redirects to the configured origin, and does not
overwrite a receipt without `--force`. Use `--allow-private-network` only for a
trusted local-development manifest. The receipt binds manifest and expectation
digests but does not parse legal prose or determine sufficiency.
