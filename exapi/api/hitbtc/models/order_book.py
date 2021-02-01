"""Has hitbtc order book, order book order models."""

from dataclasses import dataclass
from decimal import Decimal
from typing import Dict, List, TypedDict

from exapi.requesters.hitbtc.typedefs import Datetime, Symbol


class HitbtcRawOrderBookOrderModel(TypedDict):
    """Hibtc order book order json model."""

    price: str
    size: str


class HitbtcRawSingleOrderBookModel(TypedDict):
    """Order book json model from get orderbook response."""

    ask: List[HitbtcRawOrderBookOrderModel]
    bid: List[HitbtcRawOrderBookOrderModel]
    timestamp: Datetime


class HitbtcRawOrderBookModel(HitbtcRawSingleOrderBookModel):
    """Order book json model from get orderbooks response.

    Inherites hitbtc raw single order book model. Has additional symbol field.
    """

    symbol: Symbol


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
class HitbtcSingleOrderBookModel:
    """Hitbtc order book model.

    Will be returend from get orderbook response.

    Args:
        ask (List[HitbtcOrderBookOrderModel]): list of ask orders.
        bid (List[kHitbtcOrderBookOrderModel]): list of bid orders.
        timestamp: Datetime
    """

    ask: List[HitbtcOrderBookOrderModel]
    bid: List[HitbtcOrderBookOrderModel]
    timestamp: Datetime


@dataclass(frozen=True)
class HitbtcOrderBookModel(HitbtcSingleOrderBookModel):
    """Inherites hitbtc single order book model.

    Has additional symbol field.

    Will be returned from get orderbooks response.

    Args:
        ask (List[HitbtcOrderBookOrderModel]): list of ask orders.
        bid (List[HitbtcOrderBookOrderModel]): list of bid orders.
        timestamp (Datetime)
        symbol (Symbol)
    """

    symbol: Symbol


HitbtcRawOrderBooks = Dict[str, HitbtcRawOrderBookModel]
HitbtcOrderBooks = Dict[str, HitbtcOrderBookModel]