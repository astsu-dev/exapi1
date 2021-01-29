from dataclasses import dataclass
from decimal import Decimal
from typing import List

from exapi.requesters.hitbtc.typedefs import Currency, Symbol


@dataclass(frozen=True)
class HitbtcSymbolModel:
    """Hitbtc symbol model."""

    id: Symbol
    baseCurrency: Currency
    quoteCurrency: Currency
    quantityIncrement: Decimal
    tickSize: Decimal
    takeLiquidityRate: Decimal
    provideLiquidityRate: Decimal
    feeCurrency: Currency


HitbtcSymbols = List[HitbtcSymbolModel]
