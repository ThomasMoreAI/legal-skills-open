---
name: tool-sec-edgar-us-sboghossian
title: SEC EDGAR — US Public Company Filings
description: Use when due diligence or research requires reviewing US public company filings — annual reports (10-K), quarterly reports (10-Q), material event disclosures (8-K), IPO prospectuses (S-1), proxy statements (DEF 14A), or beneficial ownership schedules (13D/G). Essential for counterparty due diligence on US-listed companies, tracking risk factors before signing supply agreements, and identifying acquisition history or material contracts.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/tool/tool-sec-edgar-us
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: capital-markets
language: en
---

# SEC EDGAR — US Public Company Filings

## What it does

This tool queries the US Securities and Exchange Commission's EDGAR (Electronic Data Gathering, Analysis, and Retrieval) system — the public repository of all US public company filings. It enables lookup, retrieval, and analysis of SEC filings for due diligence, contract counterparty research, M&A preparation, and regulatory compliance in transactions involving US-listed companies.

EDGAR is a free public resource (https://www.sec.gov/cgi-bin/browse-edgar). This tool provides programmatic access to the EDGAR full-text search API and filing APIs.

## Setup / auth

No API key required for basic EDGAR access. The SEC provides a public REST API at `https://data.sec.gov/` and a full-text search API at `https://efts.sec.gov/LATEST/search-index`.

| Parameter | Description | Required |
|-----------|-------------|----------|
| `companyName` | Company name for search | Conditional |
| `cik` | SEC CIK (Central Index Key) — 10-digit identifier | Preferred when known |
| `ticker` | US stock exchange ticker symbol | Alternative to CIK |
| `formType` | SEC form type to filter (e.g., "10-K", "8-K", "S-1") | Recommended |
| `dateFrom` / `dateTo` | Filing date range | Optional |
| `keywordSearch` | Full-text search within filing documents | Optional |

The SEC also publishes machine-readable CIK lookup and company tickers JSON for bulk resolution.

## Form type reference

| Form | Description | Key uses |
|------|-------------|---------|
| **10-K** | Annual report | Comprehensive company overview, risk factors, financial statements, material agreements |
| **10-Q** | Quarterly report | Interim financials, material developments since 10-K |
| **8-K** | Material event (current report) | Acquisitions, officer changes, defaults, amendments to material contracts |
| **S-1** | IPO registration statement | Full company history, risks, use of proceeds, financial statements |
| **S-4** | Merger / acquisition registration | Deal structure, proxy information, target financial statements |
| **DEF 14A** | Definitive proxy statement | Board composition, executive compensation, shareholder votes |
| **13D / 13G** | Beneficial ownership (>5% stake) | Track who owns significant stakes; flag activist investors |
| **Form 4** | Insider trading reports | Officers/directors buying and selling shares |
| **SC 13E-3** | Going-private transactions | Management buyouts |
| **ARS** | Annual report to shareholders | Shareholder communications |

## Capabilities

### Company / CIK lookup
```
Input:  { companyName: "Acme Corporation" }
Output: { cik: "0001234567", entityName: "ACME CORPORATION", sic: "7372", state: "DE" }
```

### Filing search
```
Input:  {
  cik: "0001234567",
  formType: "10-K",
  dateFrom: "2023-01-01",
  dateTo: "2025-12-31"
}
Output: {
  filings: [
    {
      form: "10-K",
      filedAt: "2025-02-15",
      periodOfReport: "2024-12-31",
      accessionNumber: "0001234567-25-012345",
      primaryDocument: "acme-20241231.htm",
      exhibits: [
        { number: "10.1", description: "Material Agreement — Master Services Agreement" }
      ],
      url: "https://www.sec.gov/Archives/edgar/data/..."
    }
  ]
}
```

### Full-text keyword search within filings
```
Input:  {
  cik: "0001234567",
  query: "force majeure COVID-19",
  formTypes: ["10-K", "10-Q"]
}
Output: [ { filing, snippet, relevance } ]
```
Useful for extracting specific contractual risk disclosures (e.g., how the company describes its material contract terms, force majeure exposure, or supply chain risks).

### Exhibit extraction
Many material contracts are filed as exhibits to 10-Ks and 8-Ks. The tool can retrieve specific exhibits:
```
Input:  { accessionNumber: "...", exhibitNumber: "10.1" }
Output: { exhibitText, exhibitType, filedDate }
```

### Beneficial ownership tracking (13D/G)
```
Input:  { cik: "0001234567", formType: "13D" }
Output: [ { filer, sharesHeld, percentOwned, filedDate, purposeOfTransaction } ]
```

## Use cases for legal professionals

### Counterparty due diligence
When a MENA or international company enters a significant commercial contract with a US-listed entity, EDGAR provides:
- **Financial health check**: recent 10-K and 10-Q for going-concern warnings, significant litigation, or covenant defaults
- **Material agreements already filed**: many supply agreements, license agreements, and MSAs are filed as exhibits — retrieve the counterparty's standard form for negotiation context
- **Risk factors**: how does the company describe its legal and regulatory risks?
- **Litigation history**: 10-K Item 3 (Legal Proceedings) discloses material pending litigation

### M&A transaction support
- **Acquisition history**: 8-K filings for past acquisitions give context on deal structures and pricing
- **Existing material contracts**: assess what key contracts transfer in an acquisition
- **Change-of-control clauses**: search exhibits for change-of-control provisions in material agreements
- **SEC proxy materials**: DEF 14A provides fairness opinion summaries and deal terms

### Tracking insider and significant shareholder activity
- Form 4 filings show officer/director transactions — useful for timing of deal negotiations
- 13D/G filings show activist investor activity that may affect a transaction

### US-listed parent of MENA subsidiary
MENA subsidiaries of US-listed companies are not directly on EDGAR, but the parent's 10-K will include subsidiary financial statements and often disclose material agreements entered into by subsidiaries. Use this as an additional due diligence layer.

## Output schema

```json
{
  "company": {
    "cik": "0001234567",
    "entityName": "ACME CORPORATION",
    "sic": "7372",
    "sicDescription": "Prepackaged Software",
    "state": "DE",
    "fiscalYearEnd": "1231"
  },
  "filings": [
    {
      "form": "10-K",
      "filedAt": "2025-02-15",
      "periodOfReport": "2024-12-31",
      "accessionNumber": "0001234567-25-012345",
      "url": "https://www.sec.gov/...",
      "exhibits": [...]
    }
  ],
  "source": "SEC EDGAR",
  "fetchedAt": "2026-05-14T10:00:00Z"
}
```

## Limitations

- **US public companies only**: private companies do not file on EDGAR. For US private company diligence, use public records search, UCC filings, and news sources.
- **Not real-time**: EDGAR filing processing typically occurs within 1 business day of filing.
- **No financial analysis**: this tool retrieves filings; it does not perform financial ratio analysis. Pair with a financial analysis skill for that.
- **XBRL data**: structured financial data is available in XBRL format for financial statement parsing — request this format for quantitative analysis.

## Failure modes

| Failure | Symptom | Resolution |
|---------|---------|------------|
| CIK not found | No result on company search | Try ticker; check SEC EDGAR full-text search |
| Filing too old | Accession number returns 404 | Older filings may have different URL structure |
| Large filing | Timeout on exhibit extraction | Retrieve primary document first; get exhibits on demand |
| Rate limit | 429 from data.sec.gov | SEC limits to 10 requests/second per IP |

## Related skills

- [[tool-lexisnexis]] — US case law and secondary sources to complement EDGAR research
- [[tool-thomson-reuters-westlaw]] — Practical Law for M&A due diligence checklists
- [[tool-hubspot-crm-context]] — CRM context to pre-populate counterparty data
- [[tool-ofac-sanctions]] — screen US-listed entity officers and directors
- [[research-beneficial-ownership-lookup]] — UBO analysis using EDGAR 13D/G data as input
