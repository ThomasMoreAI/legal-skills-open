---
name: brief-section-drafter-uk-agents
title: /brief-section-drafter
description: Draft a skeleton argument or written submissions section in house style, consistent with the case theory — every fact cited, every case checked, every argument tied to the theory. Use when the user says "draft the [section]", "write the statement of facts", "argument section on [issue]", "draft the skeleton argument", or needs a first draft of a court submission or pleading section.
author: uk-agents
author_url: https://github.com/uk-agents/uk-legal-plugins/tree/main/litigation-legal-uk/skills/brief-section-drafter
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: gb
practice: litigation
language: en
---

# /brief-section-drafter

1. Load `~/.claude/plugins/config/uk-legal-plugins/litigation-legal-uk/CLAUDE.md` → case theory, house style.
2. Follow the workflow and reference below.
3. Draft in house format/tone/citation style (OSCOLA). Consistent with theory.
4. Output: draft section. Flag every place a fact or cite needs verification.

---

# Skeleton Argument and Written Submissions Section Drafter

## Witness statements for England & Wales — PD 57AC

If the user's jurisdiction includes England & Wales and they are asking for a trial witness statement for the Business and Property Courts (or any CPR-governed proceeding where PD 57AC applies), the Practice Direction imposes strict requirements. The statement must be in the witness's own words, must not contain argument, must identify the documents the witness used to refresh their memory, and must carry the required confirmation of compliance signed by the witness and the legal representative's certificate.

**Drafting a narrative "as the witness" from a chronology, document set, or your account of the case is exactly what PD 57AC was designed to prevent.** Courts, including the Business and Property Courts, are actively sanctioning AI-assisted witness statement drafting. If you ask me to draft a witness statement in the witness's voice from case materials, I will not.

What I WILL do:
- Prepare question prompts to elicit the witness's actual recollection
- Capture and organise what the witness says (their words, not mine) in preparation for the statement
- Generate the list of documents that were put to the witness during preparation
- Run a PD 57AC compliance checklist against a draft statement the witness has already prepared
- Draft the legal representative's certificate of compliance

For witness statements in CPR proceedings outside the Business and Property Courts, PD 57AC does not apply but the same principle holds: a statement should be in the witness's own words. A statement that reads like counsel's work product is a credibility problem in cross-examination.

## Purpose

A good skeleton argument or written submissions section is consistent with the theory, cited to the record in OSCOLA format, written in house style, and checkable. This skill produces the first draft — emphasis on *draft*. Solicitor or barrister edits.

## Written or oral?

Ask before drafting: "Is this for a written submission (skeleton argument, written submissions, pleading) or oral argument (opening, closing, reply)?" They are different crafts:

- **Written:** thorough. Cover the points, develop the authority, anticipate the responses. The tribunal reads at leisure.
- **Oral (opening, closing, reply):** strategic. Pick the 3-4 points that matter most. Concede or ignore the weak ones. Lead with your strongest. A tribunal remembers the first two minutes and the last two. "Too thorough" for oral advocacy reads as unfocused. If responding to a multi-issue submission, tell the user which issues to press and which to let go — that is the draft of the strategy, not just the words.

## Record fidelity — quotes and pinpoints

Two rules that govern every citation and every quotation in advocacy drafting.

**Verbatim quotes from the record must be verbatim.** Never put quotation marks around words attributed to opposing solicitors or counsel, a witness, the court, or any record document unless you have the exact passage in front of you and can cite to it. A quote that is almost right is worse than a paraphrase — it misrepresents the record, it is sanctionable if filed, and it will be caught. When you want to characterise what someone said but cannot find the exact words:

- **Paraphrase without quotation marks**, attributing clearly: "Counsel for the claimant submitted that X `[verify against record — transcript p. __]`."
- **Mark the placeholder:** `[verify exact quote — record cite pending]`
- **Never fill the gap.** An invented quote, even one word, is a fabrication. The reviewer note must flag every `[verify exact quote]` in the output.

Before citing any passage with quotation marks, have the source open. If working from memory or a summary, no quotation marks.

**Pinpoint cites must support the whole proposition.** If the argument is "the witness said X, Y, and Z" and you are citing one pinpoint, verify the pinpoint supports X AND Y AND Z. If it only supports Z, either (a) split the cite, or (b) narrow the proposition. A cite that supports part of a claim is how a tribunal catches you stretching — the single most common way a lawyer's credibility erodes in front of a court.

## Candour about weak arguments

When the law is against you, say so. When an argument is weak — the authority cuts the other way, the facts do not support it, the inference is a stretch — do not construct a shaky argument and present it as if it were solid. Flag it:

> "This point is weak — [authority] cuts the other way. Consider whether to press it (here is how you would frame it), concede and pivot to [stronger point], or drop it. `[review — strategic call]`."

Asserting a weak argument without flagging it erodes credibility with the tribunal and creates a professional responsibility concern (solicitors and barristers owe duties of candour to the court under the SRA Code of Conduct and the BSB Handbook). The draft should make the lawyer smarter, not confident about a bad position.

## Citation extraction coverage

