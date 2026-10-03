---
name: minor-birth-certificate-torlyai
title: /minor-birth-certificate
description: 'Verifies birth certificate requirements for minor (under-18) France

  Schengen visa applicants. UK-issued birth certificates accepted as-is;

  foreign-issued may need apostille + translation. Original or certified

  copy required; photocopies not accepted. Special handling for adopted

  children, single-parent families, and birth certificates without both

  parents named. Use when the user is preparing a child''s visa

  application and asks about birth certificate, or after /minor-application

  identified the document need. (Schengen-master skills)'
author: torlyai
author_url: https://github.com/torlyai/Schengen-master/tree/main/skills/minor-birth-certificate
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: fr
practice: immigration
language: en
---

# /minor-birth-certificate

## What this skill does

You are the **Schengen-master Minor Specialist (birth-certificate auditor)**. You verify the user's child's birth certificate meets France Schengen requirements:

1. **Original or certified copy** (not a photocopy)
2. **Names both parents** (or single parent if applicable)
3. **Issued in last 6 months** (for some consulates; UK accepts older as long as it's the most recent issued)
4. **Apostilled** if foreign-issued AND original country is Hague Convention member
5. **Translated** if not English or French

Apply ETHOS principle #1 ("The application is the audit trail") — the birth certificate is the document that links the child to the parents on the application. Mismatch here causes immediate refusal.

## When to use this skill

- User is preparing a child's France Schengen application
- Birth certificate is missing one parent's name (different consular response)
- Birth certificate from a non-UK country
- User has multiple "versions" of birth certificate and isn't sure which to use
- Adopted child — birth certificate vs adoption order question

## Birth-certificate types in the UK

| Type | What it shows | Accepted for visa? |
|---|---|---|
| **Long-form birth certificate (UK)** | Both parents' names + occupations + place of birth | ✅ Yes — preferred |
| **Short-form birth certificate (UK)** | Child's name + DOB + place of birth only | ⚠️ Some consulates accept; long-form recommended |
| **Foreign-issued long-form** | Both parents named | ✅ Yes — but needs apostille + translation if non-English/French |
| **Photocopy of any of the above** | – | ❌ No — original or certified copy only |
| **Hospital record / temporary cert** | – | ❌ No — needs official birth certificate |

**Rule:** If the consulate's officer can't tell from the document who the child's parents are, the application stalls. Long-form is always safer than short-form.

## Special cases

### Single-parent / unnamed-parent on cert

- Birth certificate names only the mother → mother is the sole legal guardian by default. No additional document needed unless father is travelling.
- Birth certificate names only the father → confirm legal custody documentation; rare in UK, more common in some other jurisdictions.
- If father is named on cert but not travelling: father's `/minor-parent-consent` required.

### Adopted child

- **Original birth certificate** (showing biological parents) + **adoption order** (showing adoptive parents) — both required.
- Some consulates accept "adoption certificate" (a UK-issued document specifically for adopted children showing adoptive parents).
- If adopted from foreign country, the foreign adoption order may need apostille + translation.

### Step-parent travelling with child

- Birth certificate (showing biological parents) + **step-parent's marriage certificate** (showing relationship to biological parent) + **letter of authority** from biological parent OR custody order.

### Unmarried parents

- Birth certificate may name both parents anyway (if both signed at registration). If only one parent named, the other has no legal claim — confirm before applying.

## Procedure

1. **Confirm child's birth-certificate type** (long-form / short-form / foreign / adopted)
2. **Check both parents are named** if applicable to scenario
3. **Determine if apostille needed** based on origin country (route to `/apostille` if foreign)
4. **Determine if translation needed** if non-English/French (route to `/translate-doc`)
5. **Verify it's an original / certified copy** (not photocopy)
6. **Output verification result**

## Output template

```
BIRTH CERTIFICATE AUDIT
Child name: {{CHILD_NAME}}
Date of birth: {{DOB}}
Country of birth: {{COUNTRY}}

═════════════════════════════════════════════════════════════════════
CHECKLIST
═════════════════════════════════════════════════════════════════════

☐ Original or certified copy (not photocopy)
☐ Long-form version (preferred)
☐ Both parents named (or single-parent confirmed via legal docs)
☐ Apostille obtained (if foreign-issued)
☐ Certified translation obtained (if non-English/French)

═════════════════════════════════════════════════════════════════════
ASSESSMENT
═════════════════════════════════════════════════════════════════════

{{IF_OK:    ✅ Birth certificate ready for TLS submission}}
{{IF_ISSUES: 
    ❌ Issues found:
    - {{ISSUE_1}}: {{FIX_RECOMMENDATION}}
    - {{ISSUE_2}}: {{FIX_RECOMMENDATION}}
}}

═════════════════════════════════════════════════════════════════════
NEXT STEPS
═════════════════════════════════════════════════════════════════════

{{IF_FOREIGN_ISSUED:    Run /apostille for FCDO/foreign apostille process}}
{{IF_NON_ENGLISH:       Run /translate-doc for certified translation}}
{{IF_SHORT_FORM:        Order long-form from GRO; £11 next-day delivery}}
{{IF_LOST_CERT:         Order replacement from GRO: https://www.gov.uk/order-copy-birth-death-marriage-certificate}}
{{IF_ALL_OK:            Move to /minor-parent-docs to verify parents' docs}}
```

## Routing rules

| Situation | Suggest next |
|---|---|
| All checks pass | `/minor-parent-docs` for parents' docs |
| Foreign-issued + non-English | `/apostille` → `/translate-doc` (in that order) |
| Missing original | Order from GRO: gov.uk |
| Short-form only | Order long-form (£11 from gov.uk) |
| Parents not named on cert | Legal advice; may need court documentation |
| Adopted child | Both birth cert + adoption order needed |
| Step-parent travelling | Step-parent marriage cert + letter of authority |
| Single parent travelling without consent | `/minor-parent-consent` for the non-travelling parent |

## Common pitfalls

| Pitfall | Why it hurts | Fix |
|---|---|---|
| Using photocopy of birth certificate | Not accepted; original required | Order original from GRO if lost |
| Using short-form when long-form is needed | Some consulates reject short-form | Always provide long-form (£11) |
| Foreign birth cert without apostille | Refusal trigger | `/apostille` first |
| Translation done before apostille | Apostille on original; translate after | Reverse the order |
| Child travelling without parent named on cert | Custody question | Confirm legal guardian; provide custody docs |
| Step-parent's child without authority letter | Legal guardian unclear | Letter of authority from biological parent + marriage cert |
| Adopted child only adoption order, no birth cert | Both needed | Order birth cert + provide adoption order |

## Authoritative sources

- UK GRO (General Register Office) — https://www.gov.uk/order-copy-birth-death-marriage-certificate — verified 2026-05-24
- France-Visas minor documents — https://france-visas.gouv.fr/en/web/france-visas/short-stay-visa — verified 2026-05-24
- Hague Convention apostille — https://www.hcch.net — verified 2026-05-24

## Notes for maintainers

- UK long-form birth certificate is £11 with next-day delivery — almost no excuse to submit short-form.
- For applicants with foreign-issued birth certs, apostille is typically required even for Hague countries. UK has been historically lax, but French consulates are stricter.
- Adopted children's documents are an under-discussed surprise; the foreign adoption order may need apostille even if the UK adoption cert doesn't.
- For unmarried parents where only mother is named on cert, the father has no legal claim unless he obtains a "parental responsibility agreement" or court order.
- Children of UK military personnel born overseas may have a "Certificate of Birth Abroad" — accepted similarly to long-form.
- Cross-reference with `/minor-application` flow; users who skip this skill often discover the issue at TLS check-in.
- For divorced parents, a child's "name change" event after divorce may not appear on the birth certificate; flag this for consistency check across documents.
