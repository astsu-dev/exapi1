from typing import Protocol

from exapi.auth.binance.typedefs import BinanceAuthHeaders


class IBinanceKeyAuth(Protocol):
    """Has methods for adds api key to headers."""

    def sign(self) -> BinanceAuthHeaders:
        """Returns headers with X-MBX-APIKEY header which contains api key.

        Returns:
            BinanceAuthHeaders
        """
