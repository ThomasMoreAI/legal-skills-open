# Common Open Source License Compliance Issues

## Top 10 Compliance Mistakes

### 1. No License = All Rights Reserved

**The Problem:**
Code published without a license file is NOT open source. Copyright law defaults to "all rights reserved" - no one can legally use, modify, or distribute it.

**How It Happens:**
- Developer pushes code to GitHub without LICENSE file
- Assumes "public repo = public domain"
- Forgets to add license after initial commit

**The Fix:**
- ALWAYS include a LICENSE file in the repository root
- Choose a license before first public commit
- Use GitHub's license picker when creating repos

**Detection:**
```bash
# Check for LICENSE file
ls LICENSE* COPYING* 2>/dev/null || echo "WARNING: No license file found"
```

---

### 2. Ignoring Copyleft Obligations

**The Problem:**
Including GPL/AGPL code in proprietary software without providing source code.

**How It Happens:**
- Not scanning dependencies for copyleft licenses
- Misunderstanding "free as in beer" vs "free as in freedom"
- Transitive dependencies pulling in GPL code

**The Fix:**
- Scan all dependencies before inclusion
- Understand copyleft obligations
- Remove or replace GPL dependencies in proprietary projects
- Or release your project under GPL

**Example:**
```
Your App (Proprietary) ❌
├── express (MIT) ✅
├── some-lib (MIT) ✅
│   └── deep-dependency (GPL-3.0) ❌ PROBLEM!
```

---

### 3. Stripping Copyright Notices

**The Problem:**
Removing or failing to preserve copyright notices and license headers.

**How It Happens:**
- Copying code snippets without attribution
- Minification removing comments
- Refactoring without preserving headers

**The Fix:**
- Preserve all copyright notices
- Configure minifiers to keep license comments
- Maintain attribution even when refactoring
- Include third-party notices in distributions

**Correct Approach:**
```javascript
/*!
 * Library Name v1.0.0
 * Copyright (c) 2024 Original Author
 * Licensed under MIT
 */
// Your modifications below...
```

---

### 4. Missing NOTICE File Preservation

**The Problem:**
Apache-2.0 licensed projects often include NOTICE files that MUST be preserved.

**How It Happens:**
- Not knowing about NOTICE requirement
- Bundling without checking for NOTICE files
- Assuming LICENSE file is sufficient

**The Fix:**
- Check all Apache-licensed dependencies for NOTICE files
- Aggregate NOTICE contents in your own NOTICE file
- Include NOTICE in distributions

**Apache-2.0 Section 4(d):**
> "If the Work includes a 'NOTICE' text file... then any Derivative Works that You distribute must include a readable copy of the attribution notices contained within such NOTICE file"

---

### 5. Static Linking with LGPL

**The Problem:**
Statically linking LGPL libraries in proprietary software violates LGPL terms.

**How It Happens:**
- Using static builds for easier deployment
- Not understanding dynamic vs static linking requirements
- Compiling LGPL code directly into binary

**The Fix:**
- Use dynamic linking (shared libraries)
- Provide object files enabling relinking, OR
- Release your code under LGPL/GPL

**LGPL Requires:**
- Users must be able to replace the LGPL library
- Either dynamic link, or provide object files for relinking

---

### 6. Apache-2.0 + GPL-2.0 Conflict

**The Problem:**
Apache-2.0 and GPL-2.0 are incompatible. You cannot combine them in the same work.

**How It Happens:**
- Assuming all OSS licenses are compatible
- Not checking specific compatibility
- Dependencies using different GPL versions

**The Fix:**
- Check compatibility before combining
- Apache-2.0 IS compatible with GPL-3.0
- Use "GPL-2.0-or-later" to enable GPL-3.0 compatibility
- Find alternative dependencies if needed

**Why Incompatible:**
Apache-2.0's patent retaliation and indemnification clauses are "additional restrictions" under GPL-2.0's terms.

---

### 7. AGPL Network Loophole Surprise

**The Problem:**
Using AGPL code in a web service triggers copyleft, even without distribution.