When this draft is cite-checked — by you, by another skill, or by a reviewer:

1. **First pass: extract.** Read the whole document and build a list of every citation — cases, statutes, practice directions, record cites, secondary authority. Report the count: "Found [N] citations."
2. **Second pass: check.** Check each one against the source. Don't sample. Don't stop when you get tired.
3. **Report coverage.** At the end: "Checked [N] of [M] citations. [K] could not be retrieved — verify manually. [J] confirmed. [I] flagged as potential miscitations. [H] flagged as misgrounded (cite exists but doesn't support the proposition)."
4. **When source text is unavailable, say "could not check," never "confirmed."**
5. **The hardest errors to catch are partial support.** A cite that backs part of a claim but not all of it.

## Echo vs repeat

Echo key framings; don't lift sentences. Consistency with prior submissions reinforces the case theory and makes the record coherent. But there is a line between echoing and repeating.

- **Echo:** use the same key terms, the same framing of the central issue, the same characterisation of the other side's theory.
- **Don't:** lift whole sentences, re-use distinctive phrasings so often the tribunal notices, or repeat the same argument verbatim without advancing it.

A reply that sounds like a re-read of the opening loses ground.

## Load context

`~/.claude/plugins/config/uk-legal-plugins/litigation-legal-uk/CLAUDE.md` → case theory, house style (citation format — OSCOLA, structure, tone, length norms).

**Conflicts gate — unbypassable.** Before drafting, check `~/.claude/plugins/config/uk-legal-plugins/litigation-legal-uk/matters/_log.yaml` for the matter slug this skill is being invoked on. If the matter is not in `_log.yaml`, refuse and route:

> "I don't see [matter slug] in the matter log. Run `/litigation-legal-uk:matter-intake` first so the conflicts check runs and the matter workspace is set up. I won't draft substantive work product on a matter that hasn't been intaken — the conflicts check is the gate."

Do not proceed on an unintaken matter. Intake is what runs conflicts, sets up `matter.md` / `history.md`, and writes the `_log.yaml` row this skill reads from.

## Workflow

### Step 1: Which section?

| Section | What it does | Inputs needed |
|---|---|---|
| Skeleton argument | Roadmap of the argument for the tribunal; pinpointed to the evidence and authorities | Case theory, key authorities, transcript/exhibit cites |
| Statement of facts | Tells the story, in our frame, cited to the record | Chronology, key docs, witness statement cites |
| Written submissions | Full argument on an issue; developed more than a skeleton | Issue, authorities, facts |
| Pleading section (particulars of claim / defence / reply) | States the case in conformity with CPR Part 16 / PD 16 | Facts, legal basis, relief |
| Conclusion / relief | Asks for the remedy | What we want |

### Step 2: Theory check

Before writing: what does this section need to accomplish for the theory?

- Statement of facts: frame the story so our theory is the natural reading.
- Skeleton argument: connect the law to the facts in a way that supports the theory.

If the section you are about to draft contradicts the theory — stop. Either the theory is wrong or the section approach is wrong. Flag it, don't paper over it.

### Step 3: Draft in house style

**Research the court's or tribunal's skeleton argument requirements, any applicable Practice Direction, and the judge's or tribunal's directions for length, formatting, citation, and filing requirements; do not rely on preferences. Cite primary sources (CPR rule number, PD para, court guide section, standing direction) in the drafting notes. Verify currency — CPR rules, practice directions, and court guides change.**

Per `~/.claude/plugins/config/uk-legal-plugins/litigation-legal-uk/CLAUDE.md`:

- **Citation format:** OSCOLA. All case citations in the form *Claimant v Defendant* [year] court report page; statute citations: Name of Act Year, s N; CPR citations: CPR r N.N or CPR PD N, para N. Match exactly — signals, pincites, and parentheticals per OSCOLA, confirmed against the applicable court guide.
- **Structure:** How does this team organise arguments? Headings that argue or headings that describe? Numbered paragraphs?
- **Tone:** Assertive ("The claimant's submission is misconceived") or measured ("The evidence does not support the claimant's position")? Match the house style.
- **Length:** per the court's or tribunal's practice directions / directions — never relying on "what this judge usually wants" when the rule is checkable.

UK skeleton arguments typically:
- Carry the heading "Skeleton argument", identify the party, the hearing, and the date
- Set out the issues in numbered paragraphs
- Cite authorities with pinpoint references and summarise the point for which each is cited
- Are lodged within the time specified by the court's directions

### Step 4: Cite everything

Every fact → record cite (witness statement paragraph, exhibit reference, transcript page).
Every legal proposition → case cite with pincite in OSCOLA.

**Marker discipline — use liberally:**
- `[VERIFY: specific factual assertion]` — anything not confirmed against the record
- `[UNCERTAIN: specific legal proposition]` — anything not confirmed against current authority
- `[CITE NEEDED: specific cite — fact/rule believed but cite not yet pinned]`

A draft with unresolved markers is not final. The markers make the verification step explicit.

