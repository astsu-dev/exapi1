"""Has hitbtc base request creator."""

import abc
from typing import Final


class HitbtcBaseRequestCreator(abc.ABC):
    """Hitbtc base request creator.

    Has ROOT_URL field which contains root hitbtc api url.
    """

    ROOT_URI: Final[str] = "https://api.hitbtc.com"
    ROOT_URL: Final[str] = ROOT_URI + "/api/2"
    base_url: str = ROOT_URL

    def _create_url(self, path: str) -> str:
        return self.base_url + path
