from typing import Any
from unittest import mock

import pytest
from exapi.response_handlers.hitbtc.base import HitbtcBaseResponseHandler
from exapi.exceptions.hitbtc import HitbtcError
from exapi.models.hitbtc import HitbtcErrorModel


@pytest.fixture(scope="module")
def handler() -> HitbtcBaseResponseHandler:
    return HitbtcBaseResponseHandler()


def test__check_response(handler: HitbtcBaseResponseHandler) -> None:
    assert handler._check_response(mock.Mock()) is None


def test__check_json_response(handler: HitbtcBaseResponseHandler) -> None:
    raw: Any = {
        "error": {
            "code": 1000,
            "message": "test"
        }
    }
    with pytest.raises(HitbtcError):
        try:
            handler._check_json_response(raw)
        except HitbtcError as e:
            assert e.code == 1000
            assert e.error == HitbtcErrorModel(code=1000, message="test")
            raise

    raw = []
    assert handler._check_json_response(raw) is None
    raw = {}
    assert handler._check_json_response(raw) is None


@pytest.mark.asyncio
async def test_handle_response(handler: HitbtcBaseResponseHandler) -> None:
    res = mock.AsyncMock()

    expected: Any = {}
    res.json.return_value = expected
    assert await handler.handle_response(res) == expected

    res.json.return_value = {
        "error": {
            "code": 1000,
            "message": "test"
        }
    }
    with pytest.raises(HitbtcError):
        await handler.handle_response(res)
