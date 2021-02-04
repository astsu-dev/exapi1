from typing import Union

import pytest
from exapi.models.hitbtc import (HitbtcErrorModel, HitbtcRawDetailedErrorModel,
                                 HitbtcRawErrorModel)
from exapi.models.hitbtc.mapper.base import HitbtcBaseModelsMapper


@pytest.fixture(scope="module")
def mapper() -> HitbtcBaseModelsMapper:
    return HitbtcBaseModelsMapper()


def test_map_to_error(mapper: HitbtcBaseModelsMapper) -> None:
    raw_error: Union[HitbtcRawErrorModel, HitbtcRawDetailedErrorModel]

    expected = HitbtcErrorModel(code=400, message="test")
    raw_error = {
        "code": 400,
        "message": "test"
    }
    assert mapper.map_to_error(raw_error) == expected

    expected = HitbtcErrorModel(code=400, message="test", description="test2")
    raw_error = {
        "code": 400,
        "message": "test",
        "description": "test2"
    }
    assert mapper.map_to_error(raw_error) == expected
