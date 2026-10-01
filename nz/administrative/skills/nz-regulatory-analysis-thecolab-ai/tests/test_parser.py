#!/usr/bin/env python3
"""Adversarial deterministic parser and safety tests."""
from __future__ import annotations

import importlib.util
import io
import sys
from email.message import Message
from pathlib import Path

SKILL_DIR = Path(__file__).resolve().parents[1]
FIXTURES = SKILL_DIR / "tests" / "fixtures"
spec = importlib.util.spec_from_file_location("nz_regulatory_cli", SKILL_DIR / "scripts" / "cli.py")
assert spec and spec.loader
cli = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = cli
spec.loader.exec_module(cli)


class FakeResponse:
    def __init__(self, body: bytes, content_type: str = "text/html") -> None:
        self._body = io.BytesIO(body)
        self.headers = Message()
        self.headers["Content-Type"] = content_type

    def read(self, amount: int) -> bytes:
        return self._body.read(amount)

    def geturl(self) -> str:
        return cli.REGULATION_INDEX


def expect_cli_error(fn, code: int, blocked: bool = False) -> None:
    try:
        fn()
    except cli.CliError as exc:
        assert exc.code == code
        assert exc.blocked is blocked
    else:
        raise AssertionError("expected CliError")


def main() -> int:
    regulation = cli.parse_regulation_search((FIXTURES / "regulation-search.html").read_text(encoding="utf-8"))
    assert regulation == [{
        "title": "Regulatory Impact Statement: Sample measure",
        "url": cli.REGULATION_INDEX + "sample-ris/",
        "published": "12 September 2026",
        "author": "Example Department",
        "document_type": "regulatory_impact_statement",
        "publisher": "Ministry for Regulation",
    }]
    print("[PASS] fixture regulation search parses one allowlisted typed result")

    environment, total = cli.parse_environment_search((FIXTURES / "environment-search.html").read_text(encoding="utf-8"))
    assert total == 1 and environment[0]["document_type"] == "publication_package"
    assert environment[0]["document_types"] == ["cabinet_paper", "regulatory_impact_statement"]
    assert environment[0]["tags"] == ["Cabinet Paper", "Regulatory Impact Statement"]
    print("[PASS] fixture environment embedded listing parses tags, total, and URL")

    detail = cli.parse_detail((FIXTURES / "detail-page.html").read_text(encoding="utf-8"), cli.ENVIRONMENT_INDEX + "synthetic-package/")
    assert detail["document_count"] == 3
    assert detail["document_type"] == "publication_page"
    assert [item["document_type"] for item in detail["documents"]] == [
        "regulatory_impact_statement", "independent_quality_assessment", "cabinet_paper"
    ]
    assert all(item["url"].startswith(cli.ENVIRONMENT_ROOT) for item in detail["documents"])
    assert all("#" not in item["url"] for item in detail["documents"])
    print("[PASS] fixture detail deduplicates fragments, excludes external PDFs, and distinguishes document types")

    first_page = (FIXTURES / "regulation-search.html").read_text(encoding="utf-8")
    second_page = (FIXTURES / "regulation-search-page-2.html").read_text(encoding="utf-8")
    first_url = cli.source_url("regulation", "sample")
    second_url = cli.REGULATION_INDEX + "?query=sample&start=12"
    requested: list[str] = []
    real_fetch = cli.fetch_html

    def fake_fetch(url: str) -> tuple[str, str]:
        requested.append(url)
        if url == first_url:
            return first_page, first_url
        if url == second_url:
            return second_page, second_url
        raise AssertionError(f"unexpected pagination URL: {url}")

    setattr(cli, "fetch_html", fake_fetch)
    try:
        paged, _ = cli.run_search("sample", "regulation", 25)
    finally:
        setattr(cli, "fetch_html", real_fetch)
    assert requested == [first_url, second_url]
    assert paged["returned"] == 2 and paged["source_totals"] == {"regulation": 2}
    assert paged["source_urls"] == requested

    real_page_limit = cli.MAX_REGULATION_PAGES
    setattr(cli, "fetch_html", fake_fetch)
    setattr(cli, "MAX_REGULATION_PAGES", 1)
    requested.clear()
    try:
        expect_cli_error(lambda: cli.run_search("sample", "regulation", 25), 6)
    finally:
        setattr(cli, "fetch_html", real_fetch)
        setattr(cli, "MAX_REGULATION_PAGES", real_page_limit)
    assert requested == [first_url]
    print("[PASS] regulation pagination is followed accurately and fails closed at its page bound")

    cases = {
        "RAS": "regulatory_analysis_summary",
        "Regulatory Impact Assessment": "regulatory_impact_assessment",
        "Supplementary Analysis Report": "supplementary_analysis_report",
        "Cost Recovery Impact Statement": "cost_recovery_impact_statement",
        "Agency quality assurance statement": "agency_quality_assessment",
        "Quality assessment": "quality_assessment",
        "Cabinet minute": "cabinet_minute",
    }
    for title, expected in cases.items():
        assert cli.classify_document(title) == expected, (title, cli.classify_document(title))
    assert cli.classify_document("Neutral package", cli.ENVIRONMENT_INDEX + "neutral/") == "publication_page"
    print("[PASS] adversarial type classifier keeps RAS, RIS, RIA, QA, SAR, CRIS, and Cabinet records distinct")

    malicious = '<listing-results-container :id="{&quot;results&quot;:[],&quot;total&quot;:0}.__class__"></listing-results-container>'
    expect_cli_error(lambda: cli.parse_environment_search(malicious), 6)
    for invalid_total in (-1, True):
        total_html = f'<listing-results-container :id="{{&quot;results&quot;:[],&quot;total&quot;:{str(invalid_total).lower()}}}"></listing-results-container>'
        expect_cli_error(lambda html=total_html: cli.parse_environment_search(html), 6)
    undersized_total = '<listing-results-container :id="{&quot;results&quot;:[{&quot;href&quot;:&quot;/what-government-is-doing/cabinet-papers-and-regulatory-impact-statements/x/&quot;,&quot;title&quot;:&quot;X&quot;}],&quot;total&quot;:0}"></listing-results-container>'
    expect_cli_error(lambda: cli.parse_environment_search(undersized_total), 6)
    expect_cli_error(lambda: cli.parse_environment_search("<html><h1>normal-looking empty page</h1></html>"), 6)
    expect_cli_error(lambda: cli.parse_regulation_search("<html><h1>normal-looking empty page</h1></html>"), 6)
    assert cli.parse_regulation_search('<div class="search__results"><div class="search__results-no-results">No match</div></div>') == []
    print("[PASS] adversarial embedded expressions and missing listings fail closed as parser errors")

    assert cli.canonical_official_url("https://outside.invalid/x.pdf") is None
    assert cli.canonical_official_url("https://www.regulation.govt.nz@outside.invalid/x") is None
    assert cli.canonical_official_url("http://www.regulation.govt.nz/publications-and-resources/regulatory-analysis-summaries/x") is None
    assert cli.canonical_official_url("https://www.regulation.govt.nz/other-area/x") is None
    assert cli.canonical_official_url("https://www.regulation.govt.nz/publications-and-resources/regulatory-analysis-summaries/%2e%2e/%2e%2e/private") is None
    assert cli.canonical_official_url("https://environment.govt.nz/assets/%252e%252e/private/x.pdf") is None
    assert cli.canonical_official_url("https://environment.govt.nz/assets/%25252e%25252e/private/x.pdf") is None
    assert cli.canonical_official_url("https://environment.govt.nz/assets/%255c..%255cprivate/x.pdf") is None
    assert cli.canonical_official_url(cli.ENVIRONMENT_INDEX, required_host="www.regulation.govt.nz") is None
    cross_regulation = (FIXTURES / "regulation-search.html").read_text(encoding="utf-8").replace(
        "/publications-and-resources/regulatory-analysis-summaries/sample-ris/",
        cli.ENVIRONMENT_INDEX + "sample-ris/",
    )
    expect_cli_error(lambda: cli.parse_regulation_search(cross_regulation), 6)
    cross_environment = (FIXTURES / "environment-search.html").read_text(encoding="utf-8").replace(
        "\\/what-government-is-doing\\/cabinet-papers-and-regulatory-impact-statements\\/synthetic-package\\/",
        "https:\\/\\/www.regulation.govt.nz\\/publications-and-resources\\/regulatory-analysis-summaries\\/example-package\\/",
    )
    expect_cli_error(lambda: cli.parse_environment_search(cross_environment), 6)
    cross_detail = '<h1>Package</h1><a href="' + cli.REGULATION_ROOT + '/assets/cross.pdf">Cross-host PDF</a>'
    assert cli.parse_detail(cross_detail, cli.ENVIRONMENT_INDEX + "package/")["document_count"] == 0
    print("[PASS] repeatedly encoded traversal cannot escape scheme, host, or publication-path allowlists")

    expect_cli_error(lambda: cli._read_response(FakeResponse(b"<html>Verify you are human</html>")), 4, True)
    expect_cli_error(lambda: cli._read_response(FakeResponse(b"%PDF", "application/pdf")), 6)
    print("[PASS] blocked-page and wrong-content contracts are explicit failures, never empty success")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
