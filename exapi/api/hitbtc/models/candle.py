"""Has hitbtc candle model."""

from dataclasses import dataclass
from decimal import Decimal

from exapi.requesters.hitbtc.typedefs import Datetime


@dataclass(frozen=True)
class HitbtcCandleModel:
    """Hitbtc candle model.

    Args:
        timestamp (Datetime)
        open (Decimal): open price.
        close (Decimal): close price.
        min (Decimal): min price.
        max (Decimal): max price.
        volume (Decimal)
        volume_quote (Decimal)
    """

    timestamp: Datetime
    open: Decimal
    close: Decimal
    min: Decimal
    max: Decimal
    volume: Decimal
    volume_quote: Decimal
