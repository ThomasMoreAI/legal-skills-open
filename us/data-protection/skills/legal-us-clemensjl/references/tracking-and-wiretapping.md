# Tracking, wiretapping and pixel litigation

Status as at 2026-08-05.

**No US statute requires opt-in consent before setting a cookie.** There is no ePrivacy Directive, no Art 5(3), no cookie law. US sites nevertheless deploy consent banners, and the reason is not statutory — it is class-action exposure under decades-old wiretap statutes that plaintiffs' firms have repurposed for web tracking, plus the opt-out and opt-out-signal duties of the state comprehensive privacy laws. Explaining the banner as "cookie consent" is wrong and leads to the wrong design. The banner exists to create a consent record and to gate third-party scripts.

Three distinct exposures, each with a different fix:

| Exposure | Mechanism | What actually mitigates it |
|---|---|---|
| State wiretap / pen-register class actions | Third-party script receives visitor communications or metadata | Blocking third-party tags until affirmative consent, plus a disclosure the visitor sees before the tag fires |
| State privacy law opt-out duties | Targeted advertising pixels are a "sale"/"share" | Working opt-out link, honouring the Global Privacy Control signal |
| VPPA | Video content plus an identifiable-person pixel | Separate, informed, standalone consent to disclose video-viewing data — or removing the pixel from video pages |

## California — CIPA, Cal. Penal Code §§ 630–638

The four provisions used against websites:

- **§ 631(a)** — wiretapping and eavesdropping on a wire communication. The theory: the third-party analytics or chat vendor is a non-party "eavesdropper" on the visitor's communications with the site.
- **§ 632** — recording a confidential communication without all-party consent. California is an all-party consent state.
- **§ 632.7** — interception of cellular and cordless telephone communications.
- **§ 638.51** — installation or use of a **pen register or trap and trace device** without a court order. This is the newer and now dominant wave: plaintiffs argue that a tracking script that captures routing, addressing or signalling data (including device fingerprinting) is a pen register. There is no damages requirement to plead.

**§ 637.2** gives a private right of action with statutory damages of **$5,000 per violation** or three times actual damages, whichever is greater, plus injunctive relief, and expressly does not require proof of actual damage. In a class posture the per-violation figure is what drives settlement value.

**Legislative reform — not enacted.** California SB 690 (2025–2026 session) has been amended repeatedly. The originally proposed broad "commercial business purpose" exemption from CIPA was **removed**; the amended bill would instead give the California Attorney General exclusive enforcement of § 638.51 pen-register claims arising from websites and apps, stripping the private right of action for that provision only. As at 2026-08-05 the bill has **not** been signed and remains subject to further amendment. Do not advise a client that CIPA exposure has been fixed. `[[UNVERIFIED: final disposition of SB 690 after the 31 August 2026 legislative deadline — recheck before relying on any exemption]]`

## Other state wiretap statutes with private rights of action

| State | Statute | Position on website tracking |
|---|---|---|
| Pennsylvania | WESCA, 18 Pa. C.S. §§ 5701–5782 | **Live.** *Popa v. Harriet Carter Gifts, Inc.*, 52 F.4th 121 (3d Cir. 2022) — the Third Circuit rejected the argument that the third-party marketing vendor could not "intercept" because the browser communicated directly with its servers. Session-replay and third-party tracking claims survive. |
| Massachusetts | G.L. c. 272, § 99 | **Largely closed.** *Vita v. New England Baptist Hospital*, SJC-13542 (Mass. 2024) — the SJC held the term "communication" ambiguous as applied to web browsing, applied the rule of lenity, and reversed the denial of motions to dismiss. The wiretap act does not reach website browsing tracking. |
| Florida | FSCA, Fla. Stat. § 934.03 | **Mixed.** *Goldstein v. Costco* (S.D. Fla. 2021) and *Jacome v. Spirit Airlines* dismissed session-replay claims, relying in part on the statutory exclusion for device-tracking communications. A 2025 federal decision revived FSCA theories in the website context. Treat as unsettled. |
| Washington | RCW 9.73.030 | All-party consent; used alongside My Health My Data claims. |

Other all-party or two-party consent states (including Illinois, Michigan, Maryland, Montana, New Hampshire, Nevada, Connecticut, Delaware, Oregon) carry equivalent statutes; whether they reach web tracking is jurisdiction-specific and mostly unlitigated. Do not assert a position for a state without a decision to cite.

