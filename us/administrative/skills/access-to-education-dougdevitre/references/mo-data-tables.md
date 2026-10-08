# Missouri Education Data Tables

<!-- Structured lookup data. When a question requires a specific number, date, or fact, check here before loading a full reference file. -->
<!-- Last verified: 2026-03. Source for all data: DESE MCDS portal, DESE publications, Missouri statutes. -->

```mermaid
graph LR
    TABLES[Data Tables] --> STUDENT_PATH[Student Pathway]
    TABLES --> EDUCATOR_PATH[Educator Pathway]
    TABLES --> SYSTEM[System & Compliance]

    STUDENT_PATH --> T1[T1: Graduation Credits - 24 min]
    STUDENT_PATH --> T2[T2: EOC Exams - 4 subjects]
    STUDENT_PATH --> T3[T3: A+ Requirements]
    STUDENT_PATH --> T4[T4: Immunizations]
    STUDENT_PATH --> T5[T5: Assessment Calendar]
    STUDENT_PATH --> T8[T8: IDEA Disability Categories]
    STUDENT_PATH --> T9[T9: ACT Benchmarks]
    STUDENT_PATH --> T12[T12: State Scholarships]
    STUDENT_PATH --> T15[T15: FRPM Eligibility]

    EDUCATOR_PATH --> T7[T7: MEES Scoring]
    EDUCATOR_PATH --> T16[T16: Certificate Types]
    EDUCATOR_PATH --> T17[T17: PSRS Retirement]

    SYSTEM --> T6[T6: Key Statutes]
    SYSTEM --> T10[T10: MSIP 6 Standards]
    SYSTEM --> T11[T11: Drill Schedule]
    SYSTEM --> T13[T13: Hotlines]
    SYSTEM --> T14[T14: SPED Timelines]
```

---

## Table 1: Graduation Credit Requirements (DESE Minimum)

| Subject | Credits | Notes |
|---------|---------|-------|
| English Language Arts | 4.0 | |
| Mathematics | 3.0 | Must include Algebra I or higher |
| Science | 3.0 | Must include at least 1 lab science |
| Social Studies | 3.0 | Must include American History, American Government, World History |
| Fine Arts | 1.0 | |
| Practical Arts | 1.0 | |
| Physical Education | 1.0 | |
| Health | 0.5 | |
| Personal Finance | 0.5 | RSMo 170.013 |
| Electives | 7.0 | |
| **TOTAL** | **24.0** | Districts may require more |

**Additional requirements:** CPR instruction (RSMo 170.310), U.S./MO Constitution instruction (RSMo 170.011), MAP/EOC participation (required; passing not a graduation gate)

---

## Table 2: EOC Exam Subjects

| Subject | Course Tied To | Participation |
|---------|---------------|--------------|
| English II | English II | Required |
| Algebra I | Algebra I (or Algebra II) | Required |
| Biology | Biology | Required |
| American Government | American Government | Required |

Scores are incorporated into course grades per local board policy. Participation is mandatory; passing the EOC is not a graduation requirement.

---

## Table 3: A+ Schools Program Requirements

| Requirement | Threshold | Statute |
|-------------|-----------|---------|
| School attendance | Designated A+ school for 3 consecutive years prior to graduation | RSMo 160.545 |
| GPA | ≥ 2.5 cumulative unweighted | RSMo 160.545 |
| Attendance | ≥ 95% cumulative grades 9-12 | RSMo 160.545 |
| Tutoring/mentoring | ≥ 50 hours unpaid | RSMo 160.545 |
| Citizenship | No unlawful drug use; no felony or qualifying misdemeanor conviction | RSMo 160.545 |
| Financial aid | FAFSA completed (or waiver) | RSMo 160.545 |
| Math proficiency | Proficient or Advanced on Algebra I EOC (or approved alternative) | RSMo 160.545 |

**Benefit:** Tuition reimbursement (last-dollar) at MO public community colleges and vo-tech schools. Up to 48 months after graduation. Must maintain 2.5 GPA and full-time enrollment at the college level.

---

## Table 4: Missouri Immunization Requirements (School Entry)

| Vaccine | Required Doses | Entry Level |
|---------|---------------|-------------|
| DTaP | 4-5 doses | K entry |
| IPV (Polio) | 3-4 doses | K entry |
| MMR | 2 doses | K entry |
| Hepatitis B | 3 doses | K entry |
| Varicella | 2 doses | K entry |
| Tdap booster | 1 dose | 8th grade entry (age-appropriate) |

**Exemptions:** Medical (physician statement) or Religious (parent statement). Missouri does NOT have a personal/philosophical exemption.

