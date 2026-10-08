from __future__ import annotations

import json
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[3]


class PlatformRoutingTests(unittest.TestCase):
    def test_universal_entrypoint_routes_without_full_repository_scan(self) -> None:
        entrypoint = (REPO_ROOT / "AI_ENTRYPOINT.md").read_text(encoding="utf-8")
        self.assertIn("routing/task-router.json", entrypoint)
        self.assertIn("Não leia o repositório inteiro", entrypoint)
        self.assertIn("relatorio_processual.md", entrypoint)

    def test_task_router_has_all_supported_tasks_and_platforms(self) -> None:
        router = json.loads((REPO_ROOT / "routing/task-router.json").read_text(encoding="utf-8"))
        self.assertEqual(
            set(router["tasks"]),
            {"ingest", "analyze", "petition", "deadlines", "evidence", "audit"},
        )
        self.assertEqual(
            set(router["platforms"]),
            {"manus", "gemini_cli", "gemini_gem", "grok", "chatgpt", "claude"},
        )

    def test_platform_entrypoints_are_present_and_separate(self) -> None:
        expected = [
            "SKILL.md",
            "GEMINI.md",
            "gemini-extension.json",
            "adapters/gemini/GEM_INSTRUCTIONS.md",
            "adapters/grok/SYSTEM_INSTRUCTIONS.md",
            "adapters/chatgpt/INSTRUCTIONS.md",
            "adapters/claude/CLAUDE_INSTRUCTIONS.md",
        ]
        for relative in expected:
            self.assertTrue((REPO_ROOT / relative).is_file(), relative)

    def test_platform_instructions_do_not_request_other_ai_calls(self) -> None:
        for path in (REPO_ROOT / "adapters").rglob("*.md"):
            text = path.read_text(encoding="utf-8").lower()
            self.assertNotIn("chame outra ia", text, path.as_posix())
            self.assertNotIn("call another ai", text, path.as_posix())


if __name__ == "__main__":
    unittest.main()
