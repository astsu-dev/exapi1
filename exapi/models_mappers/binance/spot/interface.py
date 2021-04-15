"""Has binance models mapper interface."""

from exapi.models_mappers.binance.spot.market_data.interface import \
    IBinanceSpotMarketDataModelsMapper
from exapi.models_mappers.binance.spot.trading import \
    IBinanceSpotTradingModelsMapper


class IBinanceSpotModelsMapper(IBinanceSpotMarketDataModelsMapper, IBinanceSpotTradingModelsMapper):
    """Binance models mapper interface.

    Maps json to models.
    """
