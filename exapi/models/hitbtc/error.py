"""Has hitbtc error model."""

from dataclasses import dataclass
from typing import Optional, TypedDict


class HitbtcRawErrorModel(TypedDict):
    """Hitbtc json error model."""

    code: int
    message: str


class HitbtcRawDetailedErrorModel(HitbtcRawErrorModel):
    """Hitbtc detailed json error model.

    Has additional description field.
    """

    description: str


@dataclass(frozen=True)
class HitbtcErrorModel:
    """Hitbtc error model.

    Args:
        code: error code enum.
        message: error message.
        description: description to error.
    """

    code: int
    message: str
    description: Optional[str] = None
