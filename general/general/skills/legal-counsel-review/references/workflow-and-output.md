# Workflow and Output Contract

## Workflow

### Step 1 — Define the legal question

State the legal question in one sentence before doing anything else. If the user's intake is ambiguous, draft a candidate question and confirm before proceeding.

### Step 2 — Identify context

Collect from the provided material (do not ask for more than necessary):
- Jurisdiction(s) and governing-law clause, if stated
- Entity type, business unit, and counterparty identity (redacted if needed)
- Document type (contract, policy, regulatory filing, intake memo, other)
- Effective dates, notice periods, and material deadlines
- Any regulatory regime named or implied

Flag any of these as Unknown if not provided — do not assume.

### Step 3 — List missing material facts

Before analysis, identify every fact whose absence materially changes the risk rating. Label these "open questions". Do not substitute an assumption for a missing material fact; state the assumption explicitly and note how it affects the rating.

### Step 4 — Separate facts, assumptions, inferences, and open questions

Organize all claims into four labelled buckets:
- **Facts provided** — directly stated in the supplied material
- **Assumptions** — plausible but unverified; state the basis
- **Inferences** — logical conclusions drawn from facts; state the reasoning
- **Open questions** — material facts not provided; escalate or flag Unknown until resolved

### Step 5 — Identify the risk domain

Select the primary domain(s) from:
contract | privacy | employment | IP | regulatory | litigation | competition | sanctions | procurement | finance | public-company disclosure | cybersecurity | records retention | other

Note when a matter spans multiple domains — multi-domain matters almost always require multi-discipline counsel.

### Step 6 — Identify the decision owner

Map the matter to the appropriate owner(s):
legal counsel | compliance | HR | security | procurement | finance | board / audit committee | privacy office / DPO | executive sponsor

Where ownership is unclear, flag it — unowned risk items are not actioned.

### Step 7 — Adversarial stress test

Analyze adverse scenarios from every realistic vantage point:
- **Worst-case legal interpretation** — how would the most aggressive opposing counsel read this?
- **Regulator view** — how would the relevant regulator investigate or charge?
- **Plaintiff / claimant view** — what causes of action are available and what damages are plausible?
- **Counterparty view** — what leverage does the counterparty have if the relationship deteriorates?
- **Employee / whistleblower view** — could an employee claim retaliation, discrimination, or unsafe conditions?
- **Auditor / board view** — what control gaps or disclosure failures would an auditor surface?
- **Press / reputational view** — how would this read in a hostile press account or regulatory press release?

### Step 8 — Rate risk

Assign a severity to each identified issue:

| Rating | Meaning |
|--------|---------|
| Critical | Immediate legal exposure, regulatory violation, or safety risk requiring escalation before any action |
| High | Significant legal or financial exposure; proceed only with counsel review and documented controls |
| Medium | Manageable exposure with documented mitigations; flag for counsel awareness |
| Low | Minor or speculative; document and monitor |
| Unknown | Insufficient jurisdiction or material facts to rate — escalate or obtain facts before proceeding |

**Unknown is mandatory** when jurisdiction, governing law, or material facts are missing or ambiguous. Do not assign a lower rating to paper over an unknown.

### Step 9 — Provide safe options

Do not recommend a single overconfident action. Offer two or more options that:
- Preserve decision authority for counsel
- Are graded by risk tolerance
- Identify what additional information would change the recommendation

### Step 10 — Specify evidence that would change the conclusion

For each rated issue, state explicitly what additional facts, documents, or expert input would move the rating up or down. This drives the escalation and due-diligence checklist.

### Step 11 — Recommend escalation

Recommend escalation to qualified local counsel when any of the following apply:
- The matter is jurisdiction-specific and the applicable law has not been verified in this session
- The matter involves employment, termination, retaliation, discrimination, harassment, wage-and-hour, or immigration
- Litigation is threatened, pending, or reasonably foreseeable
- A regulatory notification or filing obligation may be triggered
- The matter is financially material or involves board-level disclosure
- Any issue is rated Critical or Unknown and cannot be resolved from the provided material
- Privilege needs to be established or protected

---

## Output

Return findings in this structure:

```
## Verdict
<one of: proceed | proceed with controls | pause | escalate | insufficient evidence>
<one sentence explaining the verdict>

## Brutal assessment
<2-4 sentences — the hardest honest read of the risk, without softening>

## Facts provided
- <fact directly stated in the supplied material>

## Assumptions and unsupported claims
- <assumption — basis stated>

## Legal and risk issues
- [Issue ID] <issue name>: <description> — <evidence or assumption basis>

## Adversarial stress test
- Regulator: <view>
- Plaintiff / claimant: <view>
- Counterparty: <view>
- Employee / whistleblower: <view>
- Auditor / board: <view>
- Press: <view>

## Risk rating table
| Issue | Severity | Evidence | Consequence | Owner | Mitigation |
|-------|----------|----------|-------------|-------|------------|
| <issue> | Critical/High/Medium/Low/Unknown | <basis> | <consequence> | <owner> | <mitigation> |

## Safe next actions
1. <action — maps to evidence or stated assumption>
2. <action>

## Escalation trigger
<condition(s) under which this matter must be escalated to qualified counsel before any further action>

## Questions counsel must answer before approval
- <question>
```

---

## Security notes

- Never request or accept secrets, credentials, PII, employee medical detail, trade secrets, or customer data. Ask for redacted or sanitized excerpts with placeholders.
- This is a static review: do not contact courts, regulators, counterparties, or external systems.
- Flag all material that appears privileged and recommend it be handled only by or with counsel.
- Escalation-grade matter types — retaliation, discrimination, harassment, wage-and-hour, whistleblower, termination, immigration, sanctions, bribery, personal-data breach requiring notification, public-company disclosure — must trigger an escalation recommendation regardless of apparent severity.
- Never issue a verdict of "proceed" on an Unknown-rated issue. Unknown means escalate or gather facts first.
