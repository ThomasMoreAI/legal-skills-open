# Surface profiles

Risk profile for each common destination AI surface. The analyzer looks up the user's chosen surface here to determine the *baseline* risk posture before factoring in content and matter-posture overlays.

**Currency:** April 2026. Vendor terms change. Before relying on any profile below for a real matter, the lawyer (or firm IT/compliance) must verify the surface's current Terms of Use, Privacy Policy, and Data Processing Agreement (per ABA Op 512 § B; cite pack § 5). This file is a working snapshot, not a substitute for that review.

**Schema:**
- **Tier:** consumer | team | enterprise | api | on-prem
- **Trains on inputs (default):** yes | no | configurable
- **Retains inputs:** retention window or "zero" if ZDR
- **Third-party disclosure (per ToS):** broad | narrow | none
- **A/C privilege impact:** Heppner-style failure modes that apply
- **Work-product impact:** under Warner/Morgan reasoning, civil posture
- **ABA 512 confidentiality posture:** likely-violates | conditional | likely-compliant
- **Baseline band:** SAFE | CAUTION | STOP for matter-related content

---

## Consumer surfaces (default: STOP for any matter-related content)

### Surface: ChatGPT (Free, Plus)
- **Tier:** consumer
- **Trains on inputs (default):** yes (opt-out available in settings, but default is on)
- **Retains inputs:** indefinite by default, 30 days if chat history disabled
- **Third-party disclosure (per ToS):** broad (legal process, partners, service providers)
- **A/C privilege impact:** All three Heppner elements fail. Not an attorney; not confidential under ToS; not for purpose of obtaining legal advice from the model.
- **Work-product impact:** Under Warner/Morgan reasoning, work product MAY survive in civil discovery — but only if (a) prepared in anticipation of litigation, (b) by a party or representative, and (c) the AI tool's identity, separately discoverable per Morgan, doesn't itself reveal strategy. In criminal posture or under search warrant (Heppner), no protection.
- **ABA 512 confidentiality posture:** likely-violates for any matter-related input without specific informed client consent (cite pack § 5 — confidentiality + boilerplate-insufficient quotes).
- **Baseline band:** **STOP** for any input containing client information, attorney mental impressions, or matter-specific facts.

### Surface: Claude.ai (Free, Pro)
- **Tier:** consumer
- **Trains on inputs (default):** no for paid Pro users (per April 2026 ToS); historically variable for free tier — verify current version
- **Retains inputs:** 30-day default per Anthropic policy in effect at Heppner ruling (Feb 2026)
- **Third-party disclosure (per ToS):** Heppner court quoted Anthropic's policy as reserving the right to disclose user data to third parties including governmental regulatory authorities (cite pack § 1, element 2).
- **A/C privilege impact:** Same as ChatGPT consumer — all three Heppner elements fail. Heppner is THE governing case for Claude consumer specifically.
- **Work-product impact:** Same analysis as ChatGPT consumer.
- **ABA 512 confidentiality posture:** likely-violates for matter-related input without specific informed client consent.
- **Baseline band:** **STOP** for any input containing client information, attorney mental impressions, or matter-specific facts.

