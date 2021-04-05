"""Has hitbtc order book, order book order models."""

from dataclasses import dataclass
from decimal import Decimal
from typing import Dict, List, TypedDict

from exapi.typedefs.hitbtc import Datetime, Symbol


class HitbtcRawOrderBookOrderModel(TypedDict):
    """Hibtc order book order json model."""

    price: str
    size: str


class HitbtcRawOrderBookModel(TypedDict):
    """Order book json model from get orderbooks response.

    Inherites hitbtc raw single order book model. Has additional symbol field.
    """

    symbol: Symbol
    ask: List[HitbtcRawOrderBookOrderModel]
    bid: List[HitbtcRawOrderBookOrderModel]
    timestamp: Datetime


@dataclass(frozen=True)
class HitbtcOrderBookOrderModel:
    """Hitbtc order book order model.

    Args:
        price (Decimal)
        size (Decimal): quantity.
    """

    price: Decimal
    size: Decimal


@dataclass(frozen=True)
class HitbtcOrderBookModel:
    """Hitbtc order book model.

    Will be returend from get orderbook response.

    Args:
        ask (List[HitbtcOrderBookOrderModel]): list of ask orders.
        bid (List[kHitbtcOrderBookOrderModel]): list of bid orders.
        timestamp: Datetime
    """

    symbol: Symbol
    ask: List[HitbtcOrderBookOrderModel]
    bid: List[HitbtcOrderBookOrderModel]
    timestamp: Datetime


HitbtcRawOrderBooks = Dict[str, HitbtcRawOrderBookModel]
HitbtcOrderBooks = Dict[str, HitbtcOrderBookModel]
