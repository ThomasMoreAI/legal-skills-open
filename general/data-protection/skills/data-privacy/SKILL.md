---
name: data-privacy
title: Critical rules
description: Ensure data privacy compliance covering GDPR obligations, user consent management, data retention policies, PII detection, and data anonymisation with realistic synthetic data
author: diegosouzapw
author_url: https://github.com/diegosouzapw/awesome-omni-skill/tree/main/skills/data-ai/data-privacy
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: data-protection
language: en
---

# Critical rules

- ALWAYS use British English in output, comments, and documentation
- ALWAYS verify that a valid legal basis (Article 6 GDPR) exists for every personal data processing operation
- ALWAYS verify that explicit consent is collected before processing data that relies on consent as legal basis
- ALWAYS verify that consent is freely given, specific, informed, and unambiguous (Article 7 GDPR)
- ALWAYS verify that data retention periods are defined, documented, and enforced for every data category
- ALWAYS detect ALL categories of PII before generating replacements
- ALWAYS replace PII with realistic synthetic data that preserves the same format and structure
- ALWAYS ensure synthetic replacements are deterministic within a single document (same input entity → same synthetic output across all occurrences)
- ALWAYS preserve the semantic structure and readability of the original text
- ALWAYS flag special category data (Article 9 GDPR) with elevated severity
- ALWAYS report confidence level for each detection (HIGH, MEDIUM, LOW)
- NEVER approve a design that collects personal data without a documented legal basis
- NEVER approve pre-ticked consent checkboxes or bundled consent
- NEVER approve indefinite data retention ("keep forever") without explicit legal justification
- NEVER produce synthetic data that accidentally matches real individuals, organisations, or addresses
- NEVER leave partial PII visible (e.g., masking only part of a name but leaving the surname)
- NEVER use obviously fake placeholders like "REDACTED", "XXX", or "John Doe" — generate diverse, realistic synthetic identities
- NEVER store or log the mapping between real and synthetic data unless explicitly requested
- NEVER modify non-PII content; only PII entities are replaced

---

# Workflow

Follow these steps in order when performing a data privacy review.

### Step 1: Determine scope

Identify what kind of review is needed:

```
What is the user requesting?
├── Full data privacy review → Proceed with all sections (GDPR, consent, retention, PII)
├── GDPR compliance check → Focus on legal basis, consent, retention
├── Consent review → Focus on consent management
├── Retention review → Focus on data retention
├── PII detection only → Focus on PII detection (detect, report, no replacement)
├── PII anonymisation → Focus on PII detection + replace with synthetic data
└── Mixed → Combine relevant sections
```

### Step 2: GDPR compliance assessment

For each data processing operation identified:

1. Identify what personal data is collected
2. Verify a legal basis exists (Article 6)
3. Check if special category data is involved (Article 9)
4. Verify data subject rights are supported (Articles 13-22)
5. Check data protection by design measures (Article 25)
6. Verify Data Processing Impact Assessment exists for high-risk processing (Article 35)

### Step 3: Consent validation

If consent is used as legal basis:

1. Run through the Consent Checklist
2. Verify consent architecture matches an approved pattern (A, B, or C)
3. Check for consent anti-patterns — flag any found as CRITICAL
4. Verify consent withdrawal mechanism exists and works

### Step 4: Retention assessment

For each data category:

1. Run through the Retention Checklist
2. Apply the Retention Decision Tree
3. Verify automated deletion mechanisms exist
4. Flag any data category with undefined or indefinite retention as CRITICAL

### Step 5: PII detection (if applicable)

Scan the text/code and tag every PII entity found:

1. Apply Tier 1 patterns (direct identifiers) — HIGH priority
2. Apply Tier 2 patterns (indirect identifiers) — MEDIUM priority
3. Apply Tier 3 patterns (quasi-identifiers) — LOW priority
4. Apply Special Category patterns — CRITICAL priority
5. For each detection, record:
   - Entity text (exact match)
   - Category and tier
   - Position in text (line/offset)
   - Confidence level (HIGH, MEDIUM, LOW)
   - All occurrences of the same entity

