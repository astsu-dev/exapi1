from typing import Final

import pytest
from exapi.models.binance.typedefs import Interval
from exapi.requesters.binance.auth import BinanceKeyAuth
from exapi.requesters.binance.market_data.request_creator import \
    BinanceMarketDataRequestCreator
from exapi.requesters.request import Request
from yarl import URL

API_KEY: Final[str] = "aaa"


@pytest.fixture(scope="module")
def creator() -> BinanceMarketDataRequestCreator:
    auth = BinanceKeyAuth(API_KEY)
    return BinanceMarketDataRequestCreator(auth)


def test_create_ping_request(creator: BinanceMarketDataRequestCreator) -> None:
    method = "GET"
    url = URL("https://api.binance.com/api/v3/ping")
    expected = Request(method=method, url=url)
    assert creator.create_ping_request() == expected


def test_create_get_server_time_request(creator: BinanceMarketDataRequestCreator) -> None:
    method = "GET"
    url = URL("https://api.binance.com/api/v3/time")
    expected = Request(method=method, url=url)
    assert creator.create_get_server_time_request() == expected


def test_create_get_exchange_info_request(creator: BinanceMarketDataRequestCreator) -> None:
    method = "GET"
    url = URL("https://api.binance.com/api/v3/exchangeInfo")
    expected = Request(method=method, url=url)
    assert creator.create_get_exchange_info_request() == expected


def test_create_get_order_book_request(creator: BinanceMarketDataRequestCreator) -> None:
    method = "GET"
    url = URL("https://api.binance.com/api/v3/depth")

    symbol = "BTCUSDT"
    url = url.with_query(
        {
            "symbol": symbol
        }
    )
    expected = Request(method=method, url=url)
    assert creator.create_get_order_book_request(symbol=symbol) == expected

    limit = 5
    url = url.with_query(
        {
            "symbol": symbol,
            "limit": limit
        }
    )
    expected = Request(method=method, url=url)
    assert creator.create_get_order_book_request(
        symbol=symbol, limit=limit) == expected


def test_create_get_trades_request(creator: BinanceMarketDataRequestCreator) -> None:
    method = "GET"
    url = URL("https://api.binance.com/api/v3/trades")

    symbol = "BTCUSDT"
    url = url.with_query(
        {
            "symbol": symbol
        }
    )
    expected = Request(method=method, url=url)
    assert creator.create_get_trades_request(symbol=symbol) == expected

    limit = 5
    url = url.with_query(
        {
            "symbol": symbol,
            "limit": limit
        }
    )
    expected = Request(method=method, url=url)
    assert creator.create_get_trades_request(
        symbol=symbol, limit=limit) == expected


def test_create_get_old_trades_request(creator: BinanceMarketDataRequestCreator) -> None:
    method = "GET"
    url = URL("https://api.binance.com/api/v3/historicalTrades")
    headers = {
        "X-MBX-APIKEY": API_KEY
    }

    symbol = "BTCUSDT"
    url = url.with_query(
        {
            "symbol": symbol
        }
    )
    expected = Request(method=method, url=url, headers=headers)
    assert creator.create_get_old_trades_request(symbol=symbol) == expected

    limit = 5
    url = url.with_query(
        {
            "symbol": symbol,
            "limit": limit
        }
    )
    expected = Request(method=method, url=url, headers=headers)
    assert creator.create_get_old_trades_request(
        symbol=symbol, limit=limit) == expected

    from_id = 100
    url = url.with_query(
        {
            "symbol": symbol,
            "limit": limit,
            "fromId": str(from_id)
        }
    )
    expected = Request(method=method, url=url, headers=headers)
    assert creator.create_get_old_trades_request(
        symbol=symbol, limit=limit, from_id=from_id) == expected


