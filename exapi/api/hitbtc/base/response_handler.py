"""Has base hitbtc response handler."""

from typing import Any, Optional, Union

from exapi.api.base import BaseResponseHandler
from exapi.api.hitbtc.exceptions import HitbtcError
from exapi.api.hitbtc.models import (HitbtcRawDetailedErrorModel,
                                     HitbtcRawErrorModel)
from exapi.requesters.typedefs import RequesterResponse

from .models_mapper import HitbtcBaseModelsMapper, IHitbtcBaseModelsMapper


class HitbtcBaseResponseHandler(BaseResponseHandler):
    """Has methods for handle aiohttp response."""

    def __init__(self, models_mapper: Optional[IHitbtcBaseModelsMapper] = None,
                 json_content_type: Optional[str] = "application/json"
                 ) -> None:
        self._models_mapper = (
            models_mapper if models_mapper is not None else HitbtcBaseModelsMapper())
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

        Raises:
            HitbtcError: will be raised if response is error.

        Returns:
            Any
        """

        if not isinstance(response, dict) and "error" not in response:
            return None

        raw_error: Union[HitbtcRawDetailedErrorModel,
                         HitbtcRawErrorModel] = response["error"]
        error = self._models_mapper.map_to_error(raw_error)
        raise HitbtcError(error.code, error)
