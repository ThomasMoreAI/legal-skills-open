# Texas Title Analysis Data Schema

> **DISCLAIMER**: This schema is for data integration purposes only. All analysis data represents DRAFT outputs requiring attorney review before reliance.

---

## Overview

This document defines the data structure for Texas title analysis input/output. The schema supports:
- **JSON** - Primary format for APIs and modern systems
- **CSV/Excel** - Flattened export for spreadsheet-based systems
- **XML** - Legacy system compatibility

---

## Schema Structure

```
TitleAnalysisRecord
├── metadata                    # Record tracking info
├── matter                      # Case/file information
├── property                    # Subject property details
├── parties[]                   # All parties to transaction
├── commitment                  # Title commitment data
│   ├── scheduleA              # Coverage information
│   ├── requirementsBOne[]     # Schedule B-I requirements
│   └── exceptionsBTwo[]       # Schedule B-II exceptions
├── analysis                    # Analysis results
│   ├── chainOfTitle           # Chain analysis
│   ├── texasSpecific          # TX-specific issues
│   └── riskAssessment         # Overall risk rating
├── outputs[]                   # Generated documents
└── notes[]                     # Examiner notes
```

---

## Field Definitions

### 1. Metadata

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `schemaVersion` | string | Yes | Schema version (e.g., "1.0") |
| `recordId` | string | Yes | Unique identifier (UUID recommended) |
| `createdAt` | datetime | Yes | ISO 8601 timestamp |
| `updatedAt` | datetime | Yes | ISO 8601 timestamp |
| `createdBy` | string | Yes | User/system identifier |
| `status` | enum | Yes | `draft`, `pending_review`, `reviewed`, `approved`, `closed` |

### 2. Matter

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `fileNumber` | string | Yes | Internal file/matter number |
| `clientFileNumber` | string | No | Client's reference number |
| `transactionType` | enum | Yes | `purchase`, `refinance`, `equity`, `construction`, `commercial` |
| `estimatedClosingDate` | date | No | Expected closing date |
| `actualClosingDate` | date | No | Actual closing date |
| `underwriter` | string | No | Title insurance underwriter |
| `commitmentNumber` | string | No | Commitment/policy number |

### 3. Property

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `propertyId` | string | Yes | Unique property identifier |
| `streetAddress` | string | No | Street address |
| `city` | string | No | City |
| `county` | string | Yes | Texas county |
| `state` | string | Yes | Always "TX" |
| `zip` | string | No | ZIP code |
| `legalDescription` | string | Yes | Full legal description |
| `parcelId` | string | No | Tax parcel/account number |
| `subdivision` | string | No | Subdivision name |
| `lot` | string | No | Lot number |
| `block` | string | No | Block number |
| `section` | string | No | Section (for metes & bounds) |
| `abstract` | string | No | Abstract number |
| `survey` | string | No | Survey name |
| `acreage` | number | No | Property size in acres |
| `propertyType` | enum | Yes | `residential`, `commercial`, `agricultural`, `industrial`, `mixed` |
| `improvements` | string | No | Description of improvements |

### 4. Parties

Array of party objects:

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `partyId` | string | Yes | Unique party identifier |
| `role` | enum | Yes | `buyer`, `seller`, `lender`, `borrower`, `title_company`, `escrow`, `attorney`, `agent` |
| `entityType` | enum | Yes | `individual`, `married_couple`, `llc`, `corporation`, `lp`, `gp`, `trust`, `estate` |
| `name` | string | Yes | Full legal name |
| `dba` | string | No | Doing business as |
| `entityState` | string | No | State of organization (for entities) |
| `entityFileNumber` | string | No | SOS file number |
| `address` | object | No | Mailing address |
| `email` | string | No | Contact email |
| `phone` | string | No | Contact phone |
| `ssn_ein_last4` | string | No | Last 4 digits (for verification) |
| `maritalStatus` | enum | No | `single`, `married`, `divorced`, `widowed` (for individuals) |
| `spouseName` | string | No | Spouse name if married |

### 5. Commitment - Schedule A

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `effectiveDate` | datetime | Yes | Commitment effective date/time |
| `commitmentNumber` | string | Yes | Commitment number |
| `proposedInsured` | object | Yes | Proposed insured parties |
| `ownerPolicyAmount` | number | No | Owner's policy amount |
| `loanPolicyAmount` | number | No | Loan policy amount |
| `currentVesting` | string | Yes | Current record title holder |
| `vestingDocument` | object | No | Recording info for vesting deed |
| `legalDescription` | string | Yes | Legal description per commitment |

