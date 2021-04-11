from dataclasses import dataclass
from decimal import Decimal
from typing import List, Optional, TypedDict

from exapi.models.hitbtc.trade import HitbtcRawTradeModel, HitbtcTradeModel
from exapi.typedefs.hitbtc import (Datetime, OrderSide, OrderStatus, OrderType,
                                   Symbol, TimeInForce)


class HitbtcRawOrderModel(TypedDict):
    """Order json model.

    Args:
        id (int)
        clientOrderId (str)
        symbol (Symbol)
        side (OrderSide)
        status (OrderStatus)
        type (OrderType)
        timeInForce (TimeInForce)
        quantity (str)
        price (str)
        cumQuantity (str)
        createdAt (Datetime)
        updatedAt (Datetime)
        postOnly (bool)
        avgPrice (str, optional)
        stoPrice (str, optional)
        expireTime (str, optional)
        tradesReport (List[HitbtcRawTradeModel], optional)
    """

    id: int
    clientOrderId: str
    symbol: Symbol
    side: OrderSide
    status: OrderStatus
    type: OrderType
    timeInForce: TimeInForce
    quantity: str
    price: str
    cumQuantity: str
    createdAt: Datetime
    updatedAt: Datetime
    postOnly: bool
    avgPrice: str
    stopPrice: str
    expireTime: str
    tradesReport: List[HitbtcRawTradeModel]


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
    cum_quantity: Decimal
    created_at: Datetime
    updated_at: Datetime
    post_only: bool
    avg_price: Optional[Decimal] = None
    stop_price: Optional[Decimal] = None
    expire_time: Optional[Datetime] = None
    trades_report: Optional[List[HitbtcTradeModel]] = None


HitbtcOrders = List[HitbtcOrderModel]
HitbtcRawOrders = List[HitbtcRawOrderModel]
