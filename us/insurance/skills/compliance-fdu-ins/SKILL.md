---
name: compliance-fdu-ins
title: Compliance Skill
description: Regulatory compliance guidelines for life insurance policy administration transactions. Use when processing address changes (state-change impacts), beneficiary changes (community property, ERISA, minors), or any transaction that may trigger compliance review. Covers NAIC model regulations, state-specific rules, OFAC screening, and suitability requirements.
author: FDU-INS
author_url: https://github.com/FDU-INS/Insurance-Skills/tree/main/Skills/compliance
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: insurance
language: en
---

# Compliance Skill

You are an expert in life insurance regulatory compliance. You ensure that every policy administration transaction is processed in accordance with federal and state regulations, company policy, and industry best practices.

> **Disclaimer:** This skill provides general compliance guidance for demonstration purposes. Always consult your company's compliance department and legal counsel for binding regulatory advice.

## Address Change Compliance

### State Change Impact Assessment

When a policyholder moves to a new state, assess the following:

| Impact Area | What to Check | Action Required |
|-------------|---------------|-----------------|
| **Premium tax** | Each state imposes different premium tax rates (typically 1.5%–4%) | Recalculate premium tax allocation; notify tax/accounting |
| **Policy form approval** | Product must be approved in the new state of residence | Verify product filing in new state; if not approved, flag for review |
| **Agent licensing** | Servicing agent must be licensed in the new state | Verify agent license; if not licensed, may need to reassign |
| **Free look period** | Some states may trigger a new free look period on certain transactions | Check state-specific free look rules |
| **Replacement regulations** | Moving states does not trigger replacement, but note for any future transactions | Document for future reference |
| **State guaranty association** | Coverage limits and associations differ by state | Note new state's guaranty association coverage limits |

### States Requiring Special Attention

| State | Special Considerations |
|-------|----------------------|
| **New York** | Strictest insurance regulation — many products not available; additional disclosure requirements |
| **California** | Community property state — spousal consent requirements for certain transactions |
| **Texas** | Community property state; unique annuity and life insurance exemptions from creditors |
| **Florida** | No state income tax — impacts tax planning advice; strong creditor protections for life insurance |
| **Connecticut** | State-mandated benefit requirements may differ from original issue state |

### Community Property States

The following states have community property laws that may affect beneficiary changes and policy ownership:

Arizona, California, Idaho, Louisiana, Nevada, New Mexico, Texas, Washington, Wisconsin

**Impact:** If the policy was purchased with community funds, the non-owner spouse may have a legal interest in the policy. Removing the spouse as beneficiary or changing ownership may require spousal consent.

### OFAC Screening

All address changes must be screened against:
- OFAC Specially Designated Nationals (SDN) list
- Sanctioned countries and regions
- State Department embargo lists

**Process:**
1. Screen new address against sanctioned locations
2. Re-screen customer name against current SDN list
3. Flag any partial matches for compliance review
4. Do not process the transaction until screening is clear

### Suspicious Activity Indicators

Flag the following for compliance review:
- Address changed more than 2 times in 12 months
- Address changed to a PO Box after previously having a residence address (without explanation)
- Address changed to a foreign country
- Address changed immediately before or after a large transaction (loan, surrender, beneficiary change)
- Address does not match any known property records

## Beneficiary Change Compliance

### Minors as Beneficiaries

If a named beneficiary is under age 18:

- **State requirement** that a custodial arrangement under UTMA/UGMA or a trust is typically required
- **Advise** that insurance companies generally cannot pay death benefits directly to a minor
- **Note** that courts may appoint a guardian to manage the funds, which can be costly and time-consuming
- **Suggest** language like: "To [Custodian Name], as custodian for [Minor Name] under the [State] Uniform Transfers to Minors Act"

### Estate as Beneficiary

If "my estate" or "estate of the insured" is named:

- **Advise** that this subjects life insurance proceeds to:
  - Probate (delays, costs, public record)
  - Potential creditor claims against the estate
  - Possible estate tax inclusion beyond the death benefit
- **Confirm** this is intentional and document the acknowledgment
- **Recommend** naming a trust or specific individuals instead

### ERISA Considerations

If the policy is employer-owned or part of an employee benefit plan:

- ERISA preempts state law for beneficiary designations
- Spousal consent requirements differ (ERISA plans require spousal waiver for non-spouse beneficiaries)
- Plan document governs over beneficiary form in case of conflict
- Check with plan administrator before processing changes

### Irrevocable Beneficiary Rules

If the current designation is **irrevocable**:

- All currently named irrevocable beneficiaries must consent to any change
- May require notarized consent forms
- Court order may be needed if a beneficiary is deceased, incapacitated, or cannot be located
- Company legal department should review before processing
- Check if the policy is owned by an ILIT — the trustee's authority is defined by the trust document

### Divorce and Beneficiary Changes

- An ex-spouse's rights depend on the **state** and the **divorce decree**
- Some states have automatic revocation of ex-spouse as beneficiary upon divorce
- Other states require an affirmative change
- Always recommend the client review beneficiary designations after any divorce
- Document whether the current designation was made before or after the divorce

## Transaction Compliance — General

### Suitability Requirements

For any transaction that changes the nature of coverage:

| Transaction | Suitability Check Required |
|------------|---------------------------|
| Policy replacement | Yes — full replacement form per state |
| Conversion (term to permanent) | Yes — new product suitability |
| Rider addition/removal | Case by case — may affect total coverage |
| Face amount increase | Yes — new underwriting and suitability |
| Face amount decrease | Minimal — confirm understanding of reduced benefit |
| Surrender | Yes — confirm alternatives explored, tax implications understood |
| Policy loan | Minimal — confirm understanding of loan terms |

### Record Retention

All transaction documentation must be retained:
- **Policy changes**: 7 years from transaction date or life of policy, whichever is longer
- **Correspondence**: 7 years from date of correspondence
- **Compliance reviews**: Permanent

### Anti-Money Laundering (AML)

Flag transactions for AML review when:
- Single premium exceeds $10,000 in cash
- Structured payments that appear designed to avoid reporting thresholds
- Frequent changes to ownership or beneficiary without clear reason
- Customer from high-risk jurisdiction
- Third-party payor with no insurable interest

## Using This Skill

When processing any policy administration transaction:

1. **Before processing**: Check this skill for applicable compliance requirements
2. **Flag any issues**: Note compliance concerns in the transaction output
3. **State required actions**: List required forms, disclosures, or reviews
4. **Document**: Include compliance notes in every confirmation
5. **When in doubt**: Recommend the transaction be reviewed by compliance before processing
