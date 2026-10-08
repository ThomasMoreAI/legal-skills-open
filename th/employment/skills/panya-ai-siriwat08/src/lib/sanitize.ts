/**
 * HTML sanitization utilities — CodeQL-safe, ZERO regex.
 *
 * Previous versions used multi-character regex patterns for stripping, which
 * CodeQL flagged as "Incomplete multi-character sanitization" (alerts #16-#20).
 * The recommended fix is to either:
 *   (a) rewrite the regex to match single characters, OR
 *   (b) use a well-tested sanitization library.
 *
 * This module takes approach (a) to the extreme: it uses NO regex at all.
 * All scanning is done via manual character-by-character iteration with
 * `String.prototype.indexOf` / `startsWith` for exact substring matching.
 * This eliminates the entire class of regex-bypass vulnerabilities.
 *
 * The stripper:
 *   1. Scans the input character by character
 *   2. Drops HTML comments (<!-- ... -->) entirely
 *   3. Unwraps CDATA sections (<![CDATA[ ... ]]>) — inner content preserved
 *   4. Drops <script>/<style> blocks entirely (including text content)
 *   5. Drops all remaining tags (anything between < and >)
 *   6. Decodes HTML entities (named + numeric decimal + hex)
 *   7. Collapses whitespace runs
 *
 * NOTE: This is for *display text* sanitization only — it does not prevent
 * XSS in HTML rendering contexts. For rendering, use React's default escaping
 * or `dompurify` on the rendered output.
 */

// Entity lookup tables — populated once at module load.
const NAMED_ENTITIES: Record<string, string> = {
  lt: '<',
  gt: '>',
  amp: '&',
  quot: '"',
  apos: "'",
  nbsp: '\u00A0',
  // Common typographic entities
  hellip: '…',
  mdash: '—',
  ndash: '–',
  lsquo: '\u2018',
  rsquo: '\u2019',
  ldquo: '\u201C',
  rdquo: '\u201D',
  // Thai-relevant
  copy: '©',
  reg: '®',
  trade: '™',
};

/**
 * Decode an HTML entity reference like `&lt;` or `&#65;` or `&#x41;`.
 * Returns the decoded string, or `null` if the input is not a valid entity.
 *
 * @param entity Must include leading `&` and trailing `;`
 */
function decodeEntity(entity: string): string | null {
  if (entity.length < 3 || entity.length > 34) return null;
  if (!entity.startsWith('&') || !entity.endsWith(';')) return null;

  const body = entity.slice(1, -1);

  if (body.startsWith('#') && body.length > 1) {
    return decodeNumericEntity(body);
  }

  if (body.length === 0 || body.length > 32) return null;
  if (!isValidEntityName(body)) return null;
  return NAMED_ENTITIES[body] ?? null;
}

/** Decode a numeric entity body like `#65` or `#x41`. */
function decodeNumericEntity(body: string): string | null {
  const rest = body.slice(1);
  if (rest.startsWith('x') || rest.startsWith('X')) {
    return decodeHexEntity(rest.slice(1));
  }
  return decodeDecimalEntity(rest);
}

/** Decode a hex entity like `41` (from `&#x41;`). */
function decodeHexEntity(hex: string): string | null {
  if (hex.length === 0 || hex.length > 8) return null;
  if (!isAllHexChars(hex)) return null;
  return safeFromCodePoint(Number.parseInt(hex, 16));
}

/** Decode a decimal entity like `65` (from `&#65;`). */
function decodeDecimalEntity(rest: string): string | null {
  if (rest.length === 0 || rest.length > 10) return null;
  if (!isAllDecimalChars(rest)) return null;
  return safeFromCodePoint(Number.parseInt(rest, 10));
}

/**
 * Manual hex-char validation — no regex.
 * Returns true if every char is 0-9, a-f, or A-F.
 */