### Step 6: Build entity map (if anonymisation requested)

Create a mapping of all unique entities to synthetic replacements:

```
Entity Map:
  "María García López" → "Laura Fernández Ruiz"     [name, Tier 1, HIGH confidence]
  "maria.garcia@empresa.es" → "laura.fernandez@example.net"  [email, Tier 1, HIGH confidence]
  "+34 612 345 678" → "+34 698 721 043"              [phone, Tier 1, HIGH confidence]
  "Calle Mayor 5, 28001" → "Avenida de la Paz 12, 28003"    [address, Tier 2, MEDIUM confidence]
```

Ensure cross-field coherence:
- Email derives from synthetic name
- Phone matches same country
- Address matches same region

### Step 7: Apply replacements (if anonymisation requested)

1. Start with longest matches first (avoid partial replacements)
2. Replace all occurrences of each entity with its synthetic counterpart
3. Verify no original PII remains after replacement
4. Verify no synthetic data accidentally matches other real entities in the text

### Step 8: Validate output

For anonymisation:
```
Is any original PII still present?
├── YES → Fix missed replacements, return to Step 7
└── NO  → Continue

Does the text remain readable and coherent?
├── YES → Continue
└── NO  → Adjust synthetic data for better readability

Are there any synthetic collisions with real data?
├── YES → Regenerate colliding synthetic values
└── NO  → Output is ready
```

### Step 9: Report findings

Present findings ordered by severity (critical, high, medium, low) with GDPR article references and remediation advice.

---

# GDPR Compliance Framework

## What is personal data? (Article 4 GDPR)

Personal data means any information relating to an identified or identifiable natural person ("data subject"). An identifiable natural person is one who can be identified, directly or indirectly, by reference to an identifier such as:

- A name
- An identification number
- Location data
- An online identifier
- One or more factors specific to the physical, physiological, genetic, mental, economic, cultural, or social identity of that natural person

## Special category data (Article 9 GDPR)

Processing of special category data is prohibited unless explicit consent or legal basis exists:

- Racial or ethnic origin
- Political opinions
- Religious or philosophical beliefs
- Trade union membership
- Genetic data
- Biometric data (for identification purposes)
- Health data
- Sex life or sexual orientation data

## Data protection principles (Article 5 GDPR)

All data processing must comply with these principles:

1. **Lawfulness, fairness, and transparency** — Data must be processed lawfully, fairly, and transparently
2. **Purpose limitation** — Data must be collected for specified, explicit, and legitimate purposes
3. **Data minimisation** — Only process data that is necessary for the stated purpose
4. **Accuracy** — Data must be accurate and kept up to date
5. **Storage limitation** — Data must not be kept longer than necessary
6. **Integrity and confidentiality** — Data must be protected against unauthorised access, loss, or destruction
7. **Accountability** — The controller must demonstrate compliance with all principles

## Legal bases for processing (Article 6 GDPR)

Processing is lawful only if at least one of the following applies:

| Legal Basis | When to Use | Example |
|-------------|-------------|---------|
| **Consent** (Art. 6(1)(a)) | User freely agrees to processing for a specific purpose | Marketing emails, analytics cookies |
| **Contract** (Art. 6(1)(b)) | Processing is necessary to perform a contract with the data subject | Processing an order, delivering a service |
| **Legal obligation** (Art. 6(1)(c)) | Processing is required by law | Tax records, anti-money laundering checks |
| **Vital interests** (Art. 6(1)(d)) | Processing protects someone's life | Emergency medical situations |
| **Public task** (Art. 6(1)(e)) | Processing is necessary for a task in the public interest | Public health reporting |
| **Legitimate interests** (Art. 6(1)(f)) | Processing is necessary for legitimate interests, balanced against data subject rights | Fraud prevention, network security |

## Data subject rights

The system must support exercising these rights:

