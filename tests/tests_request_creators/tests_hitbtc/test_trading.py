import pytest
from yarl import URL

from exapi.request_creators.hitbtc.trading import \
    HitbtcTradingRequestCreator
from exapi.request_creators.request import Request
from exapi.requesters.hitbtc.auth import HitbtcAuth


@pytest.fixture(scope="module")
def creator() -> HitbtcTradingRequestCreator:
    auth = HitbtcAuth("aa", "aa")
    return HitbtcTradingRequestCreator(auth)


@pytest.fixture(scope="module")
def auth() -> HitbtcAuth:
    return HitbtcAuth("aa", "aa")


def test_create_get_trading_balance_request(creator: HitbtcTradingRequestCreator, auth: HitbtcAuth) -> None:
    expected = Request(
        method="GET",
        url=URL("https://api.hitbtc.com/api/2/trading/balance"),
        headers=auth.sign(
            method="GET", url_path="/api/2/trading/balance", url_query=""))
    req = creator.create_get_trading_balance_request()
    assert req == expected


def test_create_get_active_orders_request(creator: HitbtcTradingRequestCreator, auth: HitbtcAuth) -> None:
    expected = Request(
        method="GET",
        url=URL("https://api.hitbtc.com/api/2/order"),
        headers=auth.sign(
            method="GET", url_path="/api/2/order", url_query=""))
    req = creator.create_get_active_orders_request()
    assert req == expected

    expected = Request(
        method="GET",
        url=URL("https://api.hitbtc.com/api/2/order?symbol=BTCUSD"),
        headers=auth.sign(
            method="GET", url_path="/api/2/order", url_query="symbol=BTCUSD"))
    req = creator.create_get_active_orders_request("BTCUSD")
    assert req == expected


def test_create_get_active_order_request(creator: HitbtcTradingRequestCreator, auth: HitbtcAuth) -> None:
    expected = Request(
        method="GET",
        url=URL("https://api.hitbtc.com/api/2/order/15"),
        headers=auth.sign(
            method="GET", url_path="/api/2/order/15", url_query=""))
    req = creator.create_get_active_order_request(client_order_id=15)
    assert req == expected

    expected = Request(
        method="GET",
        url=URL("https://api.hitbtc.com/api/2/order/15?wait=10000"),
        headers=auth.sign(
            method="GET", url_path="/api/2/order/15", url_query="wait=10000"))
    req = creator.create_get_active_order_request(
        client_order_id=15, wait=10000)
    assert req == expected


