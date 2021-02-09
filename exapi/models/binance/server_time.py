"""Has binance server time model."""

from dataclasses import dataclass
from typing import TypedDict


class BinanceServerTimeJson(TypedDict):
    """Server time json."""

    serverTime: int


@dataclass(frozen=True)
class BinanceServerTimeModel:
    """Server time model."""

    server_time: int
