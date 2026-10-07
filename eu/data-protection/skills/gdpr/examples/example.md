# Example: ROPA entry for a transactional email vendor

**Prompt:**

> We just signed a contract with a US-based transactional email provider. Draft the ROPA entry and tell me what else I need to do under GDPR.

**What Claude should do with the `gdpr` skill loaded:**

1. Generate a controller ROPA entry using `references/ropa-template.md`, populated with realistic defaults (purpose: transactional emails for account/security; lawful basis: Art. 6(1)(b); data: email + name; recipients: the processor; transfer: US under SCCs).
2. Flag the **must-do checklist**:
   - Signed Article 28 DPA with the processor
   - 2021/914 Standard Contractual Clauses (Module 2 — controller→processor) executed
   - Transfer Impact Assessment (post-Schrems II)
   - Update the public privacy notice to mention the recipient category
   - Add to the vendor risk register; assess annually
3. Note when a DPIA *isn't* required here (transactional, contract-basis, low risk) and what would change that (e.g., adding marketing scope or behavioural tracking).
4. Flag legitimate-interest assessment territory if the customer ever wants to use the same vendor for marketing.
