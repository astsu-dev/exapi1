"""Has binance ping model."""

from dataclasses import dataclass
from typing import TypedDict


class BinancePingJson(TypedDict):
    """Ping json."""


@dataclass(frozen=True)
class BinancePingModel:
    """Ping model."""
