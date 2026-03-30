import hmac
import logging
import os

from fastapi import HTTPException, Security
from fastapi.security import APIKeyHeader

logger = logging.getLogger(__name__)

_api_key_header = APIKeyHeader(name="X-API-Key", auto_error=False)
_warned_no_api_key = False


async def require_api_key(
    api_key: str | None = Security(_api_key_header),
) -> str | None:
    """FastAPI dependency that enforces API key authentication.

    If the API_KEY env var is not set, authentication is skipped (dev mode).
    If set, the request must include a matching X-API-Key header.
    """
    global _warned_no_api_key
    expected = os.getenv("API_KEY")
    if not expected:
        if not _warned_no_api_key:
            logger.warning("API_KEY not set -- skipping auth (dev mode)")
            _warned_no_api_key = True
        return None
    if not api_key or not hmac.compare_digest(api_key, expected):
        raise HTTPException(status_code=401, detail="Invalid or missing API key")
    return api_key
