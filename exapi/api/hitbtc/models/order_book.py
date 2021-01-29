"""Has hitbtc order book, order book order models.
    """

from dataclasses import dataclass
from decimal import Decimal
from typing import List

from exapi.requesters.hitbtc.typedefs import Datetime


@dataclass(frozen=True)
class HitbtcOrderBookOrderModel:
    """Hitbtc order model from order book."""

    price: Decimal
    size: Decimal


@dataclass(frozen=True)
class HitbtcOrderBookModel:
    """Hitbtc order book model."""

    ask: List[HitbtcOrderBookOrderModel]
    bid: List[HitbtcOrderBookOrderModel]
    timestamp: Datetime
