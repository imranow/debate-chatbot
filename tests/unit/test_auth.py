"""Unit tests for require_api_key auth dependency."""

import pytest
from unittest.mock import patch

from fastapi import HTTPException

import backend.rag.auth as auth_module
from backend.rag.auth import require_api_key


@pytest.fixture(autouse=True)
def reset_warned_flag():
    """Reset the module-level warn-once flag between tests."""
    auth_module._warned_no_api_key = False
    yield
    auth_module._warned_no_api_key = False


@pytest.mark.asyncio
async def test_dev_mode_no_api_key_set_allows_request():
    """When API_KEY env var is not set, auth is skipped and None is returned."""
    with patch.dict("os.environ", {}, clear=True):
        # Ensure API_KEY is absent
        import os
        os.environ.pop("API_KEY", None)
        result = await require_api_key(api_key=None)
    assert result is None


@pytest.mark.asyncio
async def test_dev_mode_warns_only_once(caplog):
    """Dev mode warning is logged exactly once across multiple calls."""
    import logging
    with patch.dict("os.environ", {}, clear=True):
        import os
        os.environ.pop("API_KEY", None)
        with caplog.at_level(logging.WARNING, logger="backend.rag.auth"):
            await require_api_key(api_key=None)
            await require_api_key(api_key=None)
    warning_messages = [r for r in caplog.records if "API_KEY not set" in r.message]
    assert len(warning_messages) == 1


@pytest.mark.asyncio
async def test_valid_api_key_accepted():
    """A correct X-API-Key header is accepted and returned."""
    with patch.dict("os.environ", {"API_KEY": "secret-key-123"}):
        result = await require_api_key(api_key="secret-key-123")
    assert result == "secret-key-123"


@pytest.mark.asyncio
async def test_wrong_api_key_raises_401():
    """An incorrect API key raises HTTPException with status 401."""
    with patch.dict("os.environ", {"API_KEY": "secret-key-123"}):
        with pytest.raises(HTTPException) as exc_info:
            await require_api_key(api_key="wrong-key")
    assert exc_info.value.status_code == 401


@pytest.mark.asyncio
async def test_missing_api_key_header_raises_401():
    """A missing X-API-Key header (None) raises HTTPException with status 401."""
    with patch.dict("os.environ", {"API_KEY": "secret-key-123"}):
        with pytest.raises(HTTPException) as exc_info:
            await require_api_key(api_key=None)
    assert exc_info.value.status_code == 401


@pytest.mark.asyncio
async def test_empty_string_api_key_raises_401():
    """An empty string API key raises HTTPException with status 401."""
    with patch.dict("os.environ", {"API_KEY": "secret-key-123"}):
        with pytest.raises(HTTPException) as exc_info:
            await require_api_key(api_key="")
    assert exc_info.value.status_code == 401
