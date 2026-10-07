# Worked Example — GDPR DPA Review (Controller Perspective)

This example shows the skill applied to a Data Processing Addendum proposed by a SaaS vendor to a customer (the user) under GDPR.

## Input

**Regulatory regime:** gdpr
**Party role:** controller (data exporter)
**Data categories:** "EU customer end-user account data: name, email, IP address, behavioral usage data within the SaaS product. No special-category data."
**International transfer context:** "Vendor is US-based; data flows from EU to US"

**Document (excerpts — truncated):**

> **DATA PROCESSING ADDENDUM**
>
> **1. Definitions.** "Personal Data" means any information relating to an identified or identifiable natural person, as defined in the GDPR. "Processing" has the meaning given in the GDPR. "Controller" means Customer; "Processor" means Vendor. "Sub-processor" means any third party engaged by Vendor to process Personal Data.
>
> **2. Scope and Purpose.** Vendor processes Personal Data on behalf of Customer to provide the Services as described in the Master Services Agreement (the "MSA"). Vendor processes Personal Data in accordance with Customer's documented instructions, which are set forth in this DPA and the MSA, and as may be reasonably necessary for Vendor's performance of the Services. Vendor may also process Personal Data for Vendor's own legitimate business purposes including service improvement, security analytics, and aggregated reporting, provided that such processing does not identify any individual.
>
> **3. Confidentiality.** Vendor's personnel authorized to process Personal Data are subject to written confidentiality obligations.
>
> **4. Security.** Vendor shall implement industry-standard security measures appropriate to the risk presented by the Processing, including those measures listed in Annex II. Vendor maintains a SOC 2 Type II report which is available to Customer on request and under NDA.
>
> **5. Sub-processors.** Vendor may engage Sub-processors to assist in performing the Services. Vendor maintains a list of current Sub-processors on its website. Vendor will notify Customer of any new Sub-processor at least 14 days in advance via email. Customer may object to a new Sub-processor for reasonable data protection reasons by notifying Vendor in writing within the 14-day notice period; if no agreement can be reached, Customer's sole remedy is to terminate the affected portion of the Services. Sub-processors are bound by data protection obligations similar to those in this DPA.
>
> **6. Data Subject Rights.** Vendor shall provide commercially reasonable assistance to Customer in responding to Data Subject requests. Vendor reserves the right to charge reasonable fees for such assistance based on Vendor's then-current rates.
>
> **7. Breach Notification.** Vendor shall notify Customer of any confirmed Personal Data Breach without unreasonable delay after Vendor becomes aware of the Breach. The notification will include the information available to Vendor at the time of notification.
>
> **8. International Transfers.** To the extent that Personal Data is transferred from the European Economic Area, the United Kingdom, or Switzerland to a country that does not provide an adequate level of data protection, the parties agree that the EU Standard Contractual Clauses are incorporated by reference into this DPA.
>
> **9. Audits.** Customer may, no more than once per year and upon at least 90 days' written notice, request copies of Vendor's then-current third-party audit reports (such as SOC 2 Type II), which will be provided under NDA. On-site or Customer-conducted audits are not permitted absent demonstrated cause and Vendor's prior written consent.
>
> **10. Return and Deletion.** Within 60 days after termination of the MSA, Vendor will, at Vendor's option, return or delete Personal Data, except for Personal Data that Vendor is required to retain by law or that is contained in routine backups, which Vendor will delete pursuant to its standard backup deletion practices.
>
> *(Annex I, Annex II, Annex III references but contents not shown in this example.)*

## Output

# DPA Checklist Review: [Vendor] Data Processing Addendum

**Regulatory regime:** GDPR
**Party role:** Controller (Data Exporter)
**Data categories:** EU customer end-user account data — name, email, IP address, behavioral usage data
**International transfer context:** EU/UK to US (non-adequacy country); vendor US-based

## Overall posture

**Non-compliant.** This DPA contains material gaps that prevent GDPR compliance from a controller perspective. Five Article 28(3) terms are partial or missing in non-compliant form, and the international-transfer mechanism is incomplete. The DPA is not signable as drafted; substantial negotiation is required, or the controller should propose its own DPA template. The most consequential gaps are: (a) processor's reservation of "own legitimate business purposes" use, which is incompatible with Article 28(3)(a); (b) breach notification with no specific timeline, making compliance with Article 33's 72-hour controller obligation impossible; and (c) audit rights restricted to report-review only, which is non-compliant with Article 28(3)(h).

