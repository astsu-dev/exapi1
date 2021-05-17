from dataclasses import dataclass
from decimal import Decimal
from typing import Literal, TypedDict


class BinanceSocketSpotAggTradeEventJson(TypedDict):
    """Binance spot market data stream agg trade event json.

    Fields:
        e (Literal["aggTrade"]): event type
        E (int): event time
        s (str): symbol
        t (int): aggregated trade id
        p (str): price
        q (str): quantity
        f (int): first trade id
        l (int): last trade id
        T (int): trade time
        m (bool): is the buyer the market maker?
        M (bool): ignore
    """

    e: Literal["aggTrade"]
    E: int
    s: str
    a: int
    p: str
    q: str
    f: int
    l: int
    T: int
    m: bool
    M: bool


@dataclass(frozen=True)
class BinanceSocketSpotAggTradeEventModel:
    """Binance spot market data stream agg trade event model.

    Fields:
        event_type (Literal["aggTrade"])
        event_time (int)
        symbol (str)
        agg_trade_id (int)
        price (Decimal)
        quantity (Decimal)
        first_trade_id (int)
        last_trade_id (int)
        trade_time (int)
        is_buyer_market_maker (bool)
    """

    event_type: Literal["aggTrade"]
    event_time: int
    symbol: str
    agg_trade_id: int
    price: Decimal
    quantity: Decimal
    first_trade_id: int
    last_trade_id: int
    trade_time: int
    is_buyer_market_maker: bool
