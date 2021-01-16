"""Has abstract base classes for exchange requesters."""

import abc
from types import TracebackType
from typing import Optional, Type, cast

import aiohttp
from exapi.typedefs import T

from .interfaces import IBaseRequester


class BaseRequester(abc.ABC, IBaseRequester):
    """Has the context manager for close session."""

    _session: aiohttp.ClientSession

    async def __aenter__(self: T) -> T:
        await cast(BaseRequester, self)._session.__aenter__()
        return self

    async def __aexit__(self,
                        exc_type: Optional[Type[BaseException]],
                        exc_val: Optional[BaseException],
                        exc_tb: Optional[TracebackType],
                        ) -> None:
        await self._session.__aexit__(exc_type, exc_val, exc_tb)
