---
name: grievance-tracker-shashionline
title: Grievance Tracker
description: Track public grievance status on CPGRAMS/state portals, analyze delays, and recommend escalation steps based on timeline and response status
author: shashionline
author_url: https://github.com/shashionline/indian-law-plugin/tree/master/skills/grievance-tracker
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: in
practice: administrative
language: en
---

# Grievance Tracker

## Purpose
Track public grievance status on CPGRAMS or state grievance portals, analyze delays against statutory timelines, assess response adequacy, and provide strategic escalation recommendations.

## Skill Workflow

### Step 1: Gather Grievance Details

When invoked, extract/request:

**Essential Information**:
1. **Platform**: Where was grievance filed?
   - CPGRAMS (pgportal.gov.in) - for Central Government
   - State portal (e.g., Maha Jansampark, esamadhan.delhi.gov.in, etc.)

2. **Grievance Number**: Unique registration number (assigned when grievance filed)

3. **Filed Date**: When was grievance submitted?

4. **Issue**: What was the grievance about?
   - Service delay (passport, pension, certificate, etc.)
   - Deficiency (water supply, garbage collection, etc.)
   - Corruption/bribery

5. **Current Status** (if user knows):
   - Pending
   - Under Process
   - Resolved
   - Closed
   - Transferred
   - No update

6. **Days Elapsed**: Calculate from filed date to current date

### Step 2: Timeline Analysis

**Statutory Timeline for Grievance Response**:

**CPGRAMS** (Central Government):
- **60 days** from filing

**State Portals** (varies by state, but generally):
- **30-60 days** (check state-specific rules)
- Examples:
  - Maharashtra (Maha Jansampark): 60 days
  - Delhi (esamadhan): 30 days
  - Karnataka (Sakala): As per service-specific timeline (7-30 days)

**Calculate Status**:
```python
days_elapsed = current_date - filed_date

if days_elapsed < 30:
    status = "Within timeline (30 days pending)"
elif 30 <= days_elapsed < 60:
    status = "Approaching deadline (60 days)"
elif days_elapsed >= 60:
    status = "TIMELINE VIOLATED (60 days exceeded)"
```

**Analysis Output**:
```
**Timeline Status**:
- **Filed Date**: [Date]
- **Current Date**: [Date]
- **Days Elapsed**: [X days]
- **Statutory Deadline**: 60 days (CPGRAMS) / [State-specific days]
- **Status**: [Within timeline / Approaching deadline / TIMELINE VIOLATED]

[If violated:]
**DELAY**: [X days beyond 60-day deadline]
```

### Step 3: Response Status Assessment

**Analyze Current Status**:

**A. "Pending" / "Under Process"**:
- Grievance received, but not yet acted upon
- Department hasn't responded

**Assessment**:
- If < 30 days: Normal processing time
- If 30-60 days: Follow up needed (call/email department)
- If > 60 days: **ESCALATION REQUIRED**

**B. "Resolved" / "Closed"**:
- Department claims issue resolved

**Assessment Questions**:
1. **Is issue actually resolved?**
   - If YES → Genuine resolution
   - If NO → **FALSE "RESOLVED" STATUS** (common tactic to close grievances without action)

2. **Was resolution satisfactory?**
   - If YES → Case closed successfully
   - If NO → Partial/inadequate resolution

**C. "Transferred"**:
- Grievance transferred to another department (Section 6(3) equivalent in grievance system)

**Assessment**:
- Were you informed of transfer?
- To which department?
- Has transferred department acted?

**D. "Rejected" / "Not Admissible"**:
- Department claims grievance not within their purview

**Assessment**:
- Is rejection valid?
- Was proper reason given?

