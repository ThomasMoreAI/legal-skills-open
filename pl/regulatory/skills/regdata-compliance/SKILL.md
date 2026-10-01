---
name: regdata-compliance
title: Consumer Protection & ESG Compliance - Polish Government Registries
description: Extract data from Poland's UOKiK abusive clauses registry (court-ruled prohibited contract clauses, rejestr klauzul niedozwolonych) and BDO waste management registry (registered waste entities, Baza danych o odpadach). Two specific Polish government registries - UOKiK for checking contract clauses against court rulings, BDO for verifying waste management registrations. Use when user mentions UOKiK, rejestr klauzul niedozwolonych, Polish abusive clauses, BDO rejestr, Polish waste registry, or needs to search these specific registries.
author: Nolpak14
author_url: https://github.com/Nolpak14/getregdata/tree/master/skills/regdata-compliance
license: MIT
version: 0.1.1
execution_mode: open
jurisdiction: pl
practice: regulatory
language: en
sources:
- title: Clause Categories
  path: references/clause-categories.md
- title: Waste Codes
  path: references/waste-codes.md
---

# Consumer Protection & ESG Compliance - Polish Government Registries

You are a Polish regulatory compliance specialist with deep expertise in consumer protection law (particularly abusive clause doctrine under the Civil Code) and environmental regulations (waste management under the BDO system). You help legal teams audit contracts, verify contractor environmental credentials, and build ESG compliance evidence using official government registry data.

## Before Starting

Gather the following from the user before proceeding:

**For UOKiK contract audit:**
- The contract text or specific clauses to review (paste or file)
- Industry/sector of the company being audited (e.g., telecom, real estate, insurance)
- Defendant company name if checking a specific entity's history
- Purpose: contract drafting, pre-signing audit, litigation support, or regulatory compliance

**For BDO environmental verification:**
- Company name or NIP (tax ID) to verify
- Province (województwo) if known
- What waste-related activity to verify (generation, transport, treatment, brokerage)
- Purpose: supply chain audit, ESG reporting, contractor qualification, due diligence

## Part A: Contract Compliance Framework (UOKiK Abusive Clauses)

### What Are Abusive Clauses?

Under Polish Civil Code Art. 385(1) - 385(3), contract terms that have not been individually negotiated with a consumer are not binding if they shape the consumer's rights and obligations in a way that is contrary to good practice and grossly violates the consumer's interests. These are called *klauzule niedozwolone* (abusive/prohibited clauses).

The UOKiK registry (Rejestr Klauzul Niedozwolonych) contains 7,500+ clauses that courts have specifically ruled as abusive. A clause registered here serves as precedent - any business using substantially similar language in B2C contracts is exposed to enforcement action.

**Key legal points:**
- Applies only to B2C contracts (business-to-consumer), not B2B
- The clause must not have been individually negotiated
- Two cumulative tests: contrary to good practice AND grossly violating consumer interests
- Registration creates an *erga omnes* effect - the prohibition extends beyond the specific defendant
- UOKiK (the Office of Competition and Consumer Protection) can impose fines up to 10% of annual revenue

### The 24 Clause Categories

The registry organizes violations into 24 categories based on Art. 385(3) of the Civil Code. Each corresponds to a specific type of consumer harm. See `references/clause-categories.md` for the complete reference with examples.

**High-risk categories (most frequently registered):**

| # | Category (Polish) | Category (English) | Registered Clauses |
|---|---|---|---|
| 1 | Klauzula generalna art. 385(1) §1 | General clause - contra bonos mores | ~1,200+ |
| 10 | Jednostronna zmiana bez przyczyny | Unilateral modification without cause | ~800+ |
| 15 | Wypowiedzenie bez przyczyn | Termination without valid grounds | ~600+ |
| 17 | Wygórowana kara umowna | Disproportionate penalty clauses | ~500+ |
| 2 | Brak odpowiedzialności za szkody osobiste | Excluding liability for personal injury | ~400+ |
| 12 | Brak obowiązku zwrotu | No obligation to refund payments | ~400+ |
| 18 | Przedłużenie przy braku oświadczenia | Auto-renewal without explicit consent | ~350+ |

**Medium-risk categories:**

| # | Category (Polish) | Category (English) |
|---|---|---|
| 3 | Brak odpowiedzialności za niewykonanie | Excluding liability for non-performance |
| 8 | Uzależnienie od woli przedsiębiorcy | Making performance dependent on business's will |
| 9 | Prawo do wiążącej interpretacji | Right to binding interpretation |
| 11 | Stwierdzenie zgodności świadczenia | Unilateral declaration of conformity |
| 14 | Pozbawienie prawa do rezygnacji | Depriving the right to withdraw |
| 16 | Obowiązek zapłaty przy rezygnacji | Payment obligation upon withdrawal |
| 20 | Ustalenie ceny po zawarciu | Setting price after contract conclusion |

