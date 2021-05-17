from dataclasses import dataclass
from decimal import Decimal
from typing import List, Literal, TypedDict


class BinanceSocketSpotAssetBalanceJson(TypedDict):
    """Binance socket spot asset balance json.

    From user data stream.

    Fields:
        a (str): asset
        f (str): free
        l (str): locked
    """

    a: str
    f: str
    l: str


@dataclass(frozen=True)
class BinanceSocketSpotAssetBalanceModel:
    """Binance socket spot asset balance model.

    From user data stream.

    Fields:
        asset (str)
        free (Decimal)
        locked (Decimal)
    """

    asset: str
    free: Decimal
    locked: Decimal


class BinanceSocketSpotAccountUpdateEventJson(TypedDict):
    """Binance socket spot account update event json.

    From user data stream.

    Fields:
        e (Literal["outboundAccountPosition"]): event type
        E (int): event time
        u (int): time of last account update
        B (List[BinanceSocketSpotAssetBalanceJson]): list of balances
    """

    e: Literal["outboundAccountPosition"]
    E: int
    u: int
    B: List[BinanceSocketSpotAssetBalanceJson]


@dataclass(frozen=True)
class BinanceSocketSpotAccountUpdateEventModel:
    """Binance socket spot account update event model.

    From user data stream.

    Fields:
        event_type (Literal["outboundAccountPosition"])
        event_time (int)
        last_update_time (int): time of last account update
        balances (List[BinanceSocketSpotAssetBalanceJson])
    """

    event_type: Literal["outboundAccountPosition"]
    event_time: int
    last_update_time: int
    balances: List[BinanceSocketSpotAssetBalanceJson]
