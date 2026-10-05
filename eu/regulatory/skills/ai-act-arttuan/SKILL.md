---
name: ai-act-arttuan
title: AI Act
description: Classify the AI system, settle whether you are provider or deployer, and emit the obligations that follow — prohibitions first, then high-risk, then transparency
author: ArttuAn
author_url: https://github.com/ArttuAn/eu-compliance-skills/tree/main/skills/ai-act
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: eu
practice: regulatory
language: en
---

# AI Act

Classification decides everything, and it decides it in an order most teams get
backwards. The sequence is: **prohibited first, then role, then risk tier, then
duties.** A team that starts at "what documentation do we need for a high-risk
system" has skipped the two questions that could have ended the project or moved
the entire obligation set onto someone else.

> **Not legal advice.** Classification under the AI Act is a legal judgement with
> a €35M ceiling attached. This skill produces the facts, the candidate
> classification and the citation — counsel confirms it before you build.

```
  1. Art. 5   prohibited practice?  ──yes──► BLOCKER. No compliant version exists.
        │ no
  2. role     provider · deployer · importer · distributor
        │            (Art. 25 can turn a deployer into a provider)
  3. tier     Annex I / Annex III high-risk?  ──► Art. 6(3) derogation available?
        │                                          (not if it profiles people)
  4. duties   Chapter III if high-risk · Art. 50 transparency at EVERY tier
        │     · Art. 4 AI literacy · Chapter V if you provide a GPAI model
        ▼
  findings + technical documentation plan
```

## Use this when

- Anything in the product uses machine learning, an LLM, or an automated rule
  that produces an output about a person — before it is wired in.
- You are integrating a third-party model or API and need to know whether you
  are a deployer (light duties) or have become a provider (heavy ones).
- You are about to rebrand, fine-tune, or repurpose someone else's system —
  Art. 25 is the article that catches people here.
- Someone has claimed "it is not high-risk" and you need that claim written down
  with a reason, which is what Art. 6(3) requires anyway.

**Do not use this when** there is no AI system and no automated decision — but
verify that against the code, and note that **GDPR Art. 22 applies to automated
decisions whether or not they are AI**. A hand-written rules engine that rejects
loan applications engages Art. 22 and not the AI Act.

## Ask first

Five questions, in engineering terms. Never ask "is this a high-risk AI system".

1. **"What decision does the output change, and what happens to the person if it
   is wrong?"**
   The classification question. Everything downstream follows from the answer.
2. **"Does it infer, score, rank or categorise individual people?"**
   If yes, the Art. 6(3) derogation from high-risk is unavailable — this is the
   single most consequential answer in the skill.
3. **"Do you train it, fine-tune it, or call someone else's API? Do you put your
   name on the product it ships in?"**
   Provider vs deployer, and the Art. 25 trap.
4. **"Is it used in recruitment or worker management; education or exam scoring;
   credit or insurance; access to public benefits or essential services; law
   enforcement; migration or borders; justice; critical infrastructure safety; or
   biometrics?"**
   Annex III, read out as a list.
5. **"Does it recognise emotions, categorise people by biometric data, scrape
   faces, score social behaviour, or exploit a vulnerability of a specific
   group?"**
   Art. 5 territory. A yes here is a potential blocker and should be asked early
   enough to stop the project rather than after it is built.

And one for the humans: **"in the last hundred cases, how often did the human
reviewer go against the system, and did they see anything it did not?"** This is
how you find out whether Art. 14 oversight exists or is a rubber stamp.

## What the law requires

> **Dates move.** The AI Act's application timeline has been subject to
> amendment. Verify every date against the consolidated text on EUR-Lex before
> relying on it. See `references/legal-citations.md`.

### 1. Prohibited practices — Art. 5

No mitigation, no documentation, no conformity route. If the product depends on
one of these, there is no lawful version to build, and that is a **blocker**:

- Subliminal, manipulative or deceptive techniques that materially distort
  behaviour and cause significant harm.
- Exploiting vulnerabilities of age, disability, or a specific social or
  economic situation.
- Social scoring leading to detrimental treatment in unrelated contexts or that
  is unjustified and disproportionate.
- Predicting criminal offending based solely on profiling or personality traits.
- Untargeted scraping of facial images from the internet or CCTV to build
  recognition databases.