**Analysis Output**:
```
**Current Status on Portal**: [Pending / Under Process / Resolved / Closed / Transferred / Rejected]

**Status Assessment**:
[If Pending/Under Process:]
- Department has not responded yet
- [If < 60 days: Normal processing / If > 60 days: DELAY - Escalation needed]

[If Resolved/Closed:]
- **Is issue actually resolved?**: [User to confirm]
- [If NO: Department falsely marked resolved - Reopen grievance OR escalate]

[If Transferred:]
- **Transferred to**: [Department name, if known]
- **Were you informed?**: [Yes / No - if not informed, file RTI]

[If Rejected:]
- **Rejection Reason**: [Stated reason]
- **Is rejection valid?**: [Analyze based on issue - if invalid, escalate]
```

### Step 4: Escalation Recommendation

Based on timeline + status, recommend next steps:

---

#### Scenario 1: Days Elapsed < 30, Status "Pending"

**Recommendation**: **Wait & Monitor**

```
**Status**: Grievance within normal processing time.

**Action**:
- **Week 2-3**: Check portal status (login and view)
- **Week 4**: If no update, send reminder to Grievance Officer

**Reminder Email Format**:
To: [Grievance Officer email - check department website]
Subject: Follow-up on CPGRAMS Grievance No. [Number]

Dear Sir/Madam,

I filed grievance no. [Number] on [Date] regarding [brief issue description].

It has been [X days]. Kindly provide status update and expected timeline for resolution.

Thanking you,
[Name]
Grievance No.: [Number]

**Next Review**: Day 30 (if no response by then, escalate)
```

---

#### Scenario 2: Days Elapsed 30-60, Status "Pending"

**Recommendation**: **Active Follow-Up**

```
**Status**: Approaching 60-day deadline. Department should have acted by now.

**Immediate Actions**:

**1. Check Portal Status Daily**: Login to CPGRAMS/state portal, check for updates

**2. Email Grievance Officer**:
[Same format as above]

**3. Call Department Helpline**:
- CPGRAMS Helpline: [Service-specific helpline]
- State Portal Helpline: [State-specific number]
- Quote grievance number, ask for status

**4. Prepare for Escalation** (if no response by Day 60):
- File RTI to department
- Prepare second grievance to senior officer

**Timeline**: Day 60 is deadline. If no response, escalate immediately.
```

---

#### Scenario 3: Days Elapsed > 60, Status "Pending" / "No Update"

**Recommendation**: **ESCALATE IMMEDIATELY**

```
**Status**: TIMELINE VIOLATED. Department has failed to respond within 60 days.

**ESCALATION PATH**:

**Step 1: Reopen/Escalate Grievance on Same Portal**

Option A: **Reopen Grievance** (if portal allows):
- Login to CPGRAMS/State portal
- Find your grievance
- Click "Reopen" or "Escalate"
- Add remark: "No response received in 60 days. Request immediate action. Delay violates statutory timeline."

Option B: **File Fresh Grievance to Senior Officer**:
File new grievance addressed to **Secretary of Ministry / Department Head**:

Subject: Non-response to Grievance No. [Number] - Urgent Escalation

Description:
"I filed grievance no. [Number] on [Date] regarding [issue].

Despite 60-day deadline (as per CPGRAMS/State portal norms), no response has been received as of [current date] ([X days] delay).

This delay violates my right to timely service delivery under Citizens Charter of [Department].

Request immediate intervention and resolution.

Previous Grievance No.: [Number]"

**Step 2: File RTI**

To: Public Information Officer, [Department]

"Provide following information:

1. Status of CPGRAMS grievance no. [Number] filed on [Date]
2. Name and designation of officer responsible for responding to this grievance
3. Reasons for non-response within 60-day deadline
4. Timeline for resolution of grievance
5. Action taken against concerned officer for delay (if any)"

Fee: ₹10
Timeline: PIO must respond in 30 days

**Step 3: Parallel Complaint** (if serious issue):

- If corruption involved: File complaint to Central Vigilance Commission (cvc.gov.in) / State Lokayukta
- If service delay affecting life/liberty: Consider writ petition (Mandamus) to High Court

**Timeline**:
- RTI: 30 days for response
- Escalated Grievance: 60 days
- Writ Petition: 6 months - 2 years

**Recommended Immediate Action**: File RTI + Escalated Grievance simultaneously (multi-channel pressure)
```

