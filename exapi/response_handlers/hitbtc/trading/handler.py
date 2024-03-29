"""Has hitbtc trading response handler interface."""

from typing import Optional

from exapi.response_handlers.hitbtc.base import HitbtcBaseResponseHandler
from exapi.models_mappers.hitbtc.trading import IHitbtcTradingModelsMapper
from exapi.models.hitbtc import (HitbtcOrderModel, HitbtcOrders,
                                 HitbtcRawOrderModel, HitbtcRawOrders,
                                 HitbtcRawTradingCurrencyBalances,
                                 HitbtcRawTradingFeeModel,
                                 HitbtcTradingCurrencyBalances,
                                 HitbtcTradingFeeModel)
from exapi.models_mappers.hitbtc.mapper import HitbtcModelsMapper
from exapi.requesters.typedefs import RequesterResponse


class HitbtcTradingResponseHandler(HitbtcBaseResponseHandler):
    """Has methods for creating requests to hitbtc trading api."""

    _models_mapper: IHitbtcTradingModelsMapper

    def __init__(self, models_mapper: Optional[IHitbtcTradingModelsMapper] = None,
                 json_content_type: Optional[str] = "application/json"
                 ) -> None:
        models_mapper = (
            models_mapper if models_mapper is not None else HitbtcModelsMapper())
        super().__init__(models_mapper, json_content_type)

    async def handle_get_trading_balance_response(self, response: RequesterResponse
                                                  ) -> HitbtcTradingCurrencyBalances:
        """Handles get trading balance response.

        Args:
            response (RequesterResponse)

        Returns:
            HitbtcCurrencyTradingBalances
        """

        raw: HitbtcRawTradingCurrencyBalances = await self.handle_response(response)
        res = self._models_mapper.map_to_trading_balance(raw)
        return res

    async def handle_get_active_orders_response(self, response: RequesterResponse
                                                ) -> HitbtcOrders:
        """Handles get active orders response.

        Args:
            response (RequesterResponse)

        Returns:
            HitbtcOrders
        """

        res = await self._handle_orders_response(response)
        return res

    async def handle_get_active_order_response(self, response: RequesterResponse
                                               ) -> HitbtcOrderModel:
        """Handles get active order response.

        Args:
            response (RequesterResponse)

        Returns:
            HitbtcOrderModel
        """

        res = await self._handle_order_response(response)
        return res

    async def handle_new_order_response(self, response: RequesterResponse
                                        ) -> HitbtcOrderModel:
        """Handles new order response.

        Args:
            response (RequesterResponse)

        Returns:
            HitbtcOrderModel
        """

        res = await self._handle_order_response(response)
        return res

    async def handle_cancel_orders_response(self, response: RequesterResponse
                                            ) -> HitbtcOrders:
        """Handles cancel orders response.

        Args:
            response (RequesterResponse)

        Returns:
            HitbtcOrders
        """

        res = await self._handle_orders_response(response)
        return res

    async def handle_cancel_order_response(self, response: RequesterResponse
                                           ) -> HitbtcOrderModel:
        """Handles cancel order response.

        Args:
            response (RequesterResponse)

        Returns:
            HitbtcOrderModel
        """

        res = await self._handle_order_response(response)
        return res

    async def _handle_order_response(self, response: RequesterResponse
                                     ) -> HitbtcOrderModel:
        """Handles response with order.

        Args:
            response (RequesterResponse)

        Returns:
            HitbtcOrderModel
        """

        raw: HitbtcRawOrderModel = await self.handle_response(response)
        res = self._models_mapper.map_to_order(raw)
        return res

    async def _handle_orders_response(self, response: RequesterResponse
                                      ) -> HitbtcOrders:
        """Handles response with orders.

        Args:
            response (RequesterResponse)

        Returns:
            HitbtcOrders
        """

        raw: HitbtcRawOrders = await self.handle_response(response)
        res = self._models_mapper.map_to_orders(raw)
        return res

    async def handle_get_fee_response(self, response: RequesterResponse
                                      ) -> HitbtcTradingFeeModel:
        """Handles get trading commission response.

        Args:
            response (RequesterResponse)

        Returns:
            HitbtcTradingFeeModel
        """

        raw: HitbtcRawTradingFeeModel = await self.handle_response(response)
        res = self._models_mapper.map_to_trading_fee(raw)
        return res
