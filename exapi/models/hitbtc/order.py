from dataclasses import dataclass
from typing import List

from .typedefs import OrderSide, OrderType, TimeInForce


@dataclass(frozen=True)
class HitbtcOrderModel:
    id: int
    client_order_id: str
    symbol: Symbol
    side: OrderSide
    status: OrderStatus
    type: OrderType
    time_in_force: TimeInForce
    quantity: Decimal
    price: Decimal
    avg_price: Decimal
    cum_quantity: str
    created_at: Datetime
    updated_at: Datetime
    post_only: bool
    stop_price: Optional[str] = None
    expire_time: Optional[Datetime] = None
    trades_report: Optional[List[HitbtcTradeModel]] = None
