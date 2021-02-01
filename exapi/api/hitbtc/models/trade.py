"""Has hitbtc trade model."""

from dataclasses import dataclass
from decimal import Decimal
from typing import Dict, List, TypedDict

from exapi.requesters.hitbtc.typedefs import Datetime, OrderSide


class HitbtcRawTradeModel(TypedDict):
    """Trade json model."""

    id: int
    price: str
    quantity: str
    side: OrderSide
    timestamp: Datetime


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


HitbtcRawSymbolTrades = List[HitbtcRawTradeModel]
HitbtcRawTrades = Dict[str, HitbtcRawSymbolTrades]
HitbtcSymbolTrades = List[HitbtcTradeModel]
HitbtcTrades = Dict[str, HitbtcSymbolTrades]
