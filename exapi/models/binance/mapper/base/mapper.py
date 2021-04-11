from exapi.models.binance import BinanceErrorJson, BinanceErrorModel

from exapi.models.binance.mapper.base.interface import IBinanceBaseModelsMapper


class BinanceBaseModelsMapper(IBinanceBaseModelsMapper):
    """Binance base models mapper.

    Maps json to models.
    """

    def map_to_error(self, error_json: BinanceErrorJson) -> BinanceErrorModel:
        """Maps error json to error model.

        Args:
            error_json (BinanceErrorJson)

        Returns:
            BinanceErrorModel
        """

        return BinanceErrorModel(code=error_json["code"], msg=error_json["msg"])
