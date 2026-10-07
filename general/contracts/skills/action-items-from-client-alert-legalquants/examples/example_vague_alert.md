# Worked Example — Vague Alert

This example demonstrates Action Items from Client Alert handling a vague alert that contains substantial informational content but few extractable action items. The skill produces a brief report and explicitly notes that the alert is informational rather than actionable.

## Input

**Alert date:** 2026-04-30
**Review date:** 2026-05-07
**Document:** Law firm client alert titled "FTC Signals Heightened Focus on Algorithmic Decision-Making — What Companies Should Know"

**Optional inputs:**
- organization_context: "Mid-market consumer financial services company; uses ML models for credit decisions; subject to ECOA, FCRA."
- relevant_business_areas: "consumer protection, ML/AI use, credit decisioning"
- applicable_jurisdictions: "US federal"

**Document (excerpts):**

> **CLIENT ALERT — FTC Signals Heightened Focus on Algorithmic Decision-Making**
>
> **April 30, 2026**
>
> Recent FTC enforcement actions and statements from senior FTC officials suggest the Commission is increasing its focus on algorithmic and automated decision-making systems, particularly in consumer-facing contexts. While the FTC has not announced new rules specifically addressing algorithmic decision-making, the agency has indicated through several channels that companies using such systems should expect heightened scrutiny.
>
> **Recent Developments:**
>
> - In a March 2026 enforcement action against [Company], the FTC alleged that the company's automated screening system produced disparate outcomes that violated Section 5 of the FTC Act and the ECOA. The settlement included a $X million civil penalty and required ongoing monitoring of the company's algorithmic systems.
>
> - In April 2026 remarks, FTC Chair [name] emphasized that "the FTC's existing authorities are well-suited to address algorithmic harm" and that "companies cannot hide behind algorithms to avoid responsibility for outcomes that violate consumer protection laws."
>
> - The FTC's June 2025 staff report on algorithmic decision-making (cited in the recent remarks) outlined principles companies should consider, including transparency, auditability, fairness testing, and human oversight.
>
> **Implications for Companies:**
>
> Companies using algorithmic decision-making in consumer-facing contexts should consider the following:
>
> - Whether their existing compliance programs adequately address algorithmic risks.
> - Whether their model documentation supports the demonstration of fair and accurate outcomes.
> - Whether their human oversight mechanisms are sufficient to detect and correct disparate outcomes.
> - Whether their consumer disclosures appropriately describe the role of algorithms in decision-making.
>
> The FTC has not announced new rules. However, companies should expect that the agency will continue to use its existing authorities — Section 5, ECOA, FCRA, and others — to address algorithmic harms. We will continue to monitor developments in this area.
>
> **Looking Ahead:**
>
> Industry participants should also be aware that:
>
> - Several state attorneys general have indicated similar interest in algorithmic decision-making, particularly in California and New York.
> - The CFPB has issued related guidance on algorithmic decision-making in consumer financial contexts.
> - The EU AI Act, while not directly applicable to US-only operations, reflects the international trend toward heightened algorithmic accountability.
>
> *This alert is for general informational purposes only and is not legal advice.*

## Output

# Action Items from Client Alert: FTC Focus on Algorithmic Decision-Making

**Source document:** Client Alert dated April 30, 2026 — "FTC Signals Heightened Focus on Algorithmic Decision-Making"
**Alert date:** April 30, 2026
**Organization context:** Mid-market consumer financial services company; uses ML models for credit decisions; subject to ECOA, FCRA
**Relevant business areas:** Consumer protection, ML/AI use, credit decisioning
**Applicable jurisdictions:** US federal

## Context summary

The alert describes the FTC's signaled increase in focus on algorithmic decision-making systems based on a March 2026 enforcement action and April 2026 remarks from the FTC Chair. Critically, the FTC has not announced new rules; the alert is reporting an enforcement-priority shift, not a new requirement. For the user (consumer financial services with ML credit decisioning), the alert is highly relevant context but does not impose specific deadlines or new obligations.

## Mandatory action items

None. The alert does not describe any new mandatory requirements with deadlines.

The user's existing obligations under Section 5 of the FTC Act, ECOA, and FCRA continue to apply. The FTC's signaled focus may increase enforcement risk but does not change the underlying substantive obligations.

## Recommended action items (no specific deadline)

### 1. Review existing compliance program for algorithmic risk coverage

**What:** assess whether the user's existing compliance program adequately addresses algorithmic decision-making risks, including documentation, fairness testing, human oversight, and consumer disclosures.

**Why recommended:** the alert's "Implications for Companies" section identifies these as areas of FTC focus. While not legally required by this alert, the FTC's increased enforcement attention makes this a prudent review.

**Owner:** Legal (regulatory) coordinated with Compliance, Risk Management, and Data Science / ML teams.

**Source citation:** alert's "Implications for Companies" section.

**Applicability:** Applicable to user given ML use in credit decisioning.

### 2. Review model documentation for fair-outcomes demonstration

**What:** confirm model documentation can support demonstration of fair and accurate outcomes if challenged by the FTC, CFPB, or state attorneys general.

