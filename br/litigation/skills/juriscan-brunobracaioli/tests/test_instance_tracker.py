"""Tests for scripts/instance_tracker.py"""

import sys
import os

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'scripts'))
from instance_tracker import (
    classify_instance,
    build_instance_flow,
    build_argument_tracks,
    generate_instance_report,
)


class TestClassifyInstance:
    def test_peticao_inicial(self):
        assert classify_instance({'label': 'PETIÇÃO INICIAL'}) == '1a_instancia'

    def test_sentenca(self):
        assert classify_instance({'label': 'SENTENÇA'}) == '1a_instancia'

    def test_recurso_especial(self):
        assert classify_instance({'label': 'RECURSO ESPECIAL'}) == 'stj'

    def test_recurso_extraordinario(self):
        assert classify_instance({'label': 'RECURSO EXTRAORDINÁRIO'}) == 'stf'

    def test_acordao_tj_from_text(self):
        chunk = {
            'label': 'ACÓRDÃO',
            'text': 'TRIBUNAL DE JUSTIÇA DO ESTADO DE SÃO PAULO. Des. Ricardo Souza Oliveira. 5ª Câmara de Direito Privado.',
        }
        assert classify_instance(chunk) == 'tj'

    def test_acordao_stj_from_text(self):
        chunk = {
            'label': 'ACÓRDÃO',
            'text': 'SUPERIOR TRIBUNAL DE JUSTIÇA. Min. Nancy Andrighi. Terceira Turma.',
        }
        assert classify_instance(chunk) == 'stj'

    def test_apelacao_from_vara(self):
        chunk = {
            'label': 'APELAÇÃO',
            'text': '',
            'partes': {'vara': '5ª Câmara de Direito Privado — TJSP'},
        }
        assert classify_instance(chunk) == 'tj'

    def test_default_1a_instancia(self):
        chunk = {'label': 'CERTIDÃO', 'text': ''}
        assert classify_instance(chunk) == '1a_instancia'


class TestBuildInstanceFlow:
    def test_groups_by_instance(self):
        chunks = [
            {'index': 0, 'label': 'PETIÇÃO INICIAL', 'primary_date': '05/02/2025', 'resumo': 'PI'},
            {'index': 1, 'label': 'SENTENÇA', 'primary_date': '01/07/2025', 'resumo': 'Sent', 'decisao': 'JULGO PARCIALMENTE PROCEDENTE'},
            {'index': 2, 'label': 'ACÓRDÃO', 'text': 'TRIBUNAL DE JUSTIÇA. Des. X. Câmara.', 'primary_date': '15/10/2025', 'resumo': 'Ac', 'decisao': 'NEGO PROVIMENTO'},
        ]
        flow = build_instance_flow(chunks)
        assert '1a_instancia' in flow
        assert 'tj' in flow
        assert len(flow['1a_instancia']['pieces']) == 2
        assert len(flow['tj']['pieces']) == 1

    def test_extracts_resultado(self):
        chunks = [
            {'index': 0, 'label': 'SENTENÇA', 'decisao': 'JULGO PARCIALMENTE PROCEDENTE a ação'},
        ]
        flow = build_instance_flow(chunks)
        assert flow['1a_instancia']['resultado'] == 'parcialmente_procedente'

    def test_recurso_desprovido(self):
        chunks = [
            {'index': 0, 'label': 'ACÓRDÃO', 'text': 'Des. X. Câmara Cível.', 'decisao': 'NEGO PROVIMENTO ao recurso'},
        ]
        flow = build_instance_flow(chunks)
        assert flow['tj']['resultado'] == 'recurso_desprovido'


class TestBuildArgumentTracks:
    def test_tracks_arguments(self):
        chunks = [
            {
                'index': 0, 'label': 'PETIÇÃO INICIAL',
                'argumentos_chave': ['Responsabilidade objetiva', 'Dano moral in re ipsa'],
            },
            {
                'index': 1, 'label': 'CONTESTAÇÃO',
                'argumentos_chave': ['Fortuito externo'],
            },
        ]
        tracks = build_argument_tracks(chunks)
        assert len(tracks) == 3

    def test_same_argument_multiple_pieces(self):
        chunks = [
            {'index': 0, 'label': 'PETIÇÃO INICIAL', 'argumentos_chave': ['Súmula 479 STJ']},
            {'index': 1, 'label': 'RÉPLICA', 'argumentos_chave': ['Súmula 479 STJ']},
        ]
        tracks = build_argument_tracks(chunks)
        # Both should be grouped (same normalized text)
        sumula_track = [t for t in tracks if 'súmula 479' in t['argumento'].lower()]
        assert len(sumula_track) == 1
        assert len(sumula_track[0]['aparicoes']) == 2


class TestGenerateInstanceReport:
    def test_full_report(self, sample_analyzed):
        report = generate_instance_report(sample_analyzed)
        assert 'instances' in report
        assert 'argument_tracks' in report
        assert len(report['argument_tracks']) > 0
