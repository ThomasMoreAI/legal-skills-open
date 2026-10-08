# Contributing to Panya-AI

## Development Setup

```bash
# Install dependencies
bun install

# Start dev server
bun run dev

# Run tests
bun run test

# Run tests with coverage
bunx vitest run --coverage

# Build for production
bun run build
```

## Code Quality

This project uses the following tools to maintain code quality:

- **SonarCloud**: Automated code quality analysis on every push
- **CodeQL**: Security vulnerability scanning
- **Gitleaks**: Secret detection in source code
- **ESLint**: Code style and best practices
- **Vitest**: Unit testing with coverage

### Before Submitting a PR

1. Run `bun run test` — all tests must pass
2. Run `bun run build` — build must succeed
3. Check SonarCloud — no new issues introduced
4. No secrets or credentials in code

## Code Style

- Use TypeScript for all new code
- Follow existing naming conventions
- Extract reusable logic into `src/lib/api-helpers/`
- Write unit tests for new helper functions
- Use `readonly` for component props
- Avoid `any` types where possible

## Project Structure

```
src/
  app/              # Next.js App Router (API routes + pages)
    api/            # API route handlers
  components/       # React components
    chat/           # AI chat interface
    common/         # Shared components (BackButton, BookmarkButton)
    contract/       # Contract analysis view
    home/           # Landing page (Hero, LawList)
    judgment/       # Judgment list + detail views
    law/            # Law list + detail + section views
    layout/         # Sidebar navigation
    onboarding/     # Persona onboarding + switcher
    pdf/            # PDF builder wizard
    risk/           # Risk matrix 5×5
    search/         # Global search view
    templates/      # Contract template browser
    ui/             # shadcn/ui components (vendored — do not edit)
  lib/              # Shared libraries
    api-helpers/    # Pure functions extracted from API routes (testable)
    __tests__/      # Unit tests
    db.ts           # Prisma client singleton
    navigation.ts   # URL-based navigation hook
    persona.ts      # Persona definitions (HR/Legal/Owner)
    rag.ts          # RAG retrieval (FTS5 + LIKE fallback)
    types.ts        # Shared TypeScript types
    utils.ts        # Utility functions (cn class merge)
    zai-client.ts   # LLM client (OpenRouter/Z.AI)
```

## License

By contributing, you agree that your contributions will be licensed under the MIT License.
