# Allure Test Spec Writing Guide (Safe DOCX Adaptation)

Convert tests into Allure-readable behavioral specs that are easy to scan in reports and easy to debug on failure.

## Quick Reference (TypeScript + Vitest)

Use repo wrappers where available.

```ts
import { describe, expect } from 'vitest';
import { itAllure as it, allureStep, allureJsonAttachment } from '../testing/allure-test.js';

describe('Feature Name', () => {
  it('Human-readable test title', async () => {
    let result: { success: boolean };

    await allureStep('Given some precondition', async () => {
      await allureJsonAttachment('input', { key: 'value' });
    });

    await allureStep('When I perform an action', async () => {
      result = { success: true };
    });

    await allureStep('Then the result is correct', async () => {
      expect(result!.success).toBe(true);
    });
  });
});
```

If direct Allure calls are required:
- import from `allure-js-commons`
- `await` every Allure API call
- never import test APIs from `allure-vitest`

## Golden Rule: One Assertion Per Step

### Bad
```ts
await allureStep('Then everything works', async () => {
  expect(result.status).toBe('success');
  expect(result.count).toBe(5);
  expect(result.items[0].name).toBe('foo');
});
```

### Good
```ts
await allureStep('Then status is success', async () => {
  expect(result.status).toBe('success');
});

await allureStep('And count is 5', async () => {
  expect(result.count).toBe(5);
});

await allureStep("And first item is 'foo'", async () => {
  expect(result.items[0].name).toBe('foo');
});
```

## Given/When/Then Pattern

Use explicit step prefixes for report readability:
- Given
- And (additional setup)
- When
- Then
- And (additional expectations)

```ts
await allureStep('Given a logged-in user', async () => {
  user = createUser();
});

await allureStep('When updating the profile name', async () => {
  result = await updateProfile(user, { name: 'New Name' });
});

await allureStep('Then the update succeeds', async () => {
  expect(result.success).toBe(true);
});
```

## Attachments for Debugging

Add context that makes failures diagnosable without rerunning locally.

```ts
await allureJsonAttachment('request', requestPayload);
await allureJsonAttachment('response', responsePayload);
```

Recommended attachment content:
- input fixtures
- mutation params
- normalized output
- conflict diagnostics
- error payloads

## Severity Guidance

Default severity is `normal` in wrappers.
Use elevated severity selectively:
- `critical`: mutation correctness, data loss risk, security/path-policy guardrails
- `minor`: narrow edge-case behavior

## File Naming and Scope

- `*.test.ts`: standard collocated tests (default)
- Use Allure labels/steps/attachments inside these tests.
- Reserve `*.allure.test.ts` only for legacy files or explicit migration constraints.

Keep test files focused:
- one module or one capability per file
- avoid unrelated assertions in the same file

## Allure Report Hierarchy Notes

This repo uses package-level compat reporters and setup hooks to keep Allure 3 hierarchy stable.

Follow existing package conventions:
- `packages/safe-docx/src/testing/*`
- `packages/docx-primitives/test/helpers/*`
- `packages/docx-comparison/src/testing/*`

Do not replace compat reporter wiring in `vitest.config.ts` unless explicitly requested.

## Coverage-First Prioritization

When increasing coverage:
1. Rank by uncovered branches in high-blast-radius code.
2. Prioritize mutators, parser/serializer boundaries, and safety checks.
3. Add tests for strict/permissive modes and transactionality.
4. Verify targeted tests first, then package coverage.

## Commands

```bash
npm run test:run -w @usejunior/safe-docx
npm run test:run -w @usejunior/docx-primitives
npm run test:run -w @usejunior/docx-comparison
npm run test:coverage:packages
node scripts/report_package_coverage.mjs
```

## Quick Checklist Before Committing

- Test title is behavior-readable.
- Steps are Given/When/Then/And.
- One assertion per step where practical.
- Attachments added for nontrivial data paths.
- Error code/hint text validated for failure-path tests.
