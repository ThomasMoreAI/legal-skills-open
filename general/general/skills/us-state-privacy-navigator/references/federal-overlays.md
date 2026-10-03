# Federal Sectoral Overlays — Where Federal Law Modifies the State Privacy Analysis

## Purpose and scope

This file is the bridge between the state privacy patchwork and the federal sectoral regimes that preempt, carve out, or otherwise modify state obligations. It is **not** a standalone HIPAA / GLBA / COPPA / FERPA / FCRA navigator. The depth of those regimes warrants dedicated skills; this file documents only the *intersections* with US state comprehensive privacy laws.

**When to use this file.** Any time the entity-and-data-type filter (operating principle 4) surfaces a federal sectoral regime, before assigning state privacy duties. The entity-level vs. data-level distinction below is the single most important diagnostic.

**Citation as you go (operating principle 6).** Every federal preemption / carve-out claim must trace to either the state statute's exemption clause or the federal regime's preemption provision. Do not assert preemption without a citation.

## The entity-level vs. data-level distinction (most important diagnostic)

State privacy law exemptions for federal-regulated regimes come in two structural flavors. **Misreading which flavor a state uses is the single most common error in multi-state compliance work.**

**Entity-level exemption.** The entity is exempt from the state law in its entirety because it is regulated by the federal regime. *Example*: VA, CT, IA, IN, TN, NJ exempt **financial institutions subject to GLBA** as entities — meaning a bank doesn't comply with VCDPA at all, even for non-financial customer data the bank holds (e.g., a marketing list of prospects).

**Data-level exemption.** Only the federally-regulated *data* is carved out; the entity is otherwise subject to the state law for non-federally-regulated data it holds. *Example*: CA, CO, OR, DE exempt only the data subject to GLBA (NPI), not the institution. A bank's GLBA-covered customer financial information is exempt; the bank's marketing prospect list is not.

This distinction matters operationally for every federal regime. The matrix below identifies which states use which approach for each regime. Get this wrong and the gap analysis is wrong.

## HIPAA × state privacy law

**Federal regime in one paragraph.** HIPAA Privacy Rule (45 C.F.R. Part 164, Subpart E), Security Rule (Subpart C), and Breach Notification Rule (Subpart D) govern Protected Health Information (PHI) held by Covered Entities (health plans, health care clearinghouses, most health care providers) and their Business Associates. Authority: 42 U.S.C. § 1320d et seq.; HHS Office for Civil Rights enforces. PHI = individually identifiable health information held by a CE/BA in any form.

### Preemption framework

HIPAA establishes a federal **floor**, not a ceiling. State laws that are **more stringent** are not preempted (45 C.F.R. § 160.203). "More stringent" is defined at § 160.202 and broadly includes laws that grant individuals greater rights or impose tighter restrictions on the entity. CCPA's right to know and right to deletion are generally treated as more stringent than HIPAA's right of access, *but only as applied to non-PHI data the entity holds*; for PHI itself, HIPAA provides the operative framework.

### State exemption matrix (HIPAA)

