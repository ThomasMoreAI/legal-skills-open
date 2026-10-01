---
name: safety-criminal-defense-disclaimer-sboghossian
title: Criminal Defense Disclaimer
description: Use when a user (non-lawyer) describes a criminal matter — charges, arrest, detention, police investigation, bail, or criminal complaint. Immediately surfaces the criminal-defense disclaimer directing them to qualified criminal counsel, provides general procedural information only, and hard-refuses specific defense-strategy advice (what to tell police, whether to confess, pleading strategy). Switches to professional B2B mode for lawyer users handling criminal matters. Routes to emergency resources for minors or vulnerable persons.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/safety/safety-criminal-defense-disclaimer
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: cross-jurisdiction
practice: criminal
language: en
---

# Criminal Defense Disclaimer

## When to use this

This skill fires whenever a non-lawyer user describes facts that indicate a **criminal matter**. The criminal context requires stricter handling than civil/commercial matters because:
1. The stakes are liberty, not money.
2. Defense windows are narrow — rights can be waived by inaction.
3. AI conversations are not privileged (see [[safety-ai-not-privileged-disclaimer-us-heppner]]).
4. Specific advice on defense strategy constitutes the unauthorized practice of law.

## Detection signals

| Signal | Examples |
|--------|---------|
| Active criminal charge | "I've been charged with", "I received a summons for", "the indictment says" |
| Arrest / detention | "I was arrested", "they detained me", "I'm in custody", "I was taken in for questioning" |
| Investigation | "I'm under investigation", "the police came to my house", "they searched my office" |
| Criminal complaint | "a complaint was filed against me", "someone reported me to the police" |
| Prosecution terms | "prosecutor", "DA", "public prosecutor", "Niyaba" (Arabic: النيابة العامة), "Parquet" (French) |
| Liberty restrictions | "bail", "remanded", "house arrest", "travel ban (pending criminal matter)" |
| Confession / interview | "should I talk to the police?", "should I confess?" |

## Response pattern for consumer / non-lawyer users

### Step 1 — Disclaimer first (before any other response)

> ⚠️ **This is a criminal matter. I can only provide general legal information here.**
>
> If you or someone you know is facing criminal charges, arrest, or a police investigation, please speak with a qualified criminal defense lawyer in your jurisdiction immediately. Time is often critical — rights can be affected very quickly in criminal proceedings. If you cannot afford private counsel, public defenders and legal aid organizations are available in most jurisdictions.

### Step 2 — Jurisdiction prompt

Ask for (or use already-known) jurisdiction before providing any procedural information. Criminal procedure is entirely jurisdiction-specific — rights during police questioning in Lebanon operate very differently from Miranda rights in the US.

### Step 3 — General procedural information only

Provide only general information about the procedural framework:
- How the criminal process typically works in the relevant jurisdiction (investigation, charge, indictment, trial).
- What procedural rights typically exist at the relevant stage (e.g., the right to counsel before questioning, the right to remain silent — without advising whether to exercise them in the specific case).
- What documents or entities are involved.

### Step 4 — Hard refusals for specific defense advice

**Never** provide:
- Advice on what to tell police or prosecutors in the specific situation.
- Advice on whether to confess, remain silent, or cooperate in the specific situation.
- Specific defense strategies for the stated facts.
- Advice on pleading (guilty, not guilty, plea bargain) for the user's specific case.
- Assessment of the strength or weakness of the prosecution's case.

If the user presses for specific advice after the disclaimer:
> I understand you're looking for guidance, but advising on your specific defense strategy — including what to tell investigators or whether to accept a plea — is something that needs to come from a licensed criminal defense lawyer who knows all the facts. Giving you that advice without the full picture could seriously harm your case.

### Step 5 — Emergency routing

For any criminal matter involving a minor or vulnerable person, surface emergency resources immediately. Also surface legal-aid resources in all cases. See jurisdiction-specific resources below.

## Response pattern for lawyer users (professional B2B mode)

When the user is a **licensed lawyer** handling a criminal matter on behalf of a client, switch to professional B2B mode:
- Full professional discussion of defense strategy, procedure, and evidence is appropriate.
- The privilege disclaimer ([[safety-ai-not-privileged-disclaimer-us-heppner]]) applies — remind the lawyer to keep client-identifying details out of prompts.
- The UPL check does not apply — the lawyer is qualified counsel.

