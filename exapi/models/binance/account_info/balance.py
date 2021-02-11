from dataclasses import dataclass
from decimal import Decimal
from typing import List, TypedDict


class BinanceCurrencyBalanceJson(TypedDict):
    asset: str
    free: str
    locked: str


@dataclass(frozen=True)
class BinanceCurrencyBalanceModel:
    """Binance currency balance model.

    Args:
        asset (str): currency
        free (Decimal)
        locked (Decimal)
    """

    asset: str
    free: Decimal
    locked: Decimal


BinanceCurrencyBalancesJson = List[BinanceCurrencyBalanceJson]
BinanceCurrencyBalances = List[BinanceCurrencyBalanceModel]
