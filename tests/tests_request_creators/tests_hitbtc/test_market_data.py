import pytest
from yarl import URL

from exapi.request_creators.hitbtc.market_data import \
    HitbtcMarketDataRequestCreator
from exapi.request_creators.request import Request


@pytest.fixture(scope="module")
def creator() -> HitbtcMarketDataRequestCreator:
    return HitbtcMarketDataRequestCreator()


def test_create_get_currencies_request(creator: HitbtcMarketDataRequestCreator) -> None:
    url = URL("https://api.hitbtc.com/api/2/public/currency")
    expected = Request(
        method="GET",
        url=url)
    assert creator.create_get_currencies_request() == expected

    url = url.with_query({"currencies": "BTC,ETH"})
    expected = Request(method="GET", url=url)
    assert creator.create_get_currencies_request(
        ["BTC", "ETH"]) == expected


def test_create_get_certain_currency_request(creator: HitbtcMarketDataRequestCreator) -> None:
    url = URL("https://api.hitbtc.com/api/2/public/currency/BTC")
    expected = Request(method="GET", url=url)
    assert creator.create_get_certain_currency_request("BTC") == expected


def test_create_get_symbols_request(creator: HitbtcMarketDataRequestCreator) -> None:
    url = URL("https://api.hitbtc.com/api/2/public/symbol")
    expected = Request(method="GET", url=url)
    assert creator.create_get_symbols_request() == expected

    url = url.with_query({"symbols": "ETHBTC,BTCUSD"})
    expected = Request(method="GET", url=url)
    assert creator.create_get_symbols_request(
        ["ETHBTC", "BTCUSD"]) == expected


def test_create_get_certain_symbol_request(creator: HitbtcMarketDataRequestCreator) -> None:
    url = URL("https://api.hitbtc.com/api/2/public/symbol/BTCUSD")
    expected = Request(method="GET", url=url)
    assert creator.create_get_certain_symbol_request("BTCUSD") == expected


def test_create_get_tickers_request(creator: HitbtcMarketDataRequestCreator) -> None:
    url = URL("https://api.hitbtc.com/api/2/public/ticker")
    expected = Request(method="GET", url=url)
    assert creator.create_get_tickers_request() == expected

    url = url.with_query({"symbols": "ETHBTC,BTCUSD"})
    expected = Request(method="GET", url=url)
    assert creator.create_get_tickers_request(
        ["ETHBTC", "BTCUSD"]) == expected


def test_create_get_certain_ticker_request(creator: HitbtcMarketDataRequestCreator) -> None:
    url = URL("https://api.hitbtc.com/api/2/public/ticker/BTCUSD")
    expected = Request(method="GET", url=url)
    assert creator.create_get_certain_ticker_request("BTCUSD") == expected


def test_create_get_trades_request(creator: HitbtcMarketDataRequestCreator) -> None:
    url = URL("https://api.hitbtc.com/api/2/public/trades")
    expected = Request(
        method="GET", url=url)
    assert creator.create_get_trades_request() == expected

    url = url.with_query({"symbols": "ETHBTC,BTCUSD"})
    expected = Request(method="GET", url=url)
    assert creator.create_get_trades_request(
        symbols=["ETHBTC", "BTCUSD"]) == expected

    url = url.with_query({"symbols": "ETHBTC,BTCUSD", "sort": "ASC"})
    expected = Request(method="GET", url=url)
    assert creator.create_get_trades_request(
        symbols=["ETHBTC", "BTCUSD"], sort="ASC") == expected

    url = url.with_query({"symbols": "ETHBTC,BTCUSD",
                          "sort": "ASC", "from": "150"})
    expected = Request(method="GET", url=url)
    assert creator.create_get_trades_request(
        symbols=["ETHBTC", "BTCUSD"], sort="ASC", from_=150) == expected

    url = url.with_query({"symbols": "ETHBTC,BTCUSD",
                          "sort": "ASC", "from": "150",
                          "till": "160"})
    expected = Request(method="GET", url=url)
    assert creator.create_get_trades_request(
        symbols=["ETHBTC", "BTCUSD"], sort="ASC", from_=150, till=160) == expected

    url = url.with_query({"symbols": "ETHBTC,BTCUSD",
                          "sort": "ASC", "from": "150",
                          "till": "160", "limit": "500"})
    expected = Request(method="GET", url=url)
    assert creator.create_get_trades_request(
        symbols=["ETHBTC", "BTCUSD"], sort="ASC", from_=150, till=160, limit=500) == expected

    url = url.with_query({"symbols": "ETHBTC,BTCUSD",
                          "sort": "ASC", "from": "150",
                          "till": "160", "limit": "500",
                          "offset": "100"})
    expected = Request(method="GET", url=url)
    assert creator.create_get_trades_request(
        symbols=["ETHBTC", "BTCUSD"], sort="ASC",
        from_=150, till=160, limit=500, offset=100) == expected


