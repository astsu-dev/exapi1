from typing import Final
from unittest import mock

import pytest
from yarl import URL

from exapi.enums.binance import (BinanceOrderResponseType, BinanceOrderSide,
                                 BinanceOrderType, BinanceTimeInForce)
from exapi.request_creators.binance.spot.trading import \
    BinanceSpotTradingRequestCreator
from exapi.requesters.binance.auth import BinanceAuth, BinanceKeyAuth
from exapi.requesters.request import Request

GET_TIMESTAMP_PATH: Final[str] = "exapi.request_creators.binance.spot.trading.creator.get_timestamp"

API_KEY: Final[str] = "aaa"
API_SECRET: Final[str] = "bbb"

BASE_URL: Final[str] = "https://api.binance.com/api/v3"

key_auth = BinanceKeyAuth(API_KEY)
auth = BinanceAuth(key_auth, API_SECRET)


@pytest.fixture(scope="module")
def creator() -> BinanceSpotTradingRequestCreator:
    return BinanceSpotTradingRequestCreator(auth)


def test_create_new_test_order_request(creator: BinanceSpotTradingRequestCreator) -> None:
    method = "POST"
    url = URL(BASE_URL + "/order/test")

    symbol = "BTCUSDT"
    side = BinanceOrderSide.BUY
    type_ = BinanceOrderType.LIMIT
    time_in_force = BinanceTimeInForce.GTC
    quantity = "0.1"
    quote_order_qty = "0.2"
    price = "5.5"
    new_client_order_id = "df"
    stop_price = "5.4"
    iceberg_qty = "2.3"
    new_order_resp_type = BinanceOrderResponseType.ACK
    recv_window = 500
    timestamp = 1500

    params = {
        "symbol": symbol,
        "side": side,
        "type": type_,
        "timestamp": str(timestamp)
    }
    auth_res = auth.sign(params)
    req = creator.create_new_test_order_request(
        symbol=symbol,
        side=side,
        type=type_,
        timestamp=timestamp)
    assert req == Request(
        method=method, url=url.with_query(auth_res.params), headers=auth_res.headers)

    params = {
        "symbol": symbol,
        "side": side,
        "type": type_,
        "timestamp": str(timestamp),
        "timeInForce": time_in_force
    }
    auth_res = auth.sign(params)
    req = creator.create_new_test_order_request(
        symbol=symbol,
        side=side,
        type=type_,
        time_in_force=time_in_force,
        timestamp=timestamp)
    assert req == Request(
        method=method, url=url.with_query(auth_res.params), headers=auth_res.headers)

    params = {
        "symbol": symbol,
        "side": side,
        "type": type_,
        "timestamp": str(timestamp),
        "timeInForce": time_in_force,
        "quantity": quantity
    }
    auth_res = auth.sign(params)
    req = creator.create_new_test_order_request(
        symbol=symbol,
        side=side,
        type=type_,
        time_in_force=time_in_force,
        quantity=quantity,
        timestamp=timestamp)
    assert req == Request(
        method=method, url=url.with_query(auth_res.params), headers=auth_res.headers)

    params = {
        "symbol": symbol,
        "side": side,
        "type": type_,
        "timestamp": str(timestamp),
        "timeInForce": time_in_force,
        "quantity": quantity,
        "quoteOrderQty": quote_order_qty
    }
    auth_res = auth.sign(params)
    req = creator.create_new_test_order_request(
        symbol=symbol,
        side=side,
        type=type_,
        time_in_force=time_in_force,
        quantity=quantity,
        quote_order_qty=quote_order_qty,
        timestamp=timestamp)
    assert req == Request(
        method=method, url=url.with_query(auth_res.params), headers=auth_res.headers)

    params = {
        "symbol": symbol,
        "side": side,
        "type": type_,
        "timestamp": str(timestamp),
        "timeInForce": time_in_force,
        "quantity": quantity,
        "quoteOrderQty": quote_order_qty,
        "price": price
    }
    auth_res = auth.sign(params)
    req = creator.create_new_test_order_request(
        symbol=symbol,
        side=side,
        type=type_,
        time_in_force=time_in_force,
        quantity=quantity,
        quote_order_qty=quote_order_qty,
        price=price,
        timestamp=timestamp)
    assert req == Request(
        method=method, url=url.with_query(auth_res.params), headers=auth_res.headers)

    params = {
        "symbol": symbol,
        "side": side,
        "type": type_,
        "timestamp": str(timestamp),
        "timeInForce": time_in_force,
        "quantity": quantity,
        "quoteOrderQty": quote_order_qty,
        "price": price,
        "newClientOrderId": new_client_order_id
    }
    auth_res = auth.sign(params)
    req = creator.create_new_test_order_request(
        symbol=symbol,
        side=side,
        type=type_,
        time_in_force=time_in_force,
        quantity=quantity,
        quote_order_qty=quote_order_qty,
        price=price,
        new_client_order_id=new_client_order_id,
        timestamp=timestamp)
    assert req == Request(
        method=method, url=url.with_query(auth_res.params), headers=auth_res.headers)

    params = {
        "symbol": symbol,
        "side": side,
        "type": type_,
        "timestamp": str(timestamp),
        "timeInForce": time_in_force,
        "quantity": quantity,
        "quoteOrderQty": quote_order_qty,
        "price": price,
        "newClientOrderId": new_client_order_id,
        "stopPrice": stop_price
    }
    auth_res = auth.sign(params)
    req = creator.create_new_test_order_request(
        symbol=symbol,
        side=side,
        type=type_,
        time_in_force=time_in_force,
        quantity=quantity,
        quote_order_qty=quote_order_qty,
        price=price,
        new_client_order_id=new_client_order_id,
        stop_price=stop_price,
        timestamp=timestamp)
    assert req == Request(
        method=method, url=url.with_query(auth_res.params), headers=auth_res.headers)

    params = {
        "symbol": symbol,
        "side": side,
        "type": type_,
        "timestamp": str(timestamp),
        "timeInForce": time_in_force,
        "quantity": quantity,
        "quoteOrderQty": quote_order_qty,
        "price": price,
        "newClientOrderId": new_client_order_id,
        "stopPrice": stop_price,
        "icebergQty": iceberg_qty
    }
    auth_res = auth.sign(params)
    req = creator.create_new_test_order_request(
        symbol=symbol,
        side=side,
        type=type_,
        time_in_force=time_in_force,
        quantity=quantity,
        quote_order_qty=quote_order_qty,
        price=price,
        new_client_order_id=new_client_order_id,
        stop_price=stop_price,
        iceberg_qty=iceberg_qty,
        timestamp=timestamp)
    assert req == Request(
        method=method, url=url.with_query(auth_res.params), headers=auth_res.headers)

    params = {
        "symbol": symbol,
        "side": side,
        "type": type_,
        "timestamp": str(timestamp),
        "timeInForce": time_in_force,
        "quantity": quantity,
        "quoteOrderQty": quote_order_qty,
        "price": price,
        "newClientOrderId": new_client_order_id,
        "stopPrice": stop_price,
        "icebergQty": iceberg_qty,
        "newOrderRespType": new_order_resp_type
    }
    auth_res = auth.sign(params)
    req = creator.create_new_test_order_request(
        symbol=symbol,
        side=side,
        type=type_,
        time_in_force=time_in_force,
        quantity=quantity,
        quote_order_qty=quote_order_qty,
        price=price,
        new_client_order_id=new_client_order_id,
        stop_price=stop_price,
        iceberg_qty=iceberg_qty,
        new_order_resp_type=new_order_resp_type,
        timestamp=timestamp)
    assert req == Request(
        method=method, url=url.with_query(auth_res.params), headers=auth_res.headers)

    params = {
        "symbol": symbol,
        "side": side,
        "type": type_,
        "timestamp": str(timestamp),
        "timeInForce": time_in_force,
        "quantity": quantity,
        "quoteOrderQty": quote_order_qty,
        "price": price,
        "newClientOrderId": new_client_order_id,
        "stopPrice": stop_price,
        "icebergQty": iceberg_qty,
        "newOrderRespType": new_order_resp_type,
        "recvWindow": str(recv_window)
    }
    auth_res = auth.sign(params)
    req = creator.create_new_test_order_request(
        symbol=symbol,
        side=side,
        type=type_,
        time_in_force=time_in_force,
        quantity=quantity,
        quote_order_qty=quote_order_qty,
        price=price,
        new_client_order_id=new_client_order_id,
        stop_price=stop_price,
        iceberg_qty=iceberg_qty,
        new_order_resp_type=new_order_resp_type,
        recv_window=recv_window,
        timestamp=timestamp)
    assert req == Request(
        method=method, url=url.with_query(auth_res.params), headers=auth_res.headers)

    timestamp = 1600
    params = {
        "symbol": symbol,
        "side": side,
        "type": type_,
        "timestamp": str(timestamp),
        "timeInForce": time_in_force,
        "quantity": quantity,
        "quoteOrderQty": quote_order_qty,
        "price": price,
        "newClientOrderId": new_client_order_id,
        "stopPrice": stop_price,
        "icebergQty": iceberg_qty,
        "newOrderRespType": new_order_resp_type,
        "recvWindow": str(recv_window)
    }
    auth_res = auth.sign(params)
    with mock.patch(GET_TIMESTAMP_PATH) as get_timestamp:
        get_timestamp.return_value = timestamp
        req = creator.create_new_test_order_request(
            symbol=symbol,
            side=side,
            type=type_,
            time_in_force=time_in_force,
            quantity=quantity,
            quote_order_qty=quote_order_qty,
            price=price,
            new_client_order_id=new_client_order_id,
            stop_price=stop_price,
            iceberg_qty=iceberg_qty,
            new_order_resp_type=new_order_resp_type,
            recv_window=recv_window)
    assert req == Request(
        method=method, url=url.with_query(auth_res.params), headers=auth_res.headers)


