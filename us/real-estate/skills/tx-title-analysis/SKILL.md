---
name: tx-title-analysis
title: Texas Title Analysis Skill
description: 'Texas title examination for residential and commercial real estate. Analyzes commitments, recorded instruments, surveys, HOA docs, and searches. Outputs DRAFT title opinion letters, requirements checklists, and exception cures for attorney review.


  TRIGGERS: Title commitment uploads, title report analysis, Schedule B exceptions, title opinion requests, Texas homestead/community property/mineral questions, clearing title for closing, title insurance documents.


  Use this skill whenever someone uploads a title commitment PDF, asks about Schedule B exceptions, wants a title opinion drafted, asks about Texas homestead or community property rules, needs help clearing title for a closing, or asks questions like "what does exception #3 mean?" or "I just got a commitment from [title company], can you look at it?" or "review this title package." Also trigger on any mention of Texas title insurance forms (T-1, T-7, T-19, T-47), lender endorsements, or clearing title requirements.


  COVERS: Residential, commercial, minerals/royalties, TX title forms (T-1, T-7, T-19), lender endorsements.'
author: bstevescherer
author_url: https://github.com/bstevescherer/heycounsel-community/tree/main/skills/tx-title-analysis
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: real-estate
language: en
---

# Texas Title Analysis Skill

> ⚠️ **IMPORTANT DISCLAIMER**
>
> **THIS TOOL DOES NOT PROVIDE LEGAL ADVICE.** All outputs are provided for informational purposes only and are intended as **FIRST DRAFTS** requiring review, verification, and approval by a licensed Texas attorney before use or reliance.
>
> - All outputs are preliminary drafts, not final work product
> - This tool is a drafting assistant, not a substitute for legal counsel
> - A licensed attorney must review all outputs before any reliance
> - No attorney-client relationship is created by use of this tool
> - Laws and regulations change; verify all citations and requirements

Analyze title documents to generate DRAFT outputs that assist attorneys in their title examination work. All analysis should be thorough and well-documented to facilitate attorney review.