def test_create_get_certain_trades_request(creator: HitbtcMarketDataRequestCreator) -> None:
    url = URL("https://api.hitbtc.com/api/2/public/trades/BTCUSD")
    expected = Request(method="GET", url=url)
    assert creator.create_get_certain_trades_request("BTCUSD") == expected

    url = url.with_query({"sort": "ASC"})
    expected = Request(method="GET", url=url)
    assert creator.create_get_certain_trades_request(
        symbol="BTCUSD", sort="ASC") == expected

    url = url.with_query({"sort": "ASC", "by": "timestamp"})
    expected = Request(method="GET", url=url)
    assert creator.create_get_certain_trades_request(
        symbol="BTCUSD", sort="ASC", by="timestamp") == expected

    url = url.with_query({"sort": "ASC", "by": "timestamp",
                          "from": "150"})
    expected = Request(method="GET", url=url)
    assert creator.create_get_certain_trades_request(
        symbol="BTCUSD", sort="ASC", by="timestamp", from_=150) == expected

    url = url.with_query({"sort": "ASC", "by": "timestamp",
                          "from": "150", "till": "160"})
    expected = Request(method="GET", url=url)
    assert creator.create_get_certain_trades_request(
        symbol="BTCUSD", sort="ASC", by="timestamp", from_=150, till=160) == expected

    url = url.with_query({"sort": "ASC", "by": "timestamp",
                          "from": "150", "till": "160",
                          "limit": "500"})
    expected = Request(method="GET", url=url)
    assert creator.create_get_certain_trades_request(
        symbol="BTCUSD", sort="ASC", by="timestamp", from_=150, till=160, limit=500) == expected

    url = url.with_query({"sort": "ASC", "by": "timestamp",
                          "from": "150", "till": "160",
                          "limit": "500", "offset": "100"})
    expected = Request(method="GET", url=url)
    assert creator.create_get_certain_trades_request(
        symbol="BTCUSD", sort="ASC",
        by="timestamp", from_=150, till=160, limit=500, offset=100) == expected


def test_create_get_orderbooks_request(creator: HitbtcMarketDataRequestCreator) -> None:
    url = URL("https://api.hitbtc.com/api/2/public/orderbook")
    expected = Request(method="GET", url=url)
    assert creator.create_get_orderbooks_request() == expected

    url = url.with_query({"symbols": "ETHBTC,BTCUSD"})
    expected = Request(
        method="GET",
        url=url)
    assert creator.create_get_orderbooks_request(
        ["ETHBTC", "BTCUSD"]) == expected

    url = url.with_query({"symbols": "ETHBTC,BTCUSD", "limit": "0"})
    expected = Request(method="GET", url=url)
    assert creator.create_get_orderbooks_request(
        ["ETHBTC", "BTCUSD"], 0) == expected


def test_create_get_certain_orderbook_request(creator: HitbtcMarketDataRequestCreator) -> None:
    url = URL("https://api.hitbtc.com/api/2/public/orderbook/BTCUSD")
    expected = Request(method="GET", url=url)
    assert creator.create_get_certain_orderbook_request("BTCUSD") == expected

    url = url.with_query({"limit": "0", "volume": "15"})
    expected = Request(method="GET", url=url)
    assert creator.create_get_certain_orderbook_request(
        "BTCUSD", limit=0, volume=15) == expected

    url = url.with_query({"limit": "0"})
    expected = Request(method="GET", url=url)
    assert creator.create_get_certain_orderbook_request(
        "BTCUSD", 0) == expected