## Compliance checklist

| # | Required term | Source | Status | Clause | Assessment |
|---|---|---|---|---|---|
| F1 | Subject matter and duration of processing | GDPR Art. 28(3) preamble | Partial | §2 + MSA ref | Specified by reference to MSA; Annex I exists but contents not shown |
| F2 | Nature and purpose of processing | GDPR Art. 28(3) preamble | Partial | §2 | Generic "to provide the Services" lacks specificity |
| F3 | Type of personal data and categories of data subjects | GDPR Art. 28(3) preamble | Partial | (Annex I) | Annex referenced, contents not shown — assumed adequate but verify |
| F4 | Obligations and rights of controller | GDPR Art. 28(3) preamble | Present | (Annex I) | Annex referenced; assumed adequate |
| A | Process only on documented controller instructions | GDPR Art. 28(3)(a) | **Missing** | §2 | Processor reserves "own legitimate business purposes" — incompatible with controller-instruction model |
| B | Confidentiality of personnel | GDPR Art. 28(3)(b) | Present | §3 | Brief but adequate |
| C | Security measures (Article 32) | GDPR Art. 28(3)(c), Art. 32 | Partial | §4 + Annex II | "Industry-standard" phrasing; Annex II contents not verified; SOC 2 reference helpful but incorporation by reference rather than specific commitments |
| D | Sub-processors | GDPR Art. 28(3)(d), Art. 28(2)(4) | Partial | §5 | 14-day notice insufficient; objection remedy limited to termination is non-standard |
| E | Assistance with data subject rights | GDPR Art. 28(3)(e) | Partial | §6 | "Commercially reasonable" with charge rights; no operational SLA |
| F | Assistance with security, breach notification, DPIAs, prior consultations | GDPR Art. 28(3)(f) | **Missing** | §7 | Breach notification "without unreasonable delay" with no specific hours; only "confirmed" breaches; no DPIA assistance commitment |
| G | Return or deletion at end of processing | GDPR Art. 28(3)(g) | Partial | §10 | Vendor's option, not Controller's; backup carve-out broader than law allows |
| H | Audit and information rights | GDPR Art. 28(3)(h) | **Missing** | §9 | Limited to report-review; on-site / controller-conducted audit excluded |
| — | Processor's instruction-violation duty | GDPR Art. 28(3) closing | Missing | — | Not addressed |
| INT | International transfer mechanism | GDPR Art. 44–49 | Partial | §8 | SCCs referenced but module not specified; no TIA referenced; supplementary measures not addressed |

## Detailed findings

### A. Process only on documented controller instructions — Missing

**Required by:** GDPR Article 28(3)(a).

**What's required:** The processor processes personal data only on documented instructions from the controller. Processing for the processor's own purposes is fundamentally incompatible with the Article 28 framework — an entity processing for its own purposes is acting as a controller, not a processor.

**What the document says:** §2 permits Vendor to process for "Vendor's own legitimate business purposes including service improvement, security analytics, and aggregated reporting, provided that such processing does not identify any individual."

**Why this is a gap:** The aggregation/anonymization carve-out does not save the provision. (1) Aggregation/anonymization is itself a processing activity that requires controller instruction under GDPR. (2) "Service improvement" and "security analytics" are not "anonymized" outputs; they are model training and operational analysis on personal data. (3) The GDPR's definition of personal data includes information that can be re-identified; "does not identify any individual" is weaker than the GDPR's standard.

**Recommended language:**
> "Processor shall process Personal Data only on documented instructions from Controller, including with regard to transfers of Personal Data to a third country or an international organization, unless required to do so by Union or Member State law to which Processor is subject, in which case Processor shall inform Controller of that legal requirement before processing, unless that law prohibits such information on important grounds of public interest. Processor shall not process Personal Data for Processor's own purposes."