def test_create_new_order_request(creator: BinanceSpotTradingRequestCreator) -> None:
    method = "POST"
    url = URL(BASE_URL + "/order")

    symbol = "BTCUSDT"
    side = BinanceOrderSide.BUY
    type_ = BinanceOrderType.LIMIT
    time_in_force = BinanceTimeInForce.GTC
    quantity = "0.1"
    quote_order_qty = "0.2"
    price = "5.5"
    new_client_order_id = "df"
    stop_price = "5.4"
    iceberg_qty = "2.3"
    new_order_resp_type = BinanceOrderResponseType.ACK
    recv_window = 500
    timestamp = 1500

    params = {
        "symbol": symbol,
        "side": side,
        "type": type_,
        "timestamp": str(timestamp)
    }
    auth_res = auth.sign(params)
    req = creator.create_new_order_request(
        symbol=symbol,
        side=side,
        type=type_,
        timestamp=timestamp)
    assert req == Request(
        method=method, url=url.with_query(auth_res.params), headers=auth_res.headers)

    params = {
        "symbol": symbol,
        "side": side,
        "type": type_,
        "timestamp": str(timestamp),
        "timeInForce": time_in_force
    }
    auth_res = auth.sign(params)
    req = creator.create_new_order_request(
        symbol=symbol,
        side=side,
        type=type_,
        time_in_force=time_in_force,
        timestamp=timestamp)
    assert req == Request(
        method=method, url=url.with_query(auth_res.params), headers=auth_res.headers)

    params = {
        "symbol": symbol,
        "side": side,
        "type": type_,
        "timestamp": str(timestamp),
        "timeInForce": time_in_force,
        "quantity": quantity
    }
    auth_res = auth.sign(params)
    req = creator.create_new_order_request(
        symbol=symbol,
        side=side,
        type=type_,
        time_in_force=time_in_force,
        quantity=quantity,
        timestamp=timestamp)
    assert req == Request(
        method=method, url=url.with_query(auth_res.params), headers=auth_res.headers)

    params = {
        "symbol": symbol,
        "side": side,
        "type": type_,
        "timestamp": str(timestamp),
        "timeInForce": time_in_force,
        "quantity": quantity,
        "quoteOrderQty": quote_order_qty
    }
    auth_res = auth.sign(params)
    req = creator.create_new_order_request(
        symbol=symbol,
        side=side,
        type=type_,
        time_in_force=time_in_force,
        quantity=quantity,
        quote_order_qty=quote_order_qty,
        timestamp=timestamp)
    assert req == Request(
        method=method, url=url.with_query(auth_res.params), headers=auth_res.headers)

    params = {
        "symbol": symbol,
        "side": side,
        "type": type_,
        "timestamp": str(timestamp),
        "timeInForce": time_in_force,
        "quantity": quantity,
        "quoteOrderQty": quote_order_qty,
        "price": price
    }
    auth_res = auth.sign(params)
    req = creator.create_new_order_request(
        symbol=symbol,
        side=side,
        type=type_,
        time_in_force=time_in_force,
        quantity=quantity,
        quote_order_qty=quote_order_qty,
        price=price,
        timestamp=timestamp)
    assert req == Request(
        method=method, url=url.with_query(auth_res.params), headers=auth_res.headers)

    params = {
        "symbol": symbol,
        "side": side,
        "type": type_,
        "timestamp": str(timestamp),
        "timeInForce": time_in_force,
        "quantity": quantity,
        "quoteOrderQty": quote_order_qty,
        "price": price,
        "newClientOrderId": new_client_order_id
    }
    auth_res = auth.sign(params)
    req = creator.create_new_order_request(
        symbol=symbol,
        side=side,
        type=type_,
        time_in_force=time_in_force,
        quantity=quantity,
        quote_order_qty=quote_order_qty,
        price=price,
        new_client_order_id=new_client_order_id,
        timestamp=timestamp)
    assert req == Request(
        method=method, url=url.with_query(auth_res.params), headers=auth_res.headers)

    params = {
        "symbol": symbol,
        "side": side,
        "type": type_,
        "timestamp": str(timestamp),
        "timeInForce": time_in_force,
        "quantity": quantity,
        "quoteOrderQty": quote_order_qty,
        "price": price,
        "newClientOrderId": new_client_order_id,
        "stopPrice": stop_price
    }
    auth_res = auth.sign(params)
    req = creator.create_new_order_request(
        symbol=symbol,
        side=side,
        type=type_,
        time_in_force=time_in_force,
        quantity=quantity,
        quote_order_qty=quote_order_qty,
        price=price,
        new_client_order_id=new_client_order_id,
        stop_price=stop_price,
        timestamp=timestamp)
    assert req == Request(
        method=method, url=url.with_query(auth_res.params), headers=auth_res.headers)

    params = {
        "symbol": symbol,
        "side": side,
        "type": type_,
        "timestamp": str(timestamp),
        "timeInForce": time_in_force,
        "quantity": quantity,
        "quoteOrderQty": quote_order_qty,
        "price": price,
        "newClientOrderId": new_client_order_id,
        "stopPrice": stop_price,
        "icebergQty": iceberg_qty
    }
    auth_res = auth.sign(params)
    req = creator.create_new_order_request(
        symbol=symbol,
        side=side,
        type=type_,
        time_in_force=time_in_force,
        quantity=quantity,
        quote_order_qty=quote_order_qty,
        price=price,
        new_client_order_id=new_client_order_id,
        stop_price=stop_price,
        iceberg_qty=iceberg_qty,
        timestamp=timestamp)
    assert req == Request(
        method=method, url=url.with_query(auth_res.params), headers=auth_res.headers)

    params = {
        "symbol": symbol,
        "side": side,
        "type": type_,
        "timestamp": str(timestamp),
        "timeInForce": time_in_force,
        "quantity": quantity,
        "quoteOrderQty": quote_order_qty,
        "price": price,
        "newClientOrderId": new_client_order_id,
        "stopPrice": stop_price,
        "icebergQty": iceberg_qty,
        "newOrderRespType": new_order_resp_type
    }
    auth_res = auth.sign(params)
    req = creator.create_new_order_request(
        symbol=symbol,
        side=side,
        type=type_,
        time_in_force=time_in_force,
        quantity=quantity,
        quote_order_qty=quote_order_qty,
        price=price,
        new_client_order_id=new_client_order_id,
        stop_price=stop_price,
        iceberg_qty=iceberg_qty,
        new_order_resp_type=new_order_resp_type,
        timestamp=timestamp)
    assert req == Request(
        method=method, url=url.with_query(auth_res.params), headers=auth_res.headers)

    params = {
        "symbol": symbol,
        "side": side,
        "type": type_,
        "timestamp": str(timestamp),
        "timeInForce": time_in_force,
        "quantity": quantity,
        "quoteOrderQty": quote_order_qty,
        "price": price,
        "newClientOrderId": new_client_order_id,
        "stopPrice": stop_price,
        "icebergQty": iceberg_qty,
        "newOrderRespType": new_order_resp_type,
        "recvWindow": str(recv_window)
    }
    auth_res = auth.sign(params)
    req = creator.create_new_order_request(
        symbol=symbol,
        side=side,
        type=type_,
        time_in_force=time_in_force,
        quantity=quantity,
        quote_order_qty=quote_order_qty,
        price=price,
        new_client_order_id=new_client_order_id,
        stop_price=stop_price,
        iceberg_qty=iceberg_qty,
        new_order_resp_type=new_order_resp_type,
        recv_window=recv_window,
        timestamp=timestamp)
    assert req == Request(
        method=method, url=url.with_query(auth_res.params), headers=auth_res.headers)

    timestamp = 1600
    params = {
        "symbol": symbol,
        "side": side,
        "type": type_,
        "timestamp": str(timestamp),
        "timeInForce": time_in_force,
        "quantity": quantity,
        "quoteOrderQty": quote_order_qty,
        "price": price,
        "newClientOrderId": new_client_order_id,
        "stopPrice": stop_price,
        "icebergQty": iceberg_qty,
        "newOrderRespType": new_order_resp_type,
        "recvWindow": str(recv_window)
    }
    auth_res = auth.sign(params)
    with mock.patch(GET_TIMESTAMP_PATH) as get_timestamp:
        get_timestamp.return_value = timestamp
        req = creator.create_new_order_request(
            symbol=symbol,
            side=side,
            type=type_,
            time_in_force=time_in_force,
            quantity=quantity,
            quote_order_qty=quote_order_qty,
            price=price,
            new_client_order_id=new_client_order_id,
            stop_price=stop_price,
            iceberg_qty=iceberg_qty,
            new_order_resp_type=new_order_resp_type,
            recv_window=recv_window)
    assert req == Request(
        method=method, url=url.with_query(auth_res.params), headers=auth_res.headers)


