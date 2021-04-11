"""Has binance auth interface."""

from typing import Protocol

from exapi.requesters.binance.auth.result import BinanceAuthResult
from exapi.requesters.typedefs import Params


class IBinanceAuth(Protocol):
    """Has methods for auth requests to binance api."""

    def sign(self, params: Params, body: str = "") -> BinanceAuthResult:
        """Returns headers with api key and query string with signature.

        Args:
            params (Params): request params.

        Returns:
            BinanceAuthResult
        """
