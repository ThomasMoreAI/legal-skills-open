# Acceptance Test Plan — Skill Creator v1.0.0

## Skill summary

Meta-skill for building new skills via conversation. When attached, drives a structured conversation: what does the skill do, when should it trigger, what inputs does it need, what output format, what edge cases. Produces a complete `SKILL.md` plus optional supporting files in agentskills.io format.

## Test corpus requirements

Skill Creator's test "corpus" is a set of 5–8 skill-creation scenarios — descriptions of skills a user might want to create. Each scenario describes the skill in user-language; the test runs the Skill Creator against the scenario and verifies the output skill is well-formed.

Suggested scenarios:

- **At least 1 simple review skill** ("I want a skill that reviews termination clauses for fairness").
- **At least 1 skill with perspective branching** ("I want a skill that reviews vendor contracts from the customer's perspective").
- **At least 1 skill with optional-input design** ("I want a skill that reviews contracts and lets me specify the deal context").
- **At least 1 transformation skill** ("I want a skill that rewrites legal text in plain English for our sales team").
- **At least 1 extraction skill** ("I want a skill that extracts deadlines from regulatory bulletins").
- **At least 1 fork-an-existing-skill scenario** ("I want a version of NDA Review calibrated to our company's specific risk tolerances").
- **At least 1 ambiguous scenario** ("I want a skill that helps with contracts") — testing how the skill handles vague intent.

The scenarios are documented as `test-corpus/skill-creator/test-scenarios.md`.

## Test scenarios

### Scenario 1: Simple review skill creation

**Inputs:** A natural-language description: "I want a skill that reviews termination clauses for fairness."

**Expected output:**
- The skill engages in a structured conversation covering the six elicitation areas (what it does, when it triggers, inputs needed, output format, edge cases, examples).
- The conversation is calibrated to the M1 starter skill conventions documented in the Skill-Authoring Guide.
- The output is a complete `SKILL.md` with all required frontmatter fields, a body following the standard structure, and at least one worked example in `examples/`.
- The output is in the agentskills.io format and renders correctly when attached.

**Expected calibration:**
- The skill's questions are operational ("from whose perspective should the review be calibrated?") not abstract.
- The skill applies sensible defaults where the user doesn't specify (e.g., suggesting `perspective: customer | vendor | mutual` as optional input pattern).
- The output skill follows the conservative-posture conventions: defers enforceability, enumerates "what this skill does not do", uses severity rubric.

**Edge cases to verify:**
- The skill prompts for tags but accepts user input without imposing a fixed taxonomy.
- The skill suggests `output_format: report` for review skills (the M1 default) rather than imposing a different format.
- The skill prompts for at least one example and helps the user draft it.

**Pass criteria:**
- Structural pass: Output `SKILL.md` is well-formed (validates against the agentskills.io frontmatter schema; required sections are present in body).
- Calibration pass: The Skill-Authoring Guide reviewer confirms the output skill follows the established conventions.

### Scenario 2: Skill with perspective branching

**Inputs:** "I want a skill that reviews vendor contracts from the customer's perspective."

**Expected output:**
- The skill recognizes the perspective-branching pattern (customer / vendor / mutual).
- The skill prompts whether the perspective should be hardcoded ("only customer") or input-selectable.
- The skill structures `perspective` as an optional input following the NDA Review / MSA Review pattern if input-selectable.
- The output `SKILL.md` body addresses the perspective explicitly in the workflow and severity calibration.

**Pass criteria:** Output skill correctly implements perspective-branching pattern.

### Scenario 3: Skill with optional-input design

**Inputs:** "I want a skill that reviews contracts and lets me specify the deal context."

**Expected output:**
- The skill applies the "optional inputs change analytical depth" pattern (per Skill-Authoring Guide).
- The skill prompts what the deal context options should be (e.g., M&A diligence, vendor procurement, partnership) and how each affects analysis.
- The output `SKILL.md` documents the deal-context input as an optional input and addresses each value's impact on analysis.

**Pass criteria:** Output skill correctly implements optional-input pattern with substantive (not just cosmetic) impact.

### Scenario 4: Transformation skill creation

**Inputs:** "I want a skill that rewrites legal text in plain English for our sales team."

**Expected output:**
- The skill recognizes this is a transformation skill (similar to Comms Improver) rather than a review skill.
- The skill prompts for audience input (or reuses the `audience` pattern from Comms Improver).
- The output skill addresses preservation-of-meaning, audience calibration, and authority-preservation modes.

**Pass criteria:** Output skill follows transformation-skill conventions.

