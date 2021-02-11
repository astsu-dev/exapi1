"""Has binance price ticker model."""

from dataclasses import dataclass
from decimal import Decimal
from typing import List, TypedDict


class BinancePriceTickerJson(TypedDict):
    symbol: str
    price: str


@dataclass(frozen=True)
class BinancePriceTickerModel:
    """Binance price ticker model.

    Args:
        symbol (str)
        price (Decimal)
    """

    symbol: str
    price: Decimal


BinancePriceTickersJson = List[BinancePriceTickerJson]
BinancePriceTickers = List[BinancePriceTickerModel]