### 6. Commitment - Schedule B-I Requirements

Array of requirement objects:

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `requirementId` | string | Yes | Unique requirement ID |
| `itemNumber` | string | Yes | Item number from commitment |
| `category` | enum | Yes | `taxes`, `lien_release`, `document_execution`, `hoa`, `survey`, `entity_docs`, `affidavit`, `probate`, `other` |
| `description` | string | Yes | Full requirement text |
| `status` | enum | Yes | `open`, `in_progress`, `satisfied`, `waived`, `not_applicable` |
| `responsibleParty` | enum | No | `buyer`, `seller`, `lender`, `title_company`, `other` |
| `dueDate` | date | No | Due date if applicable |
| `satisfactionMethod` | string | No | How requirement was/will be satisfied |
| `satisfactionDocument` | object | No | Recording info for satisfaction doc |
| `satisfiedDate` | date | No | Date requirement was satisfied |
| `notes` | string | No | Additional notes |

### 7. Commitment - Schedule B-II Exceptions

Array of exception objects:

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `exceptionId` | string | Yes | Unique exception ID |
| `itemNumber` | string | Yes | Item number from commitment |
| `exceptionType` | enum | Yes | `standard`, `special`, `survey`, `taxes`, `restrictions`, `easement`, `lien`, `mineral`, `hoa`, `water_rights`, `other` |
| `description` | string | Yes | Full exception text |
| `recordingInfo` | object | No | Recording reference |
| `affectsProperty` | boolean | Yes | Does exception affect subject property? |
| `impactLevel` | enum | Yes | `none`, `low`, `medium`, `high`, `critical` |
| `impactDescription` | string | No | Description of impact |
| `curable` | boolean | Yes | Can this exception be cured? |
| `cureMethod` | string | No | Recommended cure approach |
| `cureDocuments` | string[] | No | Documents needed to cure |
| `cureResponsibleParty` | enum | No | `buyer`, `seller`, `lender`, `title_company` |
| `cureStatus` | enum | No | `not_started`, `in_progress`, `cured`, `will_remain`, `insured_over` |
| `willRemainAsException` | boolean | No | Will this remain in final policy? |
| `notes` | string | No | Additional notes |

### 8. Analysis Results

#### 8.1 Chain of Title

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `chainComplete` | boolean | Yes | Is chain complete and marketable? |
| `searchPeriod` | object | No | Start/end dates of search |
| `gapsIdentified` | boolean | No | Were gaps found? |
| `gapDetails` | string[] | No | Description of any gaps |
| `outstandingInterests` | object[] | No | Unreleased liens, interests |
| `nameVariations` | object[] | No | Name variations in chain |
| `chainNotes` | string | No | Additional chain notes |

#### 8.2 Texas-Specific Analysis

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `homesteadAnalysis` | object | No | Homestead determination |
| `homesteadAnalysis.isHomestead` | boolean | No | Is property homestead? |
| `homesteadAnalysis.homesteadType` | enum | No | `urban`, `rural`, `none` |
| `homesteadAnalysis.bothSpousesRequired` | boolean | No | Both spouses must sign? |
| `homesteadAnalysis.notes` | string | No | Homestead notes |
| `communityPropertyAnalysis` | object | No | Community property analysis |
| `communityPropertyAnalysis.isCommunityProperty` | boolean | No | Is community property? |
| `communityPropertyAnalysis.separatePropertyClaimed` | boolean | No | Separate property claimed? |
| `communityPropertyAnalysis.joindRequired` | boolean | No | Spouse joinder required? |
| `communityPropertyAnalysis.notes` | string | No | Community property notes |
| `mineralAnalysis` | object | No | Mineral rights analysis |
| `mineralAnalysis.mineralsSevered` | boolean | No | Are minerals severed? |
| `mineralAnalysis.surfaceOwnershipPct` | number | No | % of minerals with surface |
| `mineralAnalysis.activeLeases` | boolean | No | Active mineral leases? |
| `mineralAnalysis.notes` | string | No | Mineral notes |
| `waterRightsAnalysis` | object | No | Water rights analysis |
| `waterRightsAnalysis.surfaceWaterRights` | boolean | No | Surface water rights present? |
| `waterRightsAnalysis.groundwaterSevered` | boolean | No | Groundwater severed? |
| `waterRightsAnalysis.inGCD` | boolean | No | In Groundwater Conservation District? |
| `waterRightsAnalysis.gcdName` | string | No | GCD name if applicable |
| `waterRightsAnalysis.notes` | string | No | Water rights notes |
| `probateIssues` | object | No | Probate/estate analysis |
| `entityAuthorityVerified` | boolean | No | Entity authority confirmed? |

