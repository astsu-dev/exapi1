"""Has binance models mapper interface."""

from exapi.models.binance import (BinanceAccountInfoJson,
                                  BinanceAccountInfoModel,
                                  BinanceAccountTrades,
                                  BinanceAccountTradesJson,
                                  BinanceCanceledOrderJson,
                                  BinanceCanceledOrderModel,
                                  BinanceCanceledOrders,
                                  BinanceCanceledOrdersJson,
                                  BinanceOrderInfoJson, BinanceOrderInfoModel,
                                  BinanceOrderInfos, BinanceOrderInfosJson,
                                  BinanceOrderJson, BinanceOrderModel,
                                  BinanceOrders, BinanceOrdersJson,
                                  BinanceTestOrderJson, BinanceTestOrderModel)
from exapi.models_mappers.binance.base import IBinanceBaseModelsMapper


class IBinanceSpotTradingModelsMapper(IBinanceBaseModelsMapper):
    """Binance trading models mapper interface.

    Maps json to models.
    """

    def map_to_test_order(self, json: BinanceTestOrderJson) -> BinanceTestOrderModel:
        """Maps test order json to test order model.

        Args:
            json (BinanceTestOrderJson)

        Returns:
            BinanceTestOrderModel
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

    def map_to_canceled_order(self, json: BinanceCanceledOrderJson) -> BinanceCanceledOrderModel:
        """Maps order json to order model.

        Args:
            json (BinanceCanceledOrderJson)

        Returns:
            BinanceCanceledOrderModel
        """

    def map_to_canceled_orders(self, json: BinanceCanceledOrdersJson) -> BinanceCanceledOrders:
        """Maps orders json to orders model.

        Args:
            json (BinanceCanceledOrdersJson)

        Returns:
            BinanceCanceledOrders
        """

    def map_to_order_info(self, json: BinanceOrderInfoJson) -> BinanceOrderInfoModel:
        """Maps order info json to order info model.

        Args:
            json (BinanceOrderInfoJson)

        Returns:
            BinanceOrderInfoModel
        """

    def map_to_order_infos(self, json: BinanceOrderInfosJson) -> BinanceOrderInfos:
        """Maps order infos json to order infos model.

        Args:
            json (BinanceOrderInfosJson)

        Returns:
            BinanceOrderInfos
        """

    def map_to_account_info(self, json: BinanceAccountInfoJson) -> BinanceAccountInfoModel:
        """Maps account info json to account info model.

        Args:
            json (BinanceAccountInfoJson)

        Returns:
            BinanceAccountInfoModel
        """

    def map_to_account_trades(self, json: BinanceAccountTradesJson) -> BinanceAccountTrades:
        """Maps account trades json to account trades models.

        Args:
            json (BinanceAccountTradesJson)

        Returns:
            BinanceAccountTrades
        """