If the parties want to permit specific processor-controlled processing (e.g., security analytics for the processor's own platform), that processing should be either (i) covered by a separate controller-controller arrangement, or (ii) limited to specific, narrow operational purposes with adequate safeguards and explicitly authorized by Controller.

### F. Assistance with security, breach notification, DPIAs, prior consultations — Missing

**Required by:** GDPR Article 28(3)(f) (incorporating Articles 32, 33, 34, 35, 36).

**What's required:** Specific assistance commitments on (i) breach notification — including providing the controller with information necessary for its 72-hour Article 33 notification to the supervisory authority and, where required, its individual notification under Article 34; (ii) DPIA assistance under Article 35; (iii) prior consultation cooperation under Article 36.

**What the document says:** §7 covers breach notification only, "without unreasonable delay," limited to "confirmed" breaches.

**Why this is a gap:**

1. **Timeline inadequacy:** Article 33 obligates Controller to notify the supervisory authority within 72 hours of becoming aware of a breach. Vendor's "without unreasonable delay" with no specific hours commitment leaves Controller unable to plan for compliance. Vendor delays of more than ~24 hours typically make timely Controller notification impossible.

2. **"Confirmed" threshold:** Article 33's notification trigger is awareness of a breach, not confirmation. By the time Vendor has "confirmed" a breach, hours or days may have passed in investigation. Industry practice is notification on suspicion or initial detection.

3. **Notification content:** §7 says "the information available to Vendor at the time" — this is vague. Controller needs specific categories of information to comply with Article 33(3) (description of breach, categories of data, approximate number of data subjects, likely consequences, mitigation measures).

4. **Missing DPIA and Article 36 assistance:** No commitment to assist with DPIAs under Article 35 or prior consultations under Article 36.

**Recommended language:**
> "Processor shall notify Controller of any Personal Data Breach (including any reasonably suspected Personal Data Breach) without undue delay and in any event within twenty-four (24) hours after becoming aware of the Breach. The notification shall include, at a minimum: (i) a description of the nature of the Personal Data Breach including, where possible, the categories and approximate number of Data Subjects concerned and the categories and approximate number of Personal Data records concerned; (ii) the likely consequences of the Personal Data Breach; (iii) the measures taken or proposed to address the Personal Data Breach; and (iv) such other information as Controller may reasonably require to comply with its obligations under Articles 33 and 34 of the GDPR.
>
> Processor shall provide reasonable assistance to Controller in connection with: (i) Data Protection Impact Assessments under Article 35 of the GDPR, including providing information necessary for risk assessment of Processor's processing; and (ii) prior consultations with supervisory authorities under Article 36."

### H. Audit and information rights — Missing

**Required by:** GDPR Article 28(3)(h).

**What's required:** Processor must allow for and contribute to audits, including inspections, conducted by the controller or another auditor mandated by the controller. While reliance on independent audit reports for routine compliance verification is industry practice, Article 28(3)(h) requires the option of controller-conducted or controller-mandated audits.

**What the document says:** §9 limits audits to receiving Vendor's third-party audit reports under NDA. On-site or Controller-conducted audits "not permitted absent demonstrated cause and Vendor's prior written consent."

**Why this is a gap:** Article 28(3)(h) is unambiguous. Reliance on third-party reports may be reasonable as a primary mechanism for routine compliance verification, but there must be a mechanism for Controller-conducted or Controller-mandated audits where circumstances warrant. The "demonstrated cause and Vendor's prior written consent" gate effectively eliminates the right.

**Recommended language:**
> "Processor shall make available to Controller all information necessary to demonstrate compliance with Processor's obligations under this DPA and Article 28 of the GDPR. Processor shall allow for and contribute to audits, including inspections, conducted by Controller or another auditor mandated by Controller, with reasonable advance notice (typically thirty (30) days), no more than once per year (except in the event of a Personal Data Breach or regulatory inquiry), at Controller's expense, and subject to reasonable confidentiality obligations.
>
> For the avoidance of doubt: Processor's provision of independent audit reports (such as SOC 2 Type II or ISO 27001) under reasonable confidentiality terms shall satisfy Controller's information rights for routine compliance verification, but does not replace Controller's right to conduct or mandate audits where circumstances warrant."

### Other Material findings (abbreviated)

**D. Sub-processors — Partial.** 14-day notice insufficient (industry standard is 30+ days). Objection remedy limited to termination is non-standard; should include dispute-resolution path and parties' attempt to find alternatives. Sub-processors bound by "similar" obligations should be "the same" obligations under Article 28(4). Recommend rewriting.

**E. Data subject rights assistance — Partial.** "Commercially reasonable" with charge rights creates uncertainty. Replace with operational SLA (response within X business days of request) and limit fees to extraordinary cases.

**G. Return/deletion — Partial.** Article 28(3)(g) gives Controller the choice between return and deletion; this DPA gives Vendor the choice. Backup carve-out is broader than necessary; should be limited to "standard backup retention with continuing confidentiality obligations and deletion at end of backup retention cycle."

**INT. International transfer mechanism — Partial.** §8 incorporates "the EU Standard Contractual Clauses" without specifying the 2021 Commission decision (the only currently valid SCCs) or the applicable module (controller-to-processor in this case). No reference to TIA or supplementary measures despite Schrems II requirements for US transfers. SCCs themselves should be attached as an annex, not just incorporated by reference.

**Recommended language for §8:**
> "To the extent that this DPA involves the transfer of Personal Data from the European Economic Area, the United Kingdom, or Switzerland to a country that has not been deemed adequate by the European Commission (or the UK / Swiss equivalent authority), the parties shall comply with the European Commission's Standard Contractual Clauses adopted by Implementing Decision (EU) 2021/914 of 4 June 2021, Module Two (Controller to Processor), which are attached as Annex III and incorporated into this DPA by reference. For UK transfers, the parties shall execute the UK International Data Transfer Addendum to the EU SCCs, attached as Annex IV. The parties have conducted a Transfer Impact Assessment as documented at Annex V; supplementary measures are described therein."

## Items requiring human judgment

- **Whether the SCC module choice (Module Two — Controller to Processor) is correct** for the parties' specific role configuration. This example assumes a standard SaaS controller-processor relationship; complex arrangements (e.g., multi-party processing, joint controllership for some data flows) may warrant a different module.
- **Whether the user's organization's TIA (Transfer Impact Assessment) supports the transfers contemplated** under current Schrems II / EDPB guidance. The skill cannot conduct a TIA.
- **Whether Annex contents (Annex I — processing details; Annex II — security measures) are adequate** when those annexes are not provided in the document text. Verify Annexes before signing.
- **Whether the underlying MSA contains additional terms that affect this DPA's compliance.** The DPA references the MSA frequently; cross-document consistency is the user's review.

## Recommended next steps

1. **Do not sign as-is.** The combination of "own legitimate business purposes" (§2), inadequate breach notification (§7), and restricted audit rights (§9) is non-compliant with GDPR Article 28.
2. **Negotiate with the redlines proposed above.** The recommended language for §2, §7, and §9 should be non-negotiable for the controller. The remainder (§5, §6, §10, §8) is negotiable but the redlines reflect industry standard practice.
3. **Verify Annex contents.** The DPA references Annex I (processing details), Annex II (security measures), and (recommended) Annexes III/IV/V for SCCs and TIA. Confirm contents before signing.
4. **Consider proposing the user's own DPA template instead.** If the user's organization has a GDPR DPA template that has been negotiated with prior counterparties, presenting that template may be faster than redlining this one. The current document has enough structural problems that a redrafting may be more efficient than incremental fixes.

---

## What this example demonstrates

- **The structured-checklist output format provides a compliance tracker.** A privacy team can take this table directly into their compliance system; each row is a discrete trackable item.
- **Severity calibration to a non-compliant document.** Three Critical findings (A, F, H), one Critical-international-transfer finding (INT), several Material findings. The detailed-findings section addresses the Critical and Material items only; the table conveys everything else.
- **Recommended language is concrete and lawyer-grade.** Not "negotiate this" but "here is the language to propose." The user can paste the suggested language directly into a redline.
- **Statutory citations on every finding.** GDPR Article 28(3)(a) etc. are cited so the user can verify the basis and present the rationale to the counterparty.
- **The checklist surfaces gaps that a prose review might miss.** Subject-matter and duration (F1) are partial because Annex contents are unverified — a prose review would either ignore this or pad with assumptions; the checklist forces an explicit "verify before signing."
- **The "Items requiring human judgment" section appropriately surfaces what the skill cannot do.** TIA assessment, SCC module choice for non-standard arrangements, Annex content verification.
- **Bottom line opens with the recommendation, not the analysis.** "Non-compliant. Five terms partial or missing. Not signable."
