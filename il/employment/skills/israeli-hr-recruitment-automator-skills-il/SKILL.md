---
name: israeli-hr-recruitment-automator-skills-il
title: Israeli HR Recruitment Automator
description: Not legal advice. Employer-side hiring automation for Israeli companies. Drafts Hebrew job descriptions against the published requirements of the Equal Employment Opportunities Law 1988, posts to Israeli job boards (AllJobs, Drushim, JobMaster, LinkedIn Israel), screens resumes with Israeli context (military service, academic institutions, tech bootcamps), schedules interviews around Israeli holidays and Shabbat, and generates offer letters with mandatory Israeli employment clauses. Use when user asks to "write a job description", "post a job in Israel", "screen Israeli resumes", "pirsum misra", "srikat meumadim", "michtav ha'a'sa'a", or automate hiring workflows for Israeli companies. Do NOT use for job searching (use israeli-job-market), interview preparation (use israeli-tech-interview-prep), salary negotiation (use israeli-tech-salary-negotiator), employment contracts legal review (use israeli-employment-contracts), or freelancer hiring.
author: skills-il
author_url: https://github.com/skills-il/communication/tree/master/israeli-hr-recruitment-automator
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: il
practice: employment
language: en
sources:
- title: Adjacent Duties
  path: references/adjacent-duties.md
- title: Anti Discrimination Law
  path: references/anti-discrimination-law.md
- title: Domain Checklist
  path: references/domain-checklist.md
- title: Mandatory Benefits
  path: references/mandatory-benefits.md
---

# Israeli HR Recruitment Automator

## Legal notice

This skill is not legal advice and does not substitute for a licensed Israeli lawyer
(עורך דין) or a licensed accountant. It explains published employment-law duties and drafts
document text from employer-supplied inputs. It does not decide whether a specific screening
question, dismissal, or contract term is lawful in your circumstances, and it does not settle
a dispute. Anti-discrimination exposure under the Equal Employment Opportunities Law 1988 and
data-protection exposure under the Privacy Protection Law are fact-specific. Have a lawyer
review any job advertisement, screening policy, offer letter, or candidate-data policy before
you rely on it. The model may err, omit data, or state a wrong conclusion. Any text this skill
drafts, including an offer letter, is an automatic draft for your own organisation only. It is
not a document drawn by a lawyer, and it is not the statutory notice of employment terms. It
is not a substitute for advice that takes account of the particular circumstances and needs of
any individual, and any use of its output is the user's sole responsibility.

## Instructions

### Step 1: Draft Hebrew Job Descriptions Against the Published Requirements

