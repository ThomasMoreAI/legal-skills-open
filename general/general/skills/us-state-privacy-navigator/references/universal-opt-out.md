# Universal Opt-Out Mechanisms (UOOMs) — Implementation Reference

**Purpose.** Operational guidance for recognizing universal opt-out signals — most prominently the Global Privacy Control (GPC) — under the state laws that mandate it.

## What a UOOM is

A universal opt-out mechanism is a browser-, device-, or platform-level signal that allows consumers to communicate an opt-out preference to all websites or applications in a single signal — see Cal. Civ. Code § 1798.135(b), 11 CCR § 7025, Colo. Rev. Stat. § 6-1-1306(1)(a)(IV), and 4 CCR § 904-3, R 5.07 — rather than having to navigate to each site's "Do Not Sell" link individually. The dominant UOOM is the **Global Privacy Control (GPC)**, an HTTP header (`Sec-GPC: 1`) and DOM property (`navigator.globalPrivacyControl`) that browsers and browser extensions can set.

## States requiring UOOM recognition

| State | Effective | Mechanisms |
|---|---|---|
| CA | In effect (CCPA Regs § 7025) | Per CCPA Regs; GPC is recognized; CPPA enforces |
| CO | July 2024 | Per AG-published list; currently GPC |
| CT | Jan 2025 | Per CT AG; GPC |
| OR | Jan 2026 | Per ORS § 646A.578 |
| MT | Jan 2025 | |
| NJ | July 2025 (six months after effective date) | |
| NH | Jan 2025 | |
| MN | Jan 2026 | |
| MD | Oct 2025 | |
| DE | Jan 2026 | |
| RI | Jan 2026 | |
| FL | Required | Per FDBR |

States NOT requiring UOOM recognition: VA, UT, IA, TN, NE, KY, IN, TX (mandates opt-out method but does not specify UOOM by name; verify current AG guidance).

## What "recognition" requires

A controller subject to UOOM rules must, at minimum:

1. **Detect the signal** at the page-load or session level. For web, check `Sec-GPC: 1` HTTP header on every request and `navigator.globalPrivacyControl === true` in the DOM.
2. **Treat the signal as a valid opt-out request** without requiring the consumer to sign in, click a button, or take any further action. The signal IS the opt-out.
3. **Apply the opt-out to all sale, sharing, and (where applicable) targeted advertising and profiling activities** for that browser/device. Some states (CA, CO, CT) require application across the consumer's known account (logged-in profile), not just the browser session.
4. **Persist the opt-out** for the consumer's known account or as a durable preference for the browser/device.
5. **Reflect the opt-out in downstream ad-tech and analytics integrations** — the controller's opt-out signal must be passed through to ad networks, DMPs, and analytics providers consistent with the IAB Multi-State Privacy Agreement (MSPA) framework or equivalent.
6. **Not "frustrate" the signal** by requiring re-confirmation, repeated prompts, or steps that effectively negate the opt-out.

## Common implementation failure modes

These are the issues that have driven enforcement action and that should be tested for in any compliance program:

1. **Signal detected but not honored.** The controller's CMP detects GPC but does not actually disable third-party tags. This was the core issue in *In re Sephora*, the first major CCPA enforcement action.
2. **Signal applied only to anonymous users.** When a consumer logs in, the opt-out is dropped. CA, CO, CT explicitly require application to known accounts. Failing to persist is a violation.
3. **Server-side detection only, with client-side tags firing before server-side block.** Many CMPs check GPC server-side but allow the page to load with tags already executing. Implementation must intercept at the earliest possible point.
4. **Pixel-level non-compliance.** Even when first-party tags respect GPC, embedded third-party iframes (e.g., chat widgets, video players, social embeds) often do not. The controller is responsible for the third parties it embeds.
5. **No mobile / app handling.** GPC is a web standard. Apps require separate platform-specific opt-out signals (e.g., Apple's App Tracking Transparency framework, Google's Privacy Sandbox). Most states' UOOM rules apply to the web environment specifically; mobile compliance is via the platform-specific opt-out + the controller's own in-app opt-out.
6. **CMP misconfiguration.** Many CMPs have GPC handling toggled off by default. Audit the CMP configuration.

## Implementation patterns

### Web (standard)

**Server-side**: at the request layer (e.g., middleware, edge function), inspect the `Sec-GPC` header. If present and value is `1`, set a session-level flag for the user that triggers downstream tag suppression.

**Client-side**: check `navigator.globalPrivacyControl`. If `true`, suppress non-essential third-party scripts via the CMP API or a tag manager rule.

**Tag manager**: configure Google Tag Manager / Tealium / Segment / Adobe Launch with a GPC-aware variable that gates conditional tag firing.

**CMP**: ensure the CMP recognizes GPC as an opt-out signal under 11 CCR § 7025(b)–(c) and updates its consent state accordingly. Most CMPs (OneTrust, Cookiebot, Sourcepoint, etc.) support GPC handling but require explicit configuration.

### Logged-in users

When a consumer authenticates, the controller must (per Cal. Civ. Code § 1798.135(b)(2); 11 CCR § 7025(c)(7); Colo. Rev. Stat. § 6-1-1306(1)(a)(IV)):
1. Persist the opt-out in the consumer's account record.
2. Apply the opt-out across the consumer's devices and sessions.
3. Allow the consumer to revoke (a known user opting back in via clear, affirmative action).

### Mobile / native apps

State UOOM rules generally apply to the web environment. (See 11 CCR § 7025(a) (defining covered "platform").) For apps, the controller must provide an in-app opt-out method consistent with state opt-out duties, and respect platform-level privacy frameworks (App Tracking Transparency on iOS, Privacy Sandbox / Limit Ad Tracking on Android).

### Other channels

For offline (e.g., point-of-sale, call center, email), the controller must offer an opt-out method per the state's general opt-out rule under Cal. Civ. Code § 1798.135(a) and 11 CCR § 7026. UOOM-specific mandates do not typically extend to these channels.

## IAB MSPA / GPP

The IAB Multi-State Privacy Agreement and Global Privacy Platform (GPP) specify a structured way for publishers to communicate consumer opt-out states to ad-tech vendors. Adoption is widespread among ad-tech participants. A controller using IAB MSPA strings + GPP signals through its ad-tech stack is generally well-positioned for UOOM compliance, but signal accuracy must be tested.

## Documentation and audit

Maintain documentation of:
- The CMP's GPC handling configuration.
- Test results showing GPC is detected and tags are suppressed (use tools like the EFF's GPC test page).
- Consumer-account-level opt-out persistence logic.
- Vendor flow-down agreements requiring downstream respect of opt-out signals.

## Common mistakes in advice

- **Saying "GPC counts as a global opt-out"** without specifying which states require recognition. (Not all do.)
- **Confusing GPC with Do Not Track (DNT)**. DNT was a defunct earlier proposal; many state laws explicitly do NOT require DNT recognition (CA's CCPA Regs § 7025 specifies opt-out preference signals, not DNT).
- **Treating consent banner choices as overriding GPC**. They do not. If GPC is set, the consumer has opted out — the banner cannot override.
- **Assuming a CMP solves UOOM compliance**. The CMP may handle the signal but cannot solve underlying tag-architecture problems (e.g., hardcoded third-party scripts, server-side ad-tech).
