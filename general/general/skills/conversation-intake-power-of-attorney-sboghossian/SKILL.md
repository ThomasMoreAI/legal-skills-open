---
name: conversation-intake-power-of-attorney-sboghossian
title: Intake — Power of Attorney
description: Use when a user wants to draft a power of attorney (POA) and Claude must collect the identity, scope, duration, and notarization inputs before generating the instrument. Triggers on requests to prepare a general POA, special POA, limited authority letter, or agency arrangement. Covers MENA notarization requirements (KSA MOJ Najiz, UAE Notary, Lebanon Notary) and cross-border apostille/legalization chains. Routes to draft-power-of-attorney with a notarization checklist.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/conversation/conversation-intake-power-of-attorney
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: en
---

# Intake — Power of Attorney

## When this applies

Activate when a user requests drafting of a power of attorney (POA) — also known in civil-law jurisdictions as a mandate (mandat / وكالة wakala), proxy, or authority letter. POAs are one of the most common legal instruments in MENA practice: they are used for real estate transactions, banking, court representation, company management, and immigration. Incorrect scope or a missing notarization renders the POA useless at the moment it is needed.

## Behavior

Multi-turn intake (two turns for standard cases; three for cross-border or complex scope). Confirm the cross-border use question early — if apostille or MOFA legalization is required, the notarization process must be planned before the POA is even drafted.

## Required fields

### 1. Principal (Grantor)

