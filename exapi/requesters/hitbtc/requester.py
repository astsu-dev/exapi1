"""Has abstract requester classes for hitbtc requesters."""

from typing import Optional

import aiohttp
from exapi.requesters.requester import BaseRequester


class HitbtcPublicRequester(BaseRequester):
    """Hitbtc public requester which inherites base requester.

    Handles session in init.
    """

    def __init__(self, session: Optional[aiohttp.ClientSession] = None) -> None:
        self._session = session if session is not None else aiohttp.ClientSession()
