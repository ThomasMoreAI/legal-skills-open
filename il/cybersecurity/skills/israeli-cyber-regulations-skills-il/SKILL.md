---
name: israeli-cyber-regulations-skills-il
title: Israeli Cyber Regulations
description: Not legal advice and not a compliance opinion. Israeli cybersecurity regulatory framework guidance covering INCD (Ma'arach HaSyber) national directives, Bank of Israel Directive 364, the consolidated IT, information security and cyber framework that took effect 18/05/2026 and repealed Directives 357, 361 and 363, plus Directive 366 incident reporting and Directive 362 cloud, ISA disclosure for TASE-listed companies under regulation 36 and staff position 105-33, and sector rules for fintech and healthtech. Use when user asks about "cyber regulation Israel", "horaot Bank Israel 361", "INCD compliance", "Ma'arach HaSyber", "ISA cyber requirements", "sector cyber rules Israel", or "רגולציית סייבר". Covers regulatory mapping, gap analysis, compliance checklists, and audit preparation for Israeli cyber frameworks. Do NOT use for privacy law compliance (use israeli-privacy-compliance instead).
author: skills-il
author_url: https://github.com/skills-il/security-compliance/tree/master/israeli-cyber-regulations
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: il
practice: cybersecurity
language: en
sources:
- title: Domain Checklist
  path: references/domain-checklist.md
- title: Incd Guidelines
  path: references/incd-guidelines.md
- title: Sector Rules
  path: references/sector-rules.md
---

# Israeli Cyber Regulations

## Legal notice

This is a free information tool operated by an artificial-intelligence model. It maps which Israeli cybersecurity regulatory instruments apply to an organisation, summarises their published requirements, and helps prepare gap analyses and audit evidence lists. All of its output is produced automatically, without the involvement, review or approval of a lawyer, a compliance officer, or any licensed professional.

The output is not legal advice and not a legal opinion, and any text it drafts is not a document prepared by a lawyer. It is a summary of published regulatory material. The tool does not read the organisation's contracts, licences or supervisory correspondence, does not know its licence conditions, its designation status, or which instruments actually bind it. Regulatory instruments are amended, consolidated and repealed frequently, sometimes with effect from a date later than this tool's information, and an artificial-intelligence model may err, omit an instrument, or cite one no longer in force.

Do not rely on this output to determine a reporting obligation, a filing deadline, or whether an incident is disclosable. Verify every directive, regulation and statute against the regulator's own current publication, and before any filing, disclosure, board representation or approach to a regulator, consult a lawyer or a qualified compliance professional. This tool is not a substitute for advice that takes account of the particular data and needs of each person. Any use of the output is the sole responsibility of the user.

**Scope note.** For privacy-law compliance (data protection, consent, PPA registration) use the `israeli-privacy-compliance` skill; only the cyber-facing breach-notification duty is carried here.

## Instructions

### Step 1: Identify Applicable Regulatory Framework
Determine which Israeli cybersecurity regulations apply to the user's organization.

| Framework | Applies To | Regulator | Key Focus |
|-----------|-----------|-----------|-----------|
| INCD National Directives | All organizations, mandatory for critical infrastructure | Ma'arach HaSyber (INCD) | Risk management, incident reporting, baseline controls |
| **BOI Directive 364 (IN FORCE since 18/05/2026)** | Banking corporations, credit-card companies, and a payment-service provider of systemic importance. **NOT insurers** | Bank of Israel (BOI) | "Management of IT, Information Security and Cyber Protection Risks". Published 18/11/2024 (circular 2799). **The operative framework. On 18/05/2026 it repealed Directives 357, 361 and 363.** Map all control programs to 364 |
| BOI Directives 357 / 361 / 363 | -- | Bank of Israel (BOI) | **REPEALED on 18/05/2026** by 364. Historical only. 361 was Cyber Defense Management, 357 was IT Management, 363 was supply-chain cyber risk. Do NOT write a control program against these |
| BOI Directive 366 (updated 17/06/2026) | Banks | Bank of Israel (BOI) | "Reporting of technological-failure, information-security and cyber-attack events", circular 2848, update 4. The incident-reporting hook. Update 4 added a duty to report a serious security event as defined in section 31 of the Financial Information Service Law, 5782-2021, with a parallel change to reporting directive 880 |
| BOI Directive 362 (updated 17/06/2026) | Banks (cloud) | Bank of Israel (BOI) | "Cloud Computing", circular 2849, version 5. Now written as complementing **364**. Internal board/management approval by materiality, plus annual reporting to Banking Supervision under reporting directive 881. See the Gotcha: this is **not** a prior-approval regime |
| BOI Directive 368 (01/09/2025) | Banks | Bank of Israel (BOI) | "Open Banking in Israel", circular 2826. Open Banking is now a directive, no longer only a roadmap |
| **Institutional Bodies Circular 2016-9-14** | Insurers, pension and provident bodies (גופים מוסדיים) | **Capital Market, Insurance and Savings Authority**, not BOI | "Cyber risk management in institutional bodies", 31/08/2016. Issued under the Supervision of Financial Services (Insurance) Law 5741-1981 and the Provident Funds Law 5765-2005. **This, not Directive 364, is the instrument for an insurer** |
| **Payment Services and Payment Initiation Law, 5783-2023** | Non-bank payment-service and payment-initiation licensees | **Israel Securities Authority**, which the Law defines as "הרשות" | Licensing conditions include information security, cyber protection, risk management and business continuity "according to rules the Authority set in regulator instructions" (הוראות מאסדר) |
| ISA Cyber Requirements | TASE-listed companies | Israel Securities Authority (ISA/Rashut) | Disclosure, board oversight, cyber risk reporting |
| MOH Health Cyber | Hospitals, HMOs, health-tech | Ministry of Health | Patient data protection, medical device security |
| CDPA Telecom Rules | Telecom providers | Ministry of Communications | Network security, lawful intercept, data retention |

**Decision logic:**
```
Is the organization a designated body under the Regulation of Security in
Public Bodies Law, 5758-1998?
  YES -> its cyber duties and its reporting line run through its statutory
         GUIDING BODY (gorem manche), not through the voluntary INCD baseline.
         An organisation does not work this out by self-assessment: designation
         happens through the Law's schedules and the organisation is told.
         If the user does not know, that itself is the answer to establish first,
         and INCD is not the body that designates them on its own
Is the organization a banking corporation or a credit-card company?
  YES -> BOI Directive 364 applies (357/361/363 are repealed), plus 366 reporting,
         362 cloud, 368 open banking (+ INCD if designated)
Is the organization an insurer, pension fund or provident fund (guf mosdi)?
  YES -> NOT the BOI directives. Capital Market, Insurance and Savings Authority,
         Institutional Bodies Circular 2016-9-14 on cyber risk management.
         Directive 364 does not mention insurance at all
Does the organization provide payment services?
  YES -> split by systemic importance. A payment-service provider of SYSTEMIC
         IMPORTANCE (section 36T of the Banking (Licensing) Law) is inside
         Directive 364 by its own applicability clause. Every other non-bank
         payment or initiation licensee is licensed and supervised by the
         ISRAEL SECURITIES AUTHORITY under the Payment Services and Payment
         Initiation Law, 5783-2023, whose licensing conditions cover information
         security and cyber via the Authority's regulator instructions
Is the organization a digital-service or hosting provider?
  YES -> the Severe Cyber Attacks (Digital Services and Hosting) Temporary Order
         Law, 5784-2023 imposes a STATUTORY reporting duty. This is the one
         binding civilian-sector reporting statute; see Step 2
Is the organization listed on TASE?
  YES -> ISA cyber disclosure requirements apply
Is the organization in healthcare?
  YES -> MOH health cyber directives apply
ALL organizations -> INCD voluntary baseline recommendations apply
```

### Step 2: INCD (Ma'arach HaSyber) Framework Assessment
The Israel National Cyber Directorate (INCD) sets national cybersecurity policy.

**INCD Five-Pillar Framework** (Identify / Protect / Detect / Respond / Recover; זיהוי, הגנה, גילוי, תגובה, שחזור). The per-pillar requirements are in `references/incd-guidelines.md`.

**INCD incident reporting: what is actually binding, and what is not.**

INCD publishes **no reporting timeline for any sector**. Do not state one. Earlier versions of this skill asserted "critical infrastructure must report within hours" plus a four-tier deadline ladder; neither is sourced, and both were removed. Detail in `references/incd-guidelines.md`.

- **The one binding civilian-sector reporting statute** is the **Severe Cyber Attacks in the Digital Services and Hosting Sector (Temporary Order), 5784-2023** (חוק התמודדות עם תקיפות סייבר חמורות במגזר השירותים הדיגיטליים ושירותי האחסון). INCD's reporting page cites it directly. If the organisation is a digital-service or hosting provider, its reporting duty is statutory, not voluntary. **This is the most common mistake in scoping an Israeli cyber engagement.**
- **Everyone else:** reporting to INCD is voluntary. INCD states expressly that sharing information with it **does not substitute** for a reporting duty owed to a sector regulator or guiding body, so a bank still reports under Directive 366 and a listed company still reports to the ISA.
- **Sector regulators set the real clocks.** Banks: Directive 366. Listed companies: ISA. Databases at medium or high security level: the PPA, immediately.
- **Reporting channel:** the INCD operational centre on **119**, or 072-3990801, or **119@cyber.gov.il**, 24/7.
- **A designated body under the Regulation of Security in Public Bodies Law, 5758-1998, is a separate question.** Its duties and reporting line come from its statutory guiding body. This skill does not carry the Law's schedules, so establish designation status from the organisation itself rather than inferring it from a sector list.
- **A national cyber statute is close** (see the Gotchas). It is not law yet, so do not apply its clocks today.

**Annual INCD baseline checklist** (risk assessment, asset inventory including OT/IoT, tested IR plan, supply-chain review, awareness training, backup validation, external penetration testing): see `references/incd-guidelines.md`.

### Step 3: Bank of Israel Directive 364 (the operative framework)

> **Directive 361 is repealed. Do not build a control program against it.**
> Directive 364, "Management of IT, Information Security and Cyber Protection Risks" (published 18/11/2024, circular 2799), took effect **18/05/2026**, or on earlier adoption by the banking corporation, whichever came first. The BOI page states that from that date Directives **357, 361 and 363 are cancelled**, along with two 2009 supervision letters. Both dates are now past, so 364 governs every banking corporation.
>
> The substantive control content of 361 largely carries forward into 364 with stronger board accountability and supply-chain expectations, so a mature 361 program is a good starting inventory. But the citation must be 364. An audit response, board paper, or gap analysis that cites "Directive 361" is citing a repealed instrument, and this is the single most common error on this topic because most training data predates 18/05/2026.

**The surrounding directives, which 364 did NOT absorb:**

| Directive | Status | Role |
|---|---|---|
| 366 | In force, updated 17/06/2026 (circular 2848, update 4) | Incident reporting. Update 4 added a duty to report a "serious security event" as defined in section 31 of the Financial Information Service Law, 5782-2021, with a parallel amendment to reporting directive 880 |
| 362 | In force, updated 17/06/2026 (circular 2849, version 5) | Cloud computing. Now drafted as complementing 364 |
| 368 | In force, 01/09/2025 (circular 2826) | Open Banking in Israel |
| 367 | In force, updated 17/06/2026 (circular 2847) | Banking via communications (remote and electronic channels) |

**Read this before using the table below.** The control expectations that follow are a **working inventory carried over from the repealed Directive 361. They are NOT a Directive 364 control list, and this skill has not mapped them to 364's clauses.** Directive 364 is 57 pages and merges three directives (357 IT governance, 361 cyber, 363 supply chain), so an inventory derived from 361 alone is both over-specified, because it carries cadences 361 stated and 364 may not, and under-specified, because the absorbed IT-governance and supply-chain content is not represented here at all.

**Do not produce an audit evidence package from this table without reading Directive 364 itself** (linked from the BOI 364 page). Use the table to know what to look for; use the directive to know what is required and to cite it.

**Core requirements:**
1. **Board-level cyber governance:** Directive 364 requires the board to discuss, decide and approve the annual and multi-year IT work plan **once a year** (clause 17.7), and to meet the IT manager and the cyber-and-information-security manager **at least once a year** (clause 17.8). Earlier versions of this skill said "quarterly reports"; the word "quarterly" does not appear in Directive 364
2. **Dedicated CISO:** Must appoint a Chief Information Security Officer reporting to senior management
3. **Security Operations Center (SOC):** 24/7 monitoring for banks with significant digital operations
4. **Penetration testing:** external penetration testing as part of the testing regime. **This skill states no frequency and no tester-certification requirement**: both were carried over from the repealed 361 summary without a source. Take the cadence from Directive 364's own text
5. **Third-party risk:** Due diligence on all technology vendors. **Cloud is governed by Directive 362 and does NOT require prior BOI approval**, see the Gotchas
6. **Incident reporting:** Report technological-failure, information-security and cyber-attack events to Banking Supervision under Directive 366, and a "serious security event" under section 31 of the Financial Information Service Law per update 4 of 366

**Control matrix (map each row to a Directive 364 clause):**
| Control Area | What to look for | Evidence |
|---|---|---|
| Governance | Board-approved cyber policy | Policy document, board minutes |
| Personnel | Cyber and information-security manager appointed | Appointment letter, org chart |
| Monitoring | Continuous monitoring capability | Procedures, alert logs |
| Testing | Penetration testing regime | Test report, remediation plan |
| Vendor and cloud | Directive 362: internal approval by materiality, plus the annual 881 report | Approval record, cloud policy, the 881 report, SLAs |
| Incident response | Directive 366 (update 4, 17/06/2026) | IR plan, drill records, report copies |
| Business continuity | DR site and testing | BCP, DR drill results |

### Step 4: Payment and Fintech Security
Payment-service security for banks and fintech is governed by Directive 364 together with BOI supervision of payment service providers. Note: the repealed Directive 357 was "Management of Information Technology", a general IT-governance directive, never a payment-specific rule, so do not cite "357" as the payment-security authority, and do not cite it at all now that it is repealed. The substantive payment-security expectations are:

**Substantive expectations:** real-time transaction monitoring, strong authentication for high-value transactions, encryption in transit and at rest, secure API design for Open Banking, and customer alerting on suspicious activity. **PCI DSS** is a card-scheme *contractual* standard imposed through acquirer and scheme agreements, **not an Israeli legal requirement**: check the acquiring agreement, and do not tell a provider the law requires it.

**Fintech-specific considerations:**
- **There is no published pre-launch cyber sign-off, at BOI or elsewhere.** An earlier version of this skill stated that new licensees must submit a cyber assessment before launch. That is not sourced and was removed. Cyber and information-security expectations for a payment licensee are licensing conditions set by the Authority's regulator instructions under the 5783-2023 Law; read the licence conditions and ask the licensing team, and do not describe a filing gate that may not exist
- Payment initiation services require enhanced transaction monitoring
- Digital wallet providers must implement device binding and biometric verification
- Cross-border payment services face additional AML/CFT cyber controls

### Step 5: ISA Requirements for TASE-Listed Companies
The Israel Securities Authority (Rashut Niyarot Erech) requires listed companies to address cyber risk.

**Disclosure requirements:**
1. **Annual report:** Disclose material cyber risks in annual filing (Doch Shnati)
2. **Immediate report:** File immediate disclosure (Divuach Miyadi) for material cyber incidents
3. **Board oversight:** Board must demonstrate awareness of cyber risk management
4. **Risk factors:** Cyber risks must appear in risk factor section if material

**The two instruments that actually govern, and which this skill previously failed to cite:**
- **Regulation 36 of the Securities Regulations (Periodic and Immediate Reports), 5730-1970** is the immediate-reporting obligation itself.
- **ISA staff legal position 105-33, "Disclosure on Cyber"**, October 2018, updated 25 January 2023. The update added cyber-audit findings, a definition of "cyber attack", disclosure of cyber risk-management policy, board cyber expertise, and how to assess materiality for immediate reporting.

**Materiality is qualitative. There is no numeric trigger.**
```
Would a reasonable investor consider this information important?
  - Data breach affecting customers -> likely material
  - Ransomware disrupting operations -> likely material
  - Minor phishing attempt contained -> likely not material
  - Vendor breach with no data exposure -> case-by-case
Then assess against regulation 36 and staff position 105-33.
```
**Do not state a numeric threshold.** Before v1.3.0 this skill told users to file if disruption exceeded 24 hours or loss exceeded 1% of equity. Staff position 105-33 was read in full and contains neither figure, nor any percentage. Both were removed. If a user wants a bright line, the answer is that the ISA has not published one.

**ISA compliance checklist:**
- [ ] Cyber risk section in annual report reviewed and current
- [ ] Board received cyber briefing in past 12 months
- [ ] Immediate reporting procedure defined and tested
- [ ] Cyber insurance coverage assessed and disclosed (if material)

### Step 6: Sector-Specific Rules
Apply additional requirements based on industry vertical.

**Fintech / Banking:**
- BOI Directive 364 (see Steps 3-4), with 366 reporting, 362 cloud, 367 remote banking
- **Open Banking: Directive 368, "Open Banking in Israel", 01/09/2025 (circular 2826).** This is a directive now, not a roadmap
- AML/CFT applies via IMPA, but **IMPA publishes no cyber directive**. State the AML/CFT duty and the cyber duty separately, from their own instruments

**Healthtech / Digital Health:**
- **MOH Director-General Circular 06/2022**, "Basic regulation for cyber protection in the Israeli health system", effective 13.03.2022. Cite it by number; an unnumbered "MoH circular" is unusable in a compliance document
- Also the health-sector organisational defence doctrine (08.12.2021) and the cyber crisis-management PAKAL (15.03.2022, updated 13.02.2023). Detail in `references/sector-rules.md`
- Patient data: Israeli Privacy Protection Law + MOH-specific rules
- Medical devices: CE/FDA cyber requirements + MOH registration
- Telemedicine: Secure video, authentication, audit trails per MOH guidelines

**Defense / Aerospace:**
- MALMAB directives are **not published**, so this skill carries no classification ladder and no control list. Say so and route the user to their MALMAB security officer and the contract's security annex. A four-level ladder that matched no published Israeli scheme was removed in v1.3.0

**Telecom / ISPs:**
- The operative instrument is the Ministry of Communications **administrative directive "Cyber Protection Management"** and the matching **annex to licences** under the Communications (Telecommunications and Broadcasts) Law, 5742-1982. The cyber duty is a **licence condition**, which is why searching for regulations misses it. Confirm the directive's current date and the operative licence-amendment number from the ministry before citing either; this skill does not state them
- Lawful intercept and data retention are separate duties, not the cyber instrument

**Energy / Utilities:**
- Duties follow from designation under the Regulation of Security in Public Bodies Law and the guiding body, not from an INCD directive. SCADA/OT security and combined physical-and-cyber controls are the substantive areas

### Step 7: Build Regulatory Compliance Roadmap
Create a prioritized action plan based on identified gaps.

**Priority framework:**
| Priority | Criteria | Timeline |
|----------|----------|----------|
| Critical | Regulatory mandate with enforcement deadline | 0-30 days |
| High | Required by regulator, no immediate deadline | 30-90 days |
| Medium | Best practice recommended by INCD | 90-180 days |
| Low | Enhancement beyond minimum requirements | 180-365 days |

**Roadmap:** identify the applicable frameworks (Step 1, and get the regulator right before the instrument), map current controls, gap-analyse, prioritise by regulatory risk, assign owners, implement, document evidence, and schedule periodic review.

## Examples

### Example 1: Fintech Startup Pre-Launch
User says: "We're launching a payment app in Israel, what cyber regulations apply?"
Actions:
1. Identify the regulator FIRST. A non-bank payment app is almost certainly an ISA licensee under the Payment Services and Payment Initiation Law, 5783-2023, not a BOI-supervised body, unless it reaches systemic importance. Then add the INCD baseline and check whether the app is a digital service caught by the 5784-2023 temporary-order reporting statute
2. Map requirements: transaction monitoring, MFA, encryption, PCI DSS
3. Check if TASE listing planned (ISA requirements)
4. Build pre-launch compliance checklist with BOI submission requirements
Result: Prioritized regulatory compliance roadmap for the launch, built from the correct regulator's licensing conditions, with no invented submission gate.

### Example 2: Bank Annual Cyber Audit
User says: "We need to prepare for our BOI Directive 361 annual review"
Actions:
1. **Correct the premise first.** Directive 361 was repealed on 18/05/2026 by Directive 364. Tell the user plainly, because their internal documentation and audit scope are probably still written against 361
2. Re-map the existing 361 control inventory onto 364 clauses. The substance largely carries forward, so this is a re-citation and gap exercise, not a rebuild
3. Verify: board approval, CISO reporting, SOC operations, pen test results
4. Check cloud governance under Directive 362 (internal approval by materiality plus the annual 881 report), not a BOI pre-approval file
5. Confirm incident reporting is mapped to Directive 366 as updated 17/06/2026, including the Financial Information Service Law serious-security-event duty
Result: A Directive 364 evidence package, plus an explicit list of every place the organisation still cites a repealed directive.

### Example 3: TASE-Listed Company Cyber Incident
User says: "We had a data breach, do we need to file with ISA?"
Actions:
1. Apply materiality test: customer data exposed, operational impact, financial loss
2. Assess the immediate disclosure obligation under regulation 36 and ISA staff position 105-33, applying the qualitative reasonable-investor test with no numeric threshold
3. Check INCD/CERT-IL reporting requirements
4. Draft disclosure timeline: ISA immediate report + CERT-IL notification + customer notification
Result: Incident disclosure decision with regulatory reporting timeline and draft notification framework.

### Example 4: Healthtech Compliance Assessment
User says: "Our healthtech startup handles patient data, what cyber rules apply?"
Actions:
1. Identify: MOH Director-General Circular 06/2022 + INCD baseline + Privacy Protection Law and the 2017 Data Security Regulations
2. Map patient data requirements: encryption, access controls, audit trails
3. Check medical device classification (if applicable)
4. Build compliance matrix combining MOH, INCD, and privacy requirements
Result: Multi-framework compliance matrix with healthtech-specific controls and MOH submission requirements.

## Bundled Resources

### References
- `references/incd-guidelines.md` -- Comprehensive guide to INCD (Ma'arach HaSyber) framework including the five-pillar cyber defense model, CERT-IL reporting procedures, critical infrastructure designations, and national cybersecurity baseline requirements. Consult when assessing INCD compliance or preparing incident reports.
- `references/sector-rules.md` -- Sector-specific cybersecurity regulation details for financial services (BOI 364 and the surrounding directives), healthtech (MOH circular 06/2022), telecom (the licence cyber annex), and energy. Includes control matrices, reporting deadlines, and regulator contact information. Consult when mapping sector-specific requirements.

## Gotchas

- **There is no BOI pre-approval for cloud, and this skill said there was until v1.3.0.** Directive 362 (version 5, 17/06/2026) requires the banking corporation's **senior management to set a cloud policy** defining which services count as "material cloud computing" and therefore need **board** approval, which need senior-management approval, and which need other approval, plus a **written annual report to Banking Supervision** under reporting directive 881. That is an internal-governance and reporting regime, not a licensing gate. Directive 362 also states the supervisory approach is **enabling ("Business enabler")** and treats migration of systems to cloud, including material systems, as part of technological development subject to prudent risk management. An agent that tells a bank it must obtain BOI sign-off before using a cloud provider will stall a project on a requirement that does not exist. Separately, SOC 2 certification alone does not discharge the 362 obligations.
- **Do not state an INCD reporting deadline.** INCD publishes none, for any sector. Earlier versions of this skill asserted "within hours" for critical infrastructure and a four-tier deadline ladder; both were unsourced and were removed in v1.3.0. The 24-hour and 72-hour clocks that circulate come from the **pending** National Cyber Defense bill, not from current law, so quoting them today back-dates a future statute onto present obligations.
- **"Private-sector reporting is voluntary" is not true across the board.** Digital-service and hosting providers have a statutory duty under the Severe Cyber Attacks (Digital Services and Hosting) Temporary Order Law, 5784-2023. Scope the organisation before saying reporting is optional.
- The Israeli Securities Authority (ISA/Rashut) uses a different materiality test for cyber incident disclosure than the US SEC. Agents may apply US materiality standards to TASE-listed companies.
- Israel's DPO (Data Protection Officer) requirement is in force since Amendment 13 and covers **public bodies, organisations processing sensitive data at scale, AND organisations whose activity involves systematic monitoring**. The monitoring limb is routinely dropped and it is the one that catches adtech, analytics and workforce-surveillance products that hold little sensitive data. Agents with pre-2025 training data may not know the requirement exists at all.
- **Amendment 13 cross-reference for cyber teams, with the citation corrected.** The duty to notify the PPA of a serious security event **immediately** does not originate in Amendment 13. It is **regulation 11(d)(1) of the Privacy Protection (Data Security) Regulations, 5777-2017**, and it binds the owner and the holder of a database subject to the **medium or high** security level, not every organisation. What Amendment 13 added is the enforcement: a financial sanction under section 21 of the Third Schedule. The practical consequences for a playbook: check the database's security level before assuming the duty applies, and note that "immediately" is not a GDPR-style 72-hour clock.
- **The PPA has now enforced this, and its reading of "immediately" is strict.** On 21.07.2026 it imposed a **256,000 NIS** sanction for failure to report a serious security event immediately, the first since Amendment 13 took effect. Its stated position is that the duty arises on becoming aware of the event and must be performed close to discovery and without delay, and that waiting to complete all investigations empties the immediacy requirement of content. Do not draft a playbook that gathers full forensics before notifying. The PPA states the required report is a **preliminary** one based on what is known at the time, and that further detail may follow in a supplementary report, so the playbook's first notification gate should be "do we know enough to say a serious security event occurred?", not "have we finished the investigation?". In the enforced case the organisation had sufficient information at the point it blocked the actor's permissions, but reported roughly two months later.
- **National Cyber Defense Law: no longer a draft memorandum, and close to enactment.** It began as a tazkir in January 2026, became **government bill 1955** published 27 May 2026, passed first reading, and has been in the **Foreign Affairs and Defense Committee preparing for second and third reading** since 29 July 2026 (Knesset bill ID 1046714, status "הכנה לקריאה שנייה ושלישית"). **It is still not law**: a Knesset legislation-record query for an enacted law of that name returns no rows, and the bill carries no publication date. Treat it as imminent rather than speculative. What it would introduce, which is worth scoping for now but must NOT be presented as current obligation: statutory reporting clocks (immediate on one route; initial within 24 hours and follow-up within 72 hours on the other), a mandatory organisational CISO, an "essential organisation" designation mechanism, and a standards menu wider than this skill previously described, covering ISO/IEC 27001 and 27002, the Israeli standards SI 27001 and SI 27002 adopted 31 January 2023, NIST CSF 2.0 (26 February 2024) and NIST SP 800-53.
- Directive 357 was "Management of Information Technology" (general IT governance), never a payment-security directive, and it is **repealed** as of 18/05/2026. Agents citing "357" as the Israeli payment-security rule are wrong twice over. Payment-service security comes from BOI payment-service-provider supervision plus Directive 364.
- **The dominant failure mode on this whole topic is citing a repealed directive with confidence.** Directives 357, 361 and 363 were cancelled on 18/05/2026, which post-dates most models' training data, so an agent asked about "Israeli bank cyber regulation" will reach for 361 by default and sound authoritative. Before answering, open the directive's OWN page on boi.org.il, not just the index: as of 26/08/2026 the index still lists 357, 361 and 363 as ordinary rows, and the cancellation appears only on the individual directive pages and the separate cancelled-directives list. An agent that checks the index alone will conclude 361 is alive. If a user's own documents cite 361, tell them, rather than answering inside their premise.


## Reference Links

| Source | URL | What to Check |
|--------|-----|---------------|
| BOI Proper Conduct directives index | https://www.boi.org.il/roles/supervisionregulation/nbt/ | Lists the directives, but **as of 26/08/2026 it still shows 357, 361 and 363 as ordinary rows.** The index alone does NOT tell you what is in force. Use it to find the directive, then open the directive's own page, where the cancellation sentence lives, and the separate cancelled-directives page |
| BOI Directive 364 | https://www.boi.org.il/roles/supervisionregulation/nbt/nbt364/ | The operative IT/cyber framework, its effective date, and the cancellation of 357/361/363 |
| BOI Directive 366 | https://www.boi.org.il/roles/supervisionregulation/nbt/nbt366/ | Incident reporting, current update number and circular |
| BOI Directive 362 | https://www.boi.org.il/roles/supervisionregulation/nbt/nbt362/ | Cloud computing, current version. Confirm the approval and annual-reporting mechanics before advising |
| Israel National Cyber Directorate (INCD) | https://www.gov.il/he/departments/israel_national_cyber_directorate | Official cyber policy, the 119 operational centre |
| INCD cyber event reporting | https://www.gov.il/he/service/cyber-event-report | The actual reporting channel, and the statute it cites. Check whether any sector timeline has been published |
| Israel Securities Authority | https://www.isa.gov.il/ | Staff position 105-33 on cyber disclosure, and regulation 36 immediate reporting |
| Privacy Protection Authority | https://www.gov.il/he/departments/the_privacy_protection_authority | Data Security Regulations, breach reporting, Amendment 13 enforcement decisions |
| PPA serious-security-event reporting | https://www.gov.il/he/pages/reporting_security_breach | The regulation 11(d)(1) duty and which databases it binds |
| Knesset legislation records | https://main.knesset.gov.il/Activity/Legislation/Laws/Pages/default.aspx | Whether the National Cyber Defense bill has been enacted |

## Troubleshooting

### Error: "Unsure which framework applies"
Cause: Organization operates across multiple regulated sectors
Solution: Apply all applicable frameworks. Start with the INCD baseline (voluntary for most, statutory for digital-service and hosting providers under the 5784-2023 temporary order), then layer sector-specific requirements. For dual-regulated entities such as a fintech listed on TASE, combine Directive 364 with the ISA regulation 36 and 105-33 disclosure duties. Reporting duties stack rather than substitute: INCD says expressly that reporting to it does not discharge a duty owed to a sector regulator.

### Error: "Conflicting requirements between regulators"
Cause: Different regulators set different standards for overlapping areas
Solution: Apply the stricter requirement. Document the rationale. For formal conflicts, consult with legal counsel specializing in Israeli financial regulation (orech din le-regulatziya finansit).

### Error: "No clear cyber regulation for our sector"
Cause: Some sectors lack specific cyber regulation
Solution: Follow the INCD voluntary baseline as a minimum. If handling personal data, apply the Privacy Protection (Data Security) Regulations, 5777-2017, and establish the database's security level, since the immediate breach-notification duty in regulation 11(d)(1) binds only medium and high levels. Monitor the National Cyber Defense bill: once enacted it will convert much of this voluntary layer into statutory duty for "essential organisations".
