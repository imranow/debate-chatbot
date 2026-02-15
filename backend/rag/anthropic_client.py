from typing import Any

from backend.config import Settings


def make_anthropic(settings: Settings) -> Any:
    # Lazily imported so module import doesn't hard-fail when deps aren't installed yet.
    import anthropic  # type: ignore

    return anthropic.Anthropic(api_key=settings.anthropic_api_key)


def extract_text(message: Any) -> str:
    # anthropic.Message.content is a list of content blocks (TextBlock, etc.)
    blocks = getattr(message, "content", None) or []
    out = []
    for b in blocks:
        if getattr(b, "type", None) == "text":
            out.append(getattr(b, "text", "") or "")
    return "".join(out).strip()

