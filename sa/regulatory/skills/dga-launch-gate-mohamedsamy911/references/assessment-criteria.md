# DGA Assessment Criteria

**Source:** https://design.dga.gov.sa/AssessmentCriteria · **Retrieved:** 2026-08-27
**Raw capture:** `https://github.com/mohamedsamy911/dga-kit/blob/master/harvest/raw/2026-08-27-section-sweep.md` in the dga-kit repo (not shipped with
the installed skill)

The rubric a Saudi government platform is **actually scored against** before it may deploy. Every
other file in this kit describes what DGA *says*; this one describes how DGA *marks*.

> ⚠️ Until 2026-08-27 this kit recorded the Assessment Criteria as an unreachable off-site
> download and left `SKILL.md` §6 incomplete because of it. That was wrong — the page is public.
> The **downloadable checklist file** is still a separate artefact and is **still not obtained**,
> so this file covers the published rubric, not the checklist's individual line items. Do not
> claim item-level coverage.

DGA names the audience explicitly: **designers, developers, stakeholders, project managers, and
quality assurance specialists.**

---

## The four scored categories

| Category | What is evaluated |
|---|---|
| **Accessibility** | Adherence to **WCAG** for users with disabilities, and *"compatibility with assistive technologies"* |
| **Consistency** | *"uniform use of design tokens like colors, typography, spacing"* and adherence to guidelines, for a cohesive identity |
| **Design** | Visual consistency with the **design tokens and the UI Kit**, plus **responsive** design across all devices |
| **Usability** | Clarity, intuitiveness, logical flow, **load times**, and task completion |

Two of these reach beyond what a design review covers: **Accessibility** is `dga-a11y`'s lane, and
**Usability** includes *load times*, which no other DGA page mentions and which nothing else in
this kit checks. A slow platform loses marks in a category no design audit will catch.

---

## Compliance levels

DGA publishes three levels and defines them in the page's FAQ:

<!-- dga -->
> **Mandatory** criteria are non-negotiable and must be met for the project to proceed. These
> often relate to legal, security, and core functionality requirements.

> **Recommended** criteria are not essential for project approval but are advised to enhance
> quality, user experience, or future scalability. Meeting these can differentiate the project
> positively.

> **Optional** criteria are additional enhancements that could provide a competitive advantage or
> long-term benefits but are not critical for the current phase of the project.
<!-- /dga -->

### Mandatory compliance

DGA's page labels this group **Essential** and its criteria **Mandatory Compliance**; the FAQ
defines the level as **Mandatory**. This file leads with *Mandatory* because that is the word
DGA's own definition uses — *"non-negotiable and must be met for the project to proceed."*

Four criteria. Failing one is what DGA describes below under *Consequence of failure* — read the
exact wording there before telling a team they are blocked.

- [ ] **Design System Compliance** — *"Ensure the Unified Design System (Platforms Code) version
      1.0 is correctly implemented."*
- [ ] **Typography and Color Standards** — *"Implement approved primary text colors and functional
      colors in line with the Unified Design System."*
- [ ] **Layout and Spacing** — *"Follow the specified layout and spacing guidelines, including
      wireframe dimensions, a **mobile-first approach**, and a **spacing grid**."*
- [ ] **Mobile Usability** — *"fully usable on mobile devices, considering […] touch interactions,
      viewport sizing, and navigational access on smaller screens."*

