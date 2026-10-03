# License Compatibility Matrix

Comprehensive reference for open-source license obligations, compatibility, and typical use cases. All identifiers follow SPDX.

## Permissive Licenses

### MIT
- **SPDX ID:** MIT
- **Category:** Permissive
- **Key Obligations:** Include copyright notice and permission notice in all copies
- **Compatibility:** Compatible with all licenses including proprietary; can relicense under any terms
- **Typical Use:** Libraries, frameworks, developer tools, npm ecosystem default
- **Risk Level:** Low

### Apache-2.0
- **SPDX ID:** Apache-2.0
- **Category:** Permissive (with patent grant)
- **Key Obligations:** Include copyright notice, license text, and NOTICE file; state changes made to files; explicit patent grant
- **Compatibility:** Compatible with GPL-3.0-only (one-way); NOT compatible with GPL-2.0-only due to patent clause
- **Typical Use:** Enterprise projects, Kubernetes, Android, Apache Foundation projects
- **Risk Level:** Low

### BSD-2-Clause
- **SPDX ID:** BSD-2-Clause
- **Category:** Permissive
- **Key Obligations:** Include copyright notice, conditions list, and disclaimer in source and binary forms
- **Compatibility:** Compatible with all licenses including proprietary
- **Typical Use:** Minimal permissive; popular in Go ecosystem, FreeBSD components
- **Risk Level:** Low

### BSD-3-Clause
- **SPDX ID:** BSD-3-Clause
- **Category:** Permissive
- **Key Obligations:** Same as BSD-2-Clause plus prohibition on using contributor names for endorsement without permission
- **Compatibility:** Compatible with all licenses including proprietary
- **Typical Use:** Widely used; React, Go standard library parts, NumPy
- **Risk Level:** Low

### ISC
- **SPDX ID:** ISC
- **Category:** Permissive
- **Key Obligations:** Include copyright notice and permission notice
- **Compatibility:** Functionally equivalent to MIT; compatible with all licenses
- **Typical Use:** OpenBSD, npm packages, Node.js ecosystem
- **Risk Level:** Low

### Artistic-2.0
- **SPDX ID:** Artistic-2.0
- **Category:** Permissive
- **Key Obligations:** Source availability for modifications when distributed; allows relicensing under different terms
- **Compatibility:** Compatible with GPL (via relicensing clause); broadly compatible with permissive licenses
- **Typical Use:** Perl ecosystem, CPAN modules
- **Risk Level:** Low

## Public Domain Dedications

### Unlicense
- **SPDX ID:** Unlicense
- **Category:** Public domain dedication
- **Key Obligations:** No obligations; dedicates work to public domain with fallback permissive license
- **Compatibility:** Compatible with all licenses; may not be recognized in all jurisdictions (e.g., Germany)
- **Typical Use:** Small utilities, example code, reference implementations
- **Risk Level:** Low (jurisdictional caveat)

### CC0-1.0
- **SPDX ID:** CC0-1.0
- **Category:** Public domain dedication
- **Key Obligations:** No obligations; waives all copyright and related rights; no patent grant
- **Compatibility:** Compatible with all licenses; broadly recognized internationally
- **Typical Use:** Data, documentation, reference code, Creative Commons ecosystem
- **Risk Level:** Low (no patent grant)

## Copyleft Licenses

### GPL-2.0-only
- **SPDX ID:** GPL-2.0-only
- **Category:** Strong copyleft
- **Key Obligations:** Derivative works must be licensed under GPL-2.0; source code must be provided with binary distribution
- **Compatibility:** Compatible with GPL-3.0-only (via "or later" clause), LGPL-2.0; INCOMPATIBLE with Apache-2.0, MPL-2.0
- **Typical Use:** Linux kernel, MySQL, older GNU projects
- **Risk Level:** High for proprietary products

### GPL-3.0-only
- **SPDX ID:** GPL-3.0-only
- **Category:** Strong copyleft
- **Key Obligations:** Same as GPL-2.0 with added patent grant, anti-tivoization, and anti-DRM provisions
- **Compatibility:** Compatible with Apache-2.0 (one-way), LGPL-3.0; INCOMPATIBLE with GPL-2.0-only (without "or later")
- **Typical Use:** Modern GNU projects, Bash, GIMP, GCC (with exception)
- **Risk Level:** High for proprietary products

### AGPL-3.0-only
- **SPDX ID:** AGPL-3.0-only
- **Category:** Strong copyleft (network clause)
- **Key Obligations:** Same as GPL-3.0 plus source disclosure when software is accessed over a network (SaaS/cloud trigger)
- **Compatibility:** Compatible with GPL-3.0-only; INCOMPATIBLE with GPL-2.0-only
- **Typical Use:** MongoDB (pre-SSPL), Grafana, MinIO, network-facing services
- **Risk Level:** Critical for SaaS products