---

#### Scenario 4: Status "Resolved" But Issue NOT Actually Resolved

**Recommendation**: **REOPEN GRIEVANCE**

```
**Status**: Department marked grievance "Resolved" but issue not actually resolved. This is a common tactic to close files without action.

**IMMEDIATE ACTION: Reopen Grievance**

**Method**:
1. **Login to CPGRAMS / State Portal**
2. **Find your grievance** (may be in "Closed" or "Resolved" section)
3. **Click "Reopen" button** (if available)
4. **Add detailed remark**:

"Grievance was marked 'Resolved' on [date] by department. However, the issue is NOT resolved.

Current status: [Describe - service still not delivered / problem persists / no action taken]

Request re-examination and genuine resolution.

Previous Grievance No.: [Number]"

5. **Submit Reopen Request**

**If Reopen Option Not Available**:
File **fresh grievance** with description:

"This is a follow-up to grievance no. [Number] which was incorrectly marked 'Resolved' on [date] without actual resolution.

Issue: [Describe current status - service not delivered / problem continues]

Request immediate action. Previous grievance no.: [Number]"

**Parallel Action: File RTI**

"Provide:
1. Copy of resolution/action taken report for CPGRAMS grievance no. [Number]
2. Details of action taken by department to resolve grievance
3. Name of officer who marked grievance 'Resolved'
4. Basis for marking grievance resolved when issue persists"

**If Multiple Reopen Attempts Fail**:
Consider **writ petition (Mandamus)** to High Court compelling department to perform duty.
```

---

#### Scenario 5: Status "Transferred"

**Recommendation**: **Track Transfer**

```
**Status**: Grievance transferred to another department.

**VERIFY TRANSFER**:

**1. Check if You Were Informed**:
- Did you receive email/SMS about transfer?
- Was transfer notification shown on portal?

**If NOT Informed**: File RTI to original department:
"Provide:
1. Details of transfer of my grievance no. [Number] - to which department transferred, on what date
2. Copy of transfer order/intimation
3. Contact details of transferred department's Grievance Officer"

**2. Track Status in Transferred Department**:

**If Transfer Details Available**:
- Login to portal
- Check if new grievance number assigned
- Track status with new department

**If New Department Also Delays**:
- Follow same escalation path (60-day rule applies from date of transfer)

**3. If Transfer Was Improper** (i.e., your grievance WAS within original department's scope):

File fresh grievance to original department:
"My grievance no. [Number] was incorrectly transferred to [Department] on [Date].

The issue pertains to [original department's] responsibility as per [Citizens Charter / Statutory provision].

Request original department to take action instead of transferring."
```

---

#### Scenario 6: Status "Rejected" / "Not Admissible"

**Recommendation**: **Challenge Rejection**

```
**Status**: Department rejected grievance claiming it's not within their purview or not admissible.

**ANALYZE REJECTION**:

**1. Is Rejection Valid?**

Check:
- Does your issue fall within department's functions (as per Citizens Charter / Government allocation of business rules)?
- Did department provide proper reasons for rejection?

**If Rejection Invalid** (i.e., issue IS within their scope):

**Action: File Fresh Grievance Challenging Rejection**

"My grievance no. [Number] was rejected on [Date] on grounds that [stated reason].

However, this rejection is incorrect because:
1. The issue pertains to [service/function] which falls under your department's mandate as per [Citizens Charter / Allocation of Business Rules]
2. [Cite specific provision showing department's responsibility]

Request reconsideration and action on original grievance.

Previous Grievance No.: [Number]"

**2. If Rejection Arbitrary** (no proper reason given):

File RTI:
"Provide:
1. Reasons for rejection of grievance no. [Number]
2. Rules/provisions under which grievance was held inadmissible
3. Proper forum for filing this grievance (if not your department)"

**3. If Department Genuinely Not Responsible**:

Refile grievance to **correct department** (as suggested by rejecting department, if mentioned).
```