- Emotion inference in the workplace or in education (narrow exceptions for
  medical or safety reasons).
- Biometric categorisation to deduce race, political opinions, trade union
  membership, religious beliefs, sex life or sexual orientation.
- Real-time remote biometric identification in publicly accessible spaces for
  law enforcement, outside exhaustively listed exceptions.

Note two of these carefully: **emotion inference in the workplace** catches
"sentiment analysis on employee communications", which teams propose regularly.
And **untargeted scraping of facial images** catches a training-data pipeline,
not just a product feature.

### 2. Role — Arts. 3, 25

| Role | You are | Duties |
| --- | --- | --- |
| **Provider** | You develop it, or have it developed, and place it on the market or put it into service **under your own name or trademark** | The full set — Chapter III for high-risk |
| **Deployer** | You use it under your own authority in a professional capacity | Art. 26: use per instructions, assign competent human oversight, monitor, keep logs, inform affected people |
| **Importer / distributor** | You bring it into or make it available on the EU market | Verification duties |

**Art. 25 is the trap.** A deployer becomes a provider — inheriting the entire
provider obligation set — if they put their name or trademark on a high-risk
system, make a **substantial modification** to it, or **change its intended
purpose** so that it becomes high-risk. Wrapping a general-purpose model in your
product and selling it for a hiring use is all three at once, and it is what
most teams building on an LLM API are actually doing.

### 3. Tier

**High-risk, Annex I** — the system is a safety component of a product already
covered by EU harmonisation legislation (machinery, medical devices, toys,
lifts, vehicles).

**High-risk, Annex III** — the eight areas: biometrics; critical infrastructure;
education and vocational training; employment and worker management; access to
essential private and public services (including creditworthiness and life or
health insurance risk assessment); law enforcement; migration, asylum and border
control; administration of justice and democratic processes.

**Art. 6(3) derogation** — the provision states that an Annex III system is not
classified as high-risk where it performs a narrow procedural task, improves the result of a prior human activity, detects
decision patterns without replacing human assessment, or performs a preparatory
task — **unless it performs profiling of natural persons**, in which case the
derogation is unavailable regardless.

Relying on it is not free: the assessment must be **documented before** the
system is placed on the market, and the system must **still be registered** in
the EU database.

**Transparency tier — Art. 50** — applies at *every* tier including minimal:
tell people they are interacting with an AI system; mark synthetic audio, image,
video and text in a machine-readable way; disclose emotion recognition and
biometric categorisation to the people exposed to it; label deepfakes.

Teams building an ordinary chatbot skip this because they concluded they were
"minimal risk". Art. 50 still applies.

### 4. Chapter III duties, if high-risk

| Duty | Citation | The engineering shape |
| --- | --- | --- |
| Risk management system | Art. 9 | Continuous and iterative across the lifecycle — not a document |
| Data governance | Art. 10 | Provenance, representativeness, bias examination of training/validation/test sets |
| Technical documentation | Art. 11 + Annex IV | Written as you build; unreconstructable afterwards |
| Record-keeping | Art. 12 | Automatic logs over the system's lifetime. **A build-time design decision.** |
| Transparency to deployers | Art. 13 | Instructions for use: capabilities, limitations, expected accuracy |
| Human oversight | Art. 14 | Designed in, and evidenced. A claim with no evidence is a finding |
| Accuracy, robustness, cybersecurity | Art. 15 | Declared accuracy metrics; resilience to adversarial input and data poisoning |
| Quality management system | Art. 17 | Organisational |
| Conformity assessment, CE marking, EU declaration | Arts. 43, 47, 48 | |
| Registration in the EU database | Art. 49 | Including where Art. 6(3) is relied on |
| Deployer FRIA | Art. 27 | Public bodies, entities providing public services, and creditworthiness or life/health insurance risk assessment |

### 5. GPAI — Chapter V

If you provide a general-purpose AI model: technical documentation, information
for downstream providers, a copyright policy including a text-and-data-mining
reservation mechanism, and a sufficiently detailed public summary of training
content. Models meeting the systemic-risk threshold carry additional evaluation,
adversarial testing, incident reporting and cybersecurity duties.

