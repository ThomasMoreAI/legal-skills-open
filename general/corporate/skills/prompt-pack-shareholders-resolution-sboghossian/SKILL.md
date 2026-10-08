---
name: prompt-pack-shareholders-resolution-sboghossian
title: Shareholders Resolution
description: Use when a company needs to draft a shareholders' (or members') resolution to formally approve a corporate action — director elections, capital increases, amendment of constitutional documents, major transactions, or any matter requiring shareholder approval under applicable company law or the company's own constitutional documents. MENA-specific guidance covers UAE onshore LLC requirements (notarized MOA amendments), DIFC/ADGM special/ordinary resolution thresholds, and KSA general assembly formalities.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/prompt-pack/prompt-pack-shareholders-resolution
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: corporate
language: en
---

# Shareholders Resolution

## When to use this

Use this skill when:
- A company needs to pass a formal shareholder resolution to approve a corporate action (director election, capital change, M&A transaction, constitutional document amendment).
- A company secretary is preparing resolutions for an Annual General Meeting (AGM) or Extraordinary General Meeting (EGM).
- A resolution is needed to authorize management to take a specific action on behalf of the company (borrowing, acquisition, entering a major contract).
- A resolution is needed to comply with a third party's requirement (e.g., a bank requires a certified shareholders' resolution authorizing the opening of a bank account or the taking of a security interest).

## Required inputs

| Input | Why it matters | Default if omitted |
|---|---|---|
| **Company name and jurisdiction** | Determines the applicable company law, voting thresholds, and quorum requirements | Ask |
| **Entity type** | LLC / PJSC / DIFC LLC / ADGM Ltd / Saudi LLC / KSC / Lebanese SAL | Ask; each has different resolution mechanics |
| **Matter to be approved** | Defines the resolution text | Ask; be specific |
| **Shareholding structure** | Needed to verify quorum and majority calculations | Ask |
| **Meeting type** | AGM / EGM / written resolution (circular resolution) | Ask; affects notice requirements |

## Optional inputs

- **Notice waiver** — if shareholders will waive the required notice period; all shareholders must consent in writing.
- **Proxy / power of attorney** — if any shareholder is acting through a representative, verify the power of attorney is valid in the relevant jurisdiction.
- **Arabic language requirement** — required for UAE onshore and KSA resolutions filed with the commercial register or notary.

## Document structure

A shareholders' resolution (whether passed at a meeting or as a written/circular resolution) has the following components:

1. **Header**
   - Name of company
   - Resolution type: Ordinary Resolution / Special Resolution / Written Resolution
   - Date and place of meeting (or date of written resolution)
   - Whether AGM or EGM

2. **Attendance and quorum verification**
   - List of shareholders present (in person or by proxy) and their shareholdings.
   - Calculation confirming quorum is met.
   - If quorum is not met: state that the meeting was adjourned and re-convened.

3. **Notice**
   - Confirmation that proper notice was given to all shareholders ([X days] written notice for AGM; [X days] for EGM).
   - Or: confirmation that all shareholders have signed a waiver of notice.

4. **Resolutions (the operative part)**

   Each resolution should:
   - Be numbered.
   - Begin with "RESOLVED THAT" or "IT IS RESOLVED THAT."
   - State the specific action clearly and completely (do not leave blanks or cross-references to separate documents without attaching them).
   - State the voting threshold required and confirm it was met.

   **Example resolution — appointment of director:**
   ```
   RESOLVED THAT [Name], of [address], be and is hereby appointed as a Director of the Company with immediate effect, and that the Board of Directors is authorized to take all steps necessary to give effect to this resolution including updating the register of directors and making any necessary filings with [Registry].
   ```

   **Example resolution — capital increase:**
   ```
   RESOLVED THAT the authorized share capital of the Company be increased from [AED/USD X] divided into [X] shares of [AED/USD Y] each to [AED/USD Z] divided into [Z] shares of [AED/USD Y] each, and that the Memorandum of Association be amended accordingly, and that the Board be authorized to allot and issue the new shares.
   ```

   **Example resolution — major transaction:**
   ```
   RESOLVED THAT the Company be authorized to enter into [describe transaction] with [counterparty] on the terms summarized in the document tabled at this meeting, and that the [Board / CEO / named officers] be authorized to execute all documents and take all actions necessary to consummate the transaction.
   ```

5. **Voting record**
   - Votes in favor: [number] shares, representing [X%] of total shares.
   - Votes against: [number] shares, representing [X%] of total shares.
   - Abstentions: [number] shares.
   - Resolution: PASSED / FAILED.

6. **Chairman's signature** (and secretary, if applicable)

7. **Annexes** — any document referred to in a resolution (term sheet, contract draft, amended MOA) should be attached and initialed.

