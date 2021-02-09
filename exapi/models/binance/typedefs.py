from typing import Literal

SymbolStatus = Literal[
    "TRADING",
    "PRE_TRADING",
    "POST_TRADING",
    "END_OF_DAY",
    "HALT",
    "AUCTION_MATCH",
    "BREAK"
]
Interval = Literal[
    "1m",
    "3m",
    "5m",
    "15m",
    "30m",
    "1h",
    "2h",
    "4h",
    "6h",
    "8h",
    "12h",
    "1d",
    "3d",
    "1w",
    "1M"
]
