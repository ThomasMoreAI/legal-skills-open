# redfern-schedule

Build and maintain a **Redfern Schedule** (the request-to-produce table used to organise document production in international arbitration) for the **requesting party**, the **producing party**, or the **tribunal**, from one shared artefact.

Author: **Alexios vdSK**, Member, LegalQuants. Jurisdiction: regime-aware (multi).

## When to use

- Draft requests to produce and run them against the IBA Rules (2020) Article 3.3 admissibility test.
- Respond to the other side's requests by mapping objections to the Article 9.2 grounds.
- Reply to objections entered against your requests.
- Prepare a clean, decision-ready schedule for the tribunal.
- Merge a returned schedule from the other side without losing column discipline.

Do **not** use it for court-disclosure litigation (CPR / US discovery), for a full document review over a corpus, or to predict whether an objection will win. It enforces form and flags weakness, and the legal calls stay with counsel.

## How it works

1. **Privilege gate.** It opens with a hard confidentiality warning and will not read schedule content until you confirm.
2. **Intake.** It asks for role, regime, round, whether any party is a State or state-owned, and the pleaded-issues list.
3. **Pipeline.** It runs each request through Article 3.3 (Gate A identification, Gate B relevance and materiality, Gate C possession), maps objections to Article 9.2, and surfaces a content-based Article 9.2(f) sensitivity prompt for State or state-owned parties (by what a document is, not by who owns the party).
4. **Output.** A Markdown schedule table plus an internal flags memo naming your own weak requests or non-colourable objections. The memo is privileged and never served.

Regimes supported: IBA 2020 (default), Prague 2018, ICC, LCIA, ICSID. See `reference/regimes.md`.

## Files

- `SKILL.md`: the skill.
- `reference/`: the Article 3.3 checklist, the Article 9.2 objection map, the regime guide, the schedule format and ID rules, the intake script, a separable issue matcher, and `CITATIONS.md` (every legal citation byte-verified against its official source).
- `examples/`: worked examples for the requesting, producing, and tribunal roles on one shared fact pattern (`gold-fact-pattern.md`).

## Limitations

- Output is a Markdown table. It does not generate Word or Excel files.
- It does not decide materiality or whether an objection will succeed, and it does not give enforceability or privilege opinions.
- It does not invent facts, issues, or citations beyond your inputs and the reference files.
- It is not a substitute for review by qualified arbitration counsel.

## Quality assurance

This skill went through four independent gates plus a live functional test. Each is summarised below.

### 1. Citation provenance (byte-verified)

Every legal citation is checked against its official source and logged in `reference/CITATIONS.md` with the deterministic method: download the official artifact, extract its text, and match each cited number and phrase against the literal text. Sources: IBA Rules on the Taking of Evidence 2020, Prague Rules 2018, ICC Rules 2021 and 2026, LCIA Rules 2020, ICSID Arbitration Rules 2022, CIArb Guideline on the Use of AI in Arbitration 2025.

### 2. Adversarial citation review

Two independent passes re-verified every citation against the live official sources (not the skill's own ledger), with skeptic refutation of every finding. Defects found were fixed (for example, the ICSID Rule 37 heading and operative verb were corrected against the binding text). The four freshness fields are declared in the frontmatter so a reader can see when the bundled law was last verified.

### 3. claude-for-legal skills-qa

Run past Anthropic's `claude-for-legal` **skills-qa** framework: the thirteen-parameter Legal Skill Design Framework, the prompt-injection heuristic scan, and the three legal failure modes. Result: trust surface clean (prompt-only, no hooks, no MCP, no network, no out-of-directory writes), all three legal failure modes addressed (legal advice versus support, privilege, accountability gap), and the freshness and design findings applied. Verdict: ready.

### 4. Anthropic skill-creator QC (design plus empirical evals)

Run past Anthropic's `skill-creator` guide. Two parts:

- **Design review** against the anatomy, progressive-disclosure, lack-of-surprise, and writing-pattern principles. The skill is prompt-only with a concise instruction file and reference material loaded on demand. The description was made more explicit so the skill triggers on document-production requests even when the user does not say the words "Redfern Schedule".
- **Empirical evals.** Four bundled test cases (`evals/evals.json`) covering the requesting, producing, and tribunal roles plus an out-of-scope litigation request, each run with the skill and against a clean no-skill baseline, graded on objective assertions. With the skill, every assertion passed across all four cases. Against the clean baseline the skill added clear value on the high-stakes behaviours: it fires the privilege gate first (the baseline skipped it), it leaves the tribunal's decision blank and proposes nothing (the baseline went ahead and ruled), it produces a discrete privileged flags memo of the user's own weak points, it pairs objections with Article 9.5 protective measures rather than flat refusals, and it declines to invent a relevance case the user did not plead.

### 5. Live functional test

Run end to end on a real chat platform across all three roles on a fictional investor-State dispute: the privilege gate fires first, weak requests are correctly flagged (a fishing-expedition sweep fails Article 3.3, a document the requesting party already holds is flagged under Gate C, a non-party document is routed to Article 3.9), and the Article 9.2(f) prompt fires only on genuinely governmental content, not on a state-owned party's ordinary commercial documents.
