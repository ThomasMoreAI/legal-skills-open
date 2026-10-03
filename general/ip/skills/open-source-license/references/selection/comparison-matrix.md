# Open Source License Comparison Matrix

## Quick Reference Table

| License | Type | Copyleft | Patent Grant | Attribution | Commercial | Notable Projects |
|---------|------|----------|--------------|-------------|------------|------------------|
| MIT | Permissive | No | No | Yes | Yes | React, Node.js, Rails, jQuery |
| Apache-2.0 | Permissive | No | Yes | Yes | Yes | Kubernetes, TensorFlow, Android |
| BSD-2-Clause | Permissive | No | No | Yes | Yes | FreeBSD, nginx |
| BSD-3-Clause | Permissive | No | No | Yes | Yes | Django, Flask, Go |
| ISC | Permissive | No | No | Yes | Yes | npm, OpenBSD |
| Unlicense | Public Domain | No | No | No | Yes | youtube-dl |
| GPL-3.0 | Strong Copyleft | Yes | Yes | Yes | Yes* | WordPress, GIMP, Bash |
| GPL-2.0 | Strong Copyleft | Yes | No | Yes | Yes* | Linux kernel, Git |
| LGPL-3.0 | Weak Copyleft | File-level | Yes | Yes | Yes | GTK, glibc |
| AGPL-3.0 | Network Copyleft | Yes | Yes | Yes | Yes* | Nextcloud, Mastodon |
| MPL-2.0 | Weak Copyleft | File-level | Yes | Yes | Yes | Firefox, Terraform (old) |
| EPL-2.0 | Weak Copyleft | Module-level | Yes | Yes | Yes | Eclipse IDE, JUnit 5 |

*Commercial use allowed but copyleft obligations apply

---

## Detailed Feature Comparison

### Permissions

| License | Commercial Use | Distribution | Modification | Private Use | Patent Use |
|---------|---------------|--------------|--------------|-------------|------------|
| MIT | ✅ | ✅ | ✅ | ✅ | ❌ (implicit) |
| Apache-2.0 | ✅ | ✅ | ✅ | ✅ | ✅ |
| BSD-3-Clause | ✅ | ✅ | ✅ | ✅ | ❌ (implicit) |
| GPL-3.0 | ✅ | ✅ | ✅ | ✅ | ✅ |
| GPL-2.0 | ✅ | ✅ | ✅ | ✅ | ❌ |
| LGPL-3.0 | ✅ | ✅ | ✅ | ✅ | ✅ |
| AGPL-3.0 | ✅ | ✅ | ✅ | ✅ | ✅ |
| MPL-2.0 | ✅ | ✅ | ✅ | ✅ | ✅ |

### Conditions (Requirements)

| License | License Copy | Copyright Notice | State Changes | Disclose Source | Same License |
|---------|-------------|------------------|---------------|-----------------|--------------|
| MIT | ✅ | ✅ | ❌ | ❌ | ❌ |
| Apache-2.0 | ✅ | ✅ | ✅ | ❌ | ❌ |
| BSD-3-Clause | ✅ | ✅ | ❌ | ❌ | ❌ |
| GPL-3.0 | ✅ | ✅ | ✅ | ✅ | ✅ |
| GPL-2.0 | ✅ | ✅ | ✅ | ✅ | ✅ |
| LGPL-3.0 | ✅ | ✅ | ✅ | ✅ (for library) | ✅ (for library) |
| AGPL-3.0 | ✅ | ✅ | ✅ | ✅ (including SaaS) | ✅ |
| MPL-2.0 | ✅ | ✅ | ✅ | ✅ (per file) | ✅ (per file) |

### Limitations

| License | Liability | Warranty | Trademark | Patent Claims |
|---------|-----------|----------|-----------|---------------|
| MIT | ✅ Limited | ✅ None | ❌ | ❌ |
| Apache-2.0 | ✅ Limited | ✅ None | ✅ No grant | ✅ Retaliation |
| BSD-3-Clause | ✅ Limited | ✅ None | ✅ No endorsement | ❌ |
| GPL-3.0 | ✅ Limited | ✅ None | ❌ | ✅ Retaliation |
| LGPL-3.0 | ✅ Limited | ✅ None | ❌ | ✅ Retaliation |
| AGPL-3.0 | ✅ Limited | ✅ None | ❌ | ✅ Retaliation |
| MPL-2.0 | ✅ Limited | ✅ None | ✅ No grant | ✅ Retaliation |

---

## Copyleft Strength Comparison

```
Most Permissive ←————————————————————————————→ Most Restrictive

Unlicense  MIT  BSD  Apache  MPL  LGPL  EPL  GPL  AGPL
    │       │    │     │      │    │     │    │     │
    └───────┴────┴─────┴──────┴────┴─────┴────┴─────┘
         Public          Weak Copyleft    Strong    Network
         Domain/         (file/module)    Copyleft  Copyleft
         Permissive
```

### Copyleft Scope Explained

| Type | Scope | Derivative Works | Linking |
|------|-------|------------------|---------|
| None (Permissive) | N/A | Can be proprietary | No restrictions |
| File-level (MPL) | Modified files only | New files can be proprietary | No restrictions |
| Library-level (LGPL) | Library code only | Applications can be proprietary | Dynamic linking OK |
| Strong (GPL) | Entire program | Must be GPL | Static/dynamic triggers copyleft |
| Network (AGPL) | Entire program + SaaS | Must be AGPL | Network use triggers copyleft |

---

## Use Case Recommendations

### For Maximum Adoption

**Recommended:** MIT, Apache-2.0, BSD-3-Clause

Best for:
- Libraries intended for wide use
- Projects seeking corporate adoption
- Startups wanting to maximize user base

### For Patent Protection

**Recommended:** Apache-2.0, GPL-3.0, MPL-2.0

Best for:
- Projects with patentable innovations
- Enterprise software
- Projects concerned about patent trolls

### For Keeping Code Open

**Recommended:** GPL-3.0, AGPL-3.0

Best for:
- Projects wanting contributions back
- Community-driven development
- Preventing proprietary forks

### For SaaS/Cloud Protection

**Recommended:** AGPL-3.0

Best for:
- Server-side applications
- APIs and web services
- Preventing cloud providers from using without contributing

### For Libraries

**Recommended:** MIT, Apache-2.0, LGPL-3.0, MPL-2.0

Best for:
- Reusable components
- SDKs and frameworks
- Code meant to be embedded

---

## Corporate Acceptance

### Generally Accepted by Most Companies

- MIT
- Apache-2.0
- BSD-2-Clause
- BSD-3-Clause
- ISC
- Unlicense/CC0

### Often Accepted with Review

- LGPL-3.0 (dynamic linking usually OK)
- MPL-2.0 (file-level copyleft manageable)
- EPL-2.0

### Often Restricted/Prohibited

- GPL-2.0/3.0 (except for development tools)
- AGPL-3.0 (almost always prohibited)

### Red Flags (Not True Open Source)

- SSPL
- BSL/BUSL
- Elastic License
- Any "Commons Clause"
