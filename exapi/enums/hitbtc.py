"""Has hitbtc enums."""

from typing import Final, Literal


class HitbtcSortDirection:
    """Hitbtc sort direction enum."""

    ASC: Final[Literal["ASC"]] = "ASC"
    DESC: Final[Literal["DESC"]] = "DESC"


class HitbtcSortBy:
    """Hitbtc sort by enum."""

    ID: Final[Literal["id"]] = "id"
    TIMESTAMP: Final[Literal["timestamp"]] = "timestamp"


class HitbtcCandlesPeriod:
    """Hitbtc candles period enum.

    M - minutes
    H - hours
    D - days
    m - months
    """

    M1: Final[Literal["M1"]] = "M1"
    M3: Final[Literal["M3"]] = "M3"
    M5: Final[Literal["M5"]] = "M5"
    M15: Final[Literal["M15"]] = "M15"
    M30: Final[Literal["M30"]] = "M30"
    H1: Final[Literal["H1"]] = "H1"
    H4: Final[Literal["H4"]] = "H4"
    D1: Final[Literal["D1"]] = "D1"
    D7: Final[Literal["D7"]] = "D7"
    m1: Final[Literal["1M"]] = "1M"


class HitbtcOrderSide:
    """Hitbtc order side enum."""

    BUY: Final[Literal["buy"]] = "buy"
    SELL: Final[Literal["sell"]] = "sell"


class HitbtcOrderType:
    """Hitbtc order type enum."""

    LIMIT: Final[Literal["limit"]] = "limit"
    MARKET: Final[Literal["market"]] = "market"
    STOP_LIMIT: Final[Literal["stopLimit"]] = "stopLimit"
    STOP_MARKET: Final[Literal["stopMarket"]] = "stopMarket"


class HitbtcTimeInForce:
    """Hitbtc time in force enum."""

    GTC: Final[Literal["GTC"]] = "GTC"
    IOC: Final[Literal["IOC"]] = "IOC"
    FOK: Final[Literal["FOK"]] = "FOK"
    DAY: Final[Literal["Day"]] = "Day"
    GTD: Final[Literal["GTD"]] = "GTD"


class HitbtcOrderStatus:
    """Hitbtc order status enum."""

    NEW: Final[Literal["new"]] = "new"
    SUSPENDED: Final[Literal["suspended"]] = "suspended"
    PARTIALLY_FILLED: Final[Literal["partiallyFilled"]] = "partiallyFilled"
    FILLED: Final[Literal["filled"]] = "filled"
    CANCELED: Final[Literal["canceled"]] = "canceled"
    EXPIRED: Final[Literal["expired"]] = "expired"


class HitbtcErrorCode:
    """Hitbtc error code enum."""

    ACTION_IS_FORBIDDEN = 403
    TOO_MANY_REQUESTS = 429
    INTERNAL_SERVER_ERROR = 500
    SERVICE_UNAVAILABLE = 503
    GATEAWAY_TIMEOUT = 504
    AUTHORIZATION_REQUIRED = 1001
    NOT_ALLOWED_PERMISSIONS = 1003
    UNSUPPORTED_AUTHORIZATION_METHOD = 1004
    SYMBOL_NOT_FOUND = 2001
    CURRENCY_NOT_FOUND = 2002
    QUANTITY_NOT_A_VALID_NUMBER = 2010
    QUANTITY_TOO_LOW = 2011
    BAD_QUANTITY = 2012
    PRICE_NOT_A_VALID_NUMBER = 2020
    PRICE_TOO_LOW = 2021
    BAD_PRICE = 2022
    INSUFFICIENT_FUNDS = 20001
    ORDER_NOT_FOUND = 20002
    WITHDRAW_LIMIT_EXCEEDED = 20003
    TRANSACTION_NOT_FOUND = 20004
    PAYOUT_NOT_FOUND = 20005
    PAYOUT_ALREADY_COMMITTED = 20006
    PAYOUT_ALREADY_ROLLED_BACK = 20007
    DUPLICATE_CLIENT_ORDER_ID = 20008
    PRICE_AND_QUANTITY_NOT_CHANGED = 20009
    MARKET_TEMPORARY_CLOSED = 20010
    INVALID_PAYOUT_ADDRESS = 20011
    PAYOUT_UNAVAILABLE_OFFCHAIN = 20014
    MARGIN_ACCOUNT_OR_POSITION_NOT_FOUND = 20032
    POSITION_NOT_CHANGED = 20033
    POSITION_IN_CLOSE_ONLY_STATE = 20034
    MARGIN_TRADING_FORBIDDEN = 20040
    INTERNAL_ORDER_EXECUTION_DEADLINE_EXCEEDED = 20080
    VALIDATION_ERROR = 10001
    USER_DISABLED = 10021
