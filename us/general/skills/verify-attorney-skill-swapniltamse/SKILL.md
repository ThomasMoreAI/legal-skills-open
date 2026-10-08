---
name: verify-attorney-skill-swapniltamse
title: Verify Attorney
description: Use when a user, or someone they are helping, wants to check whether a lawyer, law firm, "immigration consultant", or "notario" is legitimate or a scam before hiring or paying. Triggers include "is this lawyer legit", "is this a notario scam", "check this attorney", "should I pay this immigration firm", a solicitation promising a guaranteed visa or green card, or vetting any attorney before signing a retainer.
author: swapniltamse
author_url: https://github.com/swapniltamse/verify-attorney-skill
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: general
language: en
---

# Verify Attorney

## Overview

Check whether a lawyer or legal-services provider is real, licensed, and safe to hire before the user (or a friend, family member, or job seeker they are helping) pays or signs anything. This is highest-value in immigration, where "notario" and "consultant" fraud targets visa holders, but the licensure checks apply to any US attorney.

**Core principle: verify licensure at the state bar first. A legitimate lawyer is one you can look up by name and bar number.** Everything else (fees, guarantees, contract) refines the read, but an unverifiable license is disqualifying on its own.

**Guardrail:** this skill assesses whether a provider is legitimate and safe. It does not give legal advice or immigration-strategy advice. Keep the output to legitimacy and hiring safety only.

## When to use

- "Is this lawyer legit", "is this a scam", "check this attorney or firm"
- A solicitation promising a guaranteed visa, green card, or case outcome
- Anyone advertising as a "notario publico" or "immigration consultant" for legal help
- Before signing a retainer or paying a new attorney

## Step 1 — Get a nameable, lookup-able identity

You cannot verify what you cannot name. Establish: the individual attorney's full name, the state(s) they claim to practice in, and ideally a bar number. If the provider will not give a named attorney and a jurisdiction, that refusal is itself a strong red flag. A firm name alone is not enough; representation is done by a licensed person.

## Step 2 — Run the checks

The first two decide most cases.

1. **Licensure at the state bar (authoritative).** Look the attorney up in the relevant state bar's official directory. Confirm the license is active and in good standing, and read the public disciplinary history. Every US state bar has a free online lookup. This is the primary verification; no bar record means treat as unlicensed. **If a supplied bar number resolves to a different person than the name in the message, that is impersonation of a licensed attorney: the strongest possible scam signal. Treat it as Scam regardless of any other terms, and do not be softened by the fact that a real license exists behind that number, because it belongs to someone else.**

2. **Attorney vs consultant or notario (unauthorized practice of law).** Only a licensed attorney or a DOJ EOIR accredited representative may give legal advice or represent someone in US immigration. "Notario publico," "immigration consultant," "visa agent," or "document preparer" are not law licenses. Advertising "notario" as an immigration credential is the classic notario-fraud pattern (in the US a notary cannot give legal advice, unlike the Latin American meaning of the word).

3. **Guaranteed outcome.** No ethical lawyer can guarantee approval of a green card, visa, or any case, because it is a government decision they do not control. A guarantee, or "money back if denied," is a loud disqualifying tell.

4. **Written engagement letter.** Legitimate lawyers provide a written retainer or engagement agreement stating scope and fees. "No contract needed, you have my word" removes your only paper trail and is a red flag.

5. **Payment structure and method.** Watch for cash, Zelle, Venmo, gift-card, or crypto only, and full fees demanded upfront before work begins. Those rails are irreversible with no recourse, which is why scammers prefer them. Legit firms take traceable payment, often stage fees, and hold unearned fees in a client trust account.

6. **Identity and footprint.** A real practice has a verifiable firm address, a named attorney whose bar record matches, and a genuine web and review presence. Check domain age via RDAP (`https://rdap.org/domain/<domain>`); a days-old, keyword-stuffed, hyphenated domain (`usimmigrationhelp-pros.com`) impersonating officialdom is a scam signal. Absence of any footprint, while claiming "thousands of cases," is corroborating, not conclusive.

7. **Pressure and channel.** Manufactured urgency ("spots limited this month", immigration has no spots), unsolicited contact targeting immigrants by name, and refusal to meet or be identified are pressure tactics to stop you from checking.

## Step 3 — Verdict and action

| Verdict | What it means | Action |
|---|---|---|
| Legit | Licensed, in good standing, written agreement, traceable fees | Safe to proceed. Still get everything in writing |
| Caution | Real license, record matches the name, but red-flag terms (vague fees, no clear scope, pressure) | Get a written engagement letter and fee schedule before paying. Consider a second opinion |
| Scam or UPL | No verifiable license, a bar number that names someone else, notario/consultant posing as counsel, guarantee, or irreversible upfront demand | Do not pay or send documents. Report (see sources). If money was sent by Zelle/crypto, warn it is likely unrecoverable |

## Authoritative sources

| Purpose | Source |
|---|---|
| License status and discipline | The relevant state bar's official attorney lookup |
| Immigration representation rules and scam warnings | USCIS "Find Legal Services" and "Common Scams" (uscis.gov/scams-fraud-and-misconduct) |
| Accredited non-attorney reps | DOJ EOIR list of recognized organizations and accredited representatives |
| Supporting membership signal | AILA member directory (not proof of licensure) |
| Domain age | RDAP: `https://rdap.org/domain/<domain>` |
| Reporting fraud | FTC reportfraud.ftc.gov, and the state attorney general / consumer protection office |

## Quick reference

| Check | Legit signal | Scam signal |
|---|---|---|
| License | Active bar record, matches name | No record; number names someone else; won't give a name |
| Credential | Licensed attorney or DOJ-accredited rep | "Notario" or "consultant" giving legal advice |
| Outcome | No guarantees | "Guaranteed" approval |
| Contract | Written engagement letter | "No contract, my word" |
| Payment | Traceable, staged, trust account | Cash/Zelle/crypto only, full upfront |
| Footprint | Real address, aged domain, reviews | Days-old lookalike domain, none found |

## Common mistakes

- Trusting a firm name without a named, bar-verified attorney. Verify the person, not the brand.
- Accepting a bar number without confirming the name on record matches. A number that names a different person is impersonation, not a real credential.
- Treating "immigration consultant" or "notario" as equivalent to a lawyer. In the US it is not.
- Judging on polish or a professional-looking site. The bar lookup and the guarantee tell you more than design.
- Calling "no reviews found" proof of fraud. It is supporting evidence; the license check is the decider.
- Confusing a look-alike scam domain with a real firm of a similar name. Break the tie with the bar lookup of the named attorney.
- Straying into legal or visa-strategy advice. This skill only judges whether the provider is legitimate and safe.
