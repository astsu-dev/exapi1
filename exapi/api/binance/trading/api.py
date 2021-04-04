"""Has binance trading api interface."""

from decimal import Decimal
from typing import Optional

from exapi.models.binance import (BinanceAccountInfoModel,
                                  BinanceAccountTrades,
                                  BinanceCanceledOrderModel,
                                  BinanceCanceledOrders, BinanceOrderInfoModel,
                                  BinanceOrderInfos, BinanceOrderModel,
                                  BinanceTestOrderModel)
from exapi.models.binance.typedefs import (OrderResponseType, OrderSide,
                                           OrderType, TimeInForce)
from exapi.requesters.binance.trading import IBinanceTradingRequester
from exapi.utils.numbers import decimal_to_str

from .interface import IBinanceTradingAPI
from .response_handler import (BinanceTradingResponseHandler,
                               IBinanceTradingResponseHandler)


class BinanceTradingAPI(IBinanceTradingAPI):
    """Binance trading api.

    Has methods for trading request making to binance exchange.
    """

    def __init__(self,
                 requester: IBinanceTradingRequester,
                 response_handler: Optional[IBinanceTradingResponseHandler] = None
                 ) -> None:
        self._requester = requester
        self._response_handler = (response_handler if response_handler is not None
                                  else BinanceTradingResponseHandler())

    async def new_test_order(self, symbol: str,
                             side: OrderSide,
                             type: OrderType,
                             time_in_force: Optional[TimeInForce] = None,
                             quantity: Optional[Decimal] = None,
                             quantity_precision: Optional[int] = None,
                             quote_order_qty: Optional[Decimal] = None,
                             price: Optional[Decimal] = None,
                             price_precision: Optional[int] = None,
                             new_client_order_id: Optional[str] = None,
                             stop_price: Optional[Decimal] = None,
                             iceberg_qty: Optional[Decimal] = None,
                             new_order_resp_type: Optional[OrderResponseType] = None,
                             recv_window: Optional[int] = None,
                             timestamp: Optional[int] = None
                             ) -> BinanceTestOrderModel:
        """Tests new order creation and signature/recv_window long.
        Creates and validates a new order but does not send it into the matching engine.

        Weight: 1

        Json example:
            {}

        Args:
            symbol (str)
            side (OrderSide)
            type (OrderType)
            time_in_force (Optional[TimeInForce], optional)
            quantity (Optional[Decimal], optional)
            quantity_precision (Optional[int], optional): quantity precision (digits after comma).
                If None will be used precision from number. Will not be sended in request.
            quote_order_qty (Optional[Decimal], optional)
            price (Optional[Decimal], optional)
            price_precision (Optional[int], optional): price precision (digits after comma).
                If None will be used precision from number. Will not be sended in request.
            new_client_order_id (Optional[str], optional): A unique id among open orders.
                Automatically generated if not sent.
            stop_price (Optional[Decimal], optional): Used with STOP_LOSS, STOP_LOSS_LIMIT,
                TAKE_PROFIT, and TAKE_PROFIT_LIMIT orders.
            iceberg_qty (Optional[Decimal], optional): Used with LIMIT, STOP_LOSS_LIMIT,
                and TAKE_PROFIT_LIMIT to create an iceberg order.
            new_order_resp_type ([type], optional): Set the response JSON. ACK, RESULT, or FULL;
                MARKET and LIMIT order types default to FULL, all other orders default to ACK.
            recv_window (Optional[int], optional): The value cannot be greater than 60000.
            timestamp (Optional[int]): if None current timestamp in milliseconds will be used.

        Returns:
            BinanceTestOrderModel
        """

        res_quantity = (decimal_to_str(quantity, quantity_precision)
                        if quantity is not None else quantity)
        res_quote_order_qty = (decimal_to_str(quote_order_qty, quantity_precision)
                               if quote_order_qty is not None else quote_order_qty)
        res_price = (decimal_to_str(price, price_precision)
                     if price is not None else price)
        res_stop_price = (decimal_to_str(stop_price, price_precision)
                          if stop_price is not None else stop_price)
        res_iceberg_qty = (decimal_to_str(iceberg_qty, quantity_precision)
                           if iceberg_qty is not None else iceberg_qty)

        response = await self._requester.new_test_order(
            symbol=symbol,
            side=side,
            type=type,
            time_in_force=time_in_force,
            quantity=res_quantity,
            quote_order_qty=res_quote_order_qty,
            price=res_price,
            new_client_order_id=new_client_order_id,
            stop_price=res_stop_price,
            iceberg_qty=res_iceberg_qty,
            new_order_resp_type=new_order_resp_type,
            recv_window=recv_window,
            timestamp=timestamp)
        res = await self._response_handler.handle_new_test_order_response(response)
        return res

    async def new_order(self, symbol: str,
                        side: OrderSide,
                        type: OrderType,
                        time_in_force: Optional[TimeInForce] = None,
                        quantity: Optional[Decimal] = None,
                        quantity_precision: Optional[int] = None,
                        quote_order_qty: Optional[Decimal] = None,
                        price: Optional[Decimal] = None,
                        price_precision: Optional[int] = None,
                        new_client_order_id: Optional[str] = None,
                        stop_price: Optional[Decimal] = None,
                        iceberg_qty: Optional[Decimal] = None,
                        new_order_resp_type: Optional[OrderResponseType] = None,
                        recv_window: Optional[int] = None,
                        timestamp: Optional[int] = None
                        ) -> BinanceOrderModel:
        """Send in a new order.

        Weight: 1

        Json example:
            { // ACK response type
                "symbol": "BTCUSDT",
                "orderId": 28,
                "orderListId": -1, // Unless OCO, value will be -1
                "clientOrderId": "6gCrw2kRUAF9CvJDGP16IP",
                "transactTime": 1507725176595
            } OR
            { // RESULT response type
                "symbol": "BTCUSDT",
                "orderId": 28,
                "orderListId": -1, // Unless OCO, value will be -1
                "clientOrderId": "6gCrw2kRUAF9CvJDGP16IP",
                "transactTime": 1507725176595,
                "price": "0.00000000",
                "origQty": "10.00000000",
                "executedQty": "10.00000000",
                "cummulativeQuoteQty": "10.00000000",
                "status": "FILLED",
                "timeInForce": "GTC",
                "type": "MARKET",
                "side": "SELL"
            } OR
            { // FULL response type
                "symbol": "BTCUSDT",
                "orderId": 28,
                "orderListId": -1, //Unless OCO, value will be -1
                "clientOrderId": "6gCrw2kRUAF9CvJDGP16IP",
                "transactTime": 1507725176595,
                "price": "0.00000000",
                "origQty": "10.00000000",
                "executedQty": "10.00000000",
                "cummulativeQuoteQty": "10.00000000",
                "status": "FILLED",
                "timeInForce": "GTC",
                "type": "MARKET",
                "side": "SELL",
                "fills": [
                    {
                        "price": "4000.00000000",
                        "qty": "1.00000000",
                        "commission": "4.00000000",
                        "commissionAsset": "USDT"
                    },
                    {
                        "price": "3999.00000000",
                        "qty": "5.00000000",
                        "commission": "19.99500000",
                        "commissionAsset": "USDT"
                    },
                    {
                        "price": "3998.00000000",
                        "qty": "2.00000000",
                        "commission": "7.99600000",
                        "commissionAsset": "USDT"
                    },
                    {
                        "price": "3997.00000000",
                        "qty": "1.00000000",
                        "commission": "3.99700000",
                        "commissionAsset": "USDT"
                    },
                    {
                        "price": "3995.00000000",
                        "qty": "1.00000000",
                        "commission": "3.99500000",
                        "commissionAsset": "USDT"
                    },
                    ...
                ]
            }

        Args:
            symbol (str)
            side (OrderSide)
            type (OrderType)
            time_in_force (Optional[TimeInForce], optional)
            quantity (Optional[Decimal], optional)
            quantity_precision (Optional[int], optional): quantity precision (digits after comma).
                If None will be used precision from number. Will not be sended in request.
            quote_order_qty (Optional[Decimal], optional)
            price (Optional[Decimal], optional)
            price_precision (Optional[int], optional): price precision (digits after comma).
                If None will be used precision from number. Will not be sended in request.
            new_client_order_id (Optional[str], optional): A unique id among open orders.
                Automatically generated if not sent.
            stop_price (Optional[Decimal], optional): Used with STOP_LOSS, STOP_LOSS_LIMIT,
                TAKE_PROFIT, and TAKE_PROFIT_LIMIT orders.
            iceberg_qty (Optional[Decimal], optional): Used with LIMIT, STOP_LOSS_LIMIT,
                and TAKE_PROFIT_LIMIT to create an iceberg order.
            new_order_resp_type ([type], optional): Set the response JSON. ACK, RESULT, or FULL;
                MARKET and LIMIT order types default to FULL, all other orders default to ACK.
            recv_window (Optional[int], optional): The value cannot be greater than 60000.
            timestamp (Optional[int]): if None current timestamp in milliseconds will be used.

        Returns:
            BinanceOrderModel
        """

        res_quantity = (decimal_to_str(quantity, quantity_precision)
                        if quantity is not None else quantity)
        res_quote_order_qty = (decimal_to_str(quote_order_qty, quantity_precision)
                               if quote_order_qty is not None else quote_order_qty)
        res_price = (decimal_to_str(price, price_precision)
                     if price is not None else price)
        res_stop_price = (decimal_to_str(stop_price, price_precision)
                          if stop_price is not None else stop_price)
        res_iceberg_qty = (decimal_to_str(iceberg_qty, quantity_precision)
                           if iceberg_qty is not None else iceberg_qty)

        response = await self._requester.new_order(
            symbol=symbol,
            side=side,
            type=type,
            time_in_force=time_in_force,
            quantity=res_quantity,
            quote_order_qty=res_quote_order_qty,
            price=res_price,
            new_client_order_id=new_client_order_id,
            stop_price=res_stop_price,
            iceberg_qty=res_iceberg_qty,
            new_order_resp_type=new_order_resp_type,
            recv_window=recv_window,
            timestamp=timestamp)
        res = await self._response_handler.handle_new_order_response(response)
        return res

    async def cancel_order(self, symbol: str,
                           order_id: Optional[int] = None,
                           orig_client_order_id: Optional[str] = None,
                           new_client_order_id: Optional[str] = None,
                           recv_window: Optional[int] = None,
                           timestamp: Optional[int] = None
                           ) -> BinanceCanceledOrderModel:
        """Cancel an active order.

        Either order_id or orig_client_order_id must be sent.

        Weight: 1

        Json example:
            {
                "symbol": "LTCBTC",
                "origClientOrderId": "myOrder1",
                "orderId": 4,
                "orderListId": -1, // Unless part of an OCO, the value will always be -1.
                "clientOrderId": "cancelMyOrder1",
                "price": "2.00000000",
                "origQty": "1.00000000",
                "executedQty": "0.00000000",
                "cummulativeQuoteQty": "0.00000000",
                "status": "CANCELED",
                "timeInForce": "GTC",
                "type": "LIMIT",
                "side": "BUY"
            }

        Args:
            symbol (str)
            order_id (Optional[int], optional)
            orig_client_order_id (Optional[str], optional)
            new_client_order_id (Optional[str], optional): Used to uniquely identify this cancel.
                Automatically generated by default.
            recv_window (Optional[int], optional): The value cannot be greater than 60000.
            timestamp (Optional[int]): if None current timestamp in milliseconds will be used.

        Returns:
            BinanceCanceledOrderModel
        """

        response = await self._requester.cancel_order(
            symbol=symbol,
            order_id=order_id,
            orig_client_order_id=orig_client_order_id,
            new_client_order_id=new_client_order_id,
            recv_window=recv_window,
            timestamp=timestamp)
        res = await self._response_handler.handle_cancel_order_response(response)
        return res

    async def cancel_orders(self, symbol: str,
                            recv_window: Optional[int] = None,
                            timestamp: Optional[int] = None
                            ) -> BinanceCanceledOrders:
        """Cancels all active orders on a symbol. This includes OCO orders.

        Weight: 1

        [
            {
                "symbol": "BTCUSDT",
                "origClientOrderId": "E6APeyTJvkMvLMYMqu1KQ4",
                "orderId": 11,
                "orderListId": -1,
                "clientOrderId": "pXLV6Hz6mprAcVYpVMTGgx",
                "price": "0.089853",
                "origQty": "0.178622",
                "executedQty": "0.000000",
                "cummulativeQuoteQty": "0.000000",
                "status": "CANCELED",
                "timeInForce": "GTC",
                "type": "LIMIT",
                "side": "BUY"
            },
            {
                "symbol": "BTCUSDT",
                "origClientOrderId": "A3EF2HCwxgZPFMrfwbgrhv",
                "orderId": 13,
                "orderListId": -1,
                "clientOrderId": "pXLV6Hz6mprAcVYpVMTGgx",
                "price": "0.090430",
                "origQty": "0.178622",
                "executedQty": "0.000000",
                "cummulativeQuoteQty": "0.000000",
                "status": "CANCELED",
                "timeInForce": "GTC",
                "type": "LIMIT",
                "side": "BUY"
            },
            {
                "orderListId": 1929,
                "contingencyType": "OCO",
                "listStatusType": "ALL_DONE",
                "listOrderStatus": "ALL_DONE",
                "listClientOrderId": "2inzWQdDvZLHbbAmAozX2N",
                "transactionTime": 1585230948299,
                "symbol": "BTCUSDT",
                "orders": [
                    {
                        "symbol": "BTCUSDT",
                        "orderId": 20,
                        "clientOrderId": "CwOOIPHSmYywx6jZX77TdL"
                    },
                    {
                        "symbol": "BTCUSDT",
                        "orderId": 21,
                        "clientOrderId": "461cPg51vQjV3zIMOXNz39"
                    },
                    ...
                ],
                "orderReports": [
                    {
                        "symbol": "BTCUSDT",
                        "origClientOrderId": "CwOOIPHSmYywx6jZX77TdL",
                        "orderId": 20,
                        "orderListId": 1929,
                        "clientOrderId": "pXLV6Hz6mprAcVYpVMTGgx",
                        "price": "0.668611",
                        "origQty": "0.690354",
                        "executedQty": "0.000000",
                        "cummulativeQuoteQty": "0.000000",
                        "status": "CANCELED",
                        "timeInForce": "GTC",
                        "type": "STOP_LOSS_LIMIT",
                        "side": "BUY",
                        "stopPrice": "0.378131",
                        "icebergQty": "0.017083"
                    },
                    {
                        "symbol": "BTCUSDT",
                        "origClientOrderId": "461cPg51vQjV3zIMOXNz39",
                        "orderId": 21,
                        "orderListId": 1929,
                        "clientOrderId": "pXLV6Hz6mprAcVYpVMTGgx",
                        "price": "0.008791",
                        "origQty": "0.690354",
                        "executedQty": "0.000000",
                        "cummulativeQuoteQty": "0.000000",
                        "status": "CANCELED",
                        "timeInForce": "GTC",
                        "type": "LIMIT_MAKER",
                        "side": "BUY",
                        "icebergQty": "0.639962"
                    },
                    ...
                ]
            },
            ...
        ]

        Args:
            symbol (str)
            recv_window (Optional[int], optional): The value cannot be greater than 60000.
            timestamp (Optional[int]): if None current timestamp in milliseconds will be used.

        Returns:
            BinanceCanceledOrders
        """

        response = await self._requester.cancel_orders(
            symbol=symbol,
            recv_window=recv_window,
            timestamp=timestamp)
        res = await self._response_handler.handle_cancel_orders_response(response)
        return res

    async def query_order(self, symbol: str,
                          order_id: Optional[int] = None,
                          orig_client_order_id: Optional[str] = None,
                          recv_window: Optional[int] = None,
                          timestamp: Optional[int] = None
                          ) -> BinanceOrderInfoModel:
        """Check an order's status.

        Weight: 1

        Notes:
            - Either orderId or origClientOrderId must be sent.
            - For some historical orders cummulativeQuoteQty will be < 0,
                meaning the data is not available at this time.

        Json example:
            {
                "symbol": "LTCBTC",
                "orderId": 1,
                "orderListId": -1, // Unless OCO, value will be -1
                "clientOrderId": "myOrder1",
                "price": "0.1",
                "origQty": "1.0",
                "executedQty": "0.0",
                "cummulativeQuoteQty": "0.0",
                "status": "NEW",
                "timeInForce": "GTC",
                "type": "LIMIT",
                "side": "BUY",
                "stopPrice": "0.0",
                "icebergQty": "0.0",
                "time": 1499827319559,
                "updateTime": 1499827319559,
                "isWorking": true,
                "origQuoteOrderQty": "0.000000"
            }

        Args:
            symbol (str)
            order_id (Optional[int], optional)
            orig_client_order_id (Optional[str], optional)
            recv_window (Optional[int], optional): The value cannot be greater than 60000.
            timestamp (Optional[int]): if None current timestamp in milliseconds will be used.

        Returns:
            BinanceOrderInfoModel
        """

        response = await self._requester.query_order(
            symbol=symbol,
            order_id=order_id,
            orig_client_order_id=orig_client_order_id,
            recv_window=recv_window,
            timestamp=timestamp)
        res = await self._response_handler.handle_query_order_response(response)
        return res

    async def get_current_open_orders(self, symbol: Optional[str] = None,
                                      recv_window: Optional[int] = None,
                                      timestamp: Optional[int] = None
                                      ) -> BinanceOrderInfos:
        """Get all open orders on a symbol. Careful when accessing this with no symbol.

        If the symbol is not sent, orders for all symbols will be returned in an array.

        Weight: 1 for a single symbol; 40 when the symbol parameter is omitted

        Json example:
            [
                {
                    "symbol": "LTCBTC",
                    "orderId": 1,
                    "orderListId": -1, // Unless OCO, the value will always be -1
                    "clientOrderId": "myOrder1",
                    "price": "0.1",
                    "origQty": "1.0",
                    "executedQty": "0.0",
                    "cummulativeQuoteQty": "0.0",
                    "status": "NEW",
                    "timeInForce": "GTC",
                    "type": "LIMIT",
                    "side": "BUY",
                    "stopPrice": "0.0",
                    "icebergQty": "0.0",
                    "time": 1499827319559,
                    "updateTime": 1499827319559,
                    "isWorking": true,
                    "origQuoteOrderQty": "0.000000"
                },
                ...
            ]

        Args:
            symbol (Optional[str], optional): If the symbol is not sent,
                orders for all symbols will be returned in an array.
            recv_window (Optional[int], optional): The value cannot be greater than 60000.
            timestamp (Optional[int]): if None current timestamp in milliseconds will be used.

        Returns:
            BinanceOrderInfos
        """

        response = await self._requester.get_current_open_orders(
            symbol=symbol,
            recv_window=recv_window,
            timestamp=timestamp)
        res = await self._response_handler.handle_get_current_open_orders_response(response)
        return res

    async def get_all_orders(self, symbol: str,
                             order_id: Optional[int] = None,
                             start_time: Optional[int] = None,
                             end_time: Optional[int] = None,
                             limit: Optional[int] = None,
                             recv_window: Optional[int] = None,
                             timestamp: Optional[int] = None
                             ) -> BinanceOrderInfos:
        """Get all account orders; active, canceled, or filled.

        Weight: 5 with symbol

        Notes:
            - If orderId is set, it will get orders >= that orderId.
                Otherwise most recent orders are returned.
            - For some historical orders cummulativeQuoteQty will be < 0,
                meaning the data is not available at this time.

        Json example:
            [
                {
                    "symbol": "LTCBTC",
                    "orderId": 1,
                    "orderListId": -1, // Unless OCO, the value will always be -1
                    "clientOrderId": "myOrder1",
                    "price": "0.1",
                    "origQty": "1.0",
                    "executedQty": "0.0",
                    "cummulativeQuoteQty": "0.0",
                    "status": "NEW",
                    "timeInForce": "GTC",
                    "type": "LIMIT",
                    "side": "BUY",
                    "stopPrice": "0.0",
                    "icebergQty": "0.0",
                    "time": 1499827319559,
                    "updateTime": 1499827319559,
                    "isWorking": true,
                    "origQuoteOrderQty": "0.000000"
                },
                ...
            ]

        Args:
            symbol (str)
            timestamp (int)
            order_id (Optional[int], optional)
            start_time (Optional[int], optional)
            end_time (Optional[int], optional)
            limit (Optional[int], optional): Default 500; max 1000.
            recv_window (Optional[int], optional): The value cannot be greater than 60000.

        Returns:
            BinanceOrderInfos
        """

        response = await self._requester.get_all_orders(
            symbol=symbol,
            order_id=order_id,
            start_time=start_time,
            end_time=end_time,
            limit=limit,
            recv_window=recv_window,
            timestamp=timestamp)
        res = await self._response_handler.handle_get_all_orders_response(response)
        return res

    async def get_account_info(self, recv_window: Optional[int] = None,
                               timestamp: Optional[int] = None
                               ) -> BinanceAccountInfoModel:
        """Get current account information.

        Weight: 5

        Json example:
            {
                "makerCommission": 15,
                "takerCommission": 15,
                "buyerCommission": 0,
                "sellerCommission": 0,
                "canTrade": true,
                "canWithdraw": true,
                "canDeposit": true,
                "updateTime": 123456789,
                "accountType": "SPOT",
                "balances": [
                    {
                        "asset": "BTC",
                        "free": "4723846.89208129",
                        "locked": "0.00000000"
                    },
                    {
                        "asset": "LTC",
                        "free": "4763368.68006011",
                        "locked": "0.00000000"
                    }
                ],
                "permissions": [
                    "SPOT"
                ]
            }

        Args:
            recv_window (Optional[int], optional): The value cannot be greater than 60000.
            timestamp (Optional[int]): if None current timestamp in milliseconds will be used.

        Returns:
            BinanceAccountInfoModel
        """

        response = await self._requester.get_account_info(
            recv_window=recv_window,
            timestamp=timestamp)
        res = await self._response_handler.handle_get_account_info_response(response)
        return res

    async def get_trades(self, symbol: str,
                         start_time: Optional[int] = None,
                         end_time: Optional[int] = None,
                         from_id: Optional[int] = None,
                         limit: Optional[int] = None,
                         recv_window: Optional[int] = None,
                         timestamp: Optional[int] = None
                         ) -> BinanceAccountTrades:
        """Get trades for a specific account and symbol.

        Weight: 5

        Notes:
            - If fromId is set, it will get id >= that from_id.
                Otherwise most recent trades are returned.

        Json example:
            [
                {
                    "symbol": "BNBBTC",
                    "id": 28457,
                    "orderId": 100234,
                    "orderListId": -1, // Unless OCO, the value will always be -1
                    "price": "4.00000100",
                    "qty": "12.00000000",
                    "quoteQty": "48.000012",
                    "commission": "10.10000000",
                    "commissionAsset": "BNB",
                    "time": 1499865549590,
                    "isBuyer": true,
                    "isMaker": false,
                    "isBestMatch": true
                },
                ...
            ]

        Args:
            symbol (str)
            start_time (Optional[int], optional)
            end_time (Optional[int], optional)
            from_id (Optional[int], optional): trade id to fetch from.
                Default gets most recent trades.
            limit (Optional[int], optional): Default 500; max 1000.
            recv_window (Optional[int], optional): The value cannot be greater than 60000.
            timestamp (Optional[int]): if None current timestamp in milliseconds will be used.

        Returns:
            BinanceAccountTrades
        """

        response = await self._requester.get_trades(
            symbol=symbol,
            start_time=start_time,
            end_time=end_time,
            from_id=from_id,
            limit=limit,
            recv_window=recv_window,
            timestamp=timestamp)
        res = await self._response_handler.handle_get_trades_response(response)
        return res
