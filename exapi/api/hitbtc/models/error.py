"""Has hitbtc error model."""

from dataclasses import dataclass
from typing import Optional

from exapi.api.hitbtc.error_code import HitbtcErrorCode


@dataclass(frozen=True)
class HitbtcErrorModel:
    """Hitbtc error model.

    Args:
        code: error code enum.
        message: error message.
        description: description to error.
    """

    code: HitbtcErrorCode
    message: str
    description: Optional[str] = None
