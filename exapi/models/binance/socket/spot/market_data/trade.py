from dataclasses import dataclass
from decimal import Decimal
from typing import Literal, TypedDict


class BinanceSocketSpotTradeEventJson(TypedDict):
    """Binance socket spot trade event json.

    Fields:
        e (Literal["trade"]): event type
        E (int): event time
        s (str): symbol
        t (int): trade id
        p (str): price
        q (str): quantity
        b (int): buyer order id
        a (int): seller order id
        T (int): trade time
        m (bool): is the buyer the market maker?
        M (bool): ignore
    """

    e: Literal["trade"]
    E: int
    s: str
    t: int
    p: str
    q: str
    b: int
    a: int
    T: int
    m: bool
    M: bool


@dataclass(frozen=True)
class BinanceSocketSpotTradeEventModel:
    """Binance socket spot trade event model.

    Fields:
        event_type (Literal["trade"])
        event_time (int)
        symbol (str)
        trade_id (int)
        price (Decimal)
        quantity (Decimal)
        buyer_order_id (int)
        seller_order_id (int)
        trade_time (int)
        is_buyer_market_maker (bool)
    """

    event_type: Literal["trade"]
    event_time: int
    symbol: str
    trade_id: int
    price: Decimal
    quantity: Decimal
    buyer_order_id: int
    seller_order_id: int
    trade_time: int
    is_buyer_market_maker: bool
