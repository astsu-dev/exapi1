import pytest
from exapi.requesters.binance.base.request_creator import \
    BinanceBaseRequestCreator


@pytest.fixture(scope="module")
def creator() -> BinanceBaseRequestCreator:
    return BinanceBaseRequestCreator()


def test_public_fields(creator: BinanceBaseRequestCreator) -> None:
    assert creator.ROOT_URI == "https://api.binance.com"
    assert creator.ROOT_URL == "https://api.binance.com/api/v3"


def test__create_url(creator: BinanceBaseRequestCreator) -> None:
    assert creator._create_url(
        "/ping") == "https://api.binance.com/api/v3/ping"
