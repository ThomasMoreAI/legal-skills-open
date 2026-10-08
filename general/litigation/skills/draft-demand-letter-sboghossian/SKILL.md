---
name: draft-demand-letter-sboghossian
title: Demand Letter (Letter Before Action / Mise en Demeure)
description: Use when drafting a formal demand letter (letter before action / mise en demeure) requiring payment, performance, cessation of conduct, or retraction. P0 litigation skill covering required inputs, structure, tone, and the jurisdiction-specific service and formality requirements for LB (notarial/bailiff service), KSA (licensed lawyer, bailiff), UAE (notarized via Notary Public), and common-law jurisdictions. The letter must be precise, factual, and function as admissible court evidence.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/draft/draft-demand-letter
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: litigation
language: en
---

# Demand Letter (Letter Before Action / Mise en Demeure)

## When to use this

A demand letter is the last formal step before litigation or arbitration. It creates a paper trail, establishes a record that the other party was given an opportunity to comply, and in several jurisdictions is a **legal prerequisite** to commencing certain court actions.

Use this skill when:

- A party has not paid an invoice, debt, or contractual sum and informal requests have failed.
- A party is in breach of contract (non-performance, defective performance, delay) and you want to trigger a cure period and preserve rights.
- An IP infringement has been identified and you want to demand cessation before filing.
- A regulatory complaint, arbitration, or court filing is intended and you need a pre-filing record.
- A personal-injury or tort claim requires pre-suit demand.

**When this is not enough:** some jurisdictions (UAE notarized demand, Lebanese mise en demeure via bailiff) require specific service formalities for the demand to start a statutory period running. Confirm service requirements before drafting.

## Required inputs

| Input | Why it matters | Default |
|-------|----------------|---------|
| Sender (party making demand) | Letterhead, legal name, address, contact | — |
| Recipient (party receiving demand) | Full legal name and registered address; if company, use registered office | — |
| Factual chronology | Specific dates, amounts, contract references — courts will see this | — |
| The demand (specific and quantified) | Vague demands cannot be enforced; specify amount, action, or cessation | — |
| Response deadline | Starts the clock; governs when you can file | 14 days (commercial); 7 days (urgent/injunctive matters) |
| Consequence of non-compliance | Specifies next step: filing in which court/tribunal, arbitration under which rules | — |
| Governing contract / applicable law | Identifies legal basis for the demand | — |

## Optional inputs

- List of documents attached (invoices, contracts, prior correspondence)
- Reservation of rights language (interest, costs, punitive damages)
- Request for specific documentation from recipient
- Without-prejudice vs. open letter decision (see below)

## Standard document structure

### 1. Sender header
Sender's full name (or law firm name), address, phone, email. Date. File / matter reference.

### 2. Recipient block
Full legal name, registered address. Mark "BY [delivery method]" prominently.

### 3. Subject line
"RE: [Brief description] — Formal Demand for [Payment / Performance / Cessation]"
Example: "RE: Outstanding Invoice #2024-112 dated 15 March 2024 — Formal Demand for Payment"

### 4. Salutation
"Dear [Mr/Ms/Title Last Name]," — avoid "Dear Sir or Madam" in direct-party correspondence.

### 5. Statement of facts
Chronological, specific, factual — no argument or emotion. Each sentence should be verifiable:
- "On [date], [Party A] and [Party B] entered into a [type of agreement], a copy of which is attached as Exhibit A."
- "Under Clause [X] of the Agreement, [Party B] was required to [obligation] by [date]."
- "As of the date of this letter, [Party B] has failed to [obligation] despite [number] written reminders dated [dates]."

Do not characterize the recipient's conduct with pejoratives ("fraudulent", "dishonest") unless those characterizations are legally necessary and provable — inflammatory language weakens the letter.

### 6. Legal basis
State the legal ground for the demand briefly:
- Contract clause number.
- Statutory provision (e.g., Article [X] of the UAE Commercial Transactions Law; Lebanese Code of Obligations Art. [X]).
- Common-law principle (e.g., "Under English law, [Party B] is in breach of its obligation to [X], giving rise to a claim in damages.").

Do not write a legal memorandum here — one to three sentences is enough. The purpose is to signal that the demand is grounded.

### 7. The demand
State precisely what is being demanded:
- **Payment**: "We hereby demand payment of USD [amount] (plus interest at [rate]%) within [X] days of the date of this letter."
- **Performance**: "We hereby demand that you [specific action] by no later than [date]."
- **Cessation**: "We hereby demand that you immediately cease and desist from [specific conduct] and provide written confirmation of cessation within [X] business days."

One demand per letter is clearest; if multiple demands, number them.

### 8. Consequence of non-compliance
Be specific. Generic "legal action" threats are discounted.
- "If payment is not received by [date], we will without further notice file proceedings in [specific court / arbitral tribunal] for the full outstanding amount plus accrued interest, costs of these proceedings, and legal fees."
- "We reserve all rights to seek injunctive relief."