Most teams are **downstream** of a GPAI model, not providers of one. But the
downstream position has a consequence worth recording: you depend on the
upstream provider's documentation to discharge your own Art. 10 and Art. 13
duties, and if they will not give it to you, that is a finding about a vendor,
not a gap in your paperwork.

## What to produce

**1. The classification, in `compliance.yaml`**, with the reasoning attached:

```yaml
ai:
  systems:
    - name: "applicant-ranker"
      role: provider                      # Art. 25 analysis recorded below
      role_reasoning: >
        Deployer of gpt-4o, but the product is sold under our trademark and the
        intended purpose is recruitment. Art. 25(1)(a) and (c) both engaged.
      prohibited_check: {result: none_identified, questions: [B-05]}
      annex_iii_candidate: "III(4)(a) recruitment and selection"
      profiles_natural_persons: true
      art_6_3_available: false
      art_6_3_reasoning: "profiling - third subparagraph of Art. 6(3) excludes the derogation"
      art_22_gdpr_in_play: true
      art_50_duties: ["disclose AI interaction", "mark generated screening notes"]
      classification_confirmed_by: null   # counsel; gate cannot clear without it
      source: {kind: answered, question: B-04}
```

**2. Findings, with the right severity.** Prohibited practice is a `blocker`.
An unconfirmed Annex III candidate is a `condition` with counsel as the owner.
A missing Art. 50 disclosure is a `condition` with a one-line fix.

**3. The Annex IV technical documentation skeleton**, created now, filled as you
build — `compliance/ai/technical-documentation.md` with a section per Annex IV
heading and `[to be completed: …]` markers that CI can count.

**4. Logging designed in, not bolted on.** Art. 12 requires automatic recording
of events over the lifetime. Decide at build time what an event is, what goes in
it, how long it is kept, and how it reconciles with GDPR minimisation — because
those two pull in opposite directions and the resolution belongs in the design,
not in an argument later.

**5. Oversight you can evidence.** Instrument the override rate. "A recruiter
reviews the top ten" is a claim; "the reviewer overrode the ranking in 14 of the
last 100 cases, and the interface surfaces the three features that drove the
score" is a control.

**Every assessment carries a certainty.** Each finding, each applicable or
ruled-out regime, and the headline of the brief carry `certainty` (0–100) — the
honest percent of the assessment that rests on verified sources and confirmed
facts rather than inference, open unknowns and interpretation. Wherever you
state an applicability, a classification, a citation-backed obligation or a
finding, show the percentage **and the single largest reason it is not higher**:
"ruled out NIS2 — certainty 66%: the national transposition was not read".
`references/certainty.md` holds the anchors; the rules that matter here: an
answer graded `UNKNOWN` caps anything resting on it at 70, an unread Directive
transposition caps at 60, a classification pending counsel caps at 50, and a
`100` requires every deciding fact SPECIFIC, every citation verified on EUR-Lex,
every transposition read and every regime screened. Certainty is visibility, not
a free pass — VAGUE stays rejected, an open blocker stays blocked.

## Failure modes

- **Starting at documentation.** The team builds a technical documentation file
  for a system that turns out to rely on a prohibited practice, or for which
  they are not the provider. Prohibitions first, role second.

- **Missing Art. 25.** "We just call an API" while shipping it under your own
  brand for a high-risk purpose. You are the provider, with the full Chapter III
  set, and nobody noticed.

- **Claiming Art. 6(3) while profiling.** The most common misuse. Scoring,
  ranking or categorising individuals is profiling, and the derogation is
  unavailable however advisory the output is.

- **Relying on Art. 6(3) without documenting it.** An undocumented conclusion is
  not a derogation. And registration is still required.

- **Skipping Art. 50 because the system is minimal risk.** Transparency duties
  are tier-independent. The chatbot still has to say it is a chatbot.

- **Rubber-stamp human oversight.** A reviewer who approves everything, sees no
  explanation, and has no time budget is not oversight under Art. 14. The
  override-rate question exposes it in one number.

- **Treating Art. 10 as a lawful basis.** Data governance duties under the AI
  Act do not authorise the processing. You need Art. 6 GDPR as well, separately,
  and for the training purpose specifically.

- **Forgetting Art. 22 GDPR.** It applies to solely automated decisions with
  legal or similarly significant effects whether or not there is any AI, and it
  carries its own rights: human intervention, the ability to contest, an
  explanation.

