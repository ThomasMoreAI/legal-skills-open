# USPTO Open Data Portal (ODP)

Comprehensive USPTO data via the Open Data Portal API.

**Required**: `USPTO_ODP_API_KEY` environment variable.

## Clients

| Client | Import | Description |
|--------|--------|-------------|
| `ApplicationsClient` | `from patent_client_agents.uspto_odp import ApplicationsClient` | Applications, documents, families |
| `BulkDataClient` | `from patent_client_agents.uspto_odp import BulkDataClient` | Bulk data products |
| `PetitionsClient` | `from patent_client_agents.uspto_odp import PetitionsClient` | Petition decisions |
| `PtabTrialsClient` | `from patent_client_agents.uspto_odp import PtabTrialsClient` | IPR/PGR/CBM/DER trials |
| `PtabAppealsClient` | `from patent_client_agents.uspto_odp import PtabAppealsClient` | Ex parte appeals |
| `PtabInterferencesClient` | `from patent_client_agents.uspto_odp import PtabInterferencesClient` | Interferences |

## ApplicationsClient

### search(query, ...) -> SearchResponse

Search patent applications using Lucene syntax.

```python
async with ApplicationsClient() as client:
    results = await client.search(
        query="artificial intelligence",
        fields=["applicationNumberText", "filingDate", "inventorNameArrayText"],
        sort="filingDate desc",
        limit=25,
        offset=0
    )

    for record in results.applicationBag:
        record.applicationNumberText
        record.filingDate
        record.applicationMetaData
```

### get(application_number) -> ApplicationResponse

Get single application metadata.

```python
app = await client.get("16123456")
app.applicationMetaData.applicationStatusDescriptionText
app.applicationMetaData.examinerNameText
app.inventorBag
app.applicantBag
```

### get_documents(application_number) -> DocumentsResponse

Get file wrapper documents.

```python
docs = await client.get_documents("16123456")
for doc in docs.documentBag:
    doc.documentCode
    doc.documentDescription
    doc.officialDate
    doc.pdfUrl  # Direct download URL
```

### get_assignment(application_number) -> AssignmentResponse

Get assignment history.

```python
assignments = await client.get_assignment("16123456")
for a in assignments.assignmentBag:
    a.conveyanceText
    a.recordedDate
    a.assignorBag
    a.assigneeBag
```

### get_family(application_number) -> FamilyGraphResponse

Build patent family graph (continuity tree).

```python
family = await client.get_family("16123456")
family.nodes  # List[FamilyNode] - all related applications
family.edges  # List[FamilyEdge] - parent/child relationships
```

## PtabTrialsClient

### search_proceedings(query, ...) -> PtabTrialProceedingResponse

Search IPR/PGR/CBM/DER proceedings.

```python
async with PtabTrialsClient() as client:
    results = await client.search_proceedings(
        query="patent:US10123456",
        limit=25
    )

    for proc in results.proceedingBag:
        proc.trialNumber        # "IPR2023-00001"
        proc.trialType          # "IPR", "PGR", "CBM", "DER"
        proc.filingDate
        proc.institutionDate
        proc.petitionerPartyName
        proc.patentOwnerPartyName
```

### get_proceeding(trial_number) -> PtabTrialProceedingResponse

Get single proceeding.

```python
proc = await client.get_proceeding("IPR2023-00001")
```

### get_documents_by_trial(trial_number) -> PtabTrialDocumentResponse

Get all documents filed in a trial.

```python
docs = await client.get_documents_by_trial("IPR2023-00001")
for doc in docs.documentBag:
    doc.documentIdentifier
    doc.documentTitle
    doc.filingDate
    doc.downloadUrl
```

### get_decisions_by_trial(trial_number) -> PtabTrialDecisionResponse

Get trial decisions.

```python
decisions = await client.get_decisions_by_trial("IPR2023-00001")
for dec in decisions.decisionBag:
    dec.decisionTypeCategory
    dec.issueDate
    dec.outcomeType
```

## BulkDataClient

### search(query, ...) -> BulkDataSearchResponse

Search available bulk data products.

```python
async with BulkDataClient() as client:
    products = await client.search(query="grant")

    for product in products.productBag:
        product.productIdentifier
        product.productTitle
        product.frequency
        product.fileFormat
```

### get_product(product_id, ...) -> BulkDataProductResponse

Get product with file list.

```python
product = await client.get_product(
    "PTGRXML",
    file_from_date="2024-01-01",
    file_to_date="2024-12-31",
    latest_only=True
)

for f in product.fileBag:
    f.fileName
    f.fileSize
    f.fileFromDate
    f.downloadUri  # Direct download URL
```

## Query Syntax

ODP uses Lucene query syntax:

```
# Field search
inventorNameArrayText:"John Smith"

# Wildcards
assigneeNameArrayText:Google*

# Date ranges
filingDate:[2020-01-01 TO 2023-12-31]

# Boolean
(neural network) AND assigneeNameArrayText:IBM

# Phrase
"machine learning"
```

## Common Fields

| Field | Description |
|-------|-------------|
| `applicationNumberText` | Application number (e.g., "16123456") |
| `patentNumber` | Granted patent number |
| `filingDate` | Application filing date |
| `inventorNameArrayText` | Inventor names |
| `assigneeNameArrayText` | Assignee/applicant names |
| `applicationStatusDescriptionText` | Current status |
| `cpcInventiveClassificationSymbolArrayText` | CPC codes |
