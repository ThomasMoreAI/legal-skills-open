#!/usr/bin/env python3
# ruff: noqa: E501 -- shared inline CSS and JavaScript literals stay readable.
"""Shared portable brand primitives for DocReview lawyer-facing HTML.

The generated pages stay self-contained. This module is used only while
rendering and introduces no browser runtime or network dependency.
"""

from __future__ import annotations

import posixpath
import urllib.parse

CONTRACT_ID = "lq-lawyer-review-v1"

BRAND_CSS = r"""
:root {
  color-scheme: light dark;
  --lq-background: #f4f1ea;
  --lq-surface: #ffffff;
  --lq-surface-muted: #faf8f3;
  --lq-foreground: #24211d;
  --lq-muted-foreground: #686159;
  --lq-border: #ded8cd;
  --lq-primary: #173c34;
  --lq-primary-foreground: #ffffff;
  --lq-accent: #dcebe5;
  --lq-accent-foreground: #173c34;
  --lq-success: #33613c;
  --lq-success-surface: #e6efe4;
  --lq-attention: #684813;
  --lq-attention-surface: #fff1d5;
  --lq-destructive: #7a3028;
  --lq-destructive-surface: #f6e7e4;
  --lq-ring: #173c34;
  --lq-font-sans: ui-sans-serif, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  --lq-font-serif: "Century Schoolbook", "Iowan Old Style", Palatino, Georgia, serif;
  --lq-font-mono: ui-monospace, "SF Mono", Menlo, Consolas, monospace;
}
@media (prefers-color-scheme: dark) {
  :root {
    --lq-background: #151718;
    --lq-surface: #202325;
    --lq-surface-muted: #292d2f;
    --lq-foreground: #f4f1ea;
    --lq-muted-foreground: #bbb5ac;
    --lq-border: #44494c;
    --lq-primary: #d2eee5;
    --lq-primary-foreground: #17312b;
    --lq-accent: #233a33;
    --lq-accent-foreground: #d2eee5;
    --lq-success: #a3c8a0;
    --lq-success-surface: #242e1f;
    --lq-attention: #ffe3a3;
    --lq-attention-surface: #3b3020;
    --lq-destructive: #ffc4bc;
    --lq-destructive-surface: #392725;
    --lq-ring: #d2eee5;
  }
}
html[data-theme="light"] {
  --lq-background: #f4f1ea;
  --lq-surface: #ffffff;
  --lq-surface-muted: #faf8f3;
  --lq-foreground: #24211d;
  --lq-muted-foreground: #686159;
  --lq-border: #ded8cd;
  --lq-primary: #173c34;
  --lq-primary-foreground: #ffffff;
  --lq-accent: #dcebe5;
  --lq-accent-foreground: #173c34;
  --lq-success: #33613c;
  --lq-success-surface: #e6efe4;
  --lq-attention: #684813;
  --lq-attention-surface: #fff1d5;
  --lq-destructive: #7a3028;
  --lq-destructive-surface: #f6e7e4;
  --lq-ring: #173c34;
}
html[data-theme="dark"] {
  --lq-background: #151718;
  --lq-surface: #202325;
  --lq-surface-muted: #292d2f;
  --lq-foreground: #f4f1ea;
  --lq-muted-foreground: #bbb5ac;
  --lq-border: #44494c;
  --lq-primary: #d2eee5;
  --lq-primary-foreground: #17312b;
  --lq-accent: #233a33;
  --lq-accent-foreground: #d2eee5;
  --lq-success: #a3c8a0;
  --lq-success-surface: #242e1f;
  --lq-attention: #ffe3a3;
  --lq-attention-surface: #3b3020;
  --lq-destructive: #ffc4bc;
  --lq-destructive-surface: #392725;
  --lq-ring: #d2eee5;
}
strong,b,h1,h2,h3,h4,h5,h6 { font-weight: 500; }
.lq-masthead {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 14px;
  padding: 12px 24px;
  background: var(--lq-surface);
  color: var(--lq-foreground);
  border-bottom: 1px solid var(--lq-border);
  font-family: var(--lq-font-sans);
}
.lq-brand { font-weight: 500; letter-spacing: .01em; }
.lq-context { display: flex; align-items: center; justify-content: flex-end; gap: 12px; color: var(--lq-muted-foreground); }
.lq-theme-toggle {
  appearance: none;
  border: 1px solid var(--lq-border);
  border-radius: 4px;
  background: var(--lq-surface-muted);
  color: var(--lq-foreground);
  padding: 6px 9px;
  font: 400 13px var(--lq-font-sans);
  cursor: pointer;
}
.lq-theme-toggle:focus-visible { outline: 2px solid var(--lq-ring); outline-offset: 2px; }
@media (max-width: 640px) {
  .lq-masthead { align-items: flex-start; flex-direction: column; padding: 10px 14px; }
  .lq-context { width: 100%; justify-content: space-between; }
}
@media (prefers-reduced-motion: reduce) {
  * { scroll-behavior: auto !important; transition-duration: .01ms !important; animation-duration: .01ms !important; }
}
"""

