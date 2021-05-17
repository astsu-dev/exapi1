from dataclasses import dataclass
from decimal import Decimal
from typing import List, TypedDict


class BinanceSocketSpotBookTickerEventJson(TypedDict):
    """Binance socket spot individual symbol book ticker event json.

    From @bookTicker endpoint.

    Fields:
        u (int): order book update id
        s (str): symbol
        b (str): best bid price
        B (str): best bid quantity
        a (str): best ask price
        A (str): best ask quantity
    """

    u: int
    s: str
    b: str
    B: str
    a: str
    A: str


@dataclass(frozen=True)
class BinanceSocketSpotBookTickerEventModel:
    """Binance socket spot individual symbol book ticker event model.

    From @bookTicker endpoint.

    Fields:
        update_id (int): order book update id
        symbol (str)
        best_bid_price (Decimal)
        best_bid_quantity (Decimal)
        best_ask_price (Decimal)
        best_ask_quantity (Decimal)
    """

    update_id: int
    symbol: str
    best_bid_price: Decimal
    best_bid_quantity: Decimal
    best_ask_price: Decimal
    best_ask_quantity: Decimal


BinanceSocketSpotBookTickersEventJson = List[BinanceSocketSpotBookTickerEventJson]
BinanceSocketSpotBookTickersEvent = List[BinanceSocketSpotBookTickerEventModel]
