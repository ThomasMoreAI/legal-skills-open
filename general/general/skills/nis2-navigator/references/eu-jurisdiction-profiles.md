# NIS2 EU Jurisdiction Profiles

High-level profiles for the major EU markets. These provide key national differences from the Directive — a full national deep-dive is still necessary for each jurisdiction. Always verify current status via web search on activation, as transposition timelines are shifting.

**Always search for the latest status** of the relevant Member State's transposition on activation. Several of these laws are still in legislative process as of early 2026.

---

## Italy

**Status:** Transposed and in force since 16 October 2024 (one of the earliest).
**National law:** Legislative Decree No. 138/2024 (Decreto Legislativo 4 settembre 2024, n. 138).
**Authority:** ACN — Agenzia per la Cybersicurezza Nazionale.

**Key differences from Directive:**
- **Extended scope via additional Annexes**: Annex III adds central, regional, and local government. Annex IV adds additional entity types: local public transport, research institutions, cultural organizations, in-house companies, publicly controlled companies
- **Annual registration**: Registration is not a one-off — entities must re-register every year between 1 January and 28 February on the ACN digital platform
- **Phased compliance timeline**: Obligations are being rolled out progressively: incident reporting fully applies from 15 January 2026 (24h/72h/1-month); basic security measures must be implemented by 31 October 2026; long-term measures defined by ACN by April 2026; full Art. 24 risk management and Art. 23 governance obligations apply within 18 months of ACN notification (approximately October 2026 for the first cohort)
- **Safeguard clause**: DPCM of February 2025 allows exemptions from group-level size thresholds if a company can prove total independence of its NIS2 systems and activities from linked companies. However, entities influencing cybersecurity decisions or managing critical systems are not eligible
- **National Framework**: ACN uses the National Framework for Cybersecurity and Data Protection (based on NIST CSF 2.0, updated 2025) as the reference for defining measures
- **Minimum penalty floors**: Unlike most Member States, Italy sets minimum fines: 1/20th of maximum for essential entities, 1/30th of maximum for important entities. Public administration fines range €25,000–€125,000
- **Registration portal**: ACN digital platform (requires Italian SPID or equivalent credentials)
- **Fines**: Aligned with Directive maximums (€10M/2% essential, €7M/1.4% important) plus the minimum floors above

**Useful resources:** ACN platform, Italian National Framework for Cybersecurity and Data Protection (FNCS)

---

## France

**Status:** NOT yet in force as of March 2026. The "Loi Résilience" was adopted by the Senate (March 2025) and passed the National Assembly special committee (September 2025), but has NOT completed parliamentary process. As of March 2026, examination by the full National Assembly is blocked by a political dispute over Article 16 bis (encryption backdoors) and is now expected to be pushed to July 2026. Entry into force likely H2 2026 at earliest, with technical decrees (décrets) to follow after that.
**National law (pending):** Loi Résilience (PRMD2412608L).
**Authority:** ANSSI — Agence nationale de la sécurité des systèmes d'information.

