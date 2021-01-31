"""Has hitbtc ticker model."""

from dataclasses import dataclass
from decimal import Decimal
from typing import Optional

from exapi.requesters.hitbtc.typedefs import Datetime, Symbol


@dataclass(frozen=True)
class HitbtcTickerModel:
    """Hitbtc ticker model.

    Args:
        ask (Optional[Decimal])
        bid (Optional[Decimal])
        last (Optional[Decimal])
        open (Optional[Decimal])
        low (Decimal)
        high (Decimal)
        volume (Decimal)
        volume_quote (Decimal)
        timestamp (Datetime)
        symbol (Optional[Symbol])
    """

    ask: Optional[Decimal]
    bid: Optional[Decimal]
    last: Optional[Decimal]
    open: Optional[Decimal]
    low: Decimal
    high: Decimal
    volume: Decimal
    volume_quote: Decimal
    timestamp: Datetime
    symbol: Optional[Symbol]
