# Example Output

## Scenario

User asks: "Investigate Tesco PLC from Companies House."

Access state: live source mode. Claude found public Companies House profile, officers, charges, and PSC pages for Tesco PLC, company number 00445790.

## Good Output Shape

```yaml
access_mode: live_registry
company_snapshot:
  company_name: "TESCO PLC"
  company_number: "00445790"
  status: "Active"
  incorporation_date: "1947-11-27"
  registered_office: "Tesco House, Shire Park, Kestrel Way, Welwyn Garden City, AL7 1GA"
  sic_summary: "Retail sale in non-specialised stores with food, beverages or tobacco predominating"
  source_mode: live_registry
  date_checked: "2026-05-10"
  source: "Companies House profile page: https://find-and-update.company-information.service.gov.uk/company/00445790"

registry_evidence:
  - fact: "Companies House search result reports 9 registered charges: 2 outstanding and 7 satisfied."
    source: "Companies House charges page search result for company 00445790"
    document_id: "https://find-and-update.company-information.service.gov.uk/company/00445790/charges"
    status: registry_evidence
    confidence: high
  - fact: "PSC information is not publicly available because Tesco PLC is exempt due to voting shares admitted to trading on a UK regulated market."
    source: "Companies House PSC page search result for company 00445790"
    document_id: "https://find-and-update.company-information.service.gov.uk/company/00445790/persons-with-significant-control"
    status: registry_evidence
    confidence: high

inferences:
  - observation: "Outstanding pension-trustee security agreements may be relevant to financing/security diligence but are not allegations of distress."
    basis:
      - "Charges page search result identifies two outstanding account security agreements created on 4 November 2009."
    status: needs_verification
    confidence: medium
    not_an_allegation: true

identity_cautions:
  - "Do not link Tesco officers to similarly named people in other companies without officer id/month-year of birth/address/source filing support."

follow_up:
  - "Retrieve latest accounts filing text from Companies House."
  - "Open charge instruments to confirm security scope, secured parties, and satisfaction status."
  - "Check officer page directly before relying on current officer counts."
```

## No-Source Mode

```yaml
access_mode: no_source
not_done:
  - "No registry facts stated."
next_step: "Provide company number plus Companies House profile/export/filings, or enable live access."
```
