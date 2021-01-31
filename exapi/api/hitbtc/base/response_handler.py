"""Has base hitbtc response handler."""

from typing import Any, Optional

from exapi.api.base import BaseResponseHandler
from exapi.api.hitbtc.exceptions import HitbtcError
from exapi.api.hitbtc.models import HitbtcErrorModel
from exapi.requesters.typedefs import RequesterResponse


class HitbtcBaseResponseHandler(BaseResponseHandler):
    """Has methods for handle aiohttp response."""

    def __init__(self, json_content_type: Optional[str] = "application/json") -> None:
        self._json_content_type = json_content_type

    def _check_response(self, response: RequesterResponse) -> Any:
        """Checks a response (http code, headers, ...).

        Args:
            response (RequesterResponse)

        Returns:
            Any
        """

        return None

    def _check_json_response(self, response: Any) -> Any:
        """Checks a json from response.

        Args:
            response (Any): json response.

        Returns:
            Any
        """

        if not isinstance(response, dict) and "error" not in response:
            return None

        error = response["error"]
        code = int(error["code"])
        msg = error["message"]
        description = error.get("description")
        model = HitbtcErrorModel(code, msg, description)
        raise HitbtcError(code, model)
