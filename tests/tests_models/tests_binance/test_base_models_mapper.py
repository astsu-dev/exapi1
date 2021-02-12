import pytest
from exapi.models.binance import BinanceErrorJson, BinanceErrorModel
from exapi.models.binance.mapper import BinanceBaseModelsMapper


@pytest.fixture(scope="module")
def mapper() -> BinanceBaseModelsMapper:
    return BinanceBaseModelsMapper()


def test_map_to_error(mapper: BinanceBaseModelsMapper) -> None:
    expected = BinanceErrorModel(code=-1001, msg="Not enough money.")
    json: BinanceErrorJson = {
        "code": -1001,
        "msg": "Not enough money."
    }
    assert mapper.map_to_error(json) == expected
