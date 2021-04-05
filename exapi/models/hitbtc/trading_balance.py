from dataclasses import dataclass
from decimal import Decimal
from typing import List, TypedDict

from exapi.typedefs.hitbtc import Currency


class HitbtcRawTradingCurrencyBalanceModel(TypedDict):
    """Currency trading balance json model."""

    currency: Currency
    available: str
    reserved: str


@dataclass(frozen=True)
class HitbtcTradingCurrencyBalanceModel:
    """Currency trading balance model.

    Args:
        currency (Currency)
        available (Decimal)
        reserved (Decimal)
    """

    currency: Currency
    available: Decimal
    reserved: Decimal


HitbtcRawTradingCurrencyBalances = List[HitbtcRawTradingCurrencyBalanceModel]
HitbtcTradingCurrencyBalances = List[HitbtcTradingCurrencyBalanceModel]
