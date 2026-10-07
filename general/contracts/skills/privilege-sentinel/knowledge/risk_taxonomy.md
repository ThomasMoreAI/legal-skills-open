# Risk taxonomy

How the analyzer turns a (prompt, surface, posture) tuple into a SAFE / CAUTION / STOP band with cited factors.

Every factor here references one or more entries in `citations.md` by section number (e.g., "[§ 1, element 2]"). The skill must produce that citation alongside any factor it raises.

---

## Bands

- **SAFE** — Send as-is. The prompt does not implicate privilege or work-product, OR the destination surface and posture eliminate the risk.
- **CAUTION** — Do not send as-is. Send only after at least one mitigation listed for the triggered factor (e.g., redact, obtain informed consent, switch surfaces).
- **STOP** — Do not send. Risk is high enough that mitigations within the lawyer's control are insufficient.

**Combination rule:** Final band = the most restrictive band raised by any single factor. STOP overrides CAUTION overrides SAFE. Factors do not "add up" or net out.

---

## Inputs the analyzer reads

1. **Prompt text** — the actual content the lawyer is about to send.
2. **Surface** — destination AI surface (from `surface_profiles.md`).
3. **Posture** — matter context:
   - Litigation status: `none` | `anticipated_civil` | `active_civil` | `anticipated_criminal` | `active_criminal`
   - User: `attorney` | `client_pro_se` | `client_with_counsel`
   - At counsel's direction (if user is client): `yes` | `no`
4. **Consent** — has informed client consent for AI use been obtained for this matter? `yes` | `no` | `not_applicable`
5. **Jurisdiction overlay (optional)** — `federal` | `florida` | other (defaults to federal + ABA Op 512)

---

## Content classification (pass 1)

The analyzer reads the prompt and labels each segment as one of:

| Class | Examples | Privilege/WP implication |
|---|---|---|
| `PUBLIC_LEGAL` | "What's the elements of fraud under FL law?" | None — no client info, no mental impressions |
| `HYPOTHETICAL_NO_ID` | "If a client did X, what would Y?" with no identifying detail | Low — no client information |
| `CLIENT_IDENTIFIABLE` | Names, entity names, matter numbers, dollar amounts, dates tied to a real matter | A/C confidentiality risk; ABA 512 § B |
| `MATTER_FACTS` | Specific factual narrative of a real matter | A/C confidentiality risk; potential work product if in anticipation of litigation |
| `ATTORNEY_MENTAL_IMPRESSIONS` | Legal strategy, theories of the case, witness assessments, settlement positions | Core work-product material; FRCP 26(b)(3); *Hickman v. Taylor* core protection |
| `PRIVILEGED_COMMUNICATION` | Verbatim or near-verbatim attorney-client exchanges | Highest privilege risk |
| `THIRD_PARTY_REGULATED` | PHI (HIPAA), PII (state laws), trade secrets, NAIC-regulated insurance data, financial data with regulatory hooks | Independent regulatory regimes layered on top of A/C analysis |

A prompt may have multiple classes; the analyzer flags every class present. The escalating order (low risk → high risk) is roughly the table order top-to-bottom.

---

## Factors and bands

Factors are ordered from most-restrictive to least. The analyzer runs all factors and reports every triggered factor; the final band is the most restrictive triggered.

### F1. Consumer surface + any matter-touching content → STOP

**Trigger:** Surface tier is `consumer` (per `surface_profiles.md`) AND any content class above `PUBLIC_LEGAL` is present.

**Cite:** [§ 1 — Heppner, all three A/C elements failed because of consumer Claude ToS]; [§ 5 — ABA 512 confidentiality + boilerplate-insufficient]; [§ 7 — DC Bar Op 388: free public versions are off-limits].

**Mitigation:** Switch to enterprise/API/on-prem tier OR strip prompt to `PUBLIC_LEGAL` only.

**Rationale:** Heppner is squarely on point — Anthropic's consumer ToS at issue in Heppner is materially the same posture as ChatGPT consumer, Gemini consumer, etc.

---

### F2. PRIVILEGED_COMMUNICATION content + any non-on-prem surface → STOP

