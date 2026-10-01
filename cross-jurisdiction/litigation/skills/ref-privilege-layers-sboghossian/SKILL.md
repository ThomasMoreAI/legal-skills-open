---
name: ref-privilege-layers-sboghossian
title: Reference — Privilege Layers in Legal AI
description: Use as a reference guide on the different privilege layers that apply in legal AI work — attorney-client privilege, work product doctrine, AI carve-out risks (Heppner and related), joint defense / common interest privilege, settlement privilege, and mediation privilege. Louis must apply the correct privilege treatment to AI-assisted communications and warn users when privilege is at risk. Relevant across MENA (DIFC, ADGM, UAE, KSA) and common-law jurisdictions.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/ref/ref-privilege-layers
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: cross-jurisdiction
practice: litigation
language: en
---

# Reference — Privilege Layers in Legal AI

## Scope

Privilege is one of the most important and most misunderstood dimensions of legal AI use. Submitting client content to an AI tool, sharing AI-generated analysis beyond the privileged circle, or using AI in ways that may not qualify for privilege protection can waive valuable protections. This reference sets out the key privilege layers, how they interact with AI use, and what Louis must do to preserve appropriate privilege markings and warn users at risk.

---

## Layer 1 — Attorney-Client Privilege

**What it protects:** Confidential communications between an attorney and their client, made for the purpose of obtaining or providing legal advice.

**Requirements (common across jurisdictions):**
- An attorney-client relationship must exist
- The communication must be for the purpose of legal advice (not business advice or commercial strategy that happens to involve a lawyer)
- The communication must be kept confidential — disclosure to third parties outside the privileged circle waives the privilege

**AI interaction risk:** If a client shares privileged communications with an AI tool that is not covered by a proper legal framework (attorney supervision + confidentiality + DPA), those communications may lose privilege. The key question in most jurisdictions: is the AI tool part of the attorney-client communication, or a third party that receives the communication?

**Current treatment by jurisdiction:**

| Jurisdiction | Treatment | Notes |
|---|---|---|
| US | AI tools used by lawyers in the course of legal representation are generally treated as part of the legal team (like paralegals or expert assistants); privilege preserved if confidentiality is maintained | See Heppner v. State (discussed below) for AI chat exceptions; consult Restatement (Third) of the Law Governing Lawyers § 59 |
| UK / DIFC / ADGM | Legal advice privilege covers communications between lawyer and client for legal advice; work product privilege covers materials prepared in anticipation of litigation; AI tool must be part of the lawyer's process, not a standalone third party | DIFC Courts have not yet specifically ruled on AI-assisted privilege; apply general common-law principles |
| UAE (onshore) | Privilege is recognized in general terms; Al-Amir privilege concept; less developed jurisprudence than common law | Consult local counsel for specific AI privilege strategy |
| KSA | No formal attorney-client privilege statute; confidentiality obligation under lawyer code of conduct; Sharia-based courts may treat certain communications as confidential | Conservative approach: treat all client communications as potentially discoverable unless clearly privileged |
| Lebanon | Limited statutory privilege; Bar Association confidentiality rules apply | Conservative approach; French-influenced civil procedure |
| Egypt | Lawyer confidentiality under Bar Association law; privilege less developed in procedural law | Conservative approach |

---

## Layer 2 — Work Product Doctrine

**What it protects:** Documents and materials prepared by or for a lawyer in anticipation of litigation or for trial — including factual work product (investigation results, witness lists) and opinion work product (strategy, legal analysis, mental impressions).

**AI interaction:** AI-generated legal analysis, draft briefs, research memos, and strategy documents prepared by a lawyer using an AI tool should qualify as work product provided:
- They are prepared in anticipation of specific litigation or legal proceedings
- The lawyer exercises meaningful professional judgment in directing and reviewing the AI output
- The materials are kept confidential within the legal team and client

**Protection level:** Opinion work product receives near-absolute protection; factual work product can be overcome on a showing of substantial need and inability to obtain by other means.

**Key vulnerability:** If the lawyer does not meaningfully review and adopt the AI output as their own professional work product, a court may treat it as a mere reproduction of third-party AI output, not protected work product. The lawyer's intellectual contribution matters.

---

## Layer 3 — AI Carve-Out Risk (Heppner and Related Developments)

**The Heppner issue:** In *Heppner v. State* (a US state court case that gained widespread attention in legal AI circles), the court considered whether a defendant's chats with an AI legal assistant constituted privileged attorney-client communications. The court concluded they did not — because the AI is not an attorney and the defendant did not have an attorney-client relationship with the AI provider.

**The practical implication:** A non-lawyer using an AI tool to get "legal advice" — even through a platform that presents AI responses in a legal-advice format — does not create attorney-client privilege. The AI is not a lawyer; there is no privilege.

