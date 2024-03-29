"""Has binance auth result dataclass."""

from dataclasses import dataclass

from exapi.auth.binance.typedefs import BinanceAuthHeaders
from exapi.requesters.typedefs import Params


@dataclass(frozen=True)
class BinanceAuthResult:
    """Binance auth result.

    Args:
        headers (BinanceAuthHeaders): headers with api key.
        params (Params): params with signature.
    """

    headers: BinanceAuthHeaders
    params: Params
