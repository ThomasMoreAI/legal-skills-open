"""Tests for scripts/prazo_calculator.py"""

import sys
import os
from datetime import date

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'scripts'))
from prazo_calculator import (
    load_feriados,
    is_recesso,
    is_business_day,
    next_business_day,
    calculate_prazo,
    get_standard_prazo,
    check_prazo_status,
    _strip_accents,
)


class TestLoadFeriados:
    def test_loads_national_holidays(self):
        feriados = load_feriados(year=2025)
        # Tiradentes
        assert date(2025, 4, 21) in feriados
        # Christmas
        assert date(2025, 12, 25) in feriados
        # Natal
        assert date(2025, 12, 25) in feriados

    def test_loads_mobile_holidays(self):
        feriados = load_feriados(year=2025)
        # Easter 2025 = April 20. Sexta-feira Santa = Easter - 2 = April 18
        assert date(2025, 4, 18) in feriados
        # Carnaval terça = Easter - 47 = March 4
        assert date(2025, 3, 4) in feriados

    def test_loads_state_holidays(self):
        feriados = load_feriados(state='SP', year=2025)
        # Revolução Constitucionalista de 1932
        assert date(2025, 7, 9) in feriados

    def test_no_state(self):
        feriados = load_feriados(year=2025)
        # SP holiday should NOT be in national-only set
        assert date(2025, 7, 9) not in feriados


class TestIsRecesso:
    def test_dec_20_is_recesso(self):
        assert is_recesso(date(2025, 12, 20)) is True

    def test_dec_31_is_recesso(self):
        assert is_recesso(date(2025, 12, 31)) is True

    def test_jan_1_is_recesso(self):
        assert is_recesso(date(2026, 1, 1)) is True

    def test_jan_20_is_recesso(self):
        assert is_recesso(date(2026, 1, 20)) is True

    def test_jan_21_not_recesso(self):
        assert is_recesso(date(2026, 1, 21)) is False

    def test_dec_19_not_recesso(self):
        assert is_recesso(date(2025, 12, 19)) is False

    def test_june_not_recesso(self):
        assert is_recesso(date(2025, 6, 15)) is False


class TestIsBusinessDay:
    def test_weekday(self):
        # 2025-03-17 is Monday
        assert is_business_day(date(2025, 3, 17), set()) is True

    def test_saturday(self):
        assert is_business_day(date(2025, 3, 15), set()) is False

    def test_sunday(self):
        assert is_business_day(date(2025, 3, 16), set()) is False

    def test_holiday(self):
        feriados = {date(2025, 4, 21)}  # Tiradentes
        assert is_business_day(date(2025, 4, 21), feriados) is False

    def test_recesso(self):
        assert is_business_day(date(2025, 12, 22), set()) is False  # Monday in recesso


class TestNextBusinessDay:
    def test_already_business_day(self):
        assert next_business_day(date(2025, 3, 17), set()) == date(2025, 3, 17)

    def test_saturday_to_monday(self):
        assert next_business_day(date(2025, 3, 15), set()) == date(2025, 3, 17)

    def test_holiday_to_next(self):
        feriados = {date(2025, 4, 21)}  # Monday Tiradentes
        assert next_business_day(date(2025, 4, 21), feriados) == date(2025, 4, 22)


class TestCalculatePrazo:
    def test_15_dias_uteis_from_monday(self):
        # 2025-03-17 is Monday. 15 business days = 3 full weeks = April 7 (Monday)
        feriados: set[date] = set()
        result = calculate_prazo(date(2025, 3, 17), 15, 'úteis', feriados)
        assert result == date(2025, 4, 7)

    def test_15_dias_uteis_with_holiday(self):
        # Same but with a holiday in the middle (e.g., April 21 Tiradentes)
        # Start: 2025-04-01 (Tuesday). 15 business days with April 21 being holiday
        feriados = {date(2025, 4, 21)}
        result = calculate_prazo(date(2025, 4, 1), 15, 'úteis', feriados)
        # Without holiday: April 22. With holiday: April 23
        assert result == date(2025, 4, 23)

    def test_5_dias_uteis_embargos(self):
        # 2025-03-17 (Monday). 5 business days = March 24 (Monday)
        result = calculate_prazo(date(2025, 3, 17), 5, 'úteis', set())
        assert result == date(2025, 3, 24)

    def test_across_weekend(self):
        # Start Friday. 1 business day = next Monday
        result = calculate_prazo(date(2025, 3, 14), 1, 'úteis', set())  # Friday
        assert result == date(2025, 3, 17)  # Monday

    def test_corridos(self):
        # 15 calendar days from March 17 = April 1
        result = calculate_prazo(date(2025, 3, 17), 15, 'corridos', set())
        assert result == date(2025, 4, 1)

    def test_corridos_ends_on_weekend_extends(self):
        # 10 calendar days from March 17 = March 27 (Thursday) — business day
        result = calculate_prazo(date(2025, 3, 17), 10, 'corridos', set())
        assert result == date(2025, 3, 27)

    def test_recesso_suspension(self):
        # Start Dec 15 (before recesso). 5 business days.
        # Dec 16 (Tue), 17 (Wed), 18 (Thu), 19 (Fri) = 4 days.
        # Dec 20 onwards = recesso. Resumes Jan 21.
        # Jan 21 (Wed) = 5th business day.
        result = calculate_prazo(date(2025, 12, 15), 5, 'úteis', set())
        assert result == date(2026, 1, 21)

    def test_suspended_range(self):
        # Suspend March 20-25
        suspended = [(date(2025, 3, 20), date(2025, 3, 25))]
        result = calculate_prazo(date(2025, 3, 17), 5, 'úteis', set(), suspended)
        # March 18 (1), 19 (2), skip 20-25, 26 (3), 27 (4), 28 (5)
        assert result == date(2025, 3, 28)


