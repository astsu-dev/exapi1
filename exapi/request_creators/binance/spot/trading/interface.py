"""Has binance trading request creator interface."""

from typing import Optional, Protocol

from exapi.request_creators.request import Request
from exapi.typedefs.binance import (OrderResponseType, OrderSide,
                                    OrderType, TimeInForce)


class IBinanceSpotTradingRequestCreator(Protocol):
    """Has methods for creating requests to binance spot trading api."""

    def create_new_test_order_request(self, symbol: str,
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
                                      ) -> Request:
        """Creates new test order request.

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
            Request
        """

    def create_new_order_request(self, symbol: str,
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
                                 ) -> Request:
        """Creates new test order request.

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
            Request
        """

    def create_cancel_order_request(self, symbol: str,
                                    order_id: Optional[int] = None,
                                    orig_client_order_id: Optional[str] = None,
                                    new_client_order_id: Optional[str] = None,
                                    recv_window: Optional[int] = None,
                                    timestamp: Optional[int] = None
                                    ) -> Request:
        """Creates cancel order request.

        Args:
            symbol (str)
            order_id (Optional[int], optional)
            orig_client_order_id (Optional[str], optional)
            new_client_order_id (Optional[str], optional): Used to uniquely identify this cancel.
                Automatically generated by default.
            recv_window (Optional[int], optional): The value cannot be greater than 60000.
            timestamp (Optional[int]): if None current timestamp in milliseconds will be used.

        Returns:
            Request
        """

    def create_cancel_orders_request(self, symbol: str,
                                     recv_window: Optional[int] = None,
                                     timestamp: Optional[int] = None
                                     ) -> Request:
        """Creates cancel all orders request.

        Args:
            symbol (str)
            recv_window (Optional[int], optional): The value cannot be greater than 60000.
            timestamp (Optional[int]): if None current timestamp in milliseconds will be used.

        Returns:
            Request
        """

    def create_query_order_request(self, symbol: str,
                                   order_id: Optional[int] = None,
                                   orig_client_order_id: Optional[str] = None,
                                   recv_window: Optional[int] = None,
                                   timestamp: Optional[int] = None
                                   ) -> Request:
        """Creates query order request.

        Args:
            symbol (str)
            order_id (Optional[int], optional)
            orig_client_order_id (Optional[str], optional)
            recv_window (Optional[int], optional): The value cannot be greater than 60000.
            timestamp (Optional[int]): if None current timestamp in milliseconds will be used.

        Returns:
            Request
        """

    def create_get_current_open_orders_request(self, symbol: Optional[str] = None,
                                               recv_window: Optional[int] = None,
                                               timestamp: Optional[int] = None
                                               ) -> Request:
        """Creates get current open orders request.

        Args:
            symbol (Optional[str], optional): If the symbol is not sent,
                orders for all symbols will be returned in an array.
            recv_window (Optional[int], optional): The value cannot be greater than 60000.
            timestamp (Optional[int]): if None current timestamp in milliseconds will be used.

        Returns:
            Request
        """

    def create_get_all_orders_request(self, symbol: str,
                                      order_id: Optional[int] = None,
                                      start_time: Optional[int] = None,
                                      end_time: Optional[int] = None,
                                      limit: Optional[int] = None,
                                      recv_window: Optional[int] = None,
                                      timestamp: Optional[int] = None
                                      ) -> Request:
        """Creates get all orders request.

        Args:
            symbol (str)
            order_id (Optional[int], optional)
            start_time (Optional[int], optional)
            end_time (Optional[int], optional)
            limit (Optional[int], optional): Default 500; max 1000.
            recv_window (Optional[int], optional): The value cannot be greater than 60000.
            timestamp (Optional[int]): if None current timestamp in milliseconds will be used.

        Returns:
            Request
        """

    def create_get_account_info_request(self, recv_window: Optional[int] = None,
                                        timestamp: Optional[int] = None,
                                        ) -> Request:
        """Creates get account info request.

        Args:
            recv_window (Optional[int], optional): The value cannot be greater than 60000.
            timestamp (Optional[int]): if None current timestamp in milliseconds will be used.

        Returns:
            Request
        """

    def create_get_trades_request(self, symbol: str,
                                  start_time: Optional[int] = None,
                                  end_time: Optional[int] = None,
                                  from_id: Optional[int] = None,
                                  limit: Optional[int] = None,
                                  recv_window: Optional[int] = None,
                                  timestamp: Optional[int] = None
                                  ) -> Request:
        """Creates get account trades request.

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
            Request
        """
