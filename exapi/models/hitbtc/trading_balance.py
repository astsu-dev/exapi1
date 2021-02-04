from dataclasses import dataclass
from decimal import Decimal
from typing import List, TypedDict

from .typedefs import Currency


class HitbtcRawCurrencyTradingBalanceModel(TypedDict):
    currency: Currency
    available: str
    reserved: str


@dataclass(frozen=True)
class HitbtcCurrencyTradingBalanceModel:
    currency: Currency
    available: Decimal
    reserved: Decimal


HitbtcRawCurrencyTradingBalances = List[HitbtcRawCurrencyTradingBalanceModel]
HitbtcCurrencyTradingBalances = List[HitbtcCurrencyTradingBalanceModel]
