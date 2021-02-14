"""Has binance order book model."""

from dataclasses import dataclass
from decimal import Decimal
from typing import List, Tuple, TypedDict

BinanceOrderBookOrderJson = Tuple[str, str]
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
    """Order book model.

    Args:
        last_update_id (int)
        bids (BinanceOrderBookOrders)
        asks (BinanceOrderBookOrders)
    """

    last_update_id: int
    bids: BinanceOrderBookOrders
    asks: BinanceOrderBookOrders
