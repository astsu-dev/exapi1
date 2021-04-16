"""Has hitbtc api exceptions."""

from exapi.exceptions.base import BaseExchangeError
from exapi.models.hitbtc import HitbtcErrorModel


class HitbtcError(BaseExchangeError):
    """Will be raised if response is not success.

    Has code field, which has error code enum.
    Has error field, which has whole error.
    """

    def __init__(self, code: int, error: HitbtcErrorModel) -> None:
        """Class initialization.

        Args:
            code (HitbtcErrorCode): error code.
            error (HitbtcErrorModel): full error.
        """

        self._code = code
        self._error = error

    @property
    def code(self) -> int:
        return self._code

    @property
    def error(self) -> HitbtcErrorModel:
        return self._error
