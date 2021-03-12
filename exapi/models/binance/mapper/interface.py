"""Has binance models mapper interface."""

from exapi.models.binance.mapper.market_data.interface import \
    IBinanceMarketDataModelsMapper
from exapi.models.binance.mapper.trading.interface import \
    IBinanceTradingModelsMapper


class IBinanceModelsMapper(IBinanceMarketDataModelsMapper, IBinanceTradingModelsMapper):
    """Binance models mapper interface.

    Maps json to models.
    """