When the user needs to create a job posting, generate a Hebrew job description (teur misra) and check it against the requirements the Equal Employment Opportunities Law 1988 (chok shivyon hizdamnuyot ba'avoda) publishes. Whether a given advertisement is lawful turns on facts this skill does not see.

**Anti-discrimination compliance checklist.** The job description MUST NOT:

| Prohibited Criterion | Law Reference | Example of Violation |
|---|---|---|
| Gender | Section 2(a) | "Looking for a male developer" |
| Age | Section 2(a) | "Ages 25-35 only" |
| Marital/parental status | Section 2(a) | "Single candidates preferred" |
| Pregnancy | Section 2(a) | "Not suitable for pregnant women" |
| Sexual orientation | Section 2(a) | Any reference to orientation |
| Ethnicity/nationality | Section 2(a) | "Jewish/Arab candidates only" |
| Country of origin | Section 2(a) | "Born in Israel" |
| Religion | Section 2(a) | "Sabbath-observant only" |
| Political views / party | Section 2(a) | Any party affiliation requirement |
| Place of residence | Section 2(a) | "Central region residents only", "must live near the office" |
| Reserve duty | Section 2(a) | "No miluim obligations" |
| Fertility / IVF treatments | Section 2(a) | "Not planning fertility treatment" |

**Section 8 is a separate offence from section 2.** Section 8(a) requires that a job
advertisement state the offer **in both masculine and feminine form**, singular or plural
("לא יפרסם מודעה בדבר הצעת עבודה ... אלא אם כן הצעת העבודה צויינה בלשון זכר ובלשון נקבה").
This binds the whole ad, not just the job title, so masculine-only verbs, adjectives and
pronouns in the body breach it even when the title is written "מפתח/ת". The bundled validator
checks only a handful of common title nouns, so **read the whole draft yourself for gendered
forms; a PASS from the script is not compliance with section 8.**

**Appearance is NOT an enumerated ground.** The word מראה appears nowhere in the Equal
Employment Opportunities Law. Height, weight and attractiveness requirements are still bad
practice and are attackable as a proxy for an enumerated ground or as a non-occupational
requirement, but do not tell a user they violate section 2(a). Disability sits in a different
statute, the Equal Rights for Persons with Disabilities Law 1998, and that is the statute to
cite for the reasonable-accommodation duty.

**Permitted requirements:**
- Genuine occupational qualifications (e.g., Hebrew fluency for a Hebrew content role)
- Security clearance where legally required
- Specific professional certifications or licenses
- Physical fitness requirements tied directly to job duties

**Job description structure (Hebrew template):**

```
כותרת המשרה: [Title]
חברה: [Company name]
מיקום: [Location]
סוג משרה: [Full-time/Part-time/Hybrid]
תחום: [Field]

תיאור התפקיד:
[2-3 paragraphs about the role, team, and company]

דרישות התפקיד:
- [Requirement 1]
- [Requirement 2]

דרישות רצויות (יתרון):
- [Nice-to-have 1]

מה אנחנו מציעים:
- [Benefit 1]
- [Benefit 2]

להגשת מועמדות: [Application instructions]
```

**Key rules:**
- Use gender-neutral language. In Hebrew, use both masculine and feminine forms: "מפתח/ת", "מנהל/ת" or the inclusive plural form
- List "requirements" vs "nice-to-haves" (yitron) separately to avoid discouraging qualified candidates
- Never list age, military unit, or academic institution as a requirement unless it is a genuine occupational qualification
- Include salary range when possible (not legally required but considered best practice)

Consult `references/anti-discrimination-law.md` for the full legal summary.

### Step 2: Post to Israeli Job Boards

After generating the job description, help the user post to Israeli job boards.

**Major Israeli job boards (2026):**

| Platform | URL | Programmatic posting | Notes |
|---|---|---|---|
| AllJobs | alljobs.co.il | Web employer portal only, no public API documentation | Largest Israeli job board, supports Hebrew postings |
| Drushim | drushim.co.il | Web employer console only, no public API documentation | Strong in tech and startup roles |
| JobMaster | jobmaster.co.il | Web employer area | General job board |
| LinkedIn Israel | linkedin.com | Yes, documented LinkedIn API (partner access) | International and tech roles, English-friendly |
| Comeet | comeet.com | Yes, documented API | Israeli ATS with job board distribution |

**Do not tell the user an Israeli board has a REST API unless you have opened its
documentation in this session.** No public API documentation exists for AllJobs, Drushim or
JobMaster as of August 2026, only human employer portals. An agent that assumes an API will
invent endpoints and field names. Glassdoor no longer operates a separate Israeli property:
`glassdoor.co.il` redirects to `glassdoor.com`. `gethired.co.il` no longer resolves at all.

**Posting workflow:**
1. Adapt the Hebrew job description for each platform's format and character limits
2. For AllJobs: use their structured fields (category, sub-category, region, city)
3. For LinkedIn: create both Hebrew and English versions
4. Set appropriate filters: experience level, job type (misra mle'a / chalkeet), location
5. Track posting IDs for each platform to monitor applications

**Posting tips:**
- AllJobs and Drushim have peak traffic Sunday-Tuesday
- Post by 9:00 AM Israel time for maximum visibility
- Refresh listings every 7-10 days (most boards penalize stale postings)
- Use AllJobs "hot job" promotion for urgent positions

### Step 3: Screen Resumes with Israeli Context

When screening resumes (korot chaim), apply Israeli-specific context to evaluate candidates fairly and accurately.

**Military service (sherut tzva'i) interpretation:**

| Service Type | Typical Duration | What It Indicates |
|---|---|---|
| Combat (kravi) | 32-36 months | Leadership, teamwork, physical resilience |
| Intelligence (modi'in) | 32-36 months | Analytical skills, security clearance |
| Technology (8200, 81, Mamram) | 32-36 months | Technical skills, strong tech foundation |
| Officers (ktzinim) | 36+ months | Management, responsibility |
| National service (sherut leumi) | 12-24 months | Community orientation, social skills |
| No service | N/A | Do NOT assume negative; many exemptions exist |

**IMPORTANT:** Never use military service type or unit as a filtering criterion. It is informational context only. Filtering by military unit violates the Equal Employment Opportunities Law.

**Do not rank academic institutions.** Israeli CVs name research universities, accredited
colleges, tech bootcamps and online degrees, and an agent handed a tier table will rank on it.
Institution prestige is not a job requirement and ranking on it disadvantages bootcamp
graduates and candidates who studied abroad. Treat the institution as context only.

**Resume screening best practices:**
- Focus on skills and experience, not institution prestige
- Treat bootcamp graduates equally for relevant technical roles
- Account for career gaps due to military reserve duty (miluim), maternity leave, or gap years (common in Israel after army service)
- Hebrew resumes may use different date formats (DD/MM/YYYY)
- Look for relevant volunteer work and side projects, which are common in the Israeli tech ecosystem

### Step 4: Schedule Interviews with Israeli Calendar Awareness

Schedule interviews while respecting Israeli holidays, Shabbat, and business customs.

**Israeli work week:** Sunday through Thursday (yom rishon through yom chamishi). Friday is a short workday for some companies (until 12:00-14:00). Saturday (Shabbat) is a rest day.

**Key holidays to avoid (2026):**

| Holiday | Hebrew Name | Dates (2026) | Duration |
|---|---|---|---|
| Purim | פורים | Mar 3 | 1 day (Mar 4 in walled cities / Shushan Purim) |
| Pesach | פסח | Apr 1 (eve) - Apr 8 | First seder Apr 1 evening. In Israel: Yom Tov Apr 2 (first day) and Apr 8 (Shvi'i shel Pesach); chol hamoed Apr 3-7. (The 2-day Yom Tov at each end is the Diaspora schedule, not Israel.) |
| Yom HaShoah | יום השואה | Apr 14 | 1 day (siren 10:00) |
| Yom HaZikaron | יום הזיכרון | Apr 20 (eve) - Apr 21 | 1 day (sirens 20:00 prev day, 11:00) |
| Yom Ha'Atzmaut | יום העצמאות | Apr 21 (eve) - Apr 22 | 1 day |
| Shavuot | שבועות | May 21 (eve) - May 22 | 1 day |
| Tisha B'Av | תשעה באב | Jul 23 | Fast day, partial work day in some firms |
| Rosh Hashana | ראש השנה | Sep 12-13 | 2 days |
| Yom Kippur | יום כיפור | Sep 21 | 1 day (fasting, no work) |
| Sukkot | סוכות | Sep 26 - Oct 3 | First/last days Yom Tov (Sep 26 + Oct 3); Sep 27-Oct 2 chol hamoed |
| Hanukkah | חנוכה | Dec 4-12 | 8 days (workdays, school off) |

**Scheduling rules:**
- Never schedule on Shabbat (Friday evening to Saturday evening)
- Avoid scheduling on holiday eves after 13:00
- Prefer Sunday-Thursday, 09:00-17:00 Israel time (IST/IDT, UTC+2/+3)
- Allow 30-minute buffer for Israeli traffic conditions
- For tech companies: many operate flexible hours, confirm company culture first
- Video interviews: use Israel-friendly platforms (Zoom, Google Meet, Teams)

### Step 5: Generate Offer Letters with Mandatory Israeli Clauses

When generating an offer letter (michtav ha'asa'a), include all mandatory employment benefits as required by Israeli labor law.

**Mandatory benefits table (2026):**

| Benefit | Employee Contribution | Employer Contribution | Notes |
|---|---|---|---|
| Minimum wage (sachar minimum) | N/A | NIS 6,443.85 / month, NIS 35.40 / hour | Effective Apr 1, 2026 (raise from NIS 6,247.67). Offer letter salary must meet or exceed. |
| Pension (pensia) | 6.0% of salary | 6.5% of salary | Mandatory; retroactive from day 1 after 6 months without prior pension; from day 1 (or 3 months / end of tax year, whichever is first) for employees with prior pension |
| Keren Hishtalmut | 2.5% of salary | 7.5% of salary | Not mandatory but standard in tech sector; tax-exempt after 6 years. 2026 tax-exempt salary ceiling: NIS 15,712 / month |
| Severance (pitzuim) | N/A | 6% of salary (mandatory) | This is the pension extension order's severance component. Total mandatory contributions are 18.5%: 6% employee + 6.5% employer tagmulim + 6% employer severance. |
| Severance top-up (optional) | N/A | +2.33%, to 8.33% total | 8.33% is one twelfth of monthly salary, the full statutory severance accrual. An employer may deposit the extra 2.33% into the pension product. Depositing only the mandatory 6% leaves a gap the employer still owes on dismissal. |

**Section 14 waiver (siman 14):** Most employers include a Section 14 waiver (ishur klali le-pi siman 14), which means pension contributions count toward severance. This must be explicitly stated in the offer letter. Without it, the employer may owe full severance on top of pension contributions. **Critical precondition:** Section 14 only releases the employer to the extent actually deposited, from day 1, on the employee's full salary. Two distinct gaps are easy to miss. First, if contributions are delayed (for example through the 6-month new-employee window) or computed on base salary only, the exemption does not cover the uncovered period or the uncovered pay, and the employer stays liable for statutory severance on that part. Second, depositing the mandatory 6% severance component rather than the full 8.33% leaves roughly a quarter of the accrual outside the arrangement, so the employer owes the completion on dismissal. A full release requires depositing 8.33% and saying so in the offer letter.

**Never select the Section 14 arrangement for the employer.** Present the choice, the deposit
precondition (8.33% from day 1 on full salary) and the consequence of each option, then leave
the decision to them and their lawyer. Leave line 7 of the offer-letter template unfilled until
they answer.

**Vacation days (yemei chufsha) minimums by seniority:**

| Years of Service | Annual Vacation Days |
|---|---|
| 1-5 | 16 calendar days (about 11-12 workdays on a 5-day week) |
| 6 | 18 calendar days |
| 7 | 21 calendar days |
| 8+ | Additional day per year (up to 28 calendar days) |

Note: years 1-4 were raised from 14 to 16 calendar days by Amendment 15 to the Annual Leave Law (in force since 2017), so all of years 1-5 now accrue 16 calendar days.

**Other mandatory terms:**

| Term | Requirement |
|---|---|
| Sick days (yemei machala) | 1.5 days per month, up to 90 days accumulated |
| Convalescence pay (dmei havra'a) | 5-10 days per year depending on seniority. Private-sector rate for convalescence year 2026: NIS 451.5 per day, raised from NIS 418 by an extension order published 18 August 2026 covering 1 July 2025 to 30 June 2026. Public-sector rate: NIS 511.6 per day. Sample annual entitlements at NIS 451.5: year 1 = 5 days = NIS 2,257.50; years 2-3 = 6 days = NIS 2,709; years 4-10 = 7 days = NIS 3,160.50. **Employers who already paid the 2026 convalescence year at NIS 418 owe the difference of NIS 33.50 per day.** |
| Overtime pay (sha'ot nosafot) | On a weekday: 125% for the first 2 overtime hours, 150% from the third. On the weekly rest day or a holiday the rates are higher: ordinary hours 150%, overtime 175% for the first 2 hours and 200% from the third. |
| Travel expenses (hoza'ot nesi'a) | Public transport reimbursement or set amount |
| Notice period (hodaa mukdemet) | Varies by seniority (1 day per month for first 6 months, then 2.5 days per month) |

**Offer letter structure:**

```
מכתב הצעת עבודה

לכבוד: [Candidate name]
תאריך: [Date]

הרינו שמחים להציע לך את התפקיד [Job title] בחברת [Company name].

פירוט תנאי ההעסקה:

1. תפקיד: [Job title]
2. תאריך תחילת עבודה: [Start date]
3. שכר ברוטו: [Salary] ש"ח לחודש
4. היקף משרה: [Full/Part time]
5. פנסיה: [X]% עובד, [X]% מעסיק
6. קרן השתלמות: [X]% עובד, [X]% מעסיק
7. סעיף 14: [Include Section 14 clause]
8. ימי חופשה: [X] ימים בשנה
9. ימי מחלה: בהתאם לחוק (1.5 ימים לחודש)
10. דמי הבראה: בהתאם לחוק
11. הוצאות נסיעה: [Amount/arrangement]
12. תקופת ניסיון: [X] חודשים
13. תקופת הודעה מוקדמת: [X] ימים
```

Consult `references/mandatory-benefits.md` for the complete benefits reference table.

### Step 6: Handle Candidate Data Under the Privacy Protection Law

A resume is personal data and a collection of resumes is a database under the Privacy
Protection Law (חוק הגנת הפרטיות). The Privacy Protection Authority (הרשות להגנת הפרטיות),
a unit of the Ministry of Justice, administers registration, notification and enforcement.
Raise the following with the user as employer duties to check; do not deliver a conclusion
about their specific setup.

| Duty | What it means for hiring |
|---|---|
| Notice at collection | Asking a candidate for personal data carries a duty to tell them why it is being collected. A bare "send us your CV" with no stated purpose does not discharge it. Put the notice on the application route itself, not only in a website privacy policy. |
| Purpose limitation | Hold the CV only while the recruitment purpose lasts. **There is no statutory number of months for CV retention.** The law sets a purpose test, not a clock. If the employer wants to keep CVs for future openings, that is a separate purpose needing its own consent, disclosed at collection. |
| Database registration | Registration runs through the Authority's own registry services (בקשה לרישום מאגר מידע). Whether a given recruitment database is registrable depends on the employer's circumstances. Check the Authority's current criteria rather than assuming either way. |
| Notification to the Authority | A separate duty applies to databases holding sensitive personal data at significant scale, under section 8א(ב) of the law. The Authority publishes the reporting instructions and the applicable scale. |
| Security-incident reporting | A serious security incident in a database is reportable to the Authority immediately, through a dedicated online service. A leaked candidate database is exactly this case. |

**Retention and the section 9 burden of proof pull in opposite directions. Say so.**
Section 9(a) puts the burden on the employer to prove it did not act contrary to section 2,
once an applicant shows they met the conditions or qualifications the employer itself set. In
practice the employer's defence IS its screening record: the published requirements, the
scoring rubric, the per-candidate scores and the stated reason for rejection. Purpose
limitation argues for deleting candidate data; section 9 argues for keeping enough of it to
defend a claim. These are not the same material. Advise keeping the **decision record** (the
criteria, the scores, the reason) while disposing of the underlying CV once the recruitment
purpose ends, and tell the user to set the period with their lawyer rather than guessing.

**Practical rules for the agent:**
- Never propose keeping rejected candidates' CVs indefinitely "just in case".
- Never advise deleting the screening decision record on privacy grounds alone. That is the employer's evidence under section 9.
- **Never invent a retention period, a subject-count threshold, an amendment number, or an entry-into-force date.** These are the details agents most reliably fabricate here. Cite the Authority's page or say you do not know.
- Do not tell an employer they definitely must, or definitely need not, register a database or appoint a privacy protection officer. State that thresholds exist, point at the Authority, and let them check against their own figures.
- Where the answer turns on the employer's data volumes, systems, or sector, route them to a lawyer practising privacy law rather than concluding.

### Adjacent duties this skill does NOT draft

Hiring triggers duties beyond the ad, the screening and the offer letter. Read
`references/adjacent-duties.md` and raise the relevant ones with the user. The triggers are:
every hire (a **written notice of employment terms**, a separate statutory document that an
offer letter does NOT discharge; sexual-harassment תקנון and ממונה duties), screening
(demanding a criminal-record extract is itself prohibited), a non-Israeli candidate (employer
permit and work visa), a candidate under 18, a candidate with a disability, scheduling work on
the weekly rest day (**prohibited without a permit**; the 150 / 175 / 200 percent rates price
work that is already permitted and do not authorise it), genetic or medical testing, large
employers (gender pay-gap reporting), and any sector with a collective agreement or extension
order. Never state a deadline, percentage or threshold for these from memory.

### Step 7: Run Compliance Checklist

Before finalizing any hiring document, run through this compliance checklist:

**Job Description Compliance:**
- [ ] No gender-specific language (uses inclusive forms)
- [ ] No age requirements or preferences
- [ ] No marital/parental status references
- [ ] No military unit or service type requirements
- [ ] No place-of-residence requirement or preference
- [ ] Ad is worded in both masculine and feminine form throughout, not only in the title (section 8)
- [ ] No ethnicity, religion, or national origin references
- [ ] Requirements are genuine occupational qualifications
- [ ] "Requirements" and "nice-to-haves" are clearly separated

**Offer Letter Compliance:**
- [ ] Pension terms specified (minimum 6% + 6.5%)
- [ ] Section 14 position stated as the employer decided it, not selected by the agent
- [ ] Vacation days meet legal minimum for employee's seniority
- [ ] Sick days referenced per law
- [ ] Convalescence pay (dmei havra'a) mentioned
- [ ] Notice period specified
- [ ] Start date and probation period defined
- [ ] Salary stated as gross (bruto)

**Candidate Data Compliance:**
- [ ] Application route carries a collection notice stating the purpose of collection and who is responsible for the data
- [ ] Retention of rejected candidates' CVs is time-bound and justified by a stated purpose
- [ ] Separate consent obtained if CVs are kept for future openings
- [ ] Registration / DPO thresholds checked against the employer's actual figures rather than assumed

**Interview Process Compliance:**
- [ ] No questions about marital status, children, or pregnancy plans
- [ ] No questions about religious observance
- [ ] No questions about military unit (may ask about service duration if relevant to experience)
- [ ] No questions about ethnicity or country of origin
- [ ] Reasonable accommodations offered for candidates with disabilities

Run the compliance checker script for automated validation:
```bash
python scripts/job-description-generator.py --validate --input job_description.txt
```

## Examples

### Example 1: Create a Hebrew Job Description for a Software Developer

User says: "Write a job posting for a senior full-stack developer at our Tel Aviv startup"

Actions:
1. Gather role details: tech stack, team size, company stage
2. Generate Hebrew job description using the template from Step 1
3. Run anti-discrimination compliance checklist
4. Use gender-neutral language throughout ("מפתח/ת", "מהנדס/ת")
5. Separate requirements from nice-to-haves
6. Include salary range if provided

Result: A Hebrew job description drafted against the Step 1 checklist, for the employer to review, and to have reviewed, before posting.

### Example 2: Screen a Batch of Resumes

User says: "I have 50 resumes for a product manager role, help me create a screening framework"

Actions:
1. Define screening criteria based on job requirements (not military unit or institution)
2. Create a scoring rubric: must-haves, nice-to-haves, red flags
3. Account for Israeli-specific resume patterns (army service section, gap years)
4. Flag resumes for phone screening vs rejection with reasons
5. Ensure no candidate is filtered based on protected characteristics

Result: A structured screening framework with a scored shortlist of candidates.

### Example 3: Generate an Offer Letter

User says: "Draft an offer letter for a QA engineer, 18,000 NIS gross, starting March 2026"

Actions:
1. Generate offer letter with all mandatory clauses
2. Calculate pension contributions (6% employee = 1,080 NIS, 6.5% employer = 1,170 NIS)
3. Ask the employer whether they are granting a Section 14 release and at what deposit rate; do not choose for them
4. Set vacation days to legal minimum (16 calendar days for years 1-5)
5. Add sick days, convalescence pay, and travel expense terms
6. Set notice period per seniority

Result: A draft offer letter in Hebrew covering the terms listed in Step 5, for the employer to complete and have reviewed. It is not the statutory notice of employment terms; see Adjacent duties.

### Example 4: Post to Multiple Job Boards

User says: "Post our DevOps engineer position to AllJobs and LinkedIn"

Actions:
1. Adapt the Hebrew job description for AllJobs format (structured fields)
2. Create an English version for LinkedIn
3. Select appropriate categories and filters on each platform
4. Recommend posting time (Sunday morning for maximum visibility)
5. Provide tracking instructions for monitoring applications

Result: Job posted on both platforms with tracking details.

## Bundled Resources

### Scripts
- `scripts/job-description-generator.py` -- Draft Hebrew job descriptions from structured input and flag wording that matches known discriminatory patterns. A clean run is not a compliance result. Run: `python scripts/job-description-generator.py --help`

### References
- `references/anti-discrimination-law.md` -- Summary of the Equal Employment Opportunities Law 1988 (chok shivyon hizdamnuyot ba'avoda). Lists all protected characteristics, permitted exceptions, enforcement mechanisms, and penalties. Consult when writing job descriptions or screening criteria.
- `references/domain-checklist.md` -- The coverage contract for this skill: what a complete Israeli hiring workflow must cover, what it should cover, and what is explicitly out of scope with the reasoning. Internal quality anchor; consult when deciding whether a request falls inside this skill's scope.
- `references/adjacent-duties.md` -- Statutory duties that hiring triggers but this skill does not draft: the written notice of employment terms, sexual-harassment prevention duties, the criminal-record demand prohibition, foreign-worker permits, minors, disability accommodation, rest-day permits, testing, pay-gap reporting, and collective agreements. Consult before telling a user that hiring is complete.
- `references/mandatory-benefits.md` -- Complete table of mandatory employment benefits in Israel for 2026. Includes pension rates, keren hishtalmut, vacation days by seniority, sick days, convalescence pay, overtime rules, and notice periods. Consult when drafting offer letters or employment terms.

## Gotchas

- Israeli job descriptions must use gender-inclusive Hebrew (e.g., "מפתח/ת" not "מפתח"). The Equal Employment Opportunities Law 1988 prohibits gender-specific job postings. Agents may generate masculine-only Hebrew forms.
- Military service type and unit (e.g., 8200, Mamram) must never be used as screening criteria, even though they appear on most Israeli resumes. Filtering by unit violates anti-discrimination law.
- Pension contributions in Israel are mandatory from day 1 (or after 6 months for first-time employees). The minimum is 6% employee + 6.5% employer. Agents may use outdated lower rates from pre-2017 regulations.
- Section 14 (Siman 14) waiver is standard in Israeli tech but must be explicitly stated in the offer letter. Without it, employers owe full severance on top of pension contributions. Agents may omit this critical clause.
- Israeli convalescence pay (dmei havra'a) has a per-day rate that is re-set by extension order roughly every year, usually mid-year, and the order is often published months after the convalescence year it governs. An agent quoting last cycle's rate will understate the entitlement, and the employer owes the difference retroactively. Re-check the rate rather than trusting a figure in a cached document.
- The pension extension order's mandatory severance component is 6%, not 8.33%. Agents routinely state 8.33% as the mandatory employer rate because it is the statutory severance accrual. Both numbers are real and they answer different questions, so an agent that conflates them will either overstate the employer's minimum obligation or wrongly report a Section 14 arrangement as complete.
- A CV is personal data under the Privacy Protection Law. Agents asked to "keep the good ones on file" will happily design indefinite retention, which the purpose-limitation rule does not permit.


## Reference Links

| Source | URL | What to Check |
|--------|-----|---------------|
| Equal Employment Opportunities Law (Nevo) | https://he.wikisource.org/wiki/חוק_שוויון_ההזדמנויות_בעבודה | Full text of Law 1988 with all amendments through 2025 |
| Kol Zchut, hiring obligations | https://www.kolzchut.org.il/he/חוק_שוויון_ההזדמנויות_בעבודה | Employer duties, mandatory notice to employee, recent amendments |
| Israel Ministry of Economy and Industry | https://www.gov.il/he/departments/ministry_of_economy | Minimum wage, mandatory benefits, equal pay |
| Israel Equal Employment Opportunities Commission | https://www.gov.il/he/departments/units/equal-opportunities-at-work-unit | EEOC complaint statistics, guidance, enforcement |
| Privacy Protection Authority | https://www.gov.il/he/departments/the_privacy_protection_authority | Current registration criteria, the section 8א(ב) notification duty, security-incident reporting, enforcement decisions |
| Kol Zchut, convalescence pay | https://www.kolzchut.org.il/he/דמי_הבראה | Current private and public sector per-day rate, extension-order date |
| Kol Zchut, mandatory pension insurance | https://www.kolzchut.org.il/he/חובת_ביטוח_פנסיוני_לעובדים | 18.5% split, severance component, Section 14 completion |
| AllJobs | https://www.alljobs.co.il | Job posting formats, category structure |
| Drushim | https://www.drushim.co.il | Alternative job board, posting conventions |

## Troubleshooting

### Error: "Job description flagged for discrimination"
Cause: The description contains language that references a protected characteristic (gender, age, marital status, military unit, etc.)
Solution: Review the anti-discrimination checklist in Step 1. Replace specific language with neutral alternatives. Use "mefateach/et" instead of gendered forms. Remove age ranges and military unit references.

### Error: "Missing mandatory clause in offer letter"
Cause: The offer letter does not include one or more required employment terms (pension, Section 14, vacation days, sick days, convalescence pay)
Solution: Compare against the mandatory benefits table in Step 5 and add the missing clause. Run: `python scripts/job-description-generator.py --validate --input offer_letter.txt`

### Error: "Interview scheduled on Israeli holiday"
Cause: The proposed interview date falls on a holiday or Shabbat
Solution: Check the holiday calendar in Step 4. Reschedule to a standard business day (Sunday-Thursday). Avoid holiday eves after 13:00.

### Error: "Candidate screened out by protected criterion"
Cause: Resume screening used military unit, academic institution tier, or personal status as a filter
Solution: Review Step 3 screening guidelines. Military service and institution are context only, never screening criteria. Focus on skills, experience, and job-relevant qualifications.
