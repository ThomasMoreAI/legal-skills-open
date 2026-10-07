# Model Clause — Opt-Out Disclosures

> **Use note.** Multi-state opt-out disclosures must address the right to opt out of: (1) sale of PD, (2) cross-context behavioral advertising / targeted advertising, (3) profiling for legal or similarly significant decisions (where applicable). Mechanism must include a clear and conspicuous link or page, and (in UOOM-mandate states) recognition of the Global Privacy Control.
>
> **Never paste verbatim.** Tune to actual practices.

---

## Your Privacy Choices

**Effective: [Date — AD format]**

Depending on where you live, you have the right to opt out of certain uses of your personal information. This page explains your choices and how to exercise them.

### Opt out of sale or sharing of personal information

We may [sell / share] certain categories of your personal information for purposes including [cross-context behavioral advertising / measurement / analytics across non-affiliated services]. You can opt out at any time.

To opt out:

- **Click "[Do Not Sell or Share My Personal Information](#)"** to update your preference for this device or browser.
- **Set the Global Privacy Control (GPC) signal** in your browser. We honor GPC as a valid opt-out request for [California, Colorado, Connecticut, Oregon, Montana, New Jersey, New Hampshire, Minnesota, Maryland, Delaware, Rhode Island, Florida] residents.
- **Submit a request through your account settings** (logged-in users). When you opt out while logged in, the opt-out applies to your account across devices.
- **Email us** at [privacy@example.com] or call [toll-free phone].

### Opt out of targeted advertising

For residents of [Virginia, Colorado, Connecticut, Texas, Oregon, Montana, Indiana, Tennessee, Delaware, New Jersey, New Hampshire, Nebraska, Kentucky, Maryland, Minnesota, Rhode Island, Florida]: you have the right to opt out of processing of your personal information for the purpose of targeted advertising. To opt out, [follow the steps above].

For California residents: opting out of "sharing" addresses cross-context behavioral advertising.

### Opt out of profiling for significant decisions

For residents of states whose privacy laws provide this right: you have the right to opt out of profiling that produces legal or similarly significant effects (such as decisions about [credit, employment, housing, insurance, healthcare]). [Describe the controller's profiling activities, if any. If the controller does not engage in profiling for significant decisions, state so plainly.]

### Limit Use of Sensitive Personal Information (California)

For California residents: if we use your sensitive personal information for purposes beyond providing the goods or services you reasonably expect, you may direct us to limit such use. To exercise this right, click **[Limit the Use of My Sensitive Personal Information](#)**.

### Authorized agents

You may designate an authorized agent to submit a request on your behalf. We will request:
- Written authorization from you, signed by you.
- Verification of the agent's identity.
- Verification (with you) that you authorized the agent.

### What happens after you opt out

When you opt out:
- We stop selling and sharing your personal information.
- We stop using your personal information for targeted advertising.
- We notify the third parties we have disclosed personal information to of your opt-out.
- We persist your opt-out for at least 12 months and require you to affirmatively opt in to resume.

You may continue to see ads, but they will not be based on tracking your activity across non-affiliated sites.

### Children and teens

For consumers known to us to be under 13: we do not sell or share their personal information without parental consent.

For consumers known to us to be 13 to 16 (California) or 13 to 17 (some other states): we do not sell or share their personal information for cross-context behavioral advertising without their opt-in consent (or, where required, a parent's consent).

For Maryland residents under 18: we do not sell their personal information or process it for targeted advertising regardless of consent (per Md. Code Com. Law § 14-4607).

### Right to non-discrimination

We will not discriminate against you for exercising your privacy rights. We will not deny goods or services, charge different prices, or provide a different level or quality of service because you exercised your rights, except as permitted by law (for example, where the difference is reasonably related to the value of the data).

### Appealing a denied request

If we deny a privacy request, you have the right to appeal in [Virginia, Colorado, Connecticut, Texas, Oregon, Montana, Indiana, Tennessee, Delaware, New Jersey, New Hampshire, Nebraska, Kentucky, Maryland, Minnesota, Rhode Island, Florida]. To appeal, [process — typically email to a designated address with your prior request reference]. We will respond within [60 days / 45 days, depending on state].

---

## Implementation notes (delete from production)

1. **Link placement.** "Do Not Sell or Share My Personal Information" link must be on the homepage and (per CA) clearly conspicuous. Many states accept a link in the website footer plus a privacy choices page; CA's enforcement focuses on the homepage placement.
2. **GPC handling.** The mention of GPC must reflect actual implementation. If GPC is not handled, the disclosure is misleading.
3. **State list.** The state list in each section must be kept current as new laws take effect or are amended. Recommend the controller use a single "Privacy Choices" page that updates dynamically rather than listing states inline.
4. **Profiling.** If the controller does not profile for significant decisions, the section can be brief; if it does, expand with specifics about the activity, the consequences, and the consumer's recourse.
5. **Authorized agent.** Required in CA; permitted in CO/CT for opt-out only; varies elsewhere. Configure intake accordingly.
6. **Appeal procedure.** Required in most states (not CA, UT, IA). Surface the procedure for those that require it.
