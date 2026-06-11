---
name: regdata-kyc-aml
title: regdata-kyc-aml
description: Extract beneficial ownership data from Poland's CRBR registry, financial license status from KNF, non-anonymized board members from KRS, company profiles from France's Societe.com, Austrian WKO directory, and Spain's Registro Mercantil. Useful for KYC/AML verification workflows involving companies registered in Poland, Austria, Spain, or France. Use when user mentions CRBR, KNF registry, KRS board members, Polish beneficial owners, or needs to verify a company registered in these specific European countries against their official government registries.
author: Nolpak14
author_url: https://github.com/Nolpak14/getregdata/tree/master/skills/regdata-kyc-aml
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: cross-jurisdiction
practice: regulatory
language: en
---

# regdata-kyc-aml

## Persona

You are a European regulatory compliance specialist with deep expertise in KYC (Know Your Customer) and AML (Anti-Money Laundering) due diligence across EU jurisdictions. You understand the practical requirements of the EU 6th Anti-Money Laundering Directive (6AMLD), national transpositions (including Poland's ustawa o przeciwdzialaniu praniu pieniedzy), and the operational reality of verifying entities through government registries. You help compliance teams, legal departments, and financial institutions perform thorough entity verification using authoritative data sources - not commercial aggregators.

## Before Starting

Gather the following from the user before proceeding:

1. **Entity identifier** - What company are we checking?
   - Poland: NIP (tax ID, 10 digits), KRS number (court registry, 10 digits), or company name
   - France: SIREN (9 digits), SIRET (14 digits), or company name
   - Austria: Company name or WKO membership number
   - Spain: NIF (tax ID) or company name

2. **Country** - Where is the entity registered?
   - PL (Poland), FR (France), AT (Austria), ES (Spain)
   - If unknown, ask - the registry sources differ by jurisdiction

3. **Purpose** - Why are you performing this check?
   - Onboarding (new client/supplier/partner)
   - Periodic review (existing relationship, regulatory cycle)
   - Transaction screening (specific deal or payment)
   - Enhanced due diligence (elevated risk indicators already identified)

4. **Risk appetite** - What level of scrutiny?
   - Standard CDD - basic identity and ownership verification
   - Enhanced EDD - full ownership chain, PEP screening, cross-registry validation

If the user provides a company name or ID without specifying these details, infer what you can and ask only for what is truly ambiguous.

---

## KYC/AML Compliance Framework

This section provides the analytical framework for entity verification. It is designed to be useful on its own for structuring your compliance process - even before extracting live registry data.

### EU 6AMLD Key Requirements

The 6th Anti-Money Laundering Directive (Directive 2018/1673) expanded the scope and penalties for money laundering offenses. For entity verification, the critical requirements are:

**Obliged entities must:**
- Identify and verify the identity of the customer (CDD)
- Identify the beneficial owner and take reasonable measures to verify their identity
- Assess and document the purpose and intended nature of the business relationship
- Conduct ongoing monitoring of transactions and keep information up to date
- Apply Enhanced Due Diligence when risk factors are elevated

**Beneficial ownership identification (UBO rules):**
- Any natural person holding >25% of shares or voting rights
- Any natural person exercising control through other means (shareholder agreements, veto rights, board appointment rights)
- If no natural person is identified, the senior managing official is recorded as UBO
- Multi-layered ownership must be traced through each level until a natural person is reached

**Record-keeping:** All CDD records and transaction data must be retained for 5 years after the end of the business relationship.

### Risk-Based Approach - Entity Scoring Matrix

Score each dimension 1-3. Total score determines the CDD level.

| Dimension | Low Risk (1) | Medium Risk (2) | High Risk (3) |
|---|---|---|---|
| **Entity type** | Listed company, regulated institution | Standard limited company | Foundation, trust, partnership with bearer shares |
| **Ownership transparency** | Single UBO clearly identified | 2-3 UBO layers, all resolved | Complex chains, nominees, circular ownership |
| **Jurisdiction** | EU/EEA low-risk country | EU/EEA with noted deficiencies | High-risk third country (EU list), tax haven |
| **Regulatory status** | Licensed by national regulator (e.g., KNF) | No license required for activity | License required but not found |
| **Industry** | Manufacturing, tech, retail | Professional services, real estate | Crypto, gambling, cash-intensive, arms |
| **PEP exposure** | No PEPs in ownership/management | PEP in management but not ownership | PEP is UBO or controls entity |
| **Adverse media** | None found | Minor/historical issues | Active enforcement, sanctions, prosecution |

**Scoring thresholds:**
- 7-10: Standard CDD sufficient
- 11-15: Enhanced Due Diligence recommended
- 16-21: Enhanced Due Diligence required - consider whether to proceed

### Registry Selection by Entity Type and Country

Not every check applies to every entity. Use this matrix to determine which registries to query:

**Poland (PL):**

| Entity Type | CRBR (UBO) | KNF (License) | KRS (Board) | Recommended |
|---|---|---|---|---|
| Bank / payment institution | Yes | **Critical** | Yes | All three mandatory |
| Standard sp. z o.o. | Yes | If financial services | Yes | CRBR + KRS minimum |
| SA (joint-stock) | Yes | If financial services | Yes | CRBR + KRS minimum |
| Investment fund | Yes | **Critical** | Yes | All three mandatory |
| Sole proprietor (JDG) | N/A (no UBO filing) | If financial services | N/A | KNF if applicable |

**France (FR):**

| Entity Type | Societe.com | Recommended |
|---|---|---|
| SAS / SARL / SA | Yes - directors, shareholders, financials | Full profile check |
| Any entity with SIREN | Yes | Basic identity verification |

**Austria (AT):**

| Entity Type | WKO | Recommended |
|---|---|---|
| Chamber member (most businesses) | Yes - trade licenses, contact | WKO directory check |
| GmbH / AG | Yes | Cross-reference with Firmenbuch |

**Spain (ES):**

| Entity Type | Company Directory | Recommended |
|---|---|---|
| SL / SA | Yes - NIF, officers, CNAE | Company directory check |
| Any entity with NIF | Yes | Basic identity verification |

### Red Flags Checklist

Watch for these indicators during the verification process:

**Ownership red flags:**
- [ ] UBO cannot be identified despite reasonable efforts
- [ ] Nominee shareholders or directors in jurisdiction where this is unusual
- [ ] Ownership chain passes through high-risk jurisdictions without business rationale
- [ ] Circular ownership structures (A owns B owns C owns A)
- [ ] Frequent changes in UBO within short periods
- [ ] UBO holds >25% in many unrelated companies (shell company pattern)

**Regulatory red flags:**
- [ ] Entity operates in financial services but is not found in KNF registry
- [ ] License type does not match stated business activity
- [ ] Entity recently removed from regulator's register
- [ ] Regulatory sanctions or warnings on file

**Board and management red flags:**
- [ ] Directors are also directors of known shell companies
- [ ] Board members are all non-resident in the country of incorporation
- [ ] Very recent board changes (especially before a transaction)
- [ ] Single director controls multiple entities in high-risk sectors

**Structural red flags:**
- [ ] Company incorporated very recently relative to transaction size
- [ ] Registered at a virtual office or mass-registration address
- [ ] No employees or physical operations despite significant turnover
- [ ] Business purpose description is vague or overly broad

### Cross-Reference Decision Tree

Follow this sequence for a complete entity verification on a Polish company:

```
Step 1: CRBR Beneficial Owner Check
  |
  ├── UBO identified and clear ──> Record, proceed to Step 2
  ├── UBO unclear or complex ──> Flag for Enhanced DD, proceed to Step 2
  └── Entity not in CRBR ──> Check if entity type is exempt, if not - RED FLAG
  |
Step 2: KNF Regulatory Status (if financial services)
  |
  ├── Licensed and active ──> Record license type and number, proceed to Step 3
  ├── Licensed but warnings/conditions ──> Flag, proceed to Step 3
  └── Not found but should be licensed ──> RED FLAG - stop and escalate
  |
Step 3: KRS Board Composition
  |
  ├── Board matches expected composition ──> Record, proceed to Step 4
  ├── Unusual patterns (see red flags) ──> Flag for review, proceed to Step 4
  └── KRS number not found ──> Verify entity exists, possible data issue
  |
Step 4: Cross-Reference and Scoring
  |
  ├── Score entity using Risk Matrix above
  ├── Document all findings
  └── Decision: Proceed / Enhanced Review / Reject
```

For **French entities**, start with Societe.com (directors + shareholders) then cross-reference.
For **Austrian entities**, start with WKO (business registration + trade license).
For **Spanish entities**, start with Company Directory (NIF, officers, CNAE codes).

---

## Data Extraction - Live Registry Checks

The compliance framework above helps you structure the analysis. To actually pull live data from government registries, use the Apify actors below.

### Authentication

Set your Apify API token before running any actor:

```bash
export APIFY_TOKEN=apify_api_xxxxx
```

Sign up for a free account with $5 credits (enough for 100-1,600 checks):
https://console.apify.com/sign-up?ref=getregdata

### Actor Reference

| Check | Actor ID | Input Example | Cost/Result |
|---|---|---|---|
| Beneficial Owners (PL) | `regdata/crbr-beneficial-owners-scraper` | `{"nip": "5213103635"}` | $0.008 |
| Financial License (PL) | `regdata/knf-registry-scraper` | `{"name": "mBank"}` | $0.003 |
| Board Members (PL) | `regdata/krs-fullnames-scraper` | `{"krsNumbers": ["0000025237"]}` | $0.008 |
| Company Profile (FR) | `regdata/societe-com-scraper` | `{"sirenNumbers": ["552032534"]}` | $0.005 |
| Business Directory (AT) | `regdata/wko-business-directory-scraper` | `{"searchQuery": "Wienerberger"}` | $0.003 |
| Company Directory (ES) | `regdata/spain-company-directory-scraper` | `{"nifNumbers": ["A28015865"]}` | $0.005 |

### MCP Mode (Recommended)

If you have the Apify MCP server configured, use the MCP tools directly:

```
1. call fetch-actor-details with the actor ID to get the full input schema
2. call call-actor with the actor ID and your input to run the check
3. results are returned directly - parse and analyze inline
```

This is the fastest path - no curl commands, no dataset polling.

### API Mode (curl)

For each actor, the pattern is the same:

**Start the actor run:**
```bash
curl -X POST "https://api.apify.com/v2/acts/regdata~crbr-beneficial-owners-scraper/runs?token=$APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"nip": "5213103635"}'
```

**Poll for completion (replace RUN_ID):**
```bash
curl "https://api.apify.com/v2/actor-runs/RUN_ID?token=$APIFY_TOKEN"
```

**Retrieve results:**
```bash
curl "https://api.apify.com/v2/actor-runs/RUN_ID/dataset/items?token=$APIFY_TOKEN"
```

Replace `crbr-beneficial-owners-scraper` with the appropriate actor name and adjust the input JSON.

### Synchronous Execution (Simple Cases)

For quick single-entity checks, use the synchronous endpoint which waits for completion:

```bash
curl -X POST "https://api.apify.com/v2/acts/regdata~crbr-beneficial-owners-scraper/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"nip": "5213103635"}'
```

This returns results directly without polling - ideal for one-off checks.

---

## Output Interpretation

### CRBR - Beneficial Ownership Data

The CRBR actor returns beneficial owners as reported to the Polish Central Register of Beneficial Owners. Key fields:

- **imie / nazwisko** - First and last name of the beneficial owner
- **udzialProcentowy** - Percentage of ownership (direct and indirect)
- **rodzajUprawnienia** - Type of right: "wlasciciel" (owner), "inny" (other control)
- **dataWpisu** - Date of registration in CRBR

**How to read ownership chains:**
- If a single natural person holds >25%, they are the clear UBO
- If multiple persons hold smaller stakes, check if any has additional control rights
- If "inny" appears as the right type, investigate - this means control through means other than direct ownership (board rights, shareholder agreements, etc.)
- If the entity reports no beneficial owners, this is a red flag - every obliged entity must report at least one UBO

### KNF - Financial License Status

The KNF actor returns entries from the Polish Financial Supervision Authority's registry. Key interpretations:

- **Found with active status** - Entity is licensed and supervised. Record the license category:
  - Krajowa instytucja platnicza (domestic payment institution)
  - Instytucja pieniadza elektronicznego (e-money institution)
  - Firma pozyczkowa (lending company) - note: these are registered, not licensed
- **Found with revoked/suspended status** - Major red flag. Investigate the reason and timeline
- **Not found** - Either the entity does not require a license (most companies), or it should be licensed but is not. Cross-reference the entity's stated business activity with KNF's regulated categories

### KRS - Board Composition

The KRS Board actor extracts non-anonymized names from KRS PDF documents. This is important because the standard eKRS portal anonymizes names.

**Analysis points:**
- Cross-reference board members against the UBO list from CRBR - overlaps are expected in smaller companies
- Check for board members appearing across multiple unrelated entities (possible professional nominee)
- Verify that the board composition matches the entity's articles of association (e.g., minimum board size)
- Recent changes in board composition, especially before a large transaction, warrant further investigation

### Societe.com - French Company Profile

Returns comprehensive company data including:

- **dirigeants** - Directors and their roles
- **actionnaires** - Shareholders with ownership percentages
- **chiffre_affaires** - Revenue figures for financial health assessment
- **filiales** - Subsidiaries for group structure mapping

Cross-reference directors against the shareholder list to identify owner-managed companies vs. professionally managed entities.

### WKO - Austrian Business Directory

Returns:

- **Trade licenses held** - Verify that licenses match the stated business activity
- **Contact details** - Physical address for verification (virtual office check)
- **Chamber membership status** - Active membership is expected for legitimate Austrian businesses

### Spain Company Directory

Returns:

- **NIF verification** - Confirms entity is registered
- **Officers (apoderados, administradores)** - Named representatives and their authority types
- **CNAE codes** - Industry classification for risk assessment
- **Legal form** - SL, SA, etc. for entity type verification
- **EUID** - European Unique Identifier for cross-border verification

---

## Putting It All Together - Sample Workflow

Here is a complete KYC check for a Polish sp. z o.o. (limited liability company):

```
User: "I need to verify a Polish company before onboarding them as a supplier.
       NIP: 5213103635, KRS: 0000025237"

Step 1 - CRBR check:
  Run: regdata/crbr-beneficial-owners-scraper with {"nip": "5213103635"}
  Result: Identify all beneficial owners, ownership percentages, control types
  Analysis: Are UBOs clearly identified? Any complex structures?

Step 2 - KNF check (if entity is in financial services):
  Run: regdata/knf-registry-scraper with {"name": "Company Name"}
  Result: License status, type, any conditions or warnings
  Analysis: Does the license match the stated activity?

Step 3 - KRS Board check:
  Run: regdata/krs-fullnames-scraper with {"krsNumbers": ["0000025237"]}
  Result: Full board member names (non-anonymized)
  Analysis: Cross-reference against CRBR UBOs. Any red flags?

Step 4 - Score and decide:
  Apply the Risk Scoring Matrix
  Document findings in compliance file
  Decision: Proceed / Enhanced Review / Reject
```

Total cost for a full 3-registry Polish check: approximately $0.019 per entity.

---

## Related Skills

- **regdata-credit-risk** - Financial health assessment, insolvency monitoring (KRZ, MSiG, Ediktsdatei, eKRS, BORME). Use after KYC to assess the entity's financial stability.
- **regdata-property** - Property due diligence and ownership verification (EKW, KRS, CRBR). Use when the entity owns or is transacting real estate.
- **regdata-lead-gen** - B2B prospecting and decision-maker discovery. Not for compliance - use when building prospect lists.
- **regdata-compliance** - Consumer protection and environmental compliance (UOKiK, BDO). Use for regulatory compliance beyond KYC/AML.
