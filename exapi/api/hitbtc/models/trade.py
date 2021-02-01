"""Has hitbtc trade model."""

from dataclasses import dataclass
from decimal import Decimal
from typing import Dict, List

from exapi.requesters.hitbtc.typedefs import Datetime, OrderSide


@dataclass(frozen=True)
class HitbtcTradeModel:
    """Hitbtc trade model.

    Args:
        id (int)
        price (Decimal)
        quantity (Decimal)
        side (OrderSide)
        timestamp (Datetime)
    """

    id: int
    price: Decimal
    quantity: Decimal
    side: OrderSide
    timestamp: Datetime


HitbtcSymbolTrades = List[HitbtcTradeModel]
HitbtcTrades = Dict[str, HitbtcSymbolTrades]
