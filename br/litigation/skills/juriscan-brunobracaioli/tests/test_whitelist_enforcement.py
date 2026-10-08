"""Tests for the whitelist post-hoc enforcement in scripts/agent_io.py.

Phase 4 Step 4.1: a verificador output must pass BOTH the JSON schema and
the host-whitelist check in references/whitelist_fontes.json. This file
focuses on the whitelist half (the schema half is covered by existing
validate tests).
"""

from __future__ import annotations

import datetime as dt
import json
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "scripts"))

import agent_io  # noqa: E402


TODAY = dt.date.today().isoformat()


def _write(tmp: Path, doc: dict) -> Path:
    p = tmp / "verificador.json"
    p.write_text(json.dumps(doc, ensure_ascii=False), encoding="utf-8")
    return p


def _base_doc(url: str, *, status: str = "CONFIRMADO", trecho: str = "EMENTA", access: str | None = None) -> dict:
    return {
        "schema_version": "1.0",
        "verifications": [
            {
                "tipo": "PRECEDENTE",
                "citacao_original": "REsp 1.234.567/SP",
                "status": status,
                "source_url": url,
                "access_date": access or TODAY,
                "trecho_oficial": trecho,
            }
        ],
    }


def test_whitelisted_exact_host_passes(tmp_path):
    p = _write(tmp_path, _base_doc("https://stj.jus.br/resp/1234567"))
    ok, errors = agent_io.validate_agent_output("verificador", p)
    assert ok, errors


def test_whitelisted_subdomain_passes(tmp_path):
    p = _write(tmp_path, _base_doc("https://processo.stj.jus.br/path"))
    ok, errors = agent_io.validate_agent_output("verificador", p)
    assert ok, errors


def test_non_whitelisted_domain_fails(tmp_path):
    p = _write(tmp_path, _base_doc("https://google.com/search?q=REsp"))
    ok, errors = agent_io.validate_agent_output("verificador", p)
    assert not ok
    assert any("google.com" in e for e in errors)


def test_jusbrasil_fails(tmp_path):
    p = _write(tmp_path, _base_doc("https://www.jusbrasil.com.br/jurisprudencia/..."))
    ok, errors = agent_io.validate_agent_output("verificador", p)
    assert not ok
    assert any("jusbrasil" in e for e in errors)


def test_ip_address_fails(tmp_path):
    p = _write(tmp_path, _base_doc("https://192.168.1.1/stj"))
    ok, errors = agent_io.validate_agent_output("verificador", p)
    assert not ok


def test_missing_trecho_on_confirmado_fails(tmp_path):
    p = _write(
        tmp_path,
        {
            "schema_version": "1.0",
            "verifications": [
                {
                    "tipo": "PRECEDENTE",
                    "citacao_original": "REsp 1.234/SP",
                    "status": "CONFIRMADO",
                    "source_url": "https://stj.jus.br/resp/1234",
                    "access_date": TODAY,
                }
            ],
        },
    )
    ok, errors = agent_io.validate_agent_output("verificador", p)
    assert not ok
    assert any("trecho_oficial" in e for e in errors)


def test_nao_encontrado_without_trecho_passes(tmp_path):
    p = _write(
        tmp_path,
        {
            "schema_version": "1.0",
            "verifications": [
                {
                    "tipo": "PRECEDENTE",
                    "citacao_original": "REsp 9.999.999/ZZ",
                    "status": "NAO_ENCONTRADO",
                    "source_url": "https://scon.stj.jus.br/SCON/...",
                    "access_date": TODAY,
                }
            ],
        },
    )
    ok, errors = agent_io.validate_agent_output("verificador", p)
    assert ok, errors


def test_future_access_date_fails(tmp_path):
    future = (dt.date.today() + dt.timedelta(days=365)).isoformat()
    p = _write(tmp_path, _base_doc("https://stj.jus.br/x", access=future))
    ok, errors = agent_io.validate_agent_output("verificador", p)
    assert not ok
    assert any("future" in e.lower() for e in errors)


def test_non_iso_access_date_fails(tmp_path):
    p = _write(
        tmp_path,
        {
            "schema_version": "1.0",
            "verifications": [
                {
                    "tipo": "PRECEDENTE",
                    "citacao_original": "REsp 1.234/SP",
                    "status": "CONFIRMADO",
                    "source_url": "https://stj.jus.br/resp/1234",
                    "access_date": "11/04/2026",
                    "trecho_oficial": "EMENTA",
                }
            ],
        },
    )
    ok, errors = agent_io.validate_agent_output("verificador", p)
    # Note: schema uses format: date which only validates if the validator
    # is configured with format_checker. Here we rely on our post-hoc check.
    # The schema will pass the string ("format" is advisory by default in
    # jsonschema Draft7Validator without a format_checker). Our post-hoc
    # whitelist check catches it.
    assert not ok
    assert any("YYYY-MM-DD" in e or "access_date" in e for e in errors)


def test_planalto_legislation_passes(tmp_path):
    p = _write(
        tmp_path,
        {
            "schema_version": "1.0",
            "verifications": [
                {
                    "tipo": "LEGISLACAO",
                    "citacao_original": "Lei 14.905/2024 art. 3",
                    "status": "CONFIRMADO",
                    "source_url": "https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2024/lei/L14905.htm",
                    "access_date": TODAY,
                    "trecho_oficial": "Art. 3º Os juros legais...",
                }
            ],
        },
    )
    ok, errors = agent_io.validate_agent_output("verificador", p)
    assert ok, errors


def test_empty_verifications_passes(tmp_path):
    p = _write(tmp_path, {"schema_version": "1.0", "verifications": []})
    ok, errors = agent_io.validate_agent_output("verificador", p)
    assert ok, errors


def test_non_verificador_agent_is_unaffected(tmp_path):
    """Whitelist check must not run for other agents."""
    p = tmp_path / "echo.json"
    p.write_text(json.dumps({
        "ok": True,
        "agent": "juriscan-echo",
        "input_echo": "x",
    }), encoding="utf-8")
    ok, errors = agent_io.validate_agent_output("echo", p)
    assert ok, errors
