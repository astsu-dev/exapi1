import abc
from typing import Final


class BinanceBaseRequestCreator(abc.ABC):
    """Binance base request creator."""

    ROOT_URI: Final[str] = "https://api.binance.com"
    ROOT_URL: Final[str] = ROOT_URI + "/api/v3"

    def _create_url(self, path: str) -> str:
        return self.ROOT_URL + path
