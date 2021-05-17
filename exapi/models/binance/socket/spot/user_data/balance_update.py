from dataclasses import dataclass
from decimal import Decimal
from typing import Literal, TypedDict


class BinanceSocketSpotBalanceUpdateEventJson(TypedDict):
    """Binance socket spot balance update event json.

    From user data stream.

    Fields:
        e (Literal["balanceUpdate"]): event type
        E (int): event time
        a (str): asset
        d (str): balance delta
        T (int): clear time
    """

    e: Literal["balanceUpdate"]
    E: int
    a: str
    d: str
    T: int


@dataclass(frozen=True)
class BinanceSocketSpotBalanceUpdateEventModel:
    """Binance socket spot balance update event model.

    From user data stream.

    Fields:
        e (Literal["balanceUpdate"]): event type
        E (int): event time
        a (str): asset
        d (str): balance delta
        T (int): clear time
    """

    event_type: Literal["balanceUpdate"]
    event_time: int
    asset: str
    delta: Decimal
    clear_time: int
