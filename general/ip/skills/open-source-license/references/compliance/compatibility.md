# License Compatibility Guide

## Understanding License Compatibility

License compatibility determines whether code under different licenses can be combined in the same project. Incompatibility means the combined work cannot legally be distributed.

---

## Compatibility Matrix

### Can License A code be included in a License B project?

| Include → | MIT | Apache | BSD | GPL-2 | GPL-3 | LGPL-3 | AGPL-3 | MPL-2 |
|-----------|-----|--------|-----|-------|-------|--------|--------|-------|
| **MIT** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Apache-2.0** | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ |
| **BSD-3** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **GPL-2.0** | ❌ | ❌ | ❌ | ✅ | ❌* | ❌ | ❌ | ❌ |
| **GPL-3.0** | ❌ | ❌ | ❌ | ❌* | ✅ | ✅ | ✅ | ✅ |
| **LGPL-3.0** | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ |
| **AGPL-3.0** | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ❌ |
| **MPL-2.0** | ✅ | ✅ | ✅ | ✅** | ✅ | ✅ | ✅ | ✅ |

*GPL-2.0 and GPL-3.0 are only compatible if "or later" clause is used
**MPL-2.0 has explicit GPL compatibility provisions

---

## Key Compatibility Rules

### Rule 1: Permissive licenses flow upward

Permissive code (MIT, BSD, Apache) can be included in:
- Other permissive projects
- Copyleft projects (GPL, AGPL)
- Proprietary projects

The resulting project takes on the obligations of the most restrictive license.

### Rule 2: Copyleft licenses are restrictive

GPL/AGPL code can ONLY be included in:
- Projects under the same license
- Projects under compatible copyleft licenses

The resulting project MUST be distributed under GPL/AGPL.

### Rule 3: Apache-2.0 and GPL-2.0 are incompatible

Due to patent retaliation and additional restrictions:
- Apache-2.0 code CANNOT be included in GPL-2.0 projects
- Apache-2.0 IS compatible with GPL-3.0

### Rule 4: LGPL allows linking

LGPL libraries can be linked by:
- Proprietary applications (dynamic linking)
- Any license (if modifications to LGPL code are shared)

### Rule 5: MPL-2.0 is file-scoped

MPL-2.0 code can coexist with other licenses:
- Only MPL files must remain MPL
- Other files can be any license
- Explicit secondary license provision for GPL compatibility

---

## Common Compatibility Scenarios

### Scenario 1: Building a Node.js Application

Typical dependencies are MIT-licensed.

```
Your App (MIT/Apache/Proprietary)
├── express (MIT) ✅
├── lodash (MIT) ✅
├── react (MIT) ✅
└── moment (MIT) ✅
```

**Result:** No compatibility issues. You can use any license.

### Scenario 2: Using GPL Library

```
Your App (???)
├── express (MIT) ✅
└── readline-sync (GPL-3.0) ⚠️
```

**Result:** Your entire app must be GPL-3.0 or compatible.

### Scenario 3: Mixing Apache and GPL

```
Your App (GPL-3.0)
├── Apache-2.0 library ✅ (compatible with GPL-3.0)
└── GPL-2.0 library ❌ (incompatible without "or later")
```

**Result:** Cannot combine unless GPL-2.0 code is "GPL-2.0-or-later"

### Scenario 4: LGPL Library in Proprietary App

```
Your Proprietary App
└── GTK (LGPL-3.0) ✅ if dynamically linked
```

**Requirements:**
- Must dynamically link (not static)
- Must allow users to replace the LGPL library
- Must provide LGPL license text
- Modifications to GTK itself must be LGPL

### Scenario 5: AGPL in Backend Service

```
Your SaaS Platform
└── Grafana (AGPL-3.0) ⚠️
```

**Result:** If you modify Grafana, you must:
- Release your modifications as AGPL-3.0
- Provide source to users accessing via network

---

## Resolving Incompatibilities

### Option 1: Choose a compatible license

Relicense your code to be compatible with dependencies.

### Option 2: Remove incompatible dependency

Find an alternative library with a compatible license.

### Option 3: Isolate incompatible code

Sometimes possible with:
- Separate processes communicating via IPC
- Network APIs (may not always work, especially AGPL)
- Plugins loaded at runtime

### Option 4: Obtain different license

Contact the copyright holder to negotiate alternative licensing.

### Option 5: Use the "system library" exception

GPL has an exception for system libraries (libc, etc.)

---

## Dual-Licensed Dependencies

Some projects offer multiple licenses. You can choose which applies:

```
Dependency: "MIT OR Apache-2.0"
```

You choose ONE:
- MIT: Simpler, no patent clause
- Apache-2.0: Patent grant included

SPDX expression: Use `OR` for choice, `AND` for both required.

---

## Checking Compatibility Programmatically

### Tools for License Compliance

1. **license-checker** (npm)
   ```bash
   npx license-checker --summary
   ```

2. **pip-licenses** (Python)
   ```bash
   pip-licenses --format=table
   ```

3. **go-licenses** (Go)
   ```bash
   go-licenses csv ./...
   ```

4. **FOSSA** - Enterprise compliance platform
5. **Snyk** - Security + license scanning
6. **WhiteSource/Mend** - Enterprise compliance

---

## License Compatibility Flowchart

```
                    ┌─────────────────┐
                    │ Is dependency   │
                    │ permissive?     │
                    └────────┬────────┘
                             │
              ┌──────────────┼──────────────┐
              │ YES          │              │ NO
              ▼              │              ▼
    ┌─────────────────┐      │    ┌─────────────────┐
    │ Can use with    │      │    │ Is it LGPL?     │
    │ any license     │      │    └────────┬────────┘
    └─────────────────┘      │             │
                             │    ┌────────┼────────┐
                             │    │ YES    │        │ NO
                             │    ▼        │        ▼
                             │  ┌──────────┴──┐  ┌──────────────┐
                             │  │Can link if  │  │Is it GPL/AGPL│
                             │  │dynamic +    │  └──────┬───────┘
                             │  │replaceable  │         │
                             │  └─────────────┘    ┌────┼────┐
                             │                     │YES │    │NO
                             │                     ▼    │    ▼
                             │           ┌─────────────┐│┌────────────┐
                             │           │Must use same││ │Check       │
                             │           │license for  │││ specific   │
                             │           │derivative   │││ license    │
                             │           └─────────────┘│└────────────┘
                             │                          │
                             └──────────────────────────┘
```