def test_create_get_aggregate_trades_request(creator: BinanceMarketDataRequestCreator) -> None:
    method = "GET"
    url = URL("https://api.binance.com/api/v3/aggTrades")

    symbol = "BTCUSDT"
    url = url.with_query(
        {
            "symbol": symbol
        }
    )
    expected = Request(method=method, url=url)
    assert creator.create_get_aggregate_trades_request(
        symbol=symbol) == expected

    from_id = 100
    url = url.with_query(
        {
            "symbol": symbol,
            "fromId": str(from_id)
        }
    )
    expected = Request(method=method, url=url)
    assert creator.create_get_aggregate_trades_request(
        symbol=symbol, from_id=from_id) == expected

    start_time = 1000
    url = url.with_query(
        {
            "symbol": symbol,
            "fromId": str(from_id),
            "startTime": str(start_time),
        }
    )
    expected = Request(method=method, url=url)
    assert creator.create_get_aggregate_trades_request(
        symbol=symbol, from_id=from_id, start_time=start_time) == expected

    end_time = 1000
    url = url.with_query(
        {
            "symbol": symbol,
            "fromId": str(from_id),
            "startTime": str(start_time),
            "endTime": str(end_time),
        }
    )
    expected = Request(method=method, url=url)
    assert creator.create_get_aggregate_trades_request(
        symbol=symbol, from_id=from_id,
        start_time=start_time, end_time=end_time) == expected

    limit = 100
    url = url.with_query(
        {
            "symbol": symbol,
            "fromId": str(from_id),
            "startTime": str(start_time),
            "endTime": str(end_time),
            "limit": str(limit),
        }
    )
    expected = Request(method=method, url=url)
    assert creator.create_get_aggregate_trades_request(
        symbol=symbol, from_id=from_id,
        start_time=start_time, end_time=end_time,
        limit=limit) == expected


def test_create_get_candles_request(creator: BinanceMarketDataRequestCreator) -> None:
    method = "GET"
    url = URL("https://api.binance.com/api/v3/klines")

    symbol = "BTCUSDT"
    interval: Interval = "1m"
    url = url.with_query(
        {
            "symbol": symbol,
            "interval": interval
        }
    )
    expected = Request(method=method, url=url)
    assert creator.create_get_candles_request(
        symbol=symbol, interval=interval) == expected

    start_time = 1000
    url = url.with_query(
        {
            "symbol": symbol,
            "interval": interval,
            "startTime": str(start_time),
        }
    )
    expected = Request(method=method, url=url)
    assert creator.create_get_candles_request(
        symbol=symbol, interval=interval, start_time=start_time) == expected

    end_time = 1000
    url = url.with_query(
        {
            "symbol": symbol,
            "interval": interval,
            "startTime": str(start_time),
            "endTime": str(end_time),
        }
    )
    expected = Request(method=method, url=url)
    assert creator.create_get_candles_request(
        symbol=symbol, interval=interval,
        start_time=start_time, end_time=end_time) == expected

    limit = 100
    url = url.with_query(
        {
            "symbol": symbol,
            "interval": interval,
            "startTime": str(start_time),
            "endTime": str(end_time),
            "limit": str(limit),
        }
    )
    expected = Request(method=method, url=url)
    assert creator.create_get_candles_request(
        symbol=symbol, interval=interval,
        start_time=start_time, end_time=end_time,
        limit=limit) == expected


def test_create_get_average_price_request(creator: BinanceMarketDataRequestCreator) -> None:
    method = "GET"
    url = URL("https://api.binance.com/api/v3/avgPrice")

    symbol = "BTCUSDT"
    url = url.with_query(
        {
            "symbol": symbol
        }
    )
    expected = Request(method=method, url=url)
    assert creator.create_get_average_price_request(symbol=symbol) == expected


def test_create_get_ticker_price_change_stat_request(creator: BinanceMarketDataRequestCreator) -> None:
    method = "GET"
    url = URL("https://api.binance.com/api/v3/ticker/24hr")

    expected = Request(method=method, url=url)
    assert creator.create_get_ticker_price_change_stat_request() == expected

    symbol = "BTCUSDT"
    url = url.with_query(
        {
            "symbol": symbol
        }
    )
    expected = Request(method=method, url=url)
    assert creator.create_get_ticker_price_change_stat_request(
        symbol=symbol) == expected


def test_create_get_price_ticker_request(creator: BinanceMarketDataRequestCreator) -> None:
    method = "GET"
    url = URL("https://api.binance.com/api/v3/ticker/price")

    expected = Request(method=method, url=url)
    assert creator.create_get_price_ticker_request() == expected

    symbol = "BTCUSDT"
    url = url.with_query(
        {
            "symbol": symbol
        }
    )
    expected = Request(method=method, url=url)
    assert creator.create_get_price_ticker_request(
        symbol=symbol) == expected


def test_create_get_order_book_ticker_request(creator: BinanceMarketDataRequestCreator) -> None:
    method = "GET"
    url = URL("https://api.binance.com/api/v3/ticker/bookTicker")

    expected = Request(method=method, url=url)
    assert creator.create_get_order_book_ticker_request() == expected

    symbol = "BTCUSDT"
    url = url.with_query(
        {
            "symbol": symbol
        }
    )
    expected = Request(method=method, url=url)
    assert creator.create_get_order_book_ticker_request(
        symbol=symbol) == expected
