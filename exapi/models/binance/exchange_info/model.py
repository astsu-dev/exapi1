"""Has binance exchange info model."""

from dataclasses import dataclass
from typing import TypedDict

from exapi.models.binance.exchange_info.filters.exchange import (BinanceExchangeFilters,
                               BinanceExchangeFiltersJson)
from exapi.models.binance.exchange_info.rate_limits import BinanceRateLimits, BinanceRateLimitsJson
from exapi.models.binance.exchange_info.symbol import BinanceSymbols, BinanceSymbolsJson


class BinanceExchangeInfoJson(TypedDict):
    timezone: str
    serverTime: int
    rateLimits: BinanceRateLimitsJson
    exchangeFilters: BinanceExchangeFiltersJson
    symbols: BinanceSymbolsJson


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
    server_time: int
    rate_limits: BinanceRateLimits
    exchange_filters: BinanceExchangeFilters
    symbols: BinanceSymbols