| Right | GDPR Article | Implementation Requirement |
|-------|-------------|---------------------------|
| Right to be informed | Art. 13-14 | Clear privacy notice at point of collection |
| Right of access | Art. 15 | Data export/download within 30 days |
| Right to rectification | Art. 16 | Edit personal data via self-service or request |
| Right to erasure ("right to be forgotten") | Art. 17 | Delete personal data on request (with exceptions) |
| Right to restrict processing | Art. 18 | Pause processing while disputes are resolved |
| Right to data portability | Art. 20 | Export data in machine-readable format (JSON, CSV) |
| Right to object | Art. 21 | Opt out of processing based on legitimate interests |
| Rights related to automated decision-making | Art. 22 | Human review for automated decisions with significant effects |

## Data protection by design and by default (Article 25 GDPR)

Every system must implement:

1. **Privacy by design** — Build privacy into the architecture from the start, not as an afterthought
2. **Privacy by default** — Only process data that is strictly necessary; default settings must be the most privacy-friendly
3. **Technical measures** — Anonymisation, pseudonymisation, encryption, access controls
4. **Organisational measures** — Policies, training, DPIAs, data processing agreements

---

# Consent Management

## Consent requirements (Article 7 GDPR)

Valid consent must be:

1. **Freely given** — No detriment for refusing; no power imbalance exploitation
2. **Specific** — Separate consent for each distinct processing purpose
3. **Informed** — Clear explanation of what data is collected, why, and by whom
4. **Unambiguous** — Requires a clear affirmative action (opt-in, not opt-out)

## Consent checklist

When reviewing a system for consent compliance, verify:

| # | Check |
|---|-------|
| 1 | Consent is collected via an affirmative action (checkbox, toggle, click) — never pre-ticked |
| 2 | Each processing purpose has its own separate consent request |
| 3 | The consent request clearly states: what data, why, who processes it, how long |
| 4 | Users can withdraw consent as easily as they gave it (same number of clicks) |
| 5 | Consent withdrawal actually stops the associated processing |
| 6 | Consent records are stored with timestamp, user ID, version, and scope |
| 7 | Consent is re-requested when the processing purpose changes |
| 8 | Minor users (under 16, or under 13 in some jurisdictions) have parental consent |
| 9 | Consent is not bundled with terms of service acceptance |
| 10 | Users can view and manage their active consents in a self-service dashboard |

## Consent architecture patterns

### Pattern A: Granular consent with preference centre

```
User registers
  → Present granular consent options:
      [ ] Marketing emails
      [ ] Third-party data sharing
      [ ] Analytics and personalisation
      [ ] Location-based services
  → Store each consent separately with metadata:
      { purpose, granted: true/false, timestamp, version, method }
  → Provide "Manage Preferences" dashboard:
      - View all active consents
      - Toggle each on/off
      - Changes take effect immediately
```

### Pattern B: Just-in-time consent

```
User reaches feature requiring additional data
  → Display contextual consent prompt:
      "To enable [feature], we need to collect [data].
       This will be used for [purpose] and stored for [duration].
       [Allow] [Decline]"
  → If declined, gracefully degrade feature
  → Store consent decision with context
```

### Pattern C: Cookie/tracking consent banner

```
First visit
  → Display non-blocking consent banner:
      "We use cookies for [purposes].
       [Accept All] [Reject All] [Manage Preferences]"
  → No tracking scripts loaded until consent is given
  → Preferences stored in first-party cookie
  → Re-prompt annually or when categories change
```

## Consent anti-patterns (MUST REJECT)

- ❌ Pre-ticked consent checkboxes
- ❌ "By continuing to use this site, you consent to..."
- ❌ Consent buried in terms of service
- ❌ No way to withdraw consent
- ❌ Withdrawal harder than granting (e.g., grant = 1 click, withdraw = email support)
- ❌ Bundled consent (single checkbox for multiple unrelated purposes)
- ❌ Ignoring consent withdrawal (processing continues after opt-out)
- ❌ No consent records (cannot demonstrate when/how consent was obtained)

---

# Data Retention

## Retention principles

1. **Define retention periods** for every data category before collection begins
2. **Document the legal basis** for each retention period (regulatory requirement, contract, legitimate interest)
3. **Automate deletion** — manual deletion processes are error-prone and non-compliant
4. **Log retention actions** — record when data was created, when it expires, and when it was deleted
5. **Apply the minimum principle** — if you don't need it, don't keep it