**Key differences from Directive:**
- **Combined transposition**: France transposes NIS2, CER Directive, and DORA interaction in a single legislative package — unique among Member States
- **20 security objectives**: The French draft defines 20 security objectives for essential entities and 15 for important entities (expanding beyond the Directive's 10 Art. 21 measures)
- **ReCyF published**: Since 17 March 2026, ANSSI publishes the Référentiel Cyber France (ReCyF) — a working document listing recommended measures to meet NIS2 security objectives. While currently non-binding, entities that apply it can rely on it in case of ANSSI audits. Includes a comparison tool mapping ReCyF against other frameworks
- **ISO 27001 ≠ automatic compliance**: ANSSI has explicitly stated that ISO 27001/27002 certification alone covers only ~2 out of 20 objectives
- **Estimated compliance costs**: ANSSI/SGDSN figures: Important entities €100–200k initial + ~10% annually; Essential entities €450–880k initial + ~10% annually
- **ANSSI as single authority**: ANSSI handles both supervision and sanctions. A Commission des sanctions can issue public warnings and binding instructions
- **MonEspaceNIS2**: ANSSI's planned online platform for self-assessment, registration, and compliance support (monespacenis2.cyber.gouv.fr)
- **Scope note**: Local authorities with populations >30,000 and all universities are classified as essential entities
- **Fines**: Aligned with Directive caps. State, local authorities and their administrative public establishments exempt from monetary fines

**Useful resources:** ANSSI ReCyF (March 2026), ANSSI MonEspaceNIS2 portal, ANSSI comparison tool for framework mapping

---

## The Netherlands

**Status:** Not yet in force as of March 2026. The Cyberbeveiligingswet (Cbw) was submitted to parliament (Tweede Kamer) on 2 July 2024. Plenary debate scheduled for March 2026. Entry into force expected Q2 2026. Commission issued reasoned opinion in May 2025 for failure to transpose.
**National law (pending):** Cyberbeveiligingswet (Cbw), replacing the existing Wbni framework.
**Authority:** NCSC (Nationaal Cyber Security Centrum) as CSIRT; sectoral supervisory authorities (RDI — Rijksinspectie Digitale Infrastructuur for digital infrastructure).

**Key differences from Directive:**
- **Extended scope**: Draft proposes including higher education institutions (universities, universities of applied science) — this is optional under NIS2 but the Netherlands is exercising it. Local and regional governments also included
- **Classification flexibility**: DNS, public digital communication providers, and trust service providers are classified as essential or important based on their size, rather than automatically essential
- **Phased enforcement possible**: The Explanatory Memorandum confirms different provisions may take effect at different times
- **Distributed supervisory model**: Multiple sector-specific authorities rather than a single national authority
- **Registration portal**: NCSC portal (mijn.ncsc.nl), requiring eHerkenning eID. Voluntary pre-registration available since October 2024
- **Existing self-assessment tool**: RDI launched its NIS2 self-assessment tool in October 2023
- **No specific standard prescribed**: The Cbw does not mandate a particular standard (unlike Belgium's CyFun or Italy's FNCS)
- **Fines**: Expected to align with Directive caps

**Useful resources:** RDI NIS2 self-assessment tool, NCSC NIS2 information hub, Cbw NIS2 Control Framework (published by NCSC)

---

## Austria

**Status:** Transposed on 23 December 2025. Enters into force on 1 October 2026. Until then, the existing NISG 2018 continues to apply.
**National law:** Netz- und Informationssystemsicherheitsgesetz 2026 (NISG 2026).
**Authority:** To be designated (expected continuation of existing NIS authority structure).

**Key differences from Directive:**
- **Delayed effectiveness**: Despite formal transposition in December 2025, the law does not become operational until 1 October 2026 — creating a ~9 month preparation period
- **Registration deadline**: Essential and important entities must register within 3 months after entry into force (i.e., by 1 January 2027)
- **~4,000 entities in scope**: Significantly smaller than Germany (29,500) or France (~15,000), but still a major expansion from the ~1,000 entities under NISG 2018
- **Political history**: The original NISG 2024 draft was rejected by the National Council in July 2024, leading to significant delay. The revised NISG 2026 reflects political compromise
- **Public entities**: Federal ministries and large municipalities subject to compliance orders but exempt from monetary fines
- **Secondary legislation pending**: Detailed implementing regulations for technical requirements, registration procedures, and reporting mechanisms still being finalized
- **Fines**: Aligned with Directive (€10M/2% essential, €7M/1.4% important)
- **DACH relevance**: Austrian entities often share group structures with German parent companies — coordinate BSIG-neu and NISG 2026 compliance in parallel

**Useful resources:** WKO (Austrian Chamber of Commerce) NIS2 checklist, Austrian CERT.at

---

## Spain

**Status:** Not yet in force as of March 2026. The Anteproyecto de Ley de Coordinación y Gobernanza de la Ciberseguridad (Draft Law on Cybersecurity Coordination and Governance) was approved by Council of Ministers on 14 January 2025. Public consultation completed February 2025. Still in parliamentary processing with urgent status granted.
**National law (pending):** Ley de Coordinación y Gobernanza de la Ciberseguridad.
**Authority:** New Centro Nacional de Ciberseguridad (CNC) to be created. CSIRTs: CCN-CERT (public sector), INCIBE-CERT (private sector), Joint Cyber Space Command (military).

**Key differences from Directive:**
- **New institution**: The draft creates a Centro Nacional de Ciberseguridad (CNC) attached to the Cabinet of the Presidency, centralizing cybersecurity coordination — a new body not existing under prior law
- **Extended scope**: Draft adds companies with significant public participation, universities and research centers, large municipalities (>20,000 inhabitants), private security companies, entities with impact on national defense, and foreign companies with permanent establishment in Spain meeting certain criteria
- **Tiered fine structure with lower ranges**: Beyond the Directive's maximum caps (€10M/2% and €7M/1.4%), Spain introduces intermediate categories: minor infringements €10,000–€100,000, serious €100,001–€500,000, very serious €500,001–€2,000,000
- **Triple CSIRT structure**: Incidents go to different CSIRTs depending on whether the entity is public sector (CCN-CERT), private sector (INCIBE-CERT), or military (Joint Cyber Space Command)
- **ENS alignment**: Spain's existing Esquema Nacional de Seguridad (ENS, National Security Framework) provides a baseline that organizations may already partially satisfy
- **Fines**: Both Directive-aligned caps AND lower intermediate tiers (see above)

**Useful resources:** INCIBE NIS2 information, CCN-CERT guidance, ENS framework (esquema nacional de seguridad)

---

## Usage Notes for the Skill

1. **Jurisdiction selection in Phase 1**: After determining jurisdiction focus, load this file only if a non-German EU jurisdiction is selected
2. **Always verify status**: These profiles reflect status as of early 2026. Several laws (Netherlands, France, Spain) are still in legislative process. Use the web search trigger to check for updates
3. **Directive baseline applies everywhere**: For jurisdictions where national law is not yet in force, the Art. 21 gap analysis and roadmap remain fully valid — entities should prepare against the Directive requirements regardless of national transposition delays
4. **Flag the gap**: If the selected jurisdiction hasn't transposed yet, explicitly note this and advise the entity to (a) prepare against Directive requirements now, (b) monitor national legislative developments, and (c) consider voluntary early compliance
5. **Cross-border groups**: For entities operating across multiple jurisdictions, flag that each national transposition may differ and recommend jurisdiction-specific legal counsel
