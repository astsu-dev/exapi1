"""Has hitbtc symbol model."""

from dataclasses import dataclass
from decimal import Decimal
from typing import List

from exapi.requesters.hitbtc.typedefs import Currency, Symbol


@dataclass(frozen=True)
class HitbtcSymbolModel:
    """Hitbtc symbol model.

    Args:
        id (Symbol)
        base_currency (Currency)
        quote_currency (Currency)
        quantity_increment (Decimal)
        tick_size (Decimal)
        take_liquidity_rate (Decimal): taker fee.
        provide_liquidity_rate (Decimal): maker fee.
        fee_currency (Currency)
    """

    id: Symbol
    base_currency: Currency
    quote_currency: Currency
    quantity_increment: Decimal
    tick_size: Decimal
    take_liquidity_rate: Decimal
    provide_liquidity_rate: Decimal
    fee_currency: Currency


HitbtcSymbols = List[HitbtcSymbolModel]
