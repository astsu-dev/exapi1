"""Has base response handler."""

import abc
from typing import Any, Optional

from exapi.requesters.typedefs import RequesterResponse


class BaseResponseHandler(abc.ABC):
    """Has methods for handle aiohttp response."""

    _json_content_type: Optional[str] = "application/json"

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

        async with response:
            self._check_response(response)
            json_res = await response.json(content_type=self._json_content_type)
            self._check_json_response(json_res)
            return json_res

    @abc.abstractmethod
    def _check_response(self, response: RequesterResponse) -> Any:
        """Checks a response (http code, headers, ...).

        Args:
            response (RequesterResponse)

        Returns:
            Any
        """

        raise NotImplementedError

    @abc.abstractmethod
    def _check_json_response(self, response: RequesterResponse) -> Any:
        """Checks a json from response.

        Args:
            response (RequesterResponse)

        Returns:
            Any
        """

        raise NotImplementedError