#### 8.3 Risk Assessment

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `overallRisk` | enum | Yes | `low`, `medium`, `high`, `critical` |
| `riskFactors` | object[] | No | Array of risk factors |
| `riskFactors[].factor` | string | No | Risk factor description |
| `riskFactors[].severity` | enum | No | `low`, `medium`, `high`, `critical` |
| `riskFactors[].mitigation` | string | No | Recommended mitigation |
| `recommendedAction` | enum | Yes | `proceed`, `proceed_with_conditions`, `hold`, `decline` |
| `conditions` | string[] | No | Conditions for proceeding |

### 9. Outputs Generated

Array of output objects:

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `outputId` | string | Yes | Unique output ID |
| `outputType` | enum | Yes | `title_opinion`, `requirements_checklist`, `exception_analysis`, `cure_letter`, `other` |
| `filename` | string | Yes | Output filename |
| `format` | enum | Yes | `docx`, `pdf`, `md`, `xlsx` |
| `generatedAt` | datetime | Yes | Generation timestamp |
| `generatedBy` | string | Yes | System/user that generated |
| `version` | string | No | Output version |
| `reviewStatus` | enum | Yes | `draft`, `pending_review`, `reviewed`, `approved` |
| `reviewedBy` | string | No | Attorney who reviewed |
| `reviewedAt` | datetime | No | Review timestamp |
| `filePath` | string | No | Path/URL to file |

### 10. Notes

Array of note objects:

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `noteId` | string | Yes | Unique note ID |
| `noteType` | enum | Yes | `general`, `examiner`, `attorney`, `client`, `system` |
| `content` | string | Yes | Note content |
| `createdAt` | datetime | Yes | Creation timestamp |
| `createdBy` | string | Yes | Author |
| `isPrivate` | boolean | No | Internal only? |

---

## JSON Example

