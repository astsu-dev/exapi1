"""Has hitbtc ticker model."""

from dataclasses import dataclass
from decimal import Decimal
from typing import List, Optional, TypedDict

from exapi.requesters.hitbtc.typedefs import Datetime, Symbol


class HitbtcRawTickerModel(TypedDict):
    """Ticker json model."""

    symbol: Symbol
    low: str
    high: str
    volume: str
    volumeQuote: str
    timestamp: Datetime
    ask: Optional[str]
    bid: Optional[str]
    last: Optional[str]
    open: Optional[str]


@dataclass(frozen=True)
class HitbtcTickerModel:
    """Hitbtc ticker model.

    Args:
        ask (Optional[Decimal])
        bid (Optional[Decimal])
        last (Optional[Decimal])
        open (Optional[Dkecimal])
        low (Decimal)
        high (Decimal)
        volume (Decimal)
        volume_quote (Decimal)
        timestamp (Datetime)
        symbol (Optional[Symbol])
    """

    symbol: Symbol
    low: Decimal
    high: Decimal
    volume: Decimal
    volume_quote: Decimal
    timestamp: Datetime
    ask: Optional[Decimal] = None
    bid: Optional[Decimal] = None
    last: Optional[Decimal] = None
    open: Optional[Decimal] = None


HitbtcRawTickers = List[HitbtcRawTickerModel]
HitbtcTickers = List[HitbtcTickerModel]
