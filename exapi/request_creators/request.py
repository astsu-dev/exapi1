"""Has Request data class."""

from dataclasses import dataclass
from typing import Any, Optional

from yarl import URL

from exapi.requesters.typedefs import Headers


@dataclass(frozen=True)
class Request:
    """Has data for aiohttp request."""

    method: str
    url: URL
    headers: Optional[Headers] = None
    data: Any = None
    json: Any = None
