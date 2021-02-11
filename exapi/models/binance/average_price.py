"""Has binance average price model."""

from dataclasses import dataclass
from decimal import Decimal
from typing import TypedDict


class BinanceAveragePriceJson(TypedDict):
    mins: int
    price: str


@dataclass(frozen=True)
class BinanceAveragePriceModel:
    """Binance average price model.

    Args:
        mins (int): minutes number.
        price (Decimal)
    """

    mins: int
    price: Decimal
