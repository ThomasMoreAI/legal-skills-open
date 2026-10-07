# Model Clause — Sensitive Data Notice and Consent

> **Use note.** Most states (17 of 20) require **opt-in consent** before processing sensitive data. CA uses a **right to limit use** instead of opt-in. UT and IA use **notice + opt-out**. MD imposes a **flat ban on sale of sensitive data** and additional restrictions for known minor data.
>
> The clause below provides three modules: (A) opt-in consent flow for the majority of states, (B) limit-use notice for CA, and (C) MD-specific suppression and disclosure language.

---

## Module A — Opt-In Consent for Sensitive Data (Majority of States)

**Use when**: the controller processes sensitive data and the consumer is a resident of any state requiring opt-in consent (VA, CO, CT, TX, OR, MT, IN, TN, DE, NJ, NH, NE, KY, MN, RI, FL — and MD with ban-augmentation in Module C).

### Consent flow language

> Before we can [process / collect] the following types of sensitive personal information, we need your consent:
>
> - **[Specific category, e.g., precise geolocation]** — used for [specific purpose, e.g., to provide localized search results within ~1,000 feet of your current location]. We retain this for [specific period, e.g., 90 days].
> - **[Specific category, e.g., health-related information]** — used for [specific purpose, e.g., to suggest fitness goals based on activity logs]. We retain this for [specific period].
> - **[Specific category]** — used for [purpose]. Retained for [period].
>
> **You can withdraw your consent at any time** by visiting [Privacy Choices] or contacting us at [privacy@example.com]. Withdrawal will not affect processing that occurred before withdrawal, but we will stop using or disclosing this information for the purposes above going forward.
>
> [ ] **I consent to the processing of my sensitive personal information for the purposes described above.**
>
> [Submit] [Decline and Continue Without Sensitive Features]

### Consent infrastructure requirements

- The consent must be **affirmative**, **specific** (per category and purpose), **informed**, **unambiguous**, and **freely given**. (CO CPA Rules § 7; CCPA Regs § 7004 dark-pattern prohibitions; comparable in other states.)
- **Pre-checked boxes are non-compliant.**
- **Bundled consent** (e.g., "By using our service you consent to all the things") is non-compliant.
- The **"Decline" path** must be functionally equivalent in prominence to the "Consent" path. Buttons of unequal prominence violate dark-pattern rules.
- Consent must be **revocable** as easily as it was given.
- **Consent records** must be maintained with timestamp and the specific purposes consented to. Audit trail.

---

## Module B — Limit Use of Sensitive PI (California)

**Use when**: the controller is subject to CCPA/CPRA AND processes sensitive PI for purposes that go beyond what is necessary to provide the goods or services reasonably expected by the consumer (i.e., outside the CCPA Regs § 7027(m) enumerated purposes).

If sensitive PI is used **only** for the enumerated purposes (security, fraud prevention, transient use, etc.), no "Limit Use" link is required, but the privacy notice should affirmatively state that sensitive PI is processed only for those purposes.

### Privacy notice language

> ## Sensitive Personal Information
>
> Under California law, you have the right to direct us to limit the use and disclosure of your sensitive personal information to that which is necessary to perform the services or provide the goods reasonably expected by an average consumer who requests them.
>
> **The categories of sensitive personal information we process include:**
>
> - [Specific categories — e.g., government identifiers, precise geolocation, account credentials]
>
> **We use sensitive personal information for the following purposes that go beyond providing the service you have requested:**
>
> - [Specific purpose — e.g., to personalize content or marketing based on inferences from health-related browsing patterns]
>
> To direct us to limit the use of your sensitive personal information, click **[Limit the Use of My Sensitive Personal Information](#)** or contact us at [privacy@example.com].

### Limit-use page

> ## Limit the Use of My Sensitive Personal Information
>
> By submitting this form, you direct [Company] to limit the use and disclosure of your sensitive personal information to that which is necessary to perform the services or provide the goods you have reasonably requested. We will continue to use your sensitive personal information only for [enumerated purposes — security, fraud prevention, etc.] as permitted by California Civil Code § 1798.121 and CCPA Regulations § 7027(m).
>
> [Email: ____________ | Account ID: ____________]
>
> [Submit]
>
> If you have a [Company] account, we recommend submitting this request while logged in so we can apply the limit across your devices.

### Implementation requirements

- The "Limit Use" link must be on the homepage (CCPA Regs § 7027).
- Must be functional via the link, GPC equivalent (no dedicated GPC for limit-use, but accept other equivalent signals where they exist), or by contact methods.
- Apply the limit to the consumer's known account (not just device).
- Persist the limit; require affirmative re-opt-in to resume.

---

## Module C — Maryland MODPA Sensitive Data Handling

**Use when**: the controller is subject to MODPA (Maryland) AND processes sensitive data of MD residents.

### Maryland-specific provisions

MODPA (Md. Code Com. Law § 14-4607) imposes **stricter** sensitive data rules than any other state:

1. **Flat ban on sale of sensitive data.** Cannot be cured by consent.
2. **Consent required to process** sensitive data (cannot rely on legitimate interest).
3. **Minor protections**: flat ban on sale and on processing for targeted advertising of PD of consumers known to be under 18 — **regardless of consent.**

### Privacy notice — MD-specific section

> ## Maryland Residents
>
> If you are a resident of Maryland, additional protections apply to your personal information under the Maryland Online Data Privacy Act (MODPA), Md. Code Com. Law § 14-4601 et seq.
>
> **Sale of sensitive data.** We do not sell your sensitive personal data, regardless of consent.
>
> **Processing of sensitive data.** We process your sensitive personal data only with your express consent. You can withdraw your consent at any time by [contact / Privacy Choices].
>
> **Consumers under 18.** We do not sell the personal data of, or process for targeted advertising the personal data of, any consumer we know to be under 18 years of age — regardless of any consent.
>
> **Data minimization.** We collect personal data limited to what is reasonably necessary and proportionate to provide or maintain the specific product or service you have requested. If you would like more information about our data minimization practices, please contact us at [privacy@example.com].

### Operational requirements for MD

- **Suppress sale of sensitive data of MD residents** at the data-flow level, not at the consent layer. This is a flat ban; consent infrastructure cannot cure.
- **Suppress sale and targeted advertising of known-minor data** for MD residents under 18.
- **Tighten default data collection** to comply with the strict minimization standard.
- **Document the MD-specific compliance posture** in the privacy program.

---

## Cross-state implementation notes

1. **State-detection challenge.** Most controllers cannot reliably know a user's state at sign-up. Posture options: (a) apply the strictest standard (MD flat ban + opt-in consent) globally; (b) collect state at sign-up and apply state-specific rules; (c) infer state from IP/account data and apply rules accordingly. Each has tradeoffs.
2. **Consent withdrawal** must be as easy as consent. Friction here is a frequent enforcement finding.
3. **Children**. Sensitive data definitions universally include "PD of a known child." A consent-based flow for sensitive data does NOT solve known-child data — that requires parental consent under COPPA layered with state-specific rules.
4. **Sensitive-data inventory** must be maintained as a living artifact. Adding new data types (e.g., a new wellness feature that infers health interest) creates new sensitive-data processing that may require new consent.
5. **Vendors processing sensitive data on behalf of the controller** must be flow-down constrained. The controller's processor agreements must require equivalent sensitive-data treatment.