def test_create_cancel_order_request(creator: BinanceSpotTradingRequestCreator) -> None:
    method = "DELETE"
    url = URL(BASE_URL + "/order")

    symbol = "BTCUSDT"
    order_id = 2345
    orig_client_order_id = "dff"
    new_client_order_id = "df"
    recv_window = 500
    timestamp = 1500

    params = {
        "symbol": symbol,
        "timestamp": str(timestamp)
    }
    auth_res = auth.sign(params)
    req = creator.create_cancel_order_request(
        symbol=symbol,
        timestamp=timestamp)
    assert req == Request(
        method=method, url=url.with_query(auth_res.params), headers=auth_res.headers)

    params = {
        "symbol": symbol,
        "timestamp": str(timestamp),
        "orderId": str(order_id)
    }
    auth_res = auth.sign(params)
    req = creator.create_cancel_order_request(
        symbol=symbol,
        order_id=order_id,
        timestamp=timestamp)
    assert req == Request(
        method=method, url=url.with_query(auth_res.params), headers=auth_res.headers)

    params = {
        "symbol": symbol,
        "timestamp": str(timestamp),
        "orderId": str(order_id),
        "origClientOrderId": orig_client_order_id
    }
    auth_res = auth.sign(params)
    req = creator.create_cancel_order_request(
        symbol=symbol,
        order_id=order_id,
        orig_client_order_id=orig_client_order_id,
        timestamp=timestamp)
    assert req == Request(
        method=method, url=url.with_query(auth_res.params), headers=auth_res.headers)

    params = {
        "symbol": symbol,
        "timestamp": str(timestamp),
        "orderId": str(order_id),
        "origClientOrderId": orig_client_order_id,
        "newClientOrderId": new_client_order_id
    }
    auth_res = auth.sign(params)
    req = creator.create_cancel_order_request(
        symbol=symbol,
        order_id=order_id,
        orig_client_order_id=orig_client_order_id,
        new_client_order_id=new_client_order_id,
        timestamp=timestamp)
    assert req == Request(
        method=method, url=url.with_query(auth_res.params), headers=auth_res.headers)

    params = {
        "symbol": symbol,
        "timestamp": str(timestamp),
        "orderId": str(order_id),
        "origClientOrderId": orig_client_order_id,
        "newClientOrderId": new_client_order_id,
        "recvWindow": str(recv_window)
    }
    auth_res = auth.sign(params)
    req = creator.create_cancel_order_request(
        symbol=symbol,
        order_id=order_id,
        orig_client_order_id=orig_client_order_id,
        new_client_order_id=new_client_order_id,
        recv_window=recv_window,
        timestamp=timestamp)
    assert req == Request(
        method=method, url=url.with_query(auth_res.params), headers=auth_res.headers)

    timestamp = 1400
    params = {
        "symbol": symbol,
        "timestamp": str(timestamp),
        "orderId": str(order_id),
        "origClientOrderId": orig_client_order_id,
        "newClientOrderId": new_client_order_id,
        "recvWindow": str(recv_window)
    }
    auth_res = auth.sign(params)
    with mock.patch(GET_TIMESTAMP_PATH) as get_timestamp:
        get_timestamp.return_value = timestamp
        req = creator.create_cancel_order_request(
            symbol=symbol,
            order_id=order_id,
            orig_client_order_id=orig_client_order_id,
            new_client_order_id=new_client_order_id,
            recv_window=recv_window)
    assert req == Request(
        method=method, url=url.with_query(auth_res.params), headers=auth_res.headers)


