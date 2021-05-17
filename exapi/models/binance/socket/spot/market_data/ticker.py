from dataclasses import dataclass
from decimal import Decimal
from typing import List, Literal, TypedDict


class BinanceSocketSpotTickerEventJson(TypedDict):
    """Binance socket spot individual symbol 24hr ticker event json.

    From @ticker endpoint.

    Fields:
        e (Literal["24hrTicker"]): event type
        E (int): event time
        s (str): symbol
        p (str): price change
        P (str): price change percent
        w (str): weighted average price
        x (str): first trade id - 1 price
            (first trade before the 24hr rolling window)
        c (str): last price
        Q (str): last quantity
        b (str): best bid price
        B (str): best bid quantity
        a (str): best ask price
        A (str): best ask quantity
        o (str): open price
        h (str): high price
        l (str): low price
        v (str): total traded base asset volume
        q (str): total traded quote asset volume
        O (int): statistics open time
        C (int): statistics close time
        F (int): first trade id
        L (int): last trade id
        n (int): total number of trades
    """

    e: Literal["24hrTicker"]
    E: int
    s: str
    p: str
    P: str
    w: str
    x: str
    c: str
    Q: str
    b: str
    B: str
    a: str
    A: str
    o: str
    h: str
    l: str
    v: str
    q: str
    O: int
    C: int
    F: int
    L: int
    n: int


@dataclass(frozen=True)
class BinanceSocketSpotTickerEventModel:
    """Binance socket spot individual symbol 24hr ticker event model.

    From @ticker endpoint.

    Fields:
        event_type (Literal["24hrTicker"])
        event_time (int)
        symbol (str)
        price_change (Decimal)
        price_change_percent (Decimal)
        weighted_avg_price (Decimal)
        prev_ticker_price (Decimal): first trade id - 1 price
            (first trade before the 24hr rolling window)
        last_price (Decimal)
        last_quantity (Decimal)
        best_bid_price (Decimal)
        best_bid_quantity (Decimal)
        best_ask_price (Decimal)
        best_ask_quantity (Decimal)
        open_price (Decimal)
        high_price (Decimal)
        low_price (Decimal)
        base_volume (Decimal): total traded base asset volume
        quote_volume (Decimal): total traded quote asset volume
        stats_open_time (int): statistics open time
        stats_close_time (int): statistics close time
        first_trade_id (int)
        last_trade_id (int)
        num_of_trades (int): total number of trades
    """

    event_type: Literal["24hrTicker"]
    event_time: int
    symbol: str
    price_change: Decimal
    price_change_percent: Decimal
    weighted_avg_price: Decimal
    previous_ticker_price: Decimal
    last_price: Decimal
    last_quantity: Decimal
    best_bid_price: Decimal
    best_bid_quantity: Decimal
    best_ask_price: Decimal
    best_ask_quantity: Decimal
    open_price: Decimal
    high_price: Decimal
    low_price: Decimal
    base_volume: Decimal
    quote_volume: Decimal
    stats_open_time: int
    stats_close_time: int
    first_trade_id: int
    last_trade_id: int
    num_of_trades: int


BinanceSocketSpotTickersEventJson = List[BinanceSocketSpotTickerEventJson]
BinanceSocketSpotTickersEvent = List[BinanceSocketSpotTickerEventModel]
