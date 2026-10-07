# Model Clause — Notice at Collection (CA-specific; structure useful for other states)

> **Use note.** California is the only state that imposes a separate **notice-at-collection** duty distinct from the privacy policy. CCPA Regs § 7012. The notice-at-collection must be provided at or before the point PI is collected, in plain language, and must list categories of PI to be collected, purposes, retention, and links to the privacy policy and (where applicable) opt-out and limit-use pages.
>
> **Never paste this template verbatim.** It must be tuned to the actual data categories, purposes, retention periods, and recipients in play. Generic boilerplate is worse than no notice — it misrepresents the controller's practices and creates fresh exposure.

---

## Notice at Collection

**Effective: [Date — AD format, e.g., June 1, AD 2026]**

This Notice at Collection summarizes the categories of personal information [Company Name] ("we," "us," or "our") collects from you, why we collect it, and your rights to limit certain uses. For more detail, please see our full [Privacy Policy](#) and the linked [California Privacy Notice](#).

### Categories of personal information we collect

We collect the following categories of personal information about you:

| Category | Examples (specific to our service) | Purpose for collection | Retention period (or criteria) |
|---|---|---|---|
| **Identifiers** | [Real name; email address; account username; IP address] | [Account creation; authentication; service delivery] | [Duration of account + X years; or specific criteria] |
| **Customer records / commercial info** | [Billing details; transaction history; product preferences] | [Order processing; customer support; recommendations] | [X years post-transaction for tax/audit] |
| **Internet/network activity** | [Browsing history on our properties; interaction with content; device data] | [Service operation; analytics; product improvement] | [X months for raw logs; aggregated for X years] |
| **Geolocation data** | [Approximate location from IP; precise location with consent] | [Localization; fraud prevention] | [X months] |
| **Audio/visual** | [Customer service recordings; uploaded photos] | [Quality assurance; service delivery] | [X years] |
| **Sensitive personal information** (see § 1798.140(ae)) | [List specific categories — e.g., precise geolocation; account credentials; government IDs] | [Specifically describe purposes — e.g., authentication, fraud prevention, identity verification] | [X period] |
| **Inferences** | [Preferences; characteristics derived from other categories] | [Personalization; service improvement] | [X period] |

### Sources

We collect the personal information listed above from the following categories of sources:

- Directly from you (e.g., when you create an account, contact support, or use our services).
- Automatically from your interactions with our service (e.g., cookies, pixels, server logs).
- From third parties such as [identity verification providers; advertising partners; service providers].

### Sale or sharing of personal information

[Choose one of the following blocks:]

**[If the entity does not sell or share]:**
We do **not** sell your personal information for monetary or other valuable consideration, and we do **not** share your personal information for cross-context behavioral advertising.

**[If the entity sells or shares]:**
We **sell** and/or **share** the following categories of personal information for purposes including [cross-context behavioral advertising on third-party platforms]:

- [Identifiers]
- [Internet/network activity]
- [Inferences]

You have the right to opt out of the sale and sharing of your personal information. To exercise this right, click **[Do Not Sell or Share My Personal Information](#)** or set the [Global Privacy Control](https://globalprivacycontrol.org/) signal in your browser; we honor opt-out preference signals.

### Sensitive personal information

[If the entity processes sensitive PI for purposes beyond those reasonably expected:]
We process certain categories of sensitive personal information (identified above) for purposes that may extend beyond what is reasonably expected to provide the service. You have the right to limit our use and disclosure of your sensitive personal information. To exercise this right, click **[Limit the Use of My Sensitive Personal Information](#)**.

[If the entity processes sensitive PI only for purposes reasonably expected (e.g., authentication, fraud prevention) and does not need to offer the limit-use right:]
We process sensitive personal information only as necessary to provide the service you request, including [authentication, fraud prevention, and security]. We do not use or disclose your sensitive personal information for purposes beyond those that are reasonably expected.

### Your rights

You have the right to:
- Know what personal information we collect about you and request a copy.
- Delete personal information we have collected about you (subject to enumerated exceptions).
- Correct inaccurate personal information.
- Opt out of sale or sharing of your personal information.
- Limit the use and disclosure of sensitive personal information.
- Be free from discrimination for exercising your privacy rights.

To exercise these rights, please visit [Privacy Choices](#) or contact us at [privacy@example.com] or [toll-free phone].

### Updates

This Notice was last updated on the effective date above. We will provide notice of material changes through [the privacy policy / banner / email to known users].

---

## Implementation notes (delete from production)

1. **Trigger placement.** Provide this notice at or before each point of PI collection — at minimum, on the homepage, account creation, and any data-collection form. Linking from the privacy policy alone does not satisfy CCPA Regs § 7012.
2. **Sensitive PI section.** The "Limit Use" link is required if the entity uses sensitive PI for any purpose beyond those enumerated in CCPA Regs § 7027(m). If all uses fall within those enumerated, the "Limit Use" link is not required, but the notice should make this clear.
3. **Retention.** Retention period is required (CPRA amendment). Use specific durations or specific criteria; "as long as necessary" is non-compliant absent further specificity.
4. **Categories.** Use the statutory categories from § 1798.140(v). Custom plain-language category names supplement but do not replace the statutory categories.
5. **Cross-state coverage.** This notice is structured for CA. Other states require comparable disclosure in the privacy policy but generally do not require a separate notice-at-collection. The category, purpose, and source disclosures here transfer well.
6. **Children.** If known minors are present, layer state-specific consent and notice — do not assume this notice covers minor processing.
