from exapi.requesters.binance.auth.typedefs import BinanceAuthHeaders

from exapi.requesters.binance.auth.key.interface import IBinanceKeyAuth


class BinanceKeyAuth(IBinanceKeyAuth):
    """Has methods for adds api key to headers."""

    def __init__(self, api_key: str) -> None:
        self._api_key = api_key

    def sign(self) -> BinanceAuthHeaders:
        """Returns headers with X-MBX-APIKEY header which contains api key.

        Returns:
            BinanceAuthHeaders
        """

        headers: BinanceAuthHeaders = {
            "X-MBX-APIKEY": self._api_key
        }

        return headers
