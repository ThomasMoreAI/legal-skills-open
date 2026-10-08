---
description: Expert reference for beneficial ownership data, policy, and BODS. Trigger on BODS JSON/schema/tools (bodsdata, CoVE-BODS, RDF/SPARQL, open issues), BO registries, FATF R24/R25, FATF mutual evaluations (MERs, FSRBs: APG/CFATF/MONEYVAL/ESAAMLG/MENAFATF/GIABA/EAG/GAFILAT), EU AML/AMLD6/AMLR/BORIS, country BO data (UK, Norway, France, Indonesia, Denmark, Canada/Ontario, Sri Lanka, BVI, Philippines, Ghana, Sweden), GLEIF, corporate data (OpenCorporates, Kyckr, Kausate, Sayari, ICIJ), FtM/OpenSanctions, Neo4j, BODS case studies (Latvia, Armenia, Nigeria), BO in procurement (OCDS, ChileCompra, Slovakia, PhilGEPS), BO in energy/extractives (EITI, GEM), BO in fisheries (GFW, FiTI), BO forms (Ghana, Namibia, PSC01), ICIJ/Panama Papers, BO reports (World Bank, TI, TI-UK), GODIN, UBO APIs (Kyckr, Kausate, KvK, Signicat, Companies House), BO verification (FATF, OECD toolkit, TJN), BOVS, BODS converters (bods-ftm, bods-aml-ai, bods-neo4j, bods-gql), BODS docs/primer/governance, or 2026 developments (BVI, Sri Lanka, Sweden, Ontario, Philippines, St Helena). If the question is about who owns what, use this skill.
argument-hint: "[question or task]"
---

# Beneficial Ownership Data — Expert Reference

This skill covers the full beneficial ownership data landscape: the BODS technical standard, OpenOwnership's ecosystem of tools, the regulatory policy context (FATF, EU AML), country-specific register designs, international advocacy, mapping corporate data sources to BODS, interoperability with other data models, beneficial ownership in procurement, and beneficial ownership in extractives.

**Important context**: This skill is used by Stephen Abbott Pugh — the original product owner of BODS at Open Ownership, now running the consultancy Understand Beneficial Ownership (beneficialownership.co.uk). His writing is at stephenabbottpugh.medium.com and beneficialownership.co.uk/news-articles-and-blog-posts. When helping Stephen, you can assume deep domain expertise on his part — be direct and specific rather than over-explaining fundamentals.

Always fetch live documentation when you need precise schema details; the standard is versioned and evolving.

## Quick reference: Key URLs

### BODS Standard & Tools
| Resource | URL |
|---|---|
| BODS documentation (current — `main` branch) | https://standard.openownership.org/en/main/ |
| BODS 0.4 release branch (frozen, translated) | https://standard.openownership.org/en/0.4.0/ |
| BODS schema reference | https://standard.openownership.org/en/main/standard/reference.html |
| BODS schema browser | https://standard.openownership.org/en/main/standard/schema-browser.html |
| BODS changelog | https://standard.openownership.org/en/main/standard/changelog.html |
| BODS examples | https://standard.openownership.org/en/main/examples/ |
| OpenOwnership website | https://www.openownership.org/en/ |
| OpenOwnership publications | https://www.openownership.org/en/publications/ |
| OpenOwnership GitHub org | https://github.com/orgs/openownership/repositories |
| bodsdata (data processing) | https://github.com/openownership/bodsdata |
| BODSKit docs | https://bodskit.readthedocs.io/en/master/ |
| bodsanalysis (notebooks) | https://github.com/openownership/bodsanalysis |
| bods-validator (validation + visualisation tool) | https://github.com/StephenAbbott/bods-validator |
| bods-fixtures (shared test fixture pack) | https://github.com/StephenAbbott/bods-fixtures |
| bods-v04-fixtures (PyPI) | https://pypi.org/project/bods-v04-fixtures/ |
| pytest-bods-fixtures (pytest plugin) | https://github.com/StephenAbbott/pytest-bods-fixtures |
| pytest-bods-v04-fixtures (PyPI) | https://pypi.org/project/pytest-bods-v04-fixtures/ |
| Beneficial Ownership Visualisation System (BOVS) | https://www.openownership.org/en/publications/beneficial-ownership-visualisation-system/ |
| BODS Visualisation Library (implements BOVS) | https://www.openownership.org/en/publications/beneficial-ownership-data-standard-visualisation-library/ |
| visualisation-tool / bods-dagre | https://github.com/openownership/visualisation-tool |
| visualisation spec | https://github.com/openownership/visualisation-tool/blob/main/docs/spec.md |
| bods-dagre npm | https://www.npmjs.com/package/@openownership/bods-dagre |
| CoVE-BODS web validator | https://datareview.openownership.org |
| CoVE-BODS GitHub | https://github.com/openownership/cove-bods |
| lib-cove-bods (CLI) | https://github.com/openownership/lib-cove-bods |
| BODS data generator (Google Sheets) | https://docs.google.com/spreadsheets/d/1PHjwqiOguG8DqyXN75dNSpl_tNhTyelYav1B6sk8nRQ/ |
| BODS data generator guide | https://www.openownership.org/en/publications/beneficial-ownership-data-standard-generator/user-guidance/ |
| RDF vocabulary (bodsld) | https://github.com/openownership/bodsld |
| BODS RDF terms | https://vocab.openownership.org/terms/ |
| BODS RDF Turtle 0.4 | https://vocab.openownership.org/terms/bods-vocabulary-0.4.0.ttl |
| BODS data explorer | https://bods-data.openownership.org/ |
| RDF blog post | https://www.openownership.org/en/blog/updating-the-beneficial-ownership-data-standard-rdf-vocabulary-to-help-linked-data-users/ |

### BODS Primer, About & Governance (rewritten 2026)
| Resource | URL |
|---|---|
| Primer index | https://standard.openownership.org/en/main/primer/index.html |
| What is beneficial ownership? | https://standard.openownership.org/en/main/primer/whatisbo.html |
| What is BODS? | https://standard.openownership.org/en/main/primer/whatisbods.html |
| Key concepts in BODS data | https://standard.openownership.org/en/main/primer/concepts.html |
| What is the BODS data model? (UML) | https://standard.openownership.org/en/main/primer/datamodel.html |
| About BODS | https://standard.openownership.org/en/main/about/index.html |
| Governance and development | https://standard.openownership.org/en/main/about/governance.html |
| Credits | https://standard.openownership.org/en/main/about/credits.html |
| BODS development handbook (site) | https://openownership.github.io/bods-dev-handbook/ |
| BODS development handbook (repo) | https://github.com/openownership/bods-dev-handbook |
| BODS feature tracker | https://github.com/openownership/data-standard/projects/4 |
| Implementation proposals (Discussions) | https://github.com/openownership/data-standard/discussions/categories/feature-implementation |
| Issue templates (feature request / bug) | https://github.com/openownership/data-standard/issues/new/choose |

### Stephen's BODS Conversion Repositories
| Resource | URL |
|---|---|
| bods-brightquery (BrightQuery → BODS 0.4) | https://github.com/StephenAbbott/bods-brightquery |
| bods-kyckr (Kyckr → BODS 0.4) | https://github.com/StephenAbbott/bods-kyckr |
| bods-icij-offshoreleaks (ICIJ → BODS 0.4) | https://github.com/StephenAbbott/bods-icij-offshoreleaks |
| bods-opencorporates (OpenCorporates → BODS 0.4) | https://github.com/StephenAbbott/bods-opencorporates |
| bods-ftm (BODS 0.4 ↔ FollowTheMoney, bidirectional) | https://github.com/StephenAbbott/bods-ftm |
| bods-aml-ai (BODS 0.4 → Google AML AI) | https://github.com/StephenAbbott/bods-aml-ai |
| bods-neo4j (BODS 0.4 ↔ Neo4j, bidirectional) | https://github.com/StephenAbbott/bods-neo4j |
| bods-gql (BODS 0.4 → Google BigQuery / GQL) | https://github.com/StephenAbbott/bods-gql |
| bods-xml (BODS 0.4 → XML: canonical + MRAS) | https://github.com/StephenAbbott/bods-xml |
| bods-stream (live UK PSC → BODS v0.4, streaming) | https://github.com/StephenAbbott/bods-stream |
| bods-stream (live demo) | https://bods-stream.onrender.com/ |
| bods-mapper (shared CH PSC → BODS v0.4 library) | https://github.com/StephenAbbott/bods-mapper |
| opencheck (CDD tool: LEI → 29 sources → BODS v0.4) | https://github.com/StephenAbbott/opencheck |
| opencheck (live demo) | https://opencheck.onrender.com/ |

### GLEIF → BODS 0.4
| Resource | URL |
|---|---|
| OpenOwnership news: GLEIF data in BODS 0.4 | https://www.openownership.org/en/news/global-legal-entity-ownership-data-available-in-line-with-latest-version-of-data-standard/ |
| GLEIF BODS 0.4 dataset (explorer) | https://bods-data.openownership.org/source/gleif_version_0_4/ |
| bods-gleif-pipeline (GitHub) | https://github.com/openownership/bods-gleif-pipeline/ |
| Blog: updating GLEIF → BODS mapping | https://www.openownership.org/en/blog/updating-our-mapping-of-gleif-data-to-bods-to-better-capture-the-lifecycle-of-lei-data-changes/ |

### Corporate Ownership Data Sources
| Resource | URL |
|---|---|
| Sayari documentation | https://documentation.sayari.com/home/overview |
| Sayari data model | https://documentation.sayari.com/sayari-library/data-model/data-model |
| OpenCorporates API reference | https://api.opencorporates.com/documentation/API-Reference |
| OpenCorporates data dictionaries (index) | https://knowledge.opencorporates.com/article-categories/dictionaries/ |
| OpenCorporates relationships data dictionary | https://knowledge.opencorporates.com/knowledge-base/data-dictionary-relationships/ |
| OpenCorporates officers data dictionary | https://knowledge.opencorporates.com/knowledge-base/data-dictionary-officers/ |
| OpenCorporates relationship file key info | https://knowledge.opencorporates.com/knowledge-base/count-of-relationship-records/ |
| BrightQuery organizations data dictionary | https://opendata.org/data-dictionary/organizations |
| BrightQuery locations data dictionary | https://opendata.org/data-dictionary/locations |
| BrightQuery people-business data dictionary | https://opendata.org/data-dictionary/people-business |
| InfobelPro data overview | https://www.infobelpro.com/data |
| InfobelPro methodology | https://www.infobelpro.com/data/methodology |
| OECD-UNSD MNE Information Platform | https://www.oecd.org/en/data/dashboards/oecd-unsd-multinational-enterprise-information-platform.html |
| OECD-UNSD MEIP methodology | https://www.oecd.org/en/publications/the-oecd-unsd-multinational-enterprise-information-platform_b7d90a06-en.html |
| OECD-UNSD Global Register 2024 (XLSX) | https://www.oecd.org/content/dam/oecd/en/data/dashboards/oecd-unsd-multinational-enterprise-information-platform/Global%20Register%202024%20-%20OECD-UNSD%20Multinational%20Enterprise%20Information%20Platform.xlsx |
| OECD-UNSD MEIP 2026 blog post | https://www.oecd.org/en/blogs/2026/03/MNE-thing-is-possible-New-OECD-UNSD-data-release-strengthens-open-evidence-on-multinational-enterprises.html |

### Private Sector & Register APIs: UBO/PSC Data
| Resource | URL |
|---|---|
| Kyckr company API (v2) overview | https://developer.kyckr.com/api/company-v2/#/ |
| Kyckr CorporationUBO schema | https://developer.kyckr.com/api/company-v2/#/schemas/CorporationUBO |
| Kyckr IndividualUBO schema | https://developer.kyckr.com/api/company-v2/#/schemas/IndividualUBO |
| Kyckr OtherUBO schema | https://developer.kyckr.com/api/company-v2/#/schemas/OtherUBO |
| Stephen's bods-kyckr mapping repo | https://github.com/StephenAbbott/bods-kyckr |
| Kausate extractUBOs endpoint | https://docs.kausate.com/api-reference/company-data/extractUBOs |
| Netherlands KvK UBO register API (Dataservice) | https://developers.kvk.nl/ |
| Sweden Bolagsverket API — FAQ | https://bolagsverket.se/apierochoppnadata/fragorochsvaromapierna.4611.html |
| Signicat UBO lookup (Mint step) | https://developer.signicat.com/docs/mint/steps/reference/data-verification/organisation-ubo-lookup/ |
| UK Companies House PSC API reference | https://developer-specs.company-information.service.gov.uk/companies-house-public-data-api/reference/persons-with-significant-control |

### Neo4j Graph Database: BO Ownership Analysis
| Resource | URL |
|---|---|
| Neo4j UBO developer guide (UK Companies House) | https://neo4j.com/developer/industry-use-cases/finserv/retail-banking/company-ownership-ubo-graphs/ |
| erikbijl/neo4j-company-house-demo (GitHub) | https://github.com/erikbijl/neo4j-company-house-demo |
| Neo4j FinServ webinar recording (on-demand) | https://go.neo4j.com/WBREDU260210FinServ_On-Demand.html |
| GraphAware Hume + BODS webinar (OpenOwnership blog) | https://www.openownership.org/en/blog/join-our-event-master-complex-ubo-investigations-with-advanced-graph-technology/ |
| GraphAware Hume + BODS webinar (YouTube recording) | https://www.youtube.com/watch?v=BO6TVN5UL14 |

### BODS Interoperability: Other Data Models
| Resource | URL |
|---|---|
| Senzing sz-semantics RDF namespace | https://github.com/senzing-garage/sz-semantics/wiki/ns |
| OpenSanctions OpenOwnership dataset | https://www.opensanctions.org/datasets/openownership/ |
| opensanctions/bods-ftm (archived) | https://github.com/opensanctions/bods-ftm |
| opensanctions/graph (successor) | https://github.com/opensanctions/graph |

### BODS RDF: Linked Data & SPARQL
| Resource | URL |
|---|---|
| BODS for Linked Data documentation | https://vocab.openownership.org/ |
| BODS RDF data model | https://vocab.openownership.org/pages/1_datamodel.html |
| RDF vocab publication (OpenOwnership) | https://www.openownership.org/en/publications/rdf-vocabulary-for-the-beneficial-ownership-data-standard/ |
| BODS RDF: linking BO records with other datasets | https://world.hey.com/cos/using-bods-rdf-to-link-beneficial-ownership-records-with-other-datasets-0383cbd9 |
| BODS RDF: SPARQL examples for BO use cases | https://world.hey.com/cos/bods-rdf-sparql-examples-for-various-beneficial-ownership-use-cases-284d6f73 |
| BODS RDF: ultimate parents and corporate control | https://world.hey.com/cos/ultimate-parents-and-corporate-control-with-open-ownership-bd1ee35b |
| BODS RDF: querying UBOs | https://world.hey.com/cos/querying-ubos-with-open-ownership-and-bods-rdf-6a272004 |
| BODS risk detection (RDF/SPARQL PoC) | https://www.openownership.org/en/publications/bods-risk-detection/ |
| BODS risk detection: technical details | https://www.openownership.org/en/publications/bods-risk-detection/bods-risk-tdetection-technical-details/ |
| bodsriskdetection (GitHub) | https://github.com/openownership/bodsriskdetection |

### Beneficial Ownership in Procurement
| Resource | URL |
|---|---|
| OCDS guidance: beneficial ownership | https://standard.open-contracting.org/latest/en/guidance/map/beneficial_ownership/ |
| OCDS beneficial owners extension | https://extensions.open-contracting.org/en/extensions/beneficialOwners/master/ |
| Open Contracting Partnership: BO overview | https://www.open-contracting.org/what-is-open-contracting/beneficial-ownership/ |
| Open Contracting data portal | https://data.open-contracting.org/ |
| OO blog: spotting risks (BODS + OCDS + sanctions) | https://www.openownership.org/en/blog/spotting-risks-by-combining-beneficial-ownership-public-procurement-and-sanctions-data/ |
| OO blog: connecting BO and procurement | https://www.openownership.org/en/blog/connecting-the-dots-between-beneficial-ownership-and-procurement-data-improving-processes-and-identifying-risk/ |
| OO publication: BO data in procurement | https://www.openownership.org/en/publications/beneficial-ownership-data-in-procurement/ |
| Entity identifiers in UK procurement (HEY blog) | https://world.hey.com/cos/entity-identifiers-in-uk-public-procurement-data-5f3f3815 |
| ChileCompra: conflict of interest detection 2026 | https://www.chilecompra.cl/2026/01/chilecompra-detecta-potenciales-conflictos-de-interes-por-3-452-millones-tras-cruce-de-datos-masivo/ |
| Chile BO in procurement (OCP blog, 2025) | https://www.open-contracting.org/2025/11/04/chile-companies-disclose-their-real-owners/ |
| Chile BO procurement case study (OCP/OO, 2025) | https://www.open-contracting.org/resources/casestudy-bot-pp-chile/ |
| Chile BO procurement (OO publication) | https://www.openownership.org/en/publications/beneficial-ownership-in-chiles-public-procurement-reform/ |
| Slovakia RPVS (public procurement BO register) | https://rpvs.gov.sk/rpvs |
| Slovakia RPVS on OpenSanctions | https://www.opensanctions.org/datasets/sk_rpvs/ |
| Slovakia RPVS on BODS data explorer | https://bods-data.openownership.org/source/slovakia/ |
| Philippines PhilGEPS open data | https://philgeps.gov.ph/CmsHomePages/open-data |
| Philippines BO reform (OO publication) | https://www.openownership.org/en/publications/implementation-of-cosp-resolution-10-6/beneficial-ownership-reform-in-the-philippines/ |

### Beneficial Ownership in Extractives (EITI)
| Resource | URL |
|---|---|
| EITI Requirements (Requirement 2.5: BO) | https://eiti.org/eiti-requirements#_5-beneficial-ownership-17296 |
| EITI beneficial ownership overview | https://eiti.org/beneficial-ownership |
| EITI 2023 Standard: BO transparency blog | https://eiti.org/blog-post/doubling-down-beneficial-ownership-transparency-new-eiti-standard |
| EITI 2023 Standard PDF | https://eiti.org/sites/default/files/2023-06/2023%20EITI%20Standard.pdf |
| EITI SOE database launch blog | https://eiti.org/blog-post/eiti-launches-new-database-state-owned-enterprises |
| EITI SOE database | https://soe-database.eiti.org/ |
| EITI SOE database API | https://soe-database.eiti.org/eiti_database |
| EITI BODS mapping notebook (GitHub) | https://github.com/civicliteracies/EITI_SDT_data_verification_and_validation/blob/sqlite/5_publish/1_test/eiti_bods_mapping.ipynb |
| OO news: 2023 EITI Standard and BO | https://www.openownership.org/en/news/2023-eiti-standard-strengthened-requirements-on-beneficial-ownership-transparency/ |
| OO publication: BO in extractives legislation | https://www.openownership.org/en/publications/legislating-for-effective-beneficial-ownership-transparency-reforms-in-the-extractive-sector/ |
| BODS guidance: representing SOEs | https://standard.openownership.org/en/0.3.0/schema/guidance/repr-state-owned-enterprises.html |

### Public Beneficial Ownership Registers
| Resource | URL |
|---|---|
| Armenia BO register | https://old.e-register.am/en/ |
| Botswana BO register (CIPA) | https://www.cipa.co.bw/master/ui/start/CIPARegisterSearch |
| BVI BO register (legitimate interest — live 1 April 2026) | https://gov.vg/news/legitimate-interest-access-now-fully-operational-virgin-islands |
| BVI FSC revised BO guidelines (Jan 2026) | https://www.bvifsc.vg/sites/default/files/revised_bo_guidelines_final_version_for_publication_02.01.26_0.pdf |
| BVI FSC industry circular 11-2026 | https://www.bvifsc.vg/news/industry-updates/industry-circular-11-2026-launch-legitimate-interest-transactions-and-request |
| Canada corporate registry search | https://ised-isde.canada.ca/cc/lgcy/fdrlCrpSrch.html?lang=eng |
| Nigeria BO register (CAC) | https://bor.cac.gov.ng/ |
| Philippines BO (public procurement) | http://linkedin.com/feed/update/urn:li:activity:7442395219033219072 |
| Sri Lanka BO Registry Module | https://bo.drc.gov.lk/login |
| Sri Lanka BO Regulations (Gazette 2480/48, 21 Mar 2026) | https://www.linkedin.com/pulse/sri-lankas-beneficial-ownership-registry-now-live-heres-medagoda-5sn2c/ |
| St Helena BO register (Proton Drive) | https://drive.proton.me/urls/WEC6VHS4DW#GmckfehJ8yk2 |
| UK Companies House (PSC data) | https://find-and-update.company-information.service.gov.uk/ |
| OpenOwnership global map | https://www.openownership.org/en/map/ |

### Policy & Regulation
| Resource | URL |
|---|---|
| FATF Recommendations | https://www.fatf-gafi.org/en/publications/Fatfrecommendations/Fatf-recommendations.html |
| FATF R24 guidance (legal persons) | https://www.fatf-gafi.org/en/publications/Fatfrecommendations/Guidance-Beneficial-Ownership-Legal-Persons.html |
| FATF R25 guidance (legal arrangements) | https://www.fatf-gafi.org/en/publications/Fatfrecommendations/Guidance-Beneficial-Ownership-Transparency-Legal-Arrangements.html |
| FATF methodology | https://www.fatf-gafi.org/en/publications/Mutualevaluations/Fatf-methodology.html |
| EU AML Regulation 2024/1624 (AMLR) | https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202401624 |
| EU AMLD6 2024/1640 | https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202401640 |
| EC consultation on BO data formats | https://ec.europa.eu/info/law/better-regulation/have-your-say/initiatives/14851 |
| UK open standard for BO | https://www.gov.uk/government/publications/open-standards-for-government/collect-use-and-exchange-beneficial-ownership-information |
| UK Anti-Corruption Strategy 2025 | https://www.gov.uk/government/publications/uk-anti-corruption-strategy-2025/uk-anti-corruption-strategy-2025-accessible |
| DT4CA alliance | https://dt4calliance.eu/ |