def test_create_cancel_orders_request(creator: BinanceSpotTradingRequestCreator) -> None:
    method = "DELETE"
    url = URL(BASE_URL + "/openOrders")

    symbol = "BTCUSDT"
    recv_window = 500
    timestamp = 1500

    params = {
        "symbol": symbol,
        "timestamp": str(timestamp)
    }
    auth_res = auth.sign(params)
    req = creator.create_cancel_orders_request(
        symbol=symbol,
        timestamp=timestamp)
    assert req == Request(
        method=method, url=url.with_query(auth_res.params), headers=auth_res.headers)

    params = {
        "symbol": symbol,
        "timestamp": str(timestamp),
        "recvWindow": str(recv_window)
    }
    auth_res = auth.sign(params)
    req = creator.create_cancel_orders_request(
        symbol=symbol,
        recv_window=recv_window,
        timestamp=timestamp)
    assert req == Request(
        method=method, url=url.with_query(auth_res.params), headers=auth_res.headers)

    timestamp = 1400
    params = {
        "symbol": symbol,
        "timestamp": str(timestamp),
        "recvWindow": str(recv_window)
    }
    auth_res = auth.sign(params)
    with mock.patch(GET_TIMESTAMP_PATH) as get_timestamp:
        get_timestamp.return_value = timestamp
        req = creator.create_cancel_orders_request(
            symbol=symbol,
            recv_window=recv_window)
    assert req == Request(
        method=method, url=url.with_query(auth_res.params), headers=auth_res.headers)


