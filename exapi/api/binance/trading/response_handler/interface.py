"""Has binance trading response handler interface."""

from typing import Protocol

from exapi.models.binance import (BinanceAccountInfoModel,
                                  BinanceCanceledOrderModel,
                                  BinanceCanceledOrders, BinanceOrderInfoModel,
                                  BinanceOrderInfos, BinanceOrderModel,
                                  BinanceTestOrderModel)
from exapi.models.binance.account_trade import BinanceAccountTrades
from exapi.requesters.typedefs import RequesterResponse


class IBinanceTradingResponseHandler(Protocol):
    """Has methods for handling binance trading responses."""

    async def handle_new_test_order_response(self, res: RequesterResponse) -> BinanceTestOrderModel:
        """Handles new test order response.

        Args:
            res (RequesterResponse)

        Returns:
            BinanceTestOrderModel
        """

    async def handle_new_order_response(self, res: RequesterResponse) -> BinanceOrderModel:
        """Handles new order response.

        Returns a json converted to model.

        Args:
            res (RequesterResponse)

        Returns:
            BinanceOrderModel
        """

    async def handle_cancel_order_response(self, res: RequesterResponse) -> BinanceCanceledOrderModel:
        """Handles cancel order response.

        Returns a json converted to model.

        Args:
            res (RequesterResponse)

        Returns:
            BinanceCanceledOrderModel
        """

    async def handle_cancel_orders_response(self, res: RequesterResponse) -> BinanceCanceledOrders:
        """Handles cancel orders response.

        Returns a json converted to model.

        Args:
            res (RequesterResponse)

        Returns:
            BinanceCanceledOrders
        """

    async def handle_query_order_response(self, res: RequesterResponse) -> BinanceOrderInfoModel:
        """Handles query order response.

        Returns a json converted to model.

        Args:
            res (RequesterResponse)

        Returns:
            BinanceOrderInfoModel
        """

    async def handle_get_current_open_orders_response(self, res: RequesterResponse) -> BinanceOrderInfos:
        """Handles get current open orders response.

        Returns a json converted to model.

        Args:
            res (RequesterResponse)

        Returns:
            BinanceOrderInfos
        """

    async def handle_get_all_orders_response(self, res: RequesterResponse) -> BinanceOrderInfos:
        """Handles get all orders response.

        Returns a json converted to model.

        Args:
            res (RequesterResponse)

        Returns:
            BinanceOrderInfos
        """

    async def handle_get_account_info_response(self, res: RequesterResponse) -> BinanceAccountInfoModel:
        """Handles get account info response.

        Returns a json converted to model.

        Args:
            res (RequesterResponse)

        Returns:
            BinanceAccountInfoModel
        """

    async def handle_get_trades_response(self, res: RequesterResponse) -> BinanceAccountTrades:
        """Handles get trades response.

        Returns a json converted to model.

        Args:
            res (RequesterResponse)

        Returns:
            BinanceAccountTrades
        """
