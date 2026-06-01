---
name: israeli-standards-import-checker
title: Israeli Standards Import Checker
description: Check whether a product requires Standards Institution of Israel (SII, Mechon HaTikanim) approval under an official standard (takan rishmi) before it can be imported into Israel. Returns applicable SI numbers, approval route (type approval, shipment approval, Maslol Plus declaration, EU-CoC recognition), required lab tests, timelines, and fast-track options based on the 2016 food parallel-import reform, the 2022 electronics reform, the 2025 EU-regulation reform (Amendment 19), and the November 2025 proposed US-standards Amendment 21. Use when a user asks about importing electronics, toys, cosmetics, food-contact materials, vehicles, or building materials into Israel, asks about CE/type approval, or has a shipment stuck at Israeli customs. Do NOT use for customs duty calculation (use israeli-customs-duty-calculator) or for general product safety review outside the Israeli regulatory context.
author: skills-il
author_url: https://github.com/skills-il/security-compliance/tree/master/israeli-standards-import-checker
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: il
practice: regulatory
language: en
---

# Israeli Standards Import Checker

## Problem

Products regularly get stuck, seized, or fined at Israeli customs when the importer fails to show compliance with a mandatory Israeli Standard (takan rishmi). The rules changed substantially with the 2022 electronics reform, the January 2025 "What's Good for Europe is Good for Israel" EU-recognition reform (Amendment 19), and the November 2025 proposed Amendment 21 that opens a parallel US-standards track. Per Minister of Economy Nir Barkat, the EU adoption now touches about 444 of Israel's 573 mandatory standards. Even with all of that progress, the old "just use CE" shortcut still does not work for many categories (for example AC mains electrical equipment in the 50-1000 V range). Importers and their advisors need a structured way to check, per product, which SI number applies, which approval route is open, and what documentation the shipment must carry through the Sha'ar Olami customs system.

## Instructions

Always state at the start: this skill gives regulatory guidance, not legal advice. For a specific shipment, verify the current mandatory standards list on the SII website and consult the Commissioner of Standardization or a licensed customs broker.

### Step 1: Identify the product category