## VPPA — 18 U.S.C. § 2710

Applies to a "video tape service provider" that knowingly discloses personally identifiable information — including what video a consumer requested or obtained — to a third party. Statutory damages of **$2,500 per violation** plus attorney's fees, with a private right of action. The Meta Pixel on a page containing video, combined with a Facebook ID cookie, is the standard fact pattern.

Circuit split on who is a "consumer"/"subscriber":

- **Second Circuit — broad.** *Salazar v. National Basketball Association*, No. 23-1147 (2d Cir., 15 October 2024): a person who subscribes to **any** product or service of an entity that provides audiovisual content — including a free email newsletter unrelated to video — is a "subscriber" and therefore a "consumer".
- **Sixth and D.C. Circuits — narrow**, requiring the subscription to be to audiovisual goods or services.

Practical consequence: any site with embedded video, a newsletter signup, and an advertising pixel is exposed in the Second Circuit. Consent under the VPPA must be **separate and distinct** from other terms and given in a standalone form contemporaneous with the disclosure (§ 2710(b)(2)(B)); burying it in the privacy policy does not work.

## What the banner must actually do

- Load **no** third-party advertising, analytics, session-replay, chat, or fingerprinting script before the visitor acts. First-party strictly necessary functionality may load.
- Present reject as prominently as accept. There is no US statute mandating this, but a banner that only accepts creates no usable consent record and is an FTC Act § 5 dark-pattern target.
- Record and retain: timestamp, banner version, the choice made, and the scripts blocked. The record is the entire point.
- Detect and honour the **Global Privacy Control** signal — see `opt-outs-and-gpc.md`. In states where honouring is mandatory, a banner that ignores GPC is a statutory violation regardless of what the banner says.
- Never claim in the banner or policy that the site "does not sell your data" while advertising pixels are live. That statement is a deceptive practice under 15 U.S.C. § 45 and is the single most common self-inflicted wound in US privacy work.

## Vendor contracting

The wiretap theories all turn on a **third party** receiving the communication. Two contractual facts materially change the analysis and both should be established in writing before the vendor is deployed:

- The vendor processes the data **only** on the site operator's instructions and for no purpose of its own — no model training, no cross-customer enrichment, no independent commercialisation. Under the state privacy laws this is also what makes the vendor a service provider or processor rather than a recipient of a sale.
- The vendor does not retain the data beyond what the service requires and deletes on termination.

A session-replay, heatmap or chat vendor operating under its own terms of use, for its own analytics purposes, is the fact pattern the plaintiffs' bar looks for. Chat widgets are the highest-risk category because the intercepted content is an actual conversation, which fits the wiretap statutes far better than page metadata does.

## Template — consent record fields

```json
{
  "consent_id": "[[UUID]]",
  "timestamp_utc": "[[ISO-8601]]",
  "banner_version": "[[VERSION]]",
  "policy_version": "[[VERSION]]",
  "gpc_signal_present": "[[true|false]]",
  "choice": "[[accept_all|reject_all|granular]]",
  "categories_allowed": ["[[analytics]]", "[[advertising]]"],
  "scripts_blocked": ["[[vendor domains]]"],
  "user_id": "[[if authenticated]]",
  "ip_truncated": "[[first three octets]]",
  "page_url": "[[URL]]"
}
```

Retain for the length of the applicable limitation period. The record is the only thing that converts a design decision into a defence.

## Checkpoints

- [ ] Site loaded in a clean profile with the network tab recording; every third-party domain contacted before any consent action listed
- [ ] Every listed domain either removed, moved behind consent, or justified in writing
- [ ] Session replay, heatmap and chat vendors identified by name; contracts reviewed for whether the vendor uses the data for its own purposes
- [ ] If any page has video and any advertising pixel: standalone VPPA consent implemented, or the pixel removed from those pages
- [ ] Consent record retained with timestamp and banner version
- [ ] GPC signal detection tested and demonstrably acted upon
- [ ] Privacy policy statements about selling and sharing verified against the actual tag list, not against intent
- [ ] No claim anywhere that the site is "cookie compliant" or "GDPR compliant" unless separately established
