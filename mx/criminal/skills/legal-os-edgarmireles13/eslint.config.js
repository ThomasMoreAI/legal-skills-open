import js from "@eslint/js";
import tseslint from "typescript-eslint";

export default tseslint.config(
  {
    ignores: ["dist/**", "node_modules/**", "Old_Python_Vesion/**", "docs/**"],
  },
  js.configs.recommended,
  ...tseslint.configs.recommended,
  {
    languageOptions: {
      ecmaVersion: 2022,
      sourceType: "module",
    },
    rules: {
      "@typescript-eslint/no-explicit-any": "error",
      "@typescript-eslint/no-unused-vars": [
        "error",
        {
          argsIgnorePattern: "^_",
          varsIgnorePattern: "^_",
          caughtErrorsIgnorePattern: "^_",
        },
      ],
      "@typescript-eslint/consistent-type-imports": [
        "warn",
        { prefer: "type-imports", fixStyle: "separate-type-imports" },
      ],
      "no-console": ["warn", { allow: ["error"] }],
      eqeqeq: ["error", "always"],
      "prefer-const": "error",
    },
  },
  {
    // CLI entry points print user-facing output to stdout intentionally.
    files: ["src/utils/cli-handler.ts", "src/cli/**/*.ts"],
    rules: {
      "no-console": "off",
    },
  }
);
