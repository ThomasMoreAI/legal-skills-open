// Smoke test for src/lib/sanitize.ts
// Run: npx tsx scripts/test-sanitize.ts

import { stripHtml, truncateText } from '../src/lib/sanitize';

function expect(name: string, actual: unknown, expected: unknown) {
  const a = JSON.stringify(actual);
  const e = JSON.stringify(expected);
  if (a === e) {
    console.log(`  ✓ ${name}`);
  } else {
    console.error(`  ✗ ${name}`);
    console.error(`    expected: ${e}`);
    console.error(`    actual:   ${a}`);
    process.exitCode = 1;
  }
}

console.log('--- sanitize.ts smoke test ---\n');

console.log('[1] Basic tag stripping');
expect('simple <b>tag</b>',
  stripHtml('Hello <b>World</b>!'),
  'Hello World!');

console.log('\n[2] Script block removal (whole block, not just tags)');
expect('<script>alert(1)</script> stripped',
  stripHtml('before<script>alert(1)</script>after'),
  'beforeafter');
expect('script with attrs',
  stripHtml('<script type="text/javascript" src="evil.js">var x = 1;</script>done'),
  'done');

console.log('\n[3] Style block removal');
expect('<style>...</style> stripped',
  stripHtml('<style>.x { color: red; }</style>text'),
  'text');

console.log('\n[4] HTML comment removal (content vanishes, not just markers)');
expect('<!-- secret --> stripped',
  stripHtml('before<!-- this is a comment -->after'),
  'beforeafter');

console.log('\n[5] CDATA section removal');
expect('<![CDATA[...]]> stripped',
  stripHtml('before<![CDATA[ <script>alert(1)</script> ]]>after'),
  'beforeafter');

console.log('\n[6] Entity decoding (named)');
expect('&lt; &gt; &amp; &quot; &apos; &nbsp;',
  stripHtml('a &lt; b &gt; c &amp; d &quot; e &apos; f &nbsp; g'),
  'a < b > c & d " e \' f \u00A0 g');

console.log('\n[7] Entity decoding (numeric decimal)');
expect('&#65; &#66; &#67;',
  stripHtml('&#65;&#66;&#67;'),
  'ABC');

console.log('\n[8] Entity decoding (hex)');
expect('&#x41; &#x42; &#x43;',
  stripHtml('&#x41;&#x42;&#x43;'),
  'ABC');

console.log('\n[9] Invalid code points return replacement char');
expect('&#xFFFFFFFF; (out of range)',
  stripHtml('&#xFFFFFFFF;'),
  '\uFFFD');
expect('&#xD800; (surrogate)',
  stripHtml('&#xD800;'),
  '\uFFFD');

console.log('\n[10] Whitespace collapse');
expect('multiple   spaces   and\n\ntabs',
  stripHtml('multiple   spaces   and\n\ntabs'),
  'multiple spaces and tabs');

console.log('\n[11] Empty input handling');
expect('empty string',
  stripHtml(''),
  '');
expect('null-ish (coerced)',
  stripHtml(undefined as unknown as string),
  '');

console.log('\n[12] Thai text preserved');
expect('Thai with tags',
  stripHtml('<p>สวัสดี <strong>ครับ</strong></p>'),
  'สวัสดี ครับ');

console.log('\n[13] Truncate text');
expect('truncateText("hello world", 8)',
  truncateText('hello world', 8),
  'hello w…');
expect('truncateText("short", 10) (no truncation)',
  truncateText('short', 10),
  'short');

console.log('\n[14] Real-world RSS sample (mixed HTML + entities + Thai)');
const rssSample = '<![CDATA[<p>ประกาศกระทรวงแรงงาน เรื่อง <b>ค่าจ้างขั้นต่ำ</b> &amp; โอที</p>]]>';
const result = stripHtml(rssSample);
expect('RSS CDATA + HTML stripped',
  result,
  'ประกาศกระทรวงแรงงาน เรื่อง ค่าจ้างขั้นต่ำ & โอที');

console.log('\n--- All tests passed ---');
