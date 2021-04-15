"""Has binance trading request creator interface."""

from typing import Optional

from yarl import URL

from exapi.auth.binance import IBinanceAuth
from exapi.request_creators.binance.spot.base import BinanceBaseSpotRequestCreator
from exapi.request_creators.binance.spot.trading.interface import IBinanceSpotTradingRequestCreator
from exapi.request_creators.request import Request
from exapi.requesters.typedefs import Params
from exapi.typedefs.binance import (OrderResponseType, OrderSide,
                                    OrderType, TimeInForce)
from exapi.utils.time import get_timestamp


class BinanceSpotTradingRequestCreator(BinanceBaseSpotRequestCreator, IBinanceSpotTradingRequestCreator):
    """Has methods for creating requests to binance spot trading api."""

    BASE_URL: str = BinanceBaseSpotRequestCreator.BASE_URL + "/api/v3"

    def __init__(self, auth: IBinanceAuth) -> None:
        self._auth = auth

    def create_order_request(self, test_order: bool,
                             symbol: str,
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
        """Creates request for order or test order endpoint.

        Args:
            test_order (bool): if True request for test order will be created.
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

        method = "POST"
        path = "/order/test" if test_order else "/order"
        url = URL(self._create_url(path))

        timestamp = timestamp if timestamp is not None else get_timestamp()

        params: Params = {
            "symbol": symbol,
            "side": side,
            "type": type,
            "timestamp": str(timestamp)
        }
        if time_in_force is not None:
            params["timeInForce"] = time_in_force
        if quantity is not None:
            params["quantity"] = quantity
        if quote_order_qty is not None:
            params["quoteOrderQty"] = quote_order_qty
        if price is not None:
            params["price"] = price
        if new_client_order_id is not None:
            params["newClientOrderId"] = new_client_order_id
        if stop_price is not None:
            params["stopPrice"] = stop_price
        if iceberg_qty is not None:
            params["icebergQty"] = iceberg_qty
        if new_order_resp_type is not None:
            params["newOrderRespType"] = new_order_resp_type
        if recv_window is not None:
            params["recvWindow"] = str(recv_window)

        auth_res = self._auth.sign(params)

        url = url.with_query(auth_res.params)
        req = Request(method=method, url=url, headers=auth_res.headers)

        return req

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

        return self.create_order_request(
            test_order=True,
            symbol=symbol,
            side=side,
            type=type,
            timestamp=timestamp,
            time_in_force=time_in_force,
            quantity=quantity,
            quote_order_qty=quote_order_qty,
            price=price,
            new_client_order_id=new_client_order_id,
            stop_price=stop_price,
            iceberg_qty=iceberg_qty,
            new_order_resp_type=new_order_resp_type,
            recv_window=recv_window)

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

        return self.create_order_request(
            test_order=False,
            symbol=symbol,
            side=side,
            type=type,
            timestamp=timestamp,
            time_in_force=time_in_force,
            quantity=quantity,
            quote_order_qty=quote_order_qty,
            price=price,
            new_client_order_id=new_client_order_id,
            stop_price=stop_price,
            iceberg_qty=iceberg_qty,
            new_order_resp_type=new_order_resp_type,
            recv_window=recv_window)

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

        method = "DELETE"
        path = "/order"
        url = URL(self._create_url(path))

        timestamp = timestamp if timestamp is not None else get_timestamp()

        params: Params = {
            "symbol": symbol,
            "timestamp": str(timestamp)
        }
        if order_id is not None:
            params["orderId"] = str(order_id)
        if orig_client_order_id is not None:
            params["origClientOrderId"] = orig_client_order_id
        if new_client_order_id is not None:
            params["newClientOrderId"] = new_client_order_id
        if recv_window is not None:
            params["recvWindow"] = str(recv_window)

        auth_res = self._auth.sign(params)

        url = url.with_query(auth_res.params)
        req = Request(method=method, url=url, headers=auth_res.headers)

        return req

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

        method = "DELETE"
        path = "/openOrders"
        url = URL(self._create_url(path))

        timestamp = timestamp if timestamp is not None else get_timestamp()

        params: Params = {
            "symbol": symbol,
            "timestamp": str(timestamp)
        }
        if recv_window is not None:
            params["recvWindow"] = str(recv_window)

        auth_res = self._auth.sign(params)

        url = url.with_query(auth_res.params)
        req = Request(method=method, url=url, headers=auth_res.headers)

        return req

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

        method = "GET"
        path = "/order"
        url = URL(self._create_url(path))

        timestamp = timestamp if timestamp is not None else get_timestamp()

        params: Params = {
            "symbol": symbol,
            "timestamp": str(timestamp)
        }
        if order_id is not None:
            params["orderId"] = str(order_id)
        if orig_client_order_id is not None:
            params["origClientOrderId"] = orig_client_order_id
        if recv_window is not None:
            params["recvWindow"] = str(recv_window)

        auth_res = self._auth.sign(params)

        url = url.with_query(auth_res.params)
        req = Request(method=method, url=url, headers=auth_res.headers)

        return req

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

        method = "GET"
        path = "/openOrders"
        url = URL(self._create_url(path))

        timestamp = timestamp if timestamp is not None else get_timestamp()

        params: Params = {
            "timestamp": str(timestamp)
        }
        if symbol is not None:
            params["symbol"] = symbol
        if recv_window is not None:
            params["recvWindow"] = str(recv_window)

        auth_res = self._auth.sign(params)

        url = url.with_query(auth_res.params)
        req = Request(method=method, url=url, headers=auth_res.headers)

        return req

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

        method = "GET"
        path = "/allOrders"
        url = URL(self._create_url(path))

        timestamp = timestamp if timestamp is not None else get_timestamp()

        params: Params = {
            "symbol": symbol,
            "timestamp": str(timestamp)
        }
        if order_id is not None:
            params["orderId"] = str(order_id)
        if start_time is not None:
            params["startTime"] = str(start_time)
        if end_time is not None:
            params["endTime"] = str(end_time)
        if limit is not None:
            params["limit"] = str(limit)
        if recv_window is not None:
            params["recvWindow"] = str(recv_window)

        auth_res = self._auth.sign(params)

        url = url.with_query(auth_res.params)
        req = Request(method=method, url=url, headers=auth_res.headers)

        return req

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

        method = "GET"
        path = "/account"
        url = URL(self._create_url(path))

        timestamp = timestamp if timestamp is not None else get_timestamp()

        params: Params = {
            "timestamp": str(timestamp)
        }
        if recv_window is not None:
            params["recvWindow"] = str(recv_window)

        auth_res = self._auth.sign(params)

        url = url.with_query(auth_res.params)
        req = Request(method=method, url=url, headers=auth_res.headers)

        return req

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

        method = "GET"
        path = "/myTrades"
        url = URL(self._create_url(path))

        timestamp = timestamp if timestamp is not None else get_timestamp()

        params: Params = {
            "symbol": symbol,
            "timestamp": str(timestamp)
        }
        if start_time is not None:
            params["startTime"] = str(start_time)
        if end_time is not None:
            params["endTime"] = str(end_time)
        if from_id is not None:
            params["fromId"] = str(from_id)
        if limit is not None:
            params["limit"] = str(limit)
        if recv_window is not None:
            params["recvWindow"] = str(recv_window)

        auth_res = self._auth.sign(params)

        url = url.with_query(auth_res.params)
        req = Request(method=method, url=url, headers=auth_res.headers)

        return req
