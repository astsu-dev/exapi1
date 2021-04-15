import pytest

from exapi.auth.binance import BinanceKeyAuth


@pytest.fixture(scope="module")
def auth() -> BinanceKeyAuth:
    return BinanceKeyAuth("aaa")


def test_sign(auth: BinanceKeyAuth) -> None:
    assert auth.sign() == {"X-MBX-APIKEY": "aaa"}
