"""Has interfaces for hitbtc requesters."""

from typing import Optional

import aiohttp
from exapi.requesters.interfaces import IBaseRequester


class IHitbtcPublicRequester(IBaseRequester):
    """Hitbtc public requester interface
    which inherites base requester interface.

    Handles session in init.
    """

    def __init__(self, session: Optional[aiohttp.ClientSession] = None) -> None:
        ...