**How It Happens:**
- Thinking "we're not distributing, just hosting"
- Including AGPL dependency in backend
- Not scanning server-side code for AGPL

**The Fix:**
- Scan specifically for AGPL licenses
- Understand network interaction triggers source disclosure
- Remove AGPL dependencies from proprietary services
- Or release your service source code

**AGPL Section 13:**
> "if you modify the Program, your modified version must prominently offer all users interacting with it remotely through a computer network... an opportunity to receive the Corresponding Source"

---

### 8. License File Without Actual Compliance

**The Problem:**
Including a LICENSE file but not actually following its terms.

**How It Happens:**
- Copy-pasting LICENSE without reading it
- Not including required notices
- Not providing source when required

**The Fix:**
- Read and understand your chosen license
- Follow ALL requirements, not just "include LICENSE"
- Use compliance checklist for each license type

---

### 9. Dual-License Confusion

**The Problem:**
Not understanding how to choose or apply dual licenses.

**How It Happens:**
- Mixing "OR" and "AND" license expressions
- Not explicitly stating chosen license
- Applying both licenses when only one is needed

**SPDX Expressions:**
- `MIT OR Apache-2.0` = Choose one (pick whichever suits you)
- `MIT AND Apache-2.0` = Both apply (must comply with both)
- `GPL-2.0-only` = Only GPL 2.0, no "or later"
- `GPL-2.0-or-later` = GPL 2.0 or any later version

**The Fix:**
- Document which license you're using
- Understand the difference between OR/AND
- Check if "or later" clause applies

---

### 10. Assuming Stack Overflow Code is Free

**The Problem:**
Code from Stack Overflow has specific license terms that are often ignored.

**How It Happens:**
- Copy-pasting without attribution
- Not knowing SO uses CC BY-SA
- Treating snippets as "too small to copyright"

**The Reality:**
- Stack Overflow content is CC BY-SA 4.0
- Requires attribution
- ShareAlike means derivatives must use same license
- May be incompatible with your project's license

**The Fix:**
- Attribute Stack Overflow answers
- Consider rewriting rather than copying
- Check compatibility with your license
- For MIT/BSD projects, CC BY-SA may cause issues

---

## Industry-Specific Issues

### Mobile Apps

- **iOS App Store:** GPL may conflict with DRM requirements
- **Google Play:** Must provide source for copyleft components
- **In-app notices:** Many licenses require attribution visible to users

### SaaS/Cloud

- **AGPL triggers:** Any network interaction = source disclosure
- **Modified cloud services:** Changes to AGPL code must be released
- **Containers:** Include licenses in container images

### Embedded Systems

- **GPL + Tivoization:** GPL-3.0 requires installation information
- **Binary-only distribution:** Still must provide source offer
- **Supply chain:** Vendors must pass through compliance obligations

### Enterprise Software

- **Indemnification:** Some licenses disclaim all liability
- **Export controls:** Some licenses have geographic restrictions
- **Government use:** Some licenses have specific government clauses

---

## Compliance Failure Consequences

### Legal Risks

- Copyright infringement lawsuits
- Injunctions preventing distribution
- Statutory damages up to $150,000 per work (US)
- Required source code disclosure

### Business Risks

- Forced product recalls
- Reputation damage
- M&A deal complications
- Customer contract violations

### Notable Cases

- **BusyBox lawsuits:** Multiple companies forced to comply with GPL
- **Cisco/FSF:** Settled, required GPL compliance
- **VMware/Linux:** High-profile GPL dispute
- **Google/Oracle:** API copyright (not license, but related)

---

## Prevention Best Practices

1. **Scan early, scan often** - Integrate license scanning in CI/CD
2. **Approve before adding** - Review licenses before adding dependencies
3. **Document decisions** - Keep records of why licenses were chosen
4. **Train developers** - Ensure team understands license basics
5. **Regular audits** - Periodic comprehensive license reviews
6. **Legal review** - Consult counsel for complex situations
7. **Upstream engagement** - Contribute back to avoid divergence
