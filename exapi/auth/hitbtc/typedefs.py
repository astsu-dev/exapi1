"""Has type definitions for hitbtc auth."""

from typing import TypedDict


class HitbtcAuthHeaders(TypedDict):
    """Headers with Authorization header."""

    Authorization: str
