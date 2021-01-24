import pytest
from exapi.requesters.hitbtc.market_data.request_creator import \
    HitbtcMarketDataRequestCreator
from exapi.requesters.request import Request
from yarl import URL


@pytest.fixture(scope="module")
def creator() -> HitbtcMarketDataRequestCreator:
    return HitbtcMarketDataRequestCreator()


def test_create_get_currencies_request(creator: HitbtcMarketDataRequestCreator) -> None:
    url = URL("https://api.hitbtc.com/api/2/public/currency")
    expected = Request(
        method="GET",
        url=url)
    assert creator.create_get_currencies_request() == expected
    expected = Request(
        method="GET",
        url=url,
        params={"currencies": "BTC,ETH"})
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
    expected = Request(method="GET", url=url, params={
                       "symbols": "ETHBTC,BTCUSD"})
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
    expected = Request(method="GET", url=url, params={
                       "symbols": "ETHBTC,BTCUSD"})
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

    expected = Request(
        method="GET",
        url=url,
        params={"symbols": "ETHBTC,BTCUSD"})
    assert creator.create_get_trades_request(
        symbols=["ETHBTC", "BTCUSD"]) == expected

    expected = Request(
        method="GET",
        url=url,
        params={"symbols": "ETHBTC,BTCUSD",
                "sort": "ASC"})
    assert creator.create_get_trades_request(
        symbols=["ETHBTC", "BTCUSD"], sort="ASC") == expected

    expected = Request(
        method="GET",
        url=url,
        params={"symbols": "ETHBTC,BTCUSD",
                "sort": "ASC",
                "from": "150"})
    assert creator.create_get_trades_request(
        symbols=["ETHBTC", "BTCUSD"], sort="ASC", from_=150) == expected

    expected = Request(
        method="GET",
        url=url,
        params={"symbols": "ETHBTC,BTCUSD",
                "sort": "ASC",
                "from": "150",
                "till": "160"})
    assert creator.create_get_trades_request(
        symbols=["ETHBTC", "BTCUSD"], sort="ASC", from_=150, till=160) == expected

    expected = Request(
        method="GET",
        url=url,
        params={"symbols": "ETHBTC,BTCUSD",
                "sort": "ASC",
                "from": "150",
                "till": "160",
                "limit": "500"})
    assert creator.create_get_trades_request(
        symbols=["ETHBTC", "BTCUSD"], sort="ASC", from_=150, till=160, limit=500) == expected

    expected = Request(
        method="GET",
        url=url,
        params={"symbols": "ETHBTC,BTCUSD",
                "sort": "ASC",
                "from": "150",
                "till": "160",
                "limit": "500",
                "offset": "100"})
    assert creator.create_get_trades_request(
        symbols=["ETHBTC", "BTCUSD"], sort="ASC",
        from_=150, till=160, limit=500, offset=100) == expected


def test_create_get_certain_trades_request(creator: HitbtcMarketDataRequestCreator) -> None:
    url = URL("https://api.hitbtc.com/api/2/public/trades/BTCUSD")
    expected = Request(
        method="GET",
        url=url)
    assert creator.create_get_certain_trades_request("BTCUSD") == expected

    expected = Request(
        method="GET",
        url=url,
        params={"sort": "ASC"})
    assert creator.create_get_certain_trades_request(
        symbol="BTCUSD", sort="ASC") == expected

    expected = Request(
        method="GET",
        url=url,
        params={"sort": "ASC",
                "by": "timestamp"})
    assert creator.create_get_certain_trades_request(
        symbol="BTCUSD", sort="ASC", by="timestamp") == expected

    expected = Request(
        method="GET",
        url=url,
        params={"sort": "ASC",
                "by": "timestamp",
                "from": "150"})
    assert creator.create_get_certain_trades_request(
        symbol="BTCUSD", sort="ASC", by="timestamp", from_=150) == expected

    expected = Request(
        method="GET",
        url=url,
        params={"sort": "ASC",
                "by": "timestamp",
                "from": "150",
                "till": "160"})
    assert creator.create_get_certain_trades_request(
        symbol="BTCUSD", sort="ASC", by="timestamp", from_=150, till=160) == expected

    expected = Request(
        method="GET",
        url=url,
        params={"sort": "ASC",
                "by": "timestamp",
                "from": "150",
                "till": "160",
                "limit": "500"})
    assert creator.create_get_certain_trades_request(
        symbol="BTCUSD", sort="ASC", by="timestamp", from_=150, till=160, limit=500) == expected

    expected = Request(
        method="GET",
        url=url,
        params={"sort": "ASC",
                "by": "timestamp",
                "from": "150",
                "till": "160",
                "limit": "500",
                "offset": "100"})
    assert creator.create_get_certain_trades_request(
        symbol="BTCUSD", sort="ASC",
        by="timestamp", from_=150, till=160, limit=500, offset=100) == expected


def test_create_get_orderbooks_request(creator: HitbtcMarketDataRequestCreator) -> None:
    url = URL("https://api.hitbtc.com/api/2/public/orderbook")
    expected = Request(method="GET", url=url)
    assert creator.create_get_orderbooks_request() == expected

    expected = Request(
        method="GET",
        url=url,
        params={"symbols": "ETHBTC,BTCUSD"})
    assert creator.create_get_orderbooks_request(
        ["ETHBTC", "BTCUSD"]) == expected

    expected = Request(
        method="GET",
        url=url,
        params={"symbols": "ETHBTC,BTCUSD", "limit": "0"})
    assert creator.create_get_orderbooks_request(
        ["ETHBTC", "BTCUSD"], 0) == expected


