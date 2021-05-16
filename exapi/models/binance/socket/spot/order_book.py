from dataclasses import dataclass
from decimal import Decimal
from typing import List, Literal, Tuple, TypedDict

BinanceSocketSpotOrderBookOrderJson = Tuple[str, str]


class BinanceSocketSpotPartialOrderBookEventJson(TypedDict):
    """Binance socket spot partial order book event json.

    From <symbol>@depth<levels> endpoint.

    Fields:
        lastUpdateId (int): last update id
        bids (List[BinanceSocketSpotOrderBookOrderJson]): bids to be updated
        asks (List[BinanceSocketSpotOrderBookOrderJson]): asks to be updated
    """

    lastUpdateId: int
    bids: List[BinanceSocketSpotOrderBookOrderJson]
    asks: List[BinanceSocketSpotOrderBookOrderJson]


@dataclass(frozen=True)
class BinanceSocketSpotOrderBookOrderModel:
    """Binance socket spot order book order model.

    Fields:
        price (Decimal)
        quantity (Decimal)
    """

    price: Decimal
    quantity: Decimal


@dataclass(frozen=True)
class BinanceSocketSpotPartialOrderBookEventModel:
    """Binance socket spot partial order book event json.

    From <symbol>@depth<levels> endpoint.

    Fields:
        last_update_id (int)
        bids (List[BinanceSocketSpotOrderBookOrderModel]): bids to be updated
        asks (List[BinanceSocketSpotOrderBookOrderModel]): asks to be updated
    """

    last_update_id: int
    bids: List[BinanceSocketSpotOrderBookOrderModel]
    asks: List[BinanceSocketSpotOrderBookOrderModel]


class BinanceSocketSpotDiffOrderBookEventJson(TypedDict):
    """Binance socket spot diff. order book event json.

    From <symbol>@depth endpoint.

    Fields:
        e (Literal["depthUpdate"]): event type
        E (int): event time
        s (str): symbol
        U (int): first update id
        u (int): final update id
        b (List[BinanceSocketSpotOrderBookOrderJson]): bids to be updated
        a (List[BinanceSocketSpotOrderBookOrderJson]): asks to be updated
    """

    e: Literal["depthUpdate"]
    E: int
    s: str
    U: int
    u: int
    b: List[BinanceSocketSpotOrderBookOrderJson]
    a: List[BinanceSocketSpotOrderBookOrderJson]


@dataclass(frozen=True)
class BinanceSocketSpotDiffOrderBookEventModel:
    """Binance socket spot diff. order book event model.

    From <symbol>@depth endpoint.

    If the quantity is 0, then need to remove order.

    Fields:
        event_type (Literal["depthUpdate"])
        event_time (int)
        symbol (str)
        first_update_id (int)
        final_update_id (int)
        bids (List[BinanceSocketSpotOrderBookOrderModel])
        asks (List[BinanceSocketSpotOrderBookOrderModel])
    """

    event_type: Literal["depthUpdate"]
    event_time: int
    symbol: str
    first_update_id: int
    final_update_id: int
    bids: List[BinanceSocketSpotOrderBookOrderModel]
    asks: List[BinanceSocketSpotOrderBookOrderModel]
