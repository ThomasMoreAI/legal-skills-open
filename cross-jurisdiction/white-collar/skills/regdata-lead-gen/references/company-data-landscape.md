# European Company Data Landscape

A practical guide to what official registry data is publicly available in each country, how to access it, and what to expect.

## Poland (PL)

### Official Registries
- **KRS (Krajowy Rejestr Sadowy)** - National Court Register. Central registry for all companies, foundations, and associations.
- **CRBR (Centralny Rejestr Beneficjentow Rzeczywistych)** - Beneficial Owners Register. UBO data for AML/KYC.
- **eKRS** - Electronic access to KRS with financial statement filings (balance sheets, P&L).
- **KNF (Komisja Nadzoru Finansowego)** - Financial supervision registry. Licensed payment institutions and e-money issuers.
- **GUS/REGON** - Statistical office registry with REGON numbers and PKD activity codes.

### What Is Publicly Available
- Company name, KRS number, NIP (tax ID), REGON, legal form, registered address, registration date
- Board members (Zarzad), supervisory board (Rada Nadzorcza), shareholders holding 10%+ - all with full names via PDF extracts
- Annual financial statements filed with the court (balance sheets, P&L)
- Beneficial owners with ownership percentages and nationalities

### Data Quality and Completeness
- KRS data is authoritative - companies are legally required to keep it current
- Board member data in PDF extracts is complete and non-anonymized. The API version censors names (shows L*****).
- Financial statements: coverage varies. Larger companies file reliably. Smaller sp. z o.o. may skip filings.
- CRBR data is self-reported by companies. Generally reliable but not independently verified.

### Update Frequency
- KRS: Updated within days of court filings. PDFs reflect the current state at time of download.
- eKRS financials: Annual filings, typically available 3-9 months after fiscal year end.
- CRBR: Companies must report changes within 7 days. Data is near-real-time.

### Access Method
- **KRS Board Members**: `regdata/krs-fullnames-scraper` - downloads PDF extracts and parses full names
- **KRS Financials**: `regdata/poland-krs-financial-scraper` - extracts balance sheet and P&L data
- **CRBR**: `regdata/crbr-beneficial-owners-scraper` - queries by NIP or KRS number
- Manual: https://ekrs.ms.gov.pl (free, but API anonymizes names)

### Unique Advantages
- KRS PDF extracts are the only source of non-anonymized board member names in Poland. No other public source provides this.
- Combining KRS (officers) + CRBR (owners) + eKRS (financials) gives a complete company profile unavailable from any single source.

### Limitations
- No email or phone in any Polish registry. Officer names must be matched to LinkedIn or other sources for contact details.
- No industry/activity code in KRS itself (PKD codes are in GUS/REGON, which is a separate system).
- Financial data is only available for companies that have filed - coverage is not 100%.

---

## Austria (AT)

### Official Registries
- **WKO Firmen A-Z** - Chamber of Commerce (Wirtschaftskammer) business directory. Mandatory membership for all Austrian businesses.
- **Firmenbuch** - Commercial register maintained by courts. Legal entity data, officers, share capital.
- **Ediktsdatei** - Insolvency publication portal (relevant for credit risk, not lead gen).

### What Is Publicly Available
- Company name, full address, postal code, city, federal state (Bundesland)
- Phone number, email address, website URL
- Industry classification (Branche), business description
- Trade licenses (Gewerbeberechtigungen), certifications
- WKO membership details

### Data Quality and Completeness
- WKO data quality is high - businesses maintain their listings because it serves as their official directory presence
- Contact info coverage: phone is available for most businesses. Email and website are available for a significant portion but not all.
- Industry classification is based on trade licenses, which are precise and legally defined.

### Update Frequency
- WKO directory is maintained by businesses themselves. Changes typically reflect within days.
- 620,000+ active business listings as of 2026.

### Access Method
- **WKO Directory**: `regdata/wko-business-directory-scraper` - searches by keyword, industry, state, and district
- Manual: https://firmen.wko.at (free public access, but no bulk export)

### Unique Advantages
- The only registry in our coverage that includes email, phone, and website directly in the data. No enrichment step needed.
- Trade license data provides precise activity classification - more specific than generic industry codes.
- Mandatory membership means coverage is near-complete for Austrian businesses.

### Limitations
- No individual officer/director names in WKO. For named decision-makers, you would need the Firmenbuch (not currently covered by our actors).
- No financial data. Revenue, employee count, and balance sheets are not part of the WKO directory.
- Some contact details may be outdated if the business has not updated their listing recently.

---

## Spain (ES)

### Official Registries
- **Registro Mercantil (via OpenData Registradores)** - Commercial register. Company identification, officers, activity codes.
- **BORME (Boletin Oficial del Registro Mercantil)** - Official gazette publishing daily corporate acts: incorporations, appointments, capital changes, dissolutions.
- **CNMC** - Competition authority registry (niche, not covered).

### What Is Publicly Available
- Company name (denominacion), NIF/CIF (tax ID), legal form, company status (active/dissolved)
- Registered address (domicilio social), province
- Named officers (cargos) with roles - Administrador, Consejero, Secretario, etc.
- CNAE economic activity codes
- Daily corporate acts: new companies, officer changes, capital modifications, mergers, dissolutions

