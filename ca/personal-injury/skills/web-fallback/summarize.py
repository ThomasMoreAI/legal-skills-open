"""
Constrained summarization of a verified statute fetch.

Hard rules:
- Input MUST be the dict returned by verify.verify() with verified=True.
- The model is told to summarize ONLY the supplied text.
- The model is told to NOT add facts, NOT cite other sections, NOT speculate.
- If verify failed, this returns None — never invents.

The summary is one sentence in Specter's voice. Specter (the agent) is then
free to format that for WhatsApp with the URL/citation.

Costs an Anthropic call per invocation. Skip this if you're happy showing
the user the raw cropped statute text from verify().
"""
from __future__ import annotations

import os
from typing import Any, Optional

from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()

_MODEL = os.getenv("ANTHROPIC_MODEL", "claude-haiku-4-5")
_MAX_INPUT_CHARS = 6000  # crop fed text just to be safe; verify already crops to 8000


SYSTEM = """You are summarizing a single state statute that has just been fetched live from an authoritative legislature website.

Hard rules:
- Use ONLY the statute text supplied below. Do NOT add facts from your training.
- Do NOT cite or reference any other section.
- Do NOT speculate about case law, penalties, or interpretation unless it is explicitly stated in the supplied text.
- If the supplied text is unclear or off-topic, output the literal string: NO_SUMMARY
- Output one sentence, plain prose. No markdown, no quotes around the whole thing, no preamble.
- Tone is direct and professional. No filler."""


def _user_prompt(citation: str, text: str) -> str:
    return (
        f"Citation: {citation}\n\n"
        f"Statute text (verbatim from authoritative source):\n"
        f'"""\n{text[:_MAX_INPUT_CHARS]}\n"""\n\n'
        f"Summarize in one sentence."
    )


def summarize_verified(result: dict[str, Any]) -> Optional[str]:
    """
    Summarize a verified statute fetch.

    Returns a one-sentence string, or None if:
      - the result is not a verified fetch,
      - the model emitted NO_SUMMARY,
      - or the API call failed.

    Never returns a fabricated summary. On any uncertainty, returns None
    so the caller can fall back to "no verified source" handling.
    """
    if not isinstance(result, dict) or not result.get("verified"):
        return None
    citation = result.get("citation")
    text = result.get("text")
    if not citation or not text:
        return None

    try:
        client = Anthropic()
        msg = client.messages.create(
            model=_MODEL,
            max_tokens=180,
            system=SYSTEM,
            messages=[{"role": "user", "content": _user_prompt(citation, text)}],
        )
        out = (msg.content[0].text or "").strip()
    except Exception:
        return None

    if not out or out.upper().startswith("NO_SUMMARY"):
        return None

    # Trim quotes if the model wrapped its output, despite instructions.
    if (out.startswith('"') and out.endswith('"')) or (out.startswith("'") and out.endswith("'")):
        out = out[1:-1].strip()
    return out or None


# CLI:
#   python -m openclaw.skills.web_fallback.summarize "Cal. Veh. Code § 22350"
if __name__ == "__main__":
    import json
    import sys

    if len(sys.argv) < 2:
        print("usage: python -m openclaw.skills.web_fallback.summarize '<citation>'", file=sys.stderr)
        sys.exit(2)
    from openclaw.skills.web_fallback.verify import verify
    res = verify(" ".join(sys.argv[1:]))
    if not res.get("verified"):
        print(json.dumps({"summary": None, "verify": res}, indent=2))
        sys.exit(0)
    summary = summarize_verified(res)
    print(json.dumps({
        "citation": res["citation"],
        "url": res["url"],
        "summary": summary,
    }, indent=2))
