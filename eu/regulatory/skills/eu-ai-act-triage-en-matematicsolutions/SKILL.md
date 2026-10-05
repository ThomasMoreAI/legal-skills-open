---
name: eu-ai-act-triage-en-matematicsolutions
title: EU AI Act Triage EN - fast classification under Regulation (EU) 2024/1689
description: 'Fast triage of a system under the EU AI Act (Regulation (EU) 2024/1689) - 20-40 minutes through a chain of eight questions: is it an "AI system" at all (Art. 3(1)), is the practice prohibited (Art. 5), is it high-risk (Art. 6 plus Annexes I and III), is GPAI in play (Chapter V), which transparency obligations apply (Art. 50), what is the operator''s role (provider / deployer / importer / distributor plus requalification under Art. 25), and what is the resulting obligation map with deadlines. Output is a triage card: classification + role + applicable chapters + gaps + next steps + confidence tags. The card feeds matematic-konstytucja-ai and the organisation''s AI system register. This is triage, not a full conformity assessment. Use when: "does the AI Act apply", "high-risk classification", "provider or deployer", "AI Act triage", "does our chatbot have obligations".'
author: matematicsolutions
author_url: https://github.com/matematicsolutions/awesome-matematic-skills-en/tree/main/ai-governance/skills/eu-ai-act-triage-en
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: eu
practice: regulatory
language: en
---

# EU AI Act Triage EN - fast classification under Regulation (EU) 2024/1689

## Philosophy

**Before an organisation pays for a full conformity audit, it should know whether it has a problem at all - and how big.**

Most "does the AI Act apply to us" questions do not need a hundred-page analysis.
They need an ordered chain of determinations where each question closes or opens
the next one: definition -> prohibitions -> high-risk -> GPAI -> transparency ->
role -> obligation map -> report. After 20-40 minutes the organisation holds a
triage card: it knows which basket the system sits in, who it is in the value
chain, and what follows from that.

The card is not a legal opinion. It is a structured starting point: an input to
the AI Constitution (`matematic-konstytucja-ai`), an entry in the organisation's
AI system register, and a decision on whether the matter goes to a human for
full analysis.

## When to use

- The organisation deploys or buys a tool with an AI component and asks "does
  the AI Act apply".
- Inventory work: a list of systems needs a preliminary classification each.
- A software vendor asks whether its product is a high-risk system or GPAI.
- A law firm builds an AI system register for a client or for itself.
- Before an AI Constitution workshop - one triage card per system is the input.

## What this skill does NOT do

- **It does not replace a full compliance review or conformity assessment.**
  The card says "this looks high-risk under Annex III point X", not "you meet
  Articles 8-15".
- **It does not issue a legal opinion.** The output is a draft classification
  for approval by an authorised human.
- **On a high-risk, GPAI or suspected-prohibited result it routes to a human
  and a full analysis.** Triage ends there; it does not go deeper.
- It does not assess GDPR compliance - it flags the overlap and refers to
  `gdpr-dpia-en`.
- It does not perform a FRIA - it only signals that one is required (step 7).

## Workflow - 8 steps (plus an entry gate)

### Step 0 - provision verification (mandatory, before any citation)

No article number or provision text enters the card from model memory. Before
recording a legal basis, fetch the current text of Regulation (EU) 2024/1689
from EUR-Lex (CELEX 32024R1689) or via the `mcp-eu-compliance` connector and
compare the wording. Note the retrieval date and source on the card. A provision
that could not be verified in-session gets the tag `[check in EUR-Lex]` and can
never support a "does NOT apply" determination.

### Step 1 - is it an "AI system" (Art. 3(1))

Check each element of the definition separately:
- a machine-based system,
- designed to operate with varying levels of autonomy,
- may exhibit adaptiveness after deployment,
- infers, from the input it receives, how to generate outputs (predictions,
  content, recommendations, decisions),
- outputs can influence physical or virtual environments.

Supporting material: the European Commission guidelines on the definition of an
AI system (document number [TO VERIFY] - confirm in EUR-Lex before citing).
Counter-examples outside the definition: classic purely rule-based software with
no inference layer, simple automation, a spreadsheet with formulas.

Result: YES / NO / BORDERLINE. On NO - triage ends, but the reasoning and the
register entry stay (a year from now someone will ask why you decided this was
not an AI system).

