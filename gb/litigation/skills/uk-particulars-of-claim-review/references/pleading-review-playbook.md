# Pleading Review Playbook

Use this reference when reviewing draft Particulars of Claim for England and Wales proceedings.

## Pleading Mindset

Particulars of Claim need material facts, not the full evidence bundle. A good review asks:

- What cause of action is pleaded?
- What facts are pleaded for each element?
- What source supports those facts?
- What remedy is sought?
- What procedural or limitation issue needs verification?

Do not certify merits or strategy.

## Element Map

For each cause of action:

| Field | Meaning |
|---|---|
| `cause_of_action` | claim label |
| `element` | legal/factual component to plead |
| `pleaded_facts` | paragraphs containing material facts |
| `source` | document/source supporting those facts |
| `gap` | missing or weak pleading point |
| `verification` | rule/source to check |

If the law is not supplied or retrieved, mark the element map `verify_current_law`.

## Material Facts Versus Evidence

Flag:

- evidence pleaded at unnecessary length,
- bare legal conclusions without facts,
- facts alleged without source,
- chronology too thin to support causation,
- remedy not tied to pleaded facts,
- pleaded facts inconsistent with documents.

## Common Review Areas

- Parties and capacity.
- Contract terms or duties.
- Breach or wrongful act.
- Causation.
- Loss and heads of loss.
- Interest basis, rate, and period.
- Limitation and standstill/extension assumptions.
- Jurisdiction, correct court/list, service basis, allocation/track.
- Pre-action protocol context.
- Particulars for fraud, dishonesty, misrepresentation, conspiracy, professional negligence, discrimination, or serious misconduct.

## Sensitive Allegations

For fraud, dishonesty, bad faith, conspiracy, or serious misconduct:

- require source support,
- identify who did what, when, and with what knowledge/intention where pleaded,
- mark missing particulars as `critical`,
- do not soften the need for lawyer/counsel review.

## Output Sections

1. Overall pleading health.
2. Element maps by cause of action.
3. Missing material facts.
4. Limitation and party issues.
5. Remedies and interest.
6. Source/support gaps.
7. CPR/Practice Direction/protocol checks with date checked.
8. Questions for solicitor/counsel/client.
