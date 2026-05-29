# Matter Type Profile — [Matter Type Name]

**Profile version:** [v1.0]
**Maintained by:** [Firm / Practice Group / LPM team]
**Last reviewed:** [Date]

---

## Purpose

This profile tells matter-intake-scoping what to look for, what to check, and what to flag when running pre-engagement mode on a [matter type] mandate. It routes the skill to the relevant shared-knowledge files and identifies the standard knowledge domains that should be addressed in the client brief.

The LPM uses this profile to structure the brief. The content of the shared-knowledge files — the legal and operational substance — is populated by the firm and used by attorney skills for analysis. The LPM skill flags; attorney skills determine.

---

## Matter type description

[One paragraph describing this matter type: what it typically involves, who the key parties are, what the LPM's typical role is, what makes it operationally distinct from other matter types.]

---

## Standard knowledge domains to check

For each domain, the profile identifies the relevant shared-knowledge file and what the LPM should look for in the client inputs. If the client inputs don't address the domain, it should appear in the brief as an external knowledge flag.

### [Domain 1 — e.g., Document execution requirements]

Shared-knowledge file: `shared-knowledge/[category]/[filename].md`
Status: [Available / Stub — content to be populated / Not yet created]

What to look for in client inputs: [What would the client have said or provided if they'd addressed this domain?]

If not addressed: Flag as: *[Inferred from general knowledge: [Domain] requirements are standard for this matter type. I'd suggest the partner confirms [specific issue] before scope is finalised. Recommend specialist confirmation.]*

---

### [Domain 2 — e.g., Regulatory filing requirements]

Shared-knowledge file: `shared-knowledge/[category]/[filename].md`
Status: [Available / Stub / Not yet created]

What to look for in client inputs: [Description]

If not addressed: Flag as: *[Inferred from general knowledge: [Description of standard requirement for this matter type]. This has not been addressed in the client inputs. I'd suggest the partner considers whether to include this in the proposal.]*

---

### [Domain 3 — e.g., Jurisdiction-specific requirements]

Shared-knowledge file: `shared-knowledge/jurisdictions/[jurisdiction].md`
Status: [Available / Stub / Not yet created]

What to look for in client inputs: [Description]

If not addressed: Flag as: *[Inferred from general knowledge: [Description]. Recommend review of jurisdiction-specific requirements before scope is finalised.]*

---

*[Add further domains as relevant. Each domain should have a corresponding shared-knowledge file, even if that file is currently a stub.]*

---

## Standard assumption categories for this matter type

[List the assumption categories that are typically most important and most failure-prone for this matter type. This feeds the assumptions calibration step in Mode 1.]

| Category | Typical importance | Notes |
|---|---|---|
| [Quantitative parameters] | [High / Medium / Low] | [What parameters matter most on this matter type] |
| [Regulatory timeline] | [High / Medium / Low] | [Which jurisdictions / bodies are most variable] |
| [Client-side] | [High / Medium / Low] | [Common client-side assumptions that fail] |
| [Counterparty] | [High / Medium / Low] | [Counterparty cooperation patterns] |
| [Data quality] | [High / Medium / Low] | [Common data quality issues on this matter type] |
| [Resource] | [High / Medium / Low] | [Specialist or LC availability patterns] |

See `references/standing-assumptions.md` for the firm's performance data on each assumption category.

---

## Common gaps in client inputs

[What information is typically missing or incomplete when a client first provides a mandate of this type? This helps the LPM build a more complete open questions list without having to discover these gaps from scratch each time.]

| Typical gap | Impact if unresolved | Where to look / how to flag |
|---|---|---|
| [Gap 1] | [Scope / fee / timeline impact] | [Where it typically surfaces / how to raise it] |
| [Gap 2] | [Impact] | [Handling] |

---

## Common source conflicts

[What inconsistencies typically appear across client inputs on this matter type? Helps the LPM know what to look for during conflict detection.]

| Typical conflict | Why it occurs | How to surface it |
|---|---|---|
| [Conflict 1] | [Root cause] | [How to present it in the brief] |
| [Conflict 2] | [Root cause] | [Handling] |

---

## Scope boundary considerations

[What is typically in scope and typically excluded on this matter type? What are the common "I thought you were handling that" conversations?]

Typically in scope: [List]
Typically excluded: [List — these are good candidates for explicit scope exclusions in the brief]
Common ambiguity: [What tends to fall in the grey zone between in and out]

---

## LPM involvement — typical shape

[What does the LPM typically own, facilitate, and monitor on this matter type? This gives the LPM a starting point for the involvement definition conversation with the partner.]

Typically owned by LPM: [List]
Typically facilitated by LPM: [List]
Typically monitored and flagged: [List]
Typically not LPM: [List — important to be explicit about what the LPM doesn't do on this matter type]

---

## Shared-knowledge files referenced by this profile

| File | Domain | Status |
|---|---|---|
| `shared-knowledge/[path]` | [Domain] | [Available / Stub / To be created] |

---

*This profile is maintained by [Firm / Practice Group]. It reflects operational experience on [matter type] mandates and is not legal advice. The LPM skill uses this profile to structure the pre-engagement brief; legal analysis of any flagged issues belongs to the relevant attorney skill or specialist counsel.*
