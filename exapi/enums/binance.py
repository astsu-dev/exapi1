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


class BinanceErrorCode:
    """Binance error codes."""

    UNKNOWN: Final[Literal[-1000]] = -1000
    DISCONNECTED: Final[Literal[-1001]] = -1001
    UNAUTHORIZED: Final[Literal[-1002]] = -1002
    TOO_MANY_REQUESTS: Final[Literal[-1003]] = -1003
    SERVER_BUSY: Final[Literal[-1004]] = -1004
    UNEXPECTED_RESP: Final[Literal[-1006]] = -1006
    TIMEOUT: Final[Literal[-1007]] = -1007
    UNKNOWN_ORDER_COMPOSITION: Final[Literal[-1014]] = -1014
    TOO_MANY_ORDERS: Final[Literal[-1015]] = -1015
    SERVICE_SHUTTING_DOWN: Final[Literal[-1016]] = -1016
    UNSUPPORTED_OPERATION: Final[Literal[-1020]] = -1020
    INVALID_TIMESTAMP: Final[Literal[-1021]] = -1021
    INVALID_SIGNATURE: Final[Literal[-1022]] = -1022
    # TODO -1099
    # 11xx - 2xxx Request issues
    ILLEGAL_CHARS: Final[Literal[-1100]] = -1100
    TOO_MANY_PARAMETERS: Final[Literal[-1101]] = -1101
    MANDATORY_PARAM_EMPTY_OR_MALFORMED: Final[Literal[-1102]] = -1102
    UNKNOWN_PARAM: Final[Literal[-1103]] = -1103
    UNREAD_PARAMETERS: Final[Literal[-1104]] = -1104
    PARAM_EMPTY: Final[Literal[-1105]] = -1105
    PARAM_NOT_REQUIRED: Final[Literal[-1106]] = -1106
    BAD_PRECISION: Final[Literal[-1111]] = -1111
    NO_DEPTH: Final[Literal[-1112]] = -1112
    TIF_NOT_REQUIRED: Final[Literal[-1114]] = -1114
    INVALID_TIF: Final[Literal[-1115]] = -1115
    INVALID_ORDER_TYPE: Final[Literal[-1116]] = -1116
    INVALID_SIDE: Final[Literal[-1117]] = -1117
    EMPTY_NEW_CL_ORD_ID: Final[Literal[-1118]] = -1118
    EMPTY_ORG_CL_ORD_ID: Final[Literal[-1119]] = -1119
    BAD_CANDLE_INTERVAL: Final[Literal[-1120]] = -1120
    BAD_SYMBOL: Final[Literal[-1121]] = -1121
    INVALID_LISTEN_KEY: Final[Literal[-1125]] = -1125
    MORE_THAN_XX_HOURS: Final[Literal[-1127]] = -1127
    OPTIONAL_PARAMS_BAD_COMBO: Final[Literal[-1128]] = -1128
    INVALID_PARAMETER: Final[Literal[-1130]] = -1130
    BAD_RECV_WINDOW: Final[Literal[-1131]] = -1131
    NEW_ORDER_REJECTED: Final[Literal[-2010]] = -2010
    CANCEL_REJECTED: Final[Literal[-2011]] = -2011
    NO_SUCH_ORDER: Final[Literal[-2013]] = -2013
    BAD_API_KEY_FMT: Final[Literal[-2014]] = -2014
    REJECTED_MBX_KEY: Final[Literal[-2015]] = -2015
    NO_TRADING_WINDOW: Final[Literal[-2016]] = -2016
    # 3xxx - 5xxx SAPI-specific issues
    INNER_FAILURE: Final[Literal[-3000]] = -3000
    NEED_ENABLE_2FA: Final[Literal[-3001]] = -3001
    ASSET_DEFICIENCY: Final[Literal[-3002]] = -3002
    NO_OPENED_MARGIN_ACCOUNT: Final[Literal[-3003]] = -3003
    TRADE_NOT_ALLOWED: Final[Literal[-3004]] = -3004
    TRANSFER_OUT_NOT_ALLOWED: Final[Literal[-3005]] = -3005
    EXCEED_MAX_BORROWABLE: Final[Literal[-3006]] = -3006
    HAS_PENDING_TRANSACTION: Final[Literal[-3007]] = -3007
    BORROW_NOT_ALLOWED: Final[Literal[-3008]] = -3008
    VALIDATION_FAILED: Final[Literal[-3026]] = -3026
    LISTEN_KEY_NOT_FOUND: Final[Literal[-3038]] = -3038
    BALANCE_IS_NOT_ENOUGH: Final[Literal[-3041]] = -3041
    SYSTEM_BUSY: Final[Literal[-3044]] = -3044
