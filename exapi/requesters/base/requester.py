"""Has abstract base classes for exchange requesters."""

import abc
from typing import Any, Optional

import aiohttp
from yarl import URL

from exapi.requesters.base.interface import IBaseRequester
from exapi.requesters.typedefs import Headers, RequesterResponse, Session


class BaseRequester(abc.ABC, IBaseRequester):
    """Has the context manager for close session."""

    def __init__(self, session: Session) -> None:
        self._session = session

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

        session = self._session
        res = await session.request(method, url, headers=headers,
                                    data=data, json=json, timeout=timeout)
        return res
