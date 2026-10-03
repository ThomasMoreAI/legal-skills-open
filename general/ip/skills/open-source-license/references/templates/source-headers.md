# Source File Header Templates

License headers should be placed at the top of source files to indicate copyright and licensing.

---

## When to Use Source Headers

**Required:**
- GPL/LGPL/AGPL (strongly recommended by FSF)
- MPL-2.0 (required per file)
- Apache-2.0 (recommended)

**Recommended:**
- All licenses for clarity
- Multi-contributor projects
- Projects that may be forked

**Optional:**
- Small personal projects
- MIT/BSD with clear LICENSE file

---

## MIT License Header

```
// Copyright (c) [YEAR] [FULLNAME]
// SPDX-License-Identifier: MIT
```

**Extended version:**

```
// [PROJECT NAME]
// Copyright (c) [YEAR] [FULLNAME]
//
// Permission is hereby granted, free of charge, to any person obtaining a copy
// of this software and associated documentation files (the "Software"), to deal
// in the Software without restriction, including without limitation the rights
// to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
// copies of the Software, and to permit persons to whom the Software is
// furnished to do so, subject to the following conditions:
//
// The above copyright notice and this permission notice shall be included in all
// copies or substantial portions of the Software.
//
// THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
// IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
// FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
// AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
// LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
// OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
// SOFTWARE.
```

---

## Apache-2.0 License Header

**Standard (recommended by Apache Foundation):**

```
// Copyright [YEAR] [COPYRIGHT HOLDER]
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.
```

**Short version (with SPDX):**

```
// Copyright [YEAR] [COPYRIGHT HOLDER]
// SPDX-License-Identifier: Apache-2.0
```

---

## BSD-3-Clause Header

```
// Copyright (c) [YEAR], [FULLNAME]
// SPDX-License-Identifier: BSD-3-Clause
```

**Extended version:**

```
// Copyright (c) [YEAR], [FULLNAME]
// All rights reserved.
//
// Redistribution and use in source and binary forms, with or without
// modification, are permitted provided that the following conditions are met:
//
// 1. Redistributions of source code must retain the above copyright notice,
//    this list of conditions and the following disclaimer.
// 2. Redistributions in binary form must reproduce the above copyright notice,
//    this list of conditions and the following disclaimer in the documentation
//    and/or other materials provided with the distribution.
// 3. Neither the name of the copyright holder nor the names of its contributors
//    may be used to endorse or promote products derived from this software
//    without specific prior written permission.
//
// THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
// AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
// IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
// ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
// LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
// CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
// SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
// INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
// CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
// ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
// POSSIBILITY OF SUCH DAMAGE.
```

---

## GPL-3.0 Header

**Standard (recommended by FSF):**

```
// [one line description of the program]
// Copyright (C) [YEAR]  [FULLNAME]
//
// This program is free software: you can redistribute it and/or modify
// it under the terms of the GNU General Public License as published by
// the Free Software Foundation, either version 3 of the License, or
// (at your option) any later version.
//
// This program is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
// GNU General Public License for more details.
//
// You should have received a copy of the GNU General Public License
// along with this program.  If not, see <https://www.gnu.org/licenses/>.
```

**Short version:**

```
// Copyright (C) [YEAR] [FULLNAME]
// SPDX-License-Identifier: GPL-3.0-or-later
```

---

## LGPL-3.0 Header

```
// [one line description of the library]
// Copyright (C) [YEAR]  [FULLNAME]
//
// This library is free software; you can redistribute it and/or
// modify it under the terms of the GNU Lesser General Public
// License as published by the Free Software Foundation; either
// version 3 of the License, or (at your option) any later version.
//
// This library is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
// Lesser General Public License for more details.
//
// You should have received a copy of the GNU Lesser General Public License
// along with this library; if not, see <https://www.gnu.org/licenses/>.
```

---

## AGPL-3.0 Header