function isAllHexChars(s: string): boolean {
  for (let i = 0; i < s.length; i++) {
    const c = s.codePointAt(i);
    if (c === undefined) return false;
    const isDigit = c >= 48 && c <= 57;   // '0'-'9'
    const isLower = c >= 97 && c <= 102;  // 'a'-'f'
    const isUpper = c >= 65 && c <= 70;   // 'A'-'F'
    if (!isDigit && !isLower && !isUpper) return false;
  }
  return true;
}

/**
 * Manual decimal-char validation — no regex.
 * Returns true if every char is 0-9.
 */
function isAllDecimalChars(s: string): boolean {
  for (let i = 0; i < s.length; i++) {
    const c = s.codePointAt(i);
    if (c === undefined || c < 48 || c > 57) return false;  // '0'-'9'
  }
  return true;
}

/**
 * Manual named-entity validation — no regex.
 * Valid: starts with a letter, followed by 1+ letters/digits.
 */
function isValidEntityName(s: string): boolean {
  if (s.length < 2) return false;
  const first = s.codePointAt(0);
  if (first === undefined) return false;
  const isLetter = (c: number) => (c >= 65 && c <= 90) || (c >= 97 && c <= 122);
  if (!isLetter(first)) return false;
  for (let i = 1; i < s.length; i++) {
    const c = s.codePointAt(i);
    if (c === undefined) return false;
    if (!isLetter(c) && !(c >= 48 && c <= 57)) return false;
  }
  return true;
}

/**
 * Convert a code point to a string, returning the replacement character
 * for invalid/surrogate/overlong code points.
 */
function safeFromCodePoint(code: number): string {
  if (!Number.isFinite(code) || code < 0 || code > 0x10FFFF) return '\uFFFD';
  if (code >= 0xD800 && code <= 0xDFFF) return '\uFFFD';
  if ((code >= 0xFDD0 && code <= 0xFDEF) ||
      ((code & 0xFFFE) === 0xFFFE && code <= 0x10FFFE)) {
    return '\uFFFD';
  }
  try {
    return String.fromCodePoint(code);
  } catch {
    return '\uFFFD';
  }
}

/**
 * Strip all HTML markup from a string and decode entities.
 * Returns plain text safe for inclusion in plain-text contexts
 * (GitHub issue bodies, terminal output, audit logs, etc.).
 *
 * Implementation: manual character-by-character scanning. ZERO regex used
 * for sanitization — only `/^[0-9]+$/` style character-class validation
 * for entity bodies (which does not have the multi-char bypass issue
 * because it validates single characters, not multi-char patterns).
 */
export function stripHtml(input: string): string {
  if (!input) return '';
  const len = input.length;
  let out = '';
  let i = 0;

  while (i < len) {
    const next = processChar(input, i, len);
    out += next.output;
    i = next.nextIndex;
  }
  return collapseWhitespace(out);
}

/** Process the character at position `i` and return output + next index. */
function processChar(input: string, i: number, len: number): { output: string; nextIndex: number } {
  // HTML comment
  if (startsWith(input, '<!--', i)) {
    return { output: '', nextIndex: skipTo(input, i + 4, '-->') };
  }
  // CDATA
  if (startsWith(input, '<![CDATA[', i)) {
    return processCdata(input, i, len);
  }
  // Tags
  if (input[i] === '<') {
    return processTag(input, i, len);
  }
  // Entity
  if (input[i] === '&') {
    return processEntity(input, i);
  }
  // Regular char
  return { output: input[i], nextIndex: i + 1 };
}

/** Skip to the end of a marker (e.g. '-->') and return the index after it. */
function skipTo(input: string, from: number, marker: string): number {
  const idx = input.indexOf(marker, from);
  return idx === -1 ? input.length : idx + marker.length;
}

/** Process CDATA section — unwrap and recursively strip inner content. */
function processCdata(input: string, i: number, len: number): { output: string; nextIndex: number } {
  const end = input.indexOf(']]>', i + 9);
  if (end === -1) {
    return { output: stripHtml(input.slice(i + 9)), nextIndex: len };
  }
  return { output: stripHtml(input.slice(i + 9, end)), nextIndex: end + 3 };
}

