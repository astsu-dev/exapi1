from typing import Any
from unittest import mock

import pytest
from exapi.response_handlers.binance.base import BinanceBaseResponseHandler
from exapi.api.binance.exceptions import BinanceError
from exapi.models.binance.error import BinanceErrorModel


@pytest.fixture(scope="module")
def handler() -> BinanceBaseResponseHandler:
    return BinanceBaseResponseHandler()


def test__check_response(handler: BinanceBaseResponseHandler) -> None:
    assert handler._check_response(mock.Mock()) is None


def test__check_json_response(handler: BinanceBaseResponseHandler) -> None:
    res: Any = {}
    assert handler._check_json_response(res) is None
    res = []
    assert handler._check_json_response(res) is None
    res = {"code": 100}
    assert handler._check_json_response(res) is None
    res = {"msg": "sdf"}
    assert handler._check_json_response(res) is None

    res = {
        "code": 100,
        "msg": "sdf"
    }
    with pytest.raises(BinanceError):
        try:
            handler._check_json_response(res)
        except BinanceError as e:
            assert e.code == 100
            assert e.error == BinanceErrorModel(code=100, msg="sdf")
            raise


@pytest.mark.asyncio
async def test_handle_response(handler: BinanceBaseResponseHandler) -> None:
    res = mock.AsyncMock()

    expected: Any = {}
    res.json.return_value = expected
    assert await handler.handle_response(res) == expected

    res.json.return_value = {
        "code": 100,
        "msg": "sdf"
    }
    with pytest.raises(BinanceError):
        await handler.handle_response(res)
