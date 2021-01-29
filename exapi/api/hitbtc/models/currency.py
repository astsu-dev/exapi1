"""Has hitbtc currency model."""

from dataclasses import dataclass
from decimal import Decimal
from typing import List

from exapi.requesters.hitbtc.typedefs import Symbol


@dataclass(frozen=True)
class HitbtcCurrencyModel:
    """Hitbtc currency model."""

    id: Symbol
    fullName: str
    crypto: bool
    payinEnabled: bool
    payinPaymentId: bool
    payinConfirmations: int
    payoutEnabled: bool
    payoutIsPaymentId: bool
    transferEnabled: bool
    delisted: bool
    payoutFee: Decimal
    payoutMinimalAmount: Decimal
    precisionPayout: int
    precisionTransfer: int


HitbtcCurrencies = List[HitbtcCurrencyModel]
