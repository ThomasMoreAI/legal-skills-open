---
name: israeli-company-lookup
title: Israeli Company Lookup
description: Look up Israeli company information and understand business entity types. Use when user asks about Israeli companies, "chevra", business registration, "Rasham HaChevarot", company numbers, entity types, or needs to register a business in Israel. Covers Ltd companies, partnerships, non-profits (amuta), cooperatives, and sole proprietors. Do NOT use for non-Israeli corporate registries or stock market analysis.
author: skills-il
author_url: https://github.com/skills-il/government-services/tree/master/israeli-company-lookup
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: il
practice: corporate
language: en
---

# Israeli Company Lookup

## Instructions

### Step 1: Identify the Need
| Request | Approach |
|---------|----------|
| Look up existing company | Search by name/number at Rasham |
| Choose entity type | Compare types by liability, tax, complexity |
| Register new business | Step-by-step guide per entity type |
| Due diligence check | Verify status, directors, filings |

### Step 2: Company Search
Search the Israel Corporations Authority (rashut hatagidim):
- URL: `https://ica.justice.gov.il/GenericCorporarionInfo/SearchCorporation?unit=8`
- Search by: Company name (Hebrew or English) or company number
- Free basic info: company number, name, type, limited/unlimited, legal status, registered address, purpose, annual-fee debts, and whether the company has been declared "in breach of law" (mufrat hok)
- Paid full extract (nesach chevra): submit at `https://ica.justice.gov.il/Request/OpenRequest?rt=CompanyExtract`. Approximately 15 EUR / 53 NIS per extract (2026; verify on the request form)
- For amutot (NPOs) and CHL"Tz, use GuideStar instead: `https://www.guidestar.org.il` (free; consolidated Ministry of Justice portal)
- For partnerships (shutfut), use `https://ica.justice.gov.il/Request/OpenRequest?rt=PartnershipExtract`
- Status values (2026): pe'ila (active), be-piruq (in liquidation), nimekhqa (struck off), mufrat hok (in breach of law -- e.g. unpaid annual fees, missing reports)

### Step 3: Entity Type Comparison
| Factor | Chevra Baam (Ltd) | Osek Morsheh | Amuta |
|--------|-------------------|-------------|-------|
| Liability | Limited to investment | Personal, unlimited | Limited |
| Tax | Corporate rate ~23% | Personal brackets | Exempt (conditions) |
| Registration | Rasham, approximately 2,559 NIS online or 3,123 NIS paper (2026; verify at ica.justice.gov.il) | Tax Authority, free | Rasham HaAmutot |
| Annual filing | Yes (financial statements) | Tax returns only | Yes (report to Rasham) |
| Minimum directors | 1 | N/A | 2 board members |
| Best for | Companies, startups | Freelancers, small biz | Non-profits, social |

### Step 4: Registration Steps (Chevra Baam -- most common)
1. Choose unique company name (check availability at Rasham)
2. Draft Articles of Association (takanon)
3. File incorporation documents at Rasham HaChevarot
4. Pay registration fee (approximately 2,559 NIS online or 3,123 NIS paper (2026; verify at ica.justice.gov.il))
5. Receive Certificate of Incorporation (teuda le-hitaagdut)
6. Register with Tax Authority for income tax and VAT
7. Open business bank account with incorporation certificate
8. Register with Bituach Leumi as employer (if hiring)

## Examples

### Example 1: Company Lookup
User says: "Look up the company Monday.com"
Result: Monday.com Ltd, Company No. 51-530820-1, Status: Active, Type: Public Company (listed on NASDAQ)

### Example 2: Choose Entity Type
User says: "I'm a freelance developer, what business structure should I use?"
Result: Compare Osek Morsheh (simplest) vs. Chevra Baam (limited liability). Recommend Osek Morsheh for starting, switch to Chevra Baam when annual revenue exceeds ~400K NIS or liability protection needed.

### Example 3: Compare Entity Types
User says: "I'm starting a business in Israel, should I register as an Osek Murshe or a Chevra?"
Actions:
1. Compare entity types (Osek Patur, Osek Murshe, Ltd company) by criteria -- tax rates, liability, NI contributions, compliance burden, VAT obligations
Result: Side-by-side comparison table with recommendation based on expected annual turnover.

## Bundled Resources

### Scripts
- `scripts/search_company.py` - Display Israeli business entity types (Chevra Baam, Osek Morsheh, Amuta, etc.) with side-by-side comparison of liability, tax rates, and registration requirements, plus step-by-step Chevra Baam incorporation instructions. Supports subcommands: `entity-types`, `compare`, `registration-steps`. Run: `python scripts/search_company.py --help`

### References
- `references/entity-types.md` - Comprehensive table of all 8 Israeli business entity types with their registries, liability structures, tax rates, and company number format prefixes (51- for companies, 58- for non-profits, 55- for partnerships). Consult when advising users on entity type selection or interpreting company registration numbers.