### LGPL-3.0-only
- **SPDX ID:** LGPL-3.0-only
- **Category:** Weak copyleft (library)
- **Key Obligations:** Copyleft applies only to the library itself; proprietary applications may dynamically link; modifications to library source must be shared
- **Compatibility:** Compatible with GPL-3.0-only, proprietary (via dynamic linking); static linking may trigger copyleft
- **Typical Use:** GUI toolkits (GTK), audio codecs (FFmpeg), system libraries
- **Risk Level:** Medium (linking mode matters)

## Weak Copyleft Licenses

### MPL-2.0
- **SPDX ID:** MPL-2.0
- **Category:** Weak copyleft (file-level)
- **Key Obligations:** Copyleft applies only to the original MPL-licensed files; modifications to those files must be shared; new files may be proprietary
- **Compatibility:** Compatible with GPL (via secondary licensing clause), Apache-2.0; file-level copyleft is less restrictive than GPL
- **Typical Use:** Mozilla Firefox, LibreOffice components, Rust standard library parts
- **Risk Level:** Medium

### EPL-2.0
- **SPDX ID:** EPL-2.0
- **Category:** Weak copyleft (module-level)
- **Key Obligations:** Copyleft applies to the module/plug-in level; separate modules may be proprietary; patent grant included
- **Compatibility:** Compatible with GPL (via secondary licensing); INCOMPATIBLE with pure GPL without secondary license clause
- **Typical Use:** Eclipse IDE, Java ecosystem tools, Clojure
- **Risk Level:** Medium

## Source-Available Licenses

### BSL (Business Source License)
- **SPDX ID:** BUSL-1.1 (non-standard SPDX)
- **Category:** Source-available (time-delayed)
- **Key Obligations:** Source available but restricted use; automatically converts to open-source (typically GPL or Apache-2.0) after specified period (usually 3-4 years); production use may require commercial license during restricted period
- **Compatibility:** NOT open-source during restricted period; compatible with target license after conversion date
- **Typical Use:** CockroachDB, MariaDB MaxScale, Sentry
- **Risk Level:** High (timing-dependent; commercial license needed for production)

### SSPL (Server Side Public License)
- **SPDX ID:** SSPL-1.0 (not OSI approved)
- **Category:** Source-available (broad copyleft)
- **Key Obligations:** Same as AGPL-3.0 plus must release ALL software used to operate the service (management, orchestration, monitoring, etc.); far broader than AGPL
- **Compatibility:** NOT OSI approved; effectively incompatible with proprietary use as SaaS
- **Typical Use:** MongoDB (since 2018), Elasticsearch (transitioned from Apache-2.0)
- **Risk Level:** Critical for SaaS products

### Elastic-2.0
- **SPDX ID:** Elastic-2.0 (not OSI approved)
- **Category:** Source-available (use restriction)
- **Key Obligations:** Free use except for providing the software as a managed service; cannot offer "Elasticsearch as a Service"; otherwise permissive
- **Compatibility:** NOT OSI approved; compatible for non-competing use
- **Typical Use:** Elasticsearch, Kibana
- **Risk Level:** High for managed service providers

## Compatibility Quick Reference

| Your Project →<br>↓ Dependency | Proprietary | MIT / BSD | Apache-2.0 | GPL-3.0 | AGPL-3.0 | LGPL-3.0 | MPL-2.0 |
|---|---|---|---|---|---|---|---|
| MIT | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Apache-2.0 | ✅ | ✅ | ✅ | ✅* | ✅* | ✅ | ✅ |
| BSD-2/3-Clause | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| ISC | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Unlicense / CC0 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| LGPL-3.0 | ⚠️† | ⚠️† | ⚠️† | ✅ | ✅ | ✅ | ⚠️† |
| MPL-2.0 | ⚠️‡ | ⚠️‡ | ⚠️‡ | ✅ | ✅ | ✅ | ✅ |
| GPL-3.0 | ❌ | ❌ | ✅* | ✅ | ✅ | ✅ | ❌ |
| AGPL-3.0 | ❌ | ❌ | ✅* | ✅ | ✅ | ✅ | ❌ |
| GPL-2.0 | ❌ | ❌ | ❌ | ✅§ | ❌ | ❌ | ❌ |
| BSL | ❌‖ | ❌‖ | ❌‖ | ❌‖ | ❌‖ | ❌‖ | ❌‖ |
| SSPL | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Elastic-2.0 | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |

**Legend:**
- ✅ Compatible
- ⚠️ Conditional — check obligations carefully
- ❌ Incompatible or high risk
- `*` GPL-3.0 can use Apache-2.0 code (one-way compatibility via patent grant); Apache-2.0 projects cannot use GPL-3.0 code
- `†` Dynamic linking generally safe for proprietary; static linking may trigger copyleft
- `‡` File-level copyleft; new files may remain proprietary
- `§` GPL-3.0 can use GPL-2.0 only if GPL-2.0 has "or any later version" clause
- `‖` During restricted period; converts to open-source after change date