### Data Quality and Completeness
- Registro Mercantil data is authoritative for registered companies. Coverage of SL (Sociedad Limitada) and SA (Sociedad Anonima) entities is comprehensive.
- Officer names are complete and not anonymized.
- CNAE codes provide reliable industry classification.
- BORME is published every business day with no omissions - it is the official gazette.

### Update Frequency
- Registro Mercantil: Reflects filings. New companies appear within weeks of registration.
- BORME: Published daily (business days). Acts appear 1-3 weeks after the underlying event.

### Access Method
- **Company Directory**: `regdata/spain-company-directory-scraper` - search by name, NIF, CNAE code, or province
- **BORME Corporate Acts**: `regdata/borme-corporate-acts-scraper` - parse daily PDFs by date range, province, and act type
- Manual: https://www.registradores.org/directorio (limited search without bulk export), https://www.boe.es/diario_borme/ (PDFs, not structured)

### Unique Advantages
- BORME provides a daily feed of corporate events - the only registry in our coverage with real-time trigger data for prospecting.
- Combining Registro Mercantil (company profile) + BORME (recent events) gives both static profile data and dynamic signals.
- CNAE codes enable precise industry targeting without ambiguity.

### Limitations
- No contact info (phone, email, website) in either registry. Spanish registries focus on legal/corporate data.
- The Registro Mercantil search interface has WAF protection and occasional CAPTCHAs. The actor handles this automatically but it can slow large extractions.
- BORME acts are text-heavy and sometimes require interpretation. Officer names in BORME are embedded in free-text paragraphs, not structured fields.

---

## France (FR)

### Official Registries
- **Societe.com** - Aggregator of INSEE (national statistics), INPI (industrial property/commercial court), and BODACC (official civil and commercial announcements). Not a government registry itself but the richest free consolidation of French company data.
- **INSEE/SIRENE** - Official register of SIREN/SIRET numbers and NAF activity codes.
- **INPI (Data INPI)** - Commercial court filings, officer appointments, financial statements.
- **BODACC** - Official announcements: incorporations, modifications, dissolutions, collective proceedings.

### What Is Publicly Available
- Company identifiers: SIREN (9-digit), SIRET (14-digit establishment), TVA (EU VAT number)
- Legal form (SAS, SARL, SA, etc.), NAF/APE activity code, creation date
- Named directors with roles (President, Directeur General, Gerant) and appointment dates
- Simplified financial data: annual revenue (chiffre d'affaires) and net result
- Shareholders and ownership percentages
- Subsidiaries and corporate group relationships

### Data Quality and Completeness
- SIREN/SIRET data is authoritative - assigned by INSEE at company creation.
- Director data is sourced from commercial court filings and is generally complete for active companies.
- Financial data availability depends on filing obligations. SAS and SARL companies may opt for confidentiality on certain figures.
- Societe.com's aggregation introduces a small lag vs. primary sources but provides the most complete picture in a single place.

### Update Frequency
- INSEE data: Updated continuously as companies register or modify.
- Director data: Reflects commercial court filings, typically within weeks.
- Financial data: Annual filings, available 3-12 months after fiscal year end depending on the company.

### Access Method
- **Societe.com**: `regdata/societe-com-scraper` - search by company name, SIREN, or director name. Includes optional financials and director pages.
- Manual: https://www.societe.com (free access, but no bulk export and aggressive anti-bot measures)

### Unique Advantages
- Director search by name is unique to Societe.com - find all companies associated with a specific person.
- Financial data (revenue, net result) enables prospect qualification by company size without needing a separate data provider.
- Corporate group mapping (shareholders + subsidiaries) reveals holding structures useful for enterprise sales.

### Limitations
- No user proxy or API key needed. Societe.com has anti-bot protections that block datacenter IPs, but the actor clears them internally (that cost is already in the per-result price).
- No phone or email in the data. Contact details must be sourced separately.
- Financial confidentiality: Some smaller companies exercise their right to keep revenue figures private.
- Data freshness depends on Societe.com's own aggregation cycle - there can be a lag of weeks to months vs. primary sources.

---

## Combining Sources for Complete Prospect Profiles

No single registry provides everything a sales team needs. The strongest approach combines multiple sources:

| Data Need | Best Source | Backup Source |
|---|---|---|
| Company identification | KRS (PL), WKO (AT), Spain Dir (ES), Societe.com (FR) | - |
| Decision-maker names | KRS Board (PL), Spain Dir (ES), Societe.com (FR) | BORME for recent appointments (ES) |
| Direct contact info | WKO (AT) | None - other countries require external enrichment |
| Industry classification | WKO Branche (AT), CNAE (ES), NAF (FR) | - |
| Financial data | eKRS (PL), Societe.com (FR) | - |
| Ownership structure | CRBR (PL), Societe.com (FR) | - |
| New company signals | BORME (ES) | - |
| Company status/health | Spain Dir (ES), KRZ/MSiG for insolvency (PL), Ediktsdatei (AT) | - |

**Recommended enrichment order**: Registry data first (structured, reliable, cheap) - then LinkedIn for contact details - then email finder tools for outreach addresses. Registry data provides the foundation that makes every subsequent enrichment step more accurate.
