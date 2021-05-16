from dataclasses import dataclass
from decimal import Decimal
from typing import List, Literal, TypedDict


class BinanceSocketSpotMiniTickerEventJson(TypedDict):
    """Binance socket spot individual symbol 24hr mini ticker event json.
    
    From @miniTicker endpoint.

    Fields:
        e (Literal["24hrMiniTicker"]): event type
        E (int): event time
        s (str): symbol
        c (str): close price
        o (str): open price
        h (str): high price
        l (str): low price
        v (str): total traded base asset volume
        q (str): total traded quote asset volume
    """

    e: Literal["24hrMiniTicker"]
    E: int
    s: str
    c: str
    o: str
    h: str
    l: str
    v: str
    q: str


@dataclass(frozen=True)
class BinanceSocketSpotMiniTickerEventModel:
    """Binance socket spot individual symbol 24hr mini ticker event model.

    From @miniTicker endpoint.

    Fields:
        event_type (Literal["24hrMiniTicker"])
        event_time (int)
        symbol (str)
        close_price (Decimal)
        open_price (Decimal)
        high_price (Decimal)
        low_price (Decimal)
        base_volume (Decimal): total traded base asset volume
        quote_volume (Decimal): total traded quote asset volume
    """

    event_type: Literal["24hrMiniTicker"]
    event_time: int
    symbol: str
    close_price: Decimal
    open_price: Decimal
    high_price: Decimal
    low_price: Decimal
    base_volume: Decimal
    quote_volume: Decimal


BinanceSocketSpotMiniTickersEventJson = List[BinanceSocketSpotMiniTickerEventJson]
BinanceSocketSpotMiniTickersEvent = List[BinanceSocketSpotMiniTickerEventModel]
