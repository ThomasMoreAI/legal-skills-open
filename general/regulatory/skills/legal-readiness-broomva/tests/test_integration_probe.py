from __future__ import annotations

import json
import subprocess
import sys
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

SKILL_DIR = Path(__file__).resolve().parents[1]
SCRIPT = SKILL_DIR / "scripts" / "legal_readiness.py"
EXAMPLE = SKILL_DIR / "assets" / "legal-readiness.example.json"


class _Handler(BaseHTTPRequestHandler):
    def do_GET(self) -> None:
        self.send_response(200)
        if self.path.endswith("security.txt"):
            self.send_header("Content-Type", "text/plain; charset=utf-8")
        else:
            self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()

    def log_message(self, format: str, *args: object) -> None:
        return


def test_cli_probe_crosses_real_http_boundary(tmp_path: Path) -> None:
    data = json.loads(EXAMPLE.read_text(encoding="utf-8"))
    data["project"] = {
        "name": "Mothlight Notes",
        "repository": "https://github.com/mothlight/notes",
        "base_url": "https://mothlight.test",
        "template": False,
    }
    manifest = tmp_path / "valid.json"
    manifest.write_text(json.dumps(data), encoding="utf-8")
    server = ThreadingHTTPServer(("127.0.0.1", 0), _Handler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    try:
        result = subprocess.run(
            [
                sys.executable,
                str(SCRIPT),
                "probe",
                str(manifest),
                "--base-url",
                f"http://127.0.0.1:{server.server_port}",
                "--allow-private-network",
            ],
            text=True,
            capture_output=True,
            check=False,
        )
    finally:
        server.shutdown()
        thread.join(timeout=2)
        server.server_close()

    payload = json.loads(result.stdout)
    assert result.returncode == 0, result.stdout + result.stderr
    assert payload["ok"] is True
    assert all(
        item["final_url"].startswith("http://127.0.0.1:")
        for item in payload["observations"]
    )


def test_probe_refuses_empty_surface_set(tmp_path: Path) -> None:
    data = json.loads(EXAMPLE.read_text(encoding="utf-8"))
    data["project"] = {
        "name": "Mothlight Notes",
        "repository": "https://github.com/mothlight/notes",
        "base_url": "https://mothlight.test",
        "template": False,
    }
    data["surfaces"] = []
    manifest = tmp_path / "empty.json"
    manifest.write_text(json.dumps(data), encoding="utf-8")
    result = subprocess.run(
        [sys.executable, str(SCRIPT), "probe", str(manifest)],
        text=True,
        capture_output=True,
        check=False,
    )
    assert result.returncode == 2
    assert "at least one declared surface" in result.stderr
