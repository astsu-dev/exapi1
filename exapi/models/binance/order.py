from dataclasses import dataclass
from decimal import Decimal
from typing import List, Optional, TypedDict, Union

from exapi.models.binance.typedefs import (OrderSide, OrderStatus, OrderType,
                                           TimeInForce)


class BinanceFilledOrderJson(TypedDict):
    price: str
    qty: str
    commission: str
    commissionAsset: str


@dataclass(frozen=True)
class BinanceFilledOrderModel:
    """Binance filled order model.

    Args:
        price (Decimal)
        qty (Decimal)
        commission (Decimal)
        commission_asset (str)
    """

    price: Decimal
    qty: Decimal
    commission: Decimal
    commission_asset: str


BinanceFilledOrdersJson = List[BinanceFilledOrderJson]
BinanceFilledOrders = List[BinanceFilledOrderModel]


class BinanceAckOrderJson(TypedDict):
    symbol: str
    orderId: int
    orderListId: int
    clientOrderId: str
    transactTime: int


class BinanceResultOrderJson(BinanceAckOrderJson):
    price: str
    origQty: str
    executedQty: str
    cummulativeQuoteQty: str
    status: OrderStatus
    timeInForce: TimeInForce
    type: OrderType
    side: OrderSide


class BinanceFullOrderJson(BinanceResultOrderJson):
    fills: BinanceFilledOrdersJson


class BinanceOrderInfoJson(TypedDict):
    symbol: str
    orderId: int
    orderListId: int
    clientOrderId: str
    price: str
    origQty: str
    executedQty: str
    cummulativeQuoteQty: str
    status: OrderStatus
    timeInForce: TimeInForce
    type: OrderType
    side: OrderSide
    isWorking: bool
    updateTime: int
    fills: BinanceFilledOrdersJson


@dataclass(frozen=True)
class BinanceOrderModel:
    """Binance order model.

    Args:
        symbol (str)
        order_id (int)
        order_list_id (int)
        client_order_id (str)
        transact_time (int)
        price (Optional[Decimal], optional): Defaults to None.
        orig_qty (Optional[Decimal], optional): Defaults to None.
        executed_qty (Optional[Decimal], optional): Defaults to None.
        cummulative_quote_qty (Optional[Decimal], optional): Defaults to None.
        status (Optional[OrderStatus], optional): Defaults to None.
        time_in_force (Optional[TimeInForce], optional): Defaults to None.
        type (Optional[OrderType], optional): Defaults to None.
        side (Optional[OrderSide], optional): Defaults to None.
        fills (Optional[BinanceFilledOrders], optional): Defaults to None.
    """

    symbol: str
    order_id: int
    order_list_id: int
    client_order_id: str
    transact_time: int
    price: Optional[Decimal] = None
    orig_qty: Optional[Decimal] = None
    executed_qty: Optional[Decimal] = None
    cummulative_quote_qty: Optional[Decimal] = None
    status: Optional[OrderStatus] = None
    time_in_force: Optional[TimeInForce] = None
    type: Optional[OrderType] = None
    side: Optional[OrderSide] = None
    fills: Optional[BinanceFilledOrders] = None


@dataclass(frozen=True)
class BinanceOrderInfoModel:
    """Binance order info model.

    Used in query order, get all open orders resopnses.

    Args:
        symbol (str)
        order_id (int)
        order_list_id (int)
        client_order_id (str)
        is_working: bool
        update_time: int
        price (Optional[Decimal], optional): Defaults to None.
        orig_qty (Optional[Decimal], optional): Defaults to None.
        executed_qty (Optional[Decimal], optional): Defaults to None.
        cummulative_quote_qty (Optional[Decimal], optional): Defaults to None.
        status (Optional[OrderStatus], optional): Defaults to None.
        time_in_force (Optional[TimeInForce], optional): Defaults to None.
        type (Optional[OrderType], optional): Defaults to None.
        side (Optional[OrderSide], optional): Defaults to None.
        fills (Optional[BinanceFilledOrders], optional): Defaults to None.
    """

    symbol: str
    order_id: int
    order_list_id: int
    client_order_id: str
    is_working: bool
    update_time: int
    price: Optional[Decimal] = None
    orig_qty: Optional[Decimal] = None
    executed_qty: Optional[Decimal] = None
    cummulative_quote_qty: Optional[Decimal] = None
    status: Optional[OrderStatus] = None
    time_in_force: Optional[TimeInForce] = None
    type: Optional[OrderType] = None
    side: Optional[OrderSide] = None
    fills: Optional[BinanceFilledOrders] = None


BinanceOrderJson = Union[
    BinanceAckOrderJson,
    BinanceResultOrderJson,
    BinanceFullOrderJson
]
BinanceOrdersJson = List[BinanceOrderJson]
BinanceOrders = List[BinanceOrderModel]
BinanceOrderInfosJson = List[BinanceOrderInfoJson]
BinanceOrderInfos = List[BinanceOrderInfoModel]
