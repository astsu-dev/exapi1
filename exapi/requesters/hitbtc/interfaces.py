"""Has interfaces for hitbtc requesters."""

from types import TracebackType
from typing import Optional, Protocol, Type


class IHitbtcRequester(Protocol):
    """Has the context manager for close session."""

    async def __aenter__(self) -> "IHitbtcRequester":
        ...

    async def __aexit__(self,
                        exc_type: Optional[Type[BaseException]],
                        exc_val: Optional[BaseException],
                        exc_tb: Optional[TracebackType],
                        ) -> None:
        ...
