"""Has hitbtc api exceptions."""

from exapi.api.exceptions import BaseExchangeError

from .error_code import HitbtcErrorCode
from .models.error import HitbtcErrorModel


class HitbtcError(BaseExchangeError):
    """Will be raised if response is not success.

    Has code field, which has error code enum.
    Has error field, which has whole error.
    """

    def __init__(self, code: HitbtcErrorCode, error: HitbtcErrorModel) -> None:
        self._code = code
        self._error = error

    @property
    def code(self) -> HitbtcErrorCode:
        return self._code

    @property
    def error(self) -> HitbtcErrorModel:
        return self._error
