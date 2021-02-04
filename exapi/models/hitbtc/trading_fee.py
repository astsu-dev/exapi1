from dataclasses import dataclass
from decimal import Decimal
from typing import TypedDict


class HitbtcRawTradingFeeModel(TypedDict):
    """Trading fee json model."""

    take_liquidity_rate: str
    provide_liquidity_rate: str


@dataclass(frozen=True)
class HitbtcTradingFeeModel:
    """Trading fee model for certain symbol.

    Args:
        take_liquidity_rate (Decimal): taker fee
        provide_liquidity_rate (Decimal): maker fee
    """

    take_liquidity_rate: Decimal
    provide_liquidity_rate: Decimal