## Retention policy template

Every data category must have a documented retention policy:

| Data Category | Retention Period | Legal Basis | Deletion Method | Review Cycle |
|---------------|-----------------|-------------|-----------------|-------------|
| User account data | Duration of contract + 30 days | Art. 6(1)(b) Contract | Hard delete from DB, remove backups within 90 days | Annual |
| Transaction records | 7 years from transaction date | Art. 6(1)(c) Legal obligation (tax law) | Archive → purge after 7 years | Annual |
| Marketing consent records | 3 years from last interaction | Art. 6(1)(a) Consent | Soft delete, then hard delete after 90 days | Biannual |
| Session/access logs | 90 days | Art. 6(1)(f) Legitimate interests (security) | Auto-purge via log rotation | Quarterly |
| Support tickets | 2 years from resolution | Art. 6(1)(b) Contract | Anonymise PII, keep metadata | Annual |
| Analytics data | 26 months from collection | Art. 6(1)(a) Consent | Auto-purge or aggregate/anonymise | Annual |
| Backup data | Same as source data + 90 days | Mirrors source legal basis | Rotate backups, verify purge | Quarterly |

## Retention checklist

| # | Check |
|---|-------|
| 1 | Every data category has a defined retention period |
| 2 | Retention periods have a documented legal basis |
| 3 | Automated deletion/anonymisation is implemented |
| 4 | Deletion includes backups and replicas (within defined grace period) |
| 5 | Retention schedule is reviewed at the documented review cycle |
| 6 | Data subject erasure requests are fulfilled within 30 days |
| 7 | Audit trail exists for all retention actions (creation, expiry, deletion) |
| 8 | "Right to be forgotten" requests cascade to third-party processors |
| 9 | No data category has "indefinite" retention without legal justification |
| 10 | Retention exceptions (legal hold, active investigation) are documented |

## Data lifecycle management

```
Collection → Processing → Storage → Retention → Deletion/Anonymisation
    ↓            ↓           ↓          ↓              ↓
 Consent     Purpose      Encryption   Schedule     Hard delete
 recorded    validated    at rest      enforced     or anonymise
```

---

# PII Detection Categories

## Tier 1: Direct identifiers (HIGH severity)

These directly identify a natural person:

| Category | Examples | Detection Patterns |
|----------|----------|-------------------|
| Full name | "María García López", "John Smith" | Two or more capitalised words in name context; salutation + word patterns |
| Email address | "user@example.com" | RFC 5322 pattern: `[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}` |
| Phone number | "+34 612 345 678", "(555) 123-4567" | International/national phone patterns with optional country codes |
| National ID | "12345678Z" (DNI), "AB123456C" (NI number) | Country-specific ID patterns |
| Passport number | "PAB123456" | Alphanumeric patterns in passport context |
| Social security number | "123-45-6789" (US SSN) | Country-specific SSN patterns |
| Credit/debit card number | "4111 1111 1111 1111" | Luhn-valid 13-19 digit sequences |
| IBAN / Bank account | "ES91 2100 0418 4502 0005 1332" | Country-prefix + check digit + BBAN pattern |

## Tier 2: Indirect identifiers (MEDIUM severity)

These may identify a person when combined:

| Category | Examples | Detection Patterns |
|----------|----------|-------------------|
| Postal address | "Calle Mayor 5, 28001 Madrid" | Street patterns + postcode + city combinations |
| Date of birth | "15/03/1990", "March 15, 1990" | Date patterns in birth/DOB context |
| Place of birth | "Born in Sevilla" | Location in birth context |
| Vehicle registration | "1234 BCD" (ES), "AB12 CDE" (UK) | Country-specific plate patterns |
| IP address | "192.168.1.1", "2001:0db8::1" | IPv4 and IPv6 patterns |
| Geolocation | "40.4168, -3.7038" | Coordinate pairs (lat/lon decimal) |
| Employee/student ID | "EMP-20230045" | Prefixed sequential identifiers |

