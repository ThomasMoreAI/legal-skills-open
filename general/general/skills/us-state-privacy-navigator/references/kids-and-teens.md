# Children and Teens — Multi-Layer Privacy Overlay

**Purpose.** A consolidated reference to the layered rules governing processing of minors' data. State comprehensive privacy laws layer over federal COPPA and over state-specific minor-protection laws (AADC, social media age laws). Failing to address all layers is a common gap.

## The four layers

When minors are present, the analysis must address:

1. **Federal COPPA** — Children's Online Privacy Protection Act, 15 U.S.C. §§ 6501–6506; FTC Rule at 16 C.F.R. Part 312. Children **under 13**.
2. **State comprehensive privacy laws** — sensitive-data treatment of "personal data of a known child," plus state-specific teen provisions.
3. **State Age-Appropriate Design Code laws** — design and notice obligations for services likely to be accessed by minors. CA AADC, MD AADC, others pending.
4. **State social media / minor-platform laws** — age verification, parental consent, account restrictions for specific platforms or service types.

## COPPA basics (federal floor)

COPPA applies to operators of websites or online services directed to children under 13, OR operators with actual knowledge that they are collecting personal information from children under 13.

### Core obligations

- Notice on the website / service of information practices (16 C.F.R. § 312.4).
- Direct notice to parents and obtaining **verifiable parental consent** before collecting, using, or disclosing personal information from children under 13 (§ 312.5).
- Means for parents to review the child's information and request deletion (§ 312.6).
- Limited "internal use" exceptions for support of the internal operations of the service (§ 312.5(c)).
- Reasonable security (§ 312.8).
- Data retention limits (§ 312.10).

### "Directed to children" vs. "actual knowledge"

A "directed to children" service is generally one whose subject matter, visual content, audio content, age of models, etc., target children under 13. The FTC considers a multi-factor totality test.

A general-audience service that obtains "actual knowledge" of an under-13 user's age (e.g., user enters age 9 in a registration form) becomes COPPA-covered for that user.

### "Verifiable parental consent"

Several methods satisfy verifiable parental consent (§ 312.5(b)):
- Signed consent form returned by mail/fax.
- Credit card or debit card transaction.
- Toll-free number staffed by trained personnel.
- Video conference with trained personnel.
- Government-issued ID verification.
- "Email plus" — email + delayed second confirmation step.
- Knowledge-based authentication.
- Facial-recognition match against ID.

The FTC has a "safe harbor" program for self-regulatory organizations (e.g., kidSAFE, ESRB, iKeepSafe).

### COPPA enforcement

FTC and state AGs. Significant settlements: TikTok ($170M), YouTube ($170M), Epic Games ($275M as part of $520M total), Microsoft / Xbox ($20M).

### COPPA 2.0 / proposed rule changes

The FTC proposed COPPA Rule revisions in 2023–2024. Key proposals: limits on push notifications and behavioral advertising to children, new data minimization requirements, retention limits, school-authorization changes. **Status as of skill version date: pending**; verify current status.

## State comprehensive privacy laws — minor provisions

| State | Treatment |
|---|---|
| **CA (CCPA/CPRA)** | Sale/share opt-in for ages 13–15 (the consumer or their parent must opt in); parental consent (COPPA-aligned) for under 13. Cal. Civ. Code § 1798.120(c). |
| **CT (CTDPA, as amended)** | Default off for processing of consumers known to be 13–15 for sale, targeted advertising, and profiling for legal/significant effects. Heightened data minimization for known minors. |
| **CO** | Heightened protections for known children; profiling-of-minors restrictions per CPA Rules. |
| **NJ** | Opt-in for processing of consumers known to be 13–16 for targeted advertising, sale, profiling for significant effects. |
| **MD (MODPA)** | **Flat ban on sale of PD of known minors under 18.** **Flat ban on processing of PD of known minors under 18 for targeted advertising.** Strictest in the country. |
| **MN** | Opt-in for processing of consumers known to be under 17 for targeted advertising or sale. |
| **Other states** | Treat PD of a known child as sensitive data → opt-in consent required to process. |

> **The most operationally significant trend**: states are moving from a 13-and-under-only framework (COPPA-aligned) to a 13-to-17 (or 13-to-16) framework with heightened protections for the teen tier. A program serving any teen-facing audience must address state-specific teen provisions, not just COPPA's under-13 rule.

## Age-Appropriate Design Code laws