def test_create_get_certain_orderbook_request(creator: HitbtcMarketDataRequestCreator) -> None:
    url = URL("https://api.hitbtc.com/api/2/public/orderbook/BTCUSD")
    expected = Request(
        method="GET",
        url=url)
    assert creator.create_get_certain_orderbook_request("BTCUSD") == expected

    expected = Request(
        method="GET",
        url=url,
        params={"limit": "0", "volume": "15"})
    assert creator.create_get_certain_orderbook_request(
        "BTCUSD", 0, 15) == expected

    expected = Request(
        method="GET",
        url=url,
        params={"limit": "0"})
    assert creator.create_get_certain_orderbook_request(
        "BTCUSD", 0) == expected


def test_create_get_candles_request(creator: HitbtcMarketDataRequestCreator) -> None:
    url = URL("https://api.hitbtc.com/api/2/public/candles")
    expected = Request(
        method="GET", url=url)
    assert creator.create_get_candles_request() == expected

    expected = Request(
        method="GET",
        url=url,
        params={"symbols": "ETHBTC,BTCUSD"})
    assert creator.create_get_candles_request(
        symbols=["ETHBTC", "BTCUSD"]) == expected

    expected = Request(
        method="GET",
        url=url,
        params={"symbols": "ETHBTC,BTCUSD",
                "period": "1M"})
    assert creator.create_get_candles_request(
        symbols=["ETHBTC", "BTCUSD"], period="1M") == expected

    expected = Request(
        method="GET",
        url=url,
        params={"symbols": "ETHBTC,BTCUSD",
                "period": "1M",
                "sort": "ASC"})
    assert creator.create_get_candles_request(
        symbols=["ETHBTC", "BTCUSD"], period="1M", sort="ASC") == expected

    expected = Request(
        method="GET",
        url=url,
        params={"symbols": "ETHBTC,BTCUSD",
                "period": "1M",
                "sort": "ASC",
                "from": "150"})
    assert creator.create_get_candles_request(
        symbols=["ETHBTC", "BTCUSD"], period="1M", sort="ASC", from_=150) == expected

    expected = Request(
        method="GET",
        url=url,
        params={"symbols": "ETHBTC,BTCUSD",
                "period": "1M",
                "sort": "ASC",
                "from": "150",
                "till": "160"})
    assert creator.create_get_candles_request(
        symbols=["ETHBTC", "BTCUSD"], period="1M", sort="ASC", from_=150, till=160) == expected

    expected = Request(
        method="GET",
        url=url,
        params={"symbols": "ETHBTC,BTCUSD",
                "period": "1M",
                "sort": "ASC",
                "from": "150",
                "till": "160",
                "limit": "500"})
    assert creator.create_get_candles_request(
        symbols=["ETHBTC", "BTCUSD"], period="1M", sort="ASC",
        from_=150, till=160, limit=500) == expected

    expected = Request(
        method="GET",
        url=url,
        params={"symbols": "ETHBTC,BTCUSD",
                "period": "1M",
                "sort": "ASC",
                "from": "150",
                "till": "160",
                "limit": "500",
                "offset": "100"})
    assert creator.create_get_candles_request(
        symbols=["ETHBTC", "BTCUSD"], period="1M", sort="ASC",
        from_=150, till=160, limit=500, offset=100) == expected


def test_create_get_certain_candles_request(creator: HitbtcMarketDataRequestCreator) -> None:
    url = URL("https://api.hitbtc.com/api/2/public/candles/BTCUSD")
    expected = Request(
        method="GET", url=url)
    assert creator.create_get_certain_candles_request("BTCUSD") == expected

    expected = Request(
        method="GET",
        url=url)
    assert creator.create_get_certain_candles_request(
        symbol="BTCUSD") == expected

    expected = Request(
        method="GET",
        url=url,
        params={"period": "1M"})
    assert creator.create_get_certain_candles_request(
        symbol="BTCUSD", period="1M") == expected

    expected = Request(
        method="GET",
        url=url,
        params={"period": "1M",
                "sort": "ASC"})
    assert creator.create_get_certain_candles_request(
        symbol="BTCUSD", period="1M", sort="ASC") == expected

    expected = Request(
        method="GET",
        url=url,
        params={"period": "1M",
                "sort": "ASC",
                "from": "150"})
    assert creator.create_get_certain_candles_request(
        symbol="BTCUSD", period="1M", sort="ASC", from_=150) == expected

    expected = Request(
        method="GET",
        url=url,
        params={"period": "1M",
                "sort": "ASC",
                "from": "150",
                "till": "160"})
    assert creator.create_get_certain_candles_request(
        symbol="BTCUSD", period="1M", sort="ASC", from_=150, till=160) == expected

    expected = Request(
        method="GET",
        url=url,
        params={"period": "1M",
                "sort": "ASC",
                "from": "150",
                "till": "160",
                "limit": "500"})
    assert creator.create_get_certain_candles_request(
        symbol="BTCUSD", period="1M", sort="ASC", from_=150, till=160, limit=500) == expected

    expected = Request(
        method="GET",
        url=url,
        params={"period": "1M",
                "sort": "ASC",
                "from": "150",
                "till": "160",
                "limit": "500",
                "offset": "100"})
    assert creator.create_get_certain_candles_request(
        symbol="BTCUSD", period="1M", sort="ASC",
        from_=150, till=160, limit=500, offset=100) == expected
