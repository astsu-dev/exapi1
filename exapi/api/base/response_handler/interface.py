"""Has base response handler interface."""

from typing import Any, Protocol

from exapi.requesters.typedefs import RequesterResponse


class IBaseResponseHandler(Protocol):
    """Has methods for handle aiohttp response."""

    async def handle_response(self, response: RequesterResponse) -> Any:
        """Handles response.

        Checks a http status code.
        Checks a response json.

        Returns a json from response.

        Args:
            response (RequesterResponse)

        Returns:
            Any: json from response.
        """