| State | Exemption type | Citation |
|---|---|---|
| CA (CCPA/CPRA) | **Data-level** for PHI; **also entity-level partial** for "providers of health care" governed by CMIA or HIPAA when collecting/maintaining PHI in same manner as PHI | Cal. Civ. Code § 1798.146(a)(1), (a)(2) |
| VA (VCDPA) | **Entity-level** — covered entities and business associates fully exempt | Va. Code § 59.1-576(B)(8), (B)(9) |
| CO (CPA) | **Data-level** for PHI; entity exempt for activities subject to HIPAA | Colo. Rev. Stat. § 6-1-1304(2)(j), (2)(k) |
| CT (CTDPA) | **Entity-level** — covered entities and business associates fully exempt | Conn. Gen. Stat. § 42-516(a)(8), (a)(9) |
| UT (UCPA) | **Both** — entity-level for covered entities/BAs and data-level for PHI | Utah Code § 13-61-102(1)(g)(vi), (1)(g)(vii) |
| TX (TDPSA) | **Entity-level** for covered entities/BAs | Tex. Bus. & Com. Code § 541.002(a)(4) |
| OR (OCPA) | **Data-level** for PHI; PHI carve-out only | Or. Rev. Stat. § 646A.572(2)(j) |
| MT (MCDPA) | **Entity-level** for covered entities/BAs | Mont. Code § 30-14-2803(2)(g), (2)(h) |
| IA (ICDPA) | **Entity-level** for covered entities/BAs | Iowa Code § 715D.3(1)(g), (1)(h) |
| IN (INCDPA) | **Entity-level** for covered entities/BAs | Ind. Code § 24-15-1-1(b)(7), (b)(8) |
| TN (TIPA) | **Entity-level** for covered entities/BAs | Tenn. Code § 47-18-3203(a)(8), (a)(9) |
| DE (DPDPA) | **Data-level** — PHI carve-out only | Del. Code tit. 6 § 12D-103(b)(8) |
| NJ (NJDPA) | **Entity-level** for covered entities; **data-level** for PHI as separate carve-out | N.J. Stat. § 56:8-166.5(b)(7), (b)(11) |
| NH (NHDPA) | **Entity-level** for covered entities/BAs | N.H. Rev. Stat. § 507-H:2(II)(g), (II)(h) |
| NE (NDPA) | **Entity-level** for covered entities/BAs | Neb. Rev. Stat. § 87-1102(2)(g), (2)(h) |
| KY (KCDPA) | **Entity-level** for covered entities/BAs | Ky. Rev. Stat. § 367.3611(2)(g), (2)(h) |
| MD (MODPA) | **Data-level** — PHI carve-out only; **entity not exempt** | Md. Code, Com. Law § 14-4603(b)(8). MD's narrowness here is intentional and material. |
| MN (MCDPA-MN) | **Entity-level** for covered entities/BAs | Minn. Stat. § 325O.04(b)(7), (b)(8) |
| RI (RIDTPPA) | **Data-level** — PHI carve-out only | R.I. Gen. Laws § 6-48.1-3(b)(8) |
| FL (FDBR) | **Entity-level** for covered entities/BAs | Fl. Stat. § 501.704(2)(g), (2)(h) |

### Operational implications

- A HIPAA covered entity in an **entity-level** state (VA, CT, TX, MT, IA, IN, TN, NH, NE, KY, MN, FL — most states) does not need a CCPA-style consumer rights program for any of its data while operating in that state. The state law simply does not apply to the entity. *But* if the entity also operates in CA, CO, OR, DE, MD, RI (data-level states), it must run state-law compliance for non-PHI data: marketing lists, wellness programs not covered by HIPAA, employee data (in CA only), B2B contacts (in CA only), prospect lists, patient family contacts that are not the patient's PHI.
- A HIPAA business associate is treated identically to a covered entity for exemption purposes in nearly all states. Verify this when the entity's role is mixed (e.g., a SaaS vendor that is a BA for some customers and a controller for others — the entity's status under each state depends on whether *the specific data flow* is in the BA capacity).
- **Maryland's narrow data-level approach is the binding constraint** when MD is in scope and the entity is HIPAA-regulated: MD treats the entity as in scope for everything except actual PHI. Combined with MODPA's flat ban on sensitive-data sale and minor-data targeted advertising, MD compliance becomes the multi-state ceiling.
- **The HIPAA-state interplay does not preempt state breach notification.** Almost every state's breach notification statute applies to HIPAA-regulated entities; the entity must comply with both HIPAA Breach Notification Rule and state breach notification, with whichever is more stringent controlling. See `references/enforcement.md` for breach notification overlay.
- **AHA v. Becerra (N.D. Tex. 2024)** vacated OCR's pixel-tracking guidance applying HIPAA to public-facing webpages absent an authentication or PHI input, narrowing — but not eliminating — pixel-related HIPAA exposure. Healthcare-pixel class actions under state CIPA / wiretap laws (Kaiser $46M, Frasco v. Flo Health verdict) and CMIA continue at full force regardless. See `references/enforcement_actions.json` (`hipaa-aha-v-becerra-2024`, `ca-cipa-kaiser-2025`, `ca-cipa-flo-meta-jury-2025`).

## GLBA × state privacy law

