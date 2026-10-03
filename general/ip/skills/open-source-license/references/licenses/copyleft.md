# Copyleft Open Source Licenses

Copyleft licenses require derivative works to be distributed under the same (or compatible) license terms.

---

## GNU General Public License v3.0 (GPL-3.0)

**SPDX Identifier:** `GPL-3.0-only` or `GPL-3.0-or-later`

**Notable Projects:** Linux kernel (v2), GCC, GIMP, WordPress, Drupal, Bash, Git

### Canonical Text

Due to length, the full GPL-3.0 text is available at: https://www.gnu.org/licenses/gpl-3.0.txt

### Preamble (for reference)

```
                    GNU GENERAL PUBLIC LICENSE
                       Version 3, 29 June 2007

 Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>
 Everyone is permitted to copy and distribute verbatim copies
 of this license document, but changing it is not allowed.

                            Preamble

  The GNU General Public License is a free, copyleft license for
software and other kinds of works.

  The licenses for most software and other practical works are designed
to take away your freedom to share and change the works.  By contrast,
the GNU General Public License is intended to guarantee your freedom to
share and change all versions of a program--to make sure it remains free
software for all its users.  We, the Free Software Foundation, use the
GNU General Public License for most of our software; it applies also to
any other work released this way by its authors.  You can apply it to
your programs, too.

  When we speak of free software, we are referring to freedom, not
price.  Our General Public Licenses are designed to make sure that you
have the freedom to distribute copies of free software (and charge for
them if you wish), that you receive source code or can get it if you
want it, that you can change the software or use pieces of it in new
free programs, and that you know you can do these things.

[... full text continues at gnu.org ...]
```

### Key Characteristics
- Strong copyleft: derivative works must use GPL-3.0
- Source code must be provided for distributed binaries
- Explicit patent grant
- Anti-Tivoization provisions (installation information required)
- Compatible with Apache-2.0
- Commercial use allowed (with copyleft obligations)

### GPL-3.0 Header for Source Files

```
<one line to give the program's name and a brief idea of what it does.>
Copyright (C) <year>  <name of author>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
```

---

## GNU General Public License v2.0 (GPL-2.0)

**SPDX Identifier:** `GPL-2.0-only` or `GPL-2.0-or-later`

**Notable Projects:** Linux kernel, BusyBox, MySQL (dual-licensed)

### Canonical Text

Due to length, the full GPL-2.0 text is available at: https://www.gnu.org/licenses/gpl-2.0.txt

### Key Differences from GPL-3.0
- No explicit patent grant
- No anti-Tivoization provisions
- Not compatible with Apache-2.0
- "Or any later version" clause is optional

### GPL-2.0 Header for Source Files

```
<one line to give the program's name and a brief idea of what it does.>
Copyright (C) <year>  <name of author>

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License along
with this program; if not, write to the Free Software Foundation, Inc.,
51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
```

---

## GNU Lesser General Public License v3.0 (LGPL-3.0)

**SPDX Identifier:** `LGPL-3.0-only` or `LGPL-3.0-or-later`

**Notable Projects:** GNU C Library (glibc), GTK, Qt (dual-licensed), FFmpeg (portions)

### Canonical Text

The LGPL-3.0 consists of: GPL-3.0 + additional permissions at: https://www.gnu.org/licenses/lgpl-3.0.txt

### Key Characteristics
- Weak copyleft: allows linking without copyleft obligation
- Library/framework-friendly
- Modifications to LGPL code must be LGPL
- Applications linking to LGPL libraries can be proprietary
- Must allow users to replace the LGPL library
- Commercial use allowed

### When to Use LGPL vs GPL
- Use **LGPL** for libraries you want proprietary software to use
- Use **GPL** when you want to ensure all derivative works remain open source

---

## GNU Lesser General Public License v2.1 (LGPL-2.1)

**SPDX Identifier:** `LGPL-2.1-only` or `LGPL-2.1-or-later`

**Notable Projects:** GNU C Library (older versions), many older libraries

### Canonical Text

Available at: https://www.gnu.org/licenses/lgpl-2.1.txt

### Key Differences from LGPL-3.0
- Based on GPL-2.0 (no patent grant)
- Slightly different linking provisions
- More established, widely understood

---

## GNU Affero General Public License v3.0 (AGPL-3.0)

**SPDX Identifier:** `AGPL-3.0-only` or `AGPL-3.0-or-later`

**Notable Projects:** MongoDB (pre-SSPL), Nextcloud, Mastodon, Grafana

### Canonical Text

Due to length, the full AGPL-3.0 text is available at: https://www.gnu.org/licenses/agpl-3.0.txt

### Key Section: Network Use (Section 13)

```
13. Remote Network Interaction; Use with the GNU General Public License.

Notwithstanding any other provision of this License, if you modify the
Program, your modified version must prominently offer all users
interacting with it remotely through a computer network (if your version
supports such interaction) an opportunity to receive the Corresponding
Source of your version by providing access to the Corresponding Source
from a network server at no charge, through some standard or customary
means of facilitating copying of software.
```