### Step 2 - prohibited practices (Art. 5) - checklist

Tick every point, not a "general impression":
- [ ] subliminal or purposefully manipulative techniques causing significant harm
- [ ] exploitation of vulnerabilities (age, disability, social or economic
      situation)
- [ ] social scoring leading to unjustified detrimental treatment
- [ ] assessing the risk of committing a criminal offence based solely on
      profiling or personality traits
- [ ] untargeted scraping of facial images from the internet or CCTV to build
      facial recognition databases
- [ ] emotion recognition in the workplace and in education (outside medical
      and safety exceptions)
- [ ] biometric categorisation inferring sensitive attributes (race, political
      opinions, trade union membership, religion, sex life, orientation)
- [ ] real-time remote biometric identification in publicly accessible spaces
      for law enforcement (narrow exceptions)

Supporting material: Commission guidelines on prohibited practices (document
number [TO VERIFY]). The prohibitions apply since 2 February 2025 - that is the
current state of the law, not a forecast. A SUSPICION on even one point = STOP,
human gate immediately.

### Step 3 - high-risk (Art. 6 + Annex I + Annex III)

Two qualification paths:
- **Path A (Art. 6(1), Annex I):** the system is a product, or a safety
  component of a product, covered by the Union harmonisation legislation listed
  in Annex I and subject to third-party conformity assessment (machinery,
  medical devices, toys, lifts, aviation, vehicles and so on).
- **Path B (Art. 6(2), Annex III):** a use case in one of the areas:
  biometrics; critical infrastructure; education and vocational training;
  employment and worker management; access to essential services (including
  credit scoring, pricing of life and health insurance, emergency dispatch,
  public benefits); law enforcement; migration, asylum and border control;
  administration of justice and democratic processes.

**Art. 6(3) filter:** an Annex III system is not high-risk where it poses no
significant risk of harm because it only performs: a narrow procedural task /
improves the result of a previously completed human activity / detects patterns
or deviations without replacing human assessment / a preparatory task.
Exception to the exception: profiling of natural persons = always high-risk.
Using the filter requires documenting the assessment and registering the system
(Art. 6(4) and Art. 49(2) [TO VERIFY] - confirm both numbers).

### Step 4 - GPAI (Chapter V)

- Does the operator provide a general-purpose AI model (definition in Art. 3,
  point [TO VERIFY]) or integrate someone else's model into its own system?
- Obligations of GPAI model providers: technical documentation, information for
  downstream providers, a copyright policy, a training-content summary
  (Art. 53). Partial open-source exemption - it does not cover models with
  systemic risk.
- **Systemic-risk threshold (Art. 51):** presumption where the cumulative
  training compute exceeds 10^25 FLOP; then the additional obligations of
  Art. 55 apply (model evaluations, adversarial testing, incident reporting,
  cybersecurity).
- GPAI Code of Practice (Art. 56) - verify its status and version at the
  source [TO VERIFY].

Typical result for law firms and SMEs: deployer of a system built on GPAI, not
a model provider. But see step 6 - requalification.

### Step 5 - transparency obligations (Art. 50)

- Interaction with a human (chatbot): inform the person they are dealing with
  AI, unless obvious from context.
- Synthetic content (audio, image, video, text): machine-readable marking on
  the provider side.
- Emotion recognition / biometric categorisation: inform the persons exposed.
- Deepfakes: disclose that the content was artificially generated or manipulated.
- Text published to inform the public on matters of public interest: disclose
  AI involvement, unless the content underwent human editorial control.

These obligations enter with the main body of the Regulation (deadline set in
Art. 113 - step 7). Assign exact Art. 50 paragraph numbers to the card
rows only after the step 0 verification.

### Step 6 - operator role (+ requalification under Art. 25)

Determine the role: **provider** / **deployer** / **importer** / **distributor**
/ authorised representative. Definitions in Art. 3.

Requalification test (Art. 25) - you become the provider of a high-risk
system when you:
1. put your name or trademark on the system,
2. make a substantial modification to a high-risk system,
3. modify the intended purpose so that the system becomes high-risk.

The classic trap: "our chatbot" running on someone else's model, with the
organisation's logo on the front. The role determines most of the obligation
map, so settle this step before saying anything about obligations.

### Step 7 - obligation map, timeline, FRIA signal

