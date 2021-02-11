"""Has binance candle model."""

from dataclasses import dataclass
from typing import List, Union

BinanceCandleJson = List[
    Union[
        int,
        str
    ]
]


@dataclass(frozen=True)
class BinanceCandleModel:
    """Binance candle model.

    Args:
        open_time (int)
        open (str)
        high (str)
        low (str)
        close (str)
        volume (str)
        close_time (int)
        quote_volume (str)
        trades_num (int)
        taker_buy_base_volume (str)
        taker_buy_quote_voluem (str)
        ignore (str)
    """

    open_time: int
    open: str
    high: str
    low: str
    close: str
    volume: str
    close_time: int
    quote_volume: str
    trades_num: int
    taker_buy_base_volume: str
    taker_buy_quote_voluem: str
    ignore: str


BinanceCandlesJson = List[BinanceCandleJson]
BinanceCandles = List[BinanceCandleModel]
