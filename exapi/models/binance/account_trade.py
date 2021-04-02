from dataclasses import dataclass
from decimal import Decimal
from typing import List, TypedDict


class BinanceAccountTradeJson(TypedDict):
    symbol: str
    id: int
    orderId: int
    orderListId: int
    price: str
    qty: str
    quoteQty: str
    commission: str
    commissionAsset: str
    time: int
    isBuyer: bool
    isMaker: bool
    isBestMatch: bool


@dataclass(frozen=True)
class BinanceAccountTradeModel:
    """Account trade model.

    Args:
        symbol (str)
        id (int)
        order_id (int)
        order_list_id (int)
        price (Decimal)
        qty (Decimal)
        quote_qty (Decimal)
        commission (Decimal)
        commission_asset (str)
        time (int)
        is_buyer (bool)
        is_maker (bool)
        is_best_match (bool)
    """

    symbol: str
    id: int
    order_id: int
    order_list_id: int
    price: Decimal
    qty: Decimal
    quote_qty: Decimal
    commission: Decimal
    commission_asset: str
    time: int
    is_buyer: bool
    is_maker: bool
    is_best_match: bool


BinanceAccountTrades = List[BinanceAccountTradeModel]
BinanceAccountTradesJson = List[BinanceAccountTradeJson]