### Surface: Google Gemini (consumer / Google account)
- **Tier:** consumer
- **Trains on inputs (default):** yes (human reviewers may see content per Google's Gemini Apps Privacy Hub)
- **Retains inputs:** up to 18 months default; configurable
- **Third-party disclosure (per ToS):** broad (Google's general privacy policy applies)
- **A/C privilege impact:** Same Heppner failure pattern.
- **Work-product impact:** Same analysis as ChatGPT consumer.
- **ABA 512 confidentiality posture:** likely-violates.
- **Baseline band:** **STOP** for any input containing client information.

### Surface: Free / publicly available AI tool (general)
- **Tier:** consumer
- **Trains on inputs (default):** assume yes
- **Retains inputs:** assume indefinite
- **Third-party disclosure (per ToS):** assume broad
- **ABA 512 posture:** DC Bar Op 388 specifically cited (cite pack § 7): "Most technology companies that provide these [free] services make no secret of what they will do with any information submitted to them ... user inputs are theirs to use and share as they see fit."
- **Baseline band:** **STOP** for any input containing client information.

---

## Team / Enterprise surfaces (default: CAUTION; configuration matters)

### Surface: ChatGPT Team / Enterprise
- **Tier:** team / enterprise
- **Trains on inputs (default):** no (per OpenAI Enterprise ToS — verify current version)
- **Retains inputs:** customizable; default 30 days; ZDR available on Enterprise tier with negotiation
- **Third-party disclosure (per ToS):** narrower than consumer; SOC 2 Type II; subject to legal process
- **A/C privilege impact:** Heppner element 1 (not an attorney) still fails. Element 2 (confidentiality) is closer — depends on whether ToS is "publicly accessible" or under enterprise contract with no-train + retention controls. Element 3 (purpose) depends on whether the lawyer (not the client) is the user and whether the lawyer's use is part of the representation. Even in best case, no court has yet held that any Enterprise GAI use survives privilege analysis end-to-end.
- **Work-product impact:** Strongest case for protection under Warner/Morgan if civil posture and party/representative is the user. Identity of the tool is still discoverable (Morgan).
- **ABA 512 confidentiality posture:** conditional — likely compliant IF (a) ToS reviewed and confirms no-training and adequate retention controls, (b) DPA in place, (c) informed client consent obtained when required, and (d) firm has a written AI use policy.
- **Baseline band:** **CAUTION** — depends on content overlay. Permissible for matter-related content with informed client consent and verified ToS; not permissible for the most sensitive content (privileged communications, attorney work product reflecting strategy) absent explicit ZDR + signed DPA.

### Surface: Claude Team / Enterprise
- **Tier:** team / enterprise
- **Trains on inputs (default):** no per Anthropic Enterprise ToS
- **Retains inputs:** ZDR available on Enterprise tier (and is the default for many enterprise contracts in April 2026)
- **Third-party disclosure (per ToS):** narrower than consumer; subject to legal process
- **A/C privilege impact:** Same as ChatGPT Enterprise — Heppner element 1 still fails; elements 2 and 3 are more defensible but no court has yet ruled.
- **Work-product impact:** Same as ChatGPT Enterprise.
- **ABA 512 confidentiality posture:** conditional, same conditions as above.
- **Baseline band:** **CAUTION** — same overlay considerations.

### Surface: Claude Enterprise + Zero Data Retention (ZDR)
- **Tier:** enterprise
- **Trains on inputs (default):** no
- **Retains inputs:** zero (ZDR contractually guaranteed)
- **Third-party disclosure (per ToS):** narrowest commercially-available; ZDR contracts limit disclosure to what's required by law
- **A/C privilege impact:** Heppner element 1 still fails (Claude is not an attorney). Element 2 (confidentiality) is strongest available case — no retention means no third-party disclosure pathway. Element 3 still depends on user's purpose. NO court has ruled on a ZDR-tier exchange yet; Heppner was decided on consumer-tier ToS.
- **Work-product impact:** Strongest available; civil posture + party/representative + ZDR ≈ best case for survival.
- **ABA 512 confidentiality posture:** likely-compliant for matter-related content, subject to (a) informed client consent if input includes self-learning training data, (b) review of the actual ZDR contract, (c) firm AI policy.
- **Baseline band:** **CAUTION** for privileged content (the law has not caught up); **SAFE** for non-privileged matter-related work like research, drafting, summarization — assuming proper client consent and firm policy.

### Surface: Microsoft Copilot for M365 (Business / Enterprise)
- **Tier:** enterprise
- **Trains on inputs (default):** no (tenant-isolated; per Microsoft Enterprise ToS)
- **Retains inputs:** within tenant; subject to tenant retention policy
- **Third-party disclosure (per ToS):** narrow; tenant-isolated
- **A/C privilege impact:** Heppner element 1 still fails. Elements 2 and 3 are more defensible given tenant isolation, but again — no court has ruled.
- **Work-product impact:** Similar to enterprise GAI generally.
- **ABA 512 confidentiality posture:** conditional — depends on tenant configuration and whether Copilot's data handling matches the firm's confidentiality obligations.
- **Baseline band:** **CAUTION** — same overlay considerations as ChatGPT Enterprise.

### Surface: Google Gemini for Workspace (Enterprise)
- **Tier:** enterprise
- **Trains on inputs (default):** no for Workspace Enterprise editions; verify
- **Retains inputs:** within Workspace; configurable
- **Third-party disclosure (per ToS):** narrow
- **A/C privilege impact:** Same enterprise pattern.
- **Work-product impact:** Same enterprise pattern.
- **ABA 512 confidentiality posture:** conditional.
- **Baseline band:** **CAUTION**.

### Surface: Anthropic API (direct, no enterprise contract)
- **Tier:** api
- **Trains on inputs (default):** no (per API ToS)
- **Retains inputs:** 30 days for trust & safety review; ZDR available with enterprise agreement
- **Third-party disclosure (per ToS):** subject to legal process
- **A/C privilege impact:** Same enterprise pattern — Heppner element 1 fails; elements 2/3 depend on configuration and use.
- **Work-product impact:** Similar to enterprise GAI.
- **ABA 512 confidentiality posture:** conditional. The API is the surface most readers of ABA Op 512 had in mind for "in-house" GAI; Florida Bar Op 24-1 specifically endorsed in-house GAI as mitigating confidentiality risk (cite pack § 6).
- **Baseline band:** **CAUTION** by default; can move toward SAFE with ZDR contract and proper firm controls.

---

## On-prem / self-hosted (default: SAFE for content; band-up only on truly privileged input)

### Surface: Self-hosted open-weight model (e.g., Llama, Mixtral, on firm infrastructure)
- **Tier:** on-prem
- **Trains on inputs (default):** no (you control the model)
- **Retains inputs:** only what your infrastructure logs
- **Third-party disclosure (per ToS):** none — there is no third party
- **A/C privilege impact:** Heppner element 1 still fails as a doctrinal matter (the model is still not an attorney), but elements 2 and 3 are strongest possible — no third-party disclosure pathway; nothing leaves the firm.
- **Work-product impact:** Strongest possible — equivalent to using firm word-processing software (cf. Warner court's analogy that "AI is a tool, not a person").
- **ABA 512 confidentiality posture:** likely-compliant. Florida Bar Op 24-1 explicitly favors in-house GAI for confidentiality.
- **Baseline band:** **SAFE** for matter-related content. Privileged communications still warrant a CAUTION flag for the doctrinal Heppner element-1 issue, but the practical risk is minimal.

### Surface: Firm-deployed proprietary GAI (e.g., enterprise AI platform inside firm VPN)
- **Tier:** on-prem (functionally)
- Same posture as self-hosted open-weight, with the additional benefit of vendor support and indemnification (depends on contract).
- **Baseline band:** **SAFE** for matter-related content.

---

## Special: Privilege Sentinel itself (running as a Claude Code skill)

When this tool runs as a Claude Code skill in the lawyer's local Claude Code session, the destination surface for the *prompt being analyzed* is whichever surface the lawyer plans to send it to next — that is what the user selects when invoking the skill.

The skill itself is just text running inside the lawyer's existing Claude Code environment. If the lawyer's Claude Code is wired to Claude Enterprise + ZDR (which it is in Emily's IRG configuration), then the skill's own analysis happens under those terms. The recursion: this tool warns about hosted AI surfaces while itself running locally. That is the design.

---

## How to add a new surface

When a lawyer or firm uses a surface not listed here:
1. Pull the surface's current Terms of Use, Privacy Policy, and (if applicable) Data Processing Agreement.
2. Map the surface to the schema fields above.
3. Place it in the correct tier section.
4. Determine baseline band by analogy to the closest profile.
5. Cite the relevant entries in `citations.md` for any claimed legal effect.

Do not invent surface profiles from general industry knowledge. The risk picture depends on the specific contractual terms in effect.
