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
