from typing import Protocol

from exapi.models.binance import BinanceErrorJson, BinanceErrorModel


class IBinanceBaseModelsMapper(Protocol):
    def map_to_error(self, error_json: BinanceErrorJson) -> BinanceErrorModel:
        """Maps error json to error model.

        Args:
            error_json (BinanceErrorJson)

        Returns:
            BinanceErrorModel
        """
