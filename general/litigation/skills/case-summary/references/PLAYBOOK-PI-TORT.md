# Personal Injury / Tort Playbook

---
practice_area: pi-tort
triggers:
  filenames: [medical, ems, police-report, ambulance, mri, imaging, ER, ED, PT, ortho, billing, hcfa, ub-04, demand, lien, subrogation, accident, incident]
  content_signals: [negligence, duty of care, premises liability, motor vehicle collision, slip and fall, bodily injury, pain and suffering, medical specials, loss of consortium, workers compensation lien, ERISA plan, Medicare conditional payment]
defers_to:
  - medical-record-chronology: when the corpus has a dense medical-records set
  - medical-treatment-summary: when the user needs a causation-focused treatment narrative
  - deposition-summary: when depositions appear in the corpus
  - discovery-summary: when interrogatory/RFP/RFA responses appear
  - lien-resolution-summary: when lien correspondence is load-bearing
  - pi-demand-summary: when the user's objective is a settlement demand
  - evidence-liability-summary: when the user wants a plaintiff-side liability element breakdown
---

## Dimension extensions

### Parties & posture
Add insurance columns: carrier, policy limits (if disclosed), adjuster, claim number, tender status. Identify excess carriers and any UM/UIM coverage on the plaintiff side.

### Timeline
Subdivide into: pre-incident baseline, incident, acute care (≤30 days), subacute treatment, surgical events, MMI, post-MMI maintenance. Flag treatment gaps >30 days as distinct events.

### Evidence inventory
Expected types: police/incident report, scene photos, surveillance, witness statements, 911 audio, EMS run sheet, ER record, imaging, operative notes, PT/rehab notes, billing ledgers (HCFA-1500, UB-04), employer wage records, vocational/life-care plans, expert reports.

### Claims & legal theories
Duty / breach / causation / damages. For premises: notice element (actual or constructive) is separate. For products: design vs. manufacturing vs. warning. For med-mal: standard of care + breach + proximate cause + damages, with expert affidavit where required.

### Exposure / remedies
Economic (past medical specials, future medical, lost wages past, lost earning capacity) + non-economic (pain & suffering, loss of consortium, loss of enjoyment) + punitive where pled. Offsets: comparative-fault reduction, collateral-source (jurisdiction-dependent), liens.

### Defenses
Comparative / contributory fault, pre-existing condition, failure to mitigate (treatment compliance), open-and-obvious (premises), assumption of risk, SOL, release/waiver.

### Red flags & open threads
Treatment gaps, prior claims / prior similar injuries, social media activity, surveillance footage, inconsistent statements, spoliation, low-impact bio-mechanics (low property damage), independent medical examination (IME) adverse findings.

## Queries

### Parties & posture
- `"insurance carrier policy number limits"`
- `"adjuster claim number tender acceptance"`
- `"UM UIM underinsured uninsured"`

### Timeline / incident facts
- `"date of incident accident loss occurrence"`
- `"location address intersection premises"`
- `"police report officer narrative"`
- `"witness statement observation"`
- `"mechanism of injury how it happened"`

### Evidence inventory (injuries, treatment)
- `"diagnosis ICD injury body part"`
- `"chief complaint presenting symptoms"`
- `"emergency room triage admission"`
- `"imaging MRI CT X-ray ultrasound findings"`
- `"pre-existing condition prior history"`
- `"treatment plan provider specialist referral"`
- `"surgery operative report procedure"`
- `"physical therapy rehabilitation progress"`
- `"medication prescription pain management"`
- `"maximum medical improvement MMI discharge"`
- `"treatment gap no appointment noncompliance"`

### Exposure / remedies — specials
- `"medical bill billed amount statement"`
- `"paid amount adjustment write-off balance"`
- `"CPT code procedure charge"`

### Exposure / remedies — wage loss
- `"employer wage loss time missed work"`
- `"return to work restrictions"`
- `"earnings capacity vocational"`

### Exposure / remedies — future care
- `"life care plan future treatment cost"`
- `"future medical surgery projected"`

### Exposure / remedies — non-economic
- `"pain suffering impact activities daily living"`
- `"loss of consortium enjoyment"`