class TestGetStandardPrazo:
    def test_contestacao(self):
        p = get_standard_prazo('contestação')
        assert p is not None
        assert p['dias'] == 15
        assert p['unidade'] == 'úteis'

    def test_apelacao(self):
        p = get_standard_prazo('apelação')
        assert p is not None
        assert p['dias'] == 15

    def test_embargos(self):
        p = get_standard_prazo('embargos_declaração')
        assert p is not None
        assert p['dias'] == 5

    def test_unknown(self):
        assert get_standard_prazo('xyz_inexistente') is None

    # Phase A.1 — accent-insensitive matching
    def test_apelacao_unaccented(self):
        p = get_standard_prazo('apelacao')
        assert p is not None
        assert p['ato'] == 'apelação'
        assert p['dias'] == 15

    def test_contestacao_unaccented(self):
        p = get_standard_prazo('contestacao')
        assert p is not None
        assert p['ato'] == 'contestação'
        assert p['dias'] == 15

    def test_embargos_declaracao_unaccented(self):
        p = get_standard_prazo('embargos_declaracao')
        assert p is not None
        assert p['ato'] == 'embargos_declaração'
        assert p['dias'] == 5

    def test_recurso_especial_unaccented(self):
        p = get_standard_prazo('recurso_especial')
        assert p is not None
        assert 'recurso_especial' in _strip_accents(p['ato'])


class TestCheckPrazoStatus:
    def test_em_prazo(self):
        result = check_prazo_status(
            intimation_date=date(2025, 3, 17),
            prazo_type='contestação',
            current_date=date(2025, 3, 20),
        )
        assert result is not None
        assert result['status'] == 'em_prazo'
        assert result['dias_restantes'] is not None
        assert result['dias_restantes'] > 0

    def test_vencido(self):
        result = check_prazo_status(
            intimation_date=date(2025, 1, 6),
            prazo_type='contestação',
            current_date=date(2025, 3, 1),
        )
        assert result is not None
        assert result['status'] == 'vencido'
        assert result['dias_restantes'] is None


class TestProcessStateAware:
    """Phase 5 Step 5.2 — state-aware prazo calculation."""

    def test_ativo_behaves_as_before(self):
        result = check_prazo_status(
            intimation_date=date(2025, 3, 17),
            prazo_type='contestação',
            current_date=date(2025, 3, 20),
            process_state='ativo',
        )
        assert result is not None
        assert result['status'] == 'em_prazo'
        assert result['process_state'] == 'ativo'

    def test_transito_em_julgado_switches_to_cpc_523(self):
        result = check_prazo_status(
            intimation_date=date(2025, 3, 17),
            prazo_type='apelação',  # ignored
            current_date=date(2025, 3, 20),
            process_state='transito_em_julgado',
        )
        assert result is not None
        assert result['tipo'] == 'cumprimento voluntário'
        assert 'CPC art. 523' in result['fundamento_legal']
        assert result['dias'] == 15
        assert 'note' in result
        assert 'apelação' in result['note']

    def test_suspenso_returns_suspended_status(self):
        result = check_prazo_status(
            intimation_date=date(2025, 3, 17),
            prazo_type='contestação',
            current_date=date(2025, 3, 20),
            process_state='suspenso',
        )
        assert result is not None
        assert result['status'] == 'suspenso'
        assert 'suspenso' in result['fundamento_legal'].lower()

    def test_arquivado_returns_none(self):
        result = check_prazo_status(
            intimation_date=date(2025, 3, 17),
            prazo_type='contestação',
            current_date=date(2025, 3, 20),
            process_state='arquivado',
        )
        assert result is None

    def test_desconhecido_falls_through_to_normal(self):
        result = check_prazo_status(
            intimation_date=date(2025, 3, 17),
            prazo_type='contestação',
            current_date=date(2025, 3, 20),
            process_state='desconhecido',
        )
        assert result is not None
        assert result['status'] == 'em_prazo'

    def test_invalid_state_raises(self):
        import pytest as _pytest
        with _pytest.raises(ValueError):
            check_prazo_status(
                intimation_date=date(2025, 3, 17),
                prazo_type='contestação',
                current_date=date(2025, 3, 20),
                process_state='juridiquês',
            )

    def test_backwards_compat_no_process_state(self):
        """Calling without process_state must behave identically to before."""
        result = check_prazo_status(
            intimation_date=date(2025, 3, 17),
            prazo_type='contestação',
            current_date=date(2025, 3, 20),
        )
        assert result is not None
        assert 'process_state' not in result  # not added when param omitted