- Full legal name (as it appears on passport or national ID — any discrepancy between the POA and the principal's ID will cause rejection at the notary).
- Nationality and passport / national ID number.
- Jurisdiction of residence and/or domicile.
- Capacity: individual? Corporate entity? If corporate, confirm the signatory has authority to sign the POA on behalf of the company (board resolution may be required).

### 2. Attorney-in-fact (Agent)

- Full legal name, nationality, passport / national ID number.
- Relationship to the principal: family member, employee, lawyer, trusted third party.
- Jurisdiction of residence (relevant for enforcement and for knowing which notary is competent to notarize).
- Multiple agents: are they to act jointly (all signatures required) or severally (either can act alone)? Confirm — joint authority provides more control; several authority is more practical for day-to-day transactions.

### 3. Scope of authority

This is the most consequential field. Define it precisely.

**General POA**: grants the agent broad authority across all personal and/or business matters of the principal. Used when the principal is incapacitated or moving abroad for an extended period. Risk: a general POA is easily abused; advise the user to consider whether a special POA better serves the purpose.

**Special (limited) POA**: authority restricted to one or more specific transactions or categories. Standard categories in MENA practice:

| Category | Typical scope clause |
|---|---|
| Real estate | Buy, sell, lease, mortgage a specific property (identified by plot/title number); sign all deeds, registrations, and ancillary documents |
| Banking / financial | Open/close accounts; transfer funds up to AED/SAR X per transaction; manage investments; execute agreements with named bank |
| Litigation / court | Represent principal before named court or in named case number; file, sign, and receive all court documents; engage or dismiss sub-counsel |
| Business management | Manage named company's day-to-day operations; sign contracts up to value X; hire/fire employees; bind the company in commercial transactions |
| Immigration / government | Apply for visas, residence permits, driving licenses; receive documents from government entities on behalf of principal |
| Company incorporation | Incorporate and register a named company; sign memorandum and articles; open a bank account |

Confirm: is there a monetary threshold above which the agent cannot act without additional authorization?

### 4. Duration

- **Specific date range**: e.g., "valid from 1 June 2025 to 31 December 2025." Recommended for real estate transactions with a defined closing timeline.
- **Event-conditional**: e.g., "valid until the property registered at [Plot No.] is sold and title transferred." Terminates automatically on completion.
- **Open-ended**: no expiry date specified. Remains valid until revoked by the principal. Common for general POAs; note that some jurisdictions impose limits on validity periods of unregistered open-ended POAs (UAE: no statutory maximum, but banks and government offices often require a POA dated within the last 12 months).
- **Durable (enduring)**: remains valid even if the principal becomes mentally incapacitated. UAE Federal Personal Status Law does not have a direct equivalent to the UK Lasting Power of Attorney; consider establishing a trust or separate court guardianship order for incapacity planning.

### 5. Cross-border use

Is the POA intended to be used in a jurisdiction different from where it is signed?

This is the most common source of POA failure: the instrument was signed in one country but is rejected in another because the authentication chain is incomplete.

| Scenario | Required authentication chain |
|---|---|
| Signed in UAE, used in UAE | UAE Notary Public attestation only |
| Signed in UAE, used in UK | UAE Notary → UAE MOFA attestation → UAE Embassy in UK (apostille via UK Foreign Office or MOFA, depending on route) |
| Signed in KSA, used in UAE | Saudi Notary (MOJ Najiz) → Saudi MOFA → UAE Embassy in Riyadh → UAE MOFA in Abu Dhabi |
| Signed in Lebanon, used in UAE | Lebanese Notary → Lebanese MOFA (Ministry of Foreign Affairs) → UAE Embassy in Beirut → UAE MOFA |
| Signed in UAE, used in France | UAE Notary → UAE MOFA → French Embassy in UAE → (in France) sworn translation into French if document is in Arabic or English |
| Hague Convention apostille | For countries that have joined the Hague Convention (1961): a single apostille from the competent authority suffices instead of full embassy-chain legalization. As at 2025: UAE: member (acceded 2021); KSA: member (acceded 2012); Lebanon: not a member (check current status); Egypt: not a member. |

### 6. MENA notarization process

| Jurisdiction | Notarization body | Key points |
|---|---|---|
| KSA | Ministry of Justice (MOJ) — Najiz platform (online notarization available for many POA types); physical notary offices in MOJ courthouses | Najiz allows principal to sign electronically for domestic POAs; cross-border still requires physical or embassy attestation |
| UAE (federal) | Notary Public offices under Ministry of Justice; Dubai Courts Notary; Abu Dhabi Judicial Department Notary | Principal must appear in person unless signing at a UAE embassy/consulate abroad; identity documents checked against Emirates ID / passport |
| DIFC | DIFC Courts Notary; also UAE federal notaries for DIFC entities | DIFC POAs must comply with DIFC governing law; bilateral enforcement via DIFC-UAE gateway |
| Lebanon | Notaire (notary public) attached to the Lebanese Notarial Service; or Kâtib al-Adl (civil law notary) | Arabic and/or French; MOFA attestation required for cross-border use |
| Egypt | General Authority for Real Estate Publicity; Notary Public offices | Arabic; cross-border use requires MOFA chain |

### 7. Revocability

- By default, a POA is revocable by the principal at any time.
- **Irrevocable POA** (wakala ghair qabila lil-ruju'): valid only if it is granted for the benefit of the agent or a third party and is coupled with an interest (i.e., the agent has an independent legal interest in the subject matter). Irrevocable POAs are recognized in UAE, KSA, and LB law in specific contexts (e.g., a mortgagee holding a POA over the mortgaged property as additional security). Do not draft an irrevocable POA without specific legal authority — courts are skeptical.
- **Revocation formalities**: to effectively revoke, the principal must notify the agent and, if the POA has been registered, file a revocation notice with the same registry.

### 8. Successor agent

If the primary agent is unavailable (death, incapacity, conflict of interest), is a successor agent designated? Recommended for general POAs with long validity periods.

### 9. Special instructions and limits

Any specific transaction limits, prohibited acts, or conditions:
- Maximum transaction value per single act.
- Prohibition on self-dealing (agent must not enter into transactions with themselves as counterparty).
- Requirement to keep accounts and report to principal.
- Specific property description (for real estate POAs: include title deed number, plot number, area, and emirate/district to prevent fraud).

## Output

At the end of intake, produce:

1. A structured intake summary confirming all nine fields and outstanding items.
2. A notarization checklist specifying: (a) which notary has jurisdiction; (b) what identity documents the principal must bring; (c) whether MOFA attestation is required; (d) whether apostille suffices (if the destination country is a Hague member); (e) estimated timeline.
3. A routing instruction to [[draft-power-of-attorney]] with the completed intake data.

## Critical traps — always flag

- **Apostille vs MOFA legalization**: KSA joined the Hague Apostille Convention in 2012; UAE acceded in 2021. This significantly simplifies cross-border POA authentication for transactions with Hague-member countries. For non-Hague countries (LB, EG as at 2025), the full MOFA embassy chain is still required.
- **Arabic-language requirement**: all POAs to be used in KSA courts or government offices must be in Arabic or accompanied by a certified Arabic translation. UAE government offices and DIFC courts accept Arabic (onshore) or English (DIFC). Lebanon: French or Arabic.
- **Specific property identification**: POAs granted for real estate transactions must identify the specific property by legal description (title deed number, plot number) to be enforceable and registrable at the land department. A general reference to "any real estate" will often be rejected by land registries.
- **Corporate authorization**: if the principal is a company, the signatory's authority to grant the POA must be evidenced by a board resolution. The notary will require the board resolution and a copy of the company's trade license / CR.

## Do not

- Draft an irrevocable POA without the user understanding the legal requirements — coupled-with-interest is a strict requirement.
- Omit the cross-border authentication chain for POAs intended for use in a different country from where they are signed.
- Describe the scope of authority vaguely ("all matters") for a special POA — a vague scope will be rejected by government registries and may expose the principal to unauthorized acts.

## Related skills

- [[draft-power-of-attorney]]
- [[kb-notarization-mena]]
- [[conversation-intake-incorporation]]
- [[kb-real-estate-mena]]
- [[conversation-uncertainty-language]]
