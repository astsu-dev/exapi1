"""Has binance order book model."""

from dataclasses import dataclass
from decimal import Decimal
from typing import List, TypedDict

BinanceOrderBookOrderJson = List[str]
BinanceOrderBookOrdersJson = List[BinanceOrderBookOrderJson]


class BinanceOrderBookJson(TypedDict):
    lastUpdateId: int
    bids: BinanceOrderBookOrdersJson
    asks: BinanceOrderBookOrdersJson


@dataclass(frozen=True)
class BinanceOrderBookOrderModel:
    """Order book order model.

    Args:
        price (Decimal)
        quantity (Decimal)
    """

    price: Decimal
    quantity: Decimal


BinanceOrderBookOrders = List[BinanceOrderBookOrderModel]


@dataclass(frozen=True)
class BinanceOrderBookModel:
    last_update_id: int
    bids: BinanceOrderBookOrders
    asks: BinanceOrderBookOrders
