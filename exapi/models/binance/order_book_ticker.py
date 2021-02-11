"""Has binance order book ticker model."""

from dataclasses import dataclass
from decimal import Decimal
from typing import List, TypedDict


class BinanceOrderBookTickerJson(TypedDict):
    symbol: str
    bidPrice: str
    bidQty: str
    askPrice: str
    askQty: str


@dataclass(frozen=True)
class BinanceOrderBookTickerModel:
    """Binance order book ticker model.

    Args:
        symbol (str)
        bid_price (Decimal)
        bid_qty (Decimal)
        ask_price (Decimal)
        ask_qty (Decimal)
    """

    symbol: str
    bid_price: Decimal
    bid_qty: Decimal
    ask_price: Decimal
    ask_qty: Decimal


BinanceOrderBookTickersJson = List[BinanceOrderBookTickerJson]
BinanceOrderBookTickers = List[BinanceOrderBookTickerModel]