- **Asserting a date from memory.** The timeline has moved before. Cite and
  verify, or say you could not.

## Verify

Follow `references/verification.md`. For this skill specifically:

1. **Tier 0** — install, `--help`, classify a fixture system and emit duties.

2. **Tier 1** — `pytest -q`, offline:

```python
def test_prohibited_practice_is_a_blocker():
    finding = classify(system(emotion_inference_at_work=True)).findings[0]
    assert finding.severity == "blocker"
    assert finding.citation.startswith("Art. 5")
    assert "no compliant version" in finding.statement.lower()


def test_prohibited_check_runs_before_tier():
    trace = classify(system(emotion_inference_at_work=True, annex_iii="4(a)")).trace
    assert trace.index("art_5") < trace.index("tier")


def test_profiling_blocks_the_derogation():
    result = classify(system(annex_iii="4(a)", profiles_natural_persons=True,
                             derogation_ground="preparatory task"))
    assert result.art_6_3_available is False
    assert "profiling" in result.art_6_3_reasoning


def test_derogation_still_requires_registration():
    duties = classify(system(annex_iii="4(a)", profiles_natural_persons=False,
                             derogation_ground="narrow procedural task")).duties
    assert "Art. 49" in duties
    assert "documented assessment" in " ".join(duties).lower()


def test_rebranding_turns_a_deployer_into_a_provider():
    result = classify(system(calls_third_party_api=True, own_trademark=True,
                             annex_iii="4(a)"))
    assert result.role == "provider"
    assert "Art. 25" in result.role_reasoning


def test_repurposing_to_high_risk_turns_a_deployer_into_a_provider():
    result = classify(system(calls_third_party_api=True, own_trademark=False,
                             changed_intended_purpose_to="4(a)"))
    assert result.role == "provider"


def test_art_50_applies_at_minimal_risk():
    duties = classify(system(chatbot=True, annex_iii=None)).duties
    assert any("Art. 50" in d for d in duties)


def test_high_risk_emits_the_full_chapter_iii_set():
    duties = classify(system(annex_iii="4(a)", profiles_natural_persons=True)).duties
    for article in ("Art. 9", "Art. 10", "Art. 11", "Art. 12", "Art. 13",
                    "Art. 14", "Art. 15", "Art. 17", "Art. 49"):
        assert any(article in d for d in duties)


def test_deployer_gets_art_26_not_chapter_iii():
    duties = classify(system(calls_third_party_api=True, own_trademark=False,
                             annex_iii="4(a)")).duties
    assert any("Art. 26" in d for d in duties)
    assert not any("Art. 11" in d for d in duties)


def test_art_22_gdpr_flagged_without_any_ai():
    result = classify(system(uses_ai=False, solely_automated_legal_effect=True))
    assert result.art_22_gdpr_in_play is True
    assert result.tier == "not an AI system"


def test_art_10_is_not_treated_as_a_lawful_basis(brief):
    finding = classify_into(brief).finding_for("training data")
    assert "Art. 6 GDPR" in finding.needs


def test_annex_iv_skeleton_has_every_heading():
    doc = annex_iv_skeleton()
    assert len(doc.sections) >= 9
    assert doc.incomplete_markers() > 0     # honest about what is unwritten


def test_no_classification_is_asserted_as_final(brief):
    text = render(classify_into(brief)).lower()
    assert "is not high-risk" not in text
    assert "is a high-risk ai system" not in text
    assert "candidate" in text or "must be confirmed" in text


def test_every_date_carries_a_citation_or_a_verify_note():
    for date_line in dates_in(render(classify_into(brief))):
        assert ("Art." in date_line) or ("verify" in date_line.lower())
```

3. **Tier 2** — report: prohibited practices screened and the result, the role
   with its Art. 25 reasoning, the Annex III candidate, whether Art. 6(3) was
   claimed and why it is or is not available, and the count of unfilled Annex IV
   sections. That last number is your honest distance from a technical
   documentation file.

4. **Tier 3** — counsel confirms the classification and the role. Nothing else
   in this skill is worth much until those two are settled, and they are exactly
   the two an hour of legal time can settle if you bring the brief.

Then tell the user what ran, and say plainly which dates you could not verify
and that the classification is a candidate until confirmed.
