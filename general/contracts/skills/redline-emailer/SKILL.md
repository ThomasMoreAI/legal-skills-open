---
name: redline-emailer
title: Input Modes
description: 'Translates contract redlines into client-ready or opposing-counsel emails. Accepts three input modes: (1) a .docx with tracked changes, (2) a redlined PDF with strikethrough/underline formatting, or (3) a verbal description of changes. Produces a copy-paste-ready email, tone-matched to the recipient: plain-English for own clients, professional legal cover for opposing counsel. Use when the attorney says "write the redline email", "summarize these changes for the client", "draft a cover email for the redline", "explain these edits to opposing counsel", or "turn this redline into an email". Do NOT use for drafting contracts or generating redlines — use the relevant drafter skill. Do NOT use for diffing two clean (non-redlined) document versions.'
author: bstevescherer
author_url: https://github.com/bstevescherer/heycounsel-community/tree/main/skills/redline-emailer
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: contracts
language: en
---

## Input Modes

| Mode | Trigger | Input |
|------|---------|-------|
| A: .docx Tracked Changes | User provides a `.docx` with Track Changes | Parse Word XML for `w:del`/`w:ins` elements |
| B: Redlined PDF | User provides a `.pdf` with redline formatting | Parse PDF for strikethrough/underline/color-coded text |
| C: Verbal Description | User describes changes, no file | Work from the attorney's description |

Auto-detect the mode from what the user provides. See `references/intake-questions.md` Q1.

---

## Instructions

### Step 1: Load References

Read before doing anything:
- `references/intake-questions.md` — short intake flow (4 questions, most auto-detectable)
- `references/email-templates.md` — tone guides and structural templates for both recipient types
- `references/validation-rules.md` — quality checks per recipient type

### Step 2: Run Intake

Follow `references/intake-questions.md`. This should take 60 seconds or less.

**What you must know before proceeding:**
1. Input mode (auto-detect from file type)
2. Recipient: client or opposing counsel
3. Contract identity: title, parties
4. Special instructions (if any)

Do NOT re-ask questions the attorney already answered in their initial request.
If the attorney says "write the redline email for opposing counsel" and drops a
.docx, you have all four answers — go straight to Step 3.

### Step 3: Extract Changes

This step varies by input mode.

---

#### Mode A: .docx with Tracked Changes

Extract changes from Word XML. The .docx format uses the same elements that
`redline_engine.py` writes — we're reading them instead.

**Namespace:**
```
W = 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'
```

**Element patterns:**
- `<w:del>` → `<w:r>` → `<w:delText>` = deleted text
- `<w:ins>` → `<w:r>` → `<w:t>` = inserted text

**Extraction approach:**

1. Load the .docx with `python-docx`: `doc = Document(filepath)`
2. Walk `doc.element.body` looking for `{W}del` and `{W}ins` elements
3. **Substitutions:** When `w:del` and `w:ins` are siblings in the same `w:p`,
   they represent a substitution (old → new)
4. **Pure deletions:** A `w:del` with no adjacent `w:ins` = text was removed
5. **Pure additions:** A `w:ins` with no adjacent `w:del` = text was added
6. **Comments:** Parse `word/comments.xml` from the .docx zip archive for
   `w:comment` elements — these provide reviewer context for each change.
   Match comments to changes via `w:commentRangeStart` / `w:commentReference` IDs.

**Grouping:** For each change, find the nearest preceding paragraph with a
heading style (e.g., `Heading 1`, `Heading 2`) to determine which contract
section it belongs to. If no heading styles are used, fall back to pattern
matching: "Section X.X", "Article Y", numbered paragraphs.

**Output:** A structured change list:
```
[
  { section: "Section 4.2 — Limitation of Liability",
    type: "substitution",
    old: "twelve (12) months",
    new: "twenty-four (24) months",
    comment: "Per client instruction — doubled the liability cap" },
  ...
]
```

