# Data Subject Rights (Articles 12–22)

Rights apply to individuals whose personal data you process. Controllers are responsible for responding; processors assist the controller.

## The rights

| Article | Right | Summary |
|---|---|---|
| 13 / 14 | Information | At collection (or within 1 month if obtained indirectly), subjects must receive a privacy notice. |
| 15 | Access | Confirmation of processing and a copy of personal data, plus categories, recipients, retention, rights. |
| 16 | Rectification | Correct inaccurate data. |
| 17 | Erasure ("right to be forgotten") | Delete when basis no longer applies; subject withdraws consent; unlawful processing; legal obligation. Subject to exemptions (freedom of expression, legal claims, public interest research). |
| 18 | Restriction | Temporarily halt processing (e.g., during accuracy dispute). |
| 20 | Portability | Data subject provided data, processed by automated means on consent or contract basis → provide in structured, machine-readable format. |
| 21 | Objection | Object to processing based on Art. 6(1)(e) or (f); absolute right to object to direct marketing. |
| 22 | Automated decision-making | Right not to be subject to solely automated decisions with legal or similarly significant effects, subject to exceptions + safeguards. |

## Response timing

- **Standard deadline: 1 month** from receipt of the request.
- **Extension: 2 additional months** for complex or numerous requests; must inform subject within the first month of the extension and the reasons.
- **Fee:** free, unless the request is manifestly unfounded or excessive (controller bears proof).

## Identity verification

Reasonable measures to verify the requester's identity, proportionate to the risk. Don't over-collect — asking for a passport scan to verify a profile-data deletion is typically excessive.

## Response workflow

```
Request received
  ↓
Log in DSR register (timestamp, type, subject, source)
  ↓
Verify identity (proportionate)
  ↓
Determine scope: which systems contain this person's data
  ↓
Apply exemptions (legal claims, others' rights, health data via professional)
  ↓
Execute (export / correct / delete / restrict)
  ↓
Respond to subject with outcome (or refusal with reasons)
  ↓
Instruct processors to mirror the action
  ↓
Close ticket with evidence
```

## Common complications

| Scenario | Handling |
|---|---|
| Backups | Don't need to restore backups to delete; document that backups will be overwritten on the next rotation and the data is isolated. |
| Legitimate interests objection | You must stop unless you demonstrate compelling legitimate grounds overriding the subject's rights (Art. 21(1)). |
| Joint controllers | Agreement (Art. 26) must define which party handles DSRs. |
| Child data | Parental / guardian handling per national law (age of digital consent varies 13–16 across Member States). |
| Mixed data (third parties in the same record) | Redact or withhold third-party personal data; right of the subject does not extend to others'. |

## DSR metrics worth tracking

- Requests received per month, by type
- Average and P95 response time
- % responded within 1 month
- % extensions used
- % refused (with reason codes)

Regulators increasingly benchmark organisations by DSR response performance; stale metrics are a red flag.