def test_create_get_candles_request(creator: HitbtcMarketDataRequestCreator) -> None:
    url = URL("https://api.hitbtc.com/api/2/public/candles")
    expected = Request(
        method="GET", url=url)
    assert creator.create_get_candles_request() == expected

    url = url.with_query({"symbols": "ETHBTC,BTCUSD"})
    expected = Request(method="GET", url=url)
    assert creator.create_get_candles_request(
        symbols=["ETHBTC", "BTCUSD"]) == expected

    url = url.with_query({"symbols": "ETHBTC,BTCUSD", "period": "1M"})
    expected = Request(method="GET", url=url)
    assert creator.create_get_candles_request(
        symbols=["ETHBTC", "BTCUSD"], period="1M") == expected

    url = url.with_query({"symbols": "ETHBTC,BTCUSD", "period": "1M",
                          "sort": "ASC"})
    expected = Request(method="GET", url=url)
    assert creator.create_get_candles_request(
        symbols=["ETHBTC", "BTCUSD"], period="1M", sort="ASC") == expected

    url = url.with_query({"symbols": "ETHBTC,BTCUSD", "period": "1M",
                          "sort": "ASC", "from": "150"})
    expected = Request(method="GET", url=url)
    assert creator.create_get_candles_request(
        symbols=["ETHBTC", "BTCUSD"], period="1M", sort="ASC", from_=150) == expected

    url = url.with_query({"symbols": "ETHBTC,BTCUSD", "period": "1M",
                          "sort": "ASC", "from": "150", "till": "160"})
    expected = Request(method="GET", url=url)
    assert creator.create_get_candles_request(
        symbols=["ETHBTC", "BTCUSD"], period="1M", sort="ASC", from_=150, till=160) == expected

    url = url.with_query({"symbols": "ETHBTC,BTCUSD", "period": "1M",
                          "sort": "ASC", "from": "150", "till": "160",
                          "limit": "500"})
    expected = Request(method="GET", url=url)
    assert creator.create_get_candles_request(
        symbols=["ETHBTC", "BTCUSD"], period="1M", sort="ASC",
        from_=150, till=160, limit=500) == expected

    url = url.with_query({"symbols": "ETHBTC,BTCUSD", "period": "1M",
                          "sort": "ASC", "from": "150", "till": "160",
                          "limit": "500", "offset": "100"})
    expected = Request(method="GET", url=url)
    assert creator.create_get_candles_request(
        symbols=["ETHBTC", "BTCUSD"], period="1M", sort="ASC",
        from_=150, till=160, limit=500, offset=100) == expected


def test_create_get_certain_candles_request(creator: HitbtcMarketDataRequestCreator) -> None:
    url = URL("https://api.hitbtc.com/api/2/public/candles/BTCUSD")
    expected = Request(
        method="GET", url=url)
    assert creator.create_get_certain_candles_request("BTCUSD") == expected

    expected = Request(method="GET", url=url)
    assert creator.create_get_certain_candles_request(
        symbol="BTCUSD") == expected

    url = url.with_query({"period": "1M"})
    expected = Request(method="GET", url=url)
    assert creator.create_get_certain_candles_request(
        symbol="BTCUSD", period="1M") == expected

    url = url.with_query({"period": "1M",
                          "sort": "ASC"})
    expected = Request(method="GET", url=url)
    assert creator.create_get_certain_candles_request(
        symbol="BTCUSD", period="1M", sort="ASC") == expected

    url = url.with_query({"period": "1M",
                          "sort": "ASC", "from": "150"})
    expected = Request(method="GET", url=url)
    assert creator.create_get_certain_candles_request(
        symbol="BTCUSD", period="1M", sort="ASC", from_=150) == expected

    url = url.with_query({"period": "1M",
                          "sort": "ASC", "from": "150", "till": "160"})
    expected = Request(method="GET", url=url)
    assert creator.create_get_certain_candles_request(
        symbol="BTCUSD", period="1M", sort="ASC", from_=150, till=160) == expected

    url = url.with_query({"period": "1M",
                          "sort": "ASC", "from": "150", "till": "160",
                          "limit": "500"})
    expected = Request(method="GET", url=url)
    assert creator.create_get_certain_candles_request(
        symbol="BTCUSD", period="1M", sort="ASC",
        from_=150, till=160, limit=500) == expected

    url = url.with_query({"period": "1M",
                          "sort": "ASC", "from": "150", "till": "160",
                          "limit": "500", "offset": "100"})
    expected = Request(method="GET", url=url)
    assert creator.create_get_certain_candles_request(
        symbol="BTCUSD", period="1M", sort="ASC",
        from_=150, till=160, limit=500, offset=100) == expected