## Gotchas
- Israeli company registration numbers (mispar chevra) are 9 digits, not the same as the tax ID (mispar osek). Agents may confuse these two identifiers or use one when the other is required.
- The Companies Registrar (Rasham HaChavarot) database contains Hebrew-only company names. Agents may search using English company names, which will return no results.
- Company status in the registrar has four values: "active" (pe'ila), "in liquidation" (be-piruq), "struck off" (nimekhqa), and "in breach of law" (mufrat hok). Agents that only check for "active" miss the "in breach" case, which is common (unpaid annual fees, late reports) and is a significant due-diligence red flag.
- Israeli business types include Chevra Baam (Ltd.), Shutafut (Partnership), Amuta (NPO), and Aguda Shitufit (Cooperative). Each has different registration systems. Agents may search for a partnership in the company registrar, which only lists Ltd. companies.
- Amutot and CHL"Tz (Public-Benefit Companies) live on GuideStar (`guidestar.org.il`), the Ministry of Justice's consolidated NPO portal -- not on the main `ica.justice.gov.il` search. Both extracts are free.
- Israel's UBO (Ultimate Beneficial Owner) registry is NOT yet operational. A Ministry of Justice memorandum was published for public consultation on 2025-06-26 (consultation closed 2025-07-17); the law is still pre-enactment as of May 2026, and when enacted the registry will NOT be publicly accessible (regulated entities and authorities only). Do not promise public UBO lookup until enactment + a public-access tier exists.
- "Apotropos Klali" (Official Receiver) was renamed to "ha-memuneh al chadlut pira'on ve-shikum kalkali" (Insolvency and Economic Rehabilitation Commissioner) when the Insolvency and Economic Rehabilitation Law 2018 took effect on 2019-09-15. For cases opened on or after that date, the searchable docket lives at `insolvency.justice.gov.il/poshtim/main/tikim/wfrmlisttikim.aspx`. Older "psikat regel" files predating 2019 are still under the legacy Apotropos Klali system.

## Reference Links

| Source | URL | What to Check |
|--------|-----|---------------|
| Companies Registrar (ICA / rashut hatagidim) | https://ica.justice.gov.il | Company search, status, filings, ownership |
| Free company snapshot | https://www.gov.il/en/service/company_extract | Basic info free; full extract paid (approximately 53 NIS / 15 EUR, 2026) |
| GuideStar (Amutot + CHL"Tz) | https://www.guidestar.org.il | Consolidated MoJ portal for NPOs and public-benefit companies. Free extracts |
| Partnership extract | https://ica.justice.gov.il/Request/OpenRequest?rt=PartnershipExtract | Nesach shutfut from Rasham HaShutfuyot |
| data.gov.il - ica_companies | https://data.gov.il/dataset/ica_companies | Bulk dump of companies registrar (CKAN API available) |
| Reshumot - Yalkut HaPirsumim | https://www.gov.il/he/Departments/DynamicCollectors/gazette-official | Official gazette: liquidation notices, dissolution petitions, creditor calls |
| Insolvency Commissioner (post-2019 cases) | https://insolvency.justice.gov.il/poshtim/main/tikim/wfrmlisttikim.aspx | Searchable case list under Insolvency and Economic Rehabilitation Law 2018 |
| Apotropos Klali (legacy pre-2019 files + general guardianship) | https://www.gov.il/he/departments/the_official_receiver | Older psikat regel files, kintus nechasim |
| Israel Tax Authority | https://www.gov.il/he/departments/israel_tax_authority | Verify business TIN (mispar osek) separately |
| NBCTF sanctions designations | https://nbctf.mod.gov.il/en/Minister%20Sanctions/Designation/Pages/downloads.aspx | Counter-Terrorism Law 2016 designations of sanctioned individuals and entities. Critical for due-diligence on Israeli counterparties post-Iron-Swords. |
| Israel Securities Authority (ISA) licensed entities | https://www.isa.gov.il | Portfolio managers, investment advisors, marketers (public licensed list) |
| Capital Market Authority (CMA) registries | https://www.gov.il/he/departments/capital_markets_insurance_savings_authority | Licensed insurers, pension funds, kupot gemel, investment houses |

## Troubleshooting

### Error: "Company not found"
Cause: Name spelling mismatch or company registered under different name
Solution: Try Hebrew name, or search by company number if available. Some companies register with English names different from their trading name.

### Error: "Company number format invalid"
Cause: Israeli company numbers (Chevra) are 9 digits; sole proprietor numbers match their TZ (ID); partnership and amuta numbers differ
Solution: Verify the entity type first. Companies: 51-XXXXXXX (9 digits), Amutot: 58-XXXXXXX, Partnerships: 55-XXXXXXX. Use the Rasham HaChevarot search to validate.

### Error: "Entity type confusion (Osek Patur vs Osek Morsheh)"
Cause: Users confuse tax registration types with company registration types
Solution: Osek Patur/Morsheh are VAT registration types at the Tax Authority (SHAAM), not company types at the Registrar of Companies. A person can be an Osek Morsheh without registering a company. Clarify the user's actual need: business entity lookup vs. tax registration status.

### Error: "Cannot find the amuta on ica.justice.gov.il"
Cause: Amutot and CHL"Tz are not in the main companies database
Solution: Search on GuideStar (`https://www.guidestar.org.il`) instead. It is the Ministry of Justice's consolidated portal for amutot and public-benefit companies. Basic extract is free.

### Error: "User asks for beneficial owner / UBO lookup"
Cause: User assumes Israel has a public UBO registry (similar to UK Companies House PSC register)
Solution: As of May 2026, Israel has NO operational UBO registry. The MoJ memorandum was published 2025-06-26 for public comment (closed 2025-07-17); the law is still pre-enactment and, when enacted, the registry will NOT be publicly accessible. For now, the closest signals are: directors and shareholders listed on a paid full company extract, the company's filed annual report (dorech shanati), and (for public companies only) ISA disclosures on Maya at `maya.tase.co.il`.