THEME_BUTTON = (
    '<button class="lq-theme-toggle" id="theme-toggle" type="button" '
    'aria-pressed="false">Use dark theme</button>'
)

THEME_JS = r"""
const themeToggle=document.getElementById('theme-toggle');
function systemTheme(){return window.matchMedia&&window.matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light'}
function activeTheme(){return document.documentElement.dataset.theme||systemTheme()}
function syncThemeButton(){const dark=activeTheme()==='dark';themeToggle.textContent=dark?'Use light theme':'Use dark theme';themeToggle.setAttribute('aria-pressed',String(dark))}
themeToggle.addEventListener('click',()=>{document.documentElement.dataset.theme=activeTheme()==='dark'?'light':'dark';syncThemeButton()});
syncThemeButton();
"""


def safe_source_path(value: str) -> str:
    """Return a normalized manifest path or refuse an unsafe source path."""

    if not isinstance(value, str) or not value or "\\" in value:
        raise ValueError(f"unsafe source path: {value!r}")
    normalized = posixpath.normpath(value)
    if (
        value.startswith("/")
        or normalized in {".", ".."}
        or normalized.startswith("../")
        or ":" in normalized.split("/", 1)[0]
    ):
        raise ValueError(f"unsafe source path: {value!r}")
    return normalized


def safe_source_prefix(value: str | None) -> str:
    """Return a normalized relative source prefix or refuse absolute/URL input."""

    if value in {None, ""}:
        return ""
    if not isinstance(value, str) or "\\" in value:
        raise ValueError(f"unsafe source prefix: {value!r}")
    normalized = posixpath.normpath(value)
    if (
        value.startswith("/")
        or normalized in {".", ".."}
        or normalized.startswith("../")
        or ":" in normalized.split("/", 1)[0]
    ):
        raise ValueError(f"unsafe source prefix: {value!r}")
    return normalized


def source_href(
    prefix: str | None, path: str, *, link_without_prefix: bool
) -> str | None:
    """Build a percent-encoded relative href after validating both components."""

    safe_path = safe_source_path(path)
    safe_prefix = safe_source_prefix(prefix)
    if not safe_prefix and not link_without_prefix:
        return None
    joined = posixpath.join(safe_prefix, safe_path) if safe_prefix else safe_path
    return urllib.parse.quote(joined, safe="/")


def masthead(context: str) -> str:
    """Return shared masthead markup; caller must HTML-escape context."""

    return (
        '<div class="lq-masthead" role="banner">'
        '<div class="lq-brand">LQ · Document Review</div>'
        f'<div class="lq-context"><span>{context}</span>{THEME_BUTTON}</div></div>'
    )