/** Process any tag (<script>, <style>, or regular tag). */
function processTag(input: string, i: number, len: number): { output: string; nextIndex: number } {
  if (i + 1 >= len) return { output: '', nextIndex: len };
  const nextChar = input[i + 1];
  if (nextChar === 's' || nextChar === 'S') {
    if (startsWithIgnoreCase(input, '<script', i)) {
      return skipBlockTag(input, i, '</script');
    }
    if (startsWithIgnoreCase(input, '<style', i)) {
      return skipBlockTag(input, i, '</style');
    }
  }
  // Regular tag — skip to '>'
  const tagEnd = input.indexOf('>', i);
  return { output: '', nextIndex: tagEnd === -1 ? len : tagEnd + 1 };
}

/** Skip a block tag like <script>...</script> — returns position after closing tag. */
function skipBlockTag(input: string, i: number, closeTag: string): { output: string; nextIndex: number } {
  const tagEnd = input.indexOf('>', i);
  if (tagEnd === -1) return { output: '', nextIndex: input.length };
  const closeIdx = indexOfIgnoreCase(input, closeTag, tagEnd + 1);
  if (closeIdx === -1) return { output: '', nextIndex: input.length };
  const afterClose = input.indexOf('>', closeIdx);
  return { output: '', nextIndex: afterClose === -1 ? input.length : afterClose + 1 };
}

/** Process HTML entity (&...;) — decode or output literal '&'. */
function processEntity(input: string, i: number): { output: string; nextIndex: number } {
  const semi = input.indexOf(';', i);
  if (semi !== -1 && semi - i >= 2 && semi - i <= 33) {
    const entity = input.slice(i, semi + 1);
    const decoded = decodeEntity(entity);
    if (decoded !== null) {
      return { output: decoded, nextIndex: semi + 1 };
    }
  }
  return { output: '&', nextIndex: i + 1 };
}

/**
 * Collapse runs of ASCII whitespace (space, tab, CR, LF, FF, VT) into a single
 * space, then trim leading/trailing whitespace. Non-breaking spaces (U+00A0)
 * are preserved as intentional content.
 *
 * Manual implementation — no regex used.
 */
function collapseWhitespace(input: string): string {
  const wsChars = new Set([' ', '\t', '\r', '\n', '\f', '\v']);
  const len = input.length;
  let out = '';
  let inWs = false;
  let start = 0;
  let end = input.length;

  // Find first non-ws char
  while (start < len && wsChars.has(input[start])) start++;
  // Find last non-ws char
  while (end > start && wsChars.has(input[end - 1])) end--;

  for (let i = start; i < end; i++) {
    const c = input[i];
    if (wsChars.has(c)) {
      if (!inWs) {
        out += ' ';
        inWs = true;
      }
      // else: skip — we're in a whitespace run, only emit one space
    } else {
      out += c;
      inWs = false;
    }
  }
  return out;
}

// ---------------------------------------------------------------------------
// Pure string helpers (no regex used for security-sensitive scanning)
// ---------------------------------------------------------------------------
function startsWith(str: string, prefix: string, position: number): boolean {
  return str.startsWith(prefix, position);
}

function startsWithIgnoreCase(str: string, prefix: string, position: number): boolean {
  if (position + prefix.length > str.length) return false;
  for (let j = 0; j < prefix.length; j++) {
    const a = str[position + j];
    const b = prefix[j];
    if (a === b) continue;
    if (a.toLowerCase() === b.toLowerCase()) continue;
    return false;
  }
  return true;
}

function indexOfIgnoreCase(str: string, needle: string, fromIndex: number): number {
  const lower = str.toLowerCase();
  const lowerNeedle = needle.toLowerCase();
  return lower.indexOf(lowerNeedle, fromIndex);
}

/**
 * Truncate text to `maxLen` characters, appending an ellipsis if truncated.
 * Counts visible characters (after entity decoding), not bytes.
 */
export function truncateText(text: string, maxLen: number): string {
  if (text.length <= maxLen) return text;
  if (maxLen <= 1) return text.slice(0, maxLen);
  return text.slice(0, maxLen - 1) + '…';
}
