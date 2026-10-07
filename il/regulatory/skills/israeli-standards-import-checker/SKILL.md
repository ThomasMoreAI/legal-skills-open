---
name: israeli-standards-import-checker
title: Israeli Standards Import Checker
description: Not legal advice and not a filed customs declaration. Check whether a product needs Standards Institution of Israel (SII, Mechon HaTikanim) approval under an official standard (takan rishmi) before import, and which parallel permits gate the same shipment. Returns SI numbers, the import group (1-4), the approval route (type approval, shipment approval, Maslol Plus, EU recognition under Amendment 19, and the US route under Amendment 21 passed July 2026), lab tests and timelines. Also covers the Free Import Order lookup, Ministry of Communications certificates for wireless devices, electronic-waste and packaging registration, the personal-import (yevu ishi) exemption and its limits, Hebrew labelling and Shaar Olami filing. Use when a user asks about importing electronics, chargers, toys, cosmetics or building materials into Israel, commercially or by personal import, asks about CE or type approval, or has a shipment stuck at customs. Do NOT use for duty calculation.
author: skills-il
author_url: https://github.com/skills-il/security-compliance/tree/master/israeli-standards-import-checker
license: MIT
version: 0.1.2
execution_mode: open
jurisdiction: il
practice: regulatory
language: en
sources:
- title: Approval routes
  path: references/approval-routes.md
- title: Common official standards
  path: references/common-official-standards.md
- title: Fast track options
  path: references/fast-track-options.md
---

# Israeli Standards Import Checker

## Legal notice

This is a free information tool operated by an AI model. It explains the approval routes under the Standards Law and the parallel permit regimes that gate the same shipment, and points to the official sources, with no involvement, review, or approval by a licensed customs broker or a lawyer. Its output is not legal advice, not a professional opinion, and not a customs entry or declaration that has been filed. It does not determine the goods' customs classification, does not review the product's technical file, and does not verify against the current official standards list in Reshumot. An AI model can err, omit data, or present a wrong conclusion. A declaration to the customs authority is a legal document and a false statement in it carries liability, so any wording this tool produces is an automatic draft for personal organisation only, to be checked with a customs broker or the Israel Tax Authority before filing. This tool is not a substitute for advice that takes account of the particular data and needs of each person. Before filing a shipment, signing an importer's declaration, or relying on an exemption, consult a licensed customs broker, the Commissioner of Standardization, or a lawyer. Any use of the output is at the user's sole responsibility.

## Problem

Products regularly get stuck, seized, or fined at Israeli customs when the importer fails to show compliance with a mandatory Israeli Standard (takan rishmi). The rules changed substantially with the 2022 electronics reform, the January 2025 "What's Good for Europe is Good for Israel" EU-recognition reform (Amendment 19), and Amendment 21, passed on 16 July 2026, which adds a parallel US-standards track due to take effect at the start of 2027. Published counts of how many Israeli mandatory standards the EU adoption touches vary widely between sources and none of them is authoritative; the Fifth Appendix is the only place that actually says what is adopted and from when. The single most repeated myth in this area, and one earlier versions of this skill repeated too, is that mains electrical equipment is excluded from the EU route. It is not: the Fifth Appendix positively adopts the Low Voltage Directive 2014/35/EU, described in the Hebrew text as covering electrical equipment supplied at up to 1,000 volts, in force from Amendment 19's commencement, with only low-voltage electrical cables deferred to 1 January 2027. What CE alone still does not do is make the product fit the Israeli mains: the statute separately requires an electrical device to match the electricity network in use in Israel, which is where SI 32 and the Type H plug bite. Importers and their advisors need a structured way to check, per product, which SI number applies, which approval route is open, and what documentation the shipment must carry through the Sha'ar Olami customs system.

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

Common categories with mandatory standards (current as of August 2026; verify against the live Reshumot list before filing):

