"""Common interface and utilities for statute fetchers."""

import hashlib
import json
import os
import time
from pathlib import Path
from typing import Dict, Optional, Any


def get_cache_dir() -> Path:
    """Get the cache directory, creating it if needed."""
    cache_dir = Path.home() / ".xref" / "cache"
    cache_dir.mkdir(parents=True, exist_ok=True)
    return cache_dir


def get_cache_key(citation_type: str, **params) -> str:
    """Generate a cache key from citation parameters."""
    key_parts = [citation_type] + [f"{k}={v}" for k, v in sorted(params.items())]
    key_str = "|".join(key_parts)
    return hashlib.sha256(key_str.encode()).hexdigest()


def get_cached(cache_key: str) -> Optional[Dict[str, Any]]:
    """Retrieve cached statute if it exists and isn't stale."""
    cache_dir = get_cache_dir()
    cache_file = cache_dir / f"{cache_key}.json"
    
    if not cache_file.exists():
        return None
    
    # Cache for 30 days
    if time.time() - cache_file.stat().st_mtime > 30 * 86400:
        return None
    
    try:
        with open(cache_file, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return None


def set_cached(cache_key: str, data: Dict[str, Any]) -> None:
    """Store statute in cache."""
    cache_dir = get_cache_dir()
    cache_file = cache_dir / f"{cache_key}.json"
    
    try:
        with open(cache_file, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
    except IOError:
        pass


class FetchError(Exception):
    """Raised when a fetch fails."""
    pass
