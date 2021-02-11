"""Has binance enums."""

from typing import Final, Literal


class BinanceOrderType:
    """Binance order types."""

    LIMIT: Final[Literal["LIMIT"]] = "LIMIT"
    MARKET: Final[Literal["MARKET"]] = "MARKET"
    STOP_LOSS: Final[Literal["STOP_LOSS"]] = "STOP_LOSS"
    STOP_LOSS_LIMIT: Final[Literal["STOP_LOSS_LIMIT"]] = "STOP_LOSS_LIMIT"
    TAKE_PROFIT: Final[Literal["TAKE_PROFIT"]] = "TAKE_PROFIT"
    TAKE_PROFIT_LIMIT: Final[Literal["TAKE_PROFIT_LIMIT"]
                             ] = "TAKE_PROFIT_LIMIT"
    LIMIT_MAKER: Final[Literal["LIMIT_MAKER"]] = "LIMIT_MAKER"


class BinanceOrderStatus:
    """Binance order statuses."""

    NEW: Final[Literal["NEW"]] = "NEW"
    PARTIALLY_FILLED: Final[Literal["PARTIALLY_FILLED"]] = "PARTIALLY_FILLED"
    FILLED: Final[Literal["FILLED"]] = "FILLED"
    CANCELED: Final[Literal["CANCELED"]] = "CANCELED"
    PENDING_CANCEL: Final[Literal["PENDING_CANCEL"]] = "PENDING_CANCEL"
    REJECTED: Final[Literal["REJECTED"]] = "REJECTED"
    EXPIRED: Final[Literal["EXPIRED"]] = "EXPIRED"


class BinanceOrderSide:
    """Binance order sides."""

    BUY: Final[Literal["BUY"]] = "BUY"
    SELL: Final[Literal["SELL"]] = "SELL"


class BinanceTimeInForce:
    """Binance time in force."""

    GTC: Final[Literal["GTC"]] = "GTC"
    IOC: Final[Literal["IOC"]] = "IOC"
    FOK: Final[Literal["FOK"]] = "FOK"


class BinanceSymbolPermission:
    """Binance symbol permissions."""

    SPOT: Final[Literal["SPOT"]] = "SPOT"
    MARGIN: Final[Literal["MARGIN"]] = "MARGIN"


class BinanceSymbolStatus:
    """Binance symbol statuses."""

    TRADING: Final[Literal["TRADING"]] = "TRADING"
    PRE_TRADING: Final[Literal["PRE_TRADING"]] = "PRE_TRADING"
    POST_TRADING: Final[Literal["POST_TRADING"]] = "POST_TRADING"
    END_OF_DAY: Final[Literal["END_OF_DAY"]] = "END_OF_DAY"
    HALT: Final[Literal["HALT"]] = "HALT"
    AUCTION_MATCH: Final[Literal["AUCTION_MATCH"]] = "AUCTION_MATCH"
    BREAK: Final[Literal["BREAK"]] = "BREAK"


class BinanceRateLimitInterval:
    """Binance rate limit intervals."""

    SECOND: Final[Literal["SECOND"]] = "SECOND"
    MINUTE: Final[Literal["MINUTE"]] = "MINUTE"
    DAY: Final[Literal["DAY"]] = "DAY"


class BinanceRateLimitType:
    """Binance rate limit types."""

    REQUEST_WEIGHT: Final[Literal["REQUEST_WEIGHT"]] = "REQUEST_WEIGHT"
    ORDERS: Final[Literal["ORDERS"]] = "ORDERS"
    RAW_REQUESTS: Final[Literal["RAW_REQUESTS"]] = "RAW_REQUESTS"


class BinanceSymbolFilterType:
    """Binance symbol filter types."""

    PRICE: Final[Literal["PRICE_FILTER"]] = "PRICE_FILTER"
    PERCENT_PRICE: Final[Literal["PERCENT_PRICE"]] = "PERCENT_PRICE"
    LOT_SIZE: Final[Literal["LOT_SIZE"]] = "LOT_SIZE"
    MIN_NOTIONAL: Final[Literal["MIN_NOTIONAL"]] = "MIN_NOTIONAL"
    ICEBERG_PARTS: Final[Literal["ICEBERG_PARTS"]] = "ICEBERG_PARTS"
    MARKET_LOT_SIZE: Final[Literal["MARKET_LOT_SIZE"]] = "MARKET_LOT_SIZE"
    MAX_NUM_ORDERS: Final[Literal["MAX_NUM_ORDERS"]] = "MAX_NUM_ORDERS"
    MAX_NUM_ALGO_ORDERS: Final[Literal["MAX_NUM_ALGO_ORDERS"]
                               ] = "MAX_NUM_ALGO_ORDERS"
    MAX_NUM_ICEBERG_ORDERS: Final[Literal["MAX_NUM_ICEBERG_ORDERS"]
                                  ] = "MAX_NUM_ICEBERG_ORDERS"
    MAX_POSITION: Final[Literal["MAX_POSITION"]] = "MAX_POSITION"


class BinanceExchangeFilterType:
    """Binance exchange filter types."""

    MAX_NUM_ORDERS: Final[Literal["EXCHANGE_MAX_NUM_ORDERS"]
                          ] = "EXCHANGE_MAX_NUM_ORDERS"
    MAX_NUM_ALGO_ORDERS: Final[Literal["EXCHANGE_MAX_ALGO_ORDERS"]
                               ] = "EXCHANGE_MAX_ALGO_ORDERS"


class BinanceAccountType:
    """Binance account types."""

    SPOT: Final[Literal["SPOT"]] = "SPOT"
