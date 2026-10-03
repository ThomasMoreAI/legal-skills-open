---
name: background-ip-schedule
title: Background IP Schedule Skill
description: Manage ENAC Background IP inventory and carve-out language. Use for contracts, IP ownership clauses, methodology protection, prompt or agent IP, deliverables, and Background IP schedule updates.
author: Everyone-Needs-A-Copilot
author_url: https://github.com/Everyone-Needs-A-Copilot/codex-copilot/tree/main/packs/writing-legal/skills/background-ip-schedule
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: contracts
language: en
---

# Background IP Schedule Skill

ENAC's intellectual property is the firm's core asset. The methodologies, frameworks, agents, prompts, and tools that ENAC has developed over years of work are what make every engagement possible. The Background IP Schedule is the legal instrument that protects them.

---

## What Is Background IP

Background IP is all intellectual property created before or independent of a specific client engagement. It includes everything ENAC brings to the table regardless of who the client is.

**Includes:**
- Methodologies and frameworks (how ENAC thinks about and structures problems)
- AI agent definitions and prompt libraries (the instructions that make Claude work the way ENAC needs it to)
- Templates (document, slide, report structures)
- Skill files and knowledge base content (the rules and guidance behind ENAC's work)
- Software code and configurations (Pipeline Copilot, Figma plugin, bridge server)
- Voice and writing guidelines (Pablo's presentation voice, writing style guides)
- Brand assets and visual identity
- Training materials and internal documentation
- Any tools, frameworks, or approaches that ENAC would use on more than one engagement

**Does not include:**
- Deliverables created specifically for and delivered to a specific client (Foreground IP)
- Client's own proprietary data, processes, or materials (client's property)
- Publicly available information incorporated into deliverables

---

## ENAC's Current Background IP Inventory

This is the authoritative list. Update after every engagement where new methodologies, agents, or frameworks are developed. Attach this inventory as Exhibit [X] to every government contract.

### Narrative and Presentation Frameworks
- "Not a Pitch Deck" narrative arc framework (documented in `presentation-narrative-arc` skill)
- ENAC "Confront / Co-Create / Copilot" three-phase engagement methodology
- Slide copywriting methodology and economy rules (documented in `slide-copywriting` and `proposal-slide-copywriting` skills)
- Pablo's personal presentation voice guidelines (documented in `pablo-presentation-voice` skill)
- Proposal response framework and structure (documented in `proposal-response` skill)

### Consulting Methodologies
- Client brief analysis methodology: six-question brief structure (documented in `client-brief-analysis` skill)
- Alignment document structure and SOW framework (documented in `alignment-document` skill)
- Case study narrative arc and structure (documented in `case-study` skill)
- Testimonial builder methodology (documented in `testimonial-builder` skill)
- Narrative workflow: end-to-end narrative to Figma process (documented in `narrative-workflow` skill)

### AI Agent Definitions and Workflows
- ENAC Four Agents framework: @cs (Chief of Sales), @cmo (Chief Marketing Officer), @cco (Chief Creative Officer), @cw (Copywriter)
- Legal Agent Team: @legal-gc, @legal-contracts, @legal-ip, @legal-privacy, @legal-employment, @legal-ai-gov
- Agent-First Protocol (the /protocol workflow)
- Pipeline Copilot session management workflow (/pipeline, /continue)
- All agent definition files in `.claude/commands/`

### Skills and Knowledge Base
- All skill files in `.claude/skills/`: the rules, frameworks, and guidance that govern how ENAC works
- Claude Copilot system architecture and knowledge repository structure
- Legal skills library (legal-review, legal-risks, legal-negotiate, legal-missing, legal-freelancer, legal-nda, legal-agreement, legal-compliance, contract-review-cuad, government-contracts, ip-licensing, DPIA-Sentinel, technology-services-agreement, employment-labor)
- Colorado-specific legal skills (colorado-government-contracting, background-ip-schedule, colorado-ai-act)

### Software and Tools
- Pipeline Copilot CLI (`pcopilot`): Python CLI for content workbench operations
- Figma Plugin (Pipeline Copilot): custom Figma plugin for narrative deck management
- Bridge server: CORS-enabled server for Figma plugin communication
- Word generation system: Markdown to Word document conversion
- All code in the pipeline-copilot repository

### Brand and Voice
- ENAC brand identity, visual design standards, and marketing materials
- "Everyone Needs a Copilot" brand positioning and voice
- ENAC's core beliefs, methodology names, and brand terminology

---

## Required Contract Carve-Out Language

This is the exact language to insert in every government contract and professional services agreement. Insert in the IP/deliverables section. Do not accept IP assignment language without this carve-out.

**Full version (preferred):**

> "Contractor retains all right, title, and interest in and to its pre-existing intellectual property, methodologies, frameworks, templates, tools, prompts, and know-how ('Background IP'), including any improvements, modifications, or derivatives thereof developed during the engagement. For purposes of this Agreement, 'Background IP' means all intellectual property owned or controlled by Contractor prior to or independent of this Agreement, including but not limited to the items listed in the Background IP Schedule attached hereto as Exhibit [X], and any updates or improvements thereto. Contractor grants County a perpetual, royalty-free, non-exclusive, non-transferable license to use Background IP solely to the extent embedded in the final deliverables specifically identified in the Statement of Work for County's internal business purposes only. Final deliverables specifically prepared for and delivered to County ('Foreground IP') are owned by County, excluding Background IP incorporated therein. Contractor may use de-identified findings, learnings, and methodological improvements for portfolio, case study, and marketing purposes, subject to the confidentiality provisions herein."

**Short version (use when full version is rejected: minimum acceptable):**

> "Contractor retains ownership of its pre-existing methodologies, frameworks, tools, and know-how ('Background IP'). County receives a non-exclusive license to use Background IP as embedded in the final deliverables for County's internal purposes. Final deliverables (excluding Background IP) are owned by County."

**If the short version is also rejected:** Walk away. Any IP assignment without a Background IP carve-out is a walk-away issue. Escalate to human counsel.

---

## Derivative IP Rule

Any improvement or modification to ENAC's Background IP that occurs during a client engagement belongs to ENAC, not the client.

**Why:** ENAC's methodology pre-existed the engagement. A better version of that methodology, developed while applying it to a specific client's problem, is still ENAC's methodology. The client paid for the output (the deliverable), not for ownership of ENAC's intellectual evolution.

**Practical example:** If ENAC develops a refined version of the client brief framework while working on an Adams County engagement, that refinement is ENAC's Background IP. The client received the deliverable that used the refined framework: they did not receive ownership of the framework.

**Required action:** After every engagement, identify any methodological improvements and capture them in the skills repository. Update the Background IP Schedule to include the new or refined item.

---

## Trade Secret Protection Steps

For AI prompts, agent definitions, and proprietary workflows to qualify for trade secret protection, ENAC must take reasonable steps to protect them:

1. **Mark materials:** Every document or file containing Background IP must be marked "Confidential: Trade Secret" in the header or file properties
2. **Limit access:** Personnel should access Background IP only to the extent needed for their specific work
3. **Execute NDAs:** All personnel (employees, contractors, subcontractors) must sign NDAs before accessing Background IP
4. **Separate methodology from deliverables:** Do not include raw prompt files, agent definitions, or methodology documentation in client deliverables unless specifically required: deliver the output, not the machinery
5. **Digital security:** Store Background IP in access-controlled systems; do not share via unsecured channels
6. **CORA marking:** All materials submitted to government clients are marked (see CORA section in `colorado-government-contracting` skill)

**Colorado trade secret definition (C.R.S. 7-74-102):** Information that: (a) derives independent economic value from not being generally known or readily ascertainable; and (b) is subject to reasonable efforts to maintain its secrecy.

ENAC's methodologies, agent definitions, and prompt libraries meet this definition. The reasonable efforts requirement is met by following the protection steps above.

---

## Update Protocol

The Background IP Schedule is a living document. Update it after every engagement.

**After every engagement, check:**
1. Did ENAC develop any new methodologies, frameworks, or approaches?
2. Were any existing skill files materially improved?
3. Were any new agent definitions or prompt configurations developed?
4. Was any new software code created for ENAC's internal tools?
5. Were any new assessment approaches or analytical frameworks applied for the first time?

If yes to any: add the new item to the Background IP Schedule inventory above, create or update the relevant skill file, and document the development in the engagement's work product record.

**Why this matters:** The Background IP Schedule attached to a contract protects only the items listed on it. If a new framework developed in a prior engagement is not on the schedule when you sign the next contract, that framework is not explicitly protected. Keep the schedule current.

---

## Background IP in Contractor Agreements

Every contractor and subcontractor must:
1. Receive a copy of the Background IP Schedule as part of their agreement
2. Acknowledge that the listed items are ENAC's property
3. Agree not to use, copy, or disclose any Background IP outside of their work for ENAC
4. Assign all improvements or derivative works of Background IP to ENAC
5. Return or destroy all Background IP materials at the end of the engagement

---

## Anti-Generic Rules

- NEVER sign a contract with IP assignment language without attaching the Background IP Schedule
- NEVER submit the Background IP Schedule itself as a contract deliverable: it is an exhibit, not a product of the engagement
- NEVER allow "all work product created under this agreement" language to pass without the carve-out
- NEVER treat the Background IP Schedule as a one-time document: update it after every engagement
- NEVER accept a government contract where §12.12 (or equivalent) assigns "all documentation" without a carve-out