### FATF Mutual Evaluations & Country Reports
| Resource | URL |
|---|---|
| All FATF publications (filterable by country) | https://www.fatf-gafi.org/en/publications.html |
| FATF mutual evaluations topic page | https://www.fatf-gafi.org/en/topics/mutual-evaluations.html |
| FATF countries page | https://www.fatf-gafi.org/en/countries.html |
| Consolidated assessment ratings (2014–2026) | https://www.fatf-gafi.org/en/publications/Mutualevaluations/Assessment-ratings.html |
| FATF methodology (4th round) | https://www.fatf-gafi.org/en/publications/Mutualevaluations/Fatf-methodology.html |
| Jurisdictions under Increased Monitoring (grey list) | https://www.fatf-gafi.org/en/publications/High-risk-and-other-monitored-jurisdictions/Jurisdictions-under-increased-monitoring-25-june-2021.html |
| High-Risk Jurisdictions (black list) | https://www.fatf-gafi.org/en/publications/High-risk-and-other-monitored-jurisdictions/Call-for-action-June-2021.html |
| Example MER: Belgium 2025 | https://www.fatf-gafi.org/en/publications/Mutualevaluations/mer-belgium-2025.html |
| Example follow-up: Montserrat (via CFATF) | https://www.fatf-gafi.org/en/publications/Mutualevaluations/Follow-upreportstothemutualevaluationofmontserrat.html |
| FATF Global Network (FSRBs overview) | https://www.fatf-gafi.org/en/countries/global-network.html |
| APG — Asia/Pacific Group | https://www.fatf-gafi.org/en/countries/global-network/asia-pacific-group-on-money-laundering--apg-.html |
| CFATF — Caribbean | https://www.fatf-gafi.org/en/countries/global-network/caribbean-financial-action-task-force--cfatf-.html |
| MONEYVAL — Council of Europe | https://www.fatf-gafi.org/en/countries/global-network/committee-of-experts-on-the-evaluation-of-anti-money-laundering-.html |
| ESAAMLG — Eastern & Southern Africa | https://www.fatf-gafi.org/en/countries/global-network/eastern-and-southern-africa-anti-money-laundering-group--esaamlg.html |
| MENAFATF — Middle East & North Africa | https://www.fatf-gafi.org/en/countries/global-network/middle-east-and-north-africa-financial-action-task-force--menafa.html |
| GIABA — West Africa | https://www.fatf-gafi.org/en/countries/global-network/inter-governmental-action-group-against-money-laundering-in-west-.html |
| EAG — Eurasian Group | https://www.fatf-gafi.org/en/countries/global-network/eurasian-group--eag-.html |
| GAFILAT — Latin America | https://www.fatf-gafi.org/en/countries/global-network/financial-action-task-force-of-latin-america--gafilat-.html |
| GABAC — Central Africa | https://www.fatf-gafi.org/en/countries/global-network/action-group-against-money-laundering-in-central-africa--gabac-.html |

### International Endorsements & Resources
| Resource | URL |
|---|---|
| World Bank — BO publication | https://openknowledge.worldbank.org/entities/publication/43aa154d-eb9c-49ea-b952-6811755b94da |
| OECD — tax transparency on real estate | https://www.oecd.org/en/publications/strengthening-international-tax-transparency-on-real-estate-from-concept-to-reality_fa2db2a4-en.html |
| UNODC BOT/PEP toolkit | https://www.unodc.org/rosaf/uploads/documents/Publication/UNDC_BOT_PEP_Toolkit_web.pdf |
| Canada Bill C-42 | https://www.parl.ca/legisinfo/en/bill/44-1/c-42 |
| BIS publication | https://www.bis.org/publ/othp66.htm |
| OGP guide (anti-corruption / BO) | https://www.opengovpartnership.org/open-gov-guide/anti-corruption-company-beneficial-ownership/ |
| OECD/IDB BO Frameworks Toolkit | https://www.oecd.org/content/dam/oecd/en/networks/global-forum-tax-transparency/effective-beneficial-ownership-frameworks-toolkit-en.pdf |
| IDB BO Frameworks (partner pub) | https://publications.iadb.org/en/building-effective-beneficial-ownership-frameworks-joint-global-forum-and-idb-toolkit |
| OECD Global Forum peer reviews | https://www.oecd.org/en/networks/global-forum-tax-transparency/resources/exchange-of-information-on-request-ratings.html |

### Country-Specific Registers
| Resource | URL |
|---|---|
| Norway BO register | https://www.brreg.no/reelle-rettighetshavere/ |
| Norway BO API docs | https://brreg.github.io/docs/apidokumentasjon/reelle-rettighetshavere/tilgjengeliggjoering/apier-vi-tilbyr/virksomheter/ |
| Norway BO Swagger | https://rrh.brreg.no/api/oppslag/swagger-ui/index.html |
| Norway Maskinporten auth | https://docs.digdir.no/docs/Maskinporten/maskinporten_guide_apikonsument |
| UK PSC API reference | https://developer-specs.company-information.service.gov.uk/companies-house-public-data-api/reference/persons-with-significant-control |
| France — sample BO data | https://entreprise.api.gouv.fr/catalogue/inpi/rne/beneficiaires_effectifs/exemple |
| France — API docs | https://entreprise.api.gouv.fr/catalogue/inpi/rne/beneficiaires_effectifs |
| Indonesia — BO API | https://ahu.go.id/service/getReportBo |
| Indonesia — API docs (Bahasa) | https://panduan.ahu.go.id/api/detail.php |
| Indonesia — BODS 0.4 mapping (doc) | https://docs.google.com/document/d/1jS-khhSxOkYG0gJCRbht8HmMh79ICh_YrLd29pL4Kfk/edit |
| Indonesia — BODS mapping (drive) | https://drive.google.com/file/d/1hW0UlBRuYt2vJz-PjydK0mtkAKVUKBgO/view |
| Denmark BO docs | https://confluence.sdfi.dk/pages/viewpage.action?pageId=151999753 |
| Canada: Corporations Canada federal register | https://ised-isde.canada.ca/cc/lgcy/fdrlCrpSrch.html?lang=eng |
| Canada: BOP2P (Beneficial Ownership Policy to Practice) | https://ised-isde.canada.ca/mras/partners/bop2p/ |
| Canada: OO map page | https://www.openownership.org/en/map/country/canada/ |
| Ontario: BO registry commitment (2027 budget) | https://budget.ontario.ca/2026/chapter-1b-safety.html#section-9 |
| Sri Lanka: BO Registry Module | https://bo.drc.gov.lk/login |
| Sri Lanka: BO Regulations overview (LinkedIn) | https://www.linkedin.com/pulse/sri-lankas-beneficial-ownership-registry-now-live-heres-medagoda-5sn2c/ |
| Sweden: Riksdag approval of legitimate interest access | https://www.riksdagen.se/sv/dokument-och-lagar/dokument/betankande/utlamnande-av-uppgifter-ur-registret-over-verkliga_hd01fiu35/ |
| BVI: legitimate interest access (live 1 April 2026) | https://gov.vg/news/legitimate-interest-access-now-fully-operational-virgin-islands |
| St Helena: public BO register (Proton Drive) | https://drive.proton.me/urls/WEC6VHS4DW#GmckfehJ8yk2 |

### EU BORIS: BO Registers Interconnection System
| Resource | URL |
|---|---|
| BORIS portal (e-Justice) | https://e-justice.europa.eu/topics/registers-business-insolvency-land/beneficial-ownership-registers-interconnection-system-boris_en |
| BORIS search tool | https://webgate.ec.europa.eu/e-justice/searchBoris.do |
| BORIS: finding beneficial owners (e-Justice guide) | https://e-justice.europa.eu/topics/registers-business-insolvency-land/beneficial-ownership-registers-interconnection-system-boris/general-information-finding-beneficial-owners_en |
| BORIS establishing regulation 2021/369 | https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX%3A32021R0369&from=EN |
| AMLD5 2018/843 (central BO registers) | https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=celex%3A32018L0843 |
| AMLD4 2015/849 (base AML directive) | https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=celex%3A32015L0849 |
| Stephen's Medium: BORIS challenges | https://stephenabbottpugh.medium.com/challenges-in-realising-the-goal-of-the-eus-beneficial-ownership-registers-interconnection-system-7ec7b52575ae |
| OO: value of connecting EU BO data | https://www.openownership.org/en/blog/the-value-of-connecting-beneficial-ownership-data-across-the-european-union/ |
| OO: EU steps towards standardised BO | https://www.openownership.org/en/news/european-union-takes-important-steps-towards-standardised-and-interoperable-beneficial-ownership-information/ |
| Transparency International: barriers for investigators across EU | https://www.transparency.org/en/news/barriers-investigators-face-across-eu-tracing-asset-ownership |

### Stephen's Writing & Consultancy
| Resource | URL |
|---|---|
| Stephen's Medium blog | https://stephenabbottpugh.medium.com/ |
| Stephen's website | https://www.beneficialownership.co.uk/ |
| Stephen's articles | https://www.beneficialownership.co.uk/news-articles-and-blog-posts |
| Case studies (BODS in use) | https://www.beneficialownership.co.uk/case-studies |

### BODS Case Studies & Implementations
Full case studies index: https://www.beneficialownership.co.uk/case-studies

| Resource | URL |
|---|---|
| Latvia (first national BODS publication, 2021) | https://www.openownership.org/en/blog/making-latvia-s-beneficial-ownership-data-more-useful-with-bods/ |
| Armenia (BODS BO declarations) | https://www.openownership.org/en/blog/armenia-and-bods/ |
| Botswana CIPA (BODS data collection + visualisation) | https://www.openownership.org/en/blog/botswana-beneficial-ownership-register/ |
| Nigeria CAC (first African BODS implementation) | https://www.openownership.org/en/blog/nigeria-and-the-beneficial-ownership-data-standard/ |
| Canada (BODS for pan-Canadian BO repository) | https://www.openownership.org/en/map/country/canada/ |
| Indonesia (BODS 0.4 mapping) | https://docs.google.com/document/d/1jS-khhSxOkYG0gJCRbht8HmMh79ICh_YrLd29pL4Kfk/edit |
| Slovakia RPVS (BODS data explorer) | https://bods-data.openownership.org/source/slovakia/ |
| EITI SOE database (BODS mapping) | https://github.com/civicliteracies/EITI_SDT_data_verification_and_validation/blob/sqlite/5_publish/1_test/eiti_bods_mapping.ipynb |
| Global Energy Ownership Tracker (BODS-aligned) | https://globalenergymonitor.org/projects/global-energy-ownership-tracker/ |
| Structuriser (compliance SaaS) | https://www.structuriser.com/ |
| Foster Moore Verne® (BO register product) | https://www.fostermoore.com/verne/beneficial-ownership-register |
| NRD Companies BOREG© (BO register product) | https://www.nrdcompanies.com/products-solutions/beneficial-ownership-register/ |

### ICIJ Investigations & Offshore Leaks
| Resource | URL |
|---|---|
| ICIJ homepage | https://www.icij.org/ |
| ICIJ investigations index | https://www.icij.org/investigations/ |
| Panama Papers investigation | https://www.icij.org/investigations/panama-papers/ |
| Pandora Papers investigation | https://www.icij.org/investigations/pandora-papers/ |
| FinCEN Files investigation | https://www.icij.org/investigations/fincen-files/ |
| Offshore Leaks database | https://offshoreleaks.icij.org/ |
| Offshore Leaks data download | https://offshoreleaks.icij.org/pages/database |
| ICIJ GitHub (data tools) | https://github.com/ICIJ |

### Key Beneficial Ownership Research Reports
| Resource | URL |
|---|---|
| World Bank: The Puppet Masters (2011) | https://documents.worldbank.org/en/publication/documents-reports/documentdetail/784961468152973030 |
| World Bank: Signatures for Sale (2023) | https://openknowledge.worldbank.org/entities/publication/32914fa8-e9d5-59cc-b599-105962e9b390 |
| TI: Into the Light — MENA BO frameworks | https://www.transparency.org/en/publications/into-the-light-benchmarking-beneficial-ownership-transparency-frameworks-mena |
| TI: Chasing Grand Corruption | https://www.transparency.org/en/publications/chasing-grand-corruption |
| TI: Legitimate Interest for public stakeholders | https://www.transparency.org/en/publications/legitimate-interest-measures-for-public-interest-stakeholders |
| TI: Opacity in Real Estate Ownership Index 2025 | https://www.transparency.org/en/publications/opacity-in-real-estate-ownership-index-2025 |
| TI-UK: Opening Offshore Secrecy | https://www.transparency.org.uk/publications/opening-offshore-secrecy |
| TI-UK: Improving UK Trust Registration Service | https://www.transparency.org.uk/publications/improving-uks-trust-registration-service |
| TI-UK: Legitimate Interest — Anguilla BO | https://www.transparency.org.uk/publications/providing-legitimate-interest-access-anguillas-beneficial-ownership-data |
| TI-UK: Unlocking Ownership Data | https://www.transparency.org.uk/publications/unlocking-ownership-data |
| TI-UK: Legitimate Interest — BVI BO | https://www.transparency.org.uk/publications/providing-legitimate-interest-access-british-virgin-islands-beneficial-ownership-data |
| TI-UK: Legitimate Interest — Bermuda BO | https://www.transparency.org.uk/publications/providing-legitimate-interest-access-bermudas-beneficial-ownership-data |
| TI-UK: Legitimate Interest — Cayman Islands BO | https://www.transparency.org.uk/publications/providing-legitimate-interest-access-cayman-islands-beneficial-ownership-data |

### GODIN: Global Open Data Integration Network
| Resource | URL |
|---|---|
| GODIN portal (hosted by GLEIF) | https://godin.gleif.org/ |
| Transparency Fabric (GODIN project) | https://transparencyfabric.gleif.org/ |
| GODIN GitHub repositories | https://github.com/orgs/Global-Open-Data-Integration-Network/repositories |
| GLEIF (member) | https://www.gleif.org/en |
| OpenOwnership (member) | https://www.openownership.org/en/ |
| Global Energy Monitor / GEOT (member) | https://globalenergymonitor.org/projects/global-energy-ownership-tracker/ |
| AC/DC — African Climate & Development (member) | https://acdatacollective.org/ |
| Media Registry (member) | https://www.mediaregistry.org/ |
| Open Data Services Co-op (member) | https://opendataservices.coop/ |
| OpenSanctions (member) | https://www.opensanctions.org/ |
| Data Research Center (member) | https://dataresearchcenter.org/ |
| Wikidata (supporter) | https://www.wikidata.org/wiki/Wikidata:Main_Page |

### BO Declaration & Data Collection Forms
| Resource | URL |
|---|---|
| OO blog: example form and guidance | https://www.openownership.org/en/blog/new-example-form-and-guidance-for-developing-beneficial-ownership-declarations/ |
| OO guide: forms for regulators and designers | https://www.openownership.org/en/publications/beneficial-ownership-declaration-forms-guide-for-regulators-and-designers/ |
| OO: example BO declaration form (download) | https://www.openownership.org/en/publications/example-beneficial-ownership-declaration-form/ |
| OO: example paper forms for BO data collection | https://www.openownership.org/en/publications/example-paper-forms-for-collecting-beneficial-ownership-data/ |
| OO: annex — information fields in BO forms | https://www.openownership.org/en/publications/sufficiently-detailed-beneficial-ownership-information/annex-examples-of-information-fields-in-beneficial-ownership-declaration-forms/ |
| EITI: beneficial ownership model declaration form | https://eiti.org/guidance-notes/beneficial-ownership-model-declaration-form |
| EITI: BO model form (document page) | https://eiti.org/document/beneficial-ownership-model-declaration-form |
| Ghana ORC: BO3 form (listed companies) | https://orc.dntsystems.net/wp-content/uploads/2025/08/BO3-Listed-Company-BO-Form.pdf |
| Ghana ORC: BO4 form (government entities) | https://orc.dntsystems.net/wp-content/uploads/2025/08/BO4-Government-BO-Form.pdf |
| Ghana ORC: BO forms index | https://orc.dntsystems.net/beneficial-ownership/ |
| Namibia BIPA: BO form page | https://www.bipa.na/beneficial-ownership/beneficial-ownership-form/ |
| Namibia BIPA: BO2 declaration form | https://www.bipa.na/download/beneficial-ownership-declaration-form-bo2/ |
| Namibia BIPA: BO submission guide | https://www.bipa.na/download/bo-submission-guide/ |
| UK PSC01 v4.0 (individual PSC notice) | https://assets.publishing.service.gov.uk/media/6911eb1ce9348ac8fb54f480/PSC01_v4.0-FINAL.pdf |
| UK: give notice of individual PSC (PSC01) | https://www.gov.uk/government/publications/give-notice-of-individual-person-with-significant-control-psc01 |
| UK: PSC requirements collection | https://www.gov.uk/government/collections/people-with-significant-control-requirements |
| UK: PSC guidance | https://www.gov.uk/guidance/people-with-significant-control-pscs |

### Beneficial Ownership Data Verification
| Resource | URL |
|---|---|
| OO principle: verification | https://www.openownership.org/en/principles/verification/ |
| OO: verification systems design checklist | https://www.openownership.org/en/news/designing-verification-systems-a-sample-implementation-checklist-for-beneficial-ownership-data/ |
| OO: verification of beneficial ownership data (publication) | https://www.openownership.org/en/publications/verification-of-beneficial-ownership-data/ |
| OO implementation guide: data considerations for registers | https://www.openownership.org/en/publications/guide-to-implementing-beneficial-ownership-transparency/data-considerations-for-beneficial-ownership-registers/ |
| FATF R24 guidance — section 7: means of verification (legal persons) | https://www.fatf-gafi.org/en/publications/Fatfrecommendations/Guidance-Beneficial-Ownership-Legal-Persons.html |
| FATF R25 guidance — section 4: adequate, accurate, up-to-date info (legal arrangements) | https://www.fatf-gafi.org/en/publications/Fatfrecommendations/Guidance-Beneficial-Ownership-Transparency-Legal-Arrangements.html |
| OECD BO Frameworks Toolkit (2nd edition, 2024) | https://www.oecd.org/content/dam/oecd/en/networks/global-forum-tax-transparency/effective-beneficial-ownership-frameworks-toolkit-second-edition-2024.pdf |
| OECD BO Toolkit (original) | https://www.oecd.org/content/dam/oecd/en/networks/global-forum-tax-transparency/beneficial-ownership-toolkit.pdf |
| Tax Justice Network: BO verification (truthfulness and accuracy) | https://taxjustice.net/reports/beneficial-ownership-verification-ensuring-the-truthfulness-and-accuracy-of-registered-ownership-information/ |
| Moody's KYC: brief guide to UBO verification legislation | https://www.moodys.com/web/en/us/kyc/resources/insights/who-is-in-charge-here-brief-guide-to-ultimate-beneficial-owners-verification-legislation.html |

### BODS Development: GitHub Issues & Feature Tracker
| Resource | URL |
|---|---|
| BODS data-standard repository | https://github.com/openownership/data-standard |
| Open issues (79 currently) | https://github.com/openownership/data-standard/issues |
| BODS feature tracker (project board) | https://github.com/orgs/openownership/projects/9/views/1 |
| Issue #752: Feature — representing assets | https://github.com/openownership/data-standard/issues/752 |
| Issue #737: Feature — BODS simplification | https://github.com/openownership/data-standard/issues/737 |
| Issue #466: Feature — interest modelling | https://github.com/openownership/data-standard/issues/466 |
| Issue #464: Feature — republishing, provenance and transformation | https://github.com/openownership/data-standard/issues/464 |
| Issue #389: Feature — representing missing information | https://github.com/openownership/data-standard/issues/389 |
| Issue #742: Unspecified or unknown entity | https://github.com/openownership/data-standard/issues/742 |
| Issue #744: publicationDetails no longer required? | https://github.com/openownership/data-standard/issues/744 |
| Issue #733: Review conceptual and data model | https://github.com/openownership/data-standard/issues/733 |
| BODS dev handbook | https://github.com/openownership/bods-dev-handbook |
| OO: bridging the gap — asset transparency | https://www.openownership.org/en/publications/bridging-the-gap-for-effective-asset-transparency/ |
| OO: solving the BO info puzzle (assets blog) | https://www.openownership.org/en/blog/solving-the-international-information-puzzle-of-beneficial-ownership-transparency/ |
| OO: describing interests — research note | https://www.openownership.org/en/publications/describing-interests-research-note/ |
| OO: what makes a beneficial owner? (interests blog) | https://www.openownership.org/en/blog/what-makes-a-beneficial-owner-exploring-global-differences/ |
| OO: building an auditable record of BO (missing info) | https://www.openownership.org/en/publications/building-an-auditable-record-of-beneficial-ownership/ |

### Sectoral Use Cases: Energy & Extractives (Global Energy Monitor)
| Resource | URL |
|---|---|
| Global Energy Ownership Tracker | https://globalenergymonitor.org/projects/global-energy-ownership-tracker/ |
| GEM GEOT methodology | https://globalenergymonitor.org/projects/global-energy-ownership-tracker/methodology/ |
| GEM GEOT download data | https://globalenergymonitor.org/projects/global-energy-ownership-tracker/download-data/ |
| GEOT dataset on OpenSanctions | https://www.opensanctions.org/datasets/gem_energy_ownership/ |
| Stephen's LinkedIn analysis of GEOT data | https://www.linkedin.com/posts/stephenabbottpugh_energy-heavyindustry-opendata-activity-7435326197955260416--6uB/ |
| Stephen's Bluesky analysis of GEOT data | https://bsky.app/profile/stephenabbottpugh.bsky.social/post/3mgcy4kuxpc2t |
| GEM report: oil & gas plant owners hide climate costs | https://globalenergymonitor.org/report/worlds-largest-oil-and-gas-plant-owners-hide-billions-of-dollars-in-climate-costs/ |
| GEM fossil fuel middlemen (Australia nominee structures) | https://globalenergymonitor.org/report/the-fossil-fuel-middlemen-how-nominee-structures-obscure-australian-investments-in-coal-oil-and-gas/ |
| Danwatch: hidden CO2 emissions and pension funds | https://danwatch.dk/en/hidden-co2-emissions-your-pension-money-is-polluting-the-planet-more-than-you-are-told/ |
| E3G: investment treaties and energy transition | https://www.e3g.org/publications/investment-treaties-are-undermining-the-global-energy-transition/ |
| OO: BO transparency and energy transition | https://www.openownership.org/en/publications/shining-a-light-on-company-ownership-the-role-of-beneficial-ownership-transparency-in-the-energy-transition/ |
| EITI: race to renewables report | https://eiti.org/documents/race-to-renewables |