| Category | Typical SI | Notes |
|---|---|---|
| Toys | SI 562 (parts 1, 2, 3, 7 ...) | Based on EN 71. Part 1 last revised November 2022 (published in Reshumot 17 November 2022, transition to 16 April 2023). Toy safety joined the EU-recognition catalogue from Feb/Mar 2025. |
| Household electrical appliances | SI 900 family (equivalent to IEC 60335-1) | Many sub-parts are mandatory (e.g., 2.5 dishwashers, 2.29 chargers). |
| Plugs, sockets, splitters, extension cords | SI 32 (all parts) | Official on all its parts. Israel uses the Type H plug, so a mains product shipped with a European or Chinese plug is rejected however complete its IEC 60335 file is. Part 1.1 covers plugs and socket-outlets up to 16 A. |
| Plastic food-contact materials | SI 5113 | Accepts US FDA or EU Directive as fallback. |
| Cosmetics | Pharmacists' Regulations (Cosmetics) 5783-2023, MoH notification | Post-reform: notification only for EU-compliant products, registration fee cancelled. The Standards Law EU route for cosmetics (Regulation 1223/2009) commences only three years from Amendment 19's commencement, so it is not the operative path today; the MoH notification is. |
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

1. Type approval (ishur tipus) by SII: covers a specific model; once granted, subsequent shipments of the same model can use shipment approvals or an easement plan. Required for categories genuinely outside EU recognition (see the exclusion list in route 5) and for any product whose governing EU regulation has not yet been adopted into the Fifth Appendix. Aligns with the Group 1 "model approval" step.
2. Per-shipment approval: each shipment is sampled and tested before release. This is the Group 1 "shipment inspection" step, and is also the default for new importers without a clean history.
3. Importer easement plans via Maslol Plus: Green (50% sample), Gold (33% sample after 12 months on Green), Diamond (sell before testing completes). These plans lighten the per-shipment burden for importers of higher-risk (Group 1) goods who have a clean import history and an ISO 9001 factory.
4. Declaration-based entry: from July 1, 2024, importers can declare compliance using ILAC-accredited foreign lab reports; spot-checked under the Ministry of Economy's random-surveillance programme (from July 7, 2024). Lower-risk groups (2 and 3) already rely primarily on an importer declaration.
5. EU-CoC / EU-regulation recognition. First, know that this is one of FOUR compliance bases in section 9(a)(1), not the only alternative to the Israeli standard: (a) meeting the official standard itself; (b) meeting an international standard or foreign regulation that has been adopted, wholly or partly, INTO the official standard, except where that official standard is listed in the Third Appendix (a real carve-out, and several building materials sit in it); (c) meeting a foreign regulation outright where the official standard is listed in the Fourth Appendix; (d) the adopted European regulation, below. Bases (b), (c) and (d) all require Israeli marking, and all require an electrical device to match the electricity network in use in Israel. Now the European base: from January 1, 2025 Israel began phasing EU regulations into the Standards Law under Amendment 19 (phased in stages from 1 January 2025 through 1 January 2028; check the Fifth Appendix for the regulations actually adopted and in force before relying on this route). Every entry has its OWN commencement date and its OWN conditions, and several are years away, so "is it adopted" and "can I use it today" are different questions. `references/fast-track-options.md` carries the per-entry commencement dates; the headline points are that the Low Voltage, EMC and Radio Equipment Directives run from Amendment 19's commencement, toys and general product safety from 1 February 2025, and cosmetics, construction products, batteries and lifts are all still years out. What the conditions typically require you to hold is a manufacturer declaration and a technical file as defined in section 10e, or a conformity approval under section 12; several entries also accept a declaration from a supplier established in a "recognised state" that the product is lawfully marketed in an EU state, which helps importers who buy through a distributor. The route is declaratory: customs brokers submit through Sha'ar Olami and the importer keeps a compliant product file. For the first five years enforcement focuses only on compliance with adopted directive requirements that correspond to parallel sections of the official Israeli standards. Under section 9(a)(1) of the Standards Law the route does not apply to food, to a motor vehicle, or to any product or work process under an official fire-safety standard, except portable extinguishing equipment that is not permanently fixed to land or a building, extinguishing agents, and standalone smoke detectors, which stay inside the route.
6. Radio / wireless: importing a wireless device needs a compliance certificate (ishur hat'ama) from the Ministry of Communications under regulation 2(a) of the Wireless Telegraph (Compliance Certificates) Regulations 5781-2021. Regulation 5a, added on 7 July 2022, lets an applicant whose device matches the EU regime attach an EU conformity document plus a specification of the device's radio characteristics INSTEAD of the standard document set. That is a documentation easement inside the certificate process, not an exemption from it. Any Wi-Fi or Bluetooth function in an otherwise ordinary appliance triggers this.
7. US-standards recognition (Amendment 21): the Knesset passed the Standards Law (Amendment 21) 5786-2026 in second and third reading on 16 July 2026, opening an American route alongside the European one. It starts six months after publication, so at the beginning of 2027, and the start date can be deferred. Three conditions decide whether it helps a given shipment: the product must actually be manufactured in the United States (or in Israel); the route does not apply to food, motor vehicles, cosmetics, or products subject to fire-safety standards; and the importer must follow US recall notices and manufacturer notices and report to the Commissioner of Standardization. The first wave covers baby and children's goods, toys, bottles, drinking accessories, feeding utensils, beds, cribs, strollers, swings, bouncers, bicycles, and detergents. Until the route is in force, treat US-standards documentation as supporting evidence inside an Israeli filing, not as a stand-alone import route.

### Step 4: Check the parallel permit regimes that gate the same shipment

A standards filing is only one of the gates on a container, and the others are enforced by different authorities. Before quoting a route or a timeline, walk this list and say explicitly which items apply:

- **Free Import Order (Tzav Yevu Chofshi) 5774-2014 comes first.** It decides whether the goods need anything at all: goods listed in its First Appendix require an import licence, and goods listed in the Second Appendix are released only if the approval named in column ג of that appendix was produced and the importer attached it to the import declaration. Look the customs classification up there before working out the standards route, because that is where the other authorities (Health, Environmental Protection, Agriculture, Energy, Police, Communications) appear.
- **Ministry of Communications, for anything with a radio.** See route 6 in Step 3. A compliance certificate is required for import; the EU documentation easement does not replace it.
The next two are NOT conditions of customs release. No broker is asked for them at the port, and they do not belong in the entry package. They are market-placement duties enforced by the Ministry of Environmental Protection, and they bite after the goods are already in the country, which is exactly why importers discover them late:

- **Electronic-waste and batteries.** A producer or importer of electrical or electronic equipment or of batteries must contract with a recognised implementation body (guf yisum mukar) under section 8 of the Environmental Treatment of Electrical and Electronic Equipment and Batteries Law 5772-2012. Chargers and battery packs are squarely in scope.
- **Packaging.** A producer or importer must contract with a recognised body (guf mukar) under section 9 of the Packaging Regulation Law 5771-2011. This catches essentially every commercial shipment, not only consumer packaging.
- **Energy efficiency, for energy-consuming appliances.** The Fifth Appendix adopts ecodesign and energy labelling, but both entries expressly do NOT apply to an energy-consuming appliance in any field regulated under the Energy Sources Law 5750-1989, including energy efficiency, the energy rating, and efficiency marking. So for air conditioners, refrigerators, washing machines and similar goods the Israeli energy regime is a live separate requirement that CE cannot satisfy.

So the list splits in two: the Free Import Order and the Ministry of Communications certificate gate the container, and the environmental duties gate the marketing. An importer who clears the standards route and skips either half is still exposed.

### Step 5: List required lab tests and documents

Typical documentation package:
- Manufacturer test report from an ILAC-accredited lab
- Product file (tik mutzar) with technical drawings, BOM, and user manual (Hebrew required for consumer products)
- CE Declaration of Conformity and EU test reports (for the EU recognition route)
- Importer declaration form and Maslol Plus submission
- Sample units for SII testing when the route requires it

For customs release the licensed customs broker files the declaration through the Israel Tax Authority's Sha'ar Olami (Global Gateway) system, which is the production electronic clearance platform; the SII permit, importer declaration, and test reports must be attached to that filing.

### Step 6: Estimate a timeline

Give a rough band and flag that exact turnaround depends on SII queue, category, and whether the product file already exists. Do not invent fee numbers; point the user to the SII importer service centre for the current fee schedule:
- Electrical: 03-6465160
- Electronics: 03-6465050
- Chemicals / health / environment: 03-6465138
- Mechanics / hydraulics: 03-6465141

### Step 7: Flag fast-track options

If the product qualifies for the EU-recognition route, the declaration-based route, or an easement plan, recommend that as the primary filing. Note the residual risk: random surveillance can still sample the shipment, and a failed sample can trigger market withdrawal and fines.

### Step 8: Check labeling, marking, and exemption thresholds

Labeling and marking:
- Consumer products need Hebrew labeling and a Hebrew user manual.
- The label must carry the importer's details (name and address).
- Products certified by the SII carry the SII mark; do not claim it unless the product file supports it.

Exemptions and thresholds (confirm the current rule before relying on it):
- Personal imports (ye'vu ishi) follow a lighter regime, but the statutory conditions are narrower than most people assume. Section 9(a)(2)(a) exempts personal or family import only where no licensed professional is required by law to install, operate or maintain the product, and only under the personal-import rules made under section 2 of the Import and Export Ordinance. That professional-installation cut-off is what actually catches air conditioners, water heaters and gas appliances bought abroad. Section 9(a)(3) then removes the exemption entirely for food, for motor vehicles including pedal-assist bicycles with an auxiliary motor, and for any product or device intended for medical use. The exemption never covers resale.
- Samples and prototypes can qualify for a limited exemption when they are not placed on the market.
- Group 4 products (industrial use only) are released through the Commissioner of Standardization route without an import conformity assessment.
- The old blanket exemption route was discontinued on July 7, 2024 and replaced by the declaration-based path plus random surveillance.

### Step 9: Warn about non-compliance consequences

Imports arriving without the correct approval can be held, seized, or destroyed at customs. Businesses are legally obliged to notify the Commissioner of Standardization if a product later fails to meet mandatory requirements.

## Examples

### Example 1: CE-marked children's ride-on toy

User says: "I want to import a CE-marked electric ride-on car for toddlers from a European brand."
Result: Toys are covered by SI 562 (mandatory, based on EN 71). The Toy Safety Directive entered the Fifth Appendix on 1 February 2025, so CE plus a DoC aligned with it can use the EU route. Read the entry's condition first, because this product fails it by default: the directive does NOT apply to toys for children under 3 unless the trader holds a manufacturer declaration AND a technical file as defined in section 10e, or a conformity approval under section 12. A ride-on car for toddlers is squarely under 3, so the EU route is open here only if that dossier exists. The battery and motor parts may still trigger SI 900 (electrical safety), which is not yet in the EU fast-track. Recommend: open a product file with SII Electrical (03-6465160), submit via Maslol Plus, keep the EN 71 test report and EU DoC with the shipment.

### Example 2: Imported hair dryer (220 V)

User says: "We're bringing 500 hair dryers from China."
Result: Hair dryers are household electrical appliances under the SI 900 family, and the Low Voltage Directive is adopted into the Fifth Appendix, so the EU route is open in principle. Two things still have to hold. The unit must match the electricity network in use in Israel, which the statute requires expressly for an electrical device, so check the plug against SI 32 before anything else; a European or Chinese plug sinks the shipment. And the importer has to hold the EU documentation and keep the product file retrievable, because release is declaratory and surveillance is after the fact. If the EU dossier is thin, type approval by SII plus per-shipment sampling, or a Green/Gold easement plan once a clean record is built, is the fallback. Ensure the manual is in Hebrew.

### Example 3: EU-compliant skincare cream

User says: "A French brand wants to sell a moisturiser in Israel."
Result: Covered by the Pharmacists' Regulations (Cosmetics) 5783-2023. The reform replaced the old SII + MoH registration pathway with a notification to the Israeli Ministry of Health confirming EU compliance. Registration fee is cancelled. No SII lab test required if the EU dossier is in order, but keep the EU CPNP file and safety assessment available.

## Bundled Resources

### References

- `references/common-official-standards.md` - Table of common product categories and their SI (Israeli Standard) numbers. Consult when you need to look up the standard number for a specific product type.
- `references/approval-routes.md` - Decision guide between type approval, shipment approval, easement plans, declaration-based entry, and EU-CoC recognition. Consult when picking a filing route.
- `references/fast-track-options.md` - Rules for the 2016 food parallel-import reform, the 2022 electronics/radio reforms, and the 2025 EU-regulation recognition catalogue. Consult when assessing whether a shortcut applies.

### Scripts

- `scripts/check_standard.py` - Hardcoded rules engine that takes a product category and returns applicable SI numbers, whether the standard is mandatory, the recommended approval route, required tests, and typical timeline band. Run: `python scripts/check_standard.py --category toy` or `--list` to see supported categories. Categories now include `charger` (external power supplies, Group 2), `plug` (SI 32), `led-lamp` and `cement`, and every rule reports its import group.

## Recommended MCP Servers

No MCP server currently wraps the SII or the Commissioner of Standardization. Until one exists, verify live standards lists directly on the SII website (https://www.sii.org.il) and the Ministry of Economy's standardization policy page. A future MCP could expose Maslol Plus and the Reshumot gazette.

## Gotchas

- Voluntary (takan yisra'eli) vs official (takan rishmi) is a frequent trap. A product can meet a standard that is not mandatory and still be blocked at customs because a different mandatory standard applies.
- The EU-recognition route covers only the regulations actually adopted into the Fifth Appendix of the Standards Law, and each entry has its own commencement date and conditions, so "is it adopted" and "is it in force for my product yet" are two separate questions. Under section 9(a)(1) of the Standards Law the route does not apply to food, to a motor vehicle, or to any product or work process under an official fire-safety standard, except portable extinguishing equipment that is not permanently fixed to land or a building, extinguishing agents, and standalone smoke detectors, which stay inside the route. Do NOT repeat the widespread claim that mains electrical equipment at 50-1000 V AC is excluded: that voltage band is the Low Voltage Directive's own scope, and the LVD is adopted, so it describes what the route COVERS. Agents make this error in both directions, either assuming CE is now universally accepted or assuming electrical goods can never use the route.
- Import-group risk direction is a frequent trap. Group 1 is the HIGHEST risk and carries the heaviest assessment (model approval plus shipment inspection); Group 3 is low risk and needs only an importer declaration; Group 4 is industrial-use-only with no import conformity assessment. Do not assume higher group numbers mean higher risk.
- SI 32 (plugs and socket-outlets) is the cheapest way to lose a container of mains-powered goods from Asia. It is official on all its parts, and Israel uses the Type H plug. A perfect IEC 60335 file does not rescue a product fitted with a European or Chinese plug, and shipping an adapter is not a fix for a product being placed on the market.
- "ILAC-accredited" is a moving term. IAF and ILAC have launched a successor body, Global Accreditation Cooperation Incorporated, so a lab report or accreditation mark issued under the older arrangement may be described differently going forward. Check what the accreditation body is called today rather than pattern-matching on the letters ILAC.
- A type approval (ishur tipus) covers a specific model only. Sister models, different voltages, or firmware variants need fresh filings.
- Samples must usually be sent and tested before the shipment arrives, not after. Planning the test slot late is a common delay cause.
- Israeli standards are revised by publication in Reshumot, sometimes with very short transition windows (SI 562 part 1 gave only five months in 2022-2023). Always check the current version, not a cached PDF.
- Personal imports (ye'vu ishi) follow a lighter regime than commercial imports and often pass under exemption thresholds, but the exemption does not cover resale. The personal-import VAT/purchase-tax exemption ceiling has moved four times inside a year: raised from USD 75 to USD 150 by ministerial order in December 2025, revoked by the Knesset on 24 February 2026, reset to USD 130 from 25 February 2026, and back to USD 75 from 1 June 2026. As of August 2026 the threshold is USD 75; between USD 75 and USD 500 the package carries VAT only, at 18%. This affects duty-and-tax math, not the standards regime, but importers often conflate the two; for the customs side use the `israeli-customs-duty-calculator` skill.
- The Amendment 19 EU route is declaratory: the importer signs and files a declaration through Sha'ar Olami, no SII pre-test is needed. The trap is that random surveillance after release can still pull samples and fines apply if the dossier turns out to be incomplete. Keep every CE/DoC/test report indexed and retrievable.
- Amendment 21 (US-standards recognition) is law as of 16 July 2026 but is NOT yet in force: it starts six months after publication, so at the beginning of 2027, and that date can be deferred. Two traps once it does start. It is keyed to where the product was MADE, not to which rules it meets, so a CPSC-compliant toy manufactured in China does not qualify. And cosmetics are excluded from the American route even though they are inside the European one. Until the start date, treat US-standards documentation as supporting evidence inside an Israeli filing, not as a stand-alone import route.

## Reference Links

| Source | URL | What to check |
|---|---|---|
| SII home (English) | https://www.sii.org.il/en | Contact centres, standards, certifications |
| SII importers | https://www.sii.org.il/en/importers/ | Maslol Plus filing, importer contact emails |
| SII easement plans | https://www.sii.org.il/en/tracks/ | Green / Gold / Diamond plan rules, ISO 9001 eligibility |
| Commissioner of Standardization (Ministry of Economy) | (Ministry of Economy site, Commissioner of Standardization pages) | Enforcement policy, mandatory standards, Reshumot |
| Official EU-regulation / SI search engine | https://www.gov.il/en/service/search_official_standards | Look up an SI number to get the matching EU regulation, effective dates, and import group |
| Sha'ar Olami (Customs Global Gateway) | (Israel Tax Authority customs portal) | Electronic clearance system: customs broker files the SII/declaration package here |
| US ITA Israel standards reform | https://www.trade.gov/market-intelligence/israel-standards-reform | Plain-English overview of EU-recognition and the declaration route |
| Free Import Order 5774-2014 (Nevo) | https://www.nevo.co.il/law_html/law01/500_970.htm | Which goods need an import licence (First Appendix) or a named authority's approval (Second Appendix) |
| Wireless Telegraph (Compliance Certificates) Regulations 5781-2021 (Nevo) | https://www.nevo.co.il/law_html/law01/502_483.htm | Regulation 2(a) certificate duty; regulation 5a EU documentation easement |
| Electrical and Electronic Equipment and Batteries Law 5772-2012 (Nevo) | https://www.nevo.co.il/law_html/law00/120269.htm | Section 8 duty to contract with a recognised implementation body |
| Packaging Regulation Law 5771-2011 (Nevo) | https://www.nevo.co.il/law_html/law00/75777.htm | Section 9 duty to contract with a recognised body |
| Kol Zchut personal-import guide | https://www.kolzchut.org.il/he/%D7%96%D7%9B%D7%95%D7%AA%D7%95%D7%9F_%D7%91%D7%A0%D7%95%D7%A9%D7%90_%D7%99%D7%91%D7%95%D7%90_%D7%90%D7%99%D7%A9%D7%99_%28%D7%97%D7%91%D7%99%D7%9C%D7%95%D7%AA_%D7%9E%D7%97%D7%95%22%D7%9C%29 | Current personal-import tax-exemption threshold |

## Troubleshooting

### Error: "Customs is holding our shipment, says no standards certificate"

Cause: The product probably falls under an official standard (takan rishmi) and no type approval or declaration was filed before the container arrived.
Solution: Contact the relevant SII importer centre (electrical 03-6465160, electronics 03-6465050, chemicals 03-6465138, mechanics 03-6465141) and file retroactively via Maslol Plus. Arrange sampling at the port. If release is urgent, a customs broker can sometimes request a limited shipment approval.

### Error: "CE should be enough, why is SII still asking for tests?"

Cause: usually one of three things, and they need different answers. Either the EU regulation governing this product is not in the Fifth Appendix at all; or it is there but its commencement date has not arrived (low-voltage cables, for example, only come in on 1 January 2027); or the product falls in the statutory exclusion list, meaning food, motor vehicles, or fire-safety-standard goods other than portable extinguishers, extinguishing agents and standalone smoke detectors. A fourth possibility, common with electrical goods, is that the EU route IS open and the real objection is that the unit does not match the Israeli mains.
Solution: identify which of the four applies before choosing a remedy. If the regulation is genuinely unadopted or the category is excluded, use type approval by SII or an easement plan and keep the EU test reports, since they speed up the SII file. If the objection is the mains, fix the plug against SI 32 rather than opening a type-approval file.

### Error: "Our factory changed component supplier; can we still use the same type approval?"

Cause: Type approvals cover a specific model configuration. Material changes can invalidate it.
Solution: Contact the SII case handler, submit the engineering change notice, and ask whether a variant approval or fresh file is required before the next shipment leaves the origin port.
