"""Has abstract requester classes for hitbtc requesters."""

from typing import Final

from exapi.requesters.base import BaseRequester


class HitbtcBaseRequester(BaseRequester):
    """Hitbtc base requester.

    Has ROOT_URL field which contains hitbtc api url.
    """

    ROOT_URL: Final[str] = "https://api.hitbtc.com/api/2"