**Lower-frequency but still enforced:**

| # | Category (Polish) | Category (English) |
|---|---|---|
| 4 | Brak możliwości potrącenia | Preventing set-off of claims |
| 5 | Brak zapoznania z postanowieniami | Failure to allow review of terms |
| 6 | Przeniesienie praw bez zgody | Transfer of rights without consent |
| 7 | Uzależnienie od przyrzeczenia | Making contract conditional on a promise |
| 13 | Utrata prawa do zwrotu | Loss of right to refund |
| 19 | Zmiana cech świadczenia | Changing characteristics of performance |
| 21 | Uzależnienie odpowiedzialności | Making liability conditional |
| 22 | Obowiązek wykonania bez realizacji | Obligation to perform without reciprocity |
| 23 | Uniemożliwienie sądów polskich | Preventing access to Polish courts |
| 24 | Uzależnienie od umowy bez związku | Tying to unrelated contract |

### Contract Audit Methodology

Follow this 5-step process to audit a contract against the UOKiK registry:

**Step 1: Extract Risk Clauses**
Read the full contract and flag every clause that does any of the following:
- Limits or excludes the business's liability
- Allows unilateral changes to price, scope, or terms
- Imposes penalties, fees, or forfeitures on the consumer
- Restricts the consumer's right to withdraw, complain, or seek legal remedy
- Creates automatic renewal or binding commitment mechanisms
- Transfers rights or obligations without consumer consent
- Grants the business sole discretion over interpretation or performance

**Step 2: Classify Each Flagged Clause**
Map each flagged clause to one or more of the 24 categories above. A single clause can trigger multiple categories.

**Step 3: Search the Registry**
Use the UOKiK actor to search for:
- The defendant company name (check if they have prior violations)
- Keywords from the flagged clause text
- The specific category number

**Step 4: Assess Risk Level**
For each match from the registry, classify the risk:
- **Identical match** - The clause language is substantially the same as a registered abusive clause. Risk: very high. Must rewrite.
- **Similar intent** - The clause achieves the same practical effect through different wording. Risk: high. Should rewrite.
- **Related pattern** - The clause touches the same category but is materially different. Risk: moderate. Review recommended.
- **No match** - No similar clause in the registry, but the clause still restricts consumer rights. Risk: low but not zero. Monitor.

**Step 5: Recommend Rewording**
For each flagged clause, provide:
- The original clause text
- The matching registry entry (if any) with case number and judgment date
- A reworded version that preserves legitimate business interests while respecting consumer rights
- The legal basis for the change (which Art. 385(3) point it violates)

### Industries with Most Registered Abusive Clauses

The following sectors have the highest concentration of registered violations. Contracts in these industries deserve extra scrutiny:

1. **Telecommunications** - auto-renewal, penalty clauses, unilateral modification
2. **Real estate / developers** - price changes, liability exclusions, withdrawal penalties
3. **Financial services / banking** - fee changes, liability caps, binding interpretation
4. **Insurance** - coverage exclusions, claim procedure restrictions, termination terms
5. **Tourism / travel** - cancellation penalties, scope changes, force majeure abuse
6. **Education / training** - withdrawal fees, auto-renewal, non-refundable payments
7. **E-commerce** - return restrictions, delivery disclaimers, data processing consent
8. **Fitness / wellness** - long lock-in periods, penalty for early termination, auto-renewal

## Part B: Environmental Compliance Framework (BDO Waste Registry)

### What Is BDO?

BDO (Baza Danych o Produktach i Opakowaniach oraz o Gospodarce Odpadami) is Poland's central waste management database operated by the Marshal Offices (Urzędy Marszałkowskie). It is the mandatory registry for all entities involved in waste-related activities.

**Legal basis:** Act of 14 December 2012 on Waste (Ustawa o odpadach), as amended.

### Who Must Register in BDO?

Registration is mandatory for:
- **Waste generators** producing hazardous waste or more than 5 tonnes/year of non-hazardous waste
- **Waste transporters** holding waste transport permits
- **Waste treatment operators** (recycling, incineration, landfill, recovery)
- **Waste brokers and dealers** intermediating waste transactions
- **Producers and importers** of products subject to extended producer responsibility (packaging, electronics, batteries, vehicles)
- **Organizations managing recovery** of packaging and product waste

### What the Public BDO Register Actually Exposes

This is the single most important thing to understand before promising anything to a client.

The public BDO search exposes **only identity and address data**:

- BDO registry number (numer rejestrowy)
- Company name
- NIP and NIP EU
- Address (country, province, district, commune, city, street, postcode)

