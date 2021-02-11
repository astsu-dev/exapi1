"""Has binance 24 hour ticker price change statistics model."""

from dataclasses import dataclass
from decimal import Decimal
from typing import List, TypedDict


class BinanceTickerPriceChangeStatJson(TypedDict):
    symbol: str
    priceChange: str
    weightedAvgPrice: str
    prevClosePrice: str
    lastPrice: str
    lastQty: str
    bidPrice: str
    askPrice: str
    openPrice: str
    highPrice: str
    lowPrice: str
    volume: str
    quoteVolume: str
    openTime: int
    closeTime: int
    firstId: int
    lastId: int
    count: int


@dataclass(frozen=True)
class BinanceTickerPriceChangeStatModel:
    """Binance 24 hour ticker price change statistics model.

    Args:
        symbol (str)
        price_change (Decimal)
        weighted_avg_price (Decimal)
        prev_close_price (Decimal)
        last_price (Decimal)
        last_qty (Decimal)
        bid_price (Decimal)
        ask_price (Decimal)
        open_price (Decimal)
        high_price (Decimal)
        low_price (Decimal)
        volume (Decimal)
        quote_volume (Decimal)
        open_time (int)
        close_time (int)
        first_id (int)
        last_id (int)
        count (int)
    """

    symbol: str
    price_change: Decimal
    weighted_avg_price: Decimal
    prev_close_price: Decimal
    last_price: Decimal
    last_qty: Decimal
    bid_price: Decimal
    ask_price: Decimal
    open_price: Decimal
    high_price: Decimal
    low_price: Decimal
    volume: Decimal
    quote_volume: Decimal
    open_time: int
    close_time: int
    first_id: int
    last_id: int
    count: int


BinanceTickersPriceChangeStatJson = List[BinanceTickerPriceChangeStatJson]
BinanceTickersPriceChangeStat = List[BinanceTickerPriceChangeStatModel]
