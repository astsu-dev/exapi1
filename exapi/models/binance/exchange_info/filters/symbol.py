"""Has binance symbol filters."""

from dataclasses import dataclass
from decimal import Decimal
from typing import List, Literal, TypedDict, Union


class BinancePriceSymbolFilterJson(TypedDict):
    filterType: Literal["PRICE_FILTER"]
    minPrice: str
    maxPrice: str
    tickSize: str


@dataclass(frozen=True)
class BinancePriceSymbolFilterModel:
    """The PRICE_FILTER defines the price rules for a symbol.

    There are 3 parts:
        - minPrice defines the minimum price/stopPrice allowed; disabled on minPrice == 0.
        - maxPrice defines the maximum price/stopPrice allowed; disabled on maxPrice == 0.
        - tickSize defines the intervals that a price/stopPrice can be increased/decreased by;
            disabled on tickSize == 0.

    Any of the above variables can be set to 0, which disables that rule in the price filter.
    In order to pass the price filter, the following must be true
    for price/stopPrice of the enabled rules:
        - price >= minPrice
        - price <= maxPrice
        - (price-minPrice) % tickSize == 0
    """

    filter_type: Literal["PRICE_FILTER"]
    min_price: Decimal
    max_price: Decimal
    tick_size: Decimal


class BinancePercentPriceSymbolFilterJson(TypedDict):
    filterType: Literal["PERCENT_PRICE"]
    multiplierUp: str
    multiplierDown: str
    avgPriceMins: int


@dataclass(frozen=True)
class BinancePercentPriceSymbolFilterModel:
    """The PERCENT_PRICE filter defines valid range
    for a price based on the average of the previous trades.
    `avg_price_mins` is the number of minutes the average price
    is calculated over. 0 means the last price is used.

    In order to pass the percent price, the following must be true for price:
        - price <= weightedAveragePrice * `multiplier_up`
        - price >= weightedAveragePrice * `multiplier_down`

    Args:
        filter_type (Literal["PERCENT_PRICE"])
        multiplier_up (Decimal)
        multiplier_down (Decimal)
        avg_price_mins (int)
    """

    filter_type: Literal["PERCENT_PRICE"]
    multiplier_up: Decimal
    multiplier_down: Decimal
    avg_price_mins: int


class BinanceLotSizeSymbolFilterJson(TypedDict):
    filterType: Literal["LOT_SIZE"]
    minQty: str
    maxQty: str
    stepSize: str


@dataclass(frozen=True)
class BinanceLotSizeSymbolFilterModel:
    """The LOT_SIZE filter defines the quantity
    (aka "lots" in auction terms) rules for a symbol.

    There are 3 parts:
        - minQty defines the minimum quantity/icebergQty allowed.
        - maxQty defines the maximum quantity/icebergQty allowed.
        - stepSize defines the intervals that a quantity/icebergQty
            can be increased/decreased by.

    In order to pass the lot size, the following must be true for quantity/icebergQty:
        - quantity >= minQty
        - quantity <= maxQty
        - (quantity-minQty) % stepSize == 0

    Args:
        filter_type (Literal["LOT_SIZE"])
        min_qty (Decimal)
        max_qty (Decimal)
        step_size (Decimal)
    """

    filter_type: Literal["LOT_SIZE"]
    min_qty: Decimal
    max_qty: Decimal
    step_size: Decimal


class BinanceMinNotionalSymbolFilterJson(TypedDict):
    filterType: Literal["MIN_NOTIONAL"]
    minNotional: str
    applyToMarket: bool
    avgPriceMins: int


@dataclass(frozen=True)
class BinanceMinNotionalSymbolFilterModel:
    """The MIN_NOTIONAL filter defines the minimum notional value allowed
    for an order on a symbol. An order's notional value
    is the price * quantity. If the order is an Algo order (e.g. STOP_LOSS_LIMIT),
    then the notional value of the stopPrice * quantity will also be evaluated.
    If the order is an Iceberg Order, then the notional value
    of the price * icebergQty will also be evaluated.
    `apply_to_market` determines whether or not the MIN_NOTIONAL filter will also be
    applied to MARKET orders. Since MARKET orders have no price,
    the average price is used over the last `avg_price_mins` minutes.
    `avg_price_mins` is the number of minutes the average price is calculated over.
    0 means the last price is used.

    Args:
        filter_type (Literal["MIN_NOTIONAL"])
        min_notional (str)
        apply_to_market (bool)
        avg_price_mins (int)
    """

    filter_type: Literal["MIN_NOTIONAL"]
    min_notional: Decimal
    apply_to_market: bool
    avg_price_mins: int


class BinanceIcebergPartsSymbolFilterJson(TypedDict):
    filterType: Literal["ICEBERG_PARTS"]
    limit: int


@dataclass(frozen=True)
class BinanceIcebergPartsSymbolFilterModel:
    """The ICEBERG_PARTS filter defines the maximum parts an iceberg order can have.
    The number of ICEBERG_PARTS is defined as CEIL(qty / icebergQty).

    Args:
        filter_type (Literal["ICEBERG_PARTS"])
        limit (int)
    """

    filter_type: Literal["ICEBERG_PARTS"]
    limit: int


class BinanceMarketLotSizeSymbolFilterJson(TypedDict):
    filterType: Literal["MARKET_LOT_SIZE"]
    minQty: str
    maxQty: str
    stepSize: str


