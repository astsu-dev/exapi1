"""Has base hitbtc response handler."""

from typing import Any, Optional, Union

from exapi.response_handlers.base import BaseResponseHandler
from exapi.exceptions.hitbtc import HitbtcError
from exapi.models.hitbtc import (HitbtcRawDetailedErrorModel,
                                 HitbtcRawErrorModel)
from exapi.models_mappers.hitbtc.base import (HitbtcBaseModelsMapper,
                                              IHitbtcBaseModelsMapper)
from exapi.requesters.typedefs import RequesterResponse


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

        Ignores http errors. Error must be handled in json checking.

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

        if not isinstance(response, dict) or "error" not in response:
            return None

        raw_error: Union[HitbtcRawDetailedErrorModel,
                         HitbtcRawErrorModel] = response["error"]
        error = self._models_mapper.map_to_error(raw_error)
        raise HitbtcError(error.code, error)
