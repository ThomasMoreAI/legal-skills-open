---
name: matter-briefing-lsdisconzi
title: Matter Briefing
description: Generate a deep briefing on the current case — ready for a partner, co-counsel, or client call. Distills violations, evidence items, and transcripts into an executive-ready brief.
author: lsdisconzi
author_url: https://github.com/lsdisconzi/craudio-para-adevogados/tree/main/skills/matter-briefing
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: litigation
language: en
---

# Matter Briefing

Produces audience-calibrated case briefings. Each audience gets a different depth, different language, and different framing.

## Running this skill

1. **Load configuration.** Read the configured practice profile at `~/.claude/plugins/config/craudio-p-advogados/<plugin>/CLAUDE.md` and the firm profile at `~/.claude/plugins/config/craudio-p-advogados/company-profile.md`. If either file is missing, or a critical field still shows `[PLACEHOLDER]`, STOP — tell the attorney: "This plugin needs setup. Run the `cold-start-interview` skill."
2. **Apply the frame.** The Plugin Operating Rules, Shared Guardrails, Decision posture, Jurisdiction recognition, Retrieved-content trust, and Ontology Governance sections of CLAUDE.md govern this skill. The skill workflow below is a FLOOR, not a ceiling (see "Scaffolding, not blinders").
3. **Resolve vault paths.** Every `{vault root}` reference below resolves against `## Vault location` in CLAUDE.md. Never hard-code an absolute path.
4. **Apply the work-product header** from CLAUDE.md `## Outputs` to every internal deliverable; suppress it on externally-facing output per Quiet mode.
5. **Run the workflow below.**
6. **Close** with the `⚠️ Reviewer note` block and the next-steps decision tree from CLAUDE.md `## Outputs`.

---

## Workflow

### 1. Select Audience

| Audience | Language | Depth | Focus |
|---|---|---|---|
| **Executive (partner)** | Portuguese | 2-page summary | Strategy, risks, deadlines, resources |
| **Partner brief** | Portuguese | 5-10 pages | Full legal analysis, claim strength, forum strategy |
| **Client update** | Portuguese | 2 pages | Case status, next steps, what client needs to provide |
| **Chilean co-counsel** | Spanish | 5-10 pages | Chilean claims, evidence, local procedure, coordination |
| **International co-counsel** | English | 10-15 pages | Full case theory, treaty claims, IACHR strategy |
| **Full brief** | Portuguese + English | 20+ pages | Complete case file — all violations, all evidence, all strategy |

### 2. Executive Summary (All Audiences)
Consistent across all briefings:
- **Case in one paragraph:** [Fill from CLAUDE.md incidents]
- **Bottom line:** [Fill — key violations, strongest evidence, institutional patterns]
- **Immediate deadlines:** [Fill from CLAUDE.md prescription table]
- **Estimated value:** [Fill from CLAUDE.md damages framework]

### 3. Claim Strength Assessment
Rate each claim category (fill from violations analysis):

| Claim | Jurisdiction | Evidentiary Strength | Legal Basis Strength | Overall |
|---|---|---|---|---|
| [Fill from violations analysis] | [JUR] | [RATING] | [RATING] | [RATING] |

### 4. Risk Assessment

| Risk | Likelihood | Severity | Mitigation |
|---|---|---|---|
| [Fill — prescription lapse risk] | [RATING] | [RATING] | [Mitigation strategy] |
| [Fill — jurisdictional challenge risk] | [RATING] | [RATING] | [Mitigation strategy] |

### 5. Recommended Strategy

**Immediate (this week):**
1. File demand letters to all defendants (preserve rights, toll prescription if possible)
2. Request evidence preservation via judicial order where applicable
3. Request relevant records via transparency / FOIA mechanisms

**Short-term (next 2 weeks):**
4. Complete all evidence hashing and authentication
5. Finalize claim charts for all causes of action
6. Engage foreign co-counsel (if not already retained)

**Medium-term (next 30 days):**
7. File initial petition at lead forum
8. File parallel actions at secondary fora as warranted
9. File criminal/regulatory complaints where applicable

**Long-term (after local remedies):**
10. Monitor international / treaty forum filing windows
11. Consider state-to-state or treaty complaint mechanisms

### 6. Output
- Audience-specific brief in `.docx` format
- Executive summary one-pager for all audiences
- Dashboard with claim strength, deadlines, and risk matrix
- Deck-ready summary slides (if requested)

## Guardrails
- All claim assessments are analytical, not guarantees
- Audience calibration is critical — don't give client the partner brief
- Every cited fact must have an evidence anchor
- Co-counsel briefs: flag what you need from them, not just what you have
- Client updates: plain Portuguese, no legal jargon, clear action items
- **Ontology compliance:** outputs must satisfy the litigation-relevant error codes in `core/ontology/error-catalog.md`. If an invariant violation is detected, flag with `[ONT-ERROR: <code>]` and do not produce confident output. I-1 is absolute: no conclusory language.
