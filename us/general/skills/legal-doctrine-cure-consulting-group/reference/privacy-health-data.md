# Privacy & Health Data — practice reference (NY-first)

Load when: a product stores NY residents' personal data, handles health, mood, or ADHD data outside HIPAA, records calls or encounters, uses biometrics, sells to schools, or asks "are we covered by CCPA?".
Verified 2026-09-28: GBL §899-aa (definitions incl. medical/health-insurance info, 30-day timing, agencies, 5,000 CRA threshold, penalties, limitations) and §899-bb (safeguards, small-business test, no private right) (nysenate.gov); Dec. 2024 SHIELD amendments and Mar. 21, 2025 effective date (secondary: Baker McKenzie, Ropes & Gray); NYHIPA S929 veto Dec. 19, 2025 and S9269 history (nysenate.gov bill page); Penal Law §§250.00, 250.05 (nysenate.gov); RCW 19.373.010 (app.leg.wa.gov); MHMDA effective dates, *Maxwell v. Amazon* filing (secondary); NYC Admin Code §§22-1201–22-1203 (amlegal.com / secondary); BIPA SB 2979 and *Clay v. Union Pacific* (7th Cir. 2026) (secondary); Education Law §2-d (nysenate.gov); 8 NYCRR §§121.9, 121.10 (law.cornell.edu); CCPA threshold \$26,625,000 (cppa.ca.gov FAQ via secondary); FTC HBNR 16 C.F.R. §§318.2, 318.4 (law.cornell.edu), effective July 29, 2024. Independently re-checked 2026-09-28: §899-aa inadvertent-disclosure documentation and >500 AG filing; GBL §350-d (\$5,000) as the §899-bb penalty; S929/S9269 action history; NY Const. art. IV §7; all-party recording statutes CA Penal §§632, 637.2 (leginfo), FL §934.03 (flsenate.gov), MD CJP §10-402 (mgaleg), MA c.272 §99 (malegislature.gov), MT §45-8-213 (mca.legmt.gov), NH RSA 570-A:2 (gc.nh.gov), WA RCW 9.73.030 (app.leg.wa.gov); IL 720 ILCS 5/14-2, PA §5704(4), CT §52-570d, OR ORS 165.540, DE, *Lane v. Allstate*, *Sullivan v. Gray* (secondary/justia/courtlistener); *Ambriz v. Google* and CA SB 690 status (secondary); CT SB 1295 / SB 4 (Snell & Wilmer); NV NRS 603A.400–.550 (secondary); *Maxwell* consolidation (courtlistener docket, secondary); Education Law §2-d penalties; 8 NYCRR §§121.1, 121.10; CCPA regulation phase-in (secondary).
Not verified: NYHIPA exemption count; whether CT SB 4 (2026) changes consumer-health-data rules; SB 690 signature (Governor's deadline 2026-09-30); items marked (confirm before use).

## NY SHIELD Act — breach notice (GBL §899-aa)
- **Rule:** Applies to any person or business that owns or licenses computerized data with **private information of a NY resident**. No NY presence is needed. A breach is unauthorized **access to or acquisition of** that data.
- **"Private information" includes:**
  - personal information plus SSN, driver's license, account number with access code, or **biometric** data;
  - username or email plus password or security Q&A, even standing alone;
  - **since Mar. 21, 2025:** **medical information** ("any information regarding an individual's medical history, mental or physical condition, or medical treatment or diagnosis by a health care professional") and **health insurance information** (policy or subscriber ID, claims and appeals history).
- **Numbers / deadlines:**
  - **Individuals:** notify "in the most expedient time possible and without unreasonable delay," and **no later than 30 days after discovery**. The 30-day cap was added Dec. 2024.
  - **Agencies:** notify the **AG, Department of State, Division of State Police**, and **DFS** if the entity is DFS-covered.
  - **Consumer reporting agencies:** notify them if **>5,000 NY residents** are notified at once.
  - **Exception:** an inadvertent disclosure by authorized persons, reasonably determined unlikely to cause misuse. The determination **must be in writing and kept 5 years**; if it covers **>500 NY residents**, send the written determination to the **AG**.
  - **Penalty:** civil penalty of the greater of **\$5,000** or up to **\$20 per failed notification**, capped at **\$250,000**.
  - **Limitations:** 3 years from AG awareness or notice, and 6 years max unless the breach was concealed.
- **HIPAA / GLBA / DFS entities:** No duplicate individual notice is required, but agency notice still is.
- **Applies to a product when:** An ADHD or mood app's symptom logs, a scribe's transcripts, or a wellness journal leak with names. These are now "medical information" under SHIELD even though HIPAA doesn't apply.
- **Traps:** Treating non-HIPAA health data as outside breach law. It has been inside NY's since Mar. 2025. Also watch the 30-day clock alongside the FTC HBNR 60-day clock (below).

## NY SHIELD Act — safeguards (GBL §899-bb)
- **Rule:** Maintain "reasonable safeguards" — administrative, technical, and physical. Entities compliant with GLBA, HIPAA, or **DFS Part 500** are deemed compliant.
- **Small business:** fewer than **50 employees**, OR less than **\$3M** gross revenue in each of the last 3 years, OR less than **\$5M** year-end assets. A small business's safeguards are scaled to size and sensitivity; it is **not exempt**.
- **Enforcement:** AG only; **no private right of action**. Injunction plus civil penalties under GBL §350-d: up to **\$5,000 per violation**.
- **Traps:** Plaintiffs plead §899-bb failures as negligence or GBL §349 claims anyway.

## NY Health Information Privacy Act (NYHIPA)
- **Status (verified 2026-09-28):** **Not law.**
  - **S929:** passed Senate Jan. 21, 2025 (49–10) and Assembly Jan. 22, 2025; delivered Dec. 8, 2025; **vetoed Dec. 19, 2025** (Veto Memo 135; "too broad").
  - **Revised bill S9269 / A10357:** **passed Senate June 3, 2026 (48–13) and Assembly June 4, 2026.** The bill page shows **no delivery to the Governor yet** (checked 2026-09-28). NY bills are often delivered late in the year; once delivered, the Governor has **10 days (Sundays excepted)** to act, or 30 days after the Legislature's final adjournment (NY Const. art. IV §7).
  - **If signed:** takes effect **6 months after it becomes law**.
- **What S9269 would do (per the bill and MoFo summary):**
  - covers "regulated health information" linked to a person's physical or mental health, including **inferences** from algorithms;
  - reaches entities in NY or processing NY residents' data;
  - authorization-first processing unless **"strictly necessary"** (expanded to include developing or improving a requested feature);
  - a near-total **sale ban**;
  - exemptions including HIPAA covered entities (count of 21 per MoFo: confirm before use);
  - AG-only enforcement, **up to \$15,000 per violation**.
- **Applies to a product when:** It would squarely hit ADHD/mood apps and wellness features. Design now so consent can be split by purpose.
- **Traps:** Articles titled "New York Just Passed…" are about legislative passage, not enactment. Check for a chapter number.

## Consumer-health-data laws (other states) — ADHD, mood, wellness
- **Washington My Health My Data Act (RCW ch. 19.373):**
  - **Defines** consumer health data as personal info that "identifies the consumer's past, present, or future physical or **mental** health status." It expressly includes "social, **psychological, behavioral**, and medical interventions," symptoms, biometric data, health-seeking location, and data **"derived or extrapolated from nonhealth information"** (inferences).
  - **Covers** WA residents and anyone whose data is collected in WA.
  - **Thresholds:** none; small businesses are covered.
  - **Geofence ban:** within **2,000 ft** of health-care facilities.
  - **Effective** Mar. 31, 2024 (small businesses June 30, 2024).
  - **Private right of action** through the WA Consumer Protection Act. First class action: *Maxwell v. Amazon.com* (W.D. Wash., No. 2:25-cv-261, filed Feb. 10, 2025), consolidated as *In re Amazon Ads SDK Litigation*, No. 2:25-cv-00252; no dispositive ruling found as of Sept. 2026.
  - **ADHD/mood data: yes, covered.**
- **Connecticut (CTDPA consumer-health-data amendments, 2023; Conn. Gen. Stat. §§42-515–42-526, health data at §42-526):**
  - Consumer-health-data controllers are covered **regardless of volume thresholds**, and the nonprofit exemption doesn't apply.
  - Consent is required to process or sell. No private right of action.
  - SB 1295 (2025) removed thresholds for sensitive data and sales (and cut the general threshold to 35,000 consumers), effective July 1, 2026. SB 4 (as amended by HB 5222) was signed June 2, 2026, effective Oct. 1, 2026 (geolocation-sale ban, data brokers, surveillance pricing); effect on health-data rules: confirm before use.
  - **Mental-health condition data: covered.**
- **Nevada (SB 370, NRS 603A.400–603A.550; secondary sources):**
  - Modeled on MHMDA, with no thresholds. Effective Mar. 31, 2024.
  - Enforced by the AG as a deceptive trade practice; **no private right of action**.
- **Federal — FTC Health Breach Notification Rule (16 C.F.R. Part 318; amended, effective July 29, 2024):**
  - **Covers** non-HIPAA health apps that draw data from multiple sources (e.g., user input plus device or API).
  - **"Breach" includes unauthorized disclosure,** such as sharing with ad SDKs.
  - **Timing:** notify individuals within **60 days**. For ≥500 people, notify the FTC **at the same time**; for fewer than 500, send an annual log.
  - FTC Act §5 also applies (GoodRx and BetterHelp orders, 2023).
- **Traps:** "We're not HIPAA" is the start of the analysis, not the end. Pixel and SDK sharing of screens like "ADHD assessment" is a disclosure of health data under all of the above.

## Recording consent — calls, meetings, AI scribes
- **NY (Penal Law §§250.00, 250.05):** Eavesdropping is a **class E felony**.
  - **"Mechanical overhearing"** = recording a conversation "without the consent of **at least one party** thereto, by a person **not present** thereat."
  - **"Wiretapping"** = recording a phone call by a non-party without the consent of the sender or receiver.
  - **Result:** NY is **one-party**. A participant — or the participant's tool, acting with that participant's consent — may record.
  - **Evidence:** eavesdropping evidence is inadmissible (CPLR 4506).
- **Federal:** 18 U.S.C. §2511(2)(d) — one-party, unless the recording is for a criminal or tortious purpose.
- **All-party states (statutes checked 2026-09-28; law-enforcement exceptions omitted):**
  - **California:** Penal Code §632 (confidential communications), §632.7 (cellular). Civil damages \$5,000 per violation (§637.2).
  - **Florida:** §934.03(2)(d) — lawful only when **all parties** give prior consent.
  - **Illinois:** 720 ILCS 5/14-2 — **surreptitious** recording of a **private conversation** without consent of all parties (rewritten 2014 after the prior version was struck down).
  - **Maryland:** Cts. & Jud. Proc. §10-402(c)(3) — party may record only with **all parties'** prior consent.
  - **Massachusetts:** G.L. c. 272 §99 — any *secret* recording without authority from **all parties**.
  - **Montana:** §45-8-213(1)(c) — recording with a **hidden** device without the **knowledge of all parties**; a warning by one party lets either record.
  - **New Hampshire:** RSA 570-A:2 — class B felony without consent of **all parties**.
  - **Pennsylvania:** 18 Pa.C.S. §5703; §5704(4) permits interception only where **all parties** consent.
  - **Washington:** RCW 9.73.030 — consent of **all participants**; a recorded announcement that the call is being recorded counts as consent.
  - **Hybrids:** **Connecticut** — civil all-party for phone calls (§52-570d), criminal one-party. **Nevada** — phone calls all-party by case law (*Lane v. Allstate* (Nev. 1998)), in-person one-party. **Oregon** — in-person all-party, phone one-party (ORS 165.540). **Delaware** — conflicting statutes (11 Del. C. §2402(c)(4) one-party vs. §1335(a)(4) all-party); treat as all-party. **Michigan** — statute reads all-party, but a participant exception is recognized (*Sullivan v. Gray* (Mich. Ct. App. 1982)).
- **Choice of law:** For a cross-state call, courts often apply the law of the state with the **stricter** protection where a party was located. *Kearney v. Salomon Smith Barney* (Cal. 2006) applied California §632 to a Georgia firm recording calls with California clients (injunctive relief). For telehealth, the **patient's location** controls licensure and is the safe anchor for recording consent too.
- **AI scribe / vendor risk:**
  - Under CIPA §631, plaintiffs argue a recording or transcription **vendor** is a third-party eavesdropper. N.D. Cal. courts split between the "extension" and "capability" tests. *Ambriz v. Google* (N.D. Cal. Feb. 10, 2025) adopted the capability test and denied dismissal for Google's contact-center AI; the case was in discovery as of Sept. 2026.
  - CA SB 690: the commercial-purpose exemption was **dropped** in 2026. As passed by the Legislature (Aug. 28, 2026) it only ends private suits over §638.51 pen-register/trap-and-trace claims from website and app tracking, operative Jan. 1, 2027 if signed (Governor's deadline Sept. 30, 2026). It does **not** touch §§631 or 632, so AI-scribe exposure is unchanged.
  - Get **explicit all-party consent at the start of every encounter**, logged in the record. Treat that as the default nationally.
- **Traps:** Relying on NY one-party when the patient or caller is in CA, FL, IL, PA, or WA. A "this call may be recorded" notice with no chance to object. Retaining raw audio after the note is signed. HIPAA does not preempt state wiretap laws.

## Biometrics
- **NYC (Admin. Code §§22-1201–22-1205):**
  - **Who:** "commercial establishments," meaning retail stores, food and drink establishments, and places of entertainment.
  - **Signage:** must post clear, conspicuous signs at customer entrances if they collect biometric identifier information (§22-1202(a)).
  - **No profiting:** selling, leasing, trading, or otherwise profiting from biometric data is **prohibited** (§22-1202(b)).
  - **Private right (§22-1203):** \$500 per signage violation, which requires **30-day notice and a cure opportunity**. For §22-1202(b): \$500 per negligent violation, **\$5,000** per intentional or reckless violation, plus fees.
- **Illinois BIPA (740 ILCS 14):**
  - **Requires** written notice and a written release before collection, a public retention policy, and no profiting.
  - **Private right:** \$1,000 per negligent violation, \$5,000 per intentional or reckless violation (740 ILCS 14/20).
  - **SB 2979 (signed Aug. 2, 2024):** one recovery **per person** per collection method, not per scan; e-signatures count as a written release. *Clay v. Union Pacific R.R.* (7th Cir. Apr. 1, 2026) held the amendment **retroactive** to pending cases.
  - **Reach:** applies when collection occurs in Illinois, e.g., Illinois users of a NY app's face or voice features (extraterritoriality is fact-specific — confirm).
- **NY State:** Biometric data is SHIELD "private information." There is no statewide BIPA analog (confirm pending bills).
- **Traps:** Voiceprints for speaker diarization in an AI scribe, and face matching in highlight tagging, are biometric identifiers. ID-scanner age checks in dispensaries may capture face templates (NYC signage).

## Student data — FERPA and NY Education Law §2-d
- **FERPA (20 U.S.C. §1232g; 34 C.F.R. Part 99):** Applies to schools receiving federal funds, not vendors directly.
  - **Vendor access:** vendors get data under the **"school official" exception** (34 C.F.R. §99.31(a)(1)(i)(B)): an outsourced institutional service, under the school's **direct control**, with use limited to the purpose.
  - **Other points:** redisclosure is limited (§99.33). Directory information requires notice and opt-out (§99.37).
- **NY Education Law §2-d:**
  - **Who:** a **"third-party contractor"** is anyone receiving student data (or teacher/principal APPR data) from an educational agency under a contract or other written agreement. Click-wrap terms for ed-tech count (8 NYCRR 121.1).
  - **No commercial use:** PII **"shall not be sold or used for marketing purposes."**
  - **Parents' Bill of Rights:** must be attached to each contract, with supplemental information about the contract.
  - **Data security and privacy plan:** required in the contract (8 NYCRR 121.6).
- **8 NYCRR §121.9 — contractor duties:**
  - align with the **NIST Cybersecurity Framework**;
  - **encrypt** PII in motion and at rest;
  - no sale, marketing, or commercial use;
  - limit internal access;
  - no use beyond what the contract explicitly authorizes.
- **Breach (8 NYCRR §121.10):**
  - **Contractor to school:** notify **no more than 7 calendar days** after discovery.
  - **School to parents:** notify **no more than 60 calendar days** after discovery or receipt of the contractor's notice.
  - **Costs:** the contractor pays for or reimburses the full cost of notification.
- **Penalties (§2-d):** Up to **\$1,000** for a first violation, **\$5,000** for a second, and **\$10,000** for each later one involving the same data. For a breach: the greater of **\$5,000** or up to **\$10 per student/teacher/principal**. The CPO can also bar the contractor from access.
- **Applies to a product when:** A kids' reading app is licensed by a NY district. A stats app ingests school rosters. A transparency site receives district data beyond public records.
- **Traps:** Using school-sourced data to market a consumer upgrade to parents, or to build a lead list for paid referrals. Treating a 7-day contractor clock as SHIELD's 30.

## CCPA/CPRA touchpoints (California)
- **Covered "business" (Civ. Code §1798.140(d)):** for-profit, **does business in California**, and meets **one** of these tests:
  - gross revenue above the inflation-adjusted threshold (**\$26,625,000** since Jan. 1, 2025);
  - buys, sells, or **shares** the PI of **100,000+** CA consumers or households;
  - **50%+** of revenue from selling or sharing PI.
- **Small startup:** usually out on revenue. It gets **in** via the 100,000 test if ad-tech "sharing" (cross-context behavioral ads) touches 100k CA users or devices. At that scale an SDK-heavy free app gets there.
- **When covered:**
  - health data is **sensitive PI** (right to limit);
  - under-16 data needs **opt-in** before sale or sharing (§1798.120(c));
  - private action only for data breaches (§1798.150);
  - regulations on risk assessments, ADMT, and cybersecurity audits took effect Jan. 1, 2026. Phase-in: ADMT duties for significant decisions by Jan. 1, 2027; risk assessments for pre-2026 processing by Dec. 31, 2027; cybersecurity audits due Apr. 1, 2028/2029/2030 by revenue tier (>\$100M / \$50–100M / <\$50M).
- **Not covered:** Enterprise customers will still impose **service-provider** contract terms. Comply by contract.

## HIPAA
- **Pointer only:** An AI scribe for providers is a **business associate**. It needs a BAA, the minimum-necessary standard, a Security Rule risk analysis, and breach notice to the covered entity. Use the `compliance-architect` skill. De-identified model-training data must meet §164.514 (safe harbor or expert determination).

## Where this stops
- Whether a specific data flow (SDK, pixel, model-training use) is a "sale," "sharing," or "disclosure" under MHMDA, CCPA, HBNR, or NYHIPA if enacted.
- Choice of law and consent design for multi-state recording, especially AI-scribe vendor liability under CIPA.
- Whether a SHIELD, HBNR, or state-law notice duty is triggered, and the notice content — a counsel-led incident call.
- Structuring school contracts (§2-d DPA, FERPA school-official status) where a consumer product shares the same codebase or data.
- Tracking NYHIPA delivery and signature, and CT, NV, and WA litigation — re-verify before advising.