**Primary Authority**: This skill follows the **Texas Title Examination Standards** (Vernon's Texas Statutes and Codes Annotated, Title 2—Appendix) as the authoritative reference for Texas title examination. See `references/tx-exam-standards.md` for the complete standards reference.

---

## How to Think About Title Analysis

Title examination is detective work — you're reconstructing a property's ownership history and identifying anything that could prevent a clean transfer. Every document tells part of the story, and your job is to find where the story doesn't add up.

When you find an issue, always think about it from three angles:
1. **What is it?** — Classify the issue precisely (lien, exception, chain gap, etc.)
2. **How bad is it?** — Use the Severity Framework below to prioritize
3. **What fixes it?** — Identify specific cure steps, responsible parties, and timeline

The goal is a work product that saves the reviewing attorney time — not by being perfect, but by being organized, thorough, and honest about what you're uncertain about.

---

## Severity Framework

Classify every finding using this framework. This is critical for residential transactions where not everything is equally urgent.

### 🔴 CRITICAL — Must resolve before closing
- Unreleased deeds of trust / mortgages (active liens on property)
- Breaks in the chain of title (missing links in ownership)
- Homestead violations (missing spousal joinder on conveyance)
- Active judgment liens or federal tax liens against current owner
- Failed legal description (doesn't describe the property)
- Title vested in deceased person without probate

### 🟡 IMPORTANT — Should resolve, may delay closing
- Name discrepancies without supporting affidavits
- Expired but unreleased liens (need release or affidavit)
- Missing HOA resale certificate or estoppel
- Survey exceptions that could be deleted with T-19
- Community property questions without marital status affidavit
- Mechanic's lien exposure (recent improvements without waivers)

### 🟢 INFORMATIONAL — Note for attorney, unlikely to block closing
- Standard printed exceptions (taxes not yet due, etc.)
- Utility easements along property boundaries (typical)
- Deed restrictions/CCRs (standard subdivision restrictions)
- Mineral reservations (common in Texas, usually don't affect residential closing)
- Access easements benefiting the property

Always lead with Critical findings. An attorney scanning your output should see the dealbreakers first.

---

## Handling Scanned / Image-Only Documents

Title packages are frequently scanned PDFs with no extractable text. When you encounter image-only pages:

1. **Examine each page visually** — read the document as you would a photograph
2. **Identify the document type first** — look for headers, formatting, and form numbers (e.g., "Commitment for Title Insurance," "General Warranty Deed," "Deed of Trust")
3. **Extract key data points** — recording info, names, dates, legal descriptions, amounts
4. **Note legibility issues** — if a page is blurry, cropped, or partially illegible, say so explicitly rather than guessing
5. **Flag missing pages** — scanned packages often have missing or out-of-order pages

If you cannot read critical information from a scanned page, flag it as: "⚠️ Unable to read [specific information] on page [X] — manual review required."

---

## Title Analysis Workflow

1. **Identify Documents** → Catalog all uploaded documents by type
2. **Parse Commitment** → Extract Schedule A (coverage) and Schedule B (exceptions/requirements)
3. **Analyze Chain of Title** → Review vesting, conveyances, and gaps
4. **Examine Exceptions** → Classify and assess each Schedule B exception
5. **Transaction Type & Texas-Specific Review**:
   - **5A**: Commercial RE → Entity authority, ALTA survey, environmental, UCC, leases, endorsements
   - **5B**: Manufactured Housing → SOL, TDHCA, personal-to-real conversion
   - **5C**: All transactions → Homestead, community property, minerals, water rights
6. **Cross-Reference Check** → Loop back through steps looking for contradictions
7. **Generate Outputs** → Title opinion, requirements checklist, cure recommendations

---

## Step 1: Document Identification

Catalog uploaded documents into these categories:

| Category | Documents |
|----------|-----------|
| **Commitment** | Commitment for Title Insurance, Preliminary Title Report |
| **Recorded Instruments** | Deeds, deeds of trust, liens, releases, easements, plats, restrictions |
| **Survey** | Survey, plat, metes and bounds description |
| **Tax/Assessment** | Tax certificate, tax statement, special assessment info |
| **HOA/Restrictions** | HOA docs, CCRs, bylaws, resale certificate |
| **Searches** | Judgment search, bankruptcy search, UCC search, federal tax lien search |
| **Other** | Affidavits, death certificates, divorce decrees, probate documents |

If key documents are missing, note them in the Requirements Checklist.

---

## Step 2: Parse the Commitment

Extract and organize:

### Schedule A (Coverage)
- Effective date
- Proposed insured (owner and/or lender)
- Policy amounts
- Legal description
- Current vesting (who owns the property now)

### Schedule B-I (Requirements)
Number and list each requirement. Common Texas requirements:
- Payment of current taxes
- Release of existing liens
- Execution of deed/deed of trust
- HOA resale certificate
- Survey or affidavit
- Proof of entity authority (for LLCs, corporations)
- Marital status affidavit
- Heirship affidavit

### Schedule B-II (Exceptions)
Number and list each exception. Categorize as:
- **Standard Exceptions** (deletable with proper documentation)
- **Special Exceptions** (property-specific, require individual analysis)

---

## Step 3: Chain of Title Analysis

Review recorded instruments to verify continuous, valid ownership. Think through the chain like this:

### The Reasoning Process

For each link in the chain, ask these questions in order:

1. **Who is the grantor?** Does this person/entity match the grantee from the previous conveyance? Check for exact name match, and if not exact, determine whether it's the same person (married name change, nickname, middle name variation, suffix added/dropped).

2. **What type of conveyance?** General warranty deed provides the strongest title protection. Special warranty deed limits warranties to grantor's period of ownership. Quitclaim deeds are a yellow flag — they may indicate a title dispute or an attempt to cure a defect. Note the type and what it means for the chain.

3. **Was it properly executed?** Check for: grantor signature, notarization, and evidence of delivery (recording). In Texas, a deed must be signed by the grantor but need not be signed by the grantee.

4. **Are there outstanding interests?** Look for unreleased liens (deeds of trust, judgment liens, mechanic's liens). A lien recorded against the property that has no corresponding release is a red flag until accounted for.

### Common Residential Chain Patterns

These patterns show up constantly in residential title work — be ready for them:

**Multiple refinances leaving unreleased liens**: A homeowner who has refinanced 2-4 times may have old deeds of trust that were paid off but never formally released. Look for: the new lender's deed of trust recorded close in time to the old one, suggesting a payoff. Flag the unreleased ones but note the likely payoff if the timeline supports it. Severity: 🟡 IMPORTANT (need releases or affidavits).

**Married couple where only one spouse is on title**: Very common. If the property was acquired during the marriage, it's presumptively community property regardless of whose name is on the deed. Both spouses must sign any conveyance. Check: acquisition date vs. marriage, whether spouse's joinder appears on subsequent conveyances. Severity: 🔴 CRITICAL if joinder is missing on the conveyance in question.

**Transfers between spouses (divorce)**: Look for divorce decrees that awarded the property to one spouse, followed by a deed. The decree alone doesn't transfer title in Texas — a deed is needed. Also check: was the deed of trust in both names? Does the assuming spouse qualify? Severity: 🔴 CRITICAL if deed not recorded after decree.

**Inherited property with informal heirship**: Property may pass by heirship affidavit rather than formal probate. Check: was the affidavit properly recorded? Does it identify all heirs? Is there a self-proving affidavit or court determination? Informally passed property is the #1 source of residential chain-of-title problems. See `references/tx-probate.md`. Severity: 🔴 CRITICAL if heirship affidavit is missing or incomplete.

**Property in trust**: Check for recorded trust agreement or memorandum of trust. Verify the trustee has authority to convey. See `references/tx-entities.md`. Severity: 🟡 IMPORTANT.

### Red Flags
- Gaps in chain exceeding 25 years (Texas marketable title period)
- Deeds from estates without proper probate
- Quitclaim deeds in the chain (may indicate title dispute)
- Unreleased vendor's liens or deeds of trust
- Name variations without supporting affidavits

---

## Step 4: Exception Analysis

For each Schedule B-II exception, work through this reasoning chain:

### Step-by-Step Exception Analysis

**First**: What type of exception is this?
- Standard/pre-printed exception → Usually deletable with documentation
- Specific recorded instrument → Need to assess the actual document
- General exception (e.g., "rights of parties in possession") → May be deletable

**Second**: Does it actually affect this property?
- Check the legal description in the exception against the subject property
- An easement across Lot 6 doesn't affect Lot 5
- A restriction on Block 2 does affect all lots in Block 2

**Third**: How does it impact use, value, or marketability?
- Utility easement along rear property line → minimal impact on typical residential use
- Access easement across the middle of the lot → significant impact
- Building setback restriction → depends on whether structures comply

**Fourth**: Can it be cured, and if so how?
- Release from the beneficiary
- Expiration by operation of law
- Insurance over (title company agrees to insure despite exception)
- Remains as exception to policy (buyer accepts it)

**Fifth**: Apply the Severity Framework (🔴 / 🟡 / 🟢) and note the classification.

### Exception Classification Quick Reference

| Type | Description | Typical Treatment |
|------|-------------|-------------------|
| **Standard/Pre-printed** | Taxes, survey matters, rights of parties in possession | Often deletable with documentation |
| **Deed Restrictions/CCRs** | Use restrictions, architectural controls | Usually remain; review for enforceability |
| **Easements** | Utility, access, drainage | Remain unless released; assess impact |
| **Mineral Reservations** | Oil, gas, mineral rights | See `references/tx-minerals.md` |
| **Liens/Encumbrances** | Deeds of trust, judgment liens, mechanic's liens | Must be released or subordinated |
| **HOA/POA** | Assessments, maintenance obligations | Review for delinquencies |

See `references/tx-exceptions.md` for comprehensive exception analysis guidance.

---

## Step 5: Transaction Type Detection

Before proceeding with Texas-specific analysis, identify the transaction type and run the applicable sub-workflow:

**IF commercial property** (office, retail, industrial, multifamily 5+, mixed-use, land for development) → Run **Step 5A** below
**IF manufactured housing on the property** → Run **Step 5B** below
**IF residential** (SFR, condo, townhome, 1-4 family) → Skip to **Step 5C** below

### Step 5A: Commercial Real Estate Workflow

See `references/tx-commercial.md` for complete guidance.

**Additional analysis required for commercial transactions**:

1. **Entity authority**: Verify all signing entities are authorized. Check articles, certificates of good standing, operating agreements, resolutions. See `references/tx-entities.md`
2. **ALTA/NSPS survey review**: Require current ALTA/NSPS survey with applicable Table A items. Cross-reference survey exceptions against commitment. See `references/tx-survey.md`
3. **Environmental due diligence**: Confirm Phase I ESA completed. Flag Recognized Environmental Conditions (RECs). Note CERCLA/TCEQ implications
4. **UCC search**: Review fixture filings; require UCC-3 terminations for releases
5. **Lease analysis**: For tenanted properties, review lease abstracts for title impact. Identify required SNDA agreements and tenant estoppel certificates
6. **Commercial endorsements**: Determine required endorsement package (T-1, T-2, T-19 with Table A, T-23/T-23.1, T-15/T-16, T-30, T-36, T-44 as applicable)
7. **Lien analysis**: Enhanced lien review including mechanic's liens on commercial projects (retainage, trapped funds). See `references/tx-liens.md`
8. **1031 exchange**: If applicable, verify exchange accommodator structure and timing requirements
9. **Zoning**: Note zoning classification and any pending changes
10. **Condemnation**: Check for pending or completed condemnation actions, especially pipeline/utility easements. See `references/tx-condemnation.md`

### Step 5B: Manufactured Housing Workflow

See `references/tx-manufactured-housing.md` for complete guidance.

**Analysis required for manufactured housing**:

1. **Classification check**: Determine if home is currently personal property or real property
2. **Statement of Location (SOL)**: Verify SOL filed with TDHCA AND recorded in county real property records
3. **Document of title**: Confirm TDHCA document of title has been surrendered/cancelled
4. **Election to treat as real property**: Verify proper election recorded
5. **Owner match**: Confirm owner of manufactured home = owner of land (or has qualifying leasehold)
6. **HUD labels**: Verify HUD certification labels present (serial numbers match)
7. **Lien check**: Check for liens on personal property title that weren't released before conversion
8. **Gap analysis**: If home is on land but NOT properly converted, flag as **critical title defect** — real property deed and deed of trust do NOT cover the home
9. **Title insurance**: Confirm title policy will cover the manufactured home as real property (requires proper conversion)

### Step 5C: Texas-Specific Analysis

### Homestead (Tex. Prop. Code §§ 41.001-41.005)

**Urban homestead**: Up to 10 acres (family) in city, town, or village
**Rural homestead**: Up to 100 acres (single adult) or 200 acres (family)

**Reasoning process for homestead analysis**:
1. Is the property likely a homestead? Look for: owner-occupied residence, family home, homestead exemption filed with tax authority
2. If homestead, are both spouses signing the current conveyance? This is required even if only one spouse is on title (Tex. Const. Art. XVI, § 50)
3. Check the liens against the property — only certain liens are valid against homestead: purchase money, taxes, home improvement (with specific requirements), home equity (with constitutional protections), refinance of existing valid lien
4. If there's a home equity loan: verify compliance with Tex. Const. Art. XVI, § 50(a)(6) — 80% LTV cap, 12-day cooling period, etc.

**If you can't determine homestead status**: Flag it explicitly. "⚠️ Homestead status undetermined — if this property is the owner's homestead, spousal joinder is required on all conveyances and lien restrictions apply. Recommend marital status affidavit." Severity: 🟡 IMPORTANT until resolved.

### Community Property (Tex. Fam. Code § 3.002)

**Presumption**: Property acquired during marriage is community property.

**Reasoning process**:
1. When was the property acquired? (Check deed date)
2. Was the owner married at that time? (Check marital status if known)
3. If acquired during marriage → presumptively community property → both spouses must join in conveyance
4. If claimed as separate property → need tracing evidence (gift, inheritance, pre-marriage acquisition, or partition agreement)
5. If marital status is unknown → flag it and recommend marital status affidavit

### Minerals and Royalties

See `references/tx-minerals.md` for detailed analysis.

**Key points**:
- Texas follows "ownership in place" theory
- Surface estate may be severed from mineral estate
- Dominant mineral estate doctrine
- Check for existing leases, royalty interests, executive rights, NPRIs

**For residential transactions**: Mineral reservations are extremely common in Texas and usually don't affect the residential closing. Note them, classify as 🟢 INFORMATIONAL unless the reservation includes unusual surface access rights or the buyer has specifically asked about minerals.

### Water Rights

See `references/tx-water-rights.md` for detailed analysis.

**Key points**:
- Texas has a **dual water system**: state-owned surface water vs. privately-owned groundwater
- Surface water: Prior appropriation system (permit required from TCEQ)
- Groundwater: Rule of capture (owner owns in place; *Edwards Aquifer Auth. v. Day*)
- Groundwater rights are severable — check chain for reservations
- Properties in GCDs subject to local district rules and permits
- Review for water rights conveyances, reservations, or severances

---

## Step 6: Cross-Reference Check

Before generating outputs, loop back through your analysis and look for contradictions or items you may have missed. This is where real examiners catch the issues that a linear first pass misses.

**Chain ↔ Exceptions**: Does the chain of title analysis reveal any liens or interests that should appear as exceptions but don't? Conversely, do any exceptions reference instruments you didn't see in the chain?

**Survey ↔ Exceptions**: If a survey is available, do the physical conditions shown match the exceptions? An easement exception should correspond to something on the survey. A survey showing an encroachment should generate an exception.

**Homestead ↔ Liens**: If the property is or may be homestead, re-examine every lien against the homestead lien restrictions. A home equity loan that doesn't comply with Tex. Const. Art. XVI, § 50(a)(6) is void.

**Names ↔ Everything**: Do all the names used across all documents consistently refer to the same parties? A judgment lien against "John A. Smith" may or may not affect "John Smith" depending on additional identifying information.

**Dates ↔ Timeline**: Do the dates make sense? A deed of trust recorded before the deed it's supposed to secure is a problem. A release recorded before the lien it's supposed to release is suspicious.

If you find contradictions, note them clearly in your output with the ⚠️ flag and recommend specific investigation steps.

---

## Step 7: Generate DRAFT Outputs

**CRITICAL**: All outputs must include the following header disclaimer:

```
**DRAFT - FOR ATTORNEY REVIEW**
This document is a preliminary draft prepared for informational purposes only.
It does not constitute legal advice and must be reviewed, verified, and approved
by a licensed Texas attorney before any use or reliance.
```

### Choose Output Mode

Before generating, determine which output mode fits the request:

**Quick Analysis Summary** (default for most residential): A concise, structured analysis organized by severity. Leads with Critical findings, then Important, then Informational. Includes a requirements checklist at the end. Best for: standard residential transactions, quick turnaround, initial review before deeper dive.

**Full Opinion Letter**: Formal title opinion letter with all sections per `references/tx-opinion-template.md`. Best for: complex transactions, attorney work product, situations where the user specifically requests a formal opinion.

If the user doesn't specify, default to Quick Analysis Summary for residential and Full Opinion Letter for commercial.

### Output 1: DRAFT Title Opinion Letter (or Quick Analysis Summary)

**For Quick Analysis Summary**, structure as:

1. **DRAFT DISCLAIMER** (required)
2. **Property Summary** — Address, legal description, current vesting, commitment info
3. **🔴 Critical Findings** — Anything that must be resolved before closing, with specific cure steps
4. **🟡 Important Findings** — Items that should be addressed, with recommended actions
5. **🟢 Informational Notes** — Standard items, mineral reservations, routine exceptions
6. **Requirements Checklist** — Organized action items with responsible party and status
7. **Exceptions Summary** — Brief table of all exceptions with classification and treatment
8. **Limitations** — What wasn't reviewed, what couldn't be determined

**For Full Opinion Letter**, use the docx skill to generate formal opinion. See `references/tx-opinion-template.md` for structure.

Key sections:
1. **DRAFT DISCLAIMER** (required at top of document)
2. Purpose and scope
3. Documents examined (with recording info)
4. Legal description
5. Chain of title summary
6. Current vesting
7. Requirements for clear title
8. Exception analysis with recommendations
9. Texas-specific matters (homestead, community property, minerals)
10. Opinion statement (marked as DRAFT pending attorney review)
11. Qualifications and limitations

### Output 2: DRAFT Requirements Checklist

Generate actionable checklist organized by:
- **Must Clear Before Closing** (deal-breakers) — 🔴 items
- **Documents Needed** (source and status) — 🟡 items
- **Payoffs Required** (lienholder and estimated amounts)
- **Affidavits/Certifications** (who signs, purpose)
- **HOA Items** (resale cert, assessment status)
- **Tax Items** (current/prior years, special assessments)
- **Remaining Exceptions** (items that cannot be cleared) — 🟢 items

Include disclaimer: *"This checklist is a draft for attorney review. Verify all items and requirements before reliance."*

### Output 3: DRAFT Exception Cure Recommendations

For each curable exception, provide:
- Issue description
- Severity classification (🔴 / 🟡 / 🟢)
- Specific cure steps
- Documents needed
- Responsible party (Seller/Buyer/Lender)
- Timeline estimate

Include disclaimer: *"Cure recommendations are preliminary and must be verified by a licensed attorney."*

---

## When Information Is Missing or Ambiguous

Title packages are frequently incomplete. When you encounter gaps:

1. **Don't guess.** If you can't determine something from the documents provided, say so explicitly.
2. **Flag it with a specific question.** Instead of "additional information needed," say "⚠️ The deed from Smith to Jones (Doc. No. 2019-12345) references a prior deed of trust that is not included in this package. Was this lien released? If so, please provide the release document."
3. **State your assumption and its risk.** If you need to proceed despite missing information, say: "Assuming [X] based on [Y]. If this assumption is incorrect, [consequence]."
4. **Classify the uncertainty.** A missing release for a $500K deed of trust is 🔴 CRITICAL. A missing HOA resale certificate is 🟡 IMPORTANT. A missing copy of standard subdivision restrictions is 🟢 INFORMATIONAL.

---

## When to Cite Standards

Cite Texas Title Examination Standards when they add value — not on every routine observation. Good citation practice:

**Do cite** when:
- There's a genuine title issue and the standard provides the analysis framework
- The standard resolves an ambiguity (e.g., Standard 15.90 on Texas's notice recording system)
- Homestead or community property questions arise (Standards 5.10-5.50, 6.10-6.70)
- Adverse possession or limitations issues (Standards 18.10-18.60)

**Don't cite** for:
- Routine observations ("the deed was properly recorded" doesn't need a standard citation)
- Standard exceptions that don't raise issues
- General statements about Texas law that aren't controversial

### Key Standards Quick Reference
- **Marketable Title**: Standard 2.10
- **Recording/Notice**: Standard 15.90 (Texas has a NOTICE system, not race-notice)
- **Judgment Liens**: Standards 15.40-15.60
- **Mechanic's Liens**: Standards 15.70-15.80
- **Homestead**: Standards 6.10-6.70
- **Community Property**: Standards 5.10-5.50
- **Adverse Possession**: Standards 18.10-18.60
- **Chain of Title**: Standards 3.10-3.50

---

## Reference Files

Load these as needed for detailed guidance:

### Primary Authority
- `references/tx-exam-standards.md` - **Texas Title Examination Standards** (Vernon's Texas Statutes and Codes Annotated, Title 2—Appendix). This is the authoritative reference for Texas title examination and should be consulted for all substantive title questions.

### Topic-Specific References
- `references/tx-liens.md` - Constitutional, statutory, and consensual lien analysis; priority rules; lien release/expiration
- `references/tx-commercial.md` - Commercial RE title analysis: ALTA/NSPS surveys, environmental due diligence, 1031 exchanges, commercial leases, SNDA agreements, endorsement packages
- `references/tx-condemnation.md` - Eminent domain and condemnation: condemning authorities, process, title impact, pipeline/utility easements
- `references/tx-manufactured-housing.md` - Manufactured housing title: SOL, TDHCA, personal-to-real property conversion, common defects
- `references/tx-minerals.md` - Mineral and royalty interest analysis
- `references/tx-forms.md` - Texas title insurance forms and endorsements
- `references/tx-requirements.md` - Common requirements and satisfaction methods
- `references/tx-exceptions.md` - Standard and special exception analysis
- `references/tx-opinion-template.md` - Title opinion letter template
- `references/tx-foreclosure.md` - Foreclosure, workout, and lien priority issues
- `references/tx-probate.md` - Estate and probate title issues (heirship, muniments, TODDs)
- `references/tx-entities.md` - Entity authority analysis (LLCs, corps, trusts, POAs)
- `references/tx-water-rights.md` - Water rights analysis (surface water, groundwater, GCDs)
- `references/tx-survey.md` - Survey analysis and exception deletion
- `references/tx-quality-checklist.md` - Pre-delivery verification checklist

### Sample Outputs
- `references/sample-outputs/sample-title-opinion.md` - Example draft title opinion format
- `references/sample-outputs/sample-requirements-checklist.md` - Example requirements checklist
- `references/sample-outputs/sample-exception-analysis.md` - Example exception analysis

### Data Integration
- `data/title-analysis-schema.json` - JSON Schema for structured data export
- `data/sample-analysis-record.json` - Sample analysis record in JSON format
- `references/tx-data-schema.md` - Schema documentation with field definitions and CSV mapping

Use the data schema to export analysis results to case management systems. The schema supports JSON (primary), CSV/Excel (flattened), and XML (legacy) formats.

### Quality Verification
Before delivering any output, review `references/tx-quality-checklist.md` to verify completeness and accuracy.
