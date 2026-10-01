# Entity Verification Workflow

Step-by-step multi-registry verification workflow for KYC/AML compliance checks across European government registries.

---

## Step 1: Identify Entity Type and Country

Before querying any registry, determine:

- **Legal form** - sp. z o.o., SA, SAS, SARL, GmbH, SL, etc.
- **Country of incorporation** - PL, FR, AT, ES
- **Identifier available** - NIP, KRS, SIREN, NIF, or company name only
- **Sector** - financial services (triggers KNF check), general commercial, real estate, etc.

This determines which registries are relevant and in which order to check them.

## Step 2: Beneficial Ownership Verification

**Priority: This is always the first substantive check.**

| Country | Source | Actor | Input |
|---|---|---|---|
| Poland | CRBR (Central Register of Beneficial Owners) | `regdata/crbr-beneficial-owners-scraper` | `{"nip": "..."}` |
| France | Societe.com (shareholders section) | `regdata/societe-com-scraper` | `{"sirenNumbers": ["..."]}` |
| Austria | Not directly available via registry - use WKO for entity confirmation, then request UBO documentation from the entity | - | - |
| Spain | Not directly available via registry - use Company Directory for officers, then request UBO documentation | - | - |

**Analyze the results:**

- Are all UBOs natural persons? If a legal entity appears as UBO, trace through the chain
- Does total ownership add up? Gaps may indicate unreported holders
- Are there multiple UBOs with exactly 25.01% each? This can indicate structuring to minimize visibility
- Check registration dates - very recent CRBR entries before a transaction are worth investigating
- "Inny" (other) control type in CRBR requires explanation - what is the control mechanism?

## Step 3: Regulatory Status Check

**Applies to: financial services entities, payment processors, lending companies, e-money issuers.**

| Country | Source | Actor | Input |
|---|---|---|---|
| Poland | KNF (Financial Supervision Authority) | `regdata/knf-registry-scraper` | `{"name": "..."}` |
| France | Included in Societe.com profile | (same as Step 2) | - |
| Austria | FMA registry (manual check) | - | - |
| Spain | CNMV/Banco de Espana (manual check) | - | - |

**Decision logic:**

- **Licensed and active** - record license number, category, and date. Proceed
- **Licensed with conditions/warnings** - document the conditions. Flag for review but proceed
- **Suspended or revoked** - STOP. This is a critical red flag. Escalate immediately
- **Not found, but entity claims to be regulated** - STOP. Verify directly with the regulator
- **Not found, entity does not require a license** - proceed to next step

## Step 4: Board and Management Composition

| Country | Source | Actor | Input |
|---|---|---|---|
| Poland | KRS (National Court Register) | `regdata/krs-fullnames-scraper` | `{"krsNumbers": ["..."]}` |
| France | Societe.com (dirigeants section) | (same as Step 2) | - |
| Austria | WKO Business Directory | `regdata/wko-business-directory-scraper` | `{"searchQuery": "..."}` |
| Spain | Company Directory (officers) | `regdata/spain-company-directory-scraper` | `{"nifNumbers": ["..."]}` |

**Analyze the results:**

- Cross-reference board members against UBO list from Step 2. In small companies, overlap is normal. In large companies, complete overlap may indicate insufficient governance separation
- Check for professional nominees - individuals appearing as directors of many unrelated entities
- Verify that the number of board members meets statutory minimums for the legal form
- Look for very recent changes in board composition - new directors appointed just before a transaction can indicate attempts to obscure the true decision-makers
- For Polish companies, the KRS actor returns non-anonymized names (unlike the eKRS portal) - this is critical for accurate screening

## Step 5: Business Registration and Trade License Verification

This step confirms the entity's legitimate business activity and physical presence.

| Country | Source | Actor | Input |
|---|---|---|---|
| Austria | WKO Business Directory | `regdata/wko-business-directory-scraper` | `{"searchQuery": "..."}` |
| Spain | Company Directory | `regdata/spain-company-directory-scraper` | `{"nifNumbers": ["..."]}` |
| France | Societe.com | (same as Step 2) | - |
| Poland | CRBR + KRS combination | (same as Steps 2-4) | - |

**Verify:**

- Does the registered address correspond to a real business location (not a mass-registration virtual office)?
- Do the trade licenses or CNAE codes match the entity's stated business activity?
- Is the entity actively trading (not dormant or in wind-down)?
- For Austrian entities, WKO membership is expected for legitimate businesses - absence requires explanation

## Step 6: Document Findings and Calculate Risk Score

Compile all findings into a structured assessment:

```
Entity: [Company Name]
Identifier: [NIP/KRS/SIREN/NIF]
Country: [PL/FR/AT/ES]
Date of Check: [YYYY-MM-DD]
Analyst: [Name]

1. Beneficial Ownership
   - UBOs identified: [names, percentages]
   - Ownership structure: [simple/complex]
   - Flags: [none / list flags]

2. Regulatory Status
   - License: [type, number, status] or [N/A]
   - Flags: [none / list flags]

3. Board Composition
   - Directors: [names, roles]
   - UBO-Board overlap: [yes/no, details]
   - Flags: [none / list flags]

4. Business Registration
   - Address verified: [yes/no]
   - Activity matches stated purpose: [yes/no]
   - Flags: [none / list flags]

5. Risk Score: [X/21] per scoring matrix
   - Entity type: [1-3]
   - Ownership transparency: [1-3]
   - Jurisdiction: [1-3]
   - Regulatory status: [1-3]
   - Industry: [1-3]
   - PEP exposure: [1-3]
   - Adverse media: [1-3]
```

## Step 7: Decision Matrix

Based on the risk score and individual flag severity:

| Score | Flags | Decision | Next Action |
|---|---|---|---|
| 7-10 | None | **PROCEED** | Standard onboarding, schedule periodic review |
| 7-10 | Minor flags | **PROCEED WITH CONDITIONS** | Document flags, set 6-month review cycle |
| 11-15 | None | **ENHANCED REVIEW** | Obtain additional documentation from entity |
| 11-15 | Any flags | **ENHANCED REVIEW** | Senior management approval required |
| 16-21 | None | **ENHANCED REVIEW** | Full EDD procedure, senior management approval |
| 16-21 | Any flags | **REJECT or ESCALATE** | Do not onboard without MLRO sign-off |
| Any | Critical flag (unlicensed, missing UBO, sanctions) | **REJECT or ESCALATE** | Immediate escalation to compliance officer |

**Periodic review schedule:**
- Low risk (7-10): Annual review
- Medium risk (11-15): Semi-annual review
- High risk (16-21): Quarterly review
- Trigger events: re-check immediately upon material change (new UBO, board change, adverse media)
