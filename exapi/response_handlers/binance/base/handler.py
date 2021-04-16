"""Has base binance response handler."""

from typing import Any, Optional, cast

from exapi.response_handlers.base import BaseResponseHandler
from exapi.exceptions.binance import BinanceError
from exapi.models.binance.error import BinanceErrorJson
from exapi.models_mappers.binance.base import (BinanceBaseModelsMapper,
                                               IBinanceBaseModelsMapper)
from exapi.requesters.typedefs import RequesterResponse


class BinanceBaseResponseHandler(BaseResponseHandler):
    """Has methods for handle aiohttp response."""

    def __init__(self, models_mapper: Optional[IBinanceBaseModelsMapper] = None,
                 json_content_type: Optional[str] = "application/json"
                 ) -> None:
        self._models_mapper = (
            models_mapper if models_mapper is not None else BinanceBaseModelsMapper())
        self._json_content_type = json_content_type

    def _check_response(self, response: RequesterResponse) -> None:
        """Checks a response (http code, headers, ...).

        Ignores http errors. Error must be handled in json checking.

        Args:
            response (RequesterResponse)
        """

        return None

    def _check_json_response(self, response: Any) -> None:
        """Checks a json from response.

        Args:
            response (Any): json response.

        Raises:
            BinanceError: will be raised if response is error.
        """

        if not isinstance(response, dict) or "code" not in response or "msg" not in response:
            return None

        json_error = cast(BinanceErrorJson, response)
        error = self._models_mapper.map_to_error(json_error)
        raise BinanceError(error.code, error)