**Federal regime in one paragraph.** Gramm-Leach-Bliley Act, 15 U.S.C. §§ 6801–6809, governs Nonpublic Personal Information (NPI) held by Financial Institutions. Two operative rules: Privacy Rule (CFPB Reg P, 12 C.F.R. Part 1016) requires privacy notices, opt-out for sharing with non-affiliated third parties, and content/timing requirements; Safeguards Rule (FTC, 16 C.F.R. Part 314, expanded in December 2021 with effective date June 9, 2023) requires written information security program, MFA, encryption, incident response. NYDFS Part 500 imposes parallel-and-tighter requirements for NY-regulated financial institutions.

### Preemption framework

GLBA does not preempt **more protective** state laws (15 U.S.C. § 6807). This is the same floor structure as HIPAA. State laws that grant consumers more rights are not preempted; CCPA's right to know and right to deletion as applied to non-NPI data are generally not preempted.

### State exemption matrix (GLBA)

| State | Exemption type |
|---|---|
| CA (CCPA/CPRA) | **Data-level** for NPI subject to GLBA; entity not exempt. Cal. Civ. Code § 1798.145(e). |
| VA (VCDPA) | **Entity-level** for financial institutions subject to GLBA Title V. Va. Code § 59.1-576(B)(7). |
| CO (CPA) | **Data-level** for NPI; entity not exempt for non-NPI activities. Colo. Rev. Stat. § 6-1-1304(2)(q). |
| CT (CTDPA) | **Entity-level** for financial institutions subject to GLBA. Conn. Gen. Stat. § 42-516(a)(7). |
| UT (UCPA) | **Entity-level**. Utah Code § 13-61-102(1)(g)(iv). |
| TX (TDPSA) | **Entity-level**. Tex. Bus. & Com. Code § 541.002(a)(3). |
| OR (OCPA) | **Data-level** narrowly — insurance/GLBA-aligned data only; entity activities outside GLBA scope subject to OCPA. Or. Rev. Stat. § 646A.572(2)(g). |
| MT (MCDPA) | **Entity-level** for GLBA-covered financial institutions. Mont. Code § 30-14-2803(2)(f). |
| IA (ICDPA) | **Entity-level**. Iowa Code § 715D.3(1)(f). |
| IN (INCDPA) | **Entity-level**. Ind. Code § 24-15-1-1(b)(6). |
| TN (TIPA) | **Entity-level**. Tenn. Code § 47-18-3203(a)(7). |
| DE (DPDPA) | **Data-level** — NPI only. Del. Code tit. 6 § 12D-103(b)(7). |
| NJ (NJDPA) | **Entity-level** for financial institutions. N.J. Stat. § 56:8-166.5(b)(6). |
| NH (NHDPA) | **Entity-level**. N.H. Rev. Stat. § 507-H:2(II)(f). |
| NE (NDPA) | **Entity-level**. Neb. Rev. Stat. § 87-1102(2)(f). |
| KY (KCDPA) | **Entity-level**. Ky. Rev. Stat. § 367.3611(2)(f). |
| MD (MODPA) | **Data-level** — NPI only; entity not exempt. Md. Code, Com. Law § 14-4603(b)(7). |
| MN (MCDPA-MN) | **Entity-level**. Minn. Stat. § 325O.04(b)(6). |
| RI (RIDTPPA) | **Data-level** — NPI only. R.I. Gen. Laws § 6-48.1-3(b)(7). |
| FL (FDBR) | **Entity-level**. Fl. Stat. § 501.704(2)(f). |

### Operational implications

- The entity-level / data-level split is **identical in structure to HIPAA** but with a different list of states. CA, CO, OR (narrowly), DE, MD, RI run data-level; the rest run entity-level.
- **NYDFS Part 500** is not a state privacy law but applies in parallel to GLBA-regulated financial institutions licensed in NY. It imposes its own breach notification (72-hour), CISO requirement, third-party risk management, and MFA requirements. Recent enforcement: NYDFS PayPal $2M (2024), GEICO/Travelers $11.3M joint OAG/DFS action (2024). See `references/enforcement_actions.json` (`ny-dfs-cybersecurity-pwc-2024`, `ny-geico-travelers-2024`).
- **CFPB enforcement** of GLBA (and broader UDAAP authority) overlaps with state UDAP and state privacy enforcement. Block/Cash App ($175M consent order Jan 2025) and Equifax ($15M FCRA Jan 2025) are recent anchors. See corpus entries `cfpb-block-cashapp-2025`, `cfpb-equifax-2025`.
- **Maryland's data-level approach + MODPA flat bans is, again, the binding constraint** for GLBA-regulated entities in MD. Combined with MD breach notification, it produces the strictest multi-state regime for financial institutions.
- **B2B and HR data**: GLBA does not cover B2B or HR data of the financial institution. CA's CCPA/CPRA covers both; in CA, a GLBA-regulated bank still owes CCPA duties to its employees and B2B contacts even though customer NPI is data-level exempt.

