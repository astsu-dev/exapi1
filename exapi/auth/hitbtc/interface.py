"""Has hitbtc authorizator interface."""

from typing import Optional, Protocol

from exapi.auth.hitbtc.typedefs import HitbtcAuthHeaders


class IHitbtcAuth(Protocol):
    """Has methods for authorization a request to hitbtc."""

    def sign(self, method: str,
             url_path: str,
             url_query: str,
             body: Optional[str] = None
             ) -> HitbtcAuthHeaders:
        """Returns headers with the Authorization header.

        Args:
            method (str): http method.
            url_path (str): url path.
            url_query (str): url query.
            body (str): http body.

        Returns:
            HitbtcAuthHeaders
        """
