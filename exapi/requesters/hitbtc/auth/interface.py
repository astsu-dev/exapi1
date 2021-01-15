"""Has hitbtc authorizator interface."""

from typing import Protocol

from exapi.requesters.typedefs import Headers
from yarl import URL


class IHitbtcAuth(Protocol):
    """Has methods for authorize a request to exchange."""

    def sign(self, method: str, url: URL, body: str) -> Headers:
        """Returns headers with the Authorization header.

        Args:
            method (str): http method.
            url (URL): http url.
            body (str): http body.

        Returns:
            Headers
        """