## COPPA × state privacy law

**Federal regime in one paragraph.** Children's Online Privacy Protection Act, 15 U.S.C. §§ 6501–6506; FTC Rule at 16 C.F.R. Part 312. Applies to operators of websites or online services directed to children under 13, OR operators with actual knowledge of collecting personal information from children under 13. Requires notice, verifiable parental consent (VPC) before collection, parental review/deletion rights, internal-use limitations, reasonable security, and data minimization.

### Preemption framework

COPPA contains an **express preemption clause** (15 U.S.C. § 6502(d)) that preempts state laws "inconsistent with the treatment of those activities or actions" under COPPA. Courts have generally read this narrowly — state laws that *augment* COPPA's protections are not preempted unless they directly conflict. CA AADC, MD AADC, CT/CO teen provisions, and MODPA's flat ban on minor targeted advertising have all been treated as compatible with COPPA's federal floor. See *Jones v. Google* (N.D. Cal. 2023) and the *NetChoice* AADC litigation for the active boundary disputes.

### State exemption matrix (COPPA)

Most state comprehensive privacy laws do **not** carve out COPPA entirely — instead they **incorporate** COPPA's VPC requirement when processing data of a "known child" (under 13) and add their own teen overlay (13-17). The carve-outs that do exist are narrow:

| State | Treatment |
|---|---|
| CA (CCPA/CPRA) | **No COPPA exemption** for the entity. CCPA covers minors. Sale/share of PI of consumers under 16 requires opt-in; under 13 requires VPC consistent with COPPA. Cal. Civ. Code § 1798.120(c). CCPA's minor opt-in framework operates *in addition to* COPPA. |
| VA (VCDPA) | **Data-level** for data subject to COPPA when collected/processed in compliance with COPPA. Va. Code § 59.1-576(C)(8). |
| CO (CPA) | **Data-level** for data collected/maintained/used pursuant to COPPA. Colo. Rev. Stat. § 6-1-1304(2)(o). |
| CT (CTDPA) | **Data-level** for COPPA-compliant collection. Conn. Gen. Stat. § 42-516(b)(8). Also: separate teen-protection regime for 13-17. |
| Most other states (UT, TX, OR, MT, IA, IN, TN, DE, NJ, NH, NE, KY, MN, RI, FL) | **Data-level** carve-outs for COPPA-compliant collection in similar form. |
| MD (MODPA) | **Data-level** carve-out for COPPA-compliant collection, BUT **flat ban on targeted advertising to known minors under 18** that is *not* preempted. Md. Code, Com. Law § 14-4607. |

### Operational implications

- COPPA does **not** make a service exempt from state law for older users. A child-directed service must run COPPA for under-13s and state privacy law for adult users (and 13-17 teens, where state law adds a layer).
- **The FTC's 2025 COPPA Rule amendments** (effective dates rolling through 2025-2026) added: separate VPC for third-party disclosure, biometric and government-issued identifier as "personal information," default data retention limits, school authorization for ed-tech. This expansion narrows the COPPA-state-law gap; some state requirements that were "more stringent" in 2023 are now incorporated federally.
- **State teen overlays (13-17)** are the active growth area. CA AB 1949 (2024), CT teen provisions (CTDPA amendments), CO teen provisions (CPA SB24-041), MD MODPA flat bans, NY SAFE for Kids, FL HB 3, TX SCOPE Act. These are *not* COPPA — they are state-specific minor protections that overlay state privacy law. See `references/kids-and-teens.md` for the full layered analysis.
- **Recent enforcement anchors**: Disney COPPA $10M (Dec 2025, YouTube MFK mislabeling); NGL Labs $5M (July 2024, joint FTC + LA DA, first permanent under-18 ban); Tilting Point $500k (CA AG, June 2024). See corpus entries `ftc-disney-coppa-2025`, `ftc-ngl-labs-2024`, `ca-tilting-point-2024`.

