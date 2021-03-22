import hashlib
import hmac
from typing import Final

import pytest
from exapi.requesters.binance.auth import BinanceAuth, BinanceKeyAuth

API_KEY: Final[str] = "aaa"
API_SECRET: Final[str] = "bbb"


@pytest.fixture(scope="module")
def auth() -> BinanceAuth:
    key_auth = BinanceKeyAuth(API_KEY)
    return BinanceAuth(key_auth, API_SECRET)


def test_create_signature(auth: BinanceAuth) -> None:
    en = "utf-8"

    params = {"price": "10.5", "qty": "11.8"}
    key = API_SECRET.encode(en)
    msg = "price=10.5&qty=11.8".encode(en)
    signature = hmac.new(key, msg, hashlib.sha256).hexdigest()

    assert auth.create_signature(params) == signature


def test_sign(auth: BinanceAuth) -> None:
    en = "utf-8"

    params = {"price": "10.5", "qty": "11.8"}
    auth_res = auth.sign(params)

    assert auth_res.headers == {"X-MBX-APIKEY": "aaa"}

    key = API_SECRET.encode(en)
    msg = "price=10.5&qty=11.8".encode(en)
    signature = hmac.new(key, msg, hashlib.sha256).hexdigest()

    assert auth_res.params == {
        "price": "10.5",
        "qty": "11.8",
        "signature": signature
    }
