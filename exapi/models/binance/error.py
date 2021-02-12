from dataclasses import dataclass
from typing import TypedDict


class BinanceErrorJson(TypedDict):
    code: int
    msg: str


@dataclass(frozen=True)
class BinanceErrorModel:
    """Binance error model.

    Args:
        code (int)
        msg (int): human readable message.
    """

    code: int
    msg: str
