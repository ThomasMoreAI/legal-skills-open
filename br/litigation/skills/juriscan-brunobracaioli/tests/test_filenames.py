"""Tests for scripts/utils/filenames.py"""

import sys
import os

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'scripts'))
from utils.filenames import safe_filename, FilenameRegistry


class TestSafeFilename:
    def test_simple(self):
        assert safe_filename('PETIÇÃO INICIAL') == 'peticao-inicial'

    def test_accents_removed(self):
        assert safe_filename('CONTESTAÇÃO') == 'contestacao'
        assert safe_filename('RÉPLICA') == 'replica'
        assert safe_filename('ACÓRDÃO') == 'acordao'

    def test_special_chars_removed(self):
        assert safe_filename('Art. 14 do CDC') == 'art-14-do-cdc'

    def test_disambiguation(self):
        a = safe_filename('Art. 1', disambiguation='CC Lei 10.406/2002')
        b = safe_filename('Art. 1', disambiguation='CPC Lei 13.105/2015')
        assert a != b
        assert 'cc' in a
        assert 'cpc' in b

    def test_max_length(self):
        long_label = 'A' * 200
        result = safe_filename(long_label, max_length=50)
        assert len(result) <= 50

    def test_empty_string(self):
        assert safe_filename('') == 'unnamed'

    def test_only_special_chars(self):
        assert safe_filename('§§§°°°') == 'unnamed'

    def test_unicode(self):
        assert safe_filename('Súmula 479') == 'sumula-479'

    def test_no_leading_trailing_hyphens(self):
        result = safe_filename(' - SENTENÇA - ')
        assert not result.startswith('-')
        assert not result.endswith('-')


class TestFilenameRegistry:
    def test_no_collision(self):
        reg = FilenameRegistry()
        assert reg.get('PETIÇÃO INICIAL') == 'peticao-inicial'
        assert reg.get('CONTESTAÇÃO') == 'contestacao'

    def test_collision_adds_suffix(self):
        reg = FilenameRegistry()
        assert reg.get('DESPACHO') == 'despacho'
        assert reg.get('DESPACHO') == 'despacho-2'
        assert reg.get('DESPACHO') == 'despacho-3'

    def test_reset(self):
        reg = FilenameRegistry()
        reg.get('SENTENÇA')
        reg.reset()
        assert reg.get('SENTENÇA') == 'sentenca'  # No suffix after reset
