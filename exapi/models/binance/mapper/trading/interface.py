"""Has binance models mapper interface."""

from exapi.models.binance import (BinanceAccountInfoJson,
                                  BinanceAccountInfoModel, BinanceOrderJson,
                                  BinanceOrderModel, BinanceOrders,
                                  BinanceOrdersJson)
from exapi.models.binance.mapper.base import IBinanceBaseModelsMapper


class IBinanceTradingModelsMapper(IBinanceBaseModelsMapper):
    """Binance trading models mapper interface.

    Maps json to models.
    """

    def map_to_order(self, json: BinanceOrderJson) -> BinanceOrderModel:
        """Maps order json to order model.

        Args:
            json (BinanceOrderJson)

        Returns:
            BinanceOrderModel
        """

    def map_to_orders(self, json: BinanceOrdersJson) -> BinanceOrders:
        """Maps orders json to orders model.

        Args:
            json (BinanceOrdersJson)

        Returns:
            BinanceOrders
        """

    def map_to_account_info(self, json: BinanceAccountInfoJson) -> BinanceAccountInfoModel:
        """Maps account info json to account info model.

        Args:
            json (BinanceAccountInfoJson)

        Returns:
            BinanceAccountInfoModel
        """

    # TODO: Add account trades