## FERPA × state privacy law

**Federal regime in one paragraph.** Family Educational Rights and Privacy Act, 20 U.S.C. § 1232g; 34 C.F.R. Part 99. Governs education records held by educational agencies and institutions receiving Department of Education funding. Grants parents (and students 18+) right to inspect, request amendment, and consent to disclosure, with statutory exceptions. Department of Education enforces; no private right of action (*Gonzaga Univ. v. Doe*, 536 U.S. 273 (2002)).

### Preemption framework

FERPA does not contain an express preemption clause comparable to COPPA's. State laws that grant *greater* protection are generally not preempted. State student-privacy laws (SOPIPA in CA, similar laws in 30+ states, the Student Online Personal Information Protection Act framework) operate alongside FERPA and apply to ed-tech vendors that FERPA itself does not directly reach.

### State exemption matrix (FERPA)

| State | Treatment |
|---|---|
| CA (CCPA/CPRA) | **No explicit FERPA exemption**. CCPA may apply to educational institutions for non-FERPA data; SOPIPA (Cal. Bus. & Prof. Code §§ 22584-22585) imposes parallel obligations on ed-tech operators. |
| Most other states (CO, CT, UT, OR, MT, IA, IN, TN, DE, NJ, NH, NE, KY, MN, RI, FL) | **Both data-level (FERPA records)** and **entity-level (educational institutions, postsecondary institutions)** exemptions, varying by state. Higher education institutions are commonly exempt at entity level. |
| TX (TDPSA) | Higher ed entity-level exempt; FERPA records data-level exempt. Tex. Bus. & Com. Code § 541.002(a)(2), (a)(11). |
| MD (MODPA) | Data-level only — FERPA records carved out; entity not exempt. |

### Operational implications

- The split between FERPA-covered education records and the broader data an ed-tech vendor holds is operationally critical. FERPA covers records held by the institution; once the institution shares data with an ed-tech vendor under the school official exception (34 C.F.R. § 99.31(a)(1)), the vendor's broader data holdings (analytics, optimization data, marketing email lists) may not be FERPA-protected even if the underlying school data is.
- **State student-privacy laws** (SOPIPA-style) reach ed-tech vendors directly without going through the institution, closing the gap. The Department of Education's January 2025 *Dear Colleague* guidance on AI in educational settings reinforces the FERPA + state student-privacy + COPPA + state minor-privacy stack for ed-tech.
- **Higher-ed entity-level exemptions** in most states mean a university running a marketing campaign to alumni or processing donor data is not subject to the state privacy law for *any* of that activity — even though the data is not FERPA records. CA's narrower carve-out is the exception.

## FCRA × state privacy law

**Federal regime in one paragraph.** Fair Credit Reporting Act, 15 U.S.C. §§ 1681–1681x. Governs Consumer Reporting Agencies (CRAs) that furnish "consumer reports," and the entities that furnish data to CRAs and use consumer reports. FTC and CFPB share enforcement; private right of action is available. State analogs ("mini-FCRAs") in CA (ICRAA, CCRAA), MA, NY, VT, others impose additional obligations.

### Preemption framework

FCRA contains a **partial preemption clause** (15 U.S.C. § 1681t) that is one of the most-litigated preemption provisions in US privacy law. § 1681t(b)(1)(F) preempts state laws relating to subject matter regulated under § 1681s-2 (furnisher obligations) — but the scope is contested. *Ross v. FDIC* (4th Cir. 2010), *Galper v. JP Morgan* (2d Cir. 2015), and the Ninth Circuit's evolving doctrine produce a circuit split. Conservatively, treat FCRA as preempting state laws that directly regulate the same furnisher conduct, but not state laws that regulate broader data practices that happen to involve CRAs.

### State exemption matrix (FCRA)

