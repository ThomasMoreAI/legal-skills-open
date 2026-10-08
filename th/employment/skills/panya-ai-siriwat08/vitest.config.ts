import { defineConfig } from 'vitest/config';
import path from 'path';

export default defineConfig({
  test: {
    globals: true,
    environment: 'node',
    coverage: {
      provider: 'v8',
      reporter: ['text', 'lcov', 'json-summary'],
      include: [
        'src/lib/*.ts',
        'src/lib/api-helpers/*.ts',
      ],
      exclude: [
        'src/components/**',
        'src/app/**',
        'src/hooks/**',
        'src/lib/db.ts',
        'src/lib/types.ts',
        'src/lib/navigation.ts',
        'src/lib/rag.ts',
        'src/lib/zai-client.ts',
        'src/lib/chat-sessions.ts',
        'src/lib/recently-viewed.ts',
        'src/lib/pdf-extract.ts',
        'src/**/*.test.*',
        'src/**/*.spec.*',
      ],
    },
  },
  resolve: {
    alias: {
      '@': path.resolve(__dirname, './src'),
    },
  },
});
