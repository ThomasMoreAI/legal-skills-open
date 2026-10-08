"""
filenames.py — Collision-safe filename generation for Obsidian vault export.

Solves the "Art. 1 CC" vs "Art. 1 CPC" collision problem by preserving
disambiguation context in filenames.
"""

from __future__ import annotations

import re
import unicodedata


def _normalize_unicode(text: str) -> str:
    """Normalize unicode characters, keeping accented chars as ASCII equivalents."""
    # Decompose unicode, strip combining marks (accents)
    nfkd = unicodedata.normalize('NFKD', text)
    return ''.join(c for c in nfkd if not unicodedata.combining(c))


def safe_filename(label: str, disambiguation: str | None = None, max_length: int = 100) -> str:
    """Generate a collision-safe filename from a label.

    Preserves enough context to avoid collisions like:
    - "Art. 1 CC" vs "Art. 1 CPC" -> "art-1-cc" vs "art-1-cpc"
    - "Sentença" vs "Sentença (embargos)" -> "sentenca" vs "sentenca-embargos"

    Args:
        label: The text to convert to a filename.
        disambiguation: Optional extra context appended to avoid collisions.
        max_length: Maximum filename length (without extension).

    Returns:
        A lowercase, hyphenated, ASCII-safe filename.
    """
    # Normalize unicode
    name = _normalize_unicode(label)

    # Add disambiguation context
    if disambiguation:
        name = f"{name}-{_normalize_unicode(disambiguation)}"

    # Lowercase
    name = name.lower()

    # Replace unsafe chars with hyphens
    name = re.sub(r'[<>:"/\\|?*§°º°ª]', '', name)
    name = re.sub(r'[^a-z0-9]+', '-', name)

    # Clean up multiple hyphens and trim
    name = re.sub(r'-+', '-', name)
    name = name.strip('-')

    # Truncate without breaking words
    if len(name) > max_length:
        truncated = name[:max_length]
        # Don't cut in the middle of a word
        last_hyphen = truncated.rfind('-')
        if last_hyphen > max_length * 0.6:
            truncated = truncated[:last_hyphen]
        name = truncated.rstrip('-')

    return name or 'unnamed'


class FilenameRegistry:
    """Tracks generated filenames and resolves collisions with numeric suffixes."""

    def __init__(self) -> None:
        self._used: dict[str, int] = {}

    def get(self, label: str, disambiguation: str | None = None) -> str:
        """Get a unique filename, appending -2, -3 etc. on collision."""
        base = safe_filename(label, disambiguation)

        if base not in self._used:
            self._used[base] = 1
            return base

        self._used[base] += 1
        unique = f"{base}-{self._used[base]}"
        return unique

    def reset(self) -> None:
        """Clear the registry."""
        self._used.clear()