Standard pattern across states: **data-level** exemption for data subject to FCRA when collected, sold, used, or maintained in compliance with FCRA. The state laws do not typically exempt the CRA as an entity. CRAs are subject to state privacy laws for data outside the FCRA scope.

| State | Treatment |
|---|---|
| CA (CCPA/CPRA) | Data-level for FCRA-covered data. Cal. Civ. Code § 1798.145(d). California ICRAA/CCRAA impose parallel obligations. |
| Most other states | Data-level for FCRA data; CRA entity not exempt. |

### Operational implications

- **A CRA running a non-FCRA data product** (e.g., Equifax's marketing data, or a data broker subsidiary) is fully subject to state privacy laws for that product. The FCRA exemption is data-level, not entity-level.
- **CFPB Equifax $15M (Jan 2025)** is the recent anchor — CFPB FCRA dispute-handling enforcement, demonstrating that even within FCRA's scope, federal enforcement is active and produces non-preempted state UDAP claims. See corpus entry `cfpb-equifax-2025`.
- **State data-broker registration laws** (CA, OR, TX, VT) reach CRAs that operate data-broker products outside FCRA scope. CA's CPPA data-broker sweep (2025-2026) included CRA-affiliated entities. See corpus entry `ca-cppa-data-broker-sweep-2025-2026`.

## DPPA × state privacy law (briefly)

**Driver's Privacy Protection Act**, 18 U.S.C. §§ 2721–2725, governs disclosure of personal information from motor vehicle records by state DMVs and downstream recipients. Most state comprehensive privacy laws contain a data-level carve-out for DPPA-covered records. Operationally, this affects insurance, automotive, telematics, and connected-vehicle entities. The **Texas Allstate-Arity** lawsuit (January 2025) involved telematics data that was *not* DPPA-covered (it was app-collected SDK data, not DMV records), illustrating the carve-out's narrow scope.

## Synthesis: what this reference is for

When the user's intake reveals the entity is HIPAA-covered, GLBA-covered, COPPA-subject, FERPA-related, or FCRA-touching:

1. **Run the entity-level / data-level diagnostic** for each applicable state. This is the threshold question; getting it wrong corrupts the rest of the analysis.
2. **Identify the data the federal regime does not reach** — marketing data, prospect lists, employee data (CA), B2B contacts (CA), wellness programs not covered by HIPAA, alumni/donor data for universities, non-FCRA analytics for CRAs. State privacy law applies to *that* data even where the entity-level exemption is broad.
3. **Layer the state-specific overlays** — CMIA (CA health), SHIELD Act (NY), MHMDA (WA consumer health), state mini-FCRAs (CA ICRAA/CCRAA, MA, NY, VT), state student-privacy laws (SOPIPA-style in 30+ states), state breach-notification laws (all 50 states + DC).
4. **Surface the binding constraint** through `scripts/conflict_resolver.py` once the applicable states are identified. Maryland's data-level approach to HIPAA/GLBA combined with MODPA flat bans on sensitive-data sale and minor targeted advertising routinely produces the multi-state ceiling for federally-regulated entities operating in MD.
5. **Match enforcement precedent** through `scripts/precedent_match.py` for any HIPAA-OCR, CFPB, FTC sectoral, or multistate AG matters in the corpus that align with the entity's gap pattern.

## What this reference is **not** for

This file does not analyze:

- HIPAA Privacy Rule, Security Rule, or Breach Notification Rule compliance standalone. Use a HIPAA-specific resource.
- GLBA Privacy Rule (Reg P) or Safeguards Rule compliance standalone. Use a GLBA-specific resource.
- COPPA Rule compliance standalone (notice content, VPC mechanics, internal-use exception scope). Use a COPPA-specific resource. The 2025 amendments materially changed several mechanics; verify current.
- FERPA disclosure exception analysis or directory-information determinations. Use a FERPA-specific resource.
- FCRA furnisher obligations, dispute-resolution mechanics, permissible-purpose analysis, or adverse-action notice content. Use an FCRA-specific resource.
- NYDFS Part 500, FTC Safeguards Rule, or HHS Reproductive Health Privacy amendments standalone. Each warrants its own treatment.

If the user's question is purely within one of those federal regimes — without a state privacy overlay — this skill is the wrong tool. Recommend a sectoral resource and stop.
