# Open Source License Decision Tree

## Interactive Selection Guide

Use this decision tree to help users choose the right license. Ask questions in order and follow the branches.

---

## Primary Decision Flow

### Question 1: What is your primary goal?

**A) Maximum adoption and ease of use**
→ Go to [Permissive Path](#permissive-path)

**B) Keep improvements open source**
→ Go to [Copyleft Path](#copyleft-path)

**C) Dual licensing / commercial strategy**
→ Go to [Commercial Path](#commercial-path)

**D) Not sure / want guidance**
→ Go to [Guided Questions](#guided-questions)

---

## Permissive Path

### Q: Do you need explicit patent protection?

**Yes** → **Apache-2.0**
- Explicit patent grant protects users
- Patent retaliation clause deters litigation
- Examples: Kubernetes, TensorFlow, Spark

**No, simplicity is more important** → Continue

### Q: Is this a library that might be embedded in other software?

**Yes, and I want minimal friction** → **MIT**
- Shortest, simplest, most understood
- Examples: React, Node.js, jQuery

**Yes, but I want non-endorsement protection** → **BSD-3-Clause**
- Prevents others from using your name for promotion
- Examples: Django, Flask, numpy

**No, it's a standalone project** → **MIT** or **Apache-2.0**
- MIT for simplicity
- Apache-2.0 for patent protection

---

## Copyleft Path

### Q: What scope of copyleft do you want?

**A) File-level only (modified files must be open, rest can be proprietary)**
→ **MPL-2.0**
- Good balance for libraries
- Examples: Firefox, Thunderbird

**B) Library-level (library changes must be open, applications can be proprietary)**
→ **LGPL-3.0**
- Encourages use while protecting library
- Examples: GTK, glibc, Qt

**C) Full program (entire derivative work must be open)**
→ Continue to next question

**D) Full program including network/SaaS use**
→ **AGPL-3.0**
- Strongest copyleft, covers SaaS
- Examples: Nextcloud, Mastodon, Grafana

### Q: Do you need explicit patent protection?

**Yes** → **GPL-3.0**
- Modern GPL with patent grant
- Examples: WordPress, GIMP, Bash

**No, or need compatibility with Linux kernel** → **GPL-2.0**
- Classic GPL, widely used
- Examples: Linux kernel, Git, BusyBox

---

## Commercial Path

### Q: What's your commercial strategy?

**A) Open core (free base + paid features)**
→ Consider **AGPL-3.0** for core
- Forces competitors to open source their modifications
- You can offer commercial license for proprietary extensions

**B) Dual licensing (free for OSS, paid for commercial)**
→ Consider **GPL-3.0** or **AGPL-3.0**
- Copyleft encourages purchasing commercial license
- You retain copyright to offer alternative terms

**C) Maximize adoption, monetize services**
→ Consider **Apache-2.0** or **MIT**
- Maximum adoption = more potential customers
- Monetize through support, hosting, enterprise features

---

## Guided Questions

Answer these questions to narrow down your choice:

### 1. Will companies need to use this in proprietary software?

| Answer | Implication |
|--------|-------------|
| Yes, definitely | Avoid GPL/AGPL → Consider MIT, Apache-2.0, BSD |
| Yes, but linking only | LGPL-3.0 may work |
| No, must stay open | GPL-3.0 or AGPL-3.0 |
| Don't care | Any license works |

### 2. Are there patents involved in this software?

| Answer | Implication |
|--------|-------------|
| Yes, I want to grant patent rights | Apache-2.0, GPL-3.0, MPL-2.0 |
| Yes, I want protection from patent claims | Apache-2.0, GPL-3.0 (retaliation clause) |
| No patents | MIT, BSD work fine |
| Not sure | Apache-2.0 is safe default |

### 3. Will this be used as a network service (SaaS)?

| Answer | Implication |
|--------|-------------|
| Yes, and I want users to contribute back | AGPL-3.0 |
| Yes, but I don't care about contributions | Any license |
| No, it's client-side only | GPL-3.0 or permissive |

### 4. Do you want credit/attribution?

| Answer | Implication |
|--------|-------------|
| Yes, always | MIT, Apache, BSD, GPL all require it |
| Only in source, not binaries | Boost (BSL-1.0) |
| No attribution needed | Unlicense, CC0 |

### 5. Is this a library or framework?

| Answer | Implication |
|--------|-------------|
| Yes, meant to be embedded | MIT, Apache-2.0, LGPL-3.0, MPL-2.0 |
| Yes, but must stay open | LGPL-3.0 |
| No, standalone application | Any license appropriate |

---

## Quick Recommendation Summary

| Scenario | Recommended License |
|----------|-------------------|
| Simple library, max adoption | MIT |
| Library with patent concerns | Apache-2.0 |
| Library, want changes shared | LGPL-3.0 or MPL-2.0 |
| Application, want changes shared | GPL-3.0 |
| SaaS/server, want changes shared | AGPL-3.0 |
| Corporate-friendly with patents | Apache-2.0 |
| Public domain equivalent | Unlicense or CC0 |
| Documentation/content | CC-BY-4.0 |

---

## Red Flags to Avoid

### Don't Use These for Software
- **CC-BY-NC** - Not open source (restricts commercial use)
- **CC licenses generally** - Designed for content, not code
- **No license** - All rights reserved by default!

### Be Careful With
- **Custom/modified licenses** - Compatibility issues, legal uncertainty
- **License proliferation** - Stick to well-known licenses
- **Mixing incompatible licenses** - See compatibility matrix

---

## Final Checklist

Before finalizing your license choice:

- [ ] Does this license match your project goals?
- [ ] Is it compatible with your dependencies' licenses?
- [ ] Will your target users/companies accept this license?
- [ ] Have you considered patent implications?
- [ ] Is the license OSI-approved? (if open source is important)
- [ ] Have you consulted legal counsel for commercial projects?