```
// [one line description of the program]
// Copyright (C) [YEAR]  [FULLNAME]
//
// This program is free software: you can redistribute it and/or modify
// it under the terms of the GNU Affero General Public License as published
// by the Free Software Foundation, either version 3 of the License, or
// (at your option) any later version.
//
// This program is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
// GNU Affero General Public License for more details.
//
// You should have received a copy of the GNU Affero General Public License
// along with this program.  If not, see <https://www.gnu.org/licenses/>.
```

---

## MPL-2.0 Header

**Required for each file:**

```
// This Source Code Form is subject to the terms of the Mozilla Public
// License, v. 2.0. If a copy of the MPL was not distributed with this
// file, You can obtain one at https://mozilla.org/MPL/2.0/.
```

**With copyright:**

```
// Copyright (c) [YEAR] [FULLNAME]
//
// This Source Code Form is subject to the terms of the Mozilla Public
// License, v. 2.0. If a copy of the MPL was not distributed with this
// file, You can obtain one at https://mozilla.org/MPL/2.0/.
```

---

## Language-Specific Comment Syntax

### C/C++/Java/JavaScript/Go/Rust/Swift

```c
// Single line comment
// continuation

/* Block comment
 * for longer headers
 */
```

### Python

```python
# Copyright (c) 2024 Author Name
# SPDX-License-Identifier: MIT

"""
Module docstring can also contain license info.
"""
```

### Shell/Bash

```bash
#!/bin/bash
# Copyright (c) 2024 Author Name
# SPDX-License-Identifier: MIT
```

### HTML

```html
<!--
  Copyright (c) 2024 Author Name
  SPDX-License-Identifier: MIT
-->
```

### CSS

```css
/*
 * Copyright (c) 2024 Author Name
 * SPDX-License-Identifier: MIT
 */
```

### SQL

```sql
-- Copyright (c) 2024 Author Name
-- SPDX-License-Identifier: MIT
```

### Ruby

```ruby
# Copyright (c) 2024 Author Name
# SPDX-License-Identifier: MIT
```

---

## SPDX License Identifiers

Use SPDX identifiers for machine-readable license specification:

| License | SPDX Identifier |
|---------|-----------------|
| MIT | `MIT` |
| Apache 2.0 | `Apache-2.0` |
| BSD 2-Clause | `BSD-2-Clause` |
| BSD 3-Clause | `BSD-3-Clause` |
| GPL 2.0 only | `GPL-2.0-only` |
| GPL 2.0 or later | `GPL-2.0-or-later` |
| GPL 3.0 only | `GPL-3.0-only` |
| GPL 3.0 or later | `GPL-3.0-or-later` |
| LGPL 3.0 | `LGPL-3.0-only` |
| AGPL 3.0 | `AGPL-3.0-only` |
| MPL 2.0 | `MPL-2.0` |
| ISC | `ISC` |
| Unlicense | `Unlicense` |

**Dual license expression:**
```
// SPDX-License-Identifier: MIT OR Apache-2.0
```

---

## Preserving Headers in Minification

Configure your build tools to preserve license headers:

### Terser (JavaScript)

```javascript
// terser.config.js
module.exports = {
  output: {
    comments: /^\s*!|@license|@preserve|Copyright/i
  }
};
```

### Webpack

```javascript
// webpack.config.js
const TerserPlugin = require('terser-webpack-plugin');

module.exports = {
  optimization: {
    minimizer: [
      new TerserPlugin({
        terserOptions: {
          output: {
            comments: /@license|@preserve|Copyright/i,
          },
        },
        extractComments: false,
      }),
    ],
  },
};
```

### CSS (cssnano)

```javascript
// postcss.config.js
module.exports = {
  plugins: [
    require('cssnano')({
      preset: ['default', {
        discardComments: {
          removeAll: false,
          remove: (comment) => !/@license|@preserve|Copyright/i.test(comment)
        }
      }]
    })
  ]
};
```