@dataclass(frozen=True)
class BinanceMarketLotSizeSymbolFilterModel:
    """The MARKET_LOT_SIZE filter defines the quantity (aka "lots" in auction terms)
    rules for MARKET orders on a symbol.

    There are 3 parts:

        - minQty defines the minimum quantity allowed.
        - maxQty defines the maximum quantity allowed.
        - stepSize defines the intervals that a quantity can be increased/decreased by.

    In order to pass the market lot size, the following must be true for quantity:
        - quantity >= minQty
        - quantity <= maxQty
        - (quantity-minQty) % stepSize == 0

    Args:
        filter_type (Literal["MARKET_LOT_SIZE"])
        min_qty (Decimal)
        max_qty (Decimal)
        step_size (Decimal)
    """

    filter_type: Literal["MARKET_LOT_SIZE"]
    min_qty: Decimal
    max_qty: Decimal
    step_size: Decimal


class BinanceMaxNumOrdersSymbolFilterJson(TypedDict):
    filterType: Literal["MAX_NUM_ORDERS"]
    maxNumOrders: int


@dataclass(frozen=True)
class BinanceMaxNumOrdersSymbolFilterModel:
    """The MAX_NUM_ORDERS filter defines the maximum number of orders an account
    is allowed to have open on a symbol.
    Note that both "algo" orders and normal orders are counted for this filter.

    Args:
        filter_type (Literal["MAX_NUM_ORDERS"])
        max_num_orders (int)
    """

    filter_type: Literal["MAX_NUM_ORDERS"]
    max_num_orders: int


class BinanceMaxNumAlgoOrdersSymbolFilterJson(TypedDict):
    filterType: Literal["MAX_NUM_ALGO_ORDERS"]
    maxNumAlgoOrders: int


@dataclass(frozen=True)
class BinanceMaxNumAlgoOrdersSymbolFilterModel:
    """The MAX_NUM_ALGO_ORDERS filter defines the maximum number of "algo"
    orders an account is allowed to have open on a symbol.
    "Algo" orders are STOP_LOSS, STOP_LOSS_LIMIT, TAKE_PROFIT,
    and TAKE_PROFIT_LIMIT orders.

    Args:
        filter_type (Literal["MAX_NUM_ALGO_ORDERS"])
        max_num_algo_orders (int)
    """

    filter_type: Literal["MAX_NUM_ALGO_ORDERS"]
    max_num_algo_orders: int


class BinanceMaxNumIcebergOrdersSymbolFilterJson(TypedDict):
    filterType: Literal["MAX_NUM_ICEBERG_ORDERS"]
    maxNumIcebergOrders: int


@dataclass(frozen=True)
class BinanceMaxNumIcebergOrdersSymbolFilterModel:
    """The MAX_NUM_ICEBERG_ORDERS filter defines the maximum number
    of ICEBERG orders an account is allowed to have open on a symbol.
    An ICEBERG order is any order where the icebergQty is > 0.

    Args:
        filter_type (Literal["MAX_NUM_ICEBERG_ORDERS"])
        max_num_iceberg_orders (int)
    """

    filter_type: Literal["MAX_NUM_ICEBERG_ORDERS"]
    max_num_iceberg_orders: int


class BinanceMaxPositionSymbolFilterJson(TypedDict):
    filterType: Literal["MAX_POSITION"]
    maxPosition: str


@dataclass(frozen=True)
class BinanceMaxPositionSymbolFilterModel:
    """The MAX_POSITION filter defines the allowed maximum position an account
    can have on the base asset of a symbol. An account's position defined
    as the sum of the account's:
        - free balance of the base asset
        - locked balance of the base asset
        - sum of the qty of all open BUY orders

    BUY orders will be rejected if the account's position is greater
    than the maximum position allowed.

    Args:
        filter_type (Literal["MAX_POSITION"])
        max_position (Decimal)
    """

    filter_type: Literal["MAX_POSITION"]
    max_position: Decimal


BinanceSymbolFilterJson = Union[
    BinancePriceSymbolFilterJson,
    BinancePercentPriceSymbolFilterJson,
    BinanceLotSizeSymbolFilterJson,
    BinanceMinNotionalSymbolFilterJson,
    BinanceIcebergPartsSymbolFilterJson,
    BinanceMarketLotSizeSymbolFilterJson,
    BinanceMaxNumOrdersSymbolFilterJson,
    BinanceMaxNumAlgoOrdersSymbolFilterJson,
    BinanceMaxNumIcebergOrdersSymbolFilterJson,
    BinanceMaxPositionSymbolFilterJson]
BinanceSymbolFiltersJson = List[BinanceSymbolFilterJson]
BinanceSymbolFilterModel = Union[
    BinancePriceSymbolFilterModel,
    BinancePercentPriceSymbolFilterModel,
    BinanceLotSizeSymbolFilterModel,
    BinanceMinNotionalSymbolFilterModel,
    BinanceIcebergPartsSymbolFilterModel,
    BinanceMarketLotSizeSymbolFilterModel,
    BinanceMaxNumOrdersSymbolFilterModel,
    BinanceMaxNumAlgoOrdersSymbolFilterModel,
    BinanceMaxNumIcebergOrdersSymbolFilterModel,
    BinanceMaxPositionSymbolFilterModel]
BinanceSymbolFilters = List[BinanceSymbolFilterModel]
