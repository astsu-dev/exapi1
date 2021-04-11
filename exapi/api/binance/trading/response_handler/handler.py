"""Has binance trading response handler."""

from typing import Optional

from exapi.api.binance.base import BinanceBaseResponseHandler
from exapi.api.binance.trading.response_handler.interface import IBinanceTradingResponseHandler
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
                                  BinanceTestOrderJson, BinanceTestOrderModel)
from exapi.models.binance.mapper import BinanceModelsMapper
from exapi.models.binance.mapper.trading import IBinanceTradingModelsMapper
from exapi.requesters.typedefs import RequesterResponse


class BinanceTradingResponseHandler(BinanceBaseResponseHandler, IBinanceTradingResponseHandler):
    """Has methods for handling binance trading responses."""

    _models_mapper: IBinanceTradingModelsMapper

    def __init__(self, models_mapper: Optional[IBinanceTradingModelsMapper] = None,
                 json_content_type: Optional[str] = "application/json"
                 ) -> None:
        models_mapper = models_mapper if models_mapper is not None else BinanceModelsMapper()
        super().__init__(models_mapper, json_content_type)

    async def handle_new_test_order_response(self, res: RequesterResponse) -> BinanceTestOrderModel:
        """Handles new test order response.

        Returns a json converted to model.

        Args:
            res (RequesterResponse)

        Returns:
            BinanceTestOrderModel
        """

        json: BinanceTestOrderJson = await self.handle_response(res)
        return self._models_mapper.map_to_test_order(json)

    async def handle_new_order_response(self, res: RequesterResponse) -> BinanceOrderModel:
        """Handles new order response.

        Returns a json converted to model.

        Args:
            res (RequesterResponse)

        Returns:
            BinanceOrderModel
        """

        json: BinanceOrderJson = await self.handle_response(res)
        return self._models_mapper.map_to_order(json)

    async def handle_cancel_order_response(self, res: RequesterResponse) -> BinanceCanceledOrderModel:
        """Handles cancel order response.

        Returns a json converted to model.

        Args:
            res (RequesterResponse)

        Returns:
            BinanceCanceledOrderModel
        """

        json: BinanceCanceledOrderJson = await self.handle_response(res)
        return self._models_mapper.map_to_canceled_order(json)

    async def handle_cancel_orders_response(self, res: RequesterResponse) -> BinanceCanceledOrders:
        """Handles cancel orders response.

        Returns a json converted to model.

        Args:
            res (RequesterResponse)

        Returns:
            BinanceCanceledOrders
        """

        json: BinanceCanceledOrdersJson = await self.handle_response(res)
        return self._models_mapper.map_to_canceled_orders(json)

    async def handle_query_order_response(self, res: RequesterResponse) -> BinanceOrderInfoModel:
        """Handles query order response.

        Returns a json converted to model.

        Args:
            res (RequesterResponse)

        Returns:
            BinanceOrderInfoModel
        """

        json: BinanceOrderInfoJson = await self.handle_response(res)
        return self._models_mapper.map_to_order_info(json)

    async def handle_get_current_open_orders_response(self, res: RequesterResponse) -> BinanceOrderInfos:
        """Handles get current open orders response.

        Returns a json converted to model.

        Args:
            res (RequesterResponse)

        Returns:
            BinanceOrderInfos
        """

        json: BinanceOrderInfosJson = await self.handle_response(res)
        return self._models_mapper.map_to_order_infos(json)

    async def handle_get_all_orders_response(self, res: RequesterResponse) -> BinanceOrderInfos:
        """Handles get all orders response.

        Returns a json converted to model.

        Args:
            res (RequesterResponse)

        Returns:
            BinanceOrderInfos
        """

        json: BinanceOrderInfosJson = await self.handle_response(res)
        return self._models_mapper.map_to_order_infos(json)

    async def handle_get_account_info_response(self, res: RequesterResponse) -> BinanceAccountInfoModel:
        """Handles get account info response.

        Returns a json converted to model.

        Args:
            res (RequesterResponse)

        Returns:
            BinanceAccountInfoModel
        """

        json: BinanceAccountInfoJson = await self.handle_response(res)
        return self._models_mapper.map_to_account_info(json)

    async def handle_get_trades_response(self, res: RequesterResponse) -> BinanceAccountTrades:
        """Handles get trades response.

        Returns a json converted to model.

        Args:
            res (RequesterResponse)

        Returns:
            BinanceAccountTrades
        """

        json: BinanceAccountTradesJson = await self.handle_response(res)
        return self._models_mapper.map_to_account_trades(json)
