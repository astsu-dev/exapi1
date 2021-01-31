"""Has hitbtc error model."""

from dataclasses import dataclass
from typing import Optional


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