def test_create_query_order_request(creator: BinanceSpotTradingRequestCreator) -> None:
    method = "GET"
    url = URL(BASE_URL + "/order")

    symbol = "BTCUSDT"
    order_id = 2345
    orig_client_order_id = "dff"
    recv_window = 500
    timestamp = 1500

    params = {
        "symbol": symbol,
        "timestamp": str(timestamp)
    }
    auth_res = auth.sign(params)
    req = creator.create_query_order_request(
        symbol=symbol,
        timestamp=timestamp)
    assert req == Request(
        method=method, url=url.with_query(auth_res.params), headers=auth_res.headers)

    params = {
        "symbol": symbol,
        "timestamp": str(timestamp),
        "orderId": str(order_id)
    }
    auth_res = auth.sign(params)
    req = creator.create_query_order_request(
        symbol=symbol,
        order_id=order_id,
        timestamp=timestamp)
    assert req == Request(
        method=method, url=url.with_query(auth_res.params), headers=auth_res.headers)

    params = {
        "symbol": symbol,
        "timestamp": str(timestamp),
        "orderId": str(order_id),
        "origClientOrderId": orig_client_order_id
    }
    auth_res = auth.sign(params)
    req = creator.create_query_order_request(
        symbol=symbol,
        order_id=order_id,
        orig_client_order_id=orig_client_order_id,
        timestamp=timestamp)
    assert req == Request(
        method=method, url=url.with_query(auth_res.params), headers=auth_res.headers)

    params = {
        "symbol": symbol,
        "timestamp": str(timestamp),
        "orderId": str(order_id),
        "origClientOrderId": orig_client_order_id,
        "recvWindow": str(recv_window)
    }
    auth_res = auth.sign(params)
    req = creator.create_query_order_request(
        symbol=symbol,
        order_id=order_id,
        orig_client_order_id=orig_client_order_id,
        recv_window=recv_window,
        timestamp=timestamp)
    assert req == Request(
        method=method, url=url.with_query(auth_res.params), headers=auth_res.headers)

    timestamp = 1400
    params = {
        "symbol": symbol,
        "timestamp": str(timestamp),
        "orderId": str(order_id),
        "origClientOrderId": orig_client_order_id,
        "recvWindow": str(recv_window)
    }
    auth_res = auth.sign(params)
    with mock.patch(GET_TIMESTAMP_PATH) as get_timestamp:
        get_timestamp.return_value = timestamp
        req = creator.create_query_order_request(
            symbol=symbol,
            order_id=order_id,
            orig_client_order_id=orig_client_order_id,
            recv_window=recv_window)
    assert req == Request(
        method=method, url=url.with_query(auth_res.params), headers=auth_res.headers)