---

#### Mode B: Redlined PDF

Parse the PDF for redline formatting. Redlined PDFs come in two flavors —
detect which one and apply the right strategy.

**Format detection:** Scan the first 2-3 pages using `PyMuPDF` (`fitz`):

```python
import fitz
doc = fitz.open(filepath)
page = doc[0]
blocks = page.get_text("dict")["blocks"]
```

Check text spans for formatting flags:
- Strikethrough flag present → **Strikethrough + underline format**
- Red/colored text without strikethrough → **Track Changes exported to PDF**
- Neither → **Uncertain format** (trigger fallback)

**Strikethrough + underline format:**
- Spans with strikethrough flag = deleted text
- Spans with underline flag (especially if also colored/red) = inserted text
- The `fitz` span `flags` field: bit 0x100 = strikethrough (check via `span["flags"] & 2**8`)
- Group by surrounding text context and section headings

**Track Changes exported to PDF:**
- Look for visual patterns: red text, margin annotations, inline "[Deleted: ...]" text
- Balloon-style comments in margins may appear as separate text blocks positioned
  outside the main content area (check x-coordinate relative to page margins)
- This format is harder to parse reliably — extract what you can

**Fallback (uncertain format or low-confidence extraction):**
Present the extracted text to the attorney:
> "I extracted the following text from the PDF but I'm not fully confident
> in which parts are additions vs. deletions. Can you confirm or correct?"

Show the extracted text with your best guess at markup, and let the attorney
correct before proceeding to email generation.

**Grouping:** Same heading/section detection as Mode A, applied to the PDF text flow.

---

#### Mode C: Verbal Description

No document processing. The attorney describes the changes. Structure their
description into the same change list format during email generation.

If the description is unstructured, ask:
> "Can you organize by section or topic? For example: 'In the payment terms,
> we changed X to Y. In the liability section, we added Z.'"

If the attorney prefers to stay informal, work with what they give you.

---

### Step 4: Generate Email

Using the change list from Step 3 and the recipient type from Step 2:

1. Select the appropriate template from `references/email-templates.md`
   (Template A for client, Template B for counsel)
2. Map each change to the appropriate email section
3. Apply the tone rules for the selected recipient type
4. Check for tone calibration overrides (casual, contentious, sophisticated client, etc.)
5. Fill in subject line, greeting, body sections, and sign-off
6. Leave `[Attorney Name]` / `[Firm Name]` / `[Client Name]` as placeholders
   unless provided during intake

**For client emails:** Group changes by topic/impact, not section number.
Each change gets a "what it means for you" explanation.

**For counsel emails:** List changes by section number with precise references.
Keep each bullet to 1-2 sentences.

**For large redlines (20+ changes):** Prioritize commercially significant changes.
Group minor/conforming changes under a single note: "Additional conforming
changes have been made throughout."

### Step 5: Validate and Deliver

Run every applicable check from `references/validation-rules.md`:
- Universal checks 1-4 (both recipients)
- Client checks 5-8 (Template A only)
- Counsel checks 9-12 (Template B only)

Fix any failures silently. Do not show the validation output — just deliver
a clean email.

**Deliver** the email as plain text in the conversation, formatted and ready
to copy-paste. Include the subject line on its own line at the top.

**After delivery, offer:**
> "Want me to adjust the tone, add/remove anything, or generate a version
> for [the other recipient type]?"

---

## Performance Notes

- The intake should feel instant. Do not ask questions you can answer from
  the document or from context.
- If extraction (Mode A or B) takes more than a few seconds, give the attorney
  a brief status: "Reading the tracked changes..." / "Parsing the redlined PDF..."
- The email should read like YOU wrote it, not like a template was filled in.
  Vary sentence structure. Avoid repetitive bullet patterns.
- For Mode B (PDF), be honest about extraction confidence. A partially-correct
  extraction that the attorney can fix is better than a confidently-wrong one.
