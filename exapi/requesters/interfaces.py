"""Has interfaces for exchange requesters."""

from types import TracebackType
from typing import Optional, Protocol, Type

from exapi.typedefs import T


class IBaseRequester(Protocol):
    """Has the context manager for close session."""

    async def __aenter__(self: T) -> T:
        ...

    async def __aexit__(self,
                        exc_type: Optional[Type[BaseException]],
                        exc_val: Optional[BaseException],
                        exc_tb: Optional[TracebackType],
                        ) -> None:
        ...
