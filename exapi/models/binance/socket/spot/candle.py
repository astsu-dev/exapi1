from dataclasses import dataclass
from typing import TypedDict, Literal
from decimal import Decimal
from exapi.typedefs.binance import CandleInterval


class BinanceSocketSpotCandleJson(TypedDict):
    """Binance spot market data stream candle json.

    Fields:
        t (int): candle start time
        T (int): candle close time
        s (str): symbol
        i (CandleInterval): interval
        f (int): first trade id
        L (int): last trade id
        o (str): open price
        c (str): close price
        h (str): high price
        l (str): low price
        v (str): base asset volume
        n (int): number of trades
        x (bool): is this kline closed?
        q (str): quote asset volume
        V (str): taker buy base asset volume
        Q (str): taker buy quote asset volume
        B (str): ignore
    """

    t: int
    T: int
    s: str
    i: CandleInterval
    f: int
    L: int
    o: str
    c: str
    h: str
    l: str
    v: str
    n: int
    x: bool
    q: str
    V: str
    Q: str
    B: str


@dataclass(frozen=True)
class BinanceSocketSpotCandleModel:
    """Binance spot market data stream candle model.

    Fields:
        t (int): candle start time
        T (int): candle close time
        s (str): symbol
        i (CandleInterval): interval
        f (int): first trade id
        L (int): last trade id
        o (str): open price
        c (str): close price
        h (str): high price
        l (str): low price
        v (str): base asset volume
        n (int): number of trades
        x (bool): is this kline closed?
        q (str): quote asset volume
        V (str): taker buy base asset volume
        Q (str): taker buy quote asset volume
        B (str): ignore
    """

    start_time: int
    close_time: int
    symbol: str
    interval: CandleInterval
    first_trade_id: int
    last_trade_id: int
    open_price: Decimal
    close_price: Decimal
    high_price: Decimal
    low_price: Decimal
    base_asset_volume: Decimal
    num_trades: int
    closed: bool
    quote_asset_volume: Decimal
    taker_buy_base_asset_volume: Decimal
    taker_buy_quote_asset_volume: Decimal


class BinanceSocketSpotCandleEventJson(TypedDict):
    e: Literal["kline"]
    E: int
    s: str
    k: BinanceSocketSpotCandleJson


@dataclass(frozen=True)
class BinanceSocketSpotCandleEventModel:
    event_type: Literal["kline"]
    event_time: int
    symbol: str
    candle: BinanceSocketSpotCandleModel
