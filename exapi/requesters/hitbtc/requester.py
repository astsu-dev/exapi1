"""Has abstract requester classes for hitbtc requesters."""

from typing import Final, Optional

import aiohttp
from exapi.requesters.requester import BaseRequester


class HitbtcBaseRequester(BaseRequester):
    """Hitbtc base requester.

    Has ROOT_URL field which contains hitbtc api url.
    """

    ROOT_URL: Final[str] = "https://api.hitbtc.com/api/2"


class HitbtcBasePublicRequester(HitbtcBaseRequester):
    """Hitbtc public requester which inherites hitbtc base requester.

    Handles session in init.
    """

    def __init__(self, session: Optional[aiohttp.ClientSession] = None) -> None:
        self._session = session if session is not None else aiohttp.ClientSession()