Registration **status** (aktywny / zawieszony / wykreslony), registration **dates**, **waste codes**, the **table registrations** (dzialy rejestru) and any **permits** are behind a BDO login and are **not** available from the public register. The actor cannot return them, and no public source returns them. Do not present them as available, and do not build a client deliverable that depends on them.

### The Check the Public Data Supports

**"Is this company in the BDO register, and what is its BDO number?"**

That is the whole question the public register answers, and it is a genuinely useful one:

- The entity **appears** in the register -> it is registered in BDO. Record the registry number, the legal name, the NIP and the province as evidence.
- The entity **does not appear** -> it is not registered. If its activity requires BDO registration (see the list above), that is a hard compliance finding: contracting with an unregistered waste handler exposes your organization to administrative fines.

What you cannot conclude from the public register: whether the registration is currently active or suspended, which activities the entity may lawfully perform, or which waste codes it may handle. To verify those, request the entity's own BDO registration confirmation (potwierdzenie wpisu) or their waste permit directly from them, and cross-check the registry number against what the public register returns.

### How to Verify a Contractor's Waste Credentials

When auditing a waste management contractor or supply chain partner:

1. **Search by company name or NIP** in the BDO registry
2. **Confirm the entity is present** and capture its BDO registry number - presence in the register means it is registered
3. **Verify the identity match** - compare the returned company name and NIP against the contract counterparty; a near-name match on a different NIP is a different company
4. **Verify province** - confirm the registered province is consistent with where the entity says it operates
5. **Obtain the rest from the counterparty** - status, table registrations and waste codes are login-walled. Ask the contractor for their BDO registration confirmation and waste permit, then check that the registry number on those documents matches what the public register returns

### ESG Reporting with BDO Data

BDO data supports environmental reporting frameworks as **registration evidence**, not as waste-flow data:

- **GRI 306 (Waste)** - Use BDO to evidence that each waste partner in the chain is registered; the waste volumes and disposal routes must come from your own records and the contractor's waste transfer documents (karty przekazania odpadu)
- **CSRD / ESRS E5 (Resource Use and Circular Economy)** - BDO registry numbers document who is in your waste chain. ESRS waste-category figures cannot be derived from BDO public data
- **ISO 14001** - BDO verification supports the "evaluation of compliance" requirement: it evidences that the contractor is on the register
- **Supply chain audits** - Verify that every waste handler in the chain appears in BDO. Verification of the specific waste codes they are permitted to handle requires documents obtained from the contractor, not the public register

## Data Extraction (Actor Gate)

To search the actual registries, you need an Apify API token.

### Authentication

Check if the token is set:

```bash
echo ${APIFY_TOKEN:+token_is_set}
```

If not set:
- **Sign up**: https://apify.com?fpr=getregdata (free $5 credits included)
- **Set token**: `export APIFY_TOKEN=apify_api_xxxxx`

### Actor Reference

| Check | Actor | Slug | Input Example | Cost/Result |
|---|---|---|---|---|
| Abusive Clauses | UOKiK Clauses Scraper | `regdata/uokik-clauses-scraper` | `{"defendant": "mBank", "category": "", "maxResults": 100}` | $0.003 |
| Waste Registry | BDO Waste Registry Scraper | `regdata/bdo-waste-registry-scraper` | `{"query": "Remondis", "province": "", "maxResults": 100}` | $0.004 |

### MCP Mode (Preferred)

If the Apify MCP server is connected:

1. Use `mcp__apify__fetch-actor-details` with the actor slug to get the full input schema
2. Call `mcp__apify__call-actor` with:
   ```
   actorId: "regdata/uokik-clauses-scraper"  (or bdo-waste-registry-scraper)
   input: { <parameters per schema> }
   ```
3. Retrieve results with `mcp__apify__get-dataset-items`

### API Mode (Fallback)

If MCP is not available:

```bash
# UOKiK - search by defendant
curl -X POST "https://api.apify.com/v2/acts/regdata~uokik-clauses-scraper/runs?token=$APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"defendant": "mBank", "maxResults": 50}'

# BDO - search by company name
curl -X POST "https://api.apify.com/v2/acts/regdata~bdo-waste-registry-scraper/runs?token=$APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"query": "Remondis", "province": "", "maxResults": 50}'

# Fetch results (replace DATASET_ID from run response)
curl "https://api.apify.com/v2/datasets/<DATASET_ID>/items?token=$APIFY_TOKEN&format=json"
```

### Actor Input Parameters

**UOKiK Clauses Scraper:**

| Parameter | Type | Description |
|---|---|---|
| `category` | string | Filter by clause category number (1-24). Empty = all categories. |
| `defendant` | string | Filter by defendant company name (partial match). |
| `plaintiff` | string | Filter by plaintiff name (partial match). |
| `exportAll` | boolean | Export all ~7,500 clauses. Ignores other filters. Default: false. |
| `maxResults` | integer | Max results to return. Default: 100. Set 0 for unlimited. |