**MENA application:** This issue is equally applicable in DIFC and ADGM, where attorney-client privilege is recognized in common-law form. An employee or individual using Louis without a supervising lawyer does not have a privileged communication. Louis must warn users when they appear to be seeking legal advice as individuals, not through a lawyer.

**What Louis must do:**
- Clearly identify when a user is using Louis as a legal professional (privilege preserved in the lawyer's work product) vs. as an individual non-lawyer (no privilege)
- Include the disclaimer for non-lawyer contexts: *"This AI output does not constitute legal advice and does not create an attorney-client relationship. These communications are not privileged."*
- Flag to the user if they are pasting apparently privileged client communications into a session that may not be privileged-protected

---

## Layer 4 — Joint Defense / Common Interest Privilege

**What it protects:** Communications among multiple clients (typically co-defendants or parties with a shared legal interest) and their respective lawyers, shared for the purpose of their common legal defense or strategy.

**AI interaction risk:** If privileged joint defense communications are shared with an AI platform, the multi-party nature of the privilege makes the risk higher — disclosure to the AI could potentially constitute disclosure outside the privileged circle for one or more of the parties.

**Practical rule:** Joint defense group communications should be handled through a specifically designated, audited channel with explicit privilege logging. Do not paste joint defense strategy communications into an AI prompt without confirming that all parties and their counsel have authorized the AI use.

---

## Layer 5 — Settlement Privilege

**What it protects:** Communications made in the context of negotiating a settlement of an existing or anticipated dispute — the principle that parties should be able to negotiate openly without fear that their offers will be used against them at trial.

**Treatment by jurisdiction:**
- **US:** Federal Rule of Evidence 408 and state equivalents; settlement communications generally inadmissible on the issue of liability
- **UK / DIFC / ADGM:** "Without prejudice" communications are protected from disclosure; must be clearly marked "Without Prejudice"
- **UAE onshore / KSA:** Sulh (amicable settlement) principles; less developed evidentiary privilege rules; consult local counsel
- **Lebanon / Egypt:** Civil procedure protections; consult local counsel

**AI interaction:** Settlement negotiations should not be run through an AI tool without confirming that the AI session is properly privileged and confidential. Draft settlement positions generated by AI are particularly sensitive.

**Louis rule:** Any draft settlement communication or position paper generated by Louis must be marked: *"PRIVILEGED — WITHOUT PREJUDICE — DO NOT DISCLOSE"* in the header. Remind users to add this marking before sending.

---

## Layer 6 — Mediation Privilege

**What it protects:** Communications made in the context of mediation proceedings — the mediator's role is to facilitate candid communication, which would be undermined if statements made in mediation could be used as evidence.

**Treatment by jurisdiction:**
- **DIFC:** DIFC Arbitration Law and Mediation Law protect mediation communications
- **UAE:** Federal Law on Mediation (Law No. 6/2021 amending Law No. 40/2015) provides statutory mediation privilege
- **UK:** Mediation communications generally protected as "without prejudice"
- **US / EU:** Generally protected under ADR statutes and rules

**AI interaction:** AI tools should not be used to prepare materials for mediation without confirming that the mediation privilege framework applies and that the AI tool is part of the privileged process.

---

## Louis's privilege preservation obligations

When a user session involves potentially privileged content, Louis must:

1. **Detect** signals that the content may be privileged: "This is a memo I wrote for my client..."; "This is our litigation strategy..."; "This is what I told the mediator..."
2. **Apply** the appropriate privilege marking to all generated output: *"PRIVILEGED AND CONFIDENTIAL — ATTORNEY-CLIENT COMMUNICATION / WORK PRODUCT"*
3. **Warn** when privilege may be at risk: "You are pasting what appears to be a privileged communication into a shared session. Confirm that this session is covered by your firm's legal AI DPA and privileged-communications policy."
4. **Flag the Heppner risk** when a non-lawyer user asks for legal advice: include the attorney-client disclaimer
5. **Preserve** privilege markings in all output documents: if the input was marked privileged, the output carries forward the same marking

---

## Quick decision guide

| Content type | Privilege layer | AI interaction risk level |
|---|---|---|
| Lawyer's research and analysis for a client matter | Work product | Low — if the lawyer supervises and reviews |
| Client's factual statement to their lawyer | Attorney-client | Medium — AI tool must be part of the privileged process |
| Settlement negotiation draft | Settlement privilege | High — mark "without prejudice" explicitly; confirm privileged channel |
| Joint defense strategy memo | Joint defense privilege | High — confirm all parties have authorized AI use |
| Mediation position paper | Mediation privilege | High — confirm mediation privilege framework applies |
| Non-lawyer AI conversation | No privilege | No privilege applies — include explicit disclaimer |

---

## Related skills

- [[ref-anti-patterns]]
- [[ref-mcp-hardening]]
- [[ref-verification]]
- [[intel-us-court-ai-chats-not-privileged-heppner]]