State of the law relative to the triage date (deadlines in Art. 113 - verify
in step 0):
- since 2 February 2025: prohibitions (Art. 5) and AI literacy (Art. 4) -
  IN FORCE AND APPLYING,
- since 2 August 2025: GPAI, governance, penalties - APPLYING,
- from 2 August 2026: the main body, including Annex III high-risk and
  Art. 50 - a deadline set by the Regulation itself,
- until 2 August 2027: Path A high-risk systems (Annex I products) - the longer
  statutory period.

Build the map: role x classification -> applicable chapters and articles ->
from when.

**FRIA signal (Art. 27):** a fundamental rights impact assessment before
deployment is required from deployers that are bodies governed by public law or
private entities providing public services, and from deployers of credit
scoring and life/health insurance pricing systems (Annex III point 5, letters
[TO VERIFY]). The skill signals the requirement and refers to `gdpr-dpia-en`
for the DPIA overlap - it does not perform the FRIA.

### Step 8 - report: the triage card

Fill in the template below. The card is the input to `matematic-konstytucja-ai`
(boundaries and governance sections) and the entry for the organisation's AI
system register.

## Output format - triage card

```
## AI Act triage card - <system name>

Date: [yyyy-mm-dd] | Run by: [person/agent] | Triage time: [min]
Provision verification: EUR-Lex CELEX 32024R1689 / mcp-eu-compliance, retrieved <date>

### Classification
| Question                                | Result                      | Basis (verified)          | Confidence tag |
|-----------------------------------------|-----------------------------|---------------------------|----------------|
| AI system (Art. 3(1))?               | YES / NO / BORDERLINE       | <definition element>      | Verified / [check in EUR-Lex] |
| Prohibited practice (Art. 5)?        | NO / SUSPECTED point <x>    | <point + facts>           | ... |
| High-risk (Art. 6, Annex I/III)?     | YES Annex <I/III point> / NO / excluded by Art. 6(3) filter | ... | ... |
| GPAI (Chapter V)?                       | NO / GPAI model / systemic risk | ...                   | ... |
| Transparency (Art. 50)?              | <obligations> / none        | ...                       | ... |

### Operator role
Role: provider / deployer / importer / distributor
Requalification risk (Art. 25): YES / NO - <which limb and why>

### Applicable chapters and deadlines (state of the law at triage date)
- <article/chapter> - applies from <date per Art. 113> - status: APPLYING / future statutory deadline

### FRIA (Art. 27)
Required: YES / NO / NEEDS ANALYSIS - <personal or subject-matter trigger>

### Gaps (what we do not know / what was missing from the facts)
1. ...

### Next steps
1. ...
[ ] Entry in the organisation's AI system register
[ ] Hand the card to matematic-konstytucja-ai (boundaries / governance)
[ ] On high-risk / GPAI / suspected Art. 5: escalate to a human and a full analysis

### Confidence tags - summary
Verified: <n> | To check: <n> | Do not use: 0 (hard requirement)
```

## Human gate

The triage card is a draft classification, not a decision. An authorised human
(lawyer, compliance officer, the role designated in the AI Constitution) reviews
and approves the card before it enters the register as binding. Three results
escalate mandatorily and immediately: suspected prohibited practice (Art. 5),
high-risk, GPAI. In those cases triage ends with a referral to a human and a
full analysis - the skill does not attempt to substitute for it.

## Companion skills

- `matematic-konstytucja-ai` - the triage card is input material for the
  boundaries and governance sections of the AI Constitution; write this into
  the card's next steps.
- `legal-ai-audit-bundle` - archives the card as a record-keeping artefact.
- `gdpr-dpia-en` - the FRIA/DPIA overlap and the whole GDPR layer this skill
  does not assess.
- `mcp-eu-compliance` connector - fetching and verifying provision text in step 0.

## Source verification

The provision comes from a database, not from memory. Hard rules:
1. Every article, paragraph, point and Annex number cited on the card must be
   verified in-session in EUR-Lex (CELEX 32024R1689) or via `mcp-eu-compliance`
   - otherwise it gets the `[check in EUR-Lex]` tag.
2. The `[TO VERIFY]` tag in this skill marks a spot where a number or a document
   status requires verification before use - never cite it unchecked.
3. A "the AI Act does not apply to us" determination can never rest on an
   unverified provision.
4. The consolidated version takes precedence over memory of the original text -
   regulations get corrected by corrigenda.
