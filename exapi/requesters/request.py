"""Has Request data class."""

from dataclasses import dataclass
from typing import Any, Optional

from exapi.requesters.typedefs import Headers
from yarl import URL


@dataclass(frozen=True)
class Request:
    """Has data for aiohttp request."""

    method: str
    url: URL
    headers: Optional[Headers] = None
    params: Optional[Headers] = None
    data: Any = None
    json: Any = None
