"""Has hitbtc trading response handler interface."""

from exapi.response_handlers.base import IBaseResponseHandler
from exapi.models.hitbtc import (HitbtcOrderModel, HitbtcOrders,
                                 HitbtcTradingCurrencyBalances,
                                 HitbtcTradingFeeModel)
from exapi.requesters.typedefs import RequesterResponse


class IHitbtcTradingResponseHandler(IBaseResponseHandler):
    """Has methods for creating requests to hitbtc trading api."""

    async def handle_get_trading_balance_response(self, response: RequesterResponse
                                                  ) -> HitbtcTradingCurrencyBalances:
        """Handles get trading balance response.

        Args:
            response (RequesterResponse)

        Returns:
            HitbtcCurrencyTradingBalances
        """

    async def handle_get_active_orders_response(self, response: RequesterResponse
                                                ) -> HitbtcOrders:
        """Handles get active orders response.

        Args:
            response (RequesterResponse)

        Returns:
            HitbtcOrders
        """

    async def handle_get_active_order_response(self, response: RequesterResponse
                                               ) -> HitbtcOrderModel:
        """Handles get active order response.

        Args:
            response (RequesterResponse)

        Returns:
            HitbtcOrderModel
        """

    async def handle_new_order_response(self, response: RequesterResponse
                                        ) -> HitbtcOrderModel:
        """Handles new order response.

        Args:
            response (RequesterResponse)

        Returns:
            HitbtcOrderModel
        """

    async def handle_cancel_orders_response(self, response: RequesterResponse
                                            ) -> HitbtcOrders:
        """Handles cancel orders response.

        Args:
            response (RequesterResponse)

        Returns:
            HitbtcOrders
        """

    async def handle_cancel_order_response(self, response: RequesterResponse
                                           ) -> HitbtcOrderModel:
        """Handles cancel order response.

        Args:
            response (RequesterResponse)

        Returns:
            HitbtcOrderModel
        """

    async def handle_get_fee_response(self, response: RequesterResponse
                                      ) -> HitbtcTradingFeeModel:
        """Handles get trading commission response.

        Args:
            response (RequesterResponse)

        Returns:
            HitbtcTradingFeeModel
        """