## Tier 3: Quasi-identifiers (LOW severity)

These rarely identify alone but contribute to re-identification:

| Category | Examples | Detection Patterns |
|----------|----------|-------------------|
| Age | "35 years old" | Number + age-related keywords |
| Gender | "male", "female", "non-binary" | Gender keywords in personal context |
| Job title | "Senior Software Engineer at Acme" | Title + organisation patterns |
| Nationality | "Spanish", "British" | Nationality adjectives in personal context |
| Organisation name | "works at Telefónica" | Named entity in employment context |

## Special category data (CRITICAL severity)

| Category | Examples | Detection Patterns |
|----------|----------|-------------------|
| Health data | "diagnosed with diabetes", "takes metformin" | Medical terms, diagnoses, medications |
| Racial/ethnic origin | "of Moroccan descent" | Ethnicity/race references in personal context |
| Political opinions | "member of Partido X" | Political party/affiliation references |
| Religious beliefs | "practising Muslim", "Catholic" | Religious terms in personal belief context |
| Biometric data | "fingerprint ID: ABC123" | Biometric identifiers |
| Sexual orientation | "gay", "heterosexual" | Sexual orientation terms in personal context |
| Trade union membership | "member of UGT" | Union references in membership context |
| Criminal records | "convicted of", "arrested for" | Criminal justice terms in personal context |
| Genetic data | "carries BRCA1 mutation" | Genetic markers, DNA references |

---

# Synthetic Data Generation

## General principles

1. **Format preservation** — Synthetic data must match the exact format of the original (length, separators, casing)
2. **Linguistic consistency** — Names must match the apparent cultural/linguistic context (Spanish names for Spanish text, etc.)
3. **Internal consistency** — The same real entity always maps to the same synthetic entity within a document
4. **Cross-field coherence** — Related fields should be coherent (e.g., Spanish name + Spanish phone number + Spanish address)
5. **Statistical plausibility** — Synthetic values should fall within realistic ranges (valid postcodes, plausible dates, etc.)
6. **Non-collision** — Synthetic data must not accidentally match other real entities in the text

## Replacement strategies per category

| PII Category | Synthetic Strategy | Example |
|-------------|-------------------|---------|
| Full name | Generate culturally appropriate name from synthetic name pool | "María García" → "Laura Fernández" |
| Email | Derive from synthetic name + synthetic domain | "maria.garcia@empresa.es" → "laura.fernandez@example.net" |
| Phone number | Preserve country code + generate random valid digits | "+34 612 345 678" → "+34 698 721 043" |
| National ID | Generate format-valid but non-real ID | "12345678Z" → "87654321X" (valid check digit) |
| Postal address | Generate plausible address in same region/country | "Calle Mayor 5, 28001 Madrid" → "Avenida de la Paz 12, 28003 Madrid" |
| Date of birth | Shift by random offset (±1-5 years, ±1-90 days) | "15/03/1990" → "22/07/1988" |
| IBAN | Generate format-valid IBAN with correct check digits | "ES91 2100 0418 4502 0005 1332" → "ES76 0049 1500 0512 3456 7890" |
| Credit card | Generate Luhn-valid number with same BIN prefix category | "4111 1111 1111 1111" → "4532 7895 1234 5670" |
| IP address | Generate from non-routable or documentation ranges | "85.123.45.67" → "198.51.100.42" (RFC 5737) |
| Geolocation | Offset by ±0.01-0.05 degrees | "40.4168, -3.7038" → "40.4312, -3.6891" |
| Health data | Replace specific condition with different plausible condition | "diabetes" → "hypertension" |
| Organisation | Replace with fictional but plausible organisation | "Telefónica" → "Meridian Technologies" |

## Name generation pools

Maintain diverse pools of synthetic names by cultural context:

