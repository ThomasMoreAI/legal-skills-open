# Banner UI rules that draw enforcement

Authoritative basis: EDPB Report of the work undertaken by the Cookie Banner Taskforce, adopted 17 January 2023; EDPB Guidelines 03/2022 on deceptive design patterns in social media platform interfaces, Version 2.0, adopted 24 February 2023; GDPR Articles 4(11), 7(2), 7(3), 12; CNIL recommandation n° 2020-092; Garante provvedimento 10 giugno 2021 n. 231. Status as at 2026-08-05.

Wording belongs to the `legal-*` skills. This file is about structure, controls and defaults — the parts a developer builds.

## The seven rules, each with its source

**1. A reject control on the first layer.**
Cookie Banner Taskforce para 8: when asked whether a banner offering only accept and settings, with no refuse option on any layer carrying a consent button, infringes the ePrivacy Directive, "a vast majority of authorities considered that the absence of refuse/reject/not consent options on any layer with a consent button of the cookie consent banner is not in line with the requirements for a valid consent and thus constitutes an infringement."

**2. Reject must be a control, not prose.**
Same report para 14: invalid where "the only alternative action offered (other than granting consent) consists of a link behind wording such as 'refuse' or 'continue without accepting' embedded in a paragraph of text in the cookie banner, in the absence of sufficient visual support", or where such a link sits outside the banner frame.

**3. No pre-ticked boxes, anywhere, at any layer.**
Same report para 10, invoking GDPR Recital 32: "Silence, pre-ticked boxes or inactivity should not therefore constitute consent." This covers toggles rendered in the on position in the second layer, which is where it usually happens.

**4. No nudging by colour or contrast.**
Same report para 17: no general colour standard can be imposed on controllers; assessment is case by case. Para 18 identifies at least one manifestly misleading practice: an alternative-action button "where the contrast between the text and the button background is so minimal that the text is unreadable to virtually any user." CNIL recommandation §34 goes further as a recommendation: same button size, same font, same legibility, same visual emphasis. Build to the CNIL standard — it is the only version that is testable.

**5. No cookie wall without a genuine alternative.**
Same report para 13: a controller "must not design cookie banners in a way that gives users the impression that they have to give a consent to access the website content, nor that clearly pushes the user to give consent". Whether a paid alternative rescues a wall is a legal question — escalate it, do not implement a wall on your own authority.

**6. Withdrawal as easy as giving.**
GDPR Art 7(3). Cookie Banner Taskforce para 34 states three cumulative conditions: the possibility to withdraw, the ability to withdraw at any time, and withdrawal being as easy as giving. Para 35: no specific solution can be imposed on controllers, and a hovering icon in particular cannot be mandated — but para 32 says controllers "should put in place easily accessible solutions allowing users to withdraw their consent at any time, such as an icon (small hovering and permanently visible icon) or a link placed on a visible and standardized place."

**7. A persistent way to reopen the settings.**
Follows from 6. A footer link present on every page, reachable without JavaScript errors, without login and without the banner being displayed, satisfies it. The reopened dialog must show the current state, not a fresh default.

## Testable acceptance criteria

Turn the above into assertions a reviewer can run:

| Assertion | How to test |
|---|---|
| Reject is a `<button>` on the first layer | Query the banner root for two sibling buttons; both must be in the accessibility tree |
| Equal prominence | Compare computed `width`, `height`, `font-size`, `font-weight` and contrast ratio of accept vs reject |
| Reject contrast is legible | Contrast ratio of text against button background ≥ 4.5:1 |
| No pre-ticked state | Every category input except strictly necessary reports `checked === false` on first open |
| Dismissal is not consent | Pressing Escape or clicking the backdrop must not write a granted state |
| Withdrawal reachable | Footer link present on every route; opening it shows current state |
| Withdrawal parity | Number of interactions to revoke all ≤ number to accept all |
| No re-prompt | Reload after refusal produces no banner (see `consent-record.md`) |
| Keyboard operable | Tab order reaches both buttons; focus trap while modal; Escape does not grant |
| Language | Banner locale matches page locale |

## The do-not-build list

EDPB Guidelines 03/2022 v2.0, Annex I. Names are the EDPB's; the examples are the consent-banner form each takes.

**Overloading** — "Burying users under mass of requests, information, options or possibilities in order to deter them from going further and make them keep or accept certain data practice."

- *Continuous prompting* — re-showing the banner after a refusal, on every page or every session.
- *Privacy Maze* — vendor settings four levels deep with no overview.
- *Too many options* — 300 unlabelled vendor toggles with no bulk control.

**Skipping** — "Designing the interface or user journey in such a way that users forget or do not think about all or some of the data protection aspects."

- *Deceptive snugness* — the most data-invasive options enabled by default; the toggle that ships on.
- *Look over there* — a newsletter offer or discount code inside the consent dialog.

**Stirring** — "Affecting the choice users would make by appealing to their emotions or using visual nudges."

- *Emotional Steering* — "No thanks, I don't want a better experience".
- *Hidden in plain sight* — the reject control styled as body text while accept is a filled button.

**Obstructing** — "Hindering or blocking users in their process of obtaining information or managing their data by making the action hard or impossible to achieve."

- *Dead end* — the "cookie policy" link in the banner 404s or opens the banner again.
- *Longer than necessary* — accept is one click, reject is settings → toggle six → save.
- *Misleading action* — "Save preferences" that grants everything.

**Fickle** — "The design of the interface is unstable and inconsistent."

- *Lacking hierarchy* — the same purpose described three different ways across layers.
- *Decontextualising* — withdrawal buried in the account area of a site that has no accounts.
- *Inconsistent interface* — mobile banner offers a reject button, desktop does not, or the buttons swap position.
- *Language discontinuity* — German page, English banner.

**Left in the dark** — "The interface is designed in a way to hide information or controls related to data protection."

- *Conflicting information* — banner says "we do not sell your data", vendor list contains ad exchanges.
- *Ambiguous wording or information* — "Enhance your experience" as the label for advertising cookies.

## Enforcement context

The noyb cookie-banner complaint programme that produced the Cookie Banner Taskforce is still running. EDPB Binding Decision 1/2026 (adopted 28 May 2026) addressed whether such a complaint against the Flemish broadcaster VRT could be dismissed as an abuse of the right to lodge a complaint and of the right to mandate a not-for-profit body; the EDPB's decision required the Belgian supervisory authority to handle the merits. Treat first-layer banner defects as live enforcement risk, not theoretical.

## Checkpoints

- [ ] Reject button present on the first layer, same element type as accept
- [ ] Accept and reject equal in size, weight, contrast and position emphasis
- [ ] Reject text contrast ratio ≥ 4.5:1 against its own background
- [ ] No category pre-ticked except strictly necessary, which is disabled and explained
- [ ] Escape, backdrop click and scroll do not write consent
- [ ] Settings reachable from a persistent footer link on every route
- [ ] Reopened settings reflect the stored state
- [ ] Revoking all takes no more interactions than accepting all
- [ ] Banner locale follows page locale
- [ ] Banner is keyboard operable and focus-trapped while open
- [ ] No promotional content inside the consent dialog
- [ ] Cookie wall, if proposed, escalated for legal sign-off rather than built