```json
{
  "metadata": {
    "schemaVersion": "1.0",
    "recordId": "550e8400-e29b-41d4-a716-446655440000",
    "createdAt": "2026-02-05T14:30:00Z",
    "updatedAt": "2026-02-05T16:45:00Z",
    "createdBy": "tx-title-analysis-skill",
    "status": "pending_review"
  },
  "matter": {
    "fileNumber": "2026-TX-00142",
    "clientFileNumber": "ABC-789",
    "transactionType": "purchase",
    "estimatedClosingDate": "2026-02-28",
    "underwriter": "First American",
    "commitmentNumber": "FA-2026-123456"
  },
  "property": {
    "propertyId": "prop-001",
    "streetAddress": "123 Main Street",
    "city": "Austin",
    "county": "Travis",
    "state": "TX",
    "zip": "78701",
    "legalDescription": "Lot 5, Block 2, Riverside Addition, Travis County, Texas",
    "parcelId": "01-2345-0067-0000",
    "subdivision": "Riverside Addition",
    "lot": "5",
    "block": "2",
    "propertyType": "residential"
  },
  "parties": [
    {
      "partyId": "party-001",
      "role": "seller",
      "entityType": "married_couple",
      "name": "John Smith and Jane Smith",
      "maritalStatus": "married"
    },
    {
      "partyId": "party-002",
      "role": "buyer",
      "entityType": "individual",
      "name": "Robert Johnson",
      "maritalStatus": "single"
    }
  ],
  "commitment": {
    "scheduleA": {
      "effectiveDate": "2026-02-01T08:00:00Z",
      "commitmentNumber": "FA-2026-123456",
      "proposedInsured": {
        "owner": "Robert Johnson",
        "lender": "ABC Mortgage Company"
      },
      "ownerPolicyAmount": 450000,
      "loanPolicyAmount": 360000,
      "currentVesting": "John Smith and Jane Smith, husband and wife",
      "vestingDocument": {
        "type": "Warranty Deed",
        "recordedDate": "2018-05-15",
        "volume": "15432",
        "page": "789",
        "documentNumber": "2018054321"
      }
    },
    "requirementsBOne": [
      {
        "requirementId": "req-001",
        "itemNumber": "1",
        "category": "taxes",
        "description": "Payment of all current taxes and assessments",
        "status": "open",
        "responsibleParty": "seller"
      },
      {
        "requirementId": "req-002",
        "itemNumber": "2",
        "category": "lien_release",
        "description": "Release of Deed of Trust from ABC Bank recorded in Document No. 2020123456",
        "status": "in_progress",
        "responsibleParty": "seller"
      }
    ],
    "exceptionsBTwo": [
      {
        "exceptionId": "exc-001",
        "itemNumber": "1",
        "exceptionType": "standard",
        "description": "Taxes for the year 2026 and subsequent years",
        "affectsProperty": true,
        "impactLevel": "low",
        "curable": false,
        "willRemainAsException": true
      },
      {
        "exceptionId": "exc-002",
        "itemNumber": "5",
        "exceptionType": "easement",
        "description": "Easement to Austin Energy for electric lines recorded in Volume 5432, Page 123",
        "recordingInfo": {
          "volume": "5432",
          "page": "123",
          "recordedDate": "1985-03-12"
        },
        "affectsProperty": true,
        "impactLevel": "low",
        "impactDescription": "Standard utility easement along rear property line",
        "curable": false,
        "willRemainAsException": true
      }
    ]
  },
  "analysis": {
    "chainOfTitle": {
      "chainComplete": true,
      "searchPeriod": {
        "startDate": "1996-02-05",
        "endDate": "2026-02-05"
      },
      "gapsIdentified": false
    },
    "texasSpecific": {
      "homesteadAnalysis": {
        "isHomestead": true,
        "homesteadType": "urban",
        "bothSpousesRequired": true,
        "notes": "Property is sellers' primary residence; both spouses must execute deed"
      },
      "communityPropertyAnalysis": {
        "isCommunityProperty": true,
        "separatePropertyClaimed": false,
        "joindRequired": true
      },
      "mineralAnalysis": {
        "mineralsSevered": false,
        "surfaceOwnershipPct": 100,
        "activeLeases": false
      },
      "waterRightsAnalysis": {
        "surfaceWaterRights": false,
        "groundwaterSevered": false,
        "inGCD": false
      }
    },
    "riskAssessment": {
      "overallRisk": "low",
      "riskFactors": [],
      "recommendedAction": "proceed",
      "conditions": []
    }
  },
  "outputs": [
    {
      "outputId": "out-001",
      "outputType": "title_opinion",
      "filename": "2026-TX-00142-title-opinion-DRAFT.docx",
      "format": "docx",
      "generatedAt": "2026-02-05T16:45:00Z",
      "generatedBy": "tx-title-analysis-skill",
      "version": "1.0",
      "reviewStatus": "draft"
    }
  ],
  "notes": [
    {
      "noteId": "note-001",
      "noteType": "examiner",
      "content": "Clean chain of title. Standard residential transaction.",
      "createdAt": "2026-02-05T16:45:00Z",
      "createdBy": "tx-title-analysis-skill",
      "isPrivate": false
    }
  ]
}
```

---

## CSV/Excel Mapping

For flat file export, the nested structure is flattened using these conventions:

### Primary Export Tables

| Table | Description | Key Fields |
|-------|-------------|------------|
| `matters` | One row per matter | fileNumber, transactionType, closingDate |
| `properties` | One row per property | propertyId, address, county, legalDescription |
| `parties` | One row per party | partyId, fileNumber, role, name, entityType |
| `requirements` | One row per requirement | requirementId, fileNumber, itemNumber, status |
| `exceptions` | One row per exception | exceptionId, fileNumber, itemNumber, impactLevel |
| `analysis_results` | One row per matter | fileNumber, overallRisk, recommendedAction |

### Flattened Field Names

Nested objects use underscore notation:
- `commitment.scheduleA.effectiveDate` → `commitment_scheduleA_effectiveDate`
- `analysis.texasSpecific.homesteadAnalysis.isHomestead` → `texas_homestead_isHomestead`

---

## Integration Notes

### API Integration
- Use the full JSON structure for API calls
- All dates should be ISO 8601 format
- UUIDs recommended for all ID fields

### Database Import
- Create separate tables for each major section
- Use foreign keys (fileNumber or recordId) to link tables
- Index on fileNumber, propertyId, status fields

### Legacy System (XML)
- JSON can be converted to XML using standard tools
- Maintain element names matching JSON field names
- Use CDATA for long text fields (legalDescription, description)

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-02 | Initial schema release |

---

*This schema is part of the Texas Title Analysis Skill.*