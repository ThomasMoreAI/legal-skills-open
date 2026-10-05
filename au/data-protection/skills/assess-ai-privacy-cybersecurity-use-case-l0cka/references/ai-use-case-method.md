# AI use-case assessment method

## Intake schema

Establish these facts before recommending deployment:

| Domain | Required facts |
| --- | --- |
| Purpose and benefit | Specific problem, intended benefit, evidence of need, lower-risk alternatives and measures of success |
| People and decision | Users, affected people, vulnerability, decision or action, consequence of error, human authority and contestability |
| System | Product, provider, model and version, hosting, integrations, tools or actions, update process and system boundaries |
| Data | Sources, categories, provenance, authority, identifiability, quality, prompts, retrieval, training use, outputs, logs, location, access, retention and deletion |
| Vendor and supply chain | Terms, privacy and security documentation, subprocessors, offshore handling, model improvement, incident notice, audit, change, suspension and exit rights |
| Controls and evidence | Testing, access controls, filtering, review, logging, monitoring, incident response, rollback, evaluation results and accountable owners |

An assertion that the provider is certified, compliant, enterprise-grade or
does not train on data is a claim to verify, not a control by itself.

## Suitability outcomes

- `SUITABLE`: verified law and evidence reveal no material unresolved privacy
  or cyber blocker for the bounded use, and required controls are operating and
  tested. Ordinary approval and monitoring still apply.
- `SUITABLE WITH CONTROLS`: the use can proceed only after specified,
  testable controls are implemented and approved. Do not use this outcome if a
  decisive legal threshold or high-consequence failure remains unknown.
- `PILOT ONLY`: value or safety is plausible but evidence is insufficient for
  production. Limit people, data, functionality, duration and integrations;
  prohibit consequential decisions and uncontrolled external actions.
- `NOT SUITABLE ON CURRENT INFORMATION`: a material conflict, uncontrolled
  high-consequence risk, disproportionate data use, unavailable essential
  control or inability to meet a legal requirement prevents the proposed use.
- `INSUFFICIENT INFORMATION`: missing facts prevent a defensible outcome.
  State the shortest evidence-gathering path to a decision.

These are advisory workflow outcomes, not legal conclusions or system
certification.

## Hard-stop and pilot-only prompts

Consider `NOT SUITABLE ON CURRENT INFORMATION` or `INSUFFICIENT INFORMATION`
when any of the following is material and unresolved:

- the purpose, accountable owner, affected people, system boundary or data flow
  cannot be defined;
- authority to use the data or make the proposed disclosure is not established;
- privileged, sensitive, health, secret or security-relevant material would be
  sent to an unapproved or uncontrolled system;
- a consequential action lacks meaningful human authority, validation,
  contestability, logging or rollback;
- provider terms, training use, subprocessors, hosting, retention, deletion,
  incident notice or exit cannot be established;
- prompt injection, insecure tools or excessive permissions could cause
  external action or material data access without effective containment; or
- a required legal proposition, security test or control is not verified.

Use `PILOT ONLY` when those risks can be safely isolated with non-production or
synthetic data, no consequential decisions, no uncontrolled tools, limited
users, short duration, monitoring and clear stop conditions.

## Candidate law and source routing

Use the official point-in-time legislation text. Invoke
`$check-commonwealth-legislation` for Commonwealth titles and
`$check-nsw-legislation` for NSW titles. Invoke
`$trace-commonwealth-legislative-change` when the proposed deployment or review
period crosses a Commonwealth amendment or commencement date.
Invoke `$check-australian-privacy-principles` whenever personal information or
APP-entity coverage is possible. Its decision horizon should cover the known
pilot, deployment, retention and next-review periods. A detected or unverified
APP-framework change blocks a positive suitability or pilot recommendation
until the affected analysis is refreshed.
Invoke `$route-australian-privacy-jurisdiction` for State and Territory scope,
`$assess-statutory-privacy-tort` independently of APP coverage, and
`$assess-automated-decision-transparency` for program-mediated decisions.

Candidate material may include:

- *Privacy Act 1988* (Cth), the Australian Privacy Principles, data-breach
  provisions and current or commencing automated-decision transparency
  provisions;
- applicable State or Territory public-sector privacy, health-records,
  surveillance and workplace-surveillance legislation;
- *Security of Critical Infrastructure Act 2018* (Cth), *Cyber Security Act
  2024* (Cth), Consumer Data Right, My Health Record, telecommunications and
  sector-specific legislation or instruments when triggered; and
- regulator guidance and AI risk-management standards, separately labelled as
  non-legislative material.

Verify commencement and application dates. An enacted future amendment is not
current law merely because its text exists. Preserve legislation-skill currency
flags and known-future-change qualifications.

After live APP verification, test each principle in the verified inventory
against the use case. Pay particular attention to governance and transparency,
collection and notice, scraped, inferred and generated information, momentary
holding, proportionality and data minimisation, sensitive information,
secondary model-training or evaluation uses, vendor and subprocessor access,
offshore processing, accuracy, retention, security and deletion, access and
correction. These
are issue prompts rather than a fixed statement of the APP framework.

Case law is outside scope. Separately refer material discrimination, consumer,
employment, intellectual-property, administrative, recordkeeping,
professional-duty and other sector-law issues; do not imply that a privacy and
cyber assessment completes those workstreams.

## Risk-control evidence

For each risk, distinguish:

1. inherent risk event and plausible harm;
2. preventive, detective, responsive and recovery controls;
3. design documents or vendor claims;
4. operating evidence from relevant testing;
5. residual uncertainty and acceptance owner.

Prefer use-case-specific evaluation over generic benchmark scores. Include
representative normal, edge, adversarial and affected-person scenarios. Define
acceptance criteria before testing, preserve results and set review triggers
for model, provider, data, integration, purpose or legal change.

The data-flow, document-comparison and explicit-criteria patterns are informed
by the MIT-licensed Harvey AI `harvey-labs` data-privacy-cybersecurity task
corpus. No foreign-law conclusion, fictional scenario, client artefact or
rubric answer is included.
