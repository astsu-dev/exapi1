"""Has abstract base classes for exchange requesters."""

import abc
from types import TracebackType
from typing import Any, Optional, Type, cast

import aiohttp
from exapi.typedefs import T
from yarl import URL

from .interfaces import IBaseRequester
from .typedefs import Headers, RequesterResponse


class BaseRequester(abc.ABC, IBaseRequester):
    """Has the context manager for close session."""

    _session: aiohttp.ClientSession

    async def _request(self, method: str,
                       url: URL,
                       *,
                       headers: Optional[Headers] = None,
                       data: Any = None,
                       json: Any = None,
                       timeout: Optional[aiohttp.ClientTimeout] = None
                       ) -> RequesterResponse:
        """Wrapper over aiohttp session request.

        Uses session from _session field.

        Args:
            method (str)
            url (URL)
            headers (Headers)
            data (Any)
            json (Any)
            timeout (aiohttp.ClientTimeout)

        Returns:
            RequesterResponse: aiohttp client response.
        """

        session = self._session
        res = await session.request(method, url, headers=headers, data=data,
                                    json=json, timeout=timeout)
        return res

    async def __aenter__(self: T) -> T:
        await cast(BaseRequester, self)._session.__aenter__()
        return self

    async def __aexit__(self,
                        exc_type: Optional[Type[BaseException]],
                        exc_val: Optional[BaseException],
                        exc_tb: Optional[TracebackType],
                        ) -> None:
        await self._session.__aexit__(exc_type, exc_val, exc_tb)
