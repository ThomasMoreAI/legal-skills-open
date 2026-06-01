---
name: canned-responses-escalation-triggers-all-categories
title: Universal Escalation Triggers (Apply to All Categories) (+2)
description: 'Sub-skill of canned-responses: Universal Escalation Triggers (Apply to All Categories) (+2).'
author: vamseeachanta
author_url: https://github.com/vamseeachanta/workspace-hub/tree/main/.claude/skills/_archive/business/legal/canned-responses/universal-escalation-triggers-apply-to-all-categor
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: data-protection
language: en
---

# Universal Escalation Triggers (Apply to All Categories) (+2)

## Universal Escalation Triggers (Apply to All Categories)

- The matter involves potential litigation or regulatory investigation
- The inquiry is from a regulator, government agency, or law enforcement
- The response could create a binding legal commitment or waiver
- The matter involves potential criminal liability
- Media attention is involved or likely
- The situation is unprecedented (no prior handling by the team)
- Multiple jurisdictions are involved with conflicting requirements
- The matter involves executive leadership or board members


## Category-Specific Escalation Triggers


**Data Subject Requests**:
- Request from a minor or on behalf of a minor
- Request involves data subject to litigation hold
- Requester is in active litigation or dispute with the organization
- Request is from an employee with an active HR matter
- Request scope is so broad it appears to be a fishing expedition
- Request involves special category data (health, biometric, genetic)

**Discovery Holds**:
- Potential criminal liability
- Unclear or disputed preservation scope
- Hold conflicts with regulatory deletion requirements
- Prior holds exist for related matters
- Custodian objects to the hold scope

**Vendor Questions**:
- Vendor is disputing contract terms
- Vendor is threatening litigation or termination
- Response could affect ongoing negotiation
- Question involves regulatory compliance (not just contract interpretation)

**Subpoena / Legal Process**:
- ALWAYS requires counsel review (templates are starting points only)
- Privilege issues identified
- Third-party data involved
- Cross-border production issues
- Unreasonable timeline


## When an Escalation Trigger is Detected


1. **Stop**: Do not generate a templated response
2. **Alert**: Inform the user that an escalation trigger has been detected
3. **Explain**: Describe which trigger was detected and why it matters
4. **Recommend**: Suggest the appropriate escalation path (senior counsel, outside counsel, specific team member)
5. **Offer**: Provide a draft for counsel review (clearly marked as "DRAFT - FOR COUNSEL REVIEW ONLY") rather than a final response
