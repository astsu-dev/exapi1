"""Has binance trade model."""

from dataclasses import dataclass
from decimal import Decimal
from typing import List, TypedDict


class BinanceTradeJson(TypedDict):
    id: int
    price: str
    qty: str
    quoteQty: str
    time: int
    isBuyerMaker: bool
    isBestMatch: bool


@dataclass(frozen=True)
class BinanceTradeModel:
    """Trade model.

    Args:
        id (int)
        price (Decimal)
        qty (Decimal)
        quote_qty (Decimal)
        time (int)
        is_buyer_maker (bool)
        is_best_match (bool)
    """

    id: int
    price: Decimal
    qty: Decimal
    quote_qty: Decimal
    time: int
    is_buyer_maker: bool
    is_best_match: bool


class BinanceAggregateTradeJson(TypedDict):
    """Binance aggregate trade json.

    Args:
        a (int): aggregate trade id.
        p (str): price.
        q (str): quantity.
        f (int): first trade id.
        l (int): last trade id.
        T (int): timestamp.
        m (bool): was the buyer the maker?
        M (bool): was the trade the best price match?
    """

    a: int
    p: str
    q: str
    f: int
    l: int
    T: int
    m: bool
    M: bool


@dataclass(frozen=True)
class BinanceAggregateTradeModel:
    """Binance aggregate trade model.

    Args:
        id (int)
        price (Decimal)
        qty (Decimal)
        first_id (int): first trade id
        last_id (int): last trade id
        time (int): timestamp
        is_buyer_maker (bool)
        is_best_match (bool)
    """

    id: int
    price: Decimal
    qty: Decimal
    first_id: int
    last_id: int
    time: int
    is_buyer_maker: bool
    is_best_match: bool


BinanceTradesJson = List[BinanceTradeJson]
BinanceAggregateTradesJson = List[BinanceAggregateTradeJson]
BinanceAggregateTrades = List[BinanceAggregateTradeModel]
BinanceTrades = List[BinanceTradeModel]