**Trigger:** Content includes `PRIVILEGED_COMMUNICATION` AND surface is not `on-prem`.

**Cite:** [§ 1 — Heppner element 1: AI is not an attorney]; [§ 1 — Heppner non-alchemy: sharing with counsel after the fact does not retroactively privilege].

**Mitigation:** Move to on-prem surface OR remove the privileged communication from the prompt. There is no consent path that cures this — even with informed client consent, the act of routing privileged communications through a third-party AI surface is independently a confidentiality concern under Model Rule 1.6.

---

### F3. Self-learning surface + matter-related content + no informed client consent → STOP

**Trigger:** Surface trains on inputs by default (per `surface_profiles.md`) AND content class is `CLIENT_IDENTIFIABLE` or higher AND `consent != yes`.

**Cite:** [§ 5 — ABA 512: "a client's informed consent is required prior to inputting information relating to the representation into such a GAI tool"]; [§ 5 — ABA 512: boilerplate insufficient].

**Mitigation:** (a) Obtain specific informed consent meeting ABA 512 standards (not boilerplate); OR (b) switch to a surface with no-train default; OR (c) redact to `HYPOTHETICAL_NO_ID` or below.

---

### F4. Active or anticipated criminal matter + any non-on-prem surface + matter-touching content → STOP

**Trigger:** Posture litigation status is `anticipated_criminal` or `active_criminal` AND surface is not `on-prem` AND content class is `CLIENT_IDENTIFIABLE` or higher.

**Cite:** [§ 1 — Heppner: criminal posture, government obtained AI Documents via search warrant]; [§ 4 — FRCrimP 16(b)(2)(A) was not the rule that protected, because warrant ≠ discovery].

**Mitigation:** On-prem only. The Heppner facts (Anthropic ToS, search warrant exposure) do not leave a path for any third-party surface to be safe in active or imminent criminal exposure.

---

### F5. THIRD_PARTY_REGULATED content + non-on-prem surface → STOP

**Trigger:** Content includes PHI, regulated PII, trade secrets, or industry-specific regulated data (NAIC, PCI, etc.) AND surface is not `on-prem`.

**Cite:** Beyond the privilege/WP framework — independent regulatory regimes (HIPAA, state PII statutes, NAIC AI Bulletin requirements). [§ 5 — ABA 512 confidentiality more generally].

**Mitigation:** On-prem only, or specifically negotiated BAA / DPA with vendor that addresses the regulatory regime.

---

### F6. Enterprise surface + MATTER_FACTS or higher + civil posture + no informed consent → CAUTION

**Trigger:** Surface tier is `team`, `enterprise`, or `api` AND content includes `MATTER_FACTS` AND posture is civil (active or anticipated) AND `consent != yes`.

**Cite:** [§ 5 — ABA 512 informed consent for self-learning OR for "significant decision in the representation"]; [§ 2 — Warner: civil work product survives waiver-to-AI BUT is still subject to ABA confidentiality independently]; [§ 3 — Morgan: AI tool identity is itself discoverable].

**Mitigation:** Obtain informed client consent (specific, not boilerplate) per ABA 512 standards. Document which surface is being used (Morgan).

---

### F7. ATTORNEY_MENTAL_IMPRESSIONS + non-on-prem surface (any tier) → CAUTION

**Trigger:** Content includes attorney mental impressions / strategy / theory of case AND surface is not `on-prem`.

