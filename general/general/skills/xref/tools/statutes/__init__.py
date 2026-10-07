"""Fetcher interface for statute modules."""

from .cache import get_cache_key, get_cached, set_cached, FetchError
from .us_code import fetch_us_code
from .cfr import fetch_cfr
from .uk_legislation import fetch_uk_legislation
from .eu_regulations import fetch_eu_regulation

__all__ = [
    'get_cache_key',
    'get_cached', 
    'set_cached',
    'FetchError',
    'fetch_us_code',
    'fetch_cfr',
    'fetch_uk_legislation',
    'fetch_eu_regulation',
]