def test_create_get_current_open_orders_request(creator: BinanceSpotTradingRequestCreator) -> None:
    method = "GET"
    url = URL(BASE_URL + "/openOrders")

    symbol = "BTCUSDT"
    recv_window = 500
    timestamp = 1500

    params = {
        "timestamp": str(timestamp)
    }
    auth_res = auth.sign(params)
    req = creator.create_get_current_open_orders_request(
        timestamp=timestamp)
    assert req == Request(
        method=method, url=url.with_query(auth_res.params), headers=auth_res.headers)

    params = {
        "timestamp": str(timestamp),
        "symbol": symbol
    }
    auth_res = auth.sign(params)
    req = creator.create_get_current_open_orders_request(
        symbol=symbol,
        timestamp=timestamp)
    assert req == Request(
        method=method, url=url.with_query(auth_res.params), headers=auth_res.headers)

    params = {
        "timestamp": str(timestamp),
        "symbol": symbol,
        "recvWindow": str(recv_window)
    }
    auth_res = auth.sign(params)
    req = creator.create_get_current_open_orders_request(
        symbol=symbol,
        recv_window=recv_window,
        timestamp=timestamp)
    assert req == Request(
        method=method, url=url.with_query(auth_res.params), headers=auth_res.headers)

    timestamp = 1400
    params = {
        "timestamp": str(timestamp),
        "symbol": symbol,
        "recvWindow": str(recv_window)
    }
    auth_res = auth.sign(params)
    with mock.patch(GET_TIMESTAMP_PATH) as get_timestamp:
        get_timestamp.return_value = timestamp
        req = creator.create_get_current_open_orders_request(
            symbol=symbol,
            recv_window=recv_window)
    assert req == Request(
        method=method, url=url.with_query(auth_res.params), headers=auth_res.headers)