---

## Table 5: Assessment Calendar (Typical)

| Assessment | Grades | Typical Window | Purpose |
|-----------|--------|---------------|---------|
| Kindergarten Readiness | K entry | August-September (first weeks) | Instructional planning |
| MAP ELA | 3, 4, 5, 6, 7, 8 | March-May | State accountability |
| MAP Math | 3, 4, 5, 6, 7, 8 | March-May | State accountability |
| MAP Science | 5, 8 | March-May | State accountability |
| EOC exams | Upon course completion | Fall, Spring, Summer | State accountability |
| WIDA ACCESS | K-12 (ELLs) | January-March | ELL proficiency |
| ACT (statewide) | 11 | Spring (designated date) | College readiness |
| MAP-A | Eligible students | Aligned with MAP window | Alternate assessment |

---

## Table 6: Key Missouri Education Statutes (Quick Lookup)

| Statute | Topic | Key Provision |
|---------|-------|--------------|
| RSMo 160.053 | Kindergarten age | Turn 5 by August 1 |
| RSMo 160.261 | Discipline policy | Board must adopt; mandatory reporting for weapons/drugs/assault |
| RSMo 160.400-425 | Charter schools | Authorization, governance, funding |
| RSMo 160.526 | School improvement | CSIP requirement for every school |
| RSMo 160.545 | A+ Schools | Eligibility, benefits, designation |
| RSMo 160.660 | Safety plans | Building-level crisis plans, drills |
| RSMo 160.775 | Anti-bullying | Policy requirement |
| RSMo 161.096 | Student data privacy | No commercial use of student data |
| RSMo 162.081 | Lapse of organization | State authority over failing districts |
| RSMo 162.215 | Conflict of interest | Board member disclosure |
| RSMo 167.031 | Compulsory attendance | Ages 7-17; homeschool exemption |
| RSMo 167.131 | Unaccredited transfers | Student transfer rights |
| RSMo 167.161 | Short-term suspension | ≤10 days; due process |
| RSMo 167.171 | Long-term suspension | >10 days; hearing required |
| RSMo 167.181 | Immunizations | Required for enrollment; exemptions |
| RSMo 167.621 | Diabetes in schools | Self-management + school support |
| RSMo 167.627 | Self-carry medications | Inhalers, EpiPens |
| RSMo 167.765 | Concussion protocol | Return-to-play requirements |
| RSMo 167.950 | Dyslexia screening | Screening and intervention |
| RSMo 168.028 | Mentoring program | Required for new teachers |
| RSMo 168.104 | Probation/tenure | 5-year probationary period |
| RSMo 168.114 | Tenure termination | For cause; due process |
| RSMo 168.126 | Non-renewal notice | April 15 deadline |
| RSMo 168.133 | Background checks | All employees + volunteers |
| RSMo 168.345 | NBCT supplement | Up to $2,000/year |
| RSMo 170.013 | Personal finance | Required for graduation |
| RSMo 170.015 | Sex ed opt-out | Parent right to opt out |
| RSMo 170.048 | Suicide prevention | Staff training required |
| RSMo 170.310 | CPR instruction | Required before graduation |
| RSMo 210.115 | Mandated reporting | ALL persons; report immediately |
| RSMo 210.135 | Reporter immunity | Good-faith reporters immune |
| RSMo 210.165 | Failure to report | Class A misdemeanor |
| RSMo 290.210 | Prevailing wage | Public construction >$75,000 |
| RSMo 610.020 | Open meetings | 24-hour notice required |
| RSMo 610.021 | Closed sessions | Specific enumerated reasons only |
| SB 68 (2025) | Device ban | Electronic communication devices in schools |

---

## Table 7: MEES Scoring Rubric

| Score | Level |
|-------|-------|
| 0-2 | Emerging |
| 3-4 | Developing |
| 5-6 | Proficient |
| 7 | Distinguished |

8 Standards, 36 Quality Indicators. See `references/teachers.md` §2 for full standard/indicator list.

---

## Table 8: IDEA Disability Categories (Missouri)

| # | Category |
|---|---------|
| 1 | Autism Spectrum Disorder |
| 2 | Deaf-Blindness |
| 3 | Deafness |
| 4 | Emotional Disturbance |
| 5 | Hearing Impairment |
| 6 | Intellectual Disability |
| 7 | Multiple Disabilities |
| 8 | Orthopedic Impairment |
| 9 | Other Health Impairment |
| 10 | Specific Learning Disability |
| 11 | Speech or Language Impairment |
| 12 | Traumatic Brain Injury |
| 13 | Visual Impairment (including blindness) |
| + | Young Child with Developmental Delay (ages 3-5 only) |

