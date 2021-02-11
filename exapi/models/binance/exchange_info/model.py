"""Has binance exchange info model."""

from dataclasses import dataclass
from typing import TypedDict

from .filters.exchange import (BinanceExchangeFilters,
                               BinanceExchangeFiltersJson)
from .rate_limits import BinanceRateLimits, BinanceRateLimitsJson
from .symbol import BinanceSymbols


class BinanceExchangeInfoJson(TypedDict):
    timezone: str
    serverTime: int
    rateLimits: BinanceRateLimitsJson
    exchangeFilters: BinanceExchangeFiltersJson
    symbols: BinanceSymbols


@dataclass(frozen=True)
class BinanceExchangeInfoModel:
    """Binance exchange info model.

    Args:
        timezone (str)
        serverTime (int)
        rateLimits (BinanceRateLimits)
        exchangeFilters (BinanceExchangeFilters)
        symbols (BinanceSymbols)
    """

    timezone: str
    serverTime: int
    rateLimits: BinanceRateLimits
    exchangeFilters: BinanceExchangeFilters
    symbols: BinanceSymbols
