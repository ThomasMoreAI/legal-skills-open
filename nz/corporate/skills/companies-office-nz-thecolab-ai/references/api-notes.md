# Companies Office NZ API Notes

Unofficial read-only wrapper around the NZ Companies Register website proxy endpoints.

## Source and auth

- Website: `https://app.companiesoffice.govt.nz/companies/app/ui/`
- Public search page: `https://app.companiesoffice.govt.nz/companies/app/ui/pages/companies/search`
- Service API base: `https://app.companiesoffice.govt.nz/companies/app/service/services/`
- Auth model: **none** for all implemented commands (public/read-only website proxy calls)

No login, session cookie, API key, or OAuth token is required for the implemented commands.

## Endpoint inventory

### Search

```
GET /companies/app/service/services/entity/search?mode=company&q={query}&start={start}&maxResults={limit}
```

`mode` is mandatory (any value works: `company`, `search`). Returns:

```json
{
  "list": [
    {
      "category": "entity",
      "identifier": "1830488",
      "nzbn": "9429034042984",
      "name": "XERO LIMITED",
      "status": "50",
      "statusGroup": "REGISTERED",
      "entityType": "LTD",
      "incorporationDate": "2006-07-06T00:00:00+1200",
      "entityRegisteredOffice": "19-23 Taranaki St, Te Aro, Wellington, 6011, New Zealand",
      "entityRegisteredOfficeSuppressed": false,
      "showFullDetails": true,
      "suppressed": false
    }
  ],
  "totalMatches": 1,
  "displayableCount": 1,
  "start": 0,
  "end": 1
}
```

Both company number and NZBN can be passed as `q` to find an exact match.

### Entity summary

```
GET /companies/app/service/services/entity/{company_id}
```

Returns identity, counts, previous names. Notable: `nzbn` field is always `null` here — use search results for NZBN.

Sample response keys: `entityIdentifier`, `entityType`, `entityStatus` (integer), `registrationDateTime`, `lastUpdated`, `name`, `directorCount`, `shareholderCount`, `docCount`, `previousNames[]`, `overseasCompany`, `asicRelated`.

Known `entityStatus` values observed:
- `50` → REGISTERED
- `80` → REMOVED

### Addresses

```
GET /companies/app/service/services/entity/{company_id}/addresses
```

Returns `currentAddresses`, `pendingAddresses`, `historicalAddresses`, plus `email`, `phone`, `mobile`, `fax`, `webUrl`. Each address block has `registeredIndexes`, `serviceIndexes`, `shareRegisterIndexes`, `premiseIndexes`, `recordIndexes` pointing into the `addresses[]` array.

Address objects: `line1`, `line2`, `line3`, `line4`, `postCode`, `countryCode`, `addressType` (STREET), `effectiveFrom`, `effectiveTo`.

### Documents

```
GET /companies/app/service/services/entity/{company_id}/documents?start={start}&count={count}
```

Returns `list[]` and `count` (total). Each document:

```json
{
  "id": 40233874,
  "registrationDate": "14 May 2026 14:19",
  "description": "Particulars of Shareholding",
  "bseFunctionCode": "ChangeShareholderAllocation",
  "documentFlag": true,
  "privateFlag": false,
  "archivedFlag": false,
  "attachments": [
    {
      "id": 87858001,
      "drmKey": "60448ED1FD68093C84753C3F367BB63A",
      "description": "Particulars of Shareholding",
      "documentCode": "OSH"
    }
  ]
}
```

When `drmKey` is non-null, the attachment is publicly downloadable at:
`GET /companies/app/service/services/documents/{drmKey}`

Documents without `drmKey` are not publicly downloadable (they may be internal records).

The `bseFunctionCode` field is useful for filtering filing type (e.g. `ChangeShareholderAllocation`, `ChangeDirectorAppointment`, `AnnualReturn`, `ChangeCompanyShares`, `ChangeAddresses`).

### Directors (HTML parse)

```
GET /companies/app/ui/pages/companies/{company_id}/directors
```

Directors are rendered server-side in `<div id="directorsPanel">`. Each director is in a `<td class="director">` cell containing:
- `Full legal name:` label → name text
- `Residential Address:` label → address text (city/country for overseas)
- `Appointment Date:` label → date string like `01 Oct 2020`
- Optional `Ceased Date:` or `Resignation Date:` label → date string

The equivalent JSON endpoint `GET /service/services/entity/{id}/director/` returns 403 Access Denied without a logged-in session (confirmed against Xero). HTML parsing is the reliable public path.

### Shareholders (HTML parse)

```
GET /companies/app/ui/pages/companies/{company_id}/shareholdings
```

Shareholders are in `<div id="shareholdersPanel">`. The allocation list is in `<div id="allocations">`. Each `<div class="allocationDetail">` has:
- `<input name='shares' value='{N}'>` — share count
- `({N}%)` text — percentage
- `<div class="labelValue col2">` — holder name(s), possibly linked to other companies

Listed companies show an "Extensive Shareholding" flag and note that only top parcels are listed.

The equivalent JSON endpoint `GET /service/services/entity/{id}/shareholders` returns 500 with "directorship must be specified" without an authenticated session.

## Endpoints that require authentication (not implemented)

These endpoints were tested and rejected:

| Endpoint | Error | Reason |
|----------|-------|--------|
| `/service/services/entity/{id}/director/` | 403 Access Denied | Requires session |
| `/service/services/entity/{id}/directors` | 403 | Requires session |
| `/service/services/entity/{id}/shareholders` | 500 "directorship must be specified" | Requires session |
| `/service/services/entity/{id}/shareholders?directorship=current` | 500 | Requires session |
| `/service/services/entity/{id}/charges` | 500 | Requires session |
| `/service/services/entity/{id}/filings` | 500 | Requires session |
| `/service/services/entity/{id}/roles?type=director` | 500 | Requires session |

## PPSR (charges)

The Personal Property Securities Register is at `https://ppsr.companiesoffice.govt.nz/`. The companies register links to it via a JavaScript PPSR search function. PPSR is a separate register with separate endpoints and is not covered by this skill.

## Role search (individual → entities)

```
GET /companies/app/service/services/entity/role/search?entityIdentifier={id}&role=director
```

This endpoint searches for a **person** (individual identifier) and returns the entities they have roles in — it is NOT the company directors list. Do not confuse the two.

## Address types

```
GET /companies/app/service/services/entity/search/addressTypes
→ {"ROA":"Registered office address","AFS":"Address for service","AFSR":"Address for share register","AFR":"Address for records","AUP":"Person authorised to accept service in NZ address","PPB":"Principal place of business in NZ"}
```

## Rate limits and stability

- No formal rate limit documentation found
- These are the same endpoints used by the register's own UI (public-facing, no auth)
- The service pattern is `/companies/app/service/services/` which appears to be a stable internal API (unchanged across multiple years based on JS bundle history)
- The direct official API gateway (`api.business.govt.nz/gateway/nzbn/v5`) requires a subscription key for company-level data

## Tested companies

| Company | Number | NZBN | Notes |
|---------|--------|------|-------|
| XERO LIMITED | 1830488 | 9429034042984 | Listed, extensive shareholding, 7 directors |
| TRADE ME LIMITED | 973228 | — | 2 directors, 1 shareholder |
| HOLT PROPERTY GROUP LIMITED | 9400535 | — | Small private company |
| TRADE ME GROUP LIMITED | 3590412 | — | Parent entity |
