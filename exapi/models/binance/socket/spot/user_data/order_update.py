from dataclasses import dataclass
from decimal import Decimal
from typing import List, Literal, Optional, TypedDict

from exapi.typedefs.binance import OCOOrderStatus, OCOStatus, OrderContingencyType, OrderExecutionType, OrderSide, \
    OrderStatus, \
    OrderType, \
    TimeInForce


class BinanceSocketSpotExecutionReportEventJson(TypedDict):
    """Binance socket spot execution report event json.

    For non-oco orders.

    From user data stream.

    Fields:
        e (Literal["executionReport"]): event type
        E (int): event time
        s (str): symbol
        c (str): client order id
        S (OrderSide): side
        o (OrderType): order type
        f (TimeInForce): time in force
        q (str): order quantity
        p (str): order price
        P (str): stop price
        F (str): iceberq quantity
        g (int): order list id
        C (str): original client order id
        x (OrderExecutionType): current execution type
        X (OrderStatus): current order status
        r (str): order reject reason; will be an error code
        i (int): order id
        l (str): last executed quantity
        z (str): cumulative filled quantity
        L (str): last executed price
        n (str): commission amount
        N (Optional[str]): commission asset
        T (int): transaction time
        t (int): trade id
        I (int): ignore
        w (bool): is the order on the book?
        m (bool): is this trade the maker side?
        M (bool): ignore
        O (int): order creation time
        Z (str): cumulative quote asset transacted quantity
        Y (str): last quote asset transacted quantity (i.e. lastPrice * lastQty)
        Q (str): quote order quantity
    """

    e: Literal["executionReport"]
    E: int
    s: str
    c: str
    S: OrderSide
    o: OrderType
    f: TimeInForce
    q: str
    p: str
    P: str
    F: str
    g: int
    C: str
    x: OrderExecutionType
    X: OrderStatus
    r: str
    i: int
    l: str
    z: str
    L: str
    n: str
    N: Optional[str]
    T: int
    t: int
    I: int
    w: bool
    m: bool
    M: bool
    O: int
    Z: str
    Y: str
    Q: str


@dataclass(frozen=True)
class BinanceSocketSpotExecutionReportEventModel:
    """Binance socket spot execution report event model.

    For non-oco orders.

    From user data stream.

    Fields:
        event_type (Literal["executionReport"])
        event_time (int)
        symbol (str)
        client_order_id (str)
        side (OrderSide)
        type (OrderType)
        time_in_force (TimeInForce)
        quantity (Decimal)
        price (Decimal)
        stop_price (Decimal)
        iceberg_quantity (Decimal)
        order_list_id (int)
        orig_client_order_id (str)
        execution_type (OrderExecutionType)
        status (OrderStatus)
        reject_reason (str): order reject reason; will be an error code
        id (int)
        last_executed_quantity (Decimal)
        cumulative_filled_quantity (Decimal)
        last_executed_price (Decimal)
        commission_amount (Decimal)
        commission_asset (Optional[str])
        transaction_time (int)
        trade_id (int)
        is_order_on_book (bool): is the order on the book?
        is_trade_maker_side (bool): is this trade the maker side?
        creation_time (int)
        cumulative_quote_asset (Decimal)
        last_quote_asset_transacted_quantity (Decimal)
        quote_order_quantity (Decimal)
    """

    event_type: Literal["executionReport"]
    event_time: int
    symbol: str
    client_order_id: str
    side: OrderSide
    type: OrderType
    time_in_force: TimeInForce
    quantity: Decimal
    price: Decimal
    stop_price: Decimal
    iceberg_quantity: Decimal
    order_list_id: int
    orig_client_order_id: str
    execution_type: OrderExecutionType
    status: OrderStatus
    reject_reason: str
    id: int
    last_executed_quantity: Decimal
    cumulative_filled_quantity: Decimal
    last_executed_price: Decimal
    commission_amount: Decimal
    commission_asset: Optional[str]
    transaction_time: int
    trade_id: int
    is_order_on_book: bool
    is_trade_maker_side: bool
    creation_time: int
    cumulative_quote_asset: Decimal
    last_quote_asset_transacted_quantity: Decimal
    quote_order_quantity: Decimal


class BinanceSocketSpotOCOSubOrderInfoJson(TypedDict):
    """Binance socket spot OCO sub order info json.

    From user data stream.

    Fields:
        s (str): symbol
        i (int): order id
        c (str): client order id
    """

    s: str
    i: int
    c: str


@dataclass(frozen=True)
class BinanceSocketSpotOCOSubOrderInfoModel:
    """Binance socket spot OCO sub order info model.

    From user data stream.

    Fields:
        symbol (str)
        id (int): order id
        client_order_id (str)
    """

    symbol: str
    id: int
    client_order_id: str


class BinanceSocketSpotListStatusEventJson(TypedDict):
    """Binance socket spot list status event json.

    From user data stream.

    For oco orders.

    Fields:
        e (Literal["listStatus"]): event type
        E (int): event time
        s (str): symbol
        g (int): order list id
        c (OrderContingencyType): contingency type
        l (OCOStatus): list status type
        L (OCOOrderStatus): list order status
        r (str): list reject reason
        C (str): list client order id
        T (int): transaction time
        O (List[BinanceSocketSpotOCOSubOrderInfoJson]): list of orders
    """

    e: Literal["listStatus"]
    E: int
    s: str
    g: int
    c: OrderContingencyType
    l: OCOStatus
    L: OCOOrderStatus
    r: str
    C: str
    T: int
    O: List[BinanceSocketSpotOCOSubOrderInfoJson]


@dataclass(frozen=True)
class BinanceSocketSpotListStatusEventModel:
    """Binance socket spot list status event model.

    From user data stream.

    For oco orders.

    Fields:
        event_type (Literal["listStatus"])
        event_time (int)
        symbol (str)
        order_list_id (int)
        contingency_type (OrderContingencyType)
        list_status_type (OCOStatus)
        list_order_status (OCOOrderStatus)
        list_reject_reason (str)
        client_order_id (str): list client order id
        transaction_time (int)
        orders (List[BinanceSocketSpotOCOSubOrderInfoJson]): list or orders
    """

    event_type: Literal["listStatus"]
    event_time: int
    symbol: str
    order_list_id: int
    contingency_type: OrderContingencyType
    list_status_type: OCOStatus
    list_order_status: OCOOrderStatus
    list_reject_reason: str
    client_order_id: str
    transaction_time: int
    orders: List[BinanceSocketSpotOCOSubOrderInfoJson]