---

### Step 5: Additional Strategic Recommendations

**Multi-Channel Escalation**:

When grievance delayed/unresolved, use **multiple channels simultaneously**:

1. **Escalated Grievance** (on portal)
2. **RTI** (to get information + create accountability)
3. **Email to Grievance Officer** (direct communication)
4. **Call Helpline** (immediate escalation)
5. **Social Media** (Twitter - tag department handle with grievance number - often gets quick response due to public visibility)

**Example Tweet**:
"@[DepartmentHandle] Grievance no. [Number] filed on [Date] not resolved despite 60+ days. Request immediate action. #CPGRAMS #PublicGrievance"

**Persistence Pays**:
- Check status **weekly**
- Send reminder **every 10-15 days** if no update
- Escalate at **60-day mark** without fail

**Document Everything**:
- Screenshots of portal status
- Emails sent/received
- Call logs (date, time, person spoken to, response)
- RTI applications and responses

---

### Step 6: Consolidated Output

Provide user with comprehensive tracking analysis:

```markdown
# Grievance Status Tracking & Escalation Guidance

## Grievance Details

**Platform**: [CPGRAMS / State Portal Name]
**Grievance Number**: [Number]
**Filed Date**: [Date]
**Issue**: [Brief description]
**Days Elapsed**: [X days]

---

## Timeline Analysis

**Statutory Deadline**: 60 days (CPGRAMS) / [State-specific days]

**Current Status**:
- Days Elapsed: **[X days]**
- Deadline Status: [Within timeline / Approaching deadline (Day 30-60) / **TIMELINE VIOLATED** (>60 days)]

[If violated:]
**DELAY**: [X days] beyond statutory deadline

---

## Portal Status Assessment

**Current Status on Portal**: [Pending / Under Process / Resolved / Closed / Transferred / Rejected]

**Assessment**:
[Detailed assessment based on status - see scenarios above]

---

## Recommended Next Steps

**Immediate Action** ([Based on scenario]):

[Provide specific action steps from scenarios 1-6 above]

---

## Escalation Timeline

**Week 2-3**: [Monitor status / Send reminder]
**Day 30**: [Active follow-up if no update]
**Day 60**: [ESCALATE - RTI + Fresh grievance to senior officer]
**Day 90**: [If still unresolved, consider writ petition]

---

## Multi-Channel Escalation Checklist

- [ ] Portal: Reopen/Escalate grievance
- [ ] RTI: File to get status + accountability
- [ ] Email: Grievance Officer email
- [ ] Helpline: Call department helpline
- [ ] Social Media: Tweet tagging department (if public issue)

---

## Documentation to Maintain

- [ ] Screenshot of current portal status
- [ ] Emails/correspondence
- [ ] RTI application + responses
- [ ] Call logs (date, time, person, response)

---

**Persistence is key. Grievance systems work best when citizens actively track and escalate. Don't let your grievance be forgotten in bureaucratic delays.**

For detailed grievance procedures, consult:
- **CIVIC-PUBLIC-GRIEVANCE**: CPGRAMS, escalation paths, Citizens Charter
```

---

## Integration with Agents

This skill is invoked by:
- **public-service-specialist** when user asks about grievance tracking
- **india-civic-law-specialist** for grievance status queries

Skill provides actionable status analysis and escalation roadmap based on elapsed time and current status.

---

## Special Features

**Proactive Alerts** (if implementing automation):
- Alert user when grievance approaches Day 30 (reminder to follow up)
- Alert at Day 60 (escalation deadline)
- Alert if status changes to "Resolved" (verify actual resolution)

**Status Change Recommendations**:
- If status changes from "Pending" to "Resolved": Prompt user to verify if issue actually resolved
- If status "Transferred": Provide guidance on tracking in new department

---

**Public grievance redressal is a citizen right. This skill ensures grievances don't get lost in bureaucratic delays through proactive tracking and strategic escalation.**
