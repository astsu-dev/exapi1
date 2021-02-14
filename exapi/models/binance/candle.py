"""Has binance candle model."""

from dataclasses import dataclass
from decimal import Decimal
from typing import List, Tuple

BinanceCandleJson = Tuple[
    int,
    str,
    str,
    str,
    str,
    str,
    int,
    str,
    int,
    str,
    str,
    str
]


@dataclass(frozen=True)
class BinanceCandleModel:
    """Binance candle model.

    Args:
        open_time (int)
        open (Decimal)
        high (Decimal)
        low (Decimal)
        close (Decimal)
        volume (Decimal)
        close_time (int)
        quote_volume (Decimal)
        trades_num (int)
        taker_buy_base_volume (Decimal)
        taker_buy_quote_volume (Decimal)
        ignore (Decimal)
    """

    open_time: int
    open: Decimal
    high: Decimal
    low: Decimal
    close: Decimal
    volume: Decimal
    close_time: int
    quote_volume: Decimal
    trades_num: int
    taker_buy_base_volume: Decimal
    taker_buy_quote_volume: Decimal
    ignore: Decimal


BinanceCandlesJson = List[BinanceCandleJson]
BinanceCandles = List[BinanceCandleModel]