### Claims & legal theories (liability)
- `"negligence duty breach causation"`
- `"admission statement against interest"`
- `"violation of statute regulation ordinance"`
- `"prior similar incident notice"`
- `"training policy procedure violation"`
- `"deposition admission acknowledged conceded"`

### Defenses
- `"affirmative defense comparative fault"`
- `"contributory negligence failure to mitigate"`
- `"release waiver assumption of risk"`
- `"statute of limitations"`
- `"denial liability answer"`

### Liens (sub-dimension of Exposure)
- `"Medicare conditional payment MSP"`
- `"Medicaid recovery notice"`
- `"ERISA plan reimbursement"`
- `"workers compensation subrogation"`
- `"hospital lien statutory"`
- `"health insurance subrogation right"`

### Red flags
- `"social media post photograph"`
- `"surveillance video investigation"`
- `"inconsistent statement prior"`
- `"spoliation missing evidence"`
- `"gap in treatment unexplained"`

## Output sections

### Medical Summary — slots into V Evidence inventory

**Injuries Claimed:** [List with body part and diagnosis]
**Treatment Timeline:** [Key dates and providers — cite `PLAYBOOK-PI-TORT` timeline subdivisions]
**Current Status:** [Ongoing / MMI / Discharged]
**Causation:** [Assessment of injury-incident nexus with citations]

### Damages Itemization — slots into VI Exposure/remedies

#### Economic Damages

| Category | Amount | Source |
|----------|--------|--------|
| Medical Specials (past)    | $ | [Citations] |
| Medical Specials (future)  | $ | [Citations] |
| Lost Wages (past)          | $ | [Citations] |
| Lost Earning Capacity      | $ | [Citations] |
| **Total Economic**         | **$** | |

#### Non-Economic Damages
[Pain and suffering assessment, impact on daily life, emotional distress]

### Liens — slots into VI Exposure/remedies

| Lienholder | Amount | Type | Source |
|------------|--------|------|--------|
| | $ | Medicare / Medicaid / ERISA / WC / Hospital / Health | [Citation] |

Identified, not resolved. Resolution is an attorney task; this memo flags exposure.

### Valuation — slots into VI Exposure/remedies

| Metric | Amount |
|--------|--------|
| Settlement Range (Low)  | $ |
| Settlement Range (Mid)  | $ |
| Settlement Range (High) | $ |
| Verdict Potential       | $ |
| Net to Client (est.)    | $ |

Ranges are methodology-driven estimates, not attorney judgments. Jurisdiction, venue, and insurance posture are attorney calls. See core-skill disclaimer.

## Quality checklist additions

- [ ] Every specials number traces to a specific billing document (HCFA-1500, UB-04, provider statement)
- [ ] Every lien lienholder has a citation to source correspondence
- [ ] Treatment gaps >30 days either explained or explicitly flagged
- [ ] Pre-existing conditions explicitly addressed for causation
- [ ] Comparative-fault evidence (if any) cited, not just asserted
- [ ] Insurance carrier / policy limits identified (or noted as undisclosed)
- [ ] MMI status stated (reached / not reached / unclear with reason)

## Remedies / exposure methodology

PI damages decompose into economic and non-economic categories. Economic damages are documentary-driven: every dollar ties to a specific billing document, wage record, or expert projection (life care plan, vocational). The playbook enforces that documentary tie as a quality gate.

Non-economic damages (pain and suffering, loss of consortium, loss of enjoyment) are not computable from the record alone — they are functions of jurisdiction, venue, comparable-verdict data, and insurance posture. This playbook produces an *evidentiary foundation* for non-economic damages (functional impact, treatment intensity, MMI prognosis) and notes where attorney judgment must take over.

Liens reduce net-to-client but do not reduce gross settlement value. Medicare/Medicaid liens have federal recovery rights; ERISA plans vary by plan language; workers-comp has statutory subrogation; hospital liens are state-statutory. The playbook identifies each lien and its type; resolution is an attorney task.

For settlement ranges, the playbook produces a methodology-driven estimate (specials × multiplier for general damages, adjusted for comparative-fault percentage, less reasonably-anticipated lien burden) and flags the underlying assumptions. Attorney adjusts for venue, jury characteristics, and negotiation posture.