---

## Table 9: ACT College Readiness Benchmarks

| Subject | Benchmark Score |
|---------|----------------|
| English | 18 |
| Mathematics | 22 |
| Reading | 22 |
| Science | 23 |
| Composite (general readiness) | 21 |

---

## Table 10: MSIP 6 Standards

| # | Standard | Focus |
|---|---------|-------|
| 1 | Academic Achievement | Student proficiency on MAP/EOC/ACT |
| 2 | Subgroup Achievement | Performance of historically underperforming subgroups |
| 3 | College & Career Readiness | Graduation rate, post-secondary enrollment, credentials |
| 4 | Attendance | Attendance rate, chronic absenteeism |
| 5 | School Quality / Climate | Climate surveys, teacher retention, advanced coursework, arts/CTE |

---

## Table 11: Required Drill Schedule

| Drill | Minimum Frequency | Basis |
|-------|-------------------|-------|
| Fire | Monthly (min 2/semester) | State Fire Marshal |
| Tornado / severe weather | 2/year | DESE guidance |
| Earthquake | 2/year | DESE guidance (New Madrid zone) |
| Lockdown / active threat | 2/year | RSMo 160.660 |
| Bus evacuation | 1/year | DESE guidance |

---

## Table 12: Missouri State Scholarships

| Scholarship | Basis | Amount | Requirements |
|-------------|-------|--------|-------------|
| A+ Scholarship | Merit + need | Tuition at community colleges | See Table 3 |
| Bright Flight | Merit | Up to $3,000/year | Top ACT/SAT scores; in-state institution |
| Access Missouri | Need | $300-$2,850/year | EFC-based; enrolled at approved MO institution |

---

## Table 13: Key Education Hotlines & Contact Numbers

| Service | Number |
|---------|--------|
| Children's Division (abuse/neglect) | **1-800-392-3738** |
| 988 Suicide & Crisis Lifeline | Call or text **988** |
| Crisis Text Line | Text **HOME** to **741741** |
| DESE Main Line | 573-751-4212 |
| DESE Educator Certification | 573-751-0051 |
| PSRS/PEERS | 573-634-5290 |

---

## Table 14: Key Timelines in Special Education

| Process | Timeline |
|---------|---------|
| Evaluation (from consent) | 60 calendar days |
| IEP development (from eligibility) | 30 calendar days |
| IEP annual review | Every 365 days |
| Triennial reevaluation | Every 3 years |
| Transition planning starts | IEP in effect when student turns 16 |
| Age of majority notification | 1 year before 18th birthday |
| Part C→Part B transition planning | 90 days before child's 3rd birthday |
| MDR trigger | 10+ cumulative removal days in a year |
| State complaint resolution | 60 calendar days |
| Due process hearing decision | 45 days after resolution period |
| "Stay put" during dispute | Current placement maintained |

---

## Table 15: FRPM Income Eligibility (Federal Poverty Level)

| Category | Income Threshold |
|----------|-----------------|
| Free meals | ≤ 130% Federal Poverty Level |
| Reduced-price meals | 131-185% Federal Poverty Level |
| Paid | > 185% Federal Poverty Level |

**Community Eligibility Provision (CEP):** schools with ≥40% Identified Student Percentage may provide free meals to ALL students without individual applications.

---

## Table 16: Teacher Certificate Types

| Certificate | Duration | Key Requirements |
|-------------|----------|-----------------|
| Initial Professional Certificate (IPC) | 4 years | Bachelor's, approved program, assessments, background check |
| Career Continuous Professional Certificate (CCPC) | Lifetime (with renewal) | 4 years on IPC, mentoring, PD, district recommendation |
| Substitute Certificate | 4 years | 60+ college credit hours, background check |
| Temporary Authorization Certificate (TAC) | 1-3 years | District-specific; DESE approval; enrolled in coursework |
| CTE Certificate of License to Teach | Varies | Industry experience + education coursework |

---

## Table 17: PSRS Retirement Eligibility

| Path | Requirements |
|------|-------------|
| Rule of 80 | Age + years of service ≥ 80 (minimum age 48) |
| Age + service | Age 60 with 5+ years |
| Early retirement | Age 55 with 5+ years (reduced benefit) |
| 25-and-out | 25 years regardless of age (reduced if under Rule of 80) |

**Benefit formula:** Years × 2.5% × Final Average Salary (3 highest consecutive years)
**Vesting:** 5 years of creditable service
**Social Security:** most PSRS members do NOT participate in Social Security for school employment
