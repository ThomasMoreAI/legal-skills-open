---
name: connector-sec-edgar-sboghossian
title: Connector — SEC EDGAR
description: Use when a lawyer, compliance professional, or due-diligence analyst needs to retrieve US public-company filings from the SEC's EDGAR database — including 10-K annual reports, 10-Q quarterly filings, 8-K current reports, S-1 registration statements, proxy statements, and beneficial ownership disclosures. Free public API; no authentication required. Triggers on requests involving US-listed company research, M&A due diligence on a US public entity, SEC disclosure review, or capital markets regulatory analysis.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/connector/connector-sec-edgar
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: capital-markets
language: en
---

# Connector — SEC EDGAR

## What it does

EDGAR (Electronic Data Gathering, Analysis, and Retrieval) is the US Securities and Exchange Commission's online database of public company filings. Every US-listed company is required to file disclosure documents with the SEC, and all filings are publicly accessible through EDGAR.

The SEC EDGAR connector enables the legal-AI platform to:
- Retrieve public company filings by CIK (Central Index Key), company name, or ticker.
- Search filings by form type and date range.
- Extract specific sections from large filings (e.g., risk factors from a 10-K, or the material contracts exhibit list).
- Monitor for new filings by a specific company.

## Setup / auth

**No authentication required.** The EDGAR HTTPS API and filing retrieval are public.

The SEC provides a dedicated REST API: `data.sec.gov/api/`:
- `data.sec.gov/submissions/{CIK}.json` — full filing history for a company.
- `data.sec.gov/api/xbrl/` — structured financial data.
- `efts.sec.gov/LATEST/search-index` — full-text search.

For production use, the SEC requests that automated callers include a `User-Agent` header identifying the application and a contact email address. Failure to do so may result in IP-based rate limiting.

Rate limit: 10 requests/second recommended by the SEC; enforce in the connector.

## Filing form types

| Form | What it is | Use in legal practice |
|---|---|---|
| 10-K | Annual report | Full business description, risk factors, financials, material contracts |
| 10-Q | Quarterly report | Interim financials, litigation disclosures |
| 8-K | Current report (material events) | Acquisitions, executive changes, bankruptcy, material contract entry |
| S-1 / F-1 | IPO registration statement | Business description, financials, risk factors; pre-IPO due diligence |
| 20-F | Foreign private issuer annual report | MENA-listed companies on US exchanges use this form |
| 6-K | Foreign private issuer current report | Equivalent of 8-K for foreign issuers |
| DEF 14A | Proxy statement | Shareholder voting matters, executive compensation |
| SC 13D / 13G | Beneficial ownership >5% | Identify major shareholders; change of control signals |
| Form 4 | Insider transactions | Director/officer stock purchases and sales |
| 13F | Institutional holdings | Quarterly disclosure of >$100M institutional managers |

## CIK lookup

Every EDGAR filer has a unique CIK (Central Index Key). CIK lookup by company name:
- API: `https://efts.sec.gov/LATEST/search-index?q=%22company+name%22&dateRange=custom&startdt=2000-01-01&enddt=today&forms=10-K`
- Or: `https://www.sec.gov/cgi-bin/browse-edgar?company=NAME&action=getcompany`

For MENA companies listed in the US (e.g., an Israeli tech company on Nasdaq, a Gulf-domiciled SPAC), they file as Foreign Private Issuers using 20-F and 6-K forms.

## Usage patterns

### Pattern 1 — M&A due diligence on a US-listed target

```
User: "Pull the 10-K and latest 10-Qs for TechCorp Inc."
→ Connector looks up TechCorp's CIK
→ Retrieves the most recent 10-K (annual) and last two 10-Qs
→ Returns: business description, risk factors section, material contracts list, 
  pending litigation disclosures, and financial highlights
→ Flag any risk factors related to the buyer's jurisdiction or sector
```

### Pattern 2 — 8-K monitoring for a counterparty

For ongoing transaction monitoring:
- Set up a scheduled task (via [[connector-scheduled-tasks]]) to check for new 8-K filings by a counterparty.
- Alert if an 8-K is filed describing a material event that could affect the counterparty's ability to perform (bankruptcy filing, regulatory action, change of control).

### Pattern 3 — Cross-border M&A — MENA buyer, US target

For a GCC sovereign wealth fund or MENA PE firm acquiring a US-listed company:
- Retrieve the target's most recent 10-K for the business description and risk factors.
- Review the material contracts list (Exhibit 10 filings) for change-of-control clauses that trigger on the acquisition.
- Review the proxy statement for shareholder approval requirements.

### Pattern 4 — Beneficial ownership analysis

```
User: "Who owns more than 5% of ABC Corp?"
→ Search EDGAR for ABC Corp's SC 13D and 13G filings
→ Return: list of >5% beneficial owners with their declared holdings and filing dates
→ Cross-reference owners against [[connector-ofac-sanctions]] if the transaction has US sanctions implications
```

### Pattern 5 — Foreign private issuer research

For a Lebanese company traded on a US exchange:
- Retrieve the 20-F (annual report equivalent) — note that 20-F filings use different reporting standards than domestic 10-K filings (IFRS vs US GAAP).
- The 20-F risk factors section typically includes jurisdiction-specific disclosures about the home country's regulatory environment — useful for understanding political risk in MENA issuers.

## MENA relevance

US capital markets have significant MENA intersections:
- **GCC sovereign wealth funds** (ADIA, PIF, QIA, Mubadala) hold US-listed securities and file 13F disclosures.
- **MENA PE-backed companies** pursuing US listings use F-1/20-F.
- **US-listed companies with MENA operations** disclose regional risk in their 10-K risk factors.
- **Dual-listed companies** (e.g., companies listed on both a MENA exchange and a US exchange) file both local regulatory disclosures and SEC filings.

When advising MENA clients on US capital markets transactions, EDGAR is a primary research tool. When advising US clients on MENA market entry, reviewing EDGAR filings of US-listed MENA-exposed companies provides competitive and regulatory intelligence.

## Permissions & safety

- **Public data only.** All EDGAR content is public; no PII restrictions on the filings themselves (although they may contain names of individuals in a public-company context).
- **Attribution.** When returning EDGAR content, include the form type, filing date, and EDGAR accession number for citation.
- **No financial advice.** Information from EDGAR is for legal due diligence — never frame it as investment advice.
- **Currency.** EDGAR filings reflect the state as of the filing date. For fast-moving situations (e.g., a company undergoing restructuring), check for the most recent 8-K before relying on the 10-K narrative.

## Failure modes

| Failure | Cause | Resolution |
|---|---|---|
| CIK not found | Company name variation or ticker change | Try the EDGAR full-text search; search by ticker; check for former names |
| Filing too large | 10-K files can exceed 100MB | Retrieve the index file first; then request specific exhibits by accession number |
| Rate limited | >10 requests/second | Implement rate limiter; queue requests |
| 20-F filed in non-English | EDGAR requires English but some exhibits may be in original language | Note the language; link to the original exhibit |

## Related skills

- [[connector-companies-house-uk]]
- [[connector-ofac-sanctions]]
- [[connector-eur-lex]]
- [[connector-cocounsel-thomson-reuters]]
