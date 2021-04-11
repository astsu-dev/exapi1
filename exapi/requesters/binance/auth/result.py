"""Has binance auth result dataclass."""

from dataclasses import dataclass

from exapi.requesters.typedefs import Params

from exapi.requesters.binance.auth.typedefs import BinanceAuthHeaders


@dataclass(frozen=True)
class BinanceAuthResult:
    """Binance auth result.

    Args:
        headers (BinanceAuthHeaders): headers with api key.
        params (Params): params with signature.
    """

    headers: BinanceAuthHeaders
    params: Params