### Sectoral Use Cases: Fisheries
| Resource | URL |
|---|---|
| Global Fishing Watch: UBO in fisheries (overview) | https://globalfishingwatch.org/ultimate-beneficial-ownership-ubo/ |
| GFW: UBO fact sheet | https://globalfishingwatch.org/fact-sheet/ultimate-beneficial-ownership-why-transparency-is-vital-for-effective-fisheries-governance/ |
| GFW: UBO vision document (PDF) | https://globalfishingwatch.org/wp-content/uploads/Global_Fishing_Watch-A-Vision-for-Ultimate-Beneficial-Ownership-in-Fisheries_ENG.pdf |
| GFW: UBO video | https://globalfishingwatch.org/video/ultimate-beneficial-ownership-in-fisheries-the-critical-need-for-transparency-in-vessel-ownership/ |
| GFW: FAO meeting — vessel ownership and IUU fishing | https://globalfishingwatch.org/article/at-fao-meeting-global-fishing-watch-pushes-transparency-of-vessel-ownership-to-combat-illegal-fishing/ |
| C4ADS: Anchors Away (vessel ownership) | https://c4ads.org/commentary/anchors-away/ |
| C4ADS: Sea Shells (fisheries BO) | https://c4ads.org/issue-briefs/sea-shells/ |
| FiTI Standard 2.0 | https://fiti.global/fiti-launches-its-updated-fiti-standard-2-0 |
| FiTI Standard 2.0 (CFFACAPE analysis) | https://www.cffacape.org/news-blog/new-fiti-standard-2point0 |
| Coalition for Fisheries Transparency Global Charter 2024 | https://fisheriestransparency.net/wp-content/uploads/2024/10/Coalition-for-Fisheries-Transparency-Global-Charter-2024-EN.pdf |
| Oceans 5: standard for UBO reporting in fisheries | https://www.oceans5.org/project/standard-for-ultimate-beneficial-ownership-reporting/ |
| TM Tracking: UBO in fisheries | https://www.tm-tracking.org/post/ultimate-beneficial-ownership |
| Pew: fishing company and vessel ownership transparency | https://www.pew.org/-/media/assets/2023/10/ownership-of-fishing-companies-vessels-need-greater-transparency-and-accountability.pdf |
| OO: using BO information in fisheries governance | https://www.openownership.org/en/publications/using-beneficial-ownership-information-in-fisheries-governance/ |
| OO: Charting New Waters (UNODC/OO report) | https://www.openownership.org/en/publications/charting-new-waters/ |

---

For detailed reference material, read:
- `references/bods-standard.md` — BODS 0.4 schema in depth
- `references/tools-ecosystem.md` — OpenOwnership tools
- `references/regulatory-context.md` — FATF, EU AML, policy context
- `references/international-registers.md` — country-specific BO register APIs

---

## The BODS Data Model

BODS represents beneficial ownership as a collection of **Statements**. The current version is **0.4**.

### Three statement types

**1. Person Statements**
Describe a natural person who holds or may hold a beneficial ownership interest.
Key fields: `statementId`, `statementType: "personStatement"`, `names[]`, `identifiers[]`, `nationalities[]`, `birthDate`, `placeOfBirth`, `addresses[]`, `pepStatus[]`, `hasPepStatus`.

**2. Entity Statements**
Describe a legal entity (company, trust, foundation, etc.) in the ownership chain.
Key fields: `statementId`, `statementType: "entityStatement"`, `entityType`, `names[]`, `identifiers[]`, `incorporatedInJurisdiction`, `addresses[]`, `foundingDate`, `dissolutionDate`, `isComponent`.

**3. Ownership-or-Control Statements**
Link a person or entity (the interested party) to an entity (the subject), describing the nature of their interest.
Key fields: `statementId`, `statementType: "ownershipOrControlStatement"`, `subject` (entity statementId), `interestedParty` (person or entity statementId), `interests[]` (type, share, directOrIndirect), `isComponent`, `componentStatementIDs[]`.

### Key structural concepts

- **`statementId`**: UUID-based unique identifier for each statement
- **`isComponent`**: boolean; marks whether a statement is part of an indirect ownership chain (v0.4 addition)
- **`componentStatementIDs`**: array of statementIds making up an indirect chain
- **`publicationDetails`**: metadata on publisher, date, bodsVersion
- **Temporal versioning**: multiple statements can describe the same entity over time; use `replacesStatements[]` to link them

A BODS dataset is a JSON array of statement objects. There is no wrapping container object — just a flat array.

---

## BODS Documentation Rewrite and Current Status (2026)