Ask for, or infer from the user's input:
- Product type (e.g., LED lamp, children's ride-on toy, hair dryer, infant formula, plastic food container, passenger car, drone)
- Intended use (consumer, commercial, industrial)
- Voltage / power rating for electrical products
- Age range for toys
- Whether it is a personal import (ye'vu ishi) or commercial

### Step 2: Check whether the category has an official Israeli Standard (takan rishmi)

A takan rishmi is mandatory; a plain takan yisra'eli is voluntary. Only the Minister of Economy can declare a standard mandatory, and the Commissioner of Standardization enforces it. The master list lives on the SII website and is updated through the official gazette Reshumot.

The Commissioner of Standardization runs a dedicated EU-regulation search engine on the Ministry of Economy site (https://www.gov.il/en/service/search_official_standards). Enter the Israeli Standard (SI) number and it returns the corresponding EU regulation(s), their effective dates, and the product's import group. Use it before picking a route.

Common categories with mandatory standards (current as of May 2026; verify against the live Reshumot list before filing):

| Category | Typical SI | Notes |
|---|---|---|
| Toys | SI 562 (parts 1, 2, 3, 7 ...) | Based on EN 71. Part 1 last revised November 2022 (transition to 16 April 2023); part 3 (chemical migration) also revised in the same window. Toy safety joined the EU-recognition catalogue from Feb/Mar 2025. |
| Household electrical appliances | SI 900 family (equivalent to IEC 60335-1) | Many sub-parts are mandatory (e.g., 2.5 dishwashers, 2.29 chargers). |
| Plastic food-contact materials | SI 5113 | Accepts US FDA or EU Directive as fallback. |
| Cosmetics | Pharmacists' Regulations (Cosmetics) 5783-2022, MoH notification | Post-reform: notification only for EU-compliant products, registration fee cancelled. Cosmetics also entered the EU-recognition catalogue in the July 2025 wave. |
| Passenger vehicles | Israeli Mandatory Requirements (IMR) | Adopts EU 2018/858 WVTA; US/Canadian homologation accepted. Excluded from Amendment 19. |
| Food | Various public-health regulations | Covered by the 2016 food-import reform (parallel import + Model A/B). Excluded from Amendment 19. |

### Step 3: Identify the import group, then determine the approval route

First find the product's import group. Israel splits products subject to official standards into four risk-based import groups, and the group determines how heavy the conformity assessment is:

- **Group 1, highest risk** (for example products for infants, LPG equipment, lifting devices, rebar): requires both a testing-lab model approval and a testing-lab shipment inspection.
- **Group 2, medium risk** (for example external power supplies above a certain output): requires a model certificate plus an importer's declaration that the shipment conforms to the official standard.
- **Group 3, low risk** (most products, for example computers, TVs, most household electrical appliances): requires an importer's declaration of conformity only.
- **Group 4, industrial use only**: products intended for use only in industry; no import conformity assessment, released by the Commissioner of Standardization route.

Find a product's group via the Commissioner's EU-regulation search engine (https://www.gov.il/en/service/search_official_standards) keyed by SI number.

Then pick the route that fits the group and reform status:

1. Type approval (ishur tipus) by SII: covers a specific model; once granted, subsequent shipments of the same model can use shipment approvals or an easement plan. Required for categories still excluded from EU recognition (for example AC mains electrical equipment 50-1000 V AC / 75-1500 V DC). Aligns with the Group 1 "model approval" step.
2. Per-shipment approval: each shipment is sampled and tested before release. This is the Group 1 "shipment inspection" step, and is also the default for new importers without a clean history.
3. Importer easement plans via Maslol Plus: Green (50% sample), Gold (33% sample after 12 months on Green), Diamond (sell before testing completes). These plans lighten the per-shipment burden for importers of higher-risk (Group 1) goods who have a clean import history and an ISO 9001 factory.
4. Declaration-based entry: from July 1, 2024, importers can declare compliance using ILAC-accredited foreign lab reports; spot-checked under the Ministry of Economy's random-surveillance programme (from July 7, 2024). Lower-risk groups (2 and 3) already rely primarily on an importer declaration.
5. EU-CoC / EU-regulation recognition: from January 1, 2025 Israel began phasing EU regulations into the Standards Law under Amendment 19 (about 69 EU regulations adopted as of early 2026, touching roughly 444 of Israel's 573 mandatory standards per Minister Barkat, phased in stages from 2025 through 2028). REACH, LVD, EMC, and PPE came first; toys and food-contact materials phased in from February/March 2025; a July 2025 wave added hazardous materials, medical devices, elevators and wheelchair lifts, construction materials, batteries, and cosmetics. The route is declaratory: customs brokers submit through Sha'ar Olami and the importer keeps a compliant product file. For the first five years (2025-2030) enforcement focuses only on compliance with adopted directive requirements that correspond to parallel sections of the official Israeli standards. Food, motor vehicles, official fire-safety-covered items, and AC mains electrical equipment 50-1000 V AC / 75-1500 V DC are excluded.
6. Radio / wireless: under the July 4, 2022 Ministry of Communications amendment, DoC/CoC compliant with EU regulations is accepted for radio equipment.
7. US-standards recognition (Amendment 21, proposed November 2025): a draft Amendment 21 to the Standards Law was introduced in November 2025 to mirror the EU-recognition model for compliance with US Federal Regulations. The first administrative phase, announced in March 2025, is expected in the second half of 2026 and covers children's products (toys, baby furniture, mattresses, pacifiers, feeding accessories, swings, trampolines, children's jewelry), bicycles, ladders, lighters, crockery and food packaging, and cleaning materials. Confirm the current category list with the Ministry of Economy before relying on it; as of May 2026 Amendment 21 is not yet primary legislation.

### Step 4: List required lab tests and documents

Typical documentation package:
- Manufacturer test report from an ILAC-accredited lab
- Product file (tik mutzar) with technical drawings, BOM, and user manual (Hebrew required for consumer products)
- CE Declaration of Conformity and EU test reports (for the EU recognition route)
- Importer declaration form and Maslol Plus submission
- Sample units for SII testing when the route requires it

For customs release the licensed customs broker files the declaration through the Israel Tax Authority's Sha'ar Olami (Global Gateway) system (https://shaarolami-query.customs.mof.gov.il/), which is the production electronic clearance platform; the SII permit, importer declaration, and test reports must be attached to that filing.

### Step 5: Estimate a timeline

Give a rough band and flag that exact turnaround depends on SII queue, category, and whether the product file already exists. Do not invent fee numbers; point the user to the SII importer service centre for the current fee schedule:
- Electrical: 03-6465160
- Electronics: 03-6465050
- Chemicals / health / environment: 03-6465138
- Mechanics / hydraulics: 03-6465141

### Step 6: Flag fast-track options

If the product qualifies for the EU-recognition route, the declaration-based route, or an easement plan, recommend that as the primary filing. Note the residual risk: random surveillance can still sample the shipment, and a failed sample can trigger market withdrawal and fines.

### Step 7: Check labeling, marking, and exemption thresholds

Labeling and marking:
- Consumer products need Hebrew labeling and a Hebrew user manual.
- The label must carry the importer's details (name and address).
- Products certified by the SII carry the SII mark; do not claim it unless the product file supports it.

Exemptions and thresholds (confirm the current rule before relying on it):
- Personal imports (ye'vu ishi) follow a lighter regime and often fall under quantity thresholds that exempt them from full conformity assessment, but the exemption never covers resale.
- Samples and prototypes can qualify for a limited exemption when they are not placed on the market.
- Group 4 products (industrial use only) are released through the Commissioner of Standardization route without an import conformity assessment.
- The old blanket exemption route was discontinued on July 7, 2024 and replaced by the declaration-based path plus random surveillance.

### Step 8: Warn about non-compliance consequences

Imports arriving without the correct approval can be held, seized, or destroyed at customs. Businesses are legally obliged to notify the Commissioner of Standardization if a product later fails to meet mandatory requirements.

## Examples

### Example 1: CE-marked children's ride-on toy

User says: "I want to import a CE-marked electric ride-on car for toddlers from a European brand."
Result: Toys are covered by SI 562 (mandatory, based on EN 71). From February 2025, toy safety is in the EU-recognition catalogue, so CE plus a DoC aligned with the Toy Safety Directive can potentially use the EU route. The battery and motor parts may still trigger SI 900 (electrical safety), which is not yet in the EU fast-track. Recommend: open a product file with SII Electrical (03-6465160), submit via Maslol Plus, keep the EN 71 test report and EU DoC with the shipment.

### Example 2: Imported hair dryer (220 V)

User says: "We're bringing 500 hair dryers from China."
Result: Hair dryers are household electrical appliances under the SI 900 family. Because AC mains equipment in the 50-1000 V range is still excluded from the January 2025 EU-recognition fast track, CE alone is not enough. Route: type approval by SII plus per-shipment sampling, or Green/Gold easement plan once a clean record is built. Ensure the manual is in Hebrew.

### Example 3: EU-compliant skincare cream

User says: "A French brand wants to sell a moisturiser in Israel."
Result: Covered by the Pharmacists' Regulations (Cosmetics) 5783-2022. The reform replaced the old SII + MoH registration pathway with a notification to the Israeli Ministry of Health confirming EU compliance. Registration fee is cancelled. No SII lab test required if the EU dossier is in order, but keep the EU CPNP file and safety assessment available.

## Bundled Resources

### References

- `references/common-official-standards.md` - Table of common product categories and their SI (Israeli Standard) numbers. Consult when you need to look up the standard number for a specific product type.
- `references/approval-routes.md` - Decision guide between type approval, shipment approval, easement plans, declaration-based entry, and EU-CoC recognition. Consult when picking a filing route.
- `references/fast-track-options.md` - Rules for the 2016 food parallel-import reform, the 2022 electronics/radio reforms, and the 2025 EU-regulation recognition catalogue. Consult when assessing whether a shortcut applies.

### Scripts

- `scripts/check_standard.py` - Hardcoded rules engine that takes a product category and returns applicable SI numbers, whether the standard is mandatory, the recommended approval route, required tests, and typical timeline band. Run: `python scripts/check_standard.py --category toy` or `--list` to see supported categories.

## Recommended MCP Servers

No MCP server currently wraps the SII or the Commissioner of Standardization. Until one exists, verify live standards lists directly on the SII website (https://www.sii.org.il) and the Ministry of Economy's standardization policy page. A future MCP could expose Maslol Plus and the Reshumot gazette.

## Gotchas

- Voluntary (takan yisra'eli) vs official (takan rishmi) is a frequent trap. A product can meet a standard that is not mandatory and still be blocked at customs because a different mandatory standard applies.
- The EU-recognition route covers only the regulations adopted into the Standards Law under Amendment 19 (about 69 EU regulations adopted as of early 2026, phased in from 2025 through 2028; REACH, LVD, EMC, PPE first, toys and food-contact materials added Feb/Mar 2025, a July 2025 wave covering hazardous materials, medical devices, elevators, construction materials, batteries, and cosmetics). AC mains electrical equipment 50-1000 V AC / 75-1500 V DC is explicitly excluded; food, motor vehicles, and items under official fire-safety standards are also excluded. Agents often assume CE is now universally accepted; it is not.
- Import-group risk direction is a frequent trap. Group 1 is the HIGHEST risk and carries the heaviest assessment (model approval plus shipment inspection); Group 3 is low risk and needs only an importer declaration; Group 4 is industrial-use-only with no import conformity assessment. Do not assume higher group numbers mean higher risk.
- A type approval (ishur tipus) covers a specific model only. Sister models, different voltages, or firmware variants need fresh filings.
- Samples must usually be sent and tested before the shipment arrives, not after. Planning the test slot late is a common delay cause.
- Israeli standards are revised by publication in Reshumot, sometimes with very short transition windows (SI 562 part 3 gave only five months in 2022-2023). Always check the current version, not a cached PDF.
- Personal imports (ye'vu ishi) follow a lighter regime than commercial imports and often pass under exemption thresholds, but the exemption does not cover resale. The personal-import VAT/purchase-tax exemption ceiling has changed three times in six months: raised from USD 75 to USD 150 by ministerial order in December 2025, revoked by the Knesset on 24 February 2026, and reset to USD 130 by a fresh Finance Ministry order effective midnight 24-25 February 2026. As of May 2026 the current threshold is USD 130. This affects duty-and-tax math, not the standards regime, but importers often conflate the two; for the customs side use the `israeli-customs-duty-calculator` skill.
- The Amendment 19 EU route is declaratory: the importer signs and files a declaration through Sha'ar Olami, no SII pre-test is needed. The trap is that random surveillance after release can still pull samples and fines apply if the dossier turns out to be incomplete. Keep every CE/DoC/test report indexed and retrievable.
- Amendment 21 (US-standards recognition) is still a proposal as of May 2026, not law. Treat US-standards-only documentation as supporting evidence inside an Israeli filing, not as a stand-alone import route, until the amendment is published in Reshumot.

## Reference Links

| Source | URL | What to check |
|---|---|---|
| SII home (English) | https://www.sii.org.il/en | Contact centres, standards, certifications |
| SII importers | https://www.sii.org.il/en/importers/ | Maslol Plus filing, importer contact emails |
| SII easement plans | https://www.sii.org.il/en/tracks/ | Green / Gold / Diamond plan rules, ISO 9001 eligibility |
| Commissioner of Standardization (Ministry of Economy) | https://www.gov.il/en/departments/general/standartization_policy_in_israel_legislation | Enforcement policy, mandatory standards, Reshumot |
| Official EU-regulation / SI search engine | https://www.gov.il/en/service/search_official_standards | Look up an SI number to get the matching EU regulation, effective dates, and import group |
| Sha'ar Olami (Customs Global Gateway) | https://shaarolami-query.customs.mof.gov.il/ | Electronic clearance system: customs broker files the SII/declaration package here |
| US ITA Israel standards reform | https://www.trade.gov/market-intelligence/israel-standards-reform | Plain-English overview of EU-recognition and the declaration route |
| Kol Zchut | https://www.kolzchut.org.il | Consumer rights on imports (Hebrew) |

## Troubleshooting

### Error: "Customs is holding our shipment, says no standards certificate"

Cause: The product probably falls under an official standard (takan rishmi) and no type approval or declaration was filed before the container arrived.
Solution: Contact the relevant SII importer centre (electrical 03-6465160, electronics 03-6465050, chemicals 03-6465138, mechanics 03-6465141) and file retroactively via Maslol Plus. Arrange sampling at the port. If release is urgent, a customs broker can sometimes request a limited shipment approval.

### Error: "CE should be enough, why is SII still asking for tests?"

Cause: The category is outside the January 2025 EU-recognition catalogue, or the product is AC mains electrical equipment (50-1000 V AC / 75-1500 V DC) which is explicitly excluded.
Solution: Use type approval by SII or the importer easement plan instead. Keep the EU test reports, since they speed up the SII file even when full recognition is not available.

### Error: "Our factory changed component supplier; can we still use the same type approval?"

Cause: Type approvals cover a specific model configuration. Material changes can invalidate it.
Solution: Contact the SII case handler, submit the engineering change notice, and ask whether a variant approval or fresh file is required before the next shipment leaves the origin port.
