"""Has hitbtc candle model."""

from dataclasses import dataclass
from decimal import Decimal

from exapi.requesters.hitbtc.typedefs import Datetime


@dataclass(frozen=True)
class HitbtcCandleModel:
    """Hitbtc candle model."""

    timestamp: Datetime
    open: Decimal
    close: Decimal
    min: Decimal
    max: Decimal
    volume: Decimal
    volumeQuote: Decimal
