# CUI, Classified, and Controlled Technical Data — Handling Rules

Every ExChek skill begins with a **CUI/Classified/Controlled-Data check** and stops immediately if Controlled Unclassified Information (CUI), classified material, or certain controlled technical data is involved. Cloud-hosted AI services — including Claude web, Claude Desktop, Claude CoWork, ChatGPT, Perplexity, Gemini, Cursor's cloud modes, and similar — must **never** be used to process CUI, classified, or retransfer-controlled ITAR technical data unless the environment is certified for it.

---

## The gate (step 0 of every skill)

Ask the user at the very start, before collecting any item or party information:

> **Before we start, three quick questions about the information you'll share.**
>
> 1. Does it involve **Controlled Unclassified Information (CUI)** — for example, CUI-marked export-controlled technical data, ITAR-controlled technical data (22 CFR Part 121), CUI under a government contract, or Law Enforcement Sensitive (LES) material?
> 2. Does it involve **classified information** at any level (Confidential / Secret / Top Secret / SCI)?
> 3. Does it involve **ITAR technical data subject to a § 126.18 retransfer/release authorization** — i.e., defense articles or technical data that a TAA / MLA / exemption permits you to share only with specific foreign-person dual / third-country nationals of NATO, EU, AU-group, Japan, NZ, Switzerland, or Argentina employees?
>
> Please answer **Yes**, **No**, or **Don't know** for each.

Any **Yes** → route to on-prem guidance (see below). Do **not** proceed with cloud classification, screening, or analysis.

Any **Don't know** → give the quick brief below, then ask whether to proceed in this environment (No) or move to on-prem (Yes).

All **No** → continue — *after* the agent has confirmed the user's AI platform privacy settings are acceptable (see next section).

---

## Privacy settings — user must verify before proceeding (all environments)

Even for non-CUI, non-classified work, the AI platform the user is running on can leak sensitive commercial information (item specs, party names, pricing, supplier relationships) into provider training data, support logs, or third-party analytics. Before proceeding past the gate, tell the user:

> **At a minimum, confirm your AI platform's privacy settings opt you out of data collection and model training.**
>
> - **Preferred:** Run on a plan or product tier that contractually **does not train on your usage and does not collect or log your data** — e.g., Anthropic's Claude Enterprise / Teams / API with zero-retention, OpenAI ChatGPT Enterprise or API with Zero Data Retention, Google Workspace Gemini with data-not-used-for-training, Microsoft Copilot with commercial data protection, or an equivalent enterprise agreement.
> - **Minimum acceptable:** On a consumer tier, disable "Improve the model for everyone" / "Chat history & training" / "Help improve our services" in privacy settings; disable conversation sharing; disable third-party integrations you do not trust.
> - **Not acceptable for export-compliance work:** Free consumer tiers with training enabled, any public-share link, or shared / guest accounts where you cannot attest to the privacy settings.
>
> If you cannot confirm your settings meet at least the minimum above, stop and switch tiers or environments before continuing.

Agent behavior: if the user cannot or will not confirm, **do not proceed**. Treat this as a blocking step equivalent to the CUI gate. Log the confirmation (who attested, when, what tier) in the report's AI Tool Usage & Currency Disclosure section.

---

## Quick brief (for "Don't know")

**CUI** is a federal category for unclassified information that laws, regulations, or government policies require to be protected or controlled (see 32 CFR Part 2002 and the NARA CUI Registry at archives.gov/cui). Export-relevant CUI categories include **Export Controlled (EXPT)**, **Export Controlled Research (EXPTR)**, and ITAR-controlled technical data. Items often carry markings like **"CUI"**, **"CONTROLLED // EAR CONTROLLED"**, or **"CUI // ITAR"**.

**Classified information** (Confidential, Secret, Top Secret, SCI) is subject to Executive Order 13526 and cannot be processed through any commercial cloud AI.

**§ 126.18 controlled technical data** is ITAR technical data or defense services that a specific authorization (TAA, MLA, or exemption) permits you to share only with pre-identified foreign-person dual / third-country nationals — the authorization is not a general public release. Sending that data to a cloud AI risks a retransfer violation under 22 CFR § 127.1.

If any of these might apply, stop cloud use and switch to an on-prem setup, or check with your security/compliance team before continuing.

---

## Do not use cloud or API LLMs for CUI / classified / § 126.18 data

**Do not use cloud-hosted services or API-based LLM models** to process CUI, classified, or retransfer-controlled ITAR technical data. Sending item descriptions, technical specifications, source code, party lists, or other restricted content to third-party cloud APIs (commercial Claude, ChatGPT, Gemini, Perplexity, or other cloud LLM endpoints) may violate:

- Your agency or contractor security requirements (32 CFR Part 2002; DFARS 252.204-7012; NIST SP 800-171; CMMC 2.0).
- ITAR retransfer rules (22 CFR § 127.1) and § 126.18 authorization conditions.
- EAR deemed-export rules (15 CFR § 734.2(b)) where the cloud provider staff includes foreign persons without a deemed-export license.

If the user indicates any of the three Yes paths above, or their environment requires on-premises processing:

1. **Do not** call external APIs (including the ExChek API at `api.exchek.us` or the Trade.gov CSL API at `data.trade.gov`) with item data, party names, or context that could contain restricted content.
2. **Tell the user** they must run this skill in an **on-premises (on-prem) environment** with a **local LLM** only. They should:
   - Download the ExChek skill from the public GitHub repo as a **ZIP** (not clone over an untrusted network path) at [github.com/exchekinc/exchekskills](https://github.com/exchekinc/exchekskills) → Code → Download ZIP.
   - Transfer to the on-prem environment via their organization's approved method (classified courier, approved removable media, etc.).
   - Install into their on-prem agent's skills directory (e.g., `~/.claude/skills/<skill-name>` or the equivalent for their platform).
   - Run the skill with a **local LLM** hosted within their secure boundary — Ollama, LM Studio, vLLM, or an enterprise on-prem deployment. No cloud APIs or external LLM endpoints.
3. **Regulatory data** (eCFR Parts 774, 738, 740, 742, 744, 746, 121) must also be obtained on-prem. Options:
   - Run the ExChek API refresh script on-prem (from the ExChek API codebase) to pre-fetch and store current Part data.
   - From an internet-connected system allowed to reach eCFR, fetch `https://www.ecfr.gov/api/versioner/v1/structure/current/title-15.json` and `title-22.json`, transfer the files on-prem, and extract the relevant Part subtrees.
4. **External screening lists** (CSL, 1260H, UFLPA Entity List, FCC Covered List) cannot be queried from an air-gapped environment. The user must download current list data from the source agency to the on-prem environment on a documented cadence.

Full guidance (including curl examples and refresh steps) is in the ExChek docs: **https://docs.exchek.us/docs/cui-classified**.

---

## Summary for the agent

- **Three-question gate:** CUI? Classified? § 126.18 controlled technical data? Any Yes → on-prem only, stop cloud use.
- **Privacy-settings confirmation** (all environments): user must attest that their AI platform opts out of data collection and model training — preferably an enterprise tier that contractually does not train on or log usage.
- **Logging:** record the attestation (who, when, tier) in the report's AI Tool Usage & Currency Disclosure section.
- **On-prem path:** download ZIP → transfer via approved process → install in on-prem agent → local LLM → on-prem regulatory data → on-prem list data.
- **Docs:** https://docs.exchek.us/docs/cui-classified.