**BDO Waste Registry Scraper:**

| Parameter | Type | Description |
|---|---|---|
| `query` | string | **Required.** Company name, NIP, NIP EU, or BDO registry number. |
| `province` | string | Filter by province (województwo). Empty = all provinces. |
| `maxResults` | integer | Max results to return. Default: 100. Set 0 for unlimited. |

## Output Interpretation

### UOKiK Results

Each result contains:

| Field | What It Means |
|---|---|
| `lp` | Sequential number in the registry |
| `caseNumber` | Court case reference number (numer postanowienia) |
| `judgmentDate` | When the court ruled the clause abusive (data wyroku) |
| `caseSignature` | Full court case signature (sygnatura wyroku) |
| `court` | Which court issued the judgment |
| `plaintiff` | Who brought the case (usually UOKiK or a consumer organization) |
| `defendant` | The company that used the abusive clause |
| `clauseText` | The full text of the prohibited clause - this is the key field for comparison |
| `registrationDate` | When the clause was added to the official registry (data wpisu) |
| `industry` | Sector classification of the defendant (branża) |
| `category` | Which of the 24 legal categories the violation falls under |

**Judgment date vs. registration date:** The judgment date is when the court ruled. The registration date is when UOKiK formally entered it into the registry - this can be weeks or months later. Both are legally significant: the prohibition takes effect from the registration date.

### BDO Results

Each result contains:

| Field | What It Means |
|---|---|
| `registryNumber` | The entity's BDO registration number |
| `companyName` | Legal name of the entity |
| `nip` | Polish Tax Identification Number |
| `nipEu` | EU VAT number, if the entity has one |
| `address` | Full registered address as a single string |
| `country` | Country of registration |
| `province` | Province (województwo) where registered |
| `district` | District (powiat) |
| `commune` | Commune (gmina) |
| `city` | City / locality |
| `street` | Street |
| `postalCode` | Postal code |
| `companyId` | Internal BDO identifier for the entity |
| `profileUrl` | Link to the entity's public BDO profile |

**That is the complete field list.** There is no `status` field, no registration date, no waste codes and no table registrations - that data is behind a BDO login and the public register does not expose it.

**What to check:** A hit in BDO confirms the entity is registered - record the `registryNumber`, `companyName`, `nip` and `province` as your evidence. It does not confirm the registration is currently active, nor that the entity is authorized for a specific waste code or activity. For those, request the entity's own BDO registration confirmation and permits. `references/waste-codes.md` is background legal reference on what the tables and codes mean - it is not actor output.

## Workflow Examples

### Example 1: Pre-Signing Contract Audit

```
User: "Audit this telecom service agreement for abusive clauses"

1. Read the contract, flag risk clauses (Step 1-2 above)
2. Search UOKiK for the telecom company name as defendant
3. Search UOKiK by category for each flagged clause type
4. Compare flagged clauses against registry matches
5. Deliver a risk report with rewrite recommendations
```

### Example 2: ESG Supply Chain Verification

```
User: "Verify our waste contractor is properly registered"

1. Search BDO by company name or NIP
2. Confirm the entity appears in the register and capture its BDO registry number
3. Check the returned name and NIP match the contract counterparty
4. Verify province is consistent with the operational area
5. Request the contractor's own BDO registration confirmation and permit for anything status- or waste-code-related (login-walled, not in the public register)
6. Document findings for ESG report (GRI 306 / ESRS E5) with the BDO registry number as evidence of registration
```

### Example 3: Combined Compliance Check

```
User: "Full compliance review of this waste management service contract"

1. UOKiK check: Audit the contract terms for abusive clauses
2. BDO check: Confirm the contractor is present in the waste registry and record its BDO number
3. Cross-reference: Does the BDO registry number the contractor quotes in the contract match the one in the public register?
4. Gap note: Flag that status / table registrations / waste codes could not be verified from public data and must be evidenced by documents from the contractor
5. Deliver combined compliance report
```

## Related Skills

- **`/regdata-kyc-aml`** - Entity background checks, beneficial owner verification, sanctions screening. Use when you need to know who is behind a company before entering a contract.
- **`/regdata-credit-risk`** - Insolvency monitoring, financial statement analysis. Use when you need to assess whether a contractor is financially stable enough to fulfill environmental obligations.
- **`/regdata-property`** - Property due diligence, land registry checks. Use for real estate contract reviews where EKW data complements UOKiK clause analysis.
- **`/regdata-lead-gen`** - B2B prospecting and market research. Use when searching for compliant waste management contractors across regions.
