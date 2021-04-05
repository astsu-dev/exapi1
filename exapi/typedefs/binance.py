"""Has binance type definitions."""

from typing import List, Literal

OrderType = Literal[
    "LIMIT",
    "MARKET",
    "STOP_LOSS",
    "STOP_LOSS_LIMIT",
    "TAKE_PROFIT",
    "TAKE_PROFIT_LIMIT",
    "LIMIT_MAKER"
]
OrderTypes = List[OrderType]
OrderStatus = Literal[
    "NEW",
    "PARTIALLY_FILLED",
    "FILLED",
    "CANCELED",
    "PENDING_CANCEL",
    "REJECTED",
    "EXPIRED"
]
OrderSide = Literal["BUY", "SELL"]
OrderResponseType = Literal["ACK", "RESULT", "FULL"]
TimeInForce = Literal[
    "GTC",
    "IOC",
    "FOK"
]
CandleInterval = Literal[
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
SymbolPermission = Literal["SPOT", "MARGIN"]
SymbolPermissions = List[SymbolPermission]
SymbolStatus = Literal[
    "TRADING",
    "PRE_TRADING",
    "POST_TRADING",
    "END_OF_DAY",
    "HALT",
    "AUCTION_MATCH",
    "BREAK"
]
RateLimitInterval = Literal[
    "SECOND",
    "MINUTE",
    "DAY"
]
AccountType = Literal["SPOT"]
