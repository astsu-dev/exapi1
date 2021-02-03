"""Has base requester interface."""

from typing import Any, Optional, Protocol

import aiohttp
from exapi.requesters.typedefs import Headers, RequesterResponse
from yarl import URL


class IBaseRequester(Protocol):
    """Has the context manager for close session."""

    async def request(self, method: str,
                      url: URL,
                      *,
                      headers: Optional[Headers] = None,
                      data: Any = None,
                      json: Any = None,
                      timeout: Optional[aiohttp.ClientTimeout] = None
                      ) -> RequesterResponse:
        """Wrapper over aiohttp session request.

        Args:
            method (str)
            url (URL)
            headers (Headers)
            data (Any)
            json (Any)
            timeout (aiohttp.ClientTimeout): request timeout.

        Returns:
            RequesterResponse: aiohttp client response.
        """