### California Age-Appropriate Design Code Act (AADC) — AB 2273

Codified at Cal. Civ. Code §§ 1798.99.28–1798.99.40 (effective July 1, 2024 but subject to substantial litigation). The Ninth Circuit and N.D. Cal. have addressed First Amendment challenges; **partial preliminary injunction history** in *NetChoice v. Bonta*, 113 F.4th 1101 (9th Cir. 2024). Verify current status at time of analysis.

If in effect for a given service, requires:
- Data Protection Impact Assessments for products likely to be accessed by children.
- Default privacy settings configured to "high level" for children.
- Estimating age of users with reasonable certainty.
- Transparency of terms in language suited to children's age.
- Bans on dark patterns, profiling, and use of children's PD inconsistent with their best interests.

### Maryland AADC (HB 603)

Maryland enacted its own AADC. Largely modeled on the CA AADC with some refinements aimed at constitutional concerns.

### Pending AADCs

Multiple states have proposed AADCs (NY, MN, IL, NM). Track status when advising on a multi-state design.

## State social media / minor-platform laws

These are NOT comprehensive privacy laws but layer significant additional obligations.

| State | Law | Effect |
|---|---|---|
| **CA** | SB 976 (Protecting Our Kids from Social Media Addiction Act) | Limits on addictive social media features for minors; default-off notifications for minors |
| **NY** | SAFE for Kids Act, NY Public Health Law § 1500-A et seq. | Restrictions on algorithmic feeds for minors without parental consent |
| **FL** | HB 3 | Age verification + account restrictions for under-14s on covered platforms; under-16 with parental consent |
| **TX** | SCOPE Act (HB 18) | Notice, parental tools, and content/algorithm restrictions for minors |
| **UT** | HB 311 + companion laws | Social media age verification, parental consent, time limits |
| **AR** | Social Media Safety Act | Age verification; **partial preliminary injunction** |
| **OH** | Parental Notification by Social Media Operators Act | Parental consent for under-16; **partial preliminary injunction** |

> Many of these have been partially enjoined on First Amendment / preemption grounds. Verify current enforcement status when advising.

## Practical layering — what to actually do

### For a service that may be accessed by minors

1. **Determine if "directed to children"** under COPPA. If yes: full COPPA program (notice, parental consent, limited collection, etc.).
2. **Determine if "likely to be accessed by children"** under CA AADC (and similar). If yes (and the law is in effect): DPIA, age estimation, default-high privacy, language adapted, dark-pattern audit.
3. **Determine if "actual knowledge" of minor users**. If yes: state-specific teen treatment (default off in CT for 13–15; opt-in in NJ for 13–16; flat bans in MD for under 18; opt-in in MN for under 17; opt-in in CA for 13–15 sale).
4. **Layer in sensitive-data rules** — PD of a known child is sensitive in all states, requiring opt-in (or limit-use in CA) before processing.
5. **Layer in social media / platform laws** if the service falls within their scope (e.g., a social network, a video platform).

### For a B2B SaaS used by schools or services to children

Layer FERPA + COPPA's "school authorization" framework. The "school authorization" doctrine permits schools to authorize collection of student data on behalf of parents in limited educational contexts. The FTC's 2023 NPRM proposed changes to this framework.

### For an enterprise application unlikely to be accessed by minors

Even general-purpose enterprise services should:
- Disclaim that the service is not directed to children under 13.
- Have a process for handling actual knowledge (e.g., a customer service rep encountering an under-13 user inadvertently signed up).
- Avoid features (game-like UX, kid-friendly imagery) that could raise "directed to children" arguments.

## Common errors in minor-related privacy advice

1. **Treating COPPA as the entire framework.** State teen-specific laws extend protections to ages 13–17 and require attention beyond COPPA.
2. **Confusing "directed to children" with "actual knowledge."** Either independently triggers COPPA. They are not the same test.
3. **Missing the AADC layer.** Where AADC laws are in effect, design and notice obligations apply on top of comprehensive privacy laws.
4. **Assuming parental consent solves all minor-related issues.** Maryland's flat bans on sale and targeted advertising for under-18 minors cannot be cured by consent.
5. **Not addressing social media / platform laws.** These overlay independently and have their own enforcement actions.
6. **Failing to track preliminary injunctions.** Multiple state minor-protection laws are subject to ongoing litigation. The compliance posture changes when an injunction is issued or lifted.
