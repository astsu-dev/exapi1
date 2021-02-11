"""Has binance exchange filters."""

from dataclasses import dataclass
from typing import List, Literal, TypedDict, Union


class BinanceMaxNumOrdersExchangeFilterJson(TypedDict):
    filterType: Literal["EXCHANGE_MAX_NUM_ORDERS"]
    maxNumOrders: int


@dataclass(frozen=True)
class BinanceMaxNumOrdersExchangeFilterModel:
    """The EXCHANGE_MAX_NUM_ORDERS filter defines the maximum number of orders
    an account is allowed to have open on the exchange.
    Note that both "algo" orders and normal orders are counted for this filter.

    Args:
        filter_type (Literal["EXCHANGE_MAX_NUM_ORDERS"])
        max_num_orders (int)
    """

    filter_type: Literal["EXCHANGE_MAX_NUM_ORDERS"]
    max_num_orders: int


class BinanceMaxNumAlgoOrdersExchangeFilterJson(TypedDict):
    filterType: Literal["EXCHANGE_MAX_ALGO_ORDERS"]
    maxNumAlgoOrders: int


@dataclass(frozen=True)
class BinanceMaxNumAlgoOrdersExchangeFilterModel:
    """The EXCHANGE_MAX_ALGO_ORDERS filter defines the maximum number
    of "algo" orders an account is allowed to have open on the exchange.
    "Algo" orders are STOP_LOSS, STOP_LOSS_LIMIT, TAKE_PROFIT,
    and TAKE_PROFIT_LIMIT orders.

    Args:
        filter_type (Literal["EXCHANGE_MAX_ALGO_ORDERS"])
        max_num_algo_orders (int)
    """

    filter_type: Literal["EXCHANGE_MAX_ALGO_ORDERS"]
    max_num_algo_orders: int


BinanceExchangeFilterJson = Union[
    BinanceMaxNumOrdersExchangeFilterJson,
    BinanceMaxNumAlgoOrdersExchangeFilterJson]
BinanceExchangeFiltersJson = List[BinanceExchangeFilterJson]
BinanceExchangeFilterModel = Union[
    BinanceMaxNumOrdersExchangeFilterModel,
    BinanceMaxNumAlgoOrdersExchangeFilterModel]
BinanceExchangeFilters = List[BinanceExchangeFilterModel]
