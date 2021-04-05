"""Has binance trading requester interface."""

from typing import Optional

from exapi.typedefs.binance import (OrderResponseType, OrderSide,
                                    OrderType, TimeInForce)
from exapi.requesters.base import IBaseRequester
from exapi.requesters.typedefs import RequesterResponse


class IBinanceTradingRequester(IBaseRequester):
    """Has methods for making requests to binance spot account trading api."""

    async def new_test_order(self, symbol: str,
                             side: OrderSide,
                             type: OrderType,
                             time_in_force: Optional[TimeInForce] = None,
                             quantity: Optional[str] = None,
                             quote_order_qty: Optional[str] = None,
                             price: Optional[str] = None,
                             new_client_order_id: Optional[str] = None,
                             stop_price: Optional[str] = None,
                             iceberg_qty: Optional[str] = None,
                             new_order_resp_type: Optional[OrderResponseType] = None,
                             recv_window: Optional[int] = None,
                             timestamp: Optional[int] = None
                             ) -> RequesterResponse:
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
            quantity (Optional[str], optional)
            quote_order_qty (Optional[str], optional)
            price (Optional[str], optional)
            new_client_order_id (Optional[str], optional): A unique id among open orders.
                Automatically generated if not sent.
            stop_price (Optional[str], optional): Used with STOP_LOSS, STOP_LOSS_LIMIT,
                TAKE_PROFIT, and TAKE_PROFIT_LIMIT orders.
            iceberg_qty (Optional[str], optional): Used with LIMIT, STOP_LOSS_LIMIT,
                and TAKE_PROFIT_LIMIT to create an iceberg order.
            new_order_resp_type ([type], optional): Set the response JSON. ACK, RESULT, or FULL;
                MARKET and LIMIT order types default to FULL, all other orders default to ACK.
            recv_window (Optional[int], optional): The value cannot be greater than 60000.
            timestamp (Optional[int]): if None current timestamp in milliseconds will be used.

        Returns:
            RequesterResponse
        """

    async def new_order(self, symbol: str,
                        side: OrderSide,
                        type: OrderType,
                        time_in_force: Optional[TimeInForce] = None,
                        quantity: Optional[str] = None,
                        quote_order_qty: Optional[str] = None,
                        price: Optional[str] = None,
                        new_client_order_id: Optional[str] = None,
                        stop_price: Optional[str] = None,
                        iceberg_qty: Optional[str] = None,
                        new_order_resp_type: Optional[OrderResponseType] = None,
                        recv_window: Optional[int] = None,
                        timestamp: Optional[int] = None
                        ) -> RequesterResponse:
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
            quantity (Optional[str], optional)
            quote_order_qty (Optional[str], optional)
            price (Optional[str], optional)
            new_client_order_id (Optional[str], optional): A unique id among open orders.
                Automatically generated if not sent.
            stop_price (Optional[str], optional): Used with STOP_LOSS, STOP_LOSS_LIMIT,
                TAKE_PROFIT, and TAKE_PROFIT_LIMIT orders.
            iceberg_qty (Optional[str], optional): Used with LIMIT, STOP_LOSS_LIMIT,
                and TAKE_PROFIT_LIMIT to create an iceberg order.
            new_order_resp_type ([type], optional): Set the response JSON. ACK, RESULT, or FULL;
                MARKET and LIMIT order types default to FULL, all other orders default to ACK.
            recv_window (Optional[int], optional): The value cannot be greater than 60000.
            timestamp (Optional[int]): if None current timestamp in milliseconds will be used.

        Returns:
            RequesterResponse
        """

    async def cancel_order(self, symbol: str,
                           order_id: Optional[int] = None,
                           orig_client_order_id: Optional[str] = None,
                           new_client_order_id: Optional[str] = None,
                           recv_window: Optional[int] = None,
                           timestamp: Optional[int] = None
                           ) -> RequesterResponse:
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
            RequesterResponse
        """

    async def cancel_orders(self, symbol: str,
                            recv_window: Optional[int] = None,
                            timestamp: Optional[int] = None
                            ) -> RequesterResponse:
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
            RequesterResponse
        """

    async def query_order(self, symbol: str,
                          order_id: Optional[int] = None,
                          orig_client_order_id: Optional[str] = None,
                          recv_window: Optional[int] = None,
                          timestamp: Optional[int] = None
                          ) -> RequesterResponse:
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
            RequesterResponse
        """

    async def get_current_open_orders(self, symbol: Optional[str] = None,
                                      recv_window: Optional[int] = None,
                                      timestamp: Optional[int] = None
                                      ) -> RequesterResponse:
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
            RequesterResponse
        """

    async def get_all_orders(self, symbol: str,
                             order_id: Optional[int] = None,
                             start_time: Optional[int] = None,
                             end_time: Optional[int] = None,
                             limit: Optional[int] = None,
                             recv_window: Optional[int] = None,
                             timestamp: Optional[int] = None
                             ) -> RequesterResponse:
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
            RequesterResponse
        """

    async def get_account_info(self, recv_window: Optional[int] = None,
                               timestamp: Optional[int] = None
                               ) -> RequesterResponse:
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
            RequesterResponse
        """

    async def get_trades(self, symbol: str,
                         start_time: Optional[int] = None,
                         end_time: Optional[int] = None,
                         from_id: Optional[int] = None,
                         limit: Optional[int] = None,
                         recv_window: Optional[int] = None,
                         timestamp: Optional[int] = None
                         ) -> RequesterResponse:
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
            RequesterResponse
        """