# Phase A.2 — --analysis batch mode warnings
import json as _json
import subprocess
import tempfile
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPT = REPO_ROOT / 'scripts' / 'prazo_calculator.py'


def _run_analysis(analyzed_path: Path, output_path: Path) -> subprocess.CompletedProcess:
    return subprocess.run(
        [sys.executable, str(SCRIPT), '--analysis', str(analyzed_path),
         '--output', str(output_path)],
        capture_output=True, text=True,
    )


class TestAnalysisBatchMode:
    def test_emits_prazos_for_valid_input(self, tmp_path):
        fixture = REPO_ROOT / 'tests' / 'fixtures' / 'sample_analyzed_with_prazos.json'
        out = tmp_path / 'prazos.json'
        r = _run_analysis(fixture, out)
        assert r.returncode == 0, r.stderr
        data = _json.loads(out.read_text(encoding='utf-8'))
        # Fixture has 3 valid entries (1 accented + 2 unaccented relying on A.1)
        assert len(data) == 3

    def test_accepts_unaccented_tipos(self, tmp_path):
        # apelacao + embargos_declaracao must be matched via _strip_accents (A.1)
        fixture = REPO_ROOT / 'tests' / 'fixtures' / 'sample_analyzed_with_prazos.json'
        out = tmp_path / 'prazos.json'
        r = _run_analysis(fixture, out)
        assert r.returncode == 0
        data = _json.loads(out.read_text(encoding='utf-8'))
        tipos = {p['tipo'] for p in data}
        # All three input tipos must be present in the output
        assert 'contestação' in tipos
        assert 'apelacao' in tipos
        assert 'embargos_declaracao' in tipos

    def test_warns_on_unknown_tipo(self, tmp_path):
        analyzed = tmp_path / 'analyzed.json'
        analyzed.write_text(_json.dumps({
            'chunks': [{
                'index': 0,
                'prazos': [
                    {'tipo': 'contestação', 'data_inicio': '10/03/2025'},
                    {'tipo': 'xpto_inexistente', 'data_inicio': '10/03/2025'},
                ],
            }],
        }), encoding='utf-8')
        out = tmp_path / 'prazos.json'
        r = _run_analysis(analyzed, out)
        assert r.returncode == 0
        assert 'WARN' in r.stderr
        assert 'xpto_inexistente' in r.stderr
        data = _json.loads(out.read_text(encoding='utf-8'))
        assert len(data) == 1  # only contestação survives

    def test_exits_nonzero_when_all_dropped(self, tmp_path):
        analyzed = tmp_path / 'analyzed.json'
        analyzed.write_text(_json.dumps({
            'chunks': [{
                'index': 0,
                'prazos': [
                    {'tipo': 'xpto_um', 'data_inicio': '10/03/2025'},
                    {'tipo': 'xpto_dois', 'data_inicio': '11/03/2025'},
                ],
            }],
        }), encoding='utf-8')
        out = tmp_path / 'prazos.json'
        r = _run_analysis(analyzed, out)
        assert r.returncode == 1
        assert 'WARN' in r.stderr

    def test_zero_prazos_no_drops_is_ok(self, tmp_path):
        analyzed = tmp_path / 'analyzed.json'
        analyzed.write_text(_json.dumps({
            'chunks': [{'index': 0, 'prazos': []}],
        }), encoding='utf-8')
        out = tmp_path / 'prazos.json'
        r = _run_analysis(analyzed, out)
        assert r.returncode == 0
        data = _json.loads(out.read_text(encoding='utf-8'))
        assert data == []

    def test_warns_on_missing_data_inicio(self, tmp_path):
        analyzed = tmp_path / 'analyzed.json'
        analyzed.write_text(_json.dumps({
            'chunks': [{
                'index': 0,
                'prazos': [
                    {'tipo': 'contestação'},  # no data_inicio
                    {'tipo': 'apelação', 'data_inicio': '10/03/2025'},
                ],
            }],
        }), encoding='utf-8')
        out = tmp_path / 'prazos.json'
        r = _run_analysis(analyzed, out)
        assert r.returncode == 0
        assert 'sem data_inicio' in r.stderr