> 🚩 **Typography and Color Standards is where DGA's own defect bites.** The criterion is
> *"approved primary text colors"*. `text.secondary` (#dba102) carries a text role name and
> measures **2.30:1** — it fails the Accessibility category while nominally satisfying the colour
> one. Use `secondary-gold.800` (#945c01) or darker for gold text. See
> `../../dga-design-system/references/CONTRAST-AUDIT.md`.

> **Mobile-first is mandatory, not a preference.** It appears here as an Essential criterion and
> again on `/thoughts/responsive-design`. A desktop-first build that was later made to fit small
> screens does not satisfy it.

### Recommended

Four criteria. Not blocking, but *"meeting these can differentiate the project positively."*

- [ ] **Design Consistency and Standards Compliance** — approved icons, custom-icon guidelines,
      consistent visual elements, components implemented per the design system
- [ ] **User Experience and Interaction Design** — interaction effectiveness, intuitive navigation,
      efficient task completion; *"errors are clearly explained, feedback is immediate, and
      interface behavior is predictable"*
- [ ] **Content Strategy and Localization** — a sitemap supporting navigation and content
      discoverability; **an Arabic-first content strategy**; clear, concise language
- [ ] **Usability and Accessibility** — effective search, accessible help resources, user feedback
      mechanisms, **privacy notice visibility**, consistent error handling

> 🚩 **"Ensure an Arabic-first content strategy" is DGA's own sentence.** This kit has treated
> Arabic-first as a derived principle. It is not — cite `/AssessmentCriteria` for it directly.
> It is Recommended rather than Essential, which is worth knowing before arguing it as a blocker.

### Optional

Named in the FAQ, **no criteria published**. Do not invent them, and do not tell anyone their
project has met an Optional level that DGA has not defined.

---

## Submission and timeline

<!-- dga -->
> Assessment should be submitted **at least two weeks before** the desired review date to allow
> sufficient time for thorough assessment.
<!-- /dga -->

The review itself runs about twenty days:

| Days | Stage | What happens |
|---|---|---|
| 1–2 | Initial screening | Submission confirmed; preliminary check that mandatory documents and elements are present |
| 3–10 | Detailed assessment | Design review · **accessibility review** · usability testing · compliance check against mandatory/recommended/optional |
| 11–12 | Compilation of feedback | Reviewers compile reports; review team consolidates findings |
| 13–15 | Feedback and revisions | Detailed feedback issued; project team implements changes |
| 16–20 | Final review and approval | Revised project resubmitted; **approved or rejected** |
| post-20 | Documentation and closure | Documents archived; deployment, or re-assessment if rejected |

**Plan for ~5 weeks** between "we think we are done" and an approval: two weeks of lead time plus
the twenty-day review. A revision cycle is built into the timeline, so expect one.

### What submission requires

- The completed **Assessment Checklist**, with project details, expected compliance levels, and
  comments
- Documentation (DGA marks this optional): research documents, user manuals, test reports
- Submitted through DGA's assessment form

DGA's own advice on preparing it:

> Prepare documentation showing **how each criterion was met**, including references, screenshots,
> and code snippets. This is crucial for formal reviews or audits.

> Download the checklist and use it **at each project stage, not just at the end**. […] The
> checklist is updated regularly.

> Before submitting your project, have **someone else** review the checklist to ensure all
> criteria are met.

---

## Scoring

Scored 1–100 and reported as a 1–10 grade:

| Grade | Band |
|---|---|
| 1 – 1.9 | Non-Compliant |
| 2 – 2.9 | Very Poor Compliance |
| 3 – 3.9 | Poor Compliance |
| 4 – 4.9 | Below Average Compliance |
| 5 – 5.9 | Fair Compliance |
| 6 – 6.9 | Moderate Compliance |
| 7 – 7.9 | Good Compliance |
| 8 – 8.9 | Very Good Compliance |
| 9 – 9.9 | Excellent Compliance |
| 10 | Outstanding Compliance |

> DGA publishes **no passing threshold** and does not say how the four categories are weighted.

### Consequence of failure — quote it exactly

DGA says this once, in the page's FAQ, answering *"What happens if a project fails to meet
mandatory criteria?"*. There is no section of the page with this heading.

<!-- dga -->
> If a project fails to meet mandatory criteria, it **typically** cannot proceed to deployment.
> The project team must address the deficiencies identified during the review process and resubmit
> the project for another review. Critical failures might require significant rethinking of project
> scope, design, or even objectives.
<!-- /dga -->

> 🚩 **Keep the word "typically".** DGA describes the normal outcome, not an absolute rule, and it
> names no exception process — so nobody outside DGA can say when the exception applies. Dropping
> the hedge turns a description into a guarantee this kit cannot back, which is the failure mode
> `cite or omit` exists to prevent.

So the defensible reading: **the mandatory criteria are the ones that normally decide whether a
project ships; the 1–100 score is a quality grade on top.** Report an unmet mandatory criterion as
*"DGA states this typically blocks deployment"* — never as *"this blocks deployment."* And do not
quote a target score; DGA has not set one.

---

## How this maps onto the rest of the kit

| DGA category | Checked by |
|---|---|
| Accessibility | `dga-a11y` (running code), `dga-design-review` pass 6 (design) |
| Consistency | `dga-design-review`, `dga-ui-adapter` (token wiring), `dga-tokens-sync` |
| Design | `dga-design-review`, `dga-mockup` |
| Usability | **partly uncovered** — no skill checks load times or task-completion efficiency |
| Content Strategy and Localization | `dga-content-writer`, `dga-rtl-i18n` |

> The **Usability** category is the kit's weakest coverage. Clarity and error handling are
> reviewable; *load times* and *task completion* are measured, not read. Say so rather than
> implying a design audit covers them.