**Why recommended:** the March 2026 enforcement action cited in the alert involved disparate outcomes from automated screening; documentation supporting fairness testing and outcome monitoring would be central to defending similar challenges.

**Owner:** Legal (regulatory), Compliance, Data Science / ML teams.

**Source citation:** alert's "Implications for Companies" section, citing the March 2026 enforcement action.

**Applicability:** Applicable to user.

### 3. Review human oversight mechanisms for detection and correction of disparate outcomes

**What:** confirm that human oversight processes can detect disparate outcomes from ML credit decisions and enable correction.

**Why recommended:** the alert's principles include human oversight; the FTC's posture is that algorithms do not absolve companies of substantive obligations.

**Owner:** Risk Management coordinated with Data Science / ML teams; Legal review.

**Source citation:** alert's "Implications for Companies" section.

**Applicability:** Applicable to user.

### 4. Review consumer disclosures regarding role of algorithms

**What:** review consumer disclosures (adverse action notices, application disclosures, terms of service) to ensure appropriate description of algorithmic role in decision-making.

**Why recommended:** consumer-facing disclosures are a focus area in the alert. Existing ECOA / FCRA disclosure obligations may already cover much of this; the review is to confirm adequacy under heightened FTC focus.

**Owner:** Legal (regulatory, consumer compliance) coordinated with Marketing and Operations.

**Source citation:** alert's "Implications for Companies" section.

**Applicability:** Applicable to user given consumer financial services context and ECOA / FCRA applicability.

## Informational items

- **March 2026 FTC enforcement action against [Company]:** monitoring this case (settlement details, ongoing monitoring requirements) could provide insight into FTC's algorithmic enforcement methodology.
- **June 2025 FTC staff report on algorithmic decision-making:** referenced in the alert and informs the FTC's principles. Worth obtaining for the legal team's reference file.
- **State attorneys general interest:** California and New York are mentioned as showing similar interest. State-level enforcement is also possible.
- **CFPB related guidance:** CFPB has issued related guidance on algorithmic decision-making in consumer financial contexts. Particularly relevant to the user given consumer financial services context. Obtain for compliance file.
- **EU AI Act trend:** mentioned as international context; not directly applicable to US-only operations.

## Items where applicability is unclear

None — all items are applicable given the user's organization context.

## Items not applicable to user's organization

None.

## Source references and follow-ups

- **Underlying authorities:** Section 5 of the FTC Act, ECOA, FCRA — all already applicable to user.
- **Cited materials:**
  - March 2026 FTC enforcement action against [Company] — obtain settlement details for compliance file.
  - April 2026 FTC Chair remarks — obtain text for context.
  - June 2025 FTC staff report on algorithmic decision-making — obtain for reference.
  - CFPB algorithmic decision-making guidance — obtain for compliance file.
- **Suggested follow-ups:**
  - Schedule periodic monitoring of FTC enforcement actions in algorithmic decision-making.
  - Consider engaging outside counsel for assessment of model fairness documentation if internal review identifies gaps.
  - Review whether existing model risk management framework (if any) needs enhancement to address algorithmic-specific FTC concerns.

## Notes on this extraction

The alert is informational rather than actionable. It describes an enforcement priority shift, not a new legal requirement. The "recommended action items" extracted are responses to the prudential concerns raised in the alert; they are recommended for risk management purposes but are not legally required by this alert.

If the user is looking for a new compliance roadmap, this alert does not provide one. The FTC has not issued new rules; existing FTC Act, ECOA, and FCRA obligations continue to apply. For substantive compliance assessment of the user's ML credit decisioning systems against existing law, the user should consider a separate engagement with regulatory counsel — this alert is a signal that such an engagement may be increasingly important, not a substitute for it.

---

## What this example demonstrates

- **Vague alerts produce brief reports.** No mandatory action items extracted; the report is shorter than for a regulation-implementing alert. The skill does not pad with speculation.
- **Recommended action items are differentiated from mandatory.** All four items in the report are recommended (best practice in light of FTC enforcement focus); none are legally required by this alert. The structural distinction matters for the user's prioritization.
- **Context summary is candid about the alert's nature.** "The FTC has not announced new rules; the alert is reporting an enforcement-priority shift" — this honesty helps the user calibrate how to respond. A user who expected a new compliance deadline now knows there isn't one.
- **Notes on extraction explicitly states "informational rather than actionable."** This is important — vague alerts can be misleading if treated as if they impose requirements. The skill is honest about what extraction produced.
- **Recommendation to engage regulatory counsel is appropriate.** When the alert is a signal rather than a roadmap, the right next step is often expert legal analysis tailored to the user's specific operations. The skill recommends this rather than fabricating a detailed roadmap from limited source content.
- **Informational items capture useful context without inflating to actions.** Five informational bullets describe related developments; none are converted to actions because the alert doesn't support that.
- **Source references include both legal authority and adjacent materials.** The cited materials (enforcement action, staff report, Chair remarks, CFPB guidance) are flagged for compliance file building — useful operational guidance even when the alert itself doesn't impose deadlines.