def test_create_new_order_request(creator: HitbtcTradingRequestCreator, auth: HitbtcAuth) -> None:
    url = "https://api.hitbtc.com/api/2/order"
    method = "POST"

    expected = Request(
        method=method,
        url=URL(url + "?symbol=BTCUSD&side=buy&quantity=0.5"),
        headers=auth.sign(
            method=method,
            url_path="/api/2/order",
            url_query="symbol=BTCUSD&side=buy&quantity=0.5"))
    req = creator.create_new_order_request(
        symbol="BTCUSD",
        side="buy",
        quantity="0.5")
    assert req == expected

    expected = Request(
        method=method,
        url=URL(url + "?symbol=BTCUSD&side=buy&quantity=0.5&price=0.1"),
        headers=auth.sign(
            method=method,
            url_path="/api/2/order",
            url_query="symbol=BTCUSD&side=buy&quantity=0.5&price=0.1"))
    req = creator.create_new_order_request(
        symbol="BTCUSD",
        side="buy",
        quantity="0.5",
        price="0.1")
    assert req == expected

    expected = Request(
        method=method,
        url=URL(url + "?symbol=BTCUSD&side=buy&quantity=0.5&price=0.1&type=limit"),
        headers=auth.sign(
            method=method,
            url_path="/api/2/order",
            url_query="symbol=BTCUSD&side=buy&quantity=0.5&price=0.1&type=limit"))
    req = creator.create_new_order_request(
        symbol="BTCUSD",
        side="buy",
        quantity="0.5",
        price="0.1",
        type_="limit")
    assert req == expected

    expected = Request(
        method=method,
        url=URL(
            url + "?symbol=BTCUSD&side=buy&quantity=0.5&price=0.1&type=limit&timeInForce=GTC"),
        headers=auth.sign(
            method=method,
            url_path="/api/2/order",
            url_query="symbol=BTCUSD&side=buy&quantity=0.5&price=0.1&type=limit&timeInForce=GTC"))
    req = creator.create_new_order_request(
        symbol="BTCUSD",
        side="buy",
        quantity="0.5",
        price="0.1",
        type_="limit",
        time_in_force="GTC")
    assert req == expected

    expected = Request(
        method=method,
        url=URL(
            url + "?symbol=BTCUSD&side=buy"
                  "&quantity=0.5&price=0.1&type=limit&timeInForce=GTC"
                  "&stopPrice=0.15"),
        headers=auth.sign(
            method=method,
            url_path="/api/2/order",
            url_query="symbol=BTCUSD&side=buy"
                      "&quantity=0.5&price=0.1&type=limit&timeInForce=GTC"
                      "&stopPrice=0.15"))
    req = creator.create_new_order_request(
        symbol="BTCUSD",
        side="buy",
        quantity="0.5",
        price="0.1",
        type_="limit",
        time_in_force="GTC",
        stop_price="0.15")
    assert req == expected

    expected = Request(
        method=method,
        url=URL(
            url + "?symbol=BTCUSD&side=buy" +
            "&quantity=0.5&price=0.1&type=limit&timeInForce=GTC"
            "&stopPrice=0.15&expireTime=1234"),
        headers=auth.sign(
            method=method,
            url_path="/api/2/order",
            url_query="symbol=BTCUSD&side=buy"
                      "&quantity=0.5&price=0.1&type=limit&timeInForce=GTC"
                      "&stopPrice=0.15&expireTime=1234"))
    req = creator.create_new_order_request(
        symbol="BTCUSD",
        side="buy",
        quantity="0.5",
        price="0.1",
        type_="limit",
        time_in_force="GTC",
        stop_price="0.15",
        expire_time="1234")
    assert req == expected

    expected = Request(
        method=method,
        url=URL(
            url + "?symbol=BTCUSD&side=buy" +
            "&quantity=0.5&price=0.1&type=limit&timeInForce=GTC"
            "&stopPrice=0.15&expireTime=1234&strictValidate=true"),
        headers=auth.sign(
            method=method,
            url_path="/api/2/order",
            url_query="symbol=BTCUSD&side=buy"
                      "&quantity=0.5&price=0.1&type=limit&timeInForce=GTC"
                      "&stopPrice=0.15&expireTime=1234&strictValidate=true"))
    req = creator.create_new_order_request(
        symbol="BTCUSD",
        side="buy",
        quantity="0.5",
        price="0.1",
        type_="limit",
        time_in_force="GTC",
        stop_price="0.15",
        expire_time="1234",
        strict_validate=True)
    assert req == expected

    expected = Request(
        method=method,
        url=URL(
            url + "?symbol=BTCUSD&side=buy" +
            "&quantity=0.5&price=0.1&type=limit&timeInForce=GTC"
            "&stopPrice=0.15&expireTime=1234&strictValidate=true"
            "&postOnly=true"),
        headers=auth.sign(
            method=method,
            url_path="/api/2/order",
            url_query="symbol=BTCUSD&side=buy"
                      "&quantity=0.5&price=0.1&type=limit&timeInForce=GTC"
                      "&stopPrice=0.15&expireTime=1234&strictValidate=true"
                      "&postOnly=true"))
    req = creator.create_new_order_request(
        symbol="BTCUSD",
        side="buy",
        quantity="0.5",
        price="0.1",
        type_="limit",
        time_in_force="GTC",
        stop_price="0.15",
        expire_time="1234",
        strict_validate=True,
        post_only=True)
    assert req == expected

    url += "/15"
    method = "PUT"

    expected = Request(
        method=method,
        url=URL(
            url + "?symbol=BTCUSD&side=buy" +
            "&quantity=0.5&price=0.1&type=limit&timeInForce=GTC"
            "&stopPrice=0.15&expireTime=1234&strictValidate=true"
            "&postOnly=true"),
        headers=auth.sign(
            method=method,
            url_path="/api/2/order/15",
            url_query="symbol=BTCUSD&side=buy"
                      "&quantity=0.5&price=0.1&type=limit&timeInForce=GTC"
                      "&stopPrice=0.15&expireTime=1234&strictValidate=true"
                      "&postOnly=true"))
    req = creator.create_new_order_request(
        symbol="BTCUSD",
        side="buy",
        quantity="0.5",
        price="0.1",
        type_="limit",
        time_in_force="GTC",
        stop_price="0.15",
        expire_time="1234",
        strict_validate=True,
        post_only=True,
        client_order_id=15)
    assert req == expected


def test_create_cancel_orders_request(creator: HitbtcTradingRequestCreator, auth: HitbtcAuth) -> None:
    expected = Request(
        method="DELETE",
        url=URL("https://api.hitbtc.com/api/2/order"),
        headers=auth.sign(
            method="DELETE", url_path="/api/2/order", url_query=""))
    req = creator.create_cancel_orders_request()
    assert req == expected

    expected = Request(
        method="DELETE",
        url=URL("https://api.hitbtc.com/api/2/order?symbol=BTCUSD"),
        headers=auth.sign(
            method="DELETE", url_path="/api/2/order", url_query="symbol=BTCUSD"))
    req = creator.create_cancel_orders_request("BTCUSD")
    assert req == expected


def test_create_get_fee_request(creator: HitbtcTradingRequestCreator, auth: HitbtcAuth) -> None:
    expected = Request(
        method="GET",
        url=URL("https://api.hitbtc.com/api/2/trading/fee/BTCUSD"),
        headers=auth.sign(
            method="GET", url_path="/api/2/trading/fee/BTCUSD", url_query=""))
    req = creator.create_get_fee_request("BTCUSD")
    assert req == expected