### Key Characteristics
- Strongest copyleft: covers network/SaaS use
- Closes the "ASP loophole" in GPL
- Network users must be able to get source code
- Required for SaaS deployments of AGPL code
- Commercial use allowed (with strong copyleft obligations)

### When to Use AGPL
- Server-side software you want to remain open source
- When you want to prevent SaaS providers from using your code without contributing back
- Often used with commercial dual-licensing strategy

---

## Mozilla Public License 2.0 (MPL-2.0)

**SPDX Identifier:** `MPL-2.0`

**Notable Projects:** Firefox, Thunderbird, LibreOffice, Terraform (pre-BSL)

### Canonical Text

```
Mozilla Public License Version 2.0
==================================

1. Definitions
--------------

1.1. "Contributor"
    means each individual or legal entity that creates, contributes to
    the creation of, or owns Covered Software.

1.2. "Contributor Version"
    means the combination of the Contributions of others (if any) used
    by a Contributor and that particular Contributor's Contribution.

1.3. "Contribution"
    means Covered Software of a particular Contributor.

1.4. "Covered Software"
    means Source Code Form to which the initial Contributor has attached
    the notice in Exhibit A, the Executable Form of such Source Code
    Form, and Modifications of such Source Code Form, in each case
    including portions thereof.

1.5. "Incompatible With Secondary Licenses"
    means

    (a) that the initial Contributor has attached the notice described
        in Exhibit B to the Covered Software; or

    (b) that the Covered Software was made available under the terms of
        version 1.1 or earlier of the License, but not also under the
        terms of a Secondary License.

1.6. "Executable Form"
    means any form of the work other than Source Code Form.

1.7. "Larger Work"
    means a work that combines Covered Software with other material, in
    a separate file or files, that is not Covered Software.

1.8. "License"
    means this document.

1.9. "Licensable"
    means having the right to grant, to the maximum extent possible,
    whether at the time of the initial grant or subsequently, any and
    all of the rights conveyed by this License.

1.10. "Modifications"
    means any of the following:

    (a) any file in Source Code Form that results from an addition to,
        deletion from, or modification of the contents of Covered
        Software; or

    (b) any new file in Source Code Form that contains any Covered
        Software.

1.11. "Patent Claims" of a Contributor
    means any patent claim(s), including without limitation, method,
    process, and apparatus claims, in any patent Licensable by such
    Contributor that would be infringed, but for the grant of the
    License, by the making, using, selling, offering for sale, having
    made, import, or transfer of either its Contributions or its
    Contributor Version.

1.12. "Secondary License"
    means either the GNU General Public License, Version 2.0, the GNU
    Lesser General Public License, Version 2.1, the GNU Affero General
    Public License, Version 3.0, or any later versions of those
    licenses.

1.13. "Source Code Form"
    means the form of the work preferred for making modifications.

1.14. "You" (or "Your")
    means an individual or a legal entity exercising rights under this
    License. For legal entities, "You" includes any entity that
    controls, is controlled by, or is under common control with You. For
    purposes of this definition, "control" means (a) the power, direct
    or indirect, to cause the direction or management of such entity,
    whether by contract or otherwise, or (b) ownership of more than
    fifty percent (50%) of the outstanding shares or beneficial
    ownership of such entity.

2. License Grants and Conditions
--------------------------------

2.1. Grants

Each Contributor hereby grants You a world-wide, royalty-free,
non-exclusive license:

(a) under intellectual property rights (other than patent or trademark)
    Licensable by such Contributor to use, reproduce, make available,
    modify, display, perform, distribute, and otherwise exploit its
    Contributions, either on an unmodified basis, with Modifications, or
    as part of a Larger Work; and

(b) under Patent Claims of such Contributor to make, use, sell, offer
    for sale, have made, import, and otherwise transfer either its
    Contributions or its Contributor Version.

[... continues - full text at mozilla.org/MPL/2.0/ ...]
```

### Key Characteristics
- File-level copyleft (weak copyleft)
- Modified MPL files must remain MPL
- Can combine with proprietary code in "Larger Works"
- Explicit patent grant
- Compatible with GPL (secondary license option)
- Commercial use allowed
- Good balance between permissive and copyleft

### MPL-2.0 Header

```
This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this
file, You can obtain one at https://mozilla.org/MPL/2.0/.
```

---

## Eclipse Public License 2.0 (EPL-2.0)

**SPDX Identifier:** `EPL-2.0`

**Notable Projects:** Eclipse IDE, Jakarta EE, JUnit 5

### Canonical Text

Available at: https://www.eclipse.org/legal/epl-2.0/

### Key Characteristics
- Weak copyleft (module-level)
- Explicit patent grant with retaliation clause
- Compatible with GPL via secondary license mechanism
- Commercial use allowed
- Popular in Java ecosystem