- **Spanish**: "Laura Fernández", "Carlos Ruiz", "Ana Moreno", "Pablo Jiménez", "Elena Torres", "Diego Navarro"
- **English**: "Emily Carter", "James Wilson", "Sophie Brown", "Oliver Davies", "Charlotte Evans", "William Harris"
- **French**: "Camille Dupont", "Lucas Martin", "Léa Bernard", "Hugo Petit", "Manon Durand", "Théo Lambert"
- **German**: "Hannah Müller", "Felix Schmidt", "Lena Fischer", "Maximilian Weber", "Sophie Wagner", "Paul Becker"
- **Portuguese**: "Beatriz Silva", "Tomás Santos", "Inês Costa", "Miguel Oliveira", "Mariana Ferreira", "Diogo Pereira"

(Expand pools as needed for other cultural contexts.)

---

# Decision trees

## When to anonymise vs when to flag only

```
Is the user requesting anonymisation (replace PII)?
├── YES → Detect PII + generate synthetic replacements + produce anonymised text
└── NO  → Is the user requesting PII detection only?
          ├── YES → Detect PII + report findings without replacement
          └── NO  → Is this a security review that found PII in code?
                    ├── YES → Flag as finding in security report format
                    │         Suggest: "Use @security with 'anonymise' for synthetic replacement"
                    └── NO  → Not applicable
```

## How to determine confidence level

```
Does the pattern match exactly (email regex, phone format, ID format)?
├── YES → HIGH confidence
└── NO  → Does the context strongly suggest PII (preceded by "name:", "email:", "tel:")?
          ├── YES → MEDIUM confidence
          └── NO  → Is it a partial or ambiguous match?
                    ├── YES → LOW confidence (flag but ask user to confirm)
                    └── NO  → Do not flag
```

## How to handle mixed-language text

```
Does the text contain multiple languages?
├── YES → Identify primary language per paragraph/section
│         Apply language-appropriate name pools
│         Preserve original language in synthetic output
└── NO  → Apply single-language name pool matching the text
```

## How to handle special category data

```
Is the detected PII special category (Article 9)?
├── YES → Assign CRITICAL severity
│         Warn: "Special category data detected. Ensure legal basis exists for processing."
│         Replace with different but plausible value from same category
│         Include explicit GDPR Article 9 reference in report
└── NO  → Assign severity based on tier (Tier 1 = HIGH, Tier 2 = MEDIUM, Tier 3 = LOW)
```

## Retention decision tree

```
Is there a legal obligation to retain the data?
├── YES → Set retention period to legal requirement (e.g., 7 years for tax records)
│         Document the specific law or regulation
│         Implement automated deletion on expiry
└── NO  → Is the data needed for contract performance?
          ├── YES → Retain for duration of contract + reasonable wind-down period
          │         Define wind-down period (e.g., 30 days)
          │         Delete when contract ends + wind-down expires
          └── NO  → Is the data retained based on consent?
                    ├── YES → Retain until consent is withdrawn or purpose expires
                    │         Define a maximum retention period (e.g., 26 months)
                    │         Delete promptly on consent withdrawal
                    └── NO  → Is there a legitimate interest?
                              ├── YES → Document the interest and balancing test
                              │         Set shortest reasonable retention period
                              │         Review retention regularly
                              └── NO  → DELETE IMMEDIATELY — no legal basis to retain
```

## When to require a DPIA

```
Does the processing involve:
├── Large-scale processing of special category data? → DPIA REQUIRED
├── Systematic monitoring of publicly accessible areas? → DPIA REQUIRED
├── Automated decision-making with legal/significant effects? → DPIA REQUIRED
├── Large-scale profiling? → DPIA REQUIRED
├── New technologies with high risk to rights? → DPIA REQUIRED
├── Cross-border data transfers to non-adequate countries? → DPIA RECOMMENDED
└── None of the above → DPIA not required (but recommended for high-risk processing)
```

---

# Examples

## Example 1: Consent management review

**Input:**
A registration form that asks users to accept terms and conditions with a single pre-ticked checkbox that also covers marketing emails and third-party sharing.

**Review Output:**

**Critical Issues:**
1. ❌ **Pre-ticked checkbox violates Article 7 GDPR** — Consent must require an affirmative action. Pre-ticked boxes do not constitute valid consent.
   - Remediation: Replace with unticked checkboxes that users must actively select.
