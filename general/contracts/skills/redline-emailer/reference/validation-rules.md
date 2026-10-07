# Redline Emailer — Validation Rules

Run these checks before delivering the email. Fix any failures silently —
do not show the validation output to the attorney. Just deliver a clean email.

---

## Universal Checks (both recipient types)

### 1. Completeness

Every change from the extracted change list must appear in the email.
Cross-check: count changes extracted vs. changes mentioned.

If a change was intentionally omitted (trivial formatting, punctuation,
renumbering), note it at the bottom of the email:
"Minor formatting and conforming changes were also made but are not listed here."

### 2. No Document Artifacts

The email must not contain:
- XML tags or markup (`w:del`, `w:ins`, etc.)
- Tracked-change notation (raw strikethrough markers, revision IDs)
- PDF extraction artifacts (page numbers, headers/footers from the source doc)
- Placeholder brackets like `[TBD]` (unless the contract itself has open items)
- File paths or technical references to document processing

### 3. Placeholder Fill

`[Attorney Name]`, `[Firm Name]`, `[Client Name]`, `[Client First Name]`,
`[Contract Title]`, `[Other Party]`, `[Counsel Name]` — fill all of these
if the information was provided during intake or extracted from the document.

If not provided, keep the bracket placeholder. Do not guess names.

### 4. No Legal Advice

The email summarizes changes. It does not advise the recipient on whether
to accept or reject them. These phrases should not appear unless the
attorney explicitly requested that framing:
- "you should accept"
- "I recommend rejecting"
- "this is a good/bad deal"
- "you must agree to"
- "I advise"

The exception: factual framing like "this protects you by..." is fine
in client emails — it describes the effect of a clause, not legal advice.

---

## Client-Specific Checks (Template A only)

### 5. Legalese Scan

Search the generated email for every term in the Banned Terms table
(from email-templates.md). If any banned term appears, replace it with
the plain-English equivalent before delivery.

### 6. Section Number Context

If a section number appears in the email (e.g., "Section 4.2"), it MUST
be accompanied by a topic description:
- Good: "Section 4.2, which covers payment terms"
- Bad: "We revised Section 4.2"

Bare section numbers without topic context fail validation. Either add
the topic or remove the section number.

### 7. Explanation Check

For each change mentioned in the email, verify it includes a
"what it means for you" component — not just "what changed."

- Good: "We changed the termination notice from 30 to 60 days. This gives you more time to transition if the contract ends."
- Bad: "We changed the termination notice from 30 to 60 days."

If a change is genuinely self-explanatory, a brief impact note still helps:
"...which is standard for this type of agreement."

### 8. Reading Level

The email should be understandable by a non-lawyer. If any sentence
requires legal training to parse, rewrite it. Test: could a business
owner with no legal background understand every sentence? If not, simplify.

---

## Counsel-Specific Checks (Template B only)

### 9. Section References

Every substantive change must include a section number, exhibit reference,
or defined-term reference. Changes described without location references
fail validation.

- Good: "Section 5.1 (Limitation of Liability): revised the cap from..."
- Bad: "The liability cap was revised from..."

### 10. Brevity

The key changes section should not exceed ~15 bullets. If the redline
has more substantive changes:
- Group related changes under topic headings
- Add a note: "Additional conforming changes have been made throughout."
- Prioritize the most commercially significant changes

### 11. Neutral Tone

Scan for characterizing or adversarial language. Remove or neutralize:
- "concession" / "we conceded"
- "we won" / "we secured"
- "they gave up" / "they backed down"
- "favorable" / "unfavorable"
- "aggressive" / "unreasonable"
- "our client insists" (state the position without the verb)

State facts about what changed. Let the redline speak for itself.

### 12. Professional Salutation

Must use:
- "Dear [Full Name]," or
- "Dear Counsel,"

Never:
- "Hi [First Name]"
- First name only
- "To Whom It May Concern"