**Cite:** [§ 1 — Heppner work-product analysis: "the doctrine's purpose is to protect lawyers' mental processes"]; [§ 4 — FRCP 26(b)(3) protects mental impressions of attorney's strategy].

**Mitigation:** Strongest case for protection is on-prem. If using enterprise surface, ensure: (a) civil posture, (b) prepared in anticipation of litigation, (c) ZDR contract in effect, (d) document the surface in case Morgan-style discovery follows.

---

### F8. CLIENT_IDENTIFIABLE content + enterprise surface + no informed consent → CAUTION

**Trigger:** Content includes `CLIENT_IDENTIFIABLE` AND surface tier is `team`/`enterprise`/`api` AND `consent != yes`.

**Cite:** [§ 5 — ABA 512 confidentiality: must evaluate disclosure risk]; [§ 5 — ABA 512: ToS review baseline].

**Mitigation:** Either (a) obtain informed consent OR (b) redact identifiers.

---

### F9. Active civil litigation + any third-party surface → CAUTION (Morgan-identity flag)

**Trigger:** Posture litigation status is `active_civil` AND surface tier is anything other than `on-prem`.

**Cite:** [§ 3 — Morgan: identity of AI tools used is discoverable, even when content is work-product protected].

**Mitigation:** Document the AI tool used in the matter; expect the tool's identity to be discoverable. Consider whether the *fact of use* signals strategy.

---

### F10. Florida overlay — court filing context + any AI use → CAUTION (disclosure required)

**Trigger:** Jurisdiction is `florida` AND prompt is for output that will be filed with a Florida court (e.g., drafting a brief, motion, response).

**Cite:** [§ 6 — Fla. 17th Jud. Cir. AO 2026-03-Gen and Fla. 7th Jud. Cir. AO G-2026-045-SC: disclosure and certification of AI use in filings required].

**Mitigation:** Comply with the relevant local AO's certification requirement at filing. This is not a do-not-use flag; it is a disclose-when-filing flag.

---

### F11. ON-PREM surface + non-public content → CAUTION (Heppner element 1 doctrinal note)

**Trigger:** Surface tier is `on-prem` AND content is `PRIVILEGED_COMMUNICATION` or `ATTORNEY_MENTAL_IMPRESSIONS`.

**Cite:** [§ 1 — Heppner element 1: AI is not an attorney; this analysis applies regardless of where the AI runs].

**Mitigation:** Treat as best-available, not invulnerable. The Warner/Morgan civil work-product protection is the practical shield. Privilege as such remains doctrinally vulnerable even on-prem because the model is still not an attorney.

---

### F12. PUBLIC_LEGAL only + any surface → SAFE

**Trigger:** Content is exclusively `PUBLIC_LEGAL` (no client information, no mental impressions, no matter facts, no regulated data).

**Cite:** No privilege/WP issue arises; ABA 512 § B confidentiality not triggered because no representation-related information is being input.

**Note:** Quality and accuracy concerns from ABA 512 § A (competence), § D (candor toward tribunal) still apply — verify outputs before use. But the Privilege Sentinel band is SAFE.

---

## How the analyzer composes the output

After running all factors:

1. **Band** = max severity of triggered factors.
2. **Triggered factors** = list of (factor ID, trigger summary, cite) for each factor that fired.
3. **Discovery-impact line** = one-sentence projection of what happens if this prompt content surfaces in discovery, given the posture. Examples:
   - STOP / criminal: "If seized via search warrant or subpoena, the government will have direct access to your privileged content; *Heppner* will likely control."
   - STOP / civil consumer: "If the opposing party learns you used [surface] (Morgan: identity is discoverable) and moves to compel, the prompt content will be produced and is unlikely to survive a privilege challenge."
   - CAUTION / civil enterprise: "If discovered, work-product protection is your shield under *Warner / Morgan*, but the AI tool's identity will be produced and may itself signal strategy."
   - SAFE: "No privilege or work-product material at risk."
4. **Redacted-safe rewrite** = template-based mask of:
   - Personal names → `[NAME]`
   - Entity names → `[ENTITY]`
   - Dollar amounts (`$X[,Y][.Z]`) → `[AMOUNT]`
   - Dates (numeric and "Month DD, YYYY") → `[DATE]`
   - Matter numbers (e.g., `25-cv-12345`, `Case No. ...`) → `[MATTER_NO]`
   - Email addresses, phone numbers → `[CONTACT]`
   - Quoted speech blocks attributed to a person → `[QUOTED_STATEMENT]`
   
   The rewrite is a starting point. The analyzer must explicitly state in the output: "Redaction is template-based. Review before sending."

5. **Recommended next step** for each band:
   - SAFE: "OK to send."
   - CAUTION: list the mitigations from the most-restrictive triggered factor.
   - STOP: list the surface or content changes that would move to CAUTION or SAFE.
