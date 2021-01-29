

from dataclasses import dataclass
from decimal import Decimal

from exapi.requesters.hitbtc.typedefs import Datetime, OrderSide


@dataclass(frozen=True)
class HitbtcTradeModel:
    """Hitbtc trade model."""

    id: int
    price: Decimal
    quantity: Decimal
    side: OrderSide
    timestamp: Datetime
