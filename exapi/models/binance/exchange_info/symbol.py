"""Has binance symbol model."""

from dataclasses import dataclass
from typing import List, TypedDict

from exapi.typedefs.binance import (OrderTypes, SymbolPermissions,
                                    SymbolStatus)

from .filters.symbol import BinanceSymbolFilters, BinanceSymbolFiltersJson


class BinanceSymbolJson(TypedDict):
    symbol: str
    status: SymbolStatus
    baseAsset: str
    baseAssetPrecision: int
    quoteAsset: str
    quotePrecision: int
    quoteAssetPrecision: int
    orderTypes: OrderTypes
    icebergAllowed: bool
    ocoAllowed: bool
    isSpotTradingAllowed: bool
    isMarginTradingAllowed: bool
    filters: BinanceSymbolFiltersJson
    permissions: SymbolPermissions


@dataclass(frozen=True)
class BinanceSymbolModel:
    """Binance symbol model.

    Args:
        symbol (str)
        status (SymbolStatus)
        base_asset (str)
        base_asset_precision (int)
        quote_asset (str)
        quote_precision (int)
        quote_asset_precision (int)
        order_types (OrderTypes): allowed order types.
        iceberg_allowed (bool)
        oco_allowed (bool)
        is_spot_trading_allowed (bool)
        is_margin_trading_allowed (bool)
        filters (BinanceSymbolFilters): symbol rules.
        permissions (SymbolPermissions)
    """

    symbol: str
    status: SymbolStatus
    base_asset: str
    base_asset_precision: int
    quote_asset: str
    quote_precision: int
    quote_asset_precision: int
    order_types: OrderTypes
    iceberg_allowed: bool
    oco_allowed: bool
    is_spot_trading_allowed: bool
    is_margin_trading_allowed: bool
    filters: BinanceSymbolFilters
    permissions: SymbolPermissions


BinanceSymbolsJson = List[BinanceSymbolJson]
BinanceSymbols = List[BinanceSymbolModel]