## Voting thresholds by jurisdiction and resolution type

### UAE — onshore LLC (Federal Decree-Law No. 32 of 2021)

| Resolution type | Voting threshold | Notes |
|---|---|---|
| Ordinary matters (including director appointments) | Simple majority (>50%) of shares represented at meeting with quorum | AGM quorum: shareholders representing >50% of share capital |
| Amendment of Memorandum of Association | 75% majority (three-quarters of share capital, unless MOA specifies higher) | Must be notarized; filed with DED/Commercial Register |
| Capital increase / decrease | 75% majority | Notarization required; creditor protection rules for capital decrease |
| Change of business purpose | 75% majority | Notarization required |
| Conversion of company type | 75% majority | Additional regulatory requirements |
| Merger / acquisition | 75% majority (or unanimous per MOA) | Subject to specific merger procedures under Commercial Companies Law |
| Voluntary liquidation | 75% majority (or unanimous per MOA) | Court appointment of liquidator |

**UAE notarization requirement:** Any resolution that results in an amendment to the MOA (including capital changes, director changes in certain entity types, change of name or objects) must be executed before a UAE notary public and filed with the relevant Commercial Register.

### DIFC (DIFC Companies Law, DIFC Law No. 5 of 2018)

| Resolution type | Voting threshold |
|---|---|
| Ordinary Resolution | More than 50% of votes cast |
| Special Resolution | At least 75% of votes cast |
| Written Resolution | Ordinary: 50%+ of eligible voters; Special: 75%+ |

Special resolutions are required for: amendment of articles, reduction of capital, voluntary winding-up, approval of certain major transactions.

### ADGM (ADGM Companies Regulations 2020)

Similar to DIFC: ordinary resolutions by simple majority; special resolutions by 75%. Written resolutions recognized; unanimous written resolution available for certain matters.

### KSA (Saudi Companies Law)

| Entity type | Ordinary matters | Extraordinary matters |
|---|---|---|
| LLC (SRL) | Shareholders holding >50% of share capital | Shareholders holding 75% of share capital |
| JSC (Saudi Joint Stock Company) | Majority of shares represented at meeting with quorum | 2/3 of shares represented |
| PJSC listed company | As per CMA regulations | As per CMA regulations |

**KSA formalities:** General assembly resolutions of an LLC must be documented in Arabic; amendments to the articles must be notarized and registered with MISA.

### Lebanon (Lebanese Commercial Code)

| Resolution type | Threshold |
|---|---|
| Ordinary AGM / EGM | Simple majority of shares present; quorum = 50%+ of capital (first call) / 25% (second call) |
| Extraordinary matters (amendment of articles, merger, capital change) | 2/3 majority of shares present |

### Egypt (Egyptian Companies Law No. 159 of 1981)

| Resolution type | Threshold |
|---|---|
| Ordinary General Assembly | Majority of shares present; quorum = 50%+ (first call) / no quorum requirement (second call) |
| Extraordinary General Assembly | 2/3 majority of shares present; quorum = 75%+ (first call) / 50%+ (second call) |

## Drafting standards

- Write the operative resolution in plain, imperative terms. Avoid recitations ("WHEREAS...") — keep them minimal; put the substance in the "RESOLVED THAT" clause.
- Each resolution should be a single, complete statement of the action authorized. Do not draft compound resolutions that authorize multiple unrelated actions in one clause.
- For resolutions authorizing authority to named officers: specify their names and titles; authorize them "individually and separately" if it is impractical to require them all to act jointly.
- For bank account opening resolutions: banks often have their own required format; check with the relevant bank before drafting.
- Circular (written) resolutions: ensure you have confirmed that circular resolutions are permitted under the applicable law and the company's constitutional documents; some jurisdictions (and some company constitutions) require meetings for certain matters.

## Common mistakes

- **Resolution not specific enough.** "RESOLVED THAT the Board be authorized to take all necessary actions" is too vague for a bank or regulator to act on; specify the transaction, counterparty, and authorization.
- **Quorum not verified.** Filing a resolution that was passed without the required quorum invalidates the resolution.
- **Arabic version omitted for UAE/KSA filings.** Registries and notaries require Arabic versions; an English-only resolution will be rejected.
- **MOA amendment not notarized.** Shareholders resolving to amend the MOA without notarizing the amendment — the amendment is not valid in UAE and KSA until notarized and registered.
- **No authority to execute.** A resolution approving a transaction but not naming who is authorized to sign the transaction documents leaves implementation in limbo.

## Related skills

- [[prompt-pack-shareholders-agreement]]
- [[prompt-pack-share-purchase-agreement]]
- [[prompt-pack-regulatory-filing-checklist]]
- [[prompt-pack-related-party-transaction-policy]]
- [[heuristic-always-state-jurisdiction-first]]
