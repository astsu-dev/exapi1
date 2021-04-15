"""Has hitbtc models mapper interface."""

from exapi.models_mappers.hitbtc.market_data import IHitbtcMarketDataModelsMapper
from exapi.models_mappers.hitbtc.trading import IHitbtcTradingModelsMapper


class IHitbtcModelsMapper(IHitbtcMarketDataModelsMapper, IHitbtcTradingModelsMapper):
    """Has methods for mapping hitbtc json models
    to hitbtc dataclass models.
    """