def test_create_get_all_orders_request(creator: BinanceSpotTradingRequestCreator) -> None:
    method = "GET"
    url = URL(BASE_URL + "/allOrders")

    symbol = "BTCUSDT"
    order_id = 14
    start_time = 1401
    end_time = 1402
    limit = 10
    recv_window = 500
    timestamp = 1500

    params = {
        "symbol": symbol,
        "timestamp": str(timestamp)
    }
    auth_res = auth.sign(params)
    req = creator.create_get_all_orders_request(
        symbol=symbol,
        timestamp=timestamp)
    assert req == Request(
        method=method, url=url.with_query(auth_res.params), headers=auth_res.headers)

    params = {
        "symbol": symbol,
        "timestamp": str(timestamp),
        "orderId": str(order_id)
    }
    auth_res = auth.sign(params)
    req = creator.create_get_all_orders_request(
        symbol=symbol,
        order_id=order_id,
        timestamp=timestamp)
    assert req == Request(
        method=method, url=url.with_query(auth_res.params), headers=auth_res.headers)

    params = {
        "symbol": symbol,
        "timestamp": str(timestamp),
        "orderId": str(order_id),
        "startTime": str(start_time)
    }
    auth_res = auth.sign(params)
    req = creator.create_get_all_orders_request(
        symbol=symbol,
        order_id=order_id,
        start_time=start_time,
        timestamp=timestamp)
    assert req == Request(
        method=method, url=url.with_query(auth_res.params), headers=auth_res.headers)

    params = {
        "symbol": symbol,
        "timestamp": str(timestamp),
        "orderId": str(order_id),
        "startTime": str(start_time),
        "endTime": str(end_time)
    }
    auth_res = auth.sign(params)
    req = creator.create_get_all_orders_request(
        symbol=symbol,
        order_id=order_id,
        start_time=start_time,
        end_time=end_time,
        timestamp=timestamp)
    assert req == Request(
        method=method, url=url.with_query(auth_res.params), headers=auth_res.headers)

    params = {
        "symbol": symbol,
        "timestamp": str(timestamp),
        "orderId": str(order_id),
        "startTime": str(start_time),
        "endTime": str(end_time),
        "limit": str(limit)
    }
    auth_res = auth.sign(params)
    req = creator.create_get_all_orders_request(
        symbol=symbol,
        order_id=order_id,
        start_time=start_time,
        end_time=end_time,
        limit=limit,
        timestamp=timestamp)
    assert req == Request(
        method=method, url=url.with_query(auth_res.params), headers=auth_res.headers)

    params = {
        "symbol": symbol,
        "timestamp": str(timestamp),
        "orderId": str(order_id),
        "startTime": str(start_time),
        "endTime": str(end_time),
        "limit": str(limit),
        "recvWindow": str(recv_window)
    }
    auth_res = auth.sign(params)
    req = creator.create_get_all_orders_request(
        symbol=symbol,
        order_id=order_id,
        start_time=start_time,
        end_time=end_time,
        limit=limit,
        recv_window=recv_window,
        timestamp=timestamp)
    assert req == Request(
        method=method, url=url.with_query(auth_res.params), headers=auth_res.headers)

    timestamp = 1400
    params = {
        "symbol": symbol,
        "timestamp": str(timestamp),
        "orderId": str(order_id),
        "startTime": str(start_time),
        "endTime": str(end_time),
        "limit": str(limit),
        "recvWindow": str(recv_window)
    }
    auth_res = auth.sign(params)
    with mock.patch(GET_TIMESTAMP_PATH) as get_timestamp:
        get_timestamp.return_value = timestamp
        req = creator.create_get_all_orders_request(
            symbol=symbol,
            order_id=order_id,
            start_time=start_time,
            end_time=end_time,
            limit=limit,
            recv_window=recv_window)
    assert req == Request(
        method=method, url=url.with_query(auth_res.params), headers=auth_res.headers)