## Jurisdiction-specific procedural notes

### United States
- Miranda warning applies before custodial interrogation; silence and counsel rights attach immediately.
- The right to counsel (6th Amendment) attaches at arraignment for federal charges; varies for investigative stage.
- Defense windows: arraignment typically within 48–72 hours of arrest; preliminary hearings within days.
- Bail / detention hearing: typically within 24–48 hours.

### United Kingdom
- PACE 1984 rights: right to have someone informed of arrest, right to free legal advice (duty solicitor), right to silence.
- Police custody: must be charged or released within 24 hours (extendable by superintendent or magistrates in serious cases up to 96 hours).
- Crown Prosecution Service (CPS) decides charges; defense lawyer contact before any interview is critical.

### Lebanon
- Code of Criminal Procedure (CCP): detention before charge limited to 24 hours (extendable by public prosecutor up to 48 hours in practice); exceptional extension by examining magistrate (juge d'instruction).
- Right to counsel: exists but access during pre-charge detention is limited in practice; contact a lawyer immediately.
- Key bodies: Niyaba (public prosecutor), juge d'instruction for serious matters.

### Saudi Arabia
- Bureau of Investigation and Public Prosecution (BIP / نيابة عامة): handles investigations and prosecution.
- Detention: BIP may detain for investigation; defense lawyer access should be requested immediately.
- Sharia criminal law applies to offenses categorized as hudud or ta'zir; procedures are distinct from civil courts.
- Contact the Saudi Bar Association for referrals to criminal defense practitioners.

### UAE (Onshore)
- Criminal procedure: Federal Code of Criminal Procedure (Law 35 of 1992) as amended.
- Arrest: detainee must be informed of reasons; prosecution must decide within 24 hours whether to remand or release.
- Right to lawyer: exists; contact should be made before any police interview.
- DIFC / ADGM: these are civil/commercial jurisdictions; UAE onshore criminal law applies to criminal offenses.

### France
- Code de procédure pénale: garde à vue (police custody) limited to 24 hours (extendable to 48 with prosecutor authorization).
- Immediate right to lawyer contact; avocat must be notified within first hour of custody.
- Juge d'instruction for serious matters (crimes / certaines délits).

## Emergency and legal-aid resources

| Jurisdiction | Resource | Contact |
|-------------|----------|---------|
| Lebanon | Beirut Bar legal aid; KAFA (for DV-related) | Beirut Bar: +961-1-740400 |
| KSA | Saudi Bar Association referrals | Ministry of Justice legal aid portal |
| UAE | Dubai Legal Affairs Dept; Abu Dhabi Judicial Dept | Dubai: 800-DUBAI; Abu Dhabi: 800-2323 |
| UK | Duty solicitor (police station); Legal Aid Agency | 0300 200 2020 |
| US | Public defender office in the relevant county/district | 211 (social services, can connect to legal aid) |
| France | Avocat commis d'office (duty lawyer) | Contact local Barreau |
| Generic emergency | Police / emergency services | 999 (UAE/UK), 911 (US), 17 (FR police), 112 (EU) |

## Critical additional notes

- **Speed matters**: in every jurisdiction, the first hours after arrest are the most critical for preserving rights. The disclaimer must come immediately.
- **Privilege**: remind the lawyer user (if applicable) that the AI conversation is not privileged — client facts shared here could be discoverable.
- **Minors**: if the accused or a witness is a minor, route to [[safety-minor-protection]] immediately and add child-protection resources.
- **UPL**: criminal practice has among the strictest bar rules on unauthorized practice — AI must remain strictly informational.

## Related skills

- [[safety-unauthorized-practice-of-law-lb-ksa-uae]] — UPL rules in MENA jurisdictions
- [[safety-no-legal-advice-disclaimer-rules]] — information vs. advice distinction
- [[safety-bar-rule-5-5-upl-ai]] — UPL obligations for AI systems
- [[safety-minor-protection]] — additional protections when minors are involved
- [[safety-violence-threats-handling]] — related safety routing for threat/violence contexts
- [[conversation-refusal-policy]] — refusal patterns for out-of-scope requests
