"""Unit tests for stocks.catalysts with a mocked Anthropic client (no network)."""

import json
from contextlib import contextmanager
from types import SimpleNamespace

import pytest

from stocks import catalysts
from stocks.catalysts import (
    THEMES, ThemeResult, cross_reference, extract_candidates, render_markdown, run_scan, scan_theme,
)


def _text(t, urls=()):
    return SimpleNamespace(type="text", text=t, citations=[SimpleNamespace(url=u) for u in urls])


def _search(urls):
    return SimpleNamespace(type="web_search_tool_result",
                           content=[SimpleNamespace(url=u) for u in urls])


def _msg(blocks, stop_reason="end_turn", stop_details=None):
    return SimpleNamespace(content=blocks, stop_reason=stop_reason, stop_details=stop_details,
                           usage=SimpleNamespace(input_tokens=100, output_tokens=50))


class FakeClient:
    """Returns queued messages from beta.messages.stream and records the calls."""

    def __init__(self, messages):
        self.queue = list(messages)
        self.calls = []
        self.beta = SimpleNamespace(messages=SimpleNamespace(stream=self._stream))

    @contextmanager
    def _stream(self, **kwargs):
        self.calls.append(kwargs)
        msg = self.queue.pop(0)
        yield SimpleNamespace(get_final_message=lambda: msg)


GOOD = """Summary paragraph.

| Ticker | Thesis |
|---|---|
| SIMO | controllers |

```json
[{"ticker": "simo", "name": "Silicon Motion", "thesis": "NAND controllers", "confidence": "high",
  "evidence_url": "https://example.com/simo"},
 {"ticker": "HPS.A", "name": "Hammond", "thesis": "transformers", "confidence": "medium"},
 {"name": "no ticker, dropped"}]
```"""


def test_extract_candidates_parses_last_json_block_and_normalises():
    prose, cands = extract_candidates(GOOD)
    assert "Summary paragraph" in prose and "```json" not in prose
    assert [c["ticker"] for c in cands] == ["SIMO", "HPS.A"]


def test_extract_candidates_tolerates_missing_or_bad_json():
    assert extract_candidates("just prose") == ("just prose", [])
    prose, cands = extract_candidates("text\n```json\n{not json\n```")
    assert cands == [] and prose == "text"
    _, cands = extract_candidates('```json\n{"candidates": [{"ticker": "aapl"}]}\n```')
    assert cands[0]["ticker"] == "AAPL"


def test_scan_theme_collects_text_sources_and_request_shape():
    client = FakeClient([_msg([_search(["https://a.com", "https://b.com"]), _text(GOOD, ["https://a.com"])])])
    r = scan_theme(client, THEMES[0], model="claude-opus-5")
    assert r.key == "sold_out" and r.stop_reason == "end_turn" and r.error is None
    assert [c["ticker"] for c in r.candidates] == ["SIMO", "HPS.A"]
    assert all(c["theme"] == "sold_out" for c in r.candidates)
    assert r.sources == ["https://a.com", "https://b.com"]
    assert r.usage == {"input_tokens": 100, "output_tokens": 50}
    call = client.calls[0]
    assert call["model"] == "claude-opus-5"
    assert call["tools"][0]["type"] == "web_search_20260209"
    assert call["fallbacks"] == "default" and "server-side-fallback-2026-07-01" in call["betas"]
    assert call["messages"][0]["role"] == "user"
    assert call["system"][0]["cache_control"] == {"type": "ephemeral"}


def test_scan_theme_resumes_on_pause_turn():
    paused = _msg([_search(["https://x.com"]), _text("partial")], stop_reason="pause_turn")
    final = _msg([_text(GOOD)])
    client = FakeClient([paused, final])
    r = scan_theme(client, THEMES[1])
    assert len(client.calls) == 2
    # Second request carries the paused assistant turn, with no extra user message.
    msgs = client.calls[1]["messages"]
    assert [m["role"] for m in msgs] == ["user", "assistant"]
    assert msgs[1]["content"] is paused.content
    assert "partial" in r.text and [c["ticker"] for c in r.candidates] == ["SIMO", "HPS.A"]
    assert r.usage["input_tokens"] == 200


def test_scan_theme_gives_up_after_max_continuations(monkeypatch):
    monkeypatch.setattr(catalysts, "MAX_CONTINUATIONS", 1)
    client = FakeClient([_msg([_text("a")], "pause_turn"), _msg([_text("b")], "pause_turn")])
    r = scan_theme(client, THEMES[0])
    assert len(client.calls) == 2 and r.stop_reason == "pause_turn"


def test_scan_theme_reports_refusal():
    client = FakeClient([_msg([], "refusal", SimpleNamespace(category="x", explanation="nope"))])
    r = scan_theme(client, THEMES[0])
    assert r.error == "model declined: nope" and r.candidates == []


def test_cross_reference_flags_screen_status(tmp_path):
    screen = tmp_path / "latest.json"
    screen.write_text(json.dumps({"leaderboard_symbols": ["SIMO", "MU"], "breakout_symbols": ["SIMO"]}))
    cands = [{"ticker": "SIMO"}, {"ticker": "MU"}, {"ticker": "HPS.A"}]
    cross_reference(cands, screen)
    assert cands[0]["screen_status"] == "on breakout watchlist, in Top 100"
    assert cands[1]["screen_status"] == "in Top 100"
    assert cands[2]["screen_status"] == "not yet moving in screen"
    cross_reference([{"ticker": "X"}], tmp_path / "missing.json")  # no-op


def test_render_markdown_orders_by_confidence_and_shows_errors():
    ok = ThemeResult("a", "Theme A", "prose A", [
        {"ticker": "LOW", "confidence": "low", "thesis": "l"},
        {"ticker": "HI", "confidence": "high", "thesis": "h|x", "evidence_url": "https://e.com"},
    ], ["https://s.com"], "end_turn", usage={"input_tokens": 1, "output_tokens": 2})
    bad = ThemeResult("b", "Theme B", "", [], [], "error", error="boom")
    md = render_markdown([ok, bad], "2026-09-06", "claude-opus-5")
    assert md.index("| HI ") < md.index("| LOW ")
    assert "h/x ([source](https://e.com))" in md
    assert "_Scan failed: boom_" in md and "- https://s.com" in md
    assert "Tokens: 1 in / 2 out" in md


def test_run_scan_writes_reports_and_survives_theme_failure(tmp_path):
    class Flaky(FakeClient):
        @contextmanager
        def _stream(self, **kwargs):
            self.calls.append(kwargs)
            if len(self.calls) == 2:
                raise RuntimeError("network down")
            yield SimpleNamespace(get_final_message=lambda: self.queue.pop(0))

    (tmp_path / "latest.json").write_text(json.dumps({"leaderboard_symbols": ["SIMO"], "breakout_symbols": []}))
    client = Flaky([_msg([_text(GOOD)]), _msg([_text("nothing found")])])
    latest, dated = run_scan(tmp_path, client=client, theme_keys=["sold_out", "second_tier", "price_hikes"])
    assert latest.exists() and dated.name.endswith(".md") and len(client.calls) == 3
    payload = json.loads((tmp_path / "catalysts" / "latest.json").read_text())
    assert [c["ticker"] for c in payload["candidates"]] == ["SIMO", "HPS.A"]
    assert payload["candidates"][0]["screen_status"] == "in Top 100"
    assert "second_tier" in payload["errors"] and "network down" in payload["errors"]["second_tier"]
    text = latest.read_text()
    assert "## All candidates" in text and "_Scan failed: network down_" in text