def test_create_get_account_info_request(creator: BinanceSpotTradingRequestCreator) -> None:
    method = "GET"
    url = URL(BASE_URL + "/account")

    recv_window = 500
    timestamp = 1500

    params = {
        "timestamp": str(timestamp),
    }
    auth_res = auth.sign(params)
    req = creator.create_get_account_info_request(
        timestamp=timestamp)
    assert req == Request(
        method=method, url=url.with_query(auth_res.params), headers=auth_res.headers)

    params = {
        "timestamp": str(timestamp),
        "recvWindow": str(recv_window)
    }
    auth_res = auth.sign(params)
    req = creator.create_get_account_info_request(
        recv_window=recv_window,
        timestamp=timestamp)
    assert req == Request(
        method=method, url=url.with_query(auth_res.params), headers=auth_res.headers)

    timestamp = 1400
    params = {
        "timestamp": str(timestamp),
        "recvWindow": str(recv_window)
    }
    auth_res = auth.sign(params)
    with mock.patch(GET_TIMESTAMP_PATH) as get_timestamp:
        get_timestamp.return_value = timestamp
        req = creator.create_get_account_info_request(
            recv_window=recv_window)
    assert req == Request(
        method=method, url=url.with_query(auth_res.params), headers=auth_res.headers)


def test_create_get_trades_request(creator: BinanceSpotTradingRequestCreator) -> None:
    method = "GET"
    url = URL(BASE_URL + "/myTrades")

    symbol = "BTCUSDT"
    start_time = 1401
    end_time = 1402
    from_id = 14
    limit = 10
    recv_window = 500
    timestamp = 1500

    params = {
        "symbol": symbol,
        "timestamp": str(timestamp)
    }
    auth_res = auth.sign(params)
    req = creator.create_get_trades_request(
        symbol=symbol,
        timestamp=timestamp)
    assert req == Request(
        method=method, url=url.with_query(auth_res.params), headers=auth_res.headers)

    params = {
        "symbol": symbol,
        "timestamp": str(timestamp),
        "startTime": str(start_time),
    }
    auth_res = auth.sign(params)
    req = creator.create_get_trades_request(
        symbol=symbol,
        start_time=start_time,
        timestamp=timestamp)
    assert req == Request(
        method=method, url=url.with_query(auth_res.params), headers=auth_res.headers)

    params = {
        "symbol": symbol,
        "timestamp": str(timestamp),
        "startTime": str(start_time),
        "fromId": str(from_id)
    }
    auth_res = auth.sign(params)
    req = creator.create_get_trades_request(
        symbol=symbol,
        start_time=start_time,
        from_id=from_id,
        timestamp=timestamp)
    assert req == Request(
        method=method, url=url.with_query(auth_res.params), headers=auth_res.headers)

    params = {
        "symbol": symbol,
        "timestamp": str(timestamp),
        "startTime": str(start_time),
        "endTime": str(end_time),
        "fromId": str(from_id),
    }
    auth_res = auth.sign(params)
    req = creator.create_get_trades_request(
        symbol=symbol,
        start_time=start_time,
        end_time=end_time,
        from_id=from_id,
        timestamp=timestamp)
    assert req == Request(
        method=method, url=url.with_query(auth_res.params), headers=auth_res.headers)

    params = {
        "symbol": symbol,
        "timestamp": str(timestamp),
        "startTime": str(start_time),
        "endTime": str(end_time),
        "fromId": str(from_id),
        "limit": str(limit)
    }
    auth_res = auth.sign(params)
    req = creator.create_get_trades_request(
        symbol=symbol,
        start_time=start_time,
        end_time=end_time,
        from_id=from_id,
        limit=limit,
        timestamp=timestamp)
    assert req == Request(
        method=method, url=url.with_query(auth_res.params), headers=auth_res.headers)

    params = {
        "symbol": symbol,
        "timestamp": str(timestamp),
        "startTime": str(start_time),
        "endTime": str(end_time),
        "fromId": str(from_id),
        "limit": str(limit),
        "recvWindow": str(recv_window)
    }
    auth_res = auth.sign(params)
    req = creator.create_get_trades_request(
        symbol=symbol,
        start_time=start_time,
        end_time=end_time,
        from_id=from_id,
        limit=limit,
        recv_window=recv_window,
        timestamp=timestamp)
    assert req == Request(
        method=method, url=url.with_query(auth_res.params), headers=auth_res.headers)

    timestamp = 1400
    params = {
        "symbol": symbol,
        "timestamp": str(timestamp),
        "startTime": str(start_time),
        "endTime": str(end_time),
        "fromId": str(from_id),
        "limit": str(limit),
        "recvWindow": str(recv_window)
    }
    auth_res = auth.sign(params)
    with mock.patch(GET_TIMESTAMP_PATH) as get_timestamp:
        get_timestamp.return_value = timestamp
        req = creator.create_get_trades_request(
            symbol=symbol,
            start_time=start_time,
            end_time=end_time,
            from_id=from_id,
            limit=limit,
            recv_window=recv_window)
    assert req == Request(
        method=method, url=url.with_query(auth_res.params), headers=auth_res.headers)
