from typing import Protocol

from exapi.requesters.binance.auth.typedefs import BinanceAuthHeaders


class IBinanceKeyAuth(Protocol):
    """Has methods for adds api key to headers."""

    def sign(self) -> BinanceAuthHeaders:
        """Returns headers with X-MBX-APIKEY which contains api key.

        Returns:
            BinanceAuthHeaders
        """
