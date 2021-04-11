from exapi.api.exceptions import BaseExchangeError
from exapi.models.binance import BinanceErrorModel


class BinanceError(BaseExchangeError):
    """Will be raised if response is not success.

    Has code field, which has error code enum.
    Has error field, which has whole error.
    """

    def __init__(self, code: int, error: BinanceErrorModel) -> None:
        self._code = code
        self._error = error

    @property
    def code(self) -> int:
        return self._code

    @property
    def error(self) -> BinanceErrorModel:
        return self._error