**No silent supplement.** If a research query to the configured legal research tool (uk-legal MCP, BAILII, legislation.gov.uk) returns few or no results for an authority the draft needs, report what was found and stop. Do NOT fill the gap from web search or model knowledge without asking. Say: "The search returned [N] results from [tool]. Coverage appears thin for [issue / holding]. Options: (1) broaden the search query, (2) try a different research tool, (3) search the web — results will be tagged `[web search — verify]` and should be checked against a primary source before relying, or (4) leave the `[CITE NEEDED]` marker and stop here. Which would you like?"

**Source attribution.** Tag every citation in the draft with where it came from: `[uk-legal MCP]`, `[BAILII]`, `[legislation.gov.uk]`, `[gov.uk]` for citations retrieved from a legal research connector; `[web search — verify]` for web-search citations; `[model knowledge — verify]` for citations recalled from training data; `[user provided]` for citations the solicitor or barrister supplied. Citations tagged `verify` carry higher fabrication risk than tool-retrieved citations and should be checked first. Never strip or collapse the tags — they are the reviewing lawyer's fastest signal about which citations to verify first before the document is filed.

### Step 5: Output

**Before the document is filed (the consequential act — this skill drafts, but the gate runs at the filing step regardless of who triggers it):** Read `## Who's using this` in `~/.claude/plugins/config/uk-legal-plugins/litigation-legal-uk/CLAUDE.md`. If the Role is Non-lawyer:

> Filing a skeleton argument or pleading has legal consequences — it becomes the record, binds the party on arguments and facts asserted, and a solicitor's or barrister's professional obligations attach to signature and filing. Have you reviewed this with a solicitor or barrister? If yes, proceed. If no, here's a brief to bring to them:
>
> [Generate a 1-page summary: the section drafted, the theory tie-in, authorities relied on, open `[VERIFY]` / `[UNCERTAIN]` / `[CITE NEEDED]` markers unresolved, what could go wrong (factual misstatement, unsupported citation, argument outside the theory), what to ask the solicitor/barrister before filing.]
>
> If you need to find a licensed solicitor, barrister, or other authorised legal professional: the SRA (solicitors.lawsociety.org.uk) or Bar Standards Board (barstandardsboard.org.uk/find-a-barrister) for England & Wales; the Law Society of Scotland (lawscot.org.uk) for Scotland; the Law Society of Northern Ireland (lawsoc-ni.org) for Northern Ireland.

Do not treat the draft as filing-ready without an explicit yes. Drafting itself does not require the gate — filing does.

The section, in house style, with markers inline.

Preface (not in the document — a note to the reviewing solicitor/barrister):

```markdown
[WORK-PRODUCT HEADER — per plugin config ## Outputs — differs by role; see `## Who's using this`]

## Drafting Notes — [Section] — [date]

**Theory tie-in:** [How this section supports the case theory]
**Authorities relied on:** [list — all need verification against uk-legal MCP / BAILII before filing]
**Record cites to verify:** [N] flagged inline
**Open questions for counsel:** [anything the draft assumes that should be confirmed]
**Length:** [words/pages vs. court requirements]

---

**Cite check before filing.** Citations in this draft were generated by an AI model and have not been verified against a primary source. Run every case, statute, and practice direction through the uk-legal MCP, BAILII, legislation.gov.uk, or a firm research platform for accuracy, current status, and subsequent history. Misquoted or fabricated citations in court documents can result in costs sanctions and professional-discipline consequences.

**Draft only — not a filing.** Filing this section initiates (or participates in) proceedings and carries professional-responsibility obligations (SRA Code of Conduct, BSB Handbook; duties of candour to the court under CPR r 1.3 and the overriding objective). A licensed solicitor or barrister reviews, edits, and takes professional responsibility before it is filed. Do not file unreviewed.
```

## Statement of facts specifics

The statement of facts (or chronological background section in a skeleton argument) is advocacy through selection and sequence, not argument.

- Chronological unless there is a reason not to be
- **Every fact in the statement of facts must cite to the record — a witness statement paragraph, an exhibit reference, a disclosure document reference.** "Or conceded" is not a substitute for a record cite. If the fact is established by a concession or admission in correspondence or at a hearing, cite the document or transcript.
- Frame through selection: which facts lead, which get one line, which get omitted (if not necessary and not helpful)
- No argument. "The contract unambiguously required X" is argument. "The contract stated 'X' (clause 4.1)." is fact.

## Skeleton argument specifics

- Lead with the issues the court must decide
- One argument per numbered section. If it is really two arguments, it is two sections.
- Identify the legal principles concisely; the development follows
- Address the other side's best counterargument. A skeleton that ignores the obvious counter is a skeleton the tribunal does not trust.
- Cite the primary authority for each proposition; add secondary authority (academic commentary, Law Commission reports) sparingly
- Parentheticals earn their space: if a parenthetical does not add something the citation alone does not, cut it.

## What this skill does not do

- Produce a final court document. It produces a draft. Every cite needs verification, every argument needs a solicitor's or barrister's judgment.
- Decide strategy. If there are two ways to argue the issue, flag both and let counsel choose.
- Draft PD 57AC-compliant witness statements. Those must be in the witness's own words.
- File anything. Ever.