### Scenario 5: Extraction skill creation

**Inputs:** "I want a skill that extracts deadlines from regulatory bulletins."

**Expected output:**
- The skill recognizes this is an extraction skill (similar to Action Items from Client Alert).
- The skill prompts for jurisdiction filtering, output structure (deadline-organized vs. category-organized).
- The output skill follows extraction-skill conventions.

**Pass criteria:** Output skill follows extraction-skill conventions.

### Scenario 6: Fork-an-existing-skill scenario

**Inputs:** "I want a version of NDA Review calibrated to our company's specific risk tolerances."

**Expected output:**
- The skill recognizes the fork-an-existing-skill pattern.
- The skill prompts what specifically should differ (severity calibration, perspective default, recommended language).
- The skill suggests using NDA Review as the base and applying targeted modifications, rather than creating a new skill from scratch.
- The output is either a fork (copy of NDA Review with targeted modifications) or an extension pattern (a new skill that wraps or extends NDA Review).

**Pass criteria:** Skill recognizes the fork pattern and supports it.

### Scenario 7: Ambiguous scenario

**Inputs:** "I want a skill that helps with contracts."

**Expected output:**
- The skill recognizes the ambiguity.
- The skill probes for specificity: review? extraction? generation? Q&A? rewriting?
- The skill does not produce a vague "general contracts" skill from a vague description; it scopes the conversation toward a specific skill.

**Pass criteria:** Skill avoids producing vague skills from vague inputs.

## Refusal scenarios

### Refusal 1: Skill description is out of scope

**Input:** "I want a skill that predicts the weather" or "I want a skill that helps me plan a vacation."

**Expected behavior:**
- Skill explicitly notes the scope mismatch (legal-domain skills).
- Skill optionally suggests alternative tools or approaches.

**Pass criteria:** Explicit scope refusal.

### Refusal 2: Skill description implies producing legal advice as a primary output

**Input:** "I want a skill that tells me whether contracts are enforceable" or "I want a skill that gives clients legal opinions."

**Expected behavior:**
- Skill notes that producing legal advice or enforceability opinions is outside the conservative-posture conventions for LQ.AI skills.
- Skill suggests reframing toward a contract-analysis skill that *informs* the user's analysis rather than *substituting* for it.

**Pass criteria:** Skill maintains conservative-posture conventions for skills it creates.

## Cross-cutting verification

- **Output skills validate.** Every output `SKILL.md` is a well-formed agentskills.io artifact: valid YAML frontmatter, required fields present, body follows the standard structure.
- **Output skills follow conservative-posture conventions.** Generated skills include "what this skill does not do" sections, defer enforceability, do not invent authorities.
- **Output skills are operationally usable.** A skill produced by Skill Creator could be merged into the project (after the substantive-review process) without major rework.
- **Skill Creator does not produce skills outside LQ.AI's scope.** Out-of-scope requests are refused, not silently fulfilled.
- **Skill Creator preserves the agentskills.io format.** Output skills are interoperable with other agentskills.io / Claude Skills runtimes.

## Pass / fail decision

Skill Creator v1.0.0 passes acceptance testing when:

1. All 7 test scenarios pass structural checks (output skills validate against the frontmatter schema; required sections present).
2. All 7 test scenarios pass calibration evaluation — output skills follow the Skill-Authoring Guide conventions.
3. Both refusal scenarios trigger documented refusal behavior.
4. Cross-cutting verification passes on every scenario.

## Reviewer notes

Skill Creator is the most procedurally-distinct of the M1 starter skills — it produces other skills as output rather than producing analysis of documents. The reviewing process is similarly distinct:

- The reviewer evaluates the *output skills* against the Skill-Authoring Guide conventions (rather than against substantive legal correctness — that depends on the input scenario).
- The reviewer verifies the *conversation flow* is calibrated — that Skill Creator asks operationally-useful questions, applies sensible defaults, and refuses out-of-scope.
- The reviewer verifies the *output frontmatter* validates and the *output body* follows the standard structure.

Specific competencies for the reviewer:

- Familiarity with the Skill-Authoring Guide and the conventions established by M1 starter skills.
- Ability to recognize when an output skill is well-formed vs. when it would need significant rework before merge.
- Recognition of the conservative-posture conventions and whether output skills inherit them.

Calibration assessment is documented in `test-results/skill-creator-v1.0.0/calibration-assessment.md`. The output skills produced during testing are stored in `test-results/skill-creator-v1.0.0/generated-skills/` for the reviewer to inspect.