2. ❌ **Bundled consent violates purpose limitation** — Separate consent required for: (a) Terms of Service acceptance, (b) Marketing emails, (c) Third-party data sharing.
   - Remediation: Provide three separate checkboxes with clear descriptions of each purpose.
3. ❌ **No consent withdrawal mechanism** — Users cannot revoke marketing or sharing consent after registration.
   - Remediation: Implement a preference centre accessible from user settings.

## Example 2: Retention policy review

**Input:**
A system that stores user session logs indefinitely and keeps deleted user accounts in a "soft delete" state forever.

**Review Output:**

**Critical Issues:**
1. ❌ **Indefinite session log retention violates storage limitation (Article 5(1)(e))** — Session logs have no defined retention period.
   - Remediation: Define a retention period (e.g., 90 days for security logs). Implement automated log rotation and purge.
2. ❌ **Soft-deleted accounts never purged violates right to erasure (Article 17)** — Users who request deletion expect their data to be removed, not merely hidden.
   - Remediation: Implement a hard-delete pipeline that purges soft-deleted accounts after a 30-day grace period. Ensure backups are also cleaned within 90 days.

## Example 3: Full anonymisation of a customer record

**Input:**
```
Customer: María García López
Email: maria.garcia@empresa.es
Phone: +34 612 345 678
DNI: 12345678Z
Address: Calle Mayor 5, 28001 Madrid

Notes: Patient diagnosed with diabetes. Follow-up appointment on 15/03/2025.
Emergency contact: Pedro García at +34 698 111 222.
```

**Output:**

**PII Detection:** 8 entities found (1 special category)

**Anonymised Text:**
```
Customer: Laura Fernández Ruiz
Email: laura.fernandez@example.net
Phone: +34 698 721 043
DNI: 87654321X
Address: Avenida de la Paz 12, 28003 Madrid

Notes: Patient diagnosed with hypertension. Follow-up appointment on 22/07/2025.
Emergency contact: Diego Navarro at +34 641 893 507.
```

**Validation:** All PII replaced. Internal consistency maintained (García family → separate synthetic identities). Special category data (health) flagged and replaced.

## Example 4: PII in code comments

**Input:**
```java
// Created by María García (maria.garcia@empresa.es)
// Test user: DNI 12345678Z, phone +34 612 345 678
public class UserService {
    private static final String ADMIN_EMAIL = "admin@empresa.es";
```

**Output:**

**PII Detection:** 4 entities found (name, email, DNI, phone in comments)

**Anonymised Text:**
```java
// Created by Laura Fernández (laura.fernandez@example.net)
// Test user: DNI 87654321X, phone +34 698 721 043
public class UserService {
    private static final String ADMIN_EMAIL = "admin@empresa.es";
```

**Note:** `ADMIN_EMAIL` constant flagged separately as potential hardcoded credential (escalate to security-review skill). Not treated as PII anonymisation since it is a system account, not a natural person.

---

# Output expectations

- **Findings** — Ordered by severity (critical, high, medium, low) with GDPR article references
- **Remediation** — Concrete, actionable fix for each finding
- **GDPR mapping** — Each finding mapped to the relevant article
- **Checklists** — Consent and retention checklists completed when applicable

---

# Notes

- This skill extends the security agent's capabilities; it does NOT replace the security-review skill
- The security-review skill detects secrets and vulnerabilities; this skill focuses on data privacy: GDPR, consent, retention, and PII
- Anonymisation is a form of data protection by design (Article 25 GDPR)
- True anonymisation (irreversible) vs pseudonymisation (reversible with key) — this skill performs anonymisation by default
- If the user needs pseudonymisation (reversible mapping), they must explicitly request it; in that case, the mapping must be stored securely and separately
- For automated pipelines, consider integrating with libraries like Microsoft Presidio, spaCy NER, or AWS Comprehend for production-grade detection
- The agent performs best-effort detection; it is not a substitute for formal Data Protection Impact Assessment (DPIA)
- Consent management and retention policies should be reviewed with legal counsel for jurisdiction-specific requirements
- Data retention automation should be tested thoroughly to avoid accidental data loss

---
