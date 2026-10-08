"""Shared test fixtures for juriscan."""

import json
import os
import sys

import pytest

# Add scripts to path
SCRIPTS_DIR = os.path.join(os.path.dirname(__file__), '..', 'scripts')
sys.path.insert(0, SCRIPTS_DIR)

FIXTURES_DIR = os.path.join(os.path.dirname(__file__), 'fixtures')


@pytest.fixture
def fixtures_dir():
    return FIXTURES_DIR


@pytest.fixture
def sample_index():
    with open(os.path.join(FIXTURES_DIR, 'sample_index.json'), 'r', encoding='utf-8') as f:
        return json.load(f)


@pytest.fixture
def sample_analyzed():
    with open(os.path.join(FIXTURES_DIR, 'sample_analyzed.json'), 'r', encoding='utf-8') as f:
        return json.load(f)


@pytest.fixture
def sample_peticao_text():
    with open(os.path.join(FIXTURES_DIR, 'sample_chunk_peticao.txt'), 'r', encoding='utf-8') as f:
        return f.read()


@pytest.fixture
def sample_sentenca_text():
    with open(os.path.join(FIXTURES_DIR, 'sample_chunk_sentenca.txt'), 'r', encoding='utf-8') as f:
        return f.read()


@pytest.fixture
def sample_acordao_text():
    with open(os.path.join(FIXTURES_DIR, 'sample_chunk_acordao.txt'), 'r', encoding='utf-8') as f:
        return f.read()