### 9. Reservation of rights
Standard clause: "This letter is written without prejudice to any and all further rights and remedies available to [Sender], including the right to claim additional damages, interest, costs, and penalties. Nothing in this letter constitutes a waiver of any such right."

### 10. Closing
Professional close. Sender's name, title, contact details. Signature (original where required for notarial service).

### 11. Annexes
List attached documents. Each referenced in the factual section.

## Without-prejudice vs. open letter

| Type | When to use | Effect |
|---|---|---|
| **Open letter** | When the letter is designed as a formal record, will be shown to a court, or triggers a statutory notice period | Admissible in evidence; creates public record |
| **Without-prejudice** | When you want to make a settlement proposal that cannot be used against you in litigation | Cannot be adduced in evidence on the question of liability; settlement discussions protected |

**CRITICAL:** A demand letter that states an entitlement is NOT a settlement proposal. Mark it "Open" (or do not mark it at all). Mark without-prejudice only if it contains a settlement offer. A poorly marked WP letter that turns out to be admissible can still be used to prove the claim.

## Jurisdictional service and formality requirements

### Lebanon
- **Mise en demeure** may require service via bailiff (huissier de justice) or registered mail with receipt to constitute formal legal notice in certain proceedings (e.g., to start running a statutory default interest period under Lebanese Code of Obligations and Contracts).
- For commercial disputes: registered letter with acknowledgment of receipt commonly accepted.
- For rent/eviction: specific service requirements under Lebanon Rent Law.
- **Arabic version** required for Lebanese court proceedings; bilingual acceptable.

### KSA
- Formal demand letters in litigation matters are typically sent by the licensed lawyer on record.
- For enforcement via Saudi courts: a demand via the Notary Public or notarized letter provides stronger evidence than a simple email or letter.
- For commercial arbitration (SCCA): demand letter should reference the arbitration clause and state the SCCA rules.
- **Arabic version** mandatory for court filings; bilingual acceptable as courtesy.

### UAE
- **Notarized demand letter** via a Notary Public is a common requirement as a condition precedent to certain court actions (e.g., before filing certain real-estate or rent disputes before the Rent Dispute Settlement Committee; before filing dishonored-cheque claims).
- Dubai and Abu Dhabi courts: notarized demand generally strengthens the evidence base.
- **Abu Dhabi Global Market (ADGM) / DIFC Courts**: demand letters follow English-law conventions; no notarization required, but service confirmation (recorded delivery, email read receipt) is advisable.
- **Arabic version**: for federal courts, Arabic controls; DIFC/ADGM proceedings may be in English.

### Egypt
- Demand letter sent via bailiff (mahkama) or registered mail provides formal legal notice.
- Interest on commercial debts runs from date of formal demand.
- **Arabic** required for court filings.

### France
- **Mise en demeure** may be sent by regular registered mail or via huissier (process server) — the latter preferred for important matters.
- Some statutory provisions require mise en demeure before interest runs or before certain legal actions become available.
- Courts expect standard mise en demeure format.

### UK (England & Wales)
- Pre-Action Protocols require a formal letter before claim in most civil proceedings (CPR Pre-Action Practice Direction).
- Prescribed content: brief summary of claim, documents relied on, ask for response within reasonable period (typically 14-28 days).
- Failure to comply with Pre-Action Protocol can result in cost sanctions.

### US
- No universal requirement, but demand letters are standard practice.
- Specific statutory frameworks (FDCPA for debt collection; state consumer-protection acts) prescribe content for certain demand letters.
- Attorney's demand letter on letterhead signals seriousness.

## Tone and quality standards

- **Professional, not aggressive.** The letter will likely be read by the recipient's counsel and potentially a judge. Inflammatory language reduces its effectiveness and may expose the sender to defamation risk.
- **Specific, not vague.** Every fact cited should be provable from attached documents.
- **One ask.** The demand should be clear. Multiple conditional asks create ambiguity.
- **Deadline is firm.** Set a realistic deadline and mean it. Extending deadlines repeatedly undermines credibility.
- **No legal advice in content.** The letter states the legal basis; it is not a memo explaining all possible outcomes.

## Common mistakes

1. **Omitting exhibit list** — "see attached invoice" without attaching it is procedurally weak.
2. **Vague demand** — "pay what you owe" is unenforceable; specify the exact amount.
3. **Wrong deadline** — setting a 24-hour deadline on a cross-border commercial debt where a 14-day minimum is expected signals unreasonableness.
4. **Inflammatory language** — words like "fraud", "theft", "criminal" used without legal precision invite defamation counterclaims.
5. **Missing without-prejudice distinction** — a letter that opens settlement negotiations without the WP mark is fully admissible.
6. **Wrong service method** — sending by email alone in a jurisdiction where notarized or registered-mail service is required means the notice period doesn't start.

## Related skills

- [[draft-cease-and-desist]] — variant demand focused on IP infringement and tortious conduct cessation
- [[draft-notice-of-default]] — formal default notice under a finance agreement triggering cure and acceleration
- [[review-contract]] — review the underlying contract before drafting to confirm the legal basis for the demand
- [[kb-litigation-mena]] — procedural requirements in MENA courts for pre-action steps