In 2026 Open Ownership and Open Data Services published a substantial rewrite of the BODS **non-normative** documentation — the Primer, About and Governance pages — via PRs [#754](https://github.com/openownership/data-standard/pull/754) and [#762](https://github.com/openownership/data-standard/pull/762). **No schema, field, codelist or changelog changes were made**: this was a documentation-only update, not a version release.

### Critical: which URL to cite

The default and `latest` documentation URLs now resolve to the **`main` branch**, not the `0.4.0` release branch:

| URL | Resolves to | Use for |
|---|---|---|
| `standard.openownership.org` | `/en/main` | General linking — gets latest docs |
| `standard.openownership.org/en/main/` | `main` branch | Current Primer/About/Governance content |
| `standard.openownership.org/en/latest/` | `/en/main` | Same as default |
| `standard.openownership.org/en/0.4.0/` | `0.4.0` release branch | The frozen, translated v0.4 release |

The documentation updates were merged to `main` and **deliberately not back-ported** to the `0.4.0` release branch. The v0.4 release was translated into **Spanish, French and Russian**; these subsequent documentation updates were **not** translated. So when citing the standard, prefer `/en/main/` for conceptual and governance material, and `/en/0.4.0/` only when you specifically need the frozen release or a translated version.

### Current development status

Both the README and the About page now state plainly: **"BODS is not in active development at the moment."**

- BODS v0.4 was released **May 2024**
- Implementers should be aware that **future changes may be made before a version 1.0 release**
- From v1.0 onwards, any structural or major definitional changes will only take place following consultation
- If work resumes towards v1.0, governance processes will be updated by Open Ownership (stewarding organisation) and Open Data Services (technical maintainer), in consultation with the community

This is a material point for anyone advising on BODS adoption: the standard is stable and usable, but not currently being actively extended, and pre-1.0 breaking changes remain possible.

### The rewritten Primer

The Primer is now four pages, structured by audience:

| Page | Audience | URL |
|---|---|---|
| What is beneficial ownership? | People new to the BO concept | https://standard.openownership.org/en/main/primer/whatisbo.html |
| What is BODS? | Those needing to understand the standard | https://standard.openownership.org/en/main/primer/whatisbods.html |
| What key concepts are represented in BODS data? | Conceptual grounding | https://standard.openownership.org/en/main/primer/concepts.html |
| What is the BODS data model? | Technology teams | https://standard.openownership.org/en/main/primer/datamodel.html |

### The data model page: UML class diagram and pseudo-objects

The new `datamodel.rst` page introduces a **UML class diagram** (`BODS-classes.svg`) — the clearest formal statement yet of the BODS object model. Key points worth knowing:

**Core objects (implemented in JSON Schema)**: Statements, Persons, Entities, Relationships, Interests.

**Pseudo-objects (NOT implemented as objects in JSON Schema — they are implicit)**: **Declaration** and **Record**. This is an important and easily-missed distinction. The `declaration` and `declarationSubject` properties exist as properties *of Statements* in the JSON schema, but conceptually belong to the Declaration pseudo-object. Similarly `recordId`, `recordType` and `recordStatus` are Statement properties implementing the implicit Record.

**Model relationships**:
- A Declaration contains one or more Statements; a Declaration has one Record as its subject
- A Statement is about a single Record, though a Record can be referenced from multiple Statements
- A Record captures information about a Person, an Entity, or a Relationship
- A Relationship's `interestedParty` may be a single Person or a single Entity; its `subject` is always a single Entity
- A Relationship consists of zero or more Interests; an Interest belongs to a single Relationship

**Four network shapes the model supports** (each with its own diagram):
1. The legal vehicles a person controls (top-down tree)
2. The people controlling a legal vehicle (bottom-up tree)
3. The people controlling a set of legal vehicles (non-tree graph)
4. Corporate structures without people (entity-only graph)

**Bi-temporal modelling**: the page explicitly frames Statements as enabling ledger-like histories answering "who knew what, when?" — linking to the [bi-temporal modelling](https://en.wikipedia.org/wiki/Bitemporal_Modeling) concept. Statements from different sources may conflict or overlap, and this is by design.

**No intrinsic definition of 'beneficial owner'**: the data model deliberately embeds no definition of beneficial ownership. It describes networks of ownership, control and benefit. Where a relationship is known to constitute beneficial ownership under a particular jurisdiction's definition, `beneficialOwnershipOrControl` is set to `true` on the relevant interest. This is central to why BODS works across jurisdictions with differing BO thresholds and definitions.

**Not an ERD**: the page is explicit that the data model is not an entity relationship diagram and not a database design. A database need not have a statement table — or even use the concept of "statement" — to export BODS Statements. But the model can usefully inform the design of any system handling corporate structure or BO network data, regardless of whether BODS publication is the goal.

### Rewritten governance and development

The [Governance and development](https://standard.openownership.org/en/main/about/governance.html) page now documents the full process:

- **Feature requests and bug reports**: via [issue templates](https://github.com/openownership/data-standard/issues/new/choose); OO and ODS respond via GitHub issue comments
- **Feature development**: tickets are framed as *problem statements* focused on user-need gaps, tracked on the [feature tracker](https://github.com/openownership/data-standard/projects/4). Anyone may propose an implementation; proposals go through [GitHub Discussions](https://github.com/openownership/data-standard/discussions/categories/feature-implementation) with a minimum two-week community review. Without broad consensus, a proposal is suspended
- **Release tracking**: each version gets a release tracker as a GitHub project; community gets at least two weeks to review and suggest changes. The [v0.4 release tracker](https://github.com/orgs/openownership/projects/4/views/1) is the reference example
- **OpenStand principles**: BODS development aims to meet the five [OpenStand principles](https://open-stand.org/about-us/principles/) — due process, broad consensus, transparency, balance, openness
- **BODS development handbook**: full details of development and decision-making processes now live at https://openownership.github.io/bods-dev-handbook/ (repo: https://github.com/openownership/bods-dev-handbook)

Note: the previous README described a Data Standard Working Group with quarterly meetings and a Google group. That description has been **removed** from the current README and governance page — governance is now documented via the handbook and the GitHub-based processes above. Contact for BODS technical matters is **tech@openownership.org** (general support: support@openownership.org).

---

## Using BODS for Corporate Ownership Structures (without BO declarations)

BODS is designed for beneficial ownership but is equally capable of representing corporate ownership and control structures where the ultimate beneficial owners are unknown, undisclosed, or not the focus. This is a key use case for mapping commercial corporate data sources to BODS.

### Why map corporate ownership data to BODS without BO declarations

Many real-world datasets — company registries, commercial data providers, financial data feeds — record legal entity ownership chains (parent/subsidiary relationships, shareholdings, directorship) without capturing natural-person beneficial owners. BODS accommodates this in several ways.

**Entity-to-entity ownership**: An ownership-or-control statement can link two entity statements, not just a person to an entity. This is the standard pattern for parent/subsidiary chains, joint ventures, and corporate group structures.

**Unknown or anonymous interested parties**: The `interestedParty` field supports `unspecified` as a value to indicate the interested party is not known. Use `unknownPersons` or `anonymousEntity` as the entity type when the ultimate owner is deliberately obscured or simply not recorded in the source data.

**Partial chains**: A dataset might record that Company A owns 60% of Company B, without knowing who owns Company A. This is perfectly valid BODS — just publish what is known. The `isComponent` flag and `componentStatementIDs` can be used to mark that a chain is incomplete.

**`entityType` values for corporate structures**: Beyond `registeredEntity`, BODS supports `arrangement` (for trusts, partnerships), `anonymousEntity`, `unknownEntity`, and `stateBody`. For offshore vehicles and special-purpose entities from sources like ICIJ Offshore Leaks, `arrangement` and `anonymousEntity` are most appropriate.

### Mapping heuristics for source data without BO

When mapping a dataset that records corporate relationships but not BO:

- Map each company/legal entity to a BODS **entity statement** with the appropriate `entityType`
- Map each ownership/control link to a BODS **ownership-or-control statement** with `entityType`-based `interestedParty`
- For natural persons appearing in officer/director roles (not BO roles), create a **person statement** and an **ownership-or-control statement** with `interests[].type = "controlViaDirectorship"` or `"otherInfluenceOrControl"`
- Use heuristics to distinguish natural persons from corporate entities when source data is ambiguous (e.g. ICIJ officer names that could be either)
- Record `interests[].share.exact` where share percentages are available; otherwise leave omitted or use `minimum`/`maximum` fields

---

## Stephen's BODS Conversion Repositories

These are Stephen's Python repositories for transforming third-party corporate data sources into BODS 0.4. All are pure Python, structured as `src/bods_<source>/` packages with tests.

### bods-icij-offshoreleaks
**Source**: ICIJ Offshore Leaks database — covering Panama Papers (2016), Pandora Papers (2021), Bahamas Leaks (2016), Paradise Papers (2017), Offshore Leaks (2013). 810,000+ offshore entities.

**Mapping approach**:
- ICIJ `Entity` nodes → BODS entity statements (`registeredEntity` or `arrangement` for offshore vehicles)
- ICIJ `Officer` nodes → person statements or entity statements (heuristics classify names as natural person vs. corporate)
- ICIJ `Intermediary` nodes → entity statements (`registeredEntity`, service provider firms)
- ICIJ relationship types (`officer_of`, `intermediary_of`, etc.) → BODS ownership-or-control statements with appropriate `interests[].type`
- Neo4J export also available for graph database workflows

**Repo**: https://github.com/StephenAbbott/bods-icij-offshoreleaks

### bods-opencorporates
**Source**: OpenCorporates relationship data — the world's largest open company database, 200M+ companies.

OpenCorporates tracks four relationship types: `control_statement`, `subsidiary`, `branch`, and `share_parcel`. The Relationships Supplement contains 30M+ relationships extracted from primary datasets (SEC, UK Companies House, etc.).

**Repo**: https://github.com/StephenAbbott/bods-opencorporates

### bods-brightquery
**Source**: BrightQuery corporate data via opendata.org — 324M organisations, 512M locations, 1.2B contacts across 222 countries. Government-sourced data including corporate family structures, legal status, and identity crosswalks (LEI, CIK, ISIN, NPI, etc.).

**Repo**: https://github.com/StephenAbbott/bods-brightquery

### bods-kyckr
**Source**: Kyckr relationship data — a company intelligence platform providing corporate registry data and ownership relationships.

**Repo**: https://github.com/StephenAbbott/bods-kyckr

### bods-ftm
**Conversion**: BODS 0.4 ↔ FollowTheMoney (FtM) — **bidirectional**.

**Repo**: https://github.com/StephenAbbott/bods-ftm

Note: this is distinct from the archived `opensanctions/bods-ftm` (which only converted OpenOwnership data dumps to FtM and is no longer maintained). Stephen's `bods-ftm` is a current, bidirectional converter designed for general BODS 0.4 data.

**BODS → FtM mappings**:
- `entityStatement` → FtM `Company`
- `personStatement` → FtM `Person`
- `ownershipOrControlStatement` → FtM `Ownership`, `Directorship`, or `UnknownLink` (depending on interest type)

**FtM → BODS mappings**: reverse conversion using deterministic UUID5 hashing for consistent identifier generation.

**Technical approach**: two-pass processing (entities/persons first, then relationships); indirect ownership chains consolidated rather than split; converts between org-id.guide scheme codes (e.g., `GB-COH`) and FtM named properties (e.g., `registrationNumber`).

**CLI**: `cli.py` | **Input**: BODS or FtM JSON/JSONL | **Output**: converted format with full ownership relationship chains preserved.

### bods-aml-ai
**Conversion**: BODS 0.4 → Google Anti-Money Laundering AI input format.

**Repo**: https://github.com/StephenAbbott/bods-aml-ai

Google's AML AI data model has no native concept of party-to-party ownership relationships, so the tool encodes beneficial ownership creatively through available AML AI constructs:

**Output** (three NDJSON files):
- `party.ndjson` — persons and entities as `COMPANY` or `CONSUMER` types
- `party_supplementary_data.ndjson` — numeric ownership attributes (e.g., `bo_ownership_pct_{subject_id}`, `bo_is_beneficial_owner`, interest types)
- `account_party_link.ndjson` — synthetic "ownership accounts" linking subjects (`PRIMARY_HOLDER`) to owners (`SUPPLEMENTARY_HOLDER`)

**CLI**: `cli.py` | **Input**: BODS v0.4 JSON/JSONL | **Output**: NDJSON files for AML AI ingestion.

### bods-neo4j
**Conversion**: BODS 0.4 ↔ Neo4j graph database — **bidirectional**, with built-in graph analysis.

**Repo**: https://github.com/StephenAbbott/bods-neo4j

Note: this is Stephen's BODS-native converter. For the broader Neo4j + UK Companies House PSC demo (without BODS), see `erikbijl/neo4j-company-house-demo` in the Neo4j section of Developer workflows.

**Three primary workflows**:
1. **BODS → Neo4j**: import BODS ownership datasets into graph form via CSV export or direct driver loading; produces Neo4j-importable CSV files and Cypher scripts
2. **Neo4j → BODS**: export graph data back to standardised BODS JSONL, preserving all metadata (round-trip fidelity)
3. **Graph analysis**: built-in queries for UBO detection, corporate group mapping, and circular ownership identification

**CLI**: `cli.py` | **Input**: BODS v0.4 JSON/JSONL or Neo4j instance | **Output**: Neo4j CSVs/Cypher or BODS JSONL.

### bods-xml
**Conversion**: BODS 0.4 JSON → XML, in two output modes.

**Repo**: https://github.com/StephenAbbott/bods-xml

**Two modes**:
1. **Canonical** (`canonical.py`): a faithful XML serialisation of BODS 0.4 that preserves every field and mirrors the JSON structure, under the standard's namespace
2. **MRAS preBODS** (`profiles/mras.py`): transforms the flat BODS statement array into Canada's Multijurisdictional Registry Access Service (MRAS) hierarchical XML format

**Architecture**: extensible profile system — additional output profiles (BORIS, XBRL, etc.) can be added as modules alongside the existing two.

**CLI**: `cli.py` | **Input**: BODS 0.4 JSON or JSONL | **Output**: XML | **Tests**: 31

### bods-stream
**Type**: Live streaming web application — UK beneficial ownership changes in real time as BODS v0.4.

**Repo**: https://github.com/StephenAbbott/bods-stream
**Live demo**: https://bods-stream.onrender.com/

Consumes the **Companies House PSC Streaming API** and converts every live PSC (Person with Significant Control) filing event into BODS v0.4 statements the moment it's filed — displayed as a BOVS diagram with the raw Companies House event and the mapped BODS statements side by side.

This is notable because almost no beneficial ownership registers offer a streaming API. The UK PSC stream is the standout public exception, and BODS is purpose-built to represent change (`recordStatus` new/updated/closed, `replacesStatements`, append-only). bods-stream makes that change model visible live.

**What you see per event**:
- BOVS diagram: interested party → subject company, interest type on the edge, jurisdiction/nationality flags, identity-verification tick, tinted by lifecycle
- Lifecycle badge: `NEW` / `UPDATED` / `CEASED` (driven by BODS `recordStatus`)
- Risk signals (structural, no external calls): FATF black/grey list, non-EU jurisdiction, trust/arrangement, nominee, super-secure (opaque), sanctioned flag
- Prolific PSC signal: flags when one person appears as PSC of multiple companies in the session
- Live insight bar: individual vs corporate split, cessation rate, identity-verification rate, prolific PSC of the day
- Top-20 PSC nationalities (live flag tally)
- Pause/play with live event counter

**Architecture**: FastAPI backend (SSE relay — one long-lived CH stream connection, fan-out to many browsers) + React/Vite frontend. Single-process, in-memory state (lifecycle tracking, prolific tracker); nothing persisted to disk.

**Lifecycle handling**: The CH stream has no new/updated/closed concept. bods-stream maintains an in-memory map keyed on `resource_uri` (stable PSC id) to emit correct `recordStatus` values and `replacesStatements` references, including reconstructing a `closed` record from last-seen state when a deletion event arrives.

**Privacy**: Address and date of birth stripped at ingress — never broadcast or shown in UI. Date of birth used only briefly in-process for the prolific disambiguator.

**Key dependency**: [bods-mapper](https://github.com/StephenAbbott/bods-mapper) — a separate shared repo containing the core Companies House → BODS v0.4 mapping logic, used by both bods-stream and [OpenCheck](https://github.com/StephenAbbott/opencheck) to prevent the two apps drifting.

**Replay mode**: Set `BODS_STREAM_REPLAY_FILE` to a captured `.jsonl` to feed pre-recorded events through the live pipeline (useful outside UK office hours when the live feed is quiet).

**Deployment**: Docker image builds frontend and serves it with the API (same origin). Deployed on Render via `render.yaml`. Must run as one instance/one worker (in-memory state).

### bods-mapper
**Type**: Shared Python library — canonical UK Companies House PSC → BODS v0.4 mapping core.

**Repo**: https://github.com/StephenAbbott/bods-mapper

Extracted from OpenCheck so that both `opencheck` and `bods-stream` use one canonical mapper and cannot drift apart. Takes a single Companies House PSC streaming event (the `data` block is identical to the REST PSC endpoint response) and emits a BODS v0.4 bundle containing:
- the **subject company** entity statement
- the **interested party** — a `knownPerson` (individual PSC), entity statement (corporate/legal-person PSC), or `anonymousPerson` (super-secure PSC)
- an **ownership-or-control relationship** statement

**Key features**:
- All **86 official `natures_of_control` codes** mapped to valid BODS `interestType`, each with the official Companies House short descriptor in `interest.details`
- **Cessation lifecycle**: a ceased PSC produces a relationship with `recordStatus: "closed"` — stable `recordId`, distinct `statementId`, `interest.endDate`, and `replacesStatements` pointing to the original `new` statement, per BODS information updates / record identifiers modelling rules
- **Robust country handling**: emits a BODS `Country` `code` only when a valid 2-letter ISO code resolves

**Public API**: `map_psc_event`, `company_number_from_uri`, `parse_nature`, `describe_nature`, `PSC_NATURE_DESCRIPTIONS`, `country_object`, statement factories (`make_entity_statement`, `make_person_statement`, `make_relationship_statement`), `BODSBundle`, `stable_id`, `validate_shape`

**Requirements**: Python ≥ 3.10, `pycountry`. MIT license (vendored CH nature descriptors under OGL v3.0).

### opencheck
**Type**: Full customer due diligence (CDD) web application — LEI-powered, BODS v0.4 throughout.

**Repo**: https://github.com/StephenAbbott/opencheck
**Live demo**: https://opencheck.onrender.com/

OpenCheck is a comprehensive open-source CDD tool that uses the Legal Entity Identifier as a connector spine to fan out across 29 national and international corporate data sources, mapping everything to BODS v0.4. Currently at Phase 50 (50 phases of active development, 337+ commits).

**How it works**: paste a LEI → GLEIF lookup → derive every cross-source identifier available (Companies House number, Norwegian org number, Irish CRO, Finnish Y-tunnus, Latvian, Lithuanian, Estonian, Czech IČO, Polish KRS, Austrian Firmenbuchnummer, Slovak IČO, French SIREN, Dutch KvK, Swedish org number, Swiss UID, Canadian corp number, Belgian enterprise number, Danish CVR, Croatian MBS, Australian ACN/ABN, OpenCorporates ID, Wikidata Q-ID, and more) → fan out across all active adapters → assemble into a single BODS v0.4 bundle → apply risk signals → offer export.

**National ID search** (Phase 50): look up any company by local registration number (CH number, KvK, orgnr, CVR, SIREN, etc.) — queries GLEIF's three registration-ID filter fields in parallel, scoped to the RA code. Covers 17 countries with active adapters.

**Risk signal layer** (12 signals) — mirrors the EU AMLA draft CDD RTS conditions for "complex corporate structures":
- Source-derived signals (nominee, super-secure/opaque, sanctioned flag)
- AMLA CDD RTS signals (trust/arrangement, non-EU jurisdiction, ≥3 ownership layers, composite threshold rule, subjective obfuscation advisory)
- FATF jurisdiction (black/grey list)
- Cross-source name match discrepancies
- ICIJ Offshore Leaks match

**Export formats**: JSON / JSONL / XML / ZIP (downloaded bundle includes `LICENSES.md` listing every contributing source).

**Architecture**: FastAPI backend (Python 63%) + React/TypeScript frontend, cache-first dispatch (stub mode without API keys, live mode opt-in per source via env vars). Uses `bods-dagre` for BOVS ownership diagrams and `bods-mapper` for CH PSC → BODS mapping.

**Roadmap**: live opentender.eu procurement integration; BODS RDF/SPARQL backbone via Oxigraph (load assembled BODS bundle into triple store, expose `/sparql` for Open Ownership red-flag queries).

### bods-gql
**Conversion**: BODS 0.4 → Google BigQuery property graph, queryable with GQL (ISO/IEC 39075).

**Repo**: https://github.com/StephenAbbott/bods-gql

GQL (ISO/IEC 39075) is the international standard graph query language adopted in April 2024. It uses pattern-matching syntax similar to Cypher but with different syntax for quantified paths and aggregation. BigQuery now supports GQL for property graph queries.

**Output**:
- **Node tables**: entity and person nodes with names, jurisdictions, and identifiers
- **Edge tables**: ownership interest relationships with stake percentages
- **Property graph DDL**: `CREATE PROPERTY GRAPH` statements via `graph_schema/property_graph.py`

**Includes 14 pre-built GQL queries** across three modules covering UBO detection, corporate group mapping, and circular ownership analysis. 59 tests. Demonstrated with public BigQuery datasets containing GLEIF and UK Companies House beneficial ownership data.

**CLI**: `cli.py` | **Input**: BODS v0.4 JSON/JSONL | **Output**: BigQuery CSV tables + GQL schema.

---

## GLEIF Level 1 & 2 Data → BODS 0.4

The Global Legal Entity Identifier Foundation (GLEIF) publishes two levels of open data for the 2.6M+ entities holding a Legal Entity Identifier (LEI):

- **Level 1 (LEI-CDF)**: Entity identity data — legal name, registered address, jurisdiction, entity status, entity type, registration dates
- **Level 2 (RR-CDF — Relationship Records)**: Ownership relationships between LEI holders — parent/subsidiary links, percentage ownership, relationship status, and dates
- **Level 2 (Reporting Exceptions)**: Cases where an LEI holder cannot or will not report their direct/ultimate parent — with a stated reason code

### GLEIF → BODS 0.4 mapping

| GLEIF data | BODS statement type |
|---|---|
| Level 1: LEI-CDF record | Entity statement |
| Level 2: Relationship Record (RR-CDF) | Ownership-or-control statement |
| Level 2: Reporting Exception | Entity, Person, or OOC statement (depending on exception type) |

The **bods-gleif-pipeline** (https://github.com/openownership/bods-gleif-pipeline) is the reference implementation. It runs on AWS (Kinesis data streams for pipeline stages, Elasticsearch for persistence between runs, EC2 for compute). The raw GLEIF concatenated files are 8GB+ uncompressed.

GLEIF was the **first dataset published in BODS 0.4**, making it the reference example for temporal change tracking with `replacesStatements` and the `isComponent` pattern.

Key mapping decisions in the BODS 0.4 update:
- Reporting Exceptions are now modelled as BODS statements (rather than being dropped), allowing the reason for non-disclosure to be captured
- Temporal lifecycle of LEI data changes is represented via `replacesStatements` links rather than overwriting

**Published data**: https://bods-data.openownership.org/source/gleif_version_0_4/
**OpenOwnership news release**: https://www.openownership.org/en/news/global-legal-entity-ownership-data-available-in-line-with-latest-version-of-data-standard/
**Mapping blog post**: https://www.openownership.org/en/blog/updating-our-mapping-of-gleif-data-to-bods-to-better-capture-the-lifecycle-of-lei-data-changes/

---

## Corporate Ownership Data Sources: Background Reference

These are sources useful for mapping work or for contextualising BO data. Fetch live documentation for precise field-level detail.

### Sayari
A corporate intelligence platform covering 450M+ entities from 700+ sources across 250+ jurisdictions, with 2B+ ownership and control records. Sayari applies entity resolution to link records across sources, generating `possibly-same-as` relationships where confidence is insufficient to fully merge. Coverage includes parent-subsidiary, shareholder, and beneficial ownership structures. Particularly strong on hard-to-access jurisdictions.

- Data model: https://documentation.sayari.com/sayari-library/data-model/data-model
- Documentation: https://documentation.sayari.com/home/overview

### OpenCorporates
The world's largest open company database (200M+ companies). Offers four relationship types in its Relationships File/Supplement: `control_statement`, `subsidiary`, `branch`, `share_parcel`. The Relationships Supplement has 30M+ relationships from primary sources (SEC, UK Companies House, etc.) and is separately licensed from the company data. Also provides person-with-significant-control and beneficial_owner flags. The API (v0.4.8) exposes companies, officers, and relationships.

- API reference: https://api.opencorporates.com/documentation/API-Reference
- Relationships dictionary: https://knowledge.opencorporates.com/knowledge-base/data-dictionary-relationships/
- Officers dictionary: https://knowledge.opencorporates.com/knowledge-base/data-dictionary-officers/
- Relationship file key info: https://knowledge.opencorporates.com/knowledge-base/count-of-relationship-records/

### BrightQuery / OpenData.org
BrightQuery (founded OpenData.org) provides government-sourced corporate data on 324M organisations, 512M locations, and 1.2B contacts across 222 countries. Data is structured around three core data dictionaries: organisations, locations, and people-business relationships. Key differentiator: comprehensive reference ID crosswalks (LEI, CIK, ISIN, NPI, PermID, OpenFIGI, SAM UEI, PlaceKey, OSM ID, etc.) and corporate family/hierarchy structures. OpenData.org was built with Senzing AI for entity resolution and positions itself as a consortium-governed open data platform.

- Organisations dictionary: https://opendata.org/data-dictionary/organizations
- Locations dictionary: https://opendata.org/data-dictionary/locations
- People-business dictionary: https://opendata.org/data-dictionary/people-business

### InfobelPro
A global company data provider with 375M companies across 220 countries, sourcing data from 1,100+ official registries, tax authorities, and regulated filings. Provides 460+ firmographic, hierarchical, and technographic attributes per record, including ownership links and up to 8 years of historical records. Claims to trace every record to an official source (not aggregators or web scrapes). GDPR/CCPA compliant with stable entity IDs and standardised delivery across 200+ markets.

- Data overview: https://www.infobelpro.com/data
- Methodology: https://www.infobelpro.com/data/methodology

### OECD-UNSD Multinational Enterprise Information Platform (MEIP)
A joint OECD/UN Statistics Division initiative tracking the 500 largest MNEs globally. The platform comprises a Global Register (subsidiary ownership structures and geographic footprint), a web presence register, and a media monitor. The 2024 data release (covering data as of 31 December 2024) added financial data (employees, revenue, net profit, R&D) extracted via AI from company filings and annual reports. Structured as an interactive dashboard with downloadable XLSX.

This is a useful reference dataset for mapping MNE corporate group structures to BODS, and for validating coverage of other corporate data sources.

- Platform: https://www.oecd.org/en/data/dashboards/oecd-unsd-multinational-enterprise-information-platform.html
- Methodology publication: https://www.oecd.org/en/publications/the-oecd-unsd-multinational-enterprise-information-platform_b7d90a06-en.html
- Global Register 2024 (XLSX): https://www.oecd.org/content/dam/oecd/en/data/dashboards/oecd-unsd-multinational-enterprise-information-platform/Global%20Register%202024%20-%20OECD-UNSD%20Multinational%20Enterprise%20Information%20Platform.xlsx
- 2026 data release blog: https://www.oecd.org/en/blogs/2026/03/MNE-thing-is-possible-New-OECD-UNSD-data-release-strengthens-open-evidence-on-multinational-enterprises.html

---

## BODS Interoperability: Mappings to Other Data Models

### FollowTheMoney (FtM) / OpenSanctions
FollowTheMoney (FtM) is the data model used by OpenSanctions and the broader Aleph investigative data ecosystem. It represents persons, companies, assets, relationships, and documents in a property graph format designed for investigative and compliance work.

**bods-ftm** — there are two distinct repos with this name:
- **StephenAbbott/bods-ftm** (https://github.com/StephenAbbott/bods-ftm) — current, bidirectional BODS 0.4 ↔ FtM converter for general use (see Stephen's BODS Conversion Repositories section for full details)
- **opensanctions/bods-ftm** (https://github.com/opensanctions/bods-ftm) — archived; was a one-way converter from OpenOwnership BODS data dumps to FtM object graphs. Its functionality has been incorporated into **opensanctions/graph** (https://github.com/opensanctions/graph), which now handles BODS and GLEIF RR files as inputs.

The OpenOwnership dataset on OpenSanctions (https://www.opensanctions.org/datasets/openownership/) republishes OpenOwnership BODS data in FtM format, making it available for cross-dataset analysis alongside sanctions lists, PEPs data, and company registries.

**Practical use**: BODS data in FtM format can be combined with OpenSanctions sanctions data and public procurement data (Open Contracting Data Standard) for cross-dataset risk detection. The OpenScreening proof-of-concept built on this approach matches beneficial owners to sanctions names via a graph database.

### Senzing sz-semantics / RDF
The Senzing sz-semantics namespace (https://github.com/senzing-garage/sz-semantics/wiki/ns) defines an RDF Metadata Application Profile for representing entity resolution results as a knowledge graph. It explicitly aligns with BODS, NIEM, and FollowTheMoney as "popular controlled vocabularies used by Senzing partners."

The namespace provides:
- `sz:Entity` — resolved entity (top-level concept)
- `sz:Person`, `sz:Organization` — entity subtypes
- `sz:DataRecord` — source records contributing to entity resolution
- `sz:member_of` — relationship predicate applicable to ownership/membership

This is relevant when combining BODS data with Senzing entity resolution output, or when building linked data representations that need to align BODS concepts with Senzing's resolved-entity model. The OpenData.org platform (BrightQuery) was built using Senzing AI for entity resolution.

---

## Developer workflows

### Validating BODS data

Use **CoVE-BODS** web tool: https://datareview.openownership.org
Or use **lib-cove-bods** from the command line:
```bash
pip install lib-cove-bods
libcovebods your-data.json
```
Checks: required fields, valid enums, internal reference integrity, version compliance (0.1–0.4).

**bods-validator** — an alternative online validation and visualisation tool for BODS v0.4 data:
Repo: https://github.com/StephenAbbott/bods-validator

Built with FastAPI (backend) and React/TypeScript (frontend). Performs two layers of validation:
- JSON schema compliance checks against BODS v0.4 schema
- 26 additional regulatory compliance assessments via lib-cove-bods

Three input methods: direct JSON paste, file upload, or URL retrieval. Outputs validation results with actionable guidance, interactive ownership visualisations using BOVS design conventions, and side-by-side comparisons of national data formats mapped to BODS standards. Includes example datasets from UK, France, Indonesia, and Norway.

### Testing BODS implementations

Two companion packages provide a shared, canonical fixture suite for testing any tool that ingests, transforms, or emits BODS v0.4 statements:

**bods-fixtures** — the fixture data pack:
- Repo: https://github.com/StephenAbbott/bods-fixtures
- PyPI: https://pypi.org/project/bods-v04-fixtures/ (`pip install bods-v04-fixtures`)
- Provides small, curated BODS v0.4 statement bundles targeting specific semantic edge cases, each paired with a `.expected.md` specification file describing correct adapter/query engine behaviour
- Current coverage (v0.1.1): direct ownership, circular ownership, anonymous persons
- Import: `from bods_fixtures import load, list_cases`
- Acts as "the single source of truth" for fixtures across the BODS adapter ecosystem — ensures an entity observed in two sources produces equivalent BODS output

**pytest-bods-fixtures** — pytest plugin wrapping the data pack:
- Repo: https://github.com/StephenAbbott/pytest-bods-fixtures
- PyPI: https://pypi.org/project/pytest-bods-v04-fixtures/ (`pip install pytest-bods-v04-fixtures`)
- Exposes `bods_fixture` as an auto-parametrized pytest fixture — one test function runs against every conformance case in the data pack without manual parametrization boilerplate
- Displays fixture name in test IDs, making failures easy to identify
- Supports filtering by record type via `by_record_type()`

Both packages require Python ≥ 3.9. Fixture content is licensed CC-BY-SA 4.0; code is MIT.

### Processing BODS data into flat formats

**bodsdata** (https://github.com/openownership/bodsdata) converts BODS JSON to:
- CSV / TSV
- SQLite
- Parquet
- PostgreSQL dump

It also runs consistency checks (required fields, duplicate statement IDs, broken internal references) and supports pandas/polars dataframe workflows. Use it when you need to load BODS data into a database or do tabular analysis.

**BODSKit** (https://bodskit.readthedocs.io) is a newer CLI suite with similar goals — worth checking for the latest capabilities.

### Analysing BODS data in Python (notebooks)

**bodsanalysis** (https://github.com/openownership/bodsanalysis) provides:
- `qbods.py`: functions for reading, summarising and analysing BODS 0.2 data
- Jupyter notebooks: `latvia_demo.ipynb` (Latvia register), `Insights_UK_PSC_BODS-02.ipynb` (UK People with Significant Control)
- Runs on local Jupyter, Deepnote, or Google Colab

Note: the notebooks currently target BODS 0.2. For 0.4 data, adapt the field names (especially for `isComponent` and statement references).

### Beneficial Ownership Visualisation System (BOVS)

The **Beneficial Ownership Visualisation System (BOVS)** is an OpenOwnership specification for how to illustrate beneficial ownership structures as clearly as possible.

URL: https://www.openownership.org/en/publications/beneficial-ownership-visualisation-system/

BOVS defines the rules for drawing **BOVS Diagrams** — a standardised visual language for representing ownership and control structures. Key characteristics:

- Compatible with any brand, style, colour scheme, or language
- Published under the **GNU Free Documentation License** (free to use by anyone building BO visualisations)
- Designed to help implementers choose how to represent different aspects of ownership — direct vs. indirect interests, unknown intermediaries, control vs. ownership, etc.
- Offered to anyone building visualisations of beneficial ownership structures, not just BODS users

**BODS Visualisation Library** — the BODS-specific implementation of BOVS:
URL: https://www.openownership.org/en/publications/beneficial-ownership-data-standard-visualisation-library/

The BODS Visualisation Library bakes many of the BOVS rules into a reusable library designed for rendering BODS-structured data. It is already in production use in the official beneficial ownership registers of **Armenia**, **Bermuda**, and **Botswana**.

The `bods-dagre` npm package (see below) is the developer-facing tool that implements this library.

### Visualising ownership graphs

**visualisation-tool / bods-dagre** turns BODS JSON into directed graph diagrams.

Input: a JSON array of BODS statements (person, entity, ownership-or-control).
Output: SVG/canvas network diagram with:
- Person nodes (name, nationality flag, person-type icon)
- Entity nodes (name, jurisdiction flag, entity-type icon, public company indicator)
- Directed edges showing ownership/control relationships

npm package: `@openownership/bods-dagre`
```bash
npm install @openownership/bods-dagre
```

The tool handles temporal data — it filters to a snapshot at a given point in time when multiple versions of records exist. See the full spec at https://github.com/openownership/visualisation-tool/blob/main/docs/spec.md.

### Neo4j Graph Database: UK Companies House UBO Analysis

Graph databases are a natural fit for beneficial ownership data — ownership chains, loops, and ultimate parent traversal are graph problems that relational databases handle poorly. Two resources demonstrate this with UK data:

**Neo4j developer guide — Company Ownership & UBO Graphs**
URL: https://neo4j.com/developer/industry-use-cases/finserv/retail-banking/company-ownership-ubo-graphs/

Covers the conceptual case for graph technology for UBO analysis in financial services (retail banking context). Explains variable-length path traversal for finding ultimate beneficial owners, and introduces the UK PSC dataset as a practical source.

**erikbijl/neo4j-company-house-demo**
Repo: https://github.com/erikbijl/neo4j-company-house-demo
Webinar recording: https://go.neo4j.com/WBREDU260210FinServ_On-Demand.html

A working implementation using UK Companies House open data (snapshots from January 2026):
- **Data sources**: Companies House Company Data Product + PSC Data Product
- **Graph model**: five node types (Company, LegalEntity, Individual, Address, SIC-code) with three relationship types (OWNS, REGISTERED_AT, HAS_SIC)
- **Key notebooks**: `company_house_companies.ipynb` (loads company/address/SIC data) and `company_house_psc.ipynb` (processes PSC ownership relationships)
- **Includes**: pre-built Neo4j dashboard (Company_Profile_Dashboard_2026-03-31.json) and a database backup via Google Drive
- Enables variable-length ownership traversal, root entity identification, and detection of circular ownership structures

**GraphAware Hume platform: BODS data + graph technology for UBO investigations**
Blog/event page: https://www.openownership.org/en/blog/join-our-event-master-complex-ubo-investigations-with-advanced-graph-technology/
YouTube recording: https://www.youtube.com/watch?v=BO6TVN5UL14

A webinar co-presented with Stephen Abbott Pugh showing how BODS-structured beneficial ownership data can be used alongside other data types in GraphAware's Hume platform (powered by Neo4j). Hume is a graph-based investigation platform used in financial crime, compliance, and investigative journalism contexts. The session demonstrated how BODS data integrates with Hume's entity resolution and link analysis capabilities for complex UBO investigations.

**Relationship to BODS**: The neo4j-company-house-demo uses UK PSC data directly rather than BODS JSON, but the graph model (person/entity nodes + ownership edges) closely mirrors the BODS statement model. BODS data — which standardises this structure across jurisdictions — maps naturally onto Neo4j's property graph model and would enable cross-jurisdictional UBO traversal in a single graph.

### Generating test / sample BODS data

The **BODS data generator** is a Google Sheets template that lets anyone produce valid BODS JSON without writing code. It's the fastest way to create test data or demonstrate the standard to non-technical audiences.

- Template: https://docs.google.com/spreadsheets/d/1PHjwqiOguG8DqyXN75dNSpl_tNhTyelYav1B6sk8nRQ/
- User guide: https://www.openownership.org/en/publications/beneficial-ownership-data-standard-generator/user-guidance/

The sheet has three tabs mirroring the three BODS statement types:
- `1_person_main` — person statement data
- `2_entity_main` — entity statement data
- `3_ownership_control_main` — ownership-or-control statement data

Output: paste from the Upload sheet into CoVE-BODS for validation and JSON download. Can also feed directly into the bods-dagre visualiser.

Note: the generator currently targets BODS 0.3. For 0.4 you may need to adjust output for `isComponent` and `componentStatementIDs` fields.

### Working with BODS as Linked Data / RDF

**bodsld** (https://github.com/openownership/bodsld) provides:
- BODS 0.4 RDF vocabulary in Turtle format: `bods-vocabulary-0.4.0.ttl`
- HTML documentation: https://vocab.openownership.org/terms/bods-vocabulary-0.4.0.html
- Scripts to regenerate vocabulary from the JSON Schema

Note: bodsld maps the BODS *schema* to RDF vocabulary — it does not convert BODS *instance data* to RDF triples. If you need to convert actual BODS records to RDF, you'll need to write a custom transformation.

---

## Common patterns and gotchas

**Resolving references**: Ownership-or-control statements reference persons and entities by `statementId`. When loading data, build a lookup dict keyed by `statementId` first, then resolve references.

**Indirect ownership chains**: In BODS 0.4, `isComponent: true` marks statements that are part of an indirect chain. The top-level statement uses `componentStatementIDs` to list the supporting component statements.

**Temporal data**: The same real-world entity may have multiple statements over time. To get the current picture, filter to the most recent statement for each `statementId` group (using `replacesStatements`).

**Version detection**: Check `publicationDetails.bodsVersion` to know which version of BODS the data conforms to. Field names and required properties differ between 0.2, 0.3, and 0.4.

**Missing beneficial owners**: BODS allows for `unknownPersons`, `anonymousEntity`, and similar placeholders — your code should handle these rather than assuming all interested parties resolve to named individuals.

**Corporate-only datasets**: When the source has no BO data, every `interestedParty` in an ownership-or-control statement will reference an entity statement (not a person statement). This is valid BODS — entity-to-entity ownership chains are fully supported.

---

## Policy & Regulatory Context (summary)

For full detail, read `references/regulatory-context.md`.

### FATF Recommendations 24 & 25

The Financial Action Task Force sets the global anti-money-laundering standards that drive most beneficial ownership register legislation.

- **R.24 (Legal Persons)**: Requires countries to ensure that competent authorities have timely access to adequate, accurate and up-to-date beneficial ownership information on companies and other legal persons. Revised to be significantly stronger in 2022. Guidance published March 2023.
- **R.25 (Legal Arrangements)**: Parallel requirements for trusts and similar legal arrangements (fiducie, fideicomiso, Waqf, Treuhand, etc.). Revised 2023 to bring requirements broadly in line with R.24.

A country's compliance with R.24 and R.25 is assessed during FATF mutual evaluations, which have significant diplomatic and financial consequences.

### FATF Mutual Evaluations: Country-Level AML/CFT Assessments

**Mutual evaluations are the primary mechanism by which FATF assesses whether countries are actually implementing the 40 Recommendations.** When researching what AML/CFT legislation or BO requirements a specific country has in place — or how effectively they are enforcing them — the published mutual evaluation reports (MERs) and follow-up reports are the most authoritative and detailed source available.

#### How to find country reports

All FATF publications, filterable by country, are at: **https://www.fatf-gafi.org/en/publications.html**

This page lists every published MER, follow-up report, and other country-specific output for all FATF members and associate members. Each country has a tag page accessible from the publications index. **Important**: for countries that are members of a FATF-Style Regional Body (FSRB) rather than FATF itself, the full mutual evaluation report may be published on the FSRB's own website, with the FATF country page linking out to it. The Montserrat example illustrates this: the FATF page (https://www.fatf-gafi.org/en/publications/Mutualevaluations/Follow-upreportstothemutualevaluationofmontserrat.html) links to a report hosted on the CFATF website (https://www.cfatf-gafic.org/). When looking for a country's full MER, always check the FSRB's own website if the FATF page only shows a summary or a link.

Additional entry points:
- **All countries page**: https://www.fatf-gafi.org/en/countries.html — direct links to each country's profile and published reports
- **Consolidated assessment ratings**: https://www.fatf-gafi.org/en/publications/Mutualevaluations/Assessment-ratings.html — a spreadsheet of all technical compliance and effectiveness ratings from 2014 onwards across all assessed countries; the fastest way to compare multiple countries at once
- **Mutual evaluations topic page**: https://www.fatf-gafi.org/en/topics/mutual-evaluations.html — explains the process and links to recent reports

#### What mutual evaluations assess

The 4th-round methodology (https://www.fatf-gafi.org/en/publications/Mutualevaluations/Fatf-methodology.html) assesses countries on two dimensions:

**Technical compliance** — whether the country's laws, regulations, and institutional frameworks meet the requirements of each of the 40 Recommendations. Rated: Compliant (C), Largely Compliant (LC), Partially Compliant (PC), or Non-Compliant (NC). For BO purposes, the key ratings are on R.24 (legal persons) and R.25 (legal arrangements).

**Effectiveness** — whether the country's AML/CFT system is actually working in practice. Assessed across 11 Immediate Outcomes (IOs). For BO specifically, **IO.5** covers "Legal persons and arrangements are prevented from misuse for money laundering or terrorist financing, and information on their beneficial ownership is available to competent authorities without impediment." Effectiveness ratings: Substantial, Moderate, Low, or Negligible.

A country can have high technical compliance (good laws) but low effectiveness (poor enforcement) — a common pattern revealed in MERs. Conversely, some countries with imperfect legislation may have robust enforcement practices. Reading both dimensions together is essential.

#### Post-evaluation monitoring

After an MER is published, countries enter a follow-up process. Reports are typically published:
- **Regular follow-up**: annual or biennial reports on progress against recommended actions
- **Enhanced follow-up**: for countries with significant deficiencies, more frequent and intensive monitoring

Countries with serious and strategic AML/CFT deficiencies may be placed on the **Jurisdictions under Increased Monitoring** list (the "grey list") — https://www.fatf-gafi.org/en/publications/High-risk-and-other-monitored-jurisdictions/ — which triggers enhanced due diligence by financial institutions globally and carries significant reputational and economic consequences. Countries with the most serious deficiencies may be called to action on the **High-Risk Jurisdictions** list (the "black list").

#### The FATF Global Network: FSRBs

The FATF Global Network comprises FATF itself (39 member jurisdictions) plus nine FATF-Style Regional Bodies (FSRBs), which collectively cover more than 200 jurisdictions globally. FSRBs conduct mutual evaluations of their member jurisdictions using the same FATF methodology, and publish their own reports — which are the primary source for most non-FATF-member country assessments.

| FSRB | Region | Website |
|---|---|---|
| **APG** — Asia/Pacific Group on Money Laundering | Asia-Pacific | https://www.apgml.org/ |
| **CFATF** — Caribbean Financial Action Task Force | Caribbean | https://www.cfatf-gafic.org/ |
| **MONEYVAL** — Committee of Experts on AML/CFT Measures | Council of Europe member states | https://www.coe.int/en/web/moneyval |
| **ESAAMLG** — Eastern & Southern Africa AML Group | Eastern & Southern Africa | https://www.esaamlg.org/ |
| **MENAFATF** — Middle East & North Africa FATF | MENA | https://www.menafatf.org/ |
| **GIABA** — Inter-Governmental Action Group against ML in West Africa | West Africa | https://www.giaba.org/ |
| **EAG** — Eurasian Group | Central Asia & Russia region | https://www.eurasiangroup.org/ |
| **GAFILAT** — Financial Action Task Force of Latin America | Latin America | https://www.gafilat.org/ |
| **GABAC** — Action Group against ML in Central Africa | Central Africa | https://www.gabac.org/ |

When researching a non-FATF member country's AML/CFT framework or BO requirements, identify which FSRB it belongs to and check that FSRB's website for the most recent MER and follow-up reports — these will contain the most detailed analysis of what legislation is in place and how effectively it is being implemented.

#### Using MERs for BO research

Mutual evaluation reports are typically 200–400 pages and contain the most granular publicly available analysis of a country's BO legal framework. For BO-specific research within an MER, the most relevant sections are:

- The **Technical Compliance Annexe**: detailed analysis of R.24 (legal persons) and R.25 (legal arrangements) — what laws are in place, what they require, where they fall short of the FATF standard, and the resulting rating
- **Immediate Outcome 5**: the effectiveness assessment of whether the BO framework is working in practice — how well competent authorities access and use BO information, how well obliged entities conduct customer due diligence, and what the quality of BO information in registers actually is
- **Country context** (early chapters): background on the country's legal system, entity types, and the scale of the corporate sector — essential context for understanding why certain BO risks are higher or lower

### EU AML Package (2024)

The EU adopted a sweeping new AML package in May 2024, effective from 2027:
- **AMLR — Regulation 2024/1624**: Directly applicable rules for obliged entities (banks, lawyers, crypto). Lowers UBO threshold from >25% to ≥25% shareholding/voting rights. Requires multi-source verification of BO information.
- **AMLD6 — Directive 2024/1640**: Member State rules for central BO registers. Registers must hold more data, cover more entity types including non-EU entities with EU business. Registers must interconnect via European Central Platform. Transposition deadline: 10 July 2026.
- **EC consultation on BO data formats**: The Commission is consulting on standardised data formats for BO submissions to central registers — directly relevant to BODS adoption. See https://ec.europa.eu/info/law/better-regulation/have-your-say/initiatives/14851

### UK government endorsement of BODS

The UK has formally adopted BODS as its open standard for beneficial ownership data: https://www.gov.uk/government/publications/open-standards-for-government/collect-use-and-exchange-beneficial-ownership-information

The UK Anti-Corruption Strategy 2025 includes commitments to push for international adoption of BODS.

---

## BODS RDF: Linked Data and SPARQL Querying

The BODS RDF vocabulary (https://vocab.openownership.org/) enables beneficial ownership data to be published and queried as linked data. This extends the power of BODS significantly: ownership chains become graph traversal problems expressible in SPARQL.

### What the vocabulary provides

The BODS 0.4 RDF vocabulary maps all three BODS statement types — person, entity, and ownership-or-control — to RDF classes and properties. The key property is `bods:ownsOrControls`, which captures a direct ownership or control relationship between two entities (or between a person and an entity). This allows chains to be traversed with path queries.

The full vocabulary documentation is at https://vocab.openownership.org/ with the data model at https://vocab.openownership.org/pages/1_datamodel.html.

### SPARQL use cases (world.hey.com/cos series)

Four blog posts by the BODS RDF team document real SPARQL queries against the Open Ownership register:

- **Linking BODS with other datasets** (https://world.hey.com/cos/using-bods-rdf-to-link-beneficial-ownership-records-with-other-datasets-0383cbd9): How to combine BODS RDF with other linked datasets (e.g. Wikidata, company registries) using shared entity identifiers. Covers federated queries and URI alignment.

- **SPARQL examples for BO use cases** (https://world.hey.com/cos/bods-rdf-sparql-examples-for-various-beneficial-ownership-use-cases-284d6f73): A broad collection of queries covering: finding all companies owned by a person, tracing ownership chains of a given depth, identifying share percentages along a chain, filtering by interest type, and finding companies with anonymous/unknown owners.

- **Ultimate parents and corporate control** (https://world.hey.com/cos/ultimate-parents-and-corporate-control-with-open-ownership-bd1ee35b): How to use property path queries (`bods:ownsOrControls+`) to traverse chains and identify ultimate controlling entities regardless of chain length. Covers the distinction between direct and indirect control.

- **Querying UBOs** (https://world.hey.com/cos/querying-ubos-with-open-ownership-and-bods-rdf-6a272004): How to identify ultimate beneficial owners — the natural persons at the end of an ownership chain — using SPARQL. Includes queries that retrieve share percentages and interest types across intermediate links.

### Risk detection proof of concept (bodsriskdetection)

The **bodsriskdetection** repository (https://github.com/openownership/bodsriskdetection) is a proof-of-concept system built on BODS RDF. It combines:
- BODS data from the UK register (converted to RDF)
- Public procurement data published in OCDS format
- Sanctions data from OpenSanctions
- ICIJ Offshore Leaks data

The SPARQL graph can then identify: companies owned/controlled by sanctioned individuals; networks that have been awarded large volumes of public contracts; and indirect risks — third parties connected to a target that are themselves sanctioned or PEPs.

Technical details: https://www.openownership.org/en/publications/bods-risk-detection/bods-risk-tdetection-technical-details/

---

## Beneficial Ownership in Public Procurement

Linking beneficial ownership data with public procurement (contracting) data is one of the highest-impact use cases for BO transparency. It enables detection of conflicts of interest, sanctions exposure, bid-rigging networks, and related-party contracts.

### OCDS and BODS: the core linkage mechanism

The **Open Contracting Data Standard (OCDS)** (https://standard.open-contracting.org/) is the open standard for publishing procurement data. It covers the full contracting cycle: planning, tender, award, contract, and implementation.

The key to combining OCDS and BODS is **shared organisation identifiers**. Both datasets should use the same identifier scheme (typically from the org-id.guide list) for the same legal entities. The OCDS guidance page on beneficial ownership (https://standard.open-contracting.org/latest/en/guidance/map/beneficial_ownership/) explains two approaches:

1. **Separate registers with linked identifiers**: BO data is published using BODS; procurement data is published using OCDS; they are joined via shared company identifiers. This is the preferred approach for countries with a central BO register.

2. **BO data embedded in OCDS**: The OCDS beneficial owners extension (https://extensions.open-contracting.org/en/extensions/beneficialOwners/master/) allows BO information to be published directly within an OCDS contracting process record. Useful when no separate BO register exists, or when the procurement system has a lower disclosure threshold than the register.

### ChileCompra: the leading implementation

Chile has the most advanced operational integration of BO and procurement data globally (as of 2025–2026).

- Chile's procurement law was amended in December 2023 to require BO disclosure by all suppliers as a condition of participation.
- Every supplier that participated in 2025 disclosed its ownership information — covering 1M+ procurement procedures worth US$13 billion (January–September 2025). Over 185,000 beneficial owners are now on record.
- ChileCompra, the Comptroller-General, and the National Economic Prosecutor's Office have full access to BO data and use it for investigating economic crimes and non-competitive bidding practices.
- The definition of conflict of interest was broadened to cover all public officials and their relatives. Over 7,000 complaints received via a whistleblower hotline between 2023–2025, including 114 relating to conflicts of interest.
- In January 2026, ChileCompra announced detection of potential conflicts of interest worth CLP 3.452 billion through mass data cross-referencing.
- ChileCompra uses OCDS for structured procurement data publication.

**Case study (OCP/OO, May 2025)**: https://www.open-contracting.org/resources/casestudy-bot-pp-chile/
**OO publication**: https://www.openownership.org/en/publications/beneficial-ownership-in-chiles-public-procurement-reform/

### Slovakia RPVS: procurement-linked BO register

The Slovak **Register partnerov verejného sektora (RPVS)** (https://rpvs.gov.sk/rpvs) was one of the first purpose-built procurement BO registers, established in 2015. It lists individuals and organisations receiving public funds above a legal threshold. Companies face a ban of up to three years and fines up to €1 million for participating in procurement without registering.

RPVS data is available on OpenSanctions (https://www.opensanctions.org/datasets/sk_rpvs/) — sourced directly from the Ministry of Justice API — and on the BODS data explorer (https://bods-data.openownership.org/source/slovakia/).

### Philippines PhilGEPS

The Philippines passed the **New Government Procurement Act** (Republic Act No. 12009) in July 2024, mandating BO disclosure by all bidders and contractors, with public access to the data. Key milestones:
- From 15 July 2025, corporations must submit GIS forms reflecting BO information to the Securities and Exchange Commission (SEC).
- A Data Sharing Agreement between PS-DBM and the SEC facilitates data exchange.
- PhilGEPS enhanced its Open Data Portal in October 2025, providing real-time procurement data including BO information.

**Open data**: https://philgeps.gov.ph/CmsHomePages/open-data

### Entity identifiers in UK procurement data

A key technical challenge for joining BODS and OCDS data is identifier quality. A detailed analysis of entity identifier practices in UK public procurement data is available at: https://world.hey.com/cos/entity-identifiers-in-uk-public-procurement-data-5f3f3815

---

## Beneficial Ownership in Extractives (EITI)

The Extractive Industries Transparency Initiative (EITI) is the primary global framework for transparency in the oil, gas, and mining sectors. BO disclosure is a mandatory requirement for EITI implementing countries.

### EITI 2023 Standard: strengthened BO requirements

The 2023 EITI Standard significantly strengthened BO requirements (Requirement 2.5):

- Countries are encouraged to adopt a BO threshold of **10% or lower** (down from the previous 25% norm). As of 2025, 50 EITI countries have defined BO thresholds; half set it at 10% or below. Specific examples: Argentina (1 share), Colombia (5%), Nigeria (5%), Senegal (2%).
- New requirement for **full disclosure by politically exposed persons (PEPs)** regardless of ownership level — to detect conflicts of interest in licensing.
- New requirement to disclose **legal ownership structures** as well as beneficial ownership, to enable tracing of full ownership chains.
- Encouragement for companies to disclose their **complete ownership structure and chain** where beneficial ownership is held indirectly.

**2023 Standard PDF**: https://eiti.org/sites/default/files/2023-06/2023%20EITI%20Standard.pdf

### EITI State-Owned Enterprises (SOE) database

EITI launched a dedicated database of state-owned enterprises (https://soe-database.eiti.org/) covering ~100 SOEs across EITI implementing countries, with data going back to 2017. Key features:
- Data on SOE payments to government and other extractives disclosures
- Uses UUIDs for entities, enabling time-series analysis and interoperability with international databases
- Filterable by country, company, and sector
- API endpoint: https://soe-database.eiti.org/eiti_database

**BODS mapping**: A Jupyter notebook demonstrating how the EITI SOE database maps to BODS is at: https://github.com/civicliteracies/EITI_SDT_data_verification_and_validation/blob/sqlite/5_publish/1_test/eiti_bods_mapping.ipynb

The notebook shows how state bodies (ministries, agencies) holding direct or indirect controlling interests in SOEs can be represented using BODS entity statements and ownership-or-control statements, including the `stateBody` `entityType` and control interests without share percentages.

### BODS guidance for representing SOEs

The BODS standard has specific guidance on representing state-owned enterprises: https://standard.openownership.org/en/0.3.0/schema/guidance/repr-state-owned-enterprises.html

Key modelling decisions for SOEs in BODS:
- Use `entityType: "stateBody"` for the state or government agency holding the interest
- Control relationships (e.g. board appointment powers, policy direction) use `interests[].type: "otherInfluenceOrControl"` rather than shareholding types
- Where the state holds both equity and control, use multiple `interests[]` entries within a single OOC statement

---

## Public Beneficial Ownership Registers: Selected Examples

These are examples of live public BO registers — useful as reference implementations, data sources for mapping work, or for understanding diverse approaches to BO disclosure.

| Country/System | Register | Notes |
|---|---|---|
| Armenia | https://old.e-register.am/en/ | Early public BO register; BODS-aligned; company and BO data searchable online |
| Botswana | https://www.cipa.co.bw/master/ui/start/CIPARegisterSearch | CIPA register; BODS data collection + visualisation library; online search |
| Canada | https://ised-isde.canada.ca/cc/lgcy/fdrlCrpSrch.html?lang=eng | Corporations Canada federal register (live January 2024); BODS-powered; Bill C-42 mandate |
| BVI | https://gov.vg/news/legitimate-interest-access-now-fully-operational-virgin-islands | Legitimate interest access live from 1 April 2026; one of the first UK Overseas Territories to go live |
| EU (BORIS) | https://webgate.ec.europa.eu/e-justice/searchBoris.do | Cross-border search of EU/EEA member state registers; Norway joined April 2026 as 17th connected jurisdiction; mostly paywalled |
| Ghana | https://orc.dntsystems.net/beneficial-ownership/ | ORC BO register; Companies Act 2019; BO1–BO4 form suite |
| Latvia | https://www.lursoft.lv/en/latvian-company-register | First country to publish national BO data in BODS (2021) |
| Namibia | https://www.bipa.na/beneficial-ownership/ | BIPA BO register; Companies Amendment Act 2023; ~45% compliance as of 2026 |
| Nigeria | https://bor.cac.gov.ng/ | CAC Beneficial Ownership Register; first African BODS implementation; 5% threshold |
| Philippines | http://linkedin.com/feed/update/urn:li:activity:7442395219033219072 | Public BO data for companies in public procurement; New Government Procurement Act (RA 12009, 2024) |
| Slovakia (RPVS) | https://rpvs.gov.sk/rpvs | Procurement-linked BO register; one of the first purpose-built procurement BO registers (2015) |
| Sri Lanka | https://bo.drc.gov.lk/login | BO Registry Module live from 30 March 2026 (Gazette 2480/48); BO1–BO7 form suite; Registrar of Companies |
| St Helena | https://drive.proton.me/urls/WEC6VHS4DW#GmckfehJ8yk2 | UK Overseas Territory; public BO register delivered via a shared Proton Drive folder |
| UK | https://find-and-update.company-information.service.gov.uk/ | Companies House PSC register; largest public BO dataset globally; canonical BODS reference implementation |

For a global overview of BO register status by country, see the OpenOwnership map: https://www.openownership.org/en/map/

---

## EU BORIS: Beneficial Ownership Registers Interconnection System

BORIS (Beneficial Ownership Registers Interconnection System) is the EU's attempt to create a single search point for beneficial ownership data across EU and EEA member states, hosted on the European e-Justice Portal. In concept it should allow anyone — a compliance officer, investigator, or journalist — to conduct a single search and retrieve BO records from all connected national registers. In practice, its implementation has fallen significantly short of this goal.

### Regulatory basis

BORIS is mandated by three successive AML directives and an implementing regulation:

- **AMLD4 (2015/849)**: First required member states to establish central BO registers. https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=celex%3A32015L0849
- **AMLD5 (2018/843)**: Required public access to BO registers and mandated interconnection of national registers. https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=celex%3A32018L0843
- **Regulation 2021/369**: The specific implementing regulation establishing the technical and functional specifications for BORIS. https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX%3A32021R0369&from=EN

AMLD6 (2024/1640) and the 2024 AML Regulation (2024/1624) will significantly reshape the BO disclosure landscape from 2027, including interconnection requirements.

### Current status and limitations

As of April 2026, BORIS has fallen well short of its original 2020 go-live target, though connectivity is gradually growing. Only **6 member states** (Austria, Denmark, Greece, Latvia, Malta, Netherlands) have records fully searchable by name or company ID through the portal. **Norway joined in April 2026 as the 17th connected jurisdiction**, bringing the total number of EU/EEA countries that have completed the technical steps to provide data to the platform to 17 of 30 — but most records are either inaccessible or accessible only in paid PDF format.

Key structural limitations Stephen identifies in his Medium analysis (https://stephenabbottpugh.medium.com/challenges-in-realising-the-goal-of-the-eus-beneficial-ownership-registers-interconnection-system-7ec7b52575ae):

- **No machine-readable data**: Users can only download BO records as PDFs for individual companies; bulk data access is not available through BORIS
- **Paywalled records**: Most records require payment to access, limiting use by civil society and journalists
- **Incomplete ownership chains**: Records often show only direct beneficial owners; full chains through intermediate holding companies are rarely visible
- **UBO Data Rulebook scope gap**: The Rulebook underlying BORIS only covers legal persons — not legal arrangements (trusts, nominee relationships). BODS supports both, creating a structural gap between what BORIS captures and what full BO transparency requires
- **Identifier fragmentation**: BORIS relies on EUID-structured identifiers but many legal persons and arrangements lack an EUID, creating linkage failures across borders
- **Uneven national data quality**: The 17 connected registers have highly variable data quality, field coverage, and update frequencies. A search across BORIS does not guarantee comparable results across jurisdictions

### Related analysis

- Stephen's Bluesky post on BORIS: https://bsky.app/profile/stephenabbottpugh.bsky.social/post/3lkbe4wona22j
- OO: value of connecting EU BO data: https://www.openownership.org/en/blog/the-value-of-connecting-beneficial-ownership-data-across-the-european-union/
- Transparency International: barriers for investigators across EU: https://www.transparency.org/en/news/barriers-investigators-face-across-eu-tracing-asset-ownership

---

## Canada: Corporations Canada and the Pan-Canadian BO Register

Canada has moved from a fragmented, non-public BO regime to a public federal register and an ambitious programme to create a pan-Canadian repository using BODS.

### Corporations Canada federal register

Canada launched its **public, searchable beneficial ownership registry** in January 2024 under **Bill C-42** (An Act to amend the Canada Business Corporations Act). The register covers corporations incorporated under the Canada Business Corporations Act (CBCA), which includes all federally incorporated companies.

- Register search: https://ised-isde.canada.ca/cc/lgcy/fdrlCrpSrch.html?lang=eng
- The federal register uses **BODS** to structure and publish BO data. Open Ownership worked directly with ISED to implement BODS as the technical foundation.
- OO news: https://www.openownership.org/en/news/canada-passes-law-to-create-public-beneficial-ownership-register/

### BOP2P: Beneficial Ownership Policy to Practice

The **Beneficial Ownership Policy to Practice (BOP2P)** programme (https://ised-isde.canada.ca/mras/partners/bop2p/) is Canada's federal-provincial-territorial initiative to create a **pan-Canadian BO repository** — a single point of access to BO data from federal and provincial/territorial registries across Canada, not just CBCA companies.

The programme operates through the **Multijurisdictional Registry Access Service (MRAS)**, which already interconnects business registry data across Canadian jurisdictions. BOP2P is extending this to include BO data using BODS as the common data standard across jurisdictions.

Key design choices: BODS enables each jurisdiction to publish BO data in its own format and map to the standard, while the central MRAS layer aggregates into a coherent pan-Canadian view. Open Ownership is providing technical support including working with British Columbia — one of the first provinces implementing a provincial BO register expected around 2025.

---

## Beneficial Ownership Declaration and Data Collection Forms

BO declaration forms are the primary mechanism through which companies and their owners submit beneficial ownership information to a register. Form design has significant downstream implications for data quality: poorly specified fields, missing validation, and ambiguous instructions produce unreliable data that cannot be effectively used or linked across registers.

### OpenOwnership guidance: design principles and recommended fields

OpenOwnership has produced a suite of resources specifically for regulators and form designers.

**Guide for regulators and designers** (https://www.openownership.org/en/publications/beneficial-ownership-declaration-forms-guide-for-regulators-and-designers/): Covers the full process of form design — from defining legal scope, to structuring questions, to handling edge cases (joint ownership, nominee arrangements, trusts). Key principles: use unambiguous legal definitions for each data field; capture machine-readable identifiers (national ID number, date of birth, country of nationality) rather than relying on free-text names alone; include a clear effective date for each declaration; and design explicitly for update workflows, not just initial registration.

**Example declaration form** (https://www.openownership.org/en/publications/example-beneficial-ownership-declaration-form/): A reference implementation of a BO declaration form reflecting BODS data model requirements. Contains separate sections for: (1) company/legal entity being declared; (2) each beneficial owner — name, date of birth, nationality, country of residence, national identifier, nature of interest (shareholding percentage, voting rights, control mechanisms); (3) declarant details and signed attestation.

**Example paper forms** (https://www.openownership.org/en/publications/example-paper-forms-for-collecting-beneficial-ownership-data/): A set of five modular paper forms designed to be adaptable to different legal contexts. Covers natural persons, corporate beneficial owners, trusts, nominees, and declarations of no beneficial owner meeting the threshold.

**Annex — information fields** (https://www.openownership.org/en/publications/sufficiently-detailed-beneficial-ownership-information/annex-examples-of-information-fields-in-beneficial-ownership-declaration-forms/): A comparative analysis of the actual data fields used in BO forms across multiple jurisdictions. Useful for benchmarking what a register collects against best practice and BODS field coverage.

### EITI model declaration form

The EITI model beneficial ownership declaration form (https://eiti.org/guidance-notes/beneficial-ownership-model-declaration-form) is designed for the extractive sector and aligned with the 2023 EITI Standard (Requirement 2.5). It collects: beneficial owner full name, nationality, country of residence, national ID number, date of birth; level of ownership (percentage); how control is exerted (direct equity, indirect equity, voting rights, right to appoint management, other); whether the owner is a PEP (full disclosure required regardless of ownership level); and a signed attestation with effective date. The form explicitly captures reporting exceptions — cases where a BO cannot be identified — with a reason field.

### Country examples

#### Ghana — Office of the Registrar of Companies (ORC)

Ghana's Companies Act 2019 (Act 992) mandates BO disclosure for all companies registered in Ghana. The ORC uses a suite of differentiated forms depending on entity type:

- **BO1** — general companies (natural persons as beneficial owners)
- **BO2** — companies whose beneficial owners are themselves companies
- **BO3** (https://orc.dntsystems.net/wp-content/uploads/2025/08/BO3-Listed-Company-BO-Form.pdf) — **listed companies**: captures the same core fields but with additional sections for stock exchange listing, ISIN/ticker, public float percentage, and identification of any beneficial owners who hold ≥5% of listed shares directly or indirectly
- **BO4** (https://orc.dntsystems.net/wp-content/uploads/2025/08/BO4-Government-BO-Form.pdf) — **government-owned entities**: covers state bodies and SOEs; replaces natural-person BO identification with the details of the government ministry or agency holding the interest, the name and role of the political or administrative authority responsible, and the legal basis for government ownership

The form family illustrates how a register can accommodate the full range of entity types BODS models — `registeredEntity`, `publiclyListedCompany`, `stateBody` — within a single coherent disclosure regime.

#### Namibia — Business and Intellectual Property Authority (BIPA)

Namibia's Companies Amendment Act 2 of 2023 introduced mandatory BO disclosure. BIPA administers two forms:

- **BO1**: The primary declaration. Three sections — (A) company information and BO type; (B) beneficial owner particulars (full names, date of birth, nationality, residential address, national ID number, nature and extent of the beneficial interest); (C) completion notes and attestation. Covers natural persons, publicly listed companies, and government agencies as possible beneficial owner types.
- **BO2** (https://www.bipa.na/download/beneficial-ownership-declaration-form-bo2/): A "no change" declaration for annual returns confirming that no material change to BO information has occurred since the last filing.

The August 2024 deadline required all existing companies to file or bring BO information up to date. As of 2026, compliance stands at approximately 45%.

#### UK — PSC01 (Companies House)

The UK PSC (Persons with Significant Control) regime is the world's largest public BO register by record count and the canonical reference implementation for BODS. The **PSC01 form v4.0** (https://assets.publishing.service.gov.uk/media/6911eb1ce9348ac8fb54f480/PSC01_v4.0-FINAL.pdf) — updated November 2025 — is used to notify Companies House of an individual PSC.

**Five conditions for significant control** (any one triggers PSC status):
1. Holds, directly or indirectly, **more than 25% of shares**
2. Holds, directly or indirectly, **more than 25% of voting rights**
3. Holds the right, directly or indirectly, to **appoint or remove a majority of the board of directors**
4. Has the right to exercise, or actually exercises, **significant influence or control** over the company
5. Has the right to exercise, or actually exercises, **significant influence or control over a trust or firm** that itself meets one of the above conditions

**Fields collected**: full name; date of birth (month and year only — day withheld from public register); nationality; country/state of residence; service address; usual residential address (protected — not on public register); nature of control (checkbox against each of the five conditions, with percentage bands for conditions 1–2: 25–50%, 50–75%, 75–100%); date of notification; and from November 2025, confirmation of **identity verification** status.

The v4.0 update brings mandatory identity verification into the form, aligning with the Economic Crime and Corporate Transparency Act 2023. PSCs are required to verify their identity with Companies House directly.

---

## BODS Development: Open Issues and Feature Tracker

The BODS `data-standard` repository (https://github.com/openownership/data-standard) currently has **79 open issues**. The BODS Feature Tracker project board (https://github.com/orgs/openownership/projects/9/views/1) organises feature development into Research, Proposed, and Implementation phases.

When helping with BODS schema questions, check this tracker first — some apparent "gaps" in 0.4 are already documented as known issues with active research underway.

### Feature: Representing Assets (#752)

**Status**: Research. **Urgency**: Not currently urgent.

Proposal to extend BODS beyond its current scope of legal vehicles to represent the assets connected to beneficial ownership networks. Minimum viable fields suggested: `assetType`, `assetId`, `assetName`.

Asset classes identified as requiring representation: mining and drilling concessions (EITI); media outlets (Euromedia Ownership Monitor); energy projects (Global Energy Ownership Tracker); fishing and shipping vessels (Global Fishing Watch, Triton); financial assets (EU AMLD6, OECD CRS); mixed assets for wealth investigations.

Key design decision: financial assets derived from legal entity ownership (shares, options, fund units) should remain as **interest types** rather than distinct asset objects, to avoid complexity. Physical assets — land, vessels, bank accounts, concessions — are the primary target for a new `assetStatement` type.

See also: OO publication *Bridging the Gap* (https://www.openownership.org/en/publications/bridging-the-gap-for-effective-asset-transparency/).

### Feature: BODS Simplification (#737)

**Status**: Open / Backlog.

Goal: identify and remove unnecessary complexity from BODS to make it easier to understand and implement. Areas under discussion:

- **Terminology**: Remove redundant synonyms (`element`, `claim`, `assertion`); rename `assertedBy` → `statedBy`; replace `subject` with clearer language
- **Schema restructuring**: Streamline metadata outside `recordDetails`; clarify `declaration` vs `record` distinction
- **Potential removal**: `isComponent` and `componentRecordIds` fields (#718) — these add significant complexity for a use case that may be better handled differently
- **Scope**: Challenge whether PEP information belongs in a BO standard at all

Changes range from straightforward terminology fixes to potentially breaking schema restructuring, so the issue distinguishes quick wins from changes requiring broad stakeholder input.

### Feature: Interest Modelling (#466)

**Status**: Research. **Target**: Potential BODS v1.0.

The ~20 existing interest types in BODS 0.4 have two core problems:

1. **Prescriptive definitions**: Descriptions are tied to specific legal forms (e.g. voting rights defined as "rights of shareholders") that don't hold across all jurisdictions (UK companies limited by guarantee have voting members, not shareholders)
2. **Mixed categorisation**: The codelist conflates roles (e.g. board chair) with mechanisms (e.g. asset enjoyment), making mapping from local disclosure requirements ambiguous

Three proposed approaches under discussion: exhaustive codelist (research all disclosure regimes); hierarchical taxonomy (Ownership / Control / Benefit / Other); binary classifications (decompose rights into conveyance + exercise mechanism questions).

See also: OO research note *Describing Interests* (https://www.openownership.org/en/publications/describing-interests-research-note/).

### Feature: Republishing, Provenance and Transformation (#464)

**Status**: Research.

BODS was designed for original declarations, but aggregators (like the Open Ownership Register) republish and reconcile data from multiple jurisdictions. Current BODS structure cannot represent multiple-source provenance adequately.

Five user stories driving the feature: business analysts documenting data combination; NGOs demonstrating data provenance for trust; journalists verifying original sources; KYC architects distinguishing original vs republished datasets; end-users knowing whether data is confirmed, corroborated, or contradicted.

Main constraint: field-level provenance within BODS statements would make the standard "extremely unwieldy." The proposed solution combines schema changes with guidance — metadata-level provenance rather than field-level. Depends on related features: change-over-time representation, and separation of core data and metadata within statements.

### Feature: Representing Missing Information (#389)

**Status**: Research. **Comments**: 13 (active).

Covers 10 categories of missing or incomplete BO information: exempted entities; undisclosed shareholders known to be public companies; no beneficial owners meeting the threshold; inaccessible upstream information; uncooperative parties; unknown interest types; anonymous beneficial owners; non-filing companies.

Proposed typology distinguishes:
- **Exemptions**: Entity type or revenue threshold means disclosure not required
- **Missing by design**: Information not required to be collected
- **Required but missing**: Disclosure obligation exists but unfulfilled
- **Withheld**: Data collected but not published for legitimate reasons (protection, legal restriction)

Key modelling principle: separate *that* data is missing from *why* it is missing — these serve different analytical purposes. The GLEIF Level 2 Reporting Exceptions model is cited as a reference for how to handle this in practice.

See also: OO publication *Building an Auditable Record* (https://www.openownership.org/en/publications/building-an-auditable-record-of-beneficial-ownership/).

### Other notable open issues (selected)

| Issue | Title | Status |
|---|---|---|
| #742 | Unspecified or unknown entity | feature: missing information |
| #744 | publicationDetails no longer required? | under discussion |
| #743 | Consolidate placeOfBirth into addresses | enhancement |
| #741 | Open OOC statement referencing closed entity | documentation |
| #733 | Review conceptual and data model | conceptual model |
| #731 | Reconsider statementId length constraints | bug |
| #753 | Primer improvements needed | documentation |

---

## Global Energy Monitor: Global Energy Ownership Tracker

The **Global Energy Ownership Tracker (GEOT)** is a dataset maintained by Global Energy Monitor (GEM) tracking ownership of fossil fuel and heavy industry assets worldwide. As of the February 2026 release, it covers: coal plants, oil and gas plants, bioenergy plants, iron and steel plants, coal mines, iron ore mines, cement and concrete plants, and natural gas pipelines.

**BODS alignment**: The GEOT explicitly organises ownership data following the Beneficial Ownership Data Standard. The tracker follows the SEC's 5% beneficial ownership reporting threshold (Schedule 13D) — by capturing ≥5% ownership stakes, it provides a near-comprehensive view of controlling and significant minority interests, not just majority owners. The schema differentiates privately owned and publicly traded companies in line with BODS `entityType`, partly because US-listed companies are required to publish audited financials and BO information above 5%.

**OpenSanctions dataset**: The GEOT data is published on OpenSanctions (https://www.opensanctions.org/datasets/gem_energy_ownership/) in FollowTheMoney format, enabling cross-dataset analysis with sanctions lists, PEPs data, and procurement data.

**Why it matters for energy transition and climate accountability**:

- **Hidden climate liabilities**: GEM's report *World's Largest Oil and Gas Plant Owners Hide Billions of Dollars in Climate Costs* (https://globalenergymonitor.org/report/worlds-largest-oil-and-gas-plant-owners-hide-billions-of-dollars-in-climate-costs/) demonstrates how opaque ownership structures allow major fossil fuel operators to obscure their true climate exposure from investors and regulators.
- **Nominee structures**: *The Fossil Fuel Middlemen* (https://globalenergymonitor.org/report/the-fossil-fuel-middlemen-how-nominee-structures-obscure-australian-investments-in-coal-oil-and-gas/) shows how nominee arrangements in Australia obscure beneficial ownership of coal, oil, and gas investments.
- **Pension fund exposure**: Danwatch's investigation (https://danwatch.dk/en/hidden-co2-emissions-your-pension-money-is-polluting-the-planet-more-than-you-are-told/) used GEOT data to show how pension funds are exposed to hidden CO2 emissions through complex ownership chains.
- **Investment treaty risk**: E3G analysis (https://www.e3g.org/publications/investment-treaties-are-undermining-the-global-energy-transition/) shows how opaque ownership undermines accountability in energy transition investment treaties.
- **Policy brief**: OpenOwnership's *Shining a Light on Company Ownership* (https://www.openownership.org/en/publications/shining-a-light-on-company-ownership-the-role-of-beneficial-ownership-transparency-in-the-energy-transition/) links BO transparency directly to energy transition governance.

**Stephen's analysis**: https://www.linkedin.com/posts/stephenabbottpugh_energy-heavyindustry-opendata-activity-7435326197955260416--6uB/

---

## Beneficial Ownership in Fisheries Governance

Fisheries is one of the clearest sectoral use cases for BO transparency: opaque vessel and company ownership is a primary enabler of illegal, unreported and unregulated (IUU) fishing, which accounts for more than 1 in 5 fish taken globally and costs the global economy billions annually. The commercial fishing industry generates ~$141 billion/year; determining who benefits is often impossible through official records alone.

### Why UBO matters in fisheries

Beneficial owners of fishing vessels and quota holders routinely hide behind flags of convenience, shell companies, and nominee directors. Without UBO transparency:
- Licensing authorities cannot verify who actually controls a vessel or quota
- Sanctions and debarment are evaded by restructuring ownership
- Repeat IUU offenders reappear under new company names
- Subsidies flow to unscrupulous operators who remain unidentifiable

Transparency of UBO information — combined with vessel monitoring systems (VMS) and automatic identification systems (AIS) — enables authorities to: identify hidden links across fleets and flags; build enforcement cases that follow the money to beneficial owners; and detect beneficial owner connections between licensed and unlicensed vessels.

### Global Fishing Watch

Global Fishing Watch is the leading organisation advancing UBO transparency in fisheries globally. Their Vessel Viewer platform integrates ownership history with vessel tracking data. Key resources:

- **UBO overview**: https://globalfishingwatch.org/ultimate-beneficial-ownership-ubo/
- **Fact sheet**: https://globalfishingwatch.org/fact-sheet/ultimate-beneficial-ownership-why-transparency-is-vital-for-effective-fisheries-governance/
- **Vision document** (PDF): https://globalfishingwatch.org/wp-content/uploads/Global_Fishing_Watch-A-Vision-for-Ultimate-Beneficial-Ownership-in-Fisheries_ENG.pdf

GFW actively supports the integration of UBO data into national fisheries management systems and advocated at the FAO COFI meeting for vessel ownership transparency standards. In December 2024, the UN General Assembly adopted a resolution on sustainable fisheries that includes UBO transparency provisions — a milestone GFW helped advance.

### Standards and frameworks

- **FiTI Standard 2.0** (launched February 2026): The Fisheries Transparency Initiative's first major update since 2017. Beneficial ownership now has a central place alongside small-scale fisheries and development finance. The standard requires fishing licence holders and vessel owners to disclose their beneficial owners; countries are under increasing pressure to identify UBOs across the full fishing supply chain including transshipment and transport vessels.

- **Coalition for Fisheries Transparency Global Charter 2024** (https://fisheriestransparency.net/wp-content/uploads/2024/10/Coalition-for-Fisheries-Transparency-Global-Charter-2024-EN.pdf): Multi-stakeholder framework committing signatories to advance UBO disclosure as part of broader fisheries transparency.

- **Oceans 5** has funded work on developing a standard specifically for UBO reporting in the fisheries sector: https://www.oceans5.org/project/standard-for-ultimate-beneficial-ownership-reporting/

### Research and investigations

- **C4ADS — Anchors Away** (https://c4ads.org/commentary/anchors-away/): Analysis of how shell company structures shield fishing vessel owners from accountability.
- **C4ADS — Sea Shells** (https://c4ads.org/issue-briefs/sea-shells/): Deep-dive investigation into beneficial ownership in the fishing industry using open data.
- **Pew Charitable Trusts** (https://www.pew.org/-/media/assets/2023/10/ownership-of-fishing-companies-vessels-need-greater-transparency-and-accountability.pdf): 2023 report on the need for greater transparency and accountability in fishing company and vessel ownership.

### OpenOwnership publications on fisheries

- **Using Beneficial Ownership Information in Fisheries Governance** (https://www.openownership.org/en/publications/using-beneficial-ownership-information-in-fisheries-governance/): Policy brief on how existing BO transparency infrastructure can be leveraged for fisheries governance; includes use cases (licensing, corruption detection, policy monitoring) and recommended actions for governments, RFMOs, industry, and civil society.

- **Charting New Waters** (https://www.openownership.org/en/publications/charting-new-waters/): Joint UNODC/OpenOwnership report. Identifies structural challenges (quota trading, jurisdictional patchwork, industry fragmentation) and provides actionable recommendations. Key finding: systematic use of BO information could significantly improve fisheries governance through better licensing, corruption detection, and policy oversight.

---

## BODS in Practice: Case Studies and Real-World Implementations

The [beneficialownership.co.uk/case-studies](https://www.beneficialownership.co.uk/case-studies) page curates the principal real-world deployments of BODS. These cases span national registers, EITI extractives reporting, energy ownership tracking, commercial compliance tools, and register-technology products. Together they demonstrate the breadth of contexts in which BODS has been adopted as the common interchange format for beneficial ownership data.

### National Register Publications

**Latvia — first national BODS publication (2021)**: Latvia's Enterprise Register became the first national register to publish BODS-compliant data, establishing the template for how central registers can expose BO data in a machine-readable, interoperable format. The Latvia case study is the canonical proof-of-concept that a production national register can serialise to BODS. Case study: https://www.openownership.org/en/publications/latvia-beneficial-ownership-data-standard-case-study/

**Armenia — BODS beneficial ownership declarations**: Armenia implemented BODS for its BO declaration system, covering the lifecycle from collection to publication. The implementation shows how BODS structures person statements (declarants), entity statements (companies), and ownership-or-control statements (the links between them) in a live national context. Case study: https://www.openownership.org/en/publications/armenia-beneficial-ownership-data-standard-case-study/

**Botswana CIPA — data collection and visualisation**: The Companies and Intellectual Property Authority of Botswana adopted BODS for structured data collection from registrants and linked it to a dedicated visualisation library. The Botswana case is notable for covering the full pipeline: form → structured BODS data → network visualisation. Case study: https://www.openownership.org/en/publications/botswana-beneficial-ownership-data-standard-case-study/

**Nigeria CAC — first African BODS implementation**: The Corporate Affairs Commission of Nigeria was the first African registry to implement BODS, demonstrating applicability in a large, complex jurisdiction with high volumes of entity registrations. Case study: https://www.openownership.org/en/publications/nigeria-beneficial-ownership-data-standard-case-study/

**Indonesia — BODS 0.4 mapping**: Indonesia's BO register data has been mapped to BODS 0.4, providing a worked example of how a jurisdiction with a complex national data model can be normalised to the standard. See also the Indonesia country data profile in the OpenOwnership data repository.

**Slovakia RPVS — BODS data explorer**: Slovakia's Register Partnerov Verejného Sektora (partners of the public sector) has been mapped to BODS and published with an accompanying data explorer, making it one of the best-documented examples of a procurement-linked BO register publishing to BODS. Case study: https://www.beneficialownership.co.uk/case-studies

### Sector-Specific Implementations

**EITI SOE database — BODS mapping notebook**: The Extractive Industries Transparency Initiative's state-owned enterprise (SOE) database has been mapped to BODS in a published Jupyter notebook. This is the reference implementation for how EITI data (produced under Requirement 2.5 of the 2023 EITI Standard) can be represented as BODS statements, enabling cross-dataset analysis with national register data. Notebook: see EITI SOE database entry in the Extractives section above.

**Global Energy Ownership Tracker (GEOT)**: The Global Energy Monitor's tracker covers ~50,000 fossil fuel and power assets and their owners. GEOT is published as a BODS-aligned dataset and simultaneously on OpenSanctions in FollowTheMoney format — making it one of the largest real-world applications of BODS for energy sector ownership transparency. The 5% ownership threshold mirrors SEC reporting requirements. Full detail in the Global Energy Monitor section above.

**Canada BOP2P — pan-Canadian BO repository**: The Beneficial Ownership Policy to Practice (BOP2P) programme, delivered through MRAS, uses BODS as the common data format for a federated repository aggregating BO data across federal, provincial, and territorial jurisdictions. Canada is therefore the largest-scale deployment of BODS for cross-jurisdictional data aggregation. Full detail in the Canada section above.

### Commercial and Technology Implementations

**Structuriser**: A compliance SaaS platform that uses BODS as its internal data model for representing corporate structure and beneficial ownership information, enabling portability and interoperability of corporate ownership data across compliance workflows. https://structuriser.com/

**Foster Moore Verne®**: A register technology product built on BODS as its native data model. Verne demonstrates that register vendors are beginning to embed BODS natively rather than treating it as an export format, which has significant implications for data quality and interoperability at point of collection. https://www.fostermoore.com/verne

**NRD Companies BOREG©**: A beneficial ownership register product (developed by NRD Companies) that outputs BODS-compliant data. Another example of commercial register technology adopting BODS natively as output format. https://www.nrdcompanies.com/

### What these cases demonstrate collectively

Across these twelve implementations, BODS has been used in five distinct roles:

1. **National register publication format** — serialising existing register data into a standard interchange format (Latvia, Armenia, Nigeria, Indonesia, Slovakia)
2. **Data collection schema** — structuring the forms and back-end database that captures declarations from registrants (Botswana, Armenia)
3. **Cross-jurisdictional aggregation layer** — federating BO data from multiple jurisdictions into a single repository (Canada BOP2P)
4. **Sector-specific dataset format** — applying BODS outside company registers, to extractives (EITI SOE), energy (GEOT), and procurement (Slovakia RPVS) data
5. **Native data model in register/compliance products** — commercial products building BODS in from the start rather than as an afterthought (Structuriser, Foster Moore Verne, NRD BOREG)

The progression from "export format" to "native data model" in commercial products (roles 1→5) is a significant signal of BODS maturity.

---

## ICIJ: Investigative Journalism and Leaked Beneficial Ownership Data

The International Consortium of Investigative Journalists (ICIJ — https://www.icij.org/) is the world's leading cross-border investigative journalism network. Its landmark investigations — most notably the Panama Papers — have been the single most influential force in driving global political momentum for beneficial ownership transparency. ICIJ's work makes the harms of opaque company ownership concrete and legible to policymakers, civil society, and the public in a way that policy reports alone rarely achieve.

### ICIJ Investigations

**Panama Papers (2016)** (https://www.icij.org/investigations/panama-papers/): The largest data leak in history at the time of publication — 11.5 million documents from the Panamanian law firm Mossack Fonseca, revealing how offshore shell companies were used by politicians, business leaders, criminals, and celebrities to hide wealth, evade tax, and launder money. The investigation was published simultaneously by more than 100 media partners in 76 countries and is widely credited with accelerating the global move towards mandatory BO registers. Within months of publication, the UK expanded PSC registration requirements; the EU fast-tracked AMLD4; and the OECD and FATF both cited the Papers in pushing for stronger standards.

**Pandora Papers (2021)** (https://www.icij.org/investigations/pandora-papers/): A follow-up of similar scale — 11.9 million records from 14 financial service providers across the world. Revealed how the offshore system continued to operate despite post-Panama Papers reforms, with a particular focus on trusts (a significant gap in most BO register frameworks at the time) and real estate. Directly informed policy debates about BO requirements for trusts under AMLD5/AMLD6 and FATF Recommendation 25.

**FinCEN Files (2020)** (https://www.icij.org/investigations/fincen-files/): Based on leaked Suspicious Activity Reports (SARs) from the US Financial Crimes Enforcement Network. Showed that major global banks moved more than $2 trillion in transactions flagged by their own compliance staff as potentially suspicious — often through shell companies with opaque beneficial owners. Reinforced the case that BO transparency is necessary but not sufficient: BO data must be usable by financial institutions and law enforcement to be effective.

Other major ICIJ investigations relevant to BO include the Luanda Leaks (Angola sovereign wealth), the Luxembourg Leaks (EU tax avoidance), Swiss Leaks (HSBC/Falciani data), and the Malta Files. The full investigations index is at https://www.icij.org/investigations/.

### Offshore Leaks Database

ICIJ publishes a structured, searchable database of entities, officers, and relationships from its major data leaks at https://offshoreleaks.icij.org/. The database covers entities from the Panama Papers, Pandora Papers, Offshore Leaks (2013), Bahamas Leaks, and Paradise Papers. It is one of the largest publicly available sources of leaked beneficial ownership-relevant data and is widely used by journalists, researchers, and civil society to trace offshore ownership networks.

**Key characteristics**: The Offshore Leaks database is graph-structured (entities → relationships → officers/addresses), with node and edge data downloadable in bulk from https://offshoreleaks.icij.org/pages/database. It is one of Stephen's BODS mapping targets (see the `bods-icij-offshoreleaks` repository in Stephen's BODS Mapping Repositories section above). The data does not necessarily reflect current ownership — it captures a point-in-time snapshot from the leaked documents — but it is invaluable for historical investigation and network tracing.

**Important caveat for BO practitioners**: Presence in the Offshore Leaks database does not imply wrongdoing. Many offshore structures are legal, even if the context of their use is ethically questionable. This distinction is important when using the database as a reference source in BO-related analysis.

---

## Key Beneficial Ownership Research Reports

These reports are the foundational reference literature for the field of BO transparency and anti-corruption. They are regularly cited in policy documents, standard-setting processes, and advocacy work.

### World Bank: The Puppet Masters (2011)

**Full title**: *The Puppet Masters: How the Corrupt Use Legal Structures to Hide Stolen Assets and What to Do About It*
**URL**: https://documents.worldbank.org/en/publication/documents-reports/documentdetail/784961468152973030

The Puppet Masters is the seminal empirical study of how corrupt actors use legal persons and arrangements to conceal and move stolen assets. Analysing 150 grand corruption cases, it found that corporate vehicles — particularly chains of shell companies across multiple jurisdictions — were the mechanism of choice in the vast majority of cases. The study was foundational for the development of FATF Recommendations 24 and 25 (the core international BO standards) and remains the most-cited empirical basis for why mandatory BO registers are necessary.

Key findings: in nearly all cases studied, the corrupt used multiple jurisdictions; nominee shareholders and directors were used systematically to obscure true owners; and company service providers (CSPs) played a central facilitation role. The recommendations prefigure the approach now embodied in FATF R24/R25 and the EU AML package.

### World Bank: Signatures for Sale (2023)

**Full title**: *Signatures for Sale: How Nominee Services for Shell Companies are Abused to Conceal Beneficial Owners*
**URL**: https://openknowledge.worldbank.org/entities/publication/32914fa8-e9d5-59cc-b599-105962e9b390

A more recent World Bank analysis focusing specifically on nominee directors and shareholders — the human layer used to obscure beneficial ownership behind ostensibly compliant company records. The study investigates how nominee service providers operate globally, how they are used to circumvent BO disclosure requirements, and what reforms to CSP regulation and BO register design can address the problem. Directly relevant to debates about the reliability of BO data collected through self-declaration.

### Transparency International

**Into the Light — Benchmarking BO Transparency Frameworks: MENA** (https://www.transparency.org/en/publications/into-the-light-benchmarking-beneficial-ownership-transparency-frameworks-mena): Assesses the state of BO transparency in Middle East and North Africa countries, benchmarked against FATF standards and good practice. Useful reference for MENA register design work.

**Chasing Grand Corruption** (https://www.transparency.org/en/publications/chasing-grand-corruption): TI's investigation into how grand corruption networks — typically involving senior politicians and state officials — use offshore structures. Covers how BO opacity enables impunity and what investigative and enforcement tools can help.

**Legitimate Interest: Measures for Public Interest Stakeholders** (https://www.transparency.org/en/publications/legitimate-interest-measures-for-public-interest-stakeholders): A key policy paper on the "legitimate interest" access regime — the mechanism under EU AML law (post-Sovim judgment) by which journalists, civil society, and researchers can access non-public BO register data. Directly relevant to the ongoing EU debate about who can access BO data and under what conditions.

**Opacity in Real Estate Ownership Index 2025** (https://www.transparency.org/en/publications/opacity-in-real-estate-ownership-index-2025): A 2025 ranking of jurisdictions by the opacity of their real estate ownership regimes. Real estate is one of the most significant channels for BO-obscured money laundering; this index provides comparative data for policy and advocacy work.

### Transparency International UK

TI-UK has produced a series of reports on BO transparency with particular focus on UK Overseas Territories, Crown Dependencies, and the UK's own register quality. These are especially relevant given Stephen's work on UK and Crown Dependency BO regimes.

- **Opening Offshore Secrecy** (https://www.transparency.org.uk/publications/opening-offshore-secrecy): The case for public BO registers in Overseas Territories and Crown Dependencies — foundational advocacy document.
- **Improving the UK's Trust Registration Service** (https://www.transparency.org.uk/publications/improving-uks-trust-registration-service): Analysis of the UK's TRS (the register for express trusts), its current gaps, and recommended improvements. Highly relevant to FATF R25 implementation.
- **Unlocking Ownership Data** (https://www.transparency.org.uk/publications/unlocking-ownership-data): Broader analysis of how BO data quality and accessibility can be improved across UK registers.
- **Legitimate Interest access — Anguilla** (https://www.transparency.org.uk/publications/providing-legitimate-interest-access-anguillas-beneficial-ownership-data): Practical guidance on implementing legitimate interest access frameworks in Anguilla's BO register context.
- **Legitimate Interest access — British Virgin Islands** (https://www.transparency.org.uk/publications/providing-legitimate-interest-access-british-virgin-islands-beneficial-ownership-data): Same for the BVI — one of the largest offshore jurisdictions by entity count.
- **Legitimate Interest access — Bermuda** (https://www.transparency.org.uk/publications/providing-legitimate-interest-access-bermudas-beneficial-ownership-data): Same for Bermuda.
- **Legitimate Interest access — Cayman Islands** (https://www.transparency.org.uk/publications/providing-legitimate-interest-access-cayman-islands-beneficial-ownership-data): Same for Cayman — the world's largest offshore financial centre by assets under management.

The legitimate interest series is particularly important in light of the CJEU's *Sovim* judgment (November 2022), which ruled that unrestricted public access to BO register data under AMLD5 violated GDPR. The EU's response — a legitimate interest access regime under AMLR 2024/1624 — is still being implemented; TI-UK's country-specific guidance is among the most practically useful available.

---

## GODIN: Global Open Data Integration Network

The Global Open Data Integration Network (GODIN — https://godin.gleif.org/) is a collaborative initiative to enhance global data interoperability by connecting organisations that publish open data or create open data standards, aligning their data to common global frameworks — principally the Global Legal Entity Identifier (LEI) system managed by GLEIF.

**Stephen Abbott Pugh is a co-organiser of GODIN**, which reflects the network's position at the intersection of his work on BODS, GLEIF/LEI integration, and the broader open data ecosystem.

### What GODIN does

GODIN's core mission is to make open datasets more interoperable by: establishing shared entity identifiers (primarily the LEI, but also other open identifiers like Wikidata Q-IDs); creating mappings between member datasets; and publishing alignment data that enables cross-dataset analysis. The practical goal is a "Transparency Fabric" — a linked layer of open data connecting entities across registers, databases, and datasets using common identifiers.

The GODIN Transparency Fabric (https://transparencyfabric.gleif.org/) is the primary output: a growing set of mappings between GLEIF's LEI data and other open datasets from member organisations, enabling queries like "which entities in the OpenSanctions database have an LEI?" or "which BODS-published entities can be matched to a GEOT energy asset?"

### GODIN member organisations

| Organisation | Role in GODIN |
|---|---|
| **GLEIF** (https://www.gleif.org/en) | Host organisation; LEI system is the anchor identifier |
| **OpenOwnership** (https://www.openownership.org/en/) | BO data standard (BODS) and register data |
| **Global Energy Monitor / GEOT** (https://globalenergymonitor.org/projects/global-energy-ownership-tracker/) | Energy ownership dataset |
| **AC/DC — African Climate & Development Data Collective** (https://acdatacollective.org/) | African open data |
| **Media Registry** (https://www.mediaregistry.org/) | Media ownership transparency data |
| **Open Data Services Co-op** (https://opendataservices.coop/) | Technical implementation, standards tooling |
| **OpenSanctions** (https://www.opensanctions.org/) | Sanctions, PEPs, and FollowTheMoney data |
| **Data Research Center** (https://dataresearchcenter.org/) | Open data research and analysis |

**Wikidata** (https://www.wikidata.org/) is a GODIN supporter — its Q-identifiers are used as a secondary entity linkage mechanism alongside the LEI, particularly for entities that don't have or require an LEI (individuals, governments, some NGOs).

### GODIN GitHub repositories

The GODIN GitHub organisation (https://github.com/orgs/Global-Open-Data-Integration-Network/repositories) hosts the technical outputs: alignment datasets, mapping scripts, and Transparency Fabric tooling. This is where the practical data integration work is published in machine-readable form.

### GODIN in context of BO data work

GODIN is directly relevant to BODS and BO data interoperability in several ways:
- **LEI as entity identifier in BODS**: GLEIF's LEI is one of the identifier schemes supported in BODS entity statements. GODIN's alignment work makes it easier to match BODS-published entities with GLEIF Level 1 and Level 2 data.
- **Cross-dataset entity resolution**: When working across OpenSanctions (FollowTheMoney), GEOT (BODS-aligned), and GLEIF (LEI-CDF/RR-CDF), GODIN's mappings provide the linkage layer.
- **Media ownership**: The Media Registry's participation brings media ownership into the same interoperability framework — a growing area where BO transparency tools are being applied.
- **OpenSanctions integration**: OpenSanctions' membership means GODIN alignment data feeds into the world's most widely used open sanctions and PEPs dataset.

---

## Private Sector and Register APIs: How UBO/PSC Data Is Structured and Published

This section documents the principal APIs and data schemas used by commercial data providers and national registers to expose beneficial ownership and persons with significant control (PSC) data. These are the sources that practitioners integrate when building BO data pipelines, compliance tools, or register-to-BODS mappings.

### Kyckr

Kyckr (https://developer.kyckr.com/api/company-v2/#/) is a corporate data aggregator providing structured company and UBO data from multiple jurisdictions via a single API. It is one of the principal commercial intermediaries between national registers and compliance workflows, and is a primary target for Stephen's BODS mapping work.

**UBO schemas in the Kyckr v2 API**: Kyckr distinguishes three types of UBO entities:

- **CorporationUBO** (https://developer.kyckr.com/api/company-v2/#/schemas/CorporationUBO): Represents a corporate entity that is itself a beneficial owner — i.e., a legal person that holds an interest. Fields include the entity's name, registration number, jurisdiction, and the nature/percentage of its holding.
- **IndividualUBO** (https://developer.kyckr.com/api/company-v2/#/schemas/IndividualUBO): Represents a natural person who is the ultimate beneficial owner. Fields include name, date of birth, nationality, country of residence, and the nature and percentage of their interest. This is the most common UBO type.
- **OtherUBO** (https://developer.kyckr.com/api/company-v2/#/schemas/OtherUBO): Covers cases where the UBO is neither a standard corporation nor an identifiable individual — e.g., a government entity, a trust, or a case where ownership is unverifiable. Used for edge cases and "unknown UBO" representations.

This three-way split maps naturally onto BODS concepts: CorporationUBO → entityStatement + ownershipOrControlStatement; IndividualUBO → personStatement + ownershipOrControlStatement; OtherUBO → entityStatement with an unknown/other entity type + ownershipOrControlStatement with appropriate `missingInfoReason` or `unspecifiedReason` fields.

**Stephen's BODS mapping**: https://github.com/StephenAbbott/bods-kyckr — a working implementation of the Kyckr → BODS transformation. See also the Kyckr section in the "Corporate Ownership Data Sources: Background Reference" section above for broader context on Kyckr as a data source.

### Kausate

Kausate (https://docs.kausate.com/api-reference/company-data/extractUBOs) provides a dedicated `extractUBOs` endpoint as part of its corporate data API. The endpoint takes a company identifier and returns a structured representation of the company's UBO chain, including the ultimate natural persons at the end of the ownership chain and intermediate holding entities. Kausate's data model follows the pattern of layered entity resolution — traversing the ownership tree until natural persons are reached — which aligns with the BODS concept of chained ownershipOrControlStatements. Useful reference for understanding how commercial providers handle multi-hop ownership resolution vs. how BODS represents the same information.

### Netherlands KvK UBO Register API

The Dutch Chamber of Commerce (Kamer van Koophandel, KvK) operates the Netherlands UBO register as part of the Handelsregister (Companies Register). The register came into force on 27 September 2020 pursuant to AMLD4/AMLD5 implementation. UBO data is available via the KVK Dataservice in XML format, or as a certified PDF via KVK Online.

**Key data product: KVK uittreksel UBO-register**

The product is queried by KVK-nummer (8-digit company identifier) or RSIN (legal entity number). The response includes:

- **Maatschappelijke Activiteit / Onderneming**: company name, KVK-nummer, RSIN, legal form
- **UBO records** (one or more per company), each containing:
  - *Formele registratie*: `registratietijdstip` (timestamp of registration in the register)
  - *Materiële registratie*: `datumAanvang` (start date of the interest), `datumEinde` (end date, if applicable)
  - *Belang* (interest): `aard` (nature of the interest — e.g., "Houder van feitelijke zeggenschap" / holder of actual control, or "Houder van economisch belang" / holder of economic interest) and `omvang` (extent/percentage band — e.g., ">25% and ≤50%")
  - *Is Afgeschermd* (is shielded): boolean indicating whether the UBO's personal data is restricted due to a protection order
  - *Natuurlijk Persoon* (natural person): name, date and place and country of birth, address (restricted), land (country of residence), BSN or TIN + issuing country (restricted), nationality

**Access tiers**: Some fields (marked with `*` in the data model) — including date/place of birth, address, BSN/TIN — are non-public and only available to authorised organisations under Article 51b of the Handelsregisterbesluit (financial institutions, competent authorities). Public data includes name, nature of interest, and extent of interest.

**UBO obligation scope**: Registration is required for non-listed BVs and NVs, foundations (stichtingen), associations (verenigingen), mutual guarantee societies, cooperatives, partnerships (maatschappen, VOF, CV), shipping companies, church organisations, and European company forms (SE, SCE, EESV) with their statutory seat in the Netherlands. Foreign branch offices (Ltd, GmbH with Dutch branches) are exempt — their UBOs must be registered in the country of incorporation.

**Error/warning codes** of note for data pipeline work: `IPD0015` (entity not subject to UBO obligation), `IPD0016` (UBO-obligated entity but no UBOs yet registered), `IPD5101` (UBO data under investigation — a financial institution has queried the accuracy of the registered UBO(s) and triggered a review).

**BODS mapping notes**: The `aard` (nature) field maps to BODS `interests[].type`; `omvang` (extent percentage band) maps to `interests[].share.minimum`/`maximum`; `Is Afgeschermd` maps to BODS `interests[].unspecifiedReason` or person-level redaction flags. The tiered access model (public vs. restricted fields) is directly relevant to BODS discussions about what data to include in public vs. restricted BODS publications.

### Sweden Bolagsverket API

Bolagsverket is the Swedish Companies Registration Office. It provides APIs and open data for company information including beneficial ownership data registered under Sweden's implementation of AMLD5. The FAQ/overview of their API offering is at https://bolagsverket.se/apierochoppnadata/fragorochsvaromapierna.4611.html. Sweden's BO register, like the Netherlands', is a natural candidate for BODS mapping given its structured data model and public accessibility.

### Signicat UBO Lookup

Signicat (https://developer.signicat.com/docs/mint/steps/reference/data-verification/organisation-ubo-lookup/) provides a UBO lookup step within its Mint identity orchestration platform. The endpoint takes an organisation identifier and returns UBO data sourced from national registers, formatted for use in Know Your Business (KYB) and Know Your Customer (KYC) compliance workflows. Signicat's approach illustrates how BO data from registers is consumed in real-time identity verification contexts — a different use pattern from batch data pipelines. The data model exposed by Signicat reflects what is practically available from source registers, making it a useful reference for understanding cross-jurisdictional BO data field availability.

### UK Companies House: Persons with Significant Control (PSC) API

The UK's PSC regime is the most mature and technically well-documented BO register API in the world, and is the reference implementation for many BODS mapping discussions. The full API reference for PSC data is at https://developer-specs.company-information.service.gov.uk/companies-house-public-data-api/reference/persons-with-significant-control.

The PSC API exposes individual PSCs, corporate PSCs ("relevant legal entities", RLEs), other registrable persons, and "super secure PSCs" (where personal data is protected by a court order). Key fields include: `name`, `date_of_birth` (month and year only, publicly), `nationality`, `country_of_residence`, `natures_of_control` (a codelist of PSC control categories — percentage thresholds, voting rights, appointment rights, significant influence), and `notified_on`/`ceased_on` dates.

The `natures_of_control` codelist is one of the most detailed standardised BO control-type taxonomies available and is directly relevant to BODS `interests[].type` mapping. The UK PSC data is Stephen's canonical reference for BODS personStatement and ownershipOrControlStatement field design, and the UK is one of the few jurisdictions where BODS has an official government endorsement (see Policy & Regulation section above).

---

## Beneficial Ownership Data Verification

Verification is a critical and often underestimated element of beneficial ownership reform. Collecting and publishing BO data is only valuable if that data can be trusted to reflect reality. This section covers the concepts, practical steps, BODS technical mechanisms, international standards, and country examples relevant to designing and implementing BO data verification systems.

**Primary OO references**: principle page (https://www.openownership.org/en/principles/verification/), verification policy briefing (https://www.openownership.org/en/publications/verification-of-beneficial-ownership-data/), implementation checklist (https://www.openownership.org/en/news/designing-verification-systems-a-sample-implementation-checklist-for-beneficial-ownership-data/), and implementation guide data considerations (https://www.openownership.org/en/publications/guide-to-implementing-beneficial-ownership-transparency/data-considerations-for-beneficial-ownership-registers/).

### What verification means

**Verification is a combination of checks and processes that aim to ensure that beneficial ownership statements are accurate and complete at a given point in time.** This is distinct from authentication (confirming who is submitting) and from investigation (determining whether a declared structure reflects economic reality in a deeper sense). Verification addresses two failure modes: accidental error (data entered wrongly by mistake, e.g. typos, wrong field formats) and deliberate falsehood (data entered wrongly with intent to deceive).

Checks can be deployed at two stages:
- **At the point of submission**: format validation, cross-reference checks against other government databases, guided data entry to reduce errors
- **After submission/publication**: ongoing data quality monitoring, periodic rechecks, investigations triggered by suspicious or inconsistent data, third-party reporting obligations

A good verification system delivers data that is **accurate** (free from accidental error and falsehood), **complete** (free from omissions), and **reliable** — providing clarity about the provenance of the data and what checks have been applied, reducing risks of false data, and triggering appropriate alerts when data is incomplete, false, or suspicious.

### The three-part verification framework

BO data comprises three interconnected categories of information. Verification approaches differ across each.

**1. Verifying natural persons**

Key fields: name (including alternatives), nationalities, date of birth, place of birth, identification numbers (national ID, passport, tax number), place of residence, tax residencies, other addresses, PEP status, details of PEP status, unknown person indicators.

Verification mechanisms include: checking ID numbers against national identity registers or tax authority databases (where legislation permits); validating that addresses exist and match other government records; structured name fields (first/middle/last rather than a single freetext field) to reduce ambiguity; cross-referencing with PEP and sanctions lists; and confirming that the identification number format is valid (check digit verification). Automatic checks are most effective here because the data is structured and reference databases exist.

**2. Verifying entities**

Key fields: entity type (registered company, legal arrangement, anonymous, unknown), reasons for anonymity/unknown status, name and alternatives, incorporation details, identification numbers (company number, LEI), foundation date, dissolution date, addresses.

Verification mechanisms include: checking that the company number and name correspond to the details held in the national business register; flagging dissolved companies; validating addresses against official address registers; and detecting mismatches between the declared entity type and the company register record. Critically, these checks become far easier to automate when the BO system and the company register use the same identifiers for entities — a strong argument for aligned identifier schemes (see BODS entity identifiers, GLEIF LEI).

**3. Verifying ownership or control relationships**

Key fields: subject of the relationship (entity being owned/controlled), whether ownership is direct or indirect, the interested party, type of interest (shareholding, voting rights, appointment rights, significant influence/control), interest level/percentage share, start date, end date.

Ownership or control structures are harder to check automatically than person or entity fields because there is no single reference database of "true" ownership. Some automatic checks are still possible: verifying that a start date is not in the future; that an end date follows the start date; that all required fields are populated; that the entity ID used in the relationship statement is valid and matches a known entity. Beyond these, verification typically requires manual cross-referencing against other records, notarial documentation, or intelligence from financial institutions.

### Verification stages and workflow

A worked verification workflow proceeds as follows:

1. **Pre-submission guidance**: Well-designed data collection forms with field-level guidance reduce error at source. Structured fields (separate first/middle/last name; date picker rather than freetext date; validated ID number format) prevent the most common accidental errors before the data enters the system.
2. **Automatic checks at submission**: On receipt of a submission, the system runs: format validation; database cross-checks (company register, identity register, address register, PEP/sanctions lists); business rule checks (no impossible dates, no already-dissolved company as subject, no self-referential ownership). Submissions failing checks are returned to the declarant with specific error messages.
3. **Human review queue**: Submissions flagging potential issues — but not definitively invalid — enter a review queue for manual assessment by register staff. Staff may request additional supporting documentation: certified company formation documents, shareholder agreements, certified translation of foreign documents.
4. **Post-publication monitoring**: Published data is periodically rechecked against updated reference databases. Changes in the company register (dissolution, change of directors) trigger alerts for corresponding BO records. Financial institutions and other obliged entities subject to Know Your Customer/Know Your Business requirements have an obligation to consult the BO register and report discrepancies they find to the register authority.
5. **Ongoing update obligations**: Declarants are required to update BO information within a specified timeframe (typically 14–30 days) when it changes. Failure to update is itself a compliance failure subject to sanctions.

### Sanctions and enforcement

Verification is only effective if non-compliance has consequences. An effective sanctions regime should:

- Cover all forms of non-compliance: non-submission, late submission, incomplete submission, and false submission
- Apply to all relevant parties: the person making the declaration, the beneficial owner themselves, registered officers of the company, and the declaring company
- Include both **monetary** penalties (fines) and **non-monetary** penalties (striking off, disqualification from public procurement, licence revocation) — the latter are often more powerful deterrents
- Empower relevant agencies (register authority, financial intelligence unit, tax authority, sector regulators) to enforce
- Align sanctions with policy goals: if BO transparency is mandated for public procurement, non-compliance should trigger procurement exclusion; if mandated for extractives licensing, non-compliance should be grounds for licence refusal or termination
- Make data on non-compliance publicly available to enable civil society and media scrutiny

The Kyrgyz Republic's 2018 subsoil use regulation is an example of sector-aligned sanctions: false or missing BO data is explicitly grounds for licence termination under Article 21.9.

### BODS technical mechanisms for verification

BODS 0.4 provides a `source` object on all three statement types. The `source.type` field supports `"selfDeclaration"` (the declarant provided the information themselves) and `"verified"` (the information has been subject to verification by the publishing authority). When `source.type` is `"verified"`, the source object can additionally record:

- `description`: a narrative description of how verification was carried out
- `url`: a link to the verification methodology or evidence
- `retrievedAt`: when the verification was performed
- `assertedBy`: the person or organisation that carried out the verification

This mechanism allows BODS publishers to mark an entire statement — a person, an entity, or an ownership/control relationship — as verified, and to record the provenance of that verification. It is the primary technical mechanism by which data trust can be encoded in a BODS dataset.

**Future direction**: As of the 2022 OO analysis, there was active consideration of extending verification to the field level — i.e., marking individual attributes within a statement as verified (e.g., "this person's ID number has been verified against the national identity register") rather than only marking the whole statement. This was being tracked as a BODS feature development issue on GitHub. See BODS open issues section above for the feature tracker.

### FATF standards on verification

**FATF Recommendation 24 — Legal Persons**: Section 7 of FATF's Guidance on Beneficial Ownership of Legal Persons (https://www.fatf-gafi.org/en/publications/Fatfrecommendations/Guidance-Beneficial-Ownership-Legal-Persons.html) addresses "Accurate information – means of verification of beneficial ownership information." It sets out the range of mechanisms countries may use to verify BO information held in central registers, covering: self-declaration with criminal liability for false statements; cross-checking against other government databases (company register, tax authority, financial supervisors); obliged entity reporting requirements; and risk-based enhanced verification for higher-risk companies. FATF distinguishes between information that can be verified automatically and information requiring more resource-intensive checks, and expects countries to adopt a layered approach.

**FATF Recommendation 25 — Legal Arrangements**: Section 4 of the Guidance on Beneficial Ownership and Transparency of Legal Arrangements (https://www.fatf-gafi.org/en/publications/Fatfrecommendations/Guidance-Beneficial-Ownership-Transparency-Legal-Arrangements.html) covers "Adequate, accurate and up-to-date information" for trusts and similar arrangements. The verification challenge for legal arrangements is structurally different from companies: there is no universal register of trusts in most jurisdictions, and the trustee (rather than a central authority) is typically the primary record-keeper. FATF R25 therefore focuses on: obligations on trustees to maintain accurate records; obligations on professional trustees and trust service providers to verify beneficiary information; and the role of tax authorities (via automatic exchange of information) in identifying trust-held assets.

### Country examples: Latvia and Denmark

**Latvia** undertook a five-year reform process to update its BO legislation, sanctions regime, and data publication framework. Latvia now publishes open BODS-compliant data from its Enterprise Register. The verification system includes:

- **In-depth checks at registration**: assessment of risks associated with the country of residence of the declared beneficial owner; examination of the UBO's involvement in other legal persons; review of publicly available information on the beneficial owner's reputation
- **Request for additional documentation** when checks raise doubts: certified evidence of the basis for control claimed; certified identity documentation; evidence that it is genuinely impossible to determine the beneficial owner; documents proving the full ownership structure
- **FIU referral**: where potential risks are identified during registration, the Enterprise Register disseminates a report to the Financial Intelligence Unit

**Denmark**'s Central Business Register (CVR) uses a combination of automatic and manual verification with some machine learning:

- **Automatic checks**: the civil registration number (CPR number) is unique and validated automatically; addresses are checked against the Danish Address Register; business rules prevent logically impossible situations (e.g., registering a deceased person as a UBO; declaring a company that has been dissolved)
- **Prefilling from authoritative sources**: key entity details are prefilled by pulling data from the company register based on the company registration number, reducing data entry errors
- **Machine learning**: used to identify patterns associated with potential risk or data quality issues in submitted BO information
- **Random audits**: in 2019, the Danish Business Authority randomly selected 500 companies with recorded BO information to verify their submissions
- **Dissolution power**: the Danish Business Authority has a legal basis to dissolve companies where BO information is missing or inadequate — a powerful non-monetary sanction
- **Third-party reporting**: external parties (financial institutions, lawyers, accountants) are legally obliged to report BO discrepancies they identify

### Additional reference resources

- **OECD Effective Beneficial Ownership Frameworks Toolkit (2nd edition, 2024)** (https://www.oecd.org/content/dam/oecd/en/networks/global-forum-tax-transparency/effective-beneficial-ownership-frameworks-toolkit-second-edition-2024.pdf): Comprehensive toolkit from the OECD Global Forum on Tax Transparency, including detailed guidance on verification mechanisms as part of building effective BO frameworks. The 2nd edition updates the original 2023 toolkit with new country examples and implementation guidance.
- **OECD BO Toolkit (original)** (https://www.oecd.org/content/dam/oecd/en/networks/global-forum-tax-transparency/beneficial-ownership-toolkit.pdf): The foundation document; covers the full BO framework design including data collection, verification, access, and international cooperation.
- **Tax Justice Network: Beneficial Ownership Verification** (https://taxjustice.net/reports/beneficial-ownership-verification-ensuring-the-truthfulness-and-accuracy-of-registered-ownership-information/): TJN's analysis of what makes BO verification effective, focusing on the truthfulness and accuracy of registered information. Provides a civil society perspective on gaps in current verification practices and recommendations for strengthening them.
- **Moody's KYC: Brief Guide to UBO Verification Legislation** (https://www.moodys.com/web/en/us/kyc/resources/insights/who-is-in-charge-here-brief-guide-to-ultimate-beneficial-owners-verification-legislation.html): A private sector/compliance perspective on UBO verification requirements as seen by financial institutions subject to KYC/KYB obligations. Useful for understanding how the compliance industry approaches verification and what data they require from registers.

---

## Recent Register Developments (2026)

This section records significant developments in beneficial ownership registers and access regimes that occurred in 2026, providing a running reference for the fast-moving reform landscape.

### BVI: Legitimate Interest Access Live (1 April 2026)

The British Virgin Islands activated legitimate interest access to its beneficial ownership register on **1 April 2026**, making it one of the first UK Overseas Territories to go live with a functional access mechanism for journalists, civil society, and other public interest stakeholders following years of pressure from the UK Parliament and anti-corruption campaigners.

The access framework is governed by revised BO guidelines published in January 2026 (https://www.bvifsc.vg/sites/default/files/revised_bo_guidelines_final_version_for_publication_02.01.26_0.pdf) and implemented via the BVI Financial Services Commission's Industry Circular 11-2026 (https://www.bvifsc.vg/news/industry-updates/industry-circular-11-2026-launch-legitimate-interest-transactions-and-request). Requestors must demonstrate a legitimate interest and undergo an application process; access is not unrestricted public access. Official announcement: https://gov.vg/news/legitimate-interest-access-now-fully-operational-virgin-islands.

This is directly relevant to the TI-UK legitimate interest access series (see Key Beneficial Ownership Research Reports section), which includes a specific publication on providing legitimate interest access to BVI BO data.

### Sri Lanka: BO Registry Module Live (30 March 2026)

Sri Lanka launched its **Beneficial Ownership Registry Module** on **30 March 2026**, hosted by the Registrar of Companies (Department of the Registrar of Companies): https://bo.drc.gov.lk/login.

The legal basis is the Sri Lanka BO Regulations gazetted on **21 March 2026** under Gazette No. 2480/48, effective 30 March 2026. The regulations introduce a suite of **seven BO forms** (BO1–BO7), each tied to a specific corporate event:

| Form | Trigger | Filing deadline |
|---|---|---|
| **BO1** | Incorporation | Filed together with Form 1 at incorporation |
| **BO2** | Share issue (Form 6) | Within 20 working days of issue |
| **BO3** | Share transfer | Within 20 working days of transfer |
| **BO4** | Annual Return (Form 15) | Simultaneously with the annual return |
| **BO5** | Appointment/change of authorised BO person | On appointment or change |
| **BO6** | Location of BO records | Declares where physical BO records are held |
| **BO7** | Core BO data form | Data capture for each individual beneficial owner |

The BO1–BO6 forms are event triggers; BO7 is the substantive data form that captures the beneficial owner's personal and interest details. This event-linked form architecture — where a separate form is filed for each corporate event that changes BO status — is a distinct approach compared to jurisdictions that use a single annual disclosure form. For analysis see: https://www.linkedin.com/pulse/sri-lankas-beneficial-ownership-registry-now-live-heres-medagoda-5sn2c/

Note: Sri Lanka's BO regulations are in Sinhalese (the Gazette is not translated into English). The form architecture described above is drawn from an English-language summary of the regulations.

### Sweden: Legitimate Interest Access Approved (from 1 July 2026)

The Swedish Parliament (Riksdag) has approved legislation to introduce robust legitimate interest access to Sweden's beneficial ownership register, aligned with the requirements of the Sixth Anti-Money Laundering Directive (AMLD6). The changes apply from **1 July 2026**. Parliamentary document: https://www.riksdagen.se/sv/dokument-och-lagar/dokument/betankande/utlamnande-av-uppgifter-ur-registret-over-verkliga_hd01fiu35/

Sweden's register is operated by Bolagsverket (see Private Sector and Register APIs section). This development brings Sweden's access regime into line with the AMLD6 requirement for a legitimate interest access mechanism following the CJEU's *Sovim* judgment, which struck down unrestricted public access.

### Norway: 17th Jurisdiction to Join BORIS (April 2026)

Norway became the **17th jurisdiction** to make its beneficial ownership information searchable via the EU's BORIS system in April 2026, notable because Norway is not an EU member state but participates as an EEA country. This brings the total connected jurisdictions to 17 out of 30 EU/EEA countries. The EU BORIS section above has been updated to reflect this.

Norway's BO register (Brønnøysundregistrene) already has a well-documented public API (see Country-Specific Registers table) — BORIS connectivity adds a cross-border search layer on top of the existing national data.

### Ontario: BO Registry Committed by 2027

The Canadian province of Ontario committed in its 2026 budget to establish a beneficial ownership registry by **2027** as part of efforts to combat money laundering and fraud through enhanced corporate transparency. Budget reference: https://budget.ontario.ca/2026/chapter-1b-safety.html#section-9

This adds Ontario to the growing list of Canadian sub-national jurisdictions working toward BO disclosure, and represents a significant development given Ontario's size as Canada's largest provincial economy. At the federal level, Corporations Canada and BOP2P are already operational (see Canada section above).

### Philippines: Public BO for Procurement Now Live

The Philippines now makes beneficial ownership information **publicly available** for companies involved in public procurement, following the New Government Procurement Act (Republic Act No. 12009, July 2024). This means that information on who ultimately owns and controls companies bidding for or holding government contracts is accessible publicly — a significant step beyond the initial BO disclosure requirement, which mandated collection but not necessarily public access. LinkedIn post: http://linkedin.com/feed/update/urn:li:activity:7442395219033219072

This builds on the Philippines' existing BO framework via PhilGEPS and is covered in more detail in the Beneficial Ownership in Public Procurement section above.

### St Helena: Public BO Register via Proton Drive

The **St Helena** beneficial ownership register — for this UK Overseas Territory in the South Atlantic — is published as a **publicly accessible Proton Drive folder**: https://drive.proton.me/urls/WEC6VHS4DW#GmckfehJ8yk2. This is a notable example of a minimalist, low-cost approach to public BO disclosure: rather than a formal register portal or API, the territory makes its BO data available directly via a shared cloud storage link.

St Helena is a small jurisdiction (population ~4,500) with a correspondingly small number of registered companies, making a document-store approach more feasible than it would be for larger territories. It nonetheless represents a pragmatic implementation of the principle of public access to BO information, and demonstrates that public disclosure does not necessarily require bespoke technical infrastructure.

---

## When you need more detail

- **BODS schema**: https://standard.openownership.org/en/main/standard/reference.html
- **BODS examples**: https://standard.openownership.org/en/main/examples/
- **BODS Primer / data model / governance**: https://standard.openownership.org/en/main/primer/index.html and https://standard.openownership.org/en/main/about/governance.html — note default and `/latest` URLs now resolve to `/en/main`, not `0.4.0`
- **Visualisation spec**: https://github.com/openownership/visualisation-tool/blob/main/docs/spec.md
- **All OpenOwnership repos**: https://github.com/orgs/openownership/repositories
- **Regulatory detail**: read `references/regulatory-context.md`
- **Country register APIs**: read `references/international-registers.md`
- **Corporate data sources**: fetch live docs from Sayari, OpenCorporates, BrightQuery, InfobelPro URLs above
- **GLEIF pipeline code**: https://github.com/openownership/bods-gleif-pipeline
- **FtM/OpenSanctions conversion**: https://github.com/opensanctions/graph
- **BODS RDF/SPARQL**: https://vocab.openownership.org/ and world.hey.com/cos posts above
- **Procurement + BO**: OCDS guidance, ChileCompra case study, bodsriskdetection repo
- **Extractives + BO**: EITI 2023 Standard, SOE database, BODS mapping notebook
- **Public registers**: see "Public Beneficial Ownership Registers" table above
- **BO declaration forms**: OO guide for regulators, OO example forms, EITI model form, Ghana BO3/BO4, Namibia BIPA, UK PSC01
- **BODS open issues**: https://github.com/openownership/data-standard/issues — feature tracker at https://github.com/orgs/openownership/projects/9/views/1
- **Energy + BO**: Global Energy Ownership Tracker, GEM reports, OpenSanctions GEOT dataset
- **Fisheries + BO**: Global Fishing Watch, FiTI 2.0, OO Charting New Waters, C4ADS, Pew
- **EU BORIS**: e-Justice portal, Regulation 2021/369, Stephen's Medium article on BORIS challenges
- **Canada BO**: Corporations Canada federal register, BOP2P MRAS programme, CBCA amendments
- **BODS case studies**: https://www.beneficialownership.co.uk/case-studies — Latvia, Armenia, Botswana, Nigeria, Indonesia, Slovakia, Canada, EITI SOE, GEOT, Structuriser, Foster Moore Verne, NRD BOREG
- **ICIJ + Offshore Leaks**: https://www.icij.org/investigations/ — Panama Papers, Pandora Papers, FinCEN Files; Offshore Leaks database https://offshoreleaks.icij.org/
- **Key BO reports**: World Bank Puppet Masters, Signatures for Sale; Transparency International (MENA, Chasing Grand Corruption, Legitimate Interest, Real Estate Opacity 2025); TI-UK (Offshore Secrecy, Trust Registration, Unlocking Ownership, OT/CD legitimate interest series)
- **GODIN**: https://godin.gleif.org/ — Transparency Fabric, member datasets (GLEIF, OO, GEM, OpenSanctions, Media Registry, AC/DC, Open Data Services, Data Research Center), GitHub repos
- **Private sector/register UBO APIs**: Kyckr (CorporationUBO/IndividualUBO/OtherUBO schemas + bods-kyckr mapping), Kausate (extractUBOs), Netherlands KvK (Dataservice XML, IPD codes, access tiers), Sweden Bolagsverket, Signicat (Mint UBO lookup), UK Companies House PSC API (natures_of_control codelist)
- **BO data verification**: OO verification principle + checklist + publication; FATF R24 section 7 (legal persons) + R25 section 4 (legal arrangements); OECD BO toolkits; Tax Justice Network; Moody's KYC; Latvia + Denmark country examples; BODS sourceType verified
- **FATF mutual evaluations & country reports**: https://www.fatf-gafi.org/en/publications.html (filter by country); consolidated ratings spreadsheet; IO.5 + R.24/R.25 sections in MERs; follow-up reports; grey/black lists; FSRBs (APG, CFATF, MONEYVAL, ESAAMLG, MENAFATF, GIABA, EAG, GAFILAT, GABAC) — check FSRB websites for full reports on non-FATF members
- **2026 register developments**: BVI legitimate interest (live 1 Apr 2026); Sri Lanka BO Registry Module + BO1–BO7 forms (live 30 Mar 2026); Sweden legitimate interest (from 1 Jul 2026); Norway 17th BORIS jurisdiction; Ontario BO registry by 2027; Philippines public BO for procurement; St Helena Proton Drive register
