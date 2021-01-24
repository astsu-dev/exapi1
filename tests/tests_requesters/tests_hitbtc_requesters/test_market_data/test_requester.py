import pytest
from exapi.requesters.hitbtc.market_data import HitbtcMarketDataRequester


@pytest.fixture
def requester() -> HitbtcMarketDataRequester:
    return HitbtcMarketDataRequester()


@pytest.mark.asyncio
async def test_get_currencies(requester: HitbtcMarketDataRequester) -> None:
    req = requester
    async with req:
        res = await req.get_currencies()
        async with res:
            assert res.status == 200
            json = await res.json()
            assert set("id fullName crypto".split()).issubset(json[0].keys())
        res = await req.get_currencies(["BTC", "ETH"])
        async with res:
            assert res.status == 200
            json = await res.json()
            assert set("id fullName crypto".split()).issubset(json[0].keys())
            first_id = json[0]["id"]
            second_id = json[1]["id"]
            assert first_id == "BTC" or second_id == "BTC"
            assert first_id == "ETH" or second_id == "ETH"


@pytest.mark.asyncio
async def test_get_certain_currency(requester: HitbtcMarketDataRequester) -> None:
    req = requester
    async with req:
        res = await req.get_certain_currency("BTC")
        async with res:
            assert res.status == 200
            json = await res.json()
            assert set("id fullName crypto".split()).issubset(json.keys())
            assert json["id"] == "BTC"


@pytest.mark.asyncio
async def test_get_symbols(requester: HitbtcMarketDataRequester) -> None:
    req = requester
    async with req:
        res = await req.get_symbols()
        async with res:
            assert res.status == 200
            json = await res.json()
            assert set("id baseCurrency quoteCurrency".split()
                       ).issubset(json[0].keys())

        res = await req.get_symbols(["BTCUSD", "ETHUSD"])
        async with res:
            assert res.status == 200
            json = await res.json()
            assert set("id baseCurrency quoteCurrency".split()
                       ).issubset(json[0].keys())
            first_id = json[0]["id"]
            second_id = json[1]["id"]
            assert first_id == "BTCUSD" or second_id == "BTCUSD"
            assert first_id == "ETHUSD" or second_id == "ETHUSD"


@pytest.mark.asyncio
async def test_get_certain_symbol(requester: HitbtcMarketDataRequester) -> None:
    req = requester
    async with req:
        res = await req.get_certain_symbol("BTCUSD")
        async with res:
            assert res.status == 200
            json = await res.json()
            assert set("id baseCurrency quoteCurrency".split()
                       ).issubset(json.keys())
            assert json["id"] == "BTCUSD"


@pytest.mark.asyncio
async def test_get_tickers(requester: HitbtcMarketDataRequester) -> None:
    req = requester
    async with req:
        res = await req.get_tickers()
        async with res:
            assert res.status == 200
            json = await res.json()
            assert set("symbol ask bid".split()
                       ).issubset(json[0].keys())

        res = await req.get_tickers(["BTCUSD", "ETHUSD"])
        async with res:
            assert res.status == 200
            json = await res.json()
            assert set("symbol ask bid".split()
                       ).issubset(json[0].keys())
            assert json[0]["symbol"] == "ETHUSD"
            assert json[1]["symbol"] == "BTCUSD"


@pytest.mark.asyncio
async def test_get_certain_ticker(requester: HitbtcMarketDataRequester) -> None:
    req = requester
    async with req:
        res = await req.get_certain_ticker("BTCUSD")
        async with res:
            assert res.status == 200
            json = await res.json()
            assert set("symbol ask bid".split()
                       ).issubset(json.keys())
            assert json["symbol"] == "BTCUSD"


@pytest.mark.asyncio
async def test_get_trades(requester: HitbtcMarketDataRequester) -> None:
    req = requester
    async with req:
        res = await req.get_trades()
        async with res:
            assert res.status == 200
            json = await res.json()
            assert set("id price quantity side timestamp".split()
                       ).issubset(list(json.values())[0][0].keys())

        res = await req.get_trades(["BTCUSD", "ETHUSD"])
        async with res:
            assert res.status == 200
            json = await res.json()
            assert set("id price quantity side timestamp".split()
                       ).issubset(list(json.values())[0][0].keys())
            assert "BTCUSD" in json
            assert "ETHUSD" in json


@pytest.mark.asyncio
async def test_get_certain_trades(requester: HitbtcMarketDataRequester) -> None:
    req = requester
    async with req:
        res = await req.get_certain_trades("BTCUSD")
        async with res:
            assert res.status == 200
            json = await res.json()
            assert set("id price quantity side timestamp".split()
                       ).issubset(json[0].keys())


@pytest.mark.asyncio
async def test_get_orderbooks(requester: HitbtcMarketDataRequester) -> None:
    req = requester
    async with req:
        res = await req.get_orderbooks()
        async with res:
            assert res.status == 200
            json = await res.json()
            values = list(json.values())
            assert set("symbol bid ask timestamp".split()
                       ).issubset(values[0].keys())
            assert set("price size".split()).issubset(
                values[0]["ask"][0].keys())
            assert set("price size".split()).issubset(
                values[0]["bid"][0].keys())

        res = await req.get_orderbooks(["BTCUSD", "ETHUSD"])
        async with res:
            assert res.status == 200
            json = await res.json()
            values = list(json.values())
            assert set("symbol bid ask timestamp".split()
                       ).issubset(values[0].keys())
            assert set("price size".split()).issubset(
                values[0]["ask"][0].keys())
            assert set("price size".split()).issubset(
                values[0]["bid"][0].keys())
            first_symbol = values[0]["symbol"]
            second_symbol = values[1]["symbol"]
            assert first_symbol == "BTCUSD" or second_symbol == "BTCUSD"
            assert first_symbol == "ETHUSD" or second_symbol == "ETHUSD"


@pytest.mark.asyncio
async def test_get_certain_orderbook(requester: HitbtcMarketDataRequester) -> None:
    req = requester
    async with req:
        res = await req.get_certain_orderbook("BTCUSD")
        async with res:
            assert res.status == 200
            json = await res.json()
            assert set("symbol bid ask timestamp".split()
                       ).issubset(json.keys())
            assert set("price size".split()).issubset(json["ask"][0].keys())
            assert set("price size".split()).issubset(json["bid"][0].keys())


@pytest.mark.asyncio
async def test_get_candles(requester: HitbtcMarketDataRequester) -> None:
    req = requester
    async with req:
        res = await req.get_candles()
        async with res:
            assert res.status == 200
            json = await res.json()
            assert set("timestamp open close min max volume volumeQuote".split()
                       ).issubset(list(json.values())[0][0].keys())

        res = await req.get_candles(["BTCUSD", "ETHUSD"])
        async with res:
            assert res.status == 200
            json = await res.json()
            assert set("timestamp open close min max volume volumeQuote".split()
                       ).issubset(list(json.values())[0][0].keys())
            assert "BTCUSD" in json
            assert "ETHUSD" in json


@pytest.mark.asyncio
async def test_get_certain_candles(requester: HitbtcMarketDataRequester) -> None:
    req = requester
    async with req:
        res = await req.get_certain_candles("BTCUSD")
        async with res:
            assert res.status == 200
            json = await res.json()
            assert set("timestamp open close min max volume volumeQuote".split()
                       ).issubset(json[0].keys())
